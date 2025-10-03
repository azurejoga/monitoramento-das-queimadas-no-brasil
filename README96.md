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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a31560c-7367-375a-89a4-e7c54cf698cf | -10.6819 | -48.58468 | 2025-10-03 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5bfc4b6f-086f-38da-9448-c08c30bea3e7 | -11.14399 | -43.40385 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| dea01b8b-602e-3f06-8610-48cf569ca305 | -4.67409 | -45.80769 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64c95887-2d56-3974-8a10-34473bcd9d78 | -11.90288 | -46.29376 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4b9076f-d815-30f1-8a14-3c7eeb64f0f0 | -11.41679 | -43.49541 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 895f5271-683d-322d-a0bf-fb1567e2c817 | -11.85243 | -44.96305 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0b2a7049-7839-32a6-ac54-4b4e372fba45 | -9.33017 | -45.67017 | 2025-10-03 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ceade8f-25e5-3d69-95f7-0c9555ac8d25 | -5.79219 | -45.75533 | 2025-10-03 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b52d28a-93fe-3293-aa25-1cbd559ae359 | -5.44639 | -44.8228 | 2025-10-03 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 15a9fda2-dc5f-342f-88cf-588d3b89b72b | -6.0498 | -44.63091 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3e4d32ee-34da-3fa4-88e8-de1be7e2bb8a | -7.76754 | -42.60556 | 2025-10-03 04:32:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 30d5a320-e915-3c19-bf6c-c82981fce491 | -7.75968 | -46.25924 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 502641d6-5c9b-3193-a6b5-f2f97dff4604 | -9.83628 | -48.62727 | 2025-10-03 04:32:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2ed9af9c-062f-3479-9696-c4589d18c0b7 | -6.23572 | -45.33265 | 2025-10-03 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f0d64eb-22c0-3ff7-a5f3-77798365eff5 | -6.69162 | -42.8367 | 2025-10-03 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 823187ea-4ceb-31f3-91d5-82e6497a3e4e | -10.98197 | -46.67883 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ab8792f7-ab4b-3426-b32b-7c180a5915af | -10.89031 | -46.7313 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 588e417c-6903-376a-ac42-b8e16465a51c | -10.76598 | -45.33886 | 2025-10-03 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1986112-cf05-3d8b-a826-bc7c03bff4f2 | -11.14033 | -47.18107 | 2025-10-03 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df4c7628-2ffa-38c1-b66a-17f14859ab11 | -8.19636 | -46.80597 | 2025-10-03 04:32:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64408524-7e54-3528-b1d0-84e24cf8a536 | -8.61062 | -54.97039 | 2025-10-03 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e8c98a69-ade1-34e0-aeaf-9b147ccbd5c6 | -7.76288 | -42.60858 | 2025-10-03 04:32:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 3d7fca2b-3ef5-3e9d-bc1e-58a1efd9d755 | -10.00058 | -50.25257 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 1b5247ac-7034-3640-993d-f5b07aaa9ad1 | -11.10625 | -47.84329 | 2025-10-03 04:32:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7e62ab67-7699-3df3-8ae3-d1d812f2a1f4 | -6.37672 | -44.64394 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ccc37e91-e31f-39bd-8f74-1b2d7e84dd08 | -10.21319 | -53.8718 | 2025-10-03 04:32:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e24081ee-709f-3c38-aae1-4d144afd90ad | -5.63609 | -43.90164 | 2025-10-03 04:32:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f76510a6-473d-34f8-8b6f-e7d840773fca | -5.17825 | -45.42085 | 2025-10-03 04:32:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9674d4b-7d7d-3d11-b277-a3a21f8424b9 | -7.2951 | -45.26526 | 2025-10-03 04:32:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f0fafbbf-4d43-300a-ac8e-6c8efcb889b0 | -9.94882 | -43.66276 | 2025-10-03 04:32:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0cb9ba0a-106e-3f6d-bfce-37e5340c9bd6 | -10.0688 | -48.18544 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 20ff4feb-dc13-3246-aa74-3d83e4bcbf48 | -9.32253 | -45.67289 | 2025-10-03 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 050e6ef3-9bae-30d0-aec8-83d57e99a710 | -10.60085 | -48.71143 | 2025-10-03 04:32:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 01a92ecf-dc30-3c2d-8f7d-7728fd87940a | -6.73732 | -44.5787 | 2025-10-03 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6434373-93f6-38aa-b148-d800f744df79 | -10.00397 | -50.25314 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 40601361-c017-38ba-957a-21055ebbbafb | -10.27742 | -48.06791 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3493845a-75d6-3994-a9ea-e111953c186f | -7.7574 | -46.25129 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 72055751-2a14-36b0-ac08-cb6c381f433c | -9.94775 | -43.72598 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f875f7fb-aa78-35be-9a79-b87ebcc1101f | -10.87715 | -46.72538 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e430a655-48e3-3cf4-9e6b-bc76c47ff275 | -9.94725 | -43.749 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| fe3d8be6-84d6-3fcb-84e0-cdf5bd27c44a | -7.80018 | -42.52556 | 2025-10-03 04:32:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a4df4897-8e8c-3e93-b055-6e8db8ceb922 | -6.87678 | -44.52095 | 2025-10-03 04:32:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c8f027e4-dbd3-3324-9225-a989489d15ec | -8.90713 | -46.60898 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 089a882c-ffae-3ae6-a35e-dc6964c776cf | -11.13752 | -47.1995 | 2025-10-03 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2ad9b54-1dee-31ea-9a36-d2c0ae097d19 | -5.48903 | -52.137 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c3b5b8d8-06d9-32cd-a749-9258f4bbda2a | -11.84866 | -44.96246 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e36c0e85-33cf-3626-a296-78b96588bce8 | -10.89718 | -46.73238 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14481464-b608-3596-853e-2d08ae5eedca | -9.93104 | -43.58805 | 2025-10-03 04:32:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5750e405-c8e5-39fd-9ee9-e4c53005732b | -10.94743 | -48.55874 | 2025-10-03 04:32:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d92cc09f-ac26-3a04-90ad-f9384adbd520 | -7.77521 | -42.52179 | 2025-10-03 04:32:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b9f48236-1045-363e-b869-6594e283fd83 | -9.14625 | -47.63692 | 2025-10-03 04:32:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8724a5ac-8422-37fd-9731-80fc46436aef | -10.10935 | -50.27441 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c46c5fd-7285-3b9a-bce8-1a3106931b45 | -10.06494 | -48.18842 | 2025-10-03 04:32:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b839b49-0661-31a4-b385-60c9cc1c46de | -6.40966 | -52.86179 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f41297a1-fcad-31c9-a35f-b05cfc76832f | -11.87682 | -45.00828 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 60b0aea8-0df1-38d0-a885-f550e07a20a5 | -4.67013 | -45.78845 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92ec1161-d9a0-3fc1-a22b-014e99901a40 | -10.90978 | -46.71886 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb77bfd4-b9b3-3c27-9abe-dad9c5445c55 | -7.78738 | -50.2269 | 2025-10-03 04:32:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06bb2afe-eee4-3a66-8c34-108860aedec7 | -5.79789 | -45.85413 | 2025-10-03 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e5182c1a-5ddb-3728-8231-58d0debea80c | -5.28273 | -47.52212 | 2025-10-03 04:32:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f0abc84-a589-37f3-9785-2356408f9830 | -9.29644 | -45.75015 | 2025-10-03 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 470d5858-2cd5-38e7-bd10-a63b5f8cc5e3 | -9.90011 | -43.71909 | 2025-10-03 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 0d80fc32-b62c-32b9-9006-f32e8081802b | -11.64717 | -46.86286 | 2025-10-03 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 550756c4-268a-3b76-8aa5-769825c250b8 | -12.41023 | -45.16599 | 2025-10-03 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9e276c0-77e0-31df-b076-ebde35eddd51 | -7.76371 | -46.27855 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| ef72a9a4-1072-3ec3-a52a-933e26d40c5b | -10.00856 | -50.24632 | 2025-10-03 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a5a6058-c125-39c5-8d14-616ff4be8ce9 | -4.25458 | -48.56025 | 2025-10-03 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de3c8d2c-8138-38b0-a3bd-d2dd60f561ef | -11.99212 | -47.19588 | 2025-10-03 04:32:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4842e621-8f23-35e8-bde3-2685167bd4a3 | -7.75476 | -42.56179 | 2025-10-03 04:32:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 37.9 |
| 179e67ff-8d8e-334c-b472-fdfd2d0586c9 | -7.04084 | -43.31833 | 2025-10-03 04:32:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dbc2d1b0-e669-3a55-8183-f4ad951d206b | -11.14238 | -43.38522 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ecfca347-c19e-3d35-93fd-4a90f6e3f003 | -11.83324 | -45.01484 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04bb4fce-0b9d-36ba-9e59-ef9c8efee458 | -6.2369 | -44.25431 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49a40f63-3399-3c57-904a-e36c5fabc105 | -11.60023 | -47.65533 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 84d7a7a5-8406-308d-b2e5-adfa0ea2f2a3 | -5.54255 | -51.13347 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d80ef7e-a21e-331e-9275-ad6907543b74 | -9.94946 | -43.65839 | 2025-10-03 04:32:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e22b3607-c80e-3841-86fe-e6b0dd7f86e0 | -6.0915 | -43.12848 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 6.9 |
| a7d11269-ffc7-3b65-9673-0daf3d236c34 | -11.68007 | -44.28107 | 2025-10-03 04:32:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0c27d30-5200-3c1d-ab4e-92b0d5a0dbdf | -4.66619 | -45.79155 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1f008f13-4827-3f3b-b4b9-0c8abc5c7cc3 | -4.67633 | -45.79315 | 2025-10-03 04:32:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3e5f012-02f3-3b19-904e-6042e166e076 | -6.33023 | -43.88581 | 2025-10-03 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 98e756ed-6a37-3880-a766-9dde5c85096f | -7.8248 | -46.96774 | 2025-10-03 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0f8980ca-6fd5-3c01-bc09-3a01ed086abd | -10.84595 | -45.37988 | 2025-10-03 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed47bab0-e32c-3fd8-9d2a-a9769986a556 | -7.55718 | -42.65569 | 2025-10-03 04:32:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3e3d0808-2ee9-3e30-86dd-0f733a737ee5 | -6.72857 | -44.1423 | 2025-10-03 04:32:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 927046eb-c521-3c8c-b763-c9bfe3e33c96 | -9.90116 | -45.95839 | 2025-10-03 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa868bd4-9b1f-3c6a-a864-4c7d21cccd6d | -11.01884 | -46.55127 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 53fe516b-2e2b-3b2f-83a7-5b0afc070216 | -11.84931 | -44.95786 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a407480c-b2e4-3634-85ed-5cc8d1ca3841 | -6.05584 | -44.6151 | 2025-10-03 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4d9e0695-9625-36d8-a5ab-897a7a7375ef | -7.75459 | -46.26982 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 448208c6-440e-35fe-bb3f-5f3887ae2378 | -11.90582 | -46.29826 | 2025-10-03 04:32:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 64ea28df-4d3b-3f70-9830-2575efa9e99f | -6.09687 | -43.11923 | 2025-10-03 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 657eaa05-5849-3b80-9e3e-cb6e3186ac73 | -11.44148 | -43.499 | 2025-10-03 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e61fa2a9-c12a-3a03-b01c-85d817b55d15 | -10.89432 | -46.72805 | 2025-10-03 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66600148-3cbb-3160-a47f-36c60293a1da | -7.73093 | -46.23989 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 97d26bf6-4e19-317b-8f7a-c48c3c765e63 | -11.68397 | -47.50065 | 2025-10-03 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c95a3a5e-9065-3b68-8ec8-a9d19d1da55d | -7.75799 | -46.27034 | 2025-10-03 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.6 |
| a50a0c8c-2da3-3906-b6a2-0df7e37b8d5a | -10.28045 | -44.327 | 2025-10-03 04:32:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6dcc35d-5fdd-319a-918e-a0ea3c3e3467 | -9.97762 | -48.78617 | 2025-10-03 04:32:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b3bfafb-1845-3fa6-b7a9-ba81540630e1 | -11.82479 | -44.91429 | 2025-10-03 04:32:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README97.md)
