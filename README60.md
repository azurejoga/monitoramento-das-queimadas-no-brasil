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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30de6842-3224-3044-94b8-249ebdf519ca | -3.51221 | -54.63044 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4e66fc0-d63a-312a-876f-ae9494a178fb | -3.23027 | -53.88163 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94e2d4d3-3d83-3deb-8a2c-979d88b361bc | 0.49792 | -60.60155 | 2026-10-06 05:23:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5625807-9576-3d1f-aea5-8bbdbd7f296b | -2.93103 | -54.12292 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 41a7462b-ed4c-3386-8ba2-9804f1fe6ed9 | -2.91644 | -54.10439 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6c901582-4492-3397-9a6c-d6cf8ed03e97 | -3.99226 | -56.26035 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1e36a24-ad87-3fcc-9223-0464f9d0c84c | -2.99009 | -54.04416 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0660c35-ae95-3abf-b7e3-60931595b984 | -3.51578 | -54.63486 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a16eb48-aef4-3285-b00c-0485b9eb16c3 | -2.78726 | -57.67865 | 2026-10-06 05:23:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 36253753-8e26-3e25-8607-da1ef950d9d9 | -3.57955 | -53.13055 | 2026-10-06 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f59d057-9d45-341b-89a8-e9d2fa9177c9 | -2.94928 | -54.14401 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 91346690-4fc9-3906-be3c-c4dfae55f0a9 | -3.50694 | -54.63726 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| bf48613e-0064-3e72-ad6e-b6f23f122de3 | -3.09645 | -54.17344 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7db47b4b-b724-35e7-99c5-08d26d523e4f | -2.77854 | -54.09983 | 2026-10-06 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 08d8bb97-7011-3144-b16d-a6e2a205d5cf | -2.95596 | -54.07378 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1713385c-bcf0-32a9-a054-c18e3b71b6d1 | -3.16207 | -50.44613 | 2026-10-06 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 278b0a62-f08d-3cd7-b165-fe958ad679ec | -3.84308 | -50.3078 | 2026-10-06 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 808c83f6-9cc6-3512-b78c-adb0315d5165 | -2.8869 | -54.15642 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67099f6c-287c-31ae-a7f1-55011e9e3164 | -2.95529 | -54.16295 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 75d71ed1-07f8-3717-a87c-9284624f0fa7 | -3.58839 | -54.53322 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ef1a909-6ba6-32d6-b070-26abfaaf2403 | -3.73392 | -48.87692 | 2026-10-06 05:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 3e7b1af7-15a4-35b2-80a4-8a14a0d51340 | -3.3343 | -53.39148 | 2026-10-06 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 31591746-a51e-3973-acea-070d77c10c7c | -3.08126 | -54.15863 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 36361a76-be3d-3bbb-b7c5-97479c4ccca0 | -3.09771 | -53.70933 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 67de665d-4459-3884-864a-599b88801528 | -8.64354 | -66.85329 | 2026-10-06 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 81dadea7-3f1c-32cc-b4b3-131f43c664ee | 2.46437 | -50.83968 | 2026-10-06 05:23:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 95a10d7a-3400-3ead-90de-58f9b0880068 | -2.56279 | -54.73435 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 841b4111-9f9e-3cea-b2ff-3b93ad7922b7 | -2.86862 | -54.13358 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1485e061-d8d9-392d-8ba9-74a5ae9d6b8f | -2.95108 | -54.10561 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbb4bda0-afc8-3bcf-a0e9-37e1c7531e3f | -3.12472 | -53.71141 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 732eecf9-27da-332f-ae02-d086a35f8c8b | -2.42203 | -56.53885 | 2026-10-06 05:23:00 | NOAA-21 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71d48eaf-e8ef-3f13-b114-2d0927801d22 | -3.63034 | -55.2779 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a29ea796-41c0-3647-a506-93393d5b0496 | -3.19416 | -54.09725 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81bcb343-7b45-31bb-9b0d-dab187c2cee1 | -3.05554 | -54.21565 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 4a46ac46-1921-3c11-a50d-0b8dfca4343f | -3.35073 | -59.49194 | 2026-10-06 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f9334113-1632-3249-b813-36f700208ba1 | -3.09585 | -54.17744 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8a18eeee-dba2-32f3-8875-12651b7981ec | -3.12534 | -53.70714 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41042fe0-d78f-3dd8-8e37-0359cd526c7a | -2.90301 | -54.07787 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7ba86949-e1a9-38a0-86f7-c5635abb262d | -3.12464 | -53.70919 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 54da7997-1c39-3e82-bfa9-c3e330fbd0e9 | 3.07165 | -60.57699 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7578776-a96f-3ce9-88fd-b4f40463ea94 | 3.56073 | -61.33644 | 2026-10-06 05:23:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a08fa614-2143-3eff-9e41-c94efdacfe83 | 3.07791 | -60.57225 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0edacf47-64cf-3c42-b1b3-396f9037ecf0 | -3.06191 | -54.17214 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2eb3f5da-0d54-3631-8497-f7d3f92ee020 | -3.49925 | -54.63211 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7f7bd411-62fc-3fe5-8aa7-9a77842d1c63 | -1.61439 | -55.11193 | 2026-10-06 05:23:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b759cc3-d1b2-3a43-81c9-c138cc60ed86 | -3.94632 | -55.84469 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d63c5587-b5eb-32f5-a612-25ac42ee7d06 | -3.86984 | -55.81607 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5e5c50a1-af10-363c-815a-9d5d03962b68 | -3.08068 | -54.1626 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ced62cc6-b5bd-3e62-9d37-239fbb8cb501 | -3.08646 | -54.2405 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d73a9c7d-f6e3-383f-8b9f-00dfcc85b840 | -3.44321 | -59.61968 | 2026-10-06 05:23:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f4bdaa0e-06ed-3f22-8cc5-e95410b042d7 | -2.99468 | -54.13081 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a0e9921d-b87b-3bc1-abc9-e94a6e71d907 | -2.93528 | -54.12355 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97b2b1ed-6ea1-357d-b9ca-7f3b7977e2fe | -3.08917 | -54.16395 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9daa9d2e-9e1d-3d6c-839b-9782e5a4ca0a | -3.4921 | -54.62334 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df88cc31-8323-3610-9e39-a5969bf17d8d | 2.45458 | -50.84131 | 2026-10-06 05:23:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 31.3 |
| c5b9bdb3-e80f-3ff0-9024-9e7e32dda0e9 | -3.03975 | -54.26225 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bb122bc0-b886-3b77-a2cb-fc7517b42fa1 | 3.06025 | -60.59386 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e293a078-e063-3abc-952a-f4610ae9e299 | -2.99764 | -54.11092 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e57b4cd9-a1df-3c78-a14f-b57985eda978 | 1.03338 | -59.45175 | 2026-10-06 05:23:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 597c6c4f-ec1d-3546-91d3-6e99d6534d4b | -3.72074 | -48.87981 | 2026-10-06 05:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 64178c59-3932-3d0e-87f9-90348ef4e965 | -1.72653 | -57.27248 | 2026-10-06 05:23:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 08b21dac-8fb8-3a3f-993c-646cc77a5f39 | -2.93042 | -54.12688 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d0aec3cb-050f-31d2-99cc-4dccc2f1e9d0 | -1.45632 | -60.24653 | 2026-10-06 05:23:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 839d2290-5c95-309f-807a-2b1bec032442 | -3.12902 | -53.70985 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6baea11b-4692-31e1-ad90-aa527557472b | -3.08471 | -54.25227 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| d2c3c22a-f55f-38ba-a5e1-150ad7f7645e | -4.11155 | -49.4005 | 2026-10-06 05:23:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e30ba446-db4e-3c97-8d0c-368a298c62b0 | -3.07378 | -54.23857 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 273c59a9-af7d-3def-820c-39aa9d3b06e2 | -3.31562 | -53.85418 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66b4e3c1-c220-31c4-ac58-a93d89e4f43e | -3.2346 | -53.88231 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e83fd0bf-71c5-3326-bc22-adf2e117878e | -3.49512 | -54.63143 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 223a24f1-c5e0-3660-8858-d72ab9337bf3 | -3.58617 | -54.31465 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f289ff40-6e51-3ee5-b5aa-27c5f77d7e26 | -2.87651 | -54.13885 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8167a8f2-7074-3203-a3cb-5d21fc12c34e | -3.15713 | -50.44157 | 2026-10-06 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e2e7c259-a521-3c74-80b2-84b3731be7c0 | -2.95603 | -54.15717 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 652759c6-34f1-3c84-a001-0a43e9aae8d3 | -3.17012 | -58.63621 | 2026-10-06 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47a9fdad-8fa1-3a69-af94-f6420a2c7167 | -3.95753 | -56.05444 | 2026-10-06 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 23e8473e-da61-3ff4-afba-bd11f1430df6 | -3.08313 | -54.17542 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 814e6bda-67d0-35e3-814c-87ac2801da08 | -3.0114 | -50.47366 | 2026-10-06 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8ddaa8e4-2f3c-312b-b8c7-289c1d258b9a | -1.28128 | -56.98133 | 2026-10-06 05:23:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bd830196-22d4-3713-9ad9-a5292fe24f94 | -3.09641 | -53.7179 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 795c4d51-bf8e-37d8-b352-8a65ce2e8c26 | -2.79805 | -54.14328 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e313b026-df63-379c-8326-7e571328c005 | -3.16871 | -50.43923 | 2026-10-06 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c15a7624-9513-3e80-a35e-e107e0ff40ce | -3.04211 | -54.24687 | 2026-10-06 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| feae3012-94f9-3078-872c-d7f6757790f9 | 1.81746 | -55.54358 | 2026-10-06 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8046d54-d696-30d5-93f3-48e1473e50e0 | -2.80466 | -54.12823 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f6c77a01-4b0b-3793-9dd0-76dd172e05fe | -3.27652 | -54.18755 | 2026-10-06 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c02c564a-9ee8-3c71-9f65-4108bd4c5733 | -3.06966 | -54.1489 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 01420c06-8101-3d80-8690-27ee72b70b0f | -2.78338 | -54.09653 | 2026-10-06 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bb4e1e7b-7395-3391-85eb-1e6cbca591f0 | -3.68456 | -55.96072 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3a97d94-fb80-34c2-a9bf-459c9fe7de69 | -4.05909 | -56.33304 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5157f638-66b5-3c05-9b8a-a93296836f3e | -8.99572 | -65.4017 | 2026-10-06 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7755c1cd-b0b2-3c18-a356-cc62e625f482 | -8.34997 | -62.8273 | 2026-10-06 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc26eece-681d-3413-ac9c-9eb27ddab1ef | -7.45304 | -63.55997 | 2026-10-06 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 521db7a9-4de5-38e0-8df1-66ef4259ba55 | -3.68143 | -55.95552 | 2026-10-06 05:23:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 8da21f2f-ed2a-33a5-b9a8-d4bce931c375 | -3.51279 | -54.62666 | 2026-10-06 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f22e555e-1b25-3323-afac-4e5e49c1f9b4 | -3.55596 | -59.48519 | 2026-10-06 05:23:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0bad480-1947-3c63-a6bc-fae5c122de15 | -3.0704 | -54.17344 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 83843b68-b8ae-3aca-b6c6-32c5fcf2474c | -3.05803 | -54.22813 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3ec62c2d-973e-3a9c-8f8e-bd9efdfe852b | -2.87344 | -54.13029 | 2026-10-06 05:23:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b625b09e-a708-3fc8-b8db-221e88316bc8 | -3.00219 | -57.78751 | 2026-10-06 05:23:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README61.md)
