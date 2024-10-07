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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9a8b5524-465d-39b1-868a-4741fcc71850 | -7.6212 | -42.504101 | 2024-10-07 00:28:21 | METOP-B | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c54b5ecb-2b37-367f-9d0b-0cdf4a8fc8b3 | -7.6233 | -42.513199 | 2024-10-07 00:28:21 | METOP-B | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3c2f354d-d4f0-392b-a8c7-e114a36240bd | -7.6092 | -42.497299 | 2024-10-07 00:28:21 | METOP-B | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 99414499-884f-3f1a-ba72-6127d85ec80e | -7.6114 | -42.506401 | 2024-10-07 00:28:21 | METOP-B | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2b973003-e652-3ddf-b7a5-eff6f868e095 | -7.7431 | -43.069599 | 2024-10-07 00:28:21 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| dc8927eb-23d3-37c7-80a7-d379573a67d5 | -7.6016 | -42.508701 | 2024-10-07 00:28:21 | METOP-B | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 18c00f88-b9e2-309e-81fd-2956224d6ac8 | -7.7253 | -43.0378 | 2024-10-07 00:28:21 | METOP-B | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ce664755-be16-37ef-ac2c-36a8f3882a4f | -7.7273 | -43.046398 | 2024-10-07 00:28:21 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| eddb6ed0-4c55-3ab1-806f-7ada426044dd | -7.7293 | -43.054901 | 2024-10-07 00:28:21 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4a32ebda-bf1d-38e4-915f-16c526e71f42 | -7.7175 | -43.048698 | 2024-10-07 00:28:21 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2a5bb2bb-70de-37e8-94e2-49c0dc5919dd | -7.7195 | -43.057201 | 2024-10-07 00:28:21 | METOP-B | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 99752f10-fc44-381f-9458-e7e9769e4453 | -7.2904 | -42.2374 | 2024-10-07 00:28:25 | METOP-B | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c7b9f80b-36d6-3912-9f0e-bac7a2bf57af | -7.2926 | -42.247002 | 2024-10-07 00:28:25 | METOP-B | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 654abaa6-1933-34cf-ba56-2a424b712451 | -7.1282 | -42.600601 | 2024-10-07 00:28:29 | METOP-B | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d65d4558-b326-3ec4-8cf0-3cb7e5c69653 | -7.1303 | -42.609798 | 2024-10-07 00:28:29 | METOP-B | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 164c5c96-6fcb-38ed-b000-ed7434776684 | -7.1324 | -42.6189 | 2024-10-07 00:28:29 | METOP-B | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 440abaf9-62bb-3fda-8374-953e21f48709 | -7.1346 | -42.627998 | 2024-10-07 00:28:29 | METOP-B | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| bffd9f10-8441-3920-9d97-1da46f2c5389 | -7.1162 | -42.5938 | 2024-10-07 00:28:29 | METOP-B | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9640fe20-a88c-3df7-a5ea-8b730c77c102 | -7.1226 | -42.621201 | 2024-10-07 00:28:29 | METOP-B | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1ffa6a7d-be76-3687-8b29-b3d3460eb182 | -7.1248 | -42.630299 | 2024-10-07 00:28:29 | METOP-B | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7e5de46f-07bb-3531-a8fa-0a364c5db3af | -7.1129 | -42.623501 | 2024-10-07 00:28:30 | METOP-B | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 7572cb08-be60-3f28-9c07-88751c7784be | -7.115 | -42.632599 | 2024-10-07 00:28:30 | METOP-B | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5becc8d6-6fa9-35e6-9f2e-df6557ecb9eb | -7.101 | -42.616699 | 2024-10-07 00:28:30 | METOP-B | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1b395c56-896f-3426-834b-e9b4f9c89486 | -7.1031 | -42.625801 | 2024-10-07 00:28:30 | METOP-B | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c6ccbe4d-cce7-3ff6-ba21-68f36ecb41eb | -7.1052 | -42.634899 | 2024-10-07 00:28:30 | METOP-B | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a7e385dd-4ec4-3649-b8d1-9a82babf4a14 | -6.8396 | -41.680901 | 2024-10-07 00:28:30 | METOP-B | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 75a57507-204c-3729-b175-f09efc7e651a | -6.8421 | -41.691399 | 2024-10-07 00:28:30 | METOP-B | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f4011cc8-076e-35d3-95d8-9b71deb6ea90 | -6.6329 | -42.115601 | 2024-10-07 00:28:35 | METOP-B | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2e1e48f0-a34d-310a-ae7d-530cdf0772c0 | -6.6403 | -42.103401 | 2024-10-07 00:28:35 | METOP-B | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 630343b6-57e5-33d2-980e-7242064b1cd3 | -6.6232 | -42.117901 | 2024-10-07 00:28:36 | METOP-B | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| c1aad469-0123-3cb1-b679-c56215f6f699 | -6.6255 | -42.127701 | 2024-10-07 00:28:36 | METOP-B | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cd37fa77-d6ed-30aa-9d5d-132d55d04265 | -6.611 | -42.110298 | 2024-10-07 00:28:36 | METOP-B | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8baa29c5-fbea-3633-b023-5c78b74f6859 | -6.6134 | -42.120201 | 2024-10-07 00:28:36 | METOP-B | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| dfa15c7e-a635-31e1-adbd-c54caa9743c3 | -6.6157 | -42.130001 | 2024-10-07 00:28:36 | METOP-B | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| db349d9b-23c7-3db5-a56e-1290ffc99ddf | -6.6036 | -42.122501 | 2024-10-07 00:28:36 | METOP-B | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| add38d3c-b382-31d8-b85f-7fdf98d547cf | -7.0296 | -44.040298 | 2024-10-07 00:28:36 | METOP-B | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6157f4c7-224b-3e2b-b1ee-eaab086b8eb1 | -7.2327 | -44.925098 | 2024-10-07 00:28:36 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cf70c8ba-97a1-352a-9777-d52451b78bf5 | -7.2343 | -44.932301 | 2024-10-07 00:28:36 | METOP-B | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 24159dc4-bcd1-3a73-bd8a-c2ba6daf9e1d | -6.4661 | -41.9324 | 2024-10-07 00:28:37 | METOP-B | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 543d26a8-3cef-3926-ac64-a16bee4d5be3 | -6.4685 | -41.942501 | 2024-10-07 00:28:37 | METOP-B | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ef429ba9-cac9-3c8b-8515-0e11d84b0288 | -6.2686 | -41.837601 | 2024-10-07 00:28:40 | METOP-B | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 72047744-291c-3ca3-8954-0ed85a820c6f | -6.2711 | -41.848 | 2024-10-07 00:28:40 | METOP-B | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3a51af06-18eb-386e-a6b5-b1a61f4dcbea | -6.2735 | -41.858299 | 2024-10-07 00:28:40 | METOP-B | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| aeee898f-b92c-30ea-af56-d1556edb7483 | -5.6166 | -47.392899 | 2024-10-07 00:28:40 | METOP-B | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6c5b73df-a81c-3d3a-b548-d0c0f89dea6b | -5.6181 | -47.399799 | 2024-10-07 00:28:40 | METOP-B | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 55431a64-6d6c-3b51-a8ea-08e3b53dc7dc | -6.4551 | -43.207001 | 2024-10-07 00:28:42 | METOP-B | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7c6baf37-4ccf-3ea7-a205-35373f8a4905 | -6.4571 | -43.215599 | 2024-10-07 00:28:42 | METOP-B | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 65f43598-3990-3f86-952b-b205227f287a | -5.4858 | -48.9291 | 2024-10-07 00:28:48 | METOP-B | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93e6a466-eda5-3fce-a854-f5cfd210cd04 | -5.4874 | -48.936501 | 2024-10-07 00:28:48 | METOP-B | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afaaa043-8c1b-3644-af8f-a4e5d2936dda | -4.2653 | -43.719898 | 2024-10-07 00:28:49 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1a4cda2d-7d4e-3fa6-bb6d-4521da3c01c3 | -4.2672 | -43.728401 | 2024-10-07 00:28:49 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a956edc2-d707-3bf9-b074-ee3f59ded011 | -4.2692 | -43.737 | 2024-10-07 00:28:49 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cfb7e8dc-ee33-37bc-8d96-0ffc1529ed5c | -4.2712 | -43.745602 | 2024-10-07 00:28:49 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aa05516a-ca32-3429-9c28-417658a0c717 | -4.2555 | -43.722099 | 2024-10-07 00:28:49 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7a31ebfe-4b38-39e4-b0a8-4952929ba072 | -4.2575 | -43.730598 | 2024-10-07 00:28:49 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d6a51d59-d774-31b8-91a6-ab3a154b2ea8 | -4.2594 | -43.739201 | 2024-10-07 00:28:49 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a51638ca-5879-3626-8f66-b774fba6f3d2 | -4.0386 | -43.229099 | 2024-10-07 00:28:51 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6cefab22-f7f3-3f9d-94d4-7a4ec627a0e1 | -4.0407 | -43.2383 | 2024-10-07 00:28:51 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 947add46-eb45-33c4-9a38-0adc3b11623e | -3.9488 | -46.438999 | 2024-10-07 00:29:04 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ef830d2f-32f9-311d-a46d-039632bb3361 | -3.9373 | -46.434299 | 2024-10-07 00:29:04 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a76a24a7-d479-38fc-bf24-f4701f1bdf90 | -3.926 | -46.4296 | 2024-10-07 00:29:04 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0bce0e01-6a1c-3830-8b0d-3ace4c48d847 | -3.9275 | -46.436501 | 2024-10-07 00:29:04 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a4d31338-c05a-3047-8ed0-d591babf8b1f | -6.5621 | -50.037601 | 2024-10-07 00:29:06 | METOP-B | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b6f0988-0d14-310f-966d-ff65904de38f | -6.5639 | -50.046101 | 2024-10-07 00:29:06 | METOP-B | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 236f7ce0-a616-3ff2-8a02-7e69783516c3 | -6.5522 | -50.0397 | 2024-10-07 00:29:06 | METOP-B | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d278bf43-55bf-30af-99b5-e90a62d6e6a4 | -4.0866 | -48.2393 | 2024-10-07 00:29:08 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d788e17-90b9-3fd9-9184-2079e99b7241 | -4.0881 | -48.2463 | 2024-10-07 00:29:08 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ac3d0ac-e091-3cc7-8468-14f8f5ebcee1 | -4.0897 | -48.2533 | 2024-10-07 00:29:08 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| deec318d-b73c-31a1-8246-355e6484a029 | -4.0913 | -48.260201 | 2024-10-07 00:29:08 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 532f9ce9-ae54-3998-994f-13b97e988859 | -4.1569 | -48.5994 | 2024-10-07 00:29:08 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea9a5384-0869-3773-9db3-728e92454bd0 | -4.1585 | -48.606499 | 2024-10-07 00:29:08 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7421fa40-d19e-3211-8b40-e4b9e00ed9cf | -3.9013 | -48.331402 | 2024-10-07 00:29:12 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae35b690-754a-3319-8a34-79c86138505b | -3.9029 | -48.338402 | 2024-10-07 00:29:12 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0107dfb9-b3cf-3507-acb1-d5db1537f630 | -3.9044 | -48.345299 | 2024-10-07 00:29:12 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d161ec40-304a-37e7-b8bb-cda8c9309f47 | -4.3726 | -43.0256 | 2024-10-07 00:29:15 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 700d3f1e-83d1-3016-8ec6-dcd4f7e275ef | -4.3748 | -43.034901 | 2024-10-07 00:29:15 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 57b8a2bd-a7db-3345-bd80-bf343ecfad1e | -4.2751 | -43.717602 | 2024-10-07 00:29:20 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ce7fb6db-b2e3-33b1-b704-a29fea9684b7 | -4.277 | -43.7262 | 2024-10-07 00:29:20 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 799bd5f5-50df-3a39-bfc1-37e617ae938c | -4.279 | -43.734798 | 2024-10-07 00:29:20 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c3718435-2932-3a3d-9fff-000573c60689 | -4.0072 | -43.226601 | 2024-10-07 00:29:22 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 89821281-182f-3135-a1cb-eca1b71366e2 | -4.0093 | -43.235802 | 2024-10-07 00:29:22 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b556a74d-69f4-3201-b514-a42497660afe | -4.0288 | -43.2313 | 2024-10-07 00:29:22 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3cde721e-ea8f-3327-99f1-1169d36006b7 | -4.0309 | -43.240501 | 2024-10-07 00:29:22 | METOP-B | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9a173d53-090c-3253-803d-c756f67e40d2 | -4.9512 | -49.6255 | 2024-10-07 00:29:30 | METOP-B | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3660868-7ad2-3b9f-a18f-68ad625e21a9 | -2.8766 | -49.455502 | 2024-10-07 00:29:32 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5dedd31a-e8c7-30bc-b59f-2a4716e186a0 | -2.8782 | -49.462799 | 2024-10-07 00:29:32 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f72d49b-d579-3d66-b925-f58dcaa6757b | -2.2297 | -46.720402 | 2024-10-07 00:29:33 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f64b811b-5199-3be8-a146-6e95761ce078 | -2.2313 | -46.727299 | 2024-10-07 00:29:33 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e65cbac3-32d3-35d1-bfbe-3cec57256a14 | -2.2329 | -46.734299 | 2024-10-07 00:29:33 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35bf54b5-2337-3894-9ea7-b34b48ff5885 | -2.2246 | -46.743401 | 2024-10-07 00:29:33 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60c56acf-b829-32a3-863c-3ff27bcc2564 | -2.2262 | -46.750301 | 2024-10-07 00:29:33 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95aa8ac6-0a56-3b83-a0d5-26023f8bcfa6 | -3.8476 | -46.447102 | 2024-10-07 00:29:37 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7d614260-da0a-3e37-8d81-bdb1158bcff6 | -3.8491 | -46.453999 | 2024-10-07 00:29:37 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 93673ad2-47cc-326b-afed-2d035b4b7b8c | -2.9161 | -45.8848 | 2024-10-07 00:29:50 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 90bfcf2a-81f3-38ca-baf7-088a93ddde4c | -3.489 | -48.880798 | 2024-10-07 00:29:51 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1938321f-416c-3878-9583-ef75fb289372 | -3.4906 | -48.887901 | 2024-10-07 00:29:51 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 337e7b95-704d-3f07-a6d4-9fe3660bdf93 | -3.4922 | -48.895 | 2024-10-07 00:29:51 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d364c7c8-1328-3c48-8837-b37f02099751 | -3.4938 | -48.902199 | 2024-10-07 00:29:51 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7ee70a0-54ac-3855-8980-b05f768a4080 | -3.484 | -48.904301 | 2024-10-07 00:29:51 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8cc844f-05d2-3e82-8eda-e25137a228e8 | -3.4856 | -48.9114 | 2024-10-07 00:29:51 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README11.md)
