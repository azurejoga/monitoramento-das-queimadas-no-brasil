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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b8a5422-cded-3d35-838e-2d55cd8d12b9 | -10.22599 | -46.50235 | 2026-06-28 04:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75cb1cf6-06ef-359d-be9b-69dbf69c657f | -10.27747 | -44.38188 | 2026-06-28 04:12:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d32fa32b-36cd-355e-924a-5f04c245dd5f | -10.1017 | -45.77229 | 2026-06-28 04:12:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13ebb47b-840b-3f9f-b2b2-39cbef198f70 | -10.22976 | -46.50301 | 2026-06-28 04:12:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48ec18df-bf22-3f8a-a786-08e5216012b9 | -11.60363 | -43.11273 | 2026-06-28 04:12:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 4d65a736-a39c-3f86-8694-85311c076b47 | -9.4617 | -48.14172 | 2026-06-28 04:12:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 409eb330-429a-3749-a253-846252bde95c | -6.99589 | -45.00907 | 2026-06-28 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 615dfe08-1d8e-31be-bfd3-02fd84e34548 | -6.99952 | -45.00968 | 2026-06-28 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0815a9f8-08bc-3194-87bf-182fac9c132c | -11.6075 | -43.10976 | 2026-06-28 04:12:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 025f4a2b-7ccf-3eb6-b110-dec888ce6c1b | -10.84156 | -49.13273 | 2026-06-28 04:12:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d7786086-3db1-3cbf-b366-b799f5cdb194 | -10.10097 | -45.77656 | 2026-06-28 04:12:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5cbb98a-a20d-3a09-81ab-64f516e01254 | -11.39898 | -43.24482 | 2026-06-28 04:12:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c831a275-31ab-32a6-9e9b-42d426299452 | -7.00021 | -45.00542 | 2026-06-28 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6defb62e-37e5-325d-a640-c10b8639d96d | -7.0009 | -45.00121 | 2026-06-28 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2d73e4b-07fe-3721-b7e0-db7822f7fd1a | -6.98268 | -42.89053 | 2026-06-28 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| bf838131-c902-3394-a8ec-70b12b6ac13a | -10.84678 | -49.12899 | 2026-06-28 04:12:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5aca10c8-7f3e-3d89-a6e8-6713c30cc055 | -11.52369 | -54.80008 | 2026-06-28 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 230ecd9a-4839-3666-9ae2-47225be4d0ee | -12.16564 | -57.13413 | 2026-06-28 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6883811c-ecc8-3816-9608-41c5de65bd62 | -11.20745 | -54.30523 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 91cd7e16-df35-38c9-80da-54786afb92c0 | -12.18815 | -52.9116 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 92deef41-f5cb-3cf6-bff5-9c04aa31112b | -14.86427 | -43.58923 | 2026-06-28 04:14:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f205ef56-1501-3da7-8555-4a5e170ff42d | -17.70156 | -46.77398 | 2026-06-28 04:14:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6c9055bf-0003-3b17-94ed-7d5e8814a4e0 | -11.21168 | -54.31614 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 5a6d3650-663e-3999-ba07-586064581094 | -11.21448 | -54.29856 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| bce11ee9-ebda-366c-9317-84134f24e973 | -12.18629 | -52.89184 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 73857029-a54b-3fac-b3ba-56c7c27fccec | -12.18441 | -52.87226 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 59b48229-bfd6-3543-9b01-3b5a9bc77d32 | -12.17303 | -57.14977 | 2026-06-28 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b44cac3f-857b-3471-a53b-b62f98b2063f | -12.08776 | -52.00709 | 2026-06-28 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d9e4aa6d-592a-396c-b48a-1cecece17f83 | -12.18919 | -52.87707 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| baf5b4e5-8b15-308c-ac5a-5568d98cc574 | -12.08254 | -52.00601 | 2026-06-28 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36b99ca4-ccf9-35b3-a259-491b52ee6ae7 | -11.21964 | -54.30456 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dfb7bfee-af48-3d54-8f8a-319e109cd4c2 | -12.19878 | -52.88663 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 83d477ad-e2c6-39d4-aecd-d7623100500d | -12.18962 | -52.90413 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 105a8cc1-ab59-34ed-92de-f6b405a3155a | -11.52477 | -54.7949 | 2026-06-28 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 6f8087ff-784a-3eb1-b20a-e54c313889b7 | -12.08568 | -52.01708 | 2026-06-28 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6603ea38-c7ff-3fd3-8b6c-61ac9dbf7402 | -13.51931 | -47.57221 | 2026-06-28 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4032a1e1-798a-34a0-a66f-4c9c1559aac6 | -11.21285 | -53.82018 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 665ae444-a9b9-3eb8-8279-cc614af0da8f | -17.35064 | -42.62953 | 2026-06-28 04:14:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 9b3f57fd-1184-3523-8afc-1936a1db6f97 | -12.16264 | -57.14847 | 2026-06-28 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| caa82d0d-51fc-31e6-b6b3-2e1d2b5dee53 | -11.21969 | -54.30773 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 13d22dd4-7373-3ad0-b361-06d6abbabd0d | -12.23566 | -56.55614 | 2026-06-28 04:14:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ddb46963-0cca-3356-a1c6-a6aeac29d8d6 | -12.20716 | -52.87304 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| c27a3809-fccd-3c57-b1d9-ae5c89711659 | -12.27479 | -50.10481 | 2026-06-28 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90ba5b3b-011a-3e8f-8fa4-287893209756 | -12.18721 | -57.15276 | 2026-06-28 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 54b5a44e-bd0b-3652-a1c6-29d4cad3f230 | -11.32071 | -54.4651 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 15ac838b-a5d8-32c9-b2c8-cb3eeed25723 | -13.37091 | -44.21014 | 2026-06-28 04:14:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6705e0dc-e4d3-3fd2-a4b7-5ea524418f17 | -12.20645 | -52.87669 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 05a3f899-2375-38f4-9709-9b2549d95bbd | -17.97377 | -44.56705 | 2026-06-28 04:14:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e488ce5c-3b1a-39b7-b814-5ebf9e1f025a | -17.34446 | -42.62466 | 2026-06-28 04:14:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b3fc015f-a4f1-30e3-918f-e4be410fd837 | -12.19326 | -52.88553 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b56499a7-6250-3d5c-859e-96dfde2a8ea6 | -11.31973 | -54.46994 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 554c887c-18e7-399f-bc30-698ca566b723 | -12.09049 | -52.02134 | 2026-06-28 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 84001e41-2b59-3cf3-8396-e2f0ddbafd84 | -11.5221 | -54.79281 | 2026-06-28 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| a3304ce8-5649-30f4-9180-e9bd51d8a291 | -12.27847 | -50.11052 | 2026-06-28 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4ccb337-83ee-397b-8997-9ec3c609b923 | -12.20094 | -52.87558 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 32a4757b-77a6-30f7-8ddf-cc0e40eac317 | -11.20932 | -54.29569 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 27fb367a-61d2-3d4f-a7e1-06891ee0dd05 | -12.16441 | -57.15535 | 2026-06-28 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 997a8aca-bdae-3bfd-9523-b5a5d9c9422f | -12.20166 | -52.87191 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 9c5eb55d-b5d7-3e30-ba22-9f2c2162db03 | -12.08698 | -52.01051 | 2026-06-28 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| da4be2c7-c491-3a66-b919-343118ded3c7 | -12.20237 | -52.86824 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 9d0c36c3-41f3-3405-8c29-16217abdc017 | -12.23012 | -56.54844 | 2026-06-28 04:14:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 21d1b29d-8962-3bcb-a77a-2ea338a22bef | -11.31019 | -53.94881 | 2026-06-28 04:14:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53f30407-7414-3f68-af41-918082e2269e | -12.17858 | -57.15842 | 2026-06-28 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| aaad0a42-1a9c-3f25-9470-4a2ae6ace75a | -12.08633 | -52.01378 | 2026-06-28 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 14719887-a3e6-3d14-9b63-e9b78e83675a | -17.3512 | -42.62577 | 2026-06-28 04:14:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 3f86114f-ba7d-33d9-a2f6-1d2634f93ed0 | -12.19659 | -52.8978 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b45d8daf-4912-3b25-94ce-37e08a011f5c | -12.18169 | -57.14395 | 2026-06-28 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 46b585b2-7568-3a6b-9b78-f77de90daec7 | -13.29397 | -43.55037 | 2026-06-28 04:14:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e5991417-1c1e-398b-b25d-20ccc80194ab | -12.0859 | -52.01693 | 2026-06-28 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f1704930-6114-3877-bc2c-19fab78ed8ce | -17.30848 | -42.65718 | 2026-06-28 04:14:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e529313e-117d-31cf-9958-29d14aed0994 | -12.20022 | -52.87925 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 0fbabd29-1b0c-30cf-aee6-d8ec2d63f18c | -17.70574 | -46.77056 | 2026-06-28 04:14:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 23cc4529-2271-3db4-9136-a31ef94d9a6d | -12.79032 | -54.88363 | 2026-06-28 04:14:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a10561a9-a3f8-319d-9c88-4c401dac762e | -12.08652 | -52.01363 | 2026-06-28 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d9654e82-2b8d-35e1-bec4-b17c141a84d6 | -12.18077 | -52.89077 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b8e8a1ce-8045-340a-9e66-e3eb2168c543 | -12.09282 | -52.00838 | 2026-06-28 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 25a86c57-0181-3fcc-a909-7d986d4b952e | -12.18847 | -52.88075 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5037cfd2-63cc-36a4-8710-4df78927b700 | -14.04132 | -46.33289 | 2026-06-28 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0356b2bb-c8ad-3a94-baa4-f09f42495ca0 | -12.16903 | -57.13388 | 2026-06-28 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7df4c3d1-a56d-3288-8540-d3fb447f181e | -17.30478 | -42.64915 | 2026-06-28 04:14:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 309c7710-54f0-3909-9e29-a2bb5078c0c7 | -10.9314 | -56.85889 | 2026-06-28 04:14:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b34a9e38-4d84-30fc-971c-c767a9d84284 | -12.17786 | -52.90557 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| df06fe37-3e23-39c3-bb7e-33235306f71e | -12.16413 | -57.14138 | 2026-06-28 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cb96aea3-3dfd-30a6-bc93-deada99963e1 | -12.08504 | -52.02039 | 2026-06-28 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 45ea546a-d810-33fa-8f51-ee1cffaca8a4 | -12.18368 | -52.87597 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a92d9538-8eae-3d45-89c0-c5ee20c6740b | -11.212 | -53.82457 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| d1a97208-5fa7-30ce-9290-e358af4c4026 | -17.3484 | -42.62145 | 2026-06-28 04:14:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 686b6c85-3637-3987-b806-43e864f11e99 | -12.23549 | -56.55611 | 2026-06-28 04:14:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d6f04651-9571-32b9-a1f4-fd196158b099 | -12.08067 | -52.01592 | 2026-06-28 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b37c569d-8fb8-3080-bd55-6554432dc113 | -12.26605 | -43.51818 | 2026-06-28 04:14:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db983953-9472-3684-a422-d8879ff0be95 | -12.19137 | -52.86599 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 56a0b976-416e-309d-8fcb-2b9e4b29df09 | -11.52731 | -54.79942 | 2026-06-28 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 81f55a12-1b75-3ef7-b893-a775744ab1e8 | -11.209 | -53.82286 | 2026-06-28 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| a96a1619-e6c0-3c82-ba5a-d116b3cf4475 | -12.15856 | -57.13262 | 2026-06-28 04:14:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 92df9e60-1ec1-31d3-8d11-e41afb45bd75 | -12.09173 | -52.01477 | 2026-06-28 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4994d126-b639-3d06-99ba-261fe35cd326 | -12.09296 | -52.00822 | 2026-06-28 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9874b026-a1f9-35fd-9282-11f153c2fafa | -17.30702 | -42.65716 | 2026-06-28 04:14:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 1472072d-e75b-3442-b8aa-eca6c36e1227 | -12.22878 | -56.55478 | 2026-06-28 04:14:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 79c5a79a-4a21-3da3-8935-dab0afd57edc | -12.1815 | -52.88708 | 2026-06-28 04:14:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f0c304d7-3ba7-3b88-8c7f-99062ceea01a | -13.45273 | -44.04334 | 2026-06-28 04:14:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README12.md)
