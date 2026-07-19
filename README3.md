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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a06642d5-cab0-306e-91ee-5f27dd589828 | -22.90607 | -43.43685 | 2026-07-19 03:28:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1cc14a37-1d82-3367-a0b0-18292fff9e36 | -19.81762 | -47.96436 | 2026-07-19 03:28:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 72b2e2f8-4463-36ed-9930-e96d71bdfc42 | -23.28884 | -46.15791 | 2026-07-19 03:28:00 | NOAA-21 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ca34997b-f645-3f39-ae7e-dab349b5fd7d | -19.81692 | -47.96362 | 2026-07-19 03:28:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9a53c1ba-1b61-34a4-b7b1-e0b32f02403e | -22.18985 | -45.81924 | 2026-07-19 03:28:00 | NOAA-21 | SÃO SEBASTIÃO DA BELA VISTA | MINAS GERAIS | Brasil | 3164407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 77b1ec09-8cbf-3dd4-a003-15b6f385446d | -22.91003 | -43.44293 | 2026-07-19 03:28:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a70d5df3-5351-38d4-939f-36db70a2f464 | -23.22619 | -46.23898 | 2026-07-19 03:28:00 | NOAA-21 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a89d3eed-7c03-3c66-a167-4ac04d83d49d | -29.55012 | -51.39289 | 2026-07-19 03:30:00 | NOAA-21 | HARMONIA | RIO GRANDE DO SUL | Brasil | 4309555 | 43 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 67582bfc-00ff-3c2b-b5af-6e3f23c29308 | -29.54928 | -51.3919 | 2026-07-19 03:30:00 | NOAA-21 | HARMONIA | RIO GRANDE DO SUL | Brasil | 4309555 | 43 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 037d75b2-9985-34ff-8bac-c2d82260d883 | -13.6764 | -48.7786 | 2026-07-19 03:50:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 58.1 |
| c6e11a6e-2a29-3cd5-9a7f-c8c09f98b26e | -4.58295 | -46.29963 | 2026-07-19 03:57:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c51a7675-1b69-3195-851e-44774285e85f | -4.03475 | -49.24794 | 2026-07-19 03:57:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 53d32fb1-853f-31c8-881a-58ff72d9c1e4 | -2.83362 | -48.868 | 2026-07-19 03:57:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d1e88b3-cbf1-32c7-b7e0-9946953ca20c | -4.6606 | -43.22938 | 2026-07-19 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 33662a4a-ff64-327a-92af-69c73c95c540 | -4.66511 | -43.23014 | 2026-07-19 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0387f3e9-903d-332e-a885-922f85334739 | -5.10827 | -38.06705 | 2026-07-19 03:57:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 4a463fd6-d010-3a3c-b3a6-070416bbb0ee | -4.58229 | -46.30343 | 2026-07-19 03:57:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e552636-8c52-3453-bc81-e6f7e056e1cd | -4.03942 | -49.26119 | 2026-07-19 03:57:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08d28546-062c-3100-84dd-ed74eb5c0b5a | -4.03627 | -49.24738 | 2026-07-19 03:57:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 20aa4f41-f22d-3897-bcf2-0fe09a21cd15 | -5.10885 | -38.06345 | 2026-07-19 03:57:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 88aced11-508c-35ef-8bb9-f88c41e8b81b | -4.66588 | -43.22562 | 2026-07-19 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef9b4ea2-cc6a-302b-b87a-756a91bb14b2 | -5.11223 | -38.064 | 2026-07-19 03:57:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| ee481af1-0fb5-38af-9bdb-c126393b8789 | -4.03376 | -49.25368 | 2026-07-19 03:57:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89c32274-f2e7-3453-8948-fa3b749e381b | -4.03524 | -49.25311 | 2026-07-19 03:57:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e1868c0-60b3-3582-9b6f-ae7b65bd78aa | -2.82899 | -48.86633 | 2026-07-19 03:57:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8d16756f-ddc2-352d-86d2-1ef654daa021 | -4.67039 | -43.22639 | 2026-07-19 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e68e6509-da89-3ea9-a45e-caef3b4bc138 | -4.03416 | -49.25909 | 2026-07-19 03:57:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18f5b6b6-80c8-3dbd-b187-f6fc1d0cd9fb | -2.82691 | -48.86678 | 2026-07-19 03:57:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a2cdc80-3732-3d3b-96b4-d859831cd37a | -13.6764 | -48.7786 | 2026-07-19 04:00:00 | GOES-19 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 3a4f3993-9ff6-3114-bc9d-fe4c454721e8 | -9.49503 | -47.15346 | 2026-07-19 04:00:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 412e4e90-618a-3135-8ec6-14083035ca93 | -8.92821 | -47.60391 | 2026-07-19 04:00:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a3de37bc-0970-3249-9ce2-5a46bb2517f0 | -6.7295 | -44.36784 | 2026-07-19 04:00:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6635391d-cfc1-3277-b6aa-b78fe234ce74 | -8.93874 | -47.6099 | 2026-07-19 04:00:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 500c350e-a125-3074-a832-1d89ee82eed4 | -5.52439 | -45.27274 | 2026-07-19 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f17b3959-ae9b-34ae-bcc1-55977bc47f93 | -9.08542 | -50.59023 | 2026-07-19 04:00:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c98305b-a969-35ef-8706-57a6405afbb4 | -8.36245 | -45.40186 | 2026-07-19 04:00:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 2e32c493-01e9-349e-8a14-ff09efcb1902 | -8.72929 | -47.83136 | 2026-07-19 04:00:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fde6b82a-4bce-329a-809c-4ff92ab59dff | -7.1152 | -44.04195 | 2026-07-19 04:00:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da3ccbf4-4136-3239-b68c-6896e6c28862 | -8.94436 | -47.61099 | 2026-07-19 04:00:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98abdafd-1132-3960-9687-11682a75ecee | -10.70413 | -46.61886 | 2026-07-19 04:00:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7a46c2d-f55c-3301-9100-02fb765b0b0e | -8.35758 | -45.40071 | 2026-07-19 04:00:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9f983a40-a425-3069-9bf8-734106ed5592 | -8.92538 | -47.60417 | 2026-07-19 04:00:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8e8cad76-a74b-3521-928a-9c20b638517a | -7.29924 | -46.24681 | 2026-07-19 04:00:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 82d723ab-6df7-3f60-b98c-d1ec237c3553 | -8.93101 | -47.60527 | 2026-07-19 04:00:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 155bb72b-26cd-3f37-8bf9-52f13664deae | -8.93734 | -47.6025 | 2026-07-19 04:00:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7f318290-1374-32da-9bd5-4bd1e96bc1f9 | -7.29982 | -46.24355 | 2026-07-19 04:00:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ed678a69-02d0-3b17-92ff-0536643ee5cc | -8.36326 | -45.40289 | 2026-07-19 04:00:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0da7a518-1817-3a82-8ab2-01a828ecbe7e | -5.9264 | -43.64488 | 2026-07-19 04:00:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 313b383a-0b7f-3be7-b601-effed2b2c98e | -9.3449 | -40.49629 | 2026-07-19 04:00:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e1d671b1-158c-3ab8-8de4-7e6408301df1 | -7.29864 | -46.25016 | 2026-07-19 04:00:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| f10abb5d-2a59-35c8-9992-05d3299360d3 | -8.9451 | -47.60712 | 2026-07-19 04:00:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3a276e4-5d46-31c2-ab41-074bed414d58 | -8.35953 | -45.39553 | 2026-07-19 04:00:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 102a5801-485a-3d6e-b41f-a9a23f71fed8 | -8.93594 | -47.61019 | 2026-07-19 04:00:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e2d6217f-cea0-39b3-8e69-d7fc5d91679c | -8.93664 | -47.60637 | 2026-07-19 04:00:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ccfbc0da-bc6b-33ce-b033-6f3f34611a96 | -8.93946 | -47.60606 | 2026-07-19 04:00:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4c5f1db1-c207-3096-b996-e1b7e7c49d08 | -10.66674 | -44.46642 | 2026-07-19 04:00:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f42a3c1b-4e14-3ecd-acce-c908fad86c09 | -9.95692 | -48.85562 | 2026-07-19 04:00:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ccb8be21-bde7-30e0-87f4-c11c3623a7cc | -7.30512 | -46.24448 | 2026-07-19 04:00:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9b53b2bb-bb9e-33f4-b113-c90142bb8170 | -9.09674 | -50.6112 | 2026-07-19 04:00:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f8d6c69f-779b-30c2-a2fb-0d689de2ab7a | -9.38712 | -40.7562 | 2026-07-19 04:00:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 31b502c6-d3b4-368e-9108-6a1c44f89e0f | -9.59387 | -40.61136 | 2026-07-19 04:00:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 055e5eb2-812a-3261-83f8-96a950c53824 | -9.95404 | -48.86113 | 2026-07-19 04:00:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 007a7c22-fa1a-3b05-a046-f4bbe54e40b8 | -8.36441 | -45.3966 | 2026-07-19 04:00:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7096eabb-f48e-3083-9ac8-80a10b0b14b0 | -5.52953 | -45.27345 | 2026-07-19 04:00:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ce0f5d41-24b9-3648-b7a8-887a2200c903 | -10.69224 | -46.62577 | 2026-07-19 04:00:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ce49db93-3576-3e5d-b5f0-a1f103fcf613 | -9.9549 | -48.85666 | 2026-07-19 04:00:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 47f4a202-d590-30e8-a6c3-19534f210bf7 | -8.93311 | -47.60879 | 2026-07-19 04:00:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 40f23bc6-ad88-3cc2-a288-5c26b22c2d68 | -10.69394 | -46.61665 | 2026-07-19 04:00:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6672487e-0cac-30e3-9a28-7e0d57bac74c | -5.93094 | -43.64568 | 2026-07-19 04:00:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9a686ee-fb5d-341c-8a4d-3814f4ce5a8a | -8.3584 | -45.40172 | 2026-07-19 04:00:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 89f3d0bd-eaa3-3ff0-974f-41bc29f71473 | -10.71781 | -46.57336 | 2026-07-19 04:00:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7aa83fc6-7e41-351a-99ec-90d92ee968c9 | -8.36355 | -45.39556 | 2026-07-19 04:00:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| adbc4817-c0b5-330a-b12f-72c30430af38 | -10.69792 | -46.62374 | 2026-07-19 04:00:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 29f6b4e3-e344-3565-98a8-f06105f46cbb | -5.9355 | -43.64643 | 2026-07-19 04:00:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47d6f2eb-76db-3d42-8bbe-8838006e3182 | -11.60789 | -43.11197 | 2026-07-19 04:00:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 95d721ea-ae5a-3d88-92ee-5250c3866c04 | -7.11438 | -44.04662 | 2026-07-19 04:00:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bbcc3d8b-5a4f-3b4e-a431-b62cb4e5853d | -9.95604 | -48.86005 | 2026-07-19 04:00:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 83f4df47-e301-3e86-b75f-308f8f0f263f | -10.69903 | -46.61774 | 2026-07-19 04:00:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ce8172b-9ba8-3130-ae3e-87aa1bd7bf29 | -11.60327 | -43.11475 | 2026-07-19 04:00:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 40574132-45c6-3405-9f07-aa1b40450b03 | -10.69736 | -46.62676 | 2026-07-19 04:00:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a5668a44-0398-3d30-b536-684974874897 | -7.30454 | -46.24776 | 2026-07-19 04:00:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1592c383-dd33-32db-a66a-4452903aa0eb | -10.52227 | -42.39314 | 2026-07-19 04:00:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2e850f73-dffa-35a9-bfc3-4336d326145f | -8.35865 | -45.3946 | 2026-07-19 04:00:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e991c5cb-1741-3db9-881e-0a9b628d5632 | -8.93383 | -47.605 | 2026-07-19 04:00:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f20c5d05-4dc9-37ac-b7fb-1355ccc272e3 | -9.07752 | -50.59483 | 2026-07-19 04:00:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 57fb813b-59fe-315e-9433-5e35d5cd7d23 | -8.73003 | -47.8274 | 2026-07-19 04:00:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cfdb4e91-875f-3360-b966-8f78a885212f | -9.07899 | -50.59494 | 2026-07-19 04:00:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68a38e40-04f3-328b-add1-ff3bd54f1eb6 | -10.69959 | -46.61473 | 2026-07-19 04:00:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e016f158-abb6-347a-97fb-a14a1ae4806a | -6.73421 | -44.36871 | 2026-07-19 04:00:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 52406130-d55a-3efb-a7bc-80d8cf76035b | -10.69848 | -46.62074 | 2026-07-19 04:00:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 16579826-2875-3e13-b1ba-bee7aed8b7b3 | -9.08692 | -50.59035 | 2026-07-19 04:00:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 594267d1-7019-3464-b1e7-d8415a8ca6c3 | -6.6408 | -46.54562 | 2026-07-19 04:00:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| acc21235-2362-3d0c-8b8e-59c721da4a69 | -9.10349 | -50.61246 | 2026-07-19 04:00:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 580b0a2d-7334-3210-b236-111dc0405c91 | -5.73369 | -49.10289 | 2026-07-19 04:00:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f1c858e2-8216-3fe8-ac85-eb9a87fb5c42 | -7.64935 | -37.26929 | 2026-07-19 04:00:00 | NPP-375D | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 208dd512-09d3-39cb-8de0-6db4a99537f2 | -8.9402 | -47.60221 | 2026-07-19 04:00:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d0b2d555-afe1-388e-b07d-32df11c39d94 | -10.6623 | -44.46564 | 2026-07-19 04:00:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bedf8e2f-7904-38e4-994c-2a42f116f6c7 | -10.90041 | -50.32556 | 2026-07-19 04:02:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fdc3e990-7e9a-3e64-a862-a68c74c5a296 | -11.63202 | -47.95724 | 2026-07-19 04:02:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 32ac460e-6b7c-3bf3-8688-281a7f1bd849 | -12.66599 | -48.21199 | 2026-07-19 04:02:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README4.md)
