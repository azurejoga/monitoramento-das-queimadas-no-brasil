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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60f4e342-a9cd-3ce5-a2f9-7d84652d7d58 | -5.83637 | -45.0127 | 2026-10-06 06:42:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 7e984bfa-5041-39c2-8249-6d1fc1fe13ea | -2.87053 | -54.12064 | 2026-10-06 06:42:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 42d0ed5c-c07e-32c1-8f31-f62fe9f19787 | -6.31718 | -43.34169 | 2026-10-06 06:42:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 20b7a8aa-1448-3ba6-a3ef-47458ab16d76 | -8.69873 | -45.22014 | 2026-10-06 06:42:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b3a61981-a979-3181-9c2c-76b7c411f769 | -3.07441 | -54.24304 | 2026-10-06 06:42:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| ced716cc-5389-32ac-8cdc-19807e045ba3 | -3.50934 | -54.59663 | 2026-10-06 06:42:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 8b3a82dc-7f49-347d-9179-ceec9f96830b | -5.84515 | -45.014 | 2026-10-06 06:42:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| ddc7386c-05b6-34e6-a8f1-c8b11eabb2a0 | -2.86505 | -54.15521 | 2026-10-06 06:42:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 84259b2d-97ef-3608-b043-3b6a55e65dcf | -3.50733 | -54.64125 | 2026-10-06 06:42:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 279234d7-9ed0-30b4-aab2-becdecbbab84 | -6.89524 | -43.67944 | 2026-10-06 06:42:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 29de43ec-0430-3d07-a6ea-1f40b9982c2e | -3.02604 | -53.88661 | 2026-10-06 06:42:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| e4ae9e99-bbcf-3a47-8793-7375ad21e354 | -6.00864 | -47.39164 | 2026-10-06 06:42:00 | AQUA_M-M | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| a215ae68-297b-3feb-93f9-b233f4e8df04 | -5.74994 | -46.67464 | 2026-10-06 06:42:00 | AQUA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 4df72a15-38d8-302d-bc0a-334e8fc4ea9c | -6.72248 | -44.27747 | 2026-10-06 06:42:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| cb53d8fd-43a7-3fe2-9367-f3ecde7bb652 | -3.93949 | -42.98793 | 2026-10-06 06:42:00 | AQUA_M-M | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ea1b6eee-58e1-36a1-b42b-1e30c0cc13ce | -9.25283 | -45.65634 | 2026-10-06 06:42:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 17f12019-54ec-3401-9708-c9e7224288df | -6.00713 | -47.40131 | 2026-10-06 06:42:00 | AQUA_M-M | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 7029c7f5-e417-3815-8d52-6d8c8181b811 | -2.95043 | -54.14628 | 2026-10-06 06:42:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 637afa22-1c8e-37b7-8222-99df7df83c35 | -8.57937 | -45.65678 | 2026-10-06 06:42:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e8edf0fd-29e0-3682-9908-87b81723ee63 | -5.84382 | -45.02277 | 2026-10-06 06:42:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| dabd7a5b-7f64-3bc8-bf67-09b70dd891e2 | -8.70007 | -45.21117 | 2026-10-06 06:42:00 | AQUA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 326d88e6-6ccc-3d17-9226-8fafa443331e | -2.9412 | -54.13955 | 2026-10-06 06:42:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.2 |
| fd71ba5e-43f9-3b7c-b9a1-650410a3e566 | -6.93175 | -43.67142 | 2026-10-06 06:42:00 | AQUA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 19.9 |
| eeba7545-471b-3c26-8cb6-688144ba4fe8 | -8.58814 | -45.65808 | 2026-10-06 06:42:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a8196e14-1858-38bf-bc06-aaf77a152e7b | -3.00427 | -54.11985 | 2026-10-06 06:42:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 5eda324d-f9a5-3a3a-b8b3-e972c3e86806 | -4.35705 | -47.77464 | 2026-10-06 06:42:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 2e49a295-8c29-33df-91d5-f1bea621af4a | -2.87681 | -54.12934 | 2026-10-06 06:42:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 7a9f3e26-0de9-390a-8d85-f8b7d40edac7 | -4.45615 | -47.91576 | 2026-10-06 06:42:00 | AQUA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| b4ffbbc1-e677-3a4b-adbe-f66480d09b8f | -3.51341 | -54.60529 | 2026-10-06 06:42:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 55541275-f69e-3b3f-889a-08d92f308f96 | -5.8276 | -45.0114 | 2026-10-06 06:42:00 | AQUA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 37.4 |
| da387ac0-0560-32cf-9dca-8fe293220ebb | -3.03084 | -53.88237 | 2026-10-06 06:42:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 33.9 |
| 13977747-b308-3261-b758-1791c69f54c3 | -5.61196 | -44.84375 | 2026-10-06 06:42:00 | AQUA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3c3c5596-55a6-3912-b064-ad403d02912f | -3.50349 | -54.63266 | 2026-10-06 06:42:00 | AQUA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 3cfea55d-572b-3c91-b82a-6c04c68b6775 | -11.82359 | -44.69478 | 2026-10-06 06:44:00 | AQUA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 360642f9-dc57-3f0b-a0e1-f62e8fabfbd4 | -11.7191 | -43.63717 | 2026-10-06 06:44:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 438f00f2-0cfd-3bc2-b7b8-9f9fc37ec4fe | -11.28698 | -45.52522 | 2026-10-06 06:44:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 22dd97be-955f-352a-a60c-c07c47784b38 | -11.75128 | -44.93538 | 2026-10-06 06:44:00 | AQUA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| cd39e17b-c8be-37a7-ba3f-e89fda733c6c | -11.28077 | -45.50552 | 2026-10-06 06:44:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 56b861f8-79b3-3cc2-82ea-1f2ec357cfbf | -11.2732 | -45.49501 | 2026-10-06 06:44:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 76eba30a-34f1-35dd-8eaf-7ea24cd76577 | -11.27186 | -45.5042 | 2026-10-06 06:44:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.6 |
| f250d196-05e4-33f8-9777-71eb6486a1b4 | -11.27808 | -45.52389 | 2026-10-06 06:44:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 69bab12f-b09a-3b68-83dd-79bd1fb1dbb5 | -11.28832 | -45.51603 | 2026-10-06 06:44:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 199.6 |
| 2059f383-aba4-3e42-824f-a7041434cd3d | -11.26038 | -45.51475 | 2026-10-06 06:44:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| b2b03215-597e-3a83-9669-e4236a4b012a | -11.27942 | -45.51471 | 2026-10-06 06:44:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 243.4 |
| a79ae542-2307-328d-825c-ce18e87a4288 | -11.28968 | -45.5068 | 2026-10-06 06:44:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 2c9f50c8-a310-3836-a5bc-80df80471890 | -12.76513 | -44.88008 | 2026-10-06 06:44:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 61a6b880-38e5-39ee-ade4-73aa5c1231f1 | -11.26918 | -45.52256 | 2026-10-06 06:44:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 39.7 |
| a49d5385-7b12-31b5-8567-d6f5b869ddfb | -11.27052 | -45.51338 | 2026-10-06 06:44:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.8 |
| e65eb95f-5ca7-37fa-b8d9-1834e519947a | -11.29724 | -45.5173 | 2026-10-06 06:44:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 03f9574f-c4c6-3369-a0ac-1a62d7718270 | -11.26174 | -45.50559 | 2026-10-06 06:44:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| d34b2959-bb87-3302-a4dc-4c385c450e76 | -8.60269 | -72.73135 | 2026-10-06 07:05:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 940fe05c-e08a-3d76-9291-46c035ac150b | -11.26 | -45.53 | 2026-10-06 07:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7e80de35-8d4b-38d1-95c1-6034bd631c14 | -11.29 | -45.54 | 2026-10-06 07:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| da35a58e-18c4-3b34-84ae-696a2dfdf856 | 0.45479 | -60.53781 | 2026-10-06 08:20:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 6b14e489-e0cc-3abd-b6e0-e947fdfdccb8 | 0.43958 | -60.53284 | 2026-10-06 08:20:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 803ad18b-0a60-3478-99af-a48bdc9025b3 | 0.45431 | -60.53061 | 2026-10-06 08:20:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 21.0 |
| d60082f0-6638-3d2e-af47-43bf104d6bc8 | -9.72409 | -65.08246 | 2026-10-06 08:22:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 3c2c5d8d-cdaf-39ec-b297-34cd7d20a2bc | -11.2607 | -45.5078 | 2026-10-06 09:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 458df630-2f5b-3407-8a28-b384975dee1d | -11.2607 | -45.5078 | 2026-10-06 09:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 339c8eff-5a96-3cd8-baff-65027e737622 | -11.2798 | -45.5052 | 2026-10-06 09:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 7ef8c96e-3396-3445-8b5f-04b6121c5b27 | -11.2607 | -45.5078 | 2026-10-06 10:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 20e062ed-48ae-337b-8654-3c55402e273e | -11.2798 | -45.5052 | 2026-10-06 10:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 3d0d67aa-3306-3318-8321-4444ea8874f4 | -11.2798 | -45.5052 | 2026-10-06 10:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.2 |
| c5e67433-5e9c-36c3-acf8-23acd62fac61 | -11.2607 | -45.5078 | 2026-10-06 10:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 96.8 |
| 24cdc1e4-a0d6-330b-9edd-14027957f7e8 | -11.2607 | -45.5078 | 2026-10-06 10:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.3 |
| c39f784f-0be3-36f0-b92d-df8d39ef0086 | -11.2798 | -45.5052 | 2026-10-06 10:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 7f806a75-4208-3dba-bc22-a822fd6f73f2 | -11.2607 | -45.5078 | 2026-10-06 10:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 0fbf4a24-5351-39fe-aa93-ec082596d949 | -11.2798 | -45.5052 | 2026-10-06 10:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 4a564067-83ea-3388-85fb-b11331cac24e | -11.2607 | -45.5078 | 2026-10-06 10:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 107.2 |
| c975042f-33ac-319e-86d3-8b2a819ca22a | -11.2603 | -45.5308 | 2026-10-06 11:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| ee71acc9-649d-31e1-9146-7adfae5499af | -3.32893 | -39.53385 | 2026-10-06 11:00:00 | TERRA_M-M | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 3c0c0009-8d1c-3158-b46e-0329d6606edf | -3.32787 | -39.53948 | 2026-10-06 11:00:00 | TERRA_M-M | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |
| ee985ba4-183a-3ed1-84f1-3026c773923c | -3.47832 | -39.63258 | 2026-10-06 11:00:00 | TERRA_M-M | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 27.3 |
| aa4f8d03-f2a8-3c4a-be87-51001c08c62b | -3.46825 | -39.63117 | 2026-10-06 11:00:00 | TERRA_M-M | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 5432bd4b-80aa-309a-98eb-24303494fb26 | -4.9358 | -38.9873 | 2026-10-06 11:02:00 | TERRA_M-M | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 64fe556d-0b21-374a-9082-76e62794f604 | -11.65659 | -43.65779 | 2026-10-06 11:02:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 5d30a004-403e-3df7-8097-e4869208e9af | -7.86148 | -37.91174 | 2026-10-06 11:02:00 | TERRA_M-M | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 17a4baad-c648-3a3c-bfc2-70b7cb6ed119 | -7.8531 | -38.15763 | 2026-10-06 11:02:00 | TERRA_M-M | SANTA CRUZ DA BAIXA VERDE | PERNAMBUCO | Brasil | 2612471 | 26 | 33 | nan | nan | nan | Caatinga | 6.7 |
| bfad77f3-75ac-33af-b422-ea08f1fbf03e | -7.86278 | -37.90279 | 2026-10-06 11:02:00 | TERRA_M-M | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 73694273-6847-306b-b83b-8da4ec6dd7da | -8.30162 | -39.38575 | 2026-10-06 11:02:00 | TERRA_M-M | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 699dbc3b-5b1c-38d3-8504-570d7dc1661f | -8.62304 | -37.29492 | 2026-10-06 11:02:00 | TERRA_M-M | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 33eb36df-4997-3386-bf6d-0cd4cd499ffe | -6.97681 | -39.21742 | 2026-10-06 11:02:00 | TERRA_M-M | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 095b3774-4eac-3058-93c7-1f31bdd787d4 | -6.60938 | -37.88508 | 2026-10-06 11:02:00 | TERRA_M-M | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 6.4 |
| dd88a1fa-cefe-3003-81c2-65f2a806afe8 | -4.91027 | -38.7913 | 2026-10-06 11:02:00 | TERRA_M-M | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 0538e207-45d3-39d6-9b8a-1ab523d41633 | -6.97832 | -39.20737 | 2026-10-06 11:02:00 | TERRA_M-M | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| a5cde982-99e4-34aa-8731-a7a13cc2a966 | -6.0245 | -42.28009 | 2026-10-06 11:02:00 | TERRA_M-M | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 76934361-5628-341b-b277-dfa1489f3c97 | -11.6514 | -43.65045 | 2026-10-06 11:02:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 1a305067-6cd2-39ed-bce2-ab2847c2e279 | -7.86043 | -44.15794 | 2026-10-06 11:02:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 29.8 |
| f123f733-de86-3fc3-bc0b-f69f38d1c4d3 | -5.26148 | -37.06633 | 2026-10-06 11:02:00 | TERRA_M-M | SERRA DO MEL | RIO GRANDE DO NORTE | Brasil | 2413359 | 24 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 6dd29b9c-ef63-3346-a9ef-fe8951dd54a9 | -8.30308 | -39.3758 | 2026-10-06 11:02:00 | TERRA_M-M | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 31.3 |
| cef0f21a-732c-37dc-a4e5-bef20dcb5a39 | -17.49625 | -39.50852 | 2026-10-06 11:04:00 | TERRA_M-M | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 8d1f4ce0-550d-35cb-baf6-65fe70c28223 | -13.49482 | -42.58337 | 2026-10-06 11:04:00 | TERRA_M-M | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 6.6 |
| e1826c46-4838-33b5-b4c2-30fbd3052e6a | -17.37616 | -40.94487 | 2026-10-06 11:04:00 | TERRA_M-M | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 5a6fbfc4-296d-3aca-8d3c-1c28ac223156 | -14.5597 | -41.63905 | 2026-10-06 11:04:00 | TERRA_M-M | MAETINGA | BAHIA | Brasil | 2919959 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| f774b5f1-b187-3d12-9aca-a12ed12c3e83 | -18.00644 | -42.63607 | 2026-10-06 11:04:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 82fa021e-1ad1-3b82-89ff-393d9b3f95d1 | -18.01633 | -42.63771 | 2026-10-06 11:04:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 110bebe6-a8c2-3fea-a9fb-8427464d4d33 | -18.00834 | -42.62434 | 2026-10-06 11:04:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| fc50d44a-22f3-3844-8c46-bf67a2213263 | -17.37468 | -40.95467 | 2026-10-06 11:04:00 | TERRA_M-M | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| cb9ad92b-e957-3297-b7c5-2f7e5fb0fe3d | -15.53087 | -42.63303 | 2026-10-06 11:04:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.6 |
| 6503b3d7-bce2-35d9-9465-a77002a5a516 | -14.88862 | -41.7581 | 2026-10-06 11:04:00 | TERRA_M-M | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 28.5 |


[Clique aqui para ver as próximas entradas](README80.md)
