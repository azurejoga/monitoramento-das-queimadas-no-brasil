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

## Dados Diários - Página 221

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2906de32-ca76-3525-8355-4cb801dddb34 | -17.08369 | -57.35279 | 2024-10-09 06:14:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 35.0 |
| 67a39db2-6cdc-3e41-921a-82101d6d2260 | -17.082 | -57.36618 | 2024-10-09 06:14:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 75.1 |
| 11367f05-4b0b-39a8-aa98-a4decd1d5164 | -17.07504 | -56.02174 | 2024-10-09 06:14:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 53.4 |
| ab28bfc3-2b97-332f-ad1a-b9fdafe1d041 | -17.07305 | -56.03841 | 2024-10-09 06:14:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| e06cce3d-1b61-3c05-b08e-e7d9d4609422 | -17.06709 | -56.01556 | 2024-10-09 06:14:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 56.7 |
| 02f5e4dd-3aaa-31d1-9350-63968c9a9e10 | -17.06499 | -56.03221 | 2024-10-09 06:14:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 49.2 |
| 045bf831-da22-3165-ae46-441e73ea65e9 | -17.06333 | -56.02024 | 2024-10-09 06:14:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 33.3 |
| b2a80a15-14c4-37f6-8844-20614e843975 | -17.06135 | -56.03691 | 2024-10-09 06:14:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 11698d92-5885-3060-9214-66e0883efd29 | -17.04459 | -55.0496 | 2024-10-09 06:14:00 | AQUA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 1cbf397a-97a2-33b8-95f8-40e8f551516c | -17.03426 | -55.02832 | 2024-10-09 06:14:00 | AQUA_M-M | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 1f19448b-0e92-3f93-87b9-db0b76c389aa | -16.99806 | -57.47062 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 51.6 |
| 2bb3f184-976b-3fef-bd14-ffa17961bb74 | -16.98925 | -57.45605 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 3d089981-4ed9-378f-a5d4-a5f144a62a8b | -16.97876 | -57.45462 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 16aaac91-da5f-3451-96cd-b06a40c954cc | -16.9771 | -57.46775 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.5 |
| e13e4d9e-8b6e-3203-840a-1f578f3037ac | -16.97116 | -56.78477 | 2024-10-09 06:14:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.0 |
| e4a123fc-b092-3e8e-9e73-1a951b0ac6f4 | -16.96938 | -56.77927 | 2024-10-09 06:14:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| 3023a438-c645-394f-8ae6-e38fd55c8997 | -16.96014 | -56.78332 | 2024-10-09 06:14:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.3 |
| e0a8112d-22c4-3da5-b44c-1d9494a4e928 | -16.95126 | -57.45739 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.5 |
| 75739193-e6e7-3e1f-850c-6946d44b2cf5 | -16.94922 | -57.687 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 9570084c-d118-3a4f-85c7-38cd089096d7 | -16.94761 | -57.69968 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 89b6a7fd-c7ca-331e-b726-f7a40b36ab85 | -16.94301 | -57.67935 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.4 |
| 665c3071-12ab-314c-aca2-3fe5288ca911 | -16.94131 | -57.69201 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 23.4 |
| 26d707df-007e-3584-8371-0699a6c06a27 | -16.93891 | -57.68558 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.9 |
| 0eda0fc7-f535-388c-93f9-a796d8141070 | -16.93736 | -57.48214 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 24.9 |
| 05d4a064-67bb-3f40-80aa-95540c98a9dc | -16.93565 | -57.49518 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 54.9 |
| e8a44ed2-83c3-3029-8617-7627d7262784 | -16.93059 | -55.80169 | 2024-10-09 06:14:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 15.9 |
| 4bc73622-cb10-38bb-bf93-a9b29d4b96e8 | -16.92853 | -55.81892 | 2024-10-09 06:14:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| eb4393c7-54af-3929-b0e6-6f36a6c01c0e | -16.9269 | -57.48071 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| d5178b92-2e4a-3f3f-8c34-9d19b6db41c7 | -16.92075 | -55.78292 | 2024-10-09 06:14:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 22.7 |
| 8294e2d8-5eb9-3bf8-86c6-a42d1e598a64 | -16.9187 | -55.80021 | 2024-10-09 06:14:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 28.4 |
| bd360d43-6d34-38e8-b627-728dd2ce1614 | -16.91206 | -57.67511 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| aceff93f-d902-3849-8161-142d6292aabc | -16.91199 | -55.79415 | 2024-10-09 06:14:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 37.4 |
| 72e6649d-f5d8-3e85-a1e9-2a5753844dc6 | -16.90681 | -55.79871 | 2024-10-09 06:14:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 21.8 |
| 05e0e488-e97c-35cf-b7a6-fa9a8286ecfa | -16.9001 | -55.79267 | 2024-10-09 06:14:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| e8debc74-f9e1-3faf-9d77-53e0ac6ff782 | -16.89768 | -56.72504 | 2024-10-09 06:14:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.8 |
| ff9f0ddc-330d-3a87-af8c-456dc06de7b4 | -16.89586 | -56.73977 | 2024-10-09 06:14:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.2 |
| ab69b901-043b-3096-8766-1cdc8ef52d97 | -16.88364 | -57.81166 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 27.2 |
| 37c97ab4-9937-3f96-b492-4d5d4b4d1464 | -16.87342 | -57.81026 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.6 |
| fe69b95f-56bd-34b8-b6d9-caf18f7b6c4d | -16.87179 | -57.44106 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 2028765c-84b5-36e7-914b-e6710e3a04da | -16.87006 | -57.45414 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.5 |
| be6339d2-afc0-3ef8-b3fa-916083cae20f | -16.86321 | -57.80885 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 24.4 |
| 163e06ed-f8ce-397d-b0f3-6dbdcc13155b | -16.8551 | -56.69736 | 2024-10-09 06:14:00 | AQUA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| b33d4f7d-ed5f-37bc-9b81-830ad25e41b2 | -16.81226 | -57.40622 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 28628aea-ff9c-3411-9f21-d17465d6d825 | -16.80891 | -57.43248 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 37.2 |
| 5a07c9ea-9e3e-3aaa-b2b5-8f5c7c0967ca | -16.71517 | -57.45274 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.7 |
| 9c607d9d-4266-344d-b606-b289fee00045 | -16.71351 | -57.46575 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.3 |
| 15b426b6-a587-3a39-be6e-389c2ae69d0e | -16.70638 | -57.43828 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.8 |
| f629b706-55ed-393b-82e3-6edbff8269a9 | -16.5859 | -57.74034 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| f604479f-c937-30a7-a611-1af8a1d6ccdc | -16.5794 | -58.25071 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 91287dc3-852c-3223-aa95-7be5f7ebbf24 | -16.56873 | -57.73127 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 1c9544aa-951f-36ea-ac1b-336dc2d11cb6 | -16.50579 | -57.7351 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| d5e9363d-c7b3-3b9a-8668-236e790df649 | -16.434 | -55.93105 | 2024-10-09 06:14:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 18.4 |
| 3a8e1feb-6359-30f7-9b48-cd219fa757b4 | -16.42497 | -55.9396 | 2024-10-09 06:14:00 | AQUA_M-M | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 17.1 |
| 7f6c3d26-ec2c-32b2-8c1b-24b6f34a77ae | -16.3971 | -57.70185 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| c9857759-c71d-3f04-b19d-12ceededd86c | -16.15186 | -57.41344 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 183cd072-e550-3e0f-b24a-b2b2333dc63e | -16.14997 | -57.40542 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7b0008a3-f7e2-316e-bb92-1f9cc45d5195 | -15.96266 | -57.21647 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| e45498a7-1aa1-3b36-8aee-4e0326131ef7 | -15.96089 | -57.22992 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f76e3110-1293-3ed5-bfb4-c985ea240b6c | -15.9521 | -57.21552 | 2024-10-09 06:14:00 | AQUA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 27.0 |
| f6835b97-0105-378b-b583-e459d6537c5a | -15.72398 | -59.36621 | 2024-10-09 06:14:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4ee2e92c-ee35-3c2a-86c7-3c3ca4561d94 | -15.72257 | -59.37629 | 2024-10-09 06:14:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| d4685644-8fba-34eb-85cf-efe6a66d802d | -15.72202 | -59.44701 | 2024-10-09 06:14:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 63238906-ce1a-3842-a988-5bf795592426 | -15.71339 | -59.37467 | 2024-10-09 06:14:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| e52dba64-502c-32f1-983a-f8d3299b3234 | -15.7078 | -59.41475 | 2024-10-09 06:14:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| db8ba2ba-9834-3774-bbfa-657108e79faa | -15.70277 | -59.38345 | 2024-10-09 06:14:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 4e22bc1d-8999-35cd-b39e-ec7f66fb3eb1 | -15.68226 | -59.40495 | 2024-10-09 06:14:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 07bf864b-e816-3b21-a1e5-6ac08d78ca72 | -15.67307 | -59.40356 | 2024-10-09 06:14:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f62c87b2-9288-3f0d-9085-fa3da870f543 | -15.67166 | -59.41352 | 2024-10-09 06:14:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 9c2b21db-bbe8-322d-a5d0-b02c0b09a6f4 | -15.66744 | -59.44309 | 2024-10-09 06:14:00 | AQUA_M-M | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c5155e86-31d4-3000-895b-cbcb14fcbe6e | -15.61634 | -57.35992 | 2024-10-09 06:14:00 | AQUA_M-M | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 54dd513a-8be1-3715-a33b-a345b5378b2c | -15.61466 | -57.37303 | 2024-10-09 06:14:00 | AQUA_M-M | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 095203c5-1fc2-3b82-845b-4a42c3b79550 | -15.60741 | -57.36648 | 2024-10-09 06:14:00 | AQUA_M-M | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 73e2a07f-ed4b-3dc6-a91e-98f47a71c365 | -15.60598 | -57.35867 | 2024-10-09 06:14:00 | AQUA_M-M | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 11.0 |
| cdd6c9b5-6925-32a6-bad4-95d0835ab85d | -15.42883 | -60.01837 | 2024-10-09 06:14:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 51077b40-9c62-366a-b6e2-21c1f5e288e4 | -14.7541 | -60.02945 | 2024-10-09 06:14:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9d6664eb-9cbd-3fdf-b6d9-3845a2279273 | -13.41704 | -61.92222 | 2024-10-09 06:14:00 | AQUA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 0a6260c6-e54d-3359-b097-dba3559513f5 | -13.40801 | -61.92078 | 2024-10-09 06:14:00 | AQUA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 4d754c11-b0ca-36fb-bfc6-66159ab5800b | -13.40654 | -61.93022 | 2024-10-09 06:14:00 | AQUA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 3b61e21f-4085-30b9-8584-65db52f9ff7a | -13.39751 | -61.92878 | 2024-10-09 06:14:00 | AQUA_M-M | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 60ea3ac1-5fed-3842-83b4-655b193162c4 | -13.01211 | -62.73986 | 2024-10-09 06:14:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 887cf154-3069-3ef1-b148-5fd1758fa174 | -12.98211 | -62.46128 | 2024-10-09 06:14:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| dbb331f4-b4b9-3a44-91d4-cef722482adb | -12.97744 | -62.49106 | 2024-10-09 06:14:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8e9b0b13-7bca-3cdb-87b1-d24b42734cef | -12.96817 | -62.48957 | 2024-10-09 06:14:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 20f97d22-9b1d-3ebf-8686-809a07c8ae1c | -12.93 | -62.73126 | 2024-10-09 06:14:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c1ad2b65-00ff-31d2-8427-1112b58b004c | -12.92224 | -62.71956 | 2024-10-09 06:14:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| fd72153b-97e8-36b8-a511-e7b5bc3999fd | -12.8937 | -62.4402 | 2024-10-09 06:14:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 09ddb765-90d6-3321-89e3-7d7863433570 | -12.89204 | -62.78809 | 2024-10-09 06:14:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 960be7c7-ec55-30f1-8c1c-06d305391598 | -12.8904 | -62.79837 | 2024-10-09 06:14:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 2610b925-5668-3cbf-8751-926c36187221 | -12.85528 | -62.80697 | 2024-10-09 06:14:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1857f602-d809-3e31-b98f-e8b388c4fc71 | -12.82695 | -62.45426 | 2024-10-09 06:14:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5e8c490d-9c95-37c8-80b8-f51befdccad5 | -12.77376 | -62.26718 | 2024-10-09 06:14:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 75676bba-9303-3a21-885f-b085fc2a4fe2 | -12.76456 | -62.26571 | 2024-10-09 06:14:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| af2ebf3e-61b6-30b1-a0f3-5c139828edc4 | -12.76305 | -62.2755 | 2024-10-09 06:14:00 | AQUA_M-M | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 620436bc-6e1a-3e45-85b6-e01fc2484d38 | -12.70902 | -62.95898 | 2024-10-09 06:14:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 26dfc877-d001-33fa-9fc8-e1d5c07bdcae | -12.70734 | -62.9695 | 2024-10-09 06:14:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 71017087-db29-3f43-8c7d-86890fb6b9c8 | -12.70286 | -62.93643 | 2024-10-09 06:14:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 1d02e32c-5355-330a-ad35-f7ca9d922078 | -12.70118 | -62.94693 | 2024-10-09 06:14:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 1f806a54-58e6-3b84-8d7c-095ba5a92201 | -12.6995 | -62.95743 | 2024-10-09 06:14:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 18.1 |
| a1de0be8-17fe-3657-b6fc-80ce00b76740 | -12.69782 | -62.96795 | 2024-10-09 06:14:00 | AQUA_M-M | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 46b3d7c3-092a-3ed2-9296-3c3e2325d736 | -12.67805 | -54.71768 | 2024-10-09 06:14:00 | AQUA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 15.8 |


[Clique aqui para ver as próximas entradas](README222.md)
