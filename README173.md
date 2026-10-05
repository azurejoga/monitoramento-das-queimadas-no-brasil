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

## Dados Diários - Página 173

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 902e433f-ddb4-3fb0-8288-6873ab4079cd | -9.1243 | -68.2206 | 2026-10-05 20:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 7f39bd6c-2fce-3397-b11d-3b7c9d631799 | -8.6483 | -66.8437 | 2026-10-05 20:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 89.0 |
| d86c2dfb-4394-36ef-93d3-a9eb23ce2a93 | -8.8519 | -66.8012 | 2026-10-05 20:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 108.0 |
| 98860500-cb5f-397e-b9b1-18671d0f0842 | -6.1273 | -43.4936 | 2026-10-05 20:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 158.3 |
| b4cc6fe9-359d-36ff-9ddd-4e9939a2ade7 | -9.0429 | -65.4361 | 2026-10-05 20:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 4b988a4e-e70e-36e3-a504-21bccb9b61d2 | -7.4368 | -73.4448 | 2026-10-05 20:40:00 | GOES-19 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 115.5 |
| 93129b56-2b50-30da-baf5-db2465cabc8d | -9.4435 | -67.1008 | 2026-10-05 20:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 37811232-48b6-39fe-be44-feb586388214 | -7.2349 | -45.2599 | 2026-10-05 20:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 87d2af42-b5f4-3fd9-aea5-725391223ba3 | -8.5929 | -66.8266 | 2026-10-05 20:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 40688fee-dc7b-365f-942b-b61fc4cec1fb | -6.7199 | -44.2771 | 2026-10-05 20:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 5906ea06-b4d8-3063-a398-ad9533d5dcbd | -5.8321 | -45.0332 | 2026-10-05 20:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 0b0f732d-44b0-3fea-aa23-ad1f48adb849 | -9.7126 | -65.0951 | 2026-10-05 20:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 115.0 |
| bcca70f4-36f4-33bd-b0b1-22af4982138e | -6.8952 | -43.6833 | 2026-10-05 20:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 44126dfc-e746-3962-beb8-1ef352e5b6fe | -4.5159 | -43.6999 | 2026-10-05 20:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| e165b5cd-a53a-3d17-a668-7e2764f4da90 | -8.6115 | -66.8076 | 2026-10-05 20:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 7a4d6a37-2e5e-321b-865c-d97833de2dac | -6.1461 | -43.4921 | 2026-10-05 20:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 22faf0fc-3dc8-3045-b347-6cc814a8d25a | -5.828 | -43.4243 | 2026-10-05 20:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 157.1 |
| d7b8e72b-4c75-3011-b54c-2ebdac02cbe2 | -6.6683 | -43.8196 | 2026-10-05 20:40:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 141.2 |
| b3610ad5-706b-3cce-b848-286eb8c6b7c8 | -7.9722 | -71.4173 | 2026-10-05 20:40:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 8737c5b2-ae7f-3a14-8599-de82433ee69a | -5.8094 | -43.4025 | 2026-10-05 20:40:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 389.3 |
| 76255507-efd9-3f78-8460-ad0d91fef6eb | -4.4343 | -47.5639 | 2026-10-05 20:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 118.0 |
| d49dc889-3ac9-30b9-ab68-d243c585afed | -9.4784 | -67.6566 | 2026-10-05 20:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 598b81ea-2208-3b63-b6da-472eb3f3bfe5 | -9.1613 | -68.2568 | 2026-10-05 20:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 790114b6-fb66-3d3d-ad5f-1a3dca5a7fcc | -8.593 | -66.8081 | 2026-10-05 20:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 134.2 |
| 08cc1e9c-30c1-34db-9a94-70a336142adf | -7.4739 | -72.9168 | 2026-10-05 20:40:00 | GOES-19 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 700c25b8-d0e6-3da6-9547-31729297a4c4 | -7.8232 | -72.86 | 2026-10-05 20:40:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 98.0 |
| bbb1c6e1-8584-374e-956e-2f2eb35d1c65 | -9.3431 | -64.7143 | 2026-10-05 20:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 990bc23d-dc78-3580-8d87-4ed592c4e705 | -9.0892 | -67.6665 | 2026-10-05 20:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 127.0 |
| cf9f880d-384b-3e20-a6d8-b57559f1efab | -1.2498 | -46.5707 | 2026-10-05 20:40:00 | GOES-19 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 6c4e27c9-394f-35c5-8546-a5d931a3826d | -6.176 | -44.2762 | 2026-10-05 20:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 4ab5b7fd-acec-3dc0-a656-d87c2289ace8 | -9.5424 | -65.7002 | 2026-10-05 20:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 578f9325-c1ce-3448-8459-f01abcc23544 | -7.3641 | -72.4622 | 2026-10-05 20:40:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 126.9 |
| b7006ed1-06ec-3041-9ad5-b270d876454a | -7.2537 | -45.2582 | 2026-10-05 20:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 109.9 |
| b6aa3c2d-e365-3f67-8945-531281940038 | -5.8511 | -45.0091 | 2026-10-05 20:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 135.2 |
| 2462c661-04e1-3387-a210-66289a954de4 | -6.8764 | -43.685 | 2026-10-05 20:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 90.1 |
| a8d91918-a8b3-3ad1-8d58-4095486c66e2 | -6.1161 | -42.7214 | 2026-10-05 20:40:00 | GOES-19 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 74.7 |
| 9a9c1aa0-95ac-34ed-84c0-657ea13910e2 | -8.9258 | -66.8364 | 2026-10-05 20:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 89c8c388-68ab-3799-8569-9794f984b960 | -6.1271 | -43.5169 | 2026-10-05 20:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 165.4 |
| 90c015d9-3f19-31fd-825e-39b9da9fffea | -9.0892 | -67.685 | 2026-10-05 20:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 153.0 |
| b35e9747-6ee8-33bf-9063-5c12eb5b2f86 | -6.2558 | -43.7851 | 2026-10-05 20:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 824fb438-eb22-388a-afd1-e7eab297e175 | -9.5425 | -65.6815 | 2026-10-05 20:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 120.2 |
| d1f6cd4e-ce01-38e4-bb25-fc391cac3c5d | -8.5971 | -72.7454 | 2026-10-05 20:40:00 | GOES-19 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 150.4 |
| 27905944-c8ba-3c27-a68b-0e09f72fba8c | -9.1077 | -67.6845 | 2026-10-05 20:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 133.0 |
| 16e594d1-3d49-3b23-b30c-7c30b3fa953c | -7.9722 | -71.3991 | 2026-10-05 20:40:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 81.1 |
| bf685e6f-dd1d-32d0-ba61-b5e2aac87051 | -4.4657 | -42.8877 | 2026-10-05 20:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 45b48b8b-8765-3c88-bc07-864da2238d85 | -8.5183 | -67.0139 | 2026-10-05 20:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 52635ab1-0abd-3470-abe1-ed4a2e1801fc | -6.0706 | -43.5448 | 2026-10-05 20:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 773d196d-0c18-356b-8f48-21a5d4e69627 | -9.6672 | -66.834 | 2026-10-05 20:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 979e1d53-01bb-343c-a933-8d9f7041d7c7 | -4.5161 | -43.6767 | 2026-10-05 20:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.0 |
| ccc20ce4-b677-3c3a-be89-41f41355726a | -5.8509 | -45.0318 | 2026-10-05 20:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| bc553f8d-6bf2-3db9-9412-890afbd5c3ee | -6.1758 | -44.2992 | 2026-10-05 20:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 1a991cef-4a38-3cc7-8d1e-6a66a171b94c | -7.8049 | -72.8419 | 2026-10-05 20:40:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 156.1 |
| f663a451-1617-3bbb-ace0-215e106778b7 | -8.6155 | -72.727 | 2026-10-05 20:40:00 | GOES-19 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 114.0 |
| dc33d5c9-235c-342f-92d7-8de75a7366ec | -6.237 | -43.7866 | 2026-10-05 20:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 116.6 |
| ea54b16f-41c5-3235-856d-625bfbf574e2 | -8.852 | -66.7827 | 2026-10-05 20:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |


