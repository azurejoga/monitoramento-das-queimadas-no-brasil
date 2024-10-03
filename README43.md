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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b063c9e-c694-3e10-84a6-5864a1be942c | -9.312 | -65.362198 | 2024-10-03 01:51:08 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 96612d9a-7236-3e71-a7fe-15b2b91f4c5c | -9.6385 | -66.802399 | 2024-10-03 01:51:08 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2d22677d-5142-388d-9f43-824c47e9b6fb | -9.2938 | -65.327904 | 2024-10-03 01:51:08 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ecafcdf6-d066-33a0-945a-e254f4b82085 | -9.2955 | -65.335197 | 2024-10-03 01:51:08 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 65e82f19-1d66-3bec-8bc8-a69e18c6ea71 | -9.2989 | -65.349899 | 2024-10-03 01:51:08 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 27411441-be5f-3941-95fa-923e0f33c47b | -9.3005 | -65.357201 | 2024-10-03 01:51:08 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c0e6448b-ecf7-33ba-8596-9a64d23a0279 | -9.3022 | -65.364502 | 2024-10-03 01:51:08 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6a1acd96-5933-3f1c-bd95-2dd8b09206ab | -9.3039 | -65.371803 | 2024-10-03 01:51:08 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 83eac2ca-661c-3dd7-9f8a-34eda4d71c57 | -9.5593 | -66.587402 | 2024-10-03 01:51:09 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b664ed4c-49cf-346d-be27-d422e2d20f0f | -9.5608 | -66.594299 | 2024-10-03 01:51:09 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 108d87b2-939f-3b46-a235-73703dcd37b1 | -10.1689 | -69.350899 | 2024-10-03 01:51:09 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 9ace007e-ff68-373b-996c-bb8b628e80d6 | -8.581 | -62.408501 | 2024-10-03 01:51:09 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e7d9e6a2-351c-3d74-8cc6-dda7c93ba13e | -9.3683 | -65.789803 | 2024-10-03 01:51:09 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 994cfdf7-7f21-3e16-b83d-1731585bf2af | -9.3667 | -65.827599 | 2024-10-03 01:51:09 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8149a09f-7d5d-3b66-8395-0dcd54d9ab44 | -9.3684 | -65.834702 | 2024-10-03 01:51:09 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 52a46c35-b8a3-3710-a5fa-b1549b6c06b3 | -9.0364 | -64.434898 | 2024-10-03 01:51:09 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d43b0167-9129-3a8d-a5ee-3d33ca10d2ae | -9.0383 | -64.442902 | 2024-10-03 01:51:09 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 65881e54-1dcb-3663-9bb4-189724402792 | -10.0012 | -68.720596 | 2024-10-03 01:51:09 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 466f7108-2111-3a9a-b51b-1ca7b97190f7 | -8.5565 | -62.478901 | 2024-10-03 01:51:09 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| df2537b2-c9b4-3792-bfcb-55a9bd5c58c2 | -9.0206 | -64.455399 | 2024-10-03 01:51:09 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 22df5f2d-3ed3-3702-bc5c-33076111cafe | -9.0224 | -64.463303 | 2024-10-03 01:51:09 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 8cf6b674-4455-34fd-af48-4244a19b780a | -9.241 | -65.592598 | 2024-10-03 01:51:10 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 45a8ce47-5f13-3964-8540-04e0abc004ef | -9.2427 | -65.599899 | 2024-10-03 01:51:10 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 57dcb82f-849c-3d88-af8c-a5ef1dc6d292 | -9.4632 | -66.572701 | 2024-10-03 01:51:10 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 81cb37a7-a2c0-397b-8496-ea8aa8cd9dbb | -9.4648 | -66.579697 | 2024-10-03 01:51:10 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| aa19d9b7-565c-329d-8a9d-6c9b156eb7f8 | -8.9458 | -64.355499 | 2024-10-03 01:51:10 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 084addd2-842e-3fd0-91e2-1291e6e8e0f1 | -9.6306 | -67.458504 | 2024-10-03 01:51:11 | METOP-B | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 44902787-1a23-376b-8e5f-66a65ac86afb | -9.6321 | -67.4655 | 2024-10-03 01:51:11 | METOP-B | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 98817d2d-d105-38f0-8b74-09f709c1ec2c | -9.6208 | -67.460701 | 2024-10-03 01:51:11 | METOP-B | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| c01cf1b8-b1b0-30a3-9883-78e47897b49a | -9.6223 | -67.467697 | 2024-10-03 01:51:11 | METOP-B | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 4c5eb566-7114-35db-b51a-db7d03df8563 | -8.5938 | -63.115601 | 2024-10-03 01:51:11 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f8e7026f-4cbf-3483-bc2f-04809d4e93c7 | -8.596 | -63.124901 | 2024-10-03 01:51:11 | METOP-B | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 588fea6d-ec0b-38a4-a030-81b2e99a68c5 | -8.1651 | -61.360001 | 2024-10-03 01:51:11 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8e343ec6-0bb7-32d9-8346-f8f06eebb149 | -8.168 | -61.372101 | 2024-10-03 01:51:11 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 539937cb-b2d2-31e7-89fc-f53d08c1cba1 | -9.4961 | -67.132301 | 2024-10-03 01:51:12 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b6185131-8b93-32b0-ac40-36feb6b5c99d | -9.4976 | -67.139198 | 2024-10-03 01:51:12 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eed4b863-387c-3d85-8a1e-bfac98e09a71 | -8.4509 | -62.642101 | 2024-10-03 01:51:12 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9a36d9ff-51e3-333b-9024-3ab429969351 | -8.4533 | -62.6521 | 2024-10-03 01:51:12 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5120709e-7dd2-331f-aa9d-688fa70adb0c | -8.4556 | -62.661999 | 2024-10-03 01:51:12 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 14b9acac-2eb8-34ec-aa44-227c201c63f5 | -9.7481 | -68.409401 | 2024-10-03 01:51:12 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 0f39c720-c41d-3c5f-8d70-8846a075734a | -9.7497 | -68.416603 | 2024-10-03 01:51:12 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 90ee86a2-8912-30da-aca6-91be2e9ce339 | -9.7288 | -68.368401 | 2024-10-03 01:51:12 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 3b7ab1a9-0965-3054-8929-13170d04af2c | -9.7304 | -68.375603 | 2024-10-03 01:51:12 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 991074d1-521e-324c-bf1a-de326d6f1329 | -9.7383 | -68.411598 | 2024-10-03 01:51:12 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| ac7807e7-bf5b-3466-a9ad-df1ef5bf0c1e | -9.7399 | -68.4188 | 2024-10-03 01:51:12 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 05af86a3-601b-3b72-9598-4fa19f296d64 | -9.7301 | -68.420998 | 2024-10-03 01:51:12 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 86ad8088-169e-3b88-bd4d-1d977a0d16fd | -9.7317 | -68.4282 | 2024-10-03 01:51:12 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| de526ae7-44ea-36d1-a9b2-11b04c892491 | -9.8245 | -68.899498 | 2024-10-03 01:51:13 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 7a1d51ed-9c55-3ab5-bdde-7270dd619a45 | -9.308 | -66.615303 | 2024-10-03 01:51:13 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a2f0e3d9-f5ea-36a4-8a5f-6e303d2d1849 | -9.3095 | -66.6222 | 2024-10-03 01:51:13 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3faba54d-0e6f-3f96-b754-cf55e27b1626 | -8.7405 | -64.181999 | 2024-10-03 01:51:13 | METOP-B | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9c61776c-1833-359f-abcb-6143a5a6ab09 | -9.4233 | -67.221397 | 2024-10-03 01:51:13 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d401b549-3016-39a2-b399-3a4b9517bc08 | -9.4249 | -67.228302 | 2024-10-03 01:51:13 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 73723b4a-2692-30d4-b3b5-5a3e9a2539e6 | -9.4264 | -67.235199 | 2024-10-03 01:51:13 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7cda6147-416b-3f27-8594-8ebef0264e24 | -9.4186 | -67.338699 | 2024-10-03 01:51:14 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0279a32f-6492-3b7f-94d2-4c6fb63efa8d | -9.4202 | -67.345596 | 2024-10-03 01:51:14 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bdbcd019-4a72-3909-b394-3454f94b5aaf | -9.4169 | -67.608597 | 2024-10-03 01:51:15 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0015dde5-9794-308e-ad6d-90949b106b57 | -9.4185 | -67.615601 | 2024-10-03 01:51:15 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c4aea547-5181-3b5b-8e9c-74168b463e0e | -9.6424 | -68.630501 | 2024-10-03 01:51:15 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| c18d0241-386f-3a1e-aa69-8685f78f866d | -9.6793 | -68.799301 | 2024-10-03 01:51:15 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 372d653a-182a-341d-a55e-5da521e86506 | -9.6809 | -68.806702 | 2024-10-03 01:51:15 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| eace68ae-5ce0-3710-b22c-89b86c43bd64 | -9.3561 | -67.381798 | 2024-10-03 01:51:15 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 02442342-edeb-3d87-a006-d331c831f5ff | -9.3577 | -67.388702 | 2024-10-03 01:51:15 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6993c748-9e77-3099-a9da-17c3f316b9b8 | -9.5486 | -68.250603 | 2024-10-03 01:51:15 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| e4ac7665-44ce-32b9-9cb8-2519033ea0ba | -9.5502 | -68.257698 | 2024-10-03 01:51:15 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 6313a996-30ac-34b1-a671-e2afb353b8cb | -9.5518 | -68.2649 | 2024-10-03 01:51:15 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 4dcbcd02-2627-3d5f-81cf-7da64f9cbfd5 | -9.631 | -68.625298 | 2024-10-03 01:51:15 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 71990fce-2b64-33c6-b580-ce63bec5affb | -9.6326 | -68.632599 | 2024-10-03 01:51:15 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| bdfa3920-2f64-3c6c-bd05-0eb617dcc4ac | -9.6342 | -68.6399 | 2024-10-03 01:51:15 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 731b3391-ea3b-3000-9f81-07077f8957e5 | -9.6695 | -68.801399 | 2024-10-03 01:51:15 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 330b128e-9876-365c-98ea-c87fe1083dad | -9.4935 | -68.047096 | 2024-10-03 01:51:15 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 3d41060f-0242-3378-a4c5-f51c00b29749 | -9.4951 | -68.054199 | 2024-10-03 01:51:15 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 0911bc6f-14bc-3c6c-9134-a4a56d06d72c | -8.3906 | -63.348202 | 2024-10-03 01:51:15 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f6540324-3a97-3c66-a2f0-2e6b7455e7b3 | -9.579 | -68.575798 | 2024-10-03 01:51:15 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 4381997b-5744-347f-9463-21338bbf2e85 | -9.5806 | -68.583099 | 2024-10-03 01:51:15 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| a682325a-1eb3-328d-9c3f-0c365b91567a | -9.5822 | -68.590302 | 2024-10-03 01:51:15 | METOP-B | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 509b12ea-5082-3534-922f-0c10f4e62fc6 | -8.3808 | -63.350498 | 2024-10-03 01:51:16 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a37e16f3-748a-3512-b0a1-fde820041981 | -9.6627 | -69.052696 | 2024-10-03 01:51:16 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| adcd9006-d654-3d48-8ae6-69d813a45758 | -9.3818 | -67.821404 | 2024-10-03 01:51:16 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 33c2b4f7-9e52-31a2-a437-52264a97826c | -9.3833 | -67.8284 | 2024-10-03 01:51:16 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7f64d3ce-1ba4-37f0-8af4-5badbfe21e8e | -9.3849 | -67.835403 | 2024-10-03 01:51:16 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 766ab7c2-7b50-38d6-a86e-63cbc1ab6593 | -9.3735 | -67.830597 | 2024-10-03 01:51:16 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f1c2a9a9-b90c-3b81-be75-a2ca6041ebd0 | -9.5065 | -68.432701 | 2024-10-03 01:51:16 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| f03650b0-f9ef-39f4-bdc8-8c76666179d8 | -9.5081 | -68.439903 | 2024-10-03 01:51:16 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 4612ad32-923f-37e7-8c0e-4ae9e1301b3b | -9.5096 | -68.447098 | 2024-10-03 01:51:16 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 013c9038-4835-3f63-b3f4-5eba13ed9f1c | -9.5093 | -68.4925 | 2024-10-03 01:51:16 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 3a1f2556-dd85-3478-a81f-6aeca7e9584a | -9.4964 | -68.480202 | 2024-10-03 01:51:16 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| cbb457ae-10ba-3369-8f4c-20d307f2f487 | -9.498 | -68.487503 | 2024-10-03 01:51:16 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| dbcc9dfa-b7b0-3d74-b899-f3ac61d1aaab | -9.4995 | -68.494698 | 2024-10-03 01:51:16 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 41496e45-1f80-36e9-accf-180a3b580adc | -9.4866 | -68.482399 | 2024-10-03 01:51:17 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 4c40b8ba-12da-376b-b13b-18575e5c31ca | -9.4882 | -68.4897 | 2024-10-03 01:51:17 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| c6d3682d-41e5-36fb-a498-a3708e779f11 | -9.4897 | -68.496902 | 2024-10-03 01:51:17 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 90e6e0a4-50b7-31d2-b771-7cd152c149e3 | -9.2801 | -67.595398 | 2024-10-03 01:51:17 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6cc84f03-961f-3585-9098-706a093492cd | -9.4013 | -68.141701 | 2024-10-03 01:51:17 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| a99f3657-fbd1-3469-a015-cc3f716cabfa | -9.4028 | -68.148804 | 2024-10-03 01:51:17 | METOP-B | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 12ef570e-d236-310d-9662-dea158529341 | -9.4879 | -68.535202 | 2024-10-03 01:51:17 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 52147f8b-cad9-3278-9bcb-500b50e77350 | -9.4894 | -68.542397 | 2024-10-03 01:51:17 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 14c1c05b-56df-315c-83bd-af2b62857d5a | -9.491 | -68.549698 | 2024-10-03 01:51:17 | METOP-B | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 1119ce11-f394-3b9a-9007-bd62e23bfbec | -9.2688 | -67.590698 | 2024-10-03 01:51:17 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 693264e6-ddee-3eec-af0a-898e82dd0af5 | -9.2703 | -67.597603 | 2024-10-03 01:51:17 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README44.md)
