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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f97dddc-2d57-348f-bc13-eeceb062bdb4 | -12.6143 | -46.9047 | 2025-08-16 14:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 122.3 |
| ed3a74e7-254b-3a55-98ff-844fd5a3a887 | -6.5641 | -43.0122 | 2025-08-16 14:20:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 85590844-9901-3739-ac41-fe4695d70360 | -7.9439 | -63.2225 | 2025-08-16 14:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 114.5 |
| 114f6109-56e7-386a-bdb4-75433a891ffd | -13.1077 | -57.131 | 2025-08-16 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 6280065a-d1cc-371e-b0ee-ad533eed5f00 | -14.9628 | -54.7351 | 2025-08-16 14:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 82c74d61-7f1f-3333-b564-d785ee326e24 | -13.1267 | -57.1293 | 2025-08-16 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 5ad60631-923f-3811-bb2a-28f335a6f36d | -8.9708 | -61.7033 | 2025-08-16 14:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 08b0182a-77f1-3201-84bd-ff802a751cfc | -12.6139 | -46.9273 | 2025-08-16 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 137.7 |
| db7ae68e-36f9-37e9-b4e8-b5dcc643d1a8 | -7.9624 | -63.2218 | 2025-08-16 14:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 188.9 |
| 2254c8c5-ba3c-310c-9ccb-b188d6c3c59b | -7.6296 | -63.3273 | 2025-08-16 14:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 019e346b-4c32-365c-822c-d50e3c9ac08c | -13.127 | -57.1092 | 2025-08-16 14:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 4b09ee31-ec5a-3bc3-bdb5-71f42608aeaa | -7.9625 | -63.203 | 2025-08-16 14:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 3417f0d4-4ea7-3b30-9810-76f3e40e86eb | -6.5638 | -43.0357 | 2025-08-16 14:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 5a6864b6-870b-3577-ab33-c6d1a201fec0 | -8.9893 | -61.7024 | 2025-08-16 14:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 207.1 |
| 5f5df969-fad3-30ba-a630-a4bc0d5110fb | -7.6112 | -63.328 | 2025-08-16 14:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 6e9c6e40-dfae-3fe7-ae47-28de58c8732b | -8.4572 | -64.051 | 2025-08-16 14:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| a470db33-2bba-3b61-8229-617fecab8e39 | -13.4577 | -47.071 | 2025-08-16 14:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 0b1bde07-7f7c-3484-b103-2581a0e4d406 | -15.199 | -51.1527 | 2025-08-16 14:30:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 9ec9804e-d103-39b4-aa83-53d6ce4fe16f | -8.9709 | -61.6842 | 2025-08-16 14:30:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 139.5 |
| be59d128-332b-3d9c-af97-42b92dcdbecb | -7.9623 | -63.2407 | 2025-08-16 14:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 219.9 |
| be9a488c-99e2-378f-b9c4-d031280cd782 | -15.1796 | -51.1555 | 2025-08-16 14:30:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 2496864a-b700-317c-9646-78662aac7e03 | -9.6906 | -46.2735 | 2025-08-16 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| fb68334a-cf52-3f04-96cf-0aa9948829e3 | -12.6259 | -45.2373 | 2025-08-16 14:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 8a3772fc-9c90-3528-8a74-1b6bc8206f79 | -12.5947 | -46.9301 | 2025-08-16 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 77f2e001-7840-3ba6-8168-f0e023777a76 | -6.5641 | -43.0122 | 2025-08-16 14:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| d5ceccd1-67fe-3c90-ac5c-ca58c3e0f3dd | -7.3891 | -44.9046 | 2025-08-16 14:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| f39bed8e-d9be-3a63-853d-9bc2f68681fb | -14.9825 | -54.712 | 2025-08-16 14:30:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 361.6 |
| 9caef99a-1874-3593-b586-1d110620d13d | -8.0875 | -55.5513 | 2025-08-16 14:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| e802f2c6-1744-377e-8e95-a5fdbda6d935 | -12.6143 | -46.9047 | 2025-08-16 14:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 6f07268f-ec6d-3ced-965c-b77f4218f98e | -14.9822 | -54.7328 | 2025-08-16 14:30:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 670.0 |
| fa708dcb-94e5-3a61-9078-bd46b5ca1956 | -7.6295 | -63.3462 | 2025-08-16 14:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| e7ab1e92-da70-37ea-812a-779d6d5085a8 | -14.9825 | -54.712 | 2025-08-16 14:40:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 208.0 |
| 03dcc594-36af-3cff-b3f4-107f69f81a8f | -15.1796 | -51.1555 | 2025-08-16 14:40:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 8c07e8e1-033c-33c7-99f2-e927502ab9fb | -7.9148 | -61.7478 | 2025-08-16 14:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 6fc7d84d-e81a-3954-a8f9-cae2a7406186 | -6.0978 | -44.6261 | 2025-08-16 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 458e0d8b-0c2f-34c5-a533-8b9df52002cf | -13.127 | -57.1092 | 2025-08-16 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 5cf736a3-09e9-3180-b5b5-ccdb27612248 | -12.6143 | -46.9047 | 2025-08-16 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 9e1dd68b-87fa-3897-8d3a-4f4e0b436f0a | -14.9632 | -54.7143 | 2025-08-16 14:40:00 | GOES-19 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 98.2 |
| e2b92935-64ce-3e0d-a041-44a529534e4e | -7.6295 | -63.3462 | 2025-08-16 14:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 31dcf960-ff5d-3f05-a25c-a994c73cd1e3 | -6.5638 | -43.0357 | 2025-08-16 14:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 8d0cd5c8-dc7d-3f33-81f9-8edf225ac89e | -13.1267 | -57.1293 | 2025-08-16 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 168.0 |
| 9842e660-a564-3e3f-8c1d-e9d4ea519ad9 | -12.8418 | -46.0309 | 2025-08-16 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 36696d20-16d1-3c61-ad4f-76dd064db81b | -6.6045 | -42.7496 | 2025-08-16 14:40:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 94.2 |
| 077792a8-d950-35fc-87c0-01831a10a742 | -15.199 | -51.1527 | 2025-08-16 14:40:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 5897271b-1dff-3a0d-8cca-d2528c790025 | -6.6233 | -42.7479 | 2025-08-16 14:40:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 91.4 |
| 65eb8058-98b2-3e7f-8caa-4c16214da5d2 | -13.1453 | -57.1678 | 2025-08-16 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 2346a837-4e56-3267-ac19-42740babbb69 | -13.4577 | -47.071 | 2025-08-16 14:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 83.1 |
| e0ff00c5-3f98-356b-bfc0-976d4f17ca6c | -7.9623 | -63.2407 | 2025-08-16 14:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 127.6 |
| 049b18f8-34e1-3552-ab2b-43067a585184 | -13.1077 | -57.131 | 2025-08-16 14:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 863df1ac-8652-3f22-adb1-bf07c9b5b35f | -14.9628 | -54.7351 | 2025-08-16 14:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 155.8 |
| b08b63fb-640f-3373-9870-4effde088f46 | -6.6042 | -42.7732 | 2025-08-16 14:40:00 | GOES-19 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 92.3 |
| 1090ced8-486a-384c-b5f3-585b00bb7874 | -7.6296 | -63.3273 | 2025-08-16 14:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 129.5 |
| 2707d777-6d96-34cc-bfe1-bdffaea23b39 | -6.5641 | -43.0122 | 2025-08-16 14:40:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 5fedf80f-77d1-3e23-9114-8b34663c8e29 | -7.6112 | -63.328 | 2025-08-16 14:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 2b4be664-d0f6-3f41-b2d3-99b141afee5d | -7.9624 | -63.2218 | 2025-08-16 14:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 184.3 |
| d4009af9-6c23-37c1-81a5-5729f2bae7b8 | -8.0875 | -55.5513 | 2025-08-16 14:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 9ab7b5e3-cf05-3a09-8284-d9bebd43ee86 | -6.8956 | -59.1462 | 2025-08-16 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 5633f488-66cd-3bab-87b3-b614a5324912 | -14.9822 | -54.7328 | 2025-08-16 14:40:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 425.0 |
| 64f60c38-b32d-344c-a0e6-195386f94709 | -6.0437 | -44.4014 | 2025-08-16 14:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 18059e4e-50e3-3b75-b65a-0e63791a4af9 | -12.6139 | -46.9273 | 2025-08-16 14:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 6bd2fc65-2b2e-3aca-bbe7-dba0d84bf60a | -7.9625 | -63.203 | 2025-08-16 14:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| b28b99e8-2de4-3b30-a52c-c5dc3f130286 | -8.4572 | -64.051 | 2025-08-16 14:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| a65ee14f-f673-3568-997e-9e5908ba3886 | -7.9439 | -63.2225 | 2025-08-16 14:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 108.7 |
| 686c7001-3536-30cc-a858-29e1ce615165 | -6.8771 | -59.147 | 2025-08-16 14:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| b579a02e-fb21-3a00-97e8-6ebbd2828451 | -12.6259 | -45.2373 | 2025-08-16 14:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 7f4865a2-b4a1-3f79-8d01-bd28f6cd830d | -7.4983 | -63.8199 | 2025-08-16 14:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 149.2 |


