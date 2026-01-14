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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7bce2407-7530-3427-ac75-9c6c650a4d3e | -12.8445 | -52.5182 | 2026-01-14 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0a3b827-a322-39b2-86ec-9d32df3a34fe | -2.36055 | -51.89421 | 2026-01-14 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bd34c6a-6844-3f95-b897-23ff9a529440 | -1.93582 | -53.46898 | 2026-01-14 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3184f40-374d-3c34-b268-1a701cb9331c | -12.84394 | -52.52192 | 2026-01-14 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d3f78e4-8204-3ee8-b302-9b6dc8115b81 | -5.10843 | -43.23199 | 2026-01-14 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 890448e5-004f-3373-b47b-e07c7c99c103 | -1.8933 | -53.26646 | 2026-01-14 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d08ea763-54ff-3457-9159-8a549a65798c | -5.16371 | -38.65756 | 2026-01-14 04:53:00 | NOAA-21 | BANABUIÚ | CEARÁ | Brasil | 2301851 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| d5d8ecd3-2483-35ea-99ea-6de430b3125f | -12.85129 | -52.51926 | 2026-01-14 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38fdbc0a-b884-3015-b708-bf2ac5a6c0df | -1.4208 | -54.02022 | 2026-01-14 04:53:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1577b02-4441-3913-97d8-33e87d8bc68e | -12.84111 | -52.51767 | 2026-01-14 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cac76ac8-9fa1-3c26-a56d-597c73ef37d1 | -6.59473 | -44.32606 | 2026-01-14 04:53:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11eedb2f-042d-3a4e-953c-6adc29432072 | -12.84 | -52.5251 | 2026-01-14 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6199d73e-fa64-3e1f-8ae3-03005417349d | -3.07487 | -52.80411 | 2026-01-14 04:53:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 044be582-50b8-3d48-953b-fee9ba352e00 | -5.10256 | -43.23473 | 2026-01-14 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cde27125-b66e-3fac-9f96-cba9478dde36 | -12.84789 | -52.51873 | 2026-01-14 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff6855b8-5351-35ec-bd7a-aeca79cb8f84 | -12.84339 | -52.52564 | 2026-01-14 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0b9cd62-038c-3edd-bbe3-c27c20d1bbc3 | -5.1772 | -43.27193 | 2026-01-14 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc031fef-e5f4-36b7-8111-2bce234d59db | -1.67372 | -46.70589 | 2026-01-14 04:53:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 92ffe9c8-23b1-3e9b-a63e-efa199f2fd36 | -5.10161 | -43.24141 | 2026-01-14 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3d9e9ff6-f1a3-3635-924a-ea4ddff5fec7 | -5.10746 | -43.23876 | 2026-01-14 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a278d2c0-6f47-37a1-a0db-c56393fa5e46 | -13.69115 | -55.68439 | 2026-01-14 04:53:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 63054ab4-988d-39ef-a917-cc3c80460157 | -1.29401 | -53.68622 | 2026-01-14 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb276b53-9ad2-31ac-886f-eabf2a3b0273 | -4.75134 | -43.25127 | 2026-01-14 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| faf7c2e5-189d-3090-a151-d7b05d9af215 | -1.96286 | -52.10516 | 2026-01-14 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 726b1bd9-1ea6-3186-a150-8b4e71f870b1 | -1.34739 | -53.48279 | 2026-01-14 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a5fc85c7-8d5e-3d1f-ada7-47a9ab5ede5e | -5.67643 | -45.20292 | 2026-01-14 04:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6d9a3fd9-b937-3144-870b-218e1b3ed5eb | -1.29057 | -53.68574 | 2026-01-14 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb11b712-68ee-370d-b3a7-213012ec19de | -5.10794 | -43.23538 | 2026-01-14 04:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 325ce39b-7006-3c2c-bfdc-5163a011a3fe | -2.09342 | -52.03117 | 2026-01-14 04:53:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ba9f9540-ffe1-30e5-b25c-ca676bf23771 | -12.84734 | -52.52245 | 2026-01-14 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 774db6c9-8779-3c14-aefe-38d25413239f | -12.85073 | -52.52298 | 2026-01-14 04:53:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c6512c1c-b1c6-3d9d-aecc-044edfdf0e87 | -1.88487 | -53.25412 | 2026-01-14 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5f049131-0f3e-39bf-9ec9-fe4b3f3ec7ee | -13.69056 | -55.68803 | 2026-01-14 04:53:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c45ba14b-a8da-3ab9-a7e2-e1080f38c136 | -1.25592 | -53.4837 | 2026-01-14 04:53:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 245ce52b-9a8b-38fc-9401-17d2a49f2759 | -1.93242 | -53.46846 | 2026-01-14 04:53:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2f290177-6e36-335d-b42c-f5a40da5aa84 | -15.59519 | -57.3439 | 2026-01-14 04:55:00 | NOAA-21 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 03997d35-22a5-3d80-acf6-052bb63f59b3 | -16.11175 | -56.75202 | 2026-01-14 04:55:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f356a47e-bb0e-3879-97a2-ddb9a19ca089 | -10.48821 | -44.92857 | 2026-01-14 04:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6a16b4c-f221-36fa-8076-b6db0a0328d1 | -19.54999 | -55.69149 | 2026-01-14 04:55:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1dbb2834-1551-3384-a29c-f5e990a8e871 | -11.85198 | -43.72601 | 2026-01-14 04:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6d86bee-140a-31d5-a5f7-dbb65b5e5ead | -21.52606 | -55.50705 | 2026-01-14 04:55:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9be2d3ba-3722-306c-a6ec-d97d946e47e2 | -10.4863 | -44.92904 | 2026-01-14 04:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65da2f3d-1fc0-3090-8d45-9cd889ddc12c | -16.59684 | -58.21169 | 2026-01-14 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 52650804-2026-3df3-a090-25fb9f2b982f | -11.85246 | -43.72201 | 2026-01-14 04:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d1e29a3f-5ede-304f-b73c-1d05a458ef31 | -19.13791 | -54.54129 | 2026-01-14 04:55:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e18405c8-1b77-3307-b7bf-836f54de8d0c | -11.85151 | -43.73001 | 2026-01-14 04:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1ee1f24-4797-3f53-a941-916a18c14adb | -11.85293 | -43.71802 | 2026-01-14 04:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c5f0c988-777c-3458-b077-f1f019809d3c | -15.95942 | -59.15667 | 2026-01-14 04:55:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed3ebf75-1ec6-3a80-80d7-5c70c7922cb6 | -17.909 | -54.13315 | 2026-01-14 04:55:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6be90398-a52e-3ee3-acdf-f5dea75ddbdc | -11.85721 | -43.7308 | 2026-01-14 04:55:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e7752c9-e40e-3b5f-93b5-860cde1c16c2 | -11.16014 | -43.57307 | 2026-01-14 04:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0822de3e-c112-33e1-81a3-8782b9281788 | -9.99872 | -45.21723 | 2026-01-14 04:55:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99c61eb1-faec-3c5f-a196-db00d272b7bc | -17.87893 | -54.86891 | 2026-01-14 04:55:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8cb7f87e-ee1c-3f5e-89d5-f5dd2b9433bd | -17.90956 | -54.12942 | 2026-01-14 04:55:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 25680622-82e2-3e0b-90cb-6d0b6e13d5e0 | -10.49145 | -44.92988 | 2026-01-14 04:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f60a49b0-dc39-32ed-b8f4-5bc669831fd0 | -16.59611 | -58.21589 | 2026-01-14 04:55:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| fa7df7a7-5920-3e8e-9105-28c92d77cdc5 | -11.15965 | -43.57705 | 2026-01-14 04:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b15d8465-8364-3cd0-ba53-18837ee843da | -19.13735 | -54.545 | 2026-01-14 04:55:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 290fd313-a8f2-352a-8109-e8af051f97df | -15.96319 | -59.15739 | 2026-01-14 04:55:00 | NOAA-21 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd421569-d861-32e2-a4b0-157c3e102879 | -22.0151 | -56.30478 | 2026-01-14 04:57:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4492686-d435-31a1-b6b7-44c78900f437 | -22.03222 | -56.30404 | 2026-01-14 04:57:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99ba01f5-fb49-31c2-aa7a-2a179ca42bce | -26.10498 | -50.17423 | 2026-01-14 04:57:00 | NOAA-21 | MAFRA | SANTA CATARINA | Brasil | 4210100 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3917f957-a4f9-38a0-9a87-f6c69a2b4be2 | -12.8468 | -52.5216 | 2026-01-14 05:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| fc85a4ac-e6ac-3e5f-9118-bf1023449743 | -1.29544 | -53.68591 | 2026-01-14 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b046327-1f56-3d52-9aa6-a25a6b0d6b4b | 4.39648 | -60.93639 | 2026-01-14 05:20:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 76578f86-d4f9-3cc9-8d61-ecc16b70b998 | -1.2916 | -53.68521 | 2026-01-14 05:20:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 99d82eca-73f5-3a74-99db-d3bcec0177ab | 0.05462 | -49.92822 | 2026-01-14 05:20:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d078d099-2ba9-36f7-93df-5d13945cebcb | 4.40033 | -60.93571 | 2026-01-14 05:20:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e79c5ef-2f16-3c67-bc69-a746ddf253eb | 0.05377 | -49.92288 | 2026-01-14 05:20:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d79dafd4-0957-3f7d-a867-608e240c5691 | -1.93629 | -53.47005 | 2026-01-14 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 727cc8a0-35b7-3e83-80ea-2f76f2846b42 | -2.14841 | -54.39411 | 2026-01-14 05:22:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e375c3b1-a9d7-3b61-a297-0624281d943b | -1.93311 | -53.46442 | 2026-01-14 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 17160e8a-1572-3f65-a5b8-683a91503f89 | -2.35985 | -51.89719 | 2026-01-14 05:22:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93cf5eea-e045-3bce-8252-03c6ab771289 | -2.52013 | -51.9306 | 2026-01-14 05:22:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bd9fc5b-dacc-3d1c-a830-26cbc290a8b4 | -1.88613 | -53.25238 | 2026-01-14 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68c953aa-5ec1-33a6-9ac7-6093938d4cb2 | -1.92444 | -53.46822 | 2026-01-14 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0ab6c1a6-b529-316c-a2d6-7df48a6d312a | -3.07534 | -52.80489 | 2026-01-14 05:22:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b26e49d-a0e0-3351-86e5-e05b3f681aae | -1.93234 | -53.46944 | 2026-01-14 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cffb9634-b22d-3cfd-b12b-d593ee0ca9a8 | -1.94891 | -53.46687 | 2026-01-14 05:22:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cfea8042-31b2-3e86-953f-7c56caf5a848 | -12.84644 | -52.52229 | 2026-01-14 05:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e9b7b373-48de-381a-9e37-bb7e81f82e0d | -13.68856 | -55.68484 | 2026-01-14 05:25:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff78f29b-c2d4-3868-b75f-4b36ab77c906 | -12.84716 | -52.51667 | 2026-01-14 05:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e2c784e8-b906-372d-8d61-9289b1588044 | -12.17564 | -58.21984 | 2026-01-14 05:25:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 679d6ff8-4d83-310b-b0a7-560ce843ba41 | -12.17505 | -58.22372 | 2026-01-14 05:25:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4d83bea6-1767-36ed-89ff-6752267fef16 | -16.09932 | -56.75499 | 2026-01-14 05:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78075e85-1bf8-3a0a-b3ce-4d81207331bc | -16.09864 | -56.76002 | 2026-01-14 05:27:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3df02266-e310-38c5-8922-0b83a76c9d7d | -21.52532 | -55.50644 | 2026-01-14 05:27:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c79064f-b5b9-3f00-83ef-447cec36b046 | -5.09991 | -43.23461 | 2026-01-14 05:27:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 6142ef9b-4404-3b65-8b65-7931ebc92ede | -16.59525 | -58.2133 | 2026-01-14 05:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| f13178e3-b5fb-315c-834a-96254e157583 | -15.96186 | -59.15836 | 2026-01-14 05:27:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b2a1ea3-6f47-38db-967a-d9d1a2e43ade | -1.29276 | -53.68591 | 2026-01-14 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 279ed7b1-7632-312d-af29-fe5bd67adbda | -1.29208 | -53.69018 | 2026-01-14 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 07130cac-f5c9-3e02-b89e-8a07b8d26aac | -16.09724 | -56.75847 | 2026-01-14 05:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 62e85b54-3bcf-3a02-9b8d-8f9e526efed3 | -16.09968 | -56.75432 | 2026-01-14 05:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 750e7573-c58d-3dbe-9dd1-d3afd9926f90 | -16.11199 | -56.75122 | 2026-01-14 05:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b156451-db32-3f72-b398-dffdf1be1dec | -16.10995 | -56.75114 | 2026-01-14 05:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1582bd1e-0723-321d-9a60-0ce803327f05 | -16.09921 | -56.75858 | 2026-01-14 05:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57c5f31c-354b-3b0c-b788-06a3668a8ed1 | -16.09768 | -56.7542 | 2026-01-14 05:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6a311710-8dca-3872-bc87-5a2c4b55cf0b | -16.11151 | -56.75552 | 2026-01-14 05:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 738b415a-cc10-3728-9d28-0e3fcd3fdc6b | -16.1095 | -56.75546 | 2026-01-14 05:46:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README7.md)
