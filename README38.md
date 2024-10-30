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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1e5413a-6386-3ce6-beff-0df2d16c46ad | -5.97144 | -45.36862 | 2024-10-30 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 812f339c-a59a-3b6c-970a-23a846e0c0ce | -5.97089 | -45.3721 | 2024-10-30 04:19:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| c43f6960-6a57-324f-b001-196a66446942 | -5.7496 | -45.56401 | 2024-10-30 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50b397e1-7e3b-321d-b428-4289deb2ba13 | -5.74904 | -45.56754 | 2024-10-30 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4babb9eb-2fd6-369d-8fcc-acc46e6904f1 | -5.66361 | -45.20538 | 2024-10-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16b78614-20cd-325a-b65e-b79e82446039 | -5.47824 | -45.51709 | 2024-10-30 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5fd46641-ebff-30a2-9de5-c7be885ac667 | -5.4638 | -45.50034 | 2024-10-30 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b3d181ec-b702-32a9-a520-4efa4f0c76e6 | -5.46324 | -45.50385 | 2024-10-30 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d8f9e56d-d004-3090-9a07-1cbb42509a31 | -5.46046 | -45.49981 | 2024-10-30 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1b4d9d7b-3a99-38a9-a6c8-e732e763e68e | -5.45991 | -45.50333 | 2024-10-30 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cbd15c39-7b90-3e6c-8259-eab5055ae063 | -5.42354 | -45.32489 | 2024-10-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 40a40e9a-580c-3080-b242-bfad247afadf | -5.41015 | -45.15123 | 2024-10-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 403635dd-5205-31dd-aa82-78b5384aff0a | -5.40683 | -45.15071 | 2024-10-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 09d79ba2-fc9b-31da-944a-842c48af3f6e | -5.32954 | -45.55151 | 2024-10-30 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae31a771-cd59-3ea5-af3c-54fe1d82bff6 | -5.29786 | -44.93731 | 2024-10-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a563bef-a9e1-3940-a171-2255f398b7ae | -5.29731 | -44.94077 | 2024-10-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dfd51b9c-ea3d-3352-ba4e-2a2fb0f160ba | -5.29456 | -44.93678 | 2024-10-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6f5888f-0aa7-307c-96b5-962c5c7de829 | -5.29401 | -44.94025 | 2024-10-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7b45033-1441-342f-a90f-d748c32f1440 | -5.25872 | -45.33412 | 2024-10-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6851d72-298f-320f-ba3e-f17a588b7983 | -5.22125 | -44.90408 | 2024-10-30 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8208c499-1536-3ca8-b83b-1fcbbdb76660 | -5.19483 | -45.62774 | 2024-10-30 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ad6dd5b-18c0-339a-9f20-f584661d8a9b | -5.10779 | -45.70555 | 2024-10-30 04:19:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9d55dc60-1cb3-3859-98ee-f8571b8935b5 | -5.09115 | -45.42671 | 2024-10-30 04:19:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a53685e2-d7e3-3711-9d89-466e767dfd9b | -5.36169 | -45.88161 | 2024-10-30 04:19:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 94038291-6848-3f2f-a70d-9b56ff25c838 | -5.28939 | -46.3302 | 2024-10-30 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f7b5271-b1a0-32c7-ba89-af73fda93304 | -5.27056 | -46.24776 | 2024-10-30 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 850e4209-2690-3481-b0df-73eb1a62b041 | -5.26997 | -46.25145 | 2024-10-30 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 164b2fab-eb89-30cb-ad87-e51dbd2c31c2 | -5.17228 | -46.13766 | 2024-10-30 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b7dca94b-910a-3a5f-8187-2a8e7974dc37 | -5.16761 | -46.03592 | 2024-10-30 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 740dad61-9bde-3e3f-b35d-63a234ddea6c | -5.16691 | -46.19341 | 2024-10-30 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35162779-124a-3ad0-9741-74c8a4a62745 | -6.43899 | -45.957 | 2024-10-30 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f76efde3-14b0-3109-920b-6d87ae13d8f2 | -6.33624 | -46.02529 | 2024-10-30 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19dc6b74-f2e2-3188-9bad-0e202e1dd8b5 | -6.14895 | -46.53416 | 2024-10-30 04:19:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f64a2341-2b21-3858-8908-394bb65fad2d | -5.81398 | -46.27667 | 2024-10-30 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fd3e2cdb-e706-3684-87ed-8c25caae1474 | -5.6915 | -46.47318 | 2024-10-30 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32d08e1a-d986-3953-b436-e674dbb24c88 | -5.69042 | -46.30268 | 2024-10-30 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fbeb0fef-acad-3363-a6eb-fbd8018ad8c3 | -5.65606 | -45.92109 | 2024-10-30 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0434b8b8-69a0-3d4d-99c8-52971681042e | -5.65269 | -45.92056 | 2024-10-30 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec2731d7-33ea-397c-be65-d16148bbc169 | -5.64956 | -46.38337 | 2024-10-30 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b948e819-f68d-320f-b4e0-666a459c79b9 | -5.59968 | -46.25475 | 2024-10-30 04:19:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa709f4b-1613-3f0c-aeb5-d0a43a229d2d | -5.58496 | -46.36945 | 2024-10-30 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9982c604-a8a1-3d71-bb84-6bbfa30bb163 | -6.8715 | -46.42967 | 2024-10-30 04:19:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0518bda5-b60e-3fdd-96be-e0534ce62b36 | -6.83898 | -46.07938 | 2024-10-30 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23f73216-c0d9-3765-95cc-17122a1f52df | -6.83563 | -46.07886 | 2024-10-30 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d344ecf4-93af-3926-9dfc-133cc7d007b7 | -6.82875 | -46.30706 | 2024-10-30 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8c639296-5674-3361-a666-3fa3690d3fcb | -6.68613 | -46.4936 | 2024-10-30 04:19:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 83b57ae0-9599-39b2-8d2c-766286ffa222 | -6.53012 | -45.9458 | 2024-10-30 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5c0cffe9-020a-35db-9fc1-0645fbe39aa5 | -7.23599 | -45.52826 | 2024-10-30 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4b3eafd8-226b-319e-9df5-75c485ee17ad | -7.23543 | -45.53175 | 2024-10-30 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d54de497-d0a7-328f-8ea0-6d14053d310f | -7.23212 | -45.53123 | 2024-10-30 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73994ce6-8ebe-32f7-aaa4-5ff58cff4d62 | -7.18517 | -45.48447 | 2024-10-30 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 417927c1-3c7f-31f3-a6aa-587f5666ebd4 | -7.18461 | -45.48796 | 2024-10-30 04:19:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ebd7cfea-1c81-3999-85a6-a2ec21b20404 | -7.06486 | -45.66246 | 2024-10-30 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe549e2e-61ae-3de1-9515-f5447073b802 | -7.0643 | -45.66596 | 2024-10-30 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 831b47fe-fcff-3439-aecf-4219573c3407 | -7.06097 | -45.66544 | 2024-10-30 04:19:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84b472f9-15e0-316f-9673-8197dd520c7f | -7.55572 | -46.12909 | 2024-10-30 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 354631e2-bb25-3f67-839f-219e093ef0fc | -7.55237 | -46.12856 | 2024-10-30 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| b9410925-f3db-3977-bb3a-b737e2d4884a | -7.4346 | -46.62482 | 2024-10-30 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2fb39a8-1371-3528-90e6-0ce175560eba | -7.43121 | -46.62427 | 2024-10-30 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| de6ea373-f877-34dc-8309-8ef22bce092e | -7.39597 | -46.57689 | 2024-10-30 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17f8f67b-b42a-3144-b8fc-ad16690699d9 | -7.38487 | -46.53762 | 2024-10-30 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b06c24e6-b615-39be-af17-1096edd1e5f4 | -7.3809 | -46.54073 | 2024-10-30 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7eff7c71-d9f2-3883-a852-4de3360ed644 | -7.24962 | -46.57203 | 2024-10-30 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d6db6f30-dde9-32a3-bf4c-6ae29bedaba0 | -7.24622 | -46.57151 | 2024-10-30 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d23fd578-2538-3b1b-85e4-0ddf3f610245 | -7.24563 | -46.57517 | 2024-10-30 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f69cbac-ebbd-3cb8-aa18-43c11083e6bd | -7.24504 | -46.57884 | 2024-10-30 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a900f76-8409-3ca9-b374-4efcd5f583bc | -7.24224 | -46.57465 | 2024-10-30 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 29a7f29e-5ed1-3c5a-af38-7b36d0de64e2 | -7.22351 | -46.58284 | 2024-10-30 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9501a7d-840f-3232-909c-e18294dc0e66 | -7.22262 | -46.38493 | 2024-10-30 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c99cc770-ef97-3ee2-8213-a494250165d7 | -7.19825 | -46.29935 | 2024-10-30 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| af28eff5-3013-38f9-bdd3-2ac30ad3f4af | -7.1768 | -46.3254 | 2024-10-30 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55b99ffb-385a-3bc8-ae9c-eb5ccc15682b | -7.17284 | -46.32853 | 2024-10-30 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2904f90-c59e-3520-b3ec-c2b62743b605 | -7.13081 | -46.63288 | 2024-10-30 04:19:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32779663-73a0-3393-80b0-97f207366327 | -7.10726 | -46.4558 | 2024-10-30 04:19:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75f91ddf-856f-31fe-9f1c-2485acc0f76c | -1.84142 | -47.10134 | 2024-10-30 04:19:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07e579d9-25fd-3daf-b563-54f28b66bae9 | -1.83775 | -47.10078 | 2024-10-30 04:19:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8765240b-1473-3668-a830-c46c81843d6f | -1.59873 | -47.14157 | 2024-10-30 04:19:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 11a35b99-d284-34e9-a0a2-4c963ead999a | -1.25939 | -46.12636 | 2024-10-30 04:19:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 13edc7db-11a2-34e7-aef1-c4b368c9d549 | -3.3 | -47.03073 | 2024-10-30 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0110ba8-6f74-3591-8f8a-073da8bd2732 | -3.2249 | -46.4983 | 2024-10-30 04:19:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c20c3b93-d977-3420-a049-d2b03cd659b1 | -2.82272 | -46.60773 | 2024-10-30 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 46fd71f8-b11c-3c15-aec9-72cd4e7b1e3e | -2.61404 | -46.14395 | 2024-10-30 04:19:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e543fec7-beb9-30e6-a322-97a67d442b8a | -2.56351 | -46.11294 | 2024-10-30 04:19:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| beeb466f-2bb2-3998-86cf-579e2dbbc9e4 | -2.55944 | -46.11625 | 2024-10-30 04:19:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 232c93a6-470b-3950-bba4-aeb6f21e1f34 | -2.42286 | -46.70363 | 2024-10-30 04:19:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e6ed9f3b-e485-3968-b05d-8f0b3d713953 | -2.42221 | -46.7077 | 2024-10-30 04:19:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bf1496c6-3098-3087-9d31-d810608b1296 | -2.41994 | -46.69901 | 2024-10-30 04:19:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 930418fa-57e5-338f-9939-d993039dfaa7 | -2.41929 | -46.70307 | 2024-10-30 04:19:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d4bb133-3b7c-3f08-a419-e1fa07b6e4af | -2.41864 | -46.70713 | 2024-10-30 04:19:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1eb2519-9676-319c-bad5-9f47735e8488 | -2.41638 | -46.69844 | 2024-10-30 04:19:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfd52b2c-51b9-3b64-a842-86dff2de9c95 | -2.41572 | -46.7025 | 2024-10-30 04:19:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 131a2621-831d-383d-9187-18fc52167895 | -2.37152 | -47.23502 | 2024-10-30 04:19:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36e0b4ac-9a1c-3d94-8736-0d7ec88ad369 | -2.33993 | -46.47324 | 2024-10-30 04:19:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d73b17f-7cd9-3519-923c-354e31d89123 | -2.33929 | -46.4772 | 2024-10-30 04:19:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4386e33e-4704-3165-8516-419248aad835 | -2.3379 | -46.64511 | 2024-10-30 04:19:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8518edd9-b0ca-332c-8cc5-a4947e348067 | -2.33726 | -46.64916 | 2024-10-30 04:19:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb4904bc-5397-36a8-9ffe-b7cdb2a7494b | -2.33703 | -46.46873 | 2024-10-30 04:19:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4f34bdc-a763-3ed0-8923-1e8f3cf57486 | -2.33493 | -46.59514 | 2024-10-30 04:19:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bfaaa2d2-5cbf-3afc-99c3-16d35bce7122 | -2.31782 | -46.72514 | 2024-10-30 04:19:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b0c78d6-2e78-3690-a8b9-5bd19515dc7d | -2.26903 | -46.10315 | 2024-10-30 04:19:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README39.md)
