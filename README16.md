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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 866670f7-47e1-36a0-a6c9-1d960eaa13f5 | -4.54626 | -44.12677 | 2025-11-29 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 979fc963-f97b-3499-906b-4e85e44fa6a7 | -4.47495 | -50.09188 | 2025-11-29 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a848c8f5-3ddb-3897-a174-a90efa59540c | -8.17495 | -43.20234 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d0adf10d-1266-3e57-a2dc-361ba835e2b4 | -4.11781 | -44.90613 | 2025-11-29 04:14:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a3a5a5bf-10a5-30ac-997c-d86682d88378 | -3.85817 | -44.90127 | 2025-11-29 04:14:00 | NOAA-21 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 231e6bea-6779-3e4e-951a-f452daa802f5 | -3.31861 | -50.28053 | 2025-11-29 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 00b5c9dc-8dde-381b-8c7c-ebe1024f9676 | -4.11433 | -44.90558 | 2025-11-29 04:14:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9bfe42e2-aa4c-361b-9ee9-abf0fc4c1639 | -2.93691 | -53.27295 | 2025-11-29 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ffa3008-0761-3c81-9cb1-18503581b0ed | -5.00168 | -38.54024 | 2025-11-29 04:14:00 | NOAA-21 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 10.0 |
| cadc5d74-d108-3ac9-a3a9-112bd7d81e97 | -6.71233 | -40.81559 | 2025-11-29 04:14:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 887f6b7f-ed21-38b1-b0b6-8bfe35ff3fa9 | -5.35881 | -43.02856 | 2025-11-29 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 37d80999-d9ee-37ee-87a9-fba6708f676a | -8.16449 | -43.20425 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 5d7eb2cc-319f-3624-b873-d5fc93b6e6d6 | -6.4591 | -41.7295 | 2025-11-29 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| dabae545-b720-32aa-8c3c-d0cbd8a78baa | -3.88267 | -54.20789 | 2025-11-29 04:14:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 777ed238-25b2-31fb-9560-6a827b9eca3e | -8.04262 | -43.13547 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 7dc4cac4-c310-30ed-b6bd-15700bd0a090 | -9.42725 | -40.34641 | 2025-11-29 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d3366808-6dbc-3be9-9a8f-8f22e3a7e0e8 | -5.36543 | -43.02959 | 2025-11-29 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 385d19fc-909b-3eb9-a177-5d74cc931231 | -4.04152 | -50.69977 | 2025-11-29 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e8529b8-1b9d-3a78-9fc8-c97ef2e05bba | -6.73793 | -46.29712 | 2025-11-29 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7aaf20e5-04d9-33f3-8825-b7f186f0cfdd | -5.42419 | -44.85686 | 2025-11-29 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a959b32e-674e-31fb-85fa-5132600b9df1 | -8.79403 | -40.43048 | 2025-11-29 04:14:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5d66be03-bea3-37a7-a99a-64d6c53600ad | -5.54673 | -37.50337 | 2025-11-29 04:14:00 | NOAA-21 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 55f7db55-8c9f-342e-b2db-426a3d156342 | -4.20341 | -46.16774 | 2025-11-29 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 758a25cc-2e6f-3a1d-b883-ac8ddf5fc3eb | -4.52367 | -46.4758 | 2025-11-29 04:14:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| daa0c4f9-e6fc-313a-a21d-54816ef26979 | -5.24125 | -41.24184 | 2025-11-29 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2fcb90aa-5a9d-3665-8d86-c35e81bc907c | -9.32107 | -43.09113 | 2025-11-29 04:14:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 37d59b26-9186-3df5-a602-dd13a45e685b | -4.22427 | -46.49828 | 2025-11-29 04:14:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 52e58e15-057c-3785-a08e-195808a5bb8b | -6.78439 | -41.71327 | 2025-11-29 04:14:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a09dd438-ad28-3de6-b7d8-c2609c5b129e | -8.17002 | -43.21223 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 843641a2-cb43-34f2-a7ea-8ba0e9e7cfb0 | -6.45574 | -41.72895 | 2025-11-29 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e47eb718-a460-37ec-87c5-5d577b11461c | -3.46586 | -47.63402 | 2025-11-29 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 319610bb-d937-3175-bdd3-e3b1cbbc6f7b | -3.95362 | -44.76303 | 2025-11-29 04:14:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 87030103-2a6c-3c3b-9e32-e7c3a27e13a0 | -8.16726 | -43.20824 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 26.0 |
| 1b5eca35-b6a4-3000-acb3-d868ec2eecec | -8.1678 | -43.20477 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 26.0 |
| a187cec0-25f1-34ea-8e21-33cf5a201284 | -6.30822 | -43.7827 | 2025-11-29 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ccda8208-3233-306f-9c31-3c8e8a0414cf | -6.78159 | -41.70912 | 2025-11-29 04:14:00 | NOAA-21 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 81b421eb-493c-39d3-bf61-ad743f30ade9 | -8.16503 | -43.20078 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3870d999-0f98-3703-abc6-f7be25af70b1 | -6.69707 | -41.46263 | 2025-11-29 04:14:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| c3035269-e630-354a-848e-64393f8a690c | -2.93164 | -53.26754 | 2025-11-29 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f13d6643-f2f5-34ac-b789-1b883be8ef64 | -10.23808 | -44.89509 | 2025-11-29 04:14:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7531219-5099-3b55-8aec-11b88c91a4e1 | -7.22838 | -40.28308 | 2025-11-29 04:14:00 | NOAA-21 | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a7110bcf-efe2-3e1a-8f59-bab49d36aecb | -8.03931 | -43.13495 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| f964f494-dd20-3c93-b9b2-42e6a5b80fa2 | -4.89475 | -43.96584 | 2025-11-29 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a952b42f-0b7d-3e88-b569-c5b935bef99e | -6.71007 | -41.46836 | 2025-11-29 04:14:00 | NOAA-21 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 799800ed-c9e3-3d27-96a0-acdc064fb0dd | -5.23991 | -41.24137 | 2025-11-29 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 13cb92b4-79c0-36fb-9e0f-685febcb86f3 | -9.98048 | -44.71881 | 2025-11-29 04:14:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 21e6577d-a107-3de5-852f-de678ed87729 | -5.30887 | -40.88877 | 2025-11-29 04:14:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 909549cc-cb3c-3672-945d-bda215291fd2 | -5.105 | -46.11123 | 2025-11-29 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55895914-310e-36ac-a553-f3c41e44aeb0 | -6.91068 | -37.49434 | 2025-11-29 04:14:00 | NOAA-21 | MALTA | PARAÍBA | Brasil | 2508802 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bd916433-21f6-390d-9d87-177f9f4d5886 | -8.03546 | -43.13791 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| f0b88ad7-f277-3580-a8a0-3700eacda0d1 | -8.03269 | -43.13391 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| bf31370a-1352-394a-a6f1-f4b39d42fc92 | -4.38556 | -43.83072 | 2025-11-29 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 71ebad3b-8efe-39b4-91ec-037ab18dd45d | -8.04484 | -43.14293 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8c52c4e3-2715-3767-b477-9b3323f59511 | -10.48426 | -47.34432 | 2025-11-29 04:14:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bb76da4a-734c-3e80-82b5-c000bfd0bb16 | -8.04592 | -43.13599 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 29322604-c0e1-3f59-a974-c394c3da8455 | -4.73545 | -41.17564 | 2025-11-29 04:14:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 048b074b-4bcd-390f-8ec5-5d8c7318f13c | -7.66724 | -43.75029 | 2025-11-29 04:14:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 02a841bf-d9a5-3891-8dd2-162779ce2760 | -9.43027 | -40.35127 | 2025-11-29 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c7f42ee1-dadd-34e4-9ce6-fc0e0af9ceb3 | -6.46246 | -41.73003 | 2025-11-29 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1ec53f4d-90f5-37ad-8950-e027699c0ad6 | -9.89503 | -36.14109 | 2025-11-29 04:14:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| c4b7d53c-253d-3d46-80a6-325adc0556d6 | -2.91559 | -53.07164 | 2025-11-29 04:14:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 04bd22aa-1b7a-357a-af76-85d826f64ee4 | -8.13774 | -49.51144 | 2025-11-29 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb5accd3-2d95-3447-a840-023b695badf8 | -7.48902 | -42.75935 | 2025-11-29 04:14:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9b6ea60f-dd18-3c7f-83b2-7d71ef68de98 | -7.32146 | -42.56881 | 2025-11-29 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 32c56206-d412-3f52-99b0-2cab9cbfe027 | -6.60177 | -43.69066 | 2025-11-29 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b87a8f16-a303-3990-b9a5-fc949ba68d1d | -5.23485 | -41.25164 | 2025-11-29 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3ff9eafa-a61a-3c9a-babe-dd332d4e5ce7 | -3.50937 | -47.20527 | 2025-11-29 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 87d9fc75-f91a-357a-94b2-07449ad32a40 | -4.85909 | -50.82581 | 2025-11-29 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89dda50d-3a9b-3b4a-8d1f-9559643f90b1 | -5.33793 | -40.8819 | 2025-11-29 04:14:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a343ede8-d9d0-3cea-acb7-e47d1b29893c | -5.0007 | -38.53796 | 2025-11-29 04:14:00 | NOAA-21 | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 09f04056-759e-3376-982a-0b529baf5c5d | -9.90053 | -36.13665 | 2025-11-29 04:14:00 | NOAA-21 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 5242c2a4-d80d-3eb8-b0ba-55772ccb32b0 | -4.63196 | -43.98983 | 2025-11-29 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 0d184922-e533-3e47-8c05-97675e189be6 | -8.04316 | -43.132 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 4aded4de-5955-355e-b116-5d65f5cf0c97 | -4.62917 | -43.98575 | 2025-11-29 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d4f45833-65aa-394a-af0c-08af2a06c494 | -2.96387 | -50.99677 | 2025-11-29 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be1ce964-ac73-339c-9921-f07baaf143e5 | -8.1788 | -43.19939 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 02e936e8-8e84-368f-908b-3b6a156303cd | -4.10531 | -42.90773 | 2025-11-29 04:14:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 75ce007f-4d08-3210-8570-538682cb26a0 | -6.98286 | -42.47247 | 2025-11-29 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5a952afb-4df3-312d-87c2-4906e13dedc4 | -3.46169 | -47.63336 | 2025-11-29 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fad442b4-7875-3a7a-97a8-02cab8e70538 | -5.30105 | -44.72662 | 2025-11-29 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 507822db-3018-374e-a6e2-63f66526f425 | -3.46176 | -47.63348 | 2025-11-29 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2f98dc2c-1b4b-3dfc-9697-f97f28625917 | -5.09152 | -40.24203 | 2025-11-29 04:14:00 | NOAA-21 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 00a52190-1d6f-304a-88bd-45c7d5516654 | -5.21533 | -39.56579 | 2025-11-29 04:14:00 | NOAA-21 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 754236cc-0424-3dc8-bb55-261af8c1f27a | -8.1711 | -43.20529 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 26.0 |
| 492ba9c5-76ca-38b1-88d4-a4c269917c4e | -3.95599 | -46.47444 | 2025-11-29 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 730ce5eb-2103-3bbf-be49-5e77affe1306 | -3.40299 | -47.19188 | 2025-11-29 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ba26d5c-cef3-30f9-b745-8180f3edb96e | -8.16888 | -43.19783 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9bd68d4c-ca07-31d3-8c84-5103f30b326a | -8.16834 | -43.2013 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 46a17d2a-6d00-3857-84fe-0ccf4758ba0b | -7.46797 | -39.96346 | 2025-11-29 04:14:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 10.0 |
| f37aa4a8-926d-3566-a0fb-1accc9e72553 | -8.03654 | -43.13097 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 8323f73a-8bd0-3569-9442-0402dcca7c1b | -4.47613 | -50.0904 | 2025-11-29 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 43705136-663e-3b09-b184-48b88af05bb9 | -4.24883 | -46.11594 | 2025-11-29 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b51d0a2e-4a2d-36a9-a1d8-4aee52c4b78d | -3.95302 | -44.76678 | 2025-11-29 04:14:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e5e82845-b82b-3275-b701-72fa227ec69f | -4.66613 | -44.72287 | 2025-11-29 04:14:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8fe6d84d-8c2d-3cde-9cc7-1faf0c5ed05d | -5.80773 | -40.7906 | 2025-11-29 04:14:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3aa5494c-41c4-304b-a546-539eaa46a01d | -4.40611 | -40.69226 | 2025-11-29 04:14:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b1c6b943-54e8-3422-9353-faf8dd98a47f | -4.74434 | -44.43261 | 2025-11-29 04:14:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c345f66c-e2bb-3430-b531-7745675d0658 | -8.0437 | -43.12853 | 2025-11-29 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 7cbd7176-2cd9-33e0-a5a6-814cdc7bb521 | -5.41192 | -40.72032 | 2025-11-29 04:14:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 66ca8d13-0803-3ef2-a120-cba49f46face | -4.72768 | -45.49882 | 2025-11-29 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README17.md)
