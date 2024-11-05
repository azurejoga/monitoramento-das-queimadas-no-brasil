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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03970292-ede9-336b-9595-f8cd2f506437 | -3.4437 | -50.13226 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6be30e4c-557b-3f0f-8dbf-3a8cd7bbbec3 | -1.87031 | -54.69269 | 2024-11-05 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84977c60-5ab8-3b4c-b31c-6cc2644491a9 | -5.30652 | -43.07456 | 2024-11-05 04:55:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b1ac561-05d2-3c55-8170-f51af6b9a32c | -3.41786 | -50.30153 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95879244-6862-3ac5-8cf9-9e98d28ab9be | -4.4108 | -43.11798 | 2024-11-05 04:55:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c0a2eb16-82e4-376c-ae08-33fd8a127e48 | -2.63573 | -47.96908 | 2024-11-05 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b4a20f17-e0f7-3947-9554-e5e73399e09a | -2.96375 | -48.72462 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5912d610-83c2-3f09-b34d-29fb08a77523 | -5.66155 | -45.20392 | 2024-11-05 04:55:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ca89141-39ea-3cd4-8d97-428c14e80d62 | -2.34885 | -49.61525 | 2024-11-05 04:55:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c50fe7ac-a7f4-36b2-a288-8dbd0ae1e291 | -6.52442 | -45.93526 | 2024-11-05 04:55:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ce13631-b915-357a-856a-3f747c0c0fc0 | -6.30414 | -42.03812 | 2024-11-05 04:55:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5a5c3e9e-59ba-3c87-909a-09120d98dffe | -4.6035 | -48.93135 | 2024-11-05 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d653851-1b7b-3a38-83bb-ece85df5e1c8 | -2.45453 | -48.14406 | 2024-11-05 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 89487f61-39ec-3a00-9531-1d9816aefcb4 | -2.46382 | -48.48373 | 2024-11-05 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b6039fd-e35d-3ee7-bce4-8b226cc717ba | -3.04175 | -53.27694 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b09c6ce-3a6e-3abd-bd78-18e5870aa0fd | -2.63813 | -51.74806 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d15ba58f-7047-3de5-bf88-11a51c9a90af | -3.76114 | -51.95918 | 2024-11-05 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0c740494-3611-3ee0-8a98-a41386ac4bee | -1.79318 | -50.98303 | 2024-11-05 04:55:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| debf7767-0fb4-32f3-9484-efde2c674113 | -5.43912 | -43.25559 | 2024-11-05 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97d4a2fa-43b7-3ee9-9a63-e917ab96b959 | -2.60138 | -51.30658 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 97f80097-2b9c-38a1-9df9-b7012a1902de | -5.92979 | -43.64465 | 2024-11-05 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b155a83-a173-3e92-94a7-b184b6360ea6 | -4.37637 | -47.24002 | 2024-11-05 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 99b938f1-a5b6-3813-ab14-d1aee6bcc7da | -3.10156 | -50.2655 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8dbdc4b1-4b76-3fb8-9f77-968c0875bf38 | -4.34286 | -48.1511 | 2024-11-05 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ad883fb-0c8d-356a-acaa-fd5ad63b21e3 | -3.34575 | -50.25733 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 35f3b917-b97b-304f-ac58-528f689686f8 | -3.01911 | -51.43751 | 2024-11-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53b0170f-2bbd-3e3b-8738-a2e0ea732a33 | -3.41424 | -50.30098 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 427d4fa6-2656-3c85-ae53-e66f33b50485 | -3.32866 | -50.27191 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b040246b-aea7-3815-b527-e6b41de67402 | -1.49657 | -54.86098 | 2024-11-05 04:55:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1e921106-4cbb-3d0c-b881-d4c41738bbb6 | -3.55821 | -47.39466 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a20212d2-2573-379d-a4a1-e612aee247cf | -3.04335 | -49.53035 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d21b5980-9b80-30c8-bfe8-58f9c9121e67 | -2.43592 | -51.58331 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e33b9a45-0faa-3d53-a825-653acf16f9dd | -4.8872 | -46.71213 | 2024-11-05 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7dab143-27fb-37c4-b84b-280e6f71dda8 | -5.93562 | -43.64551 | 2024-11-05 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b69680ff-51ef-32db-abfb-dbfe19a6e090 | -3.221 | -53.06506 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 101a262e-c3de-3c0b-a34d-c7a9ef3dea3f | -2.40329 | -50.3106 | 2024-11-05 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f98eb2b7-3713-31c8-baf1-a7bfd60a67f4 | -4.37388 | -47.2573 | 2024-11-05 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1fdef3ab-3dec-3e68-b611-25f4666d4f71 | -3.86591 | -52.39334 | 2024-11-05 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22ee2852-7822-373a-8bc2-c04e022f9dbc | -2.86051 | -48.45542 | 2024-11-05 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f624303a-0e7f-3249-a62b-322f5909f0ed | -3.96704 | -46.37669 | 2024-11-05 04:55:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d7a80e9-0b4a-3ec3-ab74-d02923cee1a0 | -4.36948 | -47.23625 | 2024-11-05 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0f93587d-49d7-3652-a012-3a7aa3ff8246 | -4.084 | -53.75717 | 2024-11-05 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 546ef164-9c35-3db5-9190-4bb60d003f01 | -4.34892 | -45.90876 | 2024-11-05 04:55:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 64b6fa70-5b1a-358f-b8dc-8c298f463b26 | -3.10856 | -50.29216 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62f7cf59-8ea5-3407-b6d0-b5b4e9ecba12 | -3.55266 | -47.37228 | 2024-11-05 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1d38c65-e079-3b64-8bfa-ba8d45616dbe | -5.98991 | -43.4299 | 2024-11-05 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21616d9b-2788-3b67-a9f7-25273f6583fa | -4.91066 | -44.36489 | 2024-11-05 04:55:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9161fba5-0fb4-3107-b4b9-e2337a42a3a0 | -2.65545 | -48.56598 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 4e6080e5-f6c4-3b55-9a94-7e7220a78d81 | -2.71396 | -52.96099 | 2024-11-05 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b58faa95-ac26-35ff-a381-491c51e348b0 | -3.45577 | -47.66806 | 2024-11-05 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 5ebd4353-f5df-3bdc-b164-f518aca0d74e | -2.17924 | -48.86458 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 88505a41-909c-364b-9ff9-f7ac3c7aca8d | -3.21856 | -45.45444 | 2024-11-05 04:55:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ab11f1d6-d738-3ade-bf2a-e630c68571c6 | -4.68586 | -45.81221 | 2024-11-05 04:55:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 052f8e40-53ff-3dc9-862f-449eccec4a04 | -2.22103 | -48.72716 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b43a5380-bca8-3ddf-be30-faaaa7ca78e1 | -4.89023 | -46.7054 | 2024-11-05 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 63a51df0-7774-3bc0-a27d-3d6a2cf9a812 | -4.3473 | -45.50681 | 2024-11-05 04:55:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51669ad2-1ffa-34f7-a23b-981dcce96869 | -3.12365 | -51.10563 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9dbb2773-bbf6-3005-afd1-6998c6191dc1 | -2.87509 | -51.30577 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2975dbec-733e-3041-b09d-8651659b7a81 | -5.2176 | -46.7262 | 2024-11-05 04:55:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e0ea6f0-2639-35d7-ad27-d5e963a7b166 | -3.08425 | -54.51461 | 2024-11-05 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4c219688-6544-345c-9fc6-72a850165b5d | -2.80918 | -48.65783 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4aefcd64-144f-3d9f-92c0-b17ecea86790 | -2.2868 | -50.6703 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b4f00f2-b125-3cbe-9003-aee8930fce04 | -4.71873 | -48.85709 | 2024-11-05 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6ffc717a-5261-3a35-913f-c4a5d2c949fe | -3.55147 | -51.57389 | 2024-11-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 951c2359-496f-3e40-8169-3576a0f6cff4 | -5.44505 | -43.25653 | 2024-11-05 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2a8f62c3-53c4-31fa-8cfa-2e1426badbc7 | -3.11549 | -51.11227 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc5ed1a9-3b79-3ef7-abc5-dbe2ddb1ab03 | -5.51135 | -48.08376 | 2024-11-05 04:55:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c1dc7d4-7935-339c-b206-b87ae8d7e40a | -4.61006 | -48.91472 | 2024-11-05 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8505948e-b64f-33e7-9879-429aabec831f | -2.14057 | -51.00334 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d300678-1f03-33ae-a0ad-daf74b80b762 | -5.93503 | -43.64971 | 2024-11-05 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7bca2a49-e6f0-340e-a637-baf8c522752f | -3.56199 | -45.24845 | 2024-11-05 04:55:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79f51fca-e3c6-3f03-89ec-7ff8e1a03b1c | -3.09432 | -50.2644 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa9f427a-3af7-354b-9f8b-dc12f46e8128 | -1.87977 | -51.01053 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3e8f59c-8132-307a-8494-d669b6bc414e | -4.60352 | -46.86582 | 2024-11-05 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ad412d4-fc4e-3c10-b9a8-4356e79c7b02 | -2.89776 | -48.59907 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af46d960-be5c-3403-96ac-ac5987048b3e | -2.85339 | -49.48496 | 2024-11-05 04:55:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0cefe92d-efbd-3a79-a8a1-f5de978862f7 | -5.69044 | -45.8362 | 2024-11-05 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a54e4c23-ec03-338d-be46-a87bc57d6fec | -3.08593 | -51.11938 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 786d1b62-3a35-31c8-ae90-ef9a057a6c8d | -3.09241 | -50.27692 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 044bdf53-af7c-3b03-bab2-db004c98d16c | -3.86129 | -51.40924 | 2024-11-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d0106e1-92fa-3f30-961d-3ab6ddc478ad | -3.88901 | -48.37173 | 2024-11-05 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cbc9b401-8cce-3f46-b7af-daf70a23c79c | -3.44736 | -50.13283 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bdf80d07-6ffc-36f6-afdf-dbc50a3bc27f | -3.48361 | -50.387 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01e6f810-c779-32f6-9d9a-aa7d2027d215 | -4.73759 | -46.75053 | 2024-11-05 04:55:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f6580f58-0176-341e-9675-6ee028d1c65a | -3.52813 | -51.16058 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e24cf67-d2cc-3730-80a8-8b1b8eeee4ce | -2.82331 | -52.93599 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2a99e42c-19be-3c48-87a6-6acc034becf5 | -6.12015 | -43.97638 | 2024-11-05 04:55:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 36586ce9-e2bc-359e-ab4a-42ee0ff2875a | -2.92165 | -48.60264 | 2024-11-05 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4f697e42-64f5-3002-9e9e-18fe19e4e37a | -2.8415 | -48.4454 | 2024-11-05 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2cc7c39-2052-37ab-983d-1885cdc48ee3 | -2.7987 | -51.48076 | 2024-11-05 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8573e623-a5fd-3ad0-a41f-67c2a4de9ea9 | -2.809 | -52.94083 | 2024-11-05 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0195af5b-9b8f-38d6-9741-3b7df2ca8810 | -2.87093 | -49.3939 | 2024-11-05 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4409958c-d41c-34b1-8ecf-2c1a67c6075f | -4.257 | -45.56422 | 2024-11-05 04:55:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0d02f3b-0d9e-3801-a0b2-0d5fa3a5d142 | -2.18216 | -50.32155 | 2024-11-05 04:55:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f38db6a3-0ad9-3368-a58e-cddc567f8874 | -3.64479 | -50.13721 | 2024-11-05 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fcfbf4a8-2ceb-3efa-b65b-15cb9e1efef3 | -4.37507 | -47.25951 | 2024-11-05 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d849f201-1559-351d-9a9e-5924938b2cea | -3.96875 | -48.39402 | 2024-11-05 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0ba7ee86-8afc-3e92-bc1b-4b5b7204ddab | -3.26657 | -50.33939 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19f3bf0c-3f60-3cfc-a36d-cc5b1876ab4d | -3.29184 | -50.34324 | 2024-11-05 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40f2fc56-caaf-3006-a76d-77ae5ba0449d | -2.73195 | -46.68046 | 2024-11-05 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README25.md)
