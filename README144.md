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

## Dados Diários - Página 144

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80f79797-edfa-381b-b98c-bbf94c03f92c | -14.4255 | -46.115 | 2025-10-02 11:40:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 72db0ceb-4764-3285-ae79-1236ab56643e | -12.9507 | -46.3789 | 2025-10-02 11:40:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 6481a321-8fc1-3ff8-a4bd-613f2e31ac2e | -9.9369 | -43.7422 | 2025-10-02 11:40:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 79.3 |
| 8bbe50a4-0121-32c1-86ac-66eb9f6f82e9 | -7.8879 | -47.3031 | 2025-10-02 11:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| ab5fcb92-f105-37a5-9779-927ee8ea23b0 | -9.4086 | -47.5521 | 2025-10-02 11:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 110.8 |
| c16fc425-5758-3a7d-a8c5-a2a470a9b0be | -12.9507 | -46.3789 | 2025-10-02 11:50:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 2d2499f0-f20a-3605-bc19-3f6633341b4a | -11.2799 | -47.8445 | 2025-10-02 11:50:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 786e4884-15d8-3ef9-9ab8-fc90f4000e8f | -13.9585 | -48.1376 | 2025-10-02 11:50:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 74.2 |
| cac481c7-4f2b-3a63-bb71-0efe5aa6050e | -7.8879 | -47.3031 | 2025-10-02 11:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 8f0389d0-549d-3923-b697-0f03cf5ac11c | -9.08 | -46.7215 | 2025-10-02 11:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| a4d8c75c-3fda-32ca-ad64-cc53b32e1349 | -11.0714 | -47.804 | 2025-10-02 11:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 9d079de1-097d-3a4b-9d0c-8e50fe0df4bb | -14.2121 | -46.1058 | 2025-10-02 11:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 808eb86b-98ae-3310-bc7e-6e9fd6fbcbf0 | -9.4083 | -47.5742 | 2025-10-02 11:50:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| ec893334-ba49-3b0d-bdfe-201a84451ac4 | -11.0897 | -47.846 | 2025-10-02 11:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 35c4a05c-aa97-36ff-8dc6-15f6d7205b04 | -14.1921 | -46.1321 | 2025-10-02 11:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 119.8 |
| b1a74bd7-e56e-3305-872f-b32021faa87b | -14.2116 | -46.1288 | 2025-10-02 11:50:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 84.3 |
| ae14f1bc-9992-319b-9f16-b60efd0090b5 | -14.425 | -46.1381 | 2025-10-02 11:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 81.4 |
| e621d8bb-0a9c-371d-a29c-9e03746a86a6 | -14.4757 | -48.4137 | 2025-10-02 11:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 8ad75945-610c-3215-ad1b-59a91969d69c | -9.9178 | -43.7447 | 2025-10-02 11:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 90.1 |
| 5a264983-a7f3-3985-a642-99a36d078c47 | -13.0119 | -45.1988 | 2025-10-02 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 5b0b250c-9cc2-3641-8845-16bb85768ace | -11.9276 | -47.8719 | 2025-10-02 11:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 74b316f2-e504-3334-9594-78d687c61c55 | -9.9372 | -43.7187 | 2025-10-02 11:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 73.6 |
| 2880ff9f-3866-39d5-895e-cef9028c125e | -9.9369 | -43.7422 | 2025-10-02 11:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| 4dba2d31-4bbb-350b-a61a-7d80bf44ae3b | -11.8234 | -45.0364 | 2025-10-02 11:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 1c74f24a-19b1-338a-a514-c3552f724256 | -7.8882 | -47.281 | 2025-10-02 11:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 00c6e131-68b4-3a14-85b6-865e6e70069b | -13.0114 | -45.222 | 2025-10-02 11:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 288da261-08d8-369d-ae4f-1ed117f96ef4 | -13.1542 | -47.8568 | 2025-10-02 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| c0791d24-281b-324f-88a5-0fd8017a24dc | -11.9085 | -47.8745 | 2025-10-02 11:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| fde6ce95-b2d7-3f9f-9d2e-63761b8b74b4 | -14.1921 | -46.1321 | 2025-10-02 12:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 6db47d88-c73d-3beb-8dbd-8fd4ccdb9112 | -14.4757 | -48.4137 | 2025-10-02 12:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 8c2184ae-9e17-3a54-9e10-6fa42ea0b4aa | -9.0803 | -46.6992 | 2025-10-02 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| c4488410-72c7-35d1-b0b5-30fe4c0e1426 | -12.9507 | -46.3789 | 2025-10-02 12:00:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 048728e0-b4ca-3f5e-9553-90cc925b272d | -9.9372 | -43.7187 | 2025-10-02 12:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 97.3 |
| 82e85e63-2744-3734-a040-6260f13d15e7 | -14.4753 | -48.436 | 2025-10-02 12:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 72.0 |
| bf1e5098-1409-32b6-ac76-449c310d8c79 | -15.2542 | -49.3104 | 2025-10-02 12:00:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 92f909a4-b7cf-3b17-9ea5-7e09626ad9a8 | -13.0114 | -45.222 | 2025-10-02 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 56ee214f-2191-308a-b9f6-7b7c8e8eb185 | -14.6985 | -45.1858 | 2025-10-02 12:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 623491e0-4f4b-3c32-9c83-a813580b373e | -11.8234 | -45.0364 | 2025-10-02 12:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 3968ff59-5a73-30df-bb8d-ed6a91633fa1 | -9.9178 | -43.7447 | 2025-10-02 12:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 240.6 |
| c1f5dd05-0d88-3100-8c30-953374c2fcb4 | -11.9276 | -47.8719 | 2025-10-02 12:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 111.5 |
| 5b386178-acad-3574-8a31-73183d70cc14 | -14.3119 | -45.9736 | 2025-10-02 12:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 788b8dcb-eb67-33bd-82cd-dce84c321a45 | -9.9369 | -43.7422 | 2025-10-02 12:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 151.1 |
| 5515b4c0-0e4a-3682-96ad-96b4b0316ce7 | -9.08 | -46.7215 | 2025-10-02 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 167.9 |
| 5d518926-9e7e-3cd0-88ef-b8c3a509191d | -11.8238 | -45.0132 | 2025-10-02 12:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| e94c708e-0aa0-3751-8ff5-0f1f295a247e | -11.2799 | -47.8445 | 2025-10-02 12:00:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 126.0 |
| efe16c3f-38f2-3f5e-a05c-fe8b6e405575 | -13.1542 | -47.8568 | 2025-10-02 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 6dce8f6c-b5ef-300d-924f-063a1cd3e4f5 | -9.4086 | -47.5521 | 2025-10-02 12:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 7d91ba82-42ae-355c-b177-713e2d529cb8 | -9.4272 | -47.5722 | 2025-10-02 12:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 5da46306-e0d7-346e-a87d-2c529750d53f | -13.0119 | -45.1988 | 2025-10-02 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| b13ad5b0-5269-3791-acf7-d7cac1effd30 | -11.2803 | -47.8223 | 2025-10-02 12:00:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 621475fd-ab2e-3d98-b108-3c3171df68a3 | -14.9074 | -47.242 | 2025-10-02 12:00:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 04441528-0a40-33cc-92c4-3318dc59e20a | -11.0897 | -47.846 | 2025-10-02 12:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 9d13182d-95f5-3005-aeb8-e3c314685e28 | -10.8433 | -45.3815 | 2025-10-02 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 9855d866-50af-3181-bb80-b8dd33d0c998 | -14.425 | -46.1381 | 2025-10-02 12:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 88.8 |
| fe313041-2316-3066-ab77-60e7769e05dd | -15.3185 | -46.278 | 2025-10-02 12:00:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 71.4 |
| d90eebf5-18a3-3f56-a597-0dd5dfe9f35d | -9.4083 | -47.5742 | 2025-10-02 12:00:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 125.3 |
| afbe8a81-e638-380e-9109-6f0796fcc667 | -9.9182 | -43.7212 | 2025-10-02 12:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 120.9 |
| 88528673-c609-3af0-a64e-3d573b3dff1c | -11.9085 | -47.8745 | 2025-10-02 12:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 80381049-b275-3a3e-b9cd-e73efecb5fc1 | -13.3014 | -47.1852 | 2025-10-02 12:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 65.3 |
| b8a325f8-2c4c-3738-bb0b-5f4d03dc9192 | -13.0114 | -45.222 | 2025-10-02 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 160.5 |
| e3ae3f27-2344-3cb6-9c01-e69a93c8cdcf | -14.4757 | -48.4137 | 2025-10-02 12:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 108.4 |
| f91cebd3-c9b6-3e04-bcbe-c5916dc0bb19 | -11.2799 | -47.8445 | 2025-10-02 12:10:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| d3b621fc-ab5c-3c5e-866f-3a131cd58b52 | -8.5204 | -47.8167 | 2025-10-02 12:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 53bef08f-ae8d-3534-8af6-847a67030e10 | -14.4753 | -48.436 | 2025-10-02 12:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 66.4 |
| f69bbe97-bb48-3ab3-b373-ed549ba180db | -14.425 | -46.1381 | 2025-10-02 12:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 99.0 |
| a9633a05-123a-3aeb-ab12-8be03e8eb811 | -13.1743 | -47.8093 | 2025-10-02 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 721b97a3-4a7d-3109-8aad-02d61b83ef88 | -14.3704 | -45.9634 | 2025-10-02 12:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 8bec566a-67b4-37c7-aafc-ac8fcb68abf7 | -9.08 | -46.7215 | 2025-10-02 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 10198f65-3fdf-3044-8407-d5c7e0fa0c7f | -13.1542 | -47.8568 | 2025-10-02 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| ea1075b3-f384-36d0-a2c1-e7deb1533bea | -14.3709 | -45.9403 | 2025-10-02 12:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 23afe961-862e-391e-a194-e2bebda0e568 | -14.4947 | -48.4329 | 2025-10-02 12:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 19182e54-ad70-3cf8-aae3-4d2c92a2452a | -8.7519 | -47.3322 | 2025-10-02 12:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 3469aebb-0769-3f33-8e05-dd103a800fe2 | -9.4083 | -47.5742 | 2025-10-02 12:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 152.3 |
| 9859b254-d934-30a3-ab4c-fb57029f2954 | -15.3185 | -46.278 | 2025-10-02 12:10:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 99.6 |
| 7d6c4513-c2a7-3303-a78e-e5c9f57ef7f2 | -9.9182 | -43.7212 | 2025-10-02 12:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 105.1 |
| d98d6869-6315-3834-a543-ee3b07386155 | -11.8234 | -45.0364 | 2025-10-02 12:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 0475d44d-7dd9-30ee-a78d-7223d0fd4b07 | -8.9115 | -46.6276 | 2025-10-02 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| e12fd91e-e385-3335-bdf1-745829d5256f | -14.4255 | -46.115 | 2025-10-02 12:10:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 88.8 |
| e518d753-f14b-32a8-9bdd-e788ff19454f | -9.9372 | -43.7187 | 2025-10-02 12:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 93.8 |
| 5c4cb8da-f453-38b0-a9ae-52c89220a3ea | -14.1917 | -46.1552 | 2025-10-02 12:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 168.7 |
| 6bc8ca07-b682-3614-a589-e1f39532caff | -9.4272 | -47.5722 | 2025-10-02 12:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 332ddcb2-101e-35cd-a89e-46d3e8281dc4 | -14.8212 | -45.8143 | 2025-10-02 12:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 83.5 |
| dacf5611-8082-3cd9-be4c-7045f494eddd | -13.0119 | -45.1988 | 2025-10-02 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| a964365e-9ff1-3f12-bb6b-663b4a737bd7 | -10.8433 | -45.3815 | 2025-10-02 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.4 |
| b816d1c6-213f-35c7-bf10-00f86b28657e | -11.9085 | -47.8745 | 2025-10-02 12:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 161.8 |
| 514141e2-0a06-39cd-8d5e-2eee896d8340 | -14.1921 | -46.1321 | 2025-10-02 12:10:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 114.7 |
| 1028f8b7-88b2-36e0-a3b0-b86f130c6efd | -11.9272 | -47.8941 | 2025-10-02 12:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 718b7033-a414-30f8-afc0-52bd80911ab2 | -11.8238 | -45.0132 | 2025-10-02 12:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 04f1e426-a8d9-3672-92ff-6c364bc6dbab | -10.3061 | -48.2461 | 2025-10-02 12:10:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 8f3385a0-2a71-3a8a-acc6-482f6fc23b9a | -11.0897 | -47.846 | 2025-10-02 12:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 4c24f182-b070-3fe5-b4aa-0c63fb6a54d2 | -11.9276 | -47.8719 | 2025-10-02 12:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 478.6 |
| 55daff35-27a3-3586-aadb-3fba41967786 | -13.3131 | -47.5876 | 2025-10-02 12:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 971b057c-6e6a-3053-8899-099138a154a4 | -9.9369 | -43.7422 | 2025-10-02 12:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 127.7 |
| 9f131791-0516-303c-9fa7-29e99194e6e1 | -9.4086 | -47.5521 | 2025-10-02 12:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 149.5 |
| dcd234a8-7a8f-3939-8127-0dd4e78041a1 | -12.9507 | -46.3789 | 2025-10-02 12:10:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 71.4 |
| dae23e5d-3543-3a8d-b8ed-83490fffa452 | -9.9178 | -43.7447 | 2025-10-02 12:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 162.6 |
| e291542b-2e06-3fa4-bfa6-da8e335956e7 | -8.5201 | -47.8386 | 2025-10-02 12:10:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| a87f23ec-4c80-37da-957c-d289f765921e | -11.1746 | -47.2805 | 2025-10-02 12:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 219138b8-13f8-3bc0-9290-874c7d5c3b07 | -16.0567 | -45.7204 | 2025-10-02 12:10:00 | GOES-19 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 191.5 |
| 713c1e33-6093-363d-97d7-32a6e182f08a | -15.2542 | -49.3104 | 2025-10-02 12:10:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 77.5 |


[Clique aqui para ver as próximas entradas](README145.md)
