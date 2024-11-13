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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb96c48a-3d8b-3314-84e6-62480899e930 | -3.05866 | -51.38345 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27dc57c2-353e-3a69-810e-3b24b17125fe | -1.64516 | -55.25296 | 2024-11-13 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96233ebb-4d15-3c91-8824-ae199aaa5acd | -3.22021 | -53.37379 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8917d420-63e6-3619-88d5-e755276020c8 | -1.21341 | -51.77249 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba39b1e9-3576-31e4-b1fd-ddee55e99944 | -2.03956 | -56.65559 | 2024-11-13 04:57:00 | NOAA-21 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92c0f70f-c32c-392c-8d2d-45451b291d63 | -0.73165 | -52.42505 | 2024-11-13 04:57:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55f2045f-74ed-3b3d-99aa-4ef9f39c10a2 | 1.11277 | -59.19996 | 2024-11-13 04:57:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6331e114-b4ca-352d-89e7-fa4d0d41b77d | -2.11636 | -50.69921 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 25300ef4-a714-3917-83a7-38f2bcdbd295 | -4.47691 | -49.63024 | 2024-11-13 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ab93cec-0712-3080-98e6-0e4923fbdc5f | -2.56251 | -54.03468 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3e3b97d4-cf0e-3f3e-a870-ee1f6484832f | -2.40979 | -50.3052 | 2024-11-13 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09eda34b-bc67-3be9-88bf-926cb6c29bf0 | -2.85304 | -49.21938 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 04333180-5db4-3113-b297-8b998cc4653d | -2.33392 | -48.54298 | 2024-11-13 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0cd339a-9f14-3bf7-bea3-c9858f02a6fe | -3.762 | -54.65251 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0715c26e-7445-32d3-8ac1-f553b1a522a4 | -2.87492 | -49.42982 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aaedd084-8658-31cf-8ecd-d13283a8f207 | -3.71245 | -53.75025 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 30bbee08-fb10-373d-a718-6668beab9c30 | -2.9227 | -54.1265 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d6d6027-a259-37df-8996-7b9762817d96 | -2.0997 | -48.94547 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1bc2fbee-39ec-357f-a0e2-6f0f410cfa53 | -3.65985 | -50.21555 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00490415-ce1f-3573-a43a-a7b8921a2d31 | -2.99817 | -51.45552 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a2ac3e1-9769-3986-81fa-dba63d437766 | -4.65824 | -47.428 | 2024-11-13 04:57:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 647a63a7-d383-347c-a527-48c3c130d99a | -3.80139 | -52.09895 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8390f503-1904-3c67-92f0-ec24a91e699b | -3.2277 | -50.54266 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d0043e5d-0518-38e0-8676-fccb827681a4 | -4.2179 | -46.82136 | 2024-11-13 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3bacebd8-c992-3e33-a2a1-553ad8384d1c | -1.12825 | -53.80951 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d74055de-d0c6-3dcd-b343-bddf0bd3efc2 | -1.44562 | -52.25348 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 050cf831-ce68-3268-9e05-3ee326651406 | -0.97414 | -51.72135 | 2024-11-13 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 163e1fce-6caf-3881-bc97-1eefca2b88a0 | -2.87878 | -53.97148 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4fcdcda5-699b-330e-80c3-c064086f4cdd | -1.22346 | -51.75203 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef4db8cf-73f5-3ff3-b2bb-72e202a12f46 | -1.21849 | -51.78427 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f41434ec-2ec5-3f0a-a1c2-d5b9e929ed58 | -3.0687 | -53.23424 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 205a7a69-1d48-33f5-aa6d-792004faa18c | -2.29279 | -47.91207 | 2024-11-13 04:57:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 52450b01-3b39-3528-ae40-32ed262b5597 | -2.63389 | -53.97167 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca26a847-2025-33b0-807a-8ed43ea566e9 | -2.52962 | -47.0901 | 2024-11-13 04:57:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb224d71-542e-3f23-878d-79e50ab7083b | -3.06287 | -50.32332 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e794a9a4-ee79-35f0-b13c-085adbfa545d | -3.34728 | -48.95328 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f6cf17cb-f735-3f00-bf2a-b04e57f11310 | -1.97351 | -46.57255 | 2024-11-13 04:57:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6c0d9cec-8b60-3196-8e3c-65ccb15fe38e | -3.05043 | -54.85031 | 2024-11-13 04:57:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f7ee02c4-d8c1-399f-ab26-df787ca76d23 | -3.02038 | -50.26033 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c425d6d-1987-3056-912b-b483de989156 | -2.5469 | -53.9829 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1444804-9868-3216-a337-e171704daa97 | -1.51864 | -54.98631 | 2024-11-13 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d1fe6e1-1312-308c-9df7-c4d79a184251 | -2.66235 | -51.72522 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c2ff23b4-a80d-3230-afcf-917741475603 | -2.69585 | -51.8016 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 25c7bfce-4598-391e-8db7-b6d87f017ef1 | -3.10136 | -54.31056 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b34a9cbe-8f65-3798-a7d5-aeb1558cc797 | -2.46721 | -53.68842 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30c602a6-5c2a-3bf3-b343-d4b7670cb4f9 | -2.82496 | -51.94753 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b536784-b4d6-35da-88e9-bf31981fc872 | -0.86947 | -51.95261 | 2024-11-13 04:57:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1151f1cc-6ab3-3062-a02d-cb2c2be50ab0 | -3.10855 | -51.15123 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 86faa7ed-6012-3c62-99bf-faa626e0fb32 | -3.25362 | -43.26525 | 2024-11-13 04:57:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 10c57a34-3dc7-39ab-a80f-c376b5d7e35f | -1.65271 | -47.47683 | 2024-11-13 04:57:00 | NOAA-21 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 602e882a-5f13-3a18-9d8f-7c61435282ab | -2.58343 | -54.03084 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fcd018c-642e-3fa4-b449-a0cb37bbcacc | -2.39161 | -53.66972 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41b11c6b-cec3-3e29-976e-e90abc2a2188 | -1.71109 | -52.46989 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b6bc17bb-601f-31b0-94c8-fb806b94e48e | -3.31096 | -54.18731 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0b32c8bd-7dc4-3e6e-bbe2-c961954bc35d | 1.29611 | -50.88276 | 2024-11-13 04:57:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4431fe4e-f1cf-3dfd-bb7d-fbc1c3220785 | -3.20111 | -53.40956 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b64221e-f8c9-3b65-ab2b-d9c2cb18e814 | -2.70512 | -48.65676 | 2024-11-13 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25ba6189-8317-31c6-bef0-01786988f00e | -4.36854 | -44.10467 | 2024-11-13 04:57:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 53f39b83-1eb0-3907-91e2-afa275d5012b | -4.22461 | -46.87143 | 2024-11-13 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45d6a79c-2a9a-35eb-868d-627868af1342 | -1.16911 | -47.60869 | 2024-11-13 04:57:00 | NOAA-21 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4df5725d-92c1-3065-82b8-3e2a79016663 | 0.86499 | -51.99561 | 2024-11-13 04:57:00 | NOAA-21 | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87ffcda5-1cfe-3cfb-8fcf-39f13e67f958 | -2.21238 | -50.47436 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4fbcf8fb-2251-3505-9a33-75557eba2d2a | -1.81806 | -50.96639 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ceea4d0-1131-309a-a1c0-d3cfb6cb334e | -2.60061 | -51.94675 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a5518336-d44b-3422-9478-115326491043 | -3.0367 | -51.09768 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1d0bb899-8655-37c6-8811-518cbe5891fb | -3.27792 | -51.06034 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa2715d0-ae89-3e2e-a8f6-a6df70023f18 | -3.63678 | -53.53791 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ada55aba-3a30-36da-9466-bd50a56b6007 | -3.34255 | -48.95776 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| 0dbda87d-2cc3-363c-ab26-cf896b8b1a4d | -1.09901 | -53.16521 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 033cb01c-2c9e-3b94-b0c1-89c80a68dac4 | -3.88069 | -51.17121 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 95755eab-734d-32fa-adaf-2fb590b9fc89 | -2.35921 | -53.68231 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5763f95a-a17e-3d33-a9c1-7114c23a899f | -3.17761 | -51.10517 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7cde8d4c-b5ac-3048-8876-cfe8e113e232 | -0.2854 | -51.66327 | 2024-11-13 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d99516f4-972e-38c9-842f-8a2a5f93bc9f | -2.24874 | -52.07727 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce77280a-9f02-386c-a49d-d8b29adad479 | -1.61245 | -52.40479 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4258abe4-4fbc-39f0-92ea-6f45b5a8fcef | -2.31548 | -48.52947 | 2024-11-13 04:57:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0bebd50b-f913-3940-b0d1-25621ae1cd77 | -1.12435 | -51.93362 | 2024-11-13 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 507a50e7-6659-3bff-8910-339fb2833a41 | -2.89984 | -54.00996 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 196c199d-1c0f-399d-a7af-faa822c8acd4 | -2.90873 | -49.25502 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 478e4745-84c7-30ca-b84f-8ad7ae3dea94 | -2.09411 | -50.2142 | 2024-11-13 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6bcdb62a-7e9d-302c-ad17-b83060ba2136 | -1.30603 | -54.66892 | 2024-11-13 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6a8c1860-8dc2-381b-8a28-7425fa01f063 | -2.43653 | -51.57412 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 78a05dd7-d769-324c-b176-809ac38047d7 | -2.0324 | -50.08434 | 2024-11-13 04:57:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3f97a55-7a8c-3c87-9a31-a308c0c1108d | -2.71744 | -51.70736 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d90e802-914f-3593-9898-3a21b76e57eb | -4.24932 | -50.25583 | 2024-11-13 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b34fd81a-696a-32bb-a86d-abd7c70c5d9d | -3.15835 | -50.58694 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a5e65df8-814b-353e-a483-6fc594d44bd2 | -4.20646 | -55.15758 | 2024-11-13 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 222f694f-3f66-3c29-9781-9a819f28c5e7 | -2.7265 | -51.73887 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e6b7b18-1dc9-3283-a649-87209eb3e688 | -4.41489 | -49.72797 | 2024-11-13 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 964e1f21-1bc5-3244-b1f5-cc738afb1192 | -1.3878 | -52.07538 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c6e0238-26d3-3ebd-bdc8-387d468c50ec | 1.30516 | -50.87386 | 2024-11-13 04:57:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10201660-f517-3568-9330-fb24c962217f | -2.67833 | -51.86977 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13892828-7e22-36a2-89b8-c39a17d570b0 | -2.33911 | -50.57123 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89647f48-67ac-396c-9fcc-d6aa4011b43d | -2.40508 | -53.73506 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af94f870-3fc9-3023-bd26-072b3a15c409 | -3.09225 | -51.14082 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f595888-2d06-3b97-b4e1-1d6ea9f1ab35 | -2.18124 | -53.25382 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04ed88d4-2e34-3a33-a422-e1e57a3b7e13 | -3.09034 | -53.26932 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ffe7c27-6dd6-3e61-9a78-2ae015951a12 | -4.67786 | -44.57624 | 2024-11-13 04:57:00 | NOAA-21 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4e729e34-ea50-3f03-a152-e771e0b9c23c | -3.34496 | -54.18913 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 411e188b-d6b8-38c6-9931-f6b4b565da02 | -1.64273 | -52.53772 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README32.md)
