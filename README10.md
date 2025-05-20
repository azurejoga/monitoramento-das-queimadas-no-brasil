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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5585a88d-039e-36a4-85e3-732ea9b2c722 | -10.27527 | -59.53699 | 2025-05-20 04:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9946a929-3501-303d-9203-6d16a1ab2d56 | -11.82376 | -57.81892 | 2025-05-20 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc0ede29-9389-3458-9647-ade4896a5baa | -12.13294 | -54.66506 | 2025-05-20 04:59:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05cf2302-1542-3a5a-a604-08edba25e73d | -11.36535 | -55.11798 | 2025-05-20 04:59:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2df690a-1ada-3ebe-9c1f-92742198ec44 | -13.02844 | -45.07596 | 2025-05-20 04:59:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 568c4e23-dc4d-3126-8fbe-a71514720362 | -10.81864 | -56.95892 | 2025-05-20 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d018bd9d-71a1-3609-96c0-f89d968ffd29 | -11.51885 | -48.57993 | 2025-05-20 04:59:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b534fc82-5f47-36da-be5d-c1fa875dc583 | -10.66992 | -57.63538 | 2025-05-20 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ddfa5cfa-4a23-3249-93de-d3b0857ffecb | -11.08742 | -54.77731 | 2025-05-20 04:59:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f17a57f6-beb8-3b2a-b9ee-9701af492b6b | -10.34603 | -51.68369 | 2025-05-20 04:59:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 01da723a-177e-39c7-91d8-b32fd78b4d33 | -10.76441 | -57.232 | 2025-05-20 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ba3763f8-8136-3494-a538-50e598fa3f6a | -6.95712 | -55.27977 | 2025-05-20 04:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 132450f4-bafd-3333-8d28-ba46d0d04f9a | -6.96047 | -55.28031 | 2025-05-20 04:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 52ca901e-4de0-3595-bd6f-7d443b44478a | -11.08463 | -54.77322 | 2025-05-20 04:59:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9826de7b-c380-3222-ae6d-2363b0fe722b | -11.6939 | -47.7888 | 2025-05-20 04:59:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7bccbb38-9d95-3602-8ca4-82282a18fb82 | -11.15362 | -56.79008 | 2025-05-20 04:59:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dbd4a635-baf5-3a6d-8f58-eff9194c137e | -11.6673 | -54.94199 | 2025-05-20 04:59:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20af212a-41cb-3824-a539-c3346fd96ce3 | -13.03482 | -45.07241 | 2025-05-20 04:59:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85e7bee2-6f19-3ec4-af4b-5ab2a55581f0 | -11.34926 | -55.11177 | 2025-05-20 04:59:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c4a1cee-6364-3762-8414-9725476817f3 | -11.29753 | -53.97892 | 2025-05-20 04:59:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02981e2f-37f3-3b91-ae18-b8678c8e22cd | -13.02892 | -45.07167 | 2025-05-20 04:59:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 50f0f14e-9eb8-304b-95a4-c2ad87e45d17 | -10.60668 | -46.97836 | 2025-05-20 04:59:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6973baea-6798-37c6-bb92-6d093e99b1a6 | -8.33519 | -55.09637 | 2025-05-20 04:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 47cb9b63-9e2a-302c-8ba0-a53d864c6ec6 | -11.8861 | -56.41566 | 2025-05-20 04:59:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| febee5a4-6136-3e81-a154-2688293e0402 | -10.50017 | -58.86291 | 2025-05-20 04:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2bba8fe1-6e1b-37ca-b79f-9a671291a799 | -10.05241 | -65.00018 | 2025-05-20 04:59:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 027686f1-da71-3a7c-92f8-d0205dcccb51 | -11.67008 | -54.94606 | 2025-05-20 04:59:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f532ded-c41a-38d5-a86b-9df8b885d36b | -12.42787 | -43.72499 | 2025-05-20 04:59:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32e0b485-7ed5-3bae-8347-d5870b5d2394 | -13.0238 | -45.07785 | 2025-05-20 04:59:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 876abec9-2037-3e92-a177-bdba86e7aba4 | -12.13015 | -54.66093 | 2025-05-20 04:59:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20b3840a-f1c9-3a0b-a643-eb1193a3c91b | -8.75058 | -49.75483 | 2025-05-20 04:59:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8508a739-40ed-3571-9a1e-f8db51eae647 | -12.06909 | -47.32304 | 2025-05-20 04:59:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c50dae4-d273-3afe-b2b9-5d4932623adc | -11.5137 | -48.58385 | 2025-05-20 04:59:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05ca78e9-4f0b-3b06-995f-eb116eb5fbaf | -11.51429 | -48.57925 | 2025-05-20 04:59:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ade05fa2-fa8f-3403-a918-da265881de53 | -12.30114 | -52.47606 | 2025-05-20 04:59:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 06ab3cfe-f517-3029-b72d-5592a1675c4d | -12.04179 | -54.96512 | 2025-05-20 04:59:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a05fdf29-5adb-3d3b-b392-8e467a390fef | -11.56662 | -54.56515 | 2025-05-20 04:59:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5e4dd02-79a8-37a2-850a-a7396b73da98 | -10.3583 | -47.97572 | 2025-05-20 04:59:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ffd1681e-58cd-3e45-acca-feeedc8c99b4 | -9.41593 | -58.32854 | 2025-05-20 04:59:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8e466be-ebf4-3ea9-844d-1865b9a7c298 | -9.19735 | -45.33925 | 2025-05-20 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45f28117-0697-3ace-bf69-aeb6dc2fda40 | -10.27157 | -59.5395 | 2025-05-20 04:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f3d2a8e-1271-35eb-9d99-77276fc4ba36 | -12.34538 | -49.97657 | 2025-05-20 04:59:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23f1758a-7223-3501-b69d-4bde72f0024c | -12.1363 | -54.6656 | 2025-05-20 04:59:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d47f0f29-da62-3cfb-8459-712862a111c5 | -9.41666 | -58.32423 | 2025-05-20 04:59:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d7ce5e9d-30b7-3dc3-9d7a-eab4627ce515 | -11.29414 | -53.97837 | 2025-05-20 04:59:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3846f196-067b-3b70-940b-b0eba99fd431 | -9.04844 | -49.51911 | 2025-05-20 04:59:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1338082e-eff1-30aa-9bae-63f9288a7f33 | -10.59737 | -46.9713 | 2025-05-20 04:59:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6850e75-2393-3cd9-ac0d-e257b2970b15 | -12.29089 | -52.47016 | 2025-05-20 04:59:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 94e772cc-7243-3940-a8f6-8ff0f0c6fe3d | -10.8267 | -56.9526 | 2025-05-20 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6538a266-0786-3008-9e28-1f7f337c3e2c | -8.74705 | -49.75068 | 2025-05-20 04:59:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2f50501a-ac56-31ba-a7d3-8b9ab68f815d | -13.31798 | -45.37098 | 2025-05-20 04:59:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 716fb68a-59e4-39bb-ab27-f5617d5efa2b | -11.0813 | -54.77269 | 2025-05-20 04:59:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e8fd231b-1a3b-304b-8cf0-5a33ae849776 | -10.66346 | -49.44482 | 2025-05-20 04:59:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffd62c2a-853f-305c-ad7b-a927fd1c9bff | -12.40967 | -54.41549 | 2025-05-20 04:59:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9913ea4-8ae0-3249-bcf3-a2ceb7304d99 | -11.18334 | -54.40235 | 2025-05-20 04:59:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3efa7b9f-a079-3ed3-8000-f2a1c16bcfd6 | -10.60166 | -46.97765 | 2025-05-20 04:59:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 834b0460-ea32-3b22-a2e9-dbe600770002 | -12.03845 | -54.96458 | 2025-05-20 04:59:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8f35f62-2f11-36b9-989d-ae3fd6a67227 | -11.51809 | -48.5825 | 2025-05-20 04:59:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 70785ca6-4548-3991-ad5e-369373657e40 | -12.29451 | -52.47073 | 2025-05-20 04:59:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5c109a82-fe54-3d2a-a643-4710449d7dd6 | -10.07846 | -55.49179 | 2025-05-20 04:59:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 26d2689c-31e3-38fe-9d70-6ef4e3398aa4 | -11.08797 | -54.77376 | 2025-05-20 04:59:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f8f1e8b9-ffb5-3eae-8adf-7153f7aeb7c7 | -12.30175 | -52.47184 | 2025-05-20 04:59:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8b9cdcae-6806-368b-b3b4-31ca8e2121e8 | -12.08364 | -54.58354 | 2025-05-20 04:59:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 916a7ffd-8890-3a0b-8169-95adaa8ed2b7 | -9.03921 | -47.76427 | 2025-05-20 04:59:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e57c4bbe-2a6d-3328-a97a-480a9ac5b150 | -12.29813 | -52.47128 | 2025-05-20 04:59:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5dd5b373-3842-3a04-97a6-056f5ed27b6e | -11.34981 | -55.10825 | 2025-05-20 04:59:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e0b04e3c-af1b-3a35-95ba-da0f638cb384 | -11.36203 | -55.11744 | 2025-05-20 04:59:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f67d974a-cfd4-3806-8d6d-622b8a8ccb8d | -11.51354 | -48.58184 | 2025-05-20 04:59:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8410d8dc-057b-33a7-8190-5a8769230681 | -10.05168 | -65.00397 | 2025-05-20 04:59:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a4b590a4-82ed-3c19-bb5d-eb88ddd8f39b | -11.00821 | -50.75353 | 2025-05-20 04:59:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b599f07-6fc1-327a-a18d-d3e2e3dfdc41 | -10.82608 | -56.95631 | 2025-05-20 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ee2cdd9-e25c-3429-8b3f-92f9f3dbd145 | -12.02877 | -57.10402 | 2025-05-20 04:59:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60a31960-f96f-3572-8f7f-a5e3eea5a012 | -12.24824 | -51.44918 | 2025-05-20 04:59:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 35c6fd37-103e-306f-a11a-8027b4b4facc | -11.36147 | -55.12097 | 2025-05-20 04:59:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40bb6251-c180-3e60-a0e3-4c81be07a181 | -12.12959 | -54.66453 | 2025-05-20 04:59:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 067f0bdd-ef59-3078-b1d4-44129d764ed9 | -10.27139 | -59.53632 | 2025-05-20 04:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea27222f-7f2d-3111-95db-b0be71de5221 | -11.08074 | -54.77623 | 2025-05-20 04:59:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 359eed9e-7201-3241-a196-146c4971e774 | -13.02483 | -45.06928 | 2025-05-20 04:59:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8a2ffa9c-e19d-3272-9d76-eeef966d846f | -12.83542 | -47.40304 | 2025-05-20 04:59:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3463ba34-f4f2-33d7-bb93-5f8789b2deb7 | -10.75813 | -57.22706 | 2025-05-20 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f88596b6-3bb2-303b-a394-0b488c76b9ff | -12.28666 | -52.47383 | 2025-05-20 04:59:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| a3eaf6e4-333d-3d77-ba71-d76a500d0a40 | -12.40845 | -54.41571 | 2025-05-20 04:59:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 68d91061-e21b-3058-ab4d-037729ae8d7f | -10.61095 | -46.9848 | 2025-05-20 04:59:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a50e9d4c-b39d-304b-819a-528d367505c4 | -11.00807 | -50.7569 | 2025-05-20 04:59:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d7f7ad7f-2b53-364a-bce6-25ea9e3c39c7 | -13.0302 | -45.07431 | 2025-05-20 04:59:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 55ceb8ac-5e8d-334d-8e58-b9f3c756308a | -13.03125 | -45.06562 | 2025-05-20 04:59:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ee23961-c365-3fc4-ae1d-510efd9691d3 | -12.43424 | -43.72569 | 2025-05-20 04:59:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0439afe3-08a9-377d-8652-c09f7ab834a5 | -12.98302 | -46.32359 | 2025-05-20 04:59:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c383ff65-044d-35c0-a645-3c46bfc8b3b9 | -12.29028 | -52.47439 | 2025-05-20 04:59:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| d35bdf95-937f-399c-a88d-16d6655f3488 | -11.41289 | -44.6997 | 2025-05-20 04:59:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a002d4f3-77f7-3480-9f25-43c07164ca55 | -10.81506 | -56.96284 | 2025-05-20 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0512268-4dd1-3aa6-9775-ad7b4b7c0bc0 | -11.15082 | -56.78585 | 2025-05-20 04:59:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 281c2420-ffb9-3409-af0d-6809667db051 | -10.81566 | -56.95912 | 2025-05-20 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 45af799e-e25d-3ed1-bceb-ee0f5e919cbe | -10.76158 | -57.22764 | 2025-05-20 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 505828b4-69ca-3b3b-b34f-219244523d82 | -9.41227 | -58.32789 | 2025-05-20 04:59:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0a77d8e-1ecb-3da2-81e9-3a8eb5376071 | -10.75895 | -54.77921 | 2025-05-20 04:59:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac30d106-8922-32bf-a290-51eb500893a4 | -12.29752 | -52.47551 | 2025-05-20 04:59:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1449fa59-40b1-3a78-8490-e5e67e701f14 | -10.76895 | -54.78082 | 2025-05-20 04:59:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05c5f2a0-1e46-32e0-8d2e-2d354574833a | -10.50153 | -58.86088 | 2025-05-20 04:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6caf0541-a411-3853-87b1-454b8ee76d93 | -11.23681 | -49.49168 | 2025-05-20 04:59:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README11.md)
