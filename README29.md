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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 129c7bbc-e5a8-32a3-8a91-51343cb2efd6 | -1.43796 | -53.38621 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2081082d-8e5f-3726-9151-3a97e5e97428 | -3.04221 | -54.40348 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 83fc2239-c5a2-3944-ba67-a3e130e3637d | -3.28109 | -48.807 | 2024-11-18 05:03:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43e77606-d35a-379d-8dee-f9f78a2157ed | -1.30647 | -51.74145 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| d2898e92-9936-3686-8cd0-5b6cc0052f03 | -3.44507 | -52.58044 | 2024-11-18 05:03:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eae7c544-00e0-3c83-a32b-a3848fe66f50 | -3.06866 | -53.27463 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fc9b5044-861c-30ca-8cb4-234ad50d1398 | -1.21635 | -51.78792 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a352dbc1-906c-3f38-8ea2-6988200840b5 | -3.56177 | -50.26002 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 025c62c5-df08-3afc-93d1-945fda1f1b21 | -1.37958 | -51.56288 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7f2e8dc-b408-39e2-a274-fcb01d5c9f07 | -2.75157 | -54.01763 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 03dc9fb7-cc6b-3131-b8bb-a72c7bab2d52 | -3.04886 | -54.40451 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e72987a3-cedd-3149-ad53-053320ff6bd0 | -3.2343 | -45.55115 | 2024-11-18 05:03:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5341a854-3481-3d72-b2a4-d123aec53518 | -2.58861 | -53.9961 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8f86ac66-d311-366b-afcd-c6e86f9e2dee | -1.62407 | -55.14494 | 2024-11-18 05:03:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 96d0fa65-a1d7-361d-a70d-7780eb5fbc25 | -2.62863 | -46.82932 | 2024-11-18 05:03:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b9851f4-7075-3705-9fce-64f3774ad6dd | -3.3374 | -53.35249 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ae1174c3-6ef2-361e-ace8-34d1c8f2998e | -2.80058 | -54.01078 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef2687dc-b515-322c-b4e6-d025bf0d36dc | 1.14876 | -59.87997 | 2024-11-18 05:03:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd0dfd59-2108-3d4c-ade4-c9a5aaa0080a | -1.06573 | -52.3859 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14b71677-15d2-3084-88bd-d1ace896af83 | -1.94745 | -53.33103 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a3877469-b796-3d17-900f-0136b669d660 | -1.9096 | -53.32892 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57f163b5-9bd5-3b25-893d-181947e03901 | -2.17383 | -50.60708 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ced829b-ed8a-346c-8bde-15adf41f0031 | -2.88262 | -53.96163 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15433d0b-99ff-357c-ae00-3dce7c122fde | -1.29567 | -51.73978 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 44901474-277b-3b26-ac44-001add7e8bb6 | -3.05497 | -54.40904 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 4c4b76b4-10ad-3069-b080-fc3d09c914ec | -1.13235 | -54.17459 | 2024-11-18 05:03:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25592f87-8e6a-3f6a-b48e-a569796d2a09 | -1.13854 | -51.69585 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ae5f45c-142a-3458-8a56-b37f7b738c76 | -3.57749 | -53.27422 | 2024-11-18 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| be2f7c8d-cee8-3e24-90ba-e708e9693d2c | -3.05218 | -54.40503 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6d4366bd-3914-3412-9e98-559ab0c2eca8 | -1.81573 | -46.53316 | 2024-11-18 05:03:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a82b5dec-19b5-3cc1-bd18-430a7ef74ac5 | -3.77126 | -50.16601 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6e22b33f-3c56-3363-8705-570c0fd2daae | -3.61966 | -50.15108 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 70eb2598-32ac-3d5a-b1c9-f3504eb82410 | -3.05164 | -54.40852 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f67be5fa-bbb2-35b3-90a0-7d43831e946f | -3.39838 | -50.29087 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3f077b13-8da7-3f62-aab4-bc35977debf3 | -2.36803 | -53.68206 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9bbf4de2-fce6-3e20-b597-d6b07073db78 | -3.46179 | -50.01286 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1280343a-d91a-3dd5-ad61-1e44779f2f00 | -2.40283 | -51.9892 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 433eb677-a442-376e-b283-67997b755308 | -2.84175 | -53.96641 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 31fc8cd2-8ab8-3e75-a3a9-813de4e8ad1e | -1.41022 | -52.05525 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2b1947c-599b-3c6d-adb3-762fc8d7daad | -3.48771 | -53.98892 | 2024-11-18 05:03:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a4a11192-c730-3185-b284-27ea8d920ad7 | -1.81617 | -46.53018 | 2024-11-18 05:03:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b6dc1316-13f2-3177-a0de-521a5a999569 | -2.59064 | -51.72303 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 09c667ea-8410-354e-ba1b-1690528ec108 | -1.29503 | -51.74392 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ea42e03e-c675-345d-9c44-d13bfeccbee7 | -2.98487 | -49.10187 | 2024-11-18 05:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d424472a-81b6-3427-a36b-9bcb6f15b53a | -1.8121 | -46.53559 | 2024-11-18 05:03:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 7ef3d142-0c68-39b9-a93c-6d4005babd86 | -3.92905 | -52.20583 | 2024-11-18 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 284aad4d-6e73-3bd3-9291-bc3737bd28d1 | -1.51336 | -52.08974 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2dd43d7b-9e06-3c06-b252-b76fce6f3880 | -1.58751 | -50.44494 | 2024-11-18 05:03:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11e44105-1496-3117-816e-2e7a6e99ec48 | -3.33023 | -50.49739 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5abfc938-9cf8-36d9-a504-b2b7d9216976 | -3.68892 | -51.56194 | 2024-11-18 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26550505-6ef5-3412-b954-6be4ecebecf1 | -3.05551 | -54.40554 | 2024-11-18 05:03:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 886eb28e-4005-37ec-b49b-ca24ad020f4a | -3.69567 | -50.11446 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7c4f6c5d-f60f-3a75-a08c-be29cba8f7bb | -3.18753 | -53.25425 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f53a2299-035c-304f-857e-5ed6d9c208b8 | -2.23833 | -53.60413 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 557ff465-5850-32ad-b66c-56865abbcfac | -4.95605 | -44.84768 | 2024-11-18 05:03:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 35e89bce-6189-3d2b-b88f-1d150d25ea20 | -1.39539 | -51.98727 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9f36c8f2-402f-3955-9e4c-638161767f1e | -3.52672 | -50.2409 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9840b4dd-db1f-3b79-b7e3-000e73aa3619 | -1.57973 | -50.44374 | 2024-11-18 05:03:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b22f76b-4e2e-359c-9f8a-199c78e2b9b6 | -1.21276 | -51.78737 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e5aab6a5-e119-3805-bccf-b7fa594f798f | -2.79006 | -54.03446 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48d0cc1e-bb65-3ed0-b211-94762c12d842 | -4.99498 | -44.33042 | 2024-11-18 05:03:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 45c72fd0-afdb-3a83-93f8-697128267344 | -2.86027 | -51.84414 | 2024-11-18 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 684d0050-4429-302c-80dd-16b02ab0b02d | -2.33945 | -49.13794 | 2024-11-18 05:03:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cbeec2a3-8239-3626-b3b4-052ce031e658 | -1.15634 | -49.11839 | 2024-11-18 05:03:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6a950d7-0d5c-3a10-93d8-f5d29d30b1a5 | -1.2016 | -51.76466 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c68c9b61-181b-3c0c-84ed-234e54936634 | -2.65579 | -51.71336 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0bfc5b40-a91e-383c-bf08-af5632d89465 | -2.17673 | -50.60596 | 2024-11-18 05:03:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c01a138-7326-3ff8-ac9f-cdd37aca6f46 | -1.63457 | -52.5913 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 53ad8f52-5c41-392c-a21b-c743026e1d4c | -3.57676 | -45.20934 | 2024-11-18 05:03:00 | NOAA-21 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 094242fb-86fb-3170-90f6-313e65e66f7f | -1.15694 | -49.1145 | 2024-11-18 05:03:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef17123c-3898-3763-a02f-9172d5b1875c | -4.11429 | -51.05032 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 655ea280-f33c-3b41-b89b-aef69d7114ff | -3.18694 | -53.23498 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 13f68d8d-8e4a-39a8-ac15-682a0e9ecc5d | -3.57553 | -50.25106 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| bf6189f0-22a0-3932-936a-b1d7769d8698 | -3.47083 | -49.97192 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 107fb989-47dd-3941-95be-95b9bd64eafa | -2.34698 | -53.90796 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dacae6bb-a51a-3a5c-9318-88cacb7c84e0 | -1.86906 | -53.20316 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6a8cd9d-bfaf-3492-b6b9-8018d6ec0087 | -2.84391 | -53.34296 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb33a2c3-b017-342e-b113-36cac348c0e7 | -3.39979 | -53.26693 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| edac9911-d2ac-3e4f-a0a2-58fe45a9eca1 | -1.61927 | -52.50649 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bce1930b-daad-3de9-8dbc-74f1ecab1811 | -2.86524 | -51.78824 | 2024-11-18 05:03:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 355adcf9-81bf-39b7-9f36-7645019bb374 | -2.54849 | -53.9899 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6d91825-a50d-3292-9fe2-51704764f426 | -1.62228 | -52.62455 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f1690c29-2b2d-36d0-af89-4f08355ee710 | -3.31003 | -53.37107 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 254c9cea-a061-301c-b0b6-3b4c01efa08d | -1.09293 | -51.74038 | 2024-11-18 05:03:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e386100-3661-34a4-81dc-9e5a981506e5 | -1.44133 | -53.38673 | 2024-11-18 05:03:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 83e18d07-b1f8-3d3d-877f-e8e1448660c1 | -2.84907 | -54.00737 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b97f7627-ecd6-32d6-ad60-211c8f88b1e0 | 2.24062 | -55.83111 | 2024-11-18 05:03:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 058556f6-ffeb-343d-b64e-14ac917d844e | -1.16719 | -49.13204 | 2024-11-18 05:03:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a49b6823-b950-3068-8382-d24f3f38e283 | -3.38283 | -50.33888 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8aca095c-0107-3633-a1b8-5002277f23a3 | -1.65806 | -52.53216 | 2024-11-18 05:03:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5164eaee-2665-3fea-8614-f08e8603a3fe | -2.12913 | -49.50394 | 2024-11-18 05:03:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c316724-c506-305c-9386-6ee528519161 | -3.51567 | -50.23178 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 91e1979a-f33d-31ad-b8a9-8a950fa9ecf9 | -3.10589 | -53.09968 | 2024-11-18 05:03:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0c743e18-6a93-36c7-bcb3-a56fae5207cf | -0.74958 | -52.34362 | 2024-11-18 05:03:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e11abb4-96ea-30b8-9999-a7544f6250c5 | -3.42453 | -50.25508 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 447424cb-b333-37af-b19d-8459fc278621 | -1.30351 | -51.73676 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| f6445859-a6f7-3580-8b19-fa74b6de7eaf | -2.20484 | -53.7087 | 2024-11-18 05:03:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07531f11-eb0d-3d2b-8e56-65c8b2be0a8b | -4.1044 | -51.06337 | 2024-11-18 05:03:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ee5821c1-cce1-3284-939b-c7780b04ad0a | -1.1073 | -51.74257 | 2024-11-18 05:03:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8df7692-a887-3ea6-94be-1b67411febac | -1.58362 | -50.44434 | 2024-11-18 05:03:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README30.md)
