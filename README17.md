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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a290303f-cc74-36d7-a9c5-18b09ffea7c9 | -1.5446 | -52.0905 | 2024-10-30 00:52:39 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1aea7261-6840-32ef-9067-9917edb10919 | -1.5463 | -52.097801 | 2024-10-30 00:52:39 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09cd331f-69bd-3b43-9e05-59a02632de07 | -1.5528 | -52.126701 | 2024-10-30 00:52:39 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6d8c545-09a2-3713-bdb7-ec415004c5d8 | -2.7524 | -57.4627 | 2024-10-30 00:52:39 | METOP-B | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 164d3c84-a7fc-3188-a320-619b05f0aca4 | -2.7406 | -57.455898 | 2024-10-30 00:52:39 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7ff792a0-0871-3277-8670-76a22da2e45f | -2.7426 | -57.464901 | 2024-10-30 00:52:39 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 029ba1c0-9965-3568-b301-d687e1b83132 | -1.4775 | -52.294701 | 2024-10-30 00:52:41 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba064881-d72b-32ec-ae0c-7e874cf6997f | -1.4791 | -52.301899 | 2024-10-30 00:52:41 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b3818fd-00a1-3673-b1a7-4ecc090174c7 | -1.4466 | -52.203499 | 2024-10-30 00:52:41 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37a11042-39ce-33f2-9678-28faa4ba079d | -1.4368 | -52.205601 | 2024-10-30 00:52:41 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13cecd6d-9fcc-3567-a082-b9a7c85cc3da | -1.4384 | -52.212799 | 2024-10-30 00:52:41 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 298417c2-7796-3766-917f-a3557d927601 | -1.5928 | -52.940899 | 2024-10-30 00:52:41 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7082bf83-5537-3e11-bab2-a2a224bd790a | -1.5944 | -52.9478 | 2024-10-30 00:52:41 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86baa6af-b6cd-38b1-a6ca-13fca3a3b4ff | -2.3816 | -56.4925 | 2024-10-30 00:52:41 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9c0ac1b7-1699-32a0-8097-96d310050ca1 | -1.5962 | -53.0923 | 2024-10-30 00:52:42 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00665f2a-a6d6-336f-b51b-8d7695fb5a43 | -1.5978 | -53.099201 | 2024-10-30 00:52:42 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09c81652-cbb2-363e-8598-3e6aa652c1f0 | -1.2518 | -51.7537 | 2024-10-30 00:52:42 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72bb5041-4e2f-39d1-9ae2-e11e43265767 | -1.4259 | -52.567402 | 2024-10-30 00:52:42 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7520ea74-20ef-392f-bbdc-392d1a08242d | -1.2726 | -51.936199 | 2024-10-30 00:52:43 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 205c2813-2231-3849-9c12-9113e40d135e | -2.1423 | -55.883202 | 2024-10-30 00:52:43 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a14e0c8-cce6-3976-a3b4-9ff13e12fc87 | -2.1341 | -55.892799 | 2024-10-30 00:52:43 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 104ec955-47c2-3b30-bc0a-910bebf27bcc | -1.6661 | -53.858501 | 2024-10-30 00:52:43 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9deda46b-98fa-358e-a584-7f7a1d8854dc | -1.6677 | -53.865299 | 2024-10-30 00:52:43 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0704f583-5863-3afb-95c8-00e42f9e063f | -1.8851 | -54.8759 | 2024-10-30 00:52:43 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 491289bd-4e0a-3408-ab4e-ef71e1c47317 | -1.3193 | -52.870499 | 2024-10-30 00:52:45 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eeb3e088-151e-3dd4-845f-f607845ae02c | -1.7343 | -54.938499 | 2024-10-30 00:52:46 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f73a0d97-6158-3490-91a9-dc5505254458 | -1.4757 | -54.064899 | 2024-10-30 00:52:47 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b23c8c19-81ec-36f3-bba5-9ee829639449 | -1.4656 | -54.203098 | 2024-10-30 00:52:48 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96eb13a0-6aa5-3e58-84fb-70bd59f9fcc8 | -1.4543 | -54.198399 | 2024-10-30 00:52:48 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6752240a-5f2e-3880-b372-573f01b52ceb | -1.4429 | -54.193802 | 2024-10-30 00:52:48 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0666cc81-1395-3506-a6d4-14ee8b0463cf | -1.4445 | -54.2006 | 2024-10-30 00:52:48 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 271ea83e-e10d-38ee-9b52-7bee7ba4a3ee | -1.4331 | -54.1959 | 2024-10-30 00:52:48 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29f7ac6d-c125-3e89-ac4b-e78a4401e4ae | -1.4347 | -54.202702 | 2024-10-30 00:52:48 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1a30e95-640d-3638-bee4-112d5e8e2d2e | -1.4362 | -54.209599 | 2024-10-30 00:52:48 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d3c77ed-7789-3489-91d0-5b6a21dab4ef | -1.6557 | -55.1842 | 2024-10-30 00:52:48 | METOP-B | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11296b8d-e7d7-3f06-b1f2-e647a27ea12b | -1.6573 | -55.191299 | 2024-10-30 00:52:48 | METOP-B | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2aa3f9f2-63ff-3868-af3c-fa2c414b5290 | -1.2357 | -53.367001 | 2024-10-30 00:52:48 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10a722be-56ad-3735-88e9-7e00b71ce1ab | -1.2372 | -53.373798 | 2024-10-30 00:52:48 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a0c91c1-9598-3d8a-920e-4a19ebb933da | -1.185 | -53.370998 | 2024-10-30 00:52:49 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a97abbd6-d4f5-387e-8173-f557b0725d3e | -1.1866 | -53.377899 | 2024-10-30 00:52:49 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9bb3873-bd5e-38f0-82b2-39ae678df862 | -1.1752 | -53.373199 | 2024-10-30 00:52:49 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37c037ce-8e09-3995-bb0d-121159cbc995 | -1.1768 | -53.3801 | 2024-10-30 00:52:49 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9afea15-e1e3-3c8d-bb76-b726ce20c8f4 | -1.2106 | -53.8951 | 2024-10-30 00:52:51 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3688f7c-6c67-361c-ab58-f5ffaf6bada1 | -1.2121 | -53.901901 | 2024-10-30 00:52:51 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 191b7ddf-eda9-3001-a278-5e5feb874da3 | -1.3578 | -54.593102 | 2024-10-30 00:52:51 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 00bb55d3-9c7e-3a61-a4f9-adb8bdfe4080 | -1.3593 | -54.599899 | 2024-10-30 00:52:51 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 396ea9ec-cab5-3212-bf8a-b16183e72546 | -1.3557 | -54.629601 | 2024-10-30 00:52:51 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 459fc17c-9a98-33c7-ba5b-2aa8db1e71cb | -1.3572 | -54.636501 | 2024-10-30 00:52:51 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9c86303-5520-34c0-9f90-a9030c030310 | -1.3588 | -54.643398 | 2024-10-30 00:52:51 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51c715cf-0314-3e24-8801-3c3878353dfc | -1.6136 | -55.8671 | 2024-10-30 00:52:51 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5174099c-f24c-3fb7-b9ba-bb66a6d8581d | -1.6152 | -55.8745 | 2024-10-30 00:52:51 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c65c9f32-ba23-3f4d-be66-1fe7f559bb50 | -1.1016 | -53.640499 | 2024-10-30 00:52:52 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df64c7f2-365a-3fa8-881a-2cdb9d9aa473 | -1.1032 | -53.647301 | 2024-10-30 00:52:52 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e804880-075b-3769-bdca-a91b156123b0 | -0.7164 | -51.982399 | 2024-10-30 00:52:52 | METOP-B | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| f06009e0-d754-3a5b-9ba2-7e2be37086fb | -0.7942 | -52.325901 | 2024-10-30 00:52:52 | METOP-B | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 00c8b23f-aa3e-3bf0-baf8-00cef5e139db | -1.082 | -53.644901 | 2024-10-30 00:52:52 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a603b201-1fd6-3526-a58a-f3e1ebf3c421 | -1.0836 | -53.651699 | 2024-10-30 00:52:52 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6baeac35-beef-3e22-b4b0-3678fc3b96a6 | -1.1613 | -54.041698 | 2024-10-30 00:52:52 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71696525-0459-3dae-af6b-531b7c770feb | -0.9999 | -53.691799 | 2024-10-30 00:52:53 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 839f0885-f923-3548-93de-f0dfbab41393 | -1.0014 | -53.698601 | 2024-10-30 00:52:53 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 921a4896-55af-3bc3-9f89-12cf00f1ae2f | -1.3206 | -55.708801 | 2024-10-30 00:52:56 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2fc977c-a682-3e29-b046-86bcba8c28aa | -1.3107 | -55.710999 | 2024-10-30 00:52:56 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0bb0350-be4f-3db8-8c44-c7d328ffdbcc | -1.3123 | -55.7183 | 2024-10-30 00:52:56 | METOP-B | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bd18afb-94f0-3e56-9754-053df2b480d9 | -0.1812 | -51.665401 | 2024-10-30 00:52:59 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| be9ef7c5-7a98-3394-a3fd-d7fb9cef5795 | -1.4375 | -60.259602 | 2024-10-30 00:53:10 | METOP-B | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5095ad24-79bb-3652-b57f-c5b9352f46fe | 1.6414 | -50.883099 | 2024-10-30 00:53:26 | METOP-B | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 140a2d2a-edc6-3288-8b7f-e6bdef387490 | 1.6492 | -55.834202 | 2024-10-30 00:53:44 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e695e1ec-e0c5-37de-8e74-6b8a08bf88f7 | 1.6606 | -55.829399 | 2024-10-30 00:53:44 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b402c56-3432-3aad-a7eb-7addf1bec5e6 | 1.659 | -55.836399 | 2024-10-30 00:53:44 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33b68dd1-c3c7-3135-95c5-2b56a78066c2 | 1.6574 | -55.843399 | 2024-10-30 00:53:44 | METOP-B | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58c06a44-c26a-3a50-a575-4c60777d31cd | 3.5422 | -51.2547 | 2024-10-30 00:53:58 | METOP-B | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 369b1a08-77fd-311e-a00d-e28e19e9d826 | 3.5402 | -51.2635 | 2024-10-30 00:53:58 | METOP-B | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| ca9eb7c5-f584-397f-8cb5-11aac734afa5 | 3.5382 | -51.2724 | 2024-10-30 00:53:58 | METOP-B | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 635909b6-1b18-3d1a-8ca4-5cd27bd05b9c | -2.2011 | -50.5852 | 2024-10-30 00:55:18 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 1ffb568a-8010-3f8a-985a-cd4f24528f2a | -2.833 | -49.2413 | 2024-10-30 00:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 148.2 |
| 0a2103ae-0020-3c6e-9249-d42668074e11 | -2.8331 | -49.22 | 2024-10-30 00:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 86867ca0-a0e9-34b6-8f14-79cd8c4f79c7 | -2.8515 | -49.2408 | 2024-10-30 00:55:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 16457e96-ab36-3fe6-a57f-afe0b3d9c417 | -3.0734 | -54.167 | 2024-10-30 00:55:23 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| e4dfe64a-b4af-3d92-9a01-0d019d4d49d2 | -3.1097 | -54.2865 | 2024-10-30 00:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 1e3bfa9a-f74d-30de-9908-5066dedfe2c1 | -3.1098 | -54.2665 | 2024-10-30 00:55:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 1eef0a66-db64-3427-9f45-1a9a24043482 | -3.16 | -50.6231 | 2024-10-30 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| c7ef790c-2529-350d-b9cf-a50e310ec951 | -3.1601 | -50.6021 | 2024-10-30 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 8bb6130b-817a-385c-a623-fb0971588db3 | -3.1602 | -50.5812 | 2024-10-30 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| e36fe2db-49bb-36d0-805d-e8990cf87dc1 | -3.1786 | -50.6016 | 2024-10-30 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 896fd534-2073-3929-bff9-f9fc342d3513 | -3.1787 | -50.5807 | 2024-10-30 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 55434a90-10a1-3016-b9c3-736a9c4c755f | -3.2172 | -50.1811 | 2024-10-30 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.2 |
| f17dc9d9-fe96-3187-b28c-b43b895220c2 | -3.234 | -50.5999 | 2024-10-30 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| fb8521bc-1d85-3b1e-a446-9f6fa461be60 | -3.234 | -50.5789 | 2024-10-30 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 89c76fa4-35db-371e-ad56-33e49b79453d | -3.2357 | -50.1805 | 2024-10-30 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 69a01da3-caa8-3ec7-97ab-3e787acf42a1 | -3.2534 | -50.3689 | 2024-10-30 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 3f54a704-68db-3c5a-8c1c-960f3ecefc75 | -3.2535 | -50.3479 | 2024-10-30 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 129.0 |
| df55e034-6cbd-389a-ad35-3171d2f0c6c1 | -3.2535 | -50.3269 | 2024-10-30 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 5b570128-f39d-3046-8cb5-ea401362a096 | -3.2718 | -50.3683 | 2024-10-30 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.5 |
| 058eb7b9-f6cc-3826-a080-b6a04555595f | -3.2719 | -50.3473 | 2024-10-30 00:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 38d73fe6-4b2b-3f2e-be2e-2be2927e3565 | -3.5171 | -49.2402 | 2024-10-30 00:55:26 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| b03ed011-4f5c-3e86-b392-a6728cbafce6 | -3.5631 | -47.3847 | 2024-10-30 00:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 313.3 |
| be3128a2-e702-3a0d-839c-4614a004ab57 | -3.5632 | -47.3629 | 2024-10-30 00:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 147.1 |
| 6177352d-966d-3918-9dac-5f2142add2d4 | -3.5688 | -50.043 | 2024-10-30 00:55:26 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| e4b06d5f-edf2-33d0-8a4c-4167a89673a8 | -3.5817 | -47.384 | 2024-10-30 00:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 286.1 |
| bf437604-93a4-3162-8684-ab773d8fc9b6 | -3.5818 | -47.3621 | 2024-10-30 00:55:26 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 140.8 |


[Clique aqui para ver as próximas entradas](README18.md)
