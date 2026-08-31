# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2304bad9-4e57-3633-968d-433deb4af65f | -15.9068 | -56.230701 | 2026-08-31 00:35:00 | METOP-C | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 88355fc3-f13b-31b6-842c-99c62027eed3 | -11.928 | -45.068901 | 2026-08-31 00:35:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f0f053cb-c28d-37ca-9f77-9f1c2ded9228 | -10.7567 | -44.869202 | 2026-08-31 00:35:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 140590d1-ae27-3edc-8b6a-6b145ac48f5f | -11.2227 | -45.143101 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3b1155e4-cf03-3bb7-8f7d-e79599b1812f | -11.0735 | -51.521999 | 2026-08-31 00:35:00 | METOP-C | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aa022bea-fe3c-30db-92a3-bcd3742c16ae | -19.145399 | -57.393398 | 2026-08-31 00:35:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 66b499c2-f19d-3ea1-9ebb-1da780bda2a5 | -11.2243 | -45.150299 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6b2f3ca8-8de6-354c-a10f-2578447b15d3 | -12.9545 | -45.951698 | 2026-08-31 00:35:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1bfbf7fe-2a4f-3611-a448-2aa2b842e342 | -1.5994 | -54.404202 | 2026-08-31 00:35:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f8bfc78-5764-3f01-a815-1e1d3afb7b65 | -11.2149 | -45.3335 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1203dfbf-4089-340c-8101-9b0624dc7955 | -12.8998 | -45.8466 | 2026-08-31 00:35:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 73003523-28a4-3d0c-8a32-25759ce69342 | -7.7715 | -44.069099 | 2026-08-31 00:35:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1445ab4f-f612-3ec6-93e3-b975e4d2c2d2 | -14.6045 | -54.096199 | 2026-08-31 00:35:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2a44bd82-9ea1-3325-9855-88be355b4573 | -14.1704 | -52.890499 | 2026-08-31 00:35:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 36f34bf1-6178-3cd2-bd2f-2063681b2439 | -4.8428 | -55.839298 | 2026-08-31 00:35:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8127d187-16b2-33ec-94fa-b89bd977e24d | -10.5494 | -46.212101 | 2026-08-31 00:35:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 68284c73-6579-3023-94af-64fbbf91383a | -14.4247 | -52.531799 | 2026-08-31 00:35:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1347848e-24a0-352b-9425-218d58471660 | -10.7995 | -50.660801 | 2026-08-31 00:35:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9b9b2d06-db45-3a92-bdd5-328967197a01 | -12.1158 | -45.032501 | 2026-08-31 00:35:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9307be9d-711a-3e36-a78a-b5a2902886f0 | -3.5408 | -49.483501 | 2026-08-31 00:35:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1553340-0632-3e6a-9fb5-d6363f6e28f8 | -11.0713 | -51.511501 | 2026-08-31 00:35:00 | METOP-C | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6f74045d-97c5-3e5e-b339-3b33f59ceeed | -14.3911 | -52.567299 | 2026-08-31 00:35:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7bccd649-96b6-3268-a1ae-4b151aa1f5e8 | -14.5917 | -54.135399 | 2026-08-31 00:35:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7ae3b9d4-b4ab-330d-b3b6-be27fe7f56ac | -11.2323 | -45.095299 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8af8d90d-679e-34ec-93fc-c126a81b9af4 | -5.7378 | -49.131199 | 2026-08-31 00:35:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ecb33b5-c8c0-37f4-8783-cfc21d63900c | -4.0606 | -48.958401 | 2026-08-31 00:35:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 152745c7-7e17-3efd-b201-920f46423bcf | -12.3961 | -46.4473 | 2026-08-31 00:35:00 | METOP-C | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f351ecd1-f6c3-344e-a3a0-8e5fadc745f6 | -12.9141 | -45.909599 | 2026-08-31 00:35:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 68bed117-b4c6-3b26-badc-304409fc5c05 | -8.1779 | -48.810398 | 2026-08-31 00:35:00 | METOP-C | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| ccb61fa7-e1e8-3f0b-b156-3dd18dea224e | -6.2707 | -53.3465 | 2026-08-31 00:35:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7ba05fd-f623-3849-9b25-ab0851782d57 | -6.9136 | -55.723999 | 2026-08-31 00:35:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83ac097f-bd2d-3953-93fc-c8b22206865c | -6.9428 | -55.717899 | 2026-08-31 00:35:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00f69600-ba7d-3107-9c69-52d85f6b8031 | -15.912 | -56.203098 | 2026-08-31 00:35:00 | METOP-C | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 320313fd-18f9-33c2-8596-d825d264cd96 | -11.2325 | -45.1408 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 94401302-e6c0-30f1-a7dc-b2546d8e03e8 | -12.7905 | -46.4599 | 2026-08-31 00:35:00 | METOP-C | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 11a7bcdd-07d8-3d25-8984-568503000f22 | -6.5933 | -58.581902 | 2026-08-31 00:35:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1de82499-ba98-3ec5-8c5c-30e1052e2a7d | -12.9431 | -45.946999 | 2026-08-31 00:35:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 50734f24-742e-377e-872a-d43803f3539e | -10.134 | -45.748199 | 2026-08-31 00:35:00 | METOP-C | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 84248b09-22d3-35fc-ae24-8cdb0175898c | -14.2233 | -52.849899 | 2026-08-31 00:35:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f5ddc89b-68dd-3209-9722-22e43cad1d40 | -20.364799 | -47.4561 | 2026-08-31 00:35:00 | METOP-C | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2ac6d28c-5b2d-33f0-b414-61e9e03f7f51 | -10.773 | -50.873402 | 2026-08-31 00:35:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b3d5730e-b936-353a-b683-3d7524c7e0ca | -3.409 | -50.129002 | 2026-08-31 00:35:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f65fc36-f5c6-3724-8057-e72215cc28e1 | -10.8113 | -50.668098 | 2026-08-31 00:35:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 75077a5b-5236-3dfa-ac26-d139e8117185 | -10.755 | -44.8619 | 2026-08-31 00:35:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5ab984a7-6cba-31ea-98f1-85b43de45793 | -7.1217 | -42.7658 | 2026-08-31 00:35:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 11ced13f-f6bf-3431-aac1-33b3f2a5fc32 | -8.3916 | -44.997799 | 2026-08-31 00:35:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c9155693-5d61-3020-93ce-b666d80ae4ce | -14.5948 | -54.098 | 2026-08-31 00:35:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c5e4d4db-6c83-345e-b1c4-02bf78e21e1a | -11.2406 | -45.131302 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9df9f44e-89c8-36d8-b2a8-2b3a7eb3d788 | -10.7938 | -50.7304 | 2026-08-31 00:35:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 912529e6-e61a-3c58-a29d-efa8712c2f03 | -10.3461 | -49.980301 | 2026-08-31 00:35:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 44254f90-7589-3f20-9327-571bada1e2a6 | -9.3192 | -40.2169 | 2026-08-31 00:35:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| a9ae02a9-f05f-387b-b4d9-573bbfde27c2 | -15.4107 | -52.704201 | 2026-08-31 00:35:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4579b3cf-1954-3b86-8ff9-690d43f7cb56 | -10.8036 | -50.728298 | 2026-08-31 00:35:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d54d2d6c-a3b3-3409-9b96-132d7016f759 | -10.841 | -45.367901 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 915b47f1-07f3-3713-b3a9-8b5fd2e1840e | -18.2768 | -52.687599 | 2026-08-31 00:35:00 | METOP-C | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7daf8446-9ae0-3c61-850d-dd65d5312238 | -10.7511 | -54.056301 | 2026-08-31 00:35:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7bef7db3-52c7-343b-b140-3ebccb9725f5 | -11.2141 | -45.061501 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e1ee9ecd-787e-39df-b92b-0b1191abfd32 | -4.8491 | -55.8209 | 2026-08-31 00:35:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7075bc6a-73c4-352b-b449-b48eaded8947 | -8.127 | -45.502998 | 2026-08-31 00:35:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 90fe66d7-968f-3e00-a8e0-cbfa305c46ec | -10.769 | -50.854401 | 2026-08-31 00:35:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 96ab2b54-fa4d-361c-a545-33036a8bd2dc | -18.283701 | -52.669601 | 2026-08-31 00:35:00 | METOP-C | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3bcd0dc9-12a6-3378-afb5-aafd760a1b4c | -6.4764 | -49.900501 | 2026-08-31 00:35:00 | METOP-C | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c35b2bb-0cb1-39b3-8221-9f04c811b8e2 | -11.3633 | -45.216099 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c0f0fee8-9fc8-3497-a328-e5cc78a12dd1 | -14.6015 | -54.133499 | 2026-08-31 00:35:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4190a0e4-5f87-38d2-ae52-6bceed43101d | -12.0911 | -44.970001 | 2026-08-31 00:35:00 | METOP-C | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ee393607-ef05-3368-a9a2-e9499dbbeb32 | -14.2026 | -46.558998 | 2026-08-31 00:35:00 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6b2e39ad-9d26-3af2-a385-09ba6e3c0a5c | -12.9368 | -45.919102 | 2026-08-31 00:35:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8151b34b-4161-371f-af69-2be7c0f031d5 | -5.2393 | -55.930099 | 2026-08-31 00:35:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbea4785-4727-3963-bc99-fb2470f13c1d | -7.1143 | -42.778099 | 2026-08-31 00:35:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 98210bca-4558-352f-933c-48af139d35b0 | -7.8755 | -45.219799 | 2026-08-31 00:35:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2422ae05-46b2-31bd-8a00-838c60f10a3c | -7.1119 | -42.768101 | 2026-08-31 00:35:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 67bace68-06c9-36e6-844f-d3c29a4a734b | -11.1585 | -45.043999 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ef305ebd-2aa8-3298-b6b4-b470d4af4a8e | -13.3667 | -46.9212 | 2026-08-31 00:35:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8c2cb6a7-9aea-33a5-a500-a78932a46c3f | -21.431101 | -41.140499 | 2026-08-31 00:35:00 | METOP-C | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fcc25753-c73c-3f98-b835-69dd907aa23e | -12.0954 | -47.268398 | 2026-08-31 00:35:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 50cb1118-f542-3993-81ac-55becae7b128 | -6.2682 | -53.334801 | 2026-08-31 00:35:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c318844-8b4d-3929-bd4c-ef88c6eb4d16 | -11.2177 | -45.121498 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0456e141-b644-3e53-8d99-1797ea13c2f0 | -5.8763 | -52.152302 | 2026-08-31 00:35:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d893886-ef14-3179-9532-5fa5cad6bde5 | -7.377 | -45.0732 | 2026-08-31 00:35:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c6285f71-8f41-301f-89f7-1079a4707593 | -10.5915 | -52.243599 | 2026-08-31 00:35:00 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6eda9902-8581-3b3b-a01c-45ebf72b38fa | -11.3469 | -45.189701 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ebfdeb7b-cf4b-344a-9802-7cfc6d751daa | -15.4038 | -52.720798 | 2026-08-31 00:35:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b3d0791a-c534-3b65-89c3-d4365e019e51 | -10.8427 | -45.375 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7652a814-f845-3935-b580-c88ccebb308f | -7.98 | -44.297298 | 2026-08-31 00:35:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d1c8cd08-105f-3ef6-9287-601ca5fd01d8 | -10.7348 | -50.645599 | 2026-08-31 00:35:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8942bbea-1c1b-3c06-8400-1d0ef57f10b8 | -11.3519 | -45.211201 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| af02bf1d-320d-362b-a016-423d4784dc03 | -11.342 | -45.168201 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 979ed21c-48ca-38ef-8611-876708246faa | -7.347 | -55.178902 | 2026-08-31 00:35:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2c7f962-44de-38ce-8c44-1c29bf15eadc | -4.8526 | -55.837299 | 2026-08-31 00:35:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3295b8c0-a5f6-3c6b-85d7-2fbe29c503f4 | -14.3981 | -52.551498 | 2026-08-31 00:35:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c26ede24-e460-3fcf-b59e-641ca5adc7c0 | -14.585 | -54.099899 | 2026-08-31 00:35:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f3c33c79-74a5-3732-9d8d-42efae06399c | -11.3403 | -45.160999 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bacc3b2c-4185-337a-829a-252ed0a431de | -11.3763 | -45.182899 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e4a489dc-8f6a-3a74-ac83-204a32857ac7 | -1.877 | -48.831402 | 2026-08-31 00:35:00 | METOP-C | ABAETETUBA | PARÁ | Brasil | 1500107 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44d97a8c-67df-37a4-9205-2c2fc5969049 | -11.17 | -45.049 | 2026-08-31 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cb1deb02-2622-3102-bc2b-353c49444190 | -8.0858 | -45.458698 | 2026-08-31 00:35:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5e5f7347-2d43-3b5d-9826-7bff416abfb2 | -15.3563 | -52.684601 | 2026-08-31 00:35:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e59fb6f0-fa0e-3acd-9a81-548652d45de1 | -10.0685 | -48.708801 | 2026-08-31 00:35:00 | METOP-C | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 027dd369-f8c1-31ca-ade5-f41ffe7014ae | -5.6114 | -44.011101 | 2026-08-31 00:35:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d65b33e9-6683-3681-a260-57cdcc78ffb9 | -8.1007 | -45.478401 | 2026-08-31 00:35:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README12.md)
