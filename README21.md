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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8e0e10c-1d45-31d1-a98a-b914b8264b60 | -4.36105 | -50.88364 | 2025-11-04 04:31:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 07a49b94-7feb-3c3c-ab06-15af473dbb25 | -4.47213 | -43.23316 | 2025-11-04 04:31:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2e4bf537-ae73-31f5-8e76-6f3800a9cc71 | -2.92692 | -51.76773 | 2025-11-04 04:31:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c104023-a590-3756-9b2a-bc59d8906d71 | -6.8403 | -46.30315 | 2025-11-04 04:31:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9efc1885-ca32-333f-a315-91fd83c1d8ca | -3.29132 | -50.20126 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| df61f846-4aff-3c6d-8c6a-03e32d7a0d79 | -3.40315 | -50.27329 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 41cd56bf-a509-3ea8-a9cb-85bbef79a145 | -9.04309 | -47.00998 | 2025-11-04 04:31:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ccf0fc1-c551-39d2-aa96-478e5d534031 | -2.31771 | -48.58221 | 2025-11-04 04:31:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9591bde-ba0c-30c3-8055-56aa703a4da0 | -2.98249 | -48.70731 | 2025-11-04 04:31:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c624e56-5461-3985-ac7b-a05989e75d6a | -2.82673 | -49.41895 | 2025-11-04 04:31:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a13d1d8-17ea-356b-966b-52b7e7847ac5 | -7.60477 | -43.01039 | 2025-11-04 04:31:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| abfa54c0-5d40-3379-993d-8c3a9474ff59 | -5.36315 | -44.73957 | 2025-11-04 04:31:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8851ad66-709d-3e39-99af-0376bc09f278 | -3.54831 | -46.36183 | 2025-11-04 04:31:00 | NOAA-20 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| aa7e31e7-f086-3e57-9591-7e0d65ff8020 | -2.37419 | -47.72868 | 2025-11-04 04:31:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 968c14ad-b3d8-34cd-a3ae-b1a2806f393a | -5.83081 | -44.66112 | 2025-11-04 04:31:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 480f02c1-e5c0-3621-8833-e4470dd782f2 | -3.69912 | -49.00599 | 2025-11-04 04:31:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ddf7bb37-8e35-33f9-8b34-017944379a0f | -5.07081 | -47.11494 | 2025-11-04 04:31:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6f3d96a0-4d25-36e5-adbc-f886dd483d41 | -5.36964 | -44.74463 | 2025-11-04 04:31:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10cf8534-086e-345b-bd8d-bb95186b3df8 | -3.59271 | -55.44284 | 2025-11-04 04:31:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3b27b4e-7562-350c-8277-179eaf22465e | -3.94959 | -49.32593 | 2025-11-04 04:31:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e2c48533-54a7-332e-b2f4-25185e0806e4 | -6.1464 | -44.57874 | 2025-11-04 04:31:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8da9929-8feb-358e-9ef9-60bd46b264fa | -5.76318 | -45.90052 | 2025-11-04 04:31:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7bf93ba1-728e-37a6-b7bb-a3599e6209e3 | -3.44196 | -50.21592 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc0f06c4-f98c-3dbc-9437-8b8c1cd25d25 | -8.59814 | -44.16078 | 2025-11-04 04:31:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ac6c933-8326-3aa0-acb9-34fa1d1bbb90 | -4.57089 | -45.86109 | 2025-11-04 04:31:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cd8f7bb8-9853-3e8c-aef7-75a4ee7242b9 | -4.62111 | -45.73913 | 2025-11-04 04:31:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 62d0d799-29e4-3286-a9fa-5fd692bac4c2 | -5.61924 | -45.97223 | 2025-11-04 04:31:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| dce5ada2-a4a3-363d-a5c6-aebfa21a3aed | -4.60866 | -45.75217 | 2025-11-04 04:31:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a0d48e7e-d37a-3aef-9c0e-19f1d1e63eda | -2.37198 | -47.7212 | 2025-11-04 04:31:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e734900b-8431-3264-8ffb-46ff01f17d1f | -4.96422 | -45.51678 | 2025-11-04 04:31:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b1023a2-da7a-3283-b4d3-1fa2ce911063 | -4.9544 | -44.90388 | 2025-11-04 04:31:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7dd97f4f-9fb0-391e-bf87-b7297691a911 | -5.92266 | -41.31886 | 2025-11-04 04:31:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 230cd960-45c7-3b21-834e-a4d06b356a5c | -4.42237 | -45.64251 | 2025-11-04 04:31:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8282c6d8-ae8f-315e-be7b-7ace79677cf6 | -3.45197 | -53.02021 | 2025-11-04 04:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4264df2e-a4c8-39ba-84a1-ac8e18a5839b | -6.84085 | -46.29955 | 2025-11-04 04:31:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 31186ce1-b35f-3695-90bd-c8a10f4b7516 | -5.32566 | -45.3791 | 2025-11-04 04:31:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac47db46-ecf0-30ab-a1fe-8d8c1c8fbcd7 | -7.08154 | -38.82686 | 2025-11-04 04:31:00 | NOAA-20 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 50328bcd-4cf4-34e2-a9f7-c811b2096586 | -1.96478 | -52.10884 | 2025-11-04 04:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5357b946-c147-34c5-9802-987f29e6706e | -5.03531 | -43.6242 | 2025-11-04 04:31:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0fdd65c-f52d-32ab-b138-51b2b750bae4 | -4.65028 | -46.28923 | 2025-11-04 04:31:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d001b4a5-f5d5-3511-bd7c-cb96ba2fdd0a | -4.8525 | -43.01125 | 2025-11-04 04:31:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a1c30d7-313f-3d1f-9084-0068a44c6068 | -6.31321 | -47.38153 | 2025-11-04 04:31:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5c9a18b-295b-3b71-ab74-659f9dd41a38 | -3.53522 | -54.86444 | 2025-11-04 04:31:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36c2eff0-1e58-3aa5-9099-0ba7a3dc0acd | -4.87396 | -49.00338 | 2025-11-04 04:31:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64329c8c-3366-39e8-a99c-e235c8f88a85 | -4.6938 | -45.67946 | 2025-11-04 04:31:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e07586e6-2e79-3728-919b-4f03775b90a2 | -3.10799 | -51.20804 | 2025-11-04 04:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d116878-8c49-3fa2-bc4c-9acb019ded68 | -2.32335 | -48.59057 | 2025-11-04 04:31:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c240b6a-b978-3b08-8e81-1959daa79b5c | -4.95792 | -44.90437 | 2025-11-04 04:31:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8b3c115-af17-3455-a717-d8adc75ebb4a | -5.89338 | -42.91178 | 2025-11-04 04:31:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d3c9a872-764f-31b4-8426-5bd78ba08442 | -3.59457 | -49.44187 | 2025-11-04 04:31:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4274bb76-c89b-32f7-9725-c7bfafdc6609 | -5.43005 | -44.65908 | 2025-11-04 04:31:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ae956b0b-2aa0-348a-9f3d-fda5a6ea1321 | -4.62113 | -45.69459 | 2025-11-04 04:31:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aab49027-f55c-332f-8973-1bc141060af2 | -2.96947 | -44.59401 | 2025-11-04 04:31:00 | NOAA-20 | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6e5d006-4a1e-3fa2-bd6a-16623e4a41f3 | -2.3188 | -48.59732 | 2025-11-04 04:31:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d44098aa-7dee-371d-9227-4e4db473fc82 | -5.75035 | -43.39359 | 2025-11-04 04:31:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 154cb433-eb0d-3939-a940-313ce33d1459 | -6.427 | -43.0682 | 2025-11-04 04:31:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53a329ca-129e-3a44-a641-94d9ac9ddc4d | -5.88178 | -44.34974 | 2025-11-04 04:31:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bd1c88e5-fccc-3b33-a6dd-5defed56f5d3 | -7.53048 | -47.28696 | 2025-11-04 04:31:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 581257c2-4cf8-340d-a49c-e8ee35625662 | -2.30651 | -50.47552 | 2025-11-04 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90605d27-388d-32bf-91f4-12162a69a0d8 | -3.75569 | -49.17773 | 2025-11-04 04:31:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6cd153e3-392f-3549-a983-91f2bb964757 | -2.8315 | -46.72728 | 2025-11-04 04:31:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf2b020b-0f0e-3811-8b2d-4f41783f28fe | -6.41834 | -43.07206 | 2025-11-04 04:31:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c3ff46bc-e0ad-3a7a-b27f-eaf1d86a4311 | -5.29841 | -44.80798 | 2025-11-04 04:31:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d9a77f62-3fd6-35ce-bc29-aa0315ead962 | -2.96783 | -44.59417 | 2025-11-04 04:31:00 | NOAA-20 | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c3c3953-0152-3166-9033-9c6415dde650 | -5.25922 | -48.48108 | 2025-11-04 04:31:00 | NOAA-20 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 41473e6d-8401-3170-8184-a872696c6410 | -5.40908 | -43.66276 | 2025-11-04 04:31:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b87acec-af4f-32d2-90d5-b4bf3773663c | -4.48663 | -45.88114 | 2025-11-04 04:31:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c41b6a92-fd6e-3fc8-8a7f-daf03e188cca | -2.6399 | -54.57977 | 2025-11-04 04:31:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 0239f07a-9adc-3bd5-a030-002501e6139e | -4.0304 | -45.46225 | 2025-11-04 04:31:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 59a46e36-4fd9-39d5-b9cd-10314b05e151 | -1.96947 | -52.1058 | 2025-11-04 04:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cce97e1c-e313-3788-9fd4-d585dd5ed891 | -5.28588 | -48.44218 | 2025-11-04 04:31:00 | NOAA-20 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e2b37d2-f734-379d-be69-ec8fb9b1c65d | -3.86386 | -52.3275 | 2025-11-04 04:31:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ceb2d4e6-3d3f-3acf-aed5-811bfdb4a17c | -1.96889 | -52.10946 | 2025-11-04 04:31:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0584bae6-4908-3e63-b84f-865ce5317df4 | -5.78303 | -43.95874 | 2025-11-04 04:31:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 85ccb5f2-c143-3f11-a3e8-76ca19b5479e | -3.29199 | -50.19713 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| db9c3845-2532-39f6-b2f2-84f572b3f0fe | -5.65177 | -44.06886 | 2025-11-04 04:31:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8d8c51ad-103e-307a-b489-9d153193e865 | -3.27724 | -46.50817 | 2025-11-04 04:31:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6bcdde46-b4e4-349e-866b-0a8d0bc96969 | -5.17405 | -48.95091 | 2025-11-04 04:31:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 274e6b88-59a2-36aa-b613-f0f1f8063e51 | -5.32163 | -45.38234 | 2025-11-04 04:31:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8903a552-b944-32cd-9b21-7e102c8a3c2e | -6.14012 | -41.54852 | 2025-11-04 04:31:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d7c17463-c7d9-3e6c-9db0-2f882b85f663 | -3.13914 | -44.47541 | 2025-11-04 04:31:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d46aa61c-9996-3138-b3db-c4a81d6159fa | -3.82576 | -51.22644 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f2b6e0a-f76e-3d5b-8830-5d7aeedfec0d | -6.13575 | -41.54799 | 2025-11-04 04:31:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d81b0a25-4d49-316b-a3c7-47b74bec6d24 | -3.44223 | -50.23714 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 80b6a939-70cb-3b57-92fb-dd46350377f0 | -5.28537 | -44.60874 | 2025-11-04 04:31:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91876780-6b5c-3866-b17e-74009f7697a2 | -3.77914 | -51.05774 | 2025-11-04 04:31:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0ee7ec3-6c4f-3313-af90-4edc57742428 | -3.46236 | -52.87526 | 2025-11-04 04:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d4f5bbde-68e7-3ecf-a78a-5ac2504b712f | -3.48195 | -53.28352 | 2025-11-04 04:31:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5f92e6a-b1e0-3772-9d09-a3ef264d3135 | -2.87206 | -45.2951 | 2025-11-04 04:31:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1ecb148e-be16-3ccf-b216-a8aefded7228 | -5.24013 | -44.21746 | 2025-11-04 04:31:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7b85cf4-2ca9-3830-9949-d462c0071f62 | -3.24339 | -50.79784 | 2025-11-04 04:31:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4cf75caa-4132-386f-aa8d-9f49e2da3439 | -7.55712 | -45.84761 | 2025-11-04 04:31:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a0b5ac1-50da-32b7-acad-4c4f4f78cebc | -3.5218 | -55.43425 | 2025-11-04 04:31:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a206f38a-af9e-3d28-9c63-19e8f036397e | -2.94921 | -51.57722 | 2025-11-04 04:31:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 560362e4-72b0-39cc-bc7b-1c387a3d4d98 | -5.36376 | -44.73556 | 2025-11-04 04:31:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 70135a0f-d7da-35fd-aec7-efc43e40535f | -4.61148 | -45.7563 | 2025-11-04 04:31:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d54c152b-4d80-37a1-b9df-a81aabad7153 | -3.42358 | -49.17207 | 2025-11-04 04:31:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a76587c5-79c0-31a7-9325-d30e7f384033 | -5.92393 | -41.31031 | 2025-11-04 04:31:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1c39bea7-cb0a-365b-bde2-32412fcac8bc | -3.45195 | -54.68597 | 2025-11-04 04:31:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27cf4505-e661-3f6f-b06f-6325f5adce79 | -3.31743 | -53.85226 | 2025-11-04 04:31:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README22.md)
