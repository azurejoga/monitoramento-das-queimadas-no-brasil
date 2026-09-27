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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1133f492-7573-396f-99f4-c5a3527a8610 | -8.6006 | -54.651001 | 2026-09-27 01:15:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 241511cc-a273-3d11-aa6a-af312fed5211 | -12.2979 | -50.392399 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e31b2cc0-6bfb-315b-b11e-b68f6cbe03ef | -12.6908 | -47.3148 | 2026-09-27 01:15:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3d3fecf8-f5c5-32a0-acf1-e87045ea78a8 | -20.8389 | -57.722801 | 2026-09-27 01:15:00 | METOP-C | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a5d5a40b-469f-3f48-a3a0-ab1e3d52c9b7 | -10.6741 | -57.636799 | 2026-09-27 01:15:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 79d2669c-0a3a-32c9-810b-d0a1b7fb0a11 | -2.0711 | -56.870899 | 2026-09-27 01:15:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6ff0fe90-b6cc-38ba-906b-f97f68a5e461 | -10.823 | -60.735901 | 2026-09-27 01:15:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d7388682-0178-36dc-9d70-64361c48f994 | -3.2965 | -54.695099 | 2026-09-27 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41dcce61-c5b9-3ce8-80ce-6eb460cef614 | -3.3063 | -54.692799 | 2026-09-27 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1a5c1f3-9f9d-36c8-a593-cfa994cb8c03 | -11.8962 | -50.522999 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4940d1e2-324c-3f81-9ae8-9e3847ee5ba0 | -12.2624 | -50.704102 | 2026-09-27 01:15:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 59ee2a8d-7c98-3122-9f0d-0c0cf1abbbfc | -12.2106 | -50.3745 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 63312f70-2b39-3b05-bbf1-837c3537b31d | -3.9704 | -59.339802 | 2026-09-27 01:15:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2c6941ad-7bf6-3341-9832-80c4eff4ec99 | 0.2042 | -51.325001 | 2026-09-27 01:15:00 | METOP-C | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 7df5014b-4f62-35e1-8fc4-23ac5f0cbd3b | -12.6812 | -47.317402 | 2026-09-27 01:15:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c02aa01b-377b-3a6a-acfb-b5a8a896cb94 | -2.7973 | -57.6917 | 2026-09-27 01:15:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7458c3b9-29ac-302e-94b9-e2866788cdc4 | -11.9702 | -50.570499 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| eed919fd-bc76-3d3b-93a5-65dfc064efb3 | -2.7859 | -57.686901 | 2026-09-27 01:15:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 14167581-f781-3de7-923f-00b7af6bb006 | -6.056 | -57.820702 | 2026-09-27 01:15:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8930dcc3-d570-3204-83fb-db34aa1467d6 | -11.9511 | -50.5355 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2b3d2262-4751-33ef-8d1d-a99caf00950b | -11.9254 | -50.5154 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4a3b01ef-b9ff-3163-a70c-8730da79856f | -4.5109 | -54.9482 | 2026-09-27 01:15:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07d66852-b133-33f5-92c3-7bed7f806880 | -11.2783 | -54.4408 | 2026-09-27 01:15:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f0487d77-9e94-3c27-894a-d9ff062ea982 | -11.8056 | -50.532902 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5901cbf9-5d7d-3b4b-a5d4-c79da5f19d02 | -3.9606 | -59.341999 | 2026-09-27 01:15:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ae483949-5925-344a-97e1-f332bcc2d16e | -6.0951 | -57.631401 | 2026-09-27 01:15:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c91398c6-c2c9-3c69-b2c3-fffad11b7c72 | -11.9831 | -50.580399 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 93780ac7-9611-34c3-9438-a3a4ff3652a3 | -11.0526 | -54.185902 | 2026-09-27 01:15:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bae82456-bdae-3d60-85e8-6828c22bc28c | -10.8094 | -60.7202 | 2026-09-27 01:15:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d3a4d31a-5971-3783-a6d1-e447488ecaf6 | -7.4999 | -55.019199 | 2026-09-27 01:15:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a84fea65-01bd-3f95-abf9-dd61be2816e2 | 2.6391 | -60.156399 | 2026-09-27 01:15:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2740ab73-edf7-3ad2-8425-f4cb6edc43d9 | -15.9889 | -54.930302 | 2026-09-27 01:15:00 | METOP-C | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d7840ebc-5cec-35ba-8135-6575d504d07e | 2.8853 | -60.297298 | 2026-09-27 01:15:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 35996e08-2117-30db-84af-4a9508e423f2 | -12.6663 | -47.300098 | 2026-09-27 01:15:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 14f0769e-a585-3dc1-83ce-589a54acf7f2 | -2.6647 | -56.450699 | 2026-09-27 01:15:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ff200411-8914-3d4c-bd19-942db99e2acc | -7.6953 | -54.753101 | 2026-09-27 01:15:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb4b5d6a-822f-3561-bb89-edd93d13f49f | -9.9273 | -60.7188 | 2026-09-27 01:15:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1ab02b9c-2ce0-3c29-9b6f-2dabe0230e6b | -4.5462 | -54.967201 | 2026-09-27 01:15:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9835e7e8-4092-3799-87dd-e118fbf5d7fd | -3.972 | -59.346699 | 2026-09-27 01:15:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0622b487-6f9a-33ee-af80-62bb91c09d84 | -11.7723 | -51.019699 | 2026-09-27 01:15:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 39988352-128f-3c15-941b-a844b4a4b623 | -4.2585 | -51.038799 | 2026-09-27 01:15:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6196a913-2add-3a5b-93e1-dc78bbcbf635 | -2.9323 | -56.5816 | 2026-09-27 01:15:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d60cf29-5175-3dc3-8160-6928c93c182e | -10.4209 | -53.789398 | 2026-09-27 01:15:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1b300ad8-9d8b-3790-abf7-1f978ccd4175 | -12.6836 | -47.3217 | 2026-09-27 01:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 7631edef-d381-36a6-9af0-e830dbc45532 | -8.0373 | -54.8926 | 2026-09-27 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.2 |
| dfdad9e6-5ff1-3068-aa71-deaa7d0c80fd | -12.684 | -47.2992 | 2026-09-27 01:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 351907db-d0f8-3ace-86af-8851e727b9c4 | -10.201 | -36.2386 | 2026-09-27 01:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 64.4 |
| cca3f7ea-5ea6-38ee-a6f3-787e0e7c4af3 | -3.9228 | -43.0123 | 2026-09-27 01:20:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| f0c61b47-03c5-32cf-8c57-6f076294a873 | -14.13 | -46.326 | 2026-09-27 01:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 6b3620e2-d2a1-3e06-b05d-edfe56845f35 | -2.008 | -47.0181 | 2026-09-27 01:20:00 | GOES-19 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 25293647-07ac-35c6-a257-e409aca7149e | -10.824 | -60.7246 | 2026-09-27 01:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 1bd7019c-50fb-301f-89d9-34640d863304 | -12.6643 | -47.3245 | 2026-09-27 01:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 4411bf31-6e5f-351e-800d-fdc4dfbd94d5 | -12.6647 | -47.302 | 2026-09-27 01:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 9fd06c7e-d86f-3d43-a543-1bd1e0ed6454 | 2.6359 | -60.1648 | 2026-09-27 01:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 6d1831bf-fb18-3b8a-8f12-cf42da3f5e47 | -12.289 | -50.3143 | 2026-09-27 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 42427c89-f98f-3852-a8a5-24e33cb2dda1 | -10.8052 | -60.7257 | 2026-09-27 01:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 6c2f2cdb-d979-39b7-abaa-840523ad3df8 | -12.3082 | -50.3119 | 2026-09-27 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 20fb0b05-bd82-3bdb-bfde-cbb3229135f3 | -14.1105 | -46.3293 | 2026-09-27 01:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 3c1898d3-2304-37b7-853e-29479809f1fb | -12.288 | -50.3789 | 2026-09-27 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| af5afbce-179d-3a26-a59b-e2fc1c0afdbf | -12.289 | -50.3143 | 2026-09-27 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 157.0 |
| ffd7ac23-ad68-3bbd-8401-eb861636d638 | -2.008 | -47.0181 | 2026-09-27 01:30:00 | GOES-19 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 8cc5a9fc-ec81-3643-b044-8b3fa7222580 | -12.6836 | -47.3217 | 2026-09-27 01:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 6ec75f9f-937e-31ad-931b-f32bb994565c | -12.0365 | -50.6233 | 2026-09-27 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 7d2a2bf4-690b-3a88-b9f9-325716ee5c03 | -10.824 | -60.7246 | 2026-09-27 01:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 43ed44c5-1a03-3eac-8d2a-5cc745d3b61f | -12.3082 | -50.3119 | 2026-09-27 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 6a58345e-ea7d-3e4e-8f12-696d1846411d | 2.6359 | -60.1648 | 2026-09-27 01:30:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 287d62a8-77c6-339d-bcdd-5e7b5016f6ff | -12.0559 | -50.5996 | 2026-09-27 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 145.1 |
| 7306a35d-b190-3b7b-b6bc-58bb2f8748d7 | -12.288 | -50.3789 | 2026-09-27 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 80de5431-997f-3baf-b7cf-c2a54b3febe7 | -8.0373 | -54.8926 | 2026-09-27 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 6963a481-aab8-3c9c-869d-61fa7686e190 | -10.8052 | -60.7257 | 2026-09-27 01:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| b106d2fb-f061-3a4a-9eb3-c530576572d6 | -11.8665 | -50.5362 | 2026-09-27 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 2c75bf59-d1b6-3c80-b66a-0de2fa52cda9 | -12.0556 | -50.6211 | 2026-09-27 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 62a65a88-270a-30e5-8621-e892a693e7d8 | -12.0369 | -50.6019 | 2026-09-27 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 208.6 |
| ca5a0f48-85f5-3469-901b-bb6aec71c925 | -12.0369 | -50.6019 | 2026-09-27 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 215.6 |
| 1fde5b35-d5d3-3336-a7df-0cbffb63bbff | 2.6359 | -60.1648 | 2026-09-27 01:40:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 04b7eb95-035d-305c-ace6-6e92fa509863 | -12.3085 | -50.2904 | 2026-09-27 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| dad9d5a2-a891-3f5d-a3c0-ae851800d5e0 | -12.289 | -50.3143 | 2026-09-27 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 159.6 |
| 252783f3-e256-3c81-816a-1b44716f7155 | -12.0365 | -50.6233 | 2026-09-27 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| ad9d5fcf-a7a4-3cdc-a018-c23bb8f6faa2 | -12.0559 | -50.5996 | 2026-09-27 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 161.0 |
| 92224943-c1a7-3c84-a249-471d552eb019 | -12.2894 | -50.2927 | 2026-09-27 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 0914b474-859f-3d17-9f0b-c5b254824575 | -8.0373 | -54.8926 | 2026-09-27 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 02751b87-c3d4-356d-a806-5cc3f28b65e2 | -3.9228 | -43.0123 | 2026-09-27 01:40:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| c78de6e0-d59a-32ca-a115-78f2fe660946 | -12.1185 | -50.2489 | 2026-09-27 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.3 |
| c697983e-2a34-3b98-bdaa-e9e0481e663a | -12.3082 | -50.3119 | 2026-09-27 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 163.7 |
| c864353b-9bad-30b6-a28d-9e2c1a79dc96 | -12.2894 | -50.2927 | 2026-09-27 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 62aa729f-46e1-397b-8536-f021eb156658 | -12.0369 | -50.6019 | 2026-09-27 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 203.3 |
| ac5691a4-672d-33cd-aefb-ecd0d3113c80 | -12.2699 | -50.3166 | 2026-09-27 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 18be85a9-4267-3ec9-8049-d8f2bfab4076 | -12.3085 | -50.2904 | 2026-09-27 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.5 |
| a9cf2f23-d55d-3cca-a820-74ddf02c1dd5 | -12.0365 | -50.6233 | 2026-09-27 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 69616525-4a93-313b-81c9-129db1133dcb | -12.0559 | -50.5996 | 2026-09-27 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 207.1 |
| 699c0eb9-6d15-3571-8ed5-bc2e5e3752c2 | 2.6359 | -60.1648 | 2026-09-27 01:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 60.4 |
| e25e2a94-259c-3e55-b2fb-3bf52e1fcfd4 | -12.3082 | -50.3119 | 2026-09-27 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 284.9 |
| 3f57acf9-d4f7-3bd9-a2e2-5cff92319272 | -12.288 | -50.3789 | 2026-09-27 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 6131d76e-6713-3156-9e09-334f1c622c60 | -8.0373 | -54.8926 | 2026-09-27 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 7f2bd96a-a78e-3faa-bd31-c25d37c421b4 | -12.0556 | -50.6211 | 2026-09-27 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 050eab41-bb94-3cd6-ae37-fb1b0895399b | -12.289 | -50.3143 | 2026-09-27 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 276.9 |
| 7320973d-241c-3f04-a1c6-93a25200911a | -12.0372 | -50.5804 | 2026-09-27 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| e3e21b4b-d4b3-3dda-b05a-455545b3d16a | -12.0178 | -50.6041 | 2026-09-27 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| e12cc765-565c-306a-858f-58c2d7da1de4 | 2.6359 | -60.1648 | 2026-09-27 02:00:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 3dca32cf-d2cd-3401-abf8-e9ff53f70784 | -12.0369 | -50.6019 | 2026-09-27 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 268.7 |


[Clique aqui para ver as próximas entradas](README8.md)
