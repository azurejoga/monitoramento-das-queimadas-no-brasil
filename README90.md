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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0208e8d8-1517-3b09-a3c6-c8ca559f2c89 | -8.44001 | -49.11143 | 2025-09-11 04:44:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c15f095c-7890-3f28-b7cf-fbf1a4d6fd7f | -5.86042 | -44.21519 | 2025-09-11 04:44:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d181bbe1-7b95-3e11-948e-3e3d9f0bbe32 | -6.18306 | -43.49372 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 081ab17b-9e00-3b88-af60-2bcbba44c05e | -8.04057 | -48.67244 | 2025-09-11 04:44:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3e19196b-9e17-3fdf-8983-b39fbacc93a9 | -8.04227 | -48.66114 | 2025-09-11 04:44:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 280e5b87-3f95-3622-ac83-0196f9fd72ce | -7.99679 | -45.79776 | 2025-09-11 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ddca0fa-e42f-3665-a369-5aea3d0c39e9 | -8.03111 | -48.66315 | 2025-09-11 04:44:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d1c924e9-e4ff-3b45-8f1f-73063f363931 | -5.96261 | -45.83008 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 796c67af-7ffe-3c0c-b974-ad787f35444e | -6.09656 | -45.9333 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f01e9beb-070b-371f-98c7-67ad1ac96b27 | -3.21599 | -48.6082 | 2025-09-11 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88fb289d-bda6-3e3b-9f0f-30842a864b20 | -4.38347 | -48.06717 | 2025-09-11 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 426d256b-d6ff-32f6-a2a5-0903b800b126 | -6.48693 | -41.75102 | 2025-09-11 04:44:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 955b9cb6-5075-3397-a2b4-bc0fe2190a0a | -8.03701 | -49.04901 | 2025-09-11 04:44:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ae81c838-7d0f-3cf5-af2a-75080110945b | -7.18596 | -44.95719 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c15d980b-037a-30e2-8d9d-28f557c3d91b | -7.8877 | -46.04405 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d851ebc7-de06-3517-a2c2-9768eeaa88fe | -5.22427 | -43.69633 | 2025-09-11 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aba06782-0ab5-3229-83cb-79aeb3b70f77 | -9.07851 | -46.96576 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 1832e144-4986-3a5c-9ba6-94f8cc3133fd | -6.27561 | -43.39143 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 001e9704-07c1-3ad5-b156-e1e1c490cb01 | -7.201 | -44.97673 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a2d4ff8-d23c-3fc5-aaed-153451f625ca | -9.04664 | -45.78534 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 853e94bd-463a-3efe-9d3e-ed7dccfb4a00 | -6.24297 | -44.79998 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c87072ec-34c1-3875-8796-3be5767316db | -7.38402 | -50.88948 | 2025-09-11 04:44:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d0e7689-5e48-3fee-9d32-360ac77bae43 | -6.29318 | -53.39341 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bec6805f-6f58-3704-929d-5261012edffd | -4.22187 | -46.36007 | 2025-09-11 04:44:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 787279bb-0308-3e97-9457-177b44c09e40 | -7.18535 | -44.96143 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8d70a5c2-949f-3b00-9eed-cba9e05e2b38 | -6.41872 | -44.39714 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ace2abd7-8e09-32b7-9d74-fbbb2d14679f | -9.15959 | -45.56481 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 084d9691-ed1d-37d9-8156-82ae043891ac | -8.52044 | -45.69431 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 64f6ea5f-a4d2-3258-baf0-27b12e8a320f | -8.52156 | -45.68663 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f36bc0a-218a-39fc-b11e-25836e098015 | -5.90762 | -45.75149 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e236f72-f0a4-33dd-b14d-45a81f627d1e | -7.73378 | -50.75874 | 2025-09-11 04:44:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b459df59-ea03-3278-9710-0ff8b9922cfa | -9.04123 | -45.79273 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 999eb95b-d35d-37cd-b591-7971b5a9c7e4 | -5.22963 | -43.69212 | 2025-09-11 04:44:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ecefce16-693b-3870-b475-75243e09e4b2 | -8.06725 | -52.32577 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8c381ec-acfb-301c-890e-a1dbbc40b350 | -5.82799 | -45.27588 | 2025-09-11 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b708229b-ede1-33f8-a9fa-daae92792b42 | -6.55625 | -47.50964 | 2025-09-11 04:44:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5ff01995-653c-3616-a97b-d036081b6513 | -7.11764 | -50.76864 | 2025-09-11 04:44:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5274c3ec-d098-33b1-b48b-adae5e3aa024 | -4.92419 | -55.77874 | 2025-09-11 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7f9dcc52-b258-3619-a0a9-35800d044f4a | -3.4965 | -49.56538 | 2025-09-11 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 55914c84-c465-3264-9950-8b0bfa7ce65d | -7.22082 | -45.31055 | 2025-09-11 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a6408a7f-a4b8-3791-8e9b-95c9c39b40e9 | -7.39495 | -47.37557 | 2025-09-11 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f714dec-b66f-333f-b73c-53fbb7e6e9f8 | -6.36694 | -45.15905 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 69a01fcf-3992-35f2-945b-d84432262826 | -7.85232 | -45.50928 | 2025-09-11 04:44:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c74e330e-e69e-3ac4-a6b1-617ff42cc9ec | -3.30151 | -48.71038 | 2025-09-11 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a4847d8f-3999-37cc-98ad-ab36dd96c61a | -6.83586 | -51.8876 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20acd835-cbcb-3d98-a33a-5af1fa292326 | -5.90654 | -45.75871 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14229055-fb48-380a-961f-dfdeb3d1d4fd | -8.0489 | -52.33362 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 773267c2-eb24-3938-b3d3-5ec21d14b7fd | -7.42757 | -45.87223 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70cf0aac-26a8-3fa7-97bb-fb23e9218583 | -4.19961 | -55.13273 | 2025-09-11 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eeda8435-1665-313c-bf32-7b1a3baaab29 | -3.43656 | -52.88712 | 2025-09-11 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1c748b2-aca2-3aa5-b181-52da11193396 | -9.08921 | -47.08355 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81fc487e-04a3-310a-a659-99c326722eca | -5.65872 | -43.89489 | 2025-09-11 04:44:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84d56cae-28c2-3777-b939-2770e656d9a4 | -7.86396 | -47.85841 | 2025-09-11 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 53cc7538-7f43-3042-a7a0-8e41f5edc9a0 | -6.77394 | -55.48721 | 2025-09-11 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76242752-f6e9-3377-bdc0-53f28addb90a | -8.16776 | -46.0842 | 2025-09-11 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7633130-98af-30a9-9040-f80e6a865de4 | -3.42086 | -49.04869 | 2025-09-11 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 69c2ffad-07d6-3598-a681-b3d6a05e58c9 | -5.72884 | -45.61399 | 2025-09-11 04:44:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 322026d5-5b09-3ee5-9047-ad4b29e526a3 | -5.93477 | -45.68195 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| adc8248d-745c-33c0-82b5-5e93859f0d84 | -7.66111 | -50.2651 | 2025-09-11 04:44:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a78a25f7-000f-3292-9705-eb87db100525 | -9.07895 | -47.07194 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e3c1ad2-1dcb-36a6-8aa9-6f534dac426e | -8.0225 | -49.0507 | 2025-09-11 04:44:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 700bd206-e362-3aee-b184-0557bac9f384 | -9.05539 | -47.06912 | 2025-09-11 04:44:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8af4be1a-f175-309c-b9df-1ceccbda6525 | -4.93227 | -55.78009 | 2025-09-11 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0c6114f8-60ae-3e24-a78b-fc5d44837a74 | -7.46682 | -45.28192 | 2025-09-11 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ac83faa6-db07-3ca2-8234-842e51bb0125 | -6.32729 | -47.74252 | 2025-09-11 04:44:00 | NOAA-20 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6506fa8-43c9-39d5-8dfc-9d47a3d313bc | -6.47613 | -41.7495 | 2025-09-11 04:44:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 929fe583-d521-3aa5-863b-4c2dad2f9ab2 | -7.78388 | -46.12983 | 2025-09-11 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64e383a0-d68b-3a0c-b266-5d7b5b20e982 | -7.6425 | -49.81498 | 2025-09-11 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 31e84d15-af8e-3a7a-a347-7ba26f731632 | -3.64506 | -48.32916 | 2025-09-11 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 32c6e9fd-0e41-3dc0-ab97-7636f93cf71f | -8.05036 | -49.01885 | 2025-09-11 04:44:00 | NOAA-20 | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 07330b36-2bb8-30c6-acff-872ffa4f7e5f | -7.49194 | -54.94312 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3c4f0abc-fe7e-3f98-98d5-0a5332ddb44c | -6.40654 | -53.65128 | 2025-09-11 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6820b124-2e99-37f1-b080-9bf264cbb701 | -6.30005 | -44.59481 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cbe828a1-812f-364d-8313-aced2c46f029 | -8.03938 | -48.68032 | 2025-09-11 04:44:00 | NOAA-20 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1739619e-675e-3988-9c0b-b44f81925e7e | -6.31666 | -43.41365 | 2025-09-11 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e1ccb34-d917-3ab7-bd3d-798dc93e361d | -6.67237 | -44.13335 | 2025-09-11 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4f441ad6-6674-3318-90a2-b95df95d1082 | -5.81849 | -44.20757 | 2025-09-11 04:44:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9fed5de0-968a-3ef0-a0cd-3a4425d6b07f | -3.38743 | -47.49504 | 2025-09-11 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2077c11a-1508-3c6f-9a69-f88fb54a33cd | -6.17618 | -43.50793 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 63817c33-8913-3188-914e-117b3a1a0c05 | -8.05557 | -52.33471 | 2025-09-11 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e1f3061-08b9-3dd7-85ad-6061e4ce75ba | -7.53669 | -44.66765 | 2025-09-11 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7635a58-6fc8-32cd-9be4-6faba286ad4e | -6.85574 | -47.87967 | 2025-09-11 04:44:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 59776142-46e9-3862-99a9-8ba1928bdd65 | -6.85826 | -47.86291 | 2025-09-11 04:44:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3fb8ad66-4751-32dc-acab-6d6e592275df | -6.55794 | -43.98312 | 2025-09-11 04:44:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8718a725-54d0-38cd-86b2-9b9f5599b19f | -6.44928 | -43.5774 | 2025-09-11 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed02cf0f-6279-377d-bdae-ef2ee0d767c2 | -7.36942 | -47.41796 | 2025-09-11 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dfa26c0e-d29d-3b4e-8673-b8b328262112 | -6.40457 | -47.3287 | 2025-09-11 04:44:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 85d24a7e-4ce1-3071-84c8-1b3d78df5be1 | -5.45544 | -44.3508 | 2025-09-11 04:44:00 | NOAA-20 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8eaad747-bc19-3bff-b23e-0bf10046b173 | -8.16987 | -46.0693 | 2025-09-11 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 11c86f7b-87ec-3141-88f2-418506dd3c67 | -3.54123 | -49.32483 | 2025-09-11 04:44:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 150d8ceb-1032-3ca9-8ba8-0b08cd5e056e | -8.5258 | -45.68726 | 2025-09-11 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00359880-a2e0-35dd-a620-65c891782350 | -6.23062 | -46.15548 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49daa948-8498-3433-8418-a6533c663b88 | -3.14206 | -49.89688 | 2025-09-11 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75e6055e-edca-34de-b2dd-30752379178c | -7.49034 | -48.25148 | 2025-09-11 04:44:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7fa7d58e-5e4c-3904-9d61-397ed3972a6a | -5.93714 | -45.7197 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a82cf7be-0a2b-3b16-81ab-27b61fb0b2ff | -8.0883 | -48.23148 | 2025-09-11 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fbd9e993-7086-3622-979b-c9e5d580e747 | -8.80697 | -48.09458 | 2025-09-11 04:44:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 30f2ef88-31ad-3c68-be1f-2df3aebdb883 | -6.41423 | -44.39645 | 2025-09-11 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db907a2d-4c28-374e-9006-29ebed840e08 | -6.21269 | -43.35371 | 2025-09-11 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d7cbbf75-0ae8-3f80-b25a-a655fac562ec | -5.98383 | -45.77066 | 2025-09-11 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README91.md)
