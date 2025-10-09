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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f22a8d0d-dad5-3d43-b365-c6ff3b56d6a7 | -9.75572 | -47.7011 | 2025-10-09 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c0d6781d-0b62-3999-8f9d-583d1233d7e9 | -11.47143 | -43.47876 | 2025-10-09 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06908937-16cf-32bf-b8d7-06a215a50f94 | -14.40466 | -46.02758 | 2025-10-09 04:19:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 331de846-4811-35f3-8482-1c9b6d5eaa1d | -7.76478 | -42.38458 | 2025-10-09 04:19:00 | NOAA-20 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6ebf871c-19b6-3380-805e-b12b52d361be | -10.81468 | -44.27241 | 2025-10-09 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d5aa682b-555b-3c53-ac58-773281a0a021 | -7.17793 | -46.71524 | 2025-10-09 04:19:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22284578-1279-3128-b73a-c9f7897d8d6a | -11.97826 | -44.79914 | 2025-10-09 04:19:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d1d8cd29-319d-389c-90e7-001184c8041c | -8.67901 | -43.90472 | 2025-10-09 04:19:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 00734a14-301e-37d6-a0a8-1d3e44c8e2bf | -8.19883 | -43.34053 | 2025-10-09 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 52e97925-1e13-3456-856c-30ac407ff95d | -13.80438 | -45.84961 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15d03488-64cf-311b-8414-539a0645fbea | -11.68834 | -44.26184 | 2025-10-09 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f9c88370-d38f-3c09-a64b-d57b4b61289f | -7.31818 | -44.87478 | 2025-10-09 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 57c1d4fe-c637-3b69-b3a4-43d5617c82da | -7.45553 | -47.18086 | 2025-10-09 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8cf1251-2410-3882-8da0-7b4ffa229c54 | -2.491 | -47.57336 | 2025-10-09 04:19:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e0d5820e-ecd9-3e24-bb10-0ad577826757 | -14.41903 | -43.97028 | 2025-10-09 04:19:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 42d7894c-31ea-31de-9ca8-234627b3ccf4 | -12.04799 | -43.49907 | 2025-10-09 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9501ddcc-f0f1-3d1d-9729-6305c776bee9 | -8.19545 | -43.34002 | 2025-10-09 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 77421624-a6c8-320a-b5a9-6507debcc687 | -10.89445 | -43.82123 | 2025-10-09 04:19:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3480e8ac-235b-3326-9641-17caa2360044 | -12.42356 | -45.71257 | 2025-10-09 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c6d6c8bc-9abd-3b22-b9d7-708f8dd7e394 | -10.52572 | -50.02996 | 2025-10-09 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4264506b-a9db-343e-9bab-1490f821100d | -10.8609 | -44.63079 | 2025-10-09 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 358c2268-8d7e-3709-899b-55c704eb3d21 | -11.85575 | -44.91133 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6871363e-11f6-37a5-82f4-c010fe49f391 | -10.19471 | -44.56998 | 2025-10-09 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ef95032-4254-3ad7-9df3-4267dfaf52f2 | -12.86469 | -42.62615 | 2025-10-09 04:19:00 | NOAA-20 | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c2c571d4-4633-3682-bc88-97eb56866f31 | -15.31997 | -41.73993 | 2025-10-09 04:19:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| e4c50d9c-946b-3eec-9e6e-53bbedfa6485 | -10.93566 | -42.83564 | 2025-10-09 04:19:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 19975377-1f1f-3b7a-813e-3ccdb9bad351 | -15.05565 | -42.33491 | 2025-10-09 04:19:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 5aa53d01-1c4b-3a25-a437-a95d5cc523c6 | -9.76835 | -47.71118 | 2025-10-09 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a12b62c6-fda6-3a93-b283-7552a6343864 | -8.50739 | -44.22187 | 2025-10-09 04:19:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3cd50efc-44c9-3871-97a2-8cf179483127 | -11.06013 | -40.9366 | 2025-10-09 04:19:00 | NOAA-20 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 72ca4e7e-c0ee-3aa8-8249-9391ee516113 | -11.76607 | -45.14133 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d81668d-c06e-396f-992a-c504e6ca4109 | -12.25789 | -47.87646 | 2025-10-09 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b0ace1f3-30b6-331c-9021-4ed512c64760 | -8.17003 | -43.32488 | 2025-10-09 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d642ffe8-5cf4-3283-bc09-b1843c3f7ee6 | -10.86145 | -44.62724 | 2025-10-09 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a2923f92-1d2e-32b6-872e-af0e0614d6b2 | -7.45205 | -47.1803 | 2025-10-09 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7de886aa-bb90-3d44-b7cd-d60d249f97ff | -7.79126 | -44.19929 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 57bc6d7c-2493-325e-a839-30cf2befe167 | -12.16863 | -47.78004 | 2025-10-09 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cc1dcee2-2c50-302d-bb38-f74af98b955a | -8.62445 | -48.60953 | 2025-10-09 04:19:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8621fc8c-d1f8-33e8-b6f4-632d505882e7 | -12.42467 | -45.70554 | 2025-10-09 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 02aef037-192e-34bc-95ef-968d3f7c51d7 | -7.76217 | -44.03693 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3832e82c-7217-3136-9e1e-f0c0315c1af6 | -7.30704 | -44.77364 | 2025-10-09 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 32846b48-2512-3215-95d4-3cdf379f7e86 | -7.32967 | -44.80207 | 2025-10-09 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8d92f0b-9755-3ac6-ab5d-6622447e6e2b | -11.86893 | -45.50406 | 2025-10-09 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 26a3ace4-a107-38ec-b6d5-00ac366f6203 | -3.64438 | -39.37585 | 2025-10-09 04:19:00 | NOAA-20 | TURURU | CEARÁ | Brasil | 2313559 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c2f24f4b-a2de-3462-b33c-01315d6de983 | -7.31487 | -44.87426 | 2025-10-09 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd2c9b21-e13a-3cf9-bc6f-dd3d502110c5 | -8.62533 | -45.13646 | 2025-10-09 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bebecc6b-1377-3f28-be0c-17f015d3afa2 | -11.77438 | -45.1535 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 7c20a536-0ba4-358e-842f-b6efda18b70a | -13.67199 | -48.74613 | 2025-10-09 04:19:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f86af39-a9da-3ead-9163-2a684c50e18d | -12.04742 | -43.50295 | 2025-10-09 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 917ba760-4465-31f6-9008-82f9974ac2cd | -7.81309 | -46.71252 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0ec08288-e2ad-3d94-8c22-42a0475f1d65 | -9.64599 | -42.68822 | 2025-10-09 04:19:00 | NOAA-20 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2bfb22a3-575a-3d32-a8be-6403758626ef | -8.15036 | -43.33353 | 2025-10-09 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ed68bfa7-9496-36b3-a866-fc6a723e07ce | -7.69261 | -42.38951 | 2025-10-09 04:19:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4d65581d-e6bc-3ac5-9200-9307d8560a14 | -7.22624 | -48.24532 | 2025-10-09 04:19:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c824b78-afa9-3d90-b43e-e4f68420cb60 | -12.23271 | -43.78716 | 2025-10-09 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 51a2cc6a-0b98-36b2-9123-9d0f3223d9ed | -11.7683 | -45.14891 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f4e8484-db2c-376e-9022-01fca75bbf7e | -12.74245 | -44.61185 | 2025-10-09 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c46e8b07-da34-3c0d-afc1-f00a38dbf0b9 | -11.99159 | -41.41663 | 2025-10-09 04:19:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 012f8241-c9c3-37f1-9593-1b75bee1cc40 | -7.15125 | -46.88128 | 2025-10-09 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a02e8f2-bec5-3ce6-a31e-d40d075c1a9b | -11.12992 | -47.73809 | 2025-10-09 04:19:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c7658172-27ed-3700-99b7-82a2cc7c9271 | -11.24379 | -40.3382 | 2025-10-09 04:19:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| fcc619c5-e59b-398b-a05c-3ea3f19ddac6 | -11.99357 | -45.18461 | 2025-10-09 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1881b69c-1b64-3db7-a163-f76b9c7f51d3 | -8.56056 | -44.62115 | 2025-10-09 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0877d48e-0718-316a-9237-2a3ac660915d | -7.79513 | -44.19632 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7d09ee75-20ad-38ce-9dc5-623612a4153f | -14.28839 | -47.41669 | 2025-10-09 04:19:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 08c314a9-37cf-3755-8193-ff79013aaf29 | -7.77902 | -42.39429 | 2025-10-09 04:19:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e29da5a2-5edb-32fb-a2eb-d529c81b2768 | -7.79905 | -41.65631 | 2025-10-09 04:19:00 | NOAA-20 | ISAÍAS COELHO | PIAUÍ | Brasil | 2204907 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0e4559c0-fc67-3151-a281-3bcddcfce504 | -7.77697 | -44.24712 | 2025-10-09 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d5f052f-ee76-35dd-af6d-b3b5834e7688 | -11.00803 | -44.51528 | 2025-10-09 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4daa85ad-7377-33dd-a733-b6e51c924841 | -9.7579 | -47.70945 | 2025-10-09 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3477f65c-c002-3640-9772-1efa01480aa3 | -7.82981 | -45.18403 | 2025-10-09 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 49685c92-82ee-334c-a1d9-e51cc192d121 | -11.74506 | -45.1452 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| abae8d5b-3816-3ac8-abbb-a99445f7775e | -8.59979 | -47.98136 | 2025-10-09 04:19:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ac0b9c9f-8c41-3a1e-a6fd-52a95f6f4798 | -12.42411 | -45.70905 | 2025-10-09 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b0c98e1b-4af0-38bd-b1c2-17a0729d785c | -11.98363 | -45.20475 | 2025-10-09 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 99515b3e-3c0d-35c9-ad78-80ae17827c7e | -7.79844 | -44.19685 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fd914aed-234f-3140-b1ed-c5fe06798e58 | -11.98252 | -45.21182 | 2025-10-09 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 285a5226-4f21-38af-bffa-cefc52cffe0e | -9.08899 | -47.95782 | 2025-10-09 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| baf17f31-45fc-37e4-9185-db05e371ce95 | -9.18235 | -47.85384 | 2025-10-09 04:19:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1884992b-336e-3d71-9f9d-4ed869c05510 | -7.3049 | -44.83008 | 2025-10-09 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b844eaf7-ce71-3173-a24e-29433199dbbf | -10.19192 | -44.56593 | 2025-10-09 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7cc5db7e-e428-3848-85fb-ecc7bc2b3953 | -7.73387 | -42.39982 | 2025-10-09 04:19:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5b14c4cc-e3cf-37a5-80da-7934c18b32ce | -14.53089 | -46.62762 | 2025-10-09 04:19:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 62c59970-f18f-3bfd-bfe2-4c7405eaefdf | -10.54739 | -50.04409 | 2025-10-09 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78757c98-a193-3ec7-a05f-a24208feb16c | -13.82204 | -44.4328 | 2025-10-09 04:19:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb53332c-e4ca-35e1-8621-d83a10a26092 | -7.68505 | -42.39228 | 2025-10-09 04:19:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c5268427-c815-3e32-9808-dd2492a55944 | -12.85511 | -43.81686 | 2025-10-09 04:19:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| befd6c6c-75d6-33e3-82ea-b2de64339fc7 | -7.50936 | -48.34547 | 2025-10-09 04:19:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6abe50ee-7bab-3b05-9439-48532f624f6c | -8.1807 | -43.321 | 2025-10-09 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.7 |
| a3f8d128-cdb3-3f2a-9bb0-352e71625cd3 | -6.6995 | -46.2946 | 2025-10-09 04:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 69.0 |
| dd4a8e63-f508-30b4-8aa0-1d12467a63ee | -17.2705 | -46.9627 | 2025-10-09 04:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 5d6ed77b-5967-38a1-82d9-1072cdf265f1 | -17.9583 | -44.9863 | 2025-10-09 04:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 1d3ed474-968f-3660-a083-9c35377456c0 | -10.8558 | -44.6199 | 2025-10-09 04:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 31cc9688-07d8-3f1b-bc29-a2cbccb153b1 | -17.9227 | -57.4922 | 2025-10-09 04:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.3 |
| ea7042e1-8b29-38be-a673-3742cd255d8a | -6.6808 | -46.2961 | 2025-10-09 04:20:00 | GOES-19 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 5b61cf0e-3286-39d2-92bb-57b18c192400 | -20.3088 | -49.6951 | 2025-10-09 04:20:00 | GOES-19 | AMÉRICO DE CAMPOS | SÃO PAULO | Brasil | 3501806 | 35 | 33 | nan | nan | nan | Cerrado | 84.9 |
| c0e99b0b-143b-3c8e-a6ac-6692ced75ce6 | -8.1996 | -43.3189 | 2025-10-09 04:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.3 |
| 71815245-3da9-3809-bc78-4bffa6bf0768 | -15.0585 | -42.3178 | 2025-10-09 04:20:00 | GOES-19 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 68.4 |
| b60d722a-dbf8-3e0a-a8db-b61d2622a564 | -17.41648 | -46.54482 | 2025-10-09 04:21:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 022ce076-9114-32ed-bca3-4547ff6a8ba8 | -14.93042 | -46.78524 | 2025-10-09 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README44.md)
