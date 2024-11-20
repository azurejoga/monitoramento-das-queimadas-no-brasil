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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| abd2e49d-5e1a-3bfa-9ff9-7d9b12bb3e37 | -4.345 | -45.87644 | 2024-11-20 04:50:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 93a4e982-9b7f-3e70-8c52-f4f1ea3276a6 | -1.14443 | -51.94507 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b06e290c-8dd3-3e30-afab-f8c8e501575c | -1.51059 | -52.08782 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ddb9ef6a-743a-3604-a871-f011ea2b26a7 | -2.58487 | -51.71741 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eef7a6f0-780d-3a59-b067-f71b20eede0f | -1.09334 | -51.73494 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e74138f-53ba-3d9b-985b-c04bbdf51f07 | -3.5846 | -43.6255 | 2024-11-20 04:50:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3906e182-268c-38f1-be74-4ae76d9ec35e | -1.06252 | -52.39871 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70db9758-b991-3793-a029-7c785e55faa3 | -1.60378 | -52.24887 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b89baf12-e95e-3788-9e0b-4c8fcb80d62c | -3.10342 | -53.09808 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce1d5ad9-1fa8-3111-8bb5-b29cb6b95ec7 | -2.66356 | -46.23807 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ebf1fc53-4fbf-3d48-956d-8842c7e0542b | -2.99899 | -52.37041 | 2024-11-20 04:50:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cd8725e-5efd-30f9-adf1-d84130080ca3 | -1.26901 | -52.12498 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5392433b-6f48-367a-8116-c55aa27e696c | -1.78587 | -53.58904 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c746588c-8e4f-35e8-aaf7-5bb9fb3ab4c2 | -1.76033 | -52.67028 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83db28f1-0333-3d39-b7ac-4fa42fb4fefe | -4.44683 | -46.58181 | 2024-11-20 04:50:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 23.0 |
| ba399eca-3136-312b-a160-5af997933441 | -3.9066 | -53.82401 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6cf4404-5a49-34e2-ab41-32570335c05e | -1.70224 | -50.20217 | 2024-11-20 04:50:00 | NPP-375D | CURRALINHO | PARÁ | Brasil | 1502806 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 912752ac-1396-3da7-bfbf-3e01a6bc302f | -1.45149 | -47.11528 | 2024-11-20 04:50:00 | NPP-375D | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a1bde0f2-fcac-3219-bc82-cf869907e311 | -1.54035 | -51.10889 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 916d3169-3372-302b-81e1-238187dce942 | -3.79222 | -46.94064 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b7cadff-eb46-3b73-99cf-5ce880f14f03 | -1.73476 | -45.58091 | 2024-11-20 04:50:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f2c78ce-e403-3dd4-98fc-a253f4aad030 | -5.69435 | -47.66166 | 2024-11-20 04:50:00 | NPP-375D | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a8bf799-c447-3a32-878b-3ddc606650c5 | -2.40293 | -51.98896 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ebc1014-e82f-3db5-8fa1-3218d59f300c | -1.61699 | -53.2867 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9650c4cc-68d8-34be-9828-4cf2898c1bd3 | -2.8452 | -46.6797 | 2024-11-20 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3d0b5c91-a0bc-3d29-bbbb-873937a8b60f | -1.19058 | -51.97717 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1914f138-cd9a-3425-9642-bda09379a076 | -1.86425 | -46.80052 | 2024-11-20 04:50:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| deaf4e7c-cf6b-3d4b-89c5-e43ecd211d4f | -2.62072 | -48.18261 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e35a4c57-b982-3a94-ae9c-e96ad57ec1bc | -1.44694 | -52.70598 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3127a2f0-518a-30bf-bef2-9d942fce6425 | -2.5704 | -48.43446 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e170999-ba12-3425-8049-e41319c5351b | -3.97588 | -51.24375 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e503d75a-db30-3866-a294-6337ec127620 | -3.55893 | -51.11843 | 2024-11-20 04:50:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aa714472-91cf-35a8-9cb9-9b009aa58f9c | -5.9741 | -45.3692 | 2024-11-20 04:50:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c3c3cf9-b535-314a-a9a4-97d49416e794 | -2.91498 | -53.07278 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| b2f63e89-257d-3205-b5f0-4ff61c793211 | -3.10228 | -53.10527 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b885ce4d-3685-333c-b7f2-6954758d0971 | -2.71373 | -53.1743 | 2024-11-20 04:50:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 440632fb-ca7b-3832-95d4-7e471f03758a | -1.30799 | -51.74697 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1dc10560-e94a-329d-a56e-e3e69f15d852 | -2.26996 | -45.46084 | 2024-11-20 04:50:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41a0a86d-0530-369d-952a-ceeb52cb3586 | -2.16294 | -51.96948 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce9bad16-5b5a-3c2b-996b-020fda0a3a4a | -4.3808 | -50.41604 | 2024-11-20 04:50:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b7037e4f-9d87-3870-ac7f-f1b1c0cdbef5 | -3.85304 | -49.43761 | 2024-11-20 04:50:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f5044913-7925-3616-9767-5c4ffd56cc70 | -4.13787 | -47.73127 | 2024-11-20 04:50:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf8befc0-7ce1-3ac8-92a8-905d19409a73 | -9.16957 | -44.72323 | 2024-11-20 04:50:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bda3b9c1-38aa-3648-8560-f7be0ba3160f | -1.48218 | -51.97264 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3371e08c-f840-37bd-96b8-631de53deff4 | -1.70825 | -52.48802 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 96dd391a-5536-3445-a97b-6fa22d4d0484 | -2.45561 | -53.69746 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 50e1bd68-5726-3080-a971-54c35be2cb26 | -3.88259 | -52.24275 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 797d224a-2d17-32a6-be45-eec94fd20966 | -2.97019 | -52.36616 | 2024-11-20 04:50:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db829535-8311-3323-8ab7-4dada214da8c | -3.562 | -45.01587 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 608d121a-390c-309d-addd-37047b3ef0ad | -2.68958 | -46.23436 | 2024-11-20 04:50:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1df06d1-138c-3521-9090-eefe05a7957e | -1.85587 | -47.82417 | 2024-11-20 04:50:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15f2c8e3-2641-344f-bd69-b740cdd2afc1 | -1.86788 | -53.20129 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 216778cd-43a9-32d6-9f0e-efebf80d3a8c | -1.86768 | -47.82156 | 2024-11-20 04:50:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b550fbf-73fe-347e-a78f-68142bd01470 | -2.59695 | -54.00426 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f205a11e-4182-310f-b92a-585825475aeb | -3.80392 | -52.3151 | 2024-11-20 04:50:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17291baa-fe9c-38c9-86a4-956ca433a027 | -1.64493 | -52.60503 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ace264f7-d580-3007-ae26-b651df5c3a13 | -6.07945 | -47.27126 | 2024-11-20 04:50:00 | NPP-375D | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f265714e-ae4c-3ceb-89fd-f0ddfa6f1c86 | -2.57579 | -54.02471 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 35e3001b-bdfd-33d2-bbf1-5846e34e6790 | -1.5181 | -52.36491 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5d57880-7f2c-3901-9ec2-b0977a3b0e22 | -2.4293 | -46.52674 | 2024-11-20 04:50:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c4fa0d85-723e-3141-8ce7-c4224485d330 | -2.25972 | -48.42059 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3db5351a-9063-3c22-836a-743b7391fce0 | -3.76828 | -51.67984 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c173f18e-a1a7-3e7f-a525-a48ce64186cb | -2.61025 | -49.24783 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20e8c4ff-c6bb-300c-adc5-7e70718c3a82 | -1.34728 | -51.85926 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb041acb-3b5f-33a2-88b1-6f12620e102b | -2.61256 | -49.25606 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ee43be1-4076-38e0-bf60-7892f5cec337 | -1.45878 | -52.67492 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 26cf44c5-bdc9-3dba-ba25-4c3ae832f4d9 | -1.96413 | -49.54976 | 2024-11-20 04:50:00 | NPP-375D | LIMOEIRO DO AJURU | PARÁ | Brasil | 1504000 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c4b6ed8-6af2-3027-b2fa-7b64874d0268 | -2.77914 | -48.57796 | 2024-11-20 04:50:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4934076f-c725-36d6-847a-6aeb60a68367 | -3.05737 | -54.40232 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fed5f9b5-022a-36d0-b14b-0da26feb478b | -3.11113 | -53.75126 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 82446272-ba5e-3ff0-a964-5ee60133ac3d | -1.07465 | -53.36485 | 2024-11-20 04:50:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65cf7fba-f9ad-3506-9629-b3203048f8ad | -2.82145 | -54.09322 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77ab9373-406a-3a91-8a77-9b4b8bbb7f18 | -2.17747 | -49.12994 | 2024-11-20 04:50:00 | NPP-375D | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16ad8821-0f45-3df6-90d7-0d7d50dfe46f | -3.58878 | -53.89398 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 434d9284-20bc-3697-81ea-3b4b61e0e010 | -0.9615 | -51.73157 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 84efd4fd-639e-30cd-b5f8-ade5e83192c5 | -3.57849 | -54.55001 | 2024-11-20 04:50:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 861dfa9a-1fc9-38c3-967d-6c9590677e20 | -2.78652 | -47.63683 | 2024-11-20 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2160796-b119-3d00-a6b1-06cfaa7aa14d | -0.95927 | -51.72414 | 2024-11-20 04:50:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 04bd8924-f107-382f-bb90-7faaf2db59ea | -6.24952 | -47.27009 | 2024-11-20 04:50:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fb94543e-ff15-3836-89b4-32702da72b05 | -2.41073 | -49.06844 | 2024-11-20 04:50:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 52021d71-6418-3d2b-8db3-82e7636af337 | -1.54052 | -52.04973 | 2024-11-20 04:50:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5c789a4-5296-34f0-b2bd-b9729acb4745 | -1.71161 | -52.48854 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| da979a25-cbfb-3d4e-940e-91645b099b08 | -2.61908 | -48.21733 | 2024-11-20 04:50:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b8d03dd-e775-3f67-8b87-7a8eeea3b57f | -3.99046 | -49.92108 | 2024-11-20 04:50:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c75b9b6-c4ff-32b6-852b-0670c562ed05 | -2.63316 | -54.27828 | 2024-11-20 04:50:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41990a34-a4fd-3ab5-b6c2-e6dbac4dff95 | -1.47455 | -53.48349 | 2024-11-20 04:50:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| bf30cb15-9fd7-3ae9-ab2e-fc63e79d4e3c | -3.08388 | -54.66151 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63c4920f-6cb9-390b-949f-aae768042f3d | -2.02402 | -51.17394 | 2024-11-20 04:50:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 701d1355-d5e6-3eda-a080-a13fc9151bf0 | -2.55981 | -46.5427 | 2024-11-20 04:50:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4b76518-63f3-3dcb-9d4a-9f9905e18cc1 | -4.44211 | -46.58491 | 2024-11-20 04:50:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 23.0 |
| c2b1ab2b-f451-3cc5-a059-34a76e64f355 | -3.10842 | -54.28415 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c92b48d3-91b0-30ec-986e-78b76cd0a022 | -1.48189 | -51.15628 | 2024-11-20 04:50:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3333c06b-7f55-363d-81f1-fa328f1108e7 | -3.0532 | -54.40569 | 2024-11-20 04:50:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7d66d24e-acbb-3d83-88c8-e678b7f74115 | -3.314 | -54.17258 | 2024-11-20 04:50:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb28ca3b-efe7-35c7-bfe3-266d13609eb4 | -1.7264 | -52.79662 | 2024-11-20 04:50:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9feaa96d-063f-31fd-87bd-ca5fb3250993 | -2.79296 | -51.79213 | 2024-11-20 04:50:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18e68ad8-50a4-3b0d-8e0f-71efa9f4e803 | -4.93845 | -50.64553 | 2024-11-20 04:50:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be7577bc-906a-3837-b09b-9eecebf7414f | -2.42875 | -46.53028 | 2024-11-20 04:50:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f118c558-d242-3f87-b85c-c3c45e384870 | -2.08173 | -48.53743 | 2024-11-20 04:50:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbd7fda7-d681-34fa-a748-f108ae0af58a | -5.72007 | -44.80861 | 2024-11-20 04:50:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README54.md)
