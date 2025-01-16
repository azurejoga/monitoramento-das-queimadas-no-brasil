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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6dd8f23-05ed-3d47-a71f-39067c3c0e94 | 2.195 | -61.8156 | 2025-01-16 01:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 6d189638-20f3-3763-8340-73f438d7eb42 | 2.1585 | -61.8536 | 2025-01-16 01:30:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 3c59bdfb-5674-3948-b621-f7c635a8a38f | -21.23999 | -55.91083 | 2025-01-16 01:32:00 | TERRA_M-M | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b81d6749-49cc-3018-abcf-928f811d00b0 | -11.65841 | -58.26027 | 2025-01-16 01:34:00 | TERRA_M-M | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1033291e-2a7a-3386-9983-80fd68f4603e | -16.11339 | -58.16667 | 2025-01-16 01:34:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 31c3b66b-dfc9-3952-a795-3121bfd8ef07 | -16.11717 | -58.19431 | 2025-01-16 01:34:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.1 |
| 49fd0cf5-738f-379f-9758-7b843312762d | -16.11591 | -58.18509 | 2025-01-16 01:34:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 22.9 |
| 5372e665-d6fb-345b-ad0e-db32aa23eb64 | -15.38316 | -57.42268 | 2025-01-16 01:34:00 | TERRA_M-M | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0e8c3e40-89bc-3e6b-b673-336d751e354e | -16.11465 | -58.17588 | 2025-01-16 01:34:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 34.3 |
| 91e57d1a-a42e-30e3-a108-e0059ebaab8a | -2.26829 | -54.5066 | 2025-01-16 01:36:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| a62f1d51-1419-39e1-a57f-66c7b30898ff | 1.17126 | -60.49466 | 2025-01-16 01:36:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4ce0047b-6fe2-3caf-991d-37175b312d2c | 2.11311 | -61.82088 | 2025-01-16 01:38:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 221db5f6-84d1-3d82-bfc7-c3ae5a82644d | 2.53238 | -60.58415 | 2025-01-16 01:38:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 78c2c00b-1d41-39d4-98e4-8fd5d7f6f008 | 3.1429 | -60.7034 | 2025-01-16 01:38:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 9c732866-3c7b-3211-a48d-88086f8080d5 | 1.8824 | -60.48736 | 2025-01-16 01:38:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 07dfcf68-b740-34ac-88eb-ccf2270fc57d | 2.17996 | -61.85714 | 2025-01-16 01:38:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 38.4 |
| ad50f518-c12d-3fe2-8bdf-63ce86fcbd2f | 2.16992 | -61.86466 | 2025-01-16 01:38:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 93b0c4f8-cb18-3de5-9c51-0f18fee66cac | 2.54008 | -60.59446 | 2025-01-16 01:38:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 1d06021a-6785-3cce-a746-904ac8d8bc7b | 3.14415 | -60.69435 | 2025-01-16 01:38:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.8 |
| fad35d1a-dd36-3e0d-8544-f39d4015b6ed | 2.28886 | -60.21442 | 2025-01-16 01:38:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 13.1 |
| b0667c74-4ca3-3888-a6aa-037aa710b8ac | 2.10286 | -61.81365 | 2025-01-16 01:38:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f28e6d0e-c441-32ab-ba93-9d319219173b | 4.41143 | -60.59196 | 2025-01-16 01:38:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 46eed1d0-407d-3961-806a-c38b68ce8d9d | 2.11434 | -61.81212 | 2025-01-16 01:38:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 3d20d43a-4dff-3091-a847-f3e9319b52a7 | 2.11189 | -61.82965 | 2025-01-16 01:38:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 4c2a2c8a-c0c8-35a3-8a60-ce7434f8bdd5 | 1.29154 | -60.43208 | 2025-01-16 01:38:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 095156e0-daa8-3347-bc35-e8929cee027c | 2.54134 | -60.58538 | 2025-01-16 01:38:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 5de3d8d4-02b4-3889-a7eb-c01ab0dcea12 | 4.83564 | -60.5909 | 2025-01-16 01:38:00 | TERRA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5b3b9805-e940-3622-b385-c9caf8541ea9 | 2.17114 | -61.85589 | 2025-01-16 01:38:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 1e77a2ab-9f3b-388c-a33c-15b26fe5a08d | 2.16111 | -61.86342 | 2025-01-16 01:38:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 0c9b228f-5b02-3c7f-aa2a-16550515d7f8 | 2.17874 | -61.86591 | 2025-01-16 01:38:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 7ef011bf-fa72-350a-8176-a294698c2e83 | 2.16233 | -61.85465 | 2025-01-16 01:38:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 98e5dc0c-533c-383b-8b93-303b8d670eb7 | 2.28757 | -60.22371 | 2025-01-16 01:38:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a126a3d7-0dd3-376e-b763-c438e374653b | 2.1767 | -61.8722 | 2025-01-16 01:40:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 37deaa18-a06f-304e-9f2b-ad1ab76bde43 | 2.195 | -61.8156 | 2025-01-16 01:40:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 35.6 |
| f0feb794-6850-399b-839f-176ff05a1d00 | 2.1585 | -61.8536 | 2025-01-16 01:40:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 3c88b561-bc27-3567-9748-bb4cd8f32614 | -2.907 | -54.4916 | 2025-01-16 01:40:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 0741b380-0f25-3672-a061-87f999f689c2 | 2.1767 | -61.8534 | 2025-01-16 01:40:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 61.1 |
| b783d8f7-6fd0-3704-9784-5cd477d007e4 | 2.1767 | -61.8722 | 2025-01-16 01:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 37.2 |
| ff7fe8fa-d54e-3ee3-9c18-20268f5d8a4a | 2.1767 | -61.8534 | 2025-01-16 01:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 6b066239-4d09-3f3f-a6d3-937febdcd6e8 | 2.195 | -61.8156 | 2025-01-16 01:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 51.5 |
| ba23ab64-8cfa-3b0e-a683-f6d20d4758c0 | 2.1585 | -61.8536 | 2025-01-16 01:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 50.4 |
| a487f480-9fed-32e0-b539-4eded4b1c34e | 2.5437 | -60.584 | 2025-01-16 02:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 33.6 |
| 5adf84b5-ded8-36d0-b15e-57f4354f6eab | 1.3583 | -60.3121 | 2025-01-16 02:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 40d59b65-aefd-3f47-8211-7be525a87581 | 1.3583 | -60.2931 | 2025-01-16 02:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 0c0a60f5-a3e1-3d32-ab67-a9883bbe7ffc | 2.5255 | -60.5843 | 2025-01-16 02:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 80fc4cc8-2f75-374a-abfc-d24f485d3f7e | 2.5437 | -60.584 | 2025-01-16 02:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 7b2ce271-633a-3e24-8bd9-17dea4c63628 | 2.5255 | -60.5843 | 2025-01-16 02:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 210cc199-8d02-388d-9133-7c1b3874c8c8 | 2.5437 | -60.584 | 2025-01-16 02:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 5f9c3c1c-6f11-30cf-890e-7bf8f0c9d271 | 2.5255 | -60.5843 | 2025-01-16 02:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 59.4 |
| a27fa7b1-49de-3c4c-bb81-3d48291f01b2 | 2.5437 | -60.584 | 2025-01-16 02:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 2d0f13f4-bb00-3544-800c-8e1a86e13d7f | 2.5437 | -60.584 | 2025-01-16 03:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 39.7 |
| a76571be-38a6-33a4-9cd1-7363b1785041 | -8.73618 | -35.70655 | 2025-01-16 03:19:00 | NOAA-21 | CATENDE | PERNAMBUCO | Brasil | 2604205 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| ec95ce3b-1d17-3a5b-92df-c7758365b66f | -8.74059 | -35.70705 | 2025-01-16 03:19:00 | NOAA-21 | CATENDE | PERNAMBUCO | Brasil | 2604205 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| d860418c-e113-3f1d-9831-66f051309d6e | -7.47697 | -34.84293 | 2025-01-16 03:19:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 62610b91-f8a1-3cd2-8b82-b4930fa0d38a | -7.37794 | -34.88739 | 2025-01-16 03:19:00 | NOAA-21 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3a3f7185-b422-359c-91bd-0fd4a95e9cd9 | -7.46464 | -35.25073 | 2025-01-16 03:19:00 | NOAA-21 | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3aa3a2e2-f966-3141-b516-2f4eeec7373b | -7.53019 | -35.29416 | 2025-01-16 03:19:00 | NOAA-21 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| dc40d315-72bb-30eb-ad01-5c951733f148 | -7.52949 | -35.29823 | 2025-01-16 03:19:00 | NOAA-21 | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| c75786e7-4b2e-3fc0-b763-e896d8d8b506 | 2.5255 | -60.5843 | 2025-01-16 03:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 2e6ea780-2584-383b-b20d-015c52f49d50 | 2.5437 | -60.584 | 2025-01-16 03:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 75e6cf9e-dcb2-3419-813c-e3d6521ca090 | 2.5437 | -60.603 | 2025-01-16 03:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 7a0f0fce-6821-3fea-a9f4-c2d45fe32d2d | 2.5437 | -60.584 | 2025-01-16 03:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 63.2 |
| e1ad991a-5910-3bce-9aea-d7a00e2615d4 | -7.37833 | -34.88671 | 2025-01-16 03:42:00 | NPP-375D | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ed9f312f-aa27-3258-bf03-39a41ce83058 | -6.72667 | -35.22777 | 2025-01-16 03:42:00 | NPP-375D | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4dc0492a-9558-38e4-98a6-fbad9fe58870 | -7.53043 | -35.29742 | 2025-01-16 03:42:00 | NPP-375D | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fbe2aa38-3671-3bcf-a230-9bc120545944 | -5.8737 | -35.42068 | 2025-01-16 03:42:00 | NPP-375D | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9cd2c650-c590-3d5e-a13f-b0430fbb847f | -7.52711 | -35.29688 | 2025-01-16 03:42:00 | NPP-375D | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1683b9e3-9a6f-362c-90cc-1e7a06540a2d | -7.53098 | -35.29392 | 2025-01-16 03:42:00 | NPP-375D | TIMBAÚBA | PERNAMBUCO | Brasil | 2615300 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| dad5192e-bdff-30d9-8e23-4b6302bea69c | -6.51251 | -35.35782 | 2025-01-16 03:42:00 | NPP-375D | NOVA CRUZ | RIO GRANDE DO NORTE | Brasil | 2408300 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ab8eb653-b592-38b8-a95e-84d27c6d923e | -6.71011 | -35.0076 | 2025-01-16 03:42:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a8ed5c69-9726-3a19-9c24-7e60d6b7f38b | -6.73001 | -35.22826 | 2025-01-16 03:42:00 | NPP-375D | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 930c18a9-ed63-342b-968c-3eef0097eb27 | -10.44859 | -36.75688 | 2025-01-16 03:44:00 | NPP-375D | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 8869cdcd-c94b-35c5-bee8-b7e73b2cd047 | -10.44582 | -36.75281 | 2025-01-16 03:44:00 | NPP-375D | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f15e0cdc-9c73-32cc-ab50-0964f206cfc9 | -10.44526 | -36.75633 | 2025-01-16 03:44:00 | NPP-375D | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9e4dce0b-160e-336f-9af7-7c761b394c3b | -10.44915 | -36.75335 | 2025-01-16 03:44:00 | NPP-375D | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 97b042f0-15ee-3ede-8917-4e702a46b309 | 2.5437 | -60.584 | 2025-01-16 03:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 12e06bf4-ee4a-3af8-b8b5-eec4842ad863 | -6.7309 | -35.2231 | 2025-01-16 03:50:00 | GOES-16 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 79.7 |
| 0a8a3e6d-e808-3663-9b04-8919fdfefa31 | 2.1767 | -61.8534 | 2025-01-16 03:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 8543cedf-8145-3650-8d59-c43167feee39 | 2.1585 | -61.8536 | 2025-01-16 03:50:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 8918c9bc-10c9-37de-ab53-457446f99876 | 2.5437 | -60.584 | 2025-01-16 04:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 40.1 |
| b44fc6ca-4358-3e9d-8b41-3accd15fef75 | -5.87265 | -35.42017 | 2025-01-16 04:04:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e05fa509-30c8-3685-aac8-4ed3348176c9 | -5.87514 | -35.41973 | 2025-01-16 04:04:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 6be8454b-0936-3e08-aeb2-b8ea5ede7feb | -5.87326 | -35.41606 | 2025-01-16 04:04:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 52a6ecc1-d8bb-31fb-8d77-8c5506f14c42 | -5.87695 | -35.42083 | 2025-01-16 04:04:00 | NOAA-20 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fb743094-37a4-3adf-95c3-31ae6fa52738 | -6.51099 | -35.36182 | 2025-01-16 04:06:00 | NOAA-20 | NOVA CRUZ | RIO GRANDE DO NORTE | Brasil | 2408300 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0014bd71-a801-3390-8c53-86ff11f0868f | -6.51161 | -35.35762 | 2025-01-16 04:06:00 | NOAA-20 | NOVA CRUZ | RIO GRANDE DO NORTE | Brasil | 2408300 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f16a2898-dccc-348e-8497-c2e82a3be54d | -10.44681 | -36.75399 | 2025-01-16 04:06:00 | NOAA-20 | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a7b61d61-9f56-37f5-bf5d-a813923bca5a | 2.1767 | -61.8534 | 2025-01-16 04:10:00 | GOES-16 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 54.0 |
| c494e08e-fa23-3803-8dc0-6f58e6bcf15c | 2.5255 | -60.5843 | 2025-01-16 04:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 34.5 |
| f2756941-1f81-31c6-9c3b-a904234cdb45 | 2.5437 | -60.584 | 2025-01-16 04:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 5ff9bb16-d01d-34ed-b570-ce8dfecd095c | -19.50939 | -55.31657 | 2025-01-16 04:10:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0a994731-dca5-3d7c-8ec5-d47fa5e06dc5 | -19.5056 | -55.31826 | 2025-01-16 04:10:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4f5058d7-3ea4-37f9-8124-80c284e846b4 | -23.84644 | -50.41748 | 2025-01-16 04:10:00 | NOAA-20 | FIGUEIRA | PARANÁ | Brasil | 4107751 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f8b06d0f-ed29-3a5f-97fa-9418fecb228f | -19.50651 | -55.31419 | 2025-01-16 04:10:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 459e7636-d873-3cb4-ac1b-dbead43f6723 | -27.11581 | -50.76315 | 2025-01-16 04:12:00 | NOAA-20 | FRAIBURGO | SANTA CATARINA | Brasil | 4205506 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7264bca7-3e80-3912-be6f-8bf9af64654c | -29.9815 | -51.20307 | 2025-01-16 04:12:00 | NOAA-20 | PORTO ALEGRE | RIO GRANDE DO SUL | Brasil | 4314902 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| a96e1adc-96a2-3a85-91cb-7396e15fa063 | -29.97786 | -51.20217 | 2025-01-16 04:12:00 | NOAA-20 | PORTO ALEGRE | RIO GRANDE DO SUL | Brasil | 4314902 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 6ce374a2-8b99-3c15-b304-3641f7b1c198 | -29.68135 | -53.8549 | 2025-01-16 04:12:00 | NOAA-20 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 124280a6-c1e7-3254-af22-7e398725db24 | -27.11444 | -50.76556 | 2025-01-16 04:12:00 | NOAA-20 | FRAIBURGO | SANTA CATARINA | Brasil | 4205506 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9c3e810d-dd15-3d44-88d5-7774d56d8dff | -33.30727 | -52.99213 | 2025-01-16 04:14:00 | NOAA-20 | SANTA VITÓRIA DO PALMAR | RIO GRANDE DO SUL | Brasil | 4317301 | 43 | 33 | nan | nan | nan | Pampa | 3.4 |


[Clique aqui para ver as próximas entradas](README3.md)
