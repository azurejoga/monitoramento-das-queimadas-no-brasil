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

## Dados Diários - Página 164

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4d7c1a5c-4d9a-3d95-89f0-199477945863 | -5.23781 | -40.9315 | 2024-10-25 16:52:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 167.6 |
| ab1f0392-60dc-3d56-993a-2640e0fa2649 | -5.23424 | -40.91109 | 2024-10-25 16:52:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 18.1 |
| 9d239665-115b-38f7-8434-a40d6ebdb100 | -5.2316 | -40.92876 | 2024-10-25 16:52:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| cde3b572-4576-3039-84fe-1a84d9d651e1 | -5.23093 | -40.92494 | 2024-10-25 16:52:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 08c26d89-a957-38ec-96c5-c951ae902953 | -5.22648 | -40.92625 | 2024-10-25 16:52:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 3b139101-dbfe-39a1-802b-7f51dea85557 | -5.21032 | -40.53965 | 2024-10-25 16:52:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 4b86edd8-5441-3325-a182-664474e31c80 | -5.20461 | -40.54058 | 2024-10-25 16:52:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| a2beb887-750f-3b09-b435-4fa2cef0b1f3 | -5.19197 | -40.39917 | 2024-10-25 16:52:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 9795cc23-b516-3814-a433-335bf8a39bc4 | -5.19128 | -40.39516 | 2024-10-25 16:52:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d381f7f8-0c6b-3c68-b25e-794668959912 | -5.15954 | -40.4173 | 2024-10-25 16:52:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 38.5 |
| 302f773f-7dbb-3b14-8bd8-8a591f6ceed6 | -5.15884 | -40.4133 | 2024-10-25 16:52:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 39.5 |
| 38e004ac-981d-3475-9134-a158c587fe6c | -5.12671 | -40.61117 | 2024-10-25 16:52:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 18.7 |
| bf21c5f5-6759-3ae1-b285-0dcd21aede89 | -5.97631 | -41.51289 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 50.5 |
| 3b6489e3-777d-3248-bc97-3b16792b72dd | -5.97427 | -41.5283 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 142.9 |
| 5854d3ec-b273-316b-a23f-b6936741e1aa | -5.97388 | -41.53002 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 186.6 |
| e3d5671a-0897-315d-9e1f-69a0f1a62198 | -5.97371 | -41.52499 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 142.9 |
| 93cd461a-9bb1-3220-adc0-598e2cf9d2a3 | -5.9733 | -41.52674 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 138.5 |
| f77c82a3-ca90-3672-86f6-314c8412dc21 | -5.97315 | -41.52168 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 69.6 |
| 04c13450-4bf0-3598-b24c-2fafb28bb75d | -5.97272 | -41.52344 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 138.5 |
| f847929b-5b18-35dd-8f5d-dc3a0dc12eb3 | -5.9726 | -41.51839 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 69.6 |
| af8c598f-e0d0-398b-afff-8109a874f1ed | -5.97214 | -41.52015 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 47.7 |
| 80fa6ff9-543d-356e-b0dc-97a128a3403c | -5.97157 | -41.51688 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 47.7 |
| a2ec5769-dfdb-3df2-8df4-b3c72da31f83 | -5.96952 | -41.53234 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 236.2 |
| c4a23cdb-cf57-3d3c-bdac-3a56e5f60eb2 | -5.96915 | -41.53405 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 186.6 |
| 66e70db8-1900-39f4-9174-8304e410a89e | -5.96897 | -41.52909 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 142.9 |
| 9c9754be-83a4-3a5f-a3d4-3c2be130bec1 | -5.96842 | -41.52583 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 142.9 |
| 40afa72f-e52f-3717-9a87-e49bb52189f1 | -5.96801 | -41.52758 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 138.5 |
| 28919e03-4627-3efd-89fd-5f2e2d587437 | -5.96786 | -41.52256 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 69.6 |
| f8d67d76-c76c-3108-9858-a1c74f93750c | -5.96743 | -41.52432 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 138.5 |
| d48f006c-c409-3394-b936-014c01459506 | -5.86818 | -41.5384 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 88d2eb14-f640-3f8e-ab1b-3e533353426c | -5.86762 | -41.53505 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 4a039511-061f-35fa-bdd4-f8ea8fe3ba18 | -5.86755 | -41.54042 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| b06273ca-20e9-30c7-952d-85a724a21e2a | -5.86696 | -41.53709 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 849eecd0-f90b-301b-9d09-dd314566610c | -5.86637 | -41.53374 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| d6729977-6321-3523-8fa9-cc03b2fe2f76 | -5.86235 | -41.53608 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 2606e539-d380-311d-a2ea-b26b851983ca | -5.73927 | -41.41344 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 19.7 |
| de3be331-a455-312b-bc45-e9f0931d12a4 | -5.7387 | -41.41004 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 19.7 |
| ebb25b37-6749-360c-af59-a55666e2bee9 | -5.7374 | -41.41443 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 18.9 |
| a772b9d1-a598-3d2a-b21b-c67cbdbd7157 | -5.7368 | -41.41102 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 18.9 |
| e2135faa-3e0c-39e6-b87d-26234f6eff00 | -5.66679 | -41.24736 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 94f67364-ef22-32a9-8691-9d9d0f0c2a1b | -5.6057 | -41.74161 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8d29bfbd-2a5e-35ee-bab7-1f41d78471c0 | -5.60517 | -41.73853 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e226b287-9a4d-3896-9b3c-941f662ea936 | -5.5735 | -41.19273 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8b241c73-4e8a-33d2-b49e-3f8c73dcac2e | -5.5729 | -41.18933 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| d8f9cc58-524b-313a-8e2a-d9a1ddafbe08 | -5.57162 | -41.19035 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 66e90b08-4364-321f-b71d-eca2462228ba | -5.39937 | -41.11012 | 2024-10-25 16:52:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 959012ec-8fbd-3441-b0cd-6f46eb80172c | -5.39451 | -41.11464 | 2024-10-25 16:52:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 845459db-3ee9-33a1-aa1d-e3a38a407fb4 | -5.3939 | -41.11112 | 2024-10-25 16:52:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| e4af52f6-0e80-37ad-97f1-dbbdd9b39148 | -5.39081 | -41.1258 | 2024-10-25 16:52:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 9217c25d-5df6-36a6-bd25-54af9afb6fd1 | -5.38902 | -41.11553 | 2024-10-25 16:52:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 06750a11-860e-3933-84e5-3c708f617d3d | -5.3884 | -41.11198 | 2024-10-25 16:52:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| d80d8777-b0d7-3b8d-94b2-049807a1f0b3 | -5.38534 | -41.12676 | 2024-10-25 16:52:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 24.4 |
| 9ddccbe6-dd0e-3310-83bb-4aa177e6c46b | -5.38354 | -41.11646 | 2024-10-25 16:52:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 60100044-6e51-3c48-b2df-0a21a384dfbb | -5.38291 | -41.11286 | 2024-10-25 16:52:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 21.3 |
| f1a101af-966b-3d3b-b0b3-4434822d0618 | -5.26893 | -41.20629 | 2024-10-25 16:52:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| fb9bf71d-4d24-3214-83de-94a129edfaef | -5.268 | -41.20729 | 2024-10-25 16:52:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| a9c0753b-589e-3bf3-9d67-7c205b80c7d9 | -5.26474 | -41.21444 | 2024-10-25 16:52:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| 933f75e7-53c9-34fc-a90e-56d0bf2cd830 | -5.26377 | -41.21556 | 2024-10-25 16:52:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 97c9cf30-dcc7-36b4-a486-b83f540ae750 | -5.24762 | -41.18112 | 2024-10-25 16:52:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 25.2 |
| f721f64f-f8fd-39ff-98c4-8f58f46bd1a9 | -5.247 | -41.17763 | 2024-10-25 16:52:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 25.2 |
| 6be870f3-621c-3cd9-9f16-5ab279c6cc26 | -5.24689 | -41.18209 | 2024-10-25 16:52:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 53.3 |
| 251e876d-53ff-308c-b1f9-b1588ef43c6c | -5.24639 | -41.17416 | 2024-10-25 16:52:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 35.6 |
| c663be7c-60d3-37fc-92c0-9f9e2fac158b | -5.24629 | -41.17857 | 2024-10-25 16:52:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 53.3 |
| b905a6f9-66b3-3cd6-b808-cdb1bc517b20 | -5.24577 | -41.17069 | 2024-10-25 16:52:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 35.6 |
| 4842a9c1-87e8-35ed-8ead-ac06c218aa06 | -5.2457 | -41.1751 | 2024-10-25 16:52:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 69.0 |
| 54d749c8-5557-35fd-a549-dc74277fa590 | -5.24511 | -41.17161 | 2024-10-25 16:52:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 69.0 |
| 4287c8f0-6d2d-3b8e-80dd-dcbf7b86da09 | -5.24084 | -41.1796 | 2024-10-25 16:52:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 53.3 |
| 50aa3159-4363-38ff-9467-1189c644dbca | -7.1749 | -41.4146 | 2024-10-25 16:52:00 | NOAA-21 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 26.9 |
| fecc6810-e8f4-3c5a-bd49-bc530aee9039 | -7.17435 | -41.41144 | 2024-10-25 16:52:00 | NOAA-21 | GEMINIANO | PIAUÍ | Brasil | 2204352 | 22 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 3fae5efb-1056-3814-9fef-a9320992795d | -7.09942 | -41.65921 | 2024-10-25 16:52:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 588f8a15-ca03-3639-ba42-07d205a9e5aa | -7.0968 | -41.64439 | 2024-10-25 16:52:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 62a6f933-aef7-3105-941a-9d61b771fb79 | -7.08904 | -41.82779 | 2024-10-25 16:52:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2a36f72f-c735-3920-b124-f43fbc211d03 | -7.06214 | -41.56899 | 2024-10-25 16:52:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 049f0e14-90a7-3e07-b735-a3fa0a993720 | -7.0607 | -41.56953 | 2024-10-25 16:52:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a84fe941-b90c-3ef9-9323-61d64ef27b3f | -7.02317 | -41.65992 | 2024-10-25 16:52:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 365bcfe6-18c6-3e19-9853-2d0943e2e819 | -7.00381 | -41.30034 | 2024-10-25 16:52:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 3c12c21e-a25d-377f-9976-5e1d88b32224 | -7.00328 | -41.30063 | 2024-10-25 16:52:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| d1e04871-b6d5-3ca1-af80-6a623b83b67e | -6.99854 | -41.30126 | 2024-10-25 16:52:00 | NOAA-21 | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 9a9af3a7-a368-364a-8587-4db23f5bce5a | -6.96436 | -41.32327 | 2024-10-25 16:52:00 | NOAA-21 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| b35907a9-3c32-3d3c-9b2b-3eb22a58457b | -6.95853 | -41.32098 | 2024-10-25 16:52:00 | NOAA-21 | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 98784dd6-2f7b-33d1-92bd-351de3643356 | -6.95066 | -41.5805 | 2024-10-25 16:52:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| d5c09f5b-8b4d-3aa8-b6e3-5df34c907637 | -6.94966 | -41.58254 | 2024-10-25 16:52:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| af5a9e63-25e2-3d7d-aad2-ac942949face | -6.94912 | -41.57938 | 2024-10-25 16:52:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 2d34e96d-2380-370d-9ac8-138fb2538d24 | -6.91551 | -41.01323 | 2024-10-25 16:52:00 | NOAA-21 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 459d273b-4eb5-39ab-8e1f-99357e39188f | -6.88577 | -41.52214 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 16db3b90-8549-329c-af2e-b96da5d28026 | -6.86291 | -41.72449 | 2024-10-25 16:52:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 1591c08e-5c9b-3afd-b4c1-14861c15dabc | -6.86087 | -41.7266 | 2024-10-25 16:52:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 67b8bb8e-225e-3716-ad45-ca4b9abea262 | -6.86034 | -41.7235 | 2024-10-25 16:52:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f99d914f-908a-3d9c-bc9d-2589905e8688 | -6.8025 | -41.81595 | 2024-10-25 16:52:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 31cd2e11-d0da-35b5-9411-feccfb30ab4f | -6.79045 | -41.77744 | 2024-10-25 16:52:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 32.0 |
| a0c99c01-797b-3a93-9c8b-5a2566cd3978 | -6.72641 | -41.84851 | 2024-10-25 16:52:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 52.4 |
| 9447e2fe-8c7d-388a-9a99-d7ff98b279c2 | -6.71091 | -41.10941 | 2024-10-25 16:52:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 40cf94bd-86d6-3152-9db0-1dfc53233b2b | -6.71032 | -41.10604 | 2024-10-25 16:52:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 5c731e47-a67c-33e9-aa4e-167547cca073 | -6.69188 | -41.49523 | 2024-10-25 16:52:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| f8dc33e8-229b-3d4b-bd73-294ea03455a6 | -6.68666 | -41.49617 | 2024-10-25 16:52:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| ad6ba9db-ab55-30fd-9287-407d6e677c0c | -6.6861 | -41.49297 | 2024-10-25 16:52:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 18.5 |
| b7de7cda-dcd0-3887-8091-9f6337556c67 | -6.58669 | -41.51235 | 2024-10-25 16:52:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 3271f1d5-efe9-3a46-829d-428bb70c7d75 | -6.45966 | -41.77178 | 2024-10-25 16:52:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 56373339-5f49-360b-88ae-c895591f714a | -6.4591 | -41.76859 | 2024-10-25 16:52:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 82d72833-c3ff-36b0-9abf-98df6abd7cdd | -6.45448 | -41.77251 | 2024-10-25 16:52:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |


[Clique aqui para ver as próximas entradas](README165.md)
