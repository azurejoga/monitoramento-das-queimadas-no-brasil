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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a44591e-e81b-3a40-b3f8-a2a605dfe6e9 | -6.6623 | -40.911 | 2025-10-06 04:25:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 05e1c38d-4a8d-3429-80c1-e3ddbdaaae4c | -7.74836 | -42.54307 | 2025-10-06 04:25:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f62905fe-9f06-343a-8290-deb789f4fa33 | -7.0683 | -45.12241 | 2025-10-06 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8861ce82-fb46-30e1-a2e4-74e55058648d | -5.29639 | -42.55158 | 2025-10-06 04:25:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 160c4c87-ff91-3d70-ada5-06e584bc9025 | -7.25783 | -46.96399 | 2025-10-06 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e173c96-09bb-3bca-9170-f120248c49bb | -6.55089 | -47.85413 | 2025-10-06 04:25:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a5bf3e05-299e-39b3-9d94-47bb07cbfdb9 | -8.87149 | -47.60886 | 2025-10-06 04:25:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88a503aa-0578-34b7-b006-4e60dd177992 | -3.69831 | -49.2276 | 2025-10-06 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7402ea64-19e4-3597-94a9-64b3014cb980 | -5.46764 | -43.25033 | 2025-10-06 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 019ff5d0-3bf5-38d7-81c6-7b1da43ef058 | -8.62411 | -46.32012 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d5513269-6919-3af0-b62c-23e76f44f8b1 | -4.74832 | -44.44151 | 2025-10-06 04:25:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e28b3a9-abcc-3d04-8354-88d3221431c9 | -6.64831 | -42.77246 | 2025-10-06 04:25:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 71991353-758c-307c-b1ad-e6b1c55a38c6 | -6.36861 | -44.31231 | 2025-10-06 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 18fc1a10-ff09-3fa2-b160-315eef0805ec | -7.66469 | -45.44399 | 2025-10-06 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f2dd4419-e7ed-35ac-9cc6-361fa847b50d | -6.55484 | -47.85103 | 2025-10-06 04:25:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ff7579dd-d82c-399f-9d64-42270a781e5e | -5.648 | -45.9667 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b17f9f64-7a65-3295-b176-3ffb262ecfc5 | -5.76484 | -45.75918 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ef0d4a0-41ca-31f3-9cb6-8be5770cd8db | -6.25372 | -44.26112 | 2025-10-06 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e21c3c64-640e-3514-80a5-cb1a38d754eb | -8.8748 | -47.60939 | 2025-10-06 04:25:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1b249ef-f1fa-3c82-af27-ad1cf9bdb1bc | -8.88362 | -47.61798 | 2025-10-06 04:25:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00ff5770-a3b3-3423-a663-91c9454ec060 | -8.61239 | -46.26491 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0a4c8354-5d77-35ea-861f-151f42791ff7 | -7.02914 | -42.30058 | 2025-10-06 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 17a6d061-308a-3622-b498-8f62a4c7d410 | -5.28474 | -45.17242 | 2025-10-06 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 235e0478-2ceb-3c41-b405-1f129b3e555f | -6.32652 | -41.62202 | 2025-10-06 04:25:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d9ec5d9d-9f75-3a88-a707-2015ee8ce279 | -4.36447 | -50.85551 | 2025-10-06 04:25:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc6cd4df-868d-3f69-8a0d-7cec33c1794e | -7.70343 | -46.27029 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 60cd8dea-e25c-3e08-8a16-48bcc1bb9ccb | -5.33457 | -47.28421 | 2025-10-06 04:25:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e57813b5-c026-31f4-a998-9d8878e043d2 | -6.7951 | -46.04878 | 2025-10-06 04:25:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a162db71-aefb-3394-be7d-f7cf2b0b7353 | -5.22564 | -42.44753 | 2025-10-06 04:25:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 22426758-8eb6-3efe-bc5d-06ad0519bb0d | -8.64166 | -46.3193 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45b6b270-2e84-3edd-9dd1-240151164ce3 | -7.22001 | -45.8992 | 2025-10-06 04:25:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ab3b71c-98bf-340a-9608-23d732d7e52c | -5.3279 | -47.28312 | 2025-10-06 04:25:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4b79811-9661-3b49-a093-e184d3b54be7 | -6.34985 | -43.81251 | 2025-10-06 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| da573609-8381-3afc-8f67-6349602352e8 | -6.3986 | -53.26436 | 2025-10-06 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2cfdf501-cf42-3fda-b464-684e26fee312 | -6.70551 | -42.18333 | 2025-10-06 04:25:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| fc8db3b4-ea32-3ac5-bf23-edb8e15502f8 | -9.12052 | -47.43422 | 2025-10-06 04:25:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 08dda7b9-d254-37ba-af16-d2fe302c971b | -4.94321 | -44.58873 | 2025-10-06 04:25:00 | NOAA-21 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ebb5b865-0316-3781-a6d4-9be50bfd0cf6 | -5.26062 | -46.48322 | 2025-10-06 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2c8884a-7faa-362c-b824-61c7c137af64 | -5.43278 | -45.68574 | 2025-10-06 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29736e67-fc6c-3cc8-87d1-8267cdf39355 | -7.41866 | -46.50456 | 2025-10-06 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df6a8eb3-0645-3ff0-ba0e-de2e668d0592 | -7.05516 | -41.44344 | 2025-10-06 04:25:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0bb646db-1b84-30f1-bee5-9023e95ae8e8 | -5.33419 | -42.64746 | 2025-10-06 04:25:00 | NOAA-21 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e328a2f1-7a8a-32e1-a965-c5de7ada3c18 | -9.31693 | -45.99851 | 2025-10-06 04:25:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4acda6f-1979-3008-a2f8-f0c7ca10a214 | -8.19663 | -44.17171 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c5380cea-dd18-3ab7-9d7a-04f61d432917 | -6.72809 | -42.16263 | 2025-10-06 04:25:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9fd03caf-00db-32f9-916f-862b086c6f7d | -6.69815 | -42.15384 | 2025-10-06 04:25:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b4f95fc4-f3b2-3cdf-a40b-d622bb26f367 | -8.48401 | -45.64354 | 2025-10-06 04:25:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 059dcde5-8590-3b98-965d-805d5420890a | -8.68136 | -49.4701 | 2025-10-06 04:25:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f744e5c-c216-33e5-9308-3cb57a17f58b | -6.7595 | -42.23636 | 2025-10-06 04:25:00 | NOAA-21 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 55f97f09-6538-3c29-9e77-64dc06b8acc6 | -8.551 | -47.6758 | 2025-10-06 04:25:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 927d2cca-e9fc-3567-80c1-79dbdb0be8d9 | -7.0176 | -48.22374 | 2025-10-06 04:25:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0cb5ea9-acf6-3412-9896-4812d9768acd | -8.17479 | -47.66561 | 2025-10-06 04:25:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1cd2cef2-da52-3ae8-9c8f-445685c3b895 | -5.71138 | -42.62767 | 2025-10-06 04:25:00 | NOAA-21 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c8991e82-6de9-34cc-bb75-8bc8ed0d6a68 | -7.44312 | -49.66165 | 2025-10-06 04:25:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1400936-087a-3017-86e7-74a54de0ac3e | -5.43791 | -45.73948 | 2025-10-06 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e4ba361-1369-368e-9153-f95453b352f1 | -5.41563 | -41.35016 | 2025-10-06 04:25:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| accbd55d-12fd-3d92-af5f-600007aec06a | -5.73973 | -45.50737 | 2025-10-06 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c980296-0d84-3de9-8c24-d1352cbb1157 | -7.42094 | -46.53321 | 2025-10-06 04:25:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4461543d-a820-3b1a-9001-4184a00e29e9 | -7.36261 | -45.24107 | 2025-10-06 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 29d47deb-138f-370a-a6e1-a7ba78fd8016 | -5.03708 | -42.85972 | 2025-10-06 04:25:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 83de80f4-6cfd-3bf8-86b3-685950a2c7b2 | -6.32332 | -41.61641 | 2025-10-06 04:25:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a4e53f67-412b-3f4a-b346-ab3c5409c1d2 | -7.82028 | -47.38953 | 2025-10-06 04:25:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d05f24ca-3d1c-345e-af41-46b49bc7a99d | -5.47998 | -43.26452 | 2025-10-06 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 60289e08-d9cb-3078-bd0f-ffd907f0cfe2 | -4.25175 | -48.57301 | 2025-10-06 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 32cb2d34-d7c8-3ea4-88c5-cc68eb82397e | -6.63486 | -41.98127 | 2025-10-06 04:25:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 919ef1c7-a26f-3016-b068-e7834e43a0c1 | -8.19901 | -44.15603 | 2025-10-06 04:25:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| beeacc6e-3175-3582-8ada-5d494ec9b537 | -7.78473 | -42.61008 | 2025-10-06 04:25:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 81a8e02e-ad52-3a57-9a79-2c6609045eb5 | -8.53567 | -46.36682 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ee81d5e-5036-372c-9423-d5cf994a15fb | -5.81265 | -42.50418 | 2025-10-06 04:25:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 4a32499e-af2f-300e-af65-0ccc9fd6a44d | -1.12229 | -53.05119 | 2025-10-06 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 047a2f37-5f4d-37c1-81e9-8118e50e545c | -5.56999 | -45.59047 | 2025-10-06 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87f07810-46b1-3c6e-9e6f-fb4a4462c3f0 | -8.56059 | -46.2496 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5a3e7e2c-2fc6-3668-b0f4-269808e90d17 | -6.06772 | -42.54583 | 2025-10-06 04:25:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ac4ba6a1-9642-330d-85e8-cc574ab8551c | -7.03146 | -42.7593 | 2025-10-06 04:25:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 54a606fc-8859-3de9-b267-c6ae270bac7a | -8.18834 | -46.99598 | 2025-10-06 04:25:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ecd4bd70-c7c5-36e0-bba2-d9b0046a3f4b | -7.095 | -45.0976 | 2025-10-06 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c6cbfee-d9da-3bde-8e83-1f6cc3c419c3 | -8.52698 | -46.401 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb7594b4-8cba-3017-a286-ccf97c329380 | -7.20316 | -46.85597 | 2025-10-06 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e29ed045-f3a4-36c6-9387-d183bf5f5cc9 | -5.49383 | -42.80799 | 2025-10-06 04:25:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f157c282-7c30-3cec-8986-e64ffd10d6a3 | -3.43568 | -43.43914 | 2025-10-06 04:25:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66367875-608c-3569-bd08-b462f26055b7 | -7.46986 | -43.06006 | 2025-10-06 04:25:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 91abb1c3-c373-3fd2-b135-0aea0efb0e27 | -5.47987 | -43.16975 | 2025-10-06 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6163de42-3138-3300-863e-f3ca0b97a43d | -6.33131 | -42.99134 | 2025-10-06 04:25:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1ec018c6-3eee-3bbd-88c4-0f3e7de74aff | -7.63329 | -43.06747 | 2025-10-06 04:25:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 210a6c52-fe32-36af-9f5e-44a84f30bcf3 | -7.71244 | -42.38922 | 2025-10-06 04:25:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 2eeeda61-b56a-3c55-a76a-0d0fcff13ae7 | -4.23067 | -46.75357 | 2025-10-06 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d364d0e7-444f-39cd-965d-3d894673d49c | -3.8353 | -51.20086 | 2025-10-06 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8674db0-b15d-3999-92eb-9eb6e01cfffd | -8.54733 | -46.40063 | 2025-10-06 04:25:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec04ec63-5678-3831-a7f0-800966b1551f | -4.71902 | -46.13635 | 2025-10-06 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0447fc5c-4975-39aa-90fc-9a3e3f4ab878 | -5.26722 | -46.48426 | 2025-10-06 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 82915d7c-b697-3182-8378-d1fe73c29836 | -9.20247 | -46.91341 | 2025-10-06 04:25:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a819e2f-6c5d-3aeb-832c-39eb6c8de41c | -3.83843 | -51.73816 | 2025-10-06 04:25:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc0dbfd6-c4d9-3f24-9f8d-73027f14bf30 | -5.18025 | -45.05614 | 2025-10-06 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bc034fb1-9eae-3f41-aea8-c808a0f80c74 | -8.88251 | -47.62499 | 2025-10-06 04:25:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fdc2b2ab-836a-3e1e-976e-5e9f3ae6c438 | -6.82728 | -45.97244 | 2025-10-06 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26015589-17c7-3543-93e2-5e1eb8c5815c | -5.3044 | -42.54618 | 2025-10-06 04:25:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d52e26cb-0602-36f1-97a9-083f1ef99861 | -4.25369 | -48.56106 | 2025-10-06 04:25:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03383753-0edc-3219-96fd-bf2dca7c49c9 | -7.36146 | -45.22628 | 2025-10-06 04:25:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 95014939-7d8b-30c6-a541-4d20c251779b | -8.45628 | -46.87584 | 2025-10-06 04:25:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4b6055d-64a7-38e9-b46a-db2db6b19c0f | -7.32178 | -47.31289 | 2025-10-06 04:25:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README27.md)
