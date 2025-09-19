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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 528419db-2e74-3b25-b4e1-38a1ca8c03de | -15.30767 | -59.42158 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b6b9425-9a16-39c3-81e9-62387c1b4379 | -15.32174 | -59.41254 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfa5da96-0af3-368f-bd59-8cb0855e0066 | -15.31489 | -59.41911 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| edaa6397-02ab-3daf-893d-9cbbe421da32 | -14.1867 | -51.39116 | 2025-09-19 05:16:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c87a00e9-a04d-3959-be00-67600eb99606 | -14.82748 | -60.24553 | 2025-09-19 05:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c73d5646-e8ac-39c3-a7d8-aef624b93243 | -14.82588 | -60.23407 | 2025-09-19 05:16:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ef0a1e6-04d0-3c2e-b1b3-ade9e2ae540d | -15.77924 | -59.38541 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3b28a959-062d-3ef4-ba4a-109e913ca4a5 | -15.41899 | -58.77635 | 2025-09-19 05:16:00 | NPP-375D | FIGUEIRÓPOLIS D'OESTE | MATO GROSSO | Brasil | 5103809 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec0f6e4c-4c60-3ed2-ba96-77c49482d4a5 | -15.03563 | -55.33119 | 2025-09-19 05:16:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b76eb86-f9ab-335d-ab7d-5dbfe91d171b | -15.311 | -59.42213 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3988176c-6990-375c-84ea-00797f69ce64 | -15.79797 | -56.20616 | 2025-09-19 05:16:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1cb74532-938c-3eea-839e-e346b4474397 | -15.77043 | -52.16936 | 2025-09-19 05:16:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 418bdfeb-d639-3fcc-82b4-6ec374ec1151 | -15.81843 | -59.46204 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b874fcc-3722-3255-99de-4c94d07d8bf3 | -16.68605 | -54.96818 | 2025-09-19 05:16:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ffe4152b-b80f-3ff9-8b65-21b2393a8dc3 | -20.34631 | -48.7878 | 2025-09-19 05:16:00 | NPP-375D | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f18c7d88-d699-3b06-a26c-fbc9ffb831bc | -17.09521 | -55.50181 | 2025-09-19 05:16:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 47161252-2ec3-3b8c-8a54-48e317108d24 | -15.27792 | -56.83765 | 2025-09-19 05:16:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0eb57478-f73f-3987-8a95-e5d55585231c | -15.78697 | -59.40144 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d410c6c1-a2ec-31b6-9494-7c0eefd85a9c | -15.80525 | -59.41557 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62ce9584-74fc-3f70-a405-b810dbd900b5 | -16.69136 | -54.95878 | 2025-09-19 05:16:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bc7c62ff-ec7d-30e7-9e7c-a4eec476f60f | -15.8151 | -59.46147 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db827f79-c769-3dbb-a526-079fb0df2710 | -15.7903 | -59.40201 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 314eb8c8-0478-3102-8a1e-2f5c6ffef027 | -15.42046 | -58.77988 | 2025-09-19 05:16:00 | NPP-375D | JAURU | MATO GROSSO | Brasil | 5105002 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d38760b-6b1e-33a0-8f83-f6e609f3673c | -21.04889 | -48.44036 | 2025-09-19 05:16:00 | NPP-375D | TAQUARAL | SÃO PAULO | Brasil | 3553658 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 30d6c68d-ce80-383b-9f7b-f2f659212732 | -21.05037 | -48.43999 | 2025-09-19 05:16:00 | NPP-375D | TAQUARAL | SÃO PAULO | Brasil | 3553658 | 35 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2b6d06f2-49fe-3f06-9abe-d88ba2f863d8 | -15.79583 | -59.41031 | 2025-09-19 05:16:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3602a16c-8e15-38ef-909c-aeb7d31e64a9 | -22.33656 | -46.76026 | 2025-09-19 05:18:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b6a04c7d-2f34-38cb-9387-f28c35e7c965 | -22.23956 | -55.97521 | 2025-09-19 05:18:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 45703880-8846-37d8-821c-8e3f6d2c0e31 | -23.13636 | -49.6442 | 2025-09-19 05:18:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 43310c6a-862e-3e73-ab29-6efdbecf78b5 | -22.92909 | -46.96086 | 2025-09-19 05:18:00 | NPP-375D | VALINHOS | SÃO PAULO | Brasil | 3556206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b7f780e1-402c-3ebb-b00a-80cf6368138f | -21.29035 | -54.81241 | 2025-09-19 05:18:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f7cfeb78-6858-3fef-b55e-543745c1be55 | -22.34083 | -46.75825 | 2025-09-19 05:18:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6ec16fb7-70e5-3c6b-94c7-a995158b4354 | -22.93417 | -46.95942 | 2025-09-19 05:18:00 | NPP-375D | VALINHOS | SÃO PAULO | Brasil | 3556206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 71c9c6c1-618a-3ccc-8acf-90e2424a61cc | -20.50205 | -56.86827 | 2025-09-19 05:18:00 | NPP-375D | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 40e5846e-929e-3891-80b8-ac63b3b64cf3 | -22.34035 | -46.7654 | 2025-09-19 05:18:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3205e570-a063-3fc1-8722-17ecc9512f4b | -22.32805 | -54.41349 | 2025-09-19 05:18:00 | NPP-375D | FÁTIMA DO SUL | MATO GROSSO DO SUL | Brasil | 5003801 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d07d7104-2db4-32b7-abd0-b0d740225a7a | -21.29136 | -54.80404 | 2025-09-19 05:18:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4e296238-a605-384b-9dfe-e68c21e2d1d6 | -20.7681 | -56.9799 | 2025-09-19 05:18:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c65bc198-6336-396d-b1e6-a8273d3eb6e6 | -21.29085 | -54.80823 | 2025-09-19 05:18:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f3695868-62e3-3ea7-9b0e-aaed79bb83bc | -21.2866 | -54.80764 | 2025-09-19 05:18:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3e321343-04ee-3588-9f15-756c1a6d2aa2 | -22.28172 | -55.97554 | 2025-09-19 05:18:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6b2745a1-4182-301e-9aed-060627e6635b | -22.28048 | -55.97453 | 2025-09-19 05:18:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e63effc3-4c1d-30f7-af10-c0b28798154a | -22.34312 | -46.76784 | 2025-09-19 05:18:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9cf51f97-813c-3fa9-ac6b-9991ead2506b | -21.28711 | -54.80343 | 2025-09-19 05:18:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 83c6d2fb-9ad5-399e-8894-b3279e8265d5 | -22.75205 | -51.40778 | 2025-09-19 05:18:00 | NPP-375D | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 5771fada-6e7a-39a9-b46b-31c4d5b5a1fd | -22.28449 | -55.97506 | 2025-09-19 05:18:00 | NPP-375D | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c48b4af-2c3f-3983-b4de-f48143748281 | -22.33605 | -46.76712 | 2025-09-19 05:18:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ca92aa8e-41d9-31aa-ad1a-d0ebd2c4106b | -23.13812 | -49.64446 | 2025-09-19 05:18:00 | NPP-375D | TIMBURI | SÃO PAULO | Brasil | 3554607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1c740a08-1be7-32df-bce8-58f1baee5bd9 | -20.79794 | -56.92738 | 2025-09-19 05:18:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 24c65dac-9133-36ad-b4a6-6e2df23ee3e7 | -22.7524 | -51.40424 | 2025-09-19 05:18:00 | NPP-375D | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 35f8300c-aab1-3987-a118-aafc28aa03fe | -22.74696 | -51.40399 | 2025-09-19 05:18:00 | NPP-375D | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2c4f1bf7-2db8-39ab-9d53-866f6aa668a2 | -22.93612 | -46.96157 | 2025-09-19 05:18:00 | NPP-375D | VALINHOS | SÃO PAULO | Brasil | 3556206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 90352be1-adf6-3bba-8713-726dea1631bd | -22.9365 | -46.95622 | 2025-09-19 05:18:00 | NPP-375D | VALINHOS | SÃO PAULO | Brasil | 3556206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9f247154-1a80-3200-8a3e-1ec4b5b1c5c1 | -22.34364 | -46.76082 | 2025-09-19 05:18:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 89116fbd-7599-3beb-b2c3-763e2a70b6ed | -25.68904 | -49.90202 | 2025-09-19 05:18:00 | NPP-375D | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f47cbe1a-b55f-3024-b8a3-cf83ab7a33da | -25.68294 | -49.90141 | 2025-09-19 05:18:00 | NPP-375D | LAPA | PARANÁ | Brasil | 4113205 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| af6787d9-4ae4-3e1a-951f-fea078965631 | -22.34745 | -46.76578 | 2025-09-19 05:18:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9687813f-c074-3b58-99db-dccbbc9a1a62 | -22.75275 | -51.40063 | 2025-09-19 05:18:00 | NPP-375D | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| f2ca53b3-cfa9-3249-9116-18104d8d3ba5 | 2.4131 | -60.70016 | 2025-09-19 05:31:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 072fa44c-9d0b-3fad-bd98-5c044bac059c | 4.44763 | -59.83863 | 2025-09-19 05:31:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7c0878a4-799c-33b3-a454-4ccc3f06a358 | 4.26304 | -60.6234 | 2025-09-19 05:31:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d374ed1-7107-319b-aade-b7d5452e71f5 | -3.94378 | -55.84753 | 2025-09-19 05:33:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 524400f8-8379-342e-a3c1-8333c2fd2569 | -3.5941 | -55.30481 | 2025-09-19 05:33:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e723f36d-f00c-3702-8fc5-0f9093243e7b | -6.32933 | -56.18114 | 2025-09-19 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2da3a61-0676-3de6-806d-0e07536d4479 | -5.30103 | -54.45932 | 2025-09-19 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67a0e32d-38c9-3bae-b6c7-09bdc22cd231 | -6.33334 | -56.18706 | 2025-09-19 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1bd0b653-4dee-3a77-8d0f-643b4b175be3 | -3.75745 | -61.20302 | 2025-09-19 05:33:00 | NOAA-20 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea3aedc8-66ec-3630-8dd2-8985f8b5fee2 | -6.33409 | -56.1819 | 2025-09-19 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d35c4fc0-399f-3aca-9370-9714adf2a043 | -5.30056 | -54.46254 | 2025-09-19 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 370fd764-7e0a-3b4c-9e69-9f8fa327afb2 | -3.92536 | -56.03956 | 2025-09-19 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 636aa4a9-d220-3806-bb1c-8b18ba1614b0 | -1.77664 | -55.50195 | 2025-09-19 05:33:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9732090f-5bda-3d96-a50b-6be978f2df74 | -6.35315 | -58.20016 | 2025-09-19 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 20a146c1-0511-3634-aebc-38fe2ec9ec82 | -2.94581 | -49.34278 | 2025-09-19 05:33:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a57d4337-3ba2-3c3b-b47c-f1c1191f473b | -2.94477 | -49.34978 | 2025-09-19 05:33:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ceced8bc-b335-3b38-be2d-1d2b4699a2c4 | -3.92605 | -56.03478 | 2025-09-19 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b09decb2-cc8b-390d-8c24-3e6b5dddc754 | -3.27657 | -49.15038 | 2025-09-19 05:33:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 052a312f-251a-34ef-a4d6-c6e01fca60a3 | -1.45689 | -55.21759 | 2025-09-19 05:33:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 72b416ba-69a5-308f-a9d5-7baea73f4d3b | -2.853 | -54.89669 | 2025-09-19 05:33:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 849d0304-c68e-3d85-8b60-be7db00fe77c | -3.59787 | -55.30219 | 2025-09-19 05:33:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9ed31abb-3abe-3bc6-a1c7-5ef00ecd9c7a | -10.43467 | -69.64435 | 2025-09-19 05:36:00 | NOAA-20 | ASSIS BRASIL | ACRE | Brasil | 1200054 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 749da4f0-bd42-3cb3-8cc0-e91f76206707 | -9.41876 | -68.87551 | 2025-09-19 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 742b058e-6f10-3647-92bc-96b4d95dab54 | -9.45767 | -63.2134 | 2025-09-19 05:36:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e13a733b-6b7c-3c75-999e-88102cb09278 | -7.68002 | -61.20039 | 2025-09-19 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53f080ad-fd06-3b4b-9f15-3b90be68f661 | -14.18395 | -51.38624 | 2025-09-19 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4b497057-1a2e-3205-a396-ea368f51f295 | -7.71845 | -61.51692 | 2025-09-19 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa9fcaa0-269c-3254-af66-766abf32a335 | -11.8109 | -57.63296 | 2025-09-19 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fdb1c084-26fd-332c-9830-e47e76e81746 | -9.19071 | -67.81425 | 2025-09-19 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5db4f075-a8e0-3ee8-b8d0-06335944136d | -9.19438 | -67.81487 | 2025-09-19 05:36:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9e6562e5-8fdf-388e-a9f0-864dcd1784c0 | -7.67988 | -61.19962 | 2025-09-19 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f2ebc83-1d66-3a62-b925-9c331e3b7b27 | -7.71495 | -61.51638 | 2025-09-19 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8997a3a2-4cc4-3c98-89e4-435f6b05039f | -10.0711 | -68.46733 | 2025-09-19 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 60dcba9a-6d74-3b4f-8aec-c744082c464a | -14.18619 | -51.39314 | 2025-09-19 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a9a8db2-272d-3e2c-9e59-5cd32a87bfc7 | -14.18689 | -51.38594 | 2025-09-19 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eff28e90-ad68-3c48-8265-318a8525a1d8 | -9.41961 | -68.87055 | 2025-09-19 05:36:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 137f958d-bdfe-3786-8962-27f40bb16671 | -9.45822 | -63.20982 | 2025-09-19 05:36:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54878757-2ad6-3184-ad68-535364405968 | -11.81557 | -57.63364 | 2025-09-19 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b052d3d-48b8-3ad9-b8b3-14dd74109afb | -9.46157 | -63.21035 | 2025-09-19 05:36:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6062e656-d1b7-32a7-92b1-a479a02c93e8 | -11.86329 | -63.11326 | 2025-09-19 05:36:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b066585-6794-31af-a94b-4ddca3ed696f | -10.07032 | -68.47191 | 2025-09-19 05:36:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07221e6f-542b-309a-bc36-763b90b3c85e | -14.1832 | -51.39343 | 2025-09-19 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |


[Clique aqui para ver as próximas entradas](README36.md)
