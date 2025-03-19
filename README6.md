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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72a58410-f425-316c-b3ed-e4803de1cf49 | -30.20347 | -53.60917 | 2025-03-19 04:51:00 | NOAA-20 | SÃO SEPÉ | RIO GRANDE DO SUL | Brasil | 4319604 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 7b16d7c8-7c25-31aa-9855-bbc988550653 | -31.73365 | -53.9026 | 2025-03-19 04:51:00 | NOAA-20 | HULHA NEGRA | RIO GRANDE DO SUL | Brasil | 4309654 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| d9c6bbf5-7e2a-3511-9403-2aeddb410b6b | -30.35703 | -54.2906 | 2025-03-19 04:51:00 | NOAA-20 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 4.2 |
| dfd3ae58-7bf1-3383-a345-f56a404a1c09 | 3.87697 | -60.94904 | 2025-03-19 05:33:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d80943e6-09e0-39fe-b4b4-5f30fb83fe3f | 3.87973 | -60.9451 | 2025-03-19 05:33:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a699039-ba75-3849-8940-634b44c3c6b0 | -16.16245 | -60.11308 | 2025-03-19 05:38:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d10715a9-8e27-3a83-be9e-6c5ab8e00eda | -13.28137 | -54.38438 | 2025-03-19 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3669f45e-1c1e-3fc8-99fc-4e93481182cf | 3.88375 | -60.94427 | 2025-03-19 05:57:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 02cb8cb8-ea13-3e96-9eb5-0029ec998cbb | 3.87928 | -60.94535 | 2025-03-19 05:57:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f50581fe-a25f-3bad-8e68-7db52877b95d | -13.2595 | -54.3283 | 2025-03-19 08:00:00 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| a9dcb8f4-5206-3a11-b035-e9ea1f70c9a3 | -13.2592 | -54.3489 | 2025-03-19 08:00:00 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 17689428-f2e8-3f73-a31a-ae4a758f98ad | -13.2595 | -54.3283 | 2025-03-19 08:10:00 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 3254e99d-9dfe-3b95-a920-5e8fa684854b | -13.2783 | -54.3469 | 2025-03-19 08:10:00 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| f0e9b57b-3b0d-35e0-9213-617cb785acde | -13.2592 | -54.3489 | 2025-03-19 08:10:00 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 686cdaa9-98da-30a6-8e0a-6db45294c77f | -13.2786 | -54.3262 | 2025-03-19 08:10:00 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 52.3 |
| ccef5f2e-7b07-3adb-b4d5-e2f92525063e | -13.2595 | -54.3283 | 2025-03-19 08:20:00 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 8d3ba814-095a-3d89-a096-7836a298801f | -13.2786 | -54.3262 | 2025-03-19 08:20:00 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 59fa8d17-6708-31b2-8db8-f04033c304a9 | -13.2783 | -54.3469 | 2025-03-19 08:20:00 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| af71fc82-fd22-324b-a8e8-c1ce2f7642cb | -13.2592 | -54.3489 | 2025-03-19 08:20:00 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| c811cf3b-0e79-3a49-9ee8-226774d6823b | -12.8995 | -45.0316 | 2025-03-19 12:40:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 1b3dea56-6749-30f3-9256-24ea6d88dacd | -12.899 | -45.0549 | 2025-03-19 12:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 09c2724b-1e1c-3061-bafd-d190fe752fa2 | -12.8995 | -45.0316 | 2025-03-19 12:50:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 202.4 |
| c93b04e5-9f41-3024-8572-60e15484341c | -12.899 | -45.0549 | 2025-03-19 13:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 0ea36f12-80aa-3a4c-b88f-d455ad491c28 | -12.8995 | -45.0316 | 2025-03-19 13:00:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 231.6 |
| 58b38723-32a8-3d4b-b0aa-f5163ad2f817 | -12.899 | -45.0549 | 2025-03-19 13:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 126.0 |
| af7659c7-dd81-31c6-b841-18b87774ab6b | -12.8995 | -45.0316 | 2025-03-19 13:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 301.8 |
| f5c4db89-48b9-32cc-8942-d841036ae2e4 | -12.899 | -45.0549 | 2025-03-19 13:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 40e94c7b-5e00-3d45-bf8a-66c17f02acc3 | -12.8995 | -45.0316 | 2025-03-19 13:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 290.2 |
| 9115f208-e662-3742-92ec-373e4b07d96e | -12.0812 | -45.6195 | 2025-03-19 13:30:00 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 2b6bae91-b3f7-3d39-b55a-ae0d50c8c875 | -12.8995 | -45.0316 | 2025-03-19 13:30:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 204.2 |
| 5c08d1c9-678a-3a52-b642-b2546c6027d0 | -12.0812 | -45.6195 | 2025-03-19 13:40:00 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 5b0a492e-9716-34ee-9709-654abed6ecd7 | -12.0808 | -45.6425 | 2025-03-19 13:40:00 | GOES-16 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| f13dbd98-c088-3077-a771-e241d0055c47 | -12.0812 | -45.6195 | 2025-03-19 13:50:00 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 142.9 |
| 0fd7221b-92c2-3add-8da4-ae151a1f1555 | -17.5193 | -40.0383 | 2025-03-19 14:00:00 | GOES-16 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 98.3 |
| f25b98b6-9f00-380b-82ff-52e4548eaba0 | -12.1 | -45.6396 | 2025-03-19 14:00:00 | GOES-16 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 8871d9d3-e113-348b-a66f-07603231a949 | -12.0812 | -45.6195 | 2025-03-19 14:00:00 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 167.6 |
| db3de50f-fbf2-3216-a811-edd74a9c7b51 | -12.8995 | -45.0316 | 2025-03-19 14:10:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 291.5 |
| 829684e2-0d44-3193-ab13-559a7a9a8a5c | -12.1 | -45.6396 | 2025-03-19 14:10:00 | GOES-16 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 175.3 |
| 2826f3ac-7258-3750-b90a-660e132bbbb7 | -12.0812 | -45.6195 | 2025-03-19 14:10:00 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 174.9 |
| 870c4e29-efd3-3693-b2e7-7c0d2428df20 | -17.5193 | -40.0383 | 2025-03-19 14:20:00 | GOES-16 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 111.5 |
| 3cd5add9-09e1-3e7d-a0b8-bfcbeef41e3a | -12.8995 | -45.0316 | 2025-03-19 14:20:00 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 273.5 |
| 312bdca9-d8aa-3970-bc57-e57ad27eb1df | -12.0812 | -45.6195 | 2025-03-19 14:20:00 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 180.9 |
| 52c8be8a-6a87-3153-b04a-a59e33d3c80f | -12.0812 | -45.6195 | 2025-03-19 14:30:00 | GOES-16 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 158.2 |
| df55e7fc-0763-3705-ae08-f07026798acf | -17.5193 | -40.0383 | 2025-03-19 14:30:00 | GOES-16 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 177.9 |


