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

## Dados Diários - Página 243

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e14e626a-d0cd-3372-a75c-6d273f294497 | -0.3952 | -52.0152 | 2026-10-07 17:40:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 48.9 |
| bc8e073b-423c-3f47-a785-22972db7b259 | -9.5425 | -65.6815 | 2026-10-07 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 3c3f88b0-acf0-344f-9c49-4ba601781a61 | -9.8061 | -64.9979 | 2026-10-07 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 82.5 |
| b700205b-672a-3eca-8ada-f9e3fb0d9c65 | -9.0892 | -67.685 | 2026-10-07 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 7d46880f-4dd8-3d76-a49b-e574b1bc3d5b | -11.2146 | -44.8473 | 2026-10-07 17:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| ab351ebf-c5a8-370c-9614-5294c90b34e8 | -9.1076 | -67.703 | 2026-10-07 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 194981eb-cb3d-31f3-9d8f-beccf21d4835 | -10.9571 | -45.412 | 2026-10-07 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 137.5 |
| c8a01952-c0ad-3a39-9ebc-467f81a5ded6 | 1.8038 | -55.5261 | 2026-10-07 17:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 45f7baa0-ef60-35eb-84f7-e65d648dfbd2 | -9.5124 | -46.8534 | 2026-10-07 17:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 202.2 |
| 4296fc57-89da-3a77-8b12-c20b5d3e3195 | -9.9596 | -43.5045 | 2026-10-07 17:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 6b5e96bd-a282-353a-a114-115410653779 | -9.7126 | -65.0951 | 2026-10-07 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.9 |
| ef1df998-5afa-3c00-bc0a-fce7281749bc | -10.9575 | -45.389 | 2026-10-07 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 153.0 |
| e968e59f-5506-34d6-8793-337dc46c2379 | -10.9762 | -45.4094 | 2026-10-07 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 300.1 |
| ee105283-c64d-3ab5-b40d-c69d701784e9 | -5.7304 | -53.465 | 2026-10-07 17:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 293.9 |
| 93e7a554-2768-3a06-8656-ec06d838af99 | -9.8246 | -65.016 | 2026-10-07 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.3 |
| d13a76e2-80ee-33c1-b744-3871a08fbb95 | -3.2214 | -53.8818 | 2026-10-07 17:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| fbc37b4b-845e-3bbb-8906-59e3c752af92 | -9.8245 | -65.0348 | 2026-10-07 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 520217c8-e97a-3cfb-8c54-6a1c6fad63dc | -11.8508 | -43.5361 | 2026-10-07 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 126.8 |
| c5dbf3ee-c362-3623-befa-7f4cef2204d2 | -11.8315 | -43.5391 | 2026-10-07 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.4 |
| cf6c55a0-328f-3c22-9548-f63f60d301f2 | -2.9819 | -54.0488 | 2026-10-07 17:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 285.2 |
| 6b94b297-56d8-3a93-9ac4-a7fccc384e6d | 1.8768 | -55.7227 | 2026-10-07 17:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| b2e9d8bc-a0a0-3800-9002-331cbabef87c | -9.0802 | -65.3789 | 2026-10-07 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 6e75bb1b-b180-381f-8e2f-2ceb11f2f00f | -9.1076 | -67.7215 | 2026-10-07 17:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 320b883d-44e2-37ab-a798-8e384e7c24b0 | -12.2136 | -44.6758 | 2026-10-07 17:40:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 1891a332-f254-371a-9e03-b486ac41841e | -9.9589 | -43.5516 | 2026-10-07 17:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 531.1 |
| 8a5eded0-3eb1-39d5-b17c-2bdcc356dc41 | -9.6757 | -65.0401 | 2026-10-07 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 82.7 |
| a0a4911c-3a57-380e-a633-9e36e4bdcaa9 | 1.6937 | -55.6263 | 2026-10-07 17:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| a5dd4026-af7f-3fb5-af70-fc18f18e42ee | -5.9835 | -40.9367 | 2026-10-07 17:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 255.1 |
| e1bcd70a-2ebc-371c-8e61-89d369b4a129 | 1.7121 | -55.6261 | 2026-10-07 17:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| e309e05c-0a91-3a0a-9460-197ac5db6802 | -9.806 | -65.0167 | 2026-10-07 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 2b2e3dd1-3468-36f3-87b9-b5e58bf66b3a | -9.8431 | -65.0341 | 2026-10-07 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 71.1 |
| b0ca71d2-e694-39c2-9cdc-71198f3da437 | -2.9819 | -54.0287 | 2026-10-07 17:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 103.7 |
| e8a091f1-d5c8-3dc3-a452-00ccb3efed1f | -8.9495 | -71.553 | 2026-10-07 17:50:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 147.3 |
| a28d7874-9359-3d94-ab85-3f44e0c60e0e | -9.7126 | -65.0951 | 2026-10-07 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 17fa0bf7-0119-3c8f-928e-d2c2811bb588 | -10.4594 | -46.8333 | 2026-10-07 17:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 201.1 |
| 38e03e03-c8a9-336f-a91b-33f3cb8a2ba5 | -1.2922 | -54.5585 | 2026-10-07 17:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| c82d1cca-78c4-3232-9013-a2c4690dfd53 | -3.0192 | -53.887 | 2026-10-07 17:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| e8074c49-2bf8-3b6c-837b-f821ea0a92fc | -2.0447 | -54.3085 | 2026-10-07 17:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 401.3 |
| 0399f834-9f3a-3197-8e51-418ccc08fc2a | -6.5982 | -41.5823 | 2026-10-07 17:50:00 | GOES-19 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 123.8 |
| ba0e7d10-86bb-3c8e-a3bb-2ce5799c9700 | 1.7121 | -55.6063 | 2026-10-07 17:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 45e8a0a0-7d6c-32d6-8250-cffcad0b6df4 | -9.5468 | -64.8196 | 2026-10-07 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 8d64d3ee-c148-31d2-94a9-c8fbd654d6ea | -2.7613 | -54.0941 | 2026-10-07 17:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 520.0 |
| e1bd5257-131d-38af-bcf8-8636773a9326 | -6.6753 | -44.9674 | 2026-10-07 17:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 644ed650-dc0c-36eb-b6f4-82c3f6f4b819 | -11.619 | -43.6196 | 2026-10-07 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 203.3 |
| 1792975a-c16e-3b30-8e2d-f14f23f3994e | -9.7313 | -65.0757 | 2026-10-07 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.5 |
| bd09bdef-2dcf-3575-8088-b578d598cf9b | -11.8503 | -43.5598 | 2026-10-07 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 148.0 |
| db6eade5-2c77-3cfc-bb63-045b09798099 | -9.9589 | -43.5516 | 2026-10-07 17:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 232.0 |
| cd42e242-07c6-3e3d-87ea-68120b1b3d1b | -9.0988 | -65.3596 | 2026-10-07 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 52a39b92-2ff4-3ca4-80e5-e5f2ecb4db70 | 1.7671 | -55.5859 | 2026-10-07 17:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 071a8d6b-e301-3176-81b4-8167b3919c2b | -8.2181 | -46.362 | 2026-10-07 17:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 48a66b93-532d-34ae-bf08-a7c73e61b105 | 1.6937 | -55.6461 | 2026-10-07 17:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 140.5 |
| a1b8f91c-b2f3-3161-b002-133e64f66eb1 | -2.8899 | -54.0912 | 2026-10-07 17:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 1648e395-14b2-303b-a389-ed8eaf6bee2f | -5.9838 | -40.9123 | 2026-10-07 17:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 168.2 |
| 4fc36c8e-56e6-3836-84b9-44df6aa596b1 | -7.7595 | -43.8092 | 2026-10-07 17:50:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 57.1 |
| b5f26425-dd24-346e-8ea0-2bc9b7308121 | -2.8898 | -54.1112 | 2026-10-07 17:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 2fca0f01-a927-37e7-9f1b-84eac34716e6 | -11.2333 | -44.8678 | 2026-10-07 17:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| ef178151-b1cb-3cee-a97f-054a1b07279f | -9.5469 | -64.8008 | 2026-10-07 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 0300561c-0b6f-3947-bf75-1cd1bf08a0ba | 1.7671 | -55.5661 | 2026-10-07 17:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| aaab7fef-c2eb-348e-b4a2-639210aa2ae8 | -7.7174 | -69.8841 | 2026-10-07 17:50:00 | GOES-19 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 109.6 |
| 81a1fac6-5813-3357-96c1-c1594d392562 | -9.6757 | -65.0401 | 2026-10-07 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 90.6 |
| b9f2ca2e-aef9-3b0a-8077-37391278f7d3 | -9.4509 | -45.8271 | 2026-10-07 17:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 6ce7d44b-150a-3043-90da-cd9627579f2b | -4.3045 | -50.77 | 2026-10-07 17:50:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 2beb6dfd-d77d-37ff-9fc5-510bbc61bb8d | -3.0375 | -53.9066 | 2026-10-07 17:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 485.9 |
| 59763df7-d567-30e7-8614-26a099184ed5 | -2.9819 | -54.0488 | 2026-10-07 17:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 211.3 |
| 24569c36-9aac-3494-b9c6-16c03589d20b | -9.8246 | -65.016 | 2026-10-07 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 270c6531-c831-38f2-8310-900589ef97d5 | -11.6946 | -43.6787 | 2026-10-07 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| e0cccff9-e521-375e-a37a-f5bcefbc6c15 | -10.3731 | -45.0306 | 2026-10-07 17:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 218.6 |
| 5cd61c6a-9789-3f17-b67f-62595dd1d5a4 | 1.6385 | -55.785 | 2026-10-07 17:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| d7bc5c06-98d3-3c5a-8654-579237f8174a | -9.8682 | -45.7783 | 2026-10-07 17:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 30852f01-9450-311a-9b0e-f313b55ecf90 | 1.7487 | -55.6059 | 2026-10-07 17:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| c82d9c83-ef9f-3b33-bc70-30371d8cc35e | -0.3952 | -52.0357 | 2026-10-07 17:50:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 52.9 |
| d4f82a92-459a-3bb9-a0cd-7e59334bbcb6 | -9.8071 | -44.7804 | 2026-10-07 17:50:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 3aaa12d3-f141-37a3-bca0-1b0deb8d351c | -2.5124 | -58.0959 | 2026-10-07 17:50:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 3d38eb69-76ca-3015-bc33-6add3fd0b845 | -6.5794 | -41.5841 | 2026-10-07 17:50:00 | GOES-19 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 174.3 |
| 900fd35a-1db9-3df0-964b-f680a6183ded | -5.9647 | -40.9383 | 2026-10-07 17:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 282.4 |
| 67ea0aa0-13c5-37f7-9d35-a5afc14c3b80 | -7.8146 | -45.5009 | 2026-10-07 17:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 73.7 |
| ab402699-a5c6-3487-b7f4-c469ba626852 | -3.2951 | -53.8395 | 2026-10-07 17:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| a36871ce-c082-323d-80e1-d08e0ad8f908 | -9.7312 | -65.0944 | 2026-10-07 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 1f232d9a-4451-3455-a330-a579b3dc98d3 | -9.0987 | -65.3783 | 2026-10-07 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| b186c0e8-dd35-386c-a6f8-9999c00c9094 | -9.9787 | -43.502 | 2026-10-07 17:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 156.5 |
| 84998ad2-846a-3538-814d-eda02bd2b3d3 | -8.8864 | -67.4678 | 2026-10-07 17:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 74.6 |
| ff7fb42f-6ac8-38dd-8135-caaf808c5faa | -16.9203 | -42.1171 | 2026-10-07 17:50:00 | GOES-19 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 136.8 |
| a54a461e-9c13-3e09-9b34-1bddb6fcbde6 | -2.9082 | -54.1108 | 2026-10-07 17:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| eef865b6-82ed-3289-ae8d-3cda665e3ef9 | 1.8767 | -55.7424 | 2026-10-07 17:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| c18dbdea-203e-3bee-a679-689daf7fe0e2 | -0.3768 | -52.0153 | 2026-10-07 17:50:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 4e06842c-9e1d-3a7d-a0d9-5eb45529454a | -9.462 | -67.1002 | 2026-10-07 17:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| eb710d7a-172a-3935-9b49-7f827f0e8542 | -7.6582 | -72.4237 | 2026-10-07 17:50:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 85.5 |
| a4b2bbbe-4653-3e16-9286-8cb401287cfb | -9.9291 | -46.8065 | 2026-10-07 17:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 200.8 |
| 7f83aa95-2840-3866-af42-856119ef0d8e | 1.8768 | -55.7227 | 2026-10-07 17:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| e3597fc5-1135-34be-85c8-0a3d21e54f59 | -2.8164 | -54.0929 | 2026-10-07 17:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 80402c13-1d32-3415-9321-29fb0d5ca06d | 1.6385 | -55.8047 | 2026-10-07 17:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| ecc13315-1e2f-3ea4-856a-ed60e56b7dcb | -11.7143 | -43.652 | 2026-10-07 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 282.1 |
| 5ac77e59-eb7e-3d43-8679-cc044bf609d6 | -9.8245 | -65.0348 | 2026-10-07 17:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 8fb9e13f-ddcc-34ae-b652-13a8a0b221b0 | 1.712 | -55.6459 | 2026-10-07 17:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 6a7fe702-dab2-3d22-87d6-8e927b520562 | -2.5307 | -58.0956 | 2026-10-07 17:50:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 3b78d721-5d27-307a-aa0c-f0e74403cbbd | -2.4578 | -58.0 | 2026-10-07 17:50:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| c055da8f-2547-37af-955d-e17a07789ee7 | -3.292 | -42.2673 | 2026-10-07 17:50:00 | GOES-19 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 114.5 |
| fba91784-af84-3301-af9e-263f806212f6 | -11.7335 | -43.649 | 2026-10-07 17:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 175.9 |
| 841b0d05-0e71-3252-829c-ac647e5da321 | -3.951 | -41.5426 | 2026-10-07 17:50:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 140.0 |
| 489670c7-8127-326a-8671-4261faaedbcb | -9.8685 | -45.7556 | 2026-10-07 17:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 406.5 |


[Clique aqui para ver as próximas entradas](README244.md)
