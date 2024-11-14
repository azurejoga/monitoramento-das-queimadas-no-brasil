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
| 4114bc57-7202-3862-b495-f8e97eb2ebbc | -2.20855 | -48.39915 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c3a69ae-0313-3cbe-9a5f-8f645848befa | -1.4889 | -51.12354 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a55c0008-113d-30f9-a46f-1ee4ac572d2f | -2.92333 | -48.06844 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f59dbf3a-6708-3679-b11a-f6f1bac76465 | -1.34597 | -51.4346 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62c754a3-c2d5-3295-a23b-37cc4221689b | -4.11334 | -51.10187 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1470adca-025c-3465-a0aa-d933ee222be9 | -4.29683 | -48.1807 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48a58a34-0282-3225-8754-67e5c7126408 | -4.48627 | -48.11952 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7958dd2-44ee-336a-adfd-24c89d621198 | -4.1517 | -43.73859 | 2024-11-14 04:40:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 626d7ce1-3b92-3bb8-b0b5-c06dd02accb4 | -1.57139 | -52.02008 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05227928-3a38-3bb9-b907-c56e75eb7206 | -4.3516 | -49.68619 | 2024-11-14 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5eb3b2ba-b104-343f-8098-528b8001c2f8 | -4.38968 | -47.28284 | 2024-11-14 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b078d10-bdeb-3f0f-9640-aca6fa6767f1 | -3.10166 | -51.27859 | 2024-11-14 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c72e9d6-522a-3caf-b167-893549a8cb12 | -2.60507 | -46.17586 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6382127d-703a-3f71-8eeb-b09a6ed05b9c | -3.77126 | -41.60109 | 2024-11-14 04:40:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c9350e43-0086-3d5f-b5b3-b981d50ca6a6 | -2.11588 | -50.70018 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8411d07-965b-3e6c-aae6-bcc233d9ea12 | -1.13805 | -47.3662 | 2024-11-14 04:40:00 | NOAA-21 | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ddd7b240-3cab-331a-8510-af8e71204008 | -4.28925 | -42.54128 | 2024-11-14 04:40:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 0651726c-954d-3d32-a030-1257bf1cfb5b | -3.62882 | -48.93423 | 2024-11-14 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| da598c41-f33d-3480-923f-a8d467a61804 | -2.23634 | -48.68103 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d44aba0-7af5-3ad2-ac70-3c3ff0a71018 | -1.52752 | -47.07011 | 2024-11-14 04:40:00 | NOAA-21 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 19b76920-2388-3a9e-9b95-c976446cf61a | -2.2986 | -48.58525 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22e9f8ca-18cb-3a0e-9098-86136f67d36e | -3.02045 | -47.96905 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fba60d0d-40c4-31d3-b020-d3710187b7a6 | -2.2693 | -48.4261 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c757835c-c069-3db9-98e0-25a6082848cc | -2.25729 | -48.32922 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8b24854-b8ab-30c5-9f04-29442e4203eb | -3.10293 | -45.97425 | 2024-11-14 04:40:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6420d85-01f2-380a-9fd0-312637862f17 | -2.67349 | -46.98806 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2940578d-a6ce-3915-9429-770951c0dc37 | -1.33418 | -51.42071 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46fa76fe-65ff-3981-8979-0638ee37f671 | -2.1914 | -49.12047 | 2024-11-14 04:40:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5e19172-b7d3-332e-89bb-8e692239996e | -3.02269 | -47.97655 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5aa3a509-2b73-382e-a687-c8a4670fd0c9 | -2.09137 | -46.62427 | 2024-11-14 04:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f46d867-ab1b-3f0d-80dd-c2fb90fd0d4d | -1.5093 | -52.20141 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6e33867d-17bc-3619-b284-cb49f2c34bed | -1.53742 | -51.11836 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b659e871-c77a-3b6b-97ea-9aca3fd0442e | -2.1132 | -48.20415 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd0bb724-c8c5-3fef-b87e-a4954b202863 | -2.1582 | -50.52151 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e055de6d-7363-36e3-ac2d-ddfc311e3ce9 | -3.35779 | -46.0857 | 2024-11-14 04:40:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8de65bee-206a-38db-94b3-af97f932f56e | -2.26716 | -48.43984 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e712988-67f3-3f6d-82b9-c6b3dfd3ec4a | -1.20931 | -51.77225 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4583ae66-5a20-3ef6-bd43-40077b738acf | -2.38002 | -53.84023 | 2024-11-14 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 678a578b-1efd-385d-9d4f-03ca8db97eb3 | -4.27692 | -48.1992 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6dfe7e7a-6d2b-3b98-bb72-e705e34f49cf | -2.14606 | -46.40507 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc5d84a4-8506-3695-a4a2-76e039a3b1c7 | -5.94679 | -42.43274 | 2024-11-14 04:40:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 482baa96-4f1c-3243-900d-8ac68344d793 | -3.02323 | -47.97306 | 2024-11-14 04:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33ced025-de4a-3962-b509-2b4c83ddf962 | -4.45854 | -44.92829 | 2024-11-14 04:40:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0cc1283-af82-3bd4-8fee-021e7e50cdf8 | -3.44414 | -51.46883 | 2024-11-14 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33bb9fcb-5ac3-3488-acb3-60aef839ae84 | -3.64206 | -50.59076 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d4417b57-8235-3ac6-b1de-2aab4f303ef5 | -4.05102 | -47.22495 | 2024-11-14 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 77f0af48-93cb-3d1b-bf51-f77c3a66c104 | -4.21342 | -50.49638 | 2024-11-14 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 02527627-d1ea-3fce-833b-52ab6ccd45b8 | -1.80596 | -52.17162 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 0a412f74-34f1-3b30-94e7-bf5a382856ff | -2.56451 | -48.23252 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e220c307-8524-31c9-91bb-cf6c81c4a978 | -2.6777 | -46.82619 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6bfe404b-81c1-326a-b5eb-0eab5baaad74 | -5.00105 | -44.24874 | 2024-11-14 04:40:00 | NOAA-21 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9de6ede0-285b-36cd-92ca-6903479b55e9 | -2.79352 | -46.6444 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6043a385-e1ff-3c58-b30a-b01abd44e81f | -2.31126 | -48.46069 | 2024-11-14 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2cd1fe39-fee4-3d0c-907b-94dd964d6389 | -5.60802 | -46.40085 | 2024-11-14 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 53ce6c81-12ec-31f6-a525-318aec9881ec | -1.38822 | -51.12405 | 2024-11-14 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0d4d4971-5bf7-3d7a-bc74-d6602c7a575f | -3.45151 | -42.54644 | 2024-11-14 04:40:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c3824867-5373-3258-94ec-bb1e1b85f393 | -2.70178 | -51.87069 | 2024-11-14 04:40:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40ca86a5-0234-3e08-a52e-c78fc75d6ea1 | -1.55572 | -51.85674 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fbd9da12-4be9-37b1-ba69-493fbe7c5451 | -3.90394 | -50.08894 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 62ffefd1-3b7f-301c-a5e0-d6babb08cf97 | -4.05487 | -51.02794 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 029c97b9-47d9-302f-932d-ed6b55ee3cc1 | -3.042 | -50.33157 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dee1adf7-81ae-3b7a-b1e6-61412042948c | -3.71688 | -50.60955 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 9d65d2a9-59d5-3ed3-982a-ee4264964df2 | -3.95148 | -46.70546 | 2024-11-14 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 118334d8-ddf0-38da-a4b7-07e55066c2e8 | -2.12491 | -48.89206 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 63ba7ed6-a8e2-31f8-a6b5-8e0663e1786a | -4.29241 | -48.18721 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6619f9b5-0e7e-39b4-b3e7-15a5d585eb73 | -2.56112 | -51.23206 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5a80016-dc4b-3a1d-a36f-a68eab21845a | -4.1352 | -51.07471 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a54d12d-8a4f-3d79-941e-cc98e03ff7df | -3.62936 | -48.93079 | 2024-11-14 04:40:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 55974eba-39ce-3d35-8323-17b8f560f367 | -1.61425 | -52.40561 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 501af3d7-e00e-3e81-93ae-179d48ba19e6 | -4.68888 | -48.74375 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d55162c-5bed-3612-9bf4-302b3ed913ee | -2.61212 | -48.21161 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 73d6c43d-2286-37d4-922d-6e348854bfa3 | -3.94799 | -46.70496 | 2024-11-14 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73a10aa3-57ad-37f0-8e92-5d7d807b1e39 | -3.27326 | -50.57405 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ddd8ea05-9cd7-365e-8b3d-e8fb7c4dc4e3 | -1.33495 | -51.41228 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31de07e9-64f2-30e8-a0f3-c295138a29f8 | -3.16575 | -50.58736 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 38d6617b-2103-3e64-a063-006737903c4e | -4.43594 | -47.54861 | 2024-11-14 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d33b1a7-ca2f-3dde-879e-482210c73d51 | -1.60679 | -52.49417 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a9148a87-e387-33dd-bd33-22d38bd46e7e | -2.27437 | -51.32029 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22792b56-95d2-3bca-bbb2-b0c7cac4f769 | -3.04873 | -50.33261 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc3734c2-11df-3f8d-ada4-a34ae238888a | -4.40206 | -49.77539 | 2024-11-14 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3bb89ae-609d-3576-af5f-b4c6c501f005 | -5.56215 | -45.36904 | 2024-11-14 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2ef630b4-647d-3362-8750-93cd8b594005 | -3.2693 | -50.57714 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8630d062-6e0f-3fc6-9690-ad4a619ed17e | -2.12437 | -48.89549 | 2024-11-14 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bcd60dcf-7f43-3950-bf9d-927d5c625a99 | -3.40613 | -50.28967 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 447db690-d92c-3df6-a0db-d52266282b33 | -3.29659 | -50.22913 | 2024-11-14 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2c186a8-1ff1-3581-ab34-526509801c85 | -3.27235 | -51.26946 | 2024-11-14 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a943cd24-d89d-3d6b-8000-0ca4dd29d25d | -1.56067 | -51.84887 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5cbf99a-ac44-3fd3-b691-8c89dc0a2703 | -3.27936 | -50.06004 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3560f4ee-779a-354e-b13d-614202a6645b | -1.84568 | -46.28279 | 2024-11-14 04:40:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eace06ba-3f29-3b5a-b721-fd0ce4675940 | -2.11647 | -50.69647 | 2024-11-14 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd30fee3-885e-3bb2-b37f-5f17cf2ecf81 | -2.89547 | -46.84744 | 2024-11-14 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7732c00e-aa8a-331b-8c43-1dee1310c651 | -1.40012 | -52.3847 | 2024-11-14 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f34c392e-65fc-3ffd-809a-93d732e0841b | -4.15549 | -46.244 | 2024-11-14 04:40:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 05a60f3d-8d05-3a6a-9440-7b268ae31887 | -4.44498 | -49.58754 | 2024-11-14 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 193971db-b6b0-33a8-93d9-644d299cf71f | -1.36665 | -49.12863 | 2024-11-14 04:40:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed912b4b-47e6-318c-8ba1-74db4e6148fc | -1.61135 | -52.2433 | 2024-11-14 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 456a3141-ffcc-32be-b01a-a0d7ac1c4088 | -1.21064 | -51.76387 | 2024-11-14 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e67e300b-e94b-32bc-8017-25c8120a3de2 | -2.88603 | -48.28617 | 2024-11-14 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c758c51-de1a-3419-9e53-d6e36a61f5d9 | -2.62552 | -46.53042 | 2024-11-14 04:40:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d95ea52e-fb4c-3a1f-afbb-319cde2369a9 | -4.55775 | -48.01113 | 2024-11-14 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README27.md)
