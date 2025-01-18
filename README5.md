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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c5b61c6-b97c-3b56-be1c-a607e8baa7be | 1.1141 | -59.45755 | 2025-01-18 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9591a3f5-52d3-3ff6-b1d6-796ab40f2850 | 1.12865 | -59.42804 | 2025-01-18 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6b8f020-45ab-332a-b394-bc8fb61b5ea7 | 1.1168 | -59.45964 | 2025-01-18 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98106cde-f6de-38d6-a386-01d1d8932869 | 0.67026 | -59.38229 | 2025-01-18 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ba37c432-c989-3f04-80b8-9f3a5ef4e450 | 1.11307 | -59.46021 | 2025-01-18 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b2558f0a-8958-3be5-b7d5-c00408461857 | 1.12933 | -59.43244 | 2025-01-18 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e16aed0-1677-339f-9393-8375f65ad183 | 1.32288 | -60.69619 | 2025-01-18 05:08:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e418730-1d19-3eb4-926c-7c75c1ee08e5 | 1.0921 | -59.47253 | 2025-01-18 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 981a9ae4-9026-35ed-91d4-15c7835a3169 | 0.66933 | -59.38435 | 2025-01-18 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9995fce3-df6d-3ef5-8f2b-c1b2df780467 | -0.35882 | -62.75341 | 2025-01-18 05:08:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b0eaf865-0561-3c7e-a1ad-52ca2f271621 | -1.73967 | -61.03876 | 2025-01-18 05:08:00 | NOAA-20 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43c5a2b1-30c7-3129-b093-6d7da662cc7a | 1.13238 | -59.42748 | 2025-01-18 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1111e4d2-46d6-3a86-9984-65bfe7287197 | 0.76377 | -60.09055 | 2025-01-18 05:08:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2f791ae-2163-3828-a7ef-f9f13123669b | 0.64382 | -59.57564 | 2025-01-18 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 870e69ec-1659-39aa-be96-82eb4d42830c | 0.75568 | -60.52534 | 2025-01-18 05:08:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 258f2dd4-0640-3543-a56d-564ba72a7b7c | 0.66657 | -59.38285 | 2025-01-18 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c3044b07-ba80-333a-a1f8-7127f5ecb876 | 0.72896 | -60.12033 | 2025-01-18 05:08:00 | NOAA-20 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70647e15-5456-3cfa-803a-f1bbbc5a1c60 | 1.09583 | -59.47193 | 2025-01-18 05:08:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a713130-cc0e-38e7-a32a-8f44e2c3a213 | -22.8579 | -53.5169 | 2025-01-18 05:10:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 82.1 |
| 967ab1af-0c94-3ea0-aabc-d31b5f1535b7 | -22.8585 | -53.4947 | 2025-01-18 05:10:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 71.2 |
| 54157e11-19ec-32c2-a33c-929cc31cbb65 | -7.90377 | -61.51301 | 2025-01-18 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e1d2bdcb-87c9-3092-a665-bb180444a659 | -15.56392 | -59.38767 | 2025-01-18 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d2aa7b8-9bad-397d-a94c-955ad4482f2c | -15.56994 | -59.41433 | 2025-01-18 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3a31f1bd-dd94-3c9a-a90c-97103e0f407f | -22.85953 | -53.50661 | 2025-01-18 05:14:00 | NOAA-20 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| bb160690-4a2e-3456-9799-abf106aed019 | -22.84358 | -53.47753 | 2025-01-18 05:14:00 | NOAA-20 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 31.1 |
| b9c6e3fd-a63e-3c34-88f2-54b4cf3462e3 | -22.86366 | -53.51254 | 2025-01-18 05:14:00 | NOAA-20 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| 287d6274-226e-3e0a-8a56-038e481d2244 | -22.86012 | -53.50127 | 2025-01-18 05:14:00 | NOAA-20 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| b6640f48-388c-3f5c-a772-a36b76e408d5 | -22.85541 | -53.50069 | 2025-01-18 05:14:00 | NOAA-20 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 7aadd782-3b1c-3dce-a1b7-cf09f0445b6e | -22.85424 | -53.51135 | 2025-01-18 05:14:00 | NOAA-20 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7897eca5-24e8-335b-b184-7e765f881205 | -22.85069 | -53.50011 | 2025-01-18 05:14:00 | NOAA-20 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 831143e3-577f-31e9-8ff7-75d1ffc81698 | -22.85837 | -53.51728 | 2025-01-18 05:14:00 | NOAA-20 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| fda66272-63ac-3664-aa9c-4820a2610f79 | -22.84772 | -53.48346 | 2025-01-18 05:14:00 | NOAA-20 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 9c686cd4-0078-3f45-8eb9-320f38478c9f | -22.86424 | -53.5072 | 2025-01-18 05:14:00 | NOAA-20 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| 43c01c7c-ad4a-34b9-a355-524e3290df17 | -22.85482 | -53.50603 | 2025-01-18 05:14:00 | NOAA-20 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 971940df-4952-3f15-b2b6-fcebce1870bd | -22.85895 | -53.51195 | 2025-01-18 05:14:00 | NOAA-20 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 16.9 |
| 67d01914-b416-3a45-bf6b-46f008ccc927 | -22.83887 | -53.47695 | 2025-01-18 05:14:00 | NOAA-20 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 17.4 |
| c7fa9f71-b14b-3013-a130-ad0521e5c437 | -29.10614 | -55.93873 | 2025-01-18 05:16:00 | NOAA-20 | MAÇAMBARÁ | RIO GRANDE DO SUL | Brasil | 4311718 | 43 | 33 | nan | nan | nan | Pampa | 2.6 |
| fe1838d5-9f10-38fc-b83d-212841510c3f | -29.31124 | -56.01937 | 2025-01-18 05:16:00 | NOAA-20 | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 7f34e342-9812-36a1-ac89-ad6346993145 | -22.8579 | -53.5169 | 2025-01-18 05:20:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 96.2 |
| f4795caa-0574-3a07-b14f-b2b07f33e228 | -22.8788 | -53.5128 | 2025-01-18 05:20:00 | GOES-16 | QUERÊNCIA DO NORTE | PARANÁ | Brasil | 4121000 | 41 | 33 | nan | nan | nan | Mata Atlântica | 76.1 |
| 9595085a-734e-3bb2-9dd9-a989f7defe7c | -22.859 | -53.4724 | 2025-01-18 05:20:00 | GOES-16 | QUERÊNCIA DO NORTE | PARANÁ | Brasil | 4121000 | 41 | 33 | nan | nan | nan | Mata Atlântica | 61.2 |
| b2fabe11-9fb2-3680-a44a-1db917bfc03b | -22.8794 | -53.4905 | 2025-01-18 05:20:00 | GOES-16 | QUERÊNCIA DO NORTE | PARANÁ | Brasil | 4121000 | 41 | 33 | nan | nan | nan | Mata Atlântica | 68.3 |
| 76c785ad-5d83-3e4a-819d-a8aff3111d6c | -22.8585 | -53.4947 | 2025-01-18 05:20:00 | GOES-16 | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 90.8 |
| a55f42d1-6c0c-3540-a841-812761ec2e8f | 4.37096 | -60.79758 | 2025-01-18 05:57:00 | AQUA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 34.0 |
| f9de81f6-e186-3160-8853-bd3ec89d642a | 4.3627 | -60.80489 | 2025-01-18 05:57:00 | AQUA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 298e1e30-53a3-339b-969e-1346b4105eaa | 1.65443 | -60.14028 | 2025-01-18 05:59:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d855930c-fe05-3d7d-90b0-c2f1b9c694d2 | 4.8112 | -60.63039 | 2025-01-18 05:59:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35c79545-cfd0-3593-ba93-2b6c16241b42 | 4.36521 | -60.8175 | 2025-01-18 05:59:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0e864287-feb7-377a-bedf-eafaa0912f9f | 4.36639 | -60.81577 | 2025-01-18 05:59:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9727bdcf-2d1e-30dc-a0b4-e577e1462d4a | 3.29084 | -59.95354 | 2025-01-18 05:59:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| afdcf85f-36f3-3f93-b6b2-06d68b4b9afe | 2.37425 | -61.25452 | 2025-01-18 05:59:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 818bf106-4055-3b19-83d0-0f1464c017de | 2.94573 | -60.16067 | 2025-01-18 05:59:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2b8a5f5b-6b20-32df-b628-82f12bb48d15 | 4.911 | -60.29364 | 2025-01-18 05:59:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d85e7bd0-d111-3115-a727-1e24d2b9447b | 2.6102 | -61.31434 | 2025-01-18 05:59:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 113bcb93-6ec5-3eae-8bbf-2cb6a9b401ba | 4.13291 | -60.01971 | 2025-01-18 05:59:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 042f0e45-f09b-362c-852f-a586daa0f052 | 3.61771 | -60.11655 | 2025-01-18 05:59:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5935bbf4-bf73-3e1d-b8a9-04a91ea29fd3 | 4.9157 | -60.29315 | 2025-01-18 05:59:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a438904-472d-3b76-bdda-11045b8efcc6 | 2.6147 | -61.31358 | 2025-01-18 05:59:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b19c7edd-f0a7-3892-b25f-a64380c0ed2e | 2.94736 | -60.16211 | 2025-01-18 05:59:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69803b59-828c-393f-9422-dd7473510d65 | 3.10957 | -60.76827 | 2025-01-18 05:59:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 57596bf6-f107-3522-97ea-bfb68c6bf5a6 | 4.36448 | -60.81298 | 2025-01-18 05:59:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 96597eff-59c0-30b4-8475-b9ff42b09683 | 2.67882 | -60.41802 | 2025-01-18 05:59:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 12c598cf-990f-3c6e-99ec-284a9059039f | 4.37096 | -60.81524 | 2025-01-18 05:59:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 54e65882-99e4-319c-8175-51e4d111b989 | 4.42845 | -59.9306 | 2025-01-18 05:59:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fcde9d58-633a-38f5-96bd-715c24363d82 | 4.80738 | -60.63553 | 2025-01-18 05:59:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06639854-5f50-36ab-9174-2c681edae78c | 4.36977 | -60.81691 | 2025-01-18 05:59:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c652ccb0-8784-3709-9750-c85051f71a64 | 2.60792 | -61.31184 | 2025-01-18 05:59:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 36174b7b-67e7-30ea-9ba5-a0dfd2378023 | 2.37048 | -61.25993 | 2025-01-18 05:59:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2ef5a639-4c79-3653-b975-ed97b2f8d0fd | 3.29664 | -59.95823 | 2025-01-18 05:59:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a9a71dff-93f8-3f30-9752-eb7e89b6aee8 | 2.61243 | -61.31107 | 2025-01-18 05:59:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1eddd72-b606-3a77-8281-0bfaad95e587 | 3.26704 | -59.97672 | 2025-01-18 05:59:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d618d437-fe8d-33b3-824d-cce22530c294 | 4.36715 | -60.82025 | 2025-01-18 05:59:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 63a48293-bac3-3493-baf2-30665ad1afac | 4.36905 | -60.81242 | 2025-01-18 05:59:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 822d2dd8-e54d-3919-81f8-a4d6003a75d4 | 3.26912 | -59.97416 | 2025-01-18 05:59:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 99cfdbbc-e8bb-3928-99ba-371541171f5a | 2.61394 | -61.30898 | 2025-01-18 05:59:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f375b518-4cfe-3b69-83d8-4ed652025ae8 | 4.37049 | -60.8214 | 2025-01-18 05:59:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 87813cfd-4c00-359f-b465-e91723c6fb60 | 2.18384 | -61.85595 | 2025-01-18 05:59:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b48358ab-b2a4-39ab-98a6-bb15d3f08b45 | 3.27401 | -59.97334 | 2025-01-18 05:59:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 297bfbaf-42eb-3c3f-8bbe-477d64a6ee60 | 4.37172 | -60.81977 | 2025-01-18 05:59:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 18e843b5-07d6-3a77-aa75-812afe4ce7c9 | 2.62674 | -61.46101 | 2025-01-18 05:59:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68f0cedf-b5d3-3fe6-a83e-2e31a83a7b86 | 3.27708 | -59.96153 | 2025-01-18 05:59:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0e33e9d9-b5e7-3ab9-8308-c88d4dab2e69 | 2.37359 | -61.25649 | 2025-01-18 05:59:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bd715fb6-f7b0-33bb-b604-63ca9d063984 | 4.91168 | -60.29774 | 2025-01-18 05:59:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ac280cff-5ae7-382b-b847-e318e9e43813 | 2.67831 | -60.41573 | 2025-01-18 05:59:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 86c50b43-a6a4-35a7-b01a-b90f4f00543f | 4.36594 | -60.82201 | 2025-01-18 05:59:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4751f1ac-dc93-34a0-81b0-99ce113c2ac7 | 3.2731 | -59.96785 | 2025-01-18 05:59:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 03c2532f-380b-376d-a0c8-3d33d88885ab | 3.28197 | -59.9607 | 2025-01-18 05:59:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 25a63da7-f853-36e1-8520-eaf49799ca09 | 4.3702 | -60.81075 | 2025-01-18 05:59:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a9e44972-a26b-3451-80fc-067c100cb83d | 3.28686 | -59.95988 | 2025-01-18 05:59:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 954a4aaf-5618-3488-bbec-4f94ce86b926 | 4.81195 | -60.63486 | 2025-01-18 05:59:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f82cc269-e9b7-323a-8d8c-f47ceaa8bf80 | 3.26424 | -59.97499 | 2025-01-18 05:59:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 131a4ed9-6bb2-329a-93cf-99258a9e2699 | 2.67799 | -60.41279 | 2025-01-18 05:59:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 24a35f7c-e887-38c3-b1c6-5635e6c99617 | 4.36563 | -60.81126 | 2025-01-18 05:59:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bbbe75ce-9a8f-3d0a-990d-825627471ed8 | 4.5318 | -60.68201 | 2025-01-18 05:59:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 528855ec-65bb-38db-9c6f-62c61dfd89de | 4.12792 | -60.01617 | 2025-01-18 05:59:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 13ba8148-1a77-3f7f-b1f7-fd2c3d65bcc1 | 3.6086 | -60.08712 | 2025-01-18 05:59:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf556fdb-e36e-304b-ace1-3ed5b7b4b7c1 | 4.12724 | -60.01542 | 2025-01-18 05:59:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a9bc4d38-9ff7-3db8-a3ef-6ee34e188873 | 4.42361 | -59.93123 | 2025-01-18 05:59:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e2b98839-4d73-34bd-80fc-8e8fa4d45ac7 | 4.42794 | -59.93 | 2025-01-18 05:59:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 504c49e3-20a5-31b9-8015-49432aa6694a | 2.37501 | -61.25914 | 2025-01-18 05:59:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README6.md)
