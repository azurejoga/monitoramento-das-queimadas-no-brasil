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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02d283f8-37f5-3dcf-85be-e15eb9bd11aa | -6.66164 | -44.70012 | 2024-10-30 05:08:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c5e64f7-8fc8-38ed-ab95-1ace5c3a1aef | -4.83069 | -45.71471 | 2024-10-30 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ef34dfe-8569-38e7-98d7-74cdb5491cf4 | -4.83058 | -45.71305 | 2024-10-30 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 545b7ac7-9b72-3a21-a305-0f91264d16c8 | -4.82995 | -45.71764 | 2024-10-30 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d55db45b-80cc-391a-93f9-d813fec36d1d | -4.82451 | -45.71392 | 2024-10-30 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a524e4bd-3e53-3a9f-af27-14234521a5e8 | -4.82375 | -45.71703 | 2024-10-30 05:08:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8d922ecd-28a1-39b5-aa6b-b82fc32a7caf | -5.97172 | -45.36694 | 2024-10-30 05:08:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 0ab12874-6163-323e-a121-4a6c6c577bb8 | -5.971 | -45.37219 | 2024-10-30 05:08:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| b0d99261-1b46-369c-9389-71fba8ad4a7f | -5.97029 | -45.37748 | 2024-10-30 05:08:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 93a7e6df-2078-37ec-b74b-095c4e050175 | -5.46067 | -45.50475 | 2024-10-30 05:08:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b0d37b0a-7fb4-3b42-9e47-8d2105f64f5a | -7.57594 | -46.44273 | 2024-10-30 05:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6935f567-21de-3073-a41c-dfbe7f0b7804 | -7.57591 | -46.44077 | 2024-10-30 05:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1beea55f-4914-3305-a6db-74b15bf036ec | -7.57528 | -46.44545 | 2024-10-30 05:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2dceff41-5976-3bd8-8923-72d3a54324ab | -7.55418 | -46.13028 | 2024-10-30 05:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 63c3d048-61ef-3954-a2ee-b280eeb1beaf | -7.54916 | -46.13144 | 2024-10-30 05:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ba1a1136-0f3d-3442-8178-d9ef2a384c1f | -7.24658 | -46.57674 | 2024-10-30 05:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ae720624-1bf1-3dab-85da-952e95590d22 | -7.245 | -46.57305 | 2024-10-30 05:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c501099d-1aa3-3380-8b24-777b033dda06 | -7.24438 | -46.57756 | 2024-10-30 05:08:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21035f54-4c86-3c29-b73a-fa94b1f08c5c | -7.23458 | -45.5297 | 2024-10-30 05:08:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d9653856-54d3-350c-8e65-f7619272a2ce | -7.23388 | -45.53506 | 2024-10-30 05:08:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 700b7002-c868-3616-a859-c71458da6453 | -1.84059 | -47.09993 | 2024-10-30 05:08:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f03bd90-ab45-34eb-9639-6fe01d709b58 | -1.84005 | -47.10343 | 2024-10-30 05:08:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 22f87173-ba15-39e2-9f0c-7e5bcafd7920 | -1.83769 | -47.10023 | 2024-10-30 05:08:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2779a785-b0bc-33fb-82fc-aa37bf7b692e | -1.83717 | -47.10372 | 2024-10-30 05:08:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aac773e1-b049-3186-8ec5-e2fb73842910 | -1.59758 | -47.1401 | 2024-10-30 05:08:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 826166a3-dc56-3726-8e44-865fe391ff6c | -1.59705 | -47.14346 | 2024-10-30 05:08:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| ee6b3f7e-e721-3842-8a3d-eb6d0f93230c | -2.71949 | -46.70648 | 2024-10-30 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b753f408-f5a0-322d-8172-2e5cd89c496e | -2.71501 | -46.69816 | 2024-10-30 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce7f217a-4ec2-339f-b46d-2834d3d0d5a4 | -2.71444 | -46.70191 | 2024-10-30 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 535ba208-10ac-378e-9116-da3f92ca4681 | -2.71388 | -46.70566 | 2024-10-30 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6c473a2-df88-38fe-b983-f7578a88157e | -2.19246 | -46.98718 | 2024-10-30 05:08:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a26b2662-41a0-3dd7-a2a8-2f6b5aee3d27 | -2.19195 | -46.99066 | 2024-10-30 05:08:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 893cb9c4-db02-3098-b8d6-8131baf85eab | -2.19152 | -46.98727 | 2024-10-30 05:08:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19696b1b-19fe-3dcf-ac2b-5ba483e72305 | -2.19098 | -46.99073 | 2024-10-30 05:08:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9e98833-8fb0-3bea-b589-af347afdcc48 | -5.03225 | -46.93828 | 2024-10-30 05:08:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a381e832-e4f0-3051-add2-34b851b99a30 | -5.0317 | -46.9421 | 2024-10-30 05:08:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6bb523fe-98c9-3dea-b0e3-3583de4fc3e1 | -4.49665 | -46.45684 | 2024-10-30 05:08:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb2cae1c-0fbd-3b9a-985a-1cbe0dfa6280 | -4.49601 | -46.46122 | 2024-10-30 05:08:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fe95d9c-1dcc-3bae-9e66-50b7440ed30d | -4.4958 | -46.45837 | 2024-10-30 05:08:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c90cfe66-24a7-3f68-819f-7d6a07beeac3 | -4.198 | -46.7161 | 2024-10-30 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9ab5088-a8cf-3a8e-a856-634a42e4116c | -4.19742 | -46.7201 | 2024-10-30 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4fa60da-5726-3b38-aedd-a78d1a23ebae | -4.19231 | -46.71502 | 2024-10-30 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ddaf3147-fc87-32f9-9b9b-36b872f58f52 | -4.19175 | -46.71885 | 2024-10-30 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18a4b3e3-cd72-36d9-a413-a18fd76d55a0 | -3.59504 | -47.29888 | 2024-10-30 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 606a3746-5587-3edc-ad69-6c60c988dd45 | -3.59453 | -47.3023 | 2024-10-30 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3368cca2-cc2e-3720-acd7-b59add89ec5b | -3.57319 | -47.3713 | 2024-10-30 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e7cfc85-43a3-3660-b0b9-a8554f620953 | -3.57267 | -47.37478 | 2024-10-30 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5066cbc-b440-33dc-b7b2-8ee68c2396bd | -3.57216 | -47.37826 | 2024-10-30 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 5ed90638-5350-3525-b0dc-cf212b4d8b73 | -3.57165 | -47.38174 | 2024-10-30 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 7f71ddd8-7870-332f-bd41-f0c78ec39bb7 | -3.57113 | -47.38521 | 2024-10-30 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d0336e7-6233-3d4e-8f51-054a6b20d782 | -3.57062 | -47.38866 | 2024-10-30 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 34559dfa-e37c-3ea2-9072-c64282532f47 | -3.56776 | -47.37046 | 2024-10-30 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04840370-042f-3925-be9f-47e548dc051f | -3.56725 | -47.37395 | 2024-10-30 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8c0c427-e577-34c6-b837-ced30d6aa806 | -3.56673 | -47.37744 | 2024-10-30 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 711b45c7-b00b-3ff5-947e-c7ab89cb6a4f | -3.56622 | -47.38092 | 2024-10-30 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 0149205e-e55d-3417-8b7f-84509c23dc30 | -3.56571 | -47.3844 | 2024-10-30 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6044e836-1c88-3259-896d-e051ff58fa92 | -3.5652 | -47.38785 | 2024-10-30 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bea4daa5-5142-3b80-9e42-e83bd4689f96 | -6.04589 | -46.60137 | 2024-10-30 05:08:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b4636a53-4516-3079-9cb0-93492697cef7 | -6.0453 | -46.60558 | 2024-10-30 05:08:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6a55cf24-1721-3145-a3f9-6958f0a2ca8c | -5.53452 | -46.53318 | 2024-10-30 05:08:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2e911241-1bd3-3382-8d93-d338a46448cf | -5.53392 | -46.53744 | 2024-10-30 05:08:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2365753e-0882-3e21-8dce-845c0beba675 | -7.66878 | -47.3275 | 2024-10-30 05:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9b77875d-1661-32cf-9d9d-b6c4e3040fbe | -7.66823 | -47.33155 | 2024-10-30 05:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3e80ac8-e923-3cb8-854b-ffba67fe530b | -7.4848 | -47.15702 | 2024-10-30 05:08:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84c861e3-8a3d-343b-b109-576d79c3f5a3 | -6.8835 | -46.83717 | 2024-10-30 05:08:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 99a9cc5c-6340-3291-86f9-df330da7fddb | -6.8829 | -46.84155 | 2024-10-30 05:08:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c22b7984-bae4-3fe8-a174-f7974fe52d48 | -1.05306 | -47.63791 | 2024-10-30 05:08:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a28b395a-bd10-30ed-8d39-fde010d75e98 | -2.8024 | -48.66812 | 2024-10-30 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1677146a-b291-332a-b4f7-1c538a47c6e3 | -2.63094 | -47.96818 | 2024-10-30 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2d69458f-e1b0-33a8-8b50-8e642ede9c92 | -2.60775 | -48.25765 | 2024-10-30 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 061eece6-17b8-3bf3-a056-9d60b4c9d0d9 | -2.39053 | -48.57826 | 2024-10-30 05:08:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 8d119108-4526-3415-b030-2aa8b2c0a8e6 | -2.28747 | -48.50274 | 2024-10-30 05:08:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d6c685f-fcaf-3de1-bcd7-d625edc275c0 | -2.12799 | -48.38036 | 2024-10-30 05:08:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e8a0ac8-8262-35a6-bfad-d81e9d7ddb9e | -2.99584 | -48.94899 | 2024-10-30 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d906d7ed-1152-3797-9e09-69382125da41 | -2.97764 | -48.78575 | 2024-10-30 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e29f2bf9-23f9-382b-b54d-2bd10933850c | -2.93411 | -48.02443 | 2024-10-30 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6cfe2497-c330-3006-9d60-1089ffb020f8 | -2.93365 | -48.02747 | 2024-10-30 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1fe2da59-15ca-39a2-80ef-c3d04c21da90 | -2.63609 | -47.96898 | 2024-10-30 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 382110dd-8d17-3ba5-8271-f2698daa29fd | -2.6082 | -48.25472 | 2024-10-30 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4d232bfb-2818-3588-b350-ffd9342b7421 | -2.51649 | -47.44877 | 2024-10-30 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 794a97d1-7d16-3b68-b84c-0235a351b617 | -2.30281 | -48.58047 | 2024-10-30 05:08:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc0db6d7-d7c4-3733-b6cd-616fd0c31da0 | -2.2898 | -48.4995 | 2024-10-30 05:08:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 770b0cba-38c8-32e1-b93d-6b1d79e59297 | -4.91342 | -48.65034 | 2024-10-30 05:08:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 990cc104-a29b-34fd-aa26-e803925a320f | -4.90919 | -48.64383 | 2024-10-30 05:08:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26602f3c-3cff-35b9-b080-b0796bcffa9a | -4.90876 | -48.64675 | 2024-10-30 05:08:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df11c6f3-b3ee-3e9c-810e-8d773f74bb56 | -4.89004 | -48.66841 | 2024-10-30 05:08:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a255d42-9daf-333f-950c-2d605deda675 | -4.88934 | -48.60165 | 2024-10-30 05:08:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73b59cc2-ee00-3960-9fd4-46a93d3f7c5b | -4.88424 | -48.60091 | 2024-10-30 05:08:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96fa69c8-58b5-3cd9-a23e-3625cafcb8d3 | -4.59038 | -48.07393 | 2024-10-30 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36c56529-c218-38a7-a003-15c78c55eaf3 | -4.58988 | -48.07728 | 2024-10-30 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 039212d6-6d3c-39ea-ad9e-67bdbbd8f06f | -4.48671 | -48.12022 | 2024-10-30 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62cace5c-ed12-350d-b860-b063ee59233b | -4.14641 | -48.39884 | 2024-10-30 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4330b04f-26f6-3f97-be1c-fbec9cb53e24 | -4.1306 | -48.1352 | 2024-10-30 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9a46b230-3b4e-33ca-8e4d-186247785a38 | -4.13013 | -48.1384 | 2024-10-30 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3614f874-7a89-3f85-bd77-bb6b244a3dde | -4.10583 | -48.51033 | 2024-10-30 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d736e4f0-0947-3c8e-a5da-bd35d790ff4c | -4.1054 | -48.51321 | 2024-10-30 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5167a88f-83b4-3d25-82af-020cd7bbf70e | -4.10424 | -48.51109 | 2024-10-30 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| be625d69-e571-3d83-9127-5834614a6160 | -4.10382 | -48.51398 | 2024-10-30 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8842a731-09bd-3342-af9f-224251ab3fe4 | -3.92012 | -49.07959 | 2024-10-30 05:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cddc6c6f-6654-3112-9828-7c4cab218dc0 | -3.90166 | -49.08027 | 2024-10-30 05:08:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |


[Clique aqui para ver as próximas entradas](README85.md)
