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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f766f0c-c814-337a-9d25-32446f3a8ade | -19.67527 | -57.17208 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 0bddb364-5967-3c61-a83f-43ffa5f795da | -19.62421 | -57.34399 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 34cbbc70-6fa2-3b6a-8a3e-6d1074657e67 | -19.70321 | -56.83581 | 2026-01-26 05:22:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 324df8d0-d484-3e65-896d-efe5c8733e71 | -19.61125 | -57.32061 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| fe75efb4-e9aa-3692-ae41-debc0b07373d | -19.64711 | -57.35268 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 87727865-a3a5-3d1f-94b5-90394d8e0fb6 | -19.72269 | -56.846 | 2026-01-26 05:22:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 30be2876-d8f8-3c30-ac9b-d2d8b0af1d5e | -20.91853 | -56.37313 | 2026-01-26 05:22:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cf0b18d6-0dd2-3718-876a-4087d28dca75 | -19.61773 | -57.3323 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a6b55658-ebe4-3680-a35a-18807850797a | -19.65034 | -57.35851 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| ccb0734b-a0df-303d-893f-3ee3fb105c21 | -20.91801 | -56.37737 | 2026-01-26 05:22:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c5b37cc6-14af-3feb-8770-11c230b88235 | -19.67735 | -57.1743 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 179e66a9-db8b-3cf3-8a8f-36691726112e | -18.82041 | -57.71036 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 12b442cd-11db-388b-8508-fa2822bf3c55 | -19.66362 | -57.31403 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| f091ad1c-2340-385a-b6ad-26ce9af63901 | -19.71589 | -56.83377 | 2026-01-26 05:22:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| d163117d-c16f-31b8-9803-d35ab6108f6d | -19.68133 | -57.17487 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a6972c3a-7bcf-31a7-bc8e-9e739e5842e6 | -20.31962 | -57.8173 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| cfa93705-1850-34ed-bac6-3132e0f9a4ef | -19.71441 | -56.84506 | 2026-01-26 05:22:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 4abca208-4c76-3161-bd8a-f4e38e1875da | -19.67337 | -57.17373 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 078e1a48-7d45-3ea0-b664-989217746f30 | -19.65427 | -57.35908 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c4460b6b-e1fc-310a-b725-af02ae9654d2 | -19.69102 | -56.83408 | 2026-01-26 05:22:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d72c29df-313d-3cdd-a5e1-f27fcde2b3bb | -19.7191 | -56.84165 | 2026-01-26 05:22:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.3 |
| a0f8f4a1-b068-3ea5-a6d3-c70eb82f0e32 | -19.65968 | -57.31346 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| c885148b-2620-36fb-8b53-86305130b56e | -18.84631 | -57.74115 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| cc9cefaf-f6af-3609-a463-323f772459df | -18.82355 | -57.71581 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f272cc46-8b9d-36f4-9047-b2d131515e8a | -19.66621 | -57.3252 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| b9b25dbd-c54b-3a2a-9b86-188281626bde | -20.31643 | -57.81166 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| f603324a-434c-375b-b2cf-a8723ac3ab44 | -19.61077 | -57.29358 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| debfdf26-1be9-3304-a436-82cfe0429c45 | -19.64642 | -57.3546 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 67d0c544-d322-3d5a-807c-6d61b4114ae4 | -20.31894 | -57.82237 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| e0a4ddf0-2952-3055-b490-0acd89d00472 | -19.61194 | -57.31532 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6848f21f-3988-3994-8c7e-59e6ed3941d1 | -19.71269 | -56.8599 | 2026-01-26 05:22:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 242275a5-817f-3863-bc93-33ad4302a766 | -19.65498 | -57.35382 | 2026-01-26 05:22:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 155753ba-bb1e-3f33-9e7c-ddbf21dba5ff | -6.5631 | -51.1126 | 2026-01-26 06:20:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| ac054491-eea8-3d1d-be46-1fc5b5931511 | -3.00044 | -52.86543 | 2026-01-26 06:31:00 | AQUA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b8f9ea1d-5bcd-3db1-bf22-46252a5f18d0 | -18.82144 | -57.71386 | 2026-01-26 06:37:00 | AQUA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.1 |
| d96f475d-cbca-34ae-be22-77e5d08cc82e | -19.69925 | -56.86369 | 2026-01-26 06:37:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 31.5 |
| 38e4f639-ff43-38c7-aa4f-36d689dede30 | -19.70406 | -56.83348 | 2026-01-26 06:37:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 12.0 |
| f2a950b6-18fa-37ac-b708-e93c5d4625be | -19.69764 | -56.87377 | 2026-01-26 06:37:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.0 |
| ac78f2c9-8416-3f5d-aa4a-961a019f1a63 | -19.69493 | -56.83186 | 2026-01-26 06:37:00 | AQUA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 17.9 |
| 4496e35d-1b13-3a66-aa8e-1ad6a9e2334a | -4.36707 | -37.90856 | 2026-01-26 11:34:00 | TERRA_M-M | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 4f6320ca-c143-3861-8111-3f301ab5aa47 | -5.77364 | -36.49395 | 2026-01-26 11:34:00 | TERRA_M-M | SANTANA DO MATOS | RIO GRANDE DO NORTE | Brasil | 2411403 | 24 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 1b2e6aa0-c972-381f-baa0-d5c2e180b7c1 | -7.73668 | -37.47807 | 2026-01-26 11:34:00 | TERRA_M-M | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 060b5716-e2f6-3b39-8615-d0f68254ce51 | -5.39028 | -38.03758 | 2026-01-26 11:34:00 | TERRA_M-M | TABULEIRO DO NORTE | CEARÁ | Brasil | 2313104 | 23 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 31235c6a-68cb-3230-8e08-923d09d88ad5 | -5.15659 | -39.59755 | 2026-01-26 11:34:00 | TERRA_M-M | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 2e854d83-2270-36f0-a251-65b99ed73d97 | -8.55806 | -35.47318 | 2026-01-26 11:34:00 | TERRA_M-M | ÁGUA PRETA | PERNAMBUCO | Brasil | 2600401 | 26 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| d2846615-8231-39ca-98f1-522688ea23f1 | -12.61724 | -39.27296 | 2026-01-26 11:34:00 | TERRA_M-M | CASTRO ALVES | BAHIA | Brasil | 2907301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 4b800c82-f1e4-384c-a9be-bcd02c8347cd | -8.55968 | -35.46075 | 2026-01-26 11:34:00 | TERRA_M-M | ÁGUA PRETA | PERNAMBUCO | Brasil | 2600401 | 26 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 36ce1a97-4d76-3d64-b8ec-d8b4e8b8fc8a | -4.36832 | -37.89973 | 2026-01-26 11:34:00 | TERRA_M-M | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 6b4b4c46-b110-337b-bacf-f98bb08e0558 | -7.77839 | -41.41357 | 2026-01-26 11:34:00 | TERRA_M-M | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 27b9d1c0-89ce-371e-a51f-863f0752a9cb | -9.48105 | -35.75641 | 2026-01-26 11:34:00 | TERRA_M-M | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| a6058e6f-8406-337a-be61-e20b8f5cc243 | -7.94968 | -37.08101 | 2026-01-26 11:34:00 | TERRA_M-M | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 9c1cb4ff-8f95-31c4-a758-ea348d81fa74 | -7.94829 | -37.09088 | 2026-01-26 11:34:00 | TERRA_M-M | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 82589046-32c7-3ceb-bbea-81a3fc812806 | -5.6525 | -37.22953 | 2026-01-26 11:34:00 | TERRA_M-M | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 7f661f98-b704-3466-9506-dc2532c87997 | -7.54177 | -37.75305 | 2026-01-26 11:34:00 | TERRA_M-M | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 9e73be1e-e5b2-34bb-818c-7d26ab6e60e1 | -5.73552 | -38.97144 | 2026-01-26 11:34:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 17.6 |
| 01f6877a-76cf-3b3a-a78d-46a2d503b7a0 | -17.72571 | -39.75376 | 2026-01-26 11:36:00 | TERRA_M-M | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| a3cb7223-93f0-39fa-b3a4-32258ef6c13f | -20.3092 | -57.8252 | 2026-01-26 12:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.1 |
| d67abb1d-4348-3055-931b-b14fec229769 | -20.3096 | -57.8043 | 2026-01-26 12:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.5 |
| 7f496e49-5741-3cf9-9b05-99aa110125ef | -20.3294 | -57.8224 | 2026-01-26 12:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.0 |
| ae2f6944-7b56-3743-9484-4e827034699e | -20.3092 | -57.8252 | 2026-01-26 12:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.7 |
| 91e02dfa-b839-3db3-8552-c475c2d389ad | -20.3096 | -57.8043 | 2026-01-26 12:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.7 |
| 0c1ed205-65fa-323b-88dc-060ee6cea63b | -20.3092 | -57.8252 | 2026-01-26 12:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.2 |
| 231094be-1d41-33cb-ab18-8974698bea96 | -20.3096 | -57.8043 | 2026-01-26 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 99.1 |
| 38cbc3dd-7e80-32a9-a809-a0cc8542b33a | -20.3092 | -57.8252 | 2026-01-26 13:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.5 |
| ea7eaa60-69bf-37f3-b1ef-8362b86d8b72 | -20.3092 | -57.8252 | 2026-01-26 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.2 |
| 4472e673-9773-394a-a587-db18221c8622 | -20.3096 | -57.8043 | 2026-01-26 13:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.8 |
| 788e5932-f25d-3961-a59a-e01f3fc6a105 | -7.2785 | -43.0627 | 2026-01-26 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 104.9 |
| 026ab5e2-5148-31dc-bd8b-f82506951571 | -7.2594 | -43.0881 | 2026-01-26 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 752.0 |
| 6090952b-e960-387d-a9fb-afd8dd3b0cde | -7.2782 | -43.0862 | 2026-01-26 13:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 398.6 |
| 4924b65b-2ee8-3075-b47d-03f01690803a | -7.2782 | -43.0862 | 2026-01-26 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 312.9 |
| 013b4939-4fd1-308e-9111-308f5aa5cecc | -7.2785 | -43.0627 | 2026-01-26 13:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 115.6 |
| 50eeb0a5-9c2a-380d-837e-0e7c245c1aca | -20.3287 | -57.8643 | 2026-01-26 13:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.5 |
| e1ca4eaa-4e56-38f6-8570-0d844ed6252d | -7.2782 | -43.0862 | 2026-01-26 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 288.9 |
| 90fb422d-b262-3d33-8735-71a5d2347576 | -7.2785 | -43.0627 | 2026-01-26 13:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 103.7 |
| d0fff05b-82d4-3d6d-8a9d-488b2ab613f8 | -7.2594 | -43.0881 | 2026-01-26 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 733.3 |
| 394e5f39-dcdf-3cb6-b3fb-32f655f11df7 | -7.2782 | -43.0862 | 2026-01-26 13:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 260.9 |
| 95cc4b04-0409-3f69-96cf-9551d7298ade | -7.2594 | -43.0881 | 2026-01-26 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 852.9 |
| f189c2c8-04a5-3f44-ba98-36f40be56f51 | -20.41 | -57.8323 | 2026-01-26 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.4 |
| 2f4ce7b7-a545-36f4-8142-306856fe5194 | -20.3897 | -57.8351 | 2026-01-26 14:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.8 |
| ff356cf4-7d04-3d62-8ad7-20b7c758e261 | -7.2782 | -43.0862 | 2026-01-26 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 282.8 |
| 7a268af6-5469-3f23-85be-625f3b778f05 | -20.3085 | -57.867 | 2026-01-26 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.5 |
| 8c57c559-3d16-3b6f-9296-fb5327506952 | -20.3092 | -57.8252 | 2026-01-26 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.9 |
| 808ed72e-f2d6-380c-86dc-835ead91632f | -20.3897 | -57.8351 | 2026-01-26 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.5 |
| 4fa59265-8a56-3c62-a81e-26666b29c064 | -20.3088 | -57.8461 | 2026-01-26 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.5 |
| 5bc5f574-c104-31ea-ace3-e98f294a3ced | -20.41 | -57.8323 | 2026-01-26 14:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 106.2 |


