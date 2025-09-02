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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c4674170-7af6-387b-9fe0-d194e794263d | -14.59269 | -54.57552 | 2025-09-02 05:33:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb52147e-0006-3305-a648-d580c8f236b8 | -14.99471 | -50.1959 | 2025-09-02 05:33:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 804fc61e-0fbc-3250-b43b-e988c0b1c1af | -12.62396 | -56.99868 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0121148-f70e-30ae-b956-c2786c4388a7 | -11.96818 | -63.70515 | 2025-09-02 05:33:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ce9e3a43-bf04-31a1-82b4-545202f8b6d7 | -12.90115 | -56.94952 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cca0947e-0408-3baa-97ce-752f9bbbe6db | -14.84229 | -60.04424 | 2025-09-02 05:33:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b901bbb8-b36a-3220-b288-9b7ff2b5ed2d | -11.65295 | -57.35332 | 2025-09-02 05:33:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ba82c04e-7ba8-3d25-b070-1c0f5815464c | -12.93182 | -56.95879 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7fded0bf-27b3-3816-b245-3eab8217eb6d | -12.91784 | -56.96124 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2144ddf-829b-3067-a4b1-18638c763e0f | -12.92348 | -56.95295 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec061dd6-f0dd-3a25-bcfd-08c51f1b73a0 | -12.33142 | -63.73553 | 2025-09-02 05:33:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 068deef7-1f4d-3104-97f9-f496e1fe7f7f | -14.19635 | -51.65853 | 2025-09-02 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16086445-1d53-3563-bf34-ef4fbcbbebeb | -14.20271 | -51.66 | 2025-09-02 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de7de1f7-10d1-3933-b619-e5ac0e99ed4a | -16.28558 | -52.95116 | 2025-09-02 05:33:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1bbc5a68-4eb9-3567-863f-25bf565dd534 | -11.65413 | -57.35489 | 2025-09-02 05:33:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e44b8d96-e7a5-3451-b49f-838ec47b6239 | -14.56708 | -59.73093 | 2025-09-02 05:33:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 944d7d57-2eff-3dbf-b9ef-d7f9dd7a343e | -15.72738 | -53.67628 | 2025-09-02 05:33:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1cc00c9-95c0-3956-9b30-6dfe618ef604 | -12.92527 | -56.93929 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 24a57d95-3fc9-3ede-b06f-9761b9eee571 | -12.44994 | -63.92952 | 2025-09-02 05:33:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e2a422e-7005-3a9a-a042-213ba2ab016e | -12.9202 | -56.94324 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7682faef-397d-3b0b-9244-502d4430725a | -11.65189 | -57.36123 | 2025-09-02 05:33:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 2aada824-f2dd-30d8-8e30-ee614eecf112 | -12.93242 | -56.95429 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06e9942d-41ee-3877-8157-a88f96d751f2 | -12.92114 | -56.97072 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 085e34ca-776f-3c2e-a357-aa2f95b565f2 | -12.42278 | -63.9068 | 2025-09-02 05:33:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cf3f851-5610-3d7e-b602-518ab35cfb39 | -15.7301 | -53.65059 | 2025-09-02 05:33:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a87f71a8-eb5f-32f4-9c2e-0bc798112f9a | -12.91751 | -56.92893 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 369c02c3-266e-330a-96ba-a9dc998f61fb | -12.92618 | -56.96702 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5aebafbc-6e98-383e-90d4-e0cb229726ac | -15.72965 | -53.6526 | 2025-09-02 05:33:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c6f7ed55-e17e-39c7-847b-63ebcc95e68e | -14.99407 | -50.20238 | 2025-09-02 05:33:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4a2cda07-b558-3b19-8b37-401fd265402a | -12.92172 | -56.96633 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e9b688de-0ad3-3fa1-8689-612d0f7ef9e4 | -12.92467 | -56.94387 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6d9308d8-8a59-35b1-92c9-8dad29d96da3 | -12.62899 | -56.99494 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 63717ce1-94f4-33ee-a9f8-10ecb046e02c | -12.9831 | -54.76476 | 2025-09-02 05:33:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ffcab18a-b5c6-3e12-83b6-a1a38f4b94bb | -12.62456 | -56.99426 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae6d79ca-ecab-3c78-bbff-00fb0ca08d0f | -12.42611 | -63.90736 | 2025-09-02 05:33:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e912ba8e-5000-3a45-982d-45564e4e649b | -12.93101 | -56.99932 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 646707b7-5214-39a2-8dbe-ad6929e71758 | -12.93959 | -56.96888 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f72a3fea-4cdb-3060-a4c8-875813ccdeb0 | -16.29857 | -52.94495 | 2025-09-02 05:33:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8393601b-0e27-3040-b68d-a872da6f1cf9 | -16.29764 | -52.95381 | 2025-09-02 05:33:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ac13a0b-b908-3f16-86c2-c4668590bfae | -14.84293 | -60.03955 | 2025-09-02 05:33:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afeb771d-321e-35d0-b3e0-47035be4b545 | -12.93512 | -56.96827 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| de83e86f-1f93-3a3f-b8e5-42de3071ac6c | -14.20216 | -51.66516 | 2025-09-02 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 1aecba41-c366-3eb2-82c1-53cfb6be673c | -12.92139 | -56.93413 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8cb0f820-f307-30b0-a462-3f01f53b72ff | -12.93571 | -56.96386 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0e9b4b3c-aa7c-31a8-b4a5-1fcc3625afe7 | -16.29308 | -52.9385 | 2025-09-02 05:33:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 52e9eae4-e3da-37fa-a978-2aa2642b845a | -12.92268 | -56.99359 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8c3350b7-fb8b-3cc5-a633-2aa698862c10 | -14.56461 | -53.00145 | 2025-09-02 05:33:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50d3ae8a-9f8c-352c-a75f-78ad070cfea8 | -14.58505 | -54.54702 | 2025-09-02 05:33:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9d30fbb6-9efd-3c32-ac8f-7293ff1ca99b | -12.605 | -57.0052 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 78d83f3c-c722-38cc-aa7f-d1b78f217531 | -14.21506 | -51.66648 | 2025-09-02 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4cfa92b1-eb19-3fb6-a443-cd878ca2bedc | -12.93007 | -56.97208 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69b3a412-c19f-30fb-b9d3-227f6dd091d3 | -14.98768 | -50.19472 | 2025-09-02 05:33:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3269d2b6-22f8-32d7-9d41-2b9606f78435 | -11.66043 | -57.3625 | 2025-09-02 05:33:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 54ae94fa-9e56-353b-bbf6-69f9374655a2 | -12.6278 | -57.0038 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e35d79a2-5530-36b5-b134-0cd2094d06f4 | -12.93664 | -56.99113 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 031de159-0001-32eb-afa7-ef1a455d7c99 | -9.95533 | -66.87444 | 2025-09-02 05:33:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 601ff560-99d8-31fb-ae6b-9eba727d9448 | -15.73056 | -53.64624 | 2025-09-02 05:33:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 031ed3ce-5faa-3a50-88dd-7b1a4b0f9202 | -12.60885 | -57.01024 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a9e1147d-4c79-3355-a8d0-5cff5deb0405 | -15.67163 | -56.443 | 2025-09-02 05:33:00 | NPP-375D | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a28b7dd2-d6c2-3d69-b6d6-2cffcce44500 | -16.29913 | -52.93964 | 2025-09-02 05:33:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1495f127-8295-39a4-b660-27c928e84466 | -11.65722 | -57.35395 | 2025-09-02 05:33:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2e2767d7-c3fa-3f06-aa0e-4393feebf4fc | -12.93454 | -56.97268 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e5d134d-5e82-322b-9ee0-d173bbc5ec88 | -14.2086 | -51.66592 | 2025-09-02 05:33:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 565208ff-7ab8-3502-af0f-712d1314e04e | -12.93159 | -56.99493 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 62060380-f94f-3a8f-808e-6551a96675e3 | -12.42221 | -63.91035 | 2025-09-02 05:33:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22a9a091-7324-3c21-91e9-0f4f31f78d7f | -12.91067 | -56.94638 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 813e5379-68af-3355-bda0-b0ae8fd4b190 | -14.60339 | -54.57735 | 2025-09-02 05:33:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f692a5b2-6d37-3ada-a039-4879065dc425 | -11.65242 | -57.35727 | 2025-09-02 05:33:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d8ed9d36-bb11-392b-a095-a0c38edd1738 | -14.31613 | -60.33997 | 2025-09-02 05:33:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 573abc75-5ed4-330d-865f-d4cae94e4e05 | -14.987 | -50.20158 | 2025-09-02 05:33:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 269f8e1c-87bf-3685-86c8-52bc8792c5f5 | -12.9223 | -56.96193 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b09df02-ce6f-3e5e-9cf9-5a241024af2f | -14.98833 | -50.18811 | 2025-09-02 05:33:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8c0e450b-6af9-33f9-a705-7e8aa0452403 | -12.92655 | -56.99871 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 053c2e03-7eea-39cb-9c4e-61a2e5df4943 | -11.65302 | -57.36277 | 2025-09-02 05:33:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 92102a41-25a3-3d80-9f02-1dadbaaa501e | -12.90057 | -56.95399 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbe2095a-cef5-3564-9e6a-9ca0449a972a | -12.92713 | -56.99428 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 64e312b4-8e13-3651-b42a-1aae61607730 | -12.92855 | -56.94908 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2721c9f5-f4b4-3471-a435-94fea82c1946 | -12.94077 | -56.96002 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b08533ad-e94e-342e-acb7-d8ad7e97bafb | -12.92502 | -56.97585 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef4f15d5-57a4-3f47-8f17-5ccc5b7d63de | -9.95611 | -66.86981 | 2025-09-02 05:33:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1188bf08-4ac3-33fc-8d3a-3818f98538c5 | -12.93123 | -56.96326 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ab7d15c-f66a-39f0-a72a-605c612d1ac4 | -14.56553 | -52.99316 | 2025-09-02 05:33:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c138eca-ea53-35c2-898b-3c7db063f197 | -11.83038 | -62.92579 | 2025-09-02 05:33:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ea53371-c7fa-3181-8b30-fd86c8cd3a76 | -12.93065 | -56.96767 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10f7323f-ea46-37f1-992d-d39c70461367 | -15.4531 | -59.10094 | 2025-09-02 05:33:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 61d41400-cb21-38a2-937a-c50382349e4e | -12.9363 | -56.9594 | 2025-09-02 05:33:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f92001bc-65ee-33bc-b74e-decc35b55cbf | -23.53602 | -51.59588 | 2025-09-02 05:36:00 | NPP-375D | CAMBIRA | PARANÁ | Brasil | 4103800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0f0a66d9-942e-3b8c-bf10-dead9a04d527 | -10.0623 | -48.0978 | 2025-09-02 05:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| e7760816-5126-39e4-aec6-47b6d302518f | -11.1033 | -44.6548 | 2025-09-02 05:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 726605d3-e522-3ee6-ad2a-35557b36c226 | -7.5476 | -61.3437 | 2025-09-02 05:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| bcdfb501-fbca-3c45-93e5-c11c7409953d | -11.1037 | -44.6315 | 2025-09-02 05:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 8b7b1c6b-a4dc-3b91-9a9e-8430c9c2f63b | -11.0841 | -44.6575 | 2025-09-02 05:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 34c72a5b-4d44-3805-9959-6a44c9df54f0 | -13.6918 | -46.9439 | 2025-09-02 05:40:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 51a28295-89dd-35d6-8ba8-87aae81ad648 | -7.5476 | -61.3437 | 2025-09-02 05:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 70c60473-181e-3c9e-a52c-5eaa9af0d2ce | -11.1037 | -44.6315 | 2025-09-02 05:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 40944c57-b5c7-363b-9149-3cd0deb8aeff | -11.1033 | -44.6548 | 2025-09-02 05:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 55c048e9-cc9a-3aad-b3dc-18af5db598b9 | -10.0623 | -48.0978 | 2025-09-02 05:50:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 1fac1a24-f7ff-3a70-be76-a85a06a7886f | -7.69821 | -61.10508 | 2025-09-02 05:53:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d0d4ca31-41d2-3379-8c66-5805087b0adf | -8.69144 | -62.41238 | 2025-09-02 05:53:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35495167-cae8-33f7-81c0-0750687131e3 | -6.92788 | -63.13577 | 2025-09-02 05:53:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README82.md)
