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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40ceea62-2310-3132-a821-03ecb116a22f | -6.76205 | -45.02639 | 2026-05-29 04:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9703c17-d7a4-3b82-aee8-e54562bc0b3e | -6.76179 | -45.01984 | 2026-05-29 04:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2b43803-f521-369a-85b3-ef96ad818f27 | -7.3368 | -49.86282 | 2026-05-29 04:53:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 071146c8-3986-3e96-8971-02fb4d0e373d | -7.3498 | -46.21352 | 2026-05-29 04:53:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ea40819-3e44-384c-9c83-ca65ba0236d4 | -7.00969 | -45.00706 | 2026-05-29 04:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ec70fb65-c268-3dee-8cd8-bb5f6897eeb8 | -6.99759 | -44.99656 | 2026-05-29 04:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 54690d97-cd25-37ba-9e4b-066d6bc305f0 | -7.19394 | -44.34335 | 2026-05-29 04:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4c2f1d1-1383-3f4a-9595-ff15d6932f98 | -5.92436 | -43.47981 | 2026-05-29 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2eb60797-25fe-3fd2-8e3f-f2fd861ccdb2 | -7.34051 | -49.8596 | 2026-05-29 04:53:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e626d77d-03c5-31f3-8c4f-a9024d8fba9a | -6.24665 | -48.57582 | 2026-05-29 04:53:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f8714bef-c4ff-3286-8913-00f190637540 | -7.63497 | -45.2299 | 2026-05-29 04:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29c711b4-8a0e-3a17-ba66-84f55f778ecc | -7.00523 | -45.00655 | 2026-05-29 04:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e26e7d6f-d6d7-3f5f-a1fe-e48bf3eccd4c | -6.7583 | -45.02132 | 2026-05-29 04:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 348e568c-5182-32b7-81e5-40ea73e667bb | -6.99455 | -44.99838 | 2026-05-29 04:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ba3de16-dfad-39a8-ba3a-e6fa71a58d22 | -7.56282 | -42.64515 | 2026-05-29 04:53:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f2acd434-d848-3e8c-ba87-0aed44360b97 | -7.3527 | -46.21336 | 2026-05-29 04:53:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a20dfbb7-bf5e-32d9-8139-9553e6010a77 | -7.33995 | -49.86327 | 2026-05-29 04:53:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e9a792e-980a-35b1-9551-0b5e3e97e21f | -5.83748 | -43.49906 | 2026-05-29 04:53:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 198d143a-9d81-3efd-9e13-14fdb329a9c1 | -7.33711 | -49.85907 | 2026-05-29 04:53:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a75f653e-eb96-3070-aa0a-f63274bc6589 | -5.32155 | -44.69321 | 2026-05-29 04:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0da2f71c-5abc-347c-ac52-e6e5474e9a03 | -6.7627 | -45.02205 | 2026-05-29 04:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07a35696-6b4a-3136-833a-6d020aebde42 | -7.33738 | -49.85915 | 2026-05-29 04:53:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7dca11b-8a19-3864-93f4-7916f507b506 | -5.32096 | -44.69048 | 2026-05-29 04:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c86aaf33-e60c-32ae-903e-835d99c2ac68 | -5.32537 | -44.69121 | 2026-05-29 04:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 0ac3e753-7dd7-333c-a367-a3b8cccd005b | -7.00585 | -45.00221 | 2026-05-29 04:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8794edfa-b0c8-362e-abf7-8eb54a24f0b5 | -6.53836 | -44.68464 | 2026-05-29 04:53:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6306b8bf-10fc-3065-982a-cd95a1a2e102 | -5.93644 | -43.46525 | 2026-05-29 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cabe7ca8-5d62-380a-a635-2dd34802b41f | -7.3334 | -49.86227 | 2026-05-29 04:53:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1a5bc5ad-d826-3f47-b019-67429ff5b519 | -7.63557 | -45.22564 | 2026-05-29 04:53:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6cfb50f-a6e4-35d8-af19-9d1e7458c7e1 | -7.56808 | -42.64592 | 2026-05-29 04:53:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6a5812fb-7954-3a83-815a-4535c1df5572 | -6.76117 | -45.02419 | 2026-05-29 04:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab3568ee-46d6-3705-a4f8-45220bbf752b | -7.00079 | -45.00593 | 2026-05-29 04:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b2b4199e-d883-3961-830e-1212ed2a06d6 | -5.95082 | -43.48599 | 2026-05-29 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| ff389465-19e5-37b3-ab0d-826485f7b767 | -7.33654 | -49.86274 | 2026-05-29 04:53:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e385c93-497f-3f05-9195-6b5a7b7688f7 | -5.0297 | -56.19376 | 2026-05-29 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 838cd3a5-cf78-3427-8f7c-88e6131778a2 | -5.93853 | -43.46795 | 2026-05-29 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 65ff8389-7c65-30e1-84df-9bec071b2b06 | -5.32599 | -44.68689 | 2026-05-29 04:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 03761189-ac99-330c-b1f9-e2a44e9f3965 | -11.78153 | -52.51375 | 2026-05-29 04:55:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a8fbc83-12b2-3ed0-afbc-ca7ec6ce9355 | -9.60611 | -58.34426 | 2026-05-29 04:55:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94b74943-b64d-30cd-816f-ec04c304dd8a | -11.2747 | -53.97263 | 2026-05-29 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fd7cb28f-a891-3ec4-968b-59df8d3179c2 | -9.1619 | -46.85815 | 2026-05-29 04:55:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5305fa52-9148-363c-8596-fbd2cadbd24b | -12.80481 | -54.87123 | 2026-05-29 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4a7fbfee-83d9-3315-b2c2-fb76978314e2 | -11.47264 | -57.10758 | 2026-05-29 04:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5eae6a20-2080-39da-aba0-a93c71d73c33 | -11.5918 | -47.44565 | 2026-05-29 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 2f166ca1-919b-344d-9b62-612f53a3998e | -9.60171 | -58.34343 | 2026-05-29 04:55:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c1f9be6-0cf3-3033-907a-255c9d16a5ff | -11.4474 | -55.11011 | 2026-05-29 04:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d477a96-97af-3920-b270-8ace1e59d536 | -11.47298 | -52.91967 | 2026-05-29 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92519972-3057-374b-98ee-889eb29575e8 | -11.59682 | -47.43906 | 2026-05-29 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5fa6287d-3845-3fca-95cf-423b7a7ad747 | -10.1278 | -52.40388 | 2026-05-29 04:55:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d84f5e61-349a-37e9-8e48-4d7fa65e1459 | -11.29968 | -54.03403 | 2026-05-29 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 688d5539-8958-3de1-a326-c00acb50d6e8 | -12.00074 | -45.14813 | 2026-05-29 04:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1a26924-a9e6-3fe0-bfad-b598f2222bd2 | -10.72013 | -49.03519 | 2026-05-29 04:55:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 707fc11d-3fa6-39b4-a427-b01e442e3f16 | -8.87674 | -48.50248 | 2026-05-29 04:55:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c4b543b8-8017-3f8e-8ca5-68ba367f12fb | -11.96599 | -47.3702 | 2026-05-29 04:55:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc0ab653-08d5-3db9-ac58-4b22e2be9963 | -8.68277 | -48.30534 | 2026-05-29 04:55:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a5018569-8742-3520-a009-baa23b96b309 | -11.56172 | -54.52708 | 2026-05-29 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b25f15e1-09ee-31d9-8de6-304f5cfc4ab6 | -11.4624 | -52.92156 | 2026-05-29 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 06d6056c-ff45-3945-b6d1-7efa39f209b6 | -10.13835 | -52.40199 | 2026-05-29 04:55:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5bcd44bf-7d22-3aaa-868a-2fd54cc95b85 | -12.21171 | -47.50105 | 2026-05-29 04:55:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc74373b-7d62-387f-9871-33f7ab690444 | -8.52788 | -51.57285 | 2026-05-29 04:55:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5d4e8e2-eded-3ada-a87e-fa61e12a658a | -11.79729 | -52.51616 | 2026-05-29 04:55:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3621c2c-94e7-3ccb-8300-29be129ed111 | -12.08575 | -51.21938 | 2026-05-29 04:55:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be5c1292-0015-3117-a3a3-d833686a1595 | -11.56174 | -54.57747 | 2026-05-29 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3afb2414-51fd-3e6d-b092-ce112634f099 | -8.91654 | -51.85281 | 2026-05-29 04:55:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e14e0054-38f5-3204-860a-eb547f43cb1b | -11.96548 | -47.3738 | 2026-05-29 04:55:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e542b8dd-0475-3348-a278-ecca275fc2d8 | -11.5913 | -47.44922 | 2026-05-29 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6a3980e8-a974-353b-a28a-a17297d63943 | -12.36099 | -54.16716 | 2026-05-29 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bfb3496-2f3a-33a2-839f-c81ff703495b | -10.91105 | -54.1233 | 2026-05-29 04:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 171a1d69-c379-3a01-9d60-7a2b800720ee | -12.68721 | -54.58334 | 2026-05-29 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc69d3a0-cbc8-369f-a786-62ef25653133 | -9.22532 | -47.51332 | 2026-05-29 04:55:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bbc993ff-b66b-3171-ba42-4c6491d5ecce | -11.99974 | -45.14647 | 2026-05-29 04:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 83c4baee-3921-354d-a336-c7d56cb51e86 | -14.12506 | -45.36916 | 2026-05-29 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 834b0140-6b8c-3b3e-a0fc-851884b0e57b | -11.94229 | -43.40578 | 2026-05-29 04:55:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cec13ebf-2e2a-31cd-8791-3b4fd4d9dd15 | -13.64202 | -55.75468 | 2026-05-29 04:55:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b00f4f1-eeb5-3721-9221-35b77779f32b | -12.80134 | -54.87064 | 2026-05-29 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d01fc14f-3eba-3478-a536-eefd3abb174e | -11.96954 | -47.37443 | 2026-05-29 04:55:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d40936b-f263-3e19-a6a0-7f47c09c1edf | -12.369 | -54.16093 | 2026-05-29 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9775dbb5-1f4e-3fcd-889a-c12e92b4bd55 | -10.82551 | -46.89691 | 2026-05-29 04:55:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a14baaa-9860-3275-bac6-b744ed9e2062 | -8.72594 | -47.82732 | 2026-05-29 04:55:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f75caf44-0adb-30be-a96f-c85af70c3190 | -11.62791 | -56.86405 | 2026-05-29 04:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60bdb2ac-a019-31db-a150-33219df16ae9 | -11.59534 | -47.44978 | 2026-05-29 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8790cfaf-aa41-33a5-b586-e16d354603c1 | -11.60036 | -47.4432 | 2026-05-29 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 9aa381b6-64b3-344d-b71f-7f0e0d978cbb | -9.60687 | -58.3399 | 2026-05-29 04:55:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b223eac5-afa3-3092-aec9-aa85394e0332 | -10.8219 | -46.89259 | 2026-05-29 04:55:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8ff87d71-6848-31db-bc87-372734ca2526 | -12.21192 | -47.50167 | 2026-05-29 04:55:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04ace354-2821-3bde-ba6a-dfe58b035a06 | -13.63608 | -55.75485 | 2026-05-29 04:55:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dafaf4b4-8e9f-3eee-9daa-aa7c2862491f | -11.3037 | -54.03088 | 2026-05-29 04:55:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0f1b03a0-5ebc-31d8-b559-d017022f7863 | -13.18414 | -52.70572 | 2026-05-29 04:55:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2862dce3-49e5-378b-bd1e-c734eb62ccae | -10.52033 | -48.10303 | 2026-05-29 04:55:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a18bfd4-480c-3cd5-af6e-cf42e8fc21f2 | -12.24837 | -49.10551 | 2026-05-29 04:55:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c5e63405-04d4-37f9-b681-9eab3554ff58 | -11.04796 | -49.60041 | 2026-05-29 04:55:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5313011-cfe9-3f9e-ac12-40fd5183e53b | -7.62001 | -56.73793 | 2026-05-29 04:55:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3fb9623c-4224-3a25-8d8a-9814beb2f976 | -11.74679 | -54.78667 | 2026-05-29 04:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3e22799-6466-3d3e-b03a-3753552d0549 | -13.11027 | -51.7257 | 2026-05-29 04:55:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a09c109-5dd3-3379-b165-ff76af785ae0 | -11.59632 | -47.44264 | 2026-05-29 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.3 |
| f920a933-175a-3e31-9fb1-d9460658ef48 | -10.90824 | -54.11897 | 2026-05-29 04:55:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f34ebb1-2e55-3666-a5ad-e8f2ab3ba397 | -14.12092 | -45.36317 | 2026-05-29 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fccb2caf-87f7-3bb6-b17b-d5d8e11616ae | -8.69014 | -48.30643 | 2026-05-29 04:55:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a2e2f62a-15cf-3150-ad25-ce46a74da5b2 | -8.89269 | -51.85257 | 2026-05-29 04:55:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ffcae04-cac3-3b34-b755-0eaa9272c59f | -8.22425 | -49.6738 | 2026-05-29 04:55:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README7.md)
