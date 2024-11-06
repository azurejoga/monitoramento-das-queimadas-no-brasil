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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22c12cb1-76b5-3dc9-965d-e8e93d4fa5ed | -3.02055 | -51.43709 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8ca975b-0a02-3270-8ed9-bb59082ad705 | -3.12063 | -51.10487 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ed229fb4-b1da-37fc-9cf6-ca9d032952e3 | -2.78713 | -48.57349 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1eb8ec4-9c0b-32b1-9ccf-ba6362325080 | -2.34517 | -48.92254 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 068e4b84-0090-3d9f-bb04-9f63c2537d02 | -4.78363 | -48.90793 | 2024-11-06 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fc15c155-5308-391c-bd15-6eca79ad25bf | -3.21645 | -50.19857 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be218320-f225-365a-90fe-ded3518f1f54 | -4.0566 | -46.93709 | 2024-11-06 04:36:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 070efc17-ef7c-3983-9394-b40cdfd0fd96 | -2.51965 | -46.30154 | 2024-11-06 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65459fde-c9e1-3376-af0b-9948c173a131 | -2.45209 | -48.84775 | 2024-11-06 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99e6bb30-4265-370b-8eb4-1dfc8729a644 | -4.13913 | -46.83481 | 2024-11-06 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 03220798-868b-36c0-a3de-efd6a009ef0f | -4.35822 | -46.14497 | 2024-11-06 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62065939-750d-322a-8835-1008f893d9c0 | -3.25312 | -53.41025 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6708fd92-0ad5-3a09-a9ec-e18eed02e29b | -4.59176 | -45.49874 | 2024-11-06 04:36:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d5b7a6b-d5b9-3159-a3de-81780f94bb8c | -3.27074 | -50.29179 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1aed5de-0ea2-32a4-92c2-50f37d175c14 | -3.63849 | -51.78437 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 047e1958-d0cc-320d-a4c4-8b3b05143083 | -2.84247 | -51.35024 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3463fc0f-b931-3b95-8e16-bd941fb2bcc2 | -3.16863 | -54.47409 | 2024-11-06 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6f812aee-98cb-368d-93b0-07872893d898 | -2.92907 | -52.54264 | 2024-11-06 04:36:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6157c0d5-90a8-3eb9-86a9-a030c7ff56ee | -5.36387 | -46.42672 | 2024-11-06 04:36:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b51a94a4-06ee-3c80-b7d0-c6e451a4eb61 | -0.73839 | -52.90842 | 2024-11-06 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 510799a5-2b86-3ff4-bd46-7efb50ee5f7a | -3.19959 | -53.22149 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 210578ab-6f45-398b-af37-93c6c22fd7a5 | -2.66892 | -51.8225 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 7ff852d8-0cd1-3b2a-9f33-9930fe51e633 | -3.10878 | -50.29941 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 758f48af-ea0f-30b6-93b6-613d941ad8f1 | -3.4766 | -50.3869 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c0f9a9b-56bf-3ef0-9581-f2ecf6cae2a3 | -2.77521 | -54.73948 | 2024-11-06 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ee23ecc0-6373-3b41-a7c1-7a32d064ec4b | -4.29753 | -46.35126 | 2024-11-06 04:36:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| fd5e42ce-be81-3027-adbc-d98decdedd7d | -2.83962 | -48.4584 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92437f44-6ffc-3f6d-b8c1-75402667faa1 | -2.84879 | -51.77978 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 362b543f-61f0-3844-946b-f9790d2fc22a | -2.89527 | -49.37655 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 298c6a72-3afd-313f-b529-72bb7f24036e | -2.97112 | -53.26699 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74ce3a73-3914-388a-8670-b7ccaf78db29 | -3.11801 | -54.2554 | 2024-11-06 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 37b52119-3bfa-3a44-8d15-e7a067ed619a | -2.4217 | -53.66767 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b1a19ee-94aa-3318-948a-9e355cb06e09 | -2.86974 | -49.32286 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f7a38fa5-19e7-36c2-84f0-0775d393b737 | -1.47744 | -47.22105 | 2024-11-06 04:36:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 384262f2-1f15-35a4-95ad-bd4e9cef3e71 | -2.97811 | -53.27336 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03caf15b-c9ab-39cd-9796-725450d0ddb6 | -2.46775 | -49.1783 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be935cc2-aa03-3e96-a49b-8342bb84cc3d | -4.58858 | -45.49971 | 2024-11-06 04:36:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1af7fbe4-5bd1-31d9-8597-4cff91557cba | -3.75023 | -52.22658 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f58b714d-3a7a-3f3f-9ec5-d74a7bbdd3e3 | -4.45049 | -50.75047 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fb1bea1-2acd-34ea-acaa-2ceebdade4d7 | -3.22328 | -53.39845 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f2da22d-92e0-329f-8288-6fa49bdf8d6a | -3.58386 | -53.52778 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b959327-5c71-3004-8cb4-d4ccf706e341 | -3.9735 | -48.13682 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 510896b8-ad64-300c-9a6f-ade55327b1e1 | -3.75689 | -48.89108 | 2024-11-06 04:36:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0cb5a8b3-226b-370f-8dff-02117eed3cb8 | -2.42128 | -50.49687 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b302fab-89d3-326e-a325-df5fa19fec02 | -2.5838 | -51.33592 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a7d82108-b719-30de-a45f-62715bc5b1de | -2.60745 | -48.20374 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 973a8274-9482-30ab-9125-3311a14d03cd | -2.93573 | -51.05771 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 0358b2be-f18f-31f2-af6b-e975fce5e7d4 | -3.97133 | -48.15075 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ed08995-743a-3d93-b7bb-ca05a3c8e375 | -6.0103 | -38.66569 | 2024-11-06 04:36:00 | NOAA-20 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ab207067-7b10-3627-94fc-42fef72e5a37 | -4.69255 | -45.64945 | 2024-11-06 04:36:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0cb15a1d-3da3-3a55-8a93-cdae9c01e3c5 | -3.5351 | -47.38074 | 2024-11-06 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| b18cd2f6-8b30-3d61-b125-4ddd9d6222cf | -2.87694 | -51.31528 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a9d2fff1-3a64-3f78-ac01-a019a2337e16 | -2.5323 | -48.2061 | 2024-11-06 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5a6622be-02c7-326d-bb61-2859769fa132 | -4.32276 | -45.89791 | 2024-11-06 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6346514-0c0b-35b5-8041-ffb28a8058ef | -2.67213 | -48.5063 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a469df33-90a3-3e06-afbf-b93f63e36f8a | -3.17299 | -54.47441 | 2024-11-06 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55cdea2f-23bb-3eac-a9d1-7ce54160c5a3 | -2.5817 | -51.9221 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1b39ba77-1a24-35e6-850c-1f6439b79b4f | -5.63615 | -44.18617 | 2024-11-06 04:36:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4171e37-361d-323b-8548-5b3b6bebf00b | -2.86931 | -49.39026 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34bd0cde-c1f5-3f9c-a090-ad66ea319acc | -4.75275 | -45.91249 | 2024-11-06 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b0232fd-010e-33d1-bbb3-e6216a74d30e | -3.88959 | -48.36889 | 2024-11-06 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 810f1355-22ae-34e8-a987-9191a37630d4 | -3.77885 | -51.41011 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a66e84e8-9e03-3486-ab74-34c8ef99bbe5 | -2.9534 | -53.86301 | 2024-11-06 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 42399622-9fab-3452-b4c5-f40c991098cc | -0.36055 | -51.42956 | 2024-11-06 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a48b25c-8a54-39de-adc9-855f4548f97e | -3.06902 | -50.99123 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 68d6a0cd-ad01-3a6f-ad8f-36c30c3a734b | -2.82987 | -52.92092 | 2024-11-06 04:36:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 04d9c2b8-30cd-36b3-9226-57cc0bc9eb38 | -2.06642 | -48.51312 | 2024-11-06 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 890e7c26-b158-3a2c-9f79-cfd47b952d3a | -3.95926 | -49.93348 | 2024-11-06 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7332880c-82f4-39ca-bcd9-1ca5504592e7 | -2.63002 | -48.5806 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e52dea2b-601c-30b4-bd8d-aa493d32e6b2 | -4.75434 | -45.91169 | 2024-11-06 04:36:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0b86ed87-7ed7-31bd-bd6d-f8021cc2f8e0 | -3.34977 | -50.30398 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 614e5f73-02f5-3196-be6a-ac3849730d87 | -3.76378 | -49.98906 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3354ca28-5682-3de5-832c-b6a5ba6bdd54 | -3.89126 | -51.81436 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec3c8f84-0edd-3c45-ac75-0346d66c654d | -2.50572 | -48.74354 | 2024-11-06 04:36:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e7ef368b-728d-355a-870a-068b59f363c9 | -4.50034 | -50.74344 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d525275e-1a4b-3845-aaa6-82bb1db5663c | -3.09169 | -50.26807 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8115c255-2330-38ba-9f4d-1bf0e1a348de | -3.14704 | -51.32682 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 661ff7f5-81ef-3a84-afe4-b33364bf5488 | -2.24329 | -50.71453 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3cd62520-9405-3051-acea-3925dad11824 | -3.32762 | -50.08426 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 25c54a85-74b8-3c79-816b-b7443069695c | -4.21308 | -53.56415 | 2024-11-06 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| de8f567c-4a44-3468-9034-8f9be50a0bdd | -4.45251 | -49.54377 | 2024-11-06 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee9fcebc-88fd-3f1d-9c26-7f8bbbc3b5cd | -4.12416 | -43.58588 | 2024-11-06 04:36:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| d7429e3b-e108-3349-9df2-f795835b7623 | -3.12411 | -51.10543 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f74538ee-3b28-3204-b037-23502bb01408 | -6.00681 | -38.66179 | 2024-11-06 04:36:00 | NOAA-20 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e74d9605-5401-32a3-9e3d-f17910377edf | -2.1699 | -53.70496 | 2024-11-06 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a7907610-1611-3a92-b945-5011513061e7 | -4.21389 | -53.5592 | 2024-11-06 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ebc14d51-9581-3d43-bd75-9dfd92f48b36 | 1.35087 | -50.87914 | 2024-11-06 04:36:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 75592e73-85c6-32bb-b2e6-19de9dc470ef | -2.86568 | -51.66244 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c63a9cc0-5c41-3441-ac99-fbe5b3806c59 | -3.53847 | -47.38126 | 2024-11-06 04:36:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| c01e57fd-8711-3d0e-b6dc-910228bff7da | -3.17376 | -49.09891 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2f21dfb9-dbe6-3083-8c4d-823f57ff4bf4 | -3.03454 | -48.03693 | 2024-11-06 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5594d157-6a07-33a5-be85-8ed482eee77a | -2.99382 | -51.06155 | 2024-11-06 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 25b4e3cc-83d1-33ab-94c5-5750549a16ec | -3.8152 | -51.87719 | 2024-11-06 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 999a195a-ec4b-38a8-bd3d-5c2c1d0ce459 | -3.02889 | -54.08749 | 2024-11-06 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 71e06d67-fb76-3a30-a003-baa10e767d50 | -3.28384 | -51.48954 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08297aba-0248-39f8-a35e-5df494912084 | -1.9252 | -46.44743 | 2024-11-06 04:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c0e34ba-0a7a-3fe0-a9ab-3efb8f26a2e7 | -2.91023 | -49.41123 | 2024-11-06 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d0db1b6-830d-31c1-8a59-85eaee3540df | -3.60922 | -51.38061 | 2024-11-06 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 905cc02a-166a-38e9-8fc9-620e9726ef51 | -3.03011 | -54.08008 | 2024-11-06 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3eaf69ed-7fae-3981-aabf-e565b16d8ee5 | -3.40493 | -50.28313 | 2024-11-06 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README40.md)
