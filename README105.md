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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ff34ab7-6bbf-3964-89fa-3208abf86a9b | -11.6273 | -46.4126 | 2025-08-26 13:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 219.0 |
| 69573dc7-1d64-338d-962e-3d9701c26d6c | -11.54 | -52.119 | 2025-08-26 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| d797d445-8f6f-3afc-a9ee-71077d45821e | -12.6737 | -47.8812 | 2025-08-26 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.2 |
| db04ca99-8092-30d0-9d6c-29ce70f2dd4a | -11.6086 | -46.3926 | 2025-08-26 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 162.4 |
| d92c503b-d5e8-3b91-99dd-c08f8c9a51d0 | -11.502 | -52.1229 | 2025-08-26 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 5968aa62-01c4-3cd0-80a7-8d467656d905 | -9.1375 | -45.2493 | 2025-08-26 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 192.3 |
| 3e9b8078-9e94-3e92-a5fa-c8b6a6b0b54f | -6.2459 | -60.0174 | 2025-08-26 13:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 327.0 |
| b6a9aa21-4564-3b52-91a1-a31f4fa2f6d1 | -12.9327 | -46.3134 | 2025-08-26 13:30:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 42002bea-67f9-3d4a-a09b-0d4bf3692182 | -12.8123 | -49.8599 | 2025-08-26 13:30:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 169.0 |
| 2fc04daf-2ac0-37bb-a22f-175412c7608a | -11.6304 | -46.2311 | 2025-08-26 13:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 97.4 |
| de0ddcbb-e93e-3944-8f87-a43986575f9b | -6.8413 | -58.9552 | 2025-08-26 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 2374e99f-7962-3f73-abcf-b11aee3f4453 | -11.559 | -52.117 | 2025-08-26 13:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 94.8 |
| b8f9c27f-946c-3432-9ff0-9e89496d6589 | -6.8229 | -58.956 | 2025-08-26 13:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 163.8 |
| 31f12737-51a0-374b-9dca-6085942754ef | -6.8062 | -45.0019 | 2025-08-26 13:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 124.2 |
| e9a2e3c1-0003-3e77-9847-4bc8f8be100e | -10.7787 | -47.0624 | 2025-08-26 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| d2dc2e95-9652-3208-8343-28d5a873d874 | -10.6818 | -47.1858 | 2025-08-26 13:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 5e15b56f-3b17-37f3-bf04-b1c1428dddb9 | -11.6082 | -46.4152 | 2025-08-26 13:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 0ebe212b-550b-320b-bcc7-0237b1f9622b | -12.7932 | -49.8624 | 2025-08-26 13:30:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 285.8 |
| 6f672c0b-9587-39be-9ffb-a74cc4a69e21 | -8.9874 | -65.4192 | 2025-08-26 13:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 086c51e2-f7a1-3de8-81f0-a34b739c4941 | -6.6201 | -44.8581 | 2025-08-26 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| f028fffc-7844-3158-856c-eff51a7870de | -6.8062 | -45.0019 | 2025-08-26 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| b5506bb5-1db4-33c3-9fed-529ffb583bd1 | -7.586 | -47.4835 | 2025-08-26 13:40:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 1d5cd710-9b48-3180-afbc-aa045015ee47 | -12.6741 | -47.8589 | 2025-08-26 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 100.1 |
| a5469be1-6a20-3d05-adf5-c88652079453 | -11.6273 | -46.4126 | 2025-08-26 13:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 177.2 |
| 51cde86c-9074-3c8b-b0a3-582f2092549d | -10.6818 | -47.1858 | 2025-08-26 13:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| a53090a3-0a58-3430-8f6f-66f5d656b944 | -6.8229 | -58.956 | 2025-08-26 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 241.7 |
| f4227929-d3fd-3ea9-bd7b-d3d14554bb9e | -11.502 | -52.1229 | 2025-08-26 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 4fffd852-9791-372e-8f86-685c5b65a11a | -6.8228 | -58.9753 | 2025-08-26 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 212.8 |
| e982dbee-807b-396b-907a-7a9a6c4f039e | -9.1375 | -45.2493 | 2025-08-26 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 727f6c60-495c-3a27-b008-30ab49455bf6 | -6.7819 | -59.6711 | 2025-08-26 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 35d60d6a-3008-3836-b43b-6c8187fde8c0 | -11.54 | -52.119 | 2025-08-26 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 75.1 |
| be9d214e-50e1-373b-a26c-c986f60c96ad | -6.2458 | -60.0365 | 2025-08-26 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| e1028c57-10de-353a-a177-997639cc456f | -11.5779 | -52.115 | 2025-08-26 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 1f4c1ecb-ca18-3cd4-b869-2227a18e92db | -11.559 | -52.117 | 2025-08-26 13:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 252a3a0a-d141-34cb-9382-87cd7e81e69c | -11.6089 | -46.3699 | 2025-08-26 13:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| aa47254d-8cba-3920-8210-ebb73dca4d0d | -12.8123 | -49.8599 | 2025-08-26 13:40:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 208.7 |
| a5b2a169-2d4d-352f-a99f-ec7c07ac8fa6 | -6.246 | -59.9982 | 2025-08-26 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 6aa184e1-7f7d-35f1-aafb-1e2bbc8e8768 | -16.6224 | -49.3708 | 2025-08-26 13:40:00 | GOES-19 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 130.9 |
| e74b4fb8-6c38-3e90-ab73-bdde1b781045 | -6.2275 | -60.018 | 2025-08-26 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 0cc72686-7056-3c36-8333-a44b009ea62f | -9.7916 | -64.2461 | 2025-08-26 13:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 83.8 |
| dc5e3e7d-7160-3bea-94db-9d7883f77402 | -6.7635 | -59.6718 | 2025-08-26 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 610689bd-72d8-3f55-b7c9-690f4b4c9ce0 | -12.4933 | -47.2369 | 2025-08-26 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 4362fd76-980f-300c-bad2-1d64d96d03ce | -11.6082 | -46.4152 | 2025-08-26 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 123.1 |
| a578f267-67b0-314c-982e-b67893caa71a | -6.2459 | -60.0174 | 2025-08-26 13:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 276.6 |
| c7c73f9e-3bb1-3e49-87be-096684d8c38d | -6.8413 | -58.9552 | 2025-08-26 13:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 1dabead1-d937-3ba7-9f77-fb216385bee9 | -13.4397 | -47.006 | 2025-08-26 13:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 90d56086-ade9-34fb-a107-f99c71ca84fa | -12.6737 | -47.8812 | 2025-08-26 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| b45b2def-e65a-3b1b-8355-f1310ff335a3 | -11.6112 | -46.2337 | 2025-08-26 13:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| b5bbff2a-d2f5-37a0-b063-0437f62c417f | -12.7932 | -49.8624 | 2025-08-26 13:40:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 317.5 |
| 2ba777e3-ac56-38bb-9490-36af6bdf3557 | -11.2014 | -50.5685 | 2025-08-26 13:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 70de2c09-f8ee-3da0-9034-f7b9d89ecda2 | -7.5673 | -47.4851 | 2025-08-26 13:40:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| a96af3d5-6f04-3ded-924a-2bd6898ece4b | -6.5293 | -44.5687 | 2025-08-26 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 5497bcb0-d7a6-387e-86c4-d34855223d5b | -6.8064 | -44.9791 | 2025-08-26 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| f7767a13-7018-32a4-81eb-def06abc0665 | -11.6308 | -46.2083 | 2025-08-26 13:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 252.4 |
| 88cb2215-0193-3452-802b-f9206c92d902 | -11.6086 | -46.3926 | 2025-08-26 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 196.8 |
| 4d941a70-c603-3d35-8f5f-552e23b84e69 | -9.7915 | -64.265 | 2025-08-26 13:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.0 |
| f2776d21-243f-3313-b19d-76a4451c1538 | -8.0841 | -44.997 | 2025-08-26 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 76.7 |
| c7fe935d-411f-39b4-b7e9-61255e7c62ab | -12.7932 | -49.8624 | 2025-08-26 13:50:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 189.3 |
| 6023c377-9e11-360c-be35-e475ed45d37f | -10.6818 | -47.1858 | 2025-08-26 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 8c5363e5-bb3f-37c0-a384-91deb07998ed | -10.3087 | -46.762 | 2025-08-26 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| e2f9158a-fd6c-3b6e-978e-d114bf7e3430 | -6.9128 | -59.3578 | 2025-08-26 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 84681dd0-5b5d-3b2d-9f6f-8f7292b88fcf | -12.7651 | -48.1348 | 2025-08-26 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| a80944da-92de-3c3b-95a1-efc1986b635e | -6.7635 | -59.6718 | 2025-08-26 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 7a1a2ecf-3353-3514-93fa-e82f11df278f | -12.7455 | -48.1597 | 2025-08-26 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 05048e20-e701-3a44-a46d-c9bcdbd82352 | -16.6224 | -49.3708 | 2025-08-26 13:50:00 | GOES-19 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 6148c5a5-8991-3109-bfc6-f70e4aed9aa4 | -12.7843 | -48.1321 | 2025-08-26 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.6 |
| d6366383-3063-3158-87c6-ea6e9279ce6c | -9.7916 | -64.2461 | 2025-08-26 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 8769b26b-f3cd-3dca-ba1a-d004b4b7c655 | -12.8123 | -49.8599 | 2025-08-26 13:50:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 141.7 |
| 0cfc7d0a-3eb9-3d8f-905b-c6aa3da919a9 | -6.8413 | -58.9552 | 2025-08-26 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.6 |
| a4e88e75-e2d8-3304-a2a7-7b68eabea9d7 | -6.7819 | -59.6711 | 2025-08-26 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 9516733a-a561-39fb-8363-b38a27ac4e59 | -12.7647 | -48.157 | 2025-08-26 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| bb0f3caa-86a7-3b6e-86fa-a126783859ba | -8.3317 | -44.7885 | 2025-08-26 13:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 7f550254-3d41-30ab-9d3d-1399e54390ef | -11.6308 | -46.2083 | 2025-08-26 13:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 197.8 |
| cf4e1f9e-e79b-3d4e-9e30-2239bee691c8 | -6.8228 | -58.9753 | 2025-08-26 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 213.4 |
| c3a92a18-8d06-3040-b2aa-cf5e681a6011 | -6.8044 | -58.9568 | 2025-08-26 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| f1e79def-204a-3967-a0b4-8ddb2df3fad0 | -6.2459 | -60.0174 | 2025-08-26 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 270.3 |
| bc7ebccb-feba-387f-ad39-7c11e747485f | -8.352 | -62.9436 | 2025-08-26 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 53eddee2-73bc-3292-a045-2f1e04478c10 | -12.6741 | -47.8589 | 2025-08-26 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| c04107b4-afa4-3372-b66d-5001c46f568d | -8.5387 | -62.6527 | 2025-08-26 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 1b481344-9e70-38e9-9d4a-0ce96c7c9c26 | -11.5779 | -52.115 | 2025-08-26 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 9ac094b4-cb02-35b7-90fa-7acd8fd13670 | -12.6737 | -47.8812 | 2025-08-26 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 975d483a-7a8c-366b-8d17-da56c541cc5d | -11.6082 | -46.4152 | 2025-08-26 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 38845b75-bef6-3169-801d-e3717f2663e4 | -6.5293 | -44.5687 | 2025-08-26 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 325.5 |
| a5f81b46-e03c-361c-87c0-ed0c24d48aed | -6.9061 | -44.4217 | 2025-08-26 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 2fdb302c-1840-3d4f-9a25-0f534cb55740 | -6.246 | -59.9982 | 2025-08-26 13:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 7d70c1bf-f3ab-3b44-9c36-55bd5854923a | -7.586 | -47.4835 | 2025-08-26 13:50:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| a662b46b-4680-3b39-97c5-7bb44a0df5fa | -6.8064 | -44.9791 | 2025-08-26 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 82a8cc83-4137-3b1e-babe-ba4f7d5100e9 | -10.6822 | -47.1635 | 2025-08-26 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 129.3 |
| fbc99dd0-621c-399d-9428-23bab749c52f | -11.6351 | -44.8561 | 2025-08-26 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 62.1 |
| dcb36c17-2ebd-3f7b-9110-96f476a8c096 | -6.8229 | -58.956 | 2025-08-26 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 217.5 |
| 41a88e41-c6b5-3981-bfd3-70701e6b5e6c | -11.6086 | -46.3926 | 2025-08-26 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 152.2 |
| 94507ee4-2c38-3921-b27a-f98baa107858 | -11.2014 | -50.5685 | 2025-08-26 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 131.5 |
| 5a8ff8e5-df8e-3034-8772-3916abb0e9df | -6.8062 | -45.0019 | 2025-08-26 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 0f24e3b9-0da2-3d1e-9777-8b72308c3c4e | -11.502 | -52.1229 | 2025-08-26 13:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 3072c568-557d-33ba-a14a-b503c6b0c34d | -6.6201 | -44.8581 | 2025-08-26 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 74eab980-4fdd-3a4f-baa9-3303304ffc01 | -11.6273 | -46.4126 | 2025-08-26 13:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 0ca3d9ef-b90b-3b7d-82e6-c5e8f9cc21f9 | -8.3521 | -62.9247 | 2025-08-26 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 522de135-c293-3fb8-8b2b-200c51402376 | -9.8102 | -64.2454 | 2025-08-26 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 86.1 |
| cfad9645-5bb5-3574-84de-e97b8b96bc4f | -6.8412 | -58.9746 | 2025-08-26 13:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.6 |
| d5d7c8d9-ecf0-37c9-b3a9-56f2b0668ac0 | -7.5858 | -47.5055 | 2025-08-26 13:50:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 60.9 |


[Clique aqui para ver as próximas entradas](README106.md)
