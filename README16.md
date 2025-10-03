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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 466d1c73-84d2-3721-b423-d0a88d8e0598 | -10.8791 | -46.7141 | 2025-10-03 03:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 62cad893-8a4d-37ba-b211-a14561fb3bd3 | -7.7496 | -46.2496 | 2025-10-03 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 517.0 |
| 600822ae-e634-3052-970f-0c949b8dcdff | -11.9163 | -46.2817 | 2025-10-03 03:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 138.9 |
| cc6397ae-638f-3b74-98d6-0dc332e77317 | -5.6361 | -43.9258 | 2025-10-03 03:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 06501830-158d-3dec-82d3-de4c3a6c9db8 | -17.8614 | -57.623 | 2025-10-03 03:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.3 |
| 9ae69dc1-be11-3229-ad67-1e282b87395f | -10.8929 | -47.0482 | 2025-10-03 03:40:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| ded46531-b7db-31fc-a664-655e199bd82c | -0.90012 | -47.54621 | 2025-10-03 03:40:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12b9e1f7-db8b-33bc-b7a5-34f1030eae9d | -2.9069 | -40.38968 | 2025-10-03 03:40:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 02bbfbc8-1b42-3a4a-8f90-e640be9bd2ee | -0.90718 | -47.54715 | 2025-10-03 03:40:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3057c2f4-e89a-3e68-87e8-3bf61dcca9b9 | -2.91118 | -40.39034 | 2025-10-03 03:40:00 | NOAA-21 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c8cc9a62-e164-3de1-9b97-b32d1bffd780 | -0.91424 | -47.54808 | 2025-10-03 03:40:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 452aa8f4-a718-3160-b871-03966df0d4cc | -7.15923 | -44.9909 | 2025-10-03 03:42:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 58c8cc5f-6eed-30d1-8cec-58449cd5b0d3 | -6.35085 | -44.30237 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 348bb534-f583-31ca-bedb-9045703f38e4 | -7.7077 | -46.2075 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 822b2672-915d-3ad9-aaf2-c90f560ddfed | -6.24018 | -44.22639 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cbc754fc-f5fb-3a10-a254-4a481b852b1a | -4.66363 | -45.81382 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a3ee5d84-52ce-3666-960a-f72c7baef2d2 | -7.79192 | -42.5601 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| fcb4096a-40b5-3c21-a4aa-6493adf6af76 | -6.2765 | -44.05289 | 2025-10-03 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4f90cd9b-e288-3477-9612-2fde2c0eb819 | -7.9115 | -43.5371 | 2025-10-03 03:42:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5ff9fa85-351f-3879-90c1-7d91ad864dc3 | -5.96132 | -35.58004 | 2025-10-03 03:42:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO NORTE | Brasil | 2401701 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ee98377e-a375-3c2d-a42c-18a5937a14c8 | -5.63403 | -43.91901 | 2025-10-03 03:42:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| e791ba5d-4dfc-3c35-83c2-36cb56c2e9d6 | -4.6712 | -45.80559 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 20.9 |
| ef6ebe8f-698b-3bf3-8af0-a81550d48703 | -4.66263 | -45.80043 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 144.6 |
| 2d61dda7-4209-3117-84b2-149f90b6ea98 | -5.32153 | -45.28638 | 2025-10-03 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 295016d7-93b3-3e6f-9aec-43b97c6aa17e | -6.66811 | -42.78634 | 2025-10-03 03:42:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 01766ddc-aa8f-366a-a2fb-86585a05c29a | -8.11073 | -40.91912 | 2025-10-03 03:42:00 | NOAA-21 | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 702fc34a-9f71-3bf3-b174-7c6bae85a705 | -4.66946 | -45.79671 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 144.6 |
| 63344fb6-305d-3de5-acfd-ff938d882aca | -7.75903 | -42.55947 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 40cbb39c-f6b3-386f-bc95-a70086893436 | -7.00524 | -47.1842 | 2025-10-03 03:42:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 72f7c62c-f898-3d6d-b3ea-c495ccc43209 | -6.63982 | -41.27196 | 2025-10-03 03:42:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 22717080-521e-3ae4-9951-19e68c510b8a | -7.90177 | -43.53519 | 2025-10-03 03:42:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 89b6ef23-e989-3738-807a-d251164e779b | -6.34584 | -44.3042 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| aab07c0e-5691-338b-bee2-4fa851b2319b | -4.80896 | -46.81192 | 2025-10-03 03:42:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| da73775e-6015-3f89-8307-048f588891fd | -6.4847 | -44.21945 | 2025-10-03 03:42:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e0a76c6-91e8-39b3-bce7-62fe503ad949 | -4.67795 | -45.80209 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| da575521-2eac-3712-bfe3-2954f8703329 | -7.74139 | -46.24912 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b3209d13-eb9f-32c2-9efe-abc3293bb5de | -7.77639 | -42.51409 | 2025-10-03 03:42:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 70669bf8-ec9b-3055-b932-d5f4a4c603e8 | -7.7281 | -46.2282 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d14a5a06-86bf-38d1-bdd6-9e0b00b29312 | -3.45735 | -40.23331 | 2025-10-03 03:42:00 | NOAA-21 | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| b4edcc28-6352-31c0-a311-8c26108f0629 | -4.64773 | -45.79881 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1ccf3db2-6cc4-333e-84f5-723c9bcd83e1 | -4.66589 | -45.80062 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 67.5 |
| e377034e-01e2-3afa-9a61-1062aa34f95e | -6.7299 | -44.14789 | 2025-10-03 03:42:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52221436-f071-3808-9c30-ebd4735d5b40 | -7.25159 | -49.4058 | 2025-10-03 03:42:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e42c3392-5bff-326a-a97a-18887ab57648 | -6.3322 | -43.88913 | 2025-10-03 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1171fc53-9927-3ea0-a572-39d3e41e8126 | -6.23958 | -45.34341 | 2025-10-03 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3c9f7e96-6e1d-3e1e-bd53-a4b6944c1297 | -7.76856 | -42.53198 | 2025-10-03 03:42:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 93a75b60-f6d9-3881-9653-56ae112aa4b4 | -5.34677 | -43.76537 | 2025-10-03 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4a3008f5-f567-3e66-b447-0d1abe7209ec | -4.66419 | -45.79177 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 1b6f2fb6-8514-3c55-87ce-25e4cf834b54 | -4.70189 | -37.36765 | 2025-10-03 03:42:00 | NOAA-21 | ICAPUÍ | CEARÁ | Brasil | 2305357 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 50ccec9d-10dc-33ef-8516-1ae57df45882 | -6.78505 | -47.16267 | 2025-10-03 03:42:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bd29ec72-ecc4-3fa2-96a5-0b3d47aac416 | -6.04684 | -44.62683 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 41033a01-9817-3a61-b56f-b424163c7dcd | -6.55095 | -43.87616 | 2025-10-03 03:42:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 850cb43e-8c51-38f4-9c21-b97dcf540d3b | -6.32235 | -43.88498 | 2025-10-03 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53f8f787-ba92-332c-a989-f32b0b516ecf | -6.87704 | -45.47918 | 2025-10-03 03:42:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 57b6fef5-e1e8-3745-b5b2-57141029fcff | -6.32291 | -43.88179 | 2025-10-03 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ee44810-12fa-3abb-9d19-e4a3848701ec | -5.63508 | -43.91286 | 2025-10-03 03:42:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| dac65756-a595-3107-89fb-9c9d40b24a1c | -4.66027 | -45.81361 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f80fe430-a28f-30d4-bb95-70f9b0e33e34 | -7.26128 | -48.48084 | 2025-10-03 03:42:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e47aaf8e-4303-39e8-86ba-a2ccaf39dec1 | -7.74485 | -42.58636 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 301f3200-5d3e-3a14-9899-04293df6abc9 | -7.76525 | -42.60484 | 2025-10-03 03:42:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 2aad9dda-f55c-304a-9b55-005cb117015e | -4.65603 | -45.7864 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 28d95375-1513-3bf7-ba49-3cba3d2cad50 | -6.24124 | -45.36723 | 2025-10-03 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 30110c99-0c79-3809-8132-cd9138c6404d | -7.24809 | -49.40456 | 2025-10-03 03:42:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4332e081-de7e-3039-a56f-6af6a8d82fd2 | -4.64249 | -45.7935 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c069118c-50ad-3fd2-b1e2-d5c66669a4c1 | -6.23535 | -44.25248 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1615a533-21b7-368b-a358-ad244fb2460a | -6.7073 | -42.81405 | 2025-10-03 03:42:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| c71e05c8-4881-3f26-9338-972181a23c56 | -5.24849 | -43.09993 | 2025-10-03 03:42:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d6b13e63-d2d3-35bf-ad32-15bc1352fec3 | -7.71359 | -46.2083 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 9fffba5d-f932-36af-9178-43e733316621 | -6.66336 | -42.7856 | 2025-10-03 03:42:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| f89f54b1-edd8-3d1e-a37b-ddae2e1edbfe | -4.66203 | -45.78728 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 3eb0c9c3-9a35-309a-b73d-11434af90aa6 | -7.71226 | -46.21108 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 3dbbbb67-5aed-3c76-84a4-35bde358c85c | -7.30493 | -45.25711 | 2025-10-03 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ced8918-086d-3dfd-81b0-67221ea8bb29 | -6.30245 | -43.90753 | 2025-10-03 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a71b273-d431-3774-beaa-a507fe1315f6 | -6.7202 | -45.97239 | 2025-10-03 03:42:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ffa9fc6-f516-3e1a-828b-70fa6070fb46 | -5.40479 | -41.3316 | 2025-10-03 03:42:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 526c1f6d-5e70-3f2d-85b6-c9a8ecd64ce1 | -5.62936 | -43.91501 | 2025-10-03 03:42:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c2b78825-8730-35da-9a38-d8a01e95b35d | -7.00616 | -47.17913 | 2025-10-03 03:42:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6b7de052-a555-3a1a-bc62-6b57e2c887f0 | -6.23547 | -44.25386 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a6223f5-2392-35c2-9523-4df61805b6b5 | -6.27569 | -44.05051 | 2025-10-03 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a320a02d-ebcf-3534-ab5d-25179e2313f4 | -4.65758 | -45.81318 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f14fdfb5-e692-3131-91c1-c610e1d6723f | -8.23887 | -39.02921 | 2025-10-03 03:42:00 | NOAA-21 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| efa58417-1eac-35a4-8c45-d1a133c6d0bb | -6.07045 | -44.61934 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e1d172f6-59bc-33c8-a300-e2fe3e21cd9d | -7.79439 | -42.54588 | 2025-10-03 03:42:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 498f6f02-7f0c-3f99-a4b6-9c666c2872c4 | -6.381 | -44.76015 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d1eb5889-a042-35b3-9e0f-e9fe2e46ab74 | -7.75239 | -46.25505 | 2025-10-03 03:42:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| e4f588d2-509c-34dc-95dc-517ff898e4c0 | -5.34159 | -43.76448 | 2025-10-03 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b300ea35-96d1-39c6-8a3f-82d0d75506b7 | -7.77069 | -42.60078 | 2025-10-03 03:42:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| ee70becf-28fc-3e42-b497-cab8e1346c0f | -4.70539 | -37.36818 | 2025-10-03 03:42:00 | NOAA-21 | ICAPUÍ | CEARÁ | Brasil | 2305357 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 429c6a7d-f760-38de-adef-5d0ae19aa4aa | -4.67194 | -45.80128 | 2025-10-03 03:42:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 67.5 |
| e54b3a09-98d6-3ab3-a45b-10345e2b96c9 | -6.23906 | -44.23181 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4791efc1-7326-35dd-889b-6763fa5f5078 | -6.64823 | -42.7885 | 2025-10-03 03:42:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 119c0966-7ca3-3cbc-9a9d-20d7b82d3176 | -6.97329 | -44.39263 | 2025-10-03 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b2fe360-7b5b-39c5-87eb-4d819912ecd5 | -3.67053 | -38.81182 | 2025-10-03 03:42:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6b62a41c-c75a-3d0a-9436-2f7eb9a54f17 | -7.76611 | -42.59995 | 2025-10-03 03:42:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 7a1e87d1-9204-3c29-8af3-1dbd17db3652 | -6.95975 | -45.34376 | 2025-10-03 03:42:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7bdeb9e7-041a-3c0c-9849-54d3875ed510 | -6.23256 | -44.23919 | 2025-10-03 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b1e23f09-d96f-3393-a7ab-f5edfa071036 | -7.55538 | -42.40199 | 2025-10-03 03:42:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5b5b9d67-8358-3f09-ab9e-aa50bc2f7e2c | -3.45316 | -40.23264 | 2025-10-03 03:42:00 | NOAA-21 | SANTANA DO ACARAÚ | CEARÁ | Brasil | 2312007 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 732691a9-58f4-3c65-b453-f40cb09834b9 | -6.41178 | -43.93097 | 2025-10-03 03:42:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d637484a-7305-340e-9e97-5649567732bc | -6.27102 | -44.04651 | 2025-10-03 03:42:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README17.md)
