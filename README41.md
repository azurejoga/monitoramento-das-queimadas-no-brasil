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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f10ff0b-dc1a-3611-995a-2361f7dd5535 | -5.9234 | -41.3056 | 2025-11-08 13:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 84.7 |
| 8be9d729-3c96-32fe-98ea-fcbf62c3852f | -5.9368 | -38.1694 | 2025-11-08 13:00:00 | GOES-19 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 108.6 |
| abb9060d-82c8-3422-b9c7-4aa4336e6352 | -4.0366 | -48.9852 | 2025-11-08 13:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| ca44c6d1-a79a-34f0-8f25-7fd23b9ef646 | -5.9368 | -38.1694 | 2025-11-08 13:10:00 | GOES-19 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 117.4 |
| 6d50320f-1e18-33a8-864a-75291d54183c | -2.4631 | -49.3789 | 2025-11-08 13:20:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 93066761-47b6-34a5-af84-1bb64146c3b6 | -3.4058 | -45.4424 | 2025-11-08 13:20:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 423a0d68-3e15-304e-8a84-a44781840fb5 | -3.2417 | -48.7588 | 2025-11-08 13:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| e0d53d7c-5727-3f9e-b0dd-6efd95fab9c0 | -4.0366 | -48.9852 | 2025-11-08 13:20:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| fd854599-1ff9-30d1-8a5e-90fec0a04c82 | -5.9368 | -38.1694 | 2025-11-08 13:20:00 | GOES-19 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 117.3 |
| 11718331-c5c4-3c67-ab05-9064aa465bf7 | -3.4449 | -48.8373 | 2025-11-08 13:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 2b393e90-2120-3e80-82cc-dd546b2026da | 1.9865 | -55.8198 | 2025-11-08 13:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 482fff25-43a5-363f-a2cf-6a7d9936aaf9 | -5.9368 | -38.1694 | 2025-11-08 13:30:00 | GOES-19 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 124.1 |
| 0dd5e798-3bc3-3c0a-964d-538708b2ece0 | -2.847 | -50.4648 | 2025-11-08 13:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| e52ac977-f774-37da-97d1-af6ab5330718 | -1.2822 | -49.1467 | 2025-11-08 13:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 2c6d8298-dd3a-38b0-9ee0-d33e9b222e02 | -5.6245 | -41.0887 | 2025-11-08 13:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 84.3 |
| 9a8c712f-35fe-31b5-9a99-895484cbb993 | 1.9865 | -55.8198 | 2025-11-08 13:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 97.7 |
| cb96b3b1-979a-3dd2-9337-6ce239860b3e | -2.6113 | -49.2263 | 2025-11-08 13:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 9d50ac8c-3597-3a50-b786-4e607deb334e | -2.9096 | -44.1918 | 2025-11-08 13:40:00 | GOES-19 | ROSÁRIO | MARANHÃO | Brasil | 2109601 | 21 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 4781da08-bdfd-394f-ae3d-27a0930924bb | -5.9368 | -38.1694 | 2025-11-08 13:40:00 | GOES-19 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 147.1 |
| f79923f8-2623-3d31-a299-c6e8115e7081 | -3.4058 | -45.4424 | 2025-11-08 13:40:00 | GOES-19 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 8fbd2c78-da9e-3485-96cf-b23982b84ee9 | -5.9368 | -38.1694 | 2025-11-08 13:50:00 | GOES-19 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 134.3 |
| 8d926c89-b85a-348b-aa12-102b2ca5b6ef | -3.2743 | -49.7788 | 2025-11-08 13:50:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| f8dddcfd-ce33-3c61-af8f-02b06174abff | 1.9865 | -55.8198 | 2025-11-08 13:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 39b44210-461c-3851-bdcb-8200d7c00d15 | -1.2822 | -49.1467 | 2025-11-08 13:50:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 86c6fb47-177f-35e4-8129-88646989b0c1 | -3.3464 | -50.1979 | 2025-11-08 13:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| cbafae89-8eec-38bf-bc15-9715a99213a6 | -3.2928 | -49.7782 | 2025-11-08 13:50:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| 3a9cee5f-5a72-3c19-a64e-cf550d3991ea | -2.7026 | -49.5422 | 2025-11-08 13:50:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 34fbae09-7481-3883-aeb4-59accb39e193 | -2.7211 | -49.5417 | 2025-11-08 14:00:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| b38f1a6d-5f13-348b-ad20-610ef16b2f74 | -5.9368 | -38.1694 | 2025-11-08 14:00:00 | GOES-19 | ERERÊ | CEARÁ | Brasil | 2304277 | 23 | 33 | nan | nan | nan | Caatinga | 154.4 |
| 05cb574f-6b5c-3326-9a8b-0c4a9f9af066 | -3.2928 | -49.7782 | 2025-11-08 14:00:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| f84da34a-aa87-3403-a9d7-85913e875143 | -7.9949 | -37.5423 | 2025-11-08 14:00:00 | GOES-19 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 119.0 |
| 5a2f7c5d-7e24-3543-baa6-707f945af168 | -2.7026 | -49.5422 | 2025-11-08 14:00:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| f3ea540e-32cb-36ad-ab54-d6a67a86ad76 | -11.3453 | -39.8131 | 2025-11-08 14:10:00 | GOES-19 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 114.7 |
| 7a06d8d0-b4ff-3831-8b7d-ac20e8986980 | -3.3464 | -50.1979 | 2025-11-08 14:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 95a7466c-2e1d-332c-ab39-a20252cdb4a2 | -2.7026 | -49.5422 | 2025-11-08 14:10:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| 2973fccf-f60e-3bd6-b4aa-829f422d877d | -1.1901 | -49.084 | 2025-11-08 14:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| b7785a58-06e1-3385-b07f-9ff6085e0030 | -2.7026 | -49.5422 | 2025-11-08 14:20:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 112.1 |
| 2e501450-f827-3079-bee5-11b7af7b9066 | -3.1417 | -50.6027 | 2025-11-08 14:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| de28b00b-0669-377e-89f5-a0c801a8fcc9 | -1.1716 | -49.063 | 2025-11-08 14:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| ba28642a-aaee-32aa-86fd-dfbc1953c9f6 | 0.3957 | -50.9412 | 2025-11-08 14:20:00 | GOES-19 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 2957f77f-1477-36ce-89f4-1a3f77da86c4 | -7.5662 | -45.8625 | 2025-11-08 14:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 9cfa8b36-fda0-33a0-a037-4a9f82e39a87 | -2.7211 | -49.5417 | 2025-11-08 14:20:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 9043b292-80c2-3a2f-aa6b-42208b634df3 | -1.3007 | -49.1464 | 2025-11-08 14:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 7c96647b-ad8c-327d-8ab5-718bf262ad5d | -1.2822 | -49.1467 | 2025-11-08 14:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 25f3a8b2-69f1-304c-8b21-8aa603afdf3c | -2.4631 | -49.3789 | 2025-11-08 14:20:00 | GOES-19 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 5b08ce66-d551-35ec-8d7b-059c084294cd | -1.3007 | -49.1464 | 2025-11-08 14:30:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| df103034-fede-32f6-bb2a-a77b5e7501d5 | -9.9011 | -44.8378 | 2025-11-08 14:30:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| f0e2be3a-ffd2-3c0b-b707-ed114013a53d | -2.7025 | -49.5634 | 2025-11-08 14:30:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| fc90bd41-7847-3dc7-8534-188ead5c5a56 | -2.7026 | -49.5422 | 2025-11-08 14:30:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 118.2 |
| c2d0b44f-fe4a-3cf6-9943-8b7f98313297 | -2.6113 | -49.2263 | 2025-11-08 14:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 0c8650f8-895c-3b79-9e35-58088f8c9f34 | -9.9011 | -44.8378 | 2025-11-08 14:40:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 90.1 |
| b34d034c-328a-383d-8591-7b4849379a3e | -2.7026 | -49.5422 | 2025-11-08 14:40:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 99.5 |
| b75ff804-fb30-37fd-905d-11a6d5b2c0b7 | -1.2822 | -49.1467 | 2025-11-08 14:40:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 8c6ae55e-60ff-3b9a-b39a-d369106b7442 | 1.4916 | -56.0428 | 2025-11-08 14:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 60598b80-5c24-3f3f-ab4e-b4308a0c5c12 | -3.3464 | -50.1979 | 2025-11-08 14:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| d51a66c7-2cb3-32dd-a9b2-dbd7c50d75d1 | -2.7025 | -49.5634 | 2025-11-08 14:40:00 | GOES-19 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |


