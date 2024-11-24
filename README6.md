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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01e8646c-60e8-3721-b31d-10b75f0ada80 | -0.1944 | -51.646702 | 2024-11-24 00:25:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 14596f8e-a7ba-3476-92f5-22e39f7a4d2d | -1.0747 | -53.362301 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3879802-1d33-3960-948e-e258d5d744c3 | -3.7478 | -49.9986 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 87961085-f126-3a3e-be4f-8fe2a809210f | -2.865 | -45.824902 | 2024-11-24 00:25:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b9f60886-e0d8-3222-b189-1d182384f5c0 | -5.0011 | -42.951698 | 2024-11-24 00:25:00 | METOP-B | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 12b2d27d-3a30-361d-8d49-521fe6ad9d8d | -2.1532 | -50.603001 | 2024-11-24 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04bf0a39-0087-3035-967f-10146e25f275 | -4.2675 | -48.688499 | 2024-11-24 00:25:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce33243b-a73a-3ac1-a785-68e9cac8384d | -0.7485 | -51.729599 | 2024-11-24 00:25:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 91bd001f-b1b9-30e6-972c-6af197ad7340 | -3.6881 | -49.5942 | 2024-11-24 00:25:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b21f535-bdb5-307b-8950-b3f88edd8d0d | -0.8791 | -52.7668 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c5a1c87-472b-3747-93a9-31522413d6a0 | -0.3772 | -51.5439 | 2024-11-24 00:25:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| be2763d4-b016-3cce-9170-08bd1ce8110a | -1.2042 | -51.741199 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52e39e74-8697-3f18-93cb-5f2bf13dc04e | -2.6703 | -46.597198 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 154607b3-2b98-3609-99c2-41439fab1c76 | -1.2149 | -53.666599 | 2024-11-24 00:25:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2861837d-e436-31ac-95f5-c0096324e332 | -3.1333 | -45.377399 | 2024-11-24 00:25:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| be984a6a-3b97-3434-816d-86429c3e7b31 | -3.5394 | -50.770302 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8de7414-e39c-3fe7-ad1e-f05059dd6063 | -1.6145 | -52.560699 | 2024-11-24 00:25:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 550ae907-de50-3029-bb59-d276f37b4cfe | -1.304 | -51.7272 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 078bad7b-589f-3e28-a709-96a072c60765 | -2.5241 | -45.4156 | 2024-11-24 00:25:00 | METOP-B | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8a04dbfb-6b7a-3a3d-84a3-d1ab6fbef9c2 | -1.2567 | -51.745701 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f1acb4a-2fe9-30c0-9a1f-e2736fae9e56 | -4.412 | -44.089401 | 2024-11-24 00:25:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7260cae-6506-3341-b960-8195a809b1d7 | -2.6557 | -46.126499 | 2024-11-24 00:25:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b4c11f15-a167-3219-ab51-c37b70291730 | -1.7704 | -52.705502 | 2024-11-24 00:25:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fc34020-8721-33ab-8a8e-98544e0fd962 | -1.9517 | -49.5238 | 2024-11-24 00:25:00 | METOP-B | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 650f1707-51f4-3ce2-ad4e-318d38b61ee7 | -0.2515 | -51.626301 | 2024-11-24 00:25:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 312a9a6d-0d94-30ab-96a1-02cb374edcb0 | -1.2942 | -51.729401 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84d7cbf6-16d6-33a1-b4f1-a7a9d469597e | -2.7175 | -46.2621 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c3940d58-2fca-33f7-b815-7846d45273d9 | -3.8518 | -50.4179 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 537bcb0d-f98a-37bc-a327-1b8ab11ae090 | -2.0767 | -50.307999 | 2024-11-24 00:25:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a4d425a-dc55-3c99-a7da-20a20b094e02 | -2.5838 | -51.882198 | 2024-11-24 00:25:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e677778c-cbea-3b13-b625-682eaf798821 | -3.4907 | -49.908001 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e760eaae-f9eb-349a-9579-293947708b00 | -2.4534 | -53.694199 | 2024-11-24 00:25:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46ac4b6a-37ac-379e-b9dd-92dac7efc7fe | -3.1928 | -48.5835 | 2024-11-24 00:25:00 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6547235-5a88-3306-bcf3-6b7a324bc66d | -1.6047 | -52.562901 | 2024-11-24 00:25:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a1f0f292-3d85-3277-89f6-5d6399c8e1b4 | -1.5274 | -51.621899 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71b5c310-ed6d-3299-ae9f-d2e7177b1b3c | -3.2426 | -45.539501 | 2024-11-24 00:25:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e48ccfd7-8495-3610-8da0-fd61fc0dd866 | -1.1438 | -53.3955 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a0541e9-0ef7-3d4c-89b8-dfebb24ad3cb | -1.4658 | -51.118301 | 2024-11-24 00:25:00 | METOP-B | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a255454a-7c65-376d-95c2-558883ff1a63 | -0.029 | -49.634602 | 2024-11-24 00:25:00 | METOP-B | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fdc8ffa-54ef-390d-bddf-6b43164f2328 | -4.0605 | -48.318802 | 2024-11-24 00:25:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| deea6249-a125-3cbd-9869-f1e7cb49e7af | -1.2244 | -51.785198 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 184cf664-c5c4-3412-9f05-385f7535c80a | -4.5256 | -46.417 | 2024-11-24 00:25:00 | METOP-B | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 01e979a7-0dd5-3383-a910-0ba50312667a | 0.4176 | -50.8517 | 2024-11-24 00:25:00 | METOP-B | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 09e0ba1b-6142-3b29-808d-18d3ee6e2abe | -3.8543 | -46.005798 | 2024-11-24 00:25:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c793aa0b-e0f9-3a36-bccd-acbff0994a0e | -3.696 | -47.119202 | 2024-11-24 00:25:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88cb094e-017c-3eb2-9256-6d364145ba2e | -2.2004 | -50.675201 | 2024-11-24 00:25:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 75d5a2a9-5037-3db0-9f14-7074ae89688b | -1.0726 | -53.3531 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 15947d0c-f120-3419-90de-2a3e68587731 | -2.1803 | -54.4496 | 2024-11-24 00:25:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1278dbc6-e824-35e0-ab63-5fbe7d988e8c | -2.6459 | -46.1287 | 2024-11-24 00:25:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 97f6737c-3ecb-35b0-b8d2-a4fb84bcd303 | -2.5566 | -46.550499 | 2024-11-24 00:25:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee930238-db30-3326-8f70-f3ce624a1b56 | -0.8851 | -52.7477 | 2024-11-24 00:25:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 81e9dc31-8a20-3d9c-a831-f418a1f47523 | -3.8365 | -46.018002 | 2024-11-24 00:25:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 24169875-8d3f-3074-a5b5-425a7d25ddfe | -4.2417 | -48.6656 | 2024-11-24 00:25:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fafe959-b11f-3c8d-a4be-8b2c7dd0eda0 | -0.8362 | -52.530602 | 2024-11-24 00:25:00 | METOP-B | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 64e113ed-d90c-3af9-8566-8c4ec6749e40 | -3.7029 | -51.781898 | 2024-11-24 00:25:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 463d72fb-0699-3d8c-9558-46f231fcd789 | -3.0245 | -45.1278 | 2024-11-24 00:25:00 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6d744722-e4a6-3cc9-aa19-6debc1290d72 | -3.8329 | -46.0023 | 2024-11-24 00:25:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fca76849-9c86-361a-bf5c-16c5f6bcaa04 | -1.3074 | -51.742599 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f2f5ae7-13dd-34b9-8b6b-801e68c50c62 | -1.2319 | -51.7271 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4bfa2d8-46f7-36cf-9f02-1a51e71df186 | -0.282 | -51.487301 | 2024-11-24 00:25:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a67ad73a-7984-3b56-b8f5-c8aa3b5140c0 | -4.115 | -48.514702 | 2024-11-24 00:25:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31a664c5-cfd8-397d-b21a-977b43b622ad | -0.2499 | -51.618801 | 2024-11-24 00:25:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 3ad4c0bd-dc18-3788-851c-dc281af82aa5 | -2.6466 | -46.8554 | 2024-11-24 00:25:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6df3ff57-af99-34b5-bb31-219f65509361 | -2.956 | -45.143299 | 2024-11-24 00:25:00 | METOP-B | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cfa6df8f-8450-3f32-8c80-022b55389af3 | -1.0484 | -51.735401 | 2024-11-24 00:25:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| ce941dc8-ac4a-3e16-9a62-323b9de04737 | -2.5998 | -46.197399 | 2024-11-24 00:25:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6d88e76c-0308-385e-8f9d-f5d20c47f7c6 | -1.9404 | -49.5191 | 2024-11-24 00:25:00 | METOP-B | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed2984ad-4c52-301b-bfbe-9bfbe84d33cf | -1.2764 | -47.674599 | 2024-11-24 00:25:00 | METOP-B | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 33a506eb-1c5c-3aa4-86b6-c24a110a08d1 | -3.6083 | -47.5047 | 2024-11-24 00:25:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64e41978-1024-3df3-866f-e82d355d88f4 | -1.7871 | -53.653 | 2024-11-24 00:25:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b8bcf3b-cdf7-34d9-bbbe-2e88ad98c040 | -4.2494 | -48.699699 | 2024-11-24 00:25:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e735c84c-00ec-301d-8cb5-933147fa57b4 | -1.278 | -47.681702 | 2024-11-24 00:25:00 | METOP-B | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb9f1def-9760-3291-a171-69ec9efb9a8e | -1.2924 | -51.721802 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bc2aac3-6eaa-36e5-8f64-691cf90433a7 | -2.6825 | -46.1539 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8accf27b-aeb5-3228-bfd9-8b04ec0ca29f | -3.1001 | -45.7719 | 2024-11-24 00:25:00 | METOP-B | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 93c4ec9f-ff03-3d4b-90a3-c7e5717c089c | -2.159 | -50.445099 | 2024-11-24 00:25:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1d0bcc3-4433-3313-8c0a-bbf26692ec59 | -3.2917 | -49.8932 | 2024-11-24 00:25:00 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29916001-120d-31d7-861c-c5844e90b411 | -2.5949 | -44.9603 | 2024-11-24 00:25:00 | METOP-B | PERI MIRIM | MARANHÃO | Brasil | 2108405 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 02d1a030-07da-3898-8267-c54458e77fee | -4.1173 | -49.441299 | 2024-11-24 00:25:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6c25fc4c-e127-3817-9104-7aa4a82476a9 | -2.6961 | -46.258598 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b616f73e-d2c4-3270-aeaa-4dfd0e5bbb77 | -2.2415 | -49.209202 | 2024-11-24 00:25:00 | METOP-B | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 839c5d60-3311-304e-926b-123d2a78c8e3 | -2.1828 | -54.460701 | 2024-11-24 00:25:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5cd77245-a060-3d98-83fd-ab1bc1ffbf7a | -3.1294 | -45.360298 | 2024-11-24 00:25:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0cabb80d-6aa0-3573-ac5b-5c0bb5d8ac2c | -4.9984 | -42.940498 | 2024-11-24 00:25:00 | METOP-B | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 351e77b8-439d-31e7-bb7c-3895b1477f8d | -5.5437 | -45.327702 | 2024-11-24 00:25:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d5242377-bd98-369b-a514-ce441125335f | -0.9132 | -51.637699 | 2024-11-24 00:25:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13cc9263-d533-3589-8fe4-9b4ceeb52f43 | -2.8766 | -45.830898 | 2024-11-24 00:25:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c8d78d4a-b008-38a8-8cf1-e62c768f36f4 | -4.6405 | -48.835201 | 2024-11-24 00:25:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc76ed16-0100-3271-875c-d17cf5084564 | -2.5802 | -51.866199 | 2024-11-24 00:25:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10580dd2-ec1f-3cdf-b824-63c7e5d03a3f | -1.6085 | -52.5798 | 2024-11-24 00:25:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af2998fa-e289-3ecb-9a93-948358a71315 | -4.852 | -50.797199 | 2024-11-24 00:25:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68cb282c-0ad2-3de2-bd2e-ad24ae696540 | -3.3979 | -50.321499 | 2024-11-24 00:25:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 163b1424-c1c1-368f-abea-eef3f91b1e8d | -4.1085 | -49.494099 | 2024-11-24 00:25:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 598522e4-9aff-3a30-80ea-eebd022434ee | -2.7028 | -46.107498 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 664bc507-171d-35d5-97a0-e91fc25d7cc7 | -2.7193 | -46.269901 | 2024-11-24 00:25:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5cc2f4ba-4e35-3c25-8110-d104300ac9e0 | -4.4216 | -47.682098 | 2024-11-24 00:25:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ce15073-1065-328e-a6a8-ba0af984d26a | -3.2706 | -53.817501 | 2024-11-24 00:25:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1012b18-8e35-36cb-a559-c78572540a6c | -4.4104 | -49.6465 | 2024-11-24 00:25:00 | METOP-B | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| be091bea-0831-3dd7-946f-c77592560a65 | -3.9523 | -45.983601 | 2024-11-24 00:25:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3a42a289-1480-3a8d-b047-e530e3ac0ad0 | -4.5299 | -42.9179 | 2024-11-24 00:25:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README7.md)
