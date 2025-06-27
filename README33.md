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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 704c1a04-3e28-3353-a396-6cc401e72327 | -15.72346 | -43.61798 | 2025-06-27 12:49:00 | TERRA_M-T | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 3c744830-d209-3cf8-bef9-ec547f749534 | -14.24318 | -45.49523 | 2025-06-27 12:49:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 931d2ce6-273d-3b0f-85a0-80e09f4de89b | -14.97185 | -54.61465 | 2025-06-27 12:49:00 | TERRA_M-T | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 562c11a0-b1fc-3c85-bef7-07f5ae41a6ce | -14.2442 | -45.5002 | 2025-06-27 12:50:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 4e17909e-82e0-38b5-b951-629dca7e9847 | -11.5779 | -52.115 | 2025-06-27 12:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 05cb62fb-d4d0-3b27-822d-263c07a01621 | -8.5722 | -51.5761 | 2025-06-27 12:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| d2df27db-dea0-3aff-b4cb-9d11e37cb716 | -30.34758 | -52.49501 | 2025-06-27 12:51:00 | TERRA_M-T | PANTANO GRANDE | RIO GRANDE DO SUL | Brasil | 4313953 | 43 | 33 | nan | nan | nan | Pampa | 14.7 |
| cfb9f5ee-16a9-38a5-aef8-3fbe8522a431 | -8.5722 | -51.5761 | 2025-06-27 13:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 4241ead6-2627-300a-a747-9fe1d6ac353c | -14.2442 | -45.5002 | 2025-06-27 13:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 9c5a5cc5-e0c9-33e0-b442-04e2b8c68f49 | -11.5779 | -52.115 | 2025-06-27 13:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 2bed8391-6d9d-3068-a722-fd0b91edc095 | -7.7346 | -47.6025 | 2025-06-27 13:00:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 688c2731-4509-389b-a460-2c1f0a570525 | -11.5779 | -52.115 | 2025-06-27 13:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 84104134-f312-3689-9346-853e7abfe1bd | -14.2442 | -45.5002 | 2025-06-27 13:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 107.9 |
| ac151db7-8669-3097-8a2e-432568874ce5 | -8.5722 | -51.5761 | 2025-06-27 13:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| f24c494f-2e0e-34c8-a7de-5f352ab01296 | -14.2442 | -45.5002 | 2025-06-27 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 0028fa00-e5a4-325f-a484-cf5528816538 | -11.546 | -47.8772 | 2025-06-27 13:20:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 53010505-a7bd-3c46-9627-57caccf98a8a | -11.5779 | -52.115 | 2025-06-27 13:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 1ddd3888-82e8-34b1-b651-c9ad530dbaab | -8.5722 | -51.5761 | 2025-06-27 13:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 695a06b8-3004-36f9-b42e-b267e3c6b22f | -11.546 | -47.8772 | 2025-06-27 13:30:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 66135e7c-8c50-3be7-aa42-2563de4a1d87 | -10.6323 | -46.7001 | 2025-06-27 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| e4b9cb4f-804b-34d8-90ab-e5d15615759f | -14.2442 | -45.5002 | 2025-06-27 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 5b364b38-9685-3429-bee4-8de465864809 | -11.5779 | -52.115 | 2025-06-27 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 2c6c686d-8cf0-328a-8680-a65b4a0a4c09 | -11.4337 | -54.4689 | 2025-06-27 13:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 88078a1f-8ece-33b8-ad9f-1eecb73042cc | -10.6319 | -46.7226 | 2025-06-27 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 3d97524a-6994-3cb7-bb93-b5e7d377fab4 | -11.5779 | -52.115 | 2025-06-27 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 375353f9-40f8-33f7-82a9-ce9465ee893f | -11.4337 | -54.4689 | 2025-06-27 13:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 64209edc-59e4-3435-bcd9-336ec4fdc794 | -8.5724 | -51.5552 | 2025-06-27 13:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| c679fc6d-afbf-3167-b0bc-2eb51a733353 | -8.5722 | -51.5761 | 2025-06-27 13:40:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 79f9386d-3e16-3477-bef2-b52d193561ac | -11.546 | -47.8772 | 2025-06-27 13:40:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| b28ab4bb-28e1-3164-bf8e-5a6910bd96b0 | -14.2442 | -45.5002 | 2025-06-27 13:40:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 81e6026d-3cf2-351c-a16f-a2b6be806d4c | -10.6323 | -46.7001 | 2025-06-27 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 7a7e7e5a-00bc-3c07-9816-3c95839b84df | -11.546 | -47.8772 | 2025-06-27 13:50:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 144.0 |
| fe6e14c8-b01a-37ef-b098-82f9b0c3a5d4 | -5.9213 | -43.4636 | 2025-06-27 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 32e974f2-d3cb-350c-b569-c6da16e39994 | -10.3843 | -46.7752 | 2025-06-27 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| a8bf9502-4174-3fb7-a4fa-21764bf50bcf | -10.384 | -46.7977 | 2025-06-27 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 468.4 |
| 7577973f-d100-3e32-927e-9f4fbf9d6334 | -8.5724 | -51.5552 | 2025-06-27 13:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 3dbee24f-1e85-35e0-9bce-141317092598 | -10.8196 | -53.7459 | 2025-06-27 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 45c7ebc8-00ae-39b9-83d9-fd81db68cb61 | -8.5722 | -51.5761 | 2025-06-27 13:50:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| fb58c346-0a5c-3600-8f59-df57491eba78 | -11.19 | -55.9303 | 2025-06-27 13:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 922c46c9-ee12-3691-b1cf-f385a1136478 | -11.4337 | -54.4689 | 2025-06-27 13:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 62828889-0be3-39bd-ac3b-7571888cc0ee | -11.5779 | -52.115 | 2025-06-27 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| b6c02741-bb94-390a-9cb7-4e71ef97270c | -10.6319 | -46.7226 | 2025-06-27 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| f133af53-7ced-39c6-95e9-fac324a60b7a | -11.1903 | -55.9101 | 2025-06-27 13:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 69.4 |
| e524755a-5a45-3716-a0e3-ac3d0a3a9b5d | -11.5779 | -52.115 | 2025-06-27 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 81.7 |
| e0a70e87-c726-37dc-a3f0-dc31299f1a3f | -14.2442 | -45.5002 | 2025-06-27 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 451068c8-a079-3a50-b7b8-1f87da2b4a7e | -10.6319 | -46.7226 | 2025-06-27 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| ac6d68ee-4456-3186-97ca-b6f85147be87 | -8.5722 | -51.5761 | 2025-06-27 14:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 324c331c-b76f-3790-9ca8-1ebefcedae73 | -11.4337 | -54.4689 | 2025-06-27 14:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| fad6bec8-58a7-3d0f-812e-79a34a80913f | -11.19 | -55.9303 | 2025-06-27 14:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 409b28ab-ef99-3169-8578-b22448c24b80 | -10.6323 | -46.7001 | 2025-06-27 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 86d7d2f3-3e2b-37f0-84b2-aebc060d7afe | -5.9213 | -43.4636 | 2025-06-27 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| ea792dbf-c9e1-3327-b60f-61c243b6fc6e | -11.1903 | -55.9101 | 2025-06-27 14:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| b3b72ae6-0c8c-3d77-9f57-f3a716899053 | -10.8196 | -53.7459 | 2025-06-27 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| c65fc860-610c-3258-839a-475d8fe004f3 | -11.546 | -47.8772 | 2025-06-27 14:00:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 144.9 |
| a14186e6-b7bc-324c-bf96-0082a4211db6 | -10.384 | -46.7977 | 2025-06-27 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 330.4 |
| 6ac52263-1f14-3041-8b41-de0ec6eaa4c3 | -10.2941 | -57.138 | 2025-06-27 14:00:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 343d161f-8019-35c7-a7af-baaaccb2b971 | -8.5724 | -51.5552 | 2025-06-27 14:00:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| aadc754e-c259-3847-a14f-302e172bf8e4 | -11.4337 | -54.4689 | 2025-06-27 14:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| c93e5a84-474f-3907-9644-584fe404a279 | -10.384 | -46.7977 | 2025-06-27 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| f140c702-a5a1-3466-bc4e-e014e81176a3 | -10.6319 | -46.7226 | 2025-06-27 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 845e94a2-c2f1-3bc5-be7e-a0601255de8b | -11.19 | -55.9303 | 2025-06-27 14:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 181.6 |
| 49dc3a0e-48a0-3ce5-8b0d-6c1c1f07b5fe | -11.1903 | -55.9101 | 2025-06-27 14:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 116.6 |
| 875387dd-a76e-3892-a21e-482cbc08e34e | -11.5779 | -52.115 | 2025-06-27 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 4ca7c19a-0a23-3a53-8490-ceab4bc9a825 | -5.9028 | -43.4418 | 2025-06-27 14:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| f51cafcb-d549-393a-9baa-f0fc5df7815e | -5.9216 | -43.4403 | 2025-06-27 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 92ca67d2-14e4-373e-9258-0421ed680c0e | -14.2442 | -45.5002 | 2025-06-27 14:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| d262e251-a86c-3595-b585-51bc939a3554 | -10.6323 | -46.7001 | 2025-06-27 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| e44c1a3d-f194-318e-8bfe-62933bd9790d | -10.6129 | -46.725 | 2025-06-27 14:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 682a71c9-5a17-371a-823c-043219905436 | -8.5722 | -51.5761 | 2025-06-27 14:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| d9355ea2-6ade-3570-b967-3361a58c55cf | -10.8196 | -53.7459 | 2025-06-27 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 9f4157cc-44ce-3a0c-a71a-11bfcc7fd9bf | -11.546 | -47.8772 | 2025-06-27 14:10:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 200.8 |
| 52738108-a6f5-31c2-ab2e-f2b4b37d0ebf | -5.9026 | -43.4651 | 2025-06-27 14:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 6cac8371-e359-3d7d-a3bb-72b92022a91f | -5.9213 | -43.4636 | 2025-06-27 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| d454ae29-10ee-3e68-ba23-048f3756c8cc | -11.4337 | -54.4689 | 2025-06-27 14:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 01bb05e5-f0f0-3beb-ac95-921ea4df10ab | -10.2941 | -57.138 | 2025-06-27 14:20:00 | GOES-19 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 57dcc5b8-a1b3-307d-900f-8bbb06284c81 | -10.2653 | -44.6298 | 2025-06-27 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 332f146a-383e-312e-8bfa-9620ee3a1887 | -11.546 | -47.8772 | 2025-06-27 14:20:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 167.1 |
| dfe7bba5-4a83-3570-abfd-d94b792bb159 | -10.8196 | -53.7459 | 2025-06-27 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 0dff9d8b-430b-3984-b944-688bcc5fbb4c | -10.6319 | -46.7226 | 2025-06-27 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 258d87af-2029-38dd-9bd8-dde54658cf1b | -11.5779 | -52.115 | 2025-06-27 14:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 80.0 |
| e1526076-022c-3307-ab59-017403feee4d | -12.1537 | -44.8013 | 2025-06-27 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 15f8ec6f-cb6d-303d-bbe5-7abebe6cecb0 | -8.5722 | -51.5761 | 2025-06-27 14:20:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 9a45f6a6-98ed-39f5-b087-ef9ecb172b05 | -11.19 | -55.9303 | 2025-06-27 14:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 154.3 |
| fceb1036-407f-3819-99af-6fd5dbadbe94 | -5.9216 | -43.4403 | 2025-06-27 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| ae9adb4c-22a8-33f0-8f7b-6f2ab86edf0f | -5.9026 | -43.4651 | 2025-06-27 14:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| d9054333-e983-3541-9004-5010ed98791e | -10.8198 | -53.7253 | 2025-06-27 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 4513a84d-bc56-3874-a9f3-86aeb16a704f | -10.6323 | -46.7001 | 2025-06-27 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 526f9294-4413-364b-b970-6bc317837b7e | -10.384 | -46.7977 | 2025-06-27 14:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 72345568-7e83-3f0e-8b96-e0375937184f | -11.1903 | -55.9101 | 2025-06-27 14:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 124.6 |
| 5638fbd1-6b21-3dc0-ac92-29a37f5693f9 | -5.9213 | -43.4636 | 2025-06-27 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 108.1 |
| e68d67fc-0b57-3588-9d43-13a5b1e3a8a7 | -14.2442 | -45.5002 | 2025-06-27 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| e7a58968-5444-3019-a732-93a51ec5d5cc | -10.384 | -46.7977 | 2025-06-27 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 6db22bb3-76cd-3192-89f0-9130a6b8cfe9 | -5.9213 | -43.4636 | 2025-06-27 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 100.4 |
| de19c928-54df-3e44-bde8-f403648d05be | -10.6319 | -46.7226 | 2025-06-27 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 07678685-5b49-397c-964c-7b955f396e34 | -10.8198 | -53.7253 | 2025-06-27 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| eb77214a-0c02-3d31-8640-725cbed18f7b | -11.4337 | -54.4689 | 2025-06-27 14:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 62.6 |
| f346d325-4175-3f4a-bd8e-2664cb46c11f | -8.5722 | -51.5761 | 2025-06-27 14:30:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 6b7f540d-1082-3ff7-a6cf-f6b100660247 | -11.19 | -55.9303 | 2025-06-27 14:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 196.6 |
| de3f5e46-7f95-3dbe-869e-eac33f3a8a56 | -5.9026 | -43.4651 | 2025-06-27 14:30:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| db5a1b89-aabd-3851-a070-d4ecd5111d5f | -10.6323 | -46.7001 | 2025-06-27 14:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 133.6 |


[Clique aqui para ver as próximas entradas](README34.md)
