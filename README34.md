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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ca8073ab-0db3-3292-a9f5-d051b4e68319 | -9.4065 | -60.4941 | 2025-08-27 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| be490806-ffed-376d-bf53-799e5e34d0f0 | -9.4064 | -60.5133 | 2025-08-27 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 11963cd1-2baa-3867-82a5-331cae42e95e | -9.4062 | -60.5326 | 2025-08-27 04:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 7f328a0b-03dd-3bb0-b5ea-62d161f60e98 | -9.1715 | -59.5599 | 2025-08-27 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 130decab-67df-3d2b-b4e0-6586ffb1be25 | -6.8412 | -58.9746 | 2025-08-27 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| e211451b-dc79-38d3-b1d7-b2706e6e3667 | -6.8413 | -58.9552 | 2025-08-27 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 84b3e9d9-f38e-3b06-a8e2-0e2344c14e81 | -27.82826 | -50.30563 | 2025-08-27 04:10:00 | NPP-375D | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a02dc4b3-d746-31d1-8da1-c71781f50143 | -31.26025 | -54.24239 | 2025-08-27 04:10:00 | NPP-375D | BAGÉ | RIO GRANDE DO SUL | Brasil | 4301602 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| da2f306a-0198-311f-b4ac-fc17b8ae8e23 | -8.9295 | -65.9435 | 2025-08-27 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.3 |
| f9ad279c-0cef-34e0-9dee-20ad7baeb7e3 | -9.4062 | -60.5326 | 2025-08-27 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| df7c0809-5fd1-3636-9841-38f7d37759f8 | -8.9664 | -65.961 | 2025-08-27 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 59e341f2-2b9a-3849-8f2f-2cf0a9f413a9 | -9.4065 | -60.4941 | 2025-08-27 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 58dc4b90-65f9-3e21-b643-79afa97f4ae6 | -8.9479 | -65.9616 | 2025-08-27 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 169.6 |
| 697f71ff-4866-3908-bff7-4fdbfa166a2e | -8.948 | -65.9429 | 2025-08-27 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 158.7 |
| 5fe39f00-fb7c-37ad-b79c-689ddafa1161 | -8.9296 | -65.9248 | 2025-08-27 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| c88f5ff7-1967-3b2a-9993-287c97c494c9 | -6.8413 | -58.9552 | 2025-08-27 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 2cca73b1-b94e-3bfc-933a-5c1b79f292d9 | -9.1529 | -59.5609 | 2025-08-27 04:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 08bba0a9-6437-31a9-89a0-61de06ab7bba | -8.9665 | -65.9424 | 2025-08-27 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 97.8 |
| 94393105-644c-32a8-b00d-aa753099cb2c | -9.4064 | -60.5133 | 2025-08-27 04:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 5e90f292-c44e-37d8-9512-84fbc0b5c10a | -2.91705 | -48.30225 | 2025-08-27 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 20d37db4-72b5-3b4e-b6f2-7ccc9c572c09 | -3.34566 | -43.36117 | 2025-08-27 04:23:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a701295c-141a-3cdb-9608-1cf79a656c82 | -3.46706 | -48.82095 | 2025-08-27 04:23:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 873067a9-065e-35ee-a2c9-b7da1b078b90 | -2.91995 | -48.30678 | 2025-08-27 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3260c742-1989-3977-9594-e5f73ec53c51 | -4.41136 | -42.13459 | 2025-08-27 04:23:00 | NOAA-20 | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bf40f812-a3a6-3c1d-966b-1d73e3b65d62 | -3.21911 | -46.81004 | 2025-08-27 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 343858dd-cf8a-32a8-a98a-82f5f3a42a0f | -3.41929 | -49.04612 | 2025-08-27 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4c6c0d68-726d-35ec-9c61-501a634b35b9 | -4.67419 | -41.02277 | 2025-08-27 04:23:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 12bfad06-e8fc-3f2c-bb36-505082251ae4 | -3.66592 | -48.32977 | 2025-08-27 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05bff258-7156-3a95-ae05-bb7c983380e7 | -3.42294 | -49.04671 | 2025-08-27 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 86dee52f-e7a1-3b86-aceb-9499631cc9b0 | -3.42363 | -49.04247 | 2025-08-27 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 882b9eee-b311-3b8d-a370-feb776f6052d | -3.23458 | -50.80678 | 2025-08-27 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 340e3189-be5a-39f4-a811-f7584f663501 | -3.36183 | -43.37144 | 2025-08-27 04:23:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c6e4afc-153a-3887-964d-099955ffca82 | -2.44429 | -47.33294 | 2025-08-27 04:23:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 37b710f5-e824-34f2-91c5-b6de27410795 | -2.63559 | -48.04605 | 2025-08-27 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a2e2772-f0af-32bd-baea-f04cf25b7f7a | 0.77885 | -51.33316 | 2025-08-27 04:23:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 659b66fa-4a59-3f9f-b048-aa27abc1508d | -3.97786 | -43.24557 | 2025-08-27 04:23:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c12ce0b8-1bcd-3155-87aa-333e1abb1449 | -2.91641 | -48.30622 | 2025-08-27 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2e0a733-0fdf-3462-9d7b-3bdafe6c40c4 | -4.6777 | -41.0267 | 2025-08-27 04:23:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 65a3828c-4faa-3d82-96ca-fc2f2098b550 | -3.35836 | -43.37091 | 2025-08-27 04:23:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e7b2cda0-aeb1-3d80-9b83-c530f8f45f38 | -3.53749 | -45.70392 | 2025-08-27 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ced9267f-c8eb-3a22-8cc1-95c4ba276dfb | -3.38009 | -42.33118 | 2025-08-27 04:23:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0fcfab4e-aee8-3aed-a020-ac26d7d7f640 | -3.21451 | -45.38123 | 2025-08-27 04:23:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 541b135d-bffa-398e-85b9-564ddeb3bba5 | -3.17364 | -48.8029 | 2025-08-27 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21994d86-9556-33ee-951f-ed8d4bbbb56c | -3.21967 | -46.8065 | 2025-08-27 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9897c552-6fab-398e-98b2-37642b67c6fd | -3.17018 | -49.47754 | 2025-08-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47e37aca-c311-3027-9674-709921ef2f03 | -2.88937 | -48.29377 | 2025-08-27 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2033ad32-0750-33dc-978f-0813acd89dd8 | -3.5015 | -44.76625 | 2025-08-27 04:23:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5725003b-7661-344e-a7e9-d5de6e9bd9c1 | -3.32699 | -43.03485 | 2025-08-27 04:23:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 18086126-de73-31b3-a10a-6ad0caefc599 | -2.89001 | -48.28981 | 2025-08-27 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 27649306-1315-368c-a7f6-0362b5c3843d | -2.76663 | -49.19185 | 2025-08-27 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f686fdf9-9ef5-3737-bed1-f0131eb9022c | -2.44487 | -47.32925 | 2025-08-27 04:23:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5da8fe79-6ba2-3f20-ac30-0777ef9ca2c8 | -4.87958 | -37.48365 | 2025-08-27 04:23:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 8d275b88-e82b-36ba-8d5c-48b0eed34bec | -4.23753 | -41.39704 | 2025-08-27 04:23:00 | NOAA-20 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6c7198c2-57dc-30ec-a1e6-189d36904bf9 | -3.41998 | -49.04189 | 2025-08-27 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 59ccc44d-24f3-30a7-82b0-e0d807caa8fe | -4.87915 | -37.48668 | 2025-08-27 04:23:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 08b4949c-7ea7-31cc-82f0-334f14433181 | -6.88124 | -44.43663 | 2025-08-27 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fbd6238b-c38d-3382-8b2c-36ee28df55c7 | -6.32005 | -42.88046 | 2025-08-27 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 597585ad-0600-33ba-a0ad-b17a3b8f9a59 | -8.88124 | -60.76474 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 240a9d61-d29f-3670-99a7-3fe932f0d4ff | -11.26193 | -44.96527 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e6f4a625-5ac5-3e8a-bcf0-20aa481a99a7 | -8.41374 | -47.4328 | 2025-08-27 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a6be83d5-9b77-3596-8a13-a3a168cf7a15 | -11.29048 | -44.96558 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d0e6fb7a-c0b6-3f3c-ba86-5e87a117dce5 | -9.58783 | -55.38618 | 2025-08-27 04:25:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83f4e67d-1403-30ed-81dc-47450ca9851a | -7.4801 | -46.00852 | 2025-08-27 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b740b7a0-0183-31a4-bce0-396b855af96d | -7.64531 | -42.66798 | 2025-08-27 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c12f9da2-a897-3b03-a61b-1f047c250a14 | -7.64251 | -42.68646 | 2025-08-27 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4525572c-50e4-3b38-bf33-5044cc3c6de2 | -9.21455 | -46.72952 | 2025-08-27 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e6b125f9-a14a-3ae3-96c3-aed623f2e095 | -8.88385 | -60.7741 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 83587fc7-2328-3b57-a7b3-4f7c788f3dbc | -5.24998 | -43.34815 | 2025-08-27 04:25:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d95a9875-2245-3eb3-8c0d-e2735a928cad | -9.07903 | -49.58012 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1a1d40e1-3378-3501-99ff-f474c8582163 | -9.07123 | -49.60443 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4fcfa82b-176a-32bf-969f-de91b3262be4 | -5.75525 | -53.77038 | 2025-08-27 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5183dcd8-08b6-3ec4-a2ef-92854f1feefa | -7.64461 | -42.6726 | 2025-08-27 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 443e48bc-6432-3690-914e-6bfbb0ab72d4 | -4.79229 | -47.27923 | 2025-08-27 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd0ce142-c471-31ed-a6c3-96e68ddc43ce | -8.54524 | -51.39206 | 2025-08-27 04:25:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e5e3fb4-4490-3b5f-9896-2d547412d83b | -8.12313 | -55.36795 | 2025-08-27 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a068e224-f409-3ea1-b91f-3a26ec98f5f1 | -3.97786 | -51.05571 | 2025-08-27 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6b510da-4d48-3e01-b4a2-ab72a0c4848e | -8.89228 | -60.76864 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 21b06493-7e4f-3382-85a4-648bc3cf4441 | -6.88524 | -44.43343 | 2025-08-27 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e54ef4a-2281-3981-91be-cdfbc595bfae | -6.49058 | -44.68063 | 2025-08-27 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee7916f1-24c4-362b-8eeb-afb998541c7b | -4.6987 | -56.06694 | 2025-08-27 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81488613-e911-3637-aa67-cb0b3f3d3d4b | -9.09156 | -49.56999 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f2f84cc1-4912-3904-b020-fb5059e11b2c | -6.57744 | -47.38077 | 2025-08-27 04:25:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 906abb97-6b8d-34f9-aaf9-d7b9c71e8266 | -7.64912 | -42.67133 | 2025-08-27 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a7d56116-817b-3803-bcd7-68ecf2ca59ef | -10.81819 | -46.37038 | 2025-08-27 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b78ed164-7b37-3f68-b867-f937b7d3f332 | -6.57688 | -47.3843 | 2025-08-27 04:25:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d936ce6e-249b-3764-b602-a5c269662849 | -9.0775 | -49.56766 | 2025-08-27 04:25:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d44115b-91cc-38cb-9893-b73f7ea31961 | -8.29963 | -46.32672 | 2025-08-27 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 27272b33-7482-342e-8063-52a50c107ce2 | -8.47901 | -43.65211 | 2025-08-27 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1d4c0116-6d45-3fe5-983d-c34888d3ed0b | -9.25132 | -56.904 | 2025-08-27 04:25:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43eedec5-e260-30d0-85bc-dcc627f4fab1 | -5.62254 | -45.72773 | 2025-08-27 04:25:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cbb4c82d-40f6-3df5-8d7f-04bbf5c634b4 | -5.399 | -45.11758 | 2025-08-27 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 132d6c4a-471d-3df7-87b0-548a0a97e23b | -8.89919 | -47.32829 | 2025-08-27 04:25:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 03be5561-cd6f-3885-9de9-85fe6fd9cf47 | -6.81707 | -58.9678 | 2025-08-27 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 33fcb46b-7028-33b6-a70c-ab3923c3bb68 | -6.80387 | -44.34851 | 2025-08-27 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 035d58d1-1d86-3bf0-a7d4-e4f2e3632f3c | -11.25438 | -44.99201 | 2025-08-27 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22928eae-2ca4-33e0-8800-fee43cf6554b | -6.32371 | -42.88236 | 2025-08-27 04:25:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b13d443-b006-3c0a-a42f-6b9caabcbcd7 | -9.15768 | -59.54146 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7433e706-6433-3cee-b8c7-23c7dda8902a | -6.9628 | -44.11115 | 2025-08-27 04:25:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2151489a-6952-3f48-99c6-4251e864bac1 | -6.62826 | -43.53215 | 2025-08-27 04:25:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bd71c6e3-1554-3090-85cd-3bd10b014800 | -9.16768 | -59.45622 | 2025-08-27 04:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README35.md)
