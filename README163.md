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

## Dados Diários - Página 163

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66ee6bf4-0ad3-30b8-a2e5-fa836804b48f | -5.17 | -43.7276 | 2025-10-01 14:30:00 | GOES-19 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 115.8 |
| 97b9e4d2-890d-3994-9017-07338200fafe | -6.0437 | -42.4438 | 2025-10-01 14:30:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 83.0 |
| 039a80e6-d6e6-3c7a-ae45-40288bf87bad | -9.1889 | -48.5166 | 2025-10-01 14:30:00 | GOES-19 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| adcea7ee-fc02-3160-8dd4-8093411c1871 | -11.825 | -44.9437 | 2025-10-01 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 145.8 |
| 3b5a7f7a-7bd1-3066-b129-aacc72b261c0 | -12.3669 | -50.2187 | 2025-10-01 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 361.9 |
| 59cf5be0-c9b9-3685-b16e-e4250c780ce2 | -11.9332 | -49.905 | 2025-10-01 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 8efa2958-1440-377e-b9d7-38fa72f2c07f | -6.2813 | -45.022 | 2025-10-01 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 631bfd0d-ea92-3911-856d-f70a5c98db1c | -11.0988 | -49.7866 | 2025-10-01 14:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| ad6e1f6e-dce3-3f07-9927-b63a072e93f8 | -5.3091 | -42.761 | 2025-10-01 14:30:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 86.8 |
| 2af58b14-2281-3328-8728-d78357fcb8af | -8.5864 | -45.5141 | 2025-10-01 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 89.0 |
| c45bb501-f874-3d5b-a6df-8e912c7b4f8d | -13.3278 | -47.8313 | 2025-10-01 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 5c15d064-40dc-31db-a3ec-634a115729d4 | -8.5267 | -47.2879 | 2025-10-01 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 6e540704-1cb8-394c-9465-f5ee125af515 | -9.9959 | -43.6172 | 2025-10-01 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 157.2 |
| 78abc8d5-7a50-37b2-932e-fe3588f196f6 | -13.7872 | -48.0077 | 2025-10-01 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 93.1 |
| ba3423ec-d09f-33d1-9024-a3878d942083 | -6.544 | -44.9783 | 2025-10-01 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 1a535fe8-1a68-366f-8f6d-39775123159f | -11.383 | -45.0543 | 2025-10-01 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 119688fa-5dca-3b77-82e6-c1188c3db6a6 | -4.1574 | -44.2726 | 2025-10-01 14:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| b2662969-a081-3c7b-a640-1139e60b432d | -7.646 | -45.4489 | 2025-10-01 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| eb1c1c26-e216-3969-b8ca-9c381b049eac | -5.2903 | -42.7624 | 2025-10-01 14:30:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 112.1 |
| da584787-05f2-3386-8e75-f7e778d2f371 | -11.1178 | -49.7845 | 2025-10-01 14:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 04817462-297b-391f-92c2-d5631f383f16 | -9.4007 | -54.6984 | 2025-10-01 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 441a3a08-6798-3a8c-83e9-7429a3fddc2e | -8.483 | -47.7983 | 2025-10-01 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 6e4669ad-f7cc-309d-abc8-47c2bc09aa68 | -16.0221 | -50.8989 | 2025-10-01 14:30:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 242.5 |
| 357f2ec1-30aa-3436-b354-f5249cacb06f | -12.254 | -47.7837 | 2025-10-01 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 9370ce28-7910-3733-a59d-cf0941347f30 | -9.8049 | -48.9756 | 2025-10-01 14:30:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| f676b349-8647-3c11-a6b2-3cceedf831b0 | -13.7678 | -48.0106 | 2025-10-01 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 5f1077d6-843e-35ef-bcd7-2635a60d7e86 | -11.1181 | -49.7629 | 2025-10-01 14:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 7265c0e2-34da-32d0-a988-bac0d0e1da09 | -9.8331 | -48.276 | 2025-10-01 14:30:00 | GOES-19 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 1e32fbe9-c762-3f92-b0be-3bbd82db6d62 | -9.4455 | -47.6144 | 2025-10-01 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 133.5 |
| fdebcd99-a169-35e2-a4d6-8bbe2f776a42 | -15.2823 | -47.9461 | 2025-10-01 14:30:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 88765c8c-db3a-3a02-b708-8d87aa70bf09 | -7.6272 | -45.4507 | 2025-10-01 14:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 4ea25629-65b7-3dfc-9e24-d9b1d5c70e4a | -7.4412 | -47.0109 | 2025-10-01 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 276b720c-a102-389d-a760-e5f92bb2e1dd | -12.7819 | -50.5543 | 2025-10-01 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 290.8 |
| 99ebcd19-f3a9-3c3b-9b30-308784db5e46 | -8.4833 | -47.7763 | 2025-10-01 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| c30b7939-0d53-3523-b567-006502ee6827 | -8.5016 | -47.8184 | 2025-10-01 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 4d443d32-69d9-3eb0-a0a1-abb9f95df8b9 | -5.3195 | -43.7405 | 2025-10-01 14:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 7e26fa54-d8aa-3e1c-8e07-c5b800c08ff8 | -9.9391 | -43.6012 | 2025-10-01 14:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 467.6 |
| 7b618dd9-419f-33a4-9eb4-8554c590a1d2 | -9.1248 | -47.6256 | 2025-10-01 14:30:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 106.7 |
| ba3e3154-8d00-36d7-a824-98442845acdc | -10.6158 | -49.1056 | 2025-10-01 14:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 135f9700-d6e4-3108-8806-511836ead677 | -12.8831 | -46.9101 | 2025-10-01 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 0d0b9ea1-83e7-38f3-b9d9-7951253d5215 | -12.7822 | -50.5328 | 2025-10-01 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 151.2 |
| 4700cad0-0500-35a1-8986-1d87d9c936df | -14.3519 | -45.9206 | 2025-10-01 14:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 182.0 |
| 884a94f9-34bb-3391-b5e3-1f70e7ed6897 | -13.6703 | -48.07 | 2025-10-01 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 83.2 |
| e78c518b-cb2f-314d-a78a-bbcf6bc34ceb | -12.2156 | -47.7889 | 2025-10-01 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 62f859e6-da3b-3c6b-a24d-c699b2d9fbb7 | -12.801 | -50.5519 | 2025-10-01 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 231.3 |
| 2c092669-9a58-317f-b7fc-778eddb6cd6e | -11.7797 | -47.5806 | 2025-10-01 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 144.8 |
| dff12b8e-2ac0-3f8f-972f-def71bb3e8df | -12.8014 | -50.5304 | 2025-10-01 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 163.7 |
| 114cc8a1-7ff8-37b4-99a0-01d88c38a38a | -3.7974 | -42.1475 | 2025-10-01 14:30:00 | GOES-19 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 81.8 |
| 22eacc9f-3c29-3e51-8327-cd460d306537 | -11.1757 | -47.2134 | 2025-10-01 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 1e6d34da-80e7-36b9-ab42-95011f21a0b7 | -9.4192 | -54.7172 | 2025-10-01 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 0dc3e71f-21bb-33e4-8a50-04bd89010091 | -16.0225 | -50.8771 | 2025-10-01 14:30:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 203.5 |
| 1a34378c-8aaf-3e8f-9b04-2535ea4f3e0b | -12.2344 | -47.8086 | 2025-10-01 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 9ca2ea1a-6d10-3d09-99cb-30053f0a093e | -5.6293 | -44.7065 | 2025-10-01 14:30:00 | GOES-19 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 2e054488-b738-3e6c-8c8f-d121ed38131e | -11.8246 | -44.9669 | 2025-10-01 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 123.5 |
| c7a3b6be-6aa0-30a2-a462-5dec8ec2f0ec | -13.7876 | -47.9853 | 2025-10-01 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 8d3044cf-57ef-340a-8e90-f7f2565d9ac8 | -5.4156 | -41.3233 | 2025-10-01 14:30:00 | GOES-19 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 86.6 |
| f8ff6457-0f77-3602-93e3-14dbc206b7fb | -8.8609 | -47.6521 | 2025-10-01 14:30:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 7f3defc7-3ac2-3cda-a93a-209bb08413f8 | -4.1388 | -44.2736 | 2025-10-01 14:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 53aaf9d3-2d2c-3062-bd4f-5a294001f422 | -14.3514 | -45.9437 | 2025-10-01 14:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 168.7 |
| af00754e-e989-373f-8b53-7be096210e75 | -14.3709 | -45.9403 | 2025-10-01 14:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 99.4 |
| edae24bf-fa3c-3e68-9dcc-339cf332e19a | -12.8202 | -50.5495 | 2025-10-01 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 0693ee7d-9b21-3dac-92e9-9857a47bae92 | -8.672 | -47.7144 | 2025-10-01 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| b4168445-f6a8-307a-b0c7-42153dd810b5 | -12.2623 | -44.1306 | 2025-10-01 14:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 313.5 |
| a0c2fcd4-dde3-3ef0-ba97-83fd009eb6bf | -5.8062 | -43.7512 | 2025-10-01 14:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 0dd588da-3c44-33cc-8963-04a85fe6d5ff | -8.3869 | -47.9824 | 2025-10-01 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| e7571291-38a7-32b7-8176-ffc6c637f9e6 | -3.8885 | -42.5211 | 2025-10-01 14:30:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 157.7 |
| ef039c37-ab79-389f-975a-34d7c085815f | -14.3714 | -45.9172 | 2025-10-01 14:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 14308e55-28d9-33ed-93ae-a5aa66f14189 | -9.4458 | -47.5923 | 2025-10-01 14:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 180.6 |
| ee09d002-859a-3ab7-9957-24dcbbcf42d9 | -6.0625 | -42.4422 | 2025-10-01 14:30:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 150.5 |
| 10de32a5-5d8b-3756-b5e6-168189c45b34 | -12.4441 | -50.166 | 2025-10-01 14:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| b4e00413-f955-3dd7-91bf-6ff411c733de | -12.2153 | -47.8112 | 2025-10-01 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 40e6fe8e-01c1-33c4-848b-b513c923648a | -6.7168 | -44.5758 | 2025-10-01 14:30:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 387f00c9-b034-38d6-bbb7-adc8cdff6bd1 | -8.6911 | -47.6906 | 2025-10-01 14:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| b42f7c4b-294f-3be6-9eab-5c4dff5ab83a | -9.0236 | -46.7052 | 2025-10-01 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 1a6617a5-f79f-3d3f-a7d9-e29cff6a711c | -7.8353 | -46.9764 | 2025-10-01 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 6c7125da-a651-3b3a-a7ed-e49c6c87a4cb | -11.46 | -45.0202 | 2025-10-01 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 112.8 |
| c555295f-0c98-3d82-8b44-218cd4bd8511 | -5.4967 | -42.7471 | 2025-10-01 14:30:00 | GOES-19 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 88.4 |
| 9063c1ef-82a5-34b4-a45f-7dc62ae1978b | -9.0239 | -46.6828 | 2025-10-01 14:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 7dca1d81-06c7-3933-bc5d-6140ec061233 | -11.8622 | -45.0075 | 2025-10-01 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 162.3 |
| 8c575f14-193d-368e-8aa8-147e0b485e9c | -11.2711 | -47.2012 | 2025-10-01 14:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 4fe03075-3121-35bc-b79b-d953ef64d43d | -3.8698 | -42.5221 | 2025-10-01 14:30:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 111.7 |
| b7795047-6b2f-328f-8379-a54dbcf9c9a3 | -7.5563 | -46.7573 | 2025-10-01 14:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 17ddae24-2d6a-38d0-a10d-5ab705af6aa2 | -6.079 | -42.6773 | 2025-10-01 14:30:00 | GOES-19 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 78.9 |
| 99f70b07-f3d6-379c-91dc-d7de6db540fa | -6.0623 | -42.466 | 2025-10-01 14:30:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 75.5 |
| b8aa64a3-cd99-3912-9b60-0f3968811315 | -11.7793 | -47.6029 | 2025-10-01 14:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| b09c3053-b3c5-3b83-9a0b-4a17657e63cd | -12.4249 | -50.1684 | 2025-10-01 14:30:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 92.3 |
| d03cb435-fcb4-3677-8e2d-5ab494f0da41 | -6.0997 | -42.4865 | 2025-10-01 14:30:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 68.2 |
| 3d735abb-699d-3f33-9f6e-58c1e9f125e8 | -10.8433 | -45.3815 | 2025-10-01 14:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.9 |
| 82160d0d-13f3-3055-86e0-66daf039226e | -14.8212 | -45.8143 | 2025-10-01 14:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| ce9d089f-922f-3249-a315-7e082cd82faa | -10.9182 | -44.3092 | 2025-10-01 14:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 140.6 |
| 850c5fdc-e7c1-3a71-a71b-bc1a040d4dcc | -15.5384 | -45.214 | 2025-10-01 14:30:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 50e7431f-597b-38b2-8e3c-eec93dac3272 | -6.0811 | -42.4644 | 2025-10-01 14:30:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 70.5 |
| 9980c709-bdda-37f6-83a1-8f6622503e13 | -11.9411 | -47.0675 | 2025-10-01 14:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 226.4 |
| fdc7a586-d231-3f7f-946a-a9394b6b668f | -7.4571 | -47.2744 | 2025-10-01 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 8804e4f9-161f-3adb-9c8c-db234b30dddf | -6.0978 | -42.6758 | 2025-10-01 14:30:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 149.2 |
| a06061f0-9015-3518-9281-da98026a7c1f | -8.3867 | -48.0042 | 2025-10-01 14:30:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 46cc8215-1ee8-333a-b506-539af1878ee6 | -6.214 | -44.2272 | 2025-10-01 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 0c870351-e83b-36ff-b9c9-77111d3ca490 | -10.876 | -53.7614 | 2025-10-01 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| f4475548-1520-319b-b36c-f27e232ddcfd | -6.3 | -45.0205 | 2025-10-01 14:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 110.6 |
| d296a918-bf86-3ea4-b491-86d846c40f37 | -11.4021 | -45.0515 | 2025-10-01 14:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 69.8 |


[Clique aqui para ver as próximas entradas](README164.md)
