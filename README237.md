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

## Dados Diários - Página 237

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1518eca-d900-3770-9903-e264bd6a2e9f | -8.911 | -45.229 | 2026-10-09 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 648bdd8c-80cf-3bda-bf3d-98360aa47129 | -8.9113 | -45.2062 | 2026-10-09 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 116.3 |
| ca65ee52-cb39-3cbc-abe7-e4b86084caa1 | -10.8983 | -45.5114 | 2026-10-09 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 420f4a26-fc72-3f94-a53e-3156d50e6600 | -11.5998 | -43.6226 | 2026-10-09 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| fa58ad4e-9c21-3364-ab11-e9af66db834f | -8.9687 | -45.1542 | 2026-10-09 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 6300e30a-821d-3265-b1d0-240e5a275b09 | -9.0826 | -45.1186 | 2026-10-09 13:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 124.7 |
| ba200428-bf19-3a5e-921f-f9a06e313e50 | -11.6562 | -43.6846 | 2026-10-09 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 697.2 |
| e7072ffd-ef09-3884-91d6-55e8d8c0f946 | -12.2348 | -57.0871 | 2026-10-09 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 122.9 |
| a1fd6b53-e815-3725-bf14-d19dad6592da | -16.1136 | -43.4052 | 2026-10-09 13:00:00 | GOES-19 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 95.1 |
| c05be955-34a0-3726-8c0d-86bf5704a4ef | -11.2068 | -45.3091 | 2026-10-09 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 68dfa04c-36d4-32b7-ac9e-3521088d2f93 | -8.9299 | -45.2269 | 2026-10-09 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 99ab7db1-3d5b-3ecd-b5e6-4cc142dc5e82 | -12.0054 | -43.4878 | 2026-10-09 13:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 273.9 |
| 9ff6a060-9ea4-3a76-9274-0dc1d62e454e | -11.4128 | -46.6897 | 2026-10-09 13:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 7c722eeb-fc4f-3e84-928b-7079f53c833f | -11.075 | -44.0768 | 2026-10-09 13:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 188.5 |
| 88e774e6-f55b-3302-b640-a931c7a46022 | -11.5985 | -43.6935 | 2026-10-09 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 161.3 |
| 0cb160e4-573d-3307-afd3-367c808511d3 | -9.1294 | -45.8405 | 2026-10-09 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 7d32d2d9-5f57-32b7-8cce-e82edfd5c221 | -8.9964 | -45.9002 | 2026-10-09 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 3854c1c1-1c34-394a-8909-6910f2b18390 | -16.6321 | -47.203 | 2026-10-09 13:00:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 62717f21-3d27-38d4-af31-b8e8adb7fd5b | -8.5313 | -46.911 | 2026-10-09 13:00:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 8c350380-2f45-38d4-8791-8d8ae6fae0ed | -10.4901 | -47.3201 | 2026-10-09 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 266.6 |
| 23cd57e0-0dc2-32ce-9e69-25d16f086c96 | -11.8499 | -43.5835 | 2026-10-09 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 262.9 |
| 26a171fc-214e-396c-ad8e-f0e0b9a0360b | -8.3011 | -45.7245 | 2026-10-09 13:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 452cff81-dc3a-3d86-ba65-6b459102597f | -11.5989 | -43.6699 | 2026-10-09 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 92fafc92-a4f0-382c-91f1-6f44ebffa8cd | -11.5797 | -43.6728 | 2026-10-09 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 117.0 |
| b6a8175d-a850-3500-877f-b96f9dffc4b0 | -8.9684 | -45.177 | 2026-10-09 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 175693f7-d174-3d83-a437-910ef8066232 | -12.0058 | -43.464 | 2026-10-09 13:00:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 632.0 |
| f3abd8e4-a10c-3573-946f-ce67596a2119 | -11.0558 | -44.0796 | 2026-10-09 13:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 128.1 |
| c6c74791-43e1-3de9-a479-c1f411375d58 | -9.0829 | -45.0957 | 2026-10-09 13:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 170.1 |
| 98b45189-9b81-394f-8281-f163a9a5eaad | -10.4917 | -47.2087 | 2026-10-09 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 181.8 |
| 921806b6-bd44-3a77-8780-11321b3fb8e7 | -11.8307 | -43.5866 | 2026-10-09 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 371.3 |
| 9f975988-cb66-34d1-90f3-df4046c4595f | -8.2364 | -46.405 | 2026-10-09 13:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 9ee2bb05-0146-371a-86d1-7e7d251f5e34 | -11.6566 | -43.661 | 2026-10-09 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 8c8e8b4e-7957-30f3-9e3b-3a80d20101b2 | -11.0562 | -44.0561 | 2026-10-09 13:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 663e4762-33d6-3318-a5ef-652874a94dae | -8.9302 | -45.2041 | 2026-10-09 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 130.1 |
| ac016a54-ebc8-31e6-be48-69dfe5814640 | -11.245 | -45.3037 | 2026-10-09 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 452.0 |
| 5f310ada-e10d-31e8-9c96-fe57d24ee3c8 | -12.8105 | -44.6505 | 2026-10-09 13:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 187.1 |
| 8edf840b-2a19-3165-b7ed-065219ae4179 | -11.6194 | -43.5959 | 2026-10-09 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 145.4 |
| c18f3fc2-db65-38d7-bd6a-68c909230b63 | -12.2343 | -57.1271 | 2026-10-09 13:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 8d2f4e7b-282b-314c-a89e-4846fcfce534 | -11.2259 | -45.3064 | 2026-10-09 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 220.1 |
| a39f2d8d-ce3f-31ca-969c-9495320b808e | -10.3161 | -46.2668 | 2026-10-09 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 2290a79a-b775-391e-b47e-0f351e746be0 | -8.969 | -45.1313 | 2026-10-09 13:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 165.0 |
| 501b95dc-721d-393e-a0b7-030dc6bf3aa4 | -10.9174 | -45.5088 | 2026-10-09 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.1 |
| f53b0509-ae92-36ab-aa87-b6512856c97c | -11.3371 | -46.6547 | 2026-10-09 13:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 105.7 |
| c0b14480-7a1b-30c1-94c5-a3c5737dff62 | -11.6754 | -43.6817 | 2026-10-09 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 183.4 |
| 558448c9-1dbb-3616-b345-7608151507bd | -11.0745 | -44.1003 | 2026-10-09 13:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 208.7 |
| 2b42c4d7-1084-35b2-8921-4c1d452a147b | -11.8302 | -43.6103 | 2026-10-09 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 79c6e7d2-bca6-3ee1-ba47-3c395e317e37 | -10.4334 | -47.3046 | 2026-10-09 13:00:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| bff535cd-613c-3aad-bd24-216e1f7c8df7 | -10.917 | -45.5317 | 2026-10-09 13:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 9bc88543-ccec-3d0e-9443-e13bed2c1478 | -11.5801 | -43.6492 | 2026-10-09 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 154.8 |
| 83539c07-d4bf-3e4a-9957-b8f12b1d753a | -11.6557 | -43.7083 | 2026-10-09 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 443.0 |
| 55c35251-8c04-3477-bcbd-519434fb9eeb | -8.9775 | -45.9023 | 2026-10-09 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 0a290480-1a1b-3763-afc9-e1b3b3eff70b | -10.5087 | -47.3401 | 2026-10-09 13:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 8c659619-b6df-3c7b-8f91-fb1b51035b3c | -11.619 | -43.6196 | 2026-10-09 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 172.2 |
| 39c3544c-fdd9-3fb7-b993-da5a2f4a1042 | -10.5281 | -47.3156 | 2026-10-09 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 8999ab8f-a3d1-38db-89e6-0121f89b897c | -8.9964 | -45.9002 | 2026-10-09 13:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 137.2 |
| 180fc965-c873-3f1d-92b1-001edbed87ed | -11.6562 | -43.6846 | 2026-10-09 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 599.5 |
| 7143a31f-3f3d-3736-be5e-78f3d71f15a5 | -8.5313 | -46.911 | 2026-10-09 13:10:00 | GOES-19 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 144.7 |
| f5c2ba67-0896-351c-abf9-1ded40c7ce49 | -16.1136 | -43.4052 | 2026-10-09 13:10:00 | GOES-19 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 56dbb6b3-58b6-3870-bb3c-a024f7a1a91d | -12.0256 | -43.4371 | 2026-10-09 13:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 185d826f-9c43-3305-8224-9231b2b7dda8 | -10.8789 | -45.5368 | 2026-10-09 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 134.4 |
| e3ce8137-4419-3184-8e27-ee1d9f26189d | -12.0058 | -43.464 | 2026-10-09 13:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 746.1 |
| a171f81a-48e7-3ed9-a795-d080e18aae91 | -11.2068 | -45.3091 | 2026-10-09 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 0fc10ecc-467e-38e3-833d-35952ee2f86d | -11.5985 | -43.6935 | 2026-10-09 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 209.2 |
| fed960e9-4c28-36f9-960c-852e19bf1181 | -11.6754 | -43.6817 | 2026-10-09 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 33ba4e3e-669d-3b74-a1b4-053182699dfe | -8.9299 | -45.2269 | 2026-10-09 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 141.4 |
| 7839e422-c8c2-3f85-a9f2-d48c22a78195 | -10.8979 | -45.5343 | 2026-10-09 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| c67fb394-4da5-3638-9ecc-c622b430a682 | -8.3011 | -45.7245 | 2026-10-09 13:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 97.6 |
| be07df13-6076-3a6f-9b41-cfdd8a850055 | -10.4901 | -47.3201 | 2026-10-09 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 229.6 |
| 18575d25-5cbb-3ee9-ae0b-a0860d4025b1 | -8.0764 | -45.6339 | 2026-10-09 13:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 136.5 |
| bf96d5e9-819e-345e-b5fb-2f574211cad1 | -11.8787 | -47.3668 | 2026-10-09 13:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 25de97d1-7c3b-3170-bf97-b5c0a2717e49 | -13.1056 | -46.3321 | 2026-10-09 13:10:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 94.5 |
| b82a4c2a-e53b-3c40-9d4f-690ff774a926 | -12.1729 | -44.7983 | 2026-10-09 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 1420cf72-2eee-33ee-9638-329acbd71529 | -11.8783 | -47.3892 | 2026-10-09 13:10:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 135.5 |
| ad3c780c-4d4e-33d6-8163-ff6c3d8d5e79 | -11.6177 | -43.6906 | 2026-10-09 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 139.7 |
| aadc446b-01f4-326b-bde8-bac9b96f1ecb | -12.2149 | -44.6057 | 2026-10-09 13:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 6c21a4c4-1adf-306d-a7cc-5f21f9916e39 | -12.0054 | -43.4878 | 2026-10-09 13:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 278.8 |
| 7c629e2d-b3a3-3553-9bed-3c7d3d72aaf6 | -10.4334 | -47.3046 | 2026-10-09 13:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| b446f2bf-0055-30fb-b092-c9dac1bc408d | -8.911 | -45.229 | 2026-10-09 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 132.4 |
| d665278d-8003-3d6f-aa76-62e76ee8289a | -11.5797 | -43.6728 | 2026-10-09 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 011ec47f-d654-3fcf-943c-4bb1ccdfeee9 | -10.4917 | -47.2087 | 2026-10-09 13:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 230.9 |
| b25c6825-c9e0-367c-89af-04acfc65a8d1 | -12.811 | -44.627 | 2026-10-09 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 39b77cef-03f2-3ffd-ac64-013d1b0a8f6e | -12.0063 | -43.4402 | 2026-10-09 13:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 469.7 |
| a31d7f00-15c2-3457-a964-1186234cde5d | -12.8299 | -44.6473 | 2026-10-09 13:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 723e41f8-15ad-3c68-8c11-0d2da45ac02f | -11.2475 | -46.3058 | 2026-10-09 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 163.8 |
| 5382c8de-48b6-3d9d-92e0-156e530033fb | -11.4131 | -46.6671 | 2026-10-09 13:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 107.6 |
| 7e7388ed-da78-350c-8e0a-7d20da2ab381 | -8.2364 | -46.405 | 2026-10-09 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 44df97a5-144d-3433-81e5-8adbf21bdb60 | -9.9208 | -44.7893 | 2026-10-09 13:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 3990ea79-35e4-3a3e-817d-b5c8e3c139ef | -11.9865 | -43.4671 | 2026-10-09 13:10:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1700.1 |
| 16afb35c-d442-3508-bb78-ab9876ba417c | -11.5801 | -43.6492 | 2026-10-09 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 8120442d-41bd-39f9-baab-9fb009a11116 | -10.917 | -45.5317 | 2026-10-09 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 153.3 |
| eacfcdf4-922f-354d-a2cf-7fbd5cc140ca | -8.9684 | -45.177 | 2026-10-09 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 168.0 |
| 1209ad54-d6ab-33af-8af3-6240e02a2edf | -11.5989 | -43.6699 | 2026-10-09 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 153.0 |
| d58169db-42a9-31a0-936c-177802f0c3d3 | -8.2063 | -45.7791 | 2026-10-09 13:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 657e7af0-38ab-3ed4-aa5b-9cc4d7245007 | -8.969 | -45.1313 | 2026-10-09 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 204.7 |
| a050ba49-66ee-300b-8ed1-a37421a076ab | -8.9687 | -45.1542 | 2026-10-09 13:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 5dd56b70-76ab-30da-bfde-4748b8c2fdfa | -12.1537 | -44.8013 | 2026-10-09 13:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 926b439c-2080-3dde-af23-9fe7f8a8c847 | -9.1012 | -45.1393 | 2026-10-09 13:10:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 191.2 |
| a6d56f57-611a-341f-8eec-49f8e042b532 | -16.6321 | -47.203 | 2026-10-09 13:10:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 495759ce-74fd-3b55-8d02-fd4ee94a40b6 | -13.2863 | -46.962 | 2026-10-09 13:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 62188807-4009-356c-8a85-3b8a1788ec0b | -10.8983 | -45.5114 | 2026-10-09 13:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 139.7 |


[Clique aqui para ver as próximas entradas](README238.md)
