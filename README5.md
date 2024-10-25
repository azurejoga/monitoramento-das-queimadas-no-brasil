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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d7dc8a0-280e-34ed-9fa7-19339935b92b | -10.64752 | -47.90687 | 2024-10-25 00:26:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 1078cfb1-b709-357d-8684-5fbddb5254f3 | -10.47836 | -48.29742 | 2024-10-25 00:26:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 5518a3fb-b0ab-37dd-bb78-586ecb5afc94 | -10.47528 | -48.27215 | 2024-10-25 00:26:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 3b8d1206-3f01-3999-b1ef-bbf67d24be61 | -10.46758 | -48.29308 | 2024-10-25 00:26:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| d7bf2698-d83d-363a-8593-5be419bad634 | -10.46289 | -47.34344 | 2024-10-25 00:26:00 | TERRA_M-M | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 576cf2de-fead-39b2-acfd-9dd78ccedf0d | -10.44434 | -48.089 | 2024-10-25 00:26:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 530c8d63-e938-35fc-91a1-2724097626ad | -10.43935 | -48.09489 | 2024-10-25 00:26:00 | TERRA_M-M | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 9f69fd05-d3cc-3471-87f0-d1a7ad2f912a | -11.632 | -48.4617 | 2024-10-25 00:26:11 | GOES-16 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 4a1bedeb-5e1b-3b0f-b383-4f480ad6271f | -11.883 | -56.4152 | 2024-10-25 00:26:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 0e68b020-690a-3ef3-a379-b6aff72c5581 | -11.8854 | -56.2138 | 2024-10-25 00:26:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| c2e91f6a-2ed2-3bdc-96a2-eb495c3346b3 | -11.902 | -56.4135 | 2024-10-25 00:26:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 143.5 |
| cc535ff3-a813-33f8-a3b3-38ee6dd8d515 | -11.9022 | -56.3934 | 2024-10-25 00:26:13 | GOES-16 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| c97265c5-0418-32ca-982a-4c4da7bc8013 | -12.0444 | -63.1547 | 2024-10-25 00:26:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 0626909b-2c2b-329d-b8c8-22b5a9a5da61 | -12.0445 | -63.1356 | 2024-10-25 00:26:14 | GOES-16 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 8071c3ff-3a6e-3e51-9c02-296dc334e5d5 | -12.3782 | -63.8821 | 2024-10-25 00:26:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 92c5be61-8df1-364b-915e-8f683952ab29 | -12.3971 | -63.8811 | 2024-10-25 00:26:16 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 51.6 |
| d4eb7d73-829b-3826-9d5c-65cfe41b3fae | -12.4589 | -63.1895 | 2024-10-25 00:26:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 82.4 |
| d7299857-2a75-3a72-8ff2-4f00f93fc893 | -12.4591 | -63.1704 | 2024-10-25 00:26:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 113.7 |
| cb307026-337d-3492-b7a8-c63dbc40596b | -12.478 | -63.1693 | 2024-10-25 00:26:16 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 981aeac1-218b-392a-a2a5-7ea27e7cd6c9 | -12.5356 | -63.051 | 2024-10-25 00:26:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 70100ce0-f935-3adc-9c5f-2c22aab41098 | -13.4769 | -61.6217 | 2024-10-25 00:26:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 22b23363-dd62-3b8a-a32d-3949e816d456 | -13.4957 | -61.6398 | 2024-10-25 00:26:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 98539a4d-9010-387e-8387-c300291e883b | -13.4959 | -61.6203 | 2024-10-25 00:26:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 127.2 |
| dff76750-c56b-3c5d-97a9-c62e4d6ff0ff | -15.6836 | -59.734 | 2024-10-25 00:26:34 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 70fc8295-798d-3e22-92bd-b586720b3aec | -16.94 | -57.5268 | 2024-10-25 00:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 86.5 |
| 51031ec9-26ef-346a-84e2-9043dd0bb0ce | -16.9593 | -57.545 | 2024-10-25 00:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 76.8 |
| 7a8f18cc-cb79-349d-b436-baf0f28fd7c9 | -16.9596 | -57.5245 | 2024-10-25 00:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 165.6 |
| 5a368c9f-eedc-3989-b054-54d46cca6e12 | -16.9792 | -57.5223 | 2024-10-25 00:26:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.8 |
| 29406844-ef93-364b-8c2a-1aa85ebd647c | -17.234 | -57.5131 | 2024-10-25 00:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.3 |
| f88a1e20-7468-3acb-bf5f-50e615a6f1ac | -17.2537 | -57.5108 | 2024-10-25 00:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.7 |
| 2f1ada62-cbc7-349d-a92c-9e424b1c6871 | -17.2963 | -57.3008 | 2024-10-25 00:26:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 72.1 |
| d5f8f19b-db0e-33b4-92d6-7c91d2603cbc | -17.7671 | -57.3673 | 2024-10-25 00:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 100.2 |
| 9c84e482-34ae-3514-a18e-0a0d4e46e048 | -17.9023 | -57.5359 | 2024-10-25 00:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.5 |
| 266c326e-377b-3ebc-a1e0-11ef1dd620c8 | -17.9275 | -57.2034 | 2024-10-25 00:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.5 |
| 35b39c27-7cf5-31ff-b078-42a4eecc3546 | -17.9473 | -57.2009 | 2024-10-25 00:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.8 |
| accc9662-95e5-3fd8-93a9-ca7e7929d883 | -18.0254 | -57.253 | 2024-10-25 00:26:46 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.3 |
| da313122-6f4e-37f1-9ac5-ff9dd9c85542 | -18.1219 | -57.3853 | 2024-10-25 00:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 46.7 |
| 49232c0b-ccce-3964-85de-f5a4df77e34c | -18.1223 | -57.3647 | 2024-10-25 00:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.3 |
| 65b2e27a-34f0-37e7-8611-7091b650ffd1 | -18.1417 | -57.3829 | 2024-10-25 00:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.2 |
| acb4647a-978b-36b6-ae33-49b8151436f5 | -18.1421 | -57.3622 | 2024-10-25 00:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 168.9 |
| f7dafd3a-d067-3b3c-97f5-bea166c71d73 | -18.1424 | -57.3415 | 2024-10-25 00:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.3 |
| 023198e4-9d8d-3ee8-b213-b9e6122e5cc7 | -18.1619 | -57.3597 | 2024-10-25 00:26:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.0 |
| f520a042-7d6c-394e-86e6-4441765dbcd4 | -18.3 | -56.2431 | 2024-10-25 00:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 48.6 |
| 94b9b7fb-bd9a-3314-8d99-ee33cc5297ba | -18.3004 | -56.2222 | 2024-10-25 00:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.3 |
| df5ad11e-ba75-38cc-b43c-0ac996a74fef | -18.3008 | -56.2013 | 2024-10-25 00:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.7 |
| 2b9d769b-44d7-3eef-9b13-f4a4738d21bb | -18.3199 | -56.2404 | 2024-10-25 00:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 125.8 |
| 0c88f506-2dd3-3807-8306-925103358644 | -18.3203 | -56.2195 | 2024-10-25 00:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 52.9 |
| 41868d35-6d2e-374c-bb3c-8cde8a749a4c | -18.3398 | -56.2377 | 2024-10-25 00:26:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.0 |
| 762db589-406e-3e16-afde-6e9442204d03 | -19.6256 | -56.7499 | 2024-10-25 00:26:55 | GOES-16 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 65.4 |
| e636cbbd-d909-3c0d-9855-fddfca886272 | -5.69231 | -39.59086 | 2024-10-25 00:28:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 662e82a8-75c3-3cba-8db0-2b24f6af1f39 | -1.97908 | -46.59867 | 2024-10-25 00:28:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 68c97502-283b-34da-8631-91978a4427bf | -1.96119 | -46.6287 | 2024-10-25 00:28:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2c7be5e5-b1d7-3381-83f0-68dab0062963 | -1.34515 | -47.7561 | 2024-10-25 00:28:00 | TERRA_M-M | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2af9c0da-806b-37e5-bf2e-cd7b63e89d13 | -1.15116 | -47.17252 | 2024-10-25 00:28:00 | TERRA_M-M | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e55c342a-5d4c-3dee-9b66-081e17adefbd | -6.0446 | -43.90409 | 2024-10-25 00:28:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2e5c8f2d-45a2-3760-89aa-eecea8c83c63 | -6.29309 | -43.37494 | 2024-10-25 00:28:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 5e2c36b4-d1e3-30e5-a321-17cd64c7d41f | -6.21672 | -43.28272 | 2024-10-25 00:28:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4f39e200-6a16-39fc-918d-4f2e1a1f27e5 | -6.06681 | -43.46416 | 2024-10-25 00:28:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c74efdcc-32ea-367b-af2b-ba6a6bd58904 | -5.71027 | -43.14927 | 2024-10-25 00:28:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 31424f14-372f-3570-8452-e9638b39bcd6 | -5.70113 | -43.15052 | 2024-10-25 00:28:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 25.8 |
| a6206f80-4abb-3fa1-ae2d-ae2fa7178278 | -5.69986 | -43.14109 | 2024-10-25 00:28:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 2b74b12e-d02c-37a8-95c8-e6ead265b40d | -5.69583 | -43.18011 | 2024-10-25 00:28:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 18.3 |
| d8d06d85-9ae8-3d4b-88df-3c61af0d925f | -5.68727 | -43.17803 | 2024-10-25 00:28:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 2e0fd50a-cf5e-3d68-9c0d-cdce3e056886 | -5.67944 | -43.18874 | 2024-10-25 00:28:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 39b2db57-2c47-336e-a75b-63bf87abf282 | -5.59892 | -39.44908 | 2024-10-25 00:28:00 | TERRA_M-M | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 26.2 |
| c8987485-4a9d-3f65-b327-113512b29593 | -5.5975 | -39.43911 | 2024-10-25 00:28:00 | TERRA_M-M | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 2fe5d1b8-bdd1-3aea-b134-d4f0d7f6437f | -5.58957 | -39.45037 | 2024-10-25 00:28:00 | TERRA_M-M | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 098285c8-e978-3100-8491-2e9d4035c172 | -5.45979 | -43.27015 | 2024-10-25 00:28:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 95076d55-5722-3952-add4-3488fe1686f6 | -5.45742 | -43.58168 | 2024-10-25 00:28:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ac29d2ea-d6e4-33f7-b5af-2407285481f4 | -5.44813 | -43.58295 | 2024-10-25 00:28:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 95b25014-3faf-3333-912c-098b11df039c | -5.35126 | -42.9472 | 2024-10-25 00:28:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 9e245693-7649-3218-bde9-9b649bdcac2c | -5.23817 | -41.19514 | 2024-10-25 00:28:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 53a79662-48f8-3044-a375-cec76b4174da | -4.92302 | -41.98112 | 2024-10-25 00:28:00 | TERRA_M-M | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| ee415d9e-ebed-351c-94ae-5fd8223ab785 | -4.92179 | -41.9723 | 2024-10-25 00:28:00 | TERRA_M-M | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| fd4d85e4-96b7-3b82-926d-f68be2cd8838 | -4.79817 | -42.6737 | 2024-10-25 00:28:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8e5dca73-79a6-3c10-91d6-199db89edd82 | -4.56035 | -43.56362 | 2024-10-25 00:28:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5b372e7d-049f-33ca-b1ac-a0881bc11a18 | -4.52329 | -43.48697 | 2024-10-25 00:28:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 28.3 |
| ad31993c-5b16-325f-922d-8ad9604330c2 | -4.47003 | -42.90119 | 2024-10-25 00:28:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| ad81e649-443a-3838-b14c-30be8a261f39 | -4.00278 | -43.25555 | 2024-10-25 00:28:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cc56a36c-bfc8-36f8-8102-28ab6cbac560 | -3.89736 | -41.04246 | 2024-10-25 00:28:00 | TERRA_M-M | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| c42d68aa-9d42-32a0-957d-a4f2f8066bef | -3.06544 | -40.0476 | 2024-10-25 00:28:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 40.8 |
| f1b4b1d5-df84-3994-a555-eb761b697f33 | -3.06403 | -40.03774 | 2024-10-25 00:28:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 46.4 |
| 51c2f923-1933-354d-a633-6e470649f2db | -3.04393 | -40.07708 | 2024-10-25 00:28:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 25.4 |
| 91bc9c65-4155-354c-a495-49524107bace | -3.04256 | -40.06722 | 2024-10-25 00:28:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 24.6 |
| 6d29afd0-dcad-3425-bfd1-3022f4cb1420 | -3.03462 | -40.0784 | 2024-10-25 00:28:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 8e4a3ec3-9559-3595-85bf-a9d1401b1e31 | -6.64273 | -47.8728 | 2024-10-25 00:28:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| c8689a1c-484d-30b9-bb79-3a756a644fb6 | -6.64015 | -47.85276 | 2024-10-25 00:28:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 31.4 |
| b678e282-383e-3e9a-b3a5-b5937b9b9fbf | -6.46667 | -44.6765 | 2024-10-25 00:28:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 663955d1-d35b-3770-8b7c-2cb6eb28c546 | -6.46515 | -44.66493 | 2024-10-25 00:28:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 9ccb9ffa-0653-3a02-9578-25a7993f7328 | -6.45665 | -44.67799 | 2024-10-25 00:28:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| f7969971-bb05-3176-8a97-9a1374004c8e | -6.45344 | -44.42441 | 2024-10-25 00:28:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| db751b24-a1ae-3914-948c-496a4a3282ae | -6.00325 | -45.95886 | 2024-10-25 00:28:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 78f8815a-5af8-3999-bde0-8781ec17da75 | -5.98565 | -45.37131 | 2024-10-25 00:28:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 37.2 |
| a2dce4a8-20e8-3897-98c3-d5c94501b989 | -5.98014 | -45.37848 | 2024-10-25 00:28:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 47000117-d0b5-3fe4-8f40-e9193620159d | -5.97841 | -45.36581 | 2024-10-25 00:28:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 150.3 |
| e51d4a5b-f149-3b0d-8526-d6c201b82bee | -5.89181 | -44.65817 | 2024-10-25 00:28:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ed01b57f-e1b2-3337-b8d4-0285f2a04d15 | -5.89176 | -44.65181 | 2024-10-25 00:28:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 7f6c4f75-19d4-3877-bc72-1f1008da33fa | -5.89029 | -44.64059 | 2024-10-25 00:28:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| b68b9f2e-9e3f-3115-9551-059757f664b4 | -5.89027 | -44.64697 | 2024-10-25 00:28:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 37.7 |
| e6d1fe89-94a7-3da9-ab60-c9be256a96b2 | -5.84816 | -47.29717 | 2024-10-25 00:28:00 | TERRA_M-M | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |


[Clique aqui para ver as próximas entradas](README6.md)
