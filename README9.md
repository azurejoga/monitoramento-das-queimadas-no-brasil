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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df5db8c3-11e7-3a32-93ee-897655367bd1 | -12.9813 | -51.2359 | 2026-09-30 03:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 683f146b-ecd2-371b-93ab-740799afa7ad | -12.9817 | -51.2145 | 2026-09-30 03:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 46.0 |
| c9ea23ab-88ad-3801-b20f-992866b4bb90 | -7.8486 | -45.8138 | 2026-09-30 03:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| f7ba0989-878e-37e4-b4fa-6965e822fa4f | -7.8297 | -45.8156 | 2026-09-30 03:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 21e41e0f-5b04-3485-aa6c-5d8eabb350f3 | -2.974 | -51.0247 | 2026-09-30 03:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| c69e6f4f-fe34-3549-8cb1-d1bdfd6ba045 | -12.3085 | -47.9539 | 2026-09-30 03:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 6930fa24-e236-397c-bf7c-f3a68ed5c911 | -7.8486 | -45.8138 | 2026-09-30 03:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 8a715884-23f2-353e-979b-75e55a54ad6c | -5.7374 | -45.176 | 2026-09-30 03:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 51.1 |
| b107bc65-5de1-30f9-940f-5465fa89a186 | -14.1314 | -46.2571 | 2026-09-30 03:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 136.8 |
| be16e8bd-ce42-3667-a2a9-82cc09f78317 | -7.8483 | -45.8363 | 2026-09-30 03:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 16ed1d44-9c3d-3740-bc8f-6b741b8eab58 | -7.8297 | -45.8156 | 2026-09-30 03:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 70c9f0c7-0723-3122-beee-6751ccfe3127 | -14.1119 | -46.2604 | 2026-09-30 03:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 7a186a36-fee2-3066-832b-5f039665d95a | -9.6637 | -40.5819 | 2026-09-30 03:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 77.1 |
| 7fe4073c-d9cf-3423-8e7c-8ff4a161190e | -7.8109 | -45.8173 | 2026-09-30 03:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 7339d115-0e30-3445-a723-b163c5a770cc | -3.2314 | -46.9376 | 2026-09-30 03:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| 22046088-1be3-3891-99f3-ea57d45fb0f0 | -2.9924 | -51.045 | 2026-09-30 03:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 811ae7e2-4bf6-3633-b930-9f7072e1eb3c | -2.974 | -51.0247 | 2026-09-30 03:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| a5f6b840-0000-3111-87d2-af3164964de2 | -3.25 | -46.9369 | 2026-09-30 03:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 40.3 |
| 9693ed54-eae1-33ca-ba7d-d16ad417cec1 | -2.9739 | -51.0455 | 2026-09-30 03:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 3a830021-933e-37a7-be4c-24132b447485 | -5.7561 | -45.1747 | 2026-09-30 03:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 0141358d-fb14-305d-b336-1dbae5996caa | -7.8295 | -45.8381 | 2026-09-30 03:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 4bc3ba9e-6cd0-399d-a8e7-8cef6518839e | -11.3853 | -50.9743 | 2026-09-30 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 85825c1b-a7b9-39f0-83a8-b1c1e0ae074f | -20.5138 | -49.6289 | 2026-09-30 03:50:00 | GOES-19 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 17bfddde-1d6a-3658-9b31-adc24a5b9e77 | -3.2313 | -46.9596 | 2026-09-30 03:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| a44f9f79-2582-3c79-a0d3-e7fa780e659c | -0.48831 | -49.13269 | 2026-09-30 03:53:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a473e19-956c-3122-9cd7-9f205e8ca44f | -3.24894 | -50.12231 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8cb0a83c-9f03-3a71-8484-1ad3067cbabf | -3.69094 | -39.57713 | 2026-09-30 03:53:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 05500cfb-55f5-3d22-ab21-8eda8e32f5c0 | -3.22193 | -46.94928 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bc8a98fb-5728-3285-a855-f2be90d805db | -2.97748 | -51.03072 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 67f40e61-7a31-38e3-bc25-49eeb2a87858 | -3.22459 | -46.93289 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b8ffff6d-d1e4-3e6e-921f-b7061017b0c6 | -3.22724 | -46.9409 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 8ed3e9c8-82e9-33eb-9b73-fdde37953466 | -3.23198 | -46.94515 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 846ed232-0229-35a8-8b87-1b43f360b96c | -2.98913 | -51.04587 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8da46f00-f0f8-3202-a42e-8313f53f3689 | -3.23842 | -46.93944 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| f487461e-ebf1-3a7c-8096-ea5b11cf5ae6 | -3.23254 | -46.94186 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 6ca70098-f4ef-3f4d-9d38-9054a4358411 | -3.22891 | -46.93108 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 66d863ba-97c6-3796-9351-406f4ec2664b | -3.22557 | -46.95075 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2241e542-3753-3869-a84c-22b6ea257ed1 | -3.77761 | -41.59387 | 2026-09-30 03:53:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 4e1b8f57-c357-3550-906d-103aa6eac4ab | -3.24885 | -50.12399 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9d8a6ea9-2e79-396e-b6b5-d626a7c4cb84 | -2.97735 | -51.03141 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| e2827f9c-141d-37ad-ab4c-02680759850e | -3.22881 | -46.94051 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| e8f30f24-57b7-3b1a-8902-8d616fab1a04 | -3.23786 | -46.94272 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| e24e2f14-afb6-3f7e-9469-ee33e6451100 | -3.18192 | -51.24373 | 2026-09-30 03:53:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| eb8b5f16-08b8-306c-b7e6-c5c219828c49 | -2.64091 | -49.27367 | 2026-09-30 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 870cd245-edea-349e-8281-fd0323a8d5b6 | -3.22774 | -46.9471 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2af848a8-90d2-35d2-b682-0c1a76929ed4 | -3.03506 | -48.41934 | 2026-09-30 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5aa85bea-5f9a-341e-bd92-87cc261d790b | -3.23675 | -46.94927 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| cb521a22-0162-3c86-a4ab-f576fa7b74c0 | -3.14674 | -51.03842 | 2026-09-30 03:53:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c8a8faf6-7d78-33de-b41c-ce75c5e221ff | -2.97623 | -51.03781 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 571512fd-fad3-33d4-b93a-eeec0055b4d7 | -3.03576 | -48.41515 | 2026-09-30 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 99d80529-8a97-3fcb-8cfb-9edbd11a0830 | -3.24988 | -50.11686 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d2bc6867-c27b-3ecc-a572-09f8cbfec52d | -2.97165 | -51.02322 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 35cb0783-a783-3512-af2c-91f0400d18b9 | -2.26695 | -47.87018 | 2026-09-30 03:53:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac377ac2-2f3c-3d35-8418-15ec086ebebb | -3.2331 | -46.93856 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| e240e2c8-7c4d-37d8-b68f-7fa9ec1e0608 | -3.22721 | -46.95038 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65746234-2adb-3dd5-8fee-b9a47a5f110c | -2.97398 | -51.05072 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| b7e1bbb8-22c1-31cd-8169-5a7581aeb888 | -2.97532 | -51.04359 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 56e991a0-cb6f-33df-b950-c5c61cc3d509 | -2.97044 | -51.03035 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 7cea27b1-80dd-31f3-9d9c-1c86d64a1ebb | -2.99021 | -51.0394 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| c27cd54d-0a08-3f67-a46f-fd02d042184e | -2.2723 | -48.75289 | 2026-09-30 03:53:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7d05f646-eec1-3f71-a63e-079989f471a6 | -3.23412 | -46.94141 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| f19a5f5c-f51b-3bb9-bfe3-308b8b6ed930 | -3.77613 | -41.59642 | 2026-09-30 03:53:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 37cbcbf5-53ce-300c-9f8f-ee9530f1d1bc | -2.97511 | -51.04425 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| b18237ad-45be-358e-a44e-9d4e33a1b9c0 | -3.22613 | -46.94746 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b5a8c9d4-469c-33e9-a6d9-aa6a8024d2b4 | -2.96932 | -51.03672 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| effcd4f9-3cbc-38ce-b842-997da2d37106 | -3.23305 | -46.94801 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 18ac5b9b-a99b-338c-baa3-aa13cebfd82f | -2.98201 | -51.04538 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| bf315ae6-84d5-3ec6-99ba-eae02bae56e7 | -3.223 | -46.94269 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4897f375-13bf-3ff0-9fd6-34df1c11bf1a | -3.23897 | -46.93615 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| d5f84fb9-df95-3792-b7ed-d15ce4278c8c | -2.98437 | -51.03188 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| a0c153a3-7e75-3ae7-b666-fc5a91c120c4 | -2.98314 | -51.03889 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 76271c13-72f1-3c0b-8ed1-43377d30776e | -3.22988 | -46.93392 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 701820fc-0151-3571-b288-40864fc6cb64 | -3.10809 | -50.27895 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 9cdb9cfd-7924-3f76-b7b4-788292c8f06c | -3.22353 | -46.93941 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| e2e17812-d502-37d6-be6d-1693389c54c0 | -2.97155 | -51.02396 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 3805daeb-ad60-3dc1-8098-e8ba5a464575 | -3.22827 | -46.94381 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 047eb2e3-021d-3f14-bf0a-0c64c893c3b5 | -3.22934 | -46.93722 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 03b6837b-5d43-3477-aef1-d138fb8bd157 | -2.98115 | -51.05118 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 91d88a21-686b-35b6-93de-f135b1c66bc7 | -3.0299 | -48.41413 | 2026-09-30 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| e6f626a9-f399-3bb9-a072-13aa874267f3 | -3.24998 | -50.8106 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 22fd43bf-73c8-365e-9f7b-fbe909798246 | -3.23466 | -46.93811 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 2834d3dc-38a7-35b4-bd8a-308fd81bb9b9 | -2.9796 | -51.01802 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| efb5eaab-09ec-332f-a7e6-6b0f5ffa36db | -3.1034 | -50.27664 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 58f0fc1c-bc3c-3bf3-b4bd-b1acd7a79593 | -2.97424 | -51.05007 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| ea4f3319-c852-3599-ba57-5c8c743ce8e5 | -3.69432 | -39.57769 | 2026-09-30 03:53:00 | NOAA-21 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| a2769773-34bf-3505-b956-761bf7f1e472 | -3.22406 | -46.93615 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 2ff8d78b-3396-34b5-afef-b665ba39a473 | -3.10998 | -50.27775 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6a5b4268-bab6-3f63-9384-e0b0719c12e3 | -3.23572 | -46.9315 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9cb3577c-4076-3279-ba30-7d8512499371 | -0.48351 | -49.134 | 2026-09-30 03:53:00 | NOAA-21 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 951974e7-bf5f-318c-a56c-8c7bd63b751e | -2.9809 | -51.0518 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| f581e98f-4a9d-31b1-89cc-820102ee5fde | -3.0292 | -48.41831 | 2026-09-30 03:53:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ac75526d-8604-3759-8287-4812d2926cf5 | -3.2373 | -46.946 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| ffe82a46-058d-3c21-b348-6ad717e8a6bf | -3.23041 | -46.93061 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e613a296-d8b5-34ef-94db-d2cf3b4feebf | -3.23359 | -46.94471 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5c0f296a-b610-321e-aec4-618b58debced | -2.98425 | -51.03252 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 5d193eaa-64b9-314e-b8f0-da368edb96b7 | -2.98331 | -51.03824 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 9ba18700-0f0a-3d36-95e2-0645e781081a | -3.22836 | -46.93436 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 44f37979-2b2d-315d-9834-28a31b1aec8c | -3.10904 | -50.28339 | 2026-09-30 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 76aca445-11d3-3bd7-8b11-2a86af257c8e | -3.22307 | -46.93332 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 17a6293a-bd5f-34e9-bc0b-82deff801734 | -3.23252 | -46.9513 | 2026-09-30 03:53:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README10.md)
