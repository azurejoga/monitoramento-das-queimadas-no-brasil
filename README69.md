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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 499f45ce-6437-335d-9f80-544278eed18b | -8.35868 | -49.72258 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b85cf3ad-a6d1-3966-8fb3-fcf9be2ac888 | -8.29553 | -43.39349 | 2025-10-18 04:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 517f5a24-fa2d-3bad-b739-8f655b1f9fe0 | -3.57107 | -49.44185 | 2025-10-18 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 608c867c-51d3-3ebf-b590-3849d70ffd09 | -4.96424 | -44.60555 | 2025-10-18 04:49:00 | NOAA-20 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 28073f7b-6cce-3a10-b280-194daa5ffa4e | -8.2335 | -44.00546 | 2025-10-18 04:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| af3ef631-417a-379f-b773-3eabe7266efd | -6.21318 | -53.0948 | 2025-10-18 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 60a12da5-ed46-3b12-b60a-34f41750a06f | -9.7232 | -44.54278 | 2025-10-18 04:49:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 744bfc4d-fa9f-3750-bd6f-1590ee0e18bf | -6.58515 | -47.07218 | 2025-10-18 04:49:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ecb1af0-09e1-372b-88f5-b75ad9ce7656 | -5.30558 | -44.84415 | 2025-10-18 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c0235807-0a11-3a17-8f30-b5f0d3d40fdc | -5.10915 | -46.07454 | 2025-10-18 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2bd694c1-258c-3296-9295-cbf1cd3819d2 | -6.30137 | -44.72215 | 2025-10-18 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 97a5c467-1cbb-3da7-b045-72b1c295e4c4 | -3.52702 | -50.30937 | 2025-10-18 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54418084-7ebe-3149-8d8b-5fc2a9502085 | -5.6449 | -45.10854 | 2025-10-18 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 007b22af-35b3-3de4-93eb-a77d04670c03 | -8.43808 | -48.7009 | 2025-10-18 04:49:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf0f1afe-7785-345c-93c8-abe4a358ad7d | -7.39426 | -44.75188 | 2025-10-18 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bdeeb860-e1c1-3c4a-a2fb-21d3ffb9e718 | -8.80953 | -49.68108 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d826951-6080-34d7-8ed0-95798e338484 | -7.49063 | -47.02875 | 2025-10-18 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 480854ee-6945-3b98-b865-68e2971f5e50 | -4.01103 | -50.22412 | 2025-10-18 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82ee91ea-a1d5-3c4c-a7c9-8bf884393515 | -7.71032 | -47.84941 | 2025-10-18 04:49:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 306f19b1-06aa-37a6-be63-0b3bb643cb3b | -4.45278 | -43.23564 | 2025-10-18 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 5be30e74-ab14-3082-bdb5-132176355481 | -3.60264 | -49.35233 | 2025-10-18 04:49:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a85dc84d-b79f-3252-b7b4-14bd889fec7e | -8.8264 | -49.69227 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| faa05e60-ca8c-3dec-8a7b-0ff3d08857d6 | -8.04309 | -41.1153 | 2025-10-18 04:49:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d504c6eb-f97c-3ac7-9d4e-8af417d3c077 | -8.82469 | -49.679 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 91cd5ab1-e7d6-331b-b6cb-36438d75b57f | -2.92683 | -49.17844 | 2025-10-18 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| af062340-4a60-3f3e-9b7f-f2dd2b7ee540 | -3.86547 | -51.41764 | 2025-10-18 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3aeec45a-faf7-32b2-bfc4-d89090344226 | -6.27487 | -44.38388 | 2025-10-18 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77395802-c6fc-3b32-aae4-5c2bd00b9396 | -7.34275 | -43.86521 | 2025-10-18 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 4129b76d-1156-3f8e-b188-0e0e3785ab5f | -4.83384 | -48.0813 | 2025-10-18 04:49:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62068b8c-e184-356b-8b13-b50b81bb3364 | -3.15257 | -50.24439 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fb59658c-1f64-3eb6-8eb5-e2c2efc63b12 | -4.66698 | -50.61924 | 2025-10-18 04:49:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 233944fd-e0fe-36fa-9c8d-bd817769c3ce | -7.4376 | -43.75835 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fb71fdb-7c0a-39c6-9628-a2d848ebbbc3 | -7.11463 | -44.7337 | 2025-10-18 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45a18a6c-5442-3896-bfbc-39b0a70bc0d4 | -8.16991 | -47.04347 | 2025-10-18 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90b0c21f-7c62-373c-8eb3-e7e8e5479189 | -7.98685 | -44.15881 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1db2ddff-d017-35f6-afe5-d3886e9e613f | -5.86773 | -44.85057 | 2025-10-18 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f423aeb-f297-3bc7-8710-6c38a85956d8 | -2.70431 | -49.85792 | 2025-10-18 04:49:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f204f7d5-498a-361c-a37e-66bba14731c2 | -9.24605 | -44.34754 | 2025-10-18 04:49:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97d0861c-7c22-3c77-b944-d45d35de7a3e | -3.83086 | -47.40392 | 2025-10-18 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eda2a93c-d146-3162-ba93-76499ac11ce6 | -8.13411 | -49.10388 | 2025-10-18 04:49:00 | NOAA-20 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2714471-1840-30e7-b125-9e631cdca598 | -8.91913 | -47.96194 | 2025-10-18 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c30b0ed5-ff2c-31de-9c93-58a5247d9db5 | -7.71731 | -47.85744 | 2025-10-18 04:49:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 205384aa-987d-37e7-8520-629043f79fbe | -4.44897 | -43.22542 | 2025-10-18 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 75c682d8-5ae3-3847-b0a0-8fb9fbc113e3 | -8.39055 | -46.23714 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9d698b51-7952-3b93-b808-34d5c7e3e762 | -6.37456 | -45.77034 | 2025-10-18 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2959038-bb68-3898-86fa-3436797f0993 | -6.23232 | -44.6524 | 2025-10-18 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed54a036-f0d2-3b47-8c19-45cea9db6d25 | -8.36646 | -46.26123 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42109125-44c3-3fc5-93ed-7720af0d3e0d | -2.36507 | -48.51337 | 2025-10-18 04:49:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3b0d56b-5d44-3199-8121-74ef44c5268a | -5.01198 | -46.03117 | 2025-10-18 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| c74d05df-2ada-30ed-a5ec-725b544fd3d3 | -3.15983 | -49.16926 | 2025-10-18 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| abfe532e-b748-36e6-90b8-c215662710ce | -4.0752 | -43.3984 | 2025-10-18 04:49:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 446283ea-9e3d-38a2-a5c7-884e3019da5c | -3.74959 | -49.0321 | 2025-10-18 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| be9a7562-bbf1-354d-a884-8596229dd344 | -8.64757 | -47.0831 | 2025-10-18 04:49:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52769159-7142-343f-8b94-567845c78f52 | -7.97002 | -45.86375 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9fe9db55-8c74-3bd5-88b0-c4fb506491d4 | -6.54355 | -43.91816 | 2025-10-18 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac29b4e4-0d4f-31c6-b3c4-f9a30072d70b | -7.12681 | -47.23372 | 2025-10-18 04:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76dd00d7-cc73-3ae9-974b-c6793f87303f | -2.57284 | -49.10651 | 2025-10-18 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08d09ccd-ff77-39d6-9a49-fe8160442856 | -6.61004 | -44.21493 | 2025-10-18 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f97a785d-2cf4-3395-bcda-c813ea6e9c1f | -3.65778 | -50.26621 | 2025-10-18 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d2bf247c-3876-3192-8848-9459b14a4055 | -2.93673 | -54.17376 | 2025-10-18 04:49:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 995f27ce-7668-3db6-bc93-775425669990 | -5.70091 | -49.30214 | 2025-10-18 04:49:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 09c85df0-2216-3a9f-8277-b786acbbef87 | -3.13742 | -50.25303 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a23cb77-4647-36c7-a3c0-499cacc1167e | -8.36294 | -46.20482 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 77ebdd8b-8fc9-3b4c-8c85-5cd0a2317a78 | -9.72117 | -44.5581 | 2025-10-18 04:49:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 972d9dbc-51d7-3090-9f4b-538fc8ec20dd | -6.59224 | -44.16201 | 2025-10-18 04:49:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56a7d502-6a3f-3b81-9b50-446610dbc271 | -2.87567 | -50.73371 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 872c5661-8e3b-347a-9361-0b1c52195f2e | -5.8923 | -43.90342 | 2025-10-18 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9f2b0772-bbe9-3c38-9778-dc17562d8bb4 | -2.86792 | -50.73966 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bda9c63e-07d2-369b-8f23-a1d282a78c6a | -4.53405 | -44.80163 | 2025-10-18 04:49:00 | NOAA-20 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 275406f2-c083-3e90-90b1-9b8356d15e67 | -9.07984 | -48.03252 | 2025-10-18 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c19db521-884f-3ff2-acda-7b870c828e7e | -8.36035 | -44.77276 | 2025-10-18 04:49:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f3299c1-6e84-3763-99c9-154f245580de | -4.27566 | -48.33161 | 2025-10-18 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d1d1700d-7d84-36e8-9561-146021d82c3d | -7.39695 | -44.75028 | 2025-10-18 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 660805f9-ec8b-3b80-9374-63a93611ad0f | -9.09156 | -47.83002 | 2025-10-18 04:49:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d40ecbf-2fef-33af-8a67-88dc97e4930e | -3.19628 | -52.57745 | 2025-10-18 04:49:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ee57e901-20a6-31ca-8953-aaa28f59ac35 | -6.31836 | -40.95119 | 2025-10-18 04:49:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c737a8f2-e77f-3c9e-8db8-4a8a983f128a | -9.67383 | -44.56036 | 2025-10-18 04:49:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 217ebe92-fa94-39a4-a917-93a1a9f167af | -6.52413 | -41.49361 | 2025-10-18 04:49:00 | NOAA-20 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cd424e99-e460-3f16-b4bb-db8fae648c46 | -7.70983 | -47.85286 | 2025-10-18 04:49:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c5d9e72-7f96-3d67-a978-f23e51e51d14 | -9.75249 | -43.96581 | 2025-10-18 04:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fc7a7c92-a1ed-3502-81ab-7fb692644a52 | -8.77381 | -47.84406 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 422a197a-58ee-3e82-8804-cdb999ad310e | -7.75272 | -42.50538 | 2025-10-18 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3ec5d9db-a6bf-38fd-b26c-cbe5860c9de6 | -5.00944 | -46.01854 | 2025-10-18 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 18.4 |
| b6b9f7fa-2e99-3427-8619-82fbf9fb493d | -5.30485 | -44.84909 | 2025-10-18 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9e341da6-7101-34c0-893b-b244126723af | -6.95977 | -47.11794 | 2025-10-18 04:49:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ada6c551-a6f5-33db-b469-65d2c2bc6da3 | -9.13845 | -46.66624 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc500b4e-bfc4-3d12-81c5-e6153e1b74aa | -5.24833 | -50.96035 | 2025-10-18 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d92554e-254c-30c7-ba94-2c7a9779a3d1 | -2.72406 | -48.83248 | 2025-10-18 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e79c058-9013-3814-b721-aec24dec15c9 | -2.87289 | -50.72971 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25089cec-e6bc-3d14-beac-c76d440117a3 | -7.82117 | -44.12592 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b37a22f6-6e66-3bbd-8640-4a4c54fe2dc0 | -3.14527 | -50.24693 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| d76ff222-7b5c-349a-8aea-c20458be5712 | -6.41586 | -51.54939 | 2025-10-18 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 405cb16e-0c5c-3123-a799-af666b944df4 | -8.09047 | -44.10723 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d115d6e-c347-37f5-bca4-42bd4efac926 | -4.24703 | -48.56416 | 2025-10-18 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64a09d8c-7dd9-3801-8dc9-6463c3923742 | -6.83189 | -42.43193 | 2025-10-18 04:49:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| b66a4658-037a-3c62-ba9a-0c0f56296951 | -8.10959 | -55.08629 | 2025-10-18 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2916f7e-f879-32d9-a009-3bf4cdd9ae54 | -8.82213 | -49.69596 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f01dba2-2fd0-371b-bcbe-d40a260ad3da | -8.30593 | -43.39857 | 2025-10-18 04:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 997adcdb-84db-3b9a-aa01-1b5d9dda77ae | -5.59983 | -47.50014 | 2025-10-18 04:49:00 | NOAA-20 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1613ce4c-039f-3080-acb9-e060d996c15e | -4.69366 | -48.62593 | 2025-10-18 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README70.md)
