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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8949f719-2a3d-3dd8-a480-e95f777629de | -8.1029 | -61.1878 | 2025-08-14 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 172.6 |
| b37fd34d-5442-3079-bac4-edd828883aba | -7.2375 | -57.6342 | 2025-08-14 14:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 34a2364d-4541-3daa-bd5d-0af304981b9c | -8.1215 | -61.187 | 2025-08-14 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| b30811ab-f847-311a-b899-2fe939574b76 | -6.0991 | -59.9459 | 2025-08-14 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 195.0 |
| c7e70dcb-c993-3e4d-aa00-9f5d875578a8 | -8.7572 | -44.0267 | 2025-08-14 14:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 85c663eb-8a94-38c8-bd45-c5383ffff29a | -7.6103 | -63.516 | 2025-08-14 14:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 143.7 |
| c81ce462-6490-3fba-a1fa-a0399f841bfa | -7.8775 | -61.8063 | 2025-08-14 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 92.2 |
| de58bd9d-4efb-34ff-bacc-77ecf279d84d | -13.1265 | -57.1494 | 2025-08-14 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 116.1 |
| e17fb9fa-aa78-35a2-83bc-57657ba70cab | -8.1028 | -61.2069 | 2025-08-14 14:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 131.0 |
| 9b5b6129-f7a3-3685-9cec-69ccc778a181 | -7.9119 | -46.8364 | 2025-08-14 14:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 26f18b82-854c-3dee-b8f9-c271f5343257 | -7.3116 | -60.628 | 2025-08-14 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 334.1 |
| 07bbec61-4db5-3ac6-aa2f-931d804f593f | -8.7385 | -44.0056 | 2025-08-14 14:30:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 97.9 |
| 9235f56b-4eaf-32d5-bb54-62a0e94671df | -6.1176 | -59.9261 | 2025-08-14 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| abbd5461-ee0b-3726-a8c4-41ae3cb9057b | -7.33 | -60.6273 | 2025-08-14 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 472.2 |
| 6307636a-a1fa-3c29-84ee-f6a92140e533 | -7.0799 | -59.1964 | 2025-08-14 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| d0a47489-15ef-36b4-8a95-aba289021bbd | -8.1028 | -61.2069 | 2025-08-14 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 154.9 |
| 309afce8-0fc4-34f7-8d23-bb00df678c7a | -8.1029 | -61.1878 | 2025-08-14 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 203.4 |
| 422ca96d-9693-3cd7-a9e5-d9fa590073f0 | -11.6797 | -51.62 | 2025-08-14 14:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 4b01da5a-99ee-3ab1-b8de-f68716690945 | -7.0799 | -59.1964 | 2025-08-14 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.0 |
| ace89afb-945f-357e-b520-3f8f8d56e1c8 | -7.9307 | -46.8347 | 2025-08-14 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 132.1 |
| 0f25276f-f7d6-3894-a015-dcc9098f561f | -8.1215 | -61.187 | 2025-08-14 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 140.9 |
| b065298d-b3ae-3018-8e66-b4d0aaa84136 | -7.5551 | -63.4802 | 2025-08-14 14:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 90eeeb9f-e548-35ac-98cd-f33acf757a7d | -13.1265 | -57.1494 | 2025-08-14 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 3d0d9db8-2479-3de2-82c5-6b749056d738 | -8.7382 | -44.0289 | 2025-08-14 14:40:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 250c12b6-85da-3d22-9a3d-ff735a3106d1 | -13.1074 | -57.1511 | 2025-08-14 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 71.8 |
| e183dc64-2877-3d01-8966-39b990ef0d10 | -7.2375 | -57.6342 | 2025-08-14 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 52850570-c49f-32ff-8cc9-7e60fec156f6 | -7.256 | -57.6333 | 2025-08-14 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 436397bd-790e-327a-ba1c-5e8ddc75520a | -6.6576 | -58.8274 | 2025-08-14 14:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 7994ecd5-a392-3ffb-aac9-512f7df74611 | -7.6287 | -63.5154 | 2025-08-14 14:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 43ca23b4-f8c1-3c1f-a009-2d697cf4aa48 | -7.2559 | -57.6529 | 2025-08-14 14:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 13dd5aa0-6955-35b9-b381-4f1b4ba66aed | -7.6286 | -63.5342 | 2025-08-14 14:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 57671fa8-455e-3a13-b86c-16e56ace5470 | -8.1213 | -61.2061 | 2025-08-14 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 113.1 |
| d7881389-dd3c-3dc9-8627-7684f147d111 | -7.5918 | -63.5166 | 2025-08-14 14:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 67186ec9-b20e-3e99-8d86-fd518c912ca7 | -7.8775 | -61.8063 | 2025-08-14 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 4d946c2b-7ac3-324d-8fb1-2795e6027253 | -7.8774 | -61.8253 | 2025-08-14 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 99.7 |
| d7e91bf9-3620-35f8-b2ee-eb9c53e2329c | -7.9305 | -46.8569 | 2025-08-14 14:40:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 143.0 |
| 298f9be4-fbc9-3db0-80bd-81bc639ec164 | -7.4605 | -60.4114 | 2025-08-14 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 35318d46-9733-3fd8-b142-2fdbb93de9f4 | -7.6103 | -63.516 | 2025-08-14 14:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 193.7 |


