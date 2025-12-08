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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d60bab3a-42a9-33a1-8fff-2d2da2f9d737 | -5.08115 | -37.98718 | 2025-12-08 03:53:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 83bd1661-7416-368e-b097-a21cae62c39e | -2.30909 | -45.55598 | 2025-12-08 03:53:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b01407a2-afe4-3dbe-a620-e153b71d533b | -2.10028 | -46.65796 | 2025-12-08 03:53:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2c0bd1bb-15fa-3de5-b9f5-34de968d9a68 | -4.83239 | -38.72252 | 2025-12-08 03:53:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3db0cd48-6cba-3380-9a34-c0523e9c3eff | -3.65652 | -47.16865 | 2025-12-08 03:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36919f6e-2c4f-3940-bb39-15423fceab90 | -5.08796 | -40.23582 | 2025-12-08 03:53:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9e150ce6-708b-330a-84d6-ff6b723e0bd6 | -0.89845 | -47.34724 | 2025-12-08 03:53:00 | NOAA-20 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b11d9104-92ff-3043-810d-a04b71084451 | -0.90092 | -47.34229 | 2025-12-08 03:53:00 | NOAA-20 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 07833752-bab8-34f2-9aef-d0bc3bf55361 | -5.09935 | -40.36157 | 2025-12-08 03:53:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4d35263b-7c74-380d-be38-557a1c311b49 | -2.63695 | -46.9654 | 2025-12-08 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| de9fea9a-6225-3fe9-9e5d-411fc1c9e40c | -3.47161 | -44.88327 | 2025-12-08 03:53:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e6f9a0bb-6231-32c9-9116-76f12560d28d | -2.63211 | -46.96106 | 2025-12-08 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eec06414-b53a-3248-9d89-e72863e18ecc | -2.6418 | -46.96978 | 2025-12-08 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 018791a3-7ed2-32cd-b4be-359f568ebbf4 | -1.11462 | -46.5496 | 2025-12-08 03:53:00 | NOAA-20 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 896c48d3-fce5-386e-8b0d-5f059d5aef00 | -3.38894 | -44.16543 | 2025-12-08 03:53:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b1b06ae-fc56-341e-8f9a-b9c7da3d98e6 | -0.90027 | -47.34623 | 2025-12-08 03:53:00 | NOAA-20 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68fe11ec-b0ac-3030-895c-ad93958581cc | -2.73007 | -44.00652 | 2025-12-08 03:53:00 | NOAA-20 | ICATU | MARANHÃO | Brasil | 2105104 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d49b9e98-620f-3bca-bb2e-ff293fb5bf2b | -2.25298 | -46.12245 | 2025-12-08 03:53:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3412c4e-d9cb-351a-a5a6-503eacc6c796 | -5.08735 | -40.23958 | 2025-12-08 03:53:00 | NOAA-20 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| afe453a0-5d3b-39af-aaa0-30d698da22e4 | -3.38391 | -43.51547 | 2025-12-08 03:53:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 82ea7413-c430-303e-a33d-e5a6d124a613 | -1.67981 | -45.86634 | 2025-12-08 03:53:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 351dc424-5af1-3f4f-8c6a-a13ae0938d64 | -1.13283 | -47.16811 | 2025-12-08 03:53:00 | NOAA-20 | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 099fcb1e-4d69-3de2-9a17-1ed1a39293cb | -1.67471 | -45.86544 | 2025-12-08 03:53:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79e133e7-816a-3526-b944-329334c3b715 | -5.08618 | -43.66043 | 2025-12-08 03:53:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dfef613f-3178-3226-ba91-cb6b96949361 | -1.67685 | -45.87042 | 2025-12-08 03:53:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53fbf4e1-f035-3608-b967-98489823a08a | -3.32794 | -42.84179 | 2025-12-08 03:53:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 54a47836-33ff-3bcb-8f6f-3746ffa8a276 | -4.73693 | -44.44351 | 2025-12-08 03:53:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cfef7829-14dd-3911-9488-350643f32523 | -3.88831 | -42.28531 | 2025-12-08 03:53:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0829d1d4-ffd1-320d-9a93-df4f987f06e6 | -1.67224 | -45.86657 | 2025-12-08 03:53:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 79de622f-4e11-3981-9ca8-5a1e4ca9e1fe | -0.89906 | -47.34332 | 2025-12-08 03:53:00 | NOAA-20 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9ab0d337-8c2f-3766-9455-645e945fd92a | -3.33199 | -42.84244 | 2025-12-08 03:53:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e8353a37-faa5-3c0f-ba85-5b4628ae57d4 | -4.73767 | -44.43916 | 2025-12-08 03:53:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d13c4bb3-8e7b-3363-971f-8b335466420f | -0.90477 | -47.34426 | 2025-12-08 03:53:00 | NOAA-20 | SANTARÉM NOVO | PARÁ | Brasil | 1506906 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 92bef195-4dfb-3f19-81e1-ec375b5b2889 | -3.38966 | -44.1611 | 2025-12-08 03:53:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2ef426d-1378-3a83-9d24-6d4dea9712cc | -3.97137 | -42.51236 | 2025-12-08 03:53:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a7fb89c1-7a98-354f-8f9f-fc6dbc9c6587 | -4.83294 | -38.71905 | 2025-12-08 03:53:00 | NOAA-20 | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| aa4dacca-0a2a-3ae1-9934-f6c2624f8e8e | -3.19846 | -41.50074 | 2025-12-08 03:53:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e1d512b9-581a-3476-8a66-abef98b18a7c | -4.49494 | -40.50851 | 2025-12-08 03:53:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1c816aef-8a87-3dc1-82b0-7e343959e31f | -2.72898 | -44.00888 | 2025-12-08 03:53:00 | NOAA-20 | ICATU | MARANHÃO | Brasil | 2105104 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4f245d7-3e1f-3129-8319-8d23cd7cabf8 | -4.96193 | -36.9482 | 2025-12-08 03:53:00 | NOAA-20 | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 221ed6b3-502b-375c-86c0-72417b77512f | -4.47148 | -42.99179 | 2025-12-08 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b5d0b7f0-9b7d-3710-b0bb-5cc0b991b7a4 | -5.2672 | -37.90665 | 2025-12-08 03:53:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 57914bc1-96cc-3228-81bc-d685edb77a9a | -1.67424 | -45.86842 | 2025-12-08 03:53:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a4918ea-c50c-354f-aefa-2ef2c0927fe2 | -2.25348 | -46.1194 | 2025-12-08 03:53:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9b122ed-38d8-300e-a324-c338e4c96180 | -4.49557 | -40.51213 | 2025-12-08 03:53:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7b0cf284-df28-3c94-b43a-088a89f104d6 | -3.39335 | -44.1662 | 2025-12-08 03:53:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5bb4837b-1527-3053-9df9-78996dcc5c72 | -3.69941 | -42.79379 | 2025-12-08 03:53:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4834343c-f645-3b4f-8eee-d4be867f5958 | -1.75679 | -45.86213 | 2025-12-08 03:53:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 24322886-1f1a-3204-acaa-f666eedd7109 | -2.64238 | -46.96623 | 2025-12-08 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 154a2228-49b4-3f02-9b85-89b7fdcfaf69 | -4.49432 | -40.51244 | 2025-12-08 03:53:00 | NOAA-20 | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ecd6bdcb-c336-3045-a747-c03b7db68e2f | -1.67934 | -45.8693 | 2025-12-08 03:53:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fae8e43f-b13d-32f1-bd09-27214018059a | -4.46746 | -42.99115 | 2025-12-08 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e65409b1-f987-3235-b75d-506e46be9eeb | -1.67734 | -45.86746 | 2025-12-08 03:53:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28f65742-f6c5-35d8-a4d2-25e3f5684e5b | -3.65111 | -47.16778 | 2025-12-08 03:53:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b8650ea6-7d32-39aa-94b4-80447a07c6b3 | -7.80102 | -35.29379 | 2025-12-08 03:55:00 | NOAA-20 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a1fd3947-e937-37cd-aee3-f6a58c666f08 | -11.48784 | -37.94061 | 2025-12-08 03:55:00 | NOAA-20 | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 40b89e16-cb22-31c0-976f-6cf94fad216d | -7.41728 | -35.18411 | 2025-12-08 03:55:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 35c95d51-554e-3168-8220-3c9ae6a63378 | -8.51385 | -37.94823 | 2025-12-08 03:55:00 | NOAA-20 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 62b5aa51-90a5-3b6a-aa6c-673fd33005ed | -5.49475 | -42.16739 | 2025-12-08 03:55:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 84c74aa4-c653-3fd3-b568-4baf74ccd26f | -9.40378 | -35.84177 | 2025-12-08 03:55:00 | NOAA-20 | MESSIAS | ALAGOAS | Brasil | 2705200 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bc109930-a522-306b-93c2-9e50eac7b1fa | -5.64474 | -40.68197 | 2025-12-08 03:55:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3236f101-055e-34fd-bddb-c7ca25c8d3ea | -5.64411 | -40.6859 | 2025-12-08 03:55:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 77bbd27a-4657-3690-9a0a-9e6bda3adb62 | -6.63142 | -39.11868 | 2025-12-08 03:55:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b5f947e8-776d-3923-a465-5c4c7d69a2ef | -6.66299 | -35.10838 | 2025-12-08 03:55:00 | NOAA-20 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c68f75d1-2a1d-377c-ad0f-64860e6bad35 | -5.49025 | -42.17131 | 2025-12-08 03:55:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 62c2c971-2db3-300c-baea-2e880e06e2ff | -6.63197 | -39.1152 | 2025-12-08 03:55:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1b97173d-0fbb-34b6-b662-3588d7998fe3 | -7.80836 | -35.29485 | 2025-12-08 03:55:00 | NOAA-20 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 5ac402fe-a359-3aae-a822-1ae4a303e9bd | -6.63474 | -39.11921 | 2025-12-08 03:55:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1a02548b-e2fe-3ae1-9d34-569bec21f601 | -7.80374 | -35.2969 | 2025-12-08 03:55:00 | NOAA-20 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a18e7d16-6db3-3633-85fb-fb437029ec8d | -5.77081 | -40.4627 | 2025-12-08 03:55:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1092ea3d-b571-3c28-a20a-f135d58ee66f | -5.77142 | -40.45892 | 2025-12-08 03:55:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 76e94430-3522-3d49-8d12-e61ea5277c58 | -6.63529 | -39.11573 | 2025-12-08 03:55:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| cecfe588-3cda-38b5-b99b-5b57b03edda6 | -5.43649 | -50.75184 | 2025-12-08 03:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c633b456-5e30-343c-8b09-25a77f69d20d | -6.63805 | -39.11973 | 2025-12-08 03:55:00 | NOAA-20 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0a21663e-706d-358d-ac05-cdf8b5a971ed | -7.80469 | -35.29432 | 2025-12-08 03:55:00 | NOAA-20 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 255f8cec-480c-34ed-85c7-01fafb238257 | -5.49851 | -42.16801 | 2025-12-08 03:55:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9a3473d2-396d-34d1-b0f4-72960c9d83d5 | -5.494 | -42.17194 | 2025-12-08 03:55:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 32e859f3-dfd0-3b1f-b052-4ac1e18e6a0a | -7.41664 | -35.18842 | 2025-12-08 03:55:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| eb5c0ffc-53b6-316f-8217-cdbc60ee22ae | -10.14354 | -36.37704 | 2025-12-08 03:55:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2196d84a-fbf3-3af3-b1d2-ef72922d009e | -5.14779 | -43.96328 | 2025-12-08 03:55:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6f72766-c57c-3338-95de-994e0e390074 | -6.0079 | -40.31869 | 2025-12-08 03:55:00 | NOAA-20 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a2a17afb-4a22-3115-b36c-06dea675b831 | -7.80805 | -35.29307 | 2025-12-08 03:55:00 | NOAA-20 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 96dab3e2-f883-38ae-bfd4-1e543ff53644 | -7.80438 | -35.29252 | 2025-12-08 03:55:00 | NOAA-20 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 08803f4b-d33e-3024-a4ba-5f5c35878936 | -7.80741 | -35.29743 | 2025-12-08 03:55:00 | NOAA-20 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 95ef7bde-7d5a-3419-99a2-add1533c0e3f | -21.42402 | -46.64286 | 2025-12-08 03:59:00 | NOAA-20 | TAPIRATIBA | SÃO PAULO | Brasil | 3553609 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 05e1a751-b63d-3abb-9d45-3bd35749a283 | -21.72168 | -45.58005 | 2025-12-08 03:59:00 | NOAA-20 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 63cc8c1a-90a6-3b4a-a131-a6d903a3bf4d | -24.04449 | -48.68428 | 2025-12-08 03:59:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 73cd68a9-ec02-3dcb-b0cc-429bc951c1a5 | -22.8961 | -43.65632 | 2025-12-08 03:59:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d4fb66eb-3a38-3289-90f2-a2ad5a391fb2 | -30.52368 | -51.76107 | 2025-12-08 04:01:00 | NOAA-20 | CERRO GRANDE DO SUL | RIO GRANDE DO SUL | Brasil | 4305173 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 6fa0f91e-cc6d-37e6-9115-0150557d78fb | -29.3062 | -50.51236 | 2025-12-08 04:01:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 38dd0b8f-2d2d-340f-a894-7356a88a3ec5 | -29.30713 | -50.50797 | 2025-12-08 04:01:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7e946cac-5f80-3ccb-8c40-ff2905dc8db8 | -29.30804 | -50.50359 | 2025-12-08 04:01:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 37851b3e-5778-38d9-b5ad-74891bfe0e63 | -29.31126 | -50.50912 | 2025-12-08 04:01:00 | NOAA-20 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 156f781b-2343-39fb-a3ac-0e694fd85ad3 | 3.3973 | -51.2612 | 2025-12-08 04:20:00 | GOES-19 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 5dd9b32c-82b2-39ad-8df1-16c73e1820af | 3.41477 | -51.25007 | 2025-12-08 04:42:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 015bb3bb-fc0a-30f3-8fac-c249841308fe | 3.47579 | -51.24136 | 2025-12-08 04:42:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64e40fec-4dc3-3838-a3e0-3db305d09563 | 3.40781 | -51.25113 | 2025-12-08 04:42:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 962e0ee8-fbe9-39f5-8f85-421f046767f3 | 3.40492 | -51.25549 | 2025-12-08 04:42:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1c18ec10-50c3-35ab-97c5-b1fc38fb69b3 | 3.42008 | -51.2498 | 2025-12-08 04:42:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b6995107-4bca-339c-8863-cc564dc14212 | 3.41825 | -51.24955 | 2025-12-08 04:42:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README3.md)
