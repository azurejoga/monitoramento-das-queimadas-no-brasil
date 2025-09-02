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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 473cfcfe-97ce-3d1d-af4d-e697334f9707 | -9.4023 | -48.0365 | 2025-09-02 14:40:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 054e8877-3f8e-37c5-8afc-1082644019bd | -11.9879 | -51.332 | 2025-09-02 14:40:00 | GOES-19 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 96.0 |
| b3b34376-0294-3dc2-ac69-186b40c8f9b3 | -6.9127 | -45.5819 | 2025-09-02 14:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| d0165f11-7b97-3fe1-928c-9a91083ab082 | -6.2038 | -43.3475 | 2025-09-02 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 195.7 |
| 1daf7453-b872-3b41-adbc-ca45f387dd29 | -10.2488 | -51.1128 | 2025-09-02 14:40:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 08cdcbf2-bb26-37cf-bed9-0f9b35189a8a | -6.4443 | -43.6998 | 2025-09-02 14:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| b42da6db-25b4-3905-8b93-4df94ecf2aba | -8.6698 | -62.401 | 2025-09-02 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 113.9 |
| 0527b21f-d662-3e6d-8fce-c893f473a626 | -7.5476 | -61.3437 | 2025-09-02 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 392.7 |
| d2f668a9-e82e-3d94-9a54-eaa531ce1173 | -9.7294 | -48.9834 | 2025-09-02 14:40:00 | GOES-19 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 198.0 |
| a1f148c6-baee-3302-9177-9be8c1f18cb6 | -7.2296 | -44.0466 | 2025-09-02 14:40:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 54e46a7b-d907-300c-9b49-33724361f59d | -12.2156 | -50.1295 | 2025-09-02 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 7abc85c5-8781-3fbe-8f85-6b19989cf0d5 | -7.1091 | -44.7474 | 2025-09-02 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 5be3bcc7-52d3-3e34-b375-40d941fd6681 | -8.6695 | -62.4389 | 2025-09-02 14:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.3 |
| e336e794-6796-37f5-a96b-d0639ba989d5 | -10.062 | -48.1197 | 2025-09-02 14:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| f7e606f5-0d04-3391-a5ef-d157ac671ec4 | -9.0141 | -45.9886 | 2025-09-02 14:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| c4a6019a-a738-3e19-b76f-44e92b8a140a | -7.6228 | -42.6501 | 2025-09-02 14:40:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 72.5 |
| bbfb41df-8bc7-31d0-ba69-f3035e9929b1 | -6.8281 | -52.8143 | 2025-09-02 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 3c90883f-b83b-3c40-b57c-4aef31e6561d | -6.9632 | -44.3477 | 2025-09-02 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| d9545eb3-9029-32f4-b586-f83621f8b410 | -11.6647 | -57.3533 | 2025-09-02 14:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 495.4 |
| a10218ab-a4c6-3c52-9b2d-649962b4780d | -11.1037 | -44.6315 | 2025-09-02 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 157.7 |
| 5b96b25b-0e22-3264-8d8d-4ba2ecc149af | -11.6644 | -57.3733 | 2025-09-02 14:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 120c3206-b36e-3bf0-9f91-37541a0cf44f | -11.6717 | -52.189 | 2025-09-02 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 4756bb4e-a5cb-3496-9aaf-cda081bdc9df | -11.9415 | -50.6131 | 2025-09-02 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 90ebcc28-9ed5-31ff-b7ae-8bf95048556e | -4.9125 | -43.1636 | 2025-09-02 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 103.4 |
| f6d64caf-8a00-351c-89e3-68041bdf7817 | -4.9122 | -43.2103 | 2025-09-02 14:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 183.2 |
| be4279c6-01b4-348d-9a7b-ccc6de8b1a46 | -8.4024 | -48.2646 | 2025-09-02 14:40:00 | GOES-19 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| cc911905-f050-3e54-b2b3-0d3d27a528c5 | -11.0841 | -44.6575 | 2025-09-02 14:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 125.8 |
| 83d5b698-97de-3fb3-bc52-7a0c543b015f | -6.3319 | -45.6062 | 2025-09-02 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 218.5 |
| f63a0e5c-6a7c-3a77-9db8-28bd5fafcd47 | -5.8644 | -45.6183 | 2025-09-02 14:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| f5d783e2-4f58-398d-9cc2-c94923183968 | -6.9629 | -44.3707 | 2025-09-02 14:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 83699d3d-b0f4-3560-8c73-02e5ce70cba3 | -6.2583 | -43.5294 | 2025-09-02 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 73767f2a-860c-31b9-90a2-6a4535832d40 | -10.2674 | -51.1322 | 2025-09-02 14:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| cbefaa54-d8b6-3276-9171-54b17c3dd314 | -11.9224 | -50.6153 | 2025-09-02 14:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.3 |
| f7e61e8d-50c4-3aa8-932e-c1f4720c00c4 | -6.3506 | -45.6047 | 2025-09-02 14:40:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 60cb6bbf-4242-334e-a4dc-b5baf5dd9186 | -6.8465 | -52.8337 | 2025-09-02 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 03b27989-37b7-3c2c-9871-870eb6d2689f | -6.185 | -43.3491 | 2025-09-02 14:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 123.6 |


