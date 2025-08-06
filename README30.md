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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1d5dead-6928-3888-be90-0d247ceb39fe | -10.22321 | -59.41057 | 2025-08-06 06:01:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7096dfcd-a641-33b1-bd58-e46f53397df4 | -8.92094 | -60.58788 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 96ef9ce1-1d5f-3733-b16a-d62892fb8ff4 | -8.91735 | -60.57126 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f92767c3-0dd5-36dc-93d6-b8e82afb5deb | -8.91336 | -60.75643 | 2025-08-06 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e8757b1f-d796-3ff4-8230-74f103bca248 | -3.0384 | -59.9108 | 2025-08-06 06:10:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 559196ae-f9a7-36fa-a3fc-fecd229b35cc | -8.9215 | -60.7297 | 2025-08-06 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 8214db39-b341-34d7-a5a1-270ad7e8afd4 | -8.9213 | -60.7489 | 2025-08-06 06:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 57b1c80d-0401-3eda-bd35-310c1d80c2fd | -3.0566 | -59.9105 | 2025-08-06 06:10:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| edadc0c2-dcea-35a6-9fca-911347562a68 | -21.0124 | -50.0445 | 2025-08-06 06:20:00 | GOES-19 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.8 |
| e8c24734-3c3d-3eb9-9b52-57ae470af058 | -21.033 | -50.0401 | 2025-08-06 06:20:00 | GOES-19 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 49.5 |
| 78a7f8a3-0df8-395f-8a8c-1b1efd0f35d0 | -8.9213 | -60.7489 | 2025-08-06 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.3 |
| ed87ad53-e815-35a3-b169-27f42f9c7a3f | -8.9215 | -60.7297 | 2025-08-06 06:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| e38993dd-daf9-3c4b-acf1-ca35739d6418 | -8.9213 | -60.7489 | 2025-08-06 06:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 238dc460-57a4-3a4b-8b66-8947a479981a | -3.0384 | -59.9108 | 2025-08-06 06:30:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 45e6d3b5-b1f2-300e-a795-8e25ab072209 | -3.0566 | -59.9105 | 2025-08-06 06:30:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| b0d5e3d3-44c5-38da-a92d-14ec57a2ecf7 | -8.9213 | -60.7489 | 2025-08-06 06:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 34eacd29-df26-3b08-a8f8-4c81a2c17480 | -3.0566 | -59.9105 | 2025-08-06 06:40:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| f482b8b3-0ac9-3516-a59a-7dd9d0f3549d | -3.0466 | -59.9109 | 2025-08-06 06:46:00 | AQUA_M-M | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 8b46706d-6298-32e8-aad1-ac623e2e9e72 | -3.04529 | -59.91963 | 2025-08-06 06:46:00 | AQUA_M-M | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 71f0b509-90b1-3f71-9699-659c481044ee | -8.90487 | -60.58436 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 211.5 |
| b2a5dbb7-b2c8-3684-914a-ef33882695ac | -8.92253 | -60.58697 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 024fc7ac-41e7-31fd-acf2-e88cdf209594 | -8.9212 | -60.59589 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 4b1529c4-9268-3a92-bcaf-ca3e14005674 | -8.90885 | -60.55759 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 2b4879b2-2e40-3305-ac4e-ba87653fc957 | -8.91759 | -60.7408 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| a6498596-6550-3d67-94ee-6c41f97d28e4 | -9.70508 | -61.29157 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2c49f5f9-92e0-36e1-9dba-8ee846fb716d | -8.91237 | -60.59459 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 27baec04-923c-3820-a9b8-f1703666fec8 | -8.89736 | -60.57414 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 973e7052-8f65-3e18-9667-ebb75c5eef21 | -8.92034 | -60.54105 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 2ee46faf-bf86-34f7-8c41-4d057be5e70c | -8.91493 | -60.75856 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 813916ba-dfb8-3c7e-a060-7b802ce923b5 | -8.9115 | -60.53975 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 5f1cead8-849b-3a45-90b4-1e4147749280 | -8.91891 | -60.73193 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 74597b20-ce53-3e3e-996b-e5a472badd47 | -8.90877 | -60.73951 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| e41f655d-a51c-3145-bcee-632def487727 | -8.91768 | -60.5589 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 4c57e77a-6cb7-35de-ba55-1d933548bb18 | -8.89869 | -60.5652 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 36.4 |
| bab553aa-fb39-3f17-b637-d354bdea09f6 | -13.06242 | -56.85793 | 2025-08-06 06:48:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 958611b3-2231-387a-86f4-9bdac8401b5a | -13.07398 | -56.85933 | 2025-08-06 06:48:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 31.6 |
| 16f7164c-4111-3992-8652-93af391d78e7 | -13.06477 | -56.85279 | 2025-08-06 06:48:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 4b9be1b1-604b-3ff8-a5e5-e81217abb98a | -13.05089 | -56.85635 | 2025-08-06 06:48:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| fc16c0f0-1f5f-344b-81ec-073b7e657e3d | -8.89604 | -60.58306 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 264ad112-eff0-30a9-86f4-769753e2f7ab | -8.9101 | -60.73063 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ef240543-0081-3758-b82e-3cc2e0e96e87 | -8.90001 | -60.55629 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 198.1 |
| d2b87214-8025-31bb-b266-9e0d2d276d4b | -8.91017 | -60.54866 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 108.2 |
| f9b05e6a-e3fc-3c8b-a8fe-7c2552b94f5a | -8.90134 | -60.54736 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| b2110952-7c0c-3e0e-a5e1-f2fe1636ab49 | -8.91987 | -60.60481 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f9aad498-bab9-306e-b8f9-02914ca26c1e | -8.91901 | -60.54997 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.8 |
| f7aa9de7-9ac6-3691-89e1-ef70f5b8c243 | -8.89471 | -60.59198 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c03834b8-0b5f-39b6-b758-2cf68192038d | -13.06262 | -56.86891 | 2025-08-06 06:48:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 01e4645e-f537-3333-b5d9-a58f491d6c5e | -8.90619 | -60.57544 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 2965a866-4b7f-321c-8df3-1a2dab8783bc | -8.9137 | -60.58566 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 162.7 |
| fa857b71-d5e7-3ad4-8b5c-ab2319f56c19 | -8.91626 | -60.74968 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 703876b2-0201-317e-bce9-3c0c33442255 | -8.90221 | -60.6022 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| ac44f123-7ae5-32b4-ab41-c06154e040a5 | -9.70375 | -61.30042 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8caea0bf-0290-32bd-9597-c453e487a1f8 | -8.91635 | -60.56782 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 742122cf-7aa5-3f27-8dfb-595c61f24013 | -8.91503 | -60.57674 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 37.7 |
| a2a88bc8-cd01-357c-81de-1d10b1e27e3d | -9.46417 | -57.84882 | 2025-08-06 06:48:00 | AQUA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 5e2dee2d-a3b7-3711-8f01-8f4d28bb24c6 | -10.22175 | -59.41361 | 2025-08-06 06:48:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ccf5edb0-1289-3823-8bd1-280fb2c30701 | -10.22318 | -59.40379 | 2025-08-06 06:48:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d8d2316f-9008-36ff-af25-b569ad320401 | -8.92386 | -60.57804 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 98e57943-099b-39f1-9e7d-5b52c4f95752 | -8.91104 | -60.60351 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 25.3 |
| c68a7e6a-0103-3c94-b5c5-a0b132c43467 | -8.91283 | -60.5308 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 85583ee1-8db5-3eb2-9477-810ae81a8fe7 | -8.90752 | -60.56651 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| f1b843bd-6b93-3fcd-b13f-009f799d1106 | -8.90354 | -60.59328 | 2025-08-06 06:48:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 311.4 |
| 838a26df-abc5-36b4-995e-689fc91ff173 | -3.0384 | -59.9108 | 2025-08-06 06:50:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 0c4b55bb-6ef7-3abe-a5f8-d85c82c10ea1 | -8.9215 | -60.7297 | 2025-08-06 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 589b952a-0c96-3d03-9b3f-c40b41c9c6a4 | -8.9213 | -60.7489 | 2025-08-06 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 6f0e6f5f-5763-35dd-9009-9c36e8e15a9a | -3.0384 | -59.9108 | 2025-08-06 07:00:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 3621a631-3f65-3efc-9472-1c5ff36ab181 | -8.9213 | -60.7489 | 2025-08-06 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| dab58fe6-a2af-3fbd-b44f-e3dbfc3b7615 | -3.0566 | -59.9105 | 2025-08-06 07:00:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 328137fc-8e70-3acb-b588-220e4fee64d2 | -3.0566 | -59.9105 | 2025-08-06 07:10:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| bcf0e123-2c2d-3f26-a11b-0cd8124d1bb6 | -3.0384 | -59.9108 | 2025-08-06 07:10:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| aed9af43-9dcd-36d2-8cbf-e9450b8a9aef | -8.9213 | -60.7489 | 2025-08-06 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 6f0c9ab4-4f3b-308c-900e-394532e90b23 | -3.0384 | -59.9108 | 2025-08-06 07:20:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 66dd330a-51f8-3989-b0ea-bc782ae230d9 | -8.9213 | -60.7489 | 2025-08-06 07:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 32b885b0-b895-3c8e-8e70-183be019b655 | -3.0566 | -59.9105 | 2025-08-06 07:20:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| b3d00445-8f64-3c39-a6ea-6f9a0db91358 | -3.0566 | -59.9105 | 2025-08-06 07:30:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| bda97c9c-7043-331d-a9fa-00893f2469e8 | -3.0384 | -59.9108 | 2025-08-06 07:30:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 4250664a-cf62-3ff2-b0da-cfcdf88001c6 | -11.4389 | -45.1385 | 2025-08-06 07:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 046f3ab2-1873-37ee-8939-5df06d691492 | -8.9213 | -60.7489 | 2025-08-06 07:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 4c35bfdd-ffb6-3f9c-8a1c-72798eb92730 | -8.9213 | -60.7489 | 2025-08-06 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.1 |
| b7b7646d-68f9-3a40-ad17-749c6d8d8490 | -3.0384 | -59.9108 | 2025-08-06 07:40:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| dfe9165a-22e1-3cbb-bc90-06fe29f12e66 | -3.0566 | -59.9105 | 2025-08-06 07:40:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 413a1a39-98ff-39e8-987f-dd3c5f039586 | -3.0384 | -59.9108 | 2025-08-06 07:50:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 4bb2070f-44c3-3ddf-8ab2-352f6498bb82 | -8.9213 | -60.7489 | 2025-08-06 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| ce3e6d27-e395-3f8e-b702-85238668436d | -3.0566 | -59.9105 | 2025-08-06 07:50:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| f1ef8ca5-74d7-3e13-8eb3-e172e015829a | -8.9213 | -60.7489 | 2025-08-06 08:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 1b826ff9-4bde-33bd-817e-73b17634b94c | -3.0566 | -59.9105 | 2025-08-06 08:00:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 5d417f3b-4fd3-34e4-af0f-592ddc7b294f | -3.0384 | -59.9108 | 2025-08-06 08:00:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 181142b5-3c30-3c13-b3a6-c936a3eb0f89 | -3.0566 | -59.9105 | 2025-08-06 08:10:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 538836c4-ad94-32fb-9cfd-925ced4df757 | -3.0384 | -59.9108 | 2025-08-06 08:10:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 56f9f288-ae8f-380d-a6e0-089610fe29c7 | -8.9213 | -60.7489 | 2025-08-06 08:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 40199265-1682-389b-a371-cf04537eb7c5 | -3.0384 | -59.9108 | 2025-08-06 08:20:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 958d338d-100a-398c-a90b-590c5205d227 | -21.1637 | -49.0049 | 2025-08-06 08:20:00 | GOES-19 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 48.0 |
| 9a017395-a4cb-3fd3-91c9-c5d2f9d0fe68 | -8.9213 | -60.7489 | 2025-08-06 08:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 8dc1f811-4668-3024-840b-ec1faed4cf54 | -3.0384 | -59.9108 | 2025-08-06 08:30:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| d941474a-2308-3f37-9c19-e2b8fc1c6b4b | -3.0566 | -59.9105 | 2025-08-06 08:30:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 0696da8c-4e96-3d0e-8a7c-58eb22ad776d | -8.9042 | -60.5385 | 2025-08-06 08:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 65677897-b7f0-315e-aa1b-f8d4151c8cb5 | -3.0384 | -59.9108 | 2025-08-06 08:40:00 | GOES-19 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 88.8 |
| 4e983ec7-b25d-35b5-a3c8-c85a1a2c2761 | -8.9228 | -60.5376 | 2025-08-06 08:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| e69f08ee-964b-38bb-9361-d6bb422d15bb | -8.9225 | -60.576 | 2025-08-06 08:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 1523eedc-f28c-3db8-9843-912276d173af | -8.9227 | -60.5568 | 2025-08-06 08:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.0 |


[Clique aqui para ver as próximas entradas](README31.md)
