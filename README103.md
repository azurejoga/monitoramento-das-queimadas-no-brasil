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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2926e2b0-26b6-312f-a9de-47482ca4157e | 1.80011 | -55.72492 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29ddc8c8-e1d8-3da1-8e1b-c52e0842bf8d | 1.81165 | -55.7337 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f98a7485-a31d-3523-aca3-546178fd9f95 | -3.49477 | -51.6025 | 2025-10-17 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa9b1b52-d187-3ea6-9376-0f24ae42579d | -5.50878 | -43.874 | 2025-10-17 05:08:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e6a41999-b51d-38c2-b716-ade7bfce4674 | -2.74414 | -49.38337 | 2025-10-17 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 430e89ab-ca2d-364b-aa40-f200950ef467 | 1.73328 | -55.79525 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ccda1dd5-5d82-3edc-ac10-f0c62e9dbf72 | -3.29477 | -43.24252 | 2025-10-17 05:08:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ce2ff461-127c-3996-8e76-6dc982c78ce5 | -2.74753 | -49.39035 | 2025-10-17 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc7a6a34-09bd-3da7-a49d-d8f695fc2cb1 | -7.33722 | -43.86638 | 2025-10-17 05:08:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| c483439e-f0ae-3830-bda4-9379dcff5f25 | -3.49695 | -51.54994 | 2025-10-17 05:08:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6b1d05ad-3faa-36f5-a479-dc7b5a03f33e | -3.60033 | -58.31629 | 2025-10-17 05:08:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 754c4aa1-0fd4-3055-930b-20c84ea5f529 | 1.8335 | -55.69854 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0836adcb-6a7e-3605-82b0-5d0f2307a141 | 0.87192 | -51.12715 | 2025-10-17 05:08:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23d6b17f-b518-3f1d-9600-797865135d50 | -4.10598 | -48.02239 | 2025-10-17 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba18aedb-3379-3021-93b0-c530dc43faeb | -3.47402 | -49.92073 | 2025-10-17 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eaacbf6c-4f0d-3591-a403-6aaef233afa2 | -2.74267 | -49.39278 | 2025-10-17 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 304f88e5-e341-3cdc-b8a0-158243954399 | -3.50063 | -52.49337 | 2025-10-17 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dd7ece54-64af-3d60-bcfa-8ab59a1552ef | -5.28289 | -47.93184 | 2025-10-17 05:08:00 | NOAA-20 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f1b8a0d-75d7-392d-bfa9-05d6258e0cc6 | -2.94671 | -47.31113 | 2025-10-17 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f9f1406a-5086-3751-8343-c455a2f0be8a | -3.51649 | -52.49102 | 2025-10-17 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 06eb6d7b-e452-3ffa-a2f4-5983f2919e52 | 1.89202 | -55.85524 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b65c737e-604b-3031-9d19-06f23452d03c | -3.28816 | -52.59144 | 2025-10-17 05:08:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b5c6e1b-4669-3030-a22f-6d7c7225c75e | -2.8722 | -50.72632 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 327eab18-b972-3d5d-b477-6d1f848cf576 | -5.88526 | -43.89653 | 2025-10-17 05:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6a58a61-88af-321a-80aa-c8d0b3d434f6 | 1.8975 | -55.86851 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5b54579e-e779-31dc-8d19-e735cc34a672 | -7.32748 | -44.1552 | 2025-10-17 05:08:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 39360b35-ef51-3171-ab53-264e45639288 | -0.90257 | -47.54337 | 2025-10-17 05:08:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 23166d29-7ffa-363e-9c4f-0c0fa82fc66f | -4.53838 | -48.41227 | 2025-10-17 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eceb1c6b-0d7e-385a-bf0e-835390f0663e | -5.24416 | -50.95833 | 2025-10-17 05:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b053549e-24e1-32e0-a971-de88470f7c6a | -6.56232 | -48.0476 | 2025-10-17 05:08:00 | NOAA-20 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 60951ac0-baee-39df-ae66-db7b54df306a | -2.94978 | -47.31521 | 2025-10-17 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 762758dc-66e4-3fbb-aca4-4e0166914891 | 1.82575 | -55.71383 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5e439dec-7477-3ce6-adae-e265b44f0029 | 0.3269 | -51.36164 | 2025-10-17 05:08:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a3bc98c-252d-3adc-bc23-a685251f47af | -4.51557 | -50.41096 | 2025-10-17 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ffab6ce-4cd6-3180-904e-0621d0f89760 | 1.84456 | -55.68274 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e7700710-53f2-3b57-b559-f9fe6d169c5c | -3.84212 | -47.0673 | 2025-10-17 05:08:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd9c90d0-a087-31b0-8238-23b260f47734 | 1.83296 | -55.6951 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 198c25d8-db2b-3d5e-b34a-757936a6118c | 1.75432 | -55.75671 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 691d4289-2565-30a8-a91a-8faf5501c8ca | -2.69535 | -59.43116 | 2025-10-17 05:08:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d71b4f56-ffb1-3fd0-9138-ac0f27b3cddc | -2.8728 | -50.72248 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98bfdeb4-58d2-3edd-9d9f-3201bd5c3c78 | -5.24106 | -50.94955 | 2025-10-17 05:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9e72ed0-95a0-3a0c-86d0-51e224cdfc04 | -4.43646 | -50.55094 | 2025-10-17 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 924cb4e7-e02b-331c-b886-fec4d62a8994 | -5.58143 | -47.46038 | 2025-10-17 05:08:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bf2fdb28-3e33-354b-a7a1-9104bf2308fd | -5.10392 | -56.15545 | 2025-10-17 05:08:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8db9cf41-1ddf-3ed7-8d27-5fbf197d08d5 | -3.40612 | -52.50475 | 2025-10-17 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c0224c8-26bb-3ff1-9a35-288d856d1fef | -4.41148 | -48.95747 | 2025-10-17 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f15d197-d8ca-341a-b4b9-2ea81ade7a0b | -4.4051 | -43.41204 | 2025-10-17 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7693f93e-0c12-37cc-817d-fcac159d2d80 | -3.87603 | -51.9481 | 2025-10-17 05:08:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9a21b719-c237-3a0c-b617-0daf993aa6b9 | -2.7434 | -49.38813 | 2025-10-17 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c9c08554-9299-3c65-ad01-d7dfe73b9487 | 1.04627 | -51.20834 | 2025-10-17 05:08:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99f1db57-f27f-3af8-bde4-625cec388111 | -6.40038 | -46.8778 | 2025-10-17 05:08:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4204e208-6606-372b-99ab-d8d526ece520 | -4.93686 | -48.55451 | 2025-10-17 05:08:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3726ef9f-6689-36d9-b1ab-33d7de4cbda8 | -4.39212 | -43.40378 | 2025-10-17 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 578433e5-997e-3989-9d64-40c981675489 | -4.12308 | -50.71845 | 2025-10-17 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d15d5a44-d4b9-3cd1-aa70-bc889c851a49 | 1.73605 | -55.7913 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9ed2926-63c9-3077-8b06-98c45f4af78a | -4.11072 | -48.02597 | 2025-10-17 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e934daec-d3d4-3895-835a-8f0de89b5994 | -6.7422 | -44.37929 | 2025-10-17 05:08:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| fc143d76-16f0-3bf0-9ff2-6dfad9ac59ea | -6.58678 | -47.07128 | 2025-10-17 05:08:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 778166b7-b00e-3c05-919b-fd8a33a570af | -4.71842 | -46.45068 | 2025-10-17 05:08:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cac8e059-0414-3ead-86b0-6b32f7a9b8d0 | -2.74243 | -48.3091 | 2025-10-17 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c7f8c046-df0c-309f-b317-9c54aca08fe4 | -5.73786 | -49.13628 | 2025-10-17 05:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5108ff7-3ec4-3147-ad46-f9aa17740ba1 | -4.11114 | -48.02312 | 2025-10-17 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2a75c5b-5539-328f-975f-0ad55e6421a1 | -4.21829 | -48.36401 | 2025-10-17 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26c595c2-c7ff-30e1-8467-02c7d8b2ba40 | -3.60946 | -48.91842 | 2025-10-17 05:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a37c7e7c-055f-3905-b687-d0bc85960b36 | 1.82244 | -55.71435 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4bc293ba-d687-322f-ac8a-aa56a8d6ed0c | -5.84497 | -43.88337 | 2025-10-17 05:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1d24bd1b-33b8-3255-93b1-af594b8f031a | -3.44953 | -52.85343 | 2025-10-17 05:08:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9fd1e73-8309-3d20-9a3e-55e239a4e7f7 | 1.83627 | -55.69459 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce0e9f5b-dcee-3cce-aa26-b6ea30e89830 | -2.87038 | -50.73792 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0a8b1419-ff12-322f-b3f0-c75f9856581c | -3.6802 | -47.63801 | 2025-10-17 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b8a2c39-cfac-36f3-b106-1383a80088c1 | -4.41288 | -43.40035 | 2025-10-17 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 2fa9d620-3394-3a03-88ad-5ed78b05b987 | -2.96316 | -48.58824 | 2025-10-17 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02f2f855-cb29-3062-bf80-338b6b3e2ffe | -6.2058 | -44.43742 | 2025-10-17 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bb245054-93d9-3519-8f3f-a334f161f528 | -6.21652 | -44.4347 | 2025-10-17 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| df018936-e501-33ac-b84b-e0a7c044aa36 | -4.93645 | -48.55738 | 2025-10-17 05:08:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d66ac04d-4954-3716-9829-b680f62a1eda | 1.78918 | -55.91368 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69f81ca5-5f6b-319f-8fda-aff06d2e29dc | -5.25833 | -50.98099 | 2025-10-17 05:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 708894d1-c11c-32ca-a9bd-2b112eecfc20 | -5.99179 | -44.1527 | 2025-10-17 05:08:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a0617a67-6e3d-3398-a8ff-65b9c9f5a8ef | -2.8728 | -50.72559 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e559cde-55d8-3935-b07a-12038171f5f4 | -1.60464 | -55.72535 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a5a82fe-42e9-3ecf-b627-a1fc193dfce3 | 1.85561 | -55.66693 | 2025-10-17 05:08:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ed70075d-90a4-3647-bae5-2d7604e0420c | -3.20815 | -54.9632 | 2025-10-17 05:08:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06339e16-65b1-32d1-bce7-0900e8d12d57 | -3.82778 | -52.40272 | 2025-10-17 05:08:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3791722d-0083-399d-ad3e-918a84ddc44e | -7.07567 | -44.94702 | 2025-10-17 05:08:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 12b238ec-5e68-3c95-8da4-64e32b4b8fd2 | -6.55698 | -48.04679 | 2025-10-17 05:08:00 | NOAA-20 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2b2abf37-aff3-39e5-aee2-12d0e5f55ed5 | -1.51841 | -51.6254 | 2025-10-17 05:08:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e9388d9f-3bea-3356-b020-8f1ce1ab798c | -3.24461 | -45.9784 | 2025-10-17 05:08:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30c9a682-dd31-3e5a-8a29-395ea02f6409 | -4.39106 | -43.40412 | 2025-10-17 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 91ec3c82-66a8-3885-84be-9eb2f3c7065a | 1.89419 | -55.86903 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71c0718f-8de9-34c6-a1a2-a93d435fc034 | -5.99019 | -44.15213 | 2025-10-17 05:08:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7b36d080-2c25-38c8-a2af-86943e96c72f | -0.90212 | -47.54633 | 2025-10-17 05:08:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d059faef-0e23-356c-bcbb-15089f46756b | -3.9278 | -53.81316 | 2025-10-17 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e289a270-9c40-3a20-b4c0-7c3d778844c8 | -4.39015 | -43.41721 | 2025-10-17 05:08:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2034088c-f665-3018-a7b3-47bf8c31b69b | -6.21731 | -44.42863 | 2025-10-17 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 09013b11-2633-3aaf-8541-92ff53ec0085 | -1.67177 | -55.81687 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a935e786-2db8-3b42-bbe8-ad5b953f8b2d | 1.79401 | -55.966 | 2025-10-17 05:08:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4437c0d6-9fde-3d69-b188-ff7cdc907fde | -2.87585 | -50.73397 | 2025-10-17 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99312b23-5b17-3831-9316-e2a863b5def7 | -4.55412 | -50.60602 | 2025-10-17 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 942ab7ee-c082-3003-a3b0-76c4066c5036 | -5.87255 | -44.83916 | 2025-10-17 05:08:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c741506-1e1e-39ad-b164-a74d382a9663 | -5.88622 | -43.88966 | 2025-10-17 05:08:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |


[Clique aqui para ver as próximas entradas](README104.md)
