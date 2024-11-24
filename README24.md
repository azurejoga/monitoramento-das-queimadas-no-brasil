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
| 44ec05e6-cc30-3452-a1db-28c17c0418af | -1.3666 | -53.8362 | 2024-11-24 02:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| b2f242f5-633b-304a-900e-8e4856986905 | -2.8652 | -45.8213 | 2024-11-24 02:40:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 6215075b-3c5b-3ddb-9dc9-efed590b5d4b | -3.8163 | -52.4223 | 2024-11-24 02:40:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 3b12a827-acef-3054-ba83-6f59dbb70fd5 | -3.054 | -49.4471 | 2024-11-24 02:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 50c07561-f7f2-3a93-b51b-82190207aa8d | -3.4698 | -43.8931 | 2024-11-24 02:40:00 | GOES-16 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| e69e29ac-da6a-355d-8b3d-3d9bb44c5ad3 | -3.054 | -49.4471 | 2024-11-24 02:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 38c03694-a417-3fe4-af39-53361d619924 | -2.8652 | -45.8213 | 2024-11-24 02:50:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 4382b07a-cacf-3bd8-aa03-56d9cfeec12f | -5.0998 | -43.151 | 2024-11-24 02:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 9fd739d7-7e1f-3ad2-9924-5b5458b45059 | -2.4456 | -49.0816 | 2024-11-24 02:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| b8b8d094-a4b2-3bb8-a876-e73497a76794 | -3.5159 | -53.8132 | 2024-11-24 02:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| d20a2c08-b2de-3c26-a549-fb4ea79dd021 | -3.0355 | -49.4476 | 2024-11-24 02:50:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 0a0c4c37-3510-38a5-80af-f9c660588da8 | -2.8837 | -45.843 | 2024-11-24 02:50:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 1f36c970-19b6-3374-b90a-15a9339df64e | -2.2137 | -46.3965 | 2024-11-24 02:50:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 8e359ae9-fb56-3eef-bedd-8e22aa8b627c | -2.8651 | -45.8437 | 2024-11-24 02:50:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 0c9d2395-e0ee-3516-af86-f5737e9b4f6a | -4.242 | -48.6978 | 2024-11-24 02:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 112858ce-ce3d-3e16-b47c-e8b84344b254 | -3.0355 | -49.4476 | 2024-11-24 03:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 5014c1cc-2cde-36d3-a035-cf05c536b668 | -3.5159 | -53.8132 | 2024-11-24 03:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 2f350982-d1ff-3536-a39c-0c9c6df00cd9 | -3.054 | -49.4471 | 2024-11-24 03:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 5aaa6a2d-e031-33f0-948f-e382473aaf64 | -2.4456 | -49.0816 | 2024-11-24 03:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 7067b674-72fe-3a0f-873e-93e88bbc3b96 | -2.8837 | -45.843 | 2024-11-24 03:00:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 77.8 |
| fe05fbca-39d8-3bad-9047-acf57ec8f844 | -2.8838 | -45.8207 | 2024-11-24 03:00:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 7f1479c9-6423-3ead-bff1-a1f581fbd28f | -2.2137 | -46.3965 | 2024-11-24 03:00:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 3528f984-4538-3b78-8a05-cafa1734dd43 | -4.242 | -48.6978 | 2024-11-24 03:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 2fbfb9ea-52f0-30f9-a697-2aa0dc5ccf99 | -5.0998 | -43.151 | 2024-11-24 03:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| c5837ef0-d6b2-3582-a3b6-9f9b51ec8c84 | -2.8651 | -45.8437 | 2024-11-24 03:00:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 1fec65e8-c4a4-3589-8ae8-abf320709bbe | -2.8652 | -45.8213 | 2024-11-24 03:00:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 66.6 |
| e2b28357-d139-3c88-b795-6791934e3939 | -3.1068 | -45.7903 | 2024-11-24 03:10:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 3e9f000b-4556-3a30-ada3-74f6f710b5ae | -3.0355 | -49.4476 | 2024-11-24 03:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 108.9 |
| 0edd3676-4308-30c4-baab-beab72604837 | -3.054 | -49.4471 | 2024-11-24 03:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 9c57e4e3-8c92-311a-9118-57efb3776ddd | -2.8651 | -45.8437 | 2024-11-24 03:10:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 161.0 |
| 245bc6da-15f9-3333-b247-e6f395a8bc4a | -2.8837 | -45.843 | 2024-11-24 03:10:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 50.3 |
| e58fc878-8f8b-38c0-909a-f85087c5875f | -3.0354 | -49.4688 | 2024-11-24 03:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 759a6b0f-e454-354b-833d-fca6d4a8f63b | -4.242 | -48.6978 | 2024-11-24 03:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 5e9d7970-96c0-32a9-a3dd-b644f9b3047c | -3.5159 | -53.8132 | 2024-11-24 03:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| ebe58828-7043-3b85-8e77-56a5e213b98d | -2.8652 | -45.8213 | 2024-11-24 03:10:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 0f752e2a-e3b1-3175-a0ba-d047e33de403 | -3.8963 | -38.54185 | 2024-11-24 03:12:00 | NOAA-21 | ITAITINGA | CEARÁ | Brasil | 2306256 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 56e3d5f5-7565-336a-b0e0-81af7c08812f | -5.64574 | -35.47503 | 2024-11-24 03:12:00 | NOAA-21 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 64e67133-b6f7-3633-9dd8-daf689ec87ed | -5.6467 | -35.46938 | 2024-11-24 03:12:00 | NOAA-21 | CEARÁ-MIRIM | RIO GRANDE DO NORTE | Brasil | 2402600 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 62ef6986-f488-3bd3-8297-b67cda907d9b | -3.07756 | -40.06792 | 2024-11-24 03:12:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 7bbe101b-4f2e-3a29-b74e-b138d1105662 | -8.37833 | -35.80144 | 2024-11-24 03:12:00 | NOAA-21 | CAMOCIM DE SÃO FÉLIX | PERNAMBUCO | Brasil | 2603504 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| e45da7c9-a00f-3941-a6ea-ddd9e47dede1 | -3.08665 | -40.05611 | 2024-11-24 03:12:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 6eaec266-f936-354c-a106-39bdc4c1f32a | -8.75486 | -35.23911 | 2024-11-24 03:12:00 | NOAA-21 | TAMANDARÉ | PERNAMBUCO | Brasil | 2614857 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 5c661cff-2c1c-3ad5-937b-e0ef89f805cc | -8.22009 | -37.38413 | 2024-11-24 03:12:00 | NOAA-21 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d1e624de-6df7-3e53-b196-8120bc4c1935 | -7.14565 | -38.71014 | 2024-11-24 03:12:00 | NOAA-21 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 40ee5b7c-f880-3bcd-ac0e-a56932794166 | -8.45274 | -35.08569 | 2024-11-24 03:12:00 | NOAA-21 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c58da2b2-4667-30f8-aa7b-61483dd80c98 | -5.668 | -35.28332 | 2024-11-24 03:12:00 | NOAA-21 | EXTREMOZ | RIO GRANDE DO NORTE | Brasil | 2403608 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9dda1907-948a-3ead-85c2-319b59024de6 | -6.83707 | -39.18321 | 2024-11-24 03:12:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 33bfc533-b949-3cbc-8ed3-c079cb943046 | -7.39772 | -34.82782 | 2024-11-24 03:12:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 38d570dc-8f9b-3152-870f-9e3922dbad2b | -3.89717 | -38.53683 | 2024-11-24 03:12:00 | NOAA-21 | ITAITINGA | CEARÁ | Brasil | 2306256 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| ecfde792-cc86-37d2-ba53-47dbc6cec7b0 | -4.49773 | -37.86469 | 2024-11-24 03:12:00 | NOAA-21 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 98aa61e4-8434-3738-9e39-abb9c24ad2f8 | -7.39811 | -34.83052 | 2024-11-24 03:12:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b38b6627-c8f8-3c0d-a53f-e3db5550583a | -8.75687 | -35.23713 | 2024-11-24 03:12:00 | NOAA-21 | TAMANDARÉ | PERNAMBUCO | Brasil | 2614857 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| ce6d7779-0a37-31af-b538-3da56aa0cdb6 | -7.82825 | -34.84907 | 2024-11-24 03:12:00 | NOAA-21 | IGARASSU | PERNAMBUCO | Brasil | 2606804 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 66744dc1-655e-3e0c-a3e9-e761c02056ba | -3.08627 | -40.05632 | 2024-11-24 03:12:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 47753f12-ee94-390c-aa3b-7e30621297b4 | -7.13972 | -38.70874 | 2024-11-24 03:12:00 | NOAA-21 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| cf0a8a35-1682-38a1-8c0f-66ccaa7f4881 | -5.85265 | -40.80015 | 2024-11-24 03:12:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 22.0 |
| 8054f365-ed7d-30c6-bc79-3b70a76e3a89 | -5.8516 | -40.80583 | 2024-11-24 03:12:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 22.0 |
| f2206892-53aa-3878-8789-6f5e5a8fbb80 | -4.49847 | -37.86035 | 2024-11-24 03:12:00 | NOAA-21 | FORTIM | CEARÁ | Brasil | 2304459 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5e5fd622-e2bb-3632-afa6-e0a174c1cd39 | -7.14052 | -38.70447 | 2024-11-24 03:12:00 | NOAA-21 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f6d4d28e-38c6-3860-98d1-7f0788a4aeca | -5.07173 | -37.71783 | 2024-11-24 03:12:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9a91a3f0-ed6b-3147-a6f9-995c2066d36c | -8.37739 | -35.80677 | 2024-11-24 03:12:00 | NOAA-21 | CAMOCIM DE SÃO FÉLIX | PERNAMBUCO | Brasil | 2603504 | 26 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0245723d-98d2-3389-a5dd-f3aeefa9d46c | -6.83572 | -39.18257 | 2024-11-24 03:12:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 39f7e623-6d01-30d0-9da5-8fca3af52faa | -7.39893 | -34.82568 | 2024-11-24 03:12:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 240150e5-6fa7-31cc-a7aa-d7ca815c4d64 | -3.0355 | -49.4476 | 2024-11-24 03:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| c0f37fec-8ff3-3fe3-89bc-9b5bc138e086 | -2.8838 | -45.8207 | 2024-11-24 03:20:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 60.8 |
| c2b13652-1744-3d35-a10e-ba82d9853679 | -5.0998 | -43.151 | 2024-11-24 03:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 74980150-16e2-3543-8982-b38c42ec9341 | -3.5159 | -53.8132 | 2024-11-24 03:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| bf680f61-c845-3ab3-8740-8db74a795a4d | -2.8837 | -45.843 | 2024-11-24 03:20:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 84.0 |
| e34df4a0-7fef-3862-93da-e9ead4a888d9 | -2.8651 | -45.8437 | 2024-11-24 03:20:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 108.2 |
| 99cf43d4-6b70-399c-a58a-d9a8105b755c | -3.054 | -49.4471 | 2024-11-24 03:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| a1429be6-cac5-32de-90d0-af20e55bdf95 | -2.8652 | -45.8213 | 2024-11-24 03:20:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 73.4 |
| a5e65f8c-d2bb-3d5d-9b95-7411cf2d6e05 | -2.8652 | -45.8213 | 2024-11-24 03:30:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 0bbc74d7-24ba-3a42-9751-9d39dbe5a927 | -3.054 | -49.4471 | 2024-11-24 03:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| bb9ec02a-0516-391c-b0f4-1d8ae9bf99d7 | -1.5129 | -54.1759 | 2024-11-24 03:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 6976d571-8860-3cbc-abf0-d888f1305695 | -2.8837 | -45.843 | 2024-11-24 03:30:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 49.6 |
| c77b4b80-488d-37b7-bf64-ef2c43d367f9 | -3.5159 | -53.8132 | 2024-11-24 03:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| c3e09aba-e2c0-3113-b0dc-4ae0e3a13b0d | -3.0355 | -49.4476 | 2024-11-24 03:30:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 8d942430-0d18-3062-9866-4ca1cdeceee9 | -2.8651 | -45.8437 | 2024-11-24 03:30:00 | GOES-16 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 07c5bcfe-a3a8-3927-97b8-a3e43db64858 | -3.83763 | -44.04874 | 2024-11-24 03:34:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2dfea02f-8cb3-33a2-9c97-178e71eeb2dd | -3.57701 | -41.95126 | 2024-11-24 03:34:00 | NPP-375D | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f0ec9a06-1931-3a1e-94db-90650fe0010e | -5.1096 | -43.15569 | 2024-11-24 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bd2e6013-ec0d-3b5d-84c5-c0ac3a6e824f | -2.21743 | -46.39663 | 2024-11-24 03:34:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| b9594d35-5bdf-322b-af80-5501b66cf5fe | -4.54359 | -42.91117 | 2024-11-24 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d993c38-e1b5-3d12-b921-fac138a79a39 | -3.69706 | -42.3116 | 2024-11-24 03:34:00 | NPP-375D | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| aa0e6996-f9cc-37f6-95c7-fcf04a9b4af1 | -5.6842 | -35.85627 | 2024-11-24 03:34:00 | NPP-375D | BENTO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2401602 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 46b30914-c879-399d-a5b0-c7b190fedbb3 | -4.55259 | -44.01963 | 2024-11-24 03:34:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d97f4575-d654-3922-8863-2204e7fb39e0 | -1.82091 | -46.38636 | 2024-11-24 03:34:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c2b99a77-f24f-3235-9fb1-fdce43d9bec4 | -3.77064 | -43.09579 | 2024-11-24 03:34:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6a35cc3f-3615-3225-982d-7d3ad5ee0546 | -3.10355 | -45.78496 | 2024-11-24 03:34:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| b06021e3-6735-39c0-a3f6-169e6e97c339 | -4.52941 | -42.90923 | 2024-11-24 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6a38397-d771-3ad7-9b19-9ace4a11531f | -4.70215 | -45.69589 | 2024-11-24 03:34:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cd6933fd-14bb-33c2-962a-613e26ca9b2e | -3.29714 | -45.73 | 2024-11-24 03:34:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36609ecd-cdc7-36de-a9a1-e2de38ab83ea | -3.7936 | -40.99375 | 2024-11-24 03:34:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 71cb385a-d91e-36da-a469-08a222904e0e | -3.4761 | -43.88823 | 2024-11-24 03:34:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ada2e0a9-458d-311d-9d02-19085f36260b | -2.70827 | -46.29485 | 2024-11-24 03:34:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0df11a6d-017b-3f83-a982-d03a29c928e2 | -4.01828 | -40.71809 | 2024-11-24 03:34:00 | NPP-375D | PACUJÁ | CEARÁ | Brasil | 2309904 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| eaf06546-c2dd-3f45-b1cd-7677c1be0e27 | -4.18978 | -42.96622 | 2024-11-24 03:34:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 394e161e-6159-30e0-89e4-ad2a1c10fd12 | -4.5307 | -42.90191 | 2024-11-24 03:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 892dea8c-322d-396a-a7ce-6d1e732df941 | -4.31838 | -38.12985 | 2024-11-24 03:34:00 | NPP-375D | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6012b430-5ed5-318f-93d8-1cf27620ba88 | -2.70943 | -46.28788 | 2024-11-24 03:34:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README25.md)
