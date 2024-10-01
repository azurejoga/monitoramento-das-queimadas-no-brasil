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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3ebfe25c-014e-36d3-9a9e-f1e907fd203c | -21.50542 | -49.83502 | 2024-10-01 05:08:00 | NOAA-21 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9e49a342-5350-3bf4-bdc7-d18746d017d2 | -21.50503 | -49.83677 | 2024-10-01 05:08:00 | NOAA-21 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 27e8b1b8-df28-3b27-83ec-3eec5e54f358 | -21.30416 | -49.23091 | 2024-10-01 05:08:00 | NOAA-21 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| bc285ce2-ff6d-39c1-8642-bb1ef66423a2 | -16.36382 | -49.56963 | 2024-10-01 05:08:00 | NOAA-21 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 76b34a94-ffd4-3c29-a5c0-246a4c984a2e | -16.36347 | -49.57265 | 2024-10-01 05:08:00 | NOAA-21 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 08a05bd0-d18f-357e-99ab-af34e6b35643 | -16.3588 | -49.56903 | 2024-10-01 05:08:00 | NOAA-21 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a61a9482-54c8-3140-810e-3fa9c71f62b1 | -16.35845 | -49.57205 | 2024-10-01 05:08:00 | NOAA-21 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 592f36a5-a175-306e-b61f-eeacca6377bd | -15.1991 | -49.42946 | 2024-10-01 05:08:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4044e06e-e05f-3bcb-b326-46459c80a3e4 | -15.19844 | -49.43507 | 2024-10-01 05:08:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 20c1e843-af7b-33a5-8b1a-5d91d3e91574 | -15.19414 | -49.42862 | 2024-10-01 05:08:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 8d92dc9f-8d33-35c9-9958-095681a86725 | -15.19347 | -49.43423 | 2024-10-01 05:08:00 | NOAA-21 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 6c62b018-675a-3ef0-94b9-9aaf4f446205 | -17.12798 | -49.87098 | 2024-10-01 05:08:00 | NOAA-21 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1d4051f-4e8d-332e-a49d-d8d844938320 | -17.86638 | -49.91183 | 2024-10-01 05:08:00 | NOAA-21 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1db88d6a-64bf-3cff-8efa-9f2c397e3d68 | -20.07337 | -51.09784 | 2024-10-01 05:08:00 | NOAA-21 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 620f10d6-47be-3870-bd0b-ac9fa2fc3eb2 | -20.17298 | -50.00644 | 2024-10-01 05:08:00 | NOAA-21 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d10799d2-127c-3cdb-8a41-ae0006654fbf | -20.17264 | -50.00962 | 2024-10-01 05:08:00 | NOAA-21 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 2c1b33eb-f553-31cb-ad80-362b0d386e9d | -16.66126 | -50.60189 | 2024-10-01 05:08:00 | NOAA-21 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 81326595-6942-387d-93fe-2007f64a69de | -16.66655 | -50.59755 | 2024-10-01 05:08:00 | NOAA-21 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 36.8 |
| fe7dd5b3-740c-3f36-9e7c-8005b4dd8ca7 | -16.66717 | -50.59232 | 2024-10-01 05:08:00 | NOAA-21 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 3807f464-3542-32a2-a4f4-65b77428d63f | -16.66595 | -50.60258 | 2024-10-01 05:08:00 | NOAA-21 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 0e985c8a-7812-3bd9-8072-d29dd6aef646 | -16.66186 | -50.59684 | 2024-10-01 05:08:00 | NOAA-21 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 846a24a1-a200-382c-ac8f-628381b7ceca | -16.10368 | -50.33924 | 2024-10-01 05:08:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5284bdea-b418-3770-b316-c1f26672c5d6 | -16.10307 | -50.34454 | 2024-10-01 05:08:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 673f7719-b4d4-3507-8894-740ac3a25dd3 | -16.10284 | -50.33727 | 2024-10-01 05:08:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2c981c78-9e13-3fb7-8df0-0d7d7ad0331f | -16.10219 | -50.3426 | 2024-10-01 05:08:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cafa5045-c704-3aa1-90cf-f601515c923c | -16.09864 | -50.41034 | 2024-10-01 05:08:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed3a3dfa-144e-3e9c-9bcb-2d5458a1ee04 | -16.09801 | -50.33733 | 2024-10-01 05:08:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 18966a6f-bf03-3e66-8a04-63ca391d2e6a | -16.09525 | -50.41215 | 2024-10-01 05:08:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b47d289a-ac4f-3c94-b26d-fbd687d72b42 | -16.09388 | -50.40998 | 2024-10-01 05:08:00 | NOAA-21 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a6140486-a242-3d13-a005-172821b07829 | -16.09387 | -50.33172 | 2024-10-01 05:08:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6b38a041-b341-3d60-8d8d-57ad57d61381 | -16.0932 | -50.33718 | 2024-10-01 05:08:00 | NOAA-21 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 08db5b60-0e7a-3e8f-a600-839f26be0126 | -16.08033 | -50.40303 | 2024-10-01 05:08:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98a7db23-7837-3342-8c34-bc77653e421e | -16.07464 | -50.37079 | 2024-10-01 05:08:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 49a65547-7006-3dd4-b059-45575070417e | -16.07405 | -50.37566 | 2024-10-01 05:08:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4ce99a86-934f-363b-b7f4-e819ee8ce7c6 | -16.07178 | -50.35474 | 2024-10-01 05:08:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cd61008e-2c5f-3f16-bdaa-704d2f4a9cc0 | -16.07115 | -50.35989 | 2024-10-01 05:08:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 93ab0a92-f800-30d4-8a93-b3d18961ca5a | -16.07055 | -50.36483 | 2024-10-01 05:08:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8eb3d80a-da40-368d-9d4a-2d21bc287b13 | -16.06997 | -50.36962 | 2024-10-01 05:08:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8750b516-3638-34e6-a20f-845473ab8aba | -16.0659 | -50.36349 | 2024-10-01 05:08:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b987cb03-c461-3a6d-ae53-cda99c34dfe6 | -19.31547 | -52.11227 | 2024-10-01 05:08:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 46054652-84fe-34af-b6ed-95461fdf9a61 | -19.31492 | -52.11675 | 2024-10-01 05:08:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51b280ec-6bc6-31e4-8b98-5edb7d674ead | -19.30781 | -52.13846 | 2024-10-01 05:08:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d5e31a50-37e3-350f-b4a7-116de990f1da | -19.30341 | -52.13787 | 2024-10-01 05:08:00 | NOAA-21 | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97dad0b6-975f-3ac0-883b-51a95ad20dc4 | -19.30117 | -52.11934 | 2024-10-01 05:08:00 | NOAA-21 | INOCÊNCIA | MATO GROSSO DO SUL | Brasil | 5004403 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8de149cf-80db-3a6f-90b8-d5123aaee2d1 | -20.07711 | -51.33627 | 2024-10-01 05:08:00 | NOAA-21 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bc68362e-cee5-3f17-85e5-441ada9be46b | -20.07479 | -51.3353 | 2024-10-01 05:08:00 | NOAA-21 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 80f455c2-0621-3c23-add5-45ef09a3209e | -20.07418 | -51.34055 | 2024-10-01 05:08:00 | NOAA-21 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48d99b6e-06c9-3dad-bf73-04e35f129810 | -20.07186 | -51.34078 | 2024-10-01 05:08:00 | NOAA-21 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 82621342-4e32-3629-9f47-bcc036cd327e | -21.38929 | -52.83717 | 2024-10-01 05:08:00 | NOAA-21 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| edbb211c-fd67-39de-a01c-ea731e27e7dc | -16.62716 | -52.58175 | 2024-10-01 05:08:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0d4a16e6-d1cc-3786-a59a-674c1a09ae02 | -16.62667 | -52.58556 | 2024-10-01 05:08:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7c455c8b-0a66-3059-a373-f56d6e83da9c | -16.62354 | -52.57717 | 2024-10-01 05:08:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9333eb00-7bef-3fd4-890b-a9e094cab3f6 | -16.62305 | -52.58102 | 2024-10-01 05:08:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1af8a59-a0c1-3e7f-b978-6f30c0cd7d14 | -16.62256 | -52.58485 | 2024-10-01 05:08:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbcb0447-9c6b-3358-98d2-05cd63c5e05b | -17.12807 | -52.19797 | 2024-10-01 05:08:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3337f455-b293-3700-819d-c1e0c86ac3ab | -17.70793 | -53.20651 | 2024-10-01 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 510ff516-54e2-307e-a4ae-9893c8143879 | -17.70747 | -53.21014 | 2024-10-01 05:08:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 84441da0-5e34-3507-8834-fbbffe28b2a7 | -17.64064 | -53.14536 | 2024-10-01 05:08:00 | NOAA-21 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 105d180a-d34e-31a5-8138-f4298498b1c3 | -17.62976 | -53.16617 | 2024-10-01 05:08:00 | NOAA-21 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d5da46b2-ed0f-3923-a71a-6b2675158b01 | -17.62929 | -53.16976 | 2024-10-01 05:08:00 | NOAA-21 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e457a1a1-6c55-319c-b870-b0eae8d9ef81 | -18.64498 | -52.48753 | 2024-10-01 05:08:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4c9ba4de-2d6d-3d30-879b-11ab425b7752 | -18.60329 | -53.03785 | 2024-10-01 05:08:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 80d7e0d9-c8d3-3f43-8631-0a0306f2d160 | -18.59917 | -53.03733 | 2024-10-01 05:08:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ab3a4520-a086-3ac8-bf71-d4410f3e7373 | -18.59728 | -53.05254 | 2024-10-01 05:08:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 07446785-b483-3ce8-a625-c9b51a0f38fc | -18.5968 | -53.0564 | 2024-10-01 05:08:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0126c631-dcaa-3fb0-b9e7-3529e7ab254b | -18.59459 | -53.04054 | 2024-10-01 05:08:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2b4bc783-aaaa-3dfc-ba05-84ae40a067f2 | -18.59317 | -53.052 | 2024-10-01 05:08:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| cab0232c-2381-39e7-bad8-b3be33da919e | -18.59269 | -53.05586 | 2024-10-01 05:08:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 98c4df35-ac95-3423-ac25-4abf83a95887 | -18.5881 | -53.05915 | 2024-10-01 05:08:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c4bf25f-addc-3e79-9b0e-e107cdf69ee8 | -20.81181 | -53.13028 | 2024-10-01 05:08:00 | NOAA-21 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7740de91-41f4-3916-8348-66616c839a79 | -20.81131 | -53.13431 | 2024-10-01 05:08:00 | NOAA-21 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 281ca86e-d1de-3a60-a26c-2587e5818f97 | -20.8081 | -53.12563 | 2024-10-01 05:08:00 | NOAA-21 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e31fb206-35a3-336d-9bc7-6401da67a3ea | -20.8071 | -53.13371 | 2024-10-01 05:08:00 | NOAA-21 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f65fc713-01ca-3f24-bbfe-d94004758852 | -20.80389 | -53.12502 | 2024-10-01 05:08:00 | NOAA-21 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d13bc19-aa0e-3489-a712-28bc2a5744eb | -20.80339 | -53.12905 | 2024-10-01 05:08:00 | NOAA-21 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a65177bd-e13a-3a6d-83bb-0166255cadbd | -20.80018 | -53.12033 | 2024-10-01 05:08:00 | NOAA-21 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8400349e-fb40-344f-85f5-11e4450c07b4 | -20.79969 | -53.12436 | 2024-10-01 05:08:00 | NOAA-21 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e9527909-3243-3175-9f5a-5c386b116807 | -20.79598 | -53.11965 | 2024-10-01 05:08:00 | NOAA-21 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb1c07d4-99e7-3377-b032-f616e2e8834a | -20.79327 | -53.10676 | 2024-10-01 05:08:00 | NOAA-21 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e394b36-535b-3f47-ae97-0bcf4da80b6d | -20.79277 | -53.11086 | 2024-10-01 05:08:00 | NOAA-21 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aac0ad40-7828-3e76-ba37-498fecd3d303 | -20.47855 | -53.67541 | 2024-10-01 05:08:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7df159f1-25bf-3a27-a319-85d6dd3e17a9 | -20.31946 | -53.28873 | 2024-10-01 05:08:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35fd2155-56a2-348f-af06-d0bb5747dd72 | -20.31897 | -53.29268 | 2024-10-01 05:08:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f5e1f055-c082-3792-9abe-30bbafc81a2a | -22.00093 | -54.64445 | 2024-10-01 05:08:00 | NOAA-21 | DOURADINA | MATO GROSSO DO SUL | Brasil | 5003504 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| cecc0706-f4fb-305c-aaf2-fba83b04d2c8 | -15.02253 | -53.32029 | 2024-10-01 05:08:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abe94f21-2587-3858-a93a-d21f67f9eac8 | -16.4567 | -53.93185 | 2024-10-01 05:08:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d31f73d6-58d0-3fa6-a161-206f6ec1c90d | -16.45357 | -53.92643 | 2024-10-01 05:08:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b6b8079e-c4d2-3533-97ed-a48413709d07 | -16.45229 | -53.93589 | 2024-10-01 05:08:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0f7ff76d-d01b-3e36-afb0-06bb45fbe6f3 | -16.44979 | -53.92584 | 2024-10-01 05:08:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 715c393a-0557-36bc-8e04-b35c692d2f53 | -16.44851 | -53.93528 | 2024-10-01 05:08:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c03bed57-9032-378f-be6a-7fa3c9fc12c4 | -16.44601 | -53.92524 | 2024-10-01 05:08:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68196f8f-8412-326c-8477-c57583e0c155 | -16.44536 | -53.93005 | 2024-10-01 05:08:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ebbc68e3-f388-31c3-bc8b-1ce7a4f54053 | -16.43911 | -53.91914 | 2024-10-01 05:08:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8626539d-4540-3e65-bbbe-c6ed9dd82c5f | -16.43534 | -53.91848 | 2024-10-01 05:08:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a8879c7-ee8e-340a-8178-25916937b53b | -16.43156 | -53.91784 | 2024-10-01 05:08:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 10f5ce8a-41c9-393f-a9cf-6ba68af7c286 | -16.42714 | -53.92202 | 2024-10-01 05:08:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4163be99-b2db-33dc-9c85-88d3e885c5af | -16.42336 | -53.9214 | 2024-10-01 05:08:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2f14e3b4-8ccc-3893-bf07-391645e457eb | -16.09291 | -53.54206 | 2024-10-01 05:08:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f2b13fd-65a0-339d-9181-1bbca474725f | -16.08906 | -53.54148 | 2024-10-01 05:08:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7d65eb16-7c49-36c0-b30d-3e4c7f434bd5 | -16.0885 | -53.51663 | 2024-10-01 05:08:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README128.md)
