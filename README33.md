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
| deb49a3c-f7ad-3633-a8a6-af517444388c | -5.81771 | -46.22157 | 2026-08-28 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 57d3ee80-e993-3cf3-9927-05fbd2a221cd | -3.94296 | -54.8394 | 2026-08-28 04:49:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1535f448-4462-3615-a349-a321d3c9c744 | -6.5687 | -50.0234 | 2026-08-28 04:49:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f89c5ffc-40e4-3f4b-8876-7ee4aabea29d | -5.77751 | -46.16808 | 2026-08-28 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43df6e8f-7515-3c80-85f8-4c5aad1ddfdf | -7.44395 | -41.49002 | 2026-08-28 04:49:00 | NPP-375D | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| de394a14-4a7c-377e-934c-5d8ba43d58d4 | -8.08171 | -45.85437 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4209bcba-0001-3267-a29d-2292e81b1ef8 | -8.08551 | -45.85502 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7d83865-ebeb-38dd-a620-e72d079900ca | -8.17346 | -46.1713 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f7809431-1689-3b56-9fee-ee671659bead | -6.50095 | -53.25874 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e9d77f9f-dbdf-3d7a-85da-19d61cd65dc9 | -7.78379 | -46.14774 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 656a32c7-5b12-3f85-8c3d-4cd9685a6568 | -8.16729 | -46.16129 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4946e82-1010-3c81-abda-a998c22f7e9d | -4.84182 | -45.39432 | 2026-08-28 04:49:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6fa6d0c0-2949-328a-bb05-d95ffd00eb6d | -7.27238 | -45.35245 | 2026-08-28 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 896dda7a-26ac-3a36-8307-063755cd111b | -7.2537 | -45.85738 | 2026-08-28 04:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 64025540-6dc7-3ee2-a41d-69a645f6570a | -6.23447 | -55.47056 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 363a5f5f-910c-3a75-9acb-ed7e51b480c1 | -6.26263 | -53.34259 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7be550df-c8dd-33b1-839d-d213dda6ee4c | -1.70151 | -50.23471 | 2026-08-28 04:49:00 | NPP-375D | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b8b7b154-3b43-32e8-a4bc-2143472aa08d | -6.50169 | -53.25426 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 52e76d7a-b6b2-307a-81b9-8aeaae7449f9 | -8.08177 | -45.80931 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cbd93d84-2bf6-39a8-adc6-05c0a97907ca | -7.08884 | -42.7945 | 2026-08-28 04:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d7470ae8-cb23-3438-9a23-c70e403bc823 | -8.15153 | -46.19023 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c8823af-3fc1-360a-b303-4db7ecaad970 | -5.28876 | -50.93633 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 831ba1a0-e247-3163-873b-3744dfa22274 | -5.87367 | -52.18848 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d27736f3-43f4-3960-8735-2c8651e6ac2a | -6.13058 | -53.52964 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f2c9fec-caf4-349a-b266-83f618af0e97 | -5.25622 | -50.96485 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 794eec8d-863b-3608-9aa1-5199a61bcf0c | -2.73422 | -47.04832 | 2026-08-28 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 413683e5-c877-3dda-be4b-74639456398c | -4.92741 | -47.4635 | 2026-08-28 04:49:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8328cb4-69bc-33e4-9652-c851e0d56cc3 | -2.50193 | -48.13917 | 2026-08-28 04:49:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9cfc1b2-78fc-3dc0-9fd0-71ce935972c0 | -6.63667 | -53.1842 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41b8dbf8-00e4-3767-a811-e67944f6246d | -6.53161 | -55.25133 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 313372d2-774e-30d8-87cb-42ebb1c6e360 | -5.26244 | -50.96961 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 342412d1-09f2-34bf-a747-a39bdec3bed4 | -3.05886 | -48.74673 | 2026-08-28 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a43e5f41-9764-38a4-969f-aa16073fe3df | -5.95393 | -44.7802 | 2026-08-28 04:49:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| af538fe3-5afe-38aa-9077-04d6029b154a | -5.28818 | -50.93998 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0b731a2-2239-3ecb-b749-ad1b01aaec80 | -7.27843 | -49.9475 | 2026-08-28 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 536de46a-0049-3673-be1f-439030dced11 | -4.45406 | -55.49463 | 2026-08-28 04:49:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1ea0871-9b5b-3328-8f1c-37c1b6da3f0f | -8.17478 | -46.16245 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8bab1719-df75-33ea-8d22-81d9e2dc621c | -5.82134 | -46.22213 | 2026-08-28 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6104760d-f1c6-34cd-bd33-e34f8909548d | -8.07794 | -45.80881 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 17646778-7b0a-3679-9802-bb2d5dc3be46 | -1.85921 | -55.20918 | 2026-08-28 04:49:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ee0cb1f3-d64e-3e0c-b61e-af3fbe1a3812 | -6.22669 | -55.49008 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 19db32c6-08bd-38ae-9364-8ea76dd97ce7 | -6.62483 | -53.1867 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d4fc5ea-62e9-3a30-abe2-5c6c9a07b953 | -2.73536 | -47.04102 | 2026-08-28 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5aba7c6-dd1c-3a1c-9686-dc3e332dcfab | -7.06313 | -42.1622 | 2026-08-28 04:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| da8b70a5-840f-33f4-b80a-6cfaae05f65a | -2.23405 | -47.71569 | 2026-08-28 04:49:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14484418-1343-387e-ae99-67dc9582c361 | -6.17532 | -57.79037 | 2026-08-28 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44ee6c9f-de67-3b69-86db-cd26102679ec | -7.87995 | -46.10044 | 2026-08-28 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2576e456-431c-3bd0-825c-e957d477d829 | -6.42926 | -54.9403 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a0cb623-1ada-3823-b213-8424174e9fd2 | -6.51609 | -55.2406 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 376861a4-d1c7-3b96-971d-a5ea9380b3e9 | -6.28063 | -53.37356 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f68ad44d-4632-3156-ad4a-296e99d435e0 | -3.70075 | -45.24167 | 2026-08-28 04:49:00 | NPP-375D | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7bb52948-8c36-343a-8613-2d79c8456a0a | -6.5274 | -55.25059 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55848940-b5c8-33fe-a39d-071cb372c4e3 | -6.18389 | -45.92258 | 2026-08-28 04:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0013fbc5-bff5-3659-8cbe-b6ab476a02d5 | -6.53293 | -55.24351 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e9444795-899a-3932-a1e5-f71fb8967ca3 | -7.25302 | -45.86194 | 2026-08-28 04:49:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| f5c74bfd-c67e-3217-bcff-bedba1b4397c | -5.30762 | -47.05671 | 2026-08-28 04:49:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 509f46df-a128-393f-b543-67a1e11017f4 | -6.25996 | -55.42471 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40e2e1dd-231e-34c7-b643-146bd8b45f1b | -3.53741 | -48.18019 | 2026-08-28 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42037d62-ea40-336f-a5b3-b67af7c73568 | -6.23514 | -53.4834 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d0b4798-3d07-36fe-878d-779d476455d1 | -5.94215 | -52.36506 | 2026-08-28 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 78c2985e-f75e-3cda-9263-31df956a3539 | -5.52581 | -45.23008 | 2026-08-28 04:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90493683-d3cc-3a29-8281-67cdeeacaef3 | -6.26635 | -53.36649 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e07e9c8a-0b54-3d60-a5bb-5408f1b4781e | -7.28508 | -49.94853 | 2026-08-28 04:49:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b83f2a64-c37d-360a-891b-376140614c4f | -2.73081 | -47.0478 | 2026-08-28 04:49:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 153cb327-94dc-34e8-967c-73f9cca1d219 | -6.15767 | -57.80211 | 2026-08-28 04:49:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d689fde-65c7-31ae-ab7b-3d511bcaefcd | -6.27763 | -53.36838 | 2026-08-28 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f9ff30cb-0d38-3ab7-8e33-a184b5723c07 | -6.24737 | -55.47268 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2104e61f-43d3-3b22-a7af-18f9fc8cf9c9 | -3.06218 | -48.74725 | 2026-08-28 04:49:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2e5383b-644a-3d5c-abc3-8ab09952288f | -4.8517 | -45.40498 | 2026-08-28 04:49:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 4c139482-439b-36f8-b5b5-e15e8b53daea | -6.22979 | -55.94101 | 2026-08-28 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0070022-38d1-37ce-915e-a7e42fabc4bf | -4.8425 | -45.38982 | 2026-08-28 04:49:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 61476f88-7e9e-368b-98dc-ce723be25a33 | -6.6237 | -43.73666 | 2026-08-28 04:49:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10e17f0e-343a-3672-ace7-880b9e50c88f | -16.1641 | -58.5851 | 2026-08-28 04:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 201.9 |
| af438d99-f6ae-37ea-bab7-3511bca6f649 | -12.43 | -43.4182 | 2026-08-28 04:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 88b36bdc-4cc1-39d0-a876-dd1152c43c00 | -16.1644 | -58.565 | 2026-08-28 04:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.8 |
| ee2c67e2-0487-3218-b2f7-3e9194be40f9 | -11.1922 | -51.2284 | 2026-08-28 04:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 76fc55d2-daaf-34c1-afce-6abb33a177de | -6.1656 | -57.7988 | 2026-08-28 04:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| ba549114-42a0-3cbf-b817-5e5093804b1e | -12.2659 | -50.5747 | 2026-08-28 04:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 3c15cb3e-9900-3b7d-8f7d-242854d27eb0 | -7.2471 | -45.8685 | 2026-08-28 04:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 3f42f7ee-6e42-3e3a-a5bf-21ca7702aa2a | -7.2659 | -45.8668 | 2026-08-28 04:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 9b386f6e-55ec-3c58-8ca4-27db7b158c3d | -12.4305 | -43.3944 | 2026-08-28 04:50:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 114.1 |
| 2386a45a-c270-3354-8283-3fec264d604d | -10.5168 | -64.4997 | 2026-08-28 04:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 5c6de256-9165-3dfd-930e-ee6f74edeac5 | -11.2111 | -51.2264 | 2026-08-28 04:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 4e09a6d6-1f5e-3fcd-a0a2-d2a42fdaefd0 | -10.4981 | -64.5005 | 2026-08-28 04:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 10a60ace-2788-3a2d-947e-31dd3abee278 | -7.2661 | -45.8443 | 2026-08-28 04:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 34265b6e-7572-32fd-8fbb-73130baf2078 | -7.2474 | -45.846 | 2026-08-28 04:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 4fc985bf-8aef-3005-ac5c-59a9863b071a | -16.1447 | -58.5871 | 2026-08-28 04:50:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.2 |
| 918e0ad7-0334-3ac6-a42c-7f56e3687334 | -6.1657 | -57.7793 | 2026-08-28 04:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| ace1943d-7403-308f-aa13-5c879f0454cc | -11.2109 | -51.2476 | 2026-08-28 04:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 59cbdcb9-6853-33e3-b826-c7b6dd441908 | -12.2468 | -50.577 | 2026-08-28 04:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 90777916-9c83-3aa0-8a98-52905c889ae1 | -13.60324 | -45.78331 | 2026-08-28 04:51:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 26bd64f6-ef34-3cef-bcbf-66dd24d961b9 | -8.58862 | -54.78766 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 42c912a2-f551-3304-82cc-37962a6449da | -8.60399 | -54.7141 | 2026-08-28 04:51:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60bc0bcb-7084-303d-9a68-c574d8e648e5 | -11.79708 | -47.67289 | 2026-08-28 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5977d6bf-f395-371e-bf9d-8d77f7b639d0 | -14.21669 | -45.30407 | 2026-08-28 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52f66a63-6a4c-36da-98f8-b6f19326e5d0 | -9.08082 | -53.03619 | 2026-08-28 04:51:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a3f086ce-8a36-3803-b8f7-9a36058c9af3 | -10.91437 | -50.53566 | 2026-08-28 04:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8110bede-e681-322e-8ddd-e697ddb6fcd0 | -6.83488 | -55.61128 | 2026-08-28 04:51:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46efd35b-2e5f-3035-a660-2dc34fa1758f | -13.46129 | -57.04613 | 2026-08-28 04:51:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54497967-6c98-3f20-9329-d9b833688faa | -12.91571 | -59.88346 | 2026-08-28 04:51:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README34.md)
