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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a37f20db-c92f-3863-a2cc-32cca5144edc | -4.59735 | -49.62496 | 2026-10-05 04:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 502700bd-743f-3adc-b002-98b6dd20d218 | -2.9478 | -54.13275 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a228767b-c72c-3379-b7a3-6eb9d1a69de6 | -3.30719 | -53.85807 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea2c36a2-ae6d-3655-b1e9-a704d7ee31a1 | -3.11918 | -53.76123 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 919b5cc3-b49a-332d-a37d-4fce9e2df0b2 | -3.10347 | -53.72886 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e4cf64f5-e216-3a0b-b73f-7b29cb5b0fed | -3.50635 | -54.60546 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b92a4814-e561-3ace-bf95-7e870663a81a | -2.95567 | -59.16075 | 2026-10-05 04:57:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7492f519-d308-3c26-a6e7-1d1e2a133092 | -7.47002 | -55.01395 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d121d2a6-34b6-3258-a4f6-6f5c5ea370af | -3.1312 | -53.72953 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f94fe285-99b9-3081-a311-c511e0def214 | -2.81461 | -54.10852 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff594d98-ba69-32f4-a233-c13655efe64f | -4.03957 | -50.76085 | 2026-10-05 04:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48e150b4-a7d6-32a6-8bb7-a6069c135e83 | -3.15413 | -50.44431 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| f69e864f-d270-3ad0-a5c0-43b0903b0b3d | -6.26226 | -52.86372 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4142601-9d92-3fb2-861b-6f7b705f18a1 | -3.19067 | -54.10543 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21876601-3ab2-30c5-a3c1-8cf222c6bdb8 | -2.94091 | -54.13164 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 43b6ce52-3eb5-3339-9cfe-0330036ead0d | -3.08182 | -54.17272 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| c01300da-7750-36c5-a86a-3f21ae4c5248 | -6.2639 | -52.85336 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a36c0569-dfbc-3e0a-b226-4c7e69a2c61a | -7.44004 | -63.55968 | 2026-10-05 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 03e2ea69-ec66-3b6b-a1e0-0de4b9b1d714 | -6.05894 | -53.47895 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8eaae7c1-66ff-395d-a481-bf8bc040a30a | -3.94522 | -40.93479 | 2026-10-05 04:57:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3eed9b9c-4bcb-3aaa-a81d-5b62d273060b | -3.12209 | -53.74302 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 628803b4-f00f-35d1-9f51-925b6dfe06ff | -3.31633 | -53.84453 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68c9b1a9-8df8-362d-a8e0-70d8669ed703 | -4.28015 | -50.27598 | 2026-10-05 04:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20672e4d-08ca-3120-bb4a-cda81280e7c1 | -3.37665 | -54.10374 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dd02d344-8a14-33eb-beb6-19a2fe09efad | -1.80767 | -55.19746 | 2026-10-05 04:57:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ab2954d-92e7-33d9-b566-a9922a0297ca | -6.21295 | -52.83167 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f1c2b777-407d-37c9-9883-cc7662448b0d | -3.61549 | -54.60214 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13389ead-d84e-3587-bf54-90d801378d82 | -2.93342 | -54.13428 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 742ac94c-750b-3e23-924a-6438b1c7791e | -3.15526 | -50.43701 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2565fba-195a-3bdd-9c44-201d55ad5a85 | -3.31234 | -53.84764 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6d6462c0-bb7f-3e74-8ae4-5f1c1b869a69 | -3.31516 | -53.85184 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d39f05b-f306-366d-9a07-52c4f4735504 | -3.09727 | -53.72414 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| b60dd37e-97f8-3f0f-a5b9-ee0d9f911e1a | -2.53876 | -58.02849 | 2026-10-05 04:57:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 633c7fd4-bf77-3dd8-9f26-9ca71311b890 | -2.25495 | -51.88662 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b394ee84-5f9b-34a8-8684-5c7ebaba9097 | -4.11597 | -49.07436 | 2026-10-05 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 885a7ccb-7961-3fe9-9c20-e6c024502cb7 | -3.27949 | -50.40424 | 2026-10-05 04:57:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d6dc52f-5438-3891-9fe0-ee1c9889459a | -2.8073 | -54.08811 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f61dc4b-ea16-37b6-b8dd-d8452c57ecf0 | -2.81564 | -54.12411 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 626e37e6-7964-33f7-ae5e-4f4e0e87107a | -3.112 | -53.71902 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc9d27d2-cd2b-3b88-af94-b2b25d8ee0d1 | -2.89734 | -54.11696 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 02f31670-b58b-376e-afad-4c3dc44a750c | -2.89795 | -54.11321 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5bff94bc-de29-30a5-b330-24877adb91dd | -6.25177 | -52.84435 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2916da20-4e89-3c56-a02e-e5f6c2a72ebe | -3.29114 | -49.51183 | 2026-10-05 04:57:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9c7124d2-a2a3-3707-b641-532c3d3e4b26 | -6.16815 | -55.37513 | 2026-10-05 04:57:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8811cdd6-e1d0-3e16-8bdf-dd57cde0519c | -3.30496 | -53.85022 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c17a740-36b0-3c22-b3c4-c4d94323038f | -6.01433 | -53.52525 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2813bcb4-cff4-37ed-bb4a-cf1b7c67028c | -6.20908 | -52.81334 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5d49a24-1fe6-3dc6-9f84-571443fc5df7 | -3.1186 | -53.76488 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 98dc4831-d30f-3e26-8580-32d748f5a144 | -3.06579 | -54.16246 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| e356a2ec-4fa0-3502-990f-e9c07b851b36 | -3.00523 | -53.88253 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4564f4d-fcba-310c-9d0a-b19bf525f4db | -3.70104 | -50.66507 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a694d19c-5c6b-3241-8cdc-cff09610f4f9 | -2.97324 | -54.10599 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf16160e-121c-310a-a6df-0687593e7644 | -3.01311 | -54.20427 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bf34f88d-d917-3c37-a176-d4303e79ef2c | -6.04429 | -53.29411 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ae916f4-ef21-31da-b277-79590ac72c1b | -4.03873 | -48.99818 | 2026-10-05 04:57:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| da38863d-370b-3690-9869-1718aa7ab10a | -8.67831 | -54.54529 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0e6be120-ce66-3a1b-b383-94e62b8984e0 | -3.10618 | -53.75543 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 3916ff4a-49f3-373e-8c08-8cbb35016d65 | -5.5073 | -56.17046 | 2026-10-05 04:57:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| caf24fb0-3a2b-39e8-ac57-7fa1d58a8552 | -3.28349 | -53.83184 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e02be0a2-899e-37b6-8b4b-11e5d33a31c9 | -6.0027 | -53.51264 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f8396898-8643-31a8-8e38-9d606ec6c9bc | -2.98393 | -54.0387 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea3d85e7-29ef-3629-8b2a-effb5976514a | -3.67436 | -55.51284 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 73bb219c-116e-3cb2-afca-e762b1238509 | -2.81099 | -54.1311 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04609a58-125c-3253-8fd3-4479399d0839 | -3.71063 | -50.64806 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 87be55ac-f188-3512-9ee3-6486f92ff29c | -3.27219 | -54.01097 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82939073-9c74-3513-abd1-7560eb4ddb58 | -4.42912 | -54.83739 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3c4098e-9a3e-3fb2-9cb1-05d708b0fd27 | -7.22178 | -55.20245 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| caa2a2be-97d8-3a9c-ac55-4732c02a3ed9 | -3.12722 | -53.73263 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd41867c-b2fc-3065-bc17-9cba3dc4da0a | -2.94448 | -54.19787 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6857be54-90f0-3cd3-a44a-44518f88dd99 | -2.83973 | -54.21716 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 58e14510-6af6-3800-af55-633acd950c08 | -7.71799 | -45.46295 | 2026-10-05 04:57:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c95751f5-874d-391f-b102-077a80185583 | -6.92747 | -43.67999 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d805113d-6b1e-38ed-a053-25878ddb36d9 | -9.83965 | -44.79335 | 2026-10-05 04:57:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2aa3ab4e-ee56-3270-8547-48f46aa5fc91 | -3.86023 | -55.82162 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5239a895-d5f5-3371-a214-5793b4c076fb | -7.43782 | -63.57373 | 2026-10-05 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dfe29539-72b9-3dec-889e-69e6556121ac | -5.68245 | -53.49732 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c734f971-9e94-3ee0-be9c-dea396eb1927 | -4.52851 | -49.6967 | 2026-10-05 04:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1260055c-32d2-30c7-b8dc-387fac29bab2 | -7.44436 | -63.57071 | 2026-10-05 04:57:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7934cee8-c552-3155-9afe-63c306c9761d | -1.98244 | -54.41832 | 2026-10-05 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7985a233-0aa6-3e56-8d6d-7acf7f63ff01 | -2.81685 | -54.11659 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b962e885-1bd0-3d05-87c7-e1b6f62444c1 | -3.16453 | -48.70067 | 2026-10-05 04:57:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e4325d0-efc3-383f-bd06-fb779365c98d | -3.27278 | -54.00727 | 2026-10-05 04:57:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b932b00a-cffe-3dcb-9b84-6955814314b4 | -7.88727 | -44.20007 | 2026-10-05 04:57:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 977b7780-bf77-34b6-afde-ae46132aa5d7 | -3.44716 | -51.84576 | 2026-10-05 04:57:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a02586f3-5c16-330f-b5f4-94565682236f | -6.91181 | -43.67444 | 2026-10-05 04:57:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5f35c01d-365d-3f74-a5f7-1ff91dd8d93b | -2.85315 | -53.9123 | 2026-10-05 04:57:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 743854d6-b01f-371d-8c4f-2473767d876f | -3.65756 | -55.50128 | 2026-10-05 04:57:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3b9f9aa0-da4e-3d72-835a-39f4dee5a57d | -3.01554 | -54.18917 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 358da54b-cf3b-3cae-bfe9-185fe40bb78a | -2.48723 | -56.82663 | 2026-10-05 04:57:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5c2337e3-ab69-3b75-b878-afe676af592a | -1.46805 | -54.53172 | 2026-10-05 04:57:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3878fe6a-c1ee-3be1-83c5-19ffa161fc89 | -3.51372 | -54.6265 | 2026-10-05 04:57:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf3b68c1-b79a-308e-b94a-8d35fea1f704 | -3.23135 | -54.33146 | 2026-10-05 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 26a2592a-7f50-378a-9641-c7f395cc8ff0 | -1.57196 | -55.17259 | 2026-10-05 04:57:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1ef2312d-efa0-34f8-92e1-25eefcd7ed6e | -6.23593 | -52.68659 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ed44340-866b-3e63-8d4d-1cc2de31e134 | -3.71001 | -40.34816 | 2026-10-05 04:57:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 618a691c-7e80-31f4-8275-75ea45227ebf | -5.41426 | -51.11205 | 2026-10-05 04:57:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60b1e994-c466-3d7d-adea-c3f3259c15a4 | -3.05442 | -54.39062 | 2026-10-05 04:57:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cfb42805-c6c7-39ec-8b6a-dac828ba90d3 | -3.47424 | -50.09817 | 2026-10-05 04:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b29c387c-5c99-3637-9440-fc7de3bd30e2 | -3.05365 | -54.17209 | 2026-10-05 04:57:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d340ba8-62f4-34b2-9d86-3995b581756f | -7.47023 | -54.99104 | 2026-10-05 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README34.md)
