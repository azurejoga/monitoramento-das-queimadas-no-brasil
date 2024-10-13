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
| 8087e6bb-9e9e-3fb5-9725-b9db2592bde1 | -7.3823 | -47.2586 | 2024-10-13 00:25:48 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 1590f192-699f-3e04-b156-30c96deb4361 | -7.3657 | -64.6656 | 2024-10-13 00:25:49 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 21d9bc22-dba9-3f6e-a312-46d26115e045 | -7.3841 | -64.665 | 2024-10-13 00:25:49 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 128.5 |
| 150cec0a-51a5-3d00-b9b3-d34ff4339894 | -7.3842 | -64.6464 | 2024-10-13 00:25:49 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 102.4 |
| fbebd95a-0fd7-3705-83cf-8007d862a9ef | -7.6627 | -47.3229 | 2024-10-13 00:25:50 | GOES-16 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| a1ac048c-b487-3ca3-8a15-b20459198bfa | -7.6629 | -47.3009 | 2024-10-13 00:25:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 74.3 |
| be33ecf7-63f8-32b1-9944-c325445f1563 | -7.6815 | -47.3213 | 2024-10-13 00:25:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 90798fc3-2669-3c9b-84d1-27f81ea7d0b9 | -7.6817 | -47.2992 | 2024-10-13 00:25:50 | GOES-16 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 3d84380a-f386-3d9f-820a-bfbd54693c79 | -7.9003 | -44.6264 | 2024-10-13 00:25:51 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 41862944-1a3f-3a0d-a91d-1d7a76bfa325 | -7.9006 | -44.6035 | 2024-10-13 00:25:51 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 5cff7910-3fb3-3713-903f-9d1ded9a84a6 | -7.8715 | -54.7016 | 2024-10-13 00:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 3b640384-66d1-335a-bc74-82519e24d2f1 | -8.0675 | -44.8158 | 2024-10-13 00:25:52 | GOES-16 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 2f9417bc-2d12-34fb-8df0-e410644c403a | -8.2352 | -64.0961 | 2024-10-13 00:25:54 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 89.8 |
| a4b13555-294e-3d79-9273-ea0dcb3f73b4 | -8.2352 | -64.0773 | 2024-10-13 00:25:54 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 3f973803-293f-3a41-90a3-369705bd8603 | -8.6856 | -46.6061 | 2024-10-13 00:25:55 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 8275dc63-1dfb-3f3f-ac6d-63951d133b17 | -8.7042 | -46.6266 | 2024-10-13 00:25:55 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 1c3f3b5f-50f1-38bb-877c-4f6a55020818 | -8.7045 | -46.6042 | 2024-10-13 00:25:55 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 186.7 |
| 709b7c19-390e-393f-853e-415d5ed074c1 | -8.7048 | -46.5819 | 2024-10-13 00:25:55 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| c9a9a151-2c06-306d-8a7a-dd91860682b0 | -9.7359 | -64.2295 | 2024-10-13 00:26:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 82.2 |
| b1e795fa-e25a-3142-81b1-277de4666917 | -10.9311 | -44.6789 | 2024-10-13 00:26:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 12ea70e2-7615-3f0c-a1a2-f11620820e6d | -10.9315 | -44.6557 | 2024-10-13 00:26:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| ab933ec8-18ab-3788-9126-5859fa15456f | -10.9502 | -44.6762 | 2024-10-13 00:26:08 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| e0c6e93e-ca3e-3e65-a650-d2262bb4132e | -10.8567 | -63.9177 | 2024-10-13 00:26:09 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 098e062a-8414-3b29-822d-dafba0177f99 | -11.2532 | -50.9249 | 2024-10-13 00:26:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| af09fcf0-cb9c-3db8-9975-5a794b8a13da | -11.2535 | -50.9036 | 2024-10-13 00:26:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 421fb633-9bf2-3973-af60-7c4485cf8bd4 | -11.2722 | -50.9228 | 2024-10-13 00:26:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 4ed732a4-1159-370c-b950-02607e8c05b1 | -11.2725 | -50.9016 | 2024-10-13 00:26:10 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 59224e95-798e-33b8-89d7-fb7eb78d56e6 | -11.7479 | -48.3591 | 2024-10-13 00:26:13 | GOES-16 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 50ac21ea-0568-364d-a810-c694ea520471 | -11.7308 | -64.9769 | 2024-10-13 00:26:14 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 119.9 |
| 21053a52-63ec-3e13-b43a-22c2d7f108bc | -12.2751 | -47.6696 | 2024-10-13 00:26:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 538818f6-e30c-3926-8085-da25d48cb764 | -12.2754 | -47.6473 | 2024-10-13 00:26:15 | GOES-16 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 130.2 |
| cb0a8799-481b-3e3a-9937-c35a25b42a90 | -12.3793 | -63.7294 | 2024-10-13 00:26:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 2535e1ce-11d4-32e0-b3c6-9c53ed811aa9 | -12.398 | -63.7475 | 2024-10-13 00:26:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 133.8 |
| 0237a605-e8af-3fd3-a17a-2d11fb0ce8ea | -12.3982 | -63.7284 | 2024-10-13 00:26:17 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 206.8 |
| 310610b0-dff8-39f7-a418-4e648c926a1d | -12.7688 | -62.2872 | 2024-10-13 00:26:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 89.4 |
| c6dbfc43-65a9-3660-9546-42656d47769e | -12.9182 | -62.5287 | 2024-10-13 00:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 118.4 |
| 7e341eac-35ef-348f-9dbf-c16add5e292e | -12.9372 | -62.5275 | 2024-10-13 00:26:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 163.2 |
| 421a04dd-7038-388e-80ef-b2d8d0b349b0 | -13.1475 | -62.3215 | 2024-10-13 00:26:21 | GOES-16 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 160.2 |
| d5353eb6-01b0-3f3f-a6c9-c3c4b8c6f409 | -13.7153 | -60.6289 | 2024-10-13 00:26:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 7e9eb40e-1341-3430-b5e8-ca3ff93f5e54 | -13.7155 | -60.6093 | 2024-10-13 00:26:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 50ca34d3-bcc4-3d5d-85fd-3cfc807a774c | -13.7346 | -60.6079 | 2024-10-13 00:26:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 123.8 |
| df995cdf-4744-3f71-93d0-98bb84648114 | -13.7348 | -60.5883 | 2024-10-13 00:26:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 133.8 |
| e88da13e-3e91-3d3e-8f4d-a6ce8a7b6b15 | -14.7638 | -57.799 | 2024-10-13 00:26:30 | GOES-16 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 109.4 |
| d232e357-bc14-33bc-a5cc-4183db0f4615 | -14.7641 | -57.7789 | 2024-10-13 00:26:30 | GOES-16 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| b27ea94e-6e46-3e0b-ba41-09292ac204e9 | -14.7831 | -57.7971 | 2024-10-13 00:26:30 | GOES-16 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 957a5a5b-0224-3341-9744-0a57a2f08327 | -15.6419 | -59.9767 | 2024-10-13 00:26:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 3a819063-b461-33b0-a8ef-e84a85018e0e | -15.6421 | -59.9568 | 2024-10-13 00:26:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 87fcdf95-0de0-3c93-9f6a-b269eb580383 | -15.6612 | -59.975 | 2024-10-13 00:26:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 4434884f-a019-36c0-91ec-588435c20b36 | -15.9437 | -59.0897 | 2024-10-13 00:26:36 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 60cc8f1b-5b56-3850-8dad-d2d97baa9fe3 | -15.9629 | -59.1079 | 2024-10-13 00:26:37 | GOES-16 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 61.1 |
| fe86556d-4044-31e0-9f51-a77df76ba6ef | -16.9998 | -57.4586 | 2024-10-13 00:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.7 |
| 1fa327ef-5493-3e9f-a0ef-3b3840fde127 | -17.0001 | -57.4381 | 2024-10-13 00:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 90.9 |
| abcac461-f741-3a4f-b5f4-65b8232964ed | -17.0626 | -56.01 | 2024-10-13 00:26:42 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 58.5 |
| 5809e342-553a-3006-be22-8429eb3e2809 | -17.1172 | -57.4654 | 2024-10-13 00:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.9 |
| a0c0fd4d-e675-3648-8e61-96c287c8bbb9 | -17.1758 | -57.479 | 2024-10-13 00:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 129.1 |
| ec9a8e7f-5dcd-3e32-ad86-b8886de9aa3c | -17.1761 | -57.4585 | 2024-10-13 00:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 198.8 |
| 42b42512-cdaa-3de1-b51c-aa736656917d | -17.1764 | -57.438 | 2024-10-13 00:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 108.3 |
| 090e2099-62a0-3c2d-b669-a2313fbd22dc | -17.1954 | -57.4767 | 2024-10-13 00:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.2 |
| 06723cce-a627-3a09-a0ea-c544544e127b | -17.1957 | -57.4562 | 2024-10-13 00:26:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 140.4 |
| 5b923a8f-9c2d-320b-a438-e7700e14b420 | -17.964 | -57.3843 | 2024-10-13 00:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 129.7 |
| 8823882d-db63-34d8-9093-52980ae1d1a7 | -17.9643 | -57.3637 | 2024-10-13 00:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 159.9 |
| 211b7afa-8570-38be-8397-0cae713da2ec | -17.9837 | -57.3819 | 2024-10-13 00:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 103.8 |
| 02d797b0-f146-3511-a065-6d847253fdb1 | -17.9841 | -57.3612 | 2024-10-13 00:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 144.1 |
| 04acba8e-692a-367c-9747-1da332a2f5dd | -18.1902 | -56.8601 | 2024-10-13 00:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 93.2 |
| 56bd13c2-4ece-3266-8daf-a61b32e7fa48 | -18.1905 | -56.8394 | 2024-10-13 00:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.9 |
| e280d029-6fb0-321c-95dd-41df0c27f3e3 | -18.1949 | -56.5899 | 2024-10-13 00:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.7 |
| ec8bc1a3-4e1f-3281-97d9-f509c6977f6b | -18.1953 | -56.5691 | 2024-10-13 00:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 155.1 |
| f9062d11-d79a-323a-a38b-9705a2679108 | -18.2147 | -56.5873 | 2024-10-13 00:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 179.9 |
| 45f63f1c-fc67-395f-ba21-945ca771badf | -18.2151 | -56.5665 | 2024-10-13 00:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 335.4 |
| 8b077ff3-1f73-32bd-bd3b-cbdbba4788f4 | -18.2155 | -56.5457 | 2024-10-13 00:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 122.6 |
| 566243dc-f7f1-3b8b-a3f1-eb4a22b9159f | -18.2166 | -56.4832 | 2024-10-13 00:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 140.9 |
| 61371dad-60c9-394d-a5ae-cc2f9b40f491 | -18.2169 | -56.4624 | 2024-10-13 00:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.0 |
| 825458d6-1364-301c-b477-da534cbea022 | -18.2364 | -56.4806 | 2024-10-13 00:26:49 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 128.6 |
| ac7f2d00-2c6b-3a94-9e7d-e984c4fe0e29 | -17.38394 | -39.24776 | 2024-10-13 00:35:00 | TERRA_M-M | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 1f252ce1-e91d-30f3-9ba3-f582dcdc1a96 | -1.733 | -54.173 | 2024-10-13 00:35:16 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| c35bf65a-c134-3385-af20-cdcfff0665c2 | -1.9486 | -56.4692 | 2024-10-13 00:35:17 | GOES-16 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 55.6 |
| a43174dc-2e56-34d1-99d7-9e0a91e10050 | -1.9486 | -56.4496 | 2024-10-13 00:35:17 | GOES-16 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| b5d30268-2381-335a-a162-d6783d3d29b6 | -2.1692 | -48.8322 | 2024-10-13 00:35:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| 9a28853a-301c-30ce-9ede-694bd5ea9a85 | -2.1693 | -48.8108 | 2024-10-13 00:35:19 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 31103a56-150b-3ff5-bb01-a349e629bb8a | -3.0731 | -54.2473 | 2024-10-13 00:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 111.0 |
| 836e1aab-348b-3dc3-893e-c8d9c80fdc12 | -3.0732 | -54.2273 | 2024-10-13 00:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 273de6cc-e123-3e4e-a22b-d1149ac36f19 | -3.0773 | -53.036 | 2024-10-13 00:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 9d067abf-23c9-38f2-95cd-d1bdf26ac99a | -3.0915 | -54.2469 | 2024-10-13 00:35:24 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 1b60aa0b-2281-38c3-a6c8-d76114a7d039 | -3.0956 | -53.0559 | 2024-10-13 00:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 136.3 |
| 3914514d-6045-3c5c-815d-aee47e2b5378 | -3.0957 | -53.0355 | 2024-10-13 00:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 253.5 |
| 2dfe018e-e01a-338a-bb09-4291b518cbb8 | -3.0957 | -53.0152 | 2024-10-13 00:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| c3f5a181-f673-38b7-87d6-a1c6f52b57a5 | -3.114 | -53.0554 | 2024-10-13 00:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| f1fd8707-63d2-3594-a0e1-88d5de2565de | -3.1141 | -53.0351 | 2024-10-13 00:35:24 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 124.1 |
| f3a5032d-ad30-33c8-bb81-a6c64fe7c565 | -3.1791 | -50.476 | 2024-10-13 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 325343da-dcab-3845-8c40-7ba42a394715 | -3.1792 | -50.4551 | 2024-10-13 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 66460986-7c89-3928-8ac8-428ef2e21472 | -3.1976 | -50.4545 | 2024-10-13 00:35:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 1102db9c-b776-31be-90dc-472d528bb270 | -3.5264 | -51.257 | 2024-10-13 00:35:26 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 00eaec3f-de3e-3184-8651-2b578ff85e5c | -3.5449 | -51.2564 | 2024-10-13 00:35:26 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 56669227-e374-389c-953a-1c95e8571c73 | -3.7128 | -40.7102 | 2024-10-13 00:35:27 | GOES-16 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 83.7 |
| 20e5262e-d1ae-311f-81ad-6c4c473a7754 | -3.7316 | -40.7092 | 2024-10-13 00:35:27 | GOES-16 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 63.4 |
| 8be18248-1fd2-3c7e-bfc3-29a455ac1a77 | -3.6066 | -54.1325 | 2024-10-13 00:35:27 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| c49e1f51-0321-3c83-b8c6-c3f05fd35a47 | -3.625 | -54.132 | 2024-10-13 00:35:27 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| cb11207a-d7dd-38b2-ae6c-dc1640fbc397 | -4.1148 | -48.2515 | 2024-10-13 00:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 140.8 |
| 02e0873f-14d6-3784-9baa-9a71525c2ff3 | -4.1149 | -48.2299 | 2024-10-13 00:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 113.4 |
| 07864806-2831-32ae-8bcf-7f292a2867f1 | -4.1479 | -45.7896 | 2024-10-13 00:35:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 80.7 |


[Clique aqui para ver as próximas entradas](README5.md)
