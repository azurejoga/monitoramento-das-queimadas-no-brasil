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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b133f14-23ce-3e0d-8fd1-822367b24f4f | -9.10092 | -46.66162 | 2025-10-16 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| d5a1286a-709e-39f8-a973-124bc42c4e82 | -13.85026 | -43.50712 | 2025-10-16 12:00:00 | TERRA_M-T | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d3db8edb-51b2-3c95-9d71-6c1668f684d3 | -10.83492 | -43.95273 | 2025-10-16 12:00:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 1dbeeba4-f870-3f52-9251-2c57d99695ea | -8.46602 | -44.18038 | 2025-10-16 12:00:00 | TERRA_M-T | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 113.3 |
| cacfb7ae-69e5-3211-a98e-480aa11fe26a | -13.91535 | -45.58427 | 2025-10-16 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 890a64f5-c56c-328a-9110-165911d606e1 | -8.07794 | -45.42781 | 2025-10-16 12:00:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| a6d2ac2c-4be3-3cf0-84c0-92baa9e1042d | -8.25788 | -44.0904 | 2025-10-16 12:00:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 4350a4cb-f8d5-3ee7-bbe2-00b22f25c1c2 | -9.68016 | -44.52172 | 2025-10-16 12:00:00 | TERRA_M-T | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 621d18a6-4a05-3411-b798-397e073be32a | -12.1757 | -45.05858 | 2025-10-16 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 87a00297-34ed-373a-b30a-b7ecdd99c6e5 | -8.53626 | -44.3302 | 2025-10-16 12:00:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 9fedf726-cd1e-30f3-a682-6e7ec612fa1e | -6.74925 | -44.36986 | 2025-10-16 12:00:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f305fa0b-1ec0-3249-85c1-c4a0645768a1 | -7.35798 | -44.05915 | 2025-10-16 12:00:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d8d823f1-3580-3d80-8950-103a20ef40a7 | -13.81549 | -43.35656 | 2025-10-16 12:00:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 79a408b1-42be-3a13-984f-cc13199355b4 | -12.28372 | -47.76709 | 2025-10-16 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 30.4 |
| f3f46d5d-bb44-36ba-b85d-df7ab745cc9f | -14.65465 | -42.687 | 2025-10-16 12:00:00 | TERRA_M-T | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 7ed79cb3-e21f-30fb-8364-252f7c41999d | -13.01184 | -43.0453 | 2025-10-16 12:00:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 43.6 |
| 2211884a-2ffa-367c-82f8-f0801b545f99 | -7.39492 | -39.69368 | 2025-10-16 12:00:00 | TERRA_M-T | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 43e71f67-b6a2-3794-9809-201f3384f546 | -7.93011 | -44.12202 | 2025-10-16 12:00:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 20.1 |
| e07fbb69-f8ae-33f4-b7e2-1b0ab36e7737 | -10.89182 | -47.91307 | 2025-10-16 12:00:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 9aa1c562-a0c6-3e9e-a578-0bcef964b98f | -12.74112 | -42.67178 | 2025-10-16 12:00:00 | TERRA_M-T | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 26.8 |
| 6f18156a-c3e1-3cd0-952e-a390bec1fbdd | -13.92372 | -43.49918 | 2025-10-16 12:00:00 | TERRA_M-T | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d80643a3-e068-363f-ab95-5ec60076e780 | -13.7883 | -43.61255 | 2025-10-16 12:00:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ef27e306-f315-3fcd-b098-44496f15cae0 | -8.38504 | -46.24506 | 2025-10-16 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 21.0 |
| bd218bf4-2623-3698-964e-6ac1c5d54984 | -7.66775 | -42.37173 | 2025-10-16 12:00:00 | TERRA_M-T | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 8e09f785-fa9d-31c3-95fe-2efdfa5bfcdb | -12.97801 | -47.3182 | 2025-10-16 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d017286b-ef3e-333f-b59c-f8153c9fef8a | -11.59123 | -44.07652 | 2025-10-16 12:00:00 | TERRA_M-T | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 39.2 |
| d602aeae-94a0-3c3e-93a2-679f20aeeae3 | -8.18474 | -43.32865 | 2025-10-16 12:00:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 24.8 |
| 317b8a4b-4e83-3052-bbfe-fcf10acc04a8 | -8.20373 | -43.32226 | 2025-10-16 12:00:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 42.1 |
| 41e8986b-34f4-385a-bd4e-bff686e4f489 | -11.45664 | -44.17983 | 2025-10-16 12:00:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1b032c75-8062-37d5-a63e-a28f360e3fb5 | -8.20502 | -43.31334 | 2025-10-16 12:00:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 31.3 |
| 8ad47c63-d6d4-3a04-b5c2-abcfd25a9c3a | -6.5159 | -43.69629 | 2025-10-16 12:00:00 | TERRA_M-T | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 749fe03e-ec2f-372c-8aa0-757382b88f14 | -7.08046 | -44.95077 | 2025-10-16 12:00:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| cbb4948d-1568-320b-a260-179890496db8 | -12.28732 | -47.13976 | 2025-10-16 12:00:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 274.3 |
| b7faf6e9-86ec-3808-950b-07b73e4130f3 | -8.5545 | -44.58062 | 2025-10-16 12:00:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 25f4e60b-4271-3191-8634-40200fcac53a | -13.03956 | -43.56493 | 2025-10-16 12:00:00 | TERRA_M-T | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 523d939c-2b13-344e-88a4-c6d7a89028d3 | -14.73239 | -42.79186 | 2025-10-16 12:00:00 | TERRA_M-T | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| cfc2e19c-371f-3105-87cb-62df683b60ab | -7.29062 | -42.30305 | 2025-10-16 12:00:00 | TERRA_M-T | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 9.5 |
| a439de1f-e4cf-3e26-ae5a-b57dfb868665 | -8.2461 | -43.41659 | 2025-10-16 12:00:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 28.6 |
| d512e7ca-246b-334c-a80d-94cdb55af7cf | -7.41909 | -43.76679 | 2025-10-16 12:00:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 8b2e0efa-4c0f-3894-8dca-bfd5828503e0 | -7.35049 | -43.85977 | 2025-10-16 12:00:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 177.4 |
| 91044297-2321-3b43-a3c3-a75b9b223a35 | -8.19488 | -43.321 | 2025-10-16 12:00:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 7c3f07ad-656a-30d6-956e-9e9b02bb5cc2 | -12.25873 | -47.12857 | 2025-10-16 12:00:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| cb34092c-4166-3ee6-a6c7-4ab748a9c09c | -12.97617 | -47.33006 | 2025-10-16 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 7bd91a49-d56f-3a71-87e9-99e4701d8437 | -15.21206 | -43.12022 | 2025-10-16 12:00:00 | TERRA_M-T | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 7.2 |
| b6292d01-dc81-3055-841e-1085ea9e9af3 | -12.95973 | -47.10693 | 2025-10-16 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| a91dd3a6-993a-3820-ace5-0ecde2c7c569 | -14.42384 | -42.21644 | 2025-10-16 12:00:00 | TERRA_M-T | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 29.2 |
| 2fbadc33-e38b-3688-b134-86f08c9f80a4 | -7.57618 | -43.82959 | 2025-10-16 12:00:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c0fa4db2-1da0-3530-8e3e-589a654140ba | -10.66214 | -45.30096 | 2025-10-16 12:00:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 8f9019d3-6aab-3823-a7ac-27f7630b99a2 | -11.45797 | -44.17078 | 2025-10-16 12:00:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 4ad9a600-c9c8-380f-95ae-5eaafd813065 | -9.36346 | -46.96481 | 2025-10-16 12:00:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 31.9 |
| b6118f53-f85c-3889-9528-50f963c19db1 | -12.30244 | -45.63227 | 2025-10-16 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 179.9 |
| fb269d2d-ffa6-3e1f-8bdf-538e257ed98c | -8.29793 | -43.43314 | 2025-10-16 12:00:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 239.8 |
| 175206d9-36a6-34a6-aad6-0d949a981f4b | -14.18128 | -47.95564 | 2025-10-16 12:00:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 6761096e-0251-3e0d-8c3b-923f50af3679 | -7.08196 | -44.9405 | 2025-10-16 12:00:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| db9a6fdc-529d-3992-95e4-05b84f81e1cf | -6.84917 | -44.3813 | 2025-10-16 12:00:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5be25a04-6d6e-3d28-ae22-9976a1bbba8a | -9.25016 | -44.37046 | 2025-10-16 12:00:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| c5c88883-f954-3386-8126-638613d0a368 | -7.04419 | -43.74403 | 2025-10-16 12:00:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 75c951d8-eae7-3f2a-a932-9dcb469d02ac | -8.22845 | -43.02685 | 2025-10-16 12:00:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| f065d4a2-bc99-3b09-a546-b0678c4edbb4 | -10.67617 | -45.3335 | 2025-10-16 12:00:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 17b3f7b0-2187-3c1f-8859-78e142b87e16 | -12.27064 | -47.11831 | 2025-10-16 12:00:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 6fc49ca4-6805-3d6f-a31c-3dcd74673969 | -14.42519 | -42.20646 | 2025-10-16 12:00:00 | TERRA_M-T | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 02a567b6-79e7-3828-a03b-b52f10c5020e | -7.34913 | -43.869 | 2025-10-16 12:00:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 25304d1b-9252-3756-bb6b-7684695f38b7 | -13.01056 | -43.05445 | 2025-10-16 12:00:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 55.8 |
| 7c65b515-1071-330a-ac6c-8c9252de1041 | -12.27801 | -47.77211 | 2025-10-16 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 29.0 |
| c5042556-422c-38b8-9713-cfaa57d8242d | -10.88958 | -47.92703 | 2025-10-16 12:00:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 68af0699-ca12-3596-a787-fcc9ee2d2411 | -9.25135 | -45.28263 | 2025-10-16 12:00:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 0cf60d69-15e4-366d-815a-63fefecabcf4 | -12.28922 | -47.12781 | 2025-10-16 12:00:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 32.1 |
| e4aa8540-23b6-3712-bd06-e01c1dc1cedd | -13.93129 | -43.50956 | 2025-10-16 12:00:00 | TERRA_M-T | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ddb35c76-0fb9-358b-b540-54864fe860f4 | -8.2467 | -44.04172 | 2025-10-16 12:00:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 61.4 |
| c7868f8c-1c5d-3c1e-a230-e1f2299d66b6 | -10.66361 | -45.29122 | 2025-10-16 12:00:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 81c272a6-a1ae-3374-9f00-7edeb6c54111 | -13.47823 | -43.59491 | 2025-10-16 12:00:00 | TERRA_M-T | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 43781a60-3a79-3f1e-b053-38f42636e4f6 | -6.35625 | -45.48862 | 2025-10-16 12:00:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 176f7a20-0382-3ff5-b4d1-064dd199d9e7 | -8.06668 | -45.43746 | 2025-10-16 12:00:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6b667e62-8c93-31fa-b158-691642875931 | -10.66693 | -45.332 | 2025-10-16 12:00:00 | TERRA_M-T | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 46.7 |
| 14dcc71f-d4a1-35f5-94b9-b13e41664e9e | -12.2817 | -47.78014 | 2025-10-16 12:00:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| fb7913ce-c62e-3d86-8bf6-a330958ba73d | -10.12367 | -44.58007 | 2025-10-16 12:00:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0bd65173-ddf4-39e4-b421-ccf7a199f2a6 | -9.27012 | -45.28537 | 2025-10-16 12:00:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 34.1 |
| b5f253c6-c20b-3dc2-b054-7ca6904c8c0b | -12.31464 | -45.61381 | 2025-10-16 12:00:00 | TERRA_M-T | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a5b8c54e-14eb-37c6-aee1-d5d21f21d11c | -7.18474 | -42.19448 | 2025-10-16 12:00:00 | TERRA_M-T | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 7f1a00bb-b4d6-3d50-9da4-fa8d91b1671a | -7.01592 | -43.74935 | 2025-10-16 12:00:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bd60967d-29a4-3004-87be-b083b30178be | -11.36764 | -45.28111 | 2025-10-16 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 8972ff31-b92b-313f-8939-a4bfb7eb794f | -7.65844 | -37.62049 | 2025-10-16 12:00:00 | TERRA_M-T | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 25.3 |
| 616da41b-060f-3907-99a8-9a7276e7ab95 | -7.35661 | -44.06845 | 2025-10-16 12:00:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 6ca7c397-0eb6-33ec-b143-5689749bc3b1 | -12.36334 | -42.86589 | 2025-10-16 12:00:00 | TERRA_M-T | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 72783230-b6e4-3c50-8e51-e7c5a4477076 | -10.83624 | -43.94373 | 2025-10-16 12:00:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| c79e5832-eba9-3c67-bc26-bf4a95569410 | -11.3662 | -45.29089 | 2025-10-16 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 39e25eea-d5fe-3f33-9eb5-12ded6c07667 | -11.317 | -45.24352 | 2025-10-16 12:00:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0df660a1-f34a-3b99-ade3-4d17d275d7aa | -9.24501 | -45.28547 | 2025-10-16 12:00:00 | TERRA_M-T | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 6e71f095-f817-3048-9534-6dc2f19d89d3 | -15.90113 | -43.263 | 2025-10-16 12:00:00 | TERRA_M-T | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 18c87c57-99a2-337b-be31-80c8b49f1875 | -7.10499 | -44.71768 | 2025-10-16 12:00:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 34.1 |
| c061e9a9-7957-33cf-8f1d-b8ecbf6699f8 | -6.70947 | -44.38419 | 2025-10-16 12:00:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ba97cc6b-5cbe-325c-856b-c8e105c9c10f | -11.44645 | -44.18757 | 2025-10-16 12:00:00 | TERRA_M-T | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7995e920-121c-3b1d-b06c-e76bedb8d2bd | -10.70894 | -44.42908 | 2025-10-16 12:00:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 80bb8872-6fc7-3b32-b385-55b0b65621fa | -8.47605 | -46.25382 | 2025-10-16 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| bb88508e-b2c4-3674-bda0-5c43288cae72 | -16.29795 | -44.57261 | 2025-10-16 12:00:00 | TERRA_M-T | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9c872b84-a992-3f0f-9e6a-f123e074311e | -7.47885 | -42.13629 | 2025-10-16 12:00:00 | TERRA_M-T | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 24.4 |
| 8cc6db47-52a0-3d15-a319-940327970700 | -7.75479 | -42.47133 | 2025-10-16 12:00:00 | TERRA_M-T | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| e9cba46c-3141-3aca-91e8-5a3e494667ec | -13.90761 | -45.57716 | 2025-10-16 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| a1236dea-ee4b-3e51-8b1a-02d81e369381 | -13.00294 | -43.04404 | 2025-10-16 12:00:00 | TERRA_M-T | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 8e7d361b-c4cb-3b36-8054-9a49716f9a70 | -10.12784 | -44.55197 | 2025-10-16 12:00:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 24.9 |


[Clique aqui para ver as próximas entradas](README88.md)
