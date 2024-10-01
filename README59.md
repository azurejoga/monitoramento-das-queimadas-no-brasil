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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aea25e87-9fa6-31f2-b64d-b1ae4c8f52c1 | -23.07035 | -45.39219 | 2024-10-01 03:51:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 9eee45d6-b915-32b2-9093-3e7f52e9dd63 | -23.0697 | -45.39623 | 2024-10-01 03:51:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| cea8330d-0bb3-36bf-bef6-fe9a6b0bcdde | -23.06931 | -45.39761 | 2024-10-01 03:51:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 131f1285-9d4c-366a-8c46-e91a4754054b | -23.06823 | -45.40326 | 2024-10-01 03:51:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| b5ba2d6b-1625-37ce-a0aa-55bb87b88d46 | -23.06762 | -45.40754 | 2024-10-01 03:51:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| a8f84918-f1a4-3e4d-be4c-4d5412c1a4d9 | -23.06715 | -45.40888 | 2024-10-01 03:51:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| ad27b272-3e5e-346e-b276-e1d161f37486 | -23.06579 | -45.39563 | 2024-10-01 03:51:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 1f230a72-0fef-348e-9e59-71186b9224b4 | -23.0654 | -45.39701 | 2024-10-01 03:51:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1a1ade59-c466-315d-a12d-5355cd924f0c | -23.06474 | -45.40135 | 2024-10-01 03:51:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| c780ed5b-da67-3be2-975f-83b43cc2eec2 | -23.0643 | -45.40273 | 2024-10-01 03:51:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6c72b283-c08d-3486-a1ac-458f66c7b8cb | -23.0637 | -45.40698 | 2024-10-01 03:51:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| c95b91af-9878-37e3-9653-5b7874813ceb | -23.06367 | -45.70433 | 2024-10-01 03:51:00 | NPP-375D | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| fb090176-b36c-3c38-ac1e-af4337de9895 | -23.06323 | -45.40829 | 2024-10-01 03:51:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c248921a-8c20-3388-ac6f-944bf65e65cc | -22.95981 | -45.96433 | 2024-10-01 03:51:00 | NPP-375D | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 95c78d4e-7f69-3452-bf3c-ec529095a9c4 | -22.95945 | -45.96522 | 2024-10-01 03:51:00 | NPP-375D | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 13d20f12-5056-393e-a990-d4ad3c84be38 | -22.91582 | -45.37851 | 2024-10-01 03:51:00 | NPP-375D | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 667ecd39-9e1c-3917-aae3-f37e6ef30305 | -22.87545 | -45.18443 | 2024-10-01 03:51:00 | NPP-375D | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 05bc1b41-d4fa-3055-9617-8751164e1b6d | -16.45148 | -53.93516 | 2024-10-01 03:51:00 | NPP-375D | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 343e2d1d-8e48-3db8-b8d8-a717812c635e | -28.58545 | -49.44108 | 2024-10-01 03:53:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 466475b8-ba00-3b71-a9ab-fc7eeffe744c | -26.41368 | -53.23012 | 2024-10-01 03:53:00 | NPP-375D | CAMPO ERÊ | SANTA CATARINA | Brasil | 4203501 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e1c30523-8ccf-30ca-b8fa-9343cd0fe0af | -26.41339 | -53.22683 | 2024-10-01 03:53:00 | NPP-375D | CAMPO ERÊ | SANTA CATARINA | Brasil | 4203501 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c172d650-ba8e-3ac8-af5d-9809d315c9c9 | -26.41232 | -53.23116 | 2024-10-01 03:53:00 | NPP-375D | CAMPO ERÊ | SANTA CATARINA | Brasil | 4203501 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5434f36a-a115-3c6c-9d02-373c0d48dbf8 | -26.21933 | -52.37061 | 2024-10-01 03:53:00 | NPP-375D | HONÓRIO SERPA | PARANÁ | Brasil | 4109658 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8b657aca-83d8-3696-aa51-c75316d5a165 | -26.2184 | -52.37453 | 2024-10-01 03:53:00 | NPP-375D | HONÓRIO SERPA | PARANÁ | Brasil | 4109658 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2a70af59-d219-312b-b4bb-ca610f775a46 | -26.21393 | -52.36879 | 2024-10-01 03:53:00 | NPP-375D | HONÓRIO SERPA | PARANÁ | Brasil | 4109658 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 2092399f-647d-397e-92d5-24e3c3df0836 | -2.4048 | -50.3085 | 2024-10-01 03:55:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 4bee82bd-19e4-38d7-9bc3-b052c0b67307 | -2.4047 | -50.3295 | 2024-10-01 03:55:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 324.1 |
| 9203f90c-39b7-3b58-8a65-caeb64df1f6c | -2.4046 | -50.3505 | 2024-10-01 03:55:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 105.2 |
| bafc0125-6de4-3c75-be18-5d322aaf4542 | -2.3863 | -50.3299 | 2024-10-01 03:55:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| cbd83827-4c28-359c-84e5-ad6e707daf13 | -5.9788 | -45.3621 | 2024-10-01 03:55:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| a0301eb7-84ba-3bc3-9a81-975486bc1264 | -5.9786 | -45.3847 | 2024-10-01 03:55:40 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 947ee3f4-96ac-382b-9ced-16c63dd32a81 | -6.545 | -43.0373 | 2024-10-01 03:55:43 | GOES-16 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 8b0d4e4e-1281-3f8a-8a62-cd420af27bc4 | -6.9671 | -47.6215 | 2024-10-01 03:55:45 | GOES-16 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 3d0d3398-f264-3148-a450-d2c1eb4f6e06 | -12.1406 | -50.0524 | 2024-10-01 03:56:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 216de256-eaf8-31d3-93cf-a39c628e32cf | -12.1402 | -50.074 | 2024-10-01 03:56:14 | GOES-16 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| f804b57e-b21a-3193-96c6-e78bf333f54d | -12.8397 | -62.8607 | 2024-10-01 03:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 25dee8d1-df2c-3c9c-aee2-6465ce6d7a86 | -12.9601 | -51.3664 | 2024-10-01 03:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 7aa856f3-59e0-31fa-ab51-b28fe8c88ff6 | -12.9591 | -51.4303 | 2024-10-01 03:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| b46117ca-17ad-3db3-b31a-e266ec9440eb | -12.8206 | -62.881 | 2024-10-01 03:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 66dbaef8-e4d1-39a3-8756-c01fd384fa90 | -12.94 | -51.4327 | 2024-10-01 03:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 109.2 |
| f25335af-fd98-3bb6-9196-837903208554 | -12.9396 | -51.454 | 2024-10-01 03:56:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 6e11b28f-6f40-39d0-96ba-cd1d32806f88 | -12.7827 | -62.8832 | 2024-10-01 03:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 7d8918ad-dd5a-3859-b537-88e66d3a5c70 | -12.7826 | -62.9025 | 2024-10-01 03:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 5e39afaa-c918-30c6-bc05-e8e87b5bbbe0 | -12.7636 | -62.9036 | 2024-10-01 03:56:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 9fbdb6c4-448e-374f-a221-97db217cc45e | -13.2308 | -51.2048 | 2024-10-01 03:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 125.3 |
| 1cb5f901-f853-390b-9557-eb78da0e81d7 | -13.2304 | -51.2262 | 2024-10-01 03:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 41b23f5e-38a1-37c3-8d07-440dafbe1f0e | -13.2116 | -51.2073 | 2024-10-01 03:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 2b3a03b6-a5a4-3b80-bff2-b8e586a37a01 | -13.2112 | -51.2287 | 2024-10-01 03:56:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| c23278c8-3bfe-3b80-a328-f5eb31a47b28 | -12.9169 | -62.6829 | 2024-10-01 03:56:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 316a1377-5ab1-3dbd-a33b-c88224d23c44 | -13.5066 | -48.5825 | 2024-10-01 03:56:22 | GOES-16 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 60c0a728-6897-37ec-adcf-f54cec6bc100 | -13.5961 | -51.1582 | 2024-10-01 03:56:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 4d7d7e0f-65c4-38f7-aa44-760026309eea | -13.6357 | -51.0888 | 2024-10-01 03:56:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 222.1 |
| f4d2781c-4e49-3266-b942-a2d1e7713cb2 | -13.6353 | -51.1103 | 2024-10-01 03:56:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 264.1 |
| d4f7f932-c9b2-3e11-ad36-4c8ff3db16ea | -13.6342 | -51.1746 | 2024-10-01 03:56:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 07359b27-80fc-399b-9c19-8d3998316948 | -13.6168 | -51.0698 | 2024-10-01 03:56:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 5f2717ef-f05b-3778-8fed-2369b0b50a43 | -13.6164 | -51.0913 | 2024-10-01 03:56:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 323.0 |
| 63767d90-7a74-3ea5-a4e2-94257c5a294c | -13.6161 | -51.1128 | 2024-10-01 03:56:23 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 250.7 |
| e6cdaaa9-a037-366d-b85e-3403f27fb09b | -14.7402 | -48.7721 | 2024-10-01 03:56:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 0bf96ade-3740-319c-960f-b31201fb0588 | -14.7406 | -48.7498 | 2024-10-01 03:56:28 | GOES-16 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 70.4 |
| a1471989-109e-3066-8852-3aea1fed6347 | -15.9127 | -57.1733 | 2024-10-01 03:56:36 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 40.5 |
| effb9f14-ca63-3c0b-a5d9-5b4905d74c94 | -16.5131 | -57.3509 | 2024-10-01 03:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 44.5 |
| db509384-e99e-3a03-bda4-cf2578934165 | -16.4939 | -57.3327 | 2024-10-01 03:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.4 |
| 6e9594eb-4d6c-31bf-8094-40ce2dddb648 | -16.4935 | -57.3531 | 2024-10-01 03:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.7 |
| 33c2547c-2495-31db-8b3a-7025ea75ec7c | -16.4743 | -57.3349 | 2024-10-01 03:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 56.1 |
| bde5ab1a-e84c-3083-b61f-53de97231ad7 | -16.474 | -57.3553 | 2024-10-01 03:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 61.6 |
| c9b36f1d-d42b-31f2-962e-4b7f21bfa6a9 | -16.6459 | -55.1908 | 2024-10-01 03:56:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 46.7 |
| 1d52b347-531a-363f-bd97-e6149fb13a4f | -16.6263 | -55.1934 | 2024-10-01 03:56:39 | GOES-16 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 43.2 |
| f9159e32-9c19-3a16-b0d5-95fc72a0d3bc | -16.5134 | -57.3305 | 2024-10-01 03:56:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 43.9 |
| d7a68e3a-b497-3f44-bce6-714ddd88cabe | -16.6704 | -57.2717 | 2024-10-01 03:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 61.2 |
| d4af2a67-673e-3dc4-a392-b1b9c4b4fadc | -16.6701 | -57.2922 | 2024-10-01 03:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.4 |
| 2a48dd73-17d4-373c-bb9f-9cfc24a8392a | -16.6508 | -57.2739 | 2024-10-01 03:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 77.2 |
| 6dd8adb5-970f-3394-9fc7-befe3aa14855 | -16.6505 | -57.2944 | 2024-10-01 03:56:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.4 |
| 50f99300-b35e-3a0b-a37b-eaf65def19ea | -16.8983 | -57.6949 | 2024-10-01 03:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.6 |
| e77289da-2c1c-3b23-b2c3-1f0237e78ec3 | -18.6973 | -57.333 | 2024-10-01 03:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 150.7 |
| 251bb651-a29f-3576-a203-8b0021176a84 | -18.7176 | -57.3097 | 2024-10-01 03:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 155.6 |
| 9bf53018-2739-36f3-9e03-53c4f9b4cb3d | -18.7172 | -57.3305 | 2024-10-01 03:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 129.7 |
| e44f2e7c-8dfe-38e8-857e-13505d878688 | -18.6977 | -57.3123 | 2024-10-01 03:56:51 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 134.9 |
| a28f95d4-f462-34cf-8638-856bccaf0457 | -20.0082 | -44.5336 | 2024-10-01 03:56:56 | GOES-16 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 61.6 |
| 10218500-6263-349d-a50a-a7661b4e462f | -22.3916 | -49.3194 | 2024-10-01 03:57:09 | GOES-16 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.8 |
| bcf650cd-7a3f-3aa4-afa9-5ea050c47b07 | -22.3713 | -49.3011 | 2024-10-01 03:57:09 | GOES-16 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 145.6 |
| 8042efde-adb7-3a6e-997d-7626a373cd32 | -22.3707 | -49.3244 | 2024-10-01 03:57:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 361.7 |
| 7f7220cf-38a8-3c35-9941-640a67adbeed | -22.37 | -49.3477 | 2024-10-01 03:57:09 | GOES-16 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 153.5 |
| 482a6129-2e4b-3449-b63d-adb8090d119c | -22.37 | -49.34 | 2024-10-01 04:03:16 | MSG-03 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 23c89fc2-102d-3db6-ae96-3da4adf21596 | -21.56 | -47.83 | 2024-10-01 04:03:22 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 1818328c-f1c6-3cd5-93dc-4f3356bae967 | -21.59 | -47.9 | 2024-10-01 04:03:22 | MSG-03 | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 49388773-219c-376b-afe5-2cb9c9998e35 | -21.59 | -47.84 | 2024-10-01 04:03:22 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 718c68f4-3dbe-3674-bdd5-57133791dde6 | -21.59 | -47.79 | 2024-10-01 04:03:22 | MSG-03 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| cb5b3c4e-d32d-353b-b235-73aa6e7fbdd7 | -12.98 | -51.32 | 2024-10-01 04:04:12 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9b47a6c1-cc6b-3211-b5e4-ca5ef5915b16 | -12.98 | -51.26 | 2024-10-01 04:04:12 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e181da3a-59f1-3261-9d65-c7df48a409ea | -12.98 | -51.2 | 2024-10-01 04:04:12 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9e209f0c-81b3-3683-84ca-6775037ba454 | -13.01 | -51.33 | 2024-10-01 04:04:12 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6082b6e6-90a1-3c66-b13f-394b48bf9324 | -13.01 | -51.27 | 2024-10-01 04:04:12 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b2f1274b-cb0e-380f-a1a0-ae09e688ece7 | -13.01 | -51.21 | 2024-10-01 04:04:12 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 78aa64d1-d02d-3133-82cf-5cdb02fc226d | -13.04 | -51.28 | 2024-10-01 04:04:12 | MSG-03 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 275379d0-729a-30ca-b374-93b6b1117b4c | -2.88 | -50.78 | 2024-10-01 04:05:12 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84364cc1-2e44-3639-aaf6-5d8a77066842 | -2.88 | -50.73 | 2024-10-01 04:05:12 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07dd9d1c-8e5f-3b28-a470-cb7869c4326b | -2.91 | -50.73 | 2024-10-01 04:05:12 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 416e2c54-1615-3cd1-bb2e-51e91842e4d6 | -2.4048 | -50.3085 | 2024-10-01 04:05:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 2daedd02-1679-3098-8111-d2ed345089c7 | -2.4047 | -50.3295 | 2024-10-01 04:05:19 | GOES-16 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 226.7 |
| 67d252a4-fc82-338e-8266-3186c0bcc889 | -2.4046 | -50.3505 | 2024-10-01 04:05:19 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |


[Clique aqui para ver as próximas entradas](README60.md)
