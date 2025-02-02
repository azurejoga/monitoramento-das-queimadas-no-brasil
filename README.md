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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8e7d21f-f073-3a76-a95a-cd9cbcdc6c77 | -17.8578 | -40.1263 | 2025-02-02 00:30:00 | GOES-16 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 86.6 |
| c18cadcf-92bb-35bb-826a-c109dc3fe794 | -17.845501 | -40.1465 | 2025-02-02 00:31:00 | METOP-C | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cb282934-4553-3ccf-843a-f415d97a861d | -17.8409 | -40.127998 | 2025-02-02 00:31:00 | METOP-C | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ad9959ed-8ce9-351e-bda3-4261e19be40a | -20.2733 | -41.6488 | 2025-02-02 00:31:00 | METOP-C | IBATIBA | ESPÍRITO SANTO | Brasil | 3202454 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1fef149c-faa8-343c-8423-de569987d933 | -18.845699 | -39.999199 | 2025-02-02 00:31:00 | METOP-C | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2541f212-fcb0-3175-858d-18e7a9d657f1 | -20.7712 | -41.034801 | 2025-02-02 00:31:00 | METOP-C | VARGEM ALTA | ESPÍRITO SANTO | Brasil | 3205036 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 99b3c471-96e9-3017-825c-e93cd044c15e | -18.843399 | -39.990002 | 2025-02-02 00:31:00 | METOP-C | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f340d925-333d-3f2b-9247-03977f5698cb | -17.843201 | -40.137299 | 2025-02-02 00:31:00 | METOP-C | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4b0664e2-4460-3f61-828d-0a462c4b4352 | 1.944 | -60.844501 | 2025-02-02 01:19:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 566ea554-84bb-3651-b504-cb17c1a51b72 | 2.4544 | -61.3204 | 2025-02-02 01:19:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8714a1f9-25d9-341d-bdcc-b1a8c42fead5 | 1.4112 | -59.965599 | 2025-02-02 01:19:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9ed4fa27-66ec-3872-8389-c0dc0269e4d3 | 1.421 | -59.967701 | 2025-02-02 01:19:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c57ff599-1d07-3e1e-bc8e-39ef76f1ff16 | 1.7089 | -60.333199 | 2025-02-02 01:19:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d271649d-b305-363c-ab29-f76ba26d69ff | 1.711 | -60.323799 | 2025-02-02 01:19:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c2854f2a-632e-34c2-88a7-bf4f307f0a64 | 2.4525 | -61.3288 | 2025-02-02 01:19:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| dde6e6c9-39ed-3650-8276-181fe5e77bed | 2.4427 | -61.326599 | 2025-02-02 01:19:00 | METOP-B | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d01165c5-151b-3dbc-ac50-ce0d72d0c78e | -5.652 | -67.858704 | 2025-02-02 01:19:00 | METOP-B | CARAUARI | AMAZONAS | Brasil | 1301001 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 259b90b7-0235-30e5-83f3-28f61bb46243 | 1.4134 | -59.955799 | 2025-02-02 01:19:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 059af4af-d1a6-3873-9f7b-4d86aca74529 | 1.942 | -60.853298 | 2025-02-02 01:19:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 41572a52-aa6a-3cfc-b6a8-8ed79193c967 | 0.72542 | -59.68208 | 2025-02-02 01:24:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0c072966-ba60-30fc-9ee2-aa10032abeed | 2.45864 | -61.31733 | 2025-02-02 01:26:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 025f066d-e5f5-3c1b-9177-e9a655b98b95 | 3.50177 | -60.79799 | 2025-02-02 01:26:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 196020c7-70d6-3593-afb3-2fbed2c50708 | 3.55266 | -60.36998 | 2025-02-02 01:26:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0a8f1c36-1807-3a65-95ba-2fadbf69fea9 | 1.93654 | -60.38563 | 2025-02-02 01:26:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6f265de6-248a-36fe-a9fa-afffc78ce205 | 1.94673 | -60.84567 | 2025-02-02 01:26:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 3a236856-2318-3b68-9dcf-86a18ee0b89e | 1.42455 | -59.95907 | 2025-02-02 01:26:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 15.5 |
| db5ce410-5093-33e5-9261-7522a27bc53a | 2.44919 | -61.31598 | 2025-02-02 01:26:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 21.1 |
| b71c10a3-17af-3272-ba5c-65f66a76c62e | 1.71585 | -60.3169 | 2025-02-02 01:26:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 48dad32b-bf38-36dc-b2d5-5cf97fffbbe9 | 1.94809 | -60.83588 | 2025-02-02 01:26:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 94d11e05-ff4b-3cf4-a177-7f255f879b00 | 1.71454 | -60.32626 | 2025-02-02 01:26:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.9 |
| bab3e973-8fd2-31fb-9641-7f4c2891d963 | 1.42328 | -59.96823 | 2025-02-02 01:26:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e198e464-6b2c-306b-a715-bfd2cd596a29 | 2.44772 | -61.32617 | 2025-02-02 01:26:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b7fa9e6d-ab52-3e64-9548-a3fe276150e6 | 1.41684 | -59.94864 | 2025-02-02 01:26:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 00e05a1e-63f1-3975-995c-adb74ad52023 | 1.41557 | -59.95779 | 2025-02-02 01:26:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a88fe53f-94d8-3113-b309-92c8723f824b | -18.545 | -39.94574 | 2025-02-02 03:02:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 086ba4ce-1efa-3063-af68-f05acaab07a5 | -18.54633 | -39.93995 | 2025-02-02 03:02:00 | NOAA-21 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 6e60ad53-232b-3bd9-9d3d-32abfa7f3f5d | -18.84373 | -40.00374 | 2025-02-02 03:02:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 69373036-95ba-3a19-801b-f4527684c14d | -18.84509 | -39.99787 | 2025-02-02 03:02:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| e81cccf4-893e-3bc7-8455-6c737e7d601a | -12.15265 | -37.93655 | 2025-02-02 03:25:00 | NPP-375D | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 1ad6a339-f676-3927-9c78-4d09777b29c0 | -12.15694 | -37.93732 | 2025-02-02 03:25:00 | NPP-375D | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 799e4fa0-5dfd-3933-8941-014ecb7b486f | -15.60974 | -39.62342 | 2025-02-02 03:25:00 | NPP-375D | PAU BRASIL | BAHIA | Brasil | 2923902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| b137bdfc-de0e-38a1-b158-a9b315cad8d6 | -17.00386 | -39.41956 | 2025-02-02 03:25:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5c080e74-e844-3725-93d5-8cc53f6d4542 | -17.00289 | -39.42117 | 2025-02-02 03:25:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4b76ee66-08df-306d-bf70-ca72f45de3c5 | -18.84678 | -39.99615 | 2025-02-02 03:27:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 171a9c89-b492-37a8-a4a4-28d9a91084aa | -18.8416 | -39.99964 | 2025-02-02 03:27:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| a5e4d0b5-c83d-3edc-a15c-771e47c259ba | -18.84132 | -40.00212 | 2025-02-02 03:27:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 9189b78a-5685-3986-b3cb-2a16837b5db8 | -18.44324 | -39.83504 | 2025-02-02 03:27:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7b0cd792-9a39-3b26-8e63-89b688e3e629 | -18.8474 | -39.99422 | 2025-02-02 03:27:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 35aa81ef-7a3e-3ef6-bad4-3d4ae0ff6a43 | -18.53627 | -39.79922 | 2025-02-02 03:27:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b1a7a0b6-03c7-3eb1-a925-7a45a28ce16d | -18.84654 | -39.99863 | 2025-02-02 03:27:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 2e5fc151-53ef-3d3f-b829-ecb536237d93 | -18.84243 | -39.99522 | 2025-02-02 03:27:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 9bb2216d-dc0e-3f71-9900-0b86550414e9 | -18.84595 | -40.00058 | 2025-02-02 03:27:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 51742c8f-209d-3e3f-9423-6ef45370d219 | -18.84566 | -40.00307 | 2025-02-02 03:27:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f5f75ac0-56b8-3981-918b-f221fef48fd0 | -18.84219 | -39.99771 | 2025-02-02 03:27:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| ca3ac44a-473a-327d-98f4-8cffe8597701 | -18.54448 | -39.94455 | 2025-02-02 03:27:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| a9ad574f-a57e-39d1-9fd3-6a6a6f53bcd4 | -18.54533 | -39.94015 | 2025-02-02 03:27:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 33415b0c-bcb4-3487-a218-0957e4af7e68 | -18.84076 | -40.00406 | 2025-02-02 03:27:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f3197cfd-22f4-32e9-abd7-1abf1753006b | -18.54058 | -39.80018 | 2025-02-02 03:27:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 59983936-19da-3c45-ab61-88ab0ad0de67 | -18.84511 | -40.00501 | 2025-02-02 03:27:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f7f8d564-e72e-3be4-b279-87755804aa4e | -18.54882 | -39.94552 | 2025-02-02 03:27:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| f7257dcb-9a3e-3dec-bcfc-e1c8628953fc | -6.72472 | -40.05606 | 2025-02-02 03:46:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8cad929d-f9a5-33d0-97b6-1fa7d69ae70e | -6.7315 | -35.45052 | 2025-02-02 03:46:00 | NOAA-20 | SERTÃOZINHO | PARAÍBA | Brasil | 2515930 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3d568fed-25c3-3bcb-a8cf-de710a11708c | -2.91019 | -40.33668 | 2025-02-02 03:46:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 0c6560d1-fd09-3b92-8dfa-dbbe8cafd847 | -13.97386 | -38.9492 | 2025-02-02 03:46:00 | NOAA-20 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 07236ab4-f1f6-3ce8-b89b-19f297dd157c | -12.00168 | -38.1692 | 2025-02-02 03:46:00 | NOAA-20 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1fffa47c-94ad-3bf5-aefe-ba2fc7631b41 | -7.47552 | -34.84336 | 2025-02-02 03:46:00 | NOAA-20 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| beca2450-6a80-3120-99d3-688660b42443 | -12.154 | -37.93432 | 2025-02-02 03:46:00 | NOAA-20 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| c84ff1d2-2727-3765-90d1-c3f1cc399294 | -4.68546 | -37.82002 | 2025-02-02 03:46:00 | NOAA-20 | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f2032553-9a2f-3177-ab5c-c7a0a3649684 | -6.72813 | -35.45002 | 2025-02-02 03:46:00 | NOAA-20 | SERTÃOZINHO | PARAÍBA | Brasil | 2515930 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e630ffec-1e5e-3af5-9fad-f52a8227210b | -13.3595 | -40.00356 | 2025-02-02 03:46:00 | NOAA-20 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b2a91ee3-4c72-3f50-a939-e336bc78e4ce | -7.37793 | -34.88714 | 2025-02-02 03:46:00 | NOAA-20 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 354a7026-cc5f-39e1-9f0a-1d7c78f5aba6 | -17.00075 | -39.41923 | 2025-02-02 03:49:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 68ca4d4d-acae-3b03-9ffe-2084bd1be24f | -20.42247 | -40.45999 | 2025-02-02 03:49:00 | NOAA-20 | VIANA | ESPÍRITO SANTO | Brasil | 3205101 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6be95bf9-83e0-30ce-9c76-d6bfa9f819ab | -17.38206 | -39.52054 | 2025-02-02 03:49:00 | NOAA-20 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 44f4ffa2-63ab-3750-b5f1-9aabc72b3c28 | -18.54475 | -39.94212 | 2025-02-02 03:49:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 5e304eff-2085-3189-b787-3cd34f46b922 | -18.44292 | -39.83514 | 2025-02-02 03:49:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 577e88a3-8ba5-36ab-885c-3b2612413c9c | -18.54015 | -39.79948 | 2025-02-02 03:49:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 48795ca0-055c-3e08-a651-8f54187df2c8 | -17.43629 | -39.24102 | 2025-02-02 03:49:00 | NOAA-20 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c234c111-7de5-3984-9e9e-d790f8d28d5a | -18.54806 | -39.9427 | 2025-02-02 03:49:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 5acbb233-5c1a-36a1-81cd-2a1e177c8523 | -15.60908 | -39.62315 | 2025-02-02 03:49:00 | NOAA-20 | PAU BRASIL | BAHIA | Brasil | 2923902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4184fafe-af8c-3b35-8df6-a575df2783b2 | -18.8418 | -39.99686 | 2025-02-02 03:49:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| d28e41f2-7b83-306a-a42e-80eaf68118ca | -18.53683 | -39.7989 | 2025-02-02 03:49:00 | NOAA-20 | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 594e1337-407d-3478-9edb-9dd8a6b38d54 | -15.9358 | -40.88065 | 2025-02-02 03:49:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2a07d57c-eb04-3112-807c-ef86e23a998d | -19.83702 | -40.08245 | 2025-02-02 03:49:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 881bf601-6264-3259-803d-ec7997ae7e74 | -18.84511 | -39.99744 | 2025-02-02 03:49:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 47.8 |
| 2d91baa4-aa07-3a67-b399-b39620b5d6d9 | -8.11996 | -43.13769 | 2025-02-02 03:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 50f8f44a-9d70-3a9c-b47e-57bfc2656fc8 | -15.93919 | -40.88138 | 2025-02-02 03:49:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a2ce4737-c502-3a3d-a99f-3e0769b7e164 | -30.19119 | -55.28566 | 2025-02-02 03:53:00 | NOAA-20 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 4090aeb2-e70f-3faf-92f7-b68a05fb408b | -30.19259 | -55.28027 | 2025-02-02 03:53:00 | NOAA-20 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 6c23b947-5965-3299-b7a0-8fd41bce066d | -28.64901 | -49.46409 | 2025-02-02 03:53:00 | NOAA-20 | NOVA VENEZA | SANTA CATARINA | Brasil | 4211603 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e1da47b8-dbaf-3bac-9ff6-dd1a38f08b24 | 3.92928 | -59.72908 | 2025-02-02 04:36:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c755debd-ea66-3e7e-8556-a764705307fa | 1.94875 | -60.84203 | 2025-02-02 04:38:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 82f2dfd9-afb8-370f-86aa-ad646cc2dd2f | 1.94779 | -60.83547 | 2025-02-02 04:38:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.0 |
| ef74ed1d-8bd6-39cd-8635-5121b22947ac | 1.94862 | -60.83575 | 2025-02-02 04:38:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b4572d2b-118a-3dbe-bc9b-1c2010a2edb9 | 1.94962 | -60.8423 | 2025-02-02 04:38:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 68af8527-ae51-3b11-8a9a-3153a52949eb | -12.15452 | -37.93585 | 2025-02-02 04:40:00 | NOAA-21 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| d31cf6ed-da2b-30ce-9a79-18abe08a8b0d | -15.93829 | -40.878 | 2025-02-02 04:40:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8835e2a7-a559-38eb-a2ba-f6a8f43d7017 | -15.93792 | -40.88155 | 2025-02-02 04:40:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| aae7a734-5690-3eb8-9318-e8a7eabce2c6 | -15.60772 | -39.62142 | 2025-02-02 04:40:00 | NOAA-21 | PAU BRASIL | BAHIA | Brasil | 2923902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 25796b1b-383e-34cc-95b2-11e34f40f27b | -17.72038 | -54.0815 | 2025-02-02 04:42:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README2.md)
