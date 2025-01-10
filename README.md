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
| 77f92442-0a7e-3ffe-bc2c-b434908e5c20 | -10.0265 | -36.2969 | 2025-01-10 00:00:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 128.8 |
| 9610eaed-60f7-3e56-9477-a7e418e086e5 | 1.9236 | -60.4019 | 2025-01-10 00:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 49.2 |
| af3862d4-216d-3722-9aad-87a39c4dbace | -17.6664 | -54.1684 | 2025-01-10 00:00:00 | GOES-16 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 2f0bc710-899c-361f-a2a1-f19e1a8672fc | -10.0458 | -36.2935 | 2025-01-10 00:00:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 96.3 |
| a97bf4aa-a662-31c9-b151-409b05cb7c75 | 1.9419 | -60.4017 | 2025-01-10 00:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 48.8 |
| ae1e2278-c60a-3c8b-b8a8-39a579a5173d | -10.03 | -36.28 | 2025-01-10 00:00:00 | MSG-03 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 590f4a18-0959-371b-bafe-17ed379c9e91 | -10.03 | -36.32 | 2025-01-10 00:00:00 | MSG-03 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| b8fa48c9-fb75-3808-898e-57533a3769cf | 1.9236 | -60.4019 | 2025-01-10 00:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 43.8 |
| eabbb83e-b795-3f93-bf33-7fb1d6ae165e | -17.6664 | -54.1684 | 2025-01-10 00:10:00 | GOES-16 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 65a84583-8313-3fa1-8b3b-24aa56c047d3 | -8.9146 | -36.107498 | 2025-01-10 00:12:00 | METOP-C | CANHOTINHO | PERNAMBUCO | Brasil | 2603702 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d4ef45da-2c63-3eaf-9c64-6a57f3c1f1a5 | -9.807 | -36.3409 | 2025-01-10 00:12:00 | METOP-C | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 69bd0e69-dc03-3213-9e1a-0fa7480a62c5 | -10.0753 | -36.993099 | 2025-01-10 00:12:00 | METOP-C | NOSSA SENHORA DE LOURDES | SERGIPE | Brasil | 2804706 | 28 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6b3dd0ce-417f-3a9e-bf99-23f970a8e9f3 | -9.4398 | -36.057701 | 2025-01-10 00:12:00 | METOP-C | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 83f0d1c9-980c-3df6-b068-0e22e2a3a0b3 | -8.3552 | -35.1553 | 2025-01-10 00:12:00 | METOP-C | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9dcc22d3-80f4-31d2-ac75-b0262262e5e5 | -6.5812 | -35.114399 | 2025-01-10 00:12:00 | METOP-C | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 640aafd0-4264-3396-a8b4-156cccfbbc4c | -9.7023 | -36.032501 | 2025-01-10 00:12:00 | METOP-C | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ba0930fc-03ad-365a-b878-060518d01d4f | -6.5785 | -35.103298 | 2025-01-10 00:12:00 | METOP-C | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 73ed5689-02d8-3ec9-85b5-a604102eb118 | -9.805 | -36.332401 | 2025-01-10 00:12:00 | METOP-C | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 339d7abe-0ba7-3560-9be6-120698b0be85 | -9.6926 | -36.034901 | 2025-01-10 00:12:00 | METOP-C | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 91cbef5f-77f8-3075-9bd8-3c1cb9e15e7f | -9.4148 | -36.082699 | 2025-01-10 00:12:00 | METOP-C | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ba168871-f1ec-3ec4-9558-1b4f4aae57c5 | -9.4169 | -36.091702 | 2025-01-10 00:12:00 | METOP-C | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f5856399-7860-3d71-bd0b-f1cda697d902 | -8.9124 | -36.0984 | 2025-01-10 00:12:00 | METOP-C | CANHOTINHO | PERNAMBUCO | Brasil | 2603702 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7465af4c-66bc-3cdc-9353-c068a28fec4b | -10.0552 | -36.690102 | 2025-01-10 00:12:00 | METOP-C | PORTO REAL DO COLÉGIO | ALAGOAS | Brasil | 2707503 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 40a6e4fc-9158-3ecb-8822-462a6fb75d4a | -8.2291 | -35.317001 | 2025-01-10 00:12:00 | METOP-C | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0e3911be-6fc1-3f7a-af38-310d2c28989a | -9.6641 | -37.132599 | 2025-01-10 00:12:00 | METOP-C | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 757d7e5b-8214-37e6-8d34-cb228093ddac | -6.9197 | -35.150101 | 2025-01-10 00:12:00 | METOP-C | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6ce8d40c-aad8-34e8-94a3-48248b56ccd0 | -23.3546 | -48.5195 | 2025-01-10 00:20:00 | GOES-16 | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Cerrado | 66.9 |
| b489d0d9-79e2-3c51-8bac-c3c1a648c7cd | -9.6271 | -36.043 | 2025-01-10 00:20:00 | GOES-16 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 63.7 |
| 6333f37f-83f5-3631-9890-c6d0fb869b07 | 1.9419 | -60.4017 | 2025-01-10 00:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 45.1 |
| bb80b7f5-4eb5-30c6-958c-f38d8fc3c4d5 | -9.8973 | -35.9956 | 2025-01-10 00:20:00 | GOES-16 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 54.9 |
| 3a6c93e4-0f46-34e3-8346-7d6004670d57 | 1.9236 | -60.4019 | 2025-01-10 00:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 59.7 |
| ce4c96f1-2ee7-36d9-aa56-21e6acaa065f | -9.6271 | -36.043 | 2025-01-10 00:30:00 | GOES-16 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 133.6 |
| d645222b-3e3c-374d-8704-0ad5a61cf003 | 1.9419 | -60.4017 | 2025-01-10 00:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 38.8 |
| eb5f3a3c-30ef-3b2c-bfba-5cf5bc1d6a82 | -23.3546 | -48.5195 | 2025-01-10 00:30:00 | GOES-16 | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Cerrado | 61.5 |
| b6de0bfc-975d-3b83-8f97-0f90688e9052 | -9.6073 | -36.0735 | 2025-01-10 00:30:00 | GOES-16 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 121.4 |
| 8565fc3d-50ca-393b-a67d-37661e93cf28 | -9.6266 | -36.0701 | 2025-01-10 00:30:00 | GOES-16 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 110.6 |
| 312b28f3-a25e-38d7-a391-d3708166e102 | -9.6078 | -36.0463 | 2025-01-10 00:30:00 | GOES-16 | PILAR | ALAGOAS | Brasil | 2706901 | 27 | 33 | nan | nan | nan | Mata Atlântica | 120.5 |
| 27bd499f-7af9-3a92-aa12-eb214bc43c05 | 1.9236 | -60.4019 | 2025-01-10 00:30:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 58.3 |
| bed2bfe0-7b51-34bf-a507-07a852f635ed | 1.9236 | -60.4019 | 2025-01-10 00:40:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 2360ce56-b9f6-3062-ae33-bef81beb3fdd | -9.4184 | -35.8891 | 2025-01-10 00:40:00 | GOES-16 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 68.5 |
| 4d3013ac-6673-37e5-add3-360643e87fec | -20.98091 | -49.77119 | 2025-01-10 00:49:00 | TERRA_M-M | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.0 |
| 9c379253-da6a-320b-9ab3-0537e967ac83 | -23.3557 | -48.53375 | 2025-01-10 00:49:00 | TERRA_M-M | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Cerrado | 31.0 |
| d3ca618d-210e-3e93-ae46-de36e1302fd2 | -20.87978 | -49.87053 | 2025-01-10 00:49:00 | TERRA_M-M | UNIÃO PAULISTA | SÃO PAULO | Brasil | 3555703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| b941b85a-e472-3376-90a3-4f620f8fe4cf | -20.98243 | -49.78429 | 2025-01-10 00:49:00 | TERRA_M-M | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.9 |
| 03fffedb-0afd-3d05-9bd6-d851ea74214f | -22.02272 | -49.11978 | 2025-01-10 00:49:00 | TERRA_M-M | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4c011d6c-936b-39bb-a62c-c961d88381d6 | -23.35425 | -48.52183 | 2025-01-10 00:49:00 | TERRA_M-M | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 9c771f80-999d-35cc-a8e8-df8b7d05a09f | -20.30796 | -55.69071 | 2025-01-10 00:49:00 | TERRA_M-M | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 6fc3846b-e13f-3865-9e6e-da572e4f6cb3 | -20.5246 | -49.60511 | 2025-01-10 00:49:00 | TERRA_M-M | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 51a07132-1e6a-33ea-991b-4fa69689bfdf | -17.65693 | -54.16621 | 2025-01-10 00:49:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 32fe59a6-d891-3f4a-a6ce-676c4a79f810 | 1.9236 | -60.4019 | 2025-01-10 00:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 7c122a2e-51b4-368c-9993-c9b356f246a2 | 1.9236 | -60.4208 | 2025-01-10 00:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 37.1 |
| dbfcf863-ceb9-3007-88df-4541aeb76bb3 | 1.9419 | -60.4017 | 2025-01-10 00:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 1397a400-b7b4-33e1-b472-b772a472ce93 | -20.9909 | -49.760101 | 2025-01-10 00:52:00 | METOP-B | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a1a4152a-4e1f-3769-8f9d-3e51c4c80089 | 3.3111 | -60.531399 | 2025-01-10 00:52:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0703abfa-df01-3a49-8d95-8445a6e55eb1 | -19.3276 | -54.942001 | 2025-01-10 00:52:00 | METOP-B | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9dd19d79-666e-363b-8671-ece75f89cbd1 | 3.3129 | -60.5238 | 2025-01-10 00:52:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 849bf162-e2cc-3240-bca8-496be5894e2e | -20.5361 | -49.5858 | 2025-01-10 00:52:00 | METOP-B | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bc08a4d6-19a6-368a-aa3f-8ab595b483f0 | 3.321 | -60.5336 | 2025-01-10 00:52:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ddfcefa0-cc46-3300-8315-96415f3d0cb4 | 4.3802 | -60.860901 | 2025-01-10 00:52:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e122183b-dceb-3335-9f2f-297bec0517a4 | -20.9792 | -49.754398 | 2025-01-10 00:52:00 | METOP-B | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4a826536-f0b8-3b7b-9796-e0d98b2ac3c6 | -20.305099 | -55.673599 | 2025-01-10 00:52:00 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| c0ea4ece-97cf-39cd-8bc4-aa2b831f5133 | 4.0571 | -60.6506 | 2025-01-10 00:52:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f318b2ad-c642-340c-abab-5c71ab989ba0 | 4.165 | -60.6749 | 2025-01-10 00:52:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 81fd4bae-5d30-3fe3-b6ce-a44fe7a23fd5 | 1.9408 | -60.8484 | 2025-01-10 00:52:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0bf48914-0cfa-3102-9af1-780093ccc4a2 | -20.9811 | -49.762699 | 2025-01-10 00:52:00 | METOP-B | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a14b90e0-b2df-3abd-aa4d-a5d03f641c0b | 3.972 | -59.665699 | 2025-01-10 00:52:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| fecafa91-c03a-3f3e-97f1-50792ab6be01 | -21.5688 | -54.182701 | 2025-01-10 00:52:00 | METOP-B | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5af849bc-6251-31ae-ab3a-56343aa50f6a | -3.1041 | -54.591702 | 2025-01-10 00:52:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec574932-82f9-327e-a55d-047dc106c819 | 1.9309 | -60.3937 | 2025-01-10 00:52:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8298e13b-6388-3def-ba19-6f3d7e3ea14d | -17.6647 | -54.160801 | 2025-01-10 00:52:00 | METOP-B | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| a8653335-0823-34bc-ae10-537a7e65a117 | 4.0375 | -60.646198 | 2025-01-10 00:52:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| bd72ae2c-7cbc-358a-a356-728efd634c72 | 3.3031 | -60.521599 | 2025-01-10 00:52:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6c0334ea-99b7-3084-81b4-aadbff3c9aa8 | -20.988899 | -49.751801 | 2025-01-10 00:52:00 | METOP-B | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ee12cebe-0f42-368c-b6b1-55055e3c6c62 | -22.025101 | -49.095402 | 2025-01-10 00:52:00 | METOP-B | AREALVA | SÃO PAULO | Brasil | 3503406 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 03885c22-8f51-3526-8573-8e3125a96d42 | -2.6606 | -54.861401 | 2025-01-10 00:52:00 | METOP-B | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b21cc2f-cd7c-3cf2-ab0f-94e43700c974 | 3.3048 | -60.513901 | 2025-01-10 00:52:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1db84f31-817b-3fc2-8509-bac146638ce7 | -3.1024 | -54.584301 | 2025-01-10 00:52:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d18bcf4b-2b6c-3a12-b02a-c7f2238394a5 | 4.0473 | -60.648399 | 2025-01-10 00:52:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 223de553-010d-3459-bd45-149eb355f1a1 | 3.6146 | -60.3759 | 2025-01-10 00:52:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0fdc8b80-3602-37d3-8935-cb4c303ff53d | -20.306801 | -55.682098 | 2025-01-10 00:52:00 | METOP-B | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 7c6853dc-0b77-320b-8f80-031361d8e61a | 3.6129 | -60.3834 | 2025-01-10 00:52:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0531dd7f-4074-330c-b420-8c0fc91016af | 3.7024 | -60.261799 | 2025-01-10 00:52:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d4e56710-b633-3f5f-a832-99ddc5abe45e | -2.8538 | -53.990299 | 2025-01-10 00:52:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 534facbe-a695-3616-bdf8-f08fe54a82c9 | -17.663099 | -54.1535 | 2025-01-10 00:52:00 | METOP-B | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| bb379443-6a61-3459-855d-ca2771613a3f | 4.1667 | -60.667301 | 2025-01-10 00:52:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c853b446-5443-32ec-b755-2a773abbb8b2 | -2.6589 | -54.854099 | 2025-01-10 00:52:00 | METOP-B | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1db963c9-53bb-3535-9409-f4b858be37b2 | 1.9291 | -60.401501 | 2025-01-10 00:52:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1f456c21-2f6d-3e85-b003-2eb109688589 | 4.049 | -60.6408 | 2025-01-10 00:52:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0fd57a53-94e4-31a4-a9ce-be11014478c3 | -21.5704 | -54.190498 | 2025-01-10 00:52:00 | METOP-B | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| abe179a6-a919-35a5-9d58-3ab9121c7737 | 1.9427 | -60.840199 | 2025-01-10 00:52:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| bbc06ff4-ba60-3eb4-8372-4a7a3fcc6092 | -19.307699 | -53.723598 | 2025-01-10 00:52:00 | METOP-B | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 704f7802-b649-3461-bede-016f13c96131 | 4.0392 | -60.638599 | 2025-01-10 00:52:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4f1f824d-dc2b-3023-918d-84007cc18286 | 3.3146 | -60.516102 | 2025-01-10 00:52:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9bba9b54-bbed-3217-ba57-5453e65417c8 | 4.3784 | -60.868599 | 2025-01-10 00:52:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0be28e85-9970-36fa-bd12-f173734a81e7 | 1.9327 | -60.385899 | 2025-01-10 00:52:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c0ff35a5-1c33-36c2-b741-e008975f1d13 | 3.31167 | -60.54209 | 2025-01-10 00:56:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 189ac5c8-1b4d-374d-9b63-472bfc735686 | 4.03989 | -60.66578 | 2025-01-10 00:56:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 28.3 |
| 0280f79d-9949-348a-b1a7-9f1187735905 | 4.04826 | -60.66249 | 2025-01-10 00:56:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 2c53ef86-2d47-3f36-b778-fb137785b422 | -10.0829 | -36.3676 | 2025-01-10 01:00:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 130.6 |
| 76312074-c1ce-3f08-a902-1cbe0082dcad | -10.0641 | -36.3441 | 2025-01-10 01:00:00 | GOES-16 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 88.8 |


[Clique aqui para ver as próximas entradas](README2.md)
