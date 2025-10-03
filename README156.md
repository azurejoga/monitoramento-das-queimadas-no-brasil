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

## Dados Diários - Página 156

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e06a07aa-4355-3a28-8e9c-459583517ffa | -9.062 | -46.6565 | 2025-10-03 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.2 |
| e512e238-707a-32ca-ab00-db52fafaa268 | -14.6729 | -48.2485 | 2025-10-03 14:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 12532f2c-6aa6-3202-bf39-4038deba502a | -8.8729 | -46.6985 | 2025-10-03 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 191.2 |
| 861a3013-c60c-36ba-af25-15c0055f4161 | -9.8772 | -47.8103 | 2025-10-03 14:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 82b296c6-2495-393b-adef-2f0584958f81 | -6.0809 | -42.4881 | 2025-10-03 14:40:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 179.8 |
| ce99c3f2-59ce-3775-bcfd-f93da7729168 | -9.6452 | -48.2084 | 2025-10-03 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| e1bbc788-7e04-350f-a35b-46a52c1bdc5b | -10.019 | -48.4964 | 2025-10-03 14:40:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| ee7f322e-40f6-3a76-999a-d4d5a9177d3f | -5.7323 | -43.6409 | 2025-10-03 14:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| b73dc04d-a2e4-3e0c-b979-76e904e84f8b | -16.0408 | -50.9395 | 2025-10-03 14:40:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 2e95ab71-d367-3ae8-9bcb-0f82a3448c9d | -6.0621 | -42.4897 | 2025-10-03 14:40:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 136.8 |
| 7faca31b-59db-3120-b006-f38cc2216502 | -6.3673 | -43.8916 | 2025-10-03 14:40:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 0de7b490-5f1f-34ed-bfc9-a8ebc5e3c83c | -12.1215 | -43.4453 | 2025-10-03 14:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 77fecfaf-6633-3711-a70f-2288262fbd29 | -15.2236 | -47.956 | 2025-10-03 14:40:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 7a670f53-dbd0-3a2a-bbf4-90cc1108ead0 | -14.2316 | -46.1024 | 2025-10-03 14:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 25a47109-138d-390a-b307-29361e6fe075 | -7.7941 | -42.5369 | 2025-10-03 14:40:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 159.6 |
| ba8931a9-f0d1-3c69-95d0-5959d5f2ee73 | -9.355 | -45.9284 | 2025-10-03 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| bd9e757a-e676-3859-9ce5-1fe9e038f542 | -11.5687 | -47.6526 | 2025-10-03 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 53566a2a-4833-31df-bf76-a1d3be89f79d | -6.3788 | -44.6268 | 2025-10-03 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 93521b87-08db-3825-9501-2fdf8b49fdc3 | -14.7345 | -48.082 | 2025-10-03 14:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 19016f31-1884-3b46-ace3-14a8120925c8 | -5.2708 | -42.8578 | 2025-10-03 14:40:00 | GOES-19 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 841e6433-1749-331d-854d-6db2438e8ba7 | -8.1888 | -44.1588 | 2025-10-03 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 367dbf30-e9fd-39ba-9422-de8f121c13c3 | -14.8063 | -51.424 | 2025-10-03 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.8 |
| bbfd3327-c232-3fba-aca7-2b7cc8c77ffb | -14.8651 | -48.3515 | 2025-10-03 14:40:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 155.6 |
| ae5c77df-5b92-38e8-9c0f-e4efdb2eac30 | -9.3357 | -45.9532 | 2025-10-03 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 28142b79-13e1-3fee-8819-841fbd31c8df | -8.1702 | -44.1377 | 2025-10-03 14:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 147.4 |
| b061ce8a-ac1c-397c-91ed-7a90c1b036e6 | -11.1275 | -47.8634 | 2025-10-03 14:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 1378202c-31ce-3a49-a4be-1feb5b062089 | -6.0806 | -42.5118 | 2025-10-03 14:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 247.2 |
| 39fe74c7-32e3-305e-bc06-62979d03fd2e | -9.3749 | -45.8584 | 2025-10-03 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 30e0e0bd-a2af-3fb4-86ef-5c6bc6ee7b7a | -8.9948 | -47.4845 | 2025-10-03 14:40:00 | GOES-19 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| a6e70e97-203a-3782-be65-bbe3790821ce | -10.1467 | -50.2525 | 2025-10-03 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 4ba6422d-ed69-3ca0-95bf-b19ed120a037 | -14.0042 | -44.9142 | 2025-10-03 14:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 51b117be-0cf5-3f95-b9e1-aee9ce4bea8b | -7.646 | -45.4489 | 2025-10-03 14:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 24a65a81-39e9-3f82-a611-d3369b7ee292 | -13.1156 | -47.8625 | 2025-10-03 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 249f6ce8-35ab-3d4b-874c-92cfb06777f2 | -13.1546 | -47.8345 | 2025-10-03 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.7 |
| addb7a38-e97e-38d4-af39-2348a6ae1f1c | -13.7865 | -51.2618 | 2025-10-03 14:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 4b073a65-ad68-3cf1-82e7-6fb5c41c4367 | -16.023 | -50.8553 | 2025-10-03 14:40:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 139.9 |
| adbc3b91-410b-33b9-9565-373fccb43f8f | -6.3587 | -44.7654 | 2025-10-03 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 157.1 |
| e8f66e36-3dbd-3d14-aca4-b06acb81b4d6 | -11.8818 | -44.9815 | 2025-10-03 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 44ebb153-d156-362c-8d30-98c5702995f6 | -10.1839 | -50.2914 | 2025-10-03 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 899f0c70-ecd7-31e2-9190-1aff3aadc8a2 | -8.6911 | -47.6906 | 2025-10-03 14:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 69028e48-79c4-3e03-ab6b-2c50f1b68481 | -11.1252 | -43.3874 | 2025-10-03 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 204.8 |
| 5070189f-6556-3752-814b-5a99069354fb | -12.6131 | -46.9725 | 2025-10-03 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 160.3 |
| 5e112f41-1084-3672-a41c-459a62dd87b4 | -9.9585 | -43.5752 | 2025-10-03 14:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 106.0 |
| fdcde695-81a0-3b5c-aa8c-49092c4a11f5 | -11.4792 | -45.0174 | 2025-10-03 14:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 5fe0037a-544c-3a4f-a7dd-ef832a136a7a | -7.8692 | -47.3048 | 2025-10-03 14:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 59960e95-ac7c-369b-8c24-233fd4b81d8c | -11.5496 | -47.6551 | 2025-10-03 14:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| f2225479-a232-36a9-baa2-677626ad762d | -10.1095 | -50.2135 | 2025-10-03 14:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 0c3d6e27-61e6-3a9c-ad5e-cec1ad0ca26d | -6.6978 | -42.8118 | 2025-10-03 14:40:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 89.8 |
| 44cd4f13-ad4a-3a61-99fe-e8602e48acc0 | -13.1936 | -47.8065 | 2025-10-03 14:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 61b181bf-f9c0-3f96-a641-ffbb1302733e | -11.1379 | -47.1959 | 2025-10-03 14:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 5d578f98-578f-38e5-ac00-119f1d7bd2b8 | -8.8543 | -46.6781 | 2025-10-03 14:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 161.3 |
| 4f2a6af2-d32e-35ee-9c0a-a7c4a2de4676 | -11.9085 | -46.7349 | 2025-10-03 14:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| a2fabf6e-c54d-318b-8396-f3070d316fa3 | -14.0037 | -44.9376 | 2025-10-03 14:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 231.3 |
| 32e9c23e-e17c-3515-9bd2-62da863a4f37 | -16.7717 | -43.9601 | 2025-10-03 14:40:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 109.8 |


