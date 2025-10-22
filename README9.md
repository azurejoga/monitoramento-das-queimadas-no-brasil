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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d6977f2-fd09-3e97-b6cf-fac768a1b578 | -5.44099 | -47.60653 | 2025-10-22 04:25:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3859b397-07fd-3ac8-9c69-6f76d40daa73 | -3.71144 | -47.63354 | 2025-10-22 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2f946c2-5729-3d9b-baa4-a58505cef7e9 | -7.07414 | -44.10949 | 2025-10-22 04:25:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4ae64f4-5072-3b6a-870a-3c782f4596b0 | -7.93081 | -46.01797 | 2025-10-22 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3523f501-28ef-3df3-b12e-d3b9c193376a | -6.55464 | -44.02125 | 2025-10-22 04:25:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ebda2d54-4fa8-3b3a-b4d1-4f01442c61b2 | -2.4814 | -49.2571 | 2025-10-22 04:25:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ea3daa6c-96a0-323c-bc61-62fc41196a3e | -6.64535 | -43.61174 | 2025-10-22 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7747bebf-59e5-3a85-b57f-9dcf16b869b1 | -6.32769 | -41.88382 | 2025-10-22 04:25:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 556ad443-00a7-36e3-aedf-e159ffcbfb72 | -4.31765 | -48.08629 | 2025-10-22 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ba47838-2feb-30f2-92df-35caa02becd4 | -2.95031 | -49.34003 | 2025-10-22 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 136ce5bd-827c-3856-9900-319626b19827 | -4.45994 | -43.23995 | 2025-10-22 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7520c1a-d27a-3acb-9b0c-0dde856d7314 | -10.25054 | -48.46684 | 2025-10-22 04:25:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 623be039-cdba-32a2-929b-a148940c1b62 | -2.92602 | -48.30504 | 2025-10-22 04:25:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 82bf9910-1020-3b0d-862e-acf3fc6474c5 | -3.2479 | -50.1302 | 2025-10-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 079602a3-c0ac-34de-931d-c117c70d4f26 | -3.15257 | -50.17176 | 2025-10-22 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 73ef06ff-374a-3efe-a7ea-cccccb22f854 | -3.02763 | -49.45961 | 2025-10-22 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 26258b8c-161c-3da2-a261-6fd1edc10b37 | -3.40517 | -46.90346 | 2025-10-22 04:25:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dbde925b-81e8-350a-b763-4a933a0b472b | -2.02542 | -56.88491 | 2025-10-22 04:25:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1da5366f-2e13-3f2e-ab74-aeee7e550f53 | -7.94172 | -44.84178 | 2025-10-22 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2ecae79d-fbd3-3113-92ab-78d9d828cb14 | -6.33545 | -47.3772 | 2025-10-22 04:25:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 655cc065-6668-3280-b0f0-8e4f817c86ba | -9.22038 | -48.60267 | 2025-10-22 04:25:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bdafc462-7fe4-3642-b6d6-5865b8f3b6e9 | -4.69319 | -42.94239 | 2025-10-22 04:25:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d2eb5c2-09f5-3749-af1e-b314e41b3a48 | -5.97342 | -46.61013 | 2025-10-22 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3dd13465-eed2-3366-868d-6768ebb95dfd | -3.52346 | -49.44492 | 2025-10-22 04:25:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c2acbbc5-ccd2-3378-8113-ae1e97e0d470 | -10.25111 | -48.46322 | 2025-10-22 04:25:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3ba7693e-188b-3193-8a2e-7e5e23d50932 | -6.64244 | -43.60727 | 2025-10-22 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5fe7943b-4980-3e4e-8e3b-bfec46eba6fe | -4.45645 | -43.2394 | 2025-10-22 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 513d984b-e591-340c-bfda-62d4463849fc | -7.65353 | -44.59103 | 2025-10-22 04:25:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c82e51f0-0f8e-3362-a825-8b4e9a6bef4d | -4.39868 | -43.30297 | 2025-10-22 04:25:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4450b8ca-70f7-330a-b20e-12f727bbf0ed | -5.73867 | -46.45937 | 2025-10-22 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c79e326e-f21b-3b5a-8d42-7f999e5509fa | -3.99922 | -43.27959 | 2025-10-22 04:25:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e2cb54c7-511e-31de-83f1-a033d57cca82 | -7.49013 | -47.03022 | 2025-10-22 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c3211614-7a0b-3396-8ff2-e4e2d8a5fa42 | -5.82316 | -47.54106 | 2025-10-22 04:25:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6678b4f4-1795-3c0f-a837-cff5a4c7d554 | -4.08589 | -39.96375 | 2025-10-22 04:25:00 | NOAA-21 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e87f2b6f-48b7-39ec-8c1a-fdb27c5db766 | -6.90805 | -45.17706 | 2025-10-22 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37c98e2c-e2d2-3e7c-a8d0-ba30fe0d2ac0 | -3.02385 | -49.45901 | 2025-10-22 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dbeb3dac-4c73-377a-930b-64d05c599be6 | -5.66072 | -38.31023 | 2025-10-22 04:25:00 | NOAA-21 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 18eadde7-88a0-3450-a039-cc3705fc43ed | -12.81947 | -48.64574 | 2025-10-22 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 25dc25b1-0846-3c36-a23d-e2553d63a42f | -16.8242 | -47.63929 | 2025-10-22 04:27:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c9b21ef-035e-3ed8-ada1-f185f60cbd07 | -15.48338 | -50.46396 | 2025-10-22 04:27:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 20a99829-1df6-3967-bca9-4bf6a69f5a67 | -12.28478 | -46.60787 | 2025-10-22 04:27:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9fc6bdc7-fc2a-37bc-86c1-ec6ff4fd7f77 | -10.97799 | -54.2491 | 2025-10-22 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0cf4653d-0b2f-37f8-a8fb-65fb34fbcf73 | -12.31812 | -47.83667 | 2025-10-22 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 109d28d2-8056-34bd-85e0-80f2a8fad1b3 | -12.82339 | -48.6426 | 2025-10-22 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efd1255f-e2a2-3a6b-8b44-456768c22582 | -10.59831 | -48.20727 | 2025-10-22 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14d483f0-4039-3eeb-928a-0ed8390bd333 | -12.69213 | -48.63232 | 2025-10-22 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01442d9c-f1cf-33e2-8455-3145b7ef77e1 | -15.52134 | -50.38292 | 2025-10-22 04:27:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 267692db-2f31-340c-87c7-02f87b20fe04 | -18.57786 | -44.90571 | 2025-10-22 04:27:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 221ff9d4-b8c5-38e7-a290-4aa01d95a106 | -13.38029 | -48.79848 | 2025-10-22 04:27:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cef405dc-2adf-3fd1-9c59-a888199ca60a | -17.62569 | -46.61877 | 2025-10-22 04:27:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2168a98-d441-35cb-b180-88571840996a | -16.04142 | -54.26561 | 2025-10-22 04:27:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cb81e6a9-ec61-373b-8b95-61ad9f2936bf | -17.6437 | -46.63644 | 2025-10-22 04:27:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4dd0890b-3d18-36da-b2ab-cf7db7c6d803 | -16.62731 | -43.48511 | 2025-10-22 04:27:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4c329ae6-0d7a-360a-b3e5-d90579bcc81f | -14.65662 | -53.10419 | 2025-10-22 04:27:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f9ceae77-5604-3447-a112-59a2d5abb317 | -13.37726 | -48.79822 | 2025-10-22 04:27:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fd7260b6-c907-3b9d-a526-19b45bb00eba | -17.61881 | -46.61769 | 2025-10-22 04:27:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 40103013-9e1e-3ebd-885c-c81b72937b89 | -16.06939 | -46.12973 | 2025-10-22 04:27:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 750be8f6-3e56-3392-babf-0b76243fd5c7 | -13.00333 | -48.77262 | 2025-10-22 04:27:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5edd5027-663a-3f7b-9868-0ca08f07b373 | -11.35571 | -48.72584 | 2025-10-22 04:27:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b0f4e7c6-aac2-38ad-9053-925c39fe0cf3 | -17.7307 | -44.74684 | 2025-10-22 04:27:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c700d083-7faa-3af2-853c-b424e2152128 | -17.21218 | -47.65622 | 2025-10-22 04:27:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 44365217-cea3-339b-b351-b2d42c74ab03 | -13.02266 | -48.58828 | 2025-10-22 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9489c989-8bb5-339e-acea-ccd3f11143dc | -12.50718 | -48.5759 | 2025-10-22 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54754e28-6def-324f-952f-25e005639296 | -17.64313 | -46.64037 | 2025-10-22 04:27:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8da9d15c-9c45-3683-9606-48bfc41cc150 | -15.16489 | -52.30192 | 2025-10-22 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f6702f81-0a71-34db-9f35-9feacf765c61 | -10.5727 | -48.21774 | 2025-10-22 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72c3a6c5-3e6b-3dac-ab36-cae3a8bf193d | -15.87313 | -48.81321 | 2025-10-22 04:27:00 | NOAA-21 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71a6ef94-336b-3c2c-8ee3-30177bf74b4a | -12.25193 | -49.58968 | 2025-10-22 04:27:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dca2846d-d8ef-3e46-b19c-0d0ac99b016a | -18.57911 | -44.92498 | 2025-10-22 04:27:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5da99296-eeb0-3353-a55f-c4539ae7b63a | -11.24388 | -49.00046 | 2025-10-22 04:27:00 | NOAA-21 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| deeb6b1b-62c4-35c1-8b60-67214fcaa10c | -17.62627 | -46.61483 | 2025-10-22 04:27:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cc636e00-1a13-3d33-b216-61abd2a59876 | -17.21606 | -47.6531 | 2025-10-22 04:27:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27b8995c-7655-387f-896f-8a4dd07cf02f | -12.89312 | -48.58875 | 2025-10-22 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5b45058-84d3-31b2-9d15-0915c97917d1 | -12.50442 | -48.57178 | 2025-10-22 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e4bf608-15f8-3340-87b5-4f20ff230c76 | -13.01226 | -48.56814 | 2025-10-22 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b0ca6441-a571-3586-97ad-87a5f0bc236d | -11.05932 | -45.39508 | 2025-10-22 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 51b4a3e3-537a-355f-be77-0f974373613d | -17.39666 | -46.65186 | 2025-10-22 04:27:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b16c1f3-e1a5-320f-8921-8e2c5bb28074 | -17.38241 | -52.00778 | 2025-10-22 04:27:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34895940-8427-3445-99df-dbc44c38cd91 | -11.4824 | -47.33102 | 2025-10-22 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a4427103-6b95-3293-a192-f94a60459370 | -17.62225 | -46.61823 | 2025-10-22 04:27:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 196b0a89-1ebc-3013-8bb1-1060c4a1ab2b | -14.66056 | -53.10505 | 2025-10-22 04:27:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 84c36b88-0491-333d-bf59-141185e7b265 | -16.81921 | -49.24311 | 2025-10-22 04:27:00 | NOAA-21 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f07943d-c8f6-3b3a-953e-6124f8eff672 | -15.52199 | -50.37905 | 2025-10-22 04:27:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d121d038-fd86-383a-9ea2-07da212fe75e | -12.8228 | -48.64629 | 2025-10-22 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1fdb354-16fd-3d0c-8deb-2c74389b555d | -17.62283 | -46.61428 | 2025-10-22 04:27:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d0ea4a0a-36cf-3a68-aaca-11a2dfec2c01 | -13.01718 | -48.57996 | 2025-10-22 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6b45b9f9-66de-3d3e-b6db-5c2da2d534f1 | -16.98738 | -51.76717 | 2025-10-22 04:27:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 12d1dfc4-39b4-33e5-a8d1-724c396d3337 | -16.24159 | -49.59471 | 2025-10-22 04:27:00 | NOAA-21 | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 208a0001-e7fc-3a1c-bfb1-8c8800ce3b20 | -16.87233 | -49.99162 | 2025-10-22 04:27:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6ed2eb9-e479-3d7a-a32a-b21fe483b67a | -15.4868 | -50.4646 | 2025-10-22 04:27:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d9a4502e-3a88-3858-807b-8c72bb9de150 | -12.31868 | -47.83316 | 2025-10-22 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b44cec05-e0ff-3407-b8c2-4decffda484e | -15.60041 | -51.00622 | 2025-10-22 04:27:00 | NOAA-21 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ddd52bf-573c-32d3-bbe9-6def8dbb2a4d | -12.82006 | -48.64206 | 2025-10-22 04:27:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b2a9a03-969a-372f-b47e-fe56ecc9a1af | -15.62297 | -48.91036 | 2025-10-22 04:27:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b2d64af-bad7-323b-ab79-45be02bc5bcc | -15.49087 | -50.46134 | 2025-10-22 04:27:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3fe34a6e-1126-399a-97f0-46cf52e5957b | -13.93963 | -48.96241 | 2025-10-22 04:27:00 | NOAA-21 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3c55668e-a0cb-3819-9722-b30cf6ee484c | -17.21273 | -47.65257 | 2025-10-22 04:27:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ac8ddc6-5264-3f6c-8d6b-25692ca3ee9a | -11.80412 | -47.88242 | 2025-10-22 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9faae910-246f-3a17-b478-865078d78aba | -17.15928 | -46.12265 | 2025-10-22 04:27:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 53e214bb-92e5-3cab-8f18-fdf325e6adca | -18.39544 | -44.41607 | 2025-10-22 04:27:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README10.md)
