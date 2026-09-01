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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aed8eac9-a2b5-38c6-8f1c-8ec00d1c2067 | -8.7762 | -69.342102 | 2026-09-01 01:54:00 | METOP-C | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| e7e2a0ba-55f2-3033-a4e0-450d1565a121 | -9.1592 | -60.929001 | 2026-09-01 01:54:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e01d07fc-b10e-37c1-a531-077acabdff9a | -6.6117 | -58.59 | 2026-09-01 01:54:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 829c3836-a1e4-32f0-9ffe-3ef99a4af179 | -9.0265 | -65.4384 | 2026-09-01 01:54:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2a75e45f-6309-35fb-9e39-a564ed75a717 | -9.4558 | -67.452499 | 2026-09-01 01:54:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c2314800-6d85-3cbf-9e7e-18efdf3762a1 | -6.8196 | -59.0947 | 2026-09-01 01:54:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 43274f96-aa16-362a-a562-202d72d46a40 | -9.1625 | -59.5285 | 2026-09-01 01:54:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3348f491-b30b-3b25-bed3-001966d29bf2 | -9.085 | -65.378799 | 2026-09-01 01:54:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cedf1545-167a-3f30-9cb9-2163ae3ebe29 | -9.5291 | -68.562897 | 2026-09-01 01:54:00 | METOP-C | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 1f720083-7f31-3d5d-af68-f17a74e5b558 | -8.9665 | -71.247299 | 2026-09-01 01:54:00 | METOP-C | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 41927ba3-a9f9-3f95-9744-34d32305f0df | -8.938 | -62.353802 | 2026-09-01 01:54:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| bb6959e1-28ad-35ba-925a-693360e04bd9 | -3.6299 | -60.545399 | 2026-09-01 01:54:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2ec4ed88-44ee-3335-b1f2-521fa53779b4 | -8.7987 | -62.504299 | 2026-09-01 01:54:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 23741dd0-d8f5-3a15-b5fe-0de7b45c5ffc | -16.0547 | -54.3908 | 2026-09-01 02:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 0f0df6e0-127d-30a7-8862-55a2eb7eeddf | -6.6036 | -58.5972 | 2026-09-01 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 1077b73e-64bb-3785-9d8c-61468194532b | -17.3921 | -42.3495 | 2026-09-01 02:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 179.0 |
| 5ea35f46-8eec-316a-96ab-3a6481490ee8 | -10.3574 | -50.0171 | 2026-09-01 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| a828e2d9-8e62-3449-9595-c33d99993111 | -10.2212 | -50.3303 | 2026-09-01 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 0bc8ed1a-a3ea-3235-9d54-e4d95c7c0260 | -10.8627 | -45.356 | 2026-09-01 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 08c8f0cf-4ab1-30f8-b4f0-35a697e96a40 | -6.9552 | -55.635 | 2026-09-01 02:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 84d75770-b1e6-3472-b605-7388400c0907 | -6.6976 | -55.4091 | 2026-09-01 02:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 0a55aa62-4599-3df1-a4c5-d8a43a7d3fc1 | -10.3388 | -49.9977 | 2026-09-01 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| dc16d935-e905-3e4b-bf6e-b8cfa1246fd6 | -16.4773 | -47.9381 | 2026-09-01 02:00:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 877e1997-b807-3990-9dd6-c22c30605974 | -11.277 | -50.5815 | 2026-09-01 02:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 4c6fe803-1e03-3cd4-9eae-da139b17f7b0 | -9.4769 | -40.3365 | 2026-09-01 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 137.0 |
| 2c605150-d6fd-3485-838c-107e806d64e6 | -17.3914 | -42.3744 | 2026-09-01 02:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 157cff3a-af50-3d09-ad36-b5a33816b856 | -10.8624 | -45.3789 | 2026-09-01 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 3c447f20-e3c2-38d9-80b6-5627e1468c4c | -19.1347 | -57.3589 | 2026-09-01 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.0 |
| dcd6c994-1015-3dd3-b2df-327d3fbfd494 | -3.8604 | -44.0585 | 2026-09-01 02:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 27b2293f-f4cf-3785-828c-d5aa7fa51b7b | -6.6035 | -58.6166 | 2026-09-01 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.4 |
| 1e022810-7382-3a66-ac65-244f5b0647a1 | -16.4768 | -47.9608 | 2026-09-01 02:00:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 9e1a1618-9ed0-3c70-9a82-b4c859071ff8 | -9.4578 | -40.3392 | 2026-09-01 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 79.2 |
| 3ece4d79-ca7e-306a-b4f0-54fa7acd2141 | -7.182 | -60.6904 | 2026-09-01 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| b00132a1-596a-3f18-8bc3-0a4645d2ea83 | -14.6925 | -53.5384 | 2026-09-01 02:00:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 1cec828f-7cb2-3eda-8485-bfb1626fbb97 | -18.5089 | -50.8974 | 2026-09-01 02:00:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 4b3177e0-cbaa-3baf-aa9a-0ff429fc9fbe | -11.258 | -50.5836 | 2026-09-01 02:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 508b55ce-a203-3f03-943a-969bef775d09 | -11.2957 | -50.6008 | 2026-09-01 02:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 135.0 |
| bc6acfa6-b450-3bf3-a1eb-18c1ea71736a | -3.8603 | -44.0815 | 2026-09-01 02:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 1382d2ef-d2f5-37df-be3b-15f46fc48224 | -9.4765 | -40.3613 | 2026-09-01 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 79.2 |
| 5aca381d-87fc-3294-bd38-1158f0d8fa80 | -11.2767 | -50.6029 | 2026-09-01 02:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 141.9 |
| 50939771-ec20-32ae-bce2-46a07f67ad4d | -14.4587 | -52.5151 | 2026-09-01 02:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 698acb5c-de97-3436-aa05-0d4a94ef78b2 | -10.036 | -44.7056 | 2026-09-01 02:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 3e530540-f101-3953-a5bb-78594a9c7f89 | -7.2005 | -60.6897 | 2026-09-01 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| be9831cb-dc33-3fb4-9202-35b33ad4b4fb | -10.0364 | -44.6825 | 2026-09-01 02:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 91b2050c-4d15-32d1-9290-a32050d7e3f2 | -10.8818 | -45.3534 | 2026-09-01 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 2faef89f-51a9-345c-ae7b-a3ddc6c8a0a2 | -10.2023 | -50.3322 | 2026-09-01 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 145.1 |
| a00f144b-48de-38b1-a666-3b50784fe6b8 | -10.2025 | -50.3109 | 2026-09-01 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 164.2 |
| 799797bb-f1ce-30db-baf8-489066759310 | -3.8605 | -44.0355 | 2026-09-01 02:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| c4b386c4-2b3e-33d4-85cc-38ccff15d167 | -10.1837 | -50.3128 | 2026-09-01 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 111.8 |
| d52cbf2d-d338-31bb-9a67-a2ac44d5634c | -19.1147 | -57.3615 | 2026-09-01 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.3 |
| 1ea76dd6-ce0a-3251-80e4-694bc69a1b47 | -7.2005 | -60.6897 | 2026-09-01 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 0bb889e5-e26d-3d8d-88b1-1a665d4ad96d | -19.1951 | -57.3301 | 2026-09-01 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.6 |
| 3e808709-1929-3115-a408-38a61a9b2e39 | -7.3488 | -60.5691 | 2026-09-01 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.1 |
| cb6e6eac-dff4-3c4b-a219-3bb2a3573b5c | -16.0547 | -54.3908 | 2026-09-01 02:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 80.5 |
| c913dc1a-29cc-3b47-8d62-4c850f3b5572 | -7.182 | -60.6904 | 2026-09-01 02:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.7 |
| db4c2a35-5ef3-3ae0-8ca1-2ec6c5a25823 | -13.5343 | -59.7392 | 2026-09-01 02:10:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 7ea872a0-bd4f-335e-a783-8c9616e41926 | -10.2212 | -50.3303 | 2026-09-01 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| eebe30d8-18c8-320c-86d0-3d7e6087def0 | -6.1844 | -57.7395 | 2026-09-01 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| dd0830b3-f2be-3294-86c7-d15c49cb0316 | -17.372 | -42.3544 | 2026-09-01 02:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 60.2 |
| c5dd26de-9a31-3b0f-a95c-f4e37636139d | -10.2023 | -50.3322 | 2026-09-01 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 129.2 |
| ccae6fa2-6231-3e68-b14c-26589a447cf3 | -19.1344 | -57.3797 | 2026-09-01 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.3 |
| 5d3fec66-b06e-35f9-b091-961cca48d637 | -19.1547 | -57.3562 | 2026-09-01 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.4 |
| 9e9c0ab1-28d7-3316-983b-6b99c7600dbf | -15.8547 | -47.6884 | 2026-09-01 02:10:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 339f5571-7001-32ce-b6b9-360ea433531a | -14.4587 | -52.5151 | 2026-09-01 02:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 15c342e7-1a2b-3381-8524-a09e9fa4bd85 | -18.2496 | -52.7317 | 2026-09-01 02:10:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 60.4 |
| a11acf45-6e7d-3c72-92a7-b42aa5999654 | -3.8604 | -44.0585 | 2026-09-01 02:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 6b10cc71-b9b5-39cc-906e-0e25a2d6c020 | -6.6976 | -55.4091 | 2026-09-01 02:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| d8b0545a-98c2-3853-ab74-3dcac041fc8c | -19.2155 | -57.3066 | 2026-09-01 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 67.1 |
| bdb9ba6a-d8c9-357e-a7d3-0a77a5a73025 | -10.3574 | -50.0171 | 2026-09-01 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 47475ad0-99a4-35c8-b804-f304082d1325 | -11.2767 | -50.6029 | 2026-09-01 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 4ce1a041-9833-332e-824e-afab3c3cd63d | -19.1347 | -57.3589 | 2026-09-01 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 270.9 |
| 4742cd2f-8528-333f-9a8d-f6858869770d | -10.2025 | -50.3109 | 2026-09-01 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 115.8 |
| e51cb1e6-feff-3950-8ed0-8b1e6f7f94a4 | -7.3487 | -60.5883 | 2026-09-01 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 2dac6e61-8a1b-3636-89c1-2397eed58b4e | -6.6035 | -58.6166 | 2026-09-01 02:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 50001743-742e-3ddc-927e-22f2dd607275 | -11.277 | -50.5815 | 2026-09-01 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| f3f965f5-5747-300d-b5ba-4acc92fb1844 | -11.2957 | -50.6008 | 2026-09-01 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| ed9cc90a-338f-3bb1-ba6b-d404c19f1c68 | -11.258 | -50.5836 | 2026-09-01 02:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 45681289-9735-31bb-9b99-1a4d7d53292a | -17.3921 | -42.3495 | 2026-09-01 02:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 144.4 |
| 84ffdc04-8b04-350a-aac1-785902ad23a5 | -6.9552 | -55.635 | 2026-09-01 02:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 1aae90be-e83a-3353-ba37-ff58bd30cb18 | -10.1837 | -50.3128 | 2026-09-01 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.1 |
| cb101880-525d-3aa5-8de3-7bdaf46a2fe3 | -3.8603 | -44.0815 | 2026-09-01 02:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| d272f385-17a6-3150-9a4a-fe17a70d8091 | -6.6036 | -58.5972 | 2026-09-01 02:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 111.7 |
| 160f43c9-3e7e-3c61-9242-7cb61dba7e85 | -19.2151 | -57.3275 | 2026-09-01 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.9 |
| e894d6cd-89fa-30e6-9f73-31303136acc9 | -19.1351 | -57.3381 | 2026-09-01 02:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 150.4 |
| c27adaba-034f-3ddb-9d5c-21509fca1a2a | -7.3488 | -60.5691 | 2026-09-01 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 55cd1f4d-fe66-346c-891e-a1676952008f | -19.1347 | -57.3589 | 2026-09-01 02:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 76.8 |
| 2632a22e-2264-3639-bcb9-18190970b035 | -10.1837 | -50.3128 | 2026-09-01 02:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 61.7 |
| c9113aa2-dfe4-3e03-9276-54fd26897819 | -11.2957 | -50.6008 | 2026-09-01 02:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 2ec41358-d5d3-34f7-9224-adb740f3ab73 | -17.3914 | -42.3744 | 2026-09-01 02:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 712b7167-c7b6-3cf3-87ec-7138b3c8211e | -16.0547 | -54.3908 | 2026-09-01 02:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 1ef90753-1607-33fb-835b-c6e27005f67c | -10.2025 | -50.3109 | 2026-09-01 02:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 5e59786d-71a2-325f-bb8f-5ed2416aaac3 | -10.2023 | -50.3322 | 2026-09-01 02:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 3bfb75e0-a7ca-3c94-8eeb-a3fcc5f8f8bb | -11.258 | -50.5836 | 2026-09-01 02:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.9 |
| f4f5170e-06eb-30e2-81db-cad0d4ef6281 | -6.6036 | -58.5972 | 2026-09-01 02:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 5b8c7c83-996c-3b61-860b-0008e6cdfbd8 | -7.3487 | -60.5883 | 2026-09-01 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| d0ee11c5-b101-32ca-8cc5-b0d4593b935c | -10.2212 | -50.3303 | 2026-09-01 02:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 816a3326-4f14-3480-a1fd-52b19bf54af0 | -6.9552 | -55.635 | 2026-09-01 02:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 936d2ee6-8a0d-3cb1-8e8e-3d72156ae612 | -3.8604 | -44.0585 | 2026-09-01 02:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 8336069d-74d3-3118-8c0b-8da64e37e6ca | -3.8692 | -49.1202 | 2026-09-01 02:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 39b0a195-5777-3054-9266-7d1773e199db | -6.6035 | -58.6166 | 2026-09-01 02:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 39.4 |


[Clique aqui para ver as próximas entradas](README17.md)
