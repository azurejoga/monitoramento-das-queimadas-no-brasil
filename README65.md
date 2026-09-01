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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fde385c-fede-3812-ba08-d425c06a7c70 | -5.3459 | -45.16232 | 2026-09-01 05:16:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 539f68aa-0b2a-3837-a811-c99ef44e7f99 | -5.25193 | -55.91509 | 2026-09-01 05:16:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d706af46-e412-323d-bcc4-f3655086fc1f | -6.60015 | -58.60694 | 2026-09-01 05:16:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c7e55750-c3ef-30d1-885c-dd50f85d1918 | -3.34621 | -59.43383 | 2026-09-01 05:16:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d743d7c-e75a-34fc-867c-e884a047d3fe | -6.77464 | -59.43329 | 2026-09-01 05:16:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58bfeeb9-6c3d-3501-9f58-f8609d6ccb08 | -6.13084 | -56.38627 | 2026-09-01 05:16:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ebec6baa-5c5d-371f-aa2b-3fd84de549b0 | -7.57197 | -57.69702 | 2026-09-01 05:16:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf8deede-3bd6-3d39-a603-49cba9efa320 | -11.68634 | -54.54597 | 2026-09-01 05:18:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dcb13d1b-14b5-3be8-92b5-dc06d1c1290a | -12.95125 | -45.95896 | 2026-09-01 05:18:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 549e9a14-6f28-3393-8a28-5719a1278a38 | -9.02738 | -65.45508 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b6222fc-a3c9-3030-bee6-1b194101f78f | -13.27912 | -48.55189 | 2026-09-01 05:18:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7044b432-0b06-3470-8441-9a86ae0a43de | -15.66961 | -48.71507 | 2026-09-01 05:18:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 73de8893-8daf-3ceb-8357-735897c1c751 | -11.1032 | -51.54104 | 2026-09-01 05:18:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 63e26789-4013-3bb5-b882-ea96ce71559d | -10.74148 | -54.02797 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| defd0a38-d1e6-3ae0-a55b-1e4b42091557 | -17.49255 | -48.87027 | 2026-09-01 05:18:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8cb8fa7b-3ece-3886-a38e-e71c88c264c3 | -16.04688 | -54.3824 | 2026-09-01 05:18:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| cb598e57-8228-332a-ab60-341d50c33bab | -11.28668 | -50.56748 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 45e713e5-a06e-35ca-af22-e886fedc0961 | -15.76192 | -56.09671 | 2026-09-01 05:18:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 10.7 |
| 7b745841-8a0a-3c83-9e30-0b24af6c24f0 | -9.32599 | -68.89183 | 2026-09-01 05:18:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2f3fe87d-e893-364e-90a3-2199ed3b33e5 | -13.57279 | -55.14684 | 2026-09-01 05:18:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ead08700-a199-3d24-9b53-78e28b26f987 | -15.25249 | -53.88488 | 2026-09-01 05:18:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 033e73a1-8ad7-305c-9504-e93af40ed522 | -9.79652 | -60.16306 | 2026-09-01 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2eb220f2-cc3b-3bd4-a8a9-697e2e2cf3f4 | -8.54004 | -67.1519 | 2026-09-01 05:18:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d377699a-84eb-3707-8565-319cde33e4c3 | -14.46701 | -52.51613 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f81668af-2c98-322f-988e-bf1ba96a9826 | -15.66283 | -45.9566 | 2026-09-01 05:18:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8529451e-77d5-3e39-842a-22081bf72ede | -11.29493 | -50.57311 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| e6dd0931-b1a7-3749-888f-8fe858ad4679 | -15.25389 | -53.84631 | 2026-09-01 05:18:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 290e0441-4615-33ec-af33-3680fd3051b1 | -14.57524 | -52.10545 | 2026-09-01 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc35fe65-b01a-3a2c-8463-a5a99a406494 | -10.74505 | -54.02852 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 40aaa50d-994c-3f0d-a97d-571fb7fa7d9a | -14.5903 | -54.1152 | 2026-09-01 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 877207da-da3e-34a1-9f4f-04d651a75b33 | -10.43601 | -67.84354 | 2026-09-01 05:18:00 | NPP-375D | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 899f85f1-3781-33e2-9bb9-b830780087e4 | -14.67334 | -53.54644 | 2026-09-01 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3f7d76e5-1bc5-3b25-a26b-494a9a7e0ce8 | -15.62817 | -56.38418 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a6ae05e4-8ef6-3652-ad54-b69b9aff576a | -11.24708 | -54.01064 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| acab9771-ce17-342a-bf7e-f786f92721b7 | -13.81964 | -54.01131 | 2026-09-01 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7401d5ff-9be2-3276-9620-2aac25fe8fa9 | -15.24491 | -53.88377 | 2026-09-01 05:18:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ece0039c-9405-318a-9787-30f43bd28358 | -11.69337 | -54.54708 | 2026-09-01 05:18:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a52fecb3-dd69-3bb9-a625-22886ba228df | -11.65584 | -47.60236 | 2026-09-01 05:18:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4a906d33-96c8-389d-80c8-0f44c6812ba9 | -10.7474 | -54.03725 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3d54d717-4560-3661-9271-83f46893d235 | -15.63322 | -56.41967 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7cdce5a1-cb0a-3990-bfa5-6a61b16d89c6 | -15.77569 | -56.09887 | 2026-09-01 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 1e7c931e-35ca-33b4-8828-5bddaceb214c | -11.65995 | -47.61363 | 2026-09-01 05:18:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3df1d6e9-9dd0-3cfc-a511-d0ff01f26c3f | -15.29537 | -53.18855 | 2026-09-01 05:18:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f08252f3-d84a-3846-9caf-a7a49c38f993 | -9.03295 | -65.39619 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f9fa1e8-274f-3ecc-a092-c5dce9068959 | -15.24966 | -53.8534 | 2026-09-01 05:18:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9346ef01-edbf-34db-9703-04e6e3f9a73c | -15.74992 | -56.08284 | 2026-09-01 05:18:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| c8d2bf34-175b-33d6-b550-c374548b75ea | -9.02832 | -65.39201 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a178f6a-4254-3fe4-8dfd-24ee71385407 | -10.77653 | -54.03755 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fcdbc7e-aaa4-3198-96a9-e536fe547ab2 | -10.74618 | -54.0454 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c0a8795-c62f-3398-967d-8597fe5a56bc | -8.6058 | -70.20803 | 2026-09-01 05:18:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2f020b3-2f5b-3341-869d-d99c95086a12 | -15.55771 | -56.27222 | 2026-09-01 05:18:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3475e33b-3632-35ec-a5ec-99c96c0b4f36 | -11.29689 | -50.58124 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1342c79b-9737-312d-aab0-877e8890aeb9 | -11.06118 | -51.52374 | 2026-09-01 05:18:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa6ae659-d82a-3212-af4b-10c0a333bf2f | -11.06172 | -51.51998 | 2026-09-01 05:18:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa487811-1511-3ef9-b654-b9f15b17e5bb | -11.91209 | -45.07598 | 2026-09-01 05:18:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 62d98aa0-5499-3956-8a11-72bac4025c72 | -14.71771 | -53.59262 | 2026-09-01 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3928c684-0752-3451-bb7d-a6c69a061c46 | -14.58231 | -54.07958 | 2026-09-01 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 389b65f1-0b26-32f0-a057-62ccb9ad2507 | -15.24206 | -53.85234 | 2026-09-01 05:18:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd4701cf-7cc3-3153-98c8-4a3aaa7ab733 | -8.71676 | -67.10725 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1fa6e968-b868-39d2-bfdd-6443113efde6 | -11.65539 | -47.6059 | 2026-09-01 05:18:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 175422a7-1b71-3810-b877-e648e62b7be7 | -15.43808 | -52.68487 | 2026-09-01 05:18:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| adb43f9c-d59e-344d-9b1f-fb1acfc53b2c | -15.01406 | -52.77054 | 2026-09-01 05:18:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 821ab60d-872f-3afc-ba87-ac1b33e8ee49 | -14.47006 | -52.52405 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e4e58080-8cb0-3367-b38b-5e4628c2b352 | -14.39713 | -52.48001 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17bdf42f-e2b6-3aee-b8ae-1060015725fc | -14.12886 | -52.78723 | 2026-09-01 05:18:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51761f17-b7f8-3bc1-b191-3edbfa7d70cf | -16.0405 | -54.4003 | 2026-09-01 05:18:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 502c9321-4317-3693-95fa-ace389ea5a03 | -11.29343 | -50.60743 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b993188b-f524-3a11-a211-a0dfa61c6bb9 | -16.47583 | -47.95133 | 2026-09-01 05:18:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 44f5a9f0-9c0a-3dbb-b658-619e49bd5216 | -14.50681 | -52.23748 | 2026-09-01 05:18:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dae7f5f0-c413-3f9d-ab61-a7bd25f167e5 | -10.74269 | -54.01984 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66f8054c-46a5-33c3-bd94-b43e2afedad3 | -9.00442 | -65.43263 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed93ec15-aa36-3cd7-b7da-5d45edaf49a1 | -10.06382 | -59.40771 | 2026-09-01 05:18:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 39af5922-106b-3914-a6ca-1e0e08696e6c | -11.68925 | -54.5505 | 2026-09-01 05:18:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8fc8b15-7133-305f-a476-7edfdb914dc7 | -15.60717 | -56.38462 | 2026-09-01 05:18:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2fdd8d05-8d38-3409-941b-a4ef277016ae | -16.14214 | -52.38228 | 2026-09-01 05:18:00 | NPP-375D | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7935db68-6800-355a-ac66-8013f1152bbc | -10.73912 | -54.01928 | 2026-09-01 05:18:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbaff3ae-52ee-3ec9-b895-f1b344620089 | -13.48178 | -57.06348 | 2026-09-01 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| abe4059a-e2f9-36b3-a7a0-8d092687939c | -16.04725 | -54.39035 | 2026-09-01 05:18:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| cf6065a9-4506-3c22-87de-4b3d41c58ad7 | -14.46597 | -52.5236 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bfbb791b-a8ce-3492-93e1-7f3ea2b52f02 | -14.67016 | -53.54112 | 2026-09-01 05:18:00 | NPP-375D | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 566f58aa-10af-306d-8d61-65d5770178f3 | -13.47845 | -57.06294 | 2026-09-01 05:18:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 14200000-5962-3e82-a86b-13dcd046aede | -15.17869 | -46.24639 | 2026-09-01 05:18:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a0010a58-34f7-3d14-8285-e16333edb959 | -15.2487 | -53.88712 | 2026-09-01 05:18:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c244c27b-38dc-310d-84bf-990b42d35261 | -11.05865 | -51.51185 | 2026-09-01 05:18:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa35a453-6086-3867-93ce-1599e877719b | -8.86849 | -66.77596 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9a185a6-4219-3cf3-89f2-4f5164dc9185 | -15.29142 | -53.18795 | 2026-09-01 05:18:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d95f56e2-91d1-3a32-a59d-b9907d0a5de4 | -13.96417 | -54.39509 | 2026-09-01 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40b5029b-19b1-311c-9e8f-b8c6610d3a91 | -11.30257 | -50.58309 | 2026-09-01 05:18:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f8a8f789-3a9a-340e-a2b3-73b276f9ca02 | -15.05683 | -47.9894 | 2026-09-01 05:18:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b8b18d34-ad6a-3729-9871-2f1d76ec3374 | -16.04353 | -54.38978 | 2026-09-01 05:18:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| d0badece-209e-3b09-8ed8-adcbfe4d9507 | -10.94929 | -61.6595 | 2026-09-01 05:18:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 98e9bd65-d995-312a-b1a2-3fd9989f9870 | -13.96055 | -54.39452 | 2026-09-01 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60b5d9d7-4f51-3d2f-9e7f-08cf69b7f07b | -15.66012 | -48.70346 | 2026-09-01 05:18:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c095849f-bdce-3be8-8661-bbddf5d0a953 | -8.99918 | -65.43164 | 2026-09-01 05:18:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e5c6d42-4350-32d2-9a2b-66fbb61e6895 | -12.7819 | -46.46399 | 2026-09-01 05:18:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e9bc538-1801-3b57-b292-a1a096820906 | -16.05097 | -54.39088 | 2026-09-01 05:18:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 02a63328-5001-3453-87c5-db0f7892f82f | -14.44355 | -52.5055 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fd8ab0b4-65de-3c5f-8b43-512575df9711 | -15.25034 | -53.84865 | 2026-09-01 05:18:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 507ae551-0188-3855-a271-c2e6499623a6 | -14.57986 | -54.08146 | 2026-09-01 05:18:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71ba676e-3fe8-330a-a43d-01e51659681f | -14.38923 | -52.53883 | 2026-09-01 05:18:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README66.md)
