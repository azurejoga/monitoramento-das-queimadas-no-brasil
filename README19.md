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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 759d4fc5-c1c1-3580-9c4b-326fcb905451 | -11.4939 | -44.179 | 2025-10-17 02:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 8a2b303b-c437-3bb6-847c-8ef0f0b8a949 | -4.4061 | -43.3816 | 2025-10-17 02:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 7e417b97-4046-3a37-8d02-080d10521a18 | -10.2745 | -44.0481 | 2025-10-17 02:10:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 0c3e6298-7186-32ab-bd3d-a52ef075c533 | -14.3424 | -51.4234 | 2025-10-17 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| e079d2a1-eb40-3aa7-8c80-38687fffa6aa | -11.398 | -44.1933 | 2025-10-17 02:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| a925bd72-5531-3984-86f6-e7714c1d5e5b | -14.342 | -51.4449 | 2025-10-17 02:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 5158cf24-4b48-3a55-a22c-c16052f28371 | 1.7848 | -55.9014 | 2025-10-17 02:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 406b990f-3a7a-3d00-be8c-a948cf09c80e | -10.5136 | -43.4052 | 2025-10-17 02:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 32.9 |
| c6849779-0f75-301b-9cb9-130b88d37535 | -3.236 | -45.9639 | 2025-10-17 02:20:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 52.4 |
| e862357e-a23e-396e-8131-6325986c7a95 | -11.4939 | -44.179 | 2025-10-17 02:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| f5782c12-4f52-3416-9e23-f4e84294dc65 | -14.3225 | -53.7718 | 2025-10-17 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 63.5 |
| e2e129f0-f6c9-302a-8cde-7d95defd4bc9 | -11.496 | -44.0617 | 2025-10-17 02:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 140.4 |
| 5259781a-3c02-3365-805c-d6d2159b2888 | -11.7625 | -51.1451 | 2025-10-17 02:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 39f3c579-d8f6-31e5-b352-31f3322fd471 | -3.2546 | -45.9632 | 2025-10-17 02:20:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 31fe712b-5556-3580-9bbe-b455392810ec | -11.4748 | -44.1819 | 2025-10-17 02:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 4f2ca6cd-7645-3dcb-a626-2d78ffe49ef8 | -11.3976 | -44.2167 | 2025-10-17 02:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 62.5 |
| c6799006-6da6-3b78-a4cc-330185a82a4d | -3.2359 | -45.9862 | 2025-10-17 02:20:00 | GOES-19 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 35.8 |
| e6ba6339-9f0d-3166-8769-68911f108589 | -10.2939 | -44.0221 | 2025-10-17 02:20:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 158.9 |
| 74352eb4-0f96-342f-ab44-0e2c075cba95 | -10.2748 | -44.0247 | 2025-10-17 02:20:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 147.5 |
| b8c0eda6-fa36-35e5-a589-027725f44100 | -11.4731 | -44.2756 | 2025-10-17 02:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 6906fdba-c27b-3a5e-8bb0-af8be37a821d | -14.3222 | -53.7927 | 2025-10-17 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 8b8f239a-f955-3c40-b3b5-2459d398e3a3 | -10.2745 | -44.0481 | 2025-10-17 02:20:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 61bc4dbe-7252-3c3d-8655-d03fc3cf9829 | -11.4172 | -44.1904 | 2025-10-17 02:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 0efda011-07e3-3e4f-9384-4eda31da85b4 | -10.5132 | -43.4289 | 2025-10-17 02:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 82cb606d-52bf-33ff-96ca-07690bf13027 | -2.7401 | -49.3927 | 2025-10-17 02:20:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| f7235c0b-89b0-36ed-8c79-6aada36d22a0 | -3.5028 | -52.4938 | 2025-10-17 02:20:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 62.1 |
| e2d912c0-ddde-3866-bdc6-04e9acce6eca | -4.4059 | -43.4049 | 2025-10-17 02:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 35.2 |
| e083e2b3-a346-3f7a-8fed-3b6edf5b9bdc | -8.7215 | -43.868 | 2025-10-17 02:20:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 32945b4c-3a96-36b0-bf52-70ab22873a06 | -10.2935 | -44.0455 | 2025-10-17 02:20:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 97.6 |
| 2212b8b5-9f0f-3306-ba8c-1aac7dcbf427 | -11.4965 | -44.0382 | 2025-10-17 02:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 37566631-70f7-34d6-8e41-099fb53aab16 | -11.5152 | -44.0588 | 2025-10-17 02:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 42d9363b-ef50-3540-835d-575c828baa32 | -10.4941 | -43.4315 | 2025-10-17 02:20:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 8ef99036-b855-38ec-aba3-2c0a79428286 | -11.398 | -44.1933 | 2025-10-17 02:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 87.5 |
| c44e3393-2e1a-33dc-8f30-b65d9deea00e | -8.7404 | -43.8659 | 2025-10-17 02:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 94.3 |
| ade9463c-5de8-322f-9dee-e0b10f935dda | -10.2745 | -44.0481 | 2025-10-17 02:30:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 55cf333c-07f2-3faf-9593-49a5413d9d78 | 1.7848 | -55.9014 | 2025-10-17 02:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| d49d5054-2882-3428-964a-c8590abaf3b8 | -5.872 | -44.7573 | 2025-10-17 02:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 38.9 |
| ca41c946-0a00-3a9f-a274-ca977485dda9 | -11.4939 | -44.179 | 2025-10-17 02:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 13c83b11-7c5b-3ba4-8561-1c9ee0030058 | -10.9475 | -49.7605 | 2025-10-17 02:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 2d087405-e464-3287-a77c-74c58af1b1b1 | -10.534 | -49.5471 | 2025-10-17 02:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 2b692c7b-f132-38e1-8e07-1a0ed402fd45 | -11.4731 | -44.2756 | 2025-10-17 02:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 90.1 |
| f4b476df-9408-3b99-83e0-eb2388d697b8 | -10.9665 | -49.7583 | 2025-10-17 02:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 4ec19b40-e4ed-350a-9fc6-2300fe3f1ed1 | 1.8402 | -55.7034 | 2025-10-17 02:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 1e90ecb8-b8f2-3577-9394-d0ef19c7c5c3 | -10.5132 | -43.4289 | 2025-10-17 02:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 7e9380fb-db0d-39bf-97aa-594853b4aa65 | -3.5028 | -52.4938 | 2025-10-17 02:30:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 2ecad05e-a17f-35fb-8c5d-3fbcb5988a58 | -11.4735 | -44.2522 | 2025-10-17 02:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 96.0 |
| e74911b2-0c1c-3632-9bd7-23cf322a7676 | -10.2748 | -44.0247 | 2025-10-17 02:30:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 131.0 |
| 09f31188-8765-3fec-9a7c-a940613b9ad2 | -10.5136 | -43.4052 | 2025-10-17 02:30:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 42.4 |
| e8a0e42e-c91b-38e6-9221-68cfac52b3dd | -4.4059 | -43.4049 | 2025-10-17 02:30:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| d1af2576-be29-344b-806c-6d9c5342dc61 | -11.4748 | -44.1819 | 2025-10-17 02:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 9530c6a0-0f70-3c33-9489-94df282f8813 | -10.2935 | -44.0455 | 2025-10-17 02:30:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 7a8bb630-8557-3644-a4c2-6e5b12dd74eb | -10.2939 | -44.0221 | 2025-10-17 02:30:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 153.2 |
| c58d18a1-1097-36d8-8d20-68e05e6d7e5d | -11.496 | -44.0617 | 2025-10-17 02:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 140.0 |
| e4b9a8c0-b003-3e6c-85d8-a0f769d2b9b8 | 1.8586 | -55.6637 | 2025-10-17 02:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 51.4 |
| fa0cb024-4efd-37b2-829e-4589d5202744 | -11.4944 | -44.1556 | 2025-10-17 02:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| a3a4798d-6da6-36b7-b842-8177433fd97f | -8.4641 | -46.2482 | 2025-10-17 02:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| e594cd91-aa8b-3311-9d0d-f49e9704de85 | -5.8907 | -44.7559 | 2025-10-17 02:30:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| ac23bb1b-d82b-3623-9c05-f803954649e3 | -11.5152 | -44.0588 | 2025-10-17 02:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| c250612b-9a47-3c94-a07e-13637da7af0b | -11.7625 | -51.1451 | 2025-10-17 02:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.2 |
| ede330ba-91d8-3775-9253-83c7cbf00acb | -3.5212 | -52.4932 | 2025-10-17 02:30:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 237cddb6-c71a-39d8-a25f-5de5d86994af | -11.4965 | -44.0382 | 2025-10-17 02:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 64.6 |
| bbf33e7a-c225-30bf-a0bc-ce329a222fb0 | -11.398 | -44.1933 | 2025-10-17 02:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| f50b9077-637c-31c2-a0e7-c83c0e0044fb | -8.4528 | -44.1767 | 2025-10-17 02:30:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 67.0 |
| c0ad56e5-4a33-38ef-bc4f-d48c67ba4f03 | 1.8402 | -55.6837 | 2025-10-17 02:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 87ea5b1b-819a-3f85-8268-7ee411c0097f | -2.7401 | -49.3927 | 2025-10-17 02:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 4cb2c8de-9175-36c2-999d-cc4bc7162ad3 | -14.342 | -51.4449 | 2025-10-17 02:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 57.2 |
| f6dd7886-8edc-3722-9d61-696f777d92c6 | -14.3227 | -51.4475 | 2025-10-17 02:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 52.8 |
| f208b419-4c47-3226-90e8-3df4f047acb0 | 1.8402 | -55.7034 | 2025-10-17 02:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| ab440235-c61b-3d97-b74d-7641da1f43a2 | -11.398 | -44.1933 | 2025-10-17 02:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 807446e7-53d4-31b5-be38-c3efb9ea896b | -11.3976 | -44.2167 | 2025-10-17 02:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 8d7bc8f6-6179-359e-aef7-e3e470c60993 | -14.3417 | -51.4663 | 2025-10-17 02:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 80fbad35-daaa-307d-aca9-c1bd2d115655 | -10.5136 | -43.4052 | 2025-10-17 02:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 1beaf3ac-a0c7-397e-b03a-c81c2553611b | -10.2748 | -44.0247 | 2025-10-17 02:40:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 123.1 |
| c71a25fd-6ebe-319f-b43b-8d16fb14a38c | -8.4641 | -46.2482 | 2025-10-17 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 826b03c1-d4d0-34c5-bcdd-c924fe77fb03 | -10.534 | -49.5471 | 2025-10-17 02:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 2a39e389-e582-3d4e-b2ac-e6dd29b6ec0a | -11.5152 | -44.0588 | 2025-10-17 02:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 67f2c6df-f9f4-3f44-9504-d59e455e9b65 | -3.5028 | -52.4938 | 2025-10-17 02:40:00 | GOES-19 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| ad8f05a5-31d3-3071-ad5d-920d1adb5e10 | -11.7625 | -51.1451 | 2025-10-17 02:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 91dbc2f1-6da6-35dc-b16c-812be5374eed | -2.7401 | -49.3927 | 2025-10-17 02:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 3195453e-e10c-31ec-b4b4-f5d2c940b332 | -11.496 | -44.0617 | 2025-10-17 02:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 2ea253aa-bbba-3687-81b8-21a3a364ced6 | -9.1375 | -46.6485 | 2025-10-17 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 85047ffd-5a92-324f-b0ab-e3a08f4d3e95 | 1.8402 | -55.6837 | 2025-10-17 02:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 6ddfd996-46b0-3ee8-a4a4-7eff76e0fbad | -10.5132 | -43.4289 | 2025-10-17 02:40:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| aba8c88e-7509-3c7e-9db2-65f1cc0a0e12 | -11.4748 | -44.1819 | 2025-10-17 02:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| b88a7340-418e-3441-9bef-eb5a6082ce22 | -11.4939 | -44.179 | 2025-10-17 02:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 89626fe5-c01a-31c5-a355-e101900b843f | -11.4172 | -44.1904 | 2025-10-17 02:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| fd6e1b56-c46e-3bb4-856a-df35d608fb67 | -11.4731 | -44.2756 | 2025-10-17 02:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| c6006432-351a-398f-90b1-97f4a1284da6 | -10.2745 | -44.0481 | 2025-10-17 02:40:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 1ec60642-8f07-3f77-882b-a4dcbba7fc70 | -8.4453 | -46.2501 | 2025-10-17 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.3 |
| b1e34111-12b7-3d63-b406-2229b42d39bf | -10.2935 | -44.0455 | 2025-10-17 02:40:00 | GOES-19 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 6b5318ce-4c6d-3328-9b71-96f0810a53c8 | -14.3223 | -51.4689 | 2025-10-17 02:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 53.1 |
| d6a22aed-10c8-3aee-a877-0ab5bcf7c576 | -11.4735 | -44.2522 | 2025-10-17 02:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 2eae411f-ebd2-3041-9834-37fa6dda54d4 | -8.4644 | -46.2257 | 2025-10-17 02:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| e19fe1d4-a36a-34a5-87bc-7ff70034c4b8 | -10.2939 | -44.0221 | 2025-10-17 02:40:00 | GOES-19 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 146.1 |
| e106ce52-623e-3b04-9405-6d0f1018dec1 | -11.496 | -44.0617 | 2025-10-17 02:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 118.5 |
| bbad99d6-4dbe-3bdb-8eab-338b8163ba20 | -14.3223 | -51.4689 | 2025-10-17 02:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 58e40ca4-71df-34d2-9b3c-eb66e1701731 | -8.4453 | -46.2501 | 2025-10-17 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| b8109e75-723a-3838-9b2f-7c742b23d571 | -4.4059 | -43.4049 | 2025-10-17 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 34.2 |
| f941ce9f-e26f-31f1-8721-53b12f013c92 | -10.5136 | -43.4052 | 2025-10-17 02:50:00 | GOES-19 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 73.8 |
| b401fd97-cd6a-3c54-adf0-8c696265ce95 | -9.1375 | -46.6485 | 2025-10-17 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |


[Clique aqui para ver as próximas entradas](README20.md)
