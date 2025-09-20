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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 387ab08f-de1a-32ff-aa2b-e0352922e113 | -2.7941 | -47.14829 | 2025-09-20 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5c9b7e5e-90ee-3fa1-866d-e3601799a3fb | -2.78741 | -47.1518 | 2025-09-20 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e876db92-1ef5-3331-8bef-9320609fc34e | -3.72822 | -51.35664 | 2025-09-20 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e6c920d-3035-35aa-a2a3-c70b6bb495aa | -2.82976 | -48.66216 | 2025-09-20 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e62d55ba-3555-3c1f-8932-a64a06b0fe11 | -3.344 | -48.39144 | 2025-09-20 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc80a3f7-1686-3041-8baa-89a26690b6f5 | -2.43565 | -49.33868 | 2025-09-20 05:14:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3f58e347-512d-3342-8cc2-cfa0a63dabe8 | -3.34344 | -48.39517 | 2025-09-20 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0bb771d9-507c-3fc6-8736-3386393fedbd | 2.41434 | -60.70133 | 2025-09-20 05:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 535f81b7-f8a9-3a7c-bdda-d71c73d4b1f3 | -2.43093 | -49.33476 | 2025-09-20 05:14:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e1c049b5-32d8-3d40-84bf-aa9e484e16dc | -2.98977 | -49.29242 | 2025-09-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f764d707-94a3-3d01-90a6-84ce7cbacf77 | -2.98698 | -52.62563 | 2025-09-20 05:14:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d18daa8-27fc-3f0e-ae4e-f3bdd29ed29d | -2.7994 | -47.15399 | 2025-09-20 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e2a3a19a-25f3-3bc8-bd8d-c7fc04475f0c | -1.11756 | -54.09229 | 2025-09-20 05:14:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f7c62e7-7442-397f-ba99-49781f2cb9fc | -3.3496 | -48.39229 | 2025-09-20 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47f544cb-9630-3881-ac89-4ba754a82da2 | -3.34904 | -48.39606 | 2025-09-20 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| deff1e42-5e5a-34c6-adb1-b0d9caf421e2 | -3.45959 | -51.21275 | 2025-09-20 05:14:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 6b2775ee-5493-3566-a791-6b1cbf69d9e3 | -2.79272 | -47.15746 | 2025-09-20 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 22f15575-8fc4-30e7-b477-09a5351c3c77 | -1.11514 | -54.0938 | 2025-09-20 05:14:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8fd7a088-caea-3520-9b0b-f3704e4d813b | -2.98642 | -52.62941 | 2025-09-20 05:14:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9b4645fc-5d82-3eb2-9aa6-f98033477014 | -1.17065 | -54.14092 | 2025-09-20 05:14:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 69df133d-9843-323e-8654-04f023ea36a1 | -3.51376 | -49.44862 | 2025-09-20 05:14:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5bf6875d-aa23-31be-9d52-2d4aba7351bf | -2.43047 | -49.33788 | 2025-09-20 05:14:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 02ddb008-ebc7-3436-a145-ad44f322c05c | -2.83065 | -48.66212 | 2025-09-20 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2fc4d58-4b08-35fe-91df-ddba81c345b7 | 2.41539 | -60.69827 | 2025-09-20 05:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e128fac3-c432-3ec2-8ee8-5bc9a6778b76 | -2.79341 | -47.15285 | 2025-09-20 05:14:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b21b2720-1658-39b0-953d-3a8d9d1fa39c | -2.14584 | -53.65063 | 2025-09-20 05:14:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e8241a9-1ef5-3cc5-8ddd-a2bd145fd8d8 | -2.83117 | -48.65857 | 2025-09-20 05:14:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73fe434a-2306-3c8f-b2de-5c9ca3893863 | -2.98929 | -49.29564 | 2025-09-20 05:14:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 92e69220-67b5-3b97-a088-ca3896a7e7ef | -9.40666 | -54.68907 | 2025-09-20 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd53096b-8928-3831-8093-ca6332dde9ee | -9.8426 | -59.88092 | 2025-09-20 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 88b67d93-3915-3bd8-9821-da49658a3183 | -9.41346 | -57.03586 | 2025-09-20 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b47cc7d-79a5-3067-8f4d-4f18a2486ef1 | -9.77023 | -62.32743 | 2025-09-20 05:16:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 38fa9405-9188-39bf-b83b-613d0986c22c | -9.39418 | -54.69082 | 2025-09-20 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01d6cdf9-01ad-35ff-bca3-d48236742924 | -11.28727 | -47.4142 | 2025-09-20 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42d2e3c0-bd3f-39f8-8434-2af08663f679 | -9.83593 | -57.8268 | 2025-09-20 05:16:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c832247f-2805-3f79-9f02-040253c8f7aa | -9.36334 | -54.52374 | 2025-09-20 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8effce4d-a9b0-3717-bda7-cbc3fb656b76 | -9.45482 | -60.48419 | 2025-09-20 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5adef20d-297d-3299-925f-66f0863db078 | -9.40267 | -54.68846 | 2025-09-20 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ef48c71c-83ca-3495-9bee-c1d509a698da | -9.46777 | -63.37661 | 2025-09-20 05:16:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 438175a2-10e5-31af-8d1d-bd4c3d52aacf | -9.35478 | -54.52589 | 2025-09-20 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 382fadac-8fef-34e7-8fbf-31acd4ed03b3 | -9.40935 | -57.03925 | 2025-09-20 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c98d82ee-e3a1-3eb5-9505-351c9bde1263 | -7.83718 | -45.6433 | 2025-09-20 05:16:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cf70e013-729a-3df0-bcd9-c34bc87ea5a9 | -5.04051 | -47.90681 | 2025-09-20 05:16:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adee4ed8-1991-37ce-b76e-d64e855d2d4b | -9.40876 | -57.04317 | 2025-09-20 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2551187-e65b-3521-b70f-ffecd8e3c31f | -5.80765 | -53.44245 | 2025-09-20 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50ed29da-b14c-316a-b30f-50532c5882a3 | -4.66596 | -49.33287 | 2025-09-20 05:16:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df134ac4-ab81-3401-8cb4-39d6c119bf8b | -9.39917 | -54.68435 | 2025-09-20 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a44717e-f235-35d5-a38d-2a16a665e9e7 | -4.47944 | -55.08753 | 2025-09-20 05:16:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 858dfb4c-a8a0-30f1-8ee9-ba9b8de35f4c | -10.0305 | -59.35646 | 2025-09-20 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c73ec7ba-e027-3a09-87b2-e65e96358664 | -9.35529 | -54.52239 | 2025-09-20 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 113909fc-9c29-3185-af5e-09037ea1607b | -9.82691 | -60.74839 | 2025-09-20 05:16:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e990587-b2e7-3494-9c24-c31cb1b073f6 | -9.35931 | -54.52308 | 2025-09-20 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 51cae12e-0f3f-3bd9-a7b2-8bb737de3344 | -3.43628 | -59.72722 | 2025-09-20 05:16:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9cd3e310-c721-3714-96ce-196092721f35 | -9.81761 | -62.30275 | 2025-09-20 05:16:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 23bc1ddf-bac5-384a-98a0-b640f52e8e92 | -9.90429 | -59.5975 | 2025-09-20 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8992b681-d66e-3824-a986-731e1208d847 | -2.69251 | -59.42397 | 2025-09-20 05:16:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7569e0e5-8e45-3e0a-b68a-6171a174e81c | -8.70281 | -64.20853 | 2025-09-20 05:16:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ac29704-e816-3ba4-8510-d5c5e3253a96 | -9.71754 | -62.16094 | 2025-09-20 05:16:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 56eba96b-5222-3d11-b5a5-58c12f2df6cc | -7.82885 | -45.63502 | 2025-09-20 05:16:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2d741e50-ed4e-3d7a-81bc-5b6ab6bb457d | -11.21225 | -47.36575 | 2025-09-20 05:16:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a9e1a77-b1bc-3ffb-ac4e-a453ea1e06ed | -9.40217 | -54.69198 | 2025-09-20 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e9a4951d-e6fb-3835-ac40-43c1b56167d5 | -11.27407 | -47.41222 | 2025-09-20 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f6a76c27-cdcc-3e1d-ad05-fa4b7f3ec125 | -9.1865 | -62.52497 | 2025-09-20 05:16:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1d42bece-d432-3595-bfff-e4e1d60f4f86 | -11.27826 | -47.4138 | 2025-09-20 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3c5e1c3-7c9f-3518-9335-87112d28a3c1 | -7.83486 | -45.64431 | 2025-09-20 05:16:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| feb15bb7-841e-3b81-a3d3-b9167b11402a | -9.39817 | -54.6914 | 2025-09-20 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 99fbbe71-b990-351b-b27b-5010c4c90b46 | -4.28064 | -55.7505 | 2025-09-20 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c084cdf-117c-3cf6-b3ca-cdbdc3f7792b | -5.5331 | -60.21144 | 2025-09-20 05:16:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5a6b79b-2f09-38c7-85e1-29ff33ba0652 | -8.1963 | -49.67074 | 2025-09-20 05:16:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ba414b1e-7a49-313a-9baa-298d5ecc27fc | -9.65675 | -62.26807 | 2025-09-20 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0fb0cd1d-110e-3dcc-9214-1692f85cff8a | -9.39368 | -54.69437 | 2025-09-20 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac83d7f8-d013-35a0-a299-adf894171923 | -6.10664 | -47.85542 | 2025-09-20 05:16:00 | NOAA-20 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dcefb0ca-a5ef-3ae9-9c7b-39ee08cc6d69 | -6.35285 | -49.8591 | 2025-09-20 05:16:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6093a9fb-e567-3eac-b38d-9dd9482aea47 | -2.69531 | -59.42805 | 2025-09-20 05:16:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e050d8c5-ddeb-30df-bbdc-97511a6bd696 | -3.43233 | -59.73029 | 2025-09-20 05:16:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 91f843f9-5158-3e39-9203-142bb5c20a4c | -9.41356 | -63.69687 | 2025-09-20 05:16:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 13e25db9-6efa-38d2-a0a6-c1027f1f4925 | -9.1858 | -62.61813 | 2025-09-20 05:16:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72e0583d-8b69-3de3-b753-24d6957386ae | -4.25804 | -54.84464 | 2025-09-20 05:16:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3f15ef5-c23c-3677-baec-a1bcbe376f7a | -9.66026 | -62.26862 | 2025-09-20 05:16:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3cb4f7e9-1f29-330a-b41a-664ddcfa73ea | -4.66644 | -49.32952 | 2025-09-20 05:16:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3876472a-0d0f-3a51-9194-aabe56993737 | -11.28067 | -47.41323 | 2025-09-20 05:16:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 569e2c9b-e585-3cad-8936-9b706bb81184 | -4.28003 | -55.75447 | 2025-09-20 05:16:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb5dae18-c722-3395-b776-79dd79dd29ee | -9.41406 | -57.03188 | 2025-09-20 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d72f0aa7-fca5-37e1-b7ab-800f06ba0d97 | -9.40817 | -57.0471 | 2025-09-20 05:16:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dfe05ca3-20b0-3873-a2fe-a46522705619 | -9.45242 | -63.49028 | 2025-09-20 05:16:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c98a700-f683-30c4-81af-e185d0ef8f30 | -11.20561 | -47.36491 | 2025-09-20 05:16:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bbffb4cb-97bb-3898-8bc4-ade5d971740d | -9.84205 | -59.8844 | 2025-09-20 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ddb81eaf-bd74-38b3-9c1d-cc8cba8d9184 | -8.17132 | -55.17377 | 2025-09-20 05:16:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41c9a818-dd17-373e-9a79-b355d6692f24 | -3.2089 | -58.1401 | 2025-09-20 05:16:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cfdafaff-47fa-386a-a7a1-dd061c5b3a4c | -10.73523 | -55.52153 | 2025-09-20 05:16:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b11be77f-05af-3727-89f4-0e6f73e17da2 | -9.90374 | -59.60099 | 2025-09-20 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf3f5dc9-6725-3193-9dfa-9991942baa94 | -3.59371 | -55.3033 | 2025-09-20 05:16:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cd6b81ff-d8b0-3398-b6f0-e472f0f0f0e4 | -9.90043 | -59.60046 | 2025-09-20 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1715d7b3-b58e-3f00-9849-2950020deb0d | -9.18648 | -62.614 | 2025-09-20 05:16:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15a0591b-726d-3516-8790-f4051882aa8e | -5.81345 | -49.85035 | 2025-09-20 05:16:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 42574a9e-d46a-3e98-9e75-af141d7d32a7 | -9.40716 | -54.68558 | 2025-09-20 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aacbbaef-2175-3dcf-be17-7cde0cd482bb | -9.45538 | -60.48066 | 2025-09-20 05:16:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 22fe4c33-f95e-3434-8df3-b750a0cb6787 | -9.3917 | -54.70832 | 2025-09-20 05:16:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb53b858-3ae6-343f-9445-8a35411d40cc | -5.69437 | -51.74426 | 2025-09-20 05:16:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd5d77d9-63f8-3951-9779-bedf386b2d09 | -3.11928 | -59.38866 | 2025-09-20 05:16:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README27.md)
