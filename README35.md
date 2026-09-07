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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 903dbf45-5bec-32bc-87e5-6e217b2fcf00 | -13.24002 | -61.72983 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 0c539ba5-67b9-319f-9ec0-450ce05f2485 | -7.24578 | -59.52723 | 2026-09-07 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99227769-6a46-3585-937d-9dcf94dd4807 | -13.29759 | -61.72857 | 2026-09-07 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7c92b28a-5851-3294-bb33-ce03c1fb12fe | -6.63726 | -59.44413 | 2026-09-07 05:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f3a84650-d81f-3989-b51b-17297017f419 | -13.21488 | -61.73667 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| abab37b8-986d-3f82-b9de-4d4807b950f9 | -13.26122 | -61.72602 | 2026-09-07 05:25:00 | NOAA-20 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 16c4d37c-b7f9-39a3-af0a-8ee6a9254551 | -28.67153 | -49.05151 | 2026-09-07 05:27:00 | NOAA-20 | JAGUARUNA | SANTA CATARINA | Brasil | 4208807 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| be293968-d8ad-3852-8f95-a00610126ccf | -3.1461 | -60.6696 | 2026-09-07 05:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| a75e15d6-1318-3d56-9e9c-30cac663a32f | -13.2286 | -61.7549 | 2026-09-07 05:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 2766be76-ad3c-3fbf-a19b-e19ad29d4c3d | -13.3004 | -45.2442 | 2026-09-07 05:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 116.4 |
| fb1e898a-e760-39f1-adc5-e3af2f6deab7 | -13.2097 | -61.7367 | 2026-09-07 05:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 44ed84e2-c2a4-3b00-aa4f-5fc7f486e152 | -3.1461 | -60.6696 | 2026-09-07 05:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 1308fa11-945f-3b4d-afe0-d4f5fefac198 | -13.2479 | -61.7148 | 2026-09-07 05:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 09812c1c-fd82-3c6f-b3e6-6ecdb1a60c89 | -13.2289 | -61.7161 | 2026-09-07 05:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 97560089-5b22-38fd-905f-2840af20d3ad | -13.2477 | -61.7342 | 2026-09-07 05:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 65b8d5e3-0445-3b4f-b883-03271c74cefe | -13.3009 | -45.2209 | 2026-09-07 05:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 0ea3b615-f676-3c29-863d-102329c06da3 | -13.2287 | -61.7355 | 2026-09-07 05:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 234.5 |
| dc0e0dc6-6cdb-3869-afbc-ed5d10b03ea1 | -13.3203 | -45.2177 | 2026-09-07 05:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| d8846cb6-564c-3c09-a44d-9c47789d2671 | -13.3198 | -45.2409 | 2026-09-07 05:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 5c080718-ba2c-35a1-bd19-1a2a433c7a8e | -3.1461 | -60.6696 | 2026-09-07 06:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 3029e21e-49e2-3dfe-bc19-d99047641a0c | -13.2287 | -61.7355 | 2026-09-07 06:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 137.4 |
| 91f4d571-1c37-3cd3-946d-978cf2ebc60d | -13.2477 | -61.7342 | 2026-09-07 06:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 255013b4-b107-35a1-858d-13f03452a919 | -13.2097 | -61.7367 | 2026-09-07 06:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |
| f1ef8f1f-4c83-3cea-b7ec-aabec098436a | -13.3198 | -45.2409 | 2026-09-07 06:00:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 01e73105-bdeb-3656-bf6a-c344a7e0333f | -3.13976 | -60.63502 | 2026-09-07 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9c33f7ef-4db2-3f3c-a8ac-d81fe7626c35 | -3.77001 | -61.75462 | 2026-09-07 06:08:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9e2c816-1ee9-3351-b6e8-c8d3fa4e1518 | -8.54132 | -63.87816 | 2026-09-07 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 854a8bdf-1f61-30a1-94e2-664f8e3566c1 | -3.38893 | -61.31281 | 2026-09-07 06:08:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d526ed3d-ef78-3779-b4df-e3b609be1984 | -3.18673 | -61.14087 | 2026-09-07 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9621bebf-09b8-3258-8b4d-7d0754f7b672 | -3.61278 | -60.57199 | 2026-09-07 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6fee67dd-9e27-3d4a-92bb-287f49df2447 | -3.1425 | -60.65659 | 2026-09-07 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9e761528-a324-3777-8a66-930de2dfa245 | -3.14538 | -60.63547 | 2026-09-07 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4881de02-2087-308a-834c-5d424f897e78 | -8.52146 | -63.8723 | 2026-09-07 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b465edc1-f0ea-3d74-ab05-7276c6415dfb | -3.14126 | -60.66487 | 2026-09-07 06:08:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 226af974-49cd-379e-83f9-7216407489e1 | -5.26697 | -60.16191 | 2026-09-07 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d60957cd-6bed-3164-975a-3478c7ef57dd | -3.61705 | -60.57412 | 2026-09-07 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 31ea2f38-f29c-3972-81b7-45133d6d4992 | -3.15406 | -60.65808 | 2026-09-07 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b08a1ed2-432e-3d0c-ab80-ec9711e90ded | -3.38622 | -61.32336 | 2026-09-07 06:08:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28dc4666-f460-3f39-a12d-85bcc078c568 | -3.09539 | -61.07035 | 2026-09-07 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93bfe924-f9ae-3d90-ae7f-e77fb6146400 | -3.14768 | -60.66122 | 2026-09-07 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e639ec3e-e0a8-3b62-b9e6-304caec7e3b8 | -3.6391 | -59.5473 | 2026-09-07 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 76db664c-9fb2-3f52-9f01-e665a0b8404f | -5.28399 | -60.12526 | 2026-09-07 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6d8d5b7-9f0e-3ffa-88c1-9d74bc76a01a | -3.61645 | -60.57837 | 2026-09-07 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c0bdac4d-71ab-39f3-8a2f-31366bce89a4 | -3.83318 | -60.76568 | 2026-09-07 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2d08daf-bc03-3e04-a6b1-3082b6190047 | -5.26765 | -60.15714 | 2026-09-07 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f9289919-4f2c-3b2d-92f0-a390d91717a4 | -3.37966 | -59.42503 | 2026-09-07 06:08:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5fcc3b7d-c7ab-35f9-9854-684d38ccddfc | -4.2938 | -59.95567 | 2026-09-07 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67a40db5-4f87-30ca-b413-cb30097fa3a5 | -8.54559 | -63.88484 | 2026-09-07 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 28b734df-52c6-309f-81af-7546ca761333 | -3.14707 | -60.66578 | 2026-09-07 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 4cc758db-060d-3ca1-ab6d-a2761f96b80d | -5.30677 | -60.14342 | 2026-09-07 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 98b3bb89-5cc0-3bb8-9461-1a85de6c5a0c | -4.28626 | -59.96428 | 2026-09-07 06:08:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2467312d-4451-39b0-9e07-6c98b53b02b5 | -3.76381 | -59.42411 | 2026-09-07 06:08:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2c8ee542-b1f6-350f-b54e-b6fe5c4bf584 | -3.15117 | -60.63651 | 2026-09-07 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e314f87e-17d4-34ff-9a4c-2920d255db56 | -3.38726 | -61.32399 | 2026-09-07 06:08:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9157360d-cb97-31e1-9753-78eb4e58dc40 | -3.24826 | -60.66383 | 2026-09-07 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99bcf737-9692-3c62-b187-e087d23d70d0 | -3.14768 | -60.66168 | 2026-09-07 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4fe99b23-35dd-3c78-b617-c256c5c897ac | -5.26706 | -60.15709 | 2026-09-07 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 08b4125f-0374-34fd-9e29-fce3898402c4 | -3.38111 | -59.41496 | 2026-09-07 06:08:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1b078361-1409-31cb-a9a4-8136d1edf38e | -5.82997 | -60.2518 | 2026-09-07 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7038a74a-a1af-3141-b63c-13bd1f29375e | -3.39451 | -61.31368 | 2026-09-07 06:08:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42f534dd-ac3a-319a-a079-107f98f30bd2 | -8.52692 | -63.87005 | 2026-09-07 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2e15b49-4473-3a95-8d2d-28c38c3505c7 | -3.14129 | -60.66441 | 2026-09-07 06:08:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f888f12b-e3ad-32e0-ac30-3441e3a9a9e1 | -5.27324 | -60.15802 | 2026-09-07 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 97a4182f-1433-3357-a78b-0274e5047e86 | -3.24822 | -60.66471 | 2026-09-07 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 81616f19-75a5-3c25-a170-65530f6ac599 | -5.26693 | -60.11777 | 2026-09-07 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7537655e-4d63-3dac-b0e1-1874f49dfedb | -5.3061 | -60.14824 | 2026-09-07 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b97e03dc-052d-3a42-9b57-c805aaa05b88 | -3.07974 | -61.53249 | 2026-09-07 06:08:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 71387114-1aa7-32ac-8c03-da73e966555d | -3.14188 | -60.66027 | 2026-09-07 06:08:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 856d2ec0-2bae-3c3e-9858-b9fc4bf3d849 | -3.61765 | -60.56987 | 2026-09-07 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 28750ed1-2c73-37fc-8577-c16d735c36e8 | -3.61177 | -60.56895 | 2026-09-07 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5eb6d2f9-befb-344e-99db-7c3b65b823dc | -3.14188 | -60.66075 | 2026-09-07 06:08:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b3c59a60-2e2d-3865-8b6f-f7866f674830 | -3.38675 | -61.31963 | 2026-09-07 06:08:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 005d6d82-c023-3b50-a128-52edadbde828 | -3.76506 | -61.75025 | 2026-09-07 06:08:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 656225a4-8f75-39ea-a68e-37334828d572 | -3.82736 | -60.76476 | 2026-09-07 06:08:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5dd8f149-66b8-3329-bd30-692afc02677e | -3.14709 | -60.66533 | 2026-09-07 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 044c4c3d-6ef8-3167-aa18-349bc78a2237 | -3.76901 | -61.76167 | 2026-09-07 06:08:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8db1704-dbc8-3bdc-83e8-96bcd0ef5cc5 | -8.53159 | -63.87376 | 2026-09-07 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c7f5c702-ac9d-3afa-89f2-aac5143edb4d | -3.14364 | -60.64775 | 2026-09-07 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 585d6c4f-a952-3475-a733-0d89ce6d21d4 | -3.76951 | -61.75815 | 2026-09-07 06:08:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0a8feab-75c2-3533-955f-d897ccab7a8c | -3.38781 | -61.32027 | 2026-09-07 06:08:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16a600ab-9bdc-3f65-8e25-9ee4ac958971 | -3.14826 | -60.65707 | 2026-09-07 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 0dc14de9-225b-3cbd-a36a-80d6ae4ecf1b | -3.76456 | -61.75379 | 2026-09-07 06:08:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4557ebdf-77e8-3cb0-8123-b2a726dc7b23 | -3.37482 | -59.41388 | 2026-09-07 06:08:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a831c751-a983-3aa6-a11a-45e1e8a27372 | -8.33306 | -72.80257 | 2026-09-07 06:08:00 | NOAA-21 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 06fe8d34-543f-3a39-857c-68ff629aee26 | -3.15135 | -60.63703 | 2026-09-07 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fbbc47eb-1014-304a-86b7-738a0f52b451 | -3.38569 | -61.32711 | 2026-09-07 06:08:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a758a37-9d05-3fa0-b547-f8d4a7072286 | -8.52653 | -63.87303 | 2026-09-07 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d78c3c73-6f63-32c8-84d1-8584ded47b76 | -3.18728 | -61.13704 | 2026-09-07 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c4a91b9-44b4-31c3-a180-aa16c7cdad6d | -3.38039 | -59.41999 | 2026-09-07 06:08:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f046f5a-7c58-3c45-82a6-3f180bbb22a2 | -3.13915 | -60.63911 | 2026-09-07 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8b0d86be-dc77-3d48-9671-104b07803b99 | -5.27383 | -60.15806 | 2026-09-07 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c72f059-fe13-357b-915d-f909d18d228b | -3.39074 | -61.3317 | 2026-09-07 06:08:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5512d7e6-7328-3b8c-a668-d88c231f24c7 | -5.3019 | -60.13284 | 2026-09-07 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e1300a8d-bc87-3eab-b82e-a89f6e4ce462 | -8.53666 | -63.87446 | 2026-09-07 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9736a3b8-6eb0-33fb-aa31-bd6867e4a877 | -5.30125 | -60.13765 | 2026-09-07 06:08:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 062036db-bd19-3a81-831f-712fdf939e10 | -3.13793 | -60.64734 | 2026-09-07 06:08:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49ba418a-23f4-31bb-9fbf-e02cd9f2e4db | -3.14373 | -60.64827 | 2026-09-07 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c4b69e61-af9e-3af8-8d9b-e515bddcf95f | -3.14651 | -60.66943 | 2026-09-07 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| fdc2de2b-4b4b-3958-af75-22d05c806657 | -3.14247 | -60.65609 | 2026-09-07 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 10feddda-4398-3d46-a2e7-5163458f0cdd | -3.25406 | -60.6648 | 2026-09-07 06:08:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README36.md)
