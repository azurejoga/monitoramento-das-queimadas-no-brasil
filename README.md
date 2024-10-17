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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 483363e5-ccfa-3a57-bdf4-e6245cc19d9a | -9.98572 | -36.41935 | 2024-10-17 00:03:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 64d452d6-0585-38a1-90d1-43de4e3c3d20 | -9.97627 | -36.42062 | 2024-10-17 00:03:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 32.8 |
| b5f6c834-4753-3909-ad91-62cff4581d43 | -9.30316 | -36.01217 | 2024-10-17 00:03:00 | TERRA_M-M | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 182de859-5414-3d76-9808-fb352a4278a8 | -9.30186 | -36.00246 | 2024-10-17 00:03:00 | TERRA_M-M | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 104d7d57-15ba-3b64-ae02-accd548ce60e | -8.87724 | -40.71644 | 2024-10-17 00:03:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 2052eccd-dfbf-3b63-8587-dac861ea656c | -8.73057 | -40.58847 | 2024-10-17 00:03:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 2eac0b61-2cc6-3b94-92bf-f68e0518dda6 | -8.71141 | -41.1712 | 2024-10-17 00:03:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 101.6 |
| 96c003c3-a06f-3b3c-867e-82d822cca8b6 | -8.70883 | -41.1503 | 2024-10-17 00:03:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 25.6 |
| 79111254-06e6-3c14-9519-ab58f16d9796 | -8.50991 | -39.94591 | 2024-10-17 00:03:00 | TERRA_M-M | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 17.8 |
| f17ce879-3c90-3b91-b352-4e088a680f70 | -8.50784 | -39.92906 | 2024-10-17 00:03:00 | TERRA_M-M | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 12.2 |
| a4b6edcb-cdba-313d-87ef-79e184146973 | -8.50199 | -39.9355 | 2024-10-17 00:03:00 | TERRA_M-M | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 20.3 |
| d6213226-4126-35e5-b00b-328f0701e828 | -8.47118 | -40.27525 | 2024-10-17 00:03:00 | TERRA_M-M | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 916623cf-a821-3fa0-9376-263f8c57b141 | -8.46772 | -40.28212 | 2024-10-17 00:03:00 | TERRA_M-M | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 17.5 |
| f528ccfc-f471-3d89-a239-27a8fbb1f291 | -12.14312 | -40.90462 | 2024-10-17 00:03:00 | TERRA_M-M | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 101.0 |
| d453d141-5436-3ae6-a91d-9cbd0ef1bfd4 | -8.46539 | -40.26422 | 2024-10-17 00:03:00 | TERRA_M-M | SANTA CRUZ | PERNAMBUCO | Brasil | 2612455 | 26 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 8a2a256c-2ab3-3ca5-a3db-95e549957d6f | -8.08762 | -41.08095 | 2024-10-17 00:03:00 | TERRA_M-M | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 23.2 |
| d41a436e-559d-3216-b946-915d4fbd5233 | -7.99584 | -40.97592 | 2024-10-17 00:03:00 | TERRA_M-M | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 7ebb5f2b-3473-3b03-bcaa-dfc6332eddf7 | -7.99493 | -40.96947 | 2024-10-17 00:03:00 | TERRA_M-M | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 558aadd6-a34a-3848-9cf0-358252c0d32b | -7.73899 | -42.77494 | 2024-10-17 00:03:00 | TERRA_M-M | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| e22e09ed-ac8d-3acd-90d9-4d3e238df39c | -7.72164 | -37.43518 | 2024-10-17 00:03:00 | TERRA_M-M | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 3a5941b7-feff-3e9c-b6b2-62a0732a993e | -7.1547 | -40.2337 | 2024-10-17 00:03:00 | TERRA_M-M | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 27.2 |
| 0cac7574-7161-315e-b12c-dcb94366bbea | -7.15248 | -40.21674 | 2024-10-17 00:03:00 | TERRA_M-M | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 23.0 |
| a571b751-3a3b-3fe3-9d39-b6dcea4cbe94 | -7.09926 | -40.27531 | 2024-10-17 00:03:00 | TERRA_M-M | SALITRE | CEARÁ | Brasil | 2311959 | 23 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 2f389825-dc4f-3c7b-860b-4c8fc94154b3 | -6.83297 | -38.57493 | 2024-10-17 00:03:00 | TERRA_M-M | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 8.7 |
| ee2f59b8-3a67-3c31-901f-3fbfe514f38d | -6.82092 | -35.09797 | 2024-10-17 00:03:00 | TERRA_M-M | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 53b2998f-b6e8-339c-ae42-e4477202d42a | -6.78033 | -35.20908 | 2024-10-17 00:03:00 | TERRA_M-M | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| fb04ba6c-96c3-3c56-a01f-bd9d826e252c | -6.75707 | -34.96256 | 2024-10-17 00:03:00 | TERRA_M-M | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 8fd4287d-0b8c-3130-bb6d-2ca92a8891c3 | -6.73032 | -43.56521 | 2024-10-17 00:03:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 241.1 |
| 9e1c0d00-b1fd-3051-a2d1-95e5ea953a65 | -6.72722 | -35.21656 | 2024-10-17 00:03:00 | TERRA_M-M | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 6d364f0d-aa37-3eec-aa66-d33a30ca4e7a | -6.71516 | -43.54201 | 2024-10-17 00:03:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 42.4 |
| a82b1de1-4e8f-3858-84b6-19758a4817f7 | -6.71478 | -43.56704 | 2024-10-17 00:03:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 44000748-baf3-3756-a704-9000444eec58 | -6.68414 | -43.54555 | 2024-10-17 00:03:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 51913141-68c6-300c-bbdd-83d058b8e495 | -6.67995 | -43.53952 | 2024-10-17 00:03:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| ccfa57ad-4db7-3c4e-9a98-9f277920e610 | -6.63861 | -34.98266 | 2024-10-17 00:03:00 | TERRA_M-M | BAÍA DA TRAIÇÃO | PARAÍBA | Brasil | 2501401 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| eff12c7e-040b-3e82-8d07-0f657065214d | -6.6158 | -35.01297 | 2024-10-17 00:03:00 | TERRA_M-M | BAÍA DA TRAIÇÃO | PARAÍBA | Brasil | 2501401 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 111a103b-df83-3fbf-a09a-989161e54f13 | -6.56362 | -35.1706 | 2024-10-17 00:03:00 | TERRA_M-M | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 2b2c81f1-d6e3-344c-8796-50bbb2305b8f | -6.56239 | -35.16174 | 2024-10-17 00:03:00 | TERRA_M-M | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 22.2 |
| bab4fe3a-1647-3e71-8559-e64fb4c3efab | -6.45926 | -43.2186 | 2024-10-17 00:03:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| cde1e7d9-dcfe-3a60-a006-e37e4da0a6ca | -6.21158 | -43.29871 | 2024-10-17 00:03:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 77a13637-d7d8-33d9-a144-2e5fddc26304 | -6.20952 | -43.27565 | 2024-10-17 00:03:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 47a01773-74f6-3433-97df-8c1dc7b3bd31 | -6.20811 | -43.27059 | 2024-10-17 00:03:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 3f5e71a1-a724-3c79-89ed-559ced1f0609 | -6.12103 | -35.2371 | 2024-10-17 00:03:00 | TERRA_M-M | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 24549df0-f5e6-385b-bbba-b6c196b28379 | -5.98248 | -42.14273 | 2024-10-17 00:03:00 | TERRA_M-M | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| af1b5854-facf-3be4-9970-a30591f81caa | -5.97938 | -42.11967 | 2024-10-17 00:03:00 | TERRA_M-M | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 22.9 |
| e5db4d4b-5826-3896-893f-85bfa737703e | -5.97558 | -42.13697 | 2024-10-17 00:03:00 | TERRA_M-M | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 29.9 |
| 5513b0ce-6647-3aa7-a49f-cc3b617a180c | -5.96549 | -43.38156 | 2024-10-17 00:03:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 26.1 |
| 843802ad-af7f-3d5b-988f-df3058d0ef6c | -5.96362 | -43.37504 | 2024-10-17 00:03:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 31.8 |
| e305e40b-827d-3e46-b10f-d9040620a170 | -5.94762 | -39.68409 | 2024-10-17 00:03:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 9c197956-35ad-3569-812a-b44dc90b49b3 | -4.8355 | -38.37809 | 2024-10-17 00:03:00 | TERRA_M-M | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 12.2 |
| e8d03767-562d-3ec7-91ca-0551691ec89d | -4.83399 | -38.36671 | 2024-10-17 00:03:00 | TERRA_M-M | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 78120263-e8e2-38df-8c27-202acbc0b687 | -4.79061 | -39.78409 | 2024-10-17 00:03:00 | TERRA_M-M | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| cb72f793-2cff-340a-aa44-d04076927320 | -12.14044 | -40.88132 | 2024-10-17 00:03:00 | TERRA_M-M | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 110.5 |
| 96ac1904-195d-3865-9e61-c24536bdd71f | -5.97713 | -45.38175 | 2024-10-17 00:03:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 0cb073ac-5ec1-3a56-9537-a72aede57f73 | -5.97673 | -45.38854 | 2024-10-17 00:03:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| dbb64c6a-4b4e-3508-af8c-8b7309003cc6 | -5.57441 | -44.89572 | 2024-10-17 00:03:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 62.8 |
| b00d269e-59dd-39bf-954e-a1be169b7ede | -5.57019 | -44.90297 | 2024-10-17 00:03:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 6d82bf9f-6de5-321c-bbe3-fc0c3e7cacdc | -5.1671 | -45.41289 | 2024-10-17 00:03:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 306b5c95-d6cb-32c3-81d5-5ec8cc87095b | -5.1658 | -45.41782 | 2024-10-17 00:03:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 333a662e-2f37-330d-addb-d181c3565662 | -5.16216 | -45.37217 | 2024-10-17 00:03:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 27.9 |
| 512b8a9e-f3e4-34d2-9fad-09f1bd58be3c | -5.16058 | -45.37707 | 2024-10-17 00:03:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 840f92e9-e330-37d3-9230-efabe996b4ea | -4.48528 | -42.877 | 2024-10-17 00:05:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 17c2523d-6e66-3c13-8544-b1b6987d0857 | -4.4711 | -42.87889 | 2024-10-17 00:05:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 105.6 |
| cf3639ef-8cae-37d9-afa2-3ec9efb48206 | -4.46783 | -42.85416 | 2024-10-17 00:05:00 | TERRA_M-M | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 41bcc01a-1f48-30f8-947b-57f42e4bcfc4 | -4.04936 | -43.24934 | 2024-10-17 00:05:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 971fbe9a-c716-3825-bb00-d1148b5807e9 | -3.77851 | -43.95972 | 2024-10-17 00:05:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| b3df03ed-6e6b-37db-9567-e1c4ca4e6121 | -3.7661 | -43.96642 | 2024-10-17 00:05:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| e6d77276-c268-3c7b-ae48-f61ef86a7101 | -3.40816 | -42.24804 | 2024-10-17 00:05:00 | TERRA_M-M | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 64c5eb03-198a-30bf-a9fa-9879a0c72edd | -2.96787 | -39.97023 | 2024-10-17 00:05:00 | TERRA_M-M | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 7bd743f6-657d-31f5-a93d-ab4bad7ec18c | -2.95696 | -39.97171 | 2024-10-17 00:05:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 12.6 |
| f5788482-84d8-351c-b34e-739995946cef | -4.82121 | -45.39929 | 2024-10-17 00:05:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 36.7 |
| c4c5feb8-64ba-3070-be2d-ae00c5116a53 | -4.81918 | -45.40451 | 2024-10-17 00:05:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 5d727f1e-3ac7-3dda-8c1e-a9129cb3fb89 | -4.62875 | -45.60403 | 2024-10-17 00:05:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 73b18035-adcf-3231-adb2-5575b684f230 | -4.62777 | -45.61102 | 2024-10-17 00:05:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 64353c5c-0dac-3096-8374-1f6a406cab78 | -3.60568 | -44.78136 | 2024-10-17 00:05:00 | TERRA_M-M | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 24.4 |
| ff6415e0-c0f2-316a-a569-e6a47b00d723 | -3.60142 | -44.8098 | 2024-10-17 00:05:00 | TERRA_M-M | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 74c738fa-ccb0-3302-a428-0b9cf3722cd3 | -2.6858 | -49.0752 | 2024-10-17 00:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 97.5 |
| 6ba3c178-dcb1-37dc-b77d-7a862b7ea441 | -2.6859 | -49.0539 | 2024-10-17 00:05:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 129.9 |
| 24c535f1-48d7-3ceb-a087-a85d3a812f46 | -2.8518 | -49.1556 | 2024-10-17 00:05:22 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| fd48d769-a283-3e2b-96a2-c36cc30fa032 | -2.8795 | -51.6901 | 2024-10-17 00:05:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| c31050f7-795a-3681-a790-27406febc915 | -2.8979 | -51.6896 | 2024-10-17 00:05:22 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| e86ea6c1-f872-3dca-b9f2-3bec75835b49 | -2.9674 | -47.9931 | 2024-10-17 00:05:23 | GOES-16 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 84cf30f2-f396-3c95-8c6a-deb4310cfdf5 | -3.0581 | -53.2395 | 2024-10-17 00:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 91e41fbe-90e4-34cb-9b68-a6e46061bf29 | -3.204 | -48.9312 | 2024-10-17 00:05:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 544dbe3a-6644-3e9d-a2da-a5a1bffcc225 | -3.2041 | -48.9098 | 2024-10-17 00:05:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 0fba5edd-939d-3057-8003-056e24895205 | -3.2225 | -48.9306 | 2024-10-17 00:05:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 3946cf21-11e3-3d31-bf09-3ad12e49d4f7 | -3.2226 | -48.9092 | 2024-10-17 00:05:24 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| f4ee783c-b416-357d-b849-bb31bbec0597 | -3.6822 | -45.9231 | 2024-10-17 00:05:27 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 71.2 |
| d2507eae-c848-3a94-9c9d-9a06ed8f3e7f | -3.7007 | -45.9223 | 2024-10-17 00:05:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 172.8 |
| dded0386-cfc5-3151-b89f-e40867a53bb9 | -3.7009 | -45.9 | 2024-10-17 00:05:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 152.3 |
| fb5edbd3-35ac-3dda-92f5-4dc23a81d93b | -3.7193 | -45.9215 | 2024-10-17 00:05:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 106d0690-d579-3411-b075-a862e80e191d | -3.7195 | -45.8992 | 2024-10-17 00:05:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 70.6 |
| c574e52a-79d3-34f1-8c25-6b642fc02e4f | -4.4658 | -42.8643 | 2024-10-17 00:05:31 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 9ca214fd-35dc-306b-b860-496ab51c0254 | -4.4844 | -42.8866 | 2024-10-17 00:05:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| b9aabee4-029f-39b7-a3e4-582f96269954 | -4.4845 | -42.8631 | 2024-10-17 00:05:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 143.7 |
| 1f61e225-e94a-360c-a0ea-5eee448ac300 | -4.3646 | -46.8221 | 2024-10-17 00:05:31 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 0b3dfbc6-c77f-3fd3-84f9-c9d27be0bd80 | -4.8892 | -48.9882 | 2024-10-17 00:05:34 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 3fff0d15-8333-30a6-9cb7-2ea74e439b4f | -5.2306 | -47.9566 | 2024-10-17 00:05:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 5f11d694-889d-3125-bd07-084dda3fda04 | -5.6714 | -48.6872 | 2024-10-17 00:05:38 | GOES-16 | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 4405b27f-51ec-323c-9a1d-f3d221867608 | -5.7135 | -45.7861 | 2024-10-17 00:05:38 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 5bce1e3f-3cee-3720-aa57-86e028b97a0b | -5.7137 | -45.7637 | 2024-10-17 00:05:38 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |


[Clique aqui para ver as próximas entradas](README2.md)
