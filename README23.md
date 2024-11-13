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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9fb14633-7042-3742-ba2c-0a0d9922a49d | -17.6918 | -44.64892 | 2024-11-13 04:08:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 99872dc3-edb9-30e4-9a71-c570d0a6a2be | -18.37368 | -47.51899 | 2024-11-13 04:08:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6f51f53-22b9-357d-acb0-9b7b4d98be77 | -10.36765 | -49.18066 | 2024-11-13 04:08:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| af66cda4-0809-31af-a469-79eb76db1029 | -16.13893 | -43.55676 | 2024-11-13 04:08:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 80e7d0e7-b071-3aa0-ac22-9a9dd0acb1b2 | -15.64711 | -39.18406 | 2024-11-13 04:08:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 711f4b45-5a84-3f58-8fb9-e98fb1fc1aa6 | -10.72864 | -49.53179 | 2024-11-13 04:08:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| cb3a4859-1769-310c-89f5-c2158a0443c7 | -18.37441 | -47.51469 | 2024-11-13 04:08:00 | NOAA-20 | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db685cde-44ac-3573-a1db-3731226e790a | -16.31247 | -44.4129 | 2024-11-13 04:08:00 | NOAA-20 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9987538d-aa88-3b36-9c9a-05e996ef7ca2 | -17.69122 | -44.65255 | 2024-11-13 04:08:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a328593-60f5-3fa3-bb52-fb13c7e77591 | -3.3518 | -48.9689 | 2024-11-13 04:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 8f6539b0-7ff1-3c71-b23a-b35b15d8eb91 | -10.7425 | -49.5244 | 2024-11-13 04:10:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 569dcd83-efbc-328b-a04e-46367a5550b3 | -3.3519 | -48.9475 | 2024-11-13 04:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 6a531def-810c-3d07-80cb-27f107f60234 | -3.0689 | -50.3326 | 2024-11-13 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 160.1 |
| a71e36fc-0e81-3423-90e3-8e3dff64c414 | -3.0504 | -50.3332 | 2024-11-13 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 0a67ce15-85ac-37f4-8797-79f813718782 | -3.0688 | -50.3536 | 2024-11-13 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 18956679-2466-3005-ba61-f08fa3fad8c5 | -2.9925 | -51.0242 | 2024-11-13 04:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 3dd7df0b-f814-3f2c-a068-48ca8ba04d9f | -10.7235 | -49.5265 | 2024-11-13 04:10:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 8776390e-d000-39be-b877-a663a8d24b50 | 1.0663 | -60.5985 | 2024-11-13 04:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.7 |
| e5abfe56-2c19-3876-b20f-8771ed379d4f | -20.0915 | -49.21033 | 2024-11-13 04:10:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 03821981-f8bd-391e-8684-0f1fe38e868f | -20.99038 | -47.35637 | 2024-11-13 04:10:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6f0b8490-5c8c-33a7-9fb6-1d5a89565d37 | -20.99458 | -47.41569 | 2024-11-13 04:10:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1e62401-d946-3b55-bd14-00289a46ffe7 | -20.63871 | -47.41695 | 2024-11-13 04:10:00 | NOAA-20 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f61aa19-19a3-314b-b523-b5f47f4564c9 | -18.609 | -47.57651 | 2024-11-13 04:10:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f3fedbdd-cee7-3c14-9355-ffc64674aba4 | -20.09821 | -49.21696 | 2024-11-13 04:10:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9e528b5b-06eb-37b7-8605-0d49c6bc863e | -20.09059 | -49.2153 | 2024-11-13 04:10:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ebe80c9b-235f-3617-ba22-6c1a0e8d30e5 | -20.99384 | -47.35706 | 2024-11-13 04:10:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4cbd338c-f5d1-321d-93dc-32397363a29f | -21.20375 | -47.13274 | 2024-11-13 04:10:00 | NOAA-20 | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2c74fafb-bd73-3ce6-a535-0d3040db9484 | -21.20786 | -47.12938 | 2024-11-13 04:10:00 | NOAA-20 | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be14dc93-da30-3258-a0cd-8881451fb386 | -21.20854 | -47.12537 | 2024-11-13 04:10:00 | NOAA-20 | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b78d2d25-0e80-31ed-ae29-d2660e3d8daf | -20.41818 | -43.55261 | 2024-11-13 04:10:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0a6199f0-80db-3428-b087-c84c8d31dbf4 | -19.83809 | -40.08405 | 2024-11-13 04:10:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7aff3589-a509-3242-a7df-fcadb65826a1 | -20.08678 | -49.21448 | 2024-11-13 04:10:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ccf0b8df-5383-3731-98fc-55e3784522db | -20.63523 | -47.41628 | 2024-11-13 04:10:00 | NOAA-20 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96d2d935-a4bb-385f-bd9f-ce01c5a7aa6a | -19.71663 | -40.35143 | 2024-11-13 04:10:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c33a6135-7d58-3845-9f20-41580bb63bd4 | -21.04985 | -47.24923 | 2024-11-13 04:10:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a6f6f278-fa51-36fe-84ff-8d265ae5ff69 | -19.71598 | -40.35637 | 2024-11-13 04:10:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f5a9c317-c67c-3808-a5a0-84fc653b928e | -21.20718 | -47.13338 | 2024-11-13 04:10:00 | NOAA-20 | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d587a051-2344-37c0-8a3a-6dc92639ae1d | -20.0944 | -49.21612 | 2024-11-13 04:10:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e2e8ac38-ca10-343e-8519-336a8e9544ce | -19.26595 | -45.36543 | 2024-11-13 04:10:00 | NOAA-20 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e204f5a5-77ea-3b9d-8414-a4a6c46da496 | -20.41483 | -43.55207 | 2024-11-13 04:10:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9ddfa732-00b1-33e6-9adc-7e3aa7e6594f | -20.09531 | -49.21114 | 2024-11-13 04:10:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1e3032b2-5cca-3e71-ab9d-7dc59d45ce61 | -20.99388 | -47.4198 | 2024-11-13 04:10:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8af7d81f-cffe-3a6f-972c-b34844a2292f | -20.98624 | -47.35967 | 2024-11-13 04:10:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a25cfc4c-319d-3fc0-8b87-909c85011fc0 | -29.52384 | -49.88494 | 2024-11-13 04:12:00 | NOAA-20 | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| d952f02b-e77d-315f-a4ba-f6974e514162 | -29.52572 | -49.89456 | 2024-11-13 04:12:00 | NOAA-20 | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| a4c56a66-42c1-33c8-a971-91113a58cafa | -29.52999 | -49.89097 | 2024-11-13 04:12:00 | NOAA-20 | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 11.6 |
| 6683c3e2-72f8-3491-99c0-de4cd888c77f | -29.52731 | -49.88575 | 2024-11-13 04:12:00 | NOAA-20 | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 11.6 |
| fb30c34c-75b4-37bd-aede-b639a8268e1e | -28.90931 | -51.96991 | 2024-11-13 04:12:00 | NOAA-20 | GUAPORÉ | RIO GRANDE DO SUL | Brasil | 4309407 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6a324fc0-b3db-3cdc-92fe-a31e44e842a2 | -28.58603 | -49.44208 | 2024-11-13 04:12:00 | NOAA-20 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 25a106f5-bc66-391c-8a0c-5af860b4f8cd | -29.52652 | -49.89015 | 2024-11-13 04:12:00 | NOAA-20 | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 11.6 |
| daf0b0ff-dc59-3bb2-9cbb-96d97e59f1ac | -27.46863 | -48.68007 | 2024-11-13 04:12:00 | NOAA-20 | BIGUAÇU | SANTA CATARINA | Brasil | 4202305 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 793b6671-033f-31c1-bc51-74e5559af4b4 | -28.91001 | -51.97057 | 2024-11-13 04:12:00 | NOAA-20 | GUAPORÉ | RIO GRANDE DO SUL | Brasil | 4309407 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7aacd7fb-f942-30c5-ac90-45ee0d9224b1 | -29.53078 | -49.88657 | 2024-11-13 04:12:00 | NOAA-20 | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 11.6 |
| f743717e-4b53-3ea0-ab5f-b66228447453 | -29.52304 | -49.88934 | 2024-11-13 04:12:00 | NOAA-20 | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| e5b1f395-78eb-3ad5-8ee8-6d8626d0a58d | -3.069 | -50.3117 | 2024-11-13 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 1f84501f-6164-3d5e-8978-c394ada32206 | -3.3519 | -48.9475 | 2024-11-13 04:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 135.6 |
| 340d0a03-0081-3858-aca5-7acce708cea4 | -3.3518 | -48.9689 | 2024-11-13 04:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 4eced22e-c5c5-3a02-8122-e16807de6629 | -3.0688 | -50.3536 | 2024-11-13 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 9c8d46bd-3ba7-3648-8630-f1a8d95be012 | -3.3333 | -48.9695 | 2024-11-13 04:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| e5a0846f-78da-3ace-bb3b-8e28948cdb0d | -2.9925 | -51.0242 | 2024-11-13 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| d26ae5f3-9d59-3e58-b8a0-38117f852293 | 1.048 | -60.5986 | 2024-11-13 04:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.1 |
| a7b5eb94-3d24-3fce-b49f-8a9ee1d70b9b | 1.0663 | -60.5985 | 2024-11-13 04:20:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 1df08067-0ffe-3bc9-8588-ee445530139b | -10.7425 | -49.5244 | 2024-11-13 04:20:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 194a74af-cf4f-3e57-a70c-c814f5ef0ee6 | -3.0689 | -50.3326 | 2024-11-13 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 143.4 |
| 8e6903df-2c1a-3835-ac28-18b886c564d2 | -3.3334 | -48.9482 | 2024-11-13 04:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 232753d3-e946-3c60-bd04-dd63b6ba27a5 | -3.0504 | -50.3332 | 2024-11-13 04:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 99.0 |
| c9c5519b-dbd4-343b-8cc0-6e32cb1a32c2 | 1.0663 | -60.5985 | 2024-11-13 04:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.1 |
| d9d6e6ef-676a-38dd-8738-20207cb0ea26 | -3.3519 | -48.9475 | 2024-11-13 04:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 162.5 |
| 9f5debf5-483e-3f5f-bdab-abcf8ec84520 | -2.248 | -53.7426 | 2024-11-13 04:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 11473b8b-8f9b-3ea4-a2d1-70832901beed | -3.0504 | -50.3332 | 2024-11-13 04:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 686753ce-e00e-30f8-a664-b6cb8ab93b40 | -3.3518 | -48.9689 | 2024-11-13 04:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 148.2 |
| 3be14086-6ccb-353c-8abf-4949cccdbab1 | -2.9925 | -51.0242 | 2024-11-13 04:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| c154d595-45df-303c-ba8f-23bf82f1c630 | -3.0689 | -50.3326 | 2024-11-13 04:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| b982f3d5-d309-33ce-963c-66410a6e0a03 | -2.9924 | -51.045 | 2024-11-13 04:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 30652f98-622f-37f9-996b-cd05cc3bdc95 | -2.248 | -53.7426 | 2024-11-13 04:40:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 43c3dbbd-aefc-3a84-a450-69d8de9b763c | -17.6066 | -57.551 | 2024-11-13 04:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.2 |
| 56ea0974-a41e-3bcd-815a-44f5cf6a5916 | -17.6069 | -57.5304 | 2024-11-13 04:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.6 |
| b8c9b7a2-9aab-3c8e-a80b-14e824a0fd14 | -3.0504 | -50.3332 | 2024-11-13 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 46274598-7c78-3b7d-8990-802ce866b975 | -3.0689 | -50.3326 | 2024-11-13 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| a4639a54-965b-3903-aee1-84ec0fc2a98a | -10.7425 | -49.5244 | 2024-11-13 04:40:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 60027634-5567-30fb-9906-f9f9c5522d6b | -17.5872 | -57.5328 | 2024-11-13 04:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.9 |
| 75b202ac-bad2-32dc-b34c-b6c7a08bf765 | -2.9924 | -51.045 | 2024-11-13 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 2e2b186f-f679-35d1-b3d3-2642c4ee716b | -2.9925 | -51.0242 | 2024-11-13 04:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 30b572c9-8260-3569-b1f6-bc1259006cf3 | -3.3518 | -48.9689 | 2024-11-13 04:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 002c9a3f-0068-3bbf-899c-b8dd99958066 | -3.3519 | -48.9475 | 2024-11-13 04:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 143.4 |
| 50a7b376-0f4b-3de2-b82f-4bff9ac70a58 | 1.0663 | -60.5985 | 2024-11-13 04:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.7 |
| cac398f8-9b6b-3691-933b-14058705a7c8 | -10.7235 | -49.5265 | 2024-11-13 04:40:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 9ee9cb96-9741-364a-ab08-6f7d3b9bbc2f | -10.7425 | -49.5244 | 2024-11-13 04:50:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 4162877d-72c2-3d76-bbcc-4c4547fd2a80 | -10.7235 | -49.5265 | 2024-11-13 04:50:00 | GOES-16 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 3960e516-758b-3bfe-8048-5bcc1e65c866 | -3.3518 | -48.9689 | 2024-11-13 04:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 106.9 |
| 786c471f-83f5-3e23-933b-40abb2062a13 | -3.3519 | -48.9475 | 2024-11-13 04:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 174c421a-7838-3625-bc0f-f6b18c7ca455 | -3.0689 | -50.3326 | 2024-11-13 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 83367f8e-9842-3c7c-9d90-c11487792844 | -3.0504 | -50.3332 | 2024-11-13 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 3fbeb5a0-1f95-3b59-87ca-1075fc657611 | -2.9925 | -51.0242 | 2024-11-13 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| b13487cf-03a4-3c24-a7ef-92c5b7e36530 | 1.0663 | -60.5985 | 2024-11-13 04:50:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.3 |
| d63185f1-d800-3fb6-bb64-4ab96c5b3d5a | -2.9924 | -51.045 | 2024-11-13 04:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 786b42a3-bcd8-3a46-9440-e9f56eaa6720 | -4.36754 | -44.09138 | 2024-11-13 04:57:00 | AQUA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b7e7b0a9-9009-3e55-8c6e-eaf263117f98 | -4.36519 | -44.10646 | 2024-11-13 04:57:00 | AQUA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1f5d1397-10d3-320e-992b-f9c6497e65aa | -3.35524 | -48.96416 | 2024-11-13 04:57:00 | AQUA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 5c176b4a-d1e2-3a8c-bd5b-cfa6fe8b16ca | -4.66675 | -47.41828 | 2024-11-13 04:57:00 | AQUA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 26.5 |


[Clique aqui para ver as próximas entradas](README24.md)
