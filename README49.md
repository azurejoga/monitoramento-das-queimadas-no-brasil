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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bef6d8ad-13ae-3f55-87c1-bc096a8a8422 | -3.69462 | -51.36909 | 2026-09-27 05:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a20bd4e5-5b74-38bc-99cd-a3fc60ade490 | -3.1935 | -51.04419 | 2026-09-27 05:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a9e234e7-4842-3bc9-82fd-fd31eb6103e3 | -3.71635 | -54.65802 | 2026-09-27 05:48:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee08cc84-1fed-3447-9e7a-1741bae37b7a | -3.19748 | -51.04036 | 2026-09-27 05:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 36b28db2-f016-39de-ba3b-16c7024f9141 | -2.97266 | -54.14929 | 2026-09-27 05:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af2fa475-b967-3ebb-8394-c81e51215bba | -3.21998 | -54.325 | 2026-09-27 05:48:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 365501ad-6fa1-3d58-8c43-824253b0a6a7 | -3.2968 | -54.69395 | 2026-09-27 05:48:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2b1bebc7-9c3e-366e-97d0-f9f8247c348a | -3.29734 | -54.6902 | 2026-09-27 05:48:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce7ecba5-8780-3f13-985d-77bdf5803ea6 | -3.71118 | -54.65327 | 2026-09-27 05:48:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9f30aa78-1857-3fef-ba3e-81910a60d264 | -3.22643 | -54.32176 | 2026-09-27 05:48:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db334232-b735-339a-b7ce-46f99b4ed10a | -3.69898 | -51.37481 | 2026-09-27 05:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| db367ccb-8cea-36bc-8f11-963b3b9d5dcc | -3.01142 | -54.21151 | 2026-09-27 05:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12d5cc1e-4a14-306a-8fdc-0d92f4f47148 | -2.66658 | -56.4613 | 2026-09-27 05:48:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44cd8a39-dc53-3c9b-b048-c5a5121b48f8 | -2.67202 | -56.45921 | 2026-09-27 05:48:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 51f370ab-1537-3768-a56e-484f6a84faac | -2.79228 | -57.69851 | 2026-09-27 05:48:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 41267c37-bb5e-362d-a368-53d39241e7b0 | -2.97848 | -54.15053 | 2026-09-27 05:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1261da4b-326d-3b21-b224-a6752750d8e6 | -3.19458 | -51.03692 | 2026-09-27 05:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6a683298-1f76-314d-8f5e-4f605a52ade7 | -3.20063 | -51.04514 | 2026-09-27 05:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| df825933-8bf8-3f9f-a809-c768e78015f6 | -2.67158 | -56.4621 | 2026-09-27 05:48:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 51aa42d7-3613-36be-9806-c8bd928eeee6 | -1.83552 | -54.72344 | 2026-09-27 05:48:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 38b910ba-a88c-3e3a-8232-b22e1d93410a | -3.19034 | -51.0394 | 2026-09-27 05:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bb7bc45d-cb43-3299-b821-45dca63f556f | -2.78767 | -57.69782 | 2026-09-27 05:48:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 37f0ff07-53d3-37be-b5fb-5aab1a9bed78 | -2.05605 | -56.87233 | 2026-09-27 05:48:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 796e7644-4e01-321f-8880-dbf1d7ab8089 | -2.79156 | -57.70326 | 2026-09-27 05:48:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1e70a9d6-32ae-3f87-bed6-8d74bf24d434 | -3.70063 | -51.377 | 2026-09-27 05:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5e020165-d7d0-30b3-83a4-2a7ef5d9ce21 | -3.0108 | -54.21568 | 2026-09-27 05:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15d01015-ef83-3578-a2da-33381491cbd0 | -3.19845 | -51.0336 | 2026-09-27 05:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| c1b8b91c-b5f7-3cba-bd6c-0fde690f7428 | -3.69362 | -51.37579 | 2026-09-27 05:48:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60f65ff6-1d5f-3571-80d9-991c0a25d7b9 | -1.84166 | -54.72058 | 2026-09-27 05:48:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 26f16180-e68d-3424-a4a1-87cc0b268b2b | -3.22458 | -54.33405 | 2026-09-27 05:48:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1182ad27-c501-3701-bbab-4b20b56c7d3c | -3.30052 | -54.6956 | 2026-09-27 05:48:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11c49695-f60c-32e2-9519-df4104b9464e | -2.05685 | -56.86712 | 2026-09-27 05:48:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2678eaf7-a4f0-321c-beca-70e2c3cd65c0 | -2.66702 | -56.45841 | 2026-09-27 05:48:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89b772fb-8267-3b7e-84b7-57c35bfd2556 | -3.0062 | -54.20638 | 2026-09-27 05:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c5ac75c-8be6-3fba-935e-2cf3f33e227e | -2.79617 | -57.70395 | 2026-09-27 05:48:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a34e778f-5c55-339e-bfce-d798d95c35c0 | -3.2252 | -54.32996 | 2026-09-27 05:48:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ad057cce-1dc3-3c51-9e4f-fbb41e7ebf98 | -3.00559 | -54.21045 | 2026-09-27 05:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b515c0d5-c2f6-3501-b24d-7e1d71811ad4 | -2.79689 | -57.69921 | 2026-09-27 05:48:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 528a422d-285f-32f4-8b2b-af67d6db431b | -2.06168 | -56.86784 | 2026-09-27 05:48:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c0ec51e0-a4be-3019-9b1c-ee3c1d6a46ce | -2.06571 | -56.87378 | 2026-09-27 05:48:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f01208d0-af52-3cb8-9446-5cbd17dda895 | -3.22581 | -54.32586 | 2026-09-27 05:48:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a469b9a-a381-3daf-881d-5b68ddd26944 | -2.78695 | -57.70257 | 2026-09-27 05:48:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 575aaf77-f876-3889-ba0e-e8d26a956e95 | -4.7135 | -55.71885 | 2026-09-27 05:48:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d0189c5-03fc-36f2-9ed7-4808144c65de | -4.3606 | -55.28217 | 2026-09-27 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6441331f-8697-328b-8abb-ac0315420e83 | -6.07743 | -57.81806 | 2026-09-27 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9ee09f35-fee0-387c-a7d9-f46aeaf3e299 | -5.16298 | -56.00924 | 2026-09-27 05:48:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4748e2d7-39b3-3fd4-9f3a-ccd9fb97ebd1 | -6.12875 | -53.04951 | 2026-09-27 05:48:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d394ba60-2875-345e-8d14-8eeef898340c | -3.82776 | -55.91389 | 2026-09-27 05:48:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 67fd337d-32fd-3b36-85b7-75cf8c30b915 | -3.68815 | -60.54451 | 2026-09-27 05:48:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 032e4356-9218-37f2-8620-eb670b03dfdd | -3.8478 | -55.81556 | 2026-09-27 05:48:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5932edd8-93bc-3cf4-a083-17165dd17b80 | -4.23707 | -55.16241 | 2026-09-27 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45566486-8d9f-3b02-975f-79343fe44e1e | -6.13455 | -53.05618 | 2026-09-27 05:48:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 563ea93d-d379-34e5-9f30-3b9e294c893e | -3.96358 | -59.34582 | 2026-09-27 05:48:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 88d23893-5611-3cc5-9cd5-aabcac9a182f | -6.07253 | -57.81348 | 2026-09-27 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b39daf8-aa04-350c-871d-ec619503fdb9 | -6.06073 | -57.82769 | 2026-09-27 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6458b0aa-ecfe-36bc-b10e-42c9d6be2bc7 | -3.83306 | -55.91468 | 2026-09-27 05:48:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7862a70e-fe75-336d-9e60-6eb48f2feecb | -6.1338 | -53.06174 | 2026-09-27 05:48:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f15491a3-5134-3bbd-b035-4e3302417b6f | -6.0883 | -57.63017 | 2026-09-27 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e73d7acf-d2a1-38ad-8bbd-ba4a1b82f232 | -4.28592 | -55.25723 | 2026-09-27 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 51c98aa2-ae27-3afd-92ad-c46965a06d67 | -4.5408 | -54.98174 | 2026-09-27 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f66e6697-eba6-35b7-9448-1f8d0a0ffebd | -6.86515 | -59.87698 | 2026-09-27 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe7265a6-2eda-3416-95ca-35f5347a7791 | -6.0906 | -57.6291 | 2026-09-27 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bf3eb623-ef91-3851-aca9-b38339a70b62 | -6.86659 | -59.89695 | 2026-09-27 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5835bf00-2595-33e0-ab25-75c768794fb8 | -4.49299 | -54.95049 | 2026-09-27 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 5419b00f-5a80-3439-bacb-985fa7cc63cc | -3.96836 | -59.34262 | 2026-09-27 05:48:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25b77653-8199-3808-9148-6e10b4acdbf0 | -4.51116 | -54.94574 | 2026-09-27 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a34efbae-d01f-34d8-8281-84fa34bcdd91 | -3.82825 | -55.91061 | 2026-09-27 05:48:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 516f6804-3edd-333c-a418-9c985aebc834 | -4.09576 | -54.32931 | 2026-09-27 05:48:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7d5a5a7-38fc-362b-8ae1-52f73bb909e7 | -4.29024 | -55.25717 | 2026-09-27 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fce02aa8-cc3a-3c91-8c8f-742a244db1ac | -6.07732 | -57.81433 | 2026-09-27 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91ad3bd2-dffd-3c37-8cf3-4da4ae111a2c | -6.63908 | -59.94874 | 2026-09-27 05:48:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a8fed5b9-feab-3f1f-be3f-076c5bce85c2 | -6.09242 | -57.63628 | 2026-09-27 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 04a2b4a7-7591-32af-88b3-e8018d0173f7 | -4.49922 | -54.94772 | 2026-09-27 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c36e99dc-3679-38a8-8fdb-29d9c73338b5 | -5.16882 | -56.00668 | 2026-09-27 05:48:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93010ffb-18ca-3393-9df7-eecd702741fb | -3.44532 | -59.74474 | 2026-09-27 05:48:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| df7b2629-5268-38fc-8e00-eddcc4a3216a | -4.54027 | -54.98537 | 2026-09-27 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1d36bccc-0270-3515-946f-389d77ef32b8 | -4.36112 | -55.2786 | 2026-09-27 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef80c478-bac1-3d53-8350-9942255a4813 | -4.28465 | -55.25648 | 2026-09-27 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a40734b-109f-311b-ad36-e5db8b857dcd | -6.06553 | -57.83215 | 2026-09-27 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 716ee940-f4c9-3413-b0be-78dcd02ae7c6 | -3.83933 | -55.90892 | 2026-09-27 05:48:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 71725fab-3c29-304a-9166-76d83b200948 | -4.54285 | -54.98104 | 2026-09-27 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e8fefa3d-f96f-3eeb-84d8-e58fb9ad144f | -6.06863 | -57.81123 | 2026-09-27 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3df0cd2-272a-3b04-ba14-03664eed0c7b | -5.16341 | -56.00616 | 2026-09-27 05:48:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd55dd92-7d8c-3802-a563-9d17dcc1718e | -4.50549 | -54.94466 | 2026-09-27 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c8519f29-ad02-3cd0-b1be-e09b6cc629e3 | -5.16386 | -56.00304 | 2026-09-27 05:48:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85173b1f-fa52-30cf-a315-29019c9e2d53 | -4.36007 | -55.28573 | 2026-09-27 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74d765b0-57d6-3ed7-a3c7-eeaff998a1fe | -4.49244 | -54.9543 | 2026-09-27 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 13ccdc3c-853b-37af-861e-6f210c2f650e | -4.09636 | -54.32506 | 2026-09-27 05:48:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62e30811-e1a5-3cc5-8866-e3421626e9b1 | -6.87782 | -59.87883 | 2026-09-27 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 027c12aa-158c-347c-ad95-0354873489c4 | -4.49353 | -54.94675 | 2026-09-27 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 643a0a0c-1290-3814-bf88-17f7dc9ebb50 | -6.09316 | -57.63093 | 2026-09-27 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 98d527f4-cf84-381e-b228-6175ee12e80d | -4.28648 | -55.25344 | 2026-09-27 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63744e55-e1ba-3a35-b341-8b0ea79c55bc | -4.56434 | -54.95257 | 2026-09-27 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 808e35e5-8cb5-33bc-9751-db3dc3e3730e | -4.54234 | -54.98465 | 2026-09-27 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6b763b9d-6dac-306e-acbb-7fa1eedd30b1 | -3.96777 | -59.34645 | 2026-09-27 05:48:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6282b924-839d-3820-9bf8-b3b4f0b869b2 | -4.50434 | -54.95257 | 2026-09-27 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6a5fff11-e30c-34ef-adbb-483b80bb3403 | -6.86237 | -59.89633 | 2026-09-27 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7b462ad4-94ee-3cc3-99ac-90fa36091e30 | -6.87416 | -59.87432 | 2026-09-27 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d61cea48-0841-35b5-be34-61b1fbf3b3b4 | -3.44937 | -59.74537 | 2026-09-27 05:48:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce6ed71e-caa9-3e8e-9ce3-27e777cde3fc | -4.36514 | -55.28994 | 2026-09-27 05:48:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README50.md)
