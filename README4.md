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
| 0fe1d2ba-ed76-355a-a215-94762d712eae | -11.6592 | -44.5741 | 2026-07-07 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 9f505f40-3a28-3a73-96cb-6679e7cd8bd8 | -11.6597 | -44.5508 | 2026-07-07 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 08584a26-476a-3309-8392-80b9d6b029c7 | -11.6789 | -44.5479 | 2026-07-07 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 268.5 |
| 33c97406-79f2-3020-84c7-d61b1601b18a | -10.9397 | -43.0593 | 2026-07-07 00:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 1c519446-d30b-32f5-8fae-7157a9759d4a | -6.895 | -43.7066 | 2026-07-07 00:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 7104ece9-ab99-3879-ba61-1fb2aa784606 | -11.6785 | -44.5712 | 2026-07-07 00:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 157.9 |
| 9073c572-e775-3eaa-9eb2-c7974fb72f55 | -6.9138 | -43.7049 | 2026-07-07 00:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 257.9 |
| 9655115a-1d8b-356c-940d-dbaa0d7dd505 | -13.261 | -54.2249 | 2026-07-07 00:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 631a72c0-a291-3dcb-aa6b-54b8925e0928 | -12.7741 | -44.5396 | 2026-07-07 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 9e91204d-7280-3224-8b79-7e9668933b60 | -12.7548 | -44.5428 | 2026-07-07 00:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 2b0c761e-2769-3840-8027-aa928bdaa60b | -6.9135 | -43.7281 | 2026-07-07 00:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 0958819d-b076-3260-9df5-4ca627155afa | -6.9326 | -43.7032 | 2026-07-07 00:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 174.7 |
| 85e05411-1957-3aa0-9f73-73409809acfc | -13.261 | -54.2249 | 2026-07-07 01:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 29919ead-2fbc-3cae-bec7-a1c55cfc43fb | -11.6785 | -44.5712 | 2026-07-07 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 106.9 |
| 60d7eb98-9405-3a1e-9029-ebdf11213c43 | -6.895 | -43.7066 | 2026-07-07 01:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 60.8 |
| ba19d8da-958e-35f0-bc8e-492c1f9a94ba | -11.6592 | -44.5741 | 2026-07-07 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 0c143db1-2bb4-3df3-baf2-784a9935c419 | -10.9205 | -43.0622 | 2026-07-07 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 22f6ae88-c26f-3212-b771-aaee45519a17 | -6.9138 | -43.7049 | 2026-07-07 01:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 221.6 |
| fb1ae43e-84e1-3c69-a7db-01cfe3e48302 | -11.6597 | -44.5508 | 2026-07-07 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 142.1 |
| a4bd394e-99ad-3520-9d46-b8c571e559d8 | -6.9323 | -43.7264 | 2026-07-07 01:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 229b722e-395b-3bb3-8831-2f9c3be9b826 | -6.9326 | -43.7032 | 2026-07-07 01:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 171.7 |
| dac71b9c-8ce0-397f-9d7e-10c39946cb96 | -11.6789 | -44.5479 | 2026-07-07 01:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 184.9 |
| 7571b169-5c03-3fed-8269-1129dae82ad6 | -12.7548 | -44.5428 | 2026-07-07 01:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 313b08d9-1ec3-31a5-8ea8-16a4db498dfb | -10.9397 | -43.0593 | 2026-07-07 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| dc152b3f-29d3-3874-829a-e13784c3c517 | -6.9135 | -43.7281 | 2026-07-07 01:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 20e9fdec-8381-36b0-bc95-3fb1af5af9b6 | -6.9323 | -43.7264 | 2026-07-07 01:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 45f1b260-92e0-3269-9565-3cea4d8c80d9 | -6.9135 | -43.7281 | 2026-07-07 01:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 85.0 |
| c4abfe41-6cef-3785-8950-aac4d48b4eb2 | -10.9397 | -43.0593 | 2026-07-07 01:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.4 |
| a7cc5e5d-b951-3a5c-b36b-a4ee60ca1c63 | -6.9326 | -43.7032 | 2026-07-07 01:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 6cac4daa-db07-3782-9fdf-948517538c16 | -11.6597 | -44.5508 | 2026-07-07 01:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 238b1652-8bd3-3fd9-a291-3da7ea57adfb | -6.895 | -43.7066 | 2026-07-07 01:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 39989a8c-fc21-38c9-8dfd-0dd83f750664 | -11.6789 | -44.5479 | 2026-07-07 01:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 161.2 |
| ee9e0c7c-c3f8-3760-9987-f461f902bb46 | -11.6592 | -44.5741 | 2026-07-07 01:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 00a8f1c8-b364-3618-a924-3c1985c4b288 | -11.6785 | -44.5712 | 2026-07-07 01:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 91.3 |
| c7b32c52-9044-32cd-ac3b-d2dae7b74666 | -6.9138 | -43.7049 | 2026-07-07 01:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 202.9 |
| cda222e6-f9a0-3ecb-a806-cb5a9be3f265 | -12.7548 | -44.5428 | 2026-07-07 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 79407ea7-062a-3869-9bc6-e9e8214a305a | -11.6667 | -44.562801 | 2026-07-07 01:13:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 50a489e1-afd2-3240-af47-aa2fb17a3555 | -10.7735 | -46.621101 | 2026-07-07 01:13:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 646b6c8e-bab4-3078-93a1-1332f4d8ecda | -11.6687 | -44.5322 | 2026-07-07 01:13:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c8390148-9bfb-3862-b60a-3055f2a5e1de | -13.7664 | -52.7248 | 2026-07-07 01:13:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2d445531-0ca7-3191-bd82-06e307485875 | -13.2612 | -54.231998 | 2026-07-07 01:13:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 32834e87-571d-3dc0-86af-97305f724b7e | -11.6571 | -44.565498 | 2026-07-07 01:13:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fa735142-ed7a-3d51-b50f-c25b9889d836 | -13.2994 | -54.352798 | 2026-07-07 01:13:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a488fff2-3990-38eb-8645-74c1f03cd139 | -13.2579 | -54.217499 | 2026-07-07 01:13:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2a3ce47f-98d4-3968-a304-4f35bd4cfab6 | -13.324 | -54.3699 | 2026-07-07 01:13:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1a73d296-aab8-3ef7-887f-a1e4beda4c78 | -13.5427 | -52.915401 | 2026-07-07 01:13:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 54cecadf-ab09-39b6-8a02-e5c6c73c9dc2 | -21.066601 | -47.249802 | 2026-07-07 01:13:00 | METOP-C | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a2badf47-bac9-3f69-91fd-6843337e1f9c | -7.6369 | -50.0233 | 2026-07-07 01:13:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e87f24dd-8e8d-3ba6-9a4c-b55c37962e75 | -13.5408 | -52.907398 | 2026-07-07 01:13:00 | METOP-C | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| c224b7cf-6fcd-3c73-a099-a8567c3fef66 | -13.7683 | -52.732899 | 2026-07-07 01:13:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 446b272a-4684-3c2f-9caa-b623ad089b3b | -21.0569 | -47.252602 | 2026-07-07 01:13:00 | METOP-C | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c9f33148-cee6-3415-9fab-2ded74031370 | -6.432 | -55.801601 | 2026-07-07 01:13:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f09c1eb3-74df-39c4-9aba-5347b4f390f7 | -13.2765 | -54.343102 | 2026-07-07 01:13:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 699b99bb-ecdf-3191-be94-f284d86782a4 | -11.6763 | -44.560101 | 2026-07-07 01:13:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5af8a10b-4565-324b-b094-cb075295e73e | -12.7553 | -44.549 | 2026-07-07 01:13:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4351bf91-1aaf-3cdc-96eb-7d265884ffc8 | -8.5476 | -63.368698 | 2026-07-07 01:13:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b4381166-dde5-3437-b752-13a12e966246 | -13.7742 | -52.714298 | 2026-07-07 01:13:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eb1a3a11-48d4-3eca-9261-3b0a65a3a998 | -6.4303 | -55.794498 | 2026-07-07 01:13:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5dafe04-301b-37da-9829-8d5a28eb435f | -13.2782 | -54.3503 | 2026-07-07 01:13:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4ada3d91-eeab-31bf-a162-1394fd852b37 | -12.5088 | -48.256001 | 2026-07-07 01:13:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 191a1a1d-cb41-3c76-aed8-92cfb08850c7 | -10.7831 | -46.6185 | 2026-07-07 01:13:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 73cddc5f-9ea3-328e-95bf-97a052dc72ad | -10.7004 | -49.604301 | 2026-07-07 01:13:00 | METOP-C | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e9fe84ae-3489-3135-84b7-47e848d639ce | -8.1218 | -47.111801 | 2026-07-07 01:13:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6e84ac4-a9c9-3121-9519-2ac67af7221a | -13.2799 | -54.357498 | 2026-07-07 01:13:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b044a78b-52e9-3096-adf2-c7e25b570577 | -11.6782 | -44.529499 | 2026-07-07 01:13:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fd87e546-448e-3af4-b009-e113812ddc1a | -12.7648 | -44.5462 | 2026-07-07 01:13:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 16660a93-60a3-33bc-b649-bf1311d92b24 | -13.7761 | -52.722401 | 2026-07-07 01:13:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8e3d95a7-f3fc-3b93-b15e-0be2766a519c | -13.778 | -52.730499 | 2026-07-07 01:13:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1277bdc5-c874-3f07-8b73-c6a1bdcb91e4 | -4.289 | -48.356098 | 2026-07-07 01:13:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0a1290f-01ef-3866-a4b4-12463d7b7efd | -13.2338 | -54.292099 | 2026-07-07 01:13:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f50dc773-5e6b-3dfe-8ea3-410d4e497431 | -7.6466 | -50.020901 | 2026-07-07 01:13:00 | METOP-C | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8fb4a0f-6690-33c1-b269-35ff3e452512 | -13.2863 | -54.340801 | 2026-07-07 01:13:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eeb99068-68d6-34a2-92fd-cf1696ef8c5b | -13.2847 | -54.333599 | 2026-07-07 01:13:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 617898c7-a19d-3d81-ae77-fba930f3890d | -13.7878 | -52.7281 | 2026-07-07 01:13:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cad1c5e7-4446-30c8-bc6e-d96ee3da6de9 | -21.07 | -47.262798 | 2026-07-07 01:13:00 | METOP-C | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a0653311-78e9-3694-a03b-904fd9446aa8 | -11.7539 | -51.531601 | 2026-07-07 01:13:00 | METOP-C | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 05d3314e-d6fa-31d9-8c64-5ce595249bbe | -11.6591 | -44.534901 | 2026-07-07 01:13:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c62fe046-804f-3062-9799-f099c026b81b | -13.3354 | -54.374802 | 2026-07-07 01:13:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4ce70b97-4d6e-3ab1-871c-e922a37addb0 | -13.288 | -54.348 | 2026-07-07 01:13:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 616a4c1f-63a7-3889-a21c-88118b9a76e4 | -12.8412 | -58.305901 | 2026-07-07 01:13:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 66e7307a-7bf7-3023-ba0f-b9f3c5ee0bf9 | -13.3321 | -54.360401 | 2026-07-07 01:13:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bdee753c-84cb-3359-b7c5-7d4edcf572b5 | -13.6024 | -56.612499 | 2026-07-07 01:13:00 | METOP-C | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f39c229c-1078-383a-948a-1706582d26bb | -13.2596 | -54.2248 | 2026-07-07 01:13:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e44768f5-af90-3dd6-97ef-0cf2f5c3b6f8 | -11.6858 | -44.5574 | 2026-07-07 01:13:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 79f860b1-6885-3195-8c2c-f7efd88ed41b | -12.7575 | -44.519402 | 2026-07-07 01:13:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fcf79c01-a4dc-3ebd-8409-7cb6a195c5c2 | -13.3338 | -54.367599 | 2026-07-07 01:13:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a7a4b5db-41b0-326a-97dd-ba5206994008 | -23.569099 | -47.507401 | 2026-07-07 01:13:00 | METOP-C | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 32a8c4a2-5b64-36c8-a5ed-e88ce01da363 | -13.3223 | -54.362701 | 2026-07-07 01:13:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4c7c54bf-324f-3a2b-831c-937b3231e5c2 | -6.9326 | -43.7032 | 2026-07-07 01:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 76d63ef8-5af7-3de1-b2b0-187402e25111 | -11.6789 | -44.5479 | 2026-07-07 01:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 151.0 |
| 92356ac7-1bcd-331c-a5ef-90b57fd0c14f | -12.7548 | -44.5428 | 2026-07-07 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 065bb090-a35b-3e7a-ad16-69d4904f0225 | -6.9135 | -43.7281 | 2026-07-07 01:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 70.9 |
| c3c46763-a0c6-315e-9416-0a0721658303 | -11.6597 | -44.5508 | 2026-07-07 01:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 125.4 |
| 1829da2f-51b4-37be-8879-ce4a7d255427 | -6.895 | -43.7066 | 2026-07-07 01:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 57.0 |
| c48add06-49ee-34b7-8076-d4d498cf201b | -6.9138 | -43.7049 | 2026-07-07 01:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 182.5 |
| 9e24818d-be15-3d28-b83b-9e1cb76fafde | -10.9397 | -43.0593 | 2026-07-07 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 0bcf3511-549e-348f-b44a-a0a165ffb7fd | -11.6592 | -44.5741 | 2026-07-07 01:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 115.7 |
| cce053cd-d1f5-3b9d-9347-53b573aa3261 | -11.6785 | -44.5712 | 2026-07-07 01:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 5197016d-e78d-3f14-aa5b-6737b3e45eb5 | -12.7548 | -44.5428 | 2026-07-07 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.6 |
| c0d5560b-1d02-3b42-b341-10965779430c | -6.9135 | -43.7281 | 2026-07-07 01:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 66.7 |


[Clique aqui para ver as próximas entradas](README5.md)
