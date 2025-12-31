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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1bd9cb62-3ceb-3845-b5f3-a72a3296fb38 | -17.37698 | -42.62702 | 2025-12-31 03:27:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 38dbc5d2-bfc7-3d5c-a3da-a397e0c62969 | -17.52956 | -40.62354 | 2025-12-31 03:27:00 | NOAA-20 | CARLOS CHAGAS | MINAS GERAIS | Brasil | 3113701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d07e8263-4b77-3638-9a2f-ae5f5a428271 | -17.37553 | -42.63387 | 2025-12-31 03:27:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7e10e4c3-2173-37e3-8b46-2ac7e87506ac | -33.71286 | -53.37712 | 2025-12-31 03:32:00 | NOAA-20 | CHUÍ | RIO GRANDE DO SUL | Brasil | 4305439 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| 475c6550-148a-3640-b025-c5027f8402f9 | -33.71075 | -53.3841 | 2025-12-31 03:32:00 | NOAA-20 | CHUÍ | RIO GRANDE DO SUL | Brasil | 4305439 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 70cf7965-3cd2-34b6-a7f2-56b127f7cd8f | -5.7199 | -45.0413 | 2025-12-31 03:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| ec8c97c7-4e5c-3e5a-9b67-236f42cc24c7 | -5.7199 | -45.0413 | 2025-12-31 03:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| d636f99e-2939-3154-959b-3a716ba0bd69 | -5.7199 | -45.0413 | 2025-12-31 04:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| b94e5b4e-77cb-3db7-8d42-9dcddaa8f284 | -5.9834 | -44.58952 | 2025-12-31 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44ebb339-badb-3ff6-af2c-69929470102b | -4.31015 | -43.78946 | 2025-12-31 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f57a04c8-6ac2-3bbb-8cb6-6b8781ff90c8 | -3.53271 | -43.67382 | 2025-12-31 04:14:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db112ec3-e260-3880-9235-17ecfb8a09db | -3.54942 | -43.67643 | 2025-12-31 04:14:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db655eaf-e0ef-3d58-bc00-942a80c129e9 | -6.99894 | -44.83221 | 2025-12-31 04:14:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f559845-cf54-3593-8775-c7d5b6f04c67 | -8.79035 | -38.49994 | 2025-12-31 04:14:00 | NOAA-21 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 80d06b08-b70e-3aaa-961e-279f6b703644 | -3.15479 | -48.14285 | 2025-12-31 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2731ad7b-7d27-37a0-81c1-a33cfed75966 | -6.02449 | -44.54813 | 2025-12-31 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c2fc6c9-1197-3685-8681-71ad472782b2 | -7.14825 | -45.25732 | 2025-12-31 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a370e8ea-c994-36d2-991a-ca4c28189367 | -5.62673 | -44.88799 | 2025-12-31 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 755c1826-3332-3911-9324-83cc7e7c7a60 | -7.09605 | -38.78745 | 2025-12-31 04:14:00 | NOAA-21 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| fe5ea430-2bed-3379-9232-b2da659d6e1e | -3.93901 | -42.12622 | 2025-12-31 04:14:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1e53bbb6-d8fc-37e6-b5de-aef9a2dd36cb | -1.62222 | -45.70599 | 2025-12-31 04:14:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 115f6424-5b60-3fee-a683-cd21b4243028 | -3.89488 | -42.56034 | 2025-12-31 04:14:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7f372cc4-9aee-3dce-b1de-689eee29f835 | -3.96848 | -40.91166 | 2025-12-31 04:14:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4936256f-2ea4-3231-b842-b85d1051787e | -4.50455 | -43.48687 | 2025-12-31 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b81725c-86ad-34a7-bdeb-cc68a4168341 | -1.07459 | -47.99945 | 2025-12-31 04:14:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d2dae9a-af31-3d4d-b070-5d791093ef08 | -1.07524 | -47.9954 | 2025-12-31 04:14:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9d2203f-e143-3439-93dc-d8fb1d716836 | -3.43748 | -41.67789 | 2025-12-31 04:14:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0ccc8a58-c5ed-3327-a569-1c16cc9686f3 | -7.49124 | -42.72535 | 2025-12-31 04:14:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7fcac59a-4c12-3744-b2ea-54d192eec6dd | -5.93574 | -43.51492 | 2025-12-31 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b377bd96-f276-3f83-9174-9baa76264fb4 | -5.72481 | -45.04366 | 2025-12-31 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 31.1 |
| fe0b872f-c828-3c26-897c-94a700c482cb | -5.47765 | -44.70308 | 2025-12-31 04:14:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c70975d9-9fbf-3a67-a1dd-ca3568a79641 | -3.89157 | -42.55983 | 2025-12-31 04:14:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a61dc17e-a854-3787-9db9-1148585b1d61 | -6.55809 | -43.60337 | 2025-12-31 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a3d1f32-c1d5-31a3-874f-9c85eeb5918a | -5.72422 | -45.04737 | 2025-12-31 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0e353769-7a2e-30b5-9318-6ed3650f785c | -1.08383 | -47.99673 | 2025-12-31 04:14:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b83b8a76-7dbb-3f76-a8e2-dd0e3b5a06cb | -4.43944 | -40.63512 | 2025-12-31 04:14:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 47f4d2ac-64fd-3445-b8d0-1900fde2aa5a | -4.07202 | -42.88376 | 2025-12-31 04:14:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2be8e6e7-d11d-329d-b910-98b4e050d807 | -5.53014 | -46.45455 | 2025-12-31 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3872b1e9-445c-33fe-b0c3-d84f7bca8377 | -5.72139 | -45.04312 | 2025-12-31 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a393bff-3473-34a9-9a4c-cc9d3131dab8 | -6.96276 | -46.22046 | 2025-12-31 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6dce4c57-0e78-3e84-ae2f-6f6288433a31 | -6.54704 | -43.08841 | 2025-12-31 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35c1dcc2-d77b-3d75-ad70-f45d201b49c3 | -4.76934 | -37.82176 | 2025-12-31 04:14:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 3608f2e7-4888-31c8-b929-07eb5feb6e4e | -3.55108 | -43.66585 | 2025-12-31 04:14:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bd4170f5-7448-356c-849e-d051e96ae164 | -7.14484 | -45.25678 | 2025-12-31 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9dd7c499-f2cb-319d-bb6a-ac9b09f686f8 | -1.6753 | -45.77674 | 2025-12-31 04:14:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f61ba020-8ce4-38bb-b9a0-6cb51718d500 | -5.71487 | -46.44802 | 2025-12-31 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3460ee11-d8de-3a5d-9bc5-7479df732645 | -5.05895 | -47.18781 | 2025-12-31 04:14:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b2e6431-451c-3b2b-9c4d-7f568a7bd563 | -0.93346 | -46.89071 | 2025-12-31 04:14:00 | NOAA-21 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fa88c8c8-18f9-3f04-b699-b1575ec37359 | -0.94641 | -46.93888 | 2025-12-31 04:14:00 | NOAA-21 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d744a9f-acea-3276-8ca6-aac4661adb50 | -5.79782 | -43.99963 | 2025-12-31 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83850f3a-81c5-31e6-add3-deb2f385a890 | -4.07587 | -42.88084 | 2025-12-31 04:14:00 | NOAA-21 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68f65fb4-c193-3fa1-bcfd-c84107317596 | -4.07148 | -42.8872 | 2025-12-31 04:14:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30d2d9a6-7320-37aa-b83f-4b8bf9b907fd | -1.66969 | -45.93433 | 2025-12-31 04:14:00 | NOAA-21 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca59c658-53de-3bc7-9181-c9888ad20044 | -5.54637 | -36.94223 | 2025-12-31 04:14:00 | NOAA-21 | AÇU | RIO GRANDE DO NORTE | Brasil | 2400208 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a1866120-ef62-3088-8364-6e94e4453c69 | -5.28729 | -45.83127 | 2025-12-31 04:14:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b7083acc-6c06-340e-895f-6bf7b9c24c6d | -3.49861 | -42.33204 | 2025-12-31 04:14:00 | NOAA-21 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0fd17828-cfe3-38e6-bee4-2eb37231342e | -7.48792 | -42.72483 | 2025-12-31 04:14:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 2a178a65-ff01-373e-89e0-4125ee814181 | -4.11266 | -38.72655 | 2025-12-31 04:14:00 | NOAA-21 | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e4ed7328-0124-31a9-aa3e-f84d612fe93d | -5.94406 | -44.44729 | 2025-12-31 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2bc06d0a-1b8b-3040-a87e-09701ab4b3cc | -3.54385 | -43.66833 | 2025-12-31 04:14:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d20c3bbd-76c5-3ec9-a22c-8fe6aa0d120b | -9.21563 | -35.71864 | 2025-12-31 04:14:00 | NOAA-21 | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 094bfdd4-3c5f-3f71-af2f-2e2015029946 | -5.72599 | -45.03623 | 2025-12-31 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 41d221e0-d5be-3340-83be-7cf663d6f6d8 | -3.53868 | -41.57538 | 2025-12-31 04:14:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4fef4e3e-d35b-3f79-ab0a-4cb4059cf990 | -5.92988 | -44.30637 | 2025-12-31 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13a108ca-86d8-3742-ae45-d972b56808e2 | -3.53606 | -43.67433 | 2025-12-31 04:14:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5221f727-36c0-3c69-bd81-92bae11c675b | -6.16528 | -44.7929 | 2025-12-31 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b08d2c79-af76-385f-ba09-e7f603c6545d | -5.98163 | -43.13663 | 2025-12-31 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 17ceafd2-c9e8-3f82-a537-d62fba768f63 | -2.63061 | -47.29382 | 2025-12-31 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8ef951a7-d38a-3934-ac52-d230474c52d6 | -5.7254 | -45.03995 | 2025-12-31 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 77f502ef-eb8c-3920-bbf8-16fe05d15d9d | -3.53661 | -43.6708 | 2025-12-31 04:14:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0a0c6fa-f6c4-3ebf-a6a7-e521ca71dd78 | -1.78955 | -45.8993 | 2025-12-31 04:14:00 | NOAA-21 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d1e1f46-69de-317e-9352-8ba1526424b8 | -5.04869 | -47.18792 | 2025-12-31 04:14:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b59d616-d7eb-3990-aace-82605ed2fe5f | -7.25503 | -45.48837 | 2025-12-31 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5dd9f7e-18b4-33ae-9070-da00d7ab08bc | -5.09791 | -37.54575 | 2025-12-31 04:14:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 939cb6b8-e6de-36db-a84b-20264dc73b80 | -5.04486 | -47.18728 | 2025-12-31 04:14:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 99e1a6f5-a2fa-330f-9b76-4a3d4e846da2 | -3.03353 | -44.4806 | 2025-12-31 04:14:00 | NOAA-21 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e63c39d6-a60f-38bd-b99e-98e814eab5b1 | -4.45865 | -44.12452 | 2025-12-31 04:14:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 33213a6b-b0be-300e-a829-44e0c5aaa7c1 | -3.555 | -43.68451 | 2025-12-31 04:14:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc20d212-a897-3f02-8e9a-5d26ca9bf27e | -6.23407 | -40.63221 | 2025-12-31 04:14:00 | NOAA-21 | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 41eb35c5-6aff-3eb9-8bdf-00fb680734f2 | -3.56181 | -42.32129 | 2025-12-31 04:14:00 | NOAA-21 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 67bd9b85-2869-31b6-af1e-8584709894ef | -5.71592 | -46.21085 | 2025-12-31 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e4d222b-4558-3d33-9471-af8e31a7c052 | -5.7534 | -47.95223 | 2025-12-31 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3c608b7-544b-335e-b2d3-4dc54dc61c49 | -9.21067 | -35.71789 | 2025-12-31 04:14:00 | NOAA-21 | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 30cfc5a6-13e1-363c-8e58-63745e438457 | -4.03368 | -38.2511 | 2025-12-31 04:14:00 | NOAA-21 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 24967353-84ea-32a0-a11b-aed66ef3390c | -2.90163 | -45.10326 | 2025-12-31 04:14:00 | NOAA-21 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6bc50fcd-e1f5-306b-90c0-4b0d4c325eef | -2.70541 | -45.59679 | 2025-12-31 04:14:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c66334b9-9fe8-3c58-910a-77900ffe7a99 | -5.67387 | -45.20878 | 2025-12-31 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 95b0de72-c798-3a74-aca2-4f1cc3bb3c08 | -6.22765 | -43.6925 | 2025-12-31 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc2a8efc-92ac-3e51-84c8-50ac46e7cd8b | -1.62152 | -45.71033 | 2025-12-31 04:14:00 | NOAA-21 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2851b279-c41a-3246-a6da-fa38742b896f | -4.7688 | -37.82528 | 2025-12-31 04:14:00 | NOAA-21 | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 1a4c9dd1-d390-3050-93c3-32a92be4a493 | -6.58898 | -44.20475 | 2025-12-31 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1cb620f3-b012-3883-b459-2841fe639a38 | -6.16586 | -44.78926 | 2025-12-31 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 429e7886-2fbb-331a-800f-0634c85466c1 | -4.46201 | -44.12504 | 2025-12-31 04:14:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e323a0e0-fa9a-3e3c-a463-e48c2fa65f82 | -3.54106 | -43.66428 | 2025-12-31 04:14:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0c9f09a-4d34-3fe0-a22a-3b3b70590f83 | -9.72361 | -36.67353 | 2025-12-31 04:14:00 | NOAA-21 | ARAPIRACA | ALAGOAS | Brasil | 2700300 | 27 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 13d592f7-7111-3b6f-91d3-e2d3e17aa9e3 | -6.29579 | -46.99806 | 2025-12-31 04:14:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28d0f5e9-2d9d-3124-973b-4f47d2963007 | -3.54887 | -43.67995 | 2025-12-31 04:14:00 | NOAA-21 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 16dd199c-655d-313e-9735-16d51c9aba1d | -4.62716 | -47.94086 | 2025-12-31 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90896fad-3c0d-3e4e-94b0-f8282798eab5 | -4.60913 | -45.67434 | 2025-12-31 04:14:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 207a305d-4100-334f-a6bc-0325df0f6ed8 | -2.90515 | -45.1038 | 2025-12-31 04:14:00 | NOAA-21 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README5.md)
