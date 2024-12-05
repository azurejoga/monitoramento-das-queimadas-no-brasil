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
| 1e171029-572f-3f68-8889-d8e3a9606f38 | -25.19879 | -49.32207 | 2024-12-05 04:53:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 41f332bc-e8ea-3982-91e4-1ab1d7957a16 | -28.58582 | -49.44145 | 2024-12-05 04:53:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bd34c110-7ff0-39a3-b617-fdcee8a89d73 | -21.82495 | -57.04271 | 2024-12-05 04:53:00 | NOAA-21 | CARACOL | MATO GROSSO DO SUL | Brasil | 5002803 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eb2e07a8-398a-3ca4-ab9f-787eda88dd73 | -2.1724 | -54.6263 | 2024-12-05 05:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 43cd2ac2-c1f6-35c5-805f-adfc8c843ed3 | -2.17319 | -54.62461 | 2024-12-05 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8fab9c6-2be3-32dd-b0ad-a6c4bd91905e | -1.35163 | -54.96516 | 2024-12-05 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 809357bf-a63b-3e34-97f4-c7d025f6e75f | -1.44164 | -53.81525 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc4f017b-0408-3965-848f-a328ccaf18be | 0.75056 | -59.65741 | 2024-12-05 05:08:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97d78f54-e748-3c35-a8f7-adc9e63bdeb3 | 2.42795 | -60.64895 | 2024-12-05 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 150146d2-0f95-3447-95b0-34e2c77c6423 | -1.08367 | -53.45536 | 2024-12-05 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e4b9cf9-5642-311c-b3e3-67a324ed7a75 | -2.15724 | -54.61462 | 2024-12-05 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ceb3751d-dd68-3a48-bcce-0f4a0f22a94f | -1.32923 | -52.56051 | 2024-12-05 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0665cdd-3da3-39e0-a072-b2bfdf00c9c1 | -1.46316 | -54.47683 | 2024-12-05 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5995c17a-70f6-38d7-9a36-e5ca20952c63 | 0.70379 | -59.87571 | 2024-12-05 05:08:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ae86dd2-3264-3569-9dd5-a27046952e37 | -1.6905 | -52.79569 | 2024-12-05 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12a618e2-35d1-351d-bdd8-8d7282e1135b | -1.43875 | -53.81083 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8c0573a1-ffee-3f3a-af09-ad31853ae378 | -1.07252 | -62.64186 | 2024-12-05 05:08:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 86d37d6e-a631-3355-a0b7-4cf5a8952c21 | -1.14003 | -53.80423 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c008450-4316-390b-a3c2-de3e2e25363c | -2.31887 | -53.90015 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54a49a21-4f51-3aad-8f3a-b7524b943755 | -1.87996 | -53.30805 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 464eae3a-15c1-3599-b1c2-9cc3e7ca0c5c | 2.42851 | -60.65264 | 2024-12-05 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 830f2a6c-256b-37a3-9076-f3044f6924ea | -1.27821 | -52.69205 | 2024-12-05 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76bf6c92-79b0-3730-9bcd-0869e7d0b1f6 | 1.41162 | -56.07392 | 2024-12-05 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bc5689f3-7f2f-33ab-8805-a406539cecb2 | -1.17702 | -53.4326 | 2024-12-05 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35a3972f-e3ec-3c39-99c4-00fee5278122 | 2.43263 | -60.65201 | 2024-12-05 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57c920d1-c0ea-34f0-9d5f-d6dfac06a004 | -1.18176 | -53.86477 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3fb8550-5c3a-3826-bb18-85ac6ae228cd | -1.76237 | -54.19027 | 2024-12-05 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a875cdb1-1486-3904-af72-ac279906646d | -2.16919 | -54.62775 | 2024-12-05 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 38aa85b2-a7ee-30b3-958d-05be82a9cfcb | -1.75217 | -52.80407 | 2024-12-05 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0fe12a3-7f60-34cb-be0e-50156ad333c5 | -2.45452 | -53.97884 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5ca01f76-df93-395e-abd0-dd47b3255548 | -1.66764 | -52.74771 | 2024-12-05 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 622fba6b-ba98-301a-9e47-491422850c01 | -1.67134 | -52.74828 | 2024-12-05 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0131d20-5d01-3329-977e-2652226d56a9 | -2.17034 | -54.6204 | 2024-12-05 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 07c5ac97-7e5e-30a2-9398-90d2e14e7560 | -1.78674 | -52.75151 | 2024-12-05 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9dfc8440-8eb2-3f46-9444-e27287223511 | 2.42383 | -60.64964 | 2024-12-05 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 63173d43-052c-39e0-80fb-ef543ceef550 | -1.22608 | -53.76436 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2e8ec27-9f02-3ca0-92b9-d04141e26d40 | -1.61463 | -53.81737 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a8a7cf2-d11d-35f0-a3e4-22bbc1df80fa | -1.43352 | -55.43957 | 2024-12-05 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fd494117-e36d-34fa-8fc6-7094e337e884 | -2.3511 | -54.48812 | 2024-12-05 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95d7b1cf-d3b6-37bb-b2bd-2181ec33b523 | -2.37538 | -53.85967 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e74df12-c28a-3aac-8eb3-e758527c806d | -1.32854 | -52.56491 | 2024-12-05 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6082120b-435e-3e17-b332-a0a32f6378cd | 2.48181 | -60.69732 | 2024-12-05 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2aa79624-b3f7-3d4c-88a2-3ef317601599 | -1.17346 | -53.43209 | 2024-12-05 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 74ddfe06-5303-3db3-b9e5-9f71f34836c3 | 2.43207 | -60.64832 | 2024-12-05 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6154704-511c-3fd4-807a-7af44029ed1c | -1.08075 | -53.45086 | 2024-12-05 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 840730af-9d53-3ba1-a134-87f5c6cb5bdb | -1.08304 | -53.45935 | 2024-12-05 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f239d46-0e8a-3487-907e-b610fa351283 | 1.10028 | -55.96737 | 2024-12-05 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab01c9b9-3501-3693-b563-db0b322ff48d | -1.67734 | -52.55984 | 2024-12-05 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f8aa903a-b379-32a2-bc40-6f4baad4c45e | 1.12122 | -59.58301 | 2024-12-05 05:08:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c230d5af-54cb-3689-89bf-1c99b2b763fd | -1.7073 | -52.78496 | 2024-12-05 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0f216f0-68c4-37f3-8429-a0f6ec2b8096 | -2.41844 | -54.02179 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a93997b4-9845-39f7-abd9-0f31d8aa7e38 | -1.43525 | -53.81029 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d90e1ead-6a30-3d0b-b56a-9e39d17b89a4 | -1.67714 | -52.55756 | 2024-12-05 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7737c5cb-59fd-3006-ac06-60fbe9a54671 | -1.0718 | -62.64626 | 2024-12-05 05:08:00 | NPP-375D | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0d4bde8f-917c-301b-ad6b-979c36b351d4 | -2.31596 | -53.89571 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 111e36ee-9c9f-35dc-833a-6f24e485560d | -2.2979 | -53.87292 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a0f5cc1-025c-3499-885c-da22a681acf4 | -2.4428 | -53.98493 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c73ebb7-ad4d-3bd5-b502-6fc02260f4ff | -1.31756 | -55.37817 | 2024-12-05 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 51abd2bc-ee96-30de-8a81-bea56582ad5e | -2.4299 | -53.97198 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63a76dda-4aed-3634-82c2-51eccbf0cbd8 | -1.61985 | -53.83 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0833dfbd-ac48-30a0-96e3-f894afe2381c | -1.44225 | -53.81139 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 062bb1fd-7f86-32a2-a61b-1124356f9b1e | -1.25773 | -54.53923 | 2024-12-05 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3282cdad-8fdc-381b-b085-d69b2d0cf545 | -1.61041 | -53.26309 | 2024-12-05 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 338f5124-f0fd-376f-a0bf-47f4461aad4a | -1.35588 | -53.648 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9d03fb1b-07d3-3496-b289-dac48b5c2982 | -1.44724 | -54.84874 | 2024-12-05 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ddd538b-25a7-38ca-8cb0-eb5a622905f2 | -1.45063 | -54.84923 | 2024-12-05 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45a97dca-0135-34aa-bd9e-44f28648bd2b | -2.3689 | -54.44125 | 2024-12-05 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5efb5a87-d471-310a-9fef-5751b66742cc | -1.41755 | -54.52239 | 2024-12-05 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6009a739-5ddb-31b6-8fdd-5c19b0751f03 | -0.14255 | -60.86522 | 2024-12-05 05:08:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b18087fc-70a9-3af4-a066-28cae21715fe | -1.87972 | -53.30109 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93e726ab-ba01-3b05-b6cc-be2aadbd35e8 | -1.25815 | -54.53894 | 2024-12-05 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64cac39e-dbb0-39c7-80ce-39feb16b747c | 0.70452 | -59.88039 | 2024-12-05 05:08:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3c3fc41-8fa5-39a0-b4f2-f68894a04fcd | -1.59149 | -54.46237 | 2024-12-05 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68a906f0-13a6-33e6-a083-7cbf614be3cd | 2.57724 | -60.69836 | 2024-12-05 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1c228145-c5ad-395e-be42-e2ff0bcc61a0 | -2.43464 | -53.96781 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 81ec6233-0b21-3a19-b2cb-f4cdc3439d13 | -1.18525 | -53.86529 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6e9703f1-ded7-3025-846a-0bde3b359381 | 1.10305 | -55.96341 | 2024-12-05 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 697e43f9-fe1b-3b4b-8e80-c38ebc4490ba | -2.88609 | -51.58371 | 2024-12-05 05:08:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd28e7ec-fba7-39e5-9bc3-9e7c5ee4a1bb | 0.1674 | -60.59129 | 2024-12-05 05:08:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| afc846cd-876f-3ed6-b680-37fac8232875 | -1.68412 | -53.94966 | 2024-12-05 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 18c73144-a012-3bb8-9663-1a31655a4c2b | 2.42439 | -60.65332 | 2024-12-05 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e42b2368-f0e9-39b0-9abc-24504dfed5b7 | -1.62276 | -53.83435 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7cb83497-0f09-3a1d-8a2e-0b751dc9921d | -1.25715 | -54.54286 | 2024-12-05 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14a69153-5b73-3684-aa3a-78190874ad81 | -1.30354 | -54.13892 | 2024-12-05 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21ccbf98-0b91-3787-820f-371bcfc65808 | -1.03859 | -53.55762 | 2024-12-05 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 98b28d0d-cc1a-3619-a187-2dc7642b331f | -1.68681 | -52.79512 | 2024-12-05 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3532f5ed-1793-3b8a-beaf-9f90ecfb8c38 | -1.75139 | -54.19253 | 2024-12-05 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39bd219a-ae60-3524-b69c-b2e4f97dbb00 | -1.41698 | -54.52604 | 2024-12-05 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a05d27e2-6937-3449-8d46-0824962a83e2 | -2.31826 | -53.90403 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12a0c8b2-ddeb-369f-95a8-a4f020a054db | -2.41872 | -54.02487 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc80595e-3eb5-3a7a-b5c1-301658e06671 | -2.24261 | -53.69595 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f8e8d0a-a82f-3633-8c12-eba5ab7438a6 | 1.41216 | -56.07737 | 2024-12-05 05:08:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 91925bd3-6128-374e-af4d-5e9a383048c4 | -1.61865 | -53.8377 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7dcbaa2f-343d-3062-9c13-b5bfcad5f969 | 1.03282 | -59.48545 | 2024-12-05 05:08:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e9fdc104-b586-3fd9-9636-09232dd18dfc | -1.15055 | -53.8056 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32e48678-7cc2-3e5f-b8e6-03e6c628de17 | -1.25758 | -54.54258 | 2024-12-05 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e1a1c42-3a56-324a-927f-cbf362b5414f | -2.16977 | -54.62408 | 2024-12-05 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e2cef527-ca44-33d0-9c90-3697deb60889 | -2.24198 | -53.69993 | 2024-12-05 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b71988c-1842-392c-b5eb-f718b3279ff7 | -1.39375 | -60.30042 | 2024-12-05 05:08:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ff84c31-f8ee-35b5-8097-38ced1c0c3fa | 1.14929 | -59.4422 | 2024-12-05 05:08:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README12.md)
