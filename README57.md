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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b5f3cbd8-ca74-3a84-baba-1ad6a84d1733 | -7.86376 | -46.11008 | 2026-08-26 05:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b32c71a9-5b64-3795-b73b-8c060d756ad1 | -3.13153 | -61.18498 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6865004a-fa63-3893-a780-afca2c3990b0 | -9.02684 | -50.78672 | 2026-08-26 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42f62228-3c2b-3257-8c76-f242e9b331f1 | -7.00841 | -59.56718 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4397d25-09f8-3974-acbc-97afd46952b2 | -7.28301 | -45.35279 | 2026-08-26 05:27:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9a44c28-e6ec-3599-a647-e25e678c82c1 | -6.14565 | -59.9277 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 838a9795-e7fe-35d1-a78a-7f56ff697e67 | -3.20563 | -61.14597 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc054911-c026-3bd0-99e0-f0111cc562c5 | -6.14362 | -57.71017 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 187ebfdb-67b2-3e4b-bf11-adefe2bbc83f | -6.99171 | -59.26836 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d7af6da-2c48-3f9a-aacc-7ed928ba70fe | -6.644 | -58.51141 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7ac2a643-a289-3e80-a1b6-158ae907d322 | -6.25662 | -53.37918 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 87918867-fbd5-3c11-8c40-45b0aa4b3760 | -6.23096 | -55.4784 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0880eaf6-6466-3f6b-ac6b-df72033b833c | -6.64953 | -58.49795 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| c8e27543-4ca0-3496-a615-1945d8f75f34 | -6.89099 | -59.02851 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b1546402-a139-335e-9823-6ebf8db2d83d | -7.27788 | -59.62061 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dddf4449-2ad9-3dfb-90e0-35b2854a27ab | -6.99224 | -59.24355 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42b9e3be-e53c-37b1-a3cd-43e5c12669d6 | -8.15025 | -54.99 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7aa01ba3-3f35-3ddc-9da8-bfcbf6aa7551 | -6.62458 | -58.49057 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6beb82b0-77a7-38ea-aebb-a4837223b8e5 | -6.62513 | -58.48707 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bae7b352-18d4-3124-9ad9-2acaa4ef5d90 | -6.14678 | -59.92065 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c56ccfc9-b8c4-3d86-9b4d-857672aa6872 | -8.16682 | -54.95826 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 667ced04-f117-33d2-b15d-0ae355011179 | -2.98517 | -49.27239 | 2026-08-26 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 482a4a42-660a-3470-8fb6-c2d7db5d9b75 | -4.89144 | -56.27188 | 2026-08-26 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aac538a5-e243-31b5-9194-99396c20f06b | -6.42101 | -54.93179 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90585b30-598e-31e5-8c11-38604299ddf7 | -8.60841 | -54.73992 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91ed4417-16cc-3149-b010-36fc8fcaeef2 | -6.7877 | -59.63513 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8b54ad4-fe79-309d-96ae-7b10f5ba5a5b | -9.03557 | -50.80118 | 2026-08-26 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7368d481-1bdc-3f52-be8b-be0c20cad008 | -7.02267 | -59.24483 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 713f6645-3aee-3f4d-b38e-79269c876b8d | -8.77244 | -49.97169 | 2026-08-26 05:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae998b3a-b620-3099-8d01-d5d3524a6ac8 | -9.03515 | -50.80426 | 2026-08-26 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e547971c-b446-3922-b6dd-9e711cc7b29d | -6.4086 | -60.05608 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2253058f-6001-3087-8afe-1302818da412 | -3.13445 | -61.18959 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fda3b71b-cf53-3a6f-989a-b7483e530f93 | -6.44504 | -54.97112 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be2e50c9-0fe4-3866-9665-042dd6e53d2b | -6.6329 | -58.48114 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 206fad68-289e-353a-aa8a-4f46643e0b9f | -6.98672 | -59.2569 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e8d08d8-72f5-3bd5-b629-66d107bee60b | -6.16335 | -57.80485 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e671cc88-e3fb-387b-8865-c2b5783e0178 | -6.75072 | -56.33708 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fdb3a235-d116-3888-ae40-3a40f1ee91f6 | -7.36336 | -59.63402 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fbc6d9b2-262e-3ebf-bb94-3bef894778f4 | -6.74674 | -59.63923 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 331fd18b-54b9-3ad9-ad50-4ad6664d2b25 | -6.76669 | -59.47114 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 607beef5-1b5a-3455-b264-c77e37abb08b | -7.30403 | -49.541 | 2026-08-26 05:27:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fbc93db5-bc1b-36d8-bd88-523980c2cbd1 | -7.49195 | -55.36539 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 85889be8-4048-3922-a69c-172705d57fdd | -6.98949 | -59.2609 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5987f851-f2f5-3c98-ac71-f958ffac1215 | -6.63456 | -58.50634 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fdbc12de-60ed-3a9b-a57b-6d5495c26503 | -7.10591 | -56.56461 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8a914ee-afdf-34f4-b796-9808d5b363be | -8.61022 | -50.01492 | 2026-08-26 05:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| acfcb6cb-a05d-34d5-9492-d9d436780ba9 | -6.93073 | -58.94939 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73e48e07-a5f0-3ac3-abf9-a6f7485015e7 | -3.21501 | -61.15572 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f0e1a5e-b5b5-3bcd-86cc-e3c34edca313 | -6.74544 | -58.57794 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ede3331-ea9b-3186-941d-0409227a1cbd | -6.1659 | -53.49636 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 418eef33-afe6-35a3-a768-e6f2cf2d3498 | -6.83462 | -59.94026 | 2026-08-26 05:27:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| db4a904a-c9f2-3e47-b850-e0877078fa56 | -6.63182 | -58.50959 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 170af0d9-37b4-3f0b-a9c8-df47d358cc5f | -8.01805 | -51.79273 | 2026-08-26 05:27:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 908edd59-98a2-3b38-b528-ce0bd6a6a2c3 | -8.21584 | -55.00522 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0fef14ac-9af3-3226-b115-d257826a0dc8 | -7.0017 | -59.31265 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f2cfc38-1f30-3562-9cfc-fd49ee23377c | -6.63072 | -58.51657 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9bcd9039-368c-3168-985e-00620de2f37a | -7.45505 | -59.99613 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5c1b3c1-a154-34d6-af41-e521c5157b5b | -6.79307 | -59.81493 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d0fc71b-1754-3e4b-9fbc-2a2af68de033 | -6.62846 | -58.48761 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7ffc9bd7-6655-32ca-bc64-841e839523ea | -6.64008 | -58.49289 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8fb79f8-da62-337a-9845-1a0a89b59acb | -6.94145 | -52.79408 | 2026-08-26 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 266d9284-b757-37e1-b3a7-e18ef2778e1a | -6.15224 | -57.94155 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3f926f0-e8e6-343b-a901-169d670e6947 | -3.10292 | -61.22605 | 2026-08-26 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 19848802-4411-390b-a0aa-11a72dd4be66 | -7.52453 | -61.38464 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 34.9 |
| 6400c2cb-30ec-3c56-b2a9-4c5b105ced7e | -8.55965 | -54.83677 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 494f7b17-b607-3aa7-8204-a2819db84d95 | -8.64358 | -54.75056 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cbcbecfb-2dbf-37a6-8437-2f199287f49a | -4.92918 | -55.76853 | 2026-08-26 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 194ca837-de70-310c-b9ec-9b468ced6ebd | -8.21905 | -55.01049 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 21bd1d90-d4bf-3527-a21a-8e9dd1bd5c22 | -6.62739 | -58.51605 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ff90919-cf06-3203-806b-e1251c0fb308 | -6.99503 | -59.2689 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b1809ed-09f9-3593-9271-d27779e59654 | -7.47434 | -61.37716 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 747a54c9-7568-35cc-8c3f-f8f321e1e57d | -6.42175 | -54.94355 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 558d75cf-4cb7-3df7-b11d-fade976a3d33 | -6.18795 | -53.49176 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8b0b6935-b5b0-3154-a976-1bf2faa216f4 | -6.27213 | -53.36167 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06b7f997-3fa6-3994-b33f-cb40ae8ef1f6 | -8.54661 | -54.78732 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 97bd122c-876d-3a4c-840a-ab232c00df32 | -5.6544 | -46.95241 | 2026-08-26 05:27:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72a53701-8b39-36c1-aecc-96bc914f3ea5 | -6.7999 | -59.45506 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4868d2fa-b349-35a3-b093-31349941f1ed | -6.27156 | -53.36552 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 29412322-4382-3089-b297-e7cdd357d4b7 | -8.95329 | -50.7764 | 2026-08-26 05:27:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 88afdde1-8f1d-3c95-a731-e0ad26e61bbd | -8.57452 | -55.28032 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 478438d3-e94a-369b-a846-cbc995257014 | -6.63235 | -58.48463 | 2026-08-26 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69ea1672-8f63-30d9-87a7-203667ec2daf | -7.54546 | -61.36485 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7aff996b-a007-3912-95e3-1f8219e42291 | -6.69171 | -56.15878 | 2026-08-26 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| adf20e97-2aae-390c-9436-eceb030df5d3 | -8.07474 | -47.5028 | 2026-08-26 05:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e178aa6-6a90-3419-a803-41a75bf8568f | -2.98351 | -49.27201 | 2026-08-26 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f44a8da-3e95-3abe-9cd7-1091611eefa5 | -3.25402 | -52.23345 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6855fb74-bbbd-3520-8a7e-80c7ae20a227 | -6.27269 | -53.35781 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd9ff6bc-cd89-3f7c-87c8-c676fe94f20c | -9.02251 | -50.77922 | 2026-08-26 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d95fa8bb-f6ce-3879-ab07-2783c104a5b3 | -7.51239 | -55.58641 | 2026-08-26 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17e3b851-fcf1-3fe1-bdaa-ef58186ee208 | -6.27349 | -53.38174 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 88cd02e0-cfe2-3987-89f7-5167ce705740 | -8.61941 | -54.70826 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9aac8bc6-efa3-3c5d-8008-52d05431af77 | -7.5582 | -61.41737 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5a2ccf92-2db6-3d8a-9351-2120d12e96de | -6.15037 | -57.71123 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cfe43802-453f-3eac-95cd-74fca659e46a | -7.54669 | -61.35728 | 2026-08-26 05:27:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d734985d-faab-3237-b4ca-ba176840610a | -6.7235 | -59.44289 | 2026-08-26 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f17f14a7-69bf-3bbc-be54-9cf52e8f3277 | -6.09545 | -57.70308 | 2026-08-26 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| decc6cfc-9e71-39dd-960f-091665b68d85 | -8.11297 | -51.66277 | 2026-08-26 05:27:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 65086378-d421-3d50-865a-9d18b03d9074 | -7.25454 | -49.85517 | 2026-08-26 05:27:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7ab7deb1-3ec4-382b-925a-7043675bd4d1 | -6.93445 | -62.87873 | 2026-08-26 05:27:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 418b8f0b-adab-3b7b-8272-aa76db5c5cf9 | -6.27692 | -53.35842 | 2026-08-26 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README58.md)
