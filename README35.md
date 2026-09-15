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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a3aa220-6819-3c45-9aa0-c61cc5378f27 | -4.36129 | -47.78159 | 2026-09-15 04:32:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 64ee0261-665d-3729-8e79-bee02b849800 | -1.98993 | -47.0392 | 2026-09-15 04:32:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b112b506-37af-3eaf-96bd-c3a95d12380a | -5.89904 | -52.10169 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bdfb069c-3cea-32be-aadf-71893757dd03 | -5.41487 | -48.5334 | 2026-09-15 04:32:00 | NOAA-20 | ESPERANTINA | TOCANTINS | Brasil | 1707405 | 17 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1d41b262-d65e-3454-801c-f22a74549424 | -3.84852 | -51.76046 | 2026-09-15 04:32:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5a9a67c4-fdf1-3658-9386-ae1cdfb26697 | -1.22259 | -54.12608 | 2026-09-15 04:32:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0227ad49-1500-3db3-ac78-8a1742c00969 | -2.91895 | -50.40344 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 29067b02-426e-3fa0-9af0-affcdb36a89b | -8.2101 | -43.78472 | 2026-09-15 04:32:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8735c14e-74be-3943-983c-1f83e94c021a | -7.23522 | -46.15794 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 05f12446-5d4d-3f9f-8490-9554a1110be1 | -6.26224 | -41.97392 | 2026-09-15 04:32:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| db4ef762-5349-307f-ad76-de47b694be78 | -7.09581 | -43.53666 | 2026-09-15 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dd3f7d7b-7763-363a-85db-c6b919d24039 | -2.91021 | -50.40723 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 01c10e1a-a0d0-3be6-8e10-a48cd962f662 | -6.1572 | -52.73562 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab61eef2-1317-3559-bc1e-e690439ca502 | -1.46635 | -52.96959 | 2026-09-15 04:32:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 98e020d1-0bde-3600-89ee-a93c48d3d31d | -6.16137 | -55.71107 | 2026-09-15 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6859039a-c488-3b3e-a3f8-46d05cfd794b | -4.51622 | -54.97285 | 2026-09-15 04:32:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 113c26c8-15ad-3760-80a5-28e8b006ba05 | -6.07462 | -57.86569 | 2026-09-15 04:32:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0803b3e-fe88-3d59-9e37-e76c52646b6f | -7.09947 | -41.81244 | 2026-09-15 04:32:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e5763406-a3b8-39a8-93f8-609dbd130812 | -6.69874 | -51.17425 | 2026-09-15 04:32:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e92c839e-27a9-313c-8cd0-f221e1c29b42 | -4.53925 | -55.62037 | 2026-09-15 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3be0171c-89cd-32b1-8abc-e15e3eddeb7e | -1.22753 | -54.09595 | 2026-09-15 04:32:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 19a3761b-f36f-3883-a510-1e237f41ab31 | -2.91646 | -50.41866 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 62913097-9add-33cc-8fe6-86021e3a4755 | -2.95928 | -50.4048 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8768ca7-919c-3008-9e1f-fa7eafd5b94e | -3.0454 | -51.26805 | 2026-09-15 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1ef4e5c-6a8e-3a03-b60d-f2aba521215a | -5.0757 | -56.24554 | 2026-09-15 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6dee2819-8db8-3e03-9732-3648876e6f75 | -4.38937 | -55.20931 | 2026-09-15 04:32:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0e71008-098f-3157-b624-5f98471e45e9 | -4.5226 | -54.96726 | 2026-09-15 04:32:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0bff917f-a95a-3e67-be48-59f94520159c | -2.89105 | -50.42495 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 76e4d435-96ff-3df2-909a-3fad52cd4bfd | -4.65453 | -42.44123 | 2026-09-15 04:32:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0a61c3e1-cd0b-3aa2-ae53-5ff7737a907c | -7.0968 | -47.47862 | 2026-09-15 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2a4dc17-8240-3822-859a-496fa724f4be | -3.61559 | -45.52685 | 2026-09-15 04:32:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c90f0227-3b6e-36ad-b47e-3dbeed9a23fc | -2.91729 | -50.41359 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0d0f8564-a680-346c-be7f-400c266f8ab1 | -6.70267 | -51.17488 | 2026-09-15 04:32:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 631ac33a-9d3d-350e-aefb-10944a5bd1f0 | -2.90479 | -50.39082 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fb774595-510a-3d5c-af4b-702fc5465e12 | -6.94667 | -42.55947 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5802ad31-86c5-39ee-b3f6-aacf242079ac | -3.05675 | -46.92741 | 2026-09-15 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c778df38-1439-3782-a554-4c730c7351da | -7.12804 | -45.86612 | 2026-09-15 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 927abe27-ee5c-3998-b66b-ffc9ff4f8315 | -6.33651 | -39.38865 | 2026-09-15 04:32:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 747c633a-6c4e-3193-8088-cd8fdcf32b04 | -3.42477 | -58.21334 | 2026-09-15 04:32:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64960e75-5a21-3dca-b50f-6402fe2e02f0 | -4.16889 | -44.10151 | 2026-09-15 04:32:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 22f72c05-b644-3a15-9556-cdf011ee95b2 | -2.88792 | -50.42783 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f53358fd-0c98-30b2-ba5c-630dc55a0634 | -3.84577 | -49.05646 | 2026-09-15 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4b29e9c-d2e9-3894-9df6-e1ae8878d22d | -6.00578 | -52.18951 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 942452e6-43fa-3e00-ae20-d6981acb83f6 | -5.15589 | -49.43563 | 2026-09-15 04:32:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fa692d8b-3a46-3cb2-b7ee-f647222abc04 | -7.08006 | -42.13316 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| dbb51fef-a86f-3fa7-9424-cfaed747bee2 | -3.48584 | -50.37754 | 2026-09-15 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ddc77df3-874b-3492-adab-b69ef1663c9e | -7.01871 | -44.62853 | 2026-09-15 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3b2478f-f756-311d-8f14-486f82cb79f7 | -7.13752 | -42.09899 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 92c81049-b1c5-364c-bac9-7eec906918e3 | -4.51678 | -54.96967 | 2026-09-15 04:32:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5912db12-addc-3fd8-b849-bedd63e30e1a | -7.01528 | -44.62798 | 2026-09-15 04:32:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e3bddcb-66d9-3000-a9ea-c9f1b7a7d4c0 | -2.89272 | -50.41481 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7d3a814a-ee87-332a-8456-5282cefa2961 | -3.33692 | -54.19319 | 2026-09-15 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5dc3a476-7b40-3e49-8873-87fac9a7bf49 | -7.29511 | -42.35287 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6c76ba7f-e859-38b8-9076-7c68c0965731 | -4.56965 | -54.91306 | 2026-09-15 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d422ecea-ffa6-3218-8983-78c19163377a | -7.24517 | -46.15949 | 2026-09-15 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 577ea940-ca15-3b36-91ca-b650f0dba486 | -7.73666 | -44.71627 | 2026-09-15 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39bd4a77-412e-3d39-b3c9-a1e55171452f | -6.32672 | -44.1193 | 2026-09-15 04:32:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4587038d-81e0-38ba-998d-389d68a33c06 | -7.07617 | -42.13255 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f613c63f-81ae-345d-a29b-a1b8f1580447 | -2.88709 | -50.42431 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7724be5d-8797-3a73-983a-b766051de54d | -8.39626 | -42.22132 | 2026-09-15 04:32:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3b7147db-6e23-3790-a74c-c6e07d6f86d6 | -3.38264 | -50.39404 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 091100bc-2cb4-3bfe-a5c7-b2de68f84202 | -6.02274 | -51.78655 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08c18e1e-78e5-3286-8c65-6cca235174ce | -2.96009 | -50.39975 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7fa1d2a7-21ca-309e-afdb-203698604697 | -1.79195 | -47.83921 | 2026-09-15 04:32:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bcc95bc3-2cba-3caf-baeb-f95c185ebf95 | -3.52868 | -49.37449 | 2026-09-15 04:32:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ad0462b5-cbbd-30ff-9357-90d7c4d936ea | -5.90751 | -52.10294 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 21df26bf-72d3-3a28-a516-4aa0b95ce9df | -7.9755 | -44.02426 | 2026-09-15 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6d61ca85-e506-3853-bd60-bfac7b995de4 | -2.91958 | -50.42439 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7011af77-3fad-3b2f-b023-fb74d3a4129a | -2.89896 | -50.42624 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 06f8a9af-1adf-3329-9d33-49ea0b262f49 | -5.929 | -53.54979 | 2026-09-15 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8cbee6a5-72bf-3bdc-a702-2c1f39a95d76 | -6.16084 | -52.74081 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0228ee92-bf87-3e71-9d46-04a8367e5f28 | -6.10503 | -55.6702 | 2026-09-15 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e73d9b1d-fefd-374c-8935-fa39f5290d8a | -5.8555 | -52.10366 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4880136-dd16-341b-9b4e-95166ea0d733 | -8.21371 | -43.78524 | 2026-09-15 04:32:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d6012921-8a89-3b26-a532-913d5f9a2da7 | -6.78209 | -48.66591 | 2026-09-15 04:32:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0a02cb21-3106-3349-9774-9c1e2e56f095 | -7.17774 | -43.59037 | 2026-09-15 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4bb09ae7-76e6-3aed-9eeb-ae79c922aec6 | -6.65896 | -43.6515 | 2026-09-15 04:32:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d549921f-0c5d-3d1d-b692-20e02050ff77 | -3.33184 | -54.1924 | 2026-09-15 04:32:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 67f502fe-31a5-3de9-a67c-6220cbc9c5b5 | -6.61493 | -44.20082 | 2026-09-15 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2efa2cd8-12d0-397e-9557-8ff5db29f821 | -3.39881 | -50.75984 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a223233e-bc2d-3906-b2f3-3380df6811e1 | -7.08152 | -42.12336 | 2026-09-15 04:32:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 38bd4b6e-ad8f-31a0-888f-579bde7bcf62 | -5.49497 | -45.60602 | 2026-09-15 04:32:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c25ba504-a021-3e5c-a443-668ecab93a6f | -5.13432 | -55.94421 | 2026-09-15 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b209b65d-c04e-33b4-8c0b-08f7ad4ad246 | -5.19453 | -49.33501 | 2026-09-15 04:32:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2e89cef-58e5-3a29-9793-d7ab4a81b8d6 | -2.69196 | -57.59124 | 2026-09-15 04:32:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| be49cf85-aaad-34c6-a400-2c2ef6a70f03 | -2.95138 | -50.40354 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ccffe2bf-ff09-36dc-80a0-998fe46c9ddd | -2.88227 | -50.46358 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 917c1d41-78f9-318b-89a5-bbfc85e2c3b4 | -3.73917 | -54.38387 | 2026-09-15 04:32:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d181f7dd-e7af-352e-b7c1-4d15b56d65ab | -5.80513 | -53.80441 | 2026-09-15 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4040cc93-7890-3632-b1a2-a42af443f559 | -5.84157 | -52.05682 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d77c42a9-ce06-3bd8-931c-5a1f1267e779 | -4.56442 | -54.91218 | 2026-09-15 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db912e9e-b505-33c8-b57b-e328d8463647 | -2.68878 | -57.521 | 2026-09-15 04:32:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 44999d0f-6998-3a7b-a5e5-fe44b10c3487 | -3.37582 | -50.77408 | 2026-09-15 04:32:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 695715e1-d2b4-3009-8c2d-95a624fdeefb | -6.93275 | -42.75633 | 2026-09-15 04:32:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| de320915-e498-33c4-a5c9-0d5fbc856f18 | -7.45183 | -46.87146 | 2026-09-15 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 352887da-c361-393d-849e-511cfcb364a0 | -6.42746 | -43.06771 | 2026-09-15 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4cc97ecf-bc47-30b3-aac2-1b1c2d1977b8 | -3.4228 | -58.22458 | 2026-09-15 04:32:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6035b8ff-d76a-37f0-bd66-524d5d2d1997 | -7.08925 | -41.82671 | 2026-09-15 04:32:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0960d20c-577f-3c16-90b0-aa9585f458ac | -6.16075 | -55.71455 | 2026-09-15 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e40f370-fc50-3b95-8275-7a76972e8773 | -7.56251 | -44.91523 | 2026-09-15 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README36.md)
