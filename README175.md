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

## Dados Diários - Página 175

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 034697c5-ad9c-34f6-8165-f9c0b80be156 | 3.12328 | -60.64647 | 2026-10-08 05:40:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8d14f27e-db6f-3738-a8da-0b4b1cda0e70 | -1.52326 | -54.53831 | 2026-10-08 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ccb5fcf-0c07-3961-b0d5-4d834170cb50 | 2.01452 | -61.09028 | 2026-10-08 05:40:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9846f297-a8a6-3d94-85ec-904ed0ed4013 | 3.1294 | -60.6419 | 2026-10-08 05:40:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4cdd65b9-7d1f-3987-97ea-a97328a7eac4 | 1.70091 | -55.61774 | 2026-10-08 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 60220cec-e99d-341e-809b-25fab6588618 | -1.18565 | -55.67392 | 2026-10-08 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 96597af2-ba66-3926-992f-4a1a1247e187 | 1.69792 | -55.62082 | 2026-10-08 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ed9920b-1ded-3235-b736-5e1bf21a9d6e | 2.88648 | -60.29816 | 2026-10-08 05:40:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f94041ee-8555-37d0-b9e6-70ebe7a4d4eb | 1.98475 | -59.92806 | 2026-10-08 05:40:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1295e229-8a3f-38ca-a72b-490dfb493ed5 | 2.43693 | -50.81874 | 2026-10-08 05:40:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 713c4768-09e3-30fa-93c5-4e7569c30bca | -2.10328 | -52.06781 | 2026-10-08 05:40:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75a82319-3f67-334f-8765-1db5c51811b4 | -1.52652 | -54.55066 | 2026-10-08 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1f9701ca-5236-31d6-b398-86fb994414bf | 1.6972 | -55.62276 | 2026-10-08 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52457987-8d40-3126-aa6b-605d299be70d | -1.5366 | -54.55206 | 2026-10-08 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| ad012aec-1c04-3866-8ba5-6aca9b22d829 | -1.50461 | -54.82534 | 2026-10-08 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b906019-ae0d-3655-bb3e-a8f6432b3e82 | -1.47614 | -54.54753 | 2026-10-08 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bcc6b3e-7720-36d6-bddb-3b8d30310f33 | -1.10094 | -54.16389 | 2026-10-08 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23a54760-1665-3cab-a1df-614b4e5c6433 | 0.78832 | -59.19984 | 2026-10-08 05:40:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26042e51-20b1-3a45-8b73-ce382ee3ebae | -1.71774 | -55.44389 | 2026-10-08 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 99a234a9-5f0d-3e51-ae52-cbf872f630d8 | -1.4566 | -54.76809 | 2026-10-08 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ff503063-e940-39e0-b0b7-30de28a56044 | -1.42506 | -54.6119 | 2026-10-08 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2c96fb9-62b4-337d-b912-67713fb39485 | -1.45351 | -55.25004 | 2026-10-08 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3482bb8d-d978-3282-86d5-fa505118da67 | 3.54745 | -51.28175 | 2026-10-08 05:40:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e3fd162-b5fc-3dcf-803a-393cce919aa8 | -1.10751 | -54.15558 | 2026-10-08 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7d0c32b-5fcf-3810-a386-e9d95797f392 | -1.53112 | -54.55424 | 2026-10-08 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 4630da6d-138d-30d7-a0e1-d6f81a6270f3 | 2.43848 | -50.82782 | 2026-10-08 05:40:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4b503e26-d900-3d94-b4d4-350ae77d5fc5 | 0.44396 | -60.53438 | 2026-10-08 05:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 40ac073e-464b-3436-beaf-580a2cd860ff | 4.31749 | -60.35813 | 2026-10-08 05:40:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8fc33eb-75ac-3c53-8ef9-df54fff5307e | 3.12606 | -60.64242 | 2026-10-08 05:40:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3a6ed819-2637-3bb6-9af3-fd865e911b15 | 0.56643 | -50.80237 | 2026-10-08 05:40:00 | NOAA-20 | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 43f40946-3c89-319c-bc2d-c2f382f46ad2 | -1.10559 | -54.16771 | 2026-10-08 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9fb8b1ca-f96d-3a01-8cc7-3dc592565b8c | 1.68807 | -55.64467 | 2026-10-08 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 496b513a-4eb9-32ae-9b57-ef00f970cdbb | -0.99503 | -53.74313 | 2026-10-08 05:40:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1addea52-91ef-3467-8e9a-b50cde70ea53 | 1.70834 | -55.60764 | 2026-10-08 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 26ab72ba-9927-3953-8be3-aecf0cab3cc1 | -1.20601 | -55.68972 | 2026-10-08 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e621a978-4667-39f0-9d73-531df0ba15e1 | 1.72092 | -55.60111 | 2026-10-08 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 909549c3-a1d8-334d-8789-130a99fd3238 | 3.1652 | -60.59299 | 2026-10-08 05:40:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5224a32f-2cda-3b97-8fc5-362010d8ed79 | 3.8524 | -61.32068 | 2026-10-08 05:40:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9567bc6-6521-3c46-af9c-48f19ceb5484 | 3.31351 | -60.05423 | 2026-10-08 05:40:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c818d23e-bb30-3053-8e13-54464bdf04ca | 2.90848 | -60.94232 | 2026-10-08 05:40:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09ff99a5-cabf-35af-896a-c889ceb6d8e9 | 1.69724 | -55.61646 | 2026-10-08 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ced4d36-ec38-32cc-bbff-1bad7e002719 | -1.20648 | -55.69184 | 2026-10-08 05:40:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 063e4b04-8409-39e6-8f2b-f42e79a3ef9d | -1.08802 | -54.11225 | 2026-10-08 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 674dcdf8-655b-373c-892d-d313612f154c | -1.5357 | -54.55787 | 2026-10-08 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 559670e0-042e-3273-ad38-3a83f96b5d41 | -1.52371 | -54.53536 | 2026-10-08 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a558858e-9c27-3664-964a-f6868d102ee2 | 4.31359 | -60.35513 | 2026-10-08 05:40:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c4bf49c-63e3-3efe-a24d-731759d71850 | 0.45194 | -60.54063 | 2026-10-08 05:40:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9bf06a92-2d94-333a-9655-d50238231a66 | -1.53067 | -54.55713 | 2026-10-08 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| d7b301a5-0812-35cb-9f6f-15761f883db1 | -1.45271 | -55.25519 | 2026-10-08 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3cfac160-6e5d-3d39-bf59-011bea21ce02 | -1.47671 | -53.61584 | 2026-10-08 05:40:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 143714a6-a44a-3d9d-bbf1-e130d22cfd01 | -1.28462 | -54.55878 | 2026-10-08 05:40:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1f6824f7-41c5-3c65-ab63-431be71d58a9 | -1.52605 | -54.81741 | 2026-10-08 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4b3fdff9-a21a-38bd-a460-61d484881d08 | -1.51928 | -54.56437 | 2026-10-08 05:40:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fbb020dc-b210-3611-9ff7-76b0a9b9bbec | 3.15302 | -60.62379 | 2026-10-08 05:40:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 00662a1c-9026-378e-b125-48cf03a002d3 | 4.42662 | -60.91235 | 2026-10-08 05:40:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74aa6ae8-29d6-395b-bf90-b2020bf6ed33 | 4.26937 | -60.03813 | 2026-10-08 05:40:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 997db476-d13b-3639-8a97-27f976c75f28 | 3.15222 | -60.63469 | 2026-10-08 05:40:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6e4c8bd0-08c1-3b28-b436-87d17ce94cae | -3.59283 | -61.63557 | 2026-10-08 05:42:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ecdbdb8a-267b-3f81-978c-54e4c5fc1669 | -7.74691 | -54.95392 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71a6397d-2430-35e8-b6cd-93a80b40c707 | -3.1884 | -58.64909 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73a855a4-23bb-3d1e-a529-ba63457cb624 | -3.31248 | -53.862 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2ee33123-c26c-347e-a87f-d13574ed09a7 | -4.91464 | -55.857 | 2026-10-08 05:42:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6b32cab2-02c7-3c0f-bc81-6b56341dea22 | -7.75323 | -54.94788 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| df1b1dce-5488-3db9-a3a5-877d2c188ce2 | -3.17429 | -58.63687 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 1170dd2e-3e9c-3732-8093-6d02a2d8e676 | -2.78948 | -54.08474 | 2026-10-08 05:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dfe0e5ad-c377-3590-a961-460363e31e35 | -2.39 | -56.13525 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3af4ba88-d236-360a-8188-3799966b1fca | -3.27856 | -54.04796 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe259dbb-a634-35a2-8f9e-19b931470dcc | -4.10541 | -52.06585 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 649cabc8-795c-3c5b-92c0-8173d0701b33 | -2.99809 | -54.12426 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5677d30-cc3f-3549-876f-c350250fab7b | -5.91105 | -53.88264 | 2026-10-08 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9b4cec0-432a-3eea-9969-16035beb5565 | -3.03084 | -59.21665 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e93d7599-977b-3f40-b2e4-3a42a5cca680 | -2.39072 | -56.13057 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f43ca86a-91e8-38bd-abf2-aebead9dc253 | -3.05913 | -54.21991 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a5630ce-1960-351f-af10-95ea0e69bae7 | -6.99573 | -59.12361 | 2026-10-08 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63d1c251-3024-30e9-b918-747493bab0f8 | -3.04455 | -53.92374 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 268cb0cc-e993-3f75-a509-87244050f42c | -2.57394 | -56.15967 | 2026-10-08 05:42:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 875cf7c8-b55e-34d0-a65e-252f08a186a0 | -3.5759 | -61.61063 | 2026-10-08 05:42:00 | NOAA-20 | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 74af8733-31e9-3cbf-8671-d38b92638e8c | -3.71096 | -59.6497 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05f808be-2506-355b-80f4-a6f252f0beac | -3.47977 | -54.63216 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 265dd485-8242-3c44-902f-fc4ea875def3 | -3.86178 | -56.00005 | 2026-10-08 05:42:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6f29cdf9-3d76-3047-b57c-bbec8030b8c1 | -3.36526 | -58.2016 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65c453ae-5f0c-3184-afdd-46f6328bc6a2 | -4.37522 | -54.75154 | 2026-10-08 05:42:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 020840b9-b828-3da5-ac55-4d82ff870dcc | -3.12051 | -53.79824 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 49f679db-d158-3f6d-a3d6-d72c2b9e7175 | -3.29433 | -54.08751 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0ed7a7df-5432-3a6c-877d-295897336d3a | -3.66813 | -60.61809 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a073d586-a141-34bc-9b4e-53e01287da26 | -3.65862 | -60.63276 | 2026-10-08 05:42:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82da8b8f-0eaf-3b07-8398-e296ca6c76c7 | -3.32514 | -50.18557 | 2026-10-08 05:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e783a31c-ea4a-317d-80d2-9f58f4780015 | -2.94982 | -59.16554 | 2026-10-08 05:42:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d264b477-ed76-3470-a4ea-d87cc1653148 | -3.29957 | -53.87404 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| beabc22b-2e99-39ca-baf9-33383f3cdcc3 | -3.43623 | -56.94005 | 2026-10-08 05:42:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 60cb8233-9f93-3246-b0d3-8b913bfb22a0 | -3.04224 | -53.90252 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6176cc2-0d92-3a83-a881-3ab7ffaa0832 | -4.13931 | -54.02856 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed6087db-ed81-3428-9ff7-6e2ae13e7f0c | -3.81059 | -60.47182 | 2026-10-08 05:42:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a174639e-18b8-3547-b79d-7a99d656e039 | -3.29565 | -54.04352 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f84b4e3f-5eac-3ba9-bced-e8ebcc9dcbb9 | -3.98995 | -59.22474 | 2026-10-08 05:42:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 928e1093-0ee4-37c5-b03f-cb6d8634af4b | -3.25727 | -54.0442 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b6369664-be2e-3d27-a770-b505b421a23a | -2.93614 | -54.18031 | 2026-10-08 05:42:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dac02bfb-9e98-311a-b3cc-622b43bd6eac | -4.07055 | -51.03957 | 2026-10-08 05:42:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 88825641-c159-32b3-991d-b4dac7ab050f | -3.57485 | -59.45811 | 2026-10-08 05:42:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c1e124d-a5df-377d-a6c1-7c1fbfaba6d2 | -3.26659 | -54.01873 | 2026-10-08 05:42:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README176.md)
