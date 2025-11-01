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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a88285f3-6bab-39a2-8260-af839f7ba922 | -29.14971 | -53.00252 | 2025-11-01 12:44:00 | TERRA_M-T | ARROIO DO TIGRE | RIO GRANDE DO SUL | Brasil | 4301206 | 43 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| 4a34fa98-10e2-301e-9d1e-1a7ef6754d44 | -28.97085 | -51.06384 | 2025-11-01 12:44:00 | TERRA_M-T | SÃO MARCOS | RIO GRANDE DO SUL | Brasil | 4319000 | 43 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 275f0a75-d17f-3ab7-9d85-efcf07bd624c | -29.21725 | -51.3364 | 2025-11-01 12:44:00 | TERRA_M-T | FARROUPILHA | RIO GRANDE DO SUL | Brasil | 4307906 | 43 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| b6b1e0ef-ce91-3bb5-b4ae-f50aeff02261 | -3.3672 | -42.1928 | 2025-11-01 12:50:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 93.2 |
| 0f09649e-c458-3b78-8f37-1b03ff717242 | -3.017 | -49.4482 | 2025-11-01 12:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 08fd15c1-b498-3033-a98a-f4c82c17df2a | -3.3673 | -42.1691 | 2025-11-01 12:50:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 89.3 |
| 733da95a-c822-3970-9c33-0cc8ce685e0e | 1.261 | -50.8512 | 2025-11-01 13:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 74.4 |
| f7791204-387e-3ed9-804b-a0b2f6b3420c | -4.4059 | -43.4049 | 2025-11-01 13:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| cc7644f6-f45c-365f-bdcc-bf4ab3e5b604 | 1.261 | -50.8512 | 2025-11-01 13:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 79.6 |
| efa0e6b1-a5ad-3e98-bfff-422ff3b1cab0 | 1.261 | -50.8512 | 2025-11-01 13:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 6c05f23a-692c-37de-be46-f18a151d0f52 | -3.017 | -49.4482 | 2025-11-01 13:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 886bc52b-0379-3e78-98c9-826a29427015 | 1.261 | -50.8304 | 2025-11-01 13:30:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 72.1 |
| c43ce1a2-f839-3935-9a37-e066757e945a | -3.017 | -49.4482 | 2025-11-01 13:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 008d59f2-0fa8-3831-9759-f7765aeb2462 | 1.261 | -50.8304 | 2025-11-01 13:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 87.0 |
| f887a74d-91bd-36ed-b132-7d2c3a6c9693 | 1.261 | -50.8512 | 2025-11-01 13:40:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 64c58357-668a-3af0-bfd1-489747af05c0 | -1.3562 | -49.0392 | 2025-11-01 13:50:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 46db5701-d098-349e-b9cc-6f85ae0bc071 | -3.017 | -49.4482 | 2025-11-01 13:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 0e239ae0-8a1c-3ca9-aee8-f0b905d526b3 | -3.2715 | -42.6221 | 2025-11-01 13:50:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 735e9063-d586-3029-baf3-ce8251a5fe64 | 1.261 | -50.8304 | 2025-11-01 13:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 79.5 |
| e35546c5-4773-32b3-837c-00fcf0196972 | 1.261 | -50.8512 | 2025-11-01 13:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 110.6 |
| daacc8f8-b30c-357a-a10a-72ef3d30e057 | -1.3562 | -49.0392 | 2025-11-01 14:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 61e35952-475b-3060-ab9a-f04c5f4e6cba | 1.261 | -50.8304 | 2025-11-01 14:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 76.0 |
| eca98836-85ad-3b6a-99c9-be1cfcbd63a1 | -3.95 | -41.6864 | 2025-11-01 14:10:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 86.5 |
| 6b93b21d-8b82-3374-b773-74ddb0873035 | -9.6585 | -44.5682 | 2025-11-01 14:10:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 18f82013-376e-3b49-ad3c-78dc3e6ae0ef | -1.3562 | -49.0392 | 2025-11-01 14:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 92c0b823-f37e-3f24-b5b1-a2dcd8154bf8 | 1.261 | -50.8304 | 2025-11-01 14:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 46dc4d0b-1ea5-3911-a193-d42104697cab | -18.3125 | -49.9124 | 2025-11-01 14:20:00 | GOES-19 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 94.0 |
| c9775b30-ba6b-384c-bb4b-4c99bd23c980 | -10.266 | -44.5835 | 2025-11-01 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 8ebfb059-beb4-32c7-ae23-733193a49ac2 | -7.8317 | -41.0897 | 2025-11-01 14:20:00 | GOES-19 | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 63.6 |
| aa2897bc-b5df-3cd1-925b-ac51130f916f | -11.6493 | -44.0619 | 2025-11-01 14:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 108.7 |
| fe9a166b-8c34-385b-afbc-31d47186f5a9 | 1.261 | -50.8304 | 2025-11-01 14:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 453b7a10-06b0-35a7-a7d2-f94a66de8eea | -11.3854 | -46.0378 | 2025-11-01 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 9842f8aa-4565-3b70-ab18-772c231f99b4 | -11.6493 | -44.0619 | 2025-11-01 14:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 111.3 |
| f1b3fee5-4215-3c95-bd4a-4f704e009e8e | -11.6305 | -44.0413 | 2025-11-01 14:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| d9551cb0-b373-34c8-b924-85f857966654 | -11.6493 | -44.0619 | 2025-11-01 14:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 112.7 |


