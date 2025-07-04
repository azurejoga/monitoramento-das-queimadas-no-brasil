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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 344f0858-37a6-3f4d-ab95-c8c705bf41ac | -20.72715 | -56.65678 | 2025-07-04 04:42:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90bf07d2-ece6-30b9-9e07-53bdb4306074 | -22.66411 | -47.46105 | 2025-07-04 04:42:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b959223-323f-31ca-9d11-d56fa005aaa6 | -18.37297 | -49.26694 | 2025-07-04 04:42:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51a59ebf-3d4e-358c-8c66-fd2f6cb4cbb1 | -19.72048 | -44.88517 | 2025-07-04 04:42:00 | NOAA-20 | CONCEIÇÃO DO PARÁ | MINAS GERAIS | Brasil | 3117603 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dc692c0e-9c8e-3cb6-9c84-c21aca1a27f0 | -22.5391 | -48.8124 | 2025-07-04 04:42:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd61c14c-008e-3e01-b727-dd1dd7b17410 | -21.1253 | -57.5209 | 2025-07-04 04:42:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| c0ebd167-a671-3498-b2f6-822f4f0049bc | -18.44817 | -54.66833 | 2025-07-04 04:42:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cac530b9-81c9-3c4d-ae32-43f20f173a95 | -18.44405 | -54.67164 | 2025-07-04 04:42:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 20a20ec0-b16d-3103-98b7-e165e5b2f481 | -18.71346 | -46.61179 | 2025-07-04 04:42:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 76933335-a2a2-3889-99b2-cbf04b3474a6 | -18.14126 | -53.29423 | 2025-07-04 04:42:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66a63121-b146-3e5b-8067-bba2558dff90 | -18.65616 | -55.73893 | 2025-07-04 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| e2431c21-4784-32bc-ae0a-6de05803fb4c | -21.39076 | -51.86644 | 2025-07-04 04:42:00 | NOAA-20 | PANORAMA | SÃO PAULO | Brasil | 3535408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 533c5958-b990-3e77-a7d8-a1c7976a750c | -21.03882 | -55.99664 | 2025-07-04 04:42:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16446bf1-fd45-3bc1-8cee-713327202fcd | -19.74637 | -54.00018 | 2025-07-04 04:42:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 39627af1-a7fe-32b9-ac8c-f432d19d07a1 | -23.59403 | -54.4295 | 2025-07-04 04:44:00 | NOAA-20 | IGUATEMI | MATO GROSSO DO SUL | Brasil | 5004304 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6fb96f7e-b17a-3228-bac0-00adeb1e3250 | -30.14977 | -52.0265 | 2025-07-04 04:44:00 | NOAA-20 | MINAS DO LEÃO | RIO GRANDE DO SUL | Brasil | 4312252 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 49539998-705b-3854-ab09-f9abdafb9959 | -24.24347 | -50.7391 | 2025-07-04 04:44:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7426d4bf-6eca-371d-9741-ead2cbb6983d | -24.74328 | -53.80749 | 2025-07-04 04:44:00 | NOAA-20 | TOLEDO | PARANÁ | Brasil | 4127700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 13bf9210-541c-3c2a-adfd-07843bb020e1 | -23.78408 | -52.24386 | 2025-07-04 04:44:00 | NOAA-20 | ENGENHEIRO BELTRÃO | PARANÁ | Brasil | 4107504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 39390a05-ca0d-35a0-bae3-f01321c1db89 | -27.92269 | -51.67052 | 2025-07-04 04:44:00 | NOAA-20 | SANTO EXPEDITO DO SUL | RIO GRANDE DO SUL | Brasil | 4317954 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c2ebf6c6-9d64-3a82-99f3-992bcc88139d | -10.5586 | -49.1337 | 2025-07-04 04:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 165c25a2-d407-38e3-a339-5e3b1a50aa91 | -6.6112 | -43.8941 | 2025-07-04 04:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 68070fd1-3166-30af-9939-bcd0eb834e42 | -6.6112 | -43.8941 | 2025-07-04 05:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 51.1 |
| c951314f-4a8f-31cc-b14f-552fd18396ed | -7.22472 | -43.08934 | 2025-07-04 05:04:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 36.7 |
| 6fd34f0a-187f-31fc-832d-3261f7e8f8fa | -6.60605 | -43.90295 | 2025-07-04 05:04:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 26.7 |
| fc2a4651-7bc4-35b5-a765-5dd6181f4a02 | -7.22143 | -43.09374 | 2025-07-04 05:04:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 30.4 |
| 1f92090b-2474-3a78-aba0-1ce243413fc0 | -6.6113 | -43.88484 | 2025-07-04 05:04:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 107.0 |
| e64c2f01-e00e-3d39-a808-f855e075a235 | -6.61026 | -43.8772 | 2025-07-04 05:04:00 | AQUA_M-M | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 54801305-1c4e-3050-97a0-7267af0175b5 | -6.2776 | -43.66365 | 2025-07-04 05:04:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 0938ad1d-f095-30d0-a282-82b303422015 | -6.27967 | -43.6713 | 2025-07-04 05:04:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 34.8 |
| b2635c31-7c02-3d5f-a581-0e0597b58aed | -11.91653 | -45.38428 | 2025-07-04 05:06:00 | AQUA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 98d0378f-f562-31a0-badc-823c94928b23 | -16.94287 | -46.08318 | 2025-07-04 05:08:00 | AQUA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 68.2 |
| c58de519-9b8b-30e8-a52f-d95b9d637f44 | -6.6112 | -43.8941 | 2025-07-04 05:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| d2b12d03-b933-3772-bcf6-8a601b0718b0 | -16.9556 | -46.0759 | 2025-07-04 05:20:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 107.9 |
| b0fb22fe-11b3-30c3-afef-14f59b68f240 | -16.9357 | -46.08 | 2025-07-04 05:20:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 64.2 |
| f49e1856-a0da-3e55-b49f-516ad5ca2903 | -6.6112 | -43.8941 | 2025-07-04 05:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| ab887aa3-6116-3367-987c-09ceaed7969c | -16.9551 | -46.0994 | 2025-07-04 05:20:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 8ac267d5-181a-35a4-ac2b-924cab4e9a9c | -16.9352 | -46.1034 | 2025-07-04 05:20:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 85be58d4-39ca-3b8b-bfd7-af575bf06cd6 | -8.72061 | -64.17607 | 2025-07-04 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36075c57-736e-3955-a610-a2e299bf9d5f | -10.59312 | -49.45924 | 2025-07-04 05:29:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 120d0a11-cafc-3887-8005-41115d6aaace | -9.63475 | -61.46235 | 2025-07-04 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e0085df-e15d-3456-be6f-465e8b7ea62a | -10.308 | -57.1357 | 2025-07-04 05:29:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3db89489-04b0-32b4-8b3d-2f366034c706 | -8.65572 | -64.0516 | 2025-07-04 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d3f9bae8-54fc-3afc-b481-bddf467e395f | -9.90721 | -55.52999 | 2025-07-04 05:29:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d83035a-3879-3a9a-b2af-97124bd395fa | -8.53052 | -54.7729 | 2025-07-04 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| bcec4041-1d21-34c7-95f8-2d84fd057368 | -9.24902 | -58.74339 | 2025-07-04 05:29:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec6249e9-a3b8-318c-bd6a-232a0f668802 | -10.59566 | -49.4589 | 2025-07-04 05:29:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 960e9490-bb0d-37d7-811b-5675650c7661 | -6.91262 | -59.85919 | 2025-07-04 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7dfacf34-269b-3987-9aa0-4c5f20fbce12 | -9.9079 | -55.52483 | 2025-07-04 05:29:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9df0691f-30e0-348b-a65d-c9bda9991e33 | -10.35343 | -56.49612 | 2025-07-04 05:29:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69fa5234-ad15-3fdb-b0fa-d2e5e9419b22 | -9.63137 | -61.46183 | 2025-07-04 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c9623da-1fd7-3e1f-b340-f8cf1cc16247 | -9.52685 | -58.18021 | 2025-07-04 05:29:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1523e2f1-da7b-3989-842d-d17c02e1b789 | -8.5256 | -54.7722 | 2025-07-04 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 5651d45a-59e8-3f0a-8531-c5d62dc7a735 | -8.65344 | -64.06592 | 2025-07-04 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3d657f4-84d1-33a2-898c-51836ea651c5 | -8.4469 | -49.63123 | 2025-07-04 05:29:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| e78fe39f-8797-39e4-8ba0-e5ad55a2fe7a | -8.49012 | -49.8543 | 2025-07-04 05:29:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b3ad3f4c-a87e-38f8-975b-bddd34bd1e19 | -9.24833 | -58.74812 | 2025-07-04 05:29:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf0f4546-3dc6-3cba-b428-93f0088c7e5d | -8.71783 | -64.17192 | 2025-07-04 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 076a4700-77ff-376f-86c1-3e5cc5b21811 | -10.30744 | -57.13981 | 2025-07-04 05:29:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1161bb0e-279e-3f05-9c97-fe5d095253f2 | -5.91945 | -61.30259 | 2025-07-04 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0898083f-c1d5-3e97-a994-65bc24181390 | -6.63318 | -56.27725 | 2025-07-04 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d15108b-cf5b-34ef-bf71-dfcbb1a188d5 | -8.44774 | -49.63556 | 2025-07-04 05:29:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 6d462593-65a1-3e45-baf9-986498cab116 | -10.22831 | -56.76355 | 2025-07-04 05:29:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 117db6d1-effa-3859-8acb-f7fde1dc6048 | -6.25468 | -55.65565 | 2025-07-04 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0668143-d184-300c-9a10-580d03e9c491 | -6.63378 | -56.27304 | 2025-07-04 05:29:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2f18dab-abe1-3125-8e78-9f4715564a2a | -9.31157 | -62.6526 | 2025-07-04 05:29:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 52b97ae9-71d0-39af-8b64-5d5f5d6fd018 | -10.58858 | -49.45798 | 2025-07-04 05:29:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fc67c56e-29d3-359f-a894-e64291a0d903 | -9.19078 | -61.8501 | 2025-07-04 05:29:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 03a3ba6c-7713-37d5-aeed-a20aa83dffe6 | -10.30315 | -57.13923 | 2025-07-04 05:29:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0b0a49a-00ff-358d-b9be-e908ad7fff9f | -8.52762 | -54.77269 | 2025-07-04 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| c2b54b70-3273-3c0b-aedf-775d5464a929 | -7.19131 | -59.83878 | 2025-07-04 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78799de3-f58c-39cf-9a21-bc3dc3aab5cd | -8.72119 | -64.17247 | 2025-07-04 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47dc8b28-32a8-3e22-a289-8f36f66b2605 | -7.92717 | -61.55619 | 2025-07-04 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26667e65-c09a-3226-aa5f-0e6585c627fc | -10.05481 | -59.10985 | 2025-07-04 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9a5db4d-0aae-3e66-86d0-68255bf95965 | -9.19133 | -61.84653 | 2025-07-04 05:29:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca0388f8-c7dd-3285-8993-98d80cb12a89 | -10.2327 | -56.76417 | 2025-07-04 05:29:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a492b972-4f80-3a07-b415-ed5271a4d501 | -9.03688 | -63.98486 | 2025-07-04 05:29:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d196f63c-00d3-3b69-ac4f-921e23c309d8 | -10.30054 | -57.12627 | 2025-07-04 05:29:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 417318f2-99d6-3f4b-bded-e109544c287b | -7.17727 | -59.83664 | 2025-07-04 05:29:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e15b442-2d18-32b0-b9b6-01661e5bb873 | -7.89235 | -61.47499 | 2025-07-04 05:29:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff2bc515-88ef-3739-a518-ca71d34f1a9e | -7.09849 | -49.17299 | 2025-07-04 05:29:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 71ab10f1-93ab-3db4-be60-b5ee031295fe | -8.53253 | -54.77341 | 2025-07-04 05:29:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9d03e61f-775c-3b9c-951d-9bf2f52293a6 | -9.90314 | -55.52414 | 2025-07-04 05:29:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df804a01-606b-3945-8ac4-fbd41009cf3e | -6.97821 | -55.28688 | 2025-07-04 05:29:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c59cd21-ae61-3e04-b0ca-7e63b1fc1334 | -9.63419 | -61.46599 | 2025-07-04 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b95e7487-243e-3846-8e61-c68812f0b666 | -8.44851 | -49.62917 | 2025-07-04 05:29:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 75431896-6197-3bbf-9773-c10e32a12744 | -10.29886 | -57.13865 | 2025-07-04 05:29:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b24cb1b8-4c13-3030-af6b-0bab931d83a3 | -9.63026 | -61.46912 | 2025-07-04 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5459a4b1-8cce-3069-9350-b3843c503ad0 | -9.63082 | -61.46548 | 2025-07-04 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 122c2cf7-36c9-3782-a7e5-65fc7eed7e06 | -6.6112 | -43.8941 | 2025-07-04 05:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| e2a2de7c-fc43-3dff-92f0-ffb5adc48dba | -16.9551 | -46.0994 | 2025-07-04 05:30:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 413a7149-73aa-3605-9e69-b670034443f9 | -9.53094 | -63.57634 | 2025-07-04 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 43c79210-ce50-3a39-9370-cfc183fdd8b4 | -10.52834 | -68.04586 | 2025-07-04 05:31:00 | NOAA-21 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1be6f0af-1951-3575-828b-fbebf324472f | -11.87601 | -58.73061 | 2025-07-04 05:31:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be3aa1dc-b884-3fd8-86ab-5961777dd128 | -9.22169 | -67.90767 | 2025-07-04 05:31:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e9c63081-a079-3240-96c4-df2c17201166 | -11.87926 | -58.73636 | 2025-07-04 05:31:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 49f5e2e4-080a-30e2-9db6-8545d1ab24c5 | -11.87627 | -58.73449 | 2025-07-04 05:31:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 51733acc-2c38-3e68-9856-f155410193a1 | -9.64078 | -63.50422 | 2025-07-04 05:31:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c09395d5-a5c7-31f9-b99c-f598b8337b3f | -11.32914 | -55.21619 | 2025-07-04 05:31:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a941946-28d6-350e-b607-3b13499cbe87 | -11.87995 | -58.73126 | 2025-07-04 05:31:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README21.md)
