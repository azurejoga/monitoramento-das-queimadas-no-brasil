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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de155c3c-83a5-3d22-b8d7-feb78eda1b69 | -17.98997 | -57.59472 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 4fba0bae-1d69-3d9f-bfc1-07cf4efe274d | -17.95656 | -57.60617 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| abd2900f-5377-3515-885b-c002d35e8d4b | -17.99618 | -57.60514 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| ded4dfcb-4c6d-3272-aa10-635cefe6bb4d | -17.97065 | -57.59663 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 459a7196-7c12-3659-a2f4-5c020ae92b65 | -17.98478 | -57.54844 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| fae15f77-15a3-308d-91ad-5ff7b383a044 | -17.97127 | -57.59196 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 699a1684-abd1-3b0e-8687-475e485045f2 | -17.98916 | -57.54432 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| f142fcbd-e551-3658-aca0-beae090f3f07 | -17.96171 | -57.56931 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 4863f838-937b-3dab-93ba-aa86e5a4c4fd | -17.85134 | -57.64111 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 273b464a-3263-3387-a39c-9fcbc6b18574 | -17.9669 | -57.59612 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 27f0fc44-d905-3186-b559-040934df50e4 | -17.93723 | -57.60821 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| bd4594cf-7afc-3a83-b8a6-f40c61197aeb | -17.98421 | -57.55264 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9de2f0e9-6797-3991-8541-e6ac65c46a7b | -17.93348 | -57.60773 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 33c5017c-0a26-3dd0-a1c7-2e406e5988a9 | -17.99362 | -57.53956 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.3 |
| d3b899e1-52fa-31a2-98a6-d4a2345b1dd4 | -17.96727 | -57.55683 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.1 |
| f753fd26-14e3-36d1-829f-353f7ea2bb22 | -17.98853 | -57.54895 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| f725f693-3425-3877-a01f-3c055f9788f8 | -17.96159 | -57.59747 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 912683d8-0a20-3271-be17-f8d63f29a975 | -17.87295 | -57.63297 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 22ee3717-7663-3341-8f15-f837de90efa9 | -17.97064 | -57.56829 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 7e430fb9-db1c-32ca-9d15-9e24317c450c | -17.97048 | -57.54105 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| aaab88fa-1fda-3a8d-842a-a938eabe02d7 | -17.93095 | -57.59853 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 1b928a67-0fd2-3052-b4d8-4cd3ab66b961 | -18.0093 | -57.5928 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 531ba664-5f52-3830-89fb-7cc4c5c3e888 | -17.97376 | -57.60182 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3331a52c-fcdf-3891-a2a2-ea58a6de4dc9 | -17.96254 | -57.60022 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9870c659-68ec-3dad-9838-06675fa98a6c | -17.92911 | -57.61179 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 955990c3-f196-3e29-b071-409f582fa923 | -17.97233 | -57.57531 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c889a488-e75c-3e81-906b-348fcb65ecfd | -17.9725 | -57.61115 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 946575ef-56f1-3e80-a510-c741afc097dd | -17.9613 | -57.60951 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 04f4ac3d-9e83-30fa-b54b-8a3501bd348a | -17.97564 | -57.58789 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 919a9639-81b2-3c02-92f7-0e86af7e1060 | -17.88236 | -57.64751 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| cc8c0db0-eb98-3a1d-8cfd-17984113eac7 | -17.92098 | -57.61554 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 8e71c4bd-90e6-3ab2-bc0b-d3e8da06fce1 | -17.94535 | -57.60458 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6c2537d3-9c58-3896-96b9-68d5efb32944 | -21.7022 | -50.07761 | 2025-10-06 05:21:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 38b56c46-72c0-3c79-8b06-f4a74a69bb0a | -17.96674 | -57.54042 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| a5762517-c0bf-350e-9934-cd726dbb44fb | -17.94725 | -57.5909 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 844c534a-48e4-3484-9473-016328bc3c28 | -17.87926 | -57.58644 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 01e2e990-3488-302d-851b-c366ab90df89 | -17.97875 | -57.59308 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| be9809f8-54be-31bc-947f-039a1936bba0 | -17.87612 | -57.6376 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| cfb9c271-30bf-3e45-b0d6-2f1c787676d4 | -17.9799 | -57.55627 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2ca96230-59a7-3e47-9bd7-7cc3ff779cb8 | -17.96688 | -57.56786 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 2b150b98-5a26-3f99-9020-4b65a2ae5e16 | -17.98871 | -57.60403 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| d3b8729e-bebf-33e2-a95e-2af163552f40 | -17.9929 | -57.54486 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 36a414f2-11c6-3cee-8b81-b0a0a6b96b0a | -22.29135 | -49.91418 | 2025-10-06 05:21:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 90b1692b-d100-389c-8973-ddfe39c97836 | -17.85571 | -57.63699 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 57f5b4dd-4dce-3183-9846-02eb0b6f62b7 | -17.97538 | -57.55347 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9eece33e-5ea3-3a21-84f1-3607116cee26 | -17.96916 | -57.54329 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 036f3b18-fafe-368c-95e1-7dfa44e79330 | -17.98063 | -57.57914 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 3ea2be14-d49c-39f3-b388-29920a9fb5f6 | -18.0011 | -57.5408 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.1 |
| f4b82ca2-0bd2-3a83-b20d-ee116a724d47 | -17.97252 | -57.58268 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 4ee957d5-4914-3e55-949e-24716a005efe | -17.97187 | -57.61582 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 10d84112-31d1-30b5-9ff5-833465cd1a3c | -18.00055 | -57.60102 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 759f26af-941b-3173-a4e4-3bfb85c0a500 | -17.96244 | -57.53667 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 99ac2c63-8ba4-3ce5-a82c-8b79d5c5451f | -17.97626 | -57.58324 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| bb36337d-5a00-33b2-8058-71f298d4f322 | -17.9447 | -57.60926 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 6a99013c-7642-313f-a290-1554921a6649 | -17.98 | -57.58379 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 98cbb1f0-7cb4-3b1f-954e-5a2c3af42294 | -17.87179 | -57.58534 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.9 |
| 7dabaa36-3318-3af4-96a6-c6eb97a976e6 | -17.95129 | -57.53435 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 7032e08d-9617-3172-abfa-0af3b8d90cdb | -17.94909 | -57.60511 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a0f97b99-1d54-34e7-ade5-e2a8345c64b9 | -17.95038 | -57.59587 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 15620a81-29d8-3428-a7b4-4e547da8f50d | -17.95872 | -57.53589 | 2025-10-06 05:21:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| f4a8df01-82e6-3468-9a4f-df0bcdb320a9 | -10.71995 | -69.09297 | 2025-10-06 06:08:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94e634d5-4afa-361e-be04-aeef1d0931e4 | -10.80318 | -69.03789 | 2025-10-06 06:08:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11ee0d86-4919-3909-8c53-f52eb3ee024d | -8.69972 | -70.03067 | 2025-10-06 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e2432220-f7e9-3565-9304-e21a0a8f17e2 | -10.64587 | -68.74522 | 2025-10-06 06:08:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ab70901-ce40-38f3-b6b0-74596223023e | -10.71576 | -68.60471 | 2025-10-06 06:08:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dffbdac9-8be0-3b98-a7e9-598421b0a7da | -9.30413 | -68.30406 | 2025-10-06 06:08:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5cf4560-09e7-3856-aa97-c6a4f6d2edcd | -8.32368 | -70.19749 | 2025-10-06 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37f43159-22a0-3653-9740-419a4f4c0983 | -9.62974 | -67.52634 | 2025-10-06 06:08:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c746fa6d-38b0-35e0-aa6f-5c015f5f8825 | -7.83785 | -72.93048 | 2025-10-06 06:08:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0eeea056-51a8-3c00-a0aa-7353e51d68df | -7.59469 | -64.51345 | 2025-10-06 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4b941f29-7341-31fc-b958-f950efc6d1d8 | -9.59751 | -67.4787 | 2025-10-06 06:08:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40d91824-dde5-3347-a8b0-38279bbb0fbd | -10.895 | -68.21692 | 2025-10-06 06:08:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ded65ae-ea6d-38ba-a13b-9b94933c048e | -8.42874 | -70.10597 | 2025-10-06 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| afde50bb-ed49-37bb-8c59-18cb7b853c4c | -9.15917 | -67.85423 | 2025-10-06 06:08:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f03a4e8e-7a10-3244-a247-117cb8a7a6e0 | -10.38725 | -67.89839 | 2025-10-06 06:08:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 382848bf-ae1a-35d3-9c65-4910ce0ef39f | -8.32311 | -70.20122 | 2025-10-06 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44487b18-3ab4-386a-a5f3-3dd9bc1e44d9 | -10.93122 | -68.4484 | 2025-10-06 06:08:00 | NOAA-21 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e70cf0f-e874-320d-81fa-2733942211e8 | -7.69752 | -72.28667 | 2025-10-06 06:08:00 | NOAA-21 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83838d26-bd41-3882-96c4-7021488e7b83 | -8.44017 | -70.12307 | 2025-10-06 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9dd455d2-59b6-3b06-905a-4d69b4bda3b5 | -8.44759 | -70.12038 | 2025-10-06 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70d5b058-8e01-30a3-bd35-b86f51baa882 | -8.42305 | -70.12045 | 2025-10-06 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12366490-627e-341e-ac28-fe5d43beb366 | -8.44702 | -70.12413 | 2025-10-06 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69cd06e6-dc43-398a-8e08-df456bab0734 | -8.44416 | -70.11986 | 2025-10-06 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aba434cc-e64a-3668-ab51-0bfbbbd413b0 | -8.33676 | -70.36934 | 2025-10-06 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 802e3e06-4c79-389d-a3fb-344174932635 | -9.60948 | -67.48048 | 2025-10-06 06:08:00 | NOAA-21 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09435801-52b3-3735-a54f-db8c637f3813 | -8.42648 | -70.12097 | 2025-10-06 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fb0fced3-bc9f-3b8b-bb0f-c216f6b0be17 | -8.59637 | -70.04212 | 2025-10-06 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f490c019-3e00-3593-8bc3-82327cb99d97 | -8.77307 | -69.033 | 2025-10-06 06:08:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 853959b5-85b4-3e49-a55f-3b21a67cd3df | -8.70087 | -70.02308 | 2025-10-06 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33dbb079-56ae-32ec-8e7c-4e644ca6ee83 | -8.43675 | -70.12254 | 2025-10-06 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cafb6f0-9949-3ed3-b9c5-e580c2fc3499 | -8.69685 | -70.02634 | 2025-10-06 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0b6face-e9cc-3dd5-986e-d90de478e4ae | -10.10506 | -66.95074 | 2025-10-06 06:08:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1f5313d-16c5-32a7-9ee9-c4dd4ea39c78 | -8.56542 | -70.08376 | 2025-10-06 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3294b962-0ae7-341b-a90e-4aa84bc2f04d | -9.98857 | -67.57162 | 2025-10-06 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d45db5b-ab9f-3d0a-a29e-8acc7a342158 | -8.69628 | -70.03014 | 2025-10-06 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 706f87f9-ac0b-375a-9051-9445efdbac3e | -8.44359 | -70.1236 | 2025-10-06 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a00f9b8-cd45-359c-8235-b8be4fe69418 | -9.98807 | -67.57514 | 2025-10-06 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 989d378c-03e3-3e61-983e-980c4ccd8149 | -7.58925 | -64.51787 | 2025-10-06 06:08:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1ae4e508-456d-3c1f-a465-338d2232c0ca | -10.38575 | -67.96526 | 2025-10-06 06:08:00 | NOAA-21 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27364477-5d89-3c15-9290-c559a0a0eeb5 | -8.70029 | -70.02687 | 2025-10-06 06:08:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README77.md)
