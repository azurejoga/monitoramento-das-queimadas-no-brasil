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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 371cab7f-7818-3c09-9463-5eca623fe06b | -5.42028 | -41.07791 | 2025-10-07 04:06:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f03105a2-9699-3f6c-8568-415fc55f433c | -2.8962 | -50.73475 | 2025-10-07 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84843fde-e57e-3ca2-bacb-965900f1952a | -2.99414 | -39.89808 | 2025-10-07 04:06:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d7d541b3-c231-3d91-a594-9d3c7f7b3758 | -4.68394 | -45.83997 | 2025-10-07 04:06:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 11e12e57-e3e1-389b-aafd-81fa8bcec396 | -3.37064 | -42.27238 | 2025-10-07 04:06:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9b3a413d-e45b-322e-92e8-18361083a510 | -3.233 | -45.35084 | 2025-10-07 04:06:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e33240ee-ab11-348e-8b0e-6759e7859196 | -3.14204 | -50.44675 | 2025-10-07 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d87efaec-4cd3-33aa-8576-a89ed70f415a | -3.20142 | -51.01607 | 2025-10-07 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 32c28ebf-a565-353c-95f9-368eef4f268e | -2.26925 | -47.19449 | 2025-10-07 04:06:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bc92500c-a887-3251-93da-b39a49163b5f | -5.02224 | -43.66195 | 2025-10-07 04:06:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f8a75f18-e786-35f5-af05-33592273e958 | -4.06832 | -44.51099 | 2025-10-07 04:06:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d5442f55-d96d-3af2-a316-f4457f413b3c | -3.09724 | -47.01519 | 2025-10-07 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0e5fcbfe-6cd5-3862-907f-fb735a2cb818 | -4.61175 | -43.15195 | 2025-10-07 04:06:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e12116e2-a449-35cf-b9b0-5255ac608900 | -5.39361 | -40.98929 | 2025-10-07 04:06:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 96593d64-f5b4-3af2-be47-58ccb89e4f69 | -4.20032 | -38.12297 | 2025-10-07 04:06:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 20908d08-b80a-3c9f-b6e7-fd2a8b18e553 | -5.39031 | -40.98878 | 2025-10-07 04:06:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 1e7392f4-5ad8-30bd-b861-50107ea896d2 | -2.26854 | -47.1989 | 2025-10-07 04:06:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4d6c0ba1-1d5a-3a03-8785-9aeeaaef42b7 | -4.31901 | -46.80713 | 2025-10-07 04:06:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2cc4c1b8-e754-3c91-a540-4ee414c41dc1 | -3.61248 | -50.21051 | 2025-10-07 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a7c91d3-7b2f-30e3-ac74-82954b6de6d9 | -4.13989 | -47.6589 | 2025-10-07 04:06:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c7671f20-215b-37c5-b74b-3b4117a571f9 | -3.14161 | -44.41695 | 2025-10-07 04:06:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4973b02b-42e0-38cc-b14c-ed6049d24816 | -3.11626 | -40.99202 | 2025-10-07 04:06:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 51833276-0fe1-31eb-a241-fcb53be3e9f1 | -4.64283 | -43.19885 | 2025-10-07 04:06:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b8d59b17-e0a0-3f3f-b1f3-ced29b10c1ff | -3.09154 | -47.0229 | 2025-10-07 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3cada0c7-32c6-3957-a3d8-2e95ca4be656 | -4.44649 | -43.21868 | 2025-10-07 04:06:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a74eba3-7822-3a1f-887e-4120b323afc7 | -2.90246 | -50.73183 | 2025-10-07 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae1e3718-9f9a-3a71-95be-547a1ec93e35 | -5.27278 | -39.28488 | 2025-10-07 04:06:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 70e9e7dc-0fc5-3d8c-9573-ad54f575a39e | -3.14091 | -44.42133 | 2025-10-07 04:06:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad77d882-c6e7-38ab-a88a-be61bb0cb913 | -3.58547 | -41.64408 | 2025-10-07 04:06:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a42688fc-5aba-3c45-a0ab-a2b1c92629b2 | -5.37552 | -40.99705 | 2025-10-07 04:06:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| a32a41f2-1164-3baf-a6be-bdbfabe7d9f4 | -3.14264 | -50.44317 | 2025-10-07 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d6cfeb8-d6d1-3c45-ac09-2460ef054c14 | -4.5179 | -40.93197 | 2025-10-07 04:06:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d2e6e655-4fc5-3d0b-874f-867e4265d88e | -2.24472 | -47.86989 | 2025-10-07 04:06:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 45f1629e-ad59-32ae-8cb4-df36b486150a | -3.10093 | -47.02007 | 2025-10-07 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b742d3d1-0dec-38c0-93a3-dc47646c087d | -3.66574 | -51.95295 | 2025-10-07 04:06:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8cd5a02b-3ef6-3b15-ad38-f9e26c085ff3 | -3.09288 | -47.01455 | 2025-10-07 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8bce95af-0613-3aa9-bd9a-46d4ddfba77b | -2.89057 | -50.73384 | 2025-10-07 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2bae64d3-2557-3398-96c3-b4c60eb84f24 | -4.07595 | -43.33941 | 2025-10-07 04:06:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3e924d4d-93a7-3eaf-b475-30d8e23cafda | -5.39085 | -40.98534 | 2025-10-07 04:06:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| b34cddb7-47c4-3ed8-b6bb-8613798dc0da | -5.20722 | -37.62666 | 2025-10-07 04:06:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 932a5257-f021-3f0f-82e6-cc96f87863b9 | -3.09657 | -47.01939 | 2025-10-07 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d6b02051-fa89-3c89-9f6f-6591f35c1bea | -2.14336 | -47.50856 | 2025-10-07 04:06:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9de29c14-9e32-36a3-a2ef-d92bfd7bc82f | -4.44187 | -43.22564 | 2025-10-07 04:06:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb468100-2a8d-3019-8093-55168f3cae15 | -3.6709 | -39.61473 | 2025-10-07 04:06:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 174c1659-f9d6-3786-868d-f23b3b10950b | -4.67242 | -44.85775 | 2025-10-07 04:06:00 | NOAA-21 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 14861023-9f7b-3618-b162-684a30d2ced6 | -3.08569 | -51.24907 | 2025-10-07 04:06:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ac39ce93-1fe3-329f-8400-2aa582876f87 | -3.09221 | -47.01873 | 2025-10-07 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6638eaed-f53c-3854-ba02-75509dbfb4e7 | -4.14367 | -47.66384 | 2025-10-07 04:06:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a09cb41a-5e06-365a-a1c3-7ec6eaa400f9 | -4.90699 | -43.43614 | 2025-10-07 04:06:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 828a0987-fb94-3adc-a765-c46f430775ec | -3.87797 | -38.42987 | 2025-10-07 04:06:00 | NOAA-21 | EUSÉBIO | CEARÁ | Brasil | 2304285 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e0cb9643-c55f-3098-b7b7-cd53deab0271 | -4.68312 | -45.84507 | 2025-10-07 04:06:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 519fcf3c-bb0c-3d79-8ba7-ced604993ecc | -3.87986 | -41.54893 | 2025-10-07 04:06:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 31695e33-8fda-3342-b5e0-6c64f14241da | -3.0959 | -47.02359 | 2025-10-07 04:06:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3df95060-7e4a-3ffc-ae70-74911830f9db | -5.41699 | -41.0774 | 2025-10-07 04:06:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 63ebf50a-d336-34b7-892d-b178cdda262a | -4.44696 | -43.23796 | 2025-10-07 04:06:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72abef15-3266-3aa5-80c4-7f6c8685ec88 | -3.66648 | -51.94855 | 2025-10-07 04:06:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bb454fd-8200-3dc1-b015-50cfef88ea98 | -5.55241 | -37.31779 | 2025-10-07 04:06:00 | NOAA-21 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| de8e1059-0b10-30b9-9c5b-a38ae0f6d666 | -1.61381 | -46.66269 | 2025-10-07 04:06:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 16ee23df-8d4a-3dd5-ac29-b9f018d8d1a1 | -3.33733 | -46.54503 | 2025-10-07 04:06:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 58ce14fa-5a31-38e9-9e30-0630308c8c60 | -4.4459 | -43.22242 | 2025-10-07 04:06:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d81e011-ddf8-3953-bec4-f430d8f9ed48 | -4.55283 | -38.23564 | 2025-10-07 04:06:00 | NOAA-21 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 47f0c601-ee60-3880-b3dc-a19153e878af | -4.4903 | -46.3667 | 2025-10-07 04:06:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5695bf3d-d085-338f-a991-7debac97f8fd | -3.13655 | -50.44583 | 2025-10-07 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| acb053c6-d6d6-3d04-bc1a-21759d02d9e2 | -3.0915 | -51.24998 | 2025-10-07 04:06:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2c0ebc5a-6cce-3f0c-98bc-4539b83a9a68 | -3.61191 | -50.21391 | 2025-10-07 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4f7f8a0-a906-3372-907e-23a0f0ece613 | -3.08621 | -50.57647 | 2025-10-07 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cf08cf46-6afc-3e92-ad02-731336437447 | -4.4453 | -43.22617 | 2025-10-07 04:06:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca455e67-31c6-33ff-b0ff-22e007ef68d0 | -3.09733 | -50.57822 | 2025-10-07 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a6029ccb-190d-3877-91e1-4b44f29b5fad | -5.39307 | -40.99273 | 2025-10-07 04:06:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| d2159f40-59d3-3822-a54f-6dff406e2be0 | -3.88041 | -41.54548 | 2025-10-07 04:06:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 856e13a9-c38d-3e10-8a64-868309364fa0 | -5.38924 | -40.99566 | 2025-10-07 04:06:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1ebddd9e-c199-3301-9ff3-32bdf2aef01a | -3.709 | -42.32913 | 2025-10-07 04:06:00 | NOAA-21 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b621f86b-5618-3ec5-8e50-9bc9b91d1034 | -4.06536 | -44.50612 | 2025-10-07 04:06:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c4a35887-f8a9-3e13-b7d8-58125442bc0d | -4.45532 | -38.44539 | 2025-10-07 04:06:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 5d99a191-8eac-30e8-a87f-69d1216539d4 | -3.36728 | -42.27186 | 2025-10-07 04:06:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 30858dfe-9628-3612-980c-a1cd36198395 | -4.93414 | -43.42109 | 2025-10-07 04:06:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc42100f-e1b3-3866-a106-51c2b25c3db4 | -5.01937 | -43.65758 | 2025-10-07 04:06:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac01dc67-2dff-3b95-a8f1-9815f5c9d3e3 | -3.72848 | -40.01198 | 2025-10-07 04:06:00 | NOAA-21 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b961738d-2aa6-3a0f-8755-ec228ba247d4 | -5.38977 | -40.99222 | 2025-10-07 04:06:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 35234bdf-1b76-3363-9df2-87866876d973 | -4.64343 | -43.19511 | 2025-10-07 04:06:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 82702956-f0eb-3a72-abe4-00f6f9144b72 | -3.09667 | -50.58212 | 2025-10-07 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d1727fcc-1595-342d-8401-0aa1c5182e3a | -3.35747 | -43.37896 | 2025-10-07 04:06:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3cb69382-7a90-3074-a9ed-82d4995d4f2a | -2.99082 | -39.89755 | 2025-10-07 04:06:00 | NOAA-21 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8144e4bd-6326-3255-b19f-965185472056 | -2.55722 | -47.65794 | 2025-10-07 04:06:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d63361e4-2b90-3208-b923-b05535257e38 | -3.20367 | -51.01528 | 2025-10-07 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9e19a22c-0d9e-3aea-9d76-7025704747f3 | -4.44755 | -43.23421 | 2025-10-07 04:06:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1ed178fc-dbc2-3d50-aef1-05750ef19bda | -4.45277 | -43.2235 | 2025-10-07 04:06:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2ef9387-d65e-38c2-9e56-6880f2d98c56 | -3.203 | -51.01915 | 2025-10-07 04:06:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24f2ab54-dad5-3d72-b070-aeaea8d62328 | -3.09113 | -50.58113 | 2025-10-07 04:06:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ada34d89-84d7-31d8-b4a9-e02358531a3d | -5.0251 | -43.66635 | 2025-10-07 04:06:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aa4cef34-ae5e-37bc-b06f-5c07df5cc40b | -5.77922 | -45.74114 | 2025-10-07 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42489d30-0ed2-328a-8f4e-87bb82271f76 | -11.09829 | -47.20391 | 2025-10-07 04:08:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29b31aed-5969-3832-9135-732ff7977dfd | -5.29484 | -42.5461 | 2025-10-07 04:08:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e8fbdab7-2369-31e7-bc47-c73b4fa0bed5 | -7.46808 | -43.09286 | 2025-10-07 04:08:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fc993ac3-6b6e-3bd9-9253-af92436d324c | -8.93523 | -49.85542 | 2025-10-07 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 054ce470-69cb-321b-a4e0-27f3e8222856 | -8.87698 | -47.68192 | 2025-10-07 04:08:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 344b186b-7f1a-3f5f-be80-85566562e456 | -10.57941 | -51.4728 | 2025-10-07 04:08:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0a024079-dcfe-3ba0-a992-ad320efc008b | -9.95675 | -43.75208 | 2025-10-07 04:08:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 518ede4a-5830-3f26-99e9-651de9396348 | -11.50469 | -44.97066 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2436a529-292f-3679-b6dd-b94361e117a9 | -5.41454 | -43.97755 | 2025-10-07 04:08:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README21.md)
