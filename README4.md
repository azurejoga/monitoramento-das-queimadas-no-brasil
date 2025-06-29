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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe94b001-6fb6-34f0-b763-69782e09608d | -12.1091 | -54.6702 | 2025-06-29 00:41:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d8f639e-d999-39c2-9429-e57e0631036b | -13.0165 | -53.418701 | 2025-06-29 00:41:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7012ab82-8904-3f7f-8231-f9261068fbe2 | -5.0866 | -48.357201 | 2025-06-29 00:41:00 | METOP-B | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aca70b02-424f-34c9-af5f-17d2cd4812c3 | -12.6261 | -54.213799 | 2025-06-29 00:41:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5e82d7a2-193a-3b4c-a3d8-4cf86b67192f | -17.397301 | -42.622398 | 2025-06-29 00:41:00 | METOP-B | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 51ef73b5-955f-3300-a53a-50c8ed2c5bcf | -12.5073 | -58.338501 | 2025-06-29 00:41:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 046ecdc4-9b21-35b9-82c7-5484fc3f90cd | -7.301 | -55.313301 | 2025-06-29 00:41:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69aff4bf-27a8-396c-a035-046639addc8a | -11.5352 | -52.7883 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 82f5e7c2-b689-305f-8ea0-bd903ef682b8 | -10.5501 | -52.0424 | 2025-06-29 00:41:00 | METOP-B | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3bf87a3e-bca0-3863-9857-f0fbb9301398 | -11.2691 | -52.7519 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b3f8cf6b-a32e-3076-8670-cd474a6d3f09 | -10.3575 | -57.498901 | 2025-06-29 00:41:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 97af266d-cf31-38dd-a03a-32604ebc9022 | -22.4091 | -46.822201 | 2025-06-29 00:41:00 | METOP-B | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b4330b35-0d6f-37ac-8a3e-d56711a0e91d | -9.7146 | -56.181099 | 2025-06-29 00:41:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4c95f857-a833-3838-8260-9a46a8b7b15a | -10.9279 | -44.1717 | 2025-06-29 00:41:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5b76271d-941e-3bc2-b857-43a4586c5951 | -8.3655 | -51.0756 | 2025-06-29 00:41:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 99c8dc9e-a760-342c-a2d1-5c4b8fea6585 | -11.5368 | -52.795399 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cc72ada5-6949-32a8-aece-ff07cc3168d9 | -9.7031 | -56.1758 | 2025-06-29 00:41:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f4144e44-d5d5-3341-a82c-5b7f4658823a | -11.2757 | -52.735199 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 41c5e835-4777-3b3d-a471-d0d7b43e93cc | -9.0878 | -59.4814 | 2025-06-29 00:41:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 985b4258-fdd7-3cb8-98f2-028219538822 | -9.1179 | -59.041599 | 2025-06-29 00:41:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bb8a2a55-7cc6-3028-8d47-b7c9fa94c38d | -12.9857 | -54.681999 | 2025-06-29 00:41:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b60b401-2e77-3796-85b7-d4fcb31cb70f | -12.9841 | -54.674801 | 2025-06-29 00:41:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b313b162-0415-3f4a-aad1-49d1ed009035 | -8.3753 | -51.073299 | 2025-06-29 00:41:00 | METOP-B | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b948eea9-0dbd-3eae-94dd-e54f555f3eca | -12.107 | -54.567101 | 2025-06-29 00:41:00 | METOP-B | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 435abc28-fab9-30ea-9f04-1b6a097a9229 | -9.7227 | -56.171501 | 2025-06-29 00:41:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab58aba1-ec77-3cb2-aa80-0c3780e0267f | -10.5679 | -52.030201 | 2025-06-29 00:41:00 | METOP-B | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4c849a6b-9159-3aa6-87ce-817f350a8c51 | -10.306 | -57.113602 | 2025-06-29 00:41:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 15ac03a3-6ad6-3ae3-b1c3-3f335698116c | -11.5482 | -52.800301 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 699bd5de-8e2e-3bb5-b14f-7448c2d3c0f3 | -11.5564 | -52.790901 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3efb857-dd80-3230-8d9f-245adacba60b | -21.021999 | -50.169701 | 2025-06-29 00:41:00 | METOP-B | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9768a8a0-f6f0-3fd6-af3e-5a90b89e55bc | -10.0374 | -54.331299 | 2025-06-29 00:41:00 | METOP-B | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b910e8d3-7790-3700-be37-47c97c4a8331 | -10.3477 | -57.500999 | 2025-06-29 00:41:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8e492490-a9e6-3b89-a4de-97dab8a611e0 | -9.1158 | -59.031799 | 2025-06-29 00:41:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 48aca23e-0fb1-38fc-9f6c-197aad08bf68 | -11.5254 | -52.7906 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9b0f40af-1545-31b8-b72a-9981d6e08ef8 | -9.0856 | -59.471001 | 2025-06-29 00:41:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 44a4f287-9602-3f97-bc84-33e538e022c2 | -11.5189 | -52.761902 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dc715143-a922-3926-8e48-707dbcd9949d | -10.2952 | -57.015202 | 2025-06-29 00:41:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bae6118b-5bbc-34bc-a159-555a91ebca46 | -22.3993 | -46.824902 | 2025-06-29 00:41:00 | METOP-B | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 743a080a-1ad6-3c43-b072-ce0240226f0e | -12.6137 | -57.861801 | 2025-06-29 00:41:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6181f95f-2d6f-315f-a7c9-72bb5b90dccb | -10.5662 | -52.022598 | 2025-06-29 00:41:00 | METOP-B | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f28ae5ac-e58a-39b0-b94a-6bf856693319 | -11.563 | -52.7743 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 39f219cf-2bdc-39a5-b4e2-e1cc5dd8970f | -11.5499 | -52.807499 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 63ed09db-b1a6-3ec4-9afa-8cd4f759a08f | -11.5467 | -52.748001 | 2025-06-29 00:41:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| deedfb37-f4aa-3271-ac59-0614d1852e41 | -6.6301 | -47.295399 | 2025-06-29 00:41:00 | METOP-B | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 43f94fa7-b703-3b9b-aea2-f6f0fbc05411 | -12.5094 | -58.3484 | 2025-06-29 00:41:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6d7ad46a-ffc4-363e-99c2-f1840830ddc7 | -12.4909 | -58.457199 | 2025-06-29 00:41:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 695f3bde-16bb-3cc9-858c-f47ea8515d6a | -10.5599 | -52.0401 | 2025-06-29 00:41:00 | METOP-B | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6905f7b7-5a47-3304-9b1b-d49b58af29be | -10.96 | -45.095402 | 2025-06-29 00:41:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 57c3f09a-ddaa-3e9d-aef0-9f28450870a7 | -10.5576 | -52.0499 | 2025-06-29 00:50:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 170.1 |
| e97444e7-4f03-3b2d-a9c5-1693f3ed95df | -10.9815 | -45.0874 | 2025-06-29 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| f543d229-caa9-3f74-ac15-b265ec88dd4a | -6.634 | -47.274 | 2025-06-29 00:50:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| f07693de-e3c7-3f62-95f4-6a536b6624b3 | -22.4056 | -46.8205 | 2025-06-29 00:50:00 | GOES-19 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 66.6 |
| ebdca10b-bae7-3b37-aef2-b9c5808d2c0f | -17.3844 | -42.6235 | 2025-06-29 00:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 58.3 |
| f43caacf-0ffa-3e5f-afb3-9401a89814fe | -11.0168 | -56.2659 | 2025-06-29 00:50:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| d06ee34c-e2d8-31a5-ae7b-a75422ddf0ec | -10.539 | -52.0307 | 2025-06-29 00:50:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| e0e14ffe-0d0f-3225-91a2-6f926ff955a5 | -10.9811 | -45.1104 | 2025-06-29 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 262.4 |
| 00d48112-c594-3fce-a457-6cbe184b72e7 | -11.2666 | -52.7318 | 2025-06-29 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 6d02550a-c82b-3196-a9cd-51374710e265 | -11.0166 | -56.2859 | 2025-06-29 00:50:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 105.7 |
| ea7eb5bf-8fdf-391f-a5a7-0888ec093ee6 | -6.6153 | -47.2754 | 2025-06-29 00:50:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 1159be75-3e85-3cb9-9d74-b3349575e144 | -10.9808 | -45.1335 | 2025-06-29 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 72b96186-5230-3c1b-9c53-c66f101b0c48 | -10.5387 | -52.0517 | 2025-06-29 00:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 0b32b10e-227f-36d7-9735-8b0a12e84b59 | -17.4045 | -42.6186 | 2025-06-29 00:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 104.9 |
| f0667cb0-b34a-3ad1-a60a-2271dcf46bce | -10.5765 | -52.048 | 2025-06-29 00:50:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 16d67ccb-cf96-38c5-b7f6-3903aef223dd | -10.5579 | -52.0289 | 2025-06-29 00:50:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 154.0 |
| 16619196-9368-31bf-abc8-9a63da225934 | -11.0003 | -45.1078 | 2025-06-29 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 2626efb2-5cbd-372e-8bee-551582b64ef8 | -11.0356 | -56.2644 | 2025-06-29 00:50:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 7cde9c0c-9b1b-38d6-ac67-870cf7ea9b2c | -10.962 | -45.113 | 2025-06-29 00:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 129.3 |
| f382efd8-c740-396b-b8eb-89c34311fe19 | -11.2664 | -52.7527 | 2025-06-29 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| ab8be110-3fd5-3b70-ac7d-70c76fd3772c | -11.0354 | -56.2844 | 2025-06-29 00:50:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 141.2 |
| faa6cce6-2eff-356a-b985-09447fa11a5f | -11.0166 | -56.2859 | 2025-06-29 01:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 1bc7dcf7-df0f-36a6-864a-fe8e6df695ab | -11.2666 | -52.7318 | 2025-06-29 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 2cf6e164-d25f-316b-8efe-e726430dc3f5 | -11.0354 | -56.2844 | 2025-06-29 01:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 135.2 |
| 7f799a4f-d3aa-3554-9df0-86cecc933260 | -17.3844 | -42.6235 | 2025-06-29 01:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 4eb54c43-e137-3e9a-b1eb-01d286a84a78 | -17.4045 | -42.6186 | 2025-06-29 01:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 98a9949f-0c88-3923-b9c5-f7d7156445fd | -10.962 | -45.113 | 2025-06-29 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 7562a6f0-f055-36e7-8654-a8b73d8d9134 | -10.9815 | -45.0874 | 2025-06-29 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| ca03e546-0739-3ddb-ac25-be7e565ff9c0 | -10.539 | -52.0307 | 2025-06-29 01:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 3e7dbdb6-3142-3695-a655-a0cc51879731 | -11.0356 | -56.2644 | 2025-06-29 01:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 579bfe9b-4a67-38c0-9721-171c6a1d1868 | -11.0168 | -56.2659 | 2025-06-29 01:00:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 72ba49aa-3bee-311b-9a94-ce547e9bb382 | -10.3467 | -57.5108 | 2025-06-29 01:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 687cac1d-94bc-32ea-a9e9-cc359d3e837d | -6.634 | -47.274 | 2025-06-29 01:00:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| 08e28a78-0cc2-3ec6-8152-f7e69e6b56dd | -10.9811 | -45.1104 | 2025-06-29 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 295.8 |
| 52d59830-b3cf-3b42-afc4-de15ca2449c6 | -10.5579 | -52.0289 | 2025-06-29 01:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 162.3 |
| 511f6b36-6244-3597-be4f-6532efadae4f | -11.2664 | -52.7527 | 2025-06-29 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 812deca0-42b7-3190-ad2e-dcde147dfd50 | -10.5576 | -52.0499 | 2025-06-29 01:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 209.7 |
| 0637334e-c1dd-34ae-a4c8-96a4b4bbb5db | -10.5387 | -52.0517 | 2025-06-29 01:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 3ddca5e9-1116-3c7b-b367-e81671e74ca0 | -6.634 | -47.274 | 2025-06-29 01:10:00 | GOES-19 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 44f2a372-4df9-355f-ab56-cb09ade7c7d2 | -10.5765 | -52.048 | 2025-06-29 01:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 6025c577-1f67-3187-acba-97c32d10d6d9 | -17.4045 | -42.6186 | 2025-06-29 01:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 09da8c4b-ea39-36ff-8d21-d2fda502b55d | -10.962 | -45.113 | 2025-06-29 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| f8fa8c2e-3762-3d6e-ae38-8ab92cca2f76 | -10.9811 | -45.1104 | 2025-06-29 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 257.0 |
| 4e4e135e-21c4-3f34-b9b8-64cd9edd47ee | -11.0356 | -56.2644 | 2025-06-29 01:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 40.5 |
| d79be4df-b306-38c1-ac81-5a79c55a8600 | -11.0166 | -56.2859 | 2025-06-29 01:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 87bf1fff-5fe3-34b0-867f-7172484285a4 | -10.5579 | -52.0289 | 2025-06-29 01:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 146.4 |
| cf251f85-42ce-3913-a833-6386982356e2 | -10.5387 | -52.0517 | 2025-06-29 01:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 9d5ff471-f990-3966-8748-26fdfd5ac448 | -11.0168 | -56.2659 | 2025-06-29 01:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| bfc13989-3cf5-386f-8c1c-94b0ef567fb3 | -10.5576 | -52.0499 | 2025-06-29 01:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 205.2 |
| 8e36e67a-c0b1-3d53-a07c-c78dcc729881 | -10.9815 | -45.0874 | 2025-06-29 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| 7cef90a8-b8fb-363b-92cb-a37c352dc7fb | -11.0354 | -56.2844 | 2025-06-29 01:10:00 | GOES-19 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| d65c163f-bfdf-3514-9cf9-08c7b29d73be | -11.2664 | -52.7527 | 2025-06-29 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |


[Clique aqui para ver as próximas entradas](README5.md)
