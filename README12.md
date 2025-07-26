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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74ea0325-14af-335c-9563-16a24138e24c | -12.04913 | -45.4361 | 2025-07-26 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db6272e1-3854-3dcc-ae9d-77dc29e06602 | -13.69766 | -45.69095 | 2025-07-26 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 285575fd-d91f-3b4d-9299-7df72e395f1d | -9.73092 | -48.02184 | 2025-07-26 04:04:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b50691cc-67d6-3149-b6ec-b1fcc90887fe | -9.71395 | -48.94954 | 2025-07-26 04:04:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9d505d3-08c9-39d6-8e2e-718b073734af | -13.91383 | -41.30452 | 2025-07-26 04:04:00 | NPP-375D | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 20e859d5-5065-3864-a2eb-80422522c30f | -13.11573 | -47.34784 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a40ca914-5ce9-3ca9-959c-5a0c19cfc112 | -6.01015 | -52.17873 | 2025-07-26 04:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e7bcc78-295d-39d1-baa7-f5c8dd1f5ddd | -13.09374 | -47.34829 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0f33fe0-f873-3c93-97d3-b9bf991e813d | -13.70012 | -45.67675 | 2025-07-26 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eac9cdeb-4a09-35f3-a271-f7e42550a9a3 | -13.12295 | -47.32455 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0e59261d-ce5c-3c37-93b6-6c060a7a7477 | -10.35531 | -46.64886 | 2025-07-26 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d545fdd0-62dc-3f74-9b2b-0af806d9539f | -10.84977 | -54.04115 | 2025-07-26 04:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18aa5ee1-0178-3a77-964c-a3a72f9313c7 | -10.67988 | -51.88881 | 2025-07-26 04:04:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 132e5c4b-e426-3f21-952a-2f19018b0bc3 | -8.0744 | -48.0126 | 2025-07-26 04:04:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 570b9cfc-91ef-30ed-b0bd-22068594a752 | -10.59294 | -44.74672 | 2025-07-26 04:04:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f8f85a1-1bdf-32fd-afbe-61f8d07cc735 | -13.11148 | -47.34709 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52772436-c357-3fd4-a272-88464c394ba6 | -8.29181 | -45.00319 | 2025-07-26 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d900dde9-6333-3c36-913c-196e028665ea | -13.24584 | -51.14762 | 2025-07-26 04:04:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3acfc9f-ff73-314a-b299-60520d2df12d | -9.3603 | -40.30928 | 2025-07-26 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 0bd78a93-2c3e-353b-9e57-ed8a8bd915f1 | -8.17464 | -43.21116 | 2025-07-26 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 740b804b-d1c4-30ec-a74e-4c06414a0e7a | -13.10842 | -47.36443 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 687b9ab4-ec8f-361a-b5c9-1e98c2689e89 | -6.99076 | -47.08232 | 2025-07-26 04:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 714700ad-10ae-3cad-b0cc-df1ecd354de1 | -13.10838 | -47.33231 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d4e35d7-180d-3d05-8225-3078cc49ecaa | -9.01778 | -45.35843 | 2025-07-26 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| add67025-5652-38c5-b7f2-e206c5ecf3b3 | -9.47609 | -40.37076 | 2025-07-26 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8a0be3b9-ee9e-3370-bdc2-2c7a49a5b462 | -13.11746 | -47.33059 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a40b151-4317-37a0-8f51-ec75542f9a67 | -10.35609 | -46.64442 | 2025-07-26 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| b3c49a1c-ae27-325e-a0fc-659e0f475ca5 | -10.68073 | -51.88445 | 2025-07-26 04:04:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fcd1bd9d-3f0b-3cf0-95e0-3de6b89544a0 | -8.17621 | -43.22409 | 2025-07-26 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6b168a1b-1984-3a06-9361-cea0e2635782 | -13.69469 | -45.68552 | 2025-07-26 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fe44c69d-8697-397b-b4c3-593f50cb050c | -9.47554 | -40.37426 | 2025-07-26 04:04:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 172b2acb-0e56-3ada-b5b5-cdb0ff5df020 | -13.12165 | -47.3316 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ead8d07a-00d1-384a-ac4b-2b49449016b7 | -13.69304 | -45.69499 | 2025-07-26 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8206e73d-a0a8-3702-8736-bb4a212eeb11 | -14.13389 | -45.27869 | 2025-07-26 04:04:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd020750-d129-3c1d-aef2-491993247c99 | -7.78748 | -44.5456 | 2025-07-26 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 211e7db3-4cce-3284-b374-01a6fccf116e | -13.11913 | -47.32866 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45371791-913d-3426-9192-e7f49c436bcf | -13.09299 | -47.35254 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 97d6127f-02f6-3a58-a434-9e9d58b1dc62 | -7.89991 | -42.63676 | 2025-07-26 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 504c4dcf-8a91-3326-a918-484330dad617 | -10.67306 | -51.892 | 2025-07-26 04:04:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a9a933b-a6a7-31f3-83d8-73dab2bc8f87 | -8.17553 | -43.22822 | 2025-07-26 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 20ed0ac2-23b7-31d5-a875-19e3b92ab473 | -9.58029 | -43.86094 | 2025-07-26 04:04:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 93b19a3d-6ab9-397b-9371-179074b67f21 | -12.71597 | -46.27773 | 2025-07-26 04:04:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b4c3f108-968c-32b4-a9ed-afef94670058 | -13.12101 | -47.33508 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fdc038c8-5e05-3cc4-b4d2-ae165a126848 | -8.1733 | -43.21936 | 2025-07-26 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| eaf6a32f-9941-397b-b8b6-de9fa5be2705 | -7.78364 | -44.54478 | 2025-07-26 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 995ee78e-952b-30c9-9032-29ca55178427 | -8.81363 | -46.75178 | 2025-07-26 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf6a538a-7538-3f65-8d5f-5290302be0c1 | -11.73515 | -48.18137 | 2025-07-26 04:04:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 998d1ad2-3af1-386a-9409-7011fcd09e9e | -12.68458 | -46.9944 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 799b165b-ce45-3e4d-9497-e8081ac9ac60 | -9.73239 | -48.01854 | 2025-07-26 04:04:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b78e60f6-3cbb-387a-a333-17af0b1cd86f | -12.04292 | -45.4376 | 2025-07-26 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52d6d923-8b3f-3de0-823c-e5b700ee35ae | -8.37052 | -46.6571 | 2025-07-26 04:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 878794d9-1b22-365c-a96a-8c78ad3c6479 | -8.87244 | -45.58082 | 2025-07-26 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 319978e8-807e-3127-bd11-d8d15de98617 | -10.13458 | -46.72348 | 2025-07-26 04:04:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17689bf5-834a-3e30-acfd-3ce95584a71f | -14.2142 | -43.94787 | 2025-07-26 04:04:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 26379c8d-2d64-3422-acde-4ed365a2b3fe | -9.24927 | -50.22705 | 2025-07-26 04:04:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 671a722f-8cc0-33ee-b9f2-523de85ca923 | -13.54342 | -43.56854 | 2025-07-26 04:04:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 469c0ac1-9099-3b05-b850-daa84000094f | -10.84846 | -54.04746 | 2025-07-26 04:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8a58020-e9a0-3628-8ee4-eebec1adf4c0 | -13.69336 | -45.67064 | 2025-07-26 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 929b26dd-a2c7-3d47-999f-1e6665b27370 | -13.54686 | -43.56914 | 2025-07-26 04:04:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ded39a9-ee1b-3714-bce0-b086eeee9bf8 | -9.73561 | -48.02279 | 2025-07-26 04:04:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2bcaaf6d-c3b8-3f40-8c58-595e4a7eff7f | -10.62523 | -44.76171 | 2025-07-26 04:04:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b3e3073a-5d6e-3b0b-93e6-d37001d5b8cd | -9.00268 | -45.35058 | 2025-07-26 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a3564cc9-3ace-3b9b-944e-a36d1d8f63d5 | -12.42187 | -45.3877 | 2025-07-26 04:04:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec0f5b43-f5ba-30f2-bb87-9756e404ebb8 | -7.97719 | -49.6937 | 2025-07-26 04:04:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2219befb-8667-3e57-ba3f-d7f9cce5a746 | -13.11307 | -47.35438 | 2025-07-26 04:04:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ce40316-e215-3ecd-ae59-3af4a5c3cc12 | -9.28744 | -40.44791 | 2025-07-26 04:04:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5e1a0266-c751-33df-bb53-918920f4109b | -7.66393 | -47.47509 | 2025-07-26 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 30b2cfa0-547b-372b-9733-eec8b73bf5c8 | -6.9935 | -47.08514 | 2025-07-26 04:04:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6219f2f2-14a2-3ca2-9209-dec0ed515009 | -13.72042 | -45.69512 | 2025-07-26 04:04:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1bd0da82-4e87-3c61-97af-3ecf930b3b53 | -17.70451 | -44.30679 | 2025-07-26 04:06:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a811640-544c-3370-95d4-10b9730e50fb | -18.24601 | -44.7874 | 2025-07-26 04:06:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 34.2 |
| fc668a2c-0ecb-345b-9a27-ab4685d18ceb | -14.96743 | -46.98134 | 2025-07-26 04:06:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36410822-c7a7-3651-89ca-cc0ba57663f6 | -17.86801 | -39.66408 | 2025-07-26 04:06:00 | NPP-375D | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6d376906-784f-3f97-8fd2-f38fc3600a38 | -14.96353 | -46.97993 | 2025-07-26 04:06:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9c0db23f-bfef-3e0a-ad10-565fefd6f03c | -14.95373 | -46.96526 | 2025-07-26 04:06:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3fb60bf-88ef-39c1-a9b2-66156babb95d | -18.25424 | -44.78082 | 2025-07-26 04:06:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d6d49c02-ce55-3408-9fa2-3d563e3aaa66 | -16.12589 | -47.40585 | 2025-07-26 04:06:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 315cf37d-41d0-3028-a84a-3a69d4fc5bec | -15.76081 | -47.77393 | 2025-07-26 04:06:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a5004db4-51c8-39ce-804d-68cf6a1944fe | -18.2529 | -44.7887 | 2025-07-26 04:06:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 2a484b07-d09b-35a0-85c4-1b497b5060fe | -18.05588 | -44.8391 | 2025-07-26 04:06:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5b89b9a7-3119-375f-9e3d-20ab427a0667 | -19.97006 | -48.43081 | 2025-07-26 04:06:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a24bd627-040e-3a94-8eed-3b3c8e0ad678 | -18.25012 | -44.78413 | 2025-07-26 04:06:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 145a2b2d-a129-33d5-a89c-95e732a7d78f | -15.78703 | -41.32215 | 2025-07-26 04:06:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d14e496c-00de-37c0-a7b3-9dd57b92fc3e | -14.375 | -50.3327 | 2025-07-26 04:06:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07ed0870-e5e4-30ba-b5b0-6b1810c6ffc3 | -14.93991 | -46.94999 | 2025-07-26 04:06:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ca3904b7-92be-3f5c-8937-18266c298f67 | -15.78591 | -41.32939 | 2025-07-26 04:06:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| a2b0ebb0-64cd-3f0f-9e4c-e8c21e20c4ad | -16.64205 | -49.21121 | 2025-07-26 04:06:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1d13521-a541-39d8-b71f-738ab76b9f5d | -19.9655 | -44.71827 | 2025-07-26 04:06:00 | NPP-375D | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e0025b38-bac9-3038-a298-29a38db47e30 | -15.26482 | -47.13798 | 2025-07-26 04:06:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d0772b3-ba50-3bb7-a20e-4eb94ec6b844 | -20.3908 | -42.39496 | 2025-07-26 04:06:00 | NPP-375D | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f2645629-1d0c-30bd-aeef-052d8fb03ae8 | -15.87641 | -43.28835 | 2025-07-26 04:06:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2266107-1e01-3daa-b27d-e36d512c5740 | -17.04442 | -43.77226 | 2025-07-26 04:06:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dc7995dd-5f38-3392-ad11-546bb864522c | -14.96092 | -46.97138 | 2025-07-26 04:06:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66605d57-49b3-3fae-bd0b-9192a47fff3c | -18.25769 | -44.78144 | 2025-07-26 04:06:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| db70cf8c-6cba-3dd7-a93e-9412ee0f38da | -16.3053 | -52.92593 | 2025-07-26 04:06:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 582f57ce-a3d1-3b1e-ba37-0e0de6d9de03 | -14.9544 | -46.96158 | 2025-07-26 04:06:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec37e2b7-997a-3b34-8ebe-5d8021e3ac30 | -16.09743 | -42.28015 | 2025-07-26 04:06:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| de889563-9af0-339b-9341-8ecaf9963783 | -15.78647 | -41.32577 | 2025-07-26 04:06:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 66ac31f5-85a0-3352-a403-9814e0d68125 | -16.04733 | -43.7976 | 2025-07-26 04:06:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca6d4fad-b9a8-34c4-8ebf-7a554de89b79 | -19.44528 | -41.61749 | 2025-07-26 04:06:00 | NPP-375D | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |


[Clique aqui para ver as próximas entradas](README13.md)
