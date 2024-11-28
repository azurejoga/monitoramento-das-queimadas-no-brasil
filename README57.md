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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ffd3856d-f1a0-3e75-a753-375bbc76e4ca | -3.77541 | -44.11093 | 2024-11-28 04:25:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d4acdac8-2d71-375f-b986-376356ecef23 | -3.09545 | -53.256 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 49bfd699-20b6-377a-9eea-cba1c083add9 | -3.1769 | -48.43799 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f6782dd-f023-3f76-b14e-439755d21032 | -3.83645 | -51.71352 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1310c9b4-94e6-3ea8-a67a-e836a13d4021 | -4.45337 | -45.81033 | 2024-11-28 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf4a6081-8202-384c-bb3a-e2b2e565d618 | -3.22456 | -48.81872 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af8a3926-b650-38ba-ae8b-b3dec42e03dc | -2.82109 | -51.79964 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 603d5db1-6955-3ab1-8813-ba44be94c08b | -2.63635 | -51.77267 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 254bdbf1-b307-3a80-ad03-41ac5b3d4609 | -5.22219 | -44.91151 | 2024-11-28 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d6fa5c46-80f1-36f8-9216-9d2411e47b98 | -3.09934 | -53.81839 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 829b9794-1947-34ec-b322-b7115a9e2453 | -14.48892 | -50.28032 | 2024-11-28 04:25:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b8e5a53f-bed2-3739-80e0-21226931b7ac | -1.78614 | -52.74727 | 2024-11-28 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b3a3fa1c-1a06-3281-b0e3-0a8a4996ae13 | -2.94079 | -51.58786 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ea267943-053a-3d69-8198-c67d73318c60 | -3.89073 | -46.10289 | 2024-11-28 04:25:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e19da0a-ed6e-31e6-86de-5dd31f874a23 | -3.84 | -46.53256 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4aa186aa-6e63-3757-bc41-bd560fdc8b05 | -2.86825 | -46.8742 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 259cb959-a902-3bdc-93ac-b863836df2ba | -3.84407 | -50.09291 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a81e211e-76e2-3819-a2c7-975f08eee7e3 | -2.46269 | -48.57349 | 2024-11-28 04:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 510446d9-cc0a-3845-ad30-95e6281e1555 | -3.71814 | -42.29234 | 2024-11-28 04:25:00 | NOAA-20 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 04656abd-1df2-3cf9-a120-845b0e58831f | -4.30286 | -48.23645 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c9b6b9f-20af-381f-a627-d992b9fe033e | -3.02999 | -54.01838 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d38e869-1a64-3cc1-94e0-39f91d77c677 | -4.04827 | -48.33394 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 50591921-6dda-3bbe-bdae-3c26f8fc1b96 | -2.81508 | -46.82936 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfadebb6-c608-3750-be98-a855d1ba2994 | -3.94174 | -46.91712 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88e9be1a-12bc-322c-90c7-1c8ebc6e009e | -4.35412 | -50.87001 | 2024-11-28 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1be634c7-49ef-3c16-bb5b-d38eabd54667 | -3.31871 | -53.69964 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57f91539-7efd-3651-91fb-7cc9a520148d | -3.6007 | -52.54768 | 2024-11-28 04:25:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 228a6a50-9853-3f82-afb4-9fb286758da3 | -4.18156 | -48.62867 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9173a822-31d9-3b82-ac4a-511a03e031e0 | -3.04136 | -48.51372 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cce3ea79-a02d-339b-897b-543797efe91b | -3.10956 | -53.75531 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15835eba-9a03-3522-b180-fbb9b8a2325a | -2.59548 | -53.9761 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4258eada-82b3-3355-8724-698f399f18ec | -1.65389 | -55.23804 | 2024-11-28 04:25:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a1d2cd77-e70a-3772-9ab4-902d2eed38ce | -3.23837 | -48.47994 | 2024-11-28 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8e4c826-493f-3b13-94b4-e5db6c81ed55 | -3.05756 | -53.28714 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 76a56ca9-17ad-3438-b2af-c05b1da782cf | -3.18177 | -48.43043 | 2024-11-28 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1904140-547e-32cc-b9b4-3abba147e420 | -4.00296 | -44.27818 | 2024-11-28 04:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5df979bd-dc1c-312d-9665-7bab533feebf | -3.24067 | -45.37708 | 2024-11-28 04:25:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c50504ed-6524-3a54-9575-f5b11dfa01ea | -3.97383 | -46.65076 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86728a81-1b38-380b-a29a-d6b01797e78c | -3.41576 | -53.88407 | 2024-11-28 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9b57687d-c69c-3231-91a4-c22b2e0a1524 | -4.05494 | -46.61315 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 10cd2b69-e185-3be6-a961-01208943a20c | -2.9014 | -54.17814 | 2024-11-28 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8c6b6aef-331c-39bb-ba15-ee99eee8a181 | -4.51473 | -45.80943 | 2024-11-28 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 80eb92cd-ded7-37bf-80fd-3f552978255e | -3.95151 | -46.72649 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ca5531b-321a-379e-8f5b-6e339bd5f96b | -3.69164 | -51.5607 | 2024-11-28 04:25:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34a30161-2637-3467-a8fb-d69c4211a45b | -4.0119 | -46.9869 | 2024-11-28 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 092998bd-d6ba-3299-aeec-235091b883a1 | -3.45846 | -54.48733 | 2024-11-28 04:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ab0fb5a-16ad-36fa-bcea-b3db416aa9bb | -2.65522 | -49.51616 | 2024-11-28 04:25:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d333b902-19d6-31d7-90e6-e3d973bbfb62 | -3.26994 | -53.30799 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| d3a15be4-8cb6-3ea2-abbf-343228e17069 | -2.83697 | -54.07583 | 2024-11-28 04:25:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f1ada622-856d-3231-98b3-489e1afc9a6b | -5.57832 | -43.14869 | 2024-11-28 04:25:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 460cacfb-48e2-31f6-991c-4f3ff37d1b62 | -5.48138 | -44.06934 | 2024-11-28 04:25:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee281aa6-d747-3444-ae13-b0dff57724eb | -4.31244 | -48.08724 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bcb36506-26da-3840-b105-9af30d9aa84f | -2.63263 | -51.76759 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6066dd88-9fa9-34cb-aadd-21da35546fe7 | -1.79883 | -52.76007 | 2024-11-28 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f92fb332-340f-36b5-a396-5912e356d60e | -2.84521 | -46.86694 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 75b4792b-d262-3cb2-8dcc-13843c5eff47 | -3.96412 | -46.90608 | 2024-11-28 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11b7cf4b-cce7-32cf-9249-6d1298919246 | -3.26445 | -50.51867 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 476b8354-5187-3b16-9efc-b1b74f836b1e | -4.46707 | -44.94181 | 2024-11-28 04:25:00 | NOAA-20 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ddb90c6-3e6f-3335-a83a-f4f8b5995561 | -2.44227 | -50.41961 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91e958d2-c631-373f-a921-89785746e891 | -3.27382 | -50.61463 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 63c9bcce-19b5-3fab-8cf8-1f6f34a8d52d | -3.54937 | -51.51014 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 355e025f-e6db-3ac9-b63e-a320b38e4cca | -2.4738 | -50.4062 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31129b62-b925-374f-8f19-14649eca0a5b | -2.85813 | -46.87264 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| adf5b610-97dd-3cbf-9a0b-7a42393378a4 | -3.4388 | -50.01372 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08f354cd-f90f-3b98-83b7-19c741251099 | -3.84775 | -47.06377 | 2024-11-28 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1aa51e01-36a2-3a4d-a2af-00a2ed59eb90 | -3.31145 | -50.03143 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 90fad915-c2db-3a6d-8b0c-d16208989c5b | -3.08765 | -54.12935 | 2024-11-28 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c576bf81-c09f-3764-880a-08345c1ce43a | -4.05325 | -46.6851 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72de6501-2368-3201-80d4-a8edb5f35a7a | -3.18115 | -48.5731 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c47a7c61-fc8f-388d-a5f4-ea41459f3897 | -4.36184 | -48.6604 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b80ee754-5c26-3aaa-8c84-5e022b04bdc0 | -5.09778 | -45.79547 | 2024-11-28 04:25:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abf9072f-4104-338d-a69f-449ddf3abd3a | -4.31367 | -48.07958 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c9f16b63-8e36-394b-b2e6-d06e2eaca306 | -2.74379 | -48.66299 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b36f9690-3f9a-3306-9fec-ffb508ae2d8d | -3.93931 | -46.69567 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3a542c6c-7d00-30a5-a682-b94f5749e1e5 | -2.9509 | -53.71905 | 2024-11-28 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 79b4a460-c293-3e18-a6e5-ac494bf1b5d1 | -3.23992 | -51.55135 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 19f2665a-ef8f-31bb-b2b5-f6f7968622fa | -3.79953 | -46.68069 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e06241ae-f059-3ad0-93d3-8633f4262174 | -2.00134 | -51.1767 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b13b68da-7572-364d-99d5-527378419641 | -2.01725 | -52.08353 | 2024-11-28 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29474fb8-2f34-31f7-b5e5-41479d444d3a | -5.22498 | -44.91554 | 2024-11-28 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| faefc5d7-6eb2-36dc-bd06-25ec3347625b | -3.41375 | -50.16722 | 2024-11-28 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7f8e3618-f6c9-3053-89f0-17b6b06a1171 | -2.2494 | -51.87371 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 465ae4c1-e178-3071-a532-0d4b850cfddd | -3.37625 | -50.42168 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 789f12a3-11cd-3249-9715-a1b087b5a33a | -2.88722 | -50.42532 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4fb3be7-e59f-36e1-b311-8447d41b6290 | -3.22508 | -50.31899 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55cc2558-55f2-3df9-8bb0-aab48399fabc | -4.18598 | -46.61976 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b09bc807-f89c-33b3-a910-00688a2ca27c | -3.96221 | -48.08127 | 2024-11-28 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ba3de126-b180-3638-9f44-819b58c401ae | -3.20013 | -50.91422 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2f1604c3-8b5e-341d-8436-def0b470f762 | -2.93712 | -51.58889 | 2024-11-28 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a96aaaf6-1daf-3456-bb84-25bdab7f5e5a | -4.04689 | -46.85392 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef190ca7-111a-3155-9cc2-db5c96c5d386 | -3.09802 | -50.35941 | 2024-11-28 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cecf975f-2aee-351d-bebb-84f2eae1f324 | -3.56445 | -46.33961 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14345f73-0882-309b-8673-f0b2887c854d | -3.07598 | -48.66818 | 2024-11-28 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c36885b3-b389-361c-9b71-222f944475e2 | -3.71165 | -47.12695 | 2024-11-28 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28aa97eb-a48b-3353-92bf-dc1e7ebdc6d2 | -3.2253 | -45.38877 | 2024-11-28 04:25:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3dc8e4c7-9df7-3bd3-8585-5f670b3315f9 | -2.80608 | -54.1348 | 2024-11-28 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c659444-0a16-38b0-8ce9-3b84ce35a947 | -4.93194 | -45.42339 | 2024-11-28 04:25:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8e05b921-160e-31ce-8e45-7f48ee2929a1 | -2.84536 | -46.61512 | 2024-11-28 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebe994df-a6d7-3275-b52f-148b415d2f7b | -4.29922 | -48.192 | 2024-11-28 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dfda3805-41d2-3934-8181-db39e45d0a4e | -3.80621 | -46.68175 | 2024-11-28 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |


[Clique aqui para ver as próximas entradas](README58.md)
