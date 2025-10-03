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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77c0ec0d-0708-3ee8-b242-31742bd6ebd0 | -11.06827 | -47.80614 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d1f2764-05e0-3498-909b-26087c38251c | -14.11607 | -44.31025 | 2025-10-03 04:12:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8262b363-d943-388a-bd08-9063ac6291ed | -10.96636 | -51.09807 | 2025-10-03 04:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ffccbf69-86ff-326b-9f37-12cc1372e244 | -15.17617 | -43.628 | 2025-10-03 04:12:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 788f6ec4-ddab-3446-b972-3b7bef4f05fd | -13.25946 | -47.25797 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 1ccf1d66-e22c-3946-b5e2-38533e38e5d3 | -10.30526 | -48.28477 | 2025-10-03 04:12:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ed210b8e-e1e3-328d-ac1b-d942ce3b84cb | -9.95199 | -43.65425 | 2025-10-03 04:12:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e061efe7-7ad1-3c35-8c52-8a0df644c6d4 | -9.9608 | -48.77616 | 2025-10-03 04:12:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b91eed0f-e21b-3979-bf02-f25afccacef3 | -11.55166 | -47.66277 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 85e10f38-d2a1-3006-a85e-cd92575537d9 | -13.33579 | -47.79306 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a96edfa-2c97-36f2-8aaf-a8d2ccc0cf9f | -9.95237 | -43.68048 | 2025-10-03 04:12:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83a2e262-b725-33a6-af12-bcf77c10146a | -11.32424 | -49.01782 | 2025-10-03 04:12:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b30416de-b040-309f-b06e-e5589454ea5c | -9.92314 | -43.76891 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0a306a55-642a-304a-8e26-c29d088d4645 | -13.20431 | -47.87944 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11f65832-e471-3534-a214-7e1442530402 | -10.21557 | -50.32135 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3ea15e54-5a04-3c4f-945d-479b91576cc2 | -13.37456 | -47.27901 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7a557b4c-b4c9-3a21-81b1-6bd9a4b850ee | -14.56944 | -48.33327 | 2025-10-03 04:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0fb575a7-1aef-3c85-8760-04f2e329e1fa | -13.95744 | -48.0934 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 936e9fe2-d735-3bec-bf4a-deefa5534ba8 | -14.30609 | -46.01727 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5594db66-9c3c-3e4b-9377-739926cabf27 | -12.68291 | -46.85291 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7aa13666-f80e-312c-b454-768a25a70086 | -13.9785 | -48.12576 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fb6b2574-e2c1-3a4b-b639-f5d3e677f8b3 | -14.21745 | -44.95057 | 2025-10-03 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62efa6ac-358c-3544-9185-c262e71e2f13 | -11.4211 | -42.11163 | 2025-10-03 04:12:00 | NPP-375D | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 22fa65b4-ae11-3b1e-bc50-3cf3433d74a1 | -12.22381 | -43.76629 | 2025-10-03 04:12:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a49a4b3-853e-3b97-ba6e-d51e5ba0ee1b | -11.6265 | -47.99078 | 2025-10-03 04:12:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bac33d52-f819-34ef-99e8-7721f0ba43cb | -10.86043 | -45.40987 | 2025-10-03 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c5a8414-99e9-3f93-a5b5-fae413a3afa8 | -9.90813 | -43.73272 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2e323549-d5b5-3d8c-8d16-c572859ebff3 | -8.86744 | -47.67354 | 2025-10-03 04:12:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b53e226-6d83-39d9-a13e-4e360dca97e2 | -9.95705 | -48.777 | 2025-10-03 04:12:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f02dbd2c-3a5b-3bf5-b926-02f288f9da16 | -11.06546 | -47.79819 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c707fd0-60e2-3fb9-9ed7-1783469e0494 | -13.67007 | -47.8799 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 895f6d92-018e-32c4-b6db-89fc8e8bf173 | -11.84884 | -44.96526 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a3d7a5fe-85d5-37f3-9e4c-41f05fe85efb | -14.6858 | -45.18452 | 2025-10-03 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbfeb32f-cc17-3f03-afa8-95f0c38f8ba5 | -13.9453 | -48.13932 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 71d80cf6-3955-3064-ab9a-81ac2af73b5b | -9.90254 | -43.72433 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8b4efc3c-8f7c-3d47-8778-7212f7406cb7 | -10.01221 | -50.23654 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f0869c37-04d9-3d0d-b913-f44851055b48 | -9.47747 | -47.87223 | 2025-10-03 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6a98a16c-60ff-3d7d-aaee-3fb55af5f846 | -10.83812 | -41.27604 | 2025-10-03 04:12:00 | NPP-375D | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 320671e9-1129-3735-b0d6-0248beb0b067 | -13.17982 | -47.87974 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ccbf5e65-1efc-3a48-8f34-ac68aeaa1e6d | -13.14854 | -47.89503 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39f3059f-23c5-34f8-9f8f-3d302cc45b6d | -13.9459 | -48.15908 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d8b5b4c-4293-3f05-b151-904f0181b3e3 | -13.52743 | -47.29478 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9ac41121-ef9d-3ad8-9e56-9f9a2c077c8c | -11.4157 | -43.49102 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 964b5615-9569-3ed1-961e-52a49a6f3194 | -13.67718 | -48.63728 | 2025-10-03 04:12:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6366245f-8ee7-3456-867d-5899bef53164 | -11.10266 | -47.81978 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c592706c-0268-383f-8ca3-40e42ae939b0 | -10.34184 | -43.73196 | 2025-10-03 04:12:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c3f3d0a-8b41-3b49-8bbf-bc936b70816a | -13.5368 | -47.28584 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| db706ee5-9045-382b-bc6d-70ecec819ec1 | -10.01322 | -50.23114 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| dff428c0-1509-3a09-8cb0-500af9b86242 | -13.7366 | -48.00148 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bd4ce41c-562e-3a06-8f6e-4d91689dbb76 | -13.30533 | -47.25763 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3c5ed38-f2b3-35da-8a77-d97a6b8126d8 | -11.06142 | -47.79739 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| defd08f9-05bf-3362-b371-c21ad9bd443e | -12.60905 | -49.90519 | 2025-10-03 04:12:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3654de4b-6269-3049-a597-b2e7d71013f9 | -12.66142 | -46.95333 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fd2853ac-1890-35d1-b2d5-4c4a905faa46 | -11.90477 | -46.31839 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 11dd5327-9d14-3102-aa3f-98c5222f6dc8 | -13.12529 | -47.87387 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 18990ada-90c9-3998-98b3-7721295dc2fc | -13.75557 | -48.07942 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d48ecd3c-1d71-3ba5-87f6-03685b73eb52 | -9.95566 | -48.77936 | 2025-10-03 04:12:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cd3931e6-e8f1-3433-84ed-b63643991de0 | -13.3436 | -47.79462 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5496e368-b6ae-387d-b4f4-6ca949df7753 | -13.34797 | -48.10651 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed42de71-2cb9-32fb-ac2e-4a524d43a789 | -12.20434 | -47.7873 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 861556cb-6e8b-3668-9a52-8d8d10c45b07 | -8.71046 | -47.97714 | 2025-10-03 04:12:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fc79f1f-fcff-37d7-b18c-7f1a22470ac6 | -10.29531 | -48.29152 | 2025-10-03 04:12:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b92de56-3507-35f4-819a-0ea793244a6a | -11.5974 | -47.66049 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84c4c92d-1e8e-3259-a9fc-7bfde03baf26 | -8.8681 | -47.66976 | 2025-10-03 04:12:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cad77c0e-8b02-39bd-99aa-31eacfeabcc0 | -13.56463 | -47.58749 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c40d0491-f871-31e6-a7c8-7cb443f77a67 | -9.89534 | -43.70446 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 202a1db2-4a01-3e44-b689-663a958f5b64 | -11.59929 | -47.64973 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d46a26cf-2234-3997-860f-65ad94d05072 | -9.94396 | -43.57501 | 2025-10-03 04:12:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7fd975c0-67b3-37cd-b9a5-df9bf673461c | -14.29964 | -45.88348 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4cf1cf10-eacc-38b1-a6cf-d72f79c2c8a1 | -12.87117 | -46.92599 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a4a52157-a08c-3c16-ada6-7fb1b82834e0 | -13.34701 | -48.11181 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 73168845-d1ef-323c-9f8a-ceb57382a9bf | -10.34591 | -48.17747 | 2025-10-03 04:12:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9edc8e70-119d-3c84-a5de-fdd493c53999 | -11.62478 | -45.03178 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dae6f650-5060-30df-b634-52bba4d91bb1 | -13.1222 | -47.86827 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0dc25271-37c6-3157-86c4-0e40cfe0eb01 | -11.10946 | -43.19006 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1617075f-3cd9-33a8-bb2b-bcbaa5a49f06 | -11.13897 | -43.40584 | 2025-10-03 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bb828eda-eef1-34e0-86fe-f997b50124bb | -11.11656 | -47.85966 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa98e32c-e7d2-38a6-8a00-2450d62788c1 | -12.43437 | -46.4767 | 2025-10-03 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86a01a70-2d4b-354b-afc7-343d1c8bc8b0 | -10.89404 | -56.19983 | 2025-10-03 04:12:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4a8f1054-4393-33d8-9019-4eea4a264e3c | -11.82252 | -44.90958 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fda6d303-4ea1-3e71-9af1-0dcf9dba6cd0 | -10.85896 | -45.40709 | 2025-10-03 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 630f3307-cac0-3f31-ac63-930258b55aaf | -10.93671 | -51.07346 | 2025-10-03 04:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1bee5686-57df-352a-9553-7a4a79fc15ea | -12.60818 | -49.90986 | 2025-10-03 04:12:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b73e8da-87ef-3ff4-979a-c84cb9e5c0cb | -12.38411 | -46.51591 | 2025-10-03 04:12:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a9404b6-7a36-344c-aef7-2986ce050df1 | -12.65317 | -46.95604 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed212811-4c1a-3567-b115-816e7477f2df | -12.80663 | -47.03094 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 25b4d404-dd35-39cf-9f2b-c6d4be1cd697 | -14.24966 | -47.27998 | 2025-10-03 04:12:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 13acedb0-9814-379f-8eb4-75cb98e7f274 | -11.081 | -47.70882 | 2025-10-03 04:12:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cc20df6c-06c3-3b5b-ae36-f4ed07ad1550 | -11.26123 | -47.79676 | 2025-10-03 04:12:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91a03a83-c084-3c9d-94c1-d17f92ffb509 | -13.21496 | -50.89777 | 2025-10-03 04:12:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 71032887-50bd-3656-be0d-54746ede00c7 | -9.93447 | -43.76327 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| eac6f916-9ab1-3d13-afbe-d7a9cd932c75 | -13.12962 | -47.89585 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 27.7 |
| ed4b6fb8-673b-3508-b8aa-aa2529bfd87e | -11.63123 | -47.98785 | 2025-10-03 04:12:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14443df2-ad5d-3e81-ab05-0cff5a24ce27 | -14.10265 | -44.30797 | 2025-10-03 04:12:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b6db7953-ff77-34fd-98e9-1d02bc8dae53 | -11.87258 | -45.03751 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44027574-7f33-3ce6-a60e-9c9054ef467b | -14.41548 | -46.15634 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae4a48dd-ebb4-3211-90a9-aff812594957 | -12.76439 | -44.90485 | 2025-10-03 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 518c2ab1-b846-3559-a99e-b42d25980248 | -10.96386 | -44.33509 | 2025-10-03 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbafbe21-6e9e-3c7e-a151-cd9d82625466 | -11.08878 | -47.8739 | 2025-10-03 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed29b4d4-ad05-3e26-879f-9c88d09042d3 | -13.66509 | -47.30484 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README62.md)
