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
| fa8493c7-5a38-32ef-b6ec-66f45e32480b | -7.75573 | -44.61583 | 2026-06-26 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| aff70ff2-0396-33e5-8bcf-501cadd6f2d5 | -6.97247 | -42.89598 | 2026-06-26 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 1843ef92-61c9-3353-a6e0-d1ca6b99b997 | -6.3064 | -44.64618 | 2026-06-26 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6cc07cde-3812-3527-b619-fadade7a4825 | -12.75332 | -44.49536 | 2026-06-26 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a13463e-560c-3f39-a41a-9dfaed1f5517 | -11.91633 | -43.40303 | 2026-06-26 03:55:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02fb09dc-43fc-38ba-b1b6-0d0614bcb456 | -12.75725 | -44.49606 | 2026-06-26 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| cf29f39e-1483-3020-8cac-904738a71c91 | -8.9583 | -40.14406 | 2026-06-26 03:55:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b37f6e90-8ba4-3229-a33c-e67139cb21b1 | -9.19074 | -45.32299 | 2026-06-26 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c455602-7412-306e-a7ff-71d2be7776db | -6.30496 | -44.65487 | 2026-06-26 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 443ce8c7-a8db-344b-87bc-f2541f13dcfb | -6.50503 | -42.22335 | 2026-06-26 03:55:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 9ce3153b-9865-3a24-adbd-319e16d98bd1 | -8.00876 | -49.64819 | 2026-06-26 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9afe984e-2220-369f-abf9-61c66f12c0e2 | -8.01305 | -49.64382 | 2026-06-26 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| be09ee9e-87e8-35c6-ba6d-cf58aedd3af4 | -7.73961 | -44.17831 | 2026-06-26 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a3df8633-4635-363d-8871-f5eadf2f9df2 | -7.56909 | -45.88017 | 2026-06-26 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a9332157-1ec0-3403-9d3b-06e33f71e652 | -11.3914 | -47.81482 | 2026-06-26 03:55:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4dc44441-a1f8-305e-8392-291803f31dfb | -9.07845 | -44.76641 | 2026-06-26 03:55:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8a59f0e1-c737-3142-aa1a-73394b58b019 | -8.23406 | -47.11908 | 2026-06-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4773dc11-41e6-3529-b6dc-645a9021f1c0 | -12.75424 | -44.49018 | 2026-06-26 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 2c92be9a-4803-36c9-a235-80b59c25cf6d | -7.73479 | -44.18142 | 2026-06-26 03:55:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5f54dc78-36da-3f85-9af8-0d7cd8aca706 | -7.9365 | -47.81371 | 2026-06-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 245e07fc-09b8-3c5c-9fea-b6bef5d4efb2 | -8.85691 | -46.92795 | 2026-06-26 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4aaede71-7cbd-3b0c-9e54-6b9b9366a6a0 | -12.51584 | -48.26587 | 2026-06-26 03:55:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53f9f61e-fdf0-3553-a21a-c1af6518aea4 | -10.10992 | -47.56322 | 2026-06-26 03:55:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e99a1525-2bbc-3b12-94a6-8645ee3602b2 | -7.74643 | -44.61842 | 2026-06-26 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 0a550fb8-92ca-3040-9c9a-8b91899c637f | -10.56924 | -47.20037 | 2026-06-26 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ce8bf3d-a78e-31cf-b3c0-ecdf7cd52a72 | -12.74938 | -44.49467 | 2026-06-26 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 454b346a-2d47-311c-a184-090b8ebcdb16 | -6.59516 | -43.8995 | 2026-06-26 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45f385a0-ac17-389c-a536-2f36f751c0a9 | -8.84985 | -46.93162 | 2026-06-26 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7df2d91d-b698-35f7-93c9-83998c879ccb | -11.47665 | -47.34604 | 2026-06-26 03:55:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 526457ca-1dbd-3929-bceb-bb66b150495e | -9.36487 | -50.54254 | 2026-06-26 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 495b280e-09e9-3a5f-aa9c-e2a21c527493 | -9.73534 | -47.89538 | 2026-06-26 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bffe4520-e83e-324e-bd19-e756a6ffdd8d | -9.80389 | -48.91824 | 2026-06-26 03:55:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d2e2b77d-d6a3-3f14-b039-f24194a94156 | -11.77444 | -46.45406 | 2026-06-26 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| cbbbbec5-99f4-371b-b71e-b67f93de34cb | -6.30568 | -44.6505 | 2026-06-26 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3aefd9dd-bf1d-3100-adc1-5a53a831bf15 | -6.50022 | -42.22472 | 2026-06-26 03:55:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 050af5b0-3e35-37a6-a3e1-7a43c7ba74df | -6.99832 | -42.76457 | 2026-06-26 03:55:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4a07dfcf-e80d-3a5b-9052-ff5357940dfb | -9.91115 | -45.52876 | 2026-06-26 03:55:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| fb37f8fb-67ac-32b4-9a24-d1f65c83aad7 | -11.38031 | -47.81875 | 2026-06-26 03:55:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02c69264-4339-3cf4-83a7-39040b0a74a5 | -8.13994 | -47.88449 | 2026-06-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ce1f0777-6c85-31a6-ae49-5ae670c2db07 | -12.86671 | -44.3319 | 2026-06-26 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3aa733bb-66c4-3ddb-95ff-38ce4bf583d0 | -12.87058 | -44.33266 | 2026-06-26 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7d1b5e0-887d-3683-8e51-9e8227970db5 | -8.68145 | -47.85463 | 2026-06-26 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f072177f-9904-35c7-8c23-7fe58107c136 | -12.74333 | -44.48617 | 2026-06-26 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2d235d39-44db-3ffa-8de6-7709393d13ad | -8.06333 | -46.38371 | 2026-06-26 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf21c7b8-1b70-32df-a391-60cc9e5ee1eb | -7.93822 | -47.81396 | 2026-06-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b5ebf78-88d3-38b1-a045-f4fda1798930 | -6.50546 | -42.21607 | 2026-06-26 03:55:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 687ba69a-a71e-388a-b7a2-4b94fbcfe099 | -10.29192 | -44.69258 | 2026-06-26 03:55:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 80d244ae-4351-30c5-af35-056cd3cbeb90 | -7.57379 | -45.88102 | 2026-06-26 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4856870-3fe5-336e-82ce-66ae932d22ac | -10.57023 | -47.19499 | 2026-06-26 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80b29b12-e30d-3f10-9a91-9a9e9d5fab89 | -10.1287 | -52.11113 | 2026-06-26 03:55:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cf842f5a-c8dc-3741-9b62-427f614807e7 | -11.63638 | -52.86138 | 2026-06-26 03:55:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7159d7d0-1138-3470-85e0-c241b95627e4 | -11.22446 | -46.40939 | 2026-06-26 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7a874da-ee6e-3727-aaff-81b8c3165044 | -12.51801 | -48.28185 | 2026-06-26 03:55:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8fb8fd40-7e92-3ee4-802f-e99115c60d65 | -9.37151 | -50.54691 | 2026-06-26 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 5067b876-5da0-3b2c-91cd-6db0b57a16a0 | -6.97636 | -42.89658 | 2026-06-26 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 1b00d553-df8f-3448-86f6-1c188a2f9139 | -12.74638 | -44.49205 | 2026-06-26 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d684e9b6-58d8-3f36-a7b1-edfdcb54a01b | -11.38693 | -47.81091 | 2026-06-26 03:55:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5410ce04-5f31-3905-82d3-40b50e7e4c40 | -12.75514 | -44.48827 | 2026-06-26 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f7a86758-2f35-3cd5-88f1-fef0091bbb3a | -8.8488 | -46.93765 | 2026-06-26 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d069368a-1dcd-309f-94f8-b3933ff1874b | -8.84575 | -46.93322 | 2026-06-26 03:55:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 806a22ff-d4d7-33b6-89de-203d9b286f0c | -9.0129 | -47.99679 | 2026-06-26 03:55:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d6b7be2a-7851-3c7a-9bc9-41d8da44046f | -10.54134 | -47.71283 | 2026-06-26 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3094cb1-be6e-370a-afc7-d1a0891c7ace | -12.44624 | -44.75361 | 2026-06-26 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ed77dab-2cea-3b24-a24f-b59eefbbd11d | -11.3753 | -47.8178 | 2026-06-26 03:55:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47c6138c-63a1-3953-a2e8-6eb9729fa7f1 | -6.97164 | -42.9009 | 2026-06-26 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| c0e9ef25-a837-3576-8049-946beea4aa56 | -10.12579 | -52.10958 | 2026-06-26 03:55:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35379f51-5980-3e5d-b576-08b23845badc | -12.44204 | -49.57824 | 2026-06-26 03:55:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 020f500b-4d8d-34ce-8d68-c215cef5b324 | -9.69727 | -47.69618 | 2026-06-26 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7fce4d10-7a45-3874-b83e-533226d74afd | -8.01826 | -49.64914 | 2026-06-26 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d63e93fe-6118-3b77-8552-2fcdfec22814 | -8.12997 | -47.88944 | 2026-06-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4f3be06f-8177-3919-9d81-b1618303a638 | -6.30622 | -44.64546 | 2026-06-26 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8cb7ec9c-d807-3b94-b8bf-360c7e98e25e | -8.01645 | -49.64027 | 2026-06-26 03:55:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4aec8309-512a-3e43-a49d-f24db4d1930e | -12.44132 | -49.58197 | 2026-06-26 03:55:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 081230c8-6f43-32cf-ad21-6cea3c2263f3 | -10.75848 | -49.11304 | 2026-06-26 03:55:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0bb9984f-48ba-323e-8ad8-84b5baf6ed5a | -9.70241 | -47.69701 | 2026-06-26 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05857809-1ec5-34f8-8feb-91dc661230fb | -10.75294 | -49.11211 | 2026-06-26 03:55:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| efa872e9-c1ac-319c-bbd4-70f4d8a35fd6 | -8.86094 | -46.92641 | 2026-06-26 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc514679-427a-3a95-bdd0-95a13f076ff6 | -17.97334 | -44.57099 | 2026-06-26 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea648558-a375-382d-9f02-56476735de4e | -14.84216 | -48.13414 | 2026-06-26 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f0d922d9-8c7c-3bca-8e06-1adc6b724bef | -13.73594 | -54.05641 | 2026-06-26 03:57:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 30022dff-cd2f-3a3d-95f2-8bc028f8ed54 | -13.58572 | -46.2776 | 2026-06-26 03:57:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1bc77a06-c61d-3d89-9fdf-32af5d143df4 | -14.21024 | -45.62692 | 2026-06-26 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 268fb2ed-ae6a-3a53-899e-d31e429a4140 | -14.19584 | -47.68343 | 2026-06-26 03:57:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 453ca02f-55db-36e9-8643-7c049810ca19 | -14.84555 | -48.1167 | 2026-06-26 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ae3db296-5a3c-33b0-8e41-1d5dc36d820d | -13.92881 | -47.34184 | 2026-06-26 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eb1bc0fc-ed49-3ba6-8d1d-11f887c39941 | -15.59657 | -48.35493 | 2026-06-26 03:57:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5fd63601-c2b5-3ee7-9b5f-59864f345f9e | -13.05948 | -53.35849 | 2026-06-26 03:57:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 411996fb-cf47-30c2-80eb-157743c6672e | -14.83852 | -48.12722 | 2026-06-26 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81d43e5d-8f11-3bf0-af9a-954f630bad90 | -21.30479 | -40.99286 | 2026-06-26 03:57:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 293bc03b-625b-34cc-9673-2c69cf5985a1 | -21.30203 | -40.98856 | 2026-06-26 03:57:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4ad34bfa-11f7-338a-a79c-66a90b0277b4 | -14.05404 | -45.40224 | 2026-06-26 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 031fd3a9-8728-3467-8b55-6f9115be491d | -13.86964 | -47.12664 | 2026-06-26 03:57:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 480a7bb6-83aa-32ce-913b-0af5865a1145 | -21.30147 | -40.99228 | 2026-06-26 03:57:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ad149525-ca03-3b9b-a352-cb9b86d27b71 | -17.97411 | -44.56652 | 2026-06-26 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e18ba58-ff32-371c-9824-8c2b3a56cdc9 | -13.87981 | -47.14849 | 2026-06-26 03:57:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9cd200d-66ed-3488-b179-8e57c82c728f | -14.69506 | -46.14627 | 2026-06-26 03:57:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2af60f16-c3bf-3132-a832-2c85cd42feef | -13.72898 | -54.05466 | 2026-06-26 03:57:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| c5f16969-a5ca-37e9-a065-6863230286b7 | -14.69432 | -46.1503 | 2026-06-26 03:57:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46365e93-dc30-339f-a8a9-f5b7693515fd | -15.60134 | -48.35609 | 2026-06-26 03:57:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| bf059b2a-8ff7-3669-92c3-8f4a6fa6fc3d | -13.72932 | -54.04075 | 2026-06-26 03:57:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |


[Clique aqui para ver as próximas entradas](README6.md)
