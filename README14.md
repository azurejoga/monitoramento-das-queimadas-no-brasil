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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6612d578-9267-3329-a122-9bba8bfc8df3 | -12.7386 | -45.3812 | 2025-11-18 01:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| c03287dd-941b-3742-b04f-8f95a5bfa2ca | -4.195 | -44.2247 | 2025-11-18 01:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 143.4 |
| bcc14719-ffb6-3926-a88d-31cc65712d34 | -8.3043 | -43.9842 | 2025-11-18 01:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 199.9 |
| c27fcfb9-3293-394d-bc6c-68c0fc7ede96 | -4.1762 | -44.2486 | 2025-11-18 01:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 517b0e30-7bab-3bf0-a287-0d99ea8f21be | -9.0934 | -44.3356 | 2025-11-18 01:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 60ebff4d-4f05-3643-b225-841efbc24806 | -2.5238 | -47.8115 | 2025-11-18 01:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| eac17d80-e076-3beb-86f9-e38da5ccc9d4 | -12.8566 | -41.4566 | 2025-11-18 01:10:00 | GOES-19 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 64.9 |
| f5cbcce8-64a4-307d-ae62-99620a57d228 | -9.1124 | -44.3334 | 2025-11-18 01:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 32ac1dd6-3fab-35e5-bf04-2759f1a91681 | -9.4769 | -40.3365 | 2025-11-18 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 567.4 |
| f16344de-af8a-3c68-b20c-f7bc423d672e | -8.2851 | -44.0095 | 2025-11-18 01:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 218.3 |
| a64be1c0-d16a-3d72-b423-32b5a69be332 | -3.3554 | -44.4026 | 2025-11-18 01:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 110.2 |
| e2fa87ba-2e5a-354f-a80a-6b980ce3c171 | -9.3969 | -48.4523 | 2025-11-18 01:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 127.8 |
| 9f319256-6ef7-33a0-99b3-404725988ae8 | -8.304 | -44.0075 | 2025-11-18 01:10:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 262.3 |
| 90884765-0893-35e6-b7ec-77afb41c7817 | -4.1781 | -50.2091 | 2025-11-18 01:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 124.7 |
| 2a8ab8f2-5e7a-3dea-af6f-444c08ed4bc1 | -3.4769 | -46.0879 | 2025-11-18 01:10:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 191ca726-65b2-3524-9e0d-dd6c47ed76a6 | -4.1764 | -44.2257 | 2025-11-18 01:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 125.4 |
| d69aaa7c-de17-3a1c-abf7-266f7bb8c974 | -9.4956 | -40.3586 | 2025-11-18 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 312.8 |
| 39959b38-1886-3017-a868-f9a9affeac38 | -3.1472 | -45.0924 | 2025-11-18 01:10:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 7e641e65-f253-337d-a1c1-7edee1f0e4ef | -3.1256 | -45.7449 | 2025-11-18 01:10:00 | GOES-19 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 75.1 |
| a781e30f-a6e5-3987-9ced-4ee33610a9bf | -3.477 | -46.0656 | 2025-11-18 01:10:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 187.4 |
| 9ecc4ca3-a922-3fc8-a80d-d4666c627177 | -3.2506 | -43.0449 | 2025-11-18 01:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| c7405bbe-f45d-36ca-8ab0-8ae77e35a5f2 | -9.496 | -40.3337 | 2025-11-18 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 306.0 |
| b79a2aee-8003-3753-b3f7-f8d63cfb8e7b | -3.3555 | -44.3798 | 2025-11-18 01:10:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 01ebca24-6b48-3449-ad76-6645070839f2 | -4.1949 | -44.2476 | 2025-11-18 01:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 44d65943-65c7-3665-8028-149ca796c39d | -9.4765 | -40.3613 | 2025-11-18 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 73.0 |
| a450b8f5-6a08-3fc8-be8d-1587e5ba09e5 | -3.477 | -46.0656 | 2025-11-18 01:20:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 145.6 |
| ac70a5e5-8498-37d4-a83b-1ea07067bbc2 | -5.3382 | -43.7391 | 2025-11-18 01:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| b90ef638-379b-3db9-a3e4-cc29f501ba05 | -3.2506 | -43.0449 | 2025-11-18 01:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 8a38dc46-1612-3e37-a9a9-631167201fa4 | -5.338 | -43.7623 | 2025-11-18 01:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 8dd21bc2-9d51-3545-b7a6-f641f6e29214 | -8.304 | -44.0075 | 2025-11-18 01:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 525b916b-2429-39a2-989a-6e720b479763 | -4.1762 | -44.2486 | 2025-11-18 01:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 38995929-697c-3eae-8a0a-917159daa882 | -8.2851 | -44.0095 | 2025-11-18 01:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 81eac9fc-189a-3fd4-a2f5-e7d94f2e0f57 | -9.3969 | -48.4523 | 2025-11-18 01:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 0084139a-fd93-3c34-848e-723b00811358 | -4.195 | -44.2247 | 2025-11-18 01:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 146.0 |
| f50906db-520d-337d-8acf-f60c7a76528e | -3.1472 | -45.0924 | 2025-11-18 01:20:00 | GOES-19 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 76000e14-f776-3cfb-a139-1098fcf61ed3 | -3.4769 | -46.0879 | 2025-11-18 01:20:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 71.5 |
| db1d879a-4aca-3958-9681-e1247d59f875 | -9.1124 | -44.3334 | 2025-11-18 01:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 11567e85-6bda-370d-a59c-27c95457e9c0 | -3.3555 | -44.3798 | 2025-11-18 01:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| ca1ce1b0-a371-3a7b-b4b7-dac4eb077f83 | -9.0934 | -44.3356 | 2025-11-18 01:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 74df14ea-8ef1-39f2-9c3f-2c6ee134936e | -8.2854 | -43.9863 | 2025-11-18 01:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 98fef1d1-b002-3be6-84f2-0971ed4c528c | -9.4769 | -40.3365 | 2025-11-18 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 78.7 |
| a57b1cff-4bcc-3a2c-ad98-d42afa3b9028 | -4.1949 | -44.2476 | 2025-11-18 01:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 113.9 |
| fbf75421-5947-3b9b-8f31-4432934534bd | -8.3043 | -43.9842 | 2025-11-18 01:20:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| a39cde3c-6615-36b3-bb1b-89618d0ed663 | -2.5238 | -47.8115 | 2025-11-18 01:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| ae969f61-9d3b-3514-b5b7-afeaaf4c3971 | -4.1781 | -50.2091 | 2025-11-18 01:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 105.1 |
| fac62691-bcd5-36ab-9625-57805ad11c75 | -3.3554 | -44.4026 | 2025-11-18 01:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 5cd1a8a3-6876-3d3e-ba57-2aad8bdc77b4 | -2.8298 | -45.4195 | 2025-11-18 01:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 139.5 |
| 34dbc9b2-3f89-3184-88b6-75f3efa04d2d | -10.3535 | -48.9174 | 2025-11-18 01:20:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 9469e660-435e-3483-9504-11a9adb932b9 | -4.1764 | -44.2257 | 2025-11-18 01:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 4c63ea61-e876-399d-a2dc-9292e149018e | -6.7202 | -40.7943 | 2025-11-18 01:20:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 96.7 |
| a429a996-254b-3cae-b3a0-5f24272fced9 | -4.1762 | -44.2486 | 2025-11-18 01:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| d6b7c971-1fab-3de0-9d64-357f19c60b34 | -3.3554 | -44.4026 | 2025-11-18 01:30:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| ae9d3d89-a8ff-30d9-9334-9851ab771eb3 | -3.477 | -46.0656 | 2025-11-18 01:30:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 105.0 |
| 8a3856dd-b45c-3638-87b8-1a68d11ea03a | -2.5238 | -47.8115 | 2025-11-18 01:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| d9ff4bb4-d5f0-35d5-ab88-ef98ae56159c | -4.1314 | -52.1033 | 2025-11-18 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 185.1 |
| a368c237-483e-3c3a-8db9-f65e18e829f2 | -6.7202 | -40.7943 | 2025-11-18 01:30:00 | GOES-19 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 79.4 |
| f2438c04-6018-3625-a21a-df63210ed716 | -4.1781 | -50.2091 | 2025-11-18 01:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 675a0e8d-5418-3349-8331-63254bcce0d2 | -2.4669 | -48.2238 | 2025-11-18 01:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| cf2b6402-3d03-3694-b484-e3e1b2ba2948 | -9.1124 | -44.3334 | 2025-11-18 01:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| dbe256a4-5aa5-313e-8bc5-d6aa35a32fb7 | -10.3535 | -48.9174 | 2025-11-18 01:30:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 47cbaf0d-f6ad-3660-b8f8-6a4b066bc4f3 | -2.8298 | -45.4195 | 2025-11-18 01:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 136.8 |
| b4c10f51-c0cb-3545-990a-0ef6fa0f2659 | -4.1764 | -44.2257 | 2025-11-18 01:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 3e166052-f25a-3ae1-b7e0-545120613bf4 | -4.1949 | -44.2476 | 2025-11-18 01:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 46b859a7-c84c-3585-a9a9-e87fc271a388 | -6.1138 | -42.9569 | 2025-11-18 01:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 76.2 |
| 6cdc7d9f-796a-3d6f-ad73-0d5277c3b85c | -9.3969 | -48.4523 | 2025-11-18 01:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 94ab989d-9d59-3461-bac4-88412a623ada | -11.5291 | -48.9559 | 2025-11-18 01:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 0d4728c5-eb06-3c9b-87e7-e904c762232a | -9.4956 | -40.3586 | 2025-11-18 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 136.4 |
| a5947880-c165-3c09-bb76-2ca2c55ce2ab | -9.496 | -40.3337 | 2025-11-18 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 128.4 |
| bd120005-ce6d-3d30-ac74-c1e2527e40de | -9.0934 | -44.3356 | 2025-11-18 01:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 87.0 |
| ad2f8a44-1b50-33fc-a588-12c5c9a03e8a | -4.1498 | -52.1026 | 2025-11-18 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 0a03261f-08b9-35a9-9695-e667b1c0abf7 | -6.1326 | -42.9554 | 2025-11-18 01:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 65.3 |
| 41f0ca8f-cd13-390e-9be7-b3184e402234 | -4.195 | -44.2247 | 2025-11-18 01:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 3d29a810-73c6-38ac-8c75-8e34bc76d9ab | -4.1313 | -52.1239 | 2025-11-18 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 337.0 |
| 6fe52f30-2211-388e-9b83-bb5895741ea3 | -8.304 | -44.0075 | 2025-11-18 01:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 82.9 |
| ccf7920b-3ba2-34dc-9861-956b33415075 | -4.1497 | -52.1232 | 2025-11-18 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 127.0 |
| 68898793-6d1d-32a7-8588-362fc8f33820 | -3.3555 | -44.3798 | 2025-11-18 01:30:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 15665cca-58fc-3fcc-9731-aa5ca5928af0 | -9.3972 | -48.4305 | 2025-11-18 01:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 5ff5f1e9-4f3a-3bae-8c31-3bda7e50a0e4 | -3.2506 | -43.0449 | 2025-11-18 01:30:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 556ba2b0-b2e3-31e8-b8b1-44aa73afed68 | -9.4765 | -40.3613 | 2025-11-18 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 99.5 |
| 686f0853-6eb8-35f9-bb30-22825fa9cf34 | -9.4769 | -40.3365 | 2025-11-18 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 91.3 |
| b5f238c6-b769-3abd-a5ea-0d4dfbc2d32a | -9.32974 | -64.43285 | 2025-11-18 01:32:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 47d452c9-dd10-38f7-93f4-980754539f70 | -9.33097 | -64.44175 | 2025-11-18 01:32:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ffb992f1-7729-31a9-9ac7-f8cf12a1fdb5 | -2.33102 | -55.79323 | 2025-11-18 01:34:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 88e52ff1-e49a-3bb2-874e-405880b09484 | -2.33322 | -55.78599 | 2025-11-18 01:34:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 163bce46-38b1-3f0b-8f26-95fb20d1b2e7 | -2.53459 | -58.02811 | 2025-11-18 01:34:00 | TERRA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 4dd9eae6-119a-3c8e-a944-1187552ea869 | -2.5326 | -58.03401 | 2025-11-18 01:34:00 | TERRA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| cd4f5fd8-7632-376b-adf7-58341aed1daa | -4.1497 | -52.1232 | 2025-11-18 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| a8573d00-1862-39ff-8a6c-06a4d446640e | -4.1762 | -44.2486 | 2025-11-18 01:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 8c0a2afe-8ac9-31fd-b5b2-c97e518e7c0c | -3.477 | -46.0656 | 2025-11-18 01:40:00 | GOES-19 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 4d77dad3-a718-3835-8445-63929805da18 | -4.1764 | -44.2257 | 2025-11-18 01:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 70507abf-0fe3-3313-b50f-b70ad9c11f70 | -6.1138 | -42.9569 | 2025-11-18 01:40:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 72.4 |
| 6137bbf1-e978-3728-9769-28b9b32f42bf | -2.8298 | -45.4195 | 2025-11-18 01:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 196.2 |
| a271d050-4e0b-3a65-abe2-2319b23b9026 | -4.1498 | -52.1026 | 2025-11-18 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 6f36b696-516b-3cbb-b8c8-625e4e390eab | -4.1314 | -52.1033 | 2025-11-18 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| e776ce3d-8acf-367b-a9f1-7a7c4b18e9e9 | -2.4854 | -48.2233 | 2025-11-18 01:40:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 33cd5f68-f498-3e07-a9d7-d40c6d549ae6 | -9.0934 | -44.3356 | 2025-11-18 01:40:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 33fc1b3a-aa8d-3280-a13c-e8fa42c5259a | -4.1313 | -52.1239 | 2025-11-18 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 12040704-8a44-3155-b14c-41bc338d42ff | -2.5238 | -47.8115 | 2025-11-18 01:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 48abf8a3-80f4-3d63-aed4-71de3e18308d | -9.496 | -40.3337 | 2025-11-18 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 87.0 |
| aadc7b49-a6c9-32d8-bb18-dbafc892aed3 | -3.3555 | -44.3798 | 2025-11-18 01:40:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |


[Clique aqui para ver as próximas entradas](README15.md)
