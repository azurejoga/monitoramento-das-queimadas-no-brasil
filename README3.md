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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2f1ceb69-989a-3942-9585-c4839a096754 | -29.08109 | -55.13949 | 2026-02-27 05:03:00 | NPP-375D | UNISTALDA | RIO GRANDE DO SUL | Brasil | 4322376 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 47470477-418a-3df0-90a6-7578a90acca2 | -27.68598 | -48.75369 | 2026-02-27 05:03:00 | NPP-375D | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 11666e26-1abc-35d1-8898-6580f9cc82ea | 1.4864 | -59.9308 | 2026-02-27 05:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.4 |
| e5da48b8-37d7-3713-a017-72e6fdf6d595 | 1.4864 | -59.9498 | 2026-02-27 05:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 9216189f-cd2c-3f99-b991-e437e8c8fc8f | 1.4681 | -59.9309 | 2026-02-27 05:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 35.5 |
| de34ea86-5879-3131-a598-1334a81f3f92 | 1.5046 | -59.9306 | 2026-02-27 05:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 6b71a284-27e0-3b88-92ff-a5c174f82312 | 1.5533 | -60.20433 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96dd0f3e-be3b-34ae-ac99-09acede644f2 | 3.79247 | -60.52483 | 2026-02-27 05:16:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 650a8378-0342-3c21-8d98-033fc7078acd | 4.07336 | -59.889 | 2026-02-27 05:16:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4ec1c06-d353-3e1e-94ed-e1c4e4585b3c | 1.50635 | -59.93063 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8871906e-a559-3b5e-aa45-98150a2fe49d | 1.49231 | -59.93283 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ba9c8a2-56ca-386a-82c6-545ca883d909 | 1.49004 | -59.94123 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d99ded2-5799-377e-8f33-947e7ff87df3 | 3.81066 | -61.74103 | 2026-02-27 05:16:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f23d1441-98e0-3502-b5a4-526f4a8343ea | 1.4859 | -59.93783 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5672f625-691c-330b-99d8-35ee7d86b7ac | 1.48012 | -59.9468 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08f1bef9-11f8-3469-b9b1-775927fd6541 | 1.49066 | -59.9452 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7176c345-c386-3efc-a368-ed15a137ea0c | 3.04045 | -60.06156 | 2026-02-27 05:16:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0831610-bc2a-3e64-87e8-af6b58519bfb | 1.50698 | -59.93461 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 46de2c31-38d3-3564-ac9b-3257bf6256bb | 1.50099 | -59.91952 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb2d2d4d-c09f-331c-9dd7-fa8eb0f4097d | 4.2771 | -61.32746 | 2026-02-27 05:16:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6569df9-c519-3a23-a37e-8dda348aca11 | 1.4888 | -59.93336 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 568c88bb-c08b-3e08-b056-68fe13ed80b9 | 3.89452 | -59.64478 | 2026-02-27 05:16:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c15126d4-f83c-3ec5-a05b-b48b595c7a02 | 1.50573 | -59.92672 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 442bf334-ffb1-3d28-b734-2609615b21ee | 1.48116 | -59.93055 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 54174ea1-876d-3aee-a2f4-7018739e5053 | 2.97655 | -61.2445 | 2026-02-27 05:16:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4db80da6-3b4f-38e0-a4e2-563e1314fe24 | 4.00295 | -60.38248 | 2026-02-27 05:16:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 31d56987-f09e-320c-9351-3f44e6b85e18 | 4.08361 | -60.6121 | 2026-02-27 05:16:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b52834ac-0630-3861-9ab8-bc934d0d08a8 | 4.10674 | -60.68751 | 2026-02-27 05:16:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a861655-3093-3355-ac22-efc0375fed5e | 1.49706 | -59.94016 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b5f0cfe-bc5a-34ff-88d4-24aed44df1ef | 3.04901 | -60.02239 | 2026-02-27 05:16:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a05f72b-ccba-303a-a6e7-a54f7a3a0074 | 2.97798 | -60.87933 | 2026-02-27 05:16:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21e48c3b-a740-3d8c-869c-707df5a00ec1 | 1.80817 | -60.46553 | 2026-02-27 05:16:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 39fbdd27-bd65-33d9-b015-b7975cf85f0c | 1.4824 | -59.9384 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95399f71-e4d8-313b-9b2b-1bd760a71eb7 | 1.48467 | -59.92999 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cf9a9f4c-fb4a-3ffb-89ac-a06a4f551f2e | 3.89097 | -59.64533 | 2026-02-27 05:16:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d681353d-2882-3f24-917c-e5e082ba96c6 | 3.0398 | -60.05744 | 2026-02-27 05:16:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee01b0e3-7f94-3db4-a733-403159606389 | 1.5012 | -59.94357 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f1f607f-caaa-3a8c-924d-eb7c380197fb | 1.46485 | -59.94121 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6681accf-de61-3f79-9b0c-6c0f773dd4c0 | 3.79552 | -60.51981 | 2026-02-27 05:16:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ed21a71-00c7-3b9f-8d58-6bd19e6fffc5 | 3.52643 | -60.29742 | 2026-02-27 05:16:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e5888ed-ad45-3e45-b225-39cfc771e111 | 1.4983 | -59.94804 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1d1fa8f2-ea33-324c-bd02-4141f9026199 | 1.49293 | -59.93675 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6c2869ed-8959-322f-9379-934fa37d1b3c | 1.49995 | -59.93568 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a84c3233-fd2e-3ebb-a1f6-ed86ee74b3f7 | 3.95288 | -60.22417 | 2026-02-27 05:16:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16eeb62a-d388-3aad-adf9-dd5d9718f22d | 1.48818 | -59.92946 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df5de639-6ae4-351e-9095-508fdd66ab10 | 1.49768 | -59.94411 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96582400-214a-3c40-8f2b-a5d8046c664d | 3.79081 | -60.52729 | 2026-02-27 05:16:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cceef1b5-17ea-3159-8435-419561a5b738 | 1.47827 | -59.93505 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d23d8a75-dc9a-3c7c-9901-3af9a86e66d9 | 1.47126 | -59.93618 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96f80ac1-c0be-36e2-86ea-058fe5e32efd | 1.4981 | -59.92397 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ba854cda-a95c-3785-aab8-4e4c47b64b1c | 2.86311 | -60.60624 | 2026-02-27 05:16:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b8282df4-5868-326a-830b-de1f8bb74b80 | 1.50161 | -59.9234 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55b27671-c852-3a89-936a-c211ee23b9c0 | 1.50924 | -59.92621 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 009ee0e8-29d2-3615-90b9-6fba35ab88c7 | 1.48486 | -59.95412 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a63581d-c1a9-3155-86de-4344719888e2 | 1.47248 | -59.944 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| beeb7787-6586-3303-a34e-fd28aa850330 | 2.11615 | -60.19865 | 2026-02-27 05:16:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9f6942f5-701d-3a41-8f80-3f95aac6f828 | 1.47599 | -59.94344 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 902e653b-2e3e-34e2-a351-586f7a156909 | 1.47538 | -59.93953 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7bc1c815-21a9-3dc5-841b-484a2e4fae37 | 1.4737 | -59.95179 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0644ffab-51a6-3dd7-adde-906f7d3d0feb | 3.49559 | -60.68763 | 2026-02-27 05:16:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84ce89da-aa9d-3101-8704-56ee7f62041c | 1.47766 | -59.93111 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0536cffe-6b03-3b3b-a586-8f35a6248eca | 1.46836 | -59.94065 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dbea9493-e324-37d6-9290-0ffbd2e011f6 | 1.48301 | -59.94233 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e3cf5921-44fa-37a9-aed9-5b6d688ebf27 | 4.10814 | -60.69663 | 2026-02-27 05:16:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4162c82c-a51b-31e7-a849-a74046e8c240 | 3.03621 | -60.058 | 2026-02-27 05:16:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 711dfa7f-725d-3aaa-bcd5-3560d5441044 | 1.46958 | -59.94844 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43b8c0bd-084c-324e-ab8e-c297c4ac4d4f | 3.52046 | -60.30713 | 2026-02-27 05:16:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 57d39dbb-fe05-3516-a18c-15568b64bb25 | 1.46897 | -59.94455 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57b5d459-60b4-374a-9977-4b7ed0792824 | 1.49521 | -59.92839 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41e95242-c811-394d-a773-d38c0992e3c7 | 1.47477 | -59.93561 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b058ab24-4d64-3081-8b6b-b76700cfdedd | 4.07694 | -59.88832 | 2026-02-27 05:16:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fca7199f-8806-324b-850e-334275a69180 | 3.03262 | -60.05855 | 2026-02-27 05:16:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7b854c0-67d5-31c5-a2c7-7d96cc02d731 | 1.48776 | -59.94967 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5d0c7fa-4359-3309-822c-cd8b45d8bdeb | 2.8668 | -60.60567 | 2026-02-27 05:16:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0870eb4f-f276-37c5-8022-7e442ca4be38 | 1.48425 | -59.9502 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c1da0c8-87a0-32a9-8d38-04c39b5ae29e | 1.50057 | -59.93962 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b6d5cdd-d795-37ab-a9e7-260b94f914ba | 1.47661 | -59.94734 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5e88040-36bf-3022-a384-d5247b279673 | 1.49582 | -59.9323 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72f66796-cf16-3d02-be4c-370acc7ef731 | 1.50182 | -59.9475 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fa8ff197-bd40-3053-b831-9bb926bae15c | 3.52345 | -60.30227 | 2026-02-27 05:16:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b1223a8-d597-3c86-a2ef-04c4bd884de9 | 4.13023 | -61.07124 | 2026-02-27 05:16:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cfa882fb-0931-3e40-83d4-13bc3f7990b1 | 1.49128 | -59.94912 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 413280d0-ee30-3d84-9e9a-576bcb8aa723 | 3.99559 | -60.08818 | 2026-02-27 05:16:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3f879663-abdf-311b-977d-04a2501fb899 | 1.48652 | -59.94177 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a4c1bb6b-602d-3aaf-ab55-cb37b07fe049 | 1.47187 | -59.94009 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16193863-5daf-364c-b5e6-d9f5312dff6c | 3.05682 | -60.02538 | 2026-02-27 05:16:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07fbe807-2751-339e-b0a2-c1bec09d9316 | 1.4795 | -59.94288 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c8cddd7a-0ee4-335f-b0d1-69d47b47e516 | 1.49479 | -59.94859 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a1c7b6f-bb61-3ea6-9a81-0b8118bbc404 | 1.48345 | -59.92223 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 614bccef-5d4a-3791-ab69-dca235bfb7ff | 3.52278 | -60.29798 | 2026-02-27 05:16:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37bc457a-1f6c-370d-8211-a77504862278 | 1.5076 | -59.93856 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10f9ee49-72b4-355c-a55f-a6c8e966cc5e | 1.47704 | -59.9272 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ce25db89-0688-30f5-8109-668e6488f244 | 1.50409 | -59.93909 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69700f6b-5907-3601-b1a6-11b4a5177a89 | 3.79619 | -60.52425 | 2026-02-27 05:16:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 31275113-5e71-3ae3-b404-dd2f700461cd | 1.48178 | -59.93447 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| db1104ef-1e02-3aae-a4a9-0337a2451f05 | 1.48529 | -59.93391 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 15b9291e-7b3e-3b2c-a919-9499465b055f | 3.79383 | -60.52228 | 2026-02-27 05:16:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 344e3154-aedb-3b7e-b9dd-65db6e318adc | 1.48941 | -59.93727 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9c70529-a320-3eec-99b3-8408df751bb4 | 3.81011 | -61.73742 | 2026-02-27 05:16:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7168076-85a6-371f-b9e9-a4eca6642324 | 1.49169 | -59.92893 | 2026-02-27 05:16:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README4.md)
