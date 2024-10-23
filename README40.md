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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47aa2439-8cba-3940-9d0a-72fe1e456f74 | -3.24039 | -50.85058 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 062c38d8-6f84-3127-8b61-13a0dec5ef4e | -3.23706 | -50.85006 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 102895cf-d5ab-3bc3-a6fb-697691f1022b | -3.21324 | -51.19919 | 2024-10-23 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4d886fb-3928-3186-b364-981cf38c3491 | -2.79988 | -51.36054 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8c4e213-fc71-38a0-bd5a-4921268cc451 | -2.79657 | -51.36003 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa36a4d2-5a6d-30a3-a04f-e5223b7cfc23 | -2.79604 | -51.36347 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 933751e5-ceee-37a5-b2c6-d8084f4466db | -2.79166 | -51.36983 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d357e0cf-1027-363c-b241-8940aa387f6e | -2.86451 | -51.59926 | 2024-10-23 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15174f65-d3a7-3634-946d-4a84e425c0a1 | -2.81086 | -51.35519 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9c2e7cc4-cc73-3eb5-a2e0-ccbfd2576dcb | -2.80285 | -51.6001 | 2024-10-23 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af4c50e7-cd10-357f-9e23-87d840df46e5 | -2.79934 | -51.36398 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55898d17-292b-3115-9fb6-9a804738c39c | -2.7955 | -51.36691 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96836c84-2dc6-38b0-b0a7-8e1098d3df83 | -2.79273 | -51.36295 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63c1a324-b173-356d-a30a-c6ff1be06c11 | -2.79219 | -51.36639 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18e5be68-a171-3877-92af-66fb307ce2a5 | -2.78943 | -51.36245 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f38328ff-9cb1-3618-8e96-758e534da821 | -2.75145 | -51.97495 | 2024-10-23 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30c2f5cd-2a1b-3109-b2da-51d87618dfc0 | -2.66794 | -51.24793 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad01abdb-beae-362c-8bdf-128c93ed7091 | -2.606 | -51.77257 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 173e7190-021a-3962-af53-00a175fc10ac | -2.60547 | -51.776 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 178d7b42-f723-3139-9ba7-4f5fd557e8f6 | -2.42811 | -50.49773 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60d82eba-ef17-34ab-817b-bf9bd4e025fe | -2.40407 | -50.43252 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 92b62230-fd1a-3d8b-8269-dd836639ff47 | -2.28282 | -50.46816 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c9020c67-ab3c-35a2-8e3e-94281a28adc8 | -4.63936 | -50.91165 | 2024-10-23 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5f18ef9-51c0-3f84-b4d3-3f112b7f2335 | -4.63881 | -50.91521 | 2024-10-23 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 089b378d-df21-321f-a53a-11892da3f5d7 | -4.63602 | -50.91112 | 2024-10-23 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93985f08-6d8e-3b8e-8d5a-d4355bda1160 | -4.63546 | -50.91468 | 2024-10-23 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76784619-a090-3b76-ae89-2c0156df1f07 | -4.61091 | -50.91818 | 2024-10-23 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fc5d7119-4d08-3f7f-9244-1696cc765e87 | -4.61036 | -50.92172 | 2024-10-23 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4610addf-9f32-332a-b0ca-976142aba36b | -4.60757 | -50.91765 | 2024-10-23 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ed6619e0-b73c-3140-9e10-4668ab0bfd6e | -4.60702 | -50.92119 | 2024-10-23 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 78d4287b-5d3b-3481-a389-e058b10a99e7 | -4.18164 | -51.29379 | 2024-10-23 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39500a5a-a773-39d0-b044-b95686698559 | -3.96884 | -52.1533 | 2024-10-23 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2dad3188-1538-3ab0-8378-e60aec9b32bf | -3.96602 | -52.12825 | 2024-10-23 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 878c5453-8b93-3ce1-a9db-802b5cfb46ca | -3.89166 | -52.12307 | 2024-10-23 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d73cf258-f446-3428-a2e2-0b10811f3609 | -3.89112 | -52.1265 | 2024-10-23 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97046cbf-1110-34c1-b986-ba4a3464baaf | -3.88405 | -52.15001 | 2024-10-23 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6e854917-db48-333d-a20a-6e9453b3134e | -3.85036 | -52.27839 | 2024-10-23 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcd585e2-432c-3d6c-8874-529a0f748de0 | -3.84998 | -51.67349 | 2024-10-23 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 470a1517-7c60-3a66-a1cb-d7c01df45c43 | -3.84939 | -52.13408 | 2024-10-23 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56db7fd2-513e-3795-bea8-77d550391c60 | -3.84759 | -52.27444 | 2024-10-23 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 54e7c06b-f640-3e1e-9dcb-78fdd2b33ffa | -3.84705 | -52.27788 | 2024-10-23 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e2bd0d6-2b69-3039-8e15-e6ccb32207c5 | -3.84364 | -52.23513 | 2024-10-23 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf123009-d084-3679-9898-8ea032c26e6a | -3.8242 | -51.38351 | 2024-10-23 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77da6c13-42c1-386f-a4c2-27dd7557af8b | -3.8077 | -51.3775 | 2024-10-23 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e34e4cdb-c614-3f2f-94cf-67c1bbacc587 | -3.78454 | -52.17665 | 2024-10-23 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 34374803-a080-36ff-bb5c-2ac244233f2e | -3.77242 | -52.16774 | 2024-10-23 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07040d40-7437-3378-91c3-5981b967f1e2 | -3.64008 | -51.42863 | 2024-10-23 04:51:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89c81396-2328-35cf-ba31-82676a02af1a | -3.71713 | -51.97635 | 2024-10-23 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da109eca-9751-30a9-8c7d-7e662b729380 | -3.68233 | -52.09043 | 2024-10-23 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a3baf3d6-e235-3818-9cfe-4d6a86008945 | -3.68179 | -52.09386 | 2024-10-23 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b86aa9c9-d07a-3992-8654-7cd67dae84b7 | -6.08294 | -52.30109 | 2024-10-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc6f2dcd-1fc8-3e2c-8b44-1d2939768aeb | -2.21438 | -51.99241 | 2024-10-23 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ae523ed-9f3e-3ade-89fc-9c1d19c740ab | -2.10038 | -52.45495 | 2024-10-23 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61b06614-62fb-3979-8ae8-ceba9514fc1f | -1.97086 | -52.1336 | 2024-10-23 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b641d91f-b4ee-341c-8fdf-0799f08e7e60 | -1.94624 | -52.00633 | 2024-10-23 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5c078faa-78b2-36cc-981e-c966692f5134 | -1.93441 | -52.10317 | 2024-10-23 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 650fc277-33e4-351a-b7c1-25d04f7aa1ab | -1.93333 | -52.11006 | 2024-10-23 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f0848e5-16cf-35f9-8360-4f751e8cdda6 | -1.93111 | -52.10266 | 2024-10-23 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd99d775-93c9-328d-acc3-5e483c641844 | -1.93057 | -52.1061 | 2024-10-23 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1dd5db4f-4d40-34d5-9100-371be1a6b4bc | -1.86608 | -52.08553 | 2024-10-23 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f1ea8b4-7fd1-3621-954e-989d7d1734bc | -1.8276 | -52.02588 | 2024-10-23 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbd5a807-e3ad-3121-a15b-1fe86fd0a418 | -1.8104 | -52.17849 | 2024-10-23 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 056f1134-0bc3-3681-a010-a0676c75a838 | -1.76805 | -52.23209 | 2024-10-23 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e4b2317e-1ff0-3450-a221-2c601a705b43 | -1.76751 | -52.23555 | 2024-10-23 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12b338f5-612c-302b-8d6b-1ac8aa25cc6b | -2.04531 | -52.69677 | 2024-10-23 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c5ac5ac-2eb7-3e94-9328-2266737c0367 | -2.04476 | -52.70028 | 2024-10-23 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5051fc2-8c08-3e49-8927-2d6037982876 | -2.00809 | -53.29399 | 2024-10-23 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac1b0e0f-18d9-36d7-ae00-41b1ed150a1b | -2.00751 | -53.29762 | 2024-10-23 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b100bcdc-5f4f-34ce-9a9e-e0d04ebbbda4 | -1.93239 | -52.70077 | 2024-10-23 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b61022e-bd41-39b0-baf8-7c815c9e12e4 | -1.89842 | -52.93819 | 2024-10-23 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6214ce9c-40bd-3808-815f-704bc0a9d2c4 | -1.77186 | -52.98441 | 2024-10-23 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16bf3ebb-121c-3585-ab81-70a4eab29a56 | -1.68761 | -53.04777 | 2024-10-23 04:51:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0fbaa383-ec7c-3ee2-8ed2-1b8f37276841 | -1.54294 | -53.09921 | 2024-10-23 04:51:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e67e39c0-7021-3738-bd1c-852fb99fdac0 | -3.11072 | -53.12413 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ff865ba-ece3-3d36-9431-7c3572c75e98 | -3.11016 | -53.12766 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2152bd25-1a11-3fd5-a6a7-5001649f43b2 | -3.1096 | -53.13118 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e65d266-712d-3154-b385-fd0acf0b6afa | -3.1088 | -53.11979 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bf47e68-4024-3ecb-9450-53d04250275d | -3.07471 | -53.24927 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7f94a1c2-b930-3993-8801-4551943af209 | -3.07191 | -53.2452 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2b89c3e5-956d-3d94-831a-b3674c7ea464 | -3.07135 | -53.24876 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1ae7925c-5602-36ce-976f-4045a42a38b8 | -3.06799 | -53.24824 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1851e43c-44f6-3bcc-90df-437db934e40f | -3.06743 | -53.25179 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c5c733d-f63a-32a8-9348-b7db978b0957 | -3.06519 | -53.24417 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b0395e8f-bf4a-3368-99a8-17b9c0305e11 | -3.06238 | -53.2401 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d6bca939-3f56-32aa-8a9c-961c82e1547f | -2.99695 | -53.05169 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f98d5a7-0ac1-3c9e-b2ee-8bb7975738ba | -2.98073 | -52.85093 | 2024-10-23 04:51:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c25c36d2-bbcd-3346-ab3d-9eba07ec1997 | -2.85362 | -53.33627 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90e754b4-3b26-3387-9a02-c9d53da17156 | -2.84968 | -53.33934 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee6f6131-54d3-36f2-a6be-5ea27d274420 | -2.84688 | -53.33522 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 344cc62b-4d4e-391a-b05e-e307e1f31db4 | -2.84631 | -53.33882 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ba4c0b0a-3461-3fac-8b37-4593aba5b8a3 | -2.84294 | -53.33829 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd9e3aeb-b15e-33ca-ba72-ee3ebc837c57 | -2.83957 | -53.33777 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3811c674-d1d5-3073-90ae-f74fd8976664 | -2.79493 | -52.92933 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a347857-376c-38b2-a3b6-d5927eb1aae3 | -2.78936 | -52.92128 | 2024-10-23 04:51:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 23258b8f-ce37-31a2-9540-ad88454c7519 | -2.7888 | -52.92479 | 2024-10-23 04:51:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9bd69e57-1851-308d-830a-fc58876abe64 | -2.78825 | -52.9283 | 2024-10-23 04:51:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b55721d8-c41c-35c5-9cc3-8f45cca17561 | -2.78601 | -52.92077 | 2024-10-23 04:51:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94da1d93-8f4c-3950-8858-446316332a9d | -2.78546 | -52.92429 | 2024-10-23 04:51:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1fd1eddb-b25b-313e-ba95-a733ef0d3a89 | -2.78491 | -52.9278 | 2024-10-23 04:51:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21920700-4ef3-3ae1-bf25-80b957d1da7d | -2.78259 | -52.09928 | 2024-10-23 04:51:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README41.md)
