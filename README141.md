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

## Dados Diários - Página 141

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4655b2f9-9a33-3080-93c1-2f40b939ffe7 | -20.79925 | -51.65512 | 2025-10-05 05:18:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 76bd0402-7c9f-386b-9971-171ea05ee395 | -21.82575 | -47.39072 | 2025-10-05 05:18:00 | NPP-375D | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7b937022-99f1-3a34-bc24-ffe86278a965 | -22.10015 | -46.97237 | 2025-10-05 05:18:00 | NPP-375D | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8b8c9486-fa86-3646-ab94-9e037bd64fc2 | -21.82635 | -47.40179 | 2025-10-05 05:18:00 | NPP-375D | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a2b5d051-0e94-3d4a-b559-702f84ab0c28 | -21.81892 | -47.39024 | 2025-10-05 05:18:00 | NPP-375D | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ecdf69ec-241f-35f3-86dd-b2c1cab001f7 | -22.36724 | -46.88614 | 2025-10-05 05:18:00 | NPP-375D | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f0629499-f49f-3316-9bfb-91c489d7e06e | -21.68774 | -48.42466 | 2025-10-05 05:18:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5fac139-b798-31f4-9748-508e51e9838e | -21.82531 | -47.3962 | 2025-10-05 05:18:00 | NPP-375D | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 3242a821-b4da-3a7b-8702-5f339bb0a269 | -21.82036 | -47.38997 | 2025-10-05 05:18:00 | NPP-375D | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f1191705-4a31-3010-a872-0df7ab6c4628 | -20.7989 | -51.65853 | 2025-10-05 05:18:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 02e554a7-0a80-3095-8cc3-1ebd0202e899 | -19.50525 | -50.37394 | 2025-10-05 05:18:00 | NPP-375D | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d6deaf75-3fa6-31cd-aaef-6134a87bc9e1 | -19.50562 | -50.37024 | 2025-10-05 05:18:00 | NPP-375D | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a38a91f1-f821-3778-8a93-3a5998dfbf82 | -19.516 | -50.37893 | 2025-10-05 05:18:00 | NPP-375D | UNIÃO DE MINAS | MINAS GERAIS | Brasil | 3170438 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e04064bd-05ee-3fc9-8b97-0b0a42745037 | -21.82484 | -47.402 | 2025-10-05 05:18:00 | NPP-375D | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ac2da08d-cc6a-3b77-a79f-f146d6ee58cf | -21.82719 | -47.39049 | 2025-10-05 05:18:00 | NPP-375D | PORTO FERREIRA | SÃO PAULO | Brasil | 3540705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| beecad9e-42a7-3227-9e99-64fe0c3ca108 | 4.35709 | -60.16585 | 2025-10-05 05:31:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00d0e587-2453-3065-8b5d-cc5c5da32a17 | 0.44626 | -50.80231 | 2025-10-05 05:31:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a5bc3e0-21ef-3fd7-85d1-37f0d00a1866 | 3.76053 | -59.68255 | 2025-10-05 05:31:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 481c9684-14f8-3df0-a0f4-9da9d14fd504 | 3.76392 | -59.682 | 2025-10-05 05:31:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0dcc5899-d2ac-3a83-9d48-518cb937c758 | 0.44703 | -50.80703 | 2025-10-05 05:31:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac950cd5-387d-3806-9884-d67b8730da5e | -8.61279 | -54.96889 | 2025-10-05 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47860f26-d7ab-33a7-b949-fb1329f39d40 | -8.61945 | -54.95956 | 2025-10-05 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9970f460-040c-385c-8c8b-9b7a1fcad195 | -7.50842 | -61.38303 | 2025-10-05 05:33:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 70fed445-f8d9-3948-bea8-485dc370f22e | -8.63015 | -55.00117 | 2025-10-05 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 28013a3a-b92a-3175-902e-9928db414393 | -3.81291 | -51.0773 | 2025-10-05 05:33:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 45b428d7-44ce-3975-985a-27fd43e38228 | -7.58385 | -63.35524 | 2025-10-05 05:33:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c30c6a63-ae73-365f-bc40-f5f9d40c96ad | -8.61813 | -54.96951 | 2025-10-05 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b69791a-9dd0-383e-b552-716adbd73fad | -8.61856 | -54.9662 | 2025-10-05 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 887db7d0-c03e-30d2-9b58-fb914ed671a7 | -3.81276 | -53.8394 | 2025-10-05 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ee97fe2-116e-3462-9f39-352f81c9b960 | -2.90138 | -50.7389 | 2025-10-05 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4c1d3f81-1b2e-344f-bc91-b73de0caaa79 | -8.60747 | -54.96812 | 2025-10-05 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ede3d33c-253d-36eb-bf5e-6055591706fb | -8.61323 | -54.96558 | 2025-10-05 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed4e03b8-f2ae-3e67-b1d0-5ff5bcb5ede8 | -2.89571 | -50.73255 | 2025-10-05 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a303cbdb-370c-372c-8962-f7afd4f455bc | -7.5844 | -63.35176 | 2025-10-05 05:33:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b3b38382-2691-3e8c-afd9-4ea83f60082d | -4.57064 | -55.95896 | 2025-10-05 05:33:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5ba5157-9f81-3971-b3a0-b961b5623ca7 | -3.8136 | -51.07267 | 2025-10-05 05:33:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 39817006-2c12-3551-b326-44dbd4c46250 | -8.60704 | -54.97141 | 2025-10-05 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bcb05542-9706-31ad-8cee-fa218f9ff536 | -5.13646 | -60.3872 | 2025-10-05 05:33:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| fa1eec0d-5b06-3b02-b8b5-e4b0c3980dcd | -6.86833 | -63.13274 | 2025-10-05 05:33:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59708c8b-05b0-303c-85a8-6ab3e07c4228 | -2.90216 | -50.73354 | 2025-10-05 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51dbcb9c-0cbd-30b8-b642-986428d08b64 | -2.90051 | -50.73875 | 2025-10-05 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07481ec7-8395-334c-b614-0278d0135ce0 | -2.90133 | -50.73339 | 2025-10-05 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 622b77f9-96e4-3024-8daf-335c577d2e1c | -7.58717 | -63.35576 | 2025-10-05 05:33:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48db2749-ae44-3617-9e36-e07cd4ee93b5 | -8.6079 | -54.96485 | 2025-10-05 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c8f3cda-dd4d-379d-957e-a961b44c8494 | -7.85968 | -61.40194 | 2025-10-05 05:33:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86572d50-69e6-3d8a-9b6b-5bdad20e8651 | -8.61993 | -54.99667 | 2025-10-05 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d68ae0c-8dfe-352f-8b33-d4f38eba44b7 | -2.5192 | -51.93373 | 2025-10-05 05:33:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44fc9804-88b1-3a97-a919-73a574f6f010 | -7.59217 | -63.36725 | 2025-10-05 05:33:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d743082-42e9-361b-b4c6-744c5cd01433 | -8.62569 | -54.99406 | 2025-10-05 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d98a6c78-129c-3d61-8299-40330a97f5e6 | -8.61191 | -54.97555 | 2025-10-05 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33824c1e-a577-3319-ac3d-4468cbef37c6 | -8.61908 | -55.00306 | 2025-10-05 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8134d79-70b4-3fb3-b90e-84949032d703 | -8.61412 | -54.95885 | 2025-10-05 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7dc1d700-c676-35ff-9693-2e3bbfb0b019 | -2.89493 | -50.7379 | 2025-10-05 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a0581eab-6adb-39f6-ba8f-17356d8e6e36 | -3.81481 | -51.07407 | 2025-10-05 05:33:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 14986933-6b8d-3086-86a7-15c4960a2823 | -2.69336 | -54.76998 | 2025-10-05 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef155632-1f5f-3398-8b74-a6b391a6c3e6 | -7.62231 | -61.348 | 2025-10-05 05:33:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c56bbee8-6b0d-3ea9-bb60-2f85fc3716b9 | -2.89488 | -50.73243 | 2025-10-05 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4bd39c5c-eab4-3ae6-82df-aa2c255b0cc3 | -8.62347 | -54.97009 | 2025-10-05 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95550074-6104-3a57-b09b-858f58eef7dc | -6.94787 | -63.10238 | 2025-10-05 05:33:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 460d2a48-d74f-3895-959f-597ca850ee34 | -8.62482 | -55.00052 | 2025-10-05 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76d6b29a-a94f-3dc5-919b-cfa75873b396 | -8.61367 | -54.96224 | 2025-10-05 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bba68ae4-9870-3c99-ab97-37504785dfa8 | -3.77672 | -53.93409 | 2025-10-05 05:33:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a375a3d-483b-3086-b32c-2f59dbecf294 | -8.63102 | -54.99467 | 2025-10-05 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3d350ce-af17-305d-8f48-e820a3b6c526 | -8.619 | -54.96291 | 2025-10-05 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7814dfed-db3b-3c45-96c2-cb49e3301f19 | -8.62079 | -54.99018 | 2025-10-05 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2b108cb-f586-3022-957e-b5f92d37edcc | -3.77271 | -61.75709 | 2025-10-05 05:33:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69fe216a-2b90-362a-b27b-6d9e68e87089 | -7.58771 | -63.35228 | 2025-10-05 05:33:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dea22be8-6be0-37e4-98a6-d37f90b195d3 | -3.81546 | -51.06948 | 2025-10-05 05:33:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 342e3668-4132-300e-881e-ca5e68dc4a5e | -8.61235 | -54.97222 | 2025-10-05 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82aac42e-7b83-3972-a614-6e7658773ba9 | -7.1318 | -63.12017 | 2025-10-05 05:33:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6274d248-41f2-3f98-8754-cd2c8f3ee5bf | -7.05952 | -63.14782 | 2025-10-05 05:33:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a48c45ca-8e5c-3aeb-94af-ab58fdb48aff | -3.77662 | -61.75406 | 2025-10-05 05:33:00 | NOAA-20 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f82e786f-a905-32a3-8d1e-049ed4456cb1 | -3.61536 | -61.55044 | 2025-10-05 05:33:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4c7348c2-1033-3913-ac17-30c1bc0d3cf1 | -2.89406 | -50.73777 | 2025-10-05 05:33:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7987e872-cad3-3e46-ba82-e415b4822f5e | -7.01475 | -55.2639 | 2025-10-05 05:33:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 209d778d-c2d5-395b-94bf-a067996db390 | -8.65187 | -54.96048 | 2025-10-05 05:33:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 284e39b7-daa5-340d-b204-993a231b711b | -8.67236 | -64.10168 | 2025-10-05 05:36:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2967b4af-0d9b-347c-9e5d-a4a0132ce9f9 | -10.46713 | -57.48743 | 2025-10-05 05:36:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4e17623b-a472-3734-a9ce-aaa5dc0aefe9 | -12.30696 | -55.13485 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f7b97afd-97d4-3c39-9e36-563715ae429e | -12.30603 | -55.14218 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e49ee68f-5dc5-3fc2-ae31-24f041318daf | -14.74391 | -54.65211 | 2025-10-05 05:36:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1940b416-32dc-3577-9e4f-d5aa67290a69 | -9.83419 | -58.07608 | 2025-10-05 05:36:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 330fb149-58ee-3644-8ce6-982ce4e0fb74 | -9.32721 | -54.53093 | 2025-10-05 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ff51e80-e596-3e49-837c-f574e4a1692c | -11.84567 | -63.71693 | 2025-10-05 05:36:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 062f92c2-c060-3886-9c72-b2d83b6c0412 | -12.30432 | -55.1549 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c43c3e5b-8ebc-360f-a105-2355e7fb5ba6 | -9.60191 | -57.7513 | 2025-10-05 05:36:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2146fe7f-513f-30a8-a74c-8fdd9b6f7f5e | -14.75459 | -54.66341 | 2025-10-05 05:36:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4a95c0a0-6a7d-3da9-a2a1-2247ababb826 | -11.87424 | -56.877 | 2025-10-05 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a9337378-699d-30e6-a022-bfc8bf247603 | -9.32868 | -54.51966 | 2025-10-05 05:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7bf9bff6-516d-37c3-a7ba-9a20853cd264 | -11.86626 | -56.8797 | 2025-10-05 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6efa1f52-88d4-34c5-97bc-53a0c3d37fc0 | -11.87191 | -56.87471 | 2025-10-05 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 10389406-4731-34d9-ad34-6a94ccfc88cf | -9.8336 | -58.08032 | 2025-10-05 05:36:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 29ca9615-b7a0-3246-ac93-a3aa37fd8bb2 | -11.97047 | -63.13383 | 2025-10-05 05:36:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2093406c-cf89-34b9-abb1-5a885655ef62 | -12.30557 | -55.14581 | 2025-10-05 05:36:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| abaec8a3-d8bc-352f-b42f-4ec46a6a66b6 | -9.59297 | -66.58894 | 2025-10-05 05:36:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1d7d59b-af23-32bd-91bc-46cce04b771e | -12.97995 | -51.01454 | 2025-10-05 05:36:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3a1091f8-7b92-3f01-b4a5-57f6114e4667 | -9.04946 | -61.64117 | 2025-10-05 05:36:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8214f49d-1c6e-39d0-b377-b6d2d99c24ee | -9.04595 | -61.64062 | 2025-10-05 05:36:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 300ad09d-966f-3a6b-9ee0-433f48199047 | -11.76102 | -64.93188 | 2025-10-05 05:36:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb7f570f-da76-3a03-b081-18529b5f415a | -8.09033 | -61.53069 | 2025-10-05 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README142.md)
