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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a4bf655-0909-397f-9669-77e780a59381 | -5.8439 | -44.76581 | 2024-10-28 04:57:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c174b9ba-4048-3d25-9c09-e0251ff13e17 | -5.81318 | -44.13155 | 2024-10-28 04:57:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4e620037-877d-3daf-a237-33e51c878eeb | -5.81267 | -44.13527 | 2024-10-28 04:57:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 574bff30-6e3f-3484-b938-2bd5aadf779a | -9.43564 | -44.48941 | 2024-10-28 04:57:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5f3d3216-9c13-3dae-a2ee-a61b849596a5 | -9.19424 | -45.60983 | 2024-10-28 04:57:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 008edab3-dfe8-3a2c-ab90-2a7db6ae4d99 | -9.18405 | -45.2151 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c5ea31a-3007-361e-b0fd-ce6241a41c27 | -9.17903 | -45.21099 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6995d29-9163-349b-a8ab-9759e9df7d4b | -9.17856 | -45.21447 | 2024-10-28 04:57:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a733bfa0-6e89-32f9-9f91-002925125e26 | -8.77264 | -44.71161 | 2024-10-28 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc8b0185-d85e-3f93-9659-755e9c16711a | -8.77214 | -44.71539 | 2024-10-28 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f9c7675-43c7-3780-a902-26c213ec0bba | -8.77165 | -44.71917 | 2024-10-28 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d67402a2-8f84-32a5-89ef-cae69aa37216 | -8.77115 | -44.72296 | 2024-10-28 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e51490cd-61ae-33ed-958a-8e245453aef4 | -8.77065 | -44.72674 | 2024-10-28 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f7eb114-2cf2-338f-8c56-8aa545b9ac09 | -8.76188 | -44.70629 | 2024-10-28 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5161d14-58c6-3592-8ce6-340f5325eb0c | -8.76139 | -44.71006 | 2024-10-28 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6630ea85-412f-3456-af66-337c71fc681f | -8.76089 | -44.71384 | 2024-10-28 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 067a2196-efa9-325c-9ff3-6d6be610a739 | -8.7604 | -44.7176 | 2024-10-28 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df7efe08-cb19-38ea-8d1a-d1931ecf9467 | -8.75991 | -44.72139 | 2024-10-28 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 40339572-9986-3318-a6ca-eb040303e5fa | -2.79753 | -45.34843 | 2024-10-28 04:57:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b4c904e6-2209-3286-bacd-0fa6ec113082 | -2.79669 | -45.35394 | 2024-10-28 04:57:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 37bffbbd-ea4c-3bb0-9f61-0a2f8c188796 | -2.90771 | -45.26626 | 2024-10-28 04:57:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f66a00b-4e0c-3d68-9b9c-a49d9fb69330 | -2.90729 | -45.26908 | 2024-10-28 04:57:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b32cd7ab-1145-3de2-8004-9150b16f640e | -2.90275 | -45.26546 | 2024-10-28 04:57:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 836388bd-0d0b-3d3f-866f-e8ce11d6c194 | -2.90232 | -45.26827 | 2024-10-28 04:57:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cda8efd9-8644-3ae7-8b92-79a7e87cbf85 | -2.87486 | -45.4509 | 2024-10-28 04:57:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 11a53381-aa96-319f-8624-9a1e4e55d64b | -2.86996 | -45.45013 | 2024-10-28 04:57:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 06395a2e-f369-3488-888b-0461b22e3379 | -3.01883 | -45.4929 | 2024-10-28 04:57:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 16.5 |
| aee6887b-34dd-3e1e-bd9a-2e030c010f9d | -3.01803 | -45.49837 | 2024-10-28 04:57:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 8b5592e0-f134-39a0-9a6b-407c7e047a69 | -3.01576 | -45.4963 | 2024-10-28 04:57:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 57.4 |
| e5b473db-8c1a-3083-8af8-38a22e547c29 | -3.01393 | -45.49214 | 2024-10-28 04:57:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 16.5 |
| d2cc6bf2-cdd6-3a1c-bbbc-3e041814bb75 | -3.01313 | -45.4976 | 2024-10-28 04:57:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 92b6c29f-2d49-3e6a-b7fc-ce498917af99 | -3.51302 | -45.80453 | 2024-10-28 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 51.6 |
| fa4aafa0-bf0d-3fcd-973f-71e053f8e50c | -3.51258 | -45.7999 | 2024-10-28 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 0478b91d-72fc-32c2-80e0-19ef1b5f97be | -3.51181 | -45.80525 | 2024-10-28 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 4fb0df39-e674-37a8-a06f-bb569a2bbf99 | -3.509 | -45.79847 | 2024-10-28 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 9e34308e-0b26-37b2-a081-54ea452a4eb6 | -3.50851 | -45.79383 | 2024-10-28 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ef62502a-dea6-39fb-9979-a6d95c9295dc | -3.50818 | -45.8038 | 2024-10-28 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 25904108-d756-3adb-af88-e9ac13b882a2 | -3.50774 | -45.79917 | 2024-10-28 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 48.5 |
| d6baf6fb-c3de-36cf-bf9f-2100b3600173 | -3.50697 | -45.8045 | 2024-10-28 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 2f8f55aa-f504-38d0-a148-eb8a2fc2b0de | -3.50416 | -45.79777 | 2024-10-28 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 05e0d365-fd5d-375e-bfe2-ac6bf4291a7a | -3.50335 | -45.80307 | 2024-10-28 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 32726782-8d9f-3094-b9bd-e8427b57ae98 | -3.5029 | -45.79845 | 2024-10-28 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b622a9f-655a-3963-a5de-6432b69afa69 | -3.50214 | -45.80376 | 2024-10-28 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb9741cb-53bd-37bc-ac4f-0ba2650e4e8d | -3.45056 | -45.89204 | 2024-10-28 04:57:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| da19ffcf-a89b-3a46-b01d-9be9310640ce | -4.87227 | -45.84947 | 2024-10-28 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df89e8ea-6aae-31c5-9db2-e9b5ed237984 | -4.84435 | -44.93599 | 2024-10-28 04:57:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c1a095d-a455-3efd-8dd3-6b64db8a36b5 | -4.83913 | -44.93504 | 2024-10-28 04:57:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6efbca82-51ba-3b95-856e-b3a45c689896 | -4.71154 | -46.14438 | 2024-10-28 04:57:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73942460-daa3-3734-a12d-327bc5d2c854 | -4.70442 | -45.88484 | 2024-10-28 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 28efbc62-6480-3d55-9f89-9ae2d9889925 | -4.69951 | -45.88423 | 2024-10-28 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 45657439-8c83-3858-9e73-01d54e5fefa3 | -4.69875 | -45.88952 | 2024-10-28 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 82076d95-e78b-30ee-a56a-aaec62dcf6a1 | -4.69687 | -45.88377 | 2024-10-28 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3b7e8aaa-8b0c-3389-8a4f-a823af69d0ef | -4.69607 | -45.88913 | 2024-10-28 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 35a8c1e5-9554-3177-b694-06b881b70218 | -4.6946 | -45.88359 | 2024-10-28 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d714cbce-719d-31c4-be26-fe339b55e373 | -4.56665 | -45.79953 | 2024-10-28 04:57:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2459a880-1914-36c8-b938-9068e136a237 | -4.56584 | -45.80503 | 2024-10-28 04:57:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1b5bcb63-ab6d-3061-96c3-e8720af1cb6e | -4.56173 | -45.79884 | 2024-10-28 04:57:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 604be311-811d-37d6-a7c5-57a6467de076 | -4.56089 | -45.80457 | 2024-10-28 04:57:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1cf8f625-185b-3d90-8075-4577510821fe | -4.55678 | -45.7984 | 2024-10-28 04:57:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 63349e49-d7f9-35e2-abd2-d960321b01c1 | -4.55184 | -45.79781 | 2024-10-28 04:57:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0aba6563-2a00-369b-a020-3d4e7cdf32e6 | -4.38827 | -45.34017 | 2024-10-28 04:57:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3bea674c-8a1a-3957-a106-3a83320860f8 | -4.28876 | -45.52868 | 2024-10-28 04:57:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30efcce3-99f8-314d-a469-b191a29de1db | -4.28833 | -45.53158 | 2024-10-28 04:57:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e911dff4-c23a-30b6-ae32-154c98e83a7d | -4.28789 | -45.53453 | 2024-10-28 04:57:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7ec38195-45af-3e56-afd1-833c9ff97851 | -4.28746 | -45.53747 | 2024-10-28 04:57:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e9ae8ef9-910f-3645-8c81-c710539ac661 | -4.28421 | -45.52504 | 2024-10-28 04:57:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4ded7b1-0799-3a35-87d2-37876b12e081 | -4.28378 | -45.52793 | 2024-10-28 04:57:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ccf13d56-4bc7-3fac-9916-e80e4053dd41 | -4.28335 | -45.53084 | 2024-10-28 04:57:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e68b36d-bf19-3638-b58d-13a3ad02f8f8 | -4.28292 | -45.53373 | 2024-10-28 04:57:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c52e8c28-d6af-33ea-bd3f-8d84ff968f75 | -4.28249 | -45.53661 | 2024-10-28 04:57:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9decd1bd-dbab-3699-87b8-bd7f485fbaa9 | -4.27836 | -45.53006 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bf8cd51-0e83-3173-bcf4-cda987600d93 | -4.27794 | -45.53293 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36d7e9a7-5a06-3f0f-a713-3bae7a997282 | -4.27752 | -45.5358 | 2024-10-28 04:57:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0d32f33-fb44-3024-8880-e5343442083a | -4.08048 | -44.6138 | 2024-10-28 04:57:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 57ecb731-5a05-396e-a71b-041df6e3195c | -3.66978 | -45.93392 | 2024-10-28 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8386a62-0b7b-3211-b8aa-c872c290cd95 | -3.85311 | -45.72797 | 2024-10-28 04:57:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1753512-c096-3eb5-b506-42f96a5d4772 | -3.85184 | -45.72268 | 2024-10-28 04:57:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c6215ac-bb48-3dcc-8821-87175c8fc970 | -3.85105 | -45.72816 | 2024-10-28 04:57:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 11cd959c-a348-38ed-934b-38aed9492716 | -3.84906 | -45.72176 | 2024-10-28 04:57:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2896ba89-63fd-376c-b49c-057d58b6e8bc | -3.84823 | -45.72719 | 2024-10-28 04:57:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82a0dc29-688d-311a-ab75-440ae38cd241 | -6.18663 | -46.57631 | 2024-10-28 04:57:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eea636d6-0c9f-36dd-ae66-ea3a371d4f37 | -6.18658 | -46.5741 | 2024-10-28 04:57:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7fedfa07-d66a-32af-a729-63d2859f0fcf | -6.18582 | -46.57932 | 2024-10-28 04:57:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7642748f-e297-3ebd-8763-c9444817d3e1 | -6.1845 | -45.44039 | 2024-10-28 04:57:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 429f2634-8d40-3625-891f-394506f3f230 | -6.17889 | -45.44281 | 2024-10-28 04:57:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1203e4ee-f639-32e8-a228-51b0fea1f550 | -6.17847 | -45.44585 | 2024-10-28 04:57:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59a73a85-71b7-3a6b-a764-cfa9995b105f | -5.97978 | -45.36921 | 2024-10-28 04:57:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a96d481c-8e23-3d33-a869-cdb1eaf44ca1 | -5.97935 | -45.37233 | 2024-10-28 04:57:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 739c0881-7a0b-3754-b0b8-311aa4b589e0 | -5.97463 | -45.36829 | 2024-10-28 04:57:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a32aa79f-d8fe-3ea8-a314-80019545f51e | -5.78004 | -45.73695 | 2024-10-28 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 236aeecb-23d3-355a-8d56-e13af1c3565a | -5.58366 | -46.33997 | 2024-10-28 04:57:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0e183bb2-cc7d-369b-9f0c-43cf21758a86 | -5.44946 | -45.8943 | 2024-10-28 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8beccabf-c062-3558-adcf-a1a04cc1d8e6 | -5.44568 | -45.89454 | 2024-10-28 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f545acfe-1075-34dd-8d5e-32a1375c6a42 | -5.44448 | -45.89381 | 2024-10-28 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb4aea1a-b6e6-32a2-bb8a-c0bf9e186318 | -5.40651 | -46.3479 | 2024-10-28 04:57:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8a5a4f96-9063-3f3e-ada9-47271897776d | -5.2703 | -46.20839 | 2024-10-28 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7e9bf71d-c5fb-3d9a-b451-5afa3ece5b85 | -5.2695 | -46.20875 | 2024-10-28 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2490d75-124d-35a8-bcb1-080be4910a9f | -5.24144 | -45.9253 | 2024-10-28 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8b9f8db-0272-3d48-b96a-dda08a9bc3fa | -5.22865 | -46.22354 | 2024-10-28 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3bbdc596-5c90-32b2-9432-d1346810d7ef | -5.18757 | -46.20067 | 2024-10-28 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README49.md)
