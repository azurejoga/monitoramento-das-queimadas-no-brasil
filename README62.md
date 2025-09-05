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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 46b2d676-4cdb-3953-9301-806d7995134c | -10.9856 | -46.0007 | 2025-09-05 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 521.5 |
| 51124d56-edcf-36bc-8e99-6ff9917a706e | -10.986 | -45.978 | 2025-09-05 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.9 |
| a93495e8-cef7-31af-af0b-c9ace7064517 | -12.9668 | -54.791 | 2025-09-05 12:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| f60fb5d0-a78e-3c6c-b6a7-e6fa47ce1107 | -6.1519 | -44.8501 | 2025-09-05 12:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 92f086b5-1fae-35ff-9bff-498d0425e20f | -12.9668 | -54.791 | 2025-09-05 12:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 81.5 |
| e207d771-a04a-330e-8860-452f73240c3f | -8.4787 | -45.0932 | 2025-09-05 12:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 35ab986e-6be1-3e8a-8fef-0a760f4afc5d | -10.9856 | -46.0007 | 2025-09-05 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 124.2 |
| e6b11981-6c33-3003-8112-311fb2ddeb24 | -8.479 | -45.0704 | 2025-09-05 12:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 73.2 |
| a9e63c15-0228-3a02-9bc9-8626e90db1ae | -7.8964 | -44.9473 | 2025-09-05 12:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 114.9 |
| b0ce1b6f-9566-3fa8-b222-e8ba339c8ddf | -15.7111 | -46.2281 | 2025-09-05 12:10:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 96.3 |
| f9c6dd0d-e2ca-3182-a6ef-a5a0b81c219f | -7.8923 | -45.2893 | 2025-09-05 12:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 74.2 |
| fa0cb9e7-246d-3b4b-a74e-3476d35ab080 | -8.0988 | -45.3371 | 2025-09-05 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 7d84c34f-7cd7-3ac5-827b-7e426b44b772 | -7.8923 | -45.2893 | 2025-09-05 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 95.3 |
| dc1f37b5-f91c-3bd6-a094-ad06fb1edb9e | -8.4787 | -45.0932 | 2025-09-05 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 7e37aa65-61a5-3b84-88ff-08aea13bad7a | -8.479 | -45.0704 | 2025-09-05 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 92.1 |
| d8304b0b-f95e-3574-82e9-4c237ef6862b | -15.7558 | -53.6746 | 2025-09-05 12:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| a3814024-d552-3eed-b120-b9ee51f7dfdb | -6.2609 | -43.2727 | 2025-09-05 12:20:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| b78936ca-c82e-3b26-a003-566ca73c0e1a | -12.9665 | -54.8116 | 2025-09-05 12:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 6d670d16-1e41-32ca-88eb-69a700b42607 | -12.9668 | -54.791 | 2025-09-05 12:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 22412ff3-b8c9-34a3-8270-3bb53ce0860b | -15.3254 | -52.7394 | 2025-09-05 12:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| c6776717-9cff-38f3-81d9-def168e87b7a | -15.7561 | -53.6535 | 2025-09-05 12:20:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| c6284494-5e23-3cd7-b0f7-a7baf0a9c829 | -7.8964 | -44.9473 | 2025-09-05 12:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 69.4 |
| a2851dbd-9900-3f58-9bae-a3e51dc395a2 | -15.1961 | -52.3746 | 2025-09-05 12:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 76d569a1-ea7a-3010-b8e4-832a9f24d985 | -10.9856 | -46.0007 | 2025-09-05 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 150.3 |
| c50f358a-9d5f-3584-91ee-7c9ffa44a84a | -15.7182 | -53.5954 | 2025-09-05 12:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 150.8 |
| fd5d07b4-6e17-3c41-9a48-b90c336cc642 | -13.8655 | -47.951 | 2025-09-05 12:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 61231af2-32ef-3210-a925-4e7c286b8395 | -9.7105 | -48.9853 | 2025-09-05 12:30:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| d2aa014f-0795-31a4-a913-1da6f24f27c3 | -6.2609 | -43.2727 | 2025-09-05 12:30:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 3a176ada-4147-3a1c-ba03-72ad2f6e08fb | -13.884 | -47.9929 | 2025-09-05 12:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 80de0652-fe2e-3042-b221-9587c84c971f | -8.479 | -45.0704 | 2025-09-05 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 34725cd1-dee0-3bcb-b7c2-95d8dae21e24 | -8.9037 | -45.7747 | 2025-09-05 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 102.8 |
| bda3a650-30b4-32f0-a051-cd0ffcd21b8b | -8.8848 | -45.7767 | 2025-09-05 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 62.4 |
| f51e57ac-bd4a-30d7-886c-941086202cda | -10.0815 | -48.0737 | 2025-09-05 12:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 20952ea3-1600-3b03-9f2d-aef3a3b6b964 | -13.8651 | -47.9734 | 2025-09-05 12:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 130.2 |
| e2465582-b301-3cb9-b955-7338e6d99b23 | -7.8923 | -45.2893 | 2025-09-05 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 65.8 |
| deaf13ed-7d18-3158-b828-ec6bc8636421 | -13.8845 | -47.9705 | 2025-09-05 12:30:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 168.7 |
| f15a4f33-5c52-3dcc-9c4e-cb3338dcd0ce | -12.9665 | -54.8116 | 2025-09-05 12:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 622942a9-e0cb-3b98-ac3d-d0dc00690ab2 | -8.0988 | -45.3371 | 2025-09-05 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 7f74fdd1-fe1b-3a34-807e-aa2bc3638433 | -5.5884 | -45.1185 | 2025-09-05 12:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 682abef0-ffa7-39cf-8962-f6f31343bb6e | -8.4787 | -45.0932 | 2025-09-05 12:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 246739e0-9dbe-33ed-9468-844a9da820b2 | -6.1519 | -44.8501 | 2025-09-05 12:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| f08c44e4-20e7-342c-a8f0-00d58b376e32 | -11.338 | -50.2968 | 2025-09-05 12:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 2e981718-da37-3cc3-b13a-767a7784efb8 | -12.9668 | -54.791 | 2025-09-05 12:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 124.1 |
| 9c82b093-aaed-3ab6-85c0-fd1f7dec6137 | -10.9856 | -46.0007 | 2025-09-05 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.4 |
| f71d9c7a-f6b6-3073-a061-31bbc68b126e | -15.7182 | -53.5954 | 2025-09-05 12:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 311.9 |
| c073e3b6-84cd-340c-bba3-7684fc0830f0 | -15.7374 | -53.6139 | 2025-09-05 12:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 27cbffed-e121-3991-95d9-20a21b7af213 | -15.7561 | -53.6535 | 2025-09-05 12:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 2a010a21-115f-3950-b1d4-1d0ee8f0f795 | -16.4624 | -45.2402 | 2025-09-05 12:40:00 | GOES-19 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 81.7 |
| e276df55-f467-3310-ba3f-2e58666494c9 | -15.7558 | -53.6746 | 2025-09-05 12:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| c1cd18d8-1418-3ea3-8cf7-e34d057abd09 | -6.1519 | -44.8501 | 2025-09-05 12:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| be5d264e-0fa2-3941-83a1-d74808079b9b | -12.9668 | -54.791 | 2025-09-05 12:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 155.6 |
| ba7aaa71-abc2-31e1-be8f-2bb1e7e71c27 | -13.8651 | -47.9734 | 2025-09-05 12:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 0d896ca9-afae-3b25-bd38-bb95824fda73 | -8.9037 | -45.7747 | 2025-09-05 12:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.1 |
| c241d43d-2c65-35b0-962d-59159a7f65b3 | -13.8845 | -47.9705 | 2025-09-05 12:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 173.9 |
| 71f88e69-2f61-31fb-8f8d-18b049ec88e8 | -6.7994 | -45.659 | 2025-09-05 12:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| fdb0b9d4-1d24-3825-a7f4-3b1f9b0c26fd | -12.9856 | -54.8096 | 2025-09-05 12:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 62b0606d-d367-324a-b9d2-7d97f6d1f171 | -15.7179 | -53.6165 | 2025-09-05 12:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 149.2 |
| 9ec4bcaf-5f70-357a-97da-1a7b3e3582db | -14.0691 | -53.9892 | 2025-09-05 12:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 42b2f0fc-e561-3adb-9ed3-29bbc536b131 | -5.9844 | -44.7489 | 2025-09-05 12:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 98.3 |
| dbeaabee-ba3a-3763-9a2a-0b8462ad2b20 | -8.0417 | -45.3882 | 2025-09-05 12:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 08502372-1798-3f63-89cd-6ff2ea75af78 | -7.8923 | -45.2893 | 2025-09-05 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 101.7 |
| e81ca89b-f1e5-3c18-9add-61fa54f4b660 | -8.479 | -45.0704 | 2025-09-05 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| ba222287-04bd-314e-a0aa-d734b145077b | -15.6988 | -53.598 | 2025-09-05 12:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| b2b32c34-cb13-39d7-b7ef-e169c3ce229e | -8.0988 | -45.3371 | 2025-09-05 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 0bd668c2-2dbe-335e-a227-fad2fddcde7b | -6.2609 | -43.2727 | 2025-09-05 12:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| d1c61deb-a6c4-3407-b07f-c7448b8326ff | -13.0044 | -54.8282 | 2025-09-05 12:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| f33b29a1-aef9-321b-960e-71607292a720 | -13.884 | -47.9929 | 2025-09-05 12:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 76907b70-5f25-3205-a188-b6a9906a2b21 | -12.2535 | -50.1464 | 2025-09-05 12:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| fda65188-d172-31a7-b801-11e6a699ca49 | -7.8964 | -44.9473 | 2025-09-05 12:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| c71e8e57-b53a-3b15-82d9-56d79f05b5e5 | -9.7105 | -48.9853 | 2025-09-05 12:40:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 09d57baa-a20f-3961-8954-4e6b8b6aca04 | -12.9665 | -54.8116 | 2025-09-05 12:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 148.2 |
| 0f2feedb-6358-3ecf-a344-367ccdfe7016 | -5.9846 | -44.7261 | 2025-09-05 12:40:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 8d29c6c5-bb5b-3f03-bc16-df3ee1ba9c1b | -13.8651 | -47.9734 | 2025-09-05 12:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 121.8 |
| 351cd3b7-ff99-3e74-a13b-0966253dede6 | -9.7105 | -48.9853 | 2025-09-05 12:50:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| a17ed603-0e86-3f7c-aafc-c0214168fdf9 | -6.7994 | -45.659 | 2025-09-05 12:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 8cab1dce-42c6-3987-9653-ce4cf83384c2 | -9.6916 | -48.9872 | 2025-09-05 12:50:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 55.3 |
| ad5a221e-57a3-3b31-ae47-8e09b8ff656e | -8.0988 | -45.3371 | 2025-09-05 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| b2cc080c-ac7f-3d79-bfb0-d62ee81e7e4d | -8.479 | -45.0704 | 2025-09-05 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 5dcb81b7-ded4-3729-b395-bb9660edcb0b | -8.3458 | -48.2916 | 2025-09-05 12:50:00 | GOES-19 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 5d7857b1-f4d1-31e5-a2d9-219b6d663864 | -8.9034 | -45.7973 | 2025-09-05 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 7f634139-62b9-33bf-b34b-2537381ada8e | -7.8964 | -44.9473 | 2025-09-05 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 92.0 |
| f07e1d8f-e218-3f99-8d34-90b0f1bb1c60 | -8.9037 | -45.7747 | 2025-09-05 12:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 99f0cd50-67aa-3da1-9993-123e18757430 | -15.6988 | -53.598 | 2025-09-05 12:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 511a2a15-a11c-353f-a2f1-5b03a51d6b51 | -13.8655 | -47.951 | 2025-09-05 12:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 66.8 |
| f084d8d2-9910-374a-a21e-9941dfbfcd77 | -12.9665 | -54.8116 | 2025-09-05 12:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 159.4 |
| 375dd662-d380-3578-a870-6207d0fcc47d | -6.2421 | -43.2743 | 2025-09-05 12:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 363b07b2-b7d3-3ee7-a799-e18b4a7b8c6b | -6.2609 | -43.2727 | 2025-09-05 12:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 68586d2e-f8fb-3f3f-8508-fef325116dee | -8.4294 | -47.5617 | 2025-09-05 12:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| b0f5250f-1f14-3afb-88c0-bbbec5268abf | -15.7374 | -53.6139 | 2025-09-05 12:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 00ffb385-0178-39f7-98b6-eaa4287827a0 | -6.1519 | -44.8501 | 2025-09-05 12:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| c67ed73a-cb47-3a8e-812e-fa4598829d08 | -12.9856 | -54.8096 | 2025-09-05 12:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 94136fec-210a-35a0-8098-9f5b3c6f19aa | -8.4297 | -47.5397 | 2025-09-05 12:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 9289dd08-e6b0-39e1-919d-ad730dca468f | -10.9856 | -46.0007 | 2025-09-05 12:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 72bedd74-c88d-3535-9fd2-338cde34d9d6 | -10.7688 | -45.2769 | 2025-09-05 12:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 7ff07d5d-db7c-3e72-abb5-7d252107a562 | -13.884 | -47.9929 | 2025-09-05 12:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 26105427-ac86-3065-ac54-cc8917a07547 | -10.7691 | -45.2539 | 2025-09-05 12:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 65.2 |
| e8a70361-9341-348b-b2e4-603e49dbd8a3 | -5.9844 | -44.7489 | 2025-09-05 12:50:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| b4946f43-0d11-310f-b9c8-2bdacf66653f | -8.4787 | -45.0932 | 2025-09-05 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 63dae805-08b9-35ea-a151-6b53dfa66899 | -13.8845 | -47.9705 | 2025-09-05 12:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 191.9 |
| a877b5cc-f259-379b-8cb3-3e93b6e2ea85 | -7.8923 | -45.2893 | 2025-09-05 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 77.6 |


[Clique aqui para ver as próximas entradas](README63.md)
