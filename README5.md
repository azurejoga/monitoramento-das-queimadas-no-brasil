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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1da60911-293e-3a7a-a262-b0288eb024e4 | -25.0161 | -54.051998 | 2024-10-06 00:44:25 | METOP-B | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 52f02cd3-a0be-348e-8319-213b7146744f | -25.0184 | -54.0653 | 2024-10-06 00:44:25 | METOP-B | DIAMANTE D'OESTE | PARANÁ | Brasil | 4107157 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a1b44e69-cd91-3b2b-8412-70a853637bc8 | -23.725201 | -50.044399 | 2024-10-06 00:44:34 | METOP-B | JABOTI | PARANÁ | Brasil | 4111704 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 667974d4-f27f-36ae-a123-021fd3c748a1 | -21.73 | -45.601898 | 2024-10-06 00:44:51 | METOP-B | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b4522845-d18c-3753-8025-21fc11068705 | -21.732 | -45.610298 | 2024-10-06 00:44:51 | METOP-B | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 198819a7-d33f-3611-ae07-52ff3ed7a55b | -21.7202 | -45.6045 | 2024-10-06 00:44:51 | METOP-B | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a9ba5de6-f0b0-3b30-ac7f-7a306428d318 | -21.8501 | -48.4319 | 2024-10-06 00:44:59 | METOP-B | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a15fd215-9b72-328c-a197-f3082a3f884f | -21.8517 | -48.439201 | 2024-10-06 00:44:59 | METOP-B | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 57aab185-8891-32ea-ba30-2f2c75e374e0 | -21.172199 | -45.562698 | 2024-10-06 00:45:00 | METOP-B | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7d8b674e-c860-39ef-af15-6aeb6ac0bb02 | -21.5865 | -47.930302 | 2024-10-06 00:45:02 | METOP-B | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 78e67f2c-9487-3b1a-85ee-5f007fdcb850 | -21.5881 | -47.937698 | 2024-10-06 00:45:02 | METOP-B | RINCÃO | SÃO PAULO | Brasil | 3543709 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 3cc74bca-2ec9-3bed-9417-4c4ae6ed6741 | -21.0734 | -45.7146 | 2024-10-06 00:45:02 | METOP-B | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c2e3aee1-b206-3dee-9b9a-403129a2d73d | -21.393999 | -47.5718 | 2024-10-06 00:45:03 | METOP-B | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 612628b6-198a-3866-bc86-73acd750fcd7 | -21.395599 | -47.579201 | 2024-10-06 00:45:03 | METOP-B | SÃO SIMÃO | SÃO PAULO | Brasil | 3550902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0b0a21df-09c1-3ca9-bcb5-7f3de8f10956 | -21.081301 | -46.687599 | 2024-10-06 00:45:05 | METOP-B | JACUÍ | MINAS GERAIS | Brasil | 3134806 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d6ee6978-1cbc-3e41-b9ba-b9752debeebe | -21.306101 | -47.594002 | 2024-10-06 00:45:05 | METOP-B | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 084ecb57-e9b5-36bd-9ea0-057dbcd693a2 | -21.307699 | -47.601398 | 2024-10-06 00:45:05 | METOP-B | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| bed9c258-0223-3778-bc2d-db2cafb73637 | -21.365999 | -48.6203 | 2024-10-06 00:45:08 | METOP-B | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4c38b80a-eaae-36e7-a717-d0d98e4f497a | -21.3675 | -48.627602 | 2024-10-06 00:45:08 | METOP-B | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4d2bbb2e-84e7-3e9c-86c8-f1bf34af2deb | -21.2901 | -48.7934 | 2024-10-06 00:45:09 | METOP-B | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e4ea5413-0da7-3f50-994b-17f27cb93c73 | -21.2917 | -48.800701 | 2024-10-06 00:45:09 | METOP-B | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 89dfdd0b-9b0b-3891-8f8c-f967b27c6164 | -20.759501 | -46.2766 | 2024-10-06 00:45:09 | METOP-B | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 58803a13-5626-3268-892e-b2e09c4d0874 | -22.5056 | -55.171299 | 2024-10-06 00:45:10 | METOP-B | LAGUNA CARAPÃ | MATO GROSSO DO SUL | Brasil | 5005251 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f5f04b4a-f020-38de-b977-79286892d843 | -22.507999 | -55.185398 | 2024-10-06 00:45:10 | METOP-B | LAGUNA CARAPÃ | MATO GROSSO DO SUL | Brasil | 5005251 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 7ed7f92d-9179-3d59-831e-733f59803e51 | -22.510401 | -55.1996 | 2024-10-06 00:45:10 | METOP-B | LAGUNA CARAPÃ | MATO GROSSO DO SUL | Brasil | 5005251 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5e591dc2-d043-3715-8f17-9e965c3f65d8 | -19.903299 | -44.5028 | 2024-10-06 00:45:16 | METOP-B | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d6ae9ac1-facb-3ed7-94a9-ddf1e0222156 | -19.905701 | -44.5126 | 2024-10-06 00:45:16 | METOP-B | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0d72e73a-0e98-30f8-8a0c-5df46681f5c1 | -20.7822 | -48.585602 | 2024-10-06 00:45:17 | METOP-B | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 6c0bf728-160e-3926-a658-40041b7f4f57 | -20.0191 | -45.632702 | 2024-10-06 00:45:18 | METOP-B | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 95721b24-02ec-3e5b-bdbc-c2afdfb3c340 | -20.0212 | -45.6413 | 2024-10-06 00:45:18 | METOP-B | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 321b7df4-bf0d-37d5-b281-bf7750ef52b5 | -20.023199 | -45.650002 | 2024-10-06 00:45:18 | METOP-B | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e8b15a16-4f41-33e7-8d8d-a5278026f199 | -2.6858 | -49.0752 | 2024-10-06 00:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 187.3 |
| 6ab19df9-e611-3182-8417-e39b46035510 | -2.6859 | -49.0539 | 2024-10-06 00:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 134.0 |
| 249c9ef2-0f49-3c75-afe4-3b3a89e7c847 | -2.7043 | -49.0747 | 2024-10-06 00:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 345c1e27-bc96-36e1-8791-089f98e25fc0 | -2.7043 | -49.0533 | 2024-10-06 00:45:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 2c25d62b-3ac1-31f8-8381-628a2c05048c | -2.8169 | -48.601 | 2024-10-06 00:45:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 21e37020-b0bd-30ba-9bc3-2527c823e734 | -3.1298 | -48.9764 | 2024-10-06 00:45:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 803ca118-2e64-3224-8902-2c4cbd124e02 | -3.1299 | -48.955 | 2024-10-06 00:45:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 60aa9112-8fef-3a86-8507-113bb6f9ce9a | -3.2329 | -50.8504 | 2024-10-06 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 8bd05968-1ca2-3a79-8a52-199e8c9a8620 | -3.233 | -50.8296 | 2024-10-06 00:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 68d69f28-0ca7-3782-a800-2d78e9066ac9 | -3.3084 | -50.451 | 2024-10-06 00:45:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| f3138b9b-e7b2-3a6a-bd8a-8f5dcc5a8b10 | -19.8223 | -46.4263 | 2024-10-06 00:45:25 | METOP-B | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e37f9047-ca80-30f8-9453-d0030018dbe8 | -3.7255 | -41.6748 | 2024-10-06 00:45:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 54.0 |
| 95ef16d5-90f7-3881-beff-245e36d0f734 | -3.8008 | -41.5989 | 2024-10-06 00:45:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 219.9 |
| d9ad7e02-c5a7-32ee-b88d-8d500d9489ed | -3.801 | -41.575 | 2024-10-06 00:45:27 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 105.3 |
| 4a1fda8b-d155-3abf-b026-c11631216880 | -19.605499 | -46.249802 | 2024-10-06 00:45:27 | METOP-B | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 52f0d72b-d775-3784-9d2c-dca4216b75e3 | -3.7935 | -49.4636 | 2024-10-06 00:45:28 | GOES-16 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 15621637-1d52-347f-bac5-ee90b388e83c | -19.865 | -47.8372 | 2024-10-06 00:45:29 | METOP-B | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8852cc53-068f-3f1d-8087-ccc604b77f25 | -19.866699 | -47.844601 | 2024-10-06 00:45:29 | METOP-B | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1dd196f3-20f7-37e4-8563-7ef5b12c5ed7 | -19.856899 | -47.847 | 2024-10-06 00:45:29 | METOP-B | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| afae7beb-2bbf-3994-ab87-388a23a4b85b | -19.8472 | -47.849499 | 2024-10-06 00:45:29 | METOP-B | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 02d39e94-6d96-376d-ad54-1006544134a7 | -19.848801 | -47.856899 | 2024-10-06 00:45:29 | METOP-B | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a42eba6e-03e0-38e8-bcb5-ecce729c0679 | -18.743299 | -44.168701 | 2024-10-06 00:45:33 | METOP-B | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0cf3de15-b193-3081-9f27-600ef755b793 | -18.745899 | -44.179199 | 2024-10-06 00:45:33 | METOP-B | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8b637928-2b62-3321-b771-b681ff48d748 | -18.5522 | -43.816101 | 2024-10-06 00:45:35 | METOP-B | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b4d4170d-75f1-312e-9f5f-2323730ee81d | -18.5425 | -43.818699 | 2024-10-06 00:45:35 | METOP-B | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 5080821c-e6d3-394a-8e6d-6d904bfd55de | -5.5716 | -44.8927 | 2024-10-06 00:45:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 0b3ef3a6-05bb-3001-a5f6-e64eef0c4f6a | -5.5718 | -44.87 | 2024-10-06 00:45:37 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 167.2 |
| 74604721-d79d-3669-a7e5-ee6643fcfe29 | -5.5905 | -44.8687 | 2024-10-06 00:45:38 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 157f3f6a-ce20-342d-aa8b-4d503b6d7126 | -5.8214 | -44.1426 | 2024-10-06 00:45:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 145.6 |
| ce93fb86-a493-3ed4-bffb-b1522ebfd579 | -5.8216 | -44.1196 | 2024-10-06 00:45:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 108.6 |
| e885d774-48d1-3033-b1ff-e43d5f16b8f0 | -19.063801 | -46.989899 | 2024-10-06 00:45:39 | METOP-B | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ade06fe3-8a31-3d14-bde9-2f8f1ae930ef | -19.065599 | -46.9977 | 2024-10-06 00:45:39 | METOP-B | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0944be5a-b65d-320f-9216-1eff77879255 | -20.559601 | -54.5709 | 2024-10-06 00:45:40 | METOP-B | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5db536ca-f53a-38b1-a1d1-3aaa994d9c5a | -19.086901 | -48.185101 | 2024-10-06 00:45:43 | METOP-B | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 209b357d-2a55-3ee5-8dd9-9ab74e24daa0 | -19.0886 | -48.192402 | 2024-10-06 00:45:43 | METOP-B | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 610d081a-7ae8-39b2-a78c-9cd3251c6d29 | -6.9514 | -59.0666 | 2024-10-06 00:45:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 526448f0-91c1-31a0-a7c8-bafb8823cef2 | -6.9699 | -59.0658 | 2024-10-06 00:45:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| d4d50648-ea11-372c-95e1-029dd2194ddf | -7.1532 | -59.2898 | 2024-10-06 00:45:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| a625c60f-4709-3533-a856-e75d8ee15eaf | -17.725 | -43.825699 | 2024-10-06 00:45:48 | METOP-B | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 23c1a085-de6e-3305-91b5-b8aac051d6cb | -18.438299 | -46.653801 | 2024-10-06 00:45:48 | METOP-B | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6543b013-1e29-318c-aebf-a8cb83574d49 | -7.4741 | -72.6801 | 2024-10-06 00:45:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 219c3934-3c0d-37e7-8880-0761c7fef252 | -17.3708 | -42.630199 | 2024-10-06 00:45:49 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d6c884e7-cd28-36d8-aa89-20083558c9bb | -17.3743 | -42.643902 | 2024-10-06 00:45:49 | METOP-B | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 26fba4fd-6851-3c17-9a78-99885a3b0012 | -17.361099 | -42.6329 | 2024-10-06 00:45:49 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fa52b786-41b9-33f3-9048-553d9140e3b5 | -17.364599 | -42.646599 | 2024-10-06 00:45:49 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d7ab23ec-ca62-35fb-8257-3b5f299e0e31 | -17.3549 | -42.6493 | 2024-10-06 00:45:49 | METOP-B | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3e31856c-8487-332c-ad25-fd1d2fda7c4f | -18.470699 | -47.376202 | 2024-10-06 00:45:50 | METOP-B | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2c4c01d8-963a-33fc-a09f-e3b77477cc86 | -18.4725 | -47.3839 | 2024-10-06 00:45:50 | METOP-B | ABADIA DOS DOURADOS | MINAS GERAIS | Brasil | 3100104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 838c642e-23d6-32cf-96af-3d2356460e04 | -7.8698 | -54.9029 | 2024-10-06 00:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 86ea3a14-9004-33c8-abea-fe118603a6d5 | -7.87 | -54.8828 | 2024-10-06 00:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| c7722ac3-6344-3704-b3f3-1f013dc2c2b4 | -7.9639 | -54.7764 | 2024-10-06 00:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 74ddbdc5-2657-3679-96ef-e45ae7f47227 | -7.964 | -54.7562 | 2024-10-06 00:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| b2616c04-50e7-370e-8b03-4396748792aa | -7.9825 | -54.7752 | 2024-10-06 00:45:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 0e9dfa38-7a5b-383f-80be-aa7c46790306 | -7.9826 | -54.7551 | 2024-10-06 00:45:52 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 3ebe689c-8e9e-39c3-a8de-e015fe133faf | -17.624399 | -44.381001 | 2024-10-06 00:45:52 | METOP-B | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 3543d28a-4780-38ce-9c9c-fe7e5f9d6db6 | -17.627001 | -44.391602 | 2024-10-06 00:45:52 | METOP-B | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 26ed4f35-b767-3e84-a4a8-a7e138c9cfab | -17.629601 | -44.402199 | 2024-10-06 00:45:52 | METOP-B | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 327c56c7-962d-31f4-96fa-7a7c015c55ee | -17.6173 | -44.394199 | 2024-10-06 00:45:52 | METOP-B | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| dcc35d57-76f5-3022-a030-4f729ded76e1 | -17.6199 | -44.4048 | 2024-10-06 00:45:52 | METOP-B | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 0668a734-0db6-3fc5-b643-e227e07e69e8 | -17.607599 | -44.396801 | 2024-10-06 00:45:52 | METOP-B | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 145e17f4-0293-3a94-9b60-e8590fe844f2 | -8.2139 | -61.2022 | 2024-10-06 00:45:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 3f26fe22-6801-31b4-b11c-90907196684e | -17.597799 | -44.399399 | 2024-10-06 00:45:53 | METOP-B | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8c0c140f-4e34-3fb8-93e2-88038657068d | -17.600401 | -44.41 | 2024-10-06 00:45:53 | METOP-B | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 78d1188a-904a-38df-995a-f670e1c78407 | -19.878799 | -55.055 | 2024-10-06 00:45:53 | METOP-B | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5c42000b-5e7d-33e1-bc00-11812d8a19fd | -19.8811 | -55.0676 | 2024-10-06 00:45:53 | METOP-B | CORGUINHO | MATO GROSSO DO SUL | Brasil | 5003108 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 56dbf9de-2b89-31b8-bfea-c30c87a4ed15 | -9.269 | -48.1377 | 2024-10-06 00:45:58 | GOES-16 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 5771f875-c54c-3825-b551-d9ccb06848dc | -9.1759 | -61.5794 | 2024-10-06 00:45:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 73.5 |
| ecf55ccc-2a9c-37d6-b745-a173e5725cdc | -9.176 | -61.5603 | 2024-10-06 00:45:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 90030385-3257-3d69-816e-85c36467b192 | -9.3275 | -46.5609 | 2024-10-06 00:45:59 | GOES-16 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 155.3 |


[Clique aqui para ver as próximas entradas](README6.md)
