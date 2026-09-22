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
| db7f9de1-279a-308a-b864-43dd0b504f0c | -6.2988 | -57.734299 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7e91b16-4a18-3d63-a5ff-67911037c787 | -9.1252 | -58.885399 | 2026-09-22 00:57:00 | METOP-B | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 673d4e1f-6231-3609-bac7-0b85b3e8f8df | -7.57 | -57.657799 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fb1452c2-1661-3f40-ad16-dbb8b41b1522 | -5.9696 | -57.7817 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37f4238f-2608-3cf5-886b-b26df990c58d | -5.8132 | -57.729599 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 590a9dd7-19ae-3d10-9219-d841fc2db43b | -6.2814 | -57.7481 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1458f853-b0ea-3b4a-96b4-da28a999f54f | -8.2369 | -55.262199 | 2026-09-22 00:57:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e6ce0ef-e83b-387e-8812-72c9da9f2cdb | -12.9308 | -51.035 | 2026-09-22 00:57:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2d681712-f638-3336-9b11-06e060c646b2 | -3.0485 | -54.4179 | 2026-09-22 00:57:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 931538f8-5785-3bd2-8e62-b4b1dbdeced9 | -2.4064 | -58.272701 | 2026-09-22 00:57:00 | METOP-B | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ae41e5fc-fd14-31c5-9773-3157fde9bb70 | -5.9429 | -59.9823 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f8bf6843-db57-3d16-aaa8-ba8b64fa1d43 | -6.6147 | -59.898701 | 2026-09-22 00:57:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| de4b2417-ea25-38f8-a047-c584a7aa19cf | -3.8151 | -58.888802 | 2026-09-22 00:57:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f0885fa9-6b8a-3baa-a305-cb47c892e842 | -6.3271 | -59.948898 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 309fff77-e99a-35e9-a5a3-a83bb87863fb | -7.5644 | -57.678101 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 233080d0-96d9-3dd6-b6c5-499ed83733e6 | -6.6329 | -59.933102 | 2026-09-22 00:57:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 26aebcd7-acd7-3ee8-ba34-7a456794d141 | -3.3843 | -61.284698 | 2026-09-22 00:57:00 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2762d715-9b15-3e30-8e51-121c2cbdf0c8 | -6.6393 | -59.916199 | 2026-09-22 00:57:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6628078e-5fd5-353d-8bf6-3edf5cbf0ffc | -3.3337 | -61.2887 | 2026-09-22 00:57:00 | METOP-B | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a7d7fa3e-ef1e-3993-8448-276ad678d8be | -8.8188 | -50.508499 | 2026-09-22 00:57:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af66a2dc-2e8c-364e-9e23-a5dc9b461c54 | -3.6119 | -60.564301 | 2026-09-22 00:57:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 18da936e-9464-3d57-b632-023720a4d53e | -8.2407 | -55.235001 | 2026-09-22 00:57:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44e89637-2409-360d-87a1-c83137d97ab3 | -6.289 | -57.736599 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23f2b79e-fcb8-3187-b0d9-f727c349220b | -7.3189 | -55.601799 | 2026-09-22 00:57:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffd4d334-078f-3e9a-8244-a4e515abd1d2 | -18.7279 | -46.935101 | 2026-09-22 00:57:00 | METOP-B | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9414b381-004b-3d5b-aaba-47f21a927b08 | -3.3404 | -59.872501 | 2026-09-22 00:57:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fa8a9feb-9e2a-3bf1-9018-b98a0cda6a91 | -6.7275 | -55.069901 | 2026-09-22 00:57:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52836c3f-d5b6-316d-8042-b880eb8aa5f8 | -3.9237 | -56.0401 | 2026-09-22 00:57:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3dc67a4b-f0f9-37d8-83f0-e0c78eb4eac5 | -6.6491 | -59.913898 | 2026-09-22 00:57:00 | METOP-B | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0df443a2-87d1-3f84-a1a8-08bdf3614408 | -3.1805 | -61.204601 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 08fdf95d-9eff-306e-886b-47b6b20bec94 | -6.3386 | -59.953999 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b84eac43-d7ea-3982-ac47-f4eecfbbbd4d | -7.5742 | -57.6758 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 558347e9-f27f-3996-a6d8-82bdc406dffb | -6.7422 | -59.421299 | 2026-09-22 00:57:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 28264eb3-c747-32a2-a433-34394adf59d3 | -3.7465 | -58.324501 | 2026-09-22 00:57:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 53391409-2780-3b0c-a1fb-dce642de9b25 | 0.7886 | -59.191002 | 2026-09-22 00:57:00 | METOP-B | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1879ef90-0910-359e-b229-fe1c9585fcad | -6.4599 | -59.987999 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 88ea3ce2-77a0-38a5-ba60-cd2065a81fd1 | -6.3009 | -57.7435 | 2026-09-22 00:57:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac0bb26d-2e8c-3b78-a474-41d604677fae | -9.5708 | -66.029198 | 2026-09-22 00:57:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9be40641-b6be-34fd-814d-d13c4f954407 | -3.2186 | -61.054501 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d70dc047-0bdb-3583-808b-d23395e32457 | -8.8122 | -50.483002 | 2026-09-22 00:57:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e7ddae7-378a-3c3b-8aaa-7d389c91c27f | -2.7809 | -59.949501 | 2026-09-22 00:57:00 | METOP-B | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 88525748-bce9-3f5d-bf99-e809e098af33 | -6.8266 | -55.525299 | 2026-09-22 00:57:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3daffa24-071e-3916-896c-0a2ef8c707f4 | -5.4307 | -60.222198 | 2026-09-22 00:57:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b5f2f94b-8603-32d2-98ff-2a675dd0360a | -2.9452 | -57.709499 | 2026-09-22 00:57:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 978a93c8-f3b2-30e5-999f-3d086fbfaadf | -3.0594 | -61.261398 | 2026-09-22 00:57:00 | METOP-B | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f4e26326-e230-3a79-af67-2945ebedcf74 | -3.6822 | -60.556099 | 2026-09-22 00:57:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5d956414-c3a6-3638-a35f-9c6526970e20 | -8.0931 | -55.349499 | 2026-09-22 00:57:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 359e350b-879f-38fa-ab71-a631f25c1e2e | -9.19059 | -65.85822 | 2026-09-22 00:58:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.7 |
| fcbf53a3-1cff-31f2-b0ec-9c22151dd49e | -9.56238 | -66.02719 | 2026-09-22 00:58:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 3410467e-a6ec-3bd0-bbf8-3064870162fc | -12.14366 | -61.17171 | 2026-09-22 00:58:00 | TERRA_M-M | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 0132566f-871a-3be9-8a35-b6584a8998c7 | -9.95022 | -60.2165 | 2026-09-22 00:58:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 551f1e49-3e51-3edd-bca0-336cfb4d14db | -11.31789 | -54.0432 | 2026-09-22 00:58:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 224.3 |
| 5d4e76e9-8321-3f27-b448-cc9d8d2318d3 | -9.10116 | -67.82014 | 2026-09-22 00:58:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3dd63fe0-401b-37f0-93d2-472d838cd2c2 | -11.96615 | -64.04441 | 2026-09-22 00:58:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7122ab52-74c6-3425-b6f9-636739f12047 | -7.59556 | -57.66727 | 2026-09-22 00:58:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 64b01cb4-0033-3638-bc3c-3c58423b2282 | -10.59562 | -54.01334 | 2026-09-22 00:58:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 3249c3e5-60f2-3086-9180-b41555b3c5de | -9.87351 | -55.72718 | 2026-09-22 00:58:00 | TERRA_M-M | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 30.1 |
| 2b28e53e-5840-3cd0-8e21-be96089f5022 | -10.60583 | -53.97542 | 2026-09-22 00:58:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 862.3 |
| 32c704dd-1d2c-35d2-8b19-fec95157c621 | -8.63555 | -54.63434 | 2026-09-22 00:58:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 4755d811-5a3b-3f8f-8cc1-1fcc2e996a4f | -9.40877 | -65.92119 | 2026-09-22 00:58:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b5f1d156-90b9-35aa-b421-d6f1efa3f1df | -12.11843 | -61.9492 | 2026-09-22 00:58:00 | TERRA_M-M | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f5f31338-5789-393d-a9a6-779838833a49 | -8.6275 | -54.64083 | 2026-09-22 00:58:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 1cd8aa64-66ed-32c2-a7f6-111696210c2f | -10.21996 | -53.91692 | 2026-09-22 00:58:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 9ce80cb9-e6d8-3384-80aa-65d3a5c426e2 | -9.39947 | -65.92253 | 2026-09-22 00:58:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 076cfa38-b945-3045-9694-c43bc53a5a2d | -8.25907 | -55.29398 | 2026-09-22 00:58:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 92a78730-615b-3616-a70c-37aa56dc2d76 | -9.54361 | -65.68966 | 2026-09-22 00:58:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 5f07c038-9b1e-32a6-ab70-5a645a90a783 | -8.7978 | -60.80694 | 2026-09-22 00:58:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| aad215eb-25a2-3cee-886f-3fd0f9c1b660 | -9.13861 | -67.94698 | 2026-09-22 00:58:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| a9bb755d-5e36-3f62-ba93-8be5485aa4ad | -10.60266 | -54.00483 | 2026-09-22 00:58:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 484.3 |
| c511e47f-4e9f-38ad-ab87-a32986272170 | -7.56979 | -57.67138 | 2026-09-22 00:58:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 32.1 |
| a476691d-0abe-34c6-afe7-37dd5b65cad6 | -9.29502 | -58.90773 | 2026-09-22 00:58:00 | TERRA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 07e7daf3-5dd3-33a7-8882-df289c9eebf5 | -7.57297 | -57.69156 | 2026-09-22 00:58:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| ae93ece6-3057-3125-ad56-fb433e6e7376 | -7.33293 | -55.60971 | 2026-09-22 00:58:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 672c0614-3752-33c4-8a9e-d7c798c34277 | -8.25523 | -55.28795 | 2026-09-22 00:58:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 24d24af6-0077-30f0-87dc-7c25c62c8ef9 | -10.59649 | -53.97012 | 2026-09-22 00:58:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 379.4 |
| d4d60a17-7235-3723-aec6-91e96e751e18 | -9.29728 | -58.92271 | 2026-09-22 00:58:00 | TERRA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 31.9 |
| 9f4183d5-15f4-3e41-9113-56941efee109 | -8.61954 | -54.63704 | 2026-09-22 00:58:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 36110e31-f383-38b3-b203-82492d2c910c | -8.62203 | -54.60719 | 2026-09-22 00:58:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| e23f7985-0fb8-3f5f-8af9-0fb2c663f156 | -9.36641 | -68.66297 | 2026-09-22 00:58:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 718d3f92-5be6-308f-816e-fe1a2e9d4f17 | -9.13092 | -58.89293 | 2026-09-22 00:58:00 | TERRA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 44200222-0d5c-3e75-bd1b-dd70e879e932 | -7.59872 | -57.68761 | 2026-09-22 00:58:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| b6f434c4-d01b-3b51-a724-3c5cbe014725 | -10.58966 | -53.97854 | 2026-09-22 00:58:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 78711cea-5cca-3108-8cb9-c18b3f8e4e8d | -7.58584 | -57.68957 | 2026-09-22 00:58:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 04acc5c8-dd6c-324c-9d3c-f318a5532b75 | -9.56104 | -66.01705 | 2026-09-22 00:58:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 4e13d38a-60ee-339b-b321-486d5e3e329d | -10.09896 | -69.12911 | 2026-09-22 00:58:00 | TERRA_M-M | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 12.3 |
| a8f77c05-3f44-3b9d-931e-afb0a82ae2e2 | -9.80425 | -68.13237 | 2026-09-22 00:58:00 | TERRA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 9.5 |
| f52a6fd9-c8c6-340f-9e7f-d2d8c39d84c3 | -8.10271 | -55.36337 | 2026-09-22 00:58:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| b544daa3-fdf5-30be-86c6-8a0f3c9d0dce | -10.61173 | -54.01013 | 2026-09-22 00:58:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 555.9 |
| 6d9f97a5-07e7-3629-9f92-78e0b3287a62 | -9.55835 | -65.99689 | 2026-09-22 00:58:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 17242c18-e26f-3267-9fea-fb53e22c7d24 | -9.55435 | -66.03864 | 2026-09-22 00:58:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.5 |
| fc81ad5c-4e6e-3db0-a170-017ce9dce9a2 | -9.14028 | -67.96011 | 2026-09-22 00:58:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3d05c175-103a-3baa-976d-fd0bd6d3769d | -10.6127 | -53.96719 | 2026-09-22 00:58:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 295.0 |
| 291ee667-7691-3f87-a220-29dcac1b759c | -9.55569 | -66.04876 | 2026-09-22 00:58:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| be898502-8238-35b7-bc03-5450144183be | -10.61885 | -54.00199 | 2026-09-22 00:58:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 431.5 |
| 7d70e9f1-ad3f-3eac-80a4-c9a06d4c5955 | -9.30732 | -58.91545 | 2026-09-22 00:58:00 | TERRA_M-M | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4a4f4c1b-cefd-33be-936f-d7564a3715ad | -8.60599 | -54.61001 | 2026-09-22 00:58:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 3c7c0fd8-7b1a-397c-a012-ffca208ce05a | -7.58267 | -57.66933 | 2026-09-22 00:58:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 0213e995-d54d-389b-a6d8-cc9c19161ebb | -9.56373 | -66.03734 | 2026-09-22 00:58:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 2d91312c-2365-3ad7-8b35-c332d04e6c60 | -8.26029 | -55.31798 | 2026-09-22 00:58:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| f347b131-89a3-310d-8d31-b59da59e53ba | -13.03462 | -60.36599 | 2026-09-22 00:58:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |


[Clique aqui para ver as próximas entradas](README11.md)
