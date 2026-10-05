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

## Dados Diários - Página 170

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9648093c-309d-3454-ae16-0d14f8e36ee8 | -5.4719 | -43.4278 | 2026-10-05 20:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 1c316dca-e8bb-303d-98e6-f44170ea396e | -5.7907 | -43.4039 | 2026-10-05 20:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 112.1 |
| 00bec642-8b5a-3d2c-aa5b-1485ac84bd71 | -8.593 | -66.8081 | 2026-10-05 20:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 197.3 |
| cbafd176-d472-3497-a3fa-36fb899010e1 | -9.6672 | -66.834 | 2026-10-05 20:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 783edcf5-cd94-3fe1-8023-80c7df587e3c | -13.5197 | -61.1319 | 2026-10-05 20:10:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 107.0 |
| 24e538b4-26dd-3f65-9c00-dfe9631a189c | -9.2521 | -68.7904 | 2026-10-05 20:10:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 9e5b1461-7879-3f58-8868-47acab771dd3 | -7.8232 | -72.86 | 2026-10-05 20:10:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 77.5 |
| db68ca40-c306-3d9f-b45d-96d9a5d0438f | -8.9688 | -65.4385 | 2026-10-05 20:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 8f32ef03-ee36-3764-a4db-831822d4c0ee | -9.7126 | -65.0951 | 2026-10-05 20:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 145.2 |
| 3bd7f593-2617-3f9a-a3e0-afa1a4cc095f | -5.561 | -43.9544 | 2026-10-05 20:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 163.0 |
| 84fcca9e-ad7c-3bfa-9233-cc10dee1edcb | -8.5184 | -66.9954 | 2026-10-05 20:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 054e9f06-866c-3c65-a669-762c7fd4819c | 2.4585 | -50.8299 | 2026-10-05 20:10:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 4b4d128b-9592-3679-bdcf-880605f00a22 | -9.1074 | -67.7586 | 2026-10-05 20:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 216e7c8d-ddc0-3b2e-addb-87cd8c1d5bec | -5.5797 | -43.953 | 2026-10-05 20:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 087c4dd7-0cf3-3f62-a006-01fa2e242772 | -6.9328 | -43.6799 | 2026-10-05 20:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 75.7 |
| afec46c9-a2c7-3d5f-8394-3176ba264a56 | -6.3851 | -43.9826 | 2026-10-05 20:10:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 7acaecfc-8cee-30f0-a5d8-abe07e368f0b | -2.5353 | -65.8635 | 2026-10-05 20:10:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 96.4 |
| d9d31673-de7b-336d-93a1-dad286bc0606 | -6.8322 | -39.2961 | 2026-10-05 20:10:00 | GOES-19 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 87.6 |
| c1d1d7e1-2372-3572-a949-4b82ac8247cc | -8.5929 | -66.8266 | 2026-10-05 20:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 106.1 |
| ffab9ad9-7bf3-312f-841b-f5ef8f6b6877 | -7.8785 | -72.805 | 2026-10-05 20:10:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 96.5 |
| d188894e-a523-3837-904d-2b881a5f47cf | -5.5612 | -43.9313 | 2026-10-05 20:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 471.0 |
| 61db864e-c27e-36da-af5c-b556d71895c2 | -7.8969 | -72.8049 | 2026-10-05 20:10:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 75.6 |
| fc5bb4fd-3613-3b21-be13-adf55b291486 | -5.9603 | -41.3749 | 2026-10-05 20:10:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 78.9 |
| 895e26cd-5461-3668-b8ce-232e66fde8d0 | -9.96 | -43.481 | 2026-10-05 20:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 113.6 |
| ecbd050a-b935-3e1f-87c1-e23ab913a9ed | -6.8952 | -43.6833 | 2026-10-05 20:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 135.4 |
| d25972f3-a43a-3103-b0a4-591adc4bcd53 | -13.5007 | -61.1333 | 2026-10-05 20:10:00 | GOES-19 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 43549c47-dfcf-35f4-8941-d23f8a91369b | -5.8321 | -45.0332 | 2026-10-05 20:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| b5c508e9-c3b6-3945-b648-201e6da7902e | -6.1891 | -44.87 | 2026-10-05 20:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 7215aeaf-abb4-3147-961f-497d85fb5178 | -7.3641 | -72.4622 | 2026-10-05 20:10:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 215.1 |
| f7be62a1-c2ff-3b1b-9c42-85558a123938 | -7.2537 | -45.2582 | 2026-10-05 20:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 93612da7-3837-37b0-8f5b-0c71fc6f8dfb | -8.8265 | -64.2258 | 2026-10-05 20:10:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 177.4 |
| 0f81335a-fdee-3f4c-babb-f33a2835444a | -10.444 | -67.8908 | 2026-10-05 20:10:00 | GOES-19 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 62.7 |
| fc853227-835a-3169-9465-75e04174deba | -9.4751 | -64.3336 | 2026-10-05 20:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 93.1 |
| a1744372-735c-3460-ab2b-08a4c6cdd4cf | -5.3605 | -43.3194 | 2026-10-05 20:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| c9f31851-771a-3592-ae81-2a83074ed4b9 | -7.3825 | -72.4621 | 2026-10-05 20:10:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| cd8aed3c-2b22-3149-a611-69131b57c51a | -8.2674 | -71.1398 | 2026-10-05 20:10:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 1644550f-e1cb-3c0f-8b8a-dee5c160c6cc | -8.6298 | -66.8628 | 2026-10-05 20:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 85.3 |
| d91d3ca4-eb39-3bf0-b23c-2838ded69153 | -9.1076 | -67.703 | 2026-10-05 20:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 108.8 |
| e69d38ad-748e-3d4b-8bf4-159dd15fa129 | -8.4169 | -70.1119 | 2026-10-05 20:10:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 26436291-e4d0-3dc8-8bdb-a430020f5bce | -5.4909 | -43.4032 | 2026-10-05 20:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 943da1a6-5f83-31fc-9d9f-3179d28cba67 | -6.7199 | -44.2771 | 2026-10-05 20:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 2442c56a-0d37-3c5c-b430-ba1305729817 | -8.852 | -66.7827 | 2026-10-05 20:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 1881b123-5480-37a5-adc2-461b70849253 | -9.1077 | -67.6845 | 2026-10-05 20:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| ebad0cac-e2ec-33c0-96ff-b80d81e0640d | -6.8132 | -39.2982 | 2026-10-05 20:10:00 | GOES-19 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 86.6 |
| 230613d7-d7ba-3f93-88c3-3c46cdcde550 | -9.7312 | -65.0944 | 2026-10-05 20:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 115.8 |
| 8843f038-c965-3f41-a6d6-0702bde520e1 | -7.3641 | -72.4805 | 2026-10-05 20:10:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 1b36c61b-35b5-3990-9513-a28358a6b5bf | -9.6859 | -66.8149 | 2026-10-05 20:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 62ec47cc-71a5-3925-929f-2a2cea2a3483 | -9.0429 | -65.4361 | 2026-10-05 20:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 105.1 |
| 34be8824-20ee-3635-8e25-55f081646eae | -5.8092 | -43.4258 | 2026-10-05 20:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 150.6 |
| 9477e411-a3f3-3572-9340-db09a6e842d6 | -8.5183 | -67.0139 | 2026-10-05 20:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 001d8e27-6530-347d-9fad-4bcfc72c0ef5 | -5.8282 | -43.401 | 2026-10-05 20:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 1c1738e4-95d7-3982-8723-44e3b4c02ca2 | -6.1894 | -44.8472 | 2026-10-05 20:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| dd283734-bd8b-3ab0-b988-29293e2e44f3 | -9.4435 | -67.1008 | 2026-10-05 20:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 944118ad-c89f-3d24-912a-80e0ef53eef1 | -9.6858 | -66.8335 | 2026-10-05 20:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 962eac2d-e921-3d7b-8634-e0b625041e59 | -5.828 | -43.4243 | 2026-10-05 20:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 97.4 |
| bdb02db5-5818-36d6-9ffc-7956392c7b17 | -5.7905 | -43.4272 | 2026-10-05 20:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 221.3 |
| 91a0d95f-8be4-34a7-b0da-c59e7122c4ab | -9.5424 | -65.7002 | 2026-10-05 20:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 101.2 |
| b9c15265-f341-3ed0-9ed6-05659ed899e0 | 2.4769 | -50.8294 | 2026-10-05 20:10:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 125.8 |
| dd810bb3-d70a-35de-a87a-b3bfb4eb591b | -9.1072 | -67.8141 | 2026-10-05 20:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 76.8 |
| efd04e65-284a-37b1-8091-51426d1e4995 | -9.1626 | -67.8498 | 2026-10-05 20:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| fddef0cd-8038-3ed7-aa89-e7ecfcce417a | -9.1055 | -68.3135 | 2026-10-05 20:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 113.0 |
| b462396d-7896-3d89-8a45-d28baa1109a9 | -5.8094 | -43.4025 | 2026-10-05 20:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 130.9 |
| a806bac3-665d-3279-86ce-88bdc97e488c | -7.3638 | -72.8446 | 2026-10-05 20:10:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 97524cc8-9135-3d3c-a2e2-6bef88fbdec8 | -5.4721 | -43.4045 | 2026-10-05 20:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 84aba7cf-b905-3378-83b6-cfa8d8678ec1 | -8.9875 | -65.4006 | 2026-10-05 20:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.6 |
| d266f06f-71a8-34be-b20c-1cf098696aba | -9.1076 | -67.7215 | 2026-10-05 20:10:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 8ed63695-927b-3810-89bd-b0e7d15e20cb | -7.8416 | -72.8599 | 2026-10-05 20:10:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 29c16d20-0d26-329d-aca4-6b0d02a93ee8 | -8.249 | -71.14 | 2026-10-05 20:10:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 989203c2-67ab-3366-bba3-f83e21828199 | -5.3418 | -43.3207 | 2026-10-05 20:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 151.3 |
| e2814173-2018-33b5-a902-20062542f12d | -6.4545 | -40.9422 | 2026-10-05 20:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 88.8 |
| 0066deaf-2350-3996-bab2-8065225ab07d | -8.8519 | -66.8012 | 2026-10-05 20:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 5313d54c-0fe5-303b-a0ef-bc580ec07fc6 | -2.5353 | -65.8819 | 2026-10-05 20:10:00 | GOES-19 | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | 118.6 |
| 1a8e9ea7-a7bf-38cc-8361-f4f00641f5dc | -7.01 | -48.66 | 2026-10-05 20:15:00 | MSG-03 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 42eb6945-b87d-31c1-a239-f746098ece3a | -5.8 | -43.41 | 2026-10-05 20:15:00 | MSG-03 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 003c76a7-b93b-388f-8307-7dc2cdef2e6b | -3.11 | -53.75 | 2026-10-05 20:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38911e5d-025b-33b4-a588-4e8f067e0bdd | -3.69 | -55.91 | 2026-10-05 20:15:00 | MSG-03 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ab92710-44fe-3c7e-8fa0-4083efaebf31 | -3.08 | -53.75 | 2026-10-05 20:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3365a7b-f5f3-3b3e-a49f-ae9deed0bd8b | -3.11 | -53.69 | 2026-10-05 20:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec6d2c2e-f9ad-36fd-afbb-152bc8ac4a84 | -5.77 | -43.41 | 2026-10-05 20:15:00 | MSG-03 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5a28477d-0348-3f97-942e-6c672a888313 | -8.2674 | -71.1398 | 2026-10-05 20:20:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 0183a31e-b91b-3fcc-9f21-b8e8d1b0a296 | -6.7387 | -44.2755 | 2026-10-05 20:20:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| fcce8f05-f025-3fd3-aa7b-05d020c4b6a1 | -5.8511 | -45.0091 | 2026-10-05 20:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 965d4f1a-584f-392d-8a1d-cacd6d08ae1b | -9.1613 | -68.2383 | 2026-10-05 20:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 236b8664-ba23-328f-a245-f3cc1d5a9690 | -8.5183 | -67.0139 | 2026-10-05 20:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| e9b9af10-03a1-34cf-ba0f-6f4ac2ed548c | -5.5799 | -43.9299 | 2026-10-05 20:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 169.0 |
| 52f753b6-8cbf-3b37-a211-b2808d685fc3 | -4.3481 | -43.6634 | 2026-10-05 20:20:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 1706890a-106f-32c2-9f71-ff0b0cbde0ba | -5.4181 | -43.1518 | 2026-10-05 20:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 11b1ea4e-2a7c-31ca-9f41-223112d1d4b6 | 2.4585 | -50.8299 | 2026-10-05 20:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 200.7 |
| ffc3ef41-58c0-3989-87d4-96e3df6c6f2b | -6.9328 | -43.6799 | 2026-10-05 20:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 82.1 |
| f28c85f9-f80d-3708-9188-a946af0d0f1e | -8.5929 | -66.8266 | 2026-10-05 20:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 93.2 |
| eb7f13e9-26c4-3e71-8d6c-581907c42fc5 | -6.6683 | -43.8196 | 2026-10-05 20:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| dd0e3a21-59bc-30d3-b9c4-0555bea86be0 | -6.8764 | -43.685 | 2026-10-05 20:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 111.3 |
| 73ebdf79-6b86-3013-87e4-aa35ea66d27d | -6.4359 | -40.9196 | 2026-10-05 20:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 89.8 |
| 9275d050-ad03-3259-9b67-af03393d8ab3 | -10.534 | -68.7055 | 2026-10-05 20:20:00 | GOES-19 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 282f4980-5f7d-388d-835c-fec5b23a7669 | -9.1076 | -67.703 | 2026-10-05 20:20:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 738e5275-4c94-3882-b7ab-47e6daf23a6a | -8.9478 | -72.8343 | 2026-10-05 20:20:00 | GOES-19 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 161eec4d-1cf9-3ea0-abaa-e94f11c00304 | -6.2558 | -43.7851 | 2026-10-05 20:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| af147088-6863-33f3-a9a9-8ca320e15a09 | -5.8509 | -45.0318 | 2026-10-05 20:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 8f5ab89a-5281-302c-8297-1f6b7949d1cc | -9.3259 | -68.8811 | 2026-10-05 20:20:00 | GOES-19 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 29eb07ec-cf33-30d1-a727-bfbffc2b8ac4 | -8.6114 | -66.8262 | 2026-10-05 20:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.3 |


[Clique aqui para ver as próximas entradas](README171.md)
