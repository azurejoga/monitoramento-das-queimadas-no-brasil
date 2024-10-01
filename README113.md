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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15bdd76a-0911-3433-827e-af5cf5ce00d2 | -12.96585 | -51.4357 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dc03ee64-9cbf-3450-a3b0-2b47638b184b | -12.96465 | -51.44159 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5fe26c30-194f-31e2-951f-f96839992ba6 | -12.96372 | -51.41706 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| dc3891a4-97fa-382b-a27a-c7ce13cf0265 | -12.9637 | -51.4191 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| fdea3854-d73e-323a-99d1-37ee087ec66a | -12.96318 | -51.4231 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 90e03f05-0a64-39fe-aefb-1f5ac552677f | -12.96317 | -51.42104 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 256440dd-3bf7-3a86-9d9b-59e9dcad2fd2 | -12.96262 | -51.42503 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 0a706e29-c33e-3e6c-8ed6-7ac6385c6957 | -12.95989 | -51.44496 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 805d011b-a980-3486-b9d6-d7197d119a4b | -12.95949 | -51.41645 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 7cf3a431-70e7-38c2-af8e-87cc8eb728c3 | -12.9584 | -51.42443 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 46f2eb66-7993-38b1-8a73-e988ce276f8d | -12.95786 | -51.42842 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.7 |
| d422773f-2815-35fe-b36e-0b2849ccbd1f | -12.95731 | -51.43242 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c1ea27f9-85cd-3eaf-8152-c16b6d67526f | -12.95473 | -51.41982 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |
| bf5f4149-6f53-3ddc-93b6-fbafe3a091d3 | -12.95309 | -51.43181 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cde54534-04db-335c-bcdb-e00a085f5a7f | -12.95105 | -51.41524 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 7bc31b0d-77ca-3fb6-bb61-cc74b34d3c75 | -12.95091 | -51.44773 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bc20b0d3-7cc5-3035-8367-34c7c3b8c649 | -12.9505 | -51.41922 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |
| bf5111ac-24e4-35eb-970e-b8fed403cabc | -12.94941 | -51.42721 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| b7556d9f-114f-3045-92ab-f95da9b8ae32 | -12.94616 | -51.45111 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6bc96040-b68c-337a-9801-8e3b9c3a61a8 | -12.94043 | -51.42999 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 2391a4fc-48a2-30d8-bdab-20f8d3ec844b | -12.93935 | -51.43796 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| d5b40f29-d38c-3497-9ac4-4d8657d1e41b | -12.93881 | -51.44194 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 62b8dd3c-df49-3e04-a862-4a562d5a03f0 | -12.93773 | -51.44992 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 7006ebb8-bc55-33e3-9c96-a1557cd828ef | -12.92876 | -51.4527 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dda81104-6ce3-3934-a399-54313cb0dd53 | -12.92088 | -51.4475 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9f5d9799-aa8a-3098-80c4-0cec32c29ec4 | -12.9198 | -51.45546 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c038bbb-bc4c-30de-85b6-b6279645e810 | -12.91478 | -51.2991 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6471ff5e-6417-317a-97b1-bb3d63f541f9 | -12.91453 | -51.4628 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bce4b7b4-9ee2-3877-af3d-f15924f7c696 | -12.90999 | -51.30255 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 06786fbe-d0af-32fb-9cc1-17d28eabc258 | -12.90574 | -51.30193 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c9479bb5-1732-3018-bd89-eaa56b11dafb | -12.88341 | -51.30698 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0221bfd2-a8a9-36e5-837b-3c7b6b916d68 | -13.36446 | -51.28965 | 2024-10-01 05:06:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e981038-1a88-353f-b7e5-aedf50049996 | -13.32162 | -51.35054 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4eece61f-f730-3682-aace-db51804df714 | -13.31468 | -51.33703 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cf31b2c3-5080-3c92-888a-2c912780802e | -13.31041 | -51.33644 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d252438-c44a-3924-8be7-5058e773d3ef | -13.03955 | -51.30239 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 59566c25-c483-39c4-9a24-722fc3334ba2 | -13.03901 | -51.30646 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b2d07499-5340-3341-8789-b7766bfaf8e2 | -13.03847 | -51.31052 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aa4f38d3-3d81-32f8-8c34-fa6eeee34c05 | -13.03529 | -51.30177 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc4d5c26-6411-3459-b370-b1c40b21c4bb | -13.03475 | -51.30584 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b81677c-83b5-368c-902e-210f9e3099a3 | -13.03421 | -51.30991 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8a1b3ca7-99aa-3170-848f-ec6b8308c901 | -13.03367 | -51.31398 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| eb8bbbdd-5183-3755-afc7-6e332acd83d5 | -13.03326 | -51.2514 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| af8e2568-0a49-3a3e-ac12-917bc7762695 | -13.03313 | -51.31805 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 08292f1f-815e-3c93-9533-ce8e73c8696b | -13.03272 | -51.25552 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2c2aed9c-2fd2-3a0e-b9af-195667ce56e0 | -13.03265 | -51.28893 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2f908cb6-0d58-38c8-ba87-46a26c6c1ac7 | -13.03211 | -51.29301 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aac7d7e5-b754-30f3-96e5-149f257e0872 | -13.03157 | -51.29708 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e012bdf3-c2e7-3ec1-b7ce-dc1cb3bfe7de | -13.02898 | -51.25079 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 04222def-ae97-3ead-85b9-1c220f9136bf | -13.02893 | -51.28422 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 85116e86-e5d0-3208-bdf5-f4e5c15e547e | -13.02887 | -51.31744 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2ce78d98-153b-3c90-863c-4c7d70ee4b8d | -13.02844 | -51.25491 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f4d17119-8e69-37ae-ada5-21669519f91f | -13.02839 | -51.28831 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 34.7 |
| f5ae093f-c41f-34a7-8bbb-da806a922d7c | -13.02833 | -51.32151 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1696941d-e510-3fcb-b128-afabce58562f | -13.0279 | -51.25901 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1bb86d4d-0ac9-3fef-a0df-f25bd6fc5f1b | -13.02736 | -51.26312 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c50f6683-0cc0-3e31-a67b-643133fc546d | -13.02412 | -51.28769 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 648db52d-1a59-3440-adf2-12f4b132c6cf | -13.02408 | -51.3209 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aa398084-1335-364c-ba20-7fabc0fadffd | -13.02354 | -51.32496 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1a0ddd85-0e38-3336-9134-963e7b0a0c51 | -13.02309 | -51.2625 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2ba59d4c-ee8a-376b-b5d1-96ce16486cad | -13.02304 | -51.29585 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 1165884c-7854-3513-b59b-ece0b9c60b66 | -13.02785 | -51.29239 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 90e90926-94fd-3730-af7a-67c8fba63273 | -13.02471 | -51.25018 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cbc0e2e3-4440-3def-b738-31e51818bb08 | -13.02466 | -51.2836 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 34.7 |
| 3adf00ee-eedd-3185-be55-69e453a3c5ad | -13.02417 | -51.25429 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 60e13fbb-f04d-3d62-942c-ae553b9fae45 | -13.02363 | -51.2584 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4fabbbd2-f3f4-3013-808f-3cb410149af0 | -13.02358 | -51.29177 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 832a39d9-c3f3-352e-9d39-b135853b43ea | -13.023 | -51.32902 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d41b5eb6-c0ed-3916-9a51-6558fdbbcf31 | -13.02255 | -51.26661 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4621f573-4668-3858-8593-ffea1eb0da3a | -13.02043 | -51.24957 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b14a127a-8f9c-3614-a15c-dc935582bba2 | -13.01989 | -51.25368 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c272ef10-84d8-3274-8337-f8dc67c639c3 | -13.01986 | -51.28707 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 13db5952-4565-3da3-8cd7-bc33bb0ef894 | -13.01932 | -51.29116 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 26.2 |
| aa655506-bc9a-3dfb-a847-bf3ec8ca8698 | -13.01878 | -51.29523 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 26.2 |
| dda7a556-5686-3d94-8041-b6f867d714e0 | -13.01825 | -51.29931 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ef6e3621-20e4-3427-b6ac-112a56bd3410 | -13.01821 | -51.33247 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50335256-1c0c-3fc7-b9de-a08fe057dbe8 | -13.01616 | -51.24895 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 233b8598-53ec-3cf7-8ea7-08393131244d | -13.01556 | -51.31968 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4fe3af10-d073-3916-80f1-9e5cda738f2e | -13.01503 | -51.32374 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bcf3d3c1-5160-3271-b0ec-5300e3b782b1 | -13.01449 | -51.3278 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bf4887ea-5ec1-3a0a-9e51-ffbee449d5b9 | -13.01396 | -51.33186 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 625fb603-08d8-37b7-9b9a-d382a22cad64 | -13.01345 | -51.30278 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ecf089a9-6411-39f5-87bd-da5e84e72381 | -13.01238 | -51.31092 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 21.4 |
| c81cbe65-bc4a-3ccb-a07e-0a05b44ba8dd | -13.01188 | -51.24834 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7d14569d-fe41-3698-8a3a-dbf2b7d5f2a7 | -13.01134 | -51.25245 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a171dccc-cec7-3a7b-af01-58f9adc9d22b | -13.00919 | -51.30217 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| b1f3981d-7758-3eaa-8412-2c2fd70b8093 | -13.00813 | -51.27705 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5bc95b5c-7a81-3cb8-a51e-ec3f6e8fc780 | -13.00707 | -51.25183 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 701c2ab1-bc96-3d79-aeb1-6341fd5feef4 | -13.00493 | -51.30156 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 3ee3aea6-38f3-34d6-b86d-81bdd627b1d5 | -13.00386 | -51.3097 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| c45aa378-5e68-3a94-8649-50661f84095c | -13.00386 | -51.27644 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bb0b6573-b15b-30b0-86ff-cc2fb60e65b4 | -13.00333 | -51.31377 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 5aa58d83-6396-3fe0-a3a0-606078631a1f | -13.0028 | -51.25121 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 3eeaf5a8-2697-3c0f-81d9-bc99038b3ad7 | -13.00226 | -51.25532 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 36.8 |
| b42e4c24-d362-31aa-9da0-b3a76e4cdc91 | -13.00173 | -51.25943 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 36.8 |
| b23928bb-bd38-3161-bdef-88d237361048 | -13.00014 | -51.30502 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 702e701f-3179-3b8f-97a2-2a0c52b2523a | -12.99961 | -51.30909 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 097ef841-f543-3057-8db4-699caf65a732 | -12.99907 | -51.31316 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 6f6c74b0-8a55-3752-8f0c-a6f044b79e95 | -12.99854 | -51.31722 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| a1111533-a070-3f6a-a2fa-085122aa0c5d | -12.99802 | -51.35435 | 2024-10-01 05:06:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README114.md)
