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
| dbfd8e9a-9b5d-3e2c-ba3a-f81efd452369 | -4.1688 | -44.111401 | 2024-10-28 00:49:20 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9c34cfb3-8015-36ff-8ae0-a9c8f6bfa13a | -4.5628 | -45.785702 | 2024-10-28 00:49:20 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e86f9eca-a240-351a-a4f6-fdf77136e9e5 | -4.5647 | -45.7939 | 2024-10-28 00:49:20 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c0053840-7869-38de-9e5d-e632c479b137 | -4.5666 | -45.802101 | 2024-10-28 00:49:20 | METOP-C | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 72337c07-15fe-3574-b44f-d0e0cb681f5d | -4.553 | -45.787899 | 2024-10-28 00:49:20 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ed0a15a2-0408-3992-b071-4f3e4886c4f4 | -4.5549 | -45.796101 | 2024-10-28 00:49:20 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4edbde58-eb6d-33b5-94dd-6084b7d1b433 | -3.1646 | -46.602402 | 2024-10-28 00:49:20 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 24d16c13-4a63-30ba-915e-53e73fb20113 | -4.5542 | -45.925301 | 2024-10-28 00:49:21 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 81115c59-9e61-339f-8d05-1e8e466043b0 | -4.5561 | -45.933399 | 2024-10-28 00:49:21 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c36cf908-034e-36e9-af99-e2ff16d71e62 | -4.558 | -45.941502 | 2024-10-28 00:49:21 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3fe19ce6-f4db-3142-b1f0-4bdaf22d2f15 | -4.4827 | -45.6642 | 2024-10-28 00:49:21 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3ad46a5b-3d18-3d7e-a852-822c10f0d796 | -4.4847 | -45.6726 | 2024-10-28 00:49:21 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4456f45e-3b77-3721-96e4-32a64df4350c | -4.5444 | -45.927502 | 2024-10-28 00:49:21 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c9cb1da7-4fa7-3616-93bf-ec4c16ef2000 | -4.5463 | -45.935699 | 2024-10-28 00:49:21 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c6dc43cf-c0c8-3979-9f3d-5748f60e8e7e | -4.7467 | -46.795399 | 2024-10-28 00:49:21 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bf91bad1-038f-32a9-9251-7f2fcd5983a3 | -4.7369 | -46.7976 | 2024-10-28 00:49:21 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6e4958a9-9679-3c84-8c3a-ccb880771735 | -4.2826 | -45.514301 | 2024-10-28 00:49:24 | METOP-C | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 46e39b7a-3c8e-3d02-a2a7-dd915a6dce5c | -4.2846 | -45.5229 | 2024-10-28 00:49:24 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f71c0643-b8cd-35f9-b7de-106c2a749b80 | -4.2866 | -45.531399 | 2024-10-28 00:49:24 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ece73a9a-5f01-3a07-a085-a1ea16c52408 | -4.2886 | -45.539902 | 2024-10-28 00:49:24 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 623410e7-c9d0-35f8-bd03-08daa7724ed1 | -4.2748 | -45.525101 | 2024-10-28 00:49:24 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cc11683e-a43c-3ce0-a740-35b4d4bb6919 | -4.2768 | -45.5336 | 2024-10-28 00:49:24 | METOP-C | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bbaaae0e-39a1-3f6f-bb08-afeabae59a5e | -4.3319 | -45.769001 | 2024-10-28 00:49:24 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3bd6eeba-d2d7-38a6-a4a5-75481cbbd495 | -4.3339 | -45.777302 | 2024-10-28 00:49:24 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f98baa06-5b92-32fc-9141-5852f0163eac | -4.3358 | -45.785599 | 2024-10-28 00:49:24 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0de27aa7-c5c8-381f-9961-9a6ae49cc33e | -4.3221 | -45.771301 | 2024-10-28 00:49:24 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4ba112fc-4346-3d0e-b50e-7bc9f8898638 | -4.3241 | -45.779499 | 2024-10-28 00:49:24 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| fde1f867-a515-31fe-8ef0-a7f6a4091809 | -4.3219 | -45.8582 | 2024-10-28 00:49:24 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8576acb3-d11a-367f-93b4-56a99fb68b78 | -4.3238 | -45.866402 | 2024-10-28 00:49:24 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eb8566de-69fc-3f06-a950-33bfe580df7c | -2.7459 | -45.999599 | 2024-10-28 00:49:24 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b5684565-6c95-3830-b01c-912fd72f460d | -3.6621 | -50.152802 | 2024-10-28 00:49:25 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c642d382-c3e4-3501-8bc9-0548589f6c1d | -3.6507 | -50.147999 | 2024-10-28 00:49:25 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 946b7120-918a-39e3-86b6-ce5ae7cfea64 | -3.6523 | -50.154999 | 2024-10-28 00:49:25 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3d481ef-0935-357e-b964-be198af68a23 | -3.6711 | -50.282799 | 2024-10-28 00:49:25 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85b8398a-a2b8-3075-b789-6ac3ce950cc2 | -3.6727 | -50.289799 | 2024-10-28 00:49:25 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d98be46c-08aa-353f-8e43-bd467e39469f | -3.6743 | -50.296799 | 2024-10-28 00:49:25 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc323b91-f36f-389f-8cb2-6df6fe1e0d1a | -3.6245 | -50.168598 | 2024-10-28 00:49:25 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1caa0543-f6f2-34dc-8e60-2df5c75d05b9 | -3.6261 | -50.175499 | 2024-10-28 00:49:25 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45392ccc-3569-3df6-8cc9-abc7c68a746f | -3.4989 | -49.934601 | 2024-10-28 00:49:27 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a8be58a-e81a-3846-aa77-1a936c298f9c | -3.5005 | -49.941399 | 2024-10-28 00:49:27 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3716db71-5341-3f0d-aacb-193d5c03eac2 | -2.6126 | -46.135399 | 2024-10-28 00:49:27 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ccb59b3f-3c69-350e-9c1a-c632ad55aca7 | -2.7298 | -46.684601 | 2024-10-28 00:49:27 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8541d8f-142c-3d6a-8075-ade2ba8d800b | -2.5462 | -45.982899 | 2024-10-28 00:49:27 | METOP-C | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9959d1e4-0c35-35a0-b0b7-c1838be4d9c5 | -3.8566 | -51.6898 | 2024-10-28 00:49:27 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6810e528-d59b-37e8-94c6-11070d90b91d | -3.8584 | -51.697498 | 2024-10-28 00:49:27 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a3f1d8e-b5f3-3cf9-8699-fbc65432c052 | -3.9606 | -52.195599 | 2024-10-28 00:49:27 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b50cc3c1-e00f-37e5-9eef-23ca96899aa5 | -3.9625 | -52.2038 | 2024-10-28 00:49:27 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bdcb177-d8ae-3d1e-9b74-fad9d9308c55 | -3.9305 | -52.1077 | 2024-10-28 00:49:28 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4475edd4-48e0-3083-be03-d680ea43dcd8 | -3.9323 | -52.115898 | 2024-10-28 00:49:28 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3d9b5f6c-e362-3c76-90f7-3beca5c8da2a | -3.5062 | -50.282799 | 2024-10-28 00:49:28 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48c771e9-1a6b-3fd4-ba25-9fc103ce5715 | -3.5078 | -50.289799 | 2024-10-28 00:49:28 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46e79211-c64d-332a-ab1f-f67e2b5552b2 | -3.9225 | -52.118099 | 2024-10-28 00:49:28 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b6ae11c-6e24-3a25-9a68-97ab02ad951f | -3.1088 | -48.592602 | 2024-10-28 00:49:28 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fb5597d-d254-35d8-8fdc-9178e4e9e503 | -3.1103 | -48.599499 | 2024-10-28 00:49:28 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afb20233-b7df-37f2-808c-d51ed5ff4894 | -3.1119 | -48.6063 | 2024-10-28 00:49:28 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a660682d-2f1d-3899-b026-60c94d27e26c | -4.2011 | -53.448898 | 2024-10-28 00:49:28 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b056b825-2fb1-349f-836f-3081fd819854 | -4.2033 | -53.458599 | 2024-10-28 00:49:28 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5512b22-6793-3c4b-86e5-b29988a2ef77 | -4.1381 | -46.397202 | 2024-10-28 00:49:29 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5cb4e90f-9398-3cf7-9d6b-5475e51ad700 | -4.1399 | -46.404999 | 2024-10-28 00:49:29 | METOP-C | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 114e175f-6844-3eea-b506-c65459d4a831 | -3.2632 | -49.490398 | 2024-10-28 00:49:29 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d2d8c58-d287-38e7-9b08-5bf5f02bfadb | -3.4362 | -50.247002 | 2024-10-28 00:49:29 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ba07623-25e6-32ae-b02b-9c4bd77fec2f | -3.3293 | -49.914398 | 2024-10-28 00:49:29 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29a4021d-c9a5-3fc1-ae2f-b269273ed68d | -3.3309 | -49.921299 | 2024-10-28 00:49:29 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6932254-ab9a-3f01-adb2-a3a08e056858 | -3.6925 | -51.555801 | 2024-10-28 00:49:29 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 503d6637-bbf0-3e3c-ae0c-d22a60d45b96 | -3.3377 | -50.086498 | 2024-10-28 00:49:30 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e177c92-6f6c-319a-817f-983ca22bd18a | -3.1377 | -49.167702 | 2024-10-28 00:49:30 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a1a2c73-cc93-3a19-a4a9-cb5a3d06b9f3 | -3.1393 | -49.1745 | 2024-10-28 00:49:30 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54bee4c7-c4f5-3f71-8429-1cf4b20c23f4 | -3.1409 | -49.181301 | 2024-10-28 00:49:30 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5079d98e-c566-388f-945f-78618d107cd1 | -3.6809 | -51.550301 | 2024-10-28 00:49:30 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3b7f068-ff2c-3ff2-925c-61ac58ab6bac | -3.6826 | -51.557999 | 2024-10-28 00:49:30 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96b7a14c-8aaa-320c-ba45-b7e6027a57fe | -3.6844 | -51.565601 | 2024-10-28 00:49:30 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9837ebca-7a88-3d6f-9d6d-b0506487c684 | -3.7692 | -51.940399 | 2024-10-28 00:49:30 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26731101-e861-326b-8105-8620d6f086e0 | -3.3393 | -50.093498 | 2024-10-28 00:49:30 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54adb343-0114-3f19-83ed-36ee534c6c83 | -2.973 | -48.630299 | 2024-10-28 00:49:30 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ffcf3929-5b16-3c5e-8b23-0020c2f3431a | -3.6934 | -51.8325 | 2024-10-28 00:49:30 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43988b7c-39a1-3887-b65a-2554a7843899 | -3.2697 | -50.0145 | 2024-10-28 00:49:31 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56f65f02-b754-3a98-bcc9-248c7c547ea8 | -3.2713 | -50.0214 | 2024-10-28 00:49:31 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7f8f532-fa8d-39b8-b60e-1baf253ffab7 | -4.0369 | -53.403801 | 2024-10-28 00:49:31 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7af76e8a-1ac3-3302-9edb-e999c25faea1 | -4.0391 | -53.4133 | 2024-10-28 00:49:31 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 996ea18b-97a0-3fe4-9d28-7fe6430cf5f2 | -2.358 | -46.193199 | 2024-10-28 00:49:31 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5becb0a9-e179-3ea7-856f-a376b5fbc9b2 | -4.0939 | -53.933601 | 2024-10-28 00:49:32 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| deab850b-3167-367d-a7ba-ba8bbe509fae | -4.0962 | -53.943901 | 2024-10-28 00:49:32 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17cfd11d-285f-37df-86ed-03a9ead5cc82 | -2.2955 | -46.102001 | 2024-10-28 00:49:32 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 74987f83-c1d7-3b8a-b6e2-08375a6a04c3 | -2.2974 | -46.110401 | 2024-10-28 00:49:32 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 12339b91-c1f0-37c2-b9de-8a2b1ea5af57 | -2.2994 | -46.118801 | 2024-10-28 00:49:32 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1d53e900-01cb-3207-92f1-a094b39f49ba | -2.2877 | -46.112598 | 2024-10-28 00:49:32 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c7e61f94-27fb-3bbb-9512-33d7b7ff33ea | -2.3339 | -46.311501 | 2024-10-28 00:49:32 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 37ec6a37-d5bd-3aea-9b93-cdee2f0760b4 | -2.3358 | -46.319698 | 2024-10-28 00:49:32 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ba44d281-35fc-39cf-b440-9cd527e4b1d5 | -3.2212 | -50.163399 | 2024-10-28 00:49:32 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b696c62-0a1a-3423-be79-082ca7aeb922 | -3.2228 | -50.1703 | 2024-10-28 00:49:32 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9519e79f-b745-3df8-a265-f39ab77571ee | -3.2244 | -50.1772 | 2024-10-28 00:49:32 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f8ab2c2a-001f-3f32-8c6d-f8f00ee81b40 | -2.4134 | -46.698601 | 2024-10-28 00:49:32 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| add5fbc9-b29b-3fde-9011-0ace2d534f7d | -2.4152 | -46.706402 | 2024-10-28 00:49:32 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 333bd90d-e79c-3491-8d75-0b627b1abd30 | -2.417 | -46.714298 | 2024-10-28 00:49:32 | METOP-C | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14a10b45-cb97-3600-bc50-1f34af12b695 | -2.5563 | -47.315601 | 2024-10-28 00:49:32 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5656754c-579e-352e-9a51-5437d68bdc10 | -2.8144 | -48.4342 | 2024-10-28 00:49:32 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a53d541e-2399-3237-974f-c2bce9c76b34 | -2.8159 | -48.441101 | 2024-10-28 00:49:32 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9fbce32-e556-3e53-9264-02809121c245 | -3.0545 | -49.479801 | 2024-10-28 00:49:32 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 799d75f9-78b8-34f1-a949-308f46f8cf0e | -3.0561 | -49.486599 | 2024-10-28 00:49:32 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c8e3984-bf86-3944-be0f-4f3d94a04346 | -3.0576 | -49.493401 | 2024-10-28 00:49:32 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README8.md)
