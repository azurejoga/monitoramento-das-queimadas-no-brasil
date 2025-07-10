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
| de45748a-3a9c-337b-b2ef-fbe31ea72cc4 | -10.57218 | -49.14133 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 7bb67b77-0e22-3681-8840-221c17bbf0e5 | -5.88982 | -45.57496 | 2025-07-10 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1e330f7-9b3a-332f-adcc-f911c92c97d7 | -7.32424 | -43.98125 | 2025-07-10 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4de8a64e-6e07-3dc3-8d2c-a7fa83b0a68d | -5.35351 | -45.26954 | 2025-07-10 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aa7af704-d2e7-3c8d-9017-977c56f55290 | -8.50137 | -43.29513 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 33.2 |
| 15bcef78-3b1b-381e-88e0-d671e745b1ec | -9.08914 | -47.96928 | 2025-07-10 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68293448-5b66-3d1f-8be1-525081c487a7 | -11.06412 | -45.87035 | 2025-07-10 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6a285a10-5e36-3713-8318-95663a109432 | -7.48627 | -43.93586 | 2025-07-10 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a4b144a8-576a-3b5e-a470-625ed507e528 | -6.24165 | -43.36812 | 2025-07-10 04:25:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d706d779-55b7-34c4-a110-29cceceb70c1 | -7.74017 | -43.59305 | 2025-07-10 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e0ac32aa-5a95-328f-aaf0-317125ff1869 | -9.30174 | -44.84111 | 2025-07-10 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4c71a88a-c91f-3257-ac71-3e4a17091558 | -9.30462 | -44.84547 | 2025-07-10 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8661e17e-c7bf-300f-a717-c2e25d21492d | -6.99702 | -43.48968 | 2025-07-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 14771e89-104e-3bb3-a579-fe8b11932828 | -10.5678 | -49.12537 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b412012b-dd61-3b60-9c75-97638aa57248 | -10.57278 | -49.13765 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 03778652-a3de-3483-b7dd-a4491e8b7700 | -7.67851 | -44.35607 | 2025-07-10 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33fc4090-8102-30fc-a587-12357a58849b | -5.24981 | -44.45354 | 2025-07-10 04:25:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4fbb66e-4440-3734-b71f-ee6f81ce1652 | -6.85276 | -42.80287 | 2025-07-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| c41746cb-7faa-306c-8e3f-f6ea4fb40f63 | -4.81023 | -45.65808 | 2025-07-10 04:25:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3dc6c7e5-be46-327c-b78e-dfe863c5f039 | -6.95777 | -42.72032 | 2025-07-10 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6fc19e99-8f03-3ea7-bd7b-f454b538991b | -6.95843 | -42.71579 | 2025-07-10 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 89df93c9-1ecc-3e84-b892-c4d811f40a8e | -8.50464 | -43.27985 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 30.4 |
| dd456b4f-e2d1-3e0f-8a97-948634864a0d | -8.49654 | -43.27637 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.1 |
| b8052926-2d93-3651-adae-ba20ab62772a | -6.67662 | -46.29855 | 2025-07-10 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bcb0205b-644d-3531-b988-671fad2a9069 | -6.70321 | -43.10642 | 2025-07-10 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4716faa5-a2da-3399-baa3-36dab3d84c56 | -10.62511 | -45.23036 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 032b0cf0-bca9-39cb-b291-c9b3bc9685fe | -8.50073 | -43.29953 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 33.2 |
| 2abe456d-ee88-3563-b54d-a2ae9b0edb2a | -5.41125 | -46.07064 | 2025-07-10 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| de084254-de9a-336f-9412-f006368e019c | -8.862 | -47.94725 | 2025-07-10 04:25:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb83044b-9b6f-3f1f-a751-79b55973aab1 | -10.62166 | -45.22985 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 130fe66a-a7f0-3545-a397-751901821e55 | -7.94663 | -44.86681 | 2025-07-10 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ef87a7b-8001-3997-9725-cf49d99c5cf6 | -11.6713 | -43.78105 | 2025-07-10 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a3d74f0-6bd8-3149-adcd-a672c188af9f | -11.13805 | -48.88008 | 2025-07-10 04:25:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47e6d295-c7f0-30d7-96d2-cf8ac71aba8e | -5.41401 | -46.07461 | 2025-07-10 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d039a94-9529-30cc-9a3a-1ed52e7c541e | -8.50058 | -43.32644 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bb64ed0c-2391-3eaa-87d4-37413ee8fa84 | -10.57399 | -49.13022 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6fef001f-1038-3955-bb67-2201f02c45ce | -11.87921 | -40.954 | 2025-07-10 04:25:00 | NOAA-20 | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 419ce17e-b150-3854-b3c5-c81fc8c332c4 | -7.16383 | -43.70093 | 2025-07-10 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1fbda10-542b-3944-9359-df4999d9c669 | -6.56997 | -42.89969 | 2025-07-10 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a4c59795-9eb3-35df-a3e7-8aefd4aba42a | -12.24535 | -40.96832 | 2025-07-10 04:25:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c80a3b6c-da44-3ab5-b837-b896b3e12ed1 | -4.2216 | -47.20749 | 2025-07-10 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 6f838735-336a-3eb0-a409-7cc223818c1d | -8.50811 | -43.30063 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 25bd4d2c-64c2-3ddb-82f7-275b8a89f83f | -8.50427 | -43.32699 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 8ea28d74-78aa-3338-b1f8-9b2ca4605605 | -9.11453 | -47.64119 | 2025-07-10 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6d60f6e5-c7db-3996-ac63-879d17c4b62f | -7.01989 | -44.56105 | 2025-07-10 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1f511d7f-78d5-39eb-a3b3-3e4443f074c3 | -7.22417 | -43.07255 | 2025-07-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a39fda38-bb54-300a-8d9e-644de8c9511a | -6.95767 | -42.71321 | 2025-07-10 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 53361fba-fdef-364f-8c97-c144bc274e49 | -4.22439 | -47.21157 | 2025-07-10 04:25:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3b062953-2d85-3cbe-b835-5684b5119ba6 | -6.54685 | -43.62272 | 2025-07-10 04:25:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 98119f7d-38d9-362a-acb2-d23eacca0dff | -6.95534 | -42.71074 | 2025-07-10 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e9c670b9-8bb7-3920-a567-3b09a5cece40 | -6.98859 | -43.49693 | 2025-07-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 82e912bc-52dd-3168-97ff-853e0d4e1ec7 | -8.49704 | -43.29898 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 4c9be59a-815c-3323-b06d-ffb25ddbe1a9 | -10.99633 | -42.78041 | 2025-07-10 04:25:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 60f4b6c5-0233-3947-b336-83fa4a7567fc | -8.50064 | -43.30624 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| c4717287-673f-36fb-b593-0e72f594c68f | -7.48274 | -43.93534 | 2025-07-10 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 52be9c35-19c9-31a2-8fd5-bd73a195a369 | -6.85648 | -42.8034 | 2025-07-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 9f569ea9-772f-3119-a4f7-618f6b6bbf69 | -7.31125 | -50.06192 | 2025-07-10 04:25:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 347a8bb2-2ee9-3e47-8656-ff46849eb248 | -11.52988 | -46.84196 | 2025-07-10 04:25:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa4621d9-d808-393e-987e-4cfe0b063762 | -7.64597 | -45.34746 | 2025-07-10 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b9c4dcb-f878-3514-813d-3f1c64d1d621 | -8.50859 | -43.32315 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 05956567-513d-3d79-b098-16786f15f2f9 | -6.95468 | -42.71528 | 2025-07-10 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8eff75f0-4025-3f59-bd2a-e9fcd93237e3 | -6.62968 | -56.27786 | 2025-07-10 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b9a50e1-ceb1-3dec-8fbd-07a8e58969a3 | -6.99983 | -43.51972 | 2025-07-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d4ec666a-b37c-3746-a6ca-b43190ea6c2e | -7.22681 | -43.07599 | 2025-07-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a4d92d69-3cfb-31a8-b950-5f47abf551a3 | -10.64895 | -44.48561 | 2025-07-10 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d93faba-4c58-3260-994d-b1266b4330a7 | -4.37354 | -48.22366 | 2025-07-10 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a429eef1-cdfa-3827-9bd7-b50f5a1a1463 | -8.50554 | -43.31821 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 36.6 |
| 549513f3-16c7-3343-a357-592f49afcb41 | -5.45017 | -40.61929 | 2025-07-10 04:25:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0db3b99b-750e-3bd1-8432-1a160a50699d | -10.63487 | -45.23575 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 874bba68-4abc-33ba-81ff-6c20e57dbd3d | -7.11224 | -47.83703 | 2025-07-10 04:25:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d7999779-9754-38f1-8369-6be3a5d6de16 | -7.01346 | -49.81931 | 2025-07-10 04:25:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02642cb8-8f70-387b-bfb2-689b84de84d9 | -7.00983 | -49.81873 | 2025-07-10 04:25:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e510f001-efce-32ad-b1ef-b0003dc1dd61 | -6.69956 | -43.10587 | 2025-07-10 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c65de89-3ad4-3541-bee9-5f347e2cf45e | -8.50747 | -43.30503 | 2025-07-10 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 7e82de71-041f-385b-92ed-9ea2a2839aac | -9.2977 | -44.84441 | 2025-07-10 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63972d66-09f4-3946-b9e0-64a77dbeb3fc | -7.2302 | -43.08234 | 2025-07-10 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8b6c4e0c-1933-343e-b8ad-5badbf337fe1 | -7.20574 | -45.3495 | 2025-07-10 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aba2c528-608b-3b1d-a141-90b6f9e95e6d | -11.90849 | -44.90723 | 2025-07-10 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a737556e-e463-31e7-a94b-ea748df12e9a | -4.45196 | -48.99587 | 2025-07-10 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f028336-a918-31c5-81c0-c663ecb4d7a0 | -7.08308 | -43.41671 | 2025-07-10 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 47e96907-83db-3745-a5d8-6ad742917274 | -11.08161 | -45.86923 | 2025-07-10 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c6ec8ccf-902c-3b2e-9aab-9bc0cc5f1de7 | -7.71441 | -43.74057 | 2025-07-10 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 55ccd3ec-efdb-3124-a491-d0520c9ab186 | -9.00209 | -47.45113 | 2025-07-10 04:25:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c42dbe6b-3cf8-348b-9265-135ed1344f66 | -6.84374 | -44.06848 | 2025-07-10 04:25:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62661d53-3732-350a-9a0d-6f7a5a4cda3e | -10.65705 | -49.46008 | 2025-07-10 04:25:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 23f33475-eba4-34ba-8955-4b4f0add72f7 | -11.07372 | -45.87554 | 2025-07-10 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4a8f218-e1d7-3842-a3bf-b6e6300cc177 | -16.07819 | -53.7499 | 2025-07-10 04:27:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f33383eb-c145-3d8a-9ab2-ecf1bb1a0ac7 | -16.07021 | -53.74845 | 2025-07-10 04:27:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 170d219e-9101-3083-a671-23cde0a42386 | -12.2235 | -44.2128 | 2025-07-10 04:27:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 592aed75-a8f8-3d36-9ac7-61864468c7d0 | -14.57366 | -48.13831 | 2025-07-10 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76b7d0c2-2f6d-334b-b4cc-af8e47ff74a8 | -13.33957 | -52.92543 | 2025-07-10 04:27:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a62a817-a541-3917-b420-1f2039824e3d | -12.21983 | -44.21225 | 2025-07-10 04:27:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db296ce4-9eda-3d23-b0b1-66e2f98f1361 | -12.56505 | -52.2142 | 2025-07-10 04:27:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ef1db8db-5e6d-30c5-bc4a-7ef542673308 | -11.73887 | -48.52867 | 2025-07-10 04:27:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7b48e22-7442-37a2-ab91-df5dcd6954f8 | -11.82652 | -48.21575 | 2025-07-10 04:27:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b915147-7a7a-3728-8987-977f8d4b0c00 | -12.4892 | -47.50516 | 2025-07-10 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbaab9e7-cf13-378d-b7cb-dbaec4ac429f | -13.2895 | -49.15807 | 2025-07-10 04:27:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 333b1607-778d-3c5b-8b78-91d3a9172a43 | -16.84461 | -49.34995 | 2025-07-10 04:27:00 | NOAA-20 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8270d23c-cff5-345b-a49d-24822f8fc7b3 | -11.87508 | -46.7613 | 2025-07-10 04:27:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4ffb1a1e-91c9-312d-a19c-306646da48a9 | -16.6123 | -49.39964 | 2025-07-10 04:27:00 | NOAA-20 | TRINDADE | GOIÁS | Brasil | 5221403 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README21.md)
