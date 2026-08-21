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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7acf0e1-790d-35ae-a77a-ba651ba77b87 | -11.1747 | -54.0216 | 2026-08-21 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 225.2 |
| 33bf23be-a7dd-3e7f-a3d8-aa2bbbf26f0f | -3.5406 | -48.1889 | 2026-08-21 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 124.5 |
| ca1544c3-9d5c-394a-bdb3-9e932aa60b04 | -11.1561 | -54.0028 | 2026-08-21 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.8 |
| c11e02ef-5485-3f52-9dca-bf66defd2a03 | -6.2341 | -55.6109 | 2026-08-21 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 140.1 |
| 266360b5-828b-3f50-8d26-ff53a5921f18 | -6.1177 | -59.9069 | 2026-08-21 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| bd6b8bd7-ce97-3537-a185-0e3689f5df06 | -6.6938 | -58.942 | 2026-08-21 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 140.7 |
| bbd31d2f-8357-30c7-bde4-651cd590257b | -11.1558 | -54.0233 | 2026-08-21 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 32cbe02e-b3aa-3d8c-a676-61742ed695bc | -7.3605 | -45.791 | 2026-08-21 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| efece013-640f-333f-b215-e328c0e8bde9 | -6.1361 | -59.9063 | 2026-08-21 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| c3b5c76e-eec6-3a9b-9cb5-e055764ca673 | -7.3788 | -45.8344 | 2026-08-21 02:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 20ebd8e6-9f3e-3ee9-bebf-560dacb489df | -12.7401 | -48.47 | 2026-08-21 02:00:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| 102f0ba2-876c-33f6-b7dc-acdf998ec534 | -11.175 | -54.001 | 2026-08-21 02:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 167.3 |
| 5d1f5645-fa5a-3c81-a1b1-2e31e7b7b081 | -11.175 | -54.001 | 2026-08-21 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 135.8 |
| a7d66f3d-1fc8-3a5f-9763-837bce1842a8 | -12.7401 | -48.47 | 2026-08-21 02:10:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| b9f7702c-4869-35d1-80b8-ca9606252885 | -19.7438 | -57.9633 | 2026-08-21 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.9 |
| ef363869-7e14-3f3d-98ae-b1d04150d2db | -9.4071 | -60.417 | 2026-08-21 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 408.5 |
| 2c5aa004-da92-33f0-9513-0681ee92f755 | -7.3415 | -45.8152 | 2026-08-21 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 166.9 |
| ee1e57f1-02c3-3207-86ee-2758f2d2532c | -7.36 | -45.8361 | 2026-08-21 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 701957c9-eb5f-3ec6-9fbb-cffaa77e15b2 | -9.4256 | -60.4353 | 2026-08-21 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 112a3c89-36f7-3bbe-ab02-0e8e7b010035 | -6.2156 | -55.6118 | 2026-08-21 02:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| f8ec6e57-23cf-3f54-991b-7acd06ca50c3 | -3.5406 | -48.1889 | 2026-08-21 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 145.7 |
| 41409128-c867-3a64-97e1-697463235715 | -4.0481 | -50.2984 | 2026-08-21 02:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| f59e2c7c-1428-3f91-8561-47e5cba1d932 | -8.3903 | -62.6963 | 2026-08-21 02:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 28f103d7-d51b-382a-8f6f-8f0ff67a0a3c | -6.1361 | -59.9063 | 2026-08-21 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 36.7 |
| d4863e2d-1510-3604-9e48-c7e601d4a3f8 | -7.3788 | -45.8344 | 2026-08-21 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| ed4cbd57-e348-3656-9907-3fbbaa57ff96 | -11.1747 | -54.0216 | 2026-08-21 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 221.4 |
| 5c803eb2-0cf4-323d-a4fd-158d1841769b | -7.3605 | -45.791 | 2026-08-21 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 120.5 |
| 26e12d1e-5250-3ca1-89ac-b85914e63de5 | -9.4069 | -60.4362 | 2026-08-21 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 258.6 |
| ecf2ed21-5330-3f5d-8efa-d92a83cf89c8 | -7.3791 | -45.8119 | 2026-08-21 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 271.1 |
| 3596a767-0b92-3861-9975-83380ed5887d | -11.1558 | -54.0233 | 2026-08-21 02:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 9d07d2f8-f6ea-3f05-b691-ce093676749c | -6.1177 | -59.9069 | 2026-08-21 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 65946dd8-1616-315b-8540-20859c9a5d5f | -3.5407 | -48.1673 | 2026-08-21 02:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| cbc64c11-1804-365b-81d1-46d81265c3fa | -7.3603 | -45.8136 | 2026-08-21 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 645.5 |
| 199f21bf-1002-30b9-84aa-722d893b4742 | -9.4257 | -60.416 | 2026-08-21 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 142.5 |
| cb3e3958-db9e-3a10-9a59-db904807c258 | -6.2341 | -55.6109 | 2026-08-21 02:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 175.3 |
| 0ce2af75-63df-38e1-8ace-26fed0467426 | -9.4072 | -60.3977 | 2026-08-21 02:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 1dcb42a4-129b-3041-8b8d-54f055c4189f | -7.34 | -45.85 | 2026-08-21 02:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 24a5d772-9286-38fe-b234-b7623df25450 | -13.36 | -54.36 | 2026-08-21 02:15:00 | MSG-03 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 221101f4-d3a8-3aba-9389-10e4ae1fe6d9 | -7.34 | -45.8 | 2026-08-21 02:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 01d748d8-7faa-39b3-b136-e12434e3d90b | -7.37 | -45.8 | 2026-08-21 02:15:00 | MSG-03 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2e4a7aa6-51c0-3162-81ee-3ba6db94f041 | -13.39 | -54.44 | 2026-08-21 02:15:00 | MSG-03 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e3bc6460-c63a-37ba-a4a7-953fce11765b | -13.39 | -54.38 | 2026-08-21 02:15:00 | MSG-03 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a6cc1da0-3e69-332c-a1b2-dd90dd11e2f1 | -6.2341 | -55.6109 | 2026-08-21 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 91.2 |
| e1ccfe3f-1eb0-3a9a-8a48-c13990e0c64f | -13.412 | -54.3531 | 2026-08-21 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| e86930b3-78b3-3828-b250-5fe128c24ec4 | -13.3926 | -54.3758 | 2026-08-21 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 502.0 |
| 0ceaff5b-a783-324f-ab7e-88588ffdf192 | -11.175 | -54.001 | 2026-08-21 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 131.8 |
| 0bb27479-d8f0-34aa-8d54-0355c526d527 | -13.3734 | -54.3779 | 2026-08-21 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 133.5 |
| 147c26b4-6d19-35ef-a163-51689de167a1 | -11.1561 | -54.0028 | 2026-08-21 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 5892b920-611a-3de5-9272-1f864f38f775 | -3.5406 | -48.1889 | 2026-08-21 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 5d4e50aa-4572-3a11-ba1b-c5387d5fda79 | -13.3923 | -54.3965 | 2026-08-21 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 131.1 |
| 04f25773-db6e-3b18-83f9-c2b928afec18 | -6.2155 | -55.6316 | 2026-08-21 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 8573fdb3-5770-3a59-af34-7f468b9f463a | -11.1558 | -54.0233 | 2026-08-21 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 119.9 |
| 545ec36d-e626-3ad7-85b3-55675ef6ead3 | -6.1177 | -59.9069 | 2026-08-21 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| ff60d5d1-a28c-36cd-aaac-20b30b15c25e | -11.1747 | -54.0216 | 2026-08-21 02:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 170.2 |
| 7402b9fe-4b75-3242-88ed-08a49b4b063e | -3.5407 | -48.1673 | 2026-08-21 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| b1afefe0-0a3b-314c-bc08-4034492c45ef | -13.4117 | -54.3737 | 2026-08-21 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 138.1 |
| 66cf3742-fa40-3cda-9b75-ad7fddc7d5a7 | -6.2156 | -55.6118 | 2026-08-21 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 6bef9903-e466-3a3f-93b4-913e953cfa49 | -13.3929 | -54.3551 | 2026-08-21 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 182.1 |
| 61240fa7-a331-386f-936f-20ca1c8dbaee | -6.1361 | -59.9063 | 2026-08-21 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 6296a575-48ca-3f4c-a8c9-4371c87f9c4e | -4.0481 | -50.2984 | 2026-08-21 02:20:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 08aa3611-49c6-3272-84d5-e9a0d542c74e | -13.3929 | -54.3551 | 2026-08-21 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 139.3 |
| 26d4d8fa-8c1c-312c-a52c-8f62e8989ea8 | -6.2156 | -55.6118 | 2026-08-21 02:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| dfa27d1d-a814-3870-bf76-25da22da0e17 | -6.2341 | -55.6109 | 2026-08-21 02:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 98d2dcb0-a37a-324b-a57b-3d363e87b12d | -13.3737 | -54.3572 | 2026-08-21 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 77f5088f-fb1c-3d65-b77f-dd3a0997ad3e | -11.175 | -54.001 | 2026-08-21 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 105.1 |
| eb0e5688-b5f4-3dfa-b36c-c1071bfc5b44 | -4.0481 | -50.2984 | 2026-08-21 02:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| eff2a63f-e505-37b0-b9bf-9244fa0f634d | -13.3734 | -54.3779 | 2026-08-21 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 155.3 |
| 84dc587b-51c6-3106-a725-cce38f74a6e3 | -11.1561 | -54.0028 | 2026-08-21 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| e7568835-d19d-391e-be6b-2f21b4ee9421 | -11.1747 | -54.0216 | 2026-08-21 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 160.4 |
| 2867e3f6-fdbd-38e2-adbe-95bcface449c | -3.5407 | -48.1673 | 2026-08-21 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 8da2ef80-1ce0-3953-aa3f-05dfdd3780da | -3.5406 | -48.1889 | 2026-08-21 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 93.9 |
| d387fcb2-0fef-350b-a1cd-05fe841b00f6 | -6.1361 | -59.9063 | 2026-08-21 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| a13e3e84-acb4-3313-81a5-f024b088a3a7 | -13.3923 | -54.3965 | 2026-08-21 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 4379fbee-b805-3006-85fd-2a69f10c5476 | -7.7702 | -61.1634 | 2026-08-21 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 7418faa4-2fef-37a0-8365-2dd567c6b807 | -13.3926 | -54.3758 | 2026-08-21 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 338.4 |
| 95f9c8c2-6d01-347d-a05e-2ff67d14a44d | -6.1177 | -59.9069 | 2026-08-21 02:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| eb804100-c7d9-34ca-b145-6d608b32d19e | -13.4117 | -54.3737 | 2026-08-21 02:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 5dc92e35-0769-3e9d-af3c-a3c3ee83a1c9 | -6.2155 | -55.6316 | 2026-08-21 02:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 26367049-82f8-3764-9c90-113f83d67fde | -8.7353 | -63.9472 | 2026-08-21 02:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 47.3 |
| d3d69430-4858-36fc-bb59-6612be67d1d5 | -11.1558 | -54.0233 | 2026-08-21 02:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 117.5 |
| 9ccef768-8a29-3039-92bd-7670763bc462 | -6.1177 | -59.9069 | 2026-08-21 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| c15261ef-c995-34ba-aa6c-0f095b754455 | -3.5406 | -48.1889 | 2026-08-21 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 110.8 |
| 1a9288ad-fdea-34bd-b892-15aa93dde4bf | -6.2155 | -55.6316 | 2026-08-21 02:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 01167cc1-3987-3470-9e7d-a8529a4d2c3f | -11.175 | -54.001 | 2026-08-21 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 135.9 |
| cbe0021b-62f7-387e-a795-83a84cd9f1d2 | -6.6938 | -58.942 | 2026-08-21 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 448e37af-1d9f-3284-af79-9b465fb36dfc | -13.3923 | -54.3965 | 2026-08-21 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 4ae3dafc-2a91-3ebd-81c1-06f72b11d44f | -6.2341 | -55.6109 | 2026-08-21 02:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 131.2 |
| 9153ecf6-21e6-338f-96d5-feb2d0ac38c5 | -13.3929 | -54.3551 | 2026-08-21 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 3453ed95-9a73-3358-9bf6-e942071a93d3 | -11.1558 | -54.0233 | 2026-08-21 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 76646c60-6e26-34ed-9ba6-f0d327e0de70 | -9.4259 | -60.3967 | 2026-08-21 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.3 |
| dd37a82d-00ed-384a-ba4a-7db4f8b4572c | -11.1561 | -54.0028 | 2026-08-21 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| fde5bc47-cfe2-30be-b9bb-f9eef2474088 | -13.4117 | -54.3737 | 2026-08-21 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 96.3 |
| ded2934e-f817-3bcd-97d3-8fd9ee9a224e | -3.5407 | -48.1673 | 2026-08-21 02:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 4d4519b4-cf50-3e7d-821a-0652729ee68c | -6.1361 | -59.9063 | 2026-08-21 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 5ad7a9e7-5fdb-3bde-8992-ab28db12f9fc | -7.7702 | -61.1634 | 2026-08-21 02:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 8d189559-23a8-3e24-babc-6ed56d9e988b | -9.4072 | -60.3977 | 2026-08-21 02:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 84d4656c-e4b3-3654-bc23-c94814bbaf0d | -4.0481 | -50.2984 | 2026-08-21 02:40:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| b4d70665-0be1-3ae0-bec1-a88702f4247d | -11.1747 | -54.0216 | 2026-08-21 02:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 181.2 |
| f1eb5ce6-6aa0-3ec0-b802-dbeb16a79f2b | -6.2156 | -55.6118 | 2026-08-21 02:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| a5ec3b15-9baa-35a4-9c30-6e426896a5da | -13.3926 | -54.3758 | 2026-08-21 02:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 266.5 |


[Clique aqui para ver as próximas entradas](README19.md)
