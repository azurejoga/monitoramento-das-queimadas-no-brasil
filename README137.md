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

## Dados Diários - Página 137

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03d2e6f0-a3e0-3e01-a78e-d46930a28cf4 | 4.25152 | -60.02188 | 2025-10-02 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c61577a-04c5-38b6-a327-1285d23782b1 | 2.59076 | -61.43452 | 2025-10-02 05:40:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 52feaa9b-232b-3e9c-991c-ec2bc67007fa | 4.25684 | -60.03423 | 2025-10-02 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 60fded9c-5c8b-33fe-92b5-c682c6315cfb | 2.74695 | -60.2346 | 2025-10-02 05:40:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6424b69d-0815-3fdc-92cc-5e5f9c911ada | 4.25849 | -60.02195 | 2025-10-02 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8a1997fb-db6d-314b-937b-1692fcab09e7 | 4.25195 | -60.0266 | 2025-10-02 05:40:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e44546f5-f498-39a9-bdf7-60815251dd30 | -3.81001 | -51.31611 | 2025-10-02 05:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ccb63195-4ac4-3fb0-9710-815683c7d2bb | -3.80306 | -51.31467 | 2025-10-02 05:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ecd054a3-6942-3865-b320-c01449313b59 | -9.63627 | -63.20265 | 2025-10-02 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 444d7100-bb77-382b-ac15-064de7670d02 | -9.86857 | -63.49104 | 2025-10-02 05:44:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ad8ec59e-3ac2-3a45-847e-605cd0e5b28b | -15.28484 | -56.79498 | 2025-10-02 05:44:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc7a4072-4bdd-31c8-8f33-95cc1f7292d7 | -9.83767 | -63.185 | 2025-10-02 05:44:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3309231e-d2e6-382c-b036-73a24718fe7d | -8.76234 | -64.19997 | 2025-10-02 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 153dca79-e0ac-32e6-a8ce-ce90b91f682f | -9.4344 | -63.71568 | 2025-10-02 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5d28bf4-60de-3523-b0bf-31ed7e75fee2 | -15.36088 | -56.97733 | 2025-10-02 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d209e50-aff6-3e3b-a28e-f4175daacd23 | -9.4033 | -63.69542 | 2025-10-02 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e5c74c19-b3aa-3dcf-81ac-c0fca10f5686 | -10.15721 | -61.94635 | 2025-10-02 05:44:00 | NOAA-21 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0f02d36-272f-3af0-a089-a2e3b6c20159 | -9.4114 | -63.68871 | 2025-10-02 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db1e1c79-28fd-3b57-a2ff-cee3349c535e | -10.01293 | -63.97717 | 2025-10-02 05:44:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75355a6e-0c57-3e20-8d06-ffeecec27047 | -12.42251 | -54.35271 | 2025-10-02 05:44:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7941c579-0433-317e-8ed2-f820df52f314 | -9.49478 | -63.13346 | 2025-10-02 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1d391dbf-5bde-39f7-a711-97594ec7315c | -15.32688 | -56.95189 | 2025-10-02 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c49a207b-6f8c-3413-b71e-8f28de3ae027 | -9.08415 | -63.69608 | 2025-10-02 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b0ceb7f0-4116-3164-97e8-709e5449f03e | -10.16535 | -63.44315 | 2025-10-02 05:44:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 057f0b64-8603-33fe-8b5c-099d8f8cfb87 | -9.40735 | -63.69208 | 2025-10-02 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76805894-b4db-33ab-b501-95696abd4a70 | -9.40794 | -63.68818 | 2025-10-02 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ecbfef40-06c9-36fa-867a-51799411c138 | -12.1212 | -64.09617 | 2025-10-02 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1aebc351-ccbc-3f32-bd38-c2dff2ecd9eb | -15.0048 | -55.27459 | 2025-10-02 05:44:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c2b44715-50df-30d5-b9b5-1a84b0124a31 | -9.63686 | -63.19858 | 2025-10-02 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a863a311-bf50-3933-9fb3-de247f55c6ee | -9.49539 | -63.12937 | 2025-10-02 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9bdaea6a-cc07-33de-a2d9-97e5ca3450ea | -9.64675 | -62.84156 | 2025-10-02 05:44:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fb905797-ff96-3c93-8d6a-80435badb434 | -9.91396 | -63.50488 | 2025-10-02 05:44:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6861c067-52fb-3f7b-b7b0-f681ff831381 | -9.64975 | -62.84629 | 2025-10-02 05:44:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 25ae20e2-10ea-3a9e-9171-7b6cba2b3492 | -9.40852 | -63.68431 | 2025-10-02 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a21c8bd-0935-3219-aecf-ae9552163ec0 | -9.40042 | -63.69099 | 2025-10-02 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 50a339e5-fcb8-3efd-b2c7-9f901a372bb2 | -9.65037 | -62.84208 | 2025-10-02 05:44:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5c3777b6-02e6-31ca-9cce-39a141a6e9a1 | -12.90201 | -60.35075 | 2025-10-02 05:44:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b02bea6a-1706-3beb-8bd7-bf34f026acb7 | -9.40676 | -63.69596 | 2025-10-02 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b39e0ab-3604-38c3-b8bb-115ecf03bd68 | -15.27904 | -56.79446 | 2025-10-02 05:44:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4efdf45-1887-3915-a1a4-d0072bda10bc | -12.19381 | -63.38835 | 2025-10-02 05:44:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9fd4328-738e-3663-b7c9-e22e189d6f85 | -9.40447 | -63.68766 | 2025-10-02 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21fa9855-0f23-3877-8aa8-413dc24249c5 | -15.00203 | -55.27444 | 2025-10-02 05:44:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dc01a345-504e-3828-9aec-b81dc01ff911 | -15.36695 | -56.97478 | 2025-10-02 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05b8ece4-473f-37ec-9f2e-38e0d8e05133 | -9.49798 | -63.42949 | 2025-10-02 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9445fdcf-36f8-3840-ae23-a708e9fdb0aa | -9.13823 | -61.44218 | 2025-10-02 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3bc7b6c7-d534-361f-b898-812ea00e59b3 | -9.64613 | -62.84575 | 2025-10-02 05:44:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 15cbc6a2-e495-3a4e-a202-340071cd0af1 | -12.41474 | -54.36341 | 2025-10-02 05:44:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 253ba01f-660d-3f3e-99a2-e6c69886defd | -9.40388 | -63.69154 | 2025-10-02 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6c95bd17-830f-3343-b4c0-ab0cd145e998 | -9.58391 | -64.51868 | 2025-10-02 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da08b269-0e8f-3133-a797-dce74d6a429d | -9.43093 | -63.71515 | 2025-10-02 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 145e1cb6-daf6-3ff9-9e4b-7e78abc0d924 | -12.11771 | -64.09562 | 2025-10-02 05:44:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 182a6f4a-f9cc-3c48-885e-3def7ba9409b | -10.47505 | -62.4519 | 2025-10-02 05:44:00 | NOAA-21 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f258e3c8-ebde-3722-83a7-6856aa2d53d8 | -9.6284 | -64.15542 | 2025-10-02 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 741306f8-a3af-3235-8a2c-3cf4ed1905c6 | -10.16887 | -63.44374 | 2025-10-02 05:44:00 | NOAA-21 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b711fa6-b226-3c89-9608-60452adf8215 | -9.49812 | -63.18395 | 2025-10-02 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| acddfc0a-e6d1-32e9-ba2a-662204a9ee73 | -9.72283 | -64.20428 | 2025-10-02 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79624347-ffc8-3340-aa26-302ad2f25c60 | -15.32722 | -56.94882 | 2025-10-02 05:44:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d6069926-27ab-3d06-b8a5-f49ef3f55f0b | -6.32127 | -43.04639 | 2025-10-02 05:55:00 | AQUA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| ee7ee4b0-cb10-3f51-a624-f61e088741b7 | -11.45026 | -44.96556 | 2025-10-02 05:55:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6c2d76d0-bcd6-33dc-ba98-a8f97d3eb00c | -9.93656 | -43.75164 | 2025-10-02 05:55:00 | AQUA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| d76cbf17-b00b-3581-9f8b-dd993d5b6db9 | -11.1637 | -47.26955 | 2025-10-02 05:55:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 03042036-68c7-3ba2-a4a0-8f2fca4d404d | -6.68876 | -42.82804 | 2025-10-02 05:55:00 | AQUA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 7fb64386-cfb3-3d7b-b1bb-a0b67646b88b | -6.54835 | -45.21813 | 2025-10-02 05:55:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 6fc46dfe-4379-3b93-9405-1702bfdcdcbb | -10.65078 | -48.50023 | 2025-10-02 05:55:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 6e1b4426-ac93-3591-8317-6bf426c80979 | -5.62056 | -43.22475 | 2025-10-02 05:55:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 16422a1c-4be7-3c20-8a47-804b82ae26ac | -11.00022 | -46.57913 | 2025-10-02 05:55:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| c357fb31-e906-3617-9a9e-a1d54ea861ea | -9.91718 | -43.74886 | 2025-10-02 05:55:00 | AQUA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 250236f4-38e7-331f-ae00-b0c484af511e | -10.83747 | -45.36961 | 2025-10-02 05:55:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f084d7e6-a380-3125-8cf4-fdb75218fff5 | -6.56076 | -43.87661 | 2025-10-02 05:55:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8ee95960-78bd-376d-99ee-78de137c5257 | -10.26234 | -50.32441 | 2025-10-02 05:55:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 75b9e83b-07ef-3ecc-b8a0-58e39cadabd6 | -3.34785 | -43.19086 | 2025-10-02 05:55:00 | AQUA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 271d5a8e-24a2-3e0a-8a2e-2c1e5cca572b | -11.46888 | -45.0154 | 2025-10-02 05:55:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 41.7 |
| d22e797a-a2c3-3bc3-832c-0e377858b8eb | -9.92688 | -43.7502 | 2025-10-02 05:55:00 | AQUA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 183.7 |
| 9077073a-45c8-3894-82be-c9acdd69189a | -9.93812 | -43.74074 | 2025-10-02 05:55:00 | AQUA_M-M | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 19.9 |
| 8227df98-5990-393e-876e-e0aa850d2293 | -3.4621 | -50.09102 | 2025-10-02 05:55:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 47e2aa8a-88aa-3c1d-8afe-3a85ef5645b5 | -2.26463 | -47.85214 | 2025-10-02 05:55:00 | AQUA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| fa1f7657-a7a6-3563-8cd9-8bf16fbe4a0c | -10.26796 | -50.30592 | 2025-10-02 05:55:00 | AQUA_M-M | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b93ef839-13d6-3940-a913-dc590d65cba2 | -5.48104 | -42.75498 | 2025-10-02 05:55:00 | AQUA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| d4a6a4df-5fad-31e5-827f-b6a58504e9d5 | -11.19349 | -47.19193 | 2025-10-02 05:55:00 | AQUA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e133abf3-a2b9-319d-841a-0e634a926dd2 | -10.99755 | -46.59695 | 2025-10-02 05:55:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 35568294-9dba-328c-b1bd-46708cfa27a3 | -9.40663 | -47.58057 | 2025-10-02 05:55:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 3b48bcf0-e691-327d-bc81-39125e223d65 | -10.69508 | -48.57618 | 2025-10-02 05:55:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 44d3495f-1afc-347c-a23d-f9b6d8783623 | -10.83612 | -45.37883 | 2025-10-02 05:55:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 4e6d5240-8eaa-3de4-b3d9-96c3cbbeb435 | -7.36366 | -47.04218 | 2025-10-02 05:55:00 | AQUA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 58efb56b-570c-3a6c-98fb-473ca04e7421 | -10.98743 | -46.60452 | 2025-10-02 05:55:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c562aa5d-9e6e-3ed4-9d98-7c75cdceec53 | -7.41038 | -45.19069 | 2025-10-02 05:55:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5b72d327-1336-3b3c-859d-cd10fd694d7b | -11.01168 | -46.56265 | 2025-10-02 05:55:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 92b1fac4-7e18-3bdb-84fd-cd8bf29e016b | -10.84514 | -45.37741 | 2025-10-02 05:55:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| afa9e73b-ba2c-335b-9b23-1d8f8d6a98e4 | -3.08856 | -47.00443 | 2025-10-02 05:55:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| a7c26318-0dd5-3d56-974d-2380a82452ca | -3.34928 | -43.18114 | 2025-10-02 05:55:00 | AQUA_M-M | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 30c21e88-984c-3d64-8ee8-151aba5bd134 | -11.3573 | -44.96689 | 2025-10-02 05:55:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 57f5451b-0227-39d1-b653-b8d5ab74c2d9 | -5.61907 | -43.23516 | 2025-10-02 05:55:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b601352c-8105-333c-805a-c237926be953 | -11.09464 | -47.84066 | 2025-10-02 05:55:00 | AQUA_M-M | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b73f2c69-e924-3d10-94a5-e46920984cfb | -5.30758 | -44.80409 | 2025-10-02 05:55:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 87a4793e-15df-3ac7-b80a-a44abafc7454 | -5.69628 | -42.69341 | 2025-10-02 05:55:00 | AQUA_M-M | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 34f77908-cbf8-37fa-93d3-2f4b335186a2 | -11.45745 | -44.96325 | 2025-10-02 05:55:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5fc91064-aa25-391f-be2a-b95d67d10820 | -10.22217 | -48.22878 | 2025-10-02 05:55:00 | AQUA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 1e7a753d-3c12-3fac-8775-144066cf66a6 | -6.0541 | -44.18316 | 2025-10-02 05:55:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1e5abb5a-2d38-323e-86d5-94f16a17a3fc | -9.40244 | -47.5452 | 2025-10-02 05:55:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| e9d062c6-f292-3b64-9100-ec36d813aa7b | -7.77373 | -42.54575 | 2025-10-02 05:55:00 | AQUA_M-M | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |


[Clique aqui para ver as próximas entradas](README138.md)
