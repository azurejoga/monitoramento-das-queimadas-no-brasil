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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07c95a30-ca27-3662-b9fb-1417b88e2bf9 | -3.30028 | -51.11293 | 2024-10-03 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb58407f-9c0f-3b33-85c1-05433ea0f1cb | -3.25329 | -50.9405 | 2024-10-03 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b1051682-85a5-30eb-bb7c-9680e0ac116f | -3.22649 | -50.79287 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 226fe1a8-0927-3f24-be68-dec2846da8ef | -3.22241 | -50.79226 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2f7142c0-22d2-3d6d-a9f6-d03163e1f5db | -3.22182 | -50.79588 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| bd742adf-32b3-3b62-a2ad-266c85cfd729 | -3.04463 | -50.98308 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e349f3e-41ea-3668-b394-155d6c111022 | -3.04402 | -50.98677 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b1eb965-381a-3a3a-95ed-f887ec7f6bab | -2.90787 | -50.74912 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15fc2d0e-51c6-3c36-bd41-f22efc1bd9e2 | -2.90728 | -50.75279 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 13761b01-bd9b-3520-9e0b-c67c44a4d03f | -2.90555 | -50.73754 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9e64620-1a50-37a2-bca1-475dda59f16f | -2.90496 | -50.74118 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61449c0d-8acd-3661-822c-4048f57f1bca | -2.90319 | -50.75214 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8514443-7e13-3986-a3ca-1f05fa5d6741 | -2.90092 | -50.71447 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c99ca954-d4a0-3465-9013-7271445ccf0e | -2.90033 | -50.7181 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5a5ec8f-40a8-3bd9-a06d-c32c9d33850d | -2.90029 | -50.74417 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1d287c62-3d4b-380e-936f-73017923db0d | -2.89969 | -50.74782 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d9e5c67f-33d4-328b-96c3-df5a6ff3140e | -2.8991 | -50.75148 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5c34275-101d-3b9d-adb0-ea8a505c5a2d | -2.89684 | -50.71383 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dfd9df77-775d-309e-8f6b-6a5ced6d001b | -2.89624 | -50.71745 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e97ff91-c791-3ce7-8392-1a0cb9b73c1e | -2.8956 | -50.74717 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65a3adb1-566b-3294-972f-56df61d5e3a0 | -2.89269 | -50.73926 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ea470a1-17b5-314f-b071-7e7860aa9b3c | -2.89216 | -50.71682 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf189b34-2b30-3aef-9c39-b772e14a1dc5 | -2.8921 | -50.74289 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4feb4119-0a52-3267-93a1-89d2fca3d45c | -2.89157 | -50.72046 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d67e3b2d-c803-3222-8268-4fb5ff0aa3f8 | -2.89098 | -50.72408 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3912ca94-ec56-33cf-8d22-ccf458879062 | -2.88808 | -50.71617 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1968da53-0227-3d39-83a3-4b3afa0d5f15 | -2.88801 | -50.74225 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4c6e527-238b-31f8-a0fd-788554486e37 | -2.88689 | -50.72345 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 33f2ca54-01b3-31a2-b2e5-0f842431c531 | -2.88459 | -50.71188 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c13025dc-93b6-36b9-8e8d-5a7c5a9d61de | -2.884 | -50.71552 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02ade3c2-1a58-34d7-8bc5-09eee6356e35 | -2.88333 | -50.74525 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be9ab125-4346-3ebf-9a33-795a839cd4e9 | -2.88273 | -50.74891 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4049fe0f-2b90-3432-86c4-e328aad32b25 | -2.8811 | -50.70762 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6dbf98f6-174d-379e-b079-9827ee065ff3 | -2.88051 | -50.71124 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0956b869-1829-35fb-8bf1-b1390f4df0b6 | -2.87991 | -50.71487 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c823a525-368b-35dd-8e1f-b958102a0889 | -2.86526 | -50.7275 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e607d56d-8469-3f3c-abc0-bbe45fea992c | -2.86178 | -50.72321 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a2719d1d-7118-38e7-981d-322ffadaa086 | -2.85812 | -50.72188 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef94dfef-efaa-3b7d-a4d9-b2de7eeaf619 | -2.85754 | -50.72553 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e8f4176-0d8e-33dc-826d-96386a095d26 | -2.85709 | -50.72622 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b41287c-1151-338a-951f-1b97f92ba11c | -2.85518 | -50.71395 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ed0cbf91-930d-3ecb-9207-efc4395f7366 | -2.85421 | -50.71831 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15790fa3-c0e2-3c25-9d89-1a804e72ce91 | -2.85287 | -50.72855 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56ef27e3-7896-3b8d-9e1e-967adce9f81d | -2.8524 | -50.72923 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27be6dcd-ebc6-3bfb-8672-eaeab4b0cd2b | -2.8523 | -50.73219 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9e0b9bf-9075-3387-9777-d78600e62709 | -2.85179 | -50.73286 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7641664-a6b0-353a-acfb-5a23d809d264 | -2.85052 | -50.71695 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d9b8700-31e3-3320-b67b-c70eda7e88d6 | -2.84936 | -50.72424 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab02e371-af36-33ed-8a3d-33dff96684c4 | -2.90847 | -50.74546 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 379a7c9b-5752-3d95-b81b-5ba3cab66099 | -2.90438 | -50.74481 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c44076d-20b7-3dc5-976c-18758822a840 | -2.90378 | -50.74847 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 032a8788-3afa-3b2c-a4d8-df42145d73d7 | -2.90087 | -50.74054 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0da118e-a370-3962-8116-851622294d83 | -2.89974 | -50.72172 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cdd4b70c-21df-3846-a299-d16698121508 | -2.89678 | -50.73991 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b62eea30-abe8-3c80-a7a3-be1c48308877 | -2.89619 | -50.74353 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62e62761-427c-3ac3-b575-1ba0396498d8 | -2.89565 | -50.72109 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6e9636be-9343-3143-997b-f7ede53826db | -2.89506 | -50.72472 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7475165-16ba-3146-89ab-2810e832d5a0 | -2.89501 | -50.75082 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c5d4355-a923-35b2-b750-da672b926a6f | -2.89275 | -50.71318 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb2c9794-0ed3-3abd-8507-d930567d2183 | -2.88926 | -50.7089 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3886e3bc-3fea-3a2c-a9ea-607453e6bcc6 | -2.8892 | -50.73498 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2774a549-137a-307a-bbf4-ff90de183230 | -2.88867 | -50.71254 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df4d0af3-4f55-3d16-a555-af777d4e8eb9 | -2.88861 | -50.73861 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 317a5cc3-d0b5-3870-8d81-d15017a7af8d | -2.88748 | -50.71982 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbbb129d-057e-39ab-9a5a-519a23c2b64a | -2.88518 | -50.70826 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 27577a7f-773a-38eb-aee3-2fb4926e8ffc | -2.8834 | -50.71917 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 294bb77c-0c6b-38f0-b652-8f644d36169c | -2.8828 | -50.7228 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40f7b029-1d56-37cf-91f8-20da0beac273 | -2.86586 | -50.72386 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3cb019f9-7671-33c5-ad32-0ef005f79101 | -2.86298 | -50.71594 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a53dc0d-e187-356b-8836-b37027edaad4 | -2.86238 | -50.71957 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c02dc25-ca0b-3903-9d7a-a879b6cca1c1 | -2.86118 | -50.72686 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 403b02e0-5abf-3748-88b7-aaa33df8d100 | -2.85926 | -50.7146 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7be78ada-70b6-382c-9f30-2cc1fb81f829 | -2.85889 | -50.71531 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 45489afe-846b-3652-bad4-25597a8afae7 | -2.85869 | -50.71824 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c1ad6132-b2aa-3f88-828a-446e5dd16d03 | -2.85829 | -50.71894 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 365e1db1-16b9-3684-b5a0-a2c6e075cf0a | -2.85769 | -50.72258 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec187bdf-319a-31d5-b5dd-ac931f57b5b4 | -2.85481 | -50.71467 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0809b224-ec14-3a8b-8141-8b473f0bdfad | -2.8546 | -50.7176 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93f4606b-9b41-3439-9437-b0e6d19c4bda | -2.85403 | -50.72124 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e85ebbb-58c3-3894-8fe0-e031bd6c1645 | -2.8536 | -50.72194 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40f3429b-52cc-30b1-8295-50c73bff7e4d | -2.85345 | -50.72489 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6fcd3db-f4d8-316c-8dce-024275197a86 | -2.853 | -50.72559 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ee117e3-d6d8-3aaa-a8d5-a1a740fcb0d0 | -2.84994 | -50.72058 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 828ef594-17da-381b-8bb2-31605089cd1c | -3.4878 | -50.80424 | 2024-10-03 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3afaeacf-7226-3e2d-aeef-6c345107594d | -3.4737 | -51.7763 | 2024-10-03 04:25:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a098a66-1791-3367-aa58-614841fb2a94 | -3.45661 | -51.06829 | 2024-10-03 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0d30d945-e0b9-38f1-be7e-87375dcf52a1 | -3.9582 | -50.89212 | 2024-10-03 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d1d0815b-886d-37c6-bf3f-04eb4a7e420e | -3.95266 | -51.00261 | 2024-10-03 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 19ff67d9-ebb8-34e2-b4fc-de1d6e6fa7c2 | -3.95207 | -51.00624 | 2024-10-03 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bc45bfac-1d47-37b4-ba8e-a6feb3d02012 | -3.94857 | -51.00196 | 2024-10-03 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fb8d2550-63c5-31d4-a15b-759d76beb13a | -3.94756 | -51.24271 | 2024-10-03 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3bb24d6d-42e3-3f69-afaa-8e23b6abeb88 | -3.8713 | -51.18784 | 2024-10-03 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0f925b5-9ec2-3a3c-9ccf-52dfaf6e63a6 | -3.86924 | -51.18696 | 2024-10-03 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d10a8d1c-dc6d-36be-ae9d-6f936330189a | -3.7896 | -50.79799 | 2024-10-03 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d59bd99-6239-3bff-9d37-669e9fdeb53c | -3.78261 | -51.32555 | 2024-10-03 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 842096cf-139f-3ecc-a55e-5d1576264554 | -3.76359 | -51.71008 | 2024-10-03 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2796703-0cef-3f46-8f55-1d152136f403 | -3.7529 | -51.13029 | 2024-10-03 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ef9f992-88e4-38eb-90be-4a043cd683a6 | -3.72766 | -51.20765 | 2024-10-03 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74c20bb7-7860-3d03-b176-f6bf35d03deb | -3.7235 | -51.20696 | 2024-10-03 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d89b681c-046c-3076-b2c6-b44fc9ba9689 | -4.09751 | -51.11636 | 2024-10-03 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README85.md)
