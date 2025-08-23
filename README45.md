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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb76eef5-2d66-36f9-a4b4-5e4076ef5075 | -11.12972 | -44.77243 | 2025-08-23 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2a5fcf4b-83d3-3fff-ad0e-f8a45950ccc3 | -5.80769 | -59.21596 | 2025-08-23 04:51:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87ee25a4-0d99-3393-9076-eb5ea30cef98 | -5.88437 | -53.62368 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44b0d1dd-0bdb-3852-b621-7be3058f4b1f | -5.82834 | -52.07116 | 2025-08-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 44567eb1-45a4-36be-b643-000f613a7edd | -6.10855 | -44.40203 | 2025-08-23 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a24eb20-bfc5-3587-817d-dde5f81d92e4 | -4.83297 | -55.76956 | 2025-08-23 04:51:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7dcdb6fc-d584-39dd-b041-020403f9a769 | -5.85501 | -43.89241 | 2025-08-23 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 5e10a057-7ade-3367-92e1-6b1d747ff77d | -5.85545 | -43.88939 | 2025-08-23 04:51:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1ee497d8-be08-3a19-986b-6d24d56aa1dc | -7.03978 | -44.65825 | 2025-08-23 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b09d72b1-65b0-3d4a-b4ea-a63e868a4c63 | -6.38123 | -44.39266 | 2025-08-23 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a53dc2db-677a-33fe-855a-79ae83a41b83 | -10.21212 | -47.5733 | 2025-08-23 04:51:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cbadaf60-9849-3439-b602-f4e70bd17510 | -8.59668 | -62.624 | 2025-08-23 04:51:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dd2fc6c2-ed4a-3c67-9536-92b9080be371 | -7.39346 | -48.18288 | 2025-08-23 04:51:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ffc12adc-07eb-3929-8c61-6fc37da65ebc | -6.18515 | -45.43216 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 36ae0daf-eb7d-3408-9b41-34cf1e367d01 | -9.18581 | -59.61461 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f396b981-6a1b-3568-b0fd-e1940bc7ec57 | -6.3802 | -45.54002 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 44d83666-90be-394e-93cf-4e93bd076d1d | -8.67548 | -62.87652 | 2025-08-23 04:51:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c3c6f117-715a-3318-bf90-bfbeee82c5e0 | -7.07538 | -44.06489 | 2025-08-23 04:51:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e63118da-a5d0-3f59-a67e-137e3debeab8 | -9.56567 | -48.50587 | 2025-08-23 04:51:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 81d0d262-b5da-3e30-bbcd-d41abea5c4a0 | -9.18367 | -59.62722 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f2b60b3b-8a41-32a4-ad12-5bd55e935bd5 | -8.85194 | -49.86716 | 2025-08-23 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 81b24d60-b20e-354c-9db6-534ebe606a7f | -7.64226 | -46.28002 | 2025-08-23 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bf400a21-38af-38d1-ae87-4533f2e11e3a | -6.70974 | -43.19454 | 2025-08-23 04:51:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.4 |
| e28451ac-c1dc-3ea3-bfea-fea64546b930 | -6.00862 | -42.80249 | 2025-08-23 04:51:00 | NOAA-21 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fca8cdc8-8e71-3dfd-ba8e-1886a154e778 | -9.17444 | -59.7078 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e48a1fb-6105-3c6b-8f04-ac99cc15345d | -6.16552 | -60.09313 | 2025-08-23 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e70029d5-4110-3e77-8a55-a65321858182 | -7.03898 | -44.66388 | 2025-08-23 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35304c99-9b43-3e14-a7b1-9254335e0aef | -6.31907 | -43.76163 | 2025-08-23 04:51:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa82c685-3a40-3099-aaac-20844a8e1e0a | -7.79449 | -61.58334 | 2025-08-23 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7372ceeb-9477-32dd-b752-9f056114340d | -7.08018 | -44.06884 | 2025-08-23 04:51:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bfa5267c-1d4f-3a9f-bfeb-3e564ba20b11 | -6.62484 | -58.54652 | 2025-08-23 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea7624aa-5971-3b9a-977e-ed2bf2cac6ed | -6.39319 | -45.51659 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 49ddd4b3-5d42-3ca1-8901-585c24f27ac5 | -6.77573 | -44.32264 | 2025-08-23 04:51:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6dbf2d92-dbd9-3953-b250-476b3eac497f | -10.632 | -50.14138 | 2025-08-23 04:51:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b8598f94-35ad-3080-87a7-6d2cfc1dfce6 | -9.18249 | -59.59245 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b5d2274-3628-32f7-b8e1-49d07ffabdf9 | -8.52627 | -48.85886 | 2025-08-23 04:51:00 | NOAA-21 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f45d133f-c9ca-3796-84b3-0bbfeccba20d | -10.74289 | -48.26173 | 2025-08-23 04:51:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31bd51a3-f7e9-3449-be05-8091a77a2360 | -6.45793 | -53.3959 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50528f7a-a8e6-33ee-9415-c4f0832abb8e | -10.20836 | -47.56858 | 2025-08-23 04:51:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7fe06807-f3d0-3087-940f-8e105edb8eda | -9.20375 | -59.47308 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 33cfcde6-f54d-3f87-92c4-a4fb1f7ddfd0 | -7.09898 | -59.77533 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 85d07bc4-1276-3e13-88da-7c84b99a9050 | -6.45461 | -53.39537 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1b9fd1c3-69da-34f1-8d95-637af8bf765a | -9.19535 | -59.45473 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 42c08f89-e722-39eb-9329-e2c4b3bfc4b0 | -4.36578 | -54.8924 | 2025-08-23 04:51:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 692dd036-171c-3fcd-b1bf-03fe3895aa0b | -6.44798 | -53.39433 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 929128ef-d874-38b3-9305-c61902e4b84d | -6.11359 | -44.4028 | 2025-08-23 04:51:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37329c8f-73ce-37cc-ae92-715fddd72ae4 | -9.20597 | -59.44411 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8510c448-219a-3e2d-a208-2655a5fd298d | -6.37828 | -45.5371 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| eba65172-7ad2-3482-ad57-484f7ca50581 | -6.18638 | -55.46158 | 2025-08-23 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6a87b0d1-5ba2-3455-9746-f555847dbd85 | -11.13666 | -44.75982 | 2025-08-23 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ca973d9c-b163-30bc-81e1-1db6cf505bef | -9.44659 | -47.65435 | 2025-08-23 04:51:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 823f8f02-d864-3a5e-9e4b-67b0322c357c | -8.858 | -52.04361 | 2025-08-23 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 07462b8d-b840-3c5a-80a4-5aa5359d3475 | -6.39244 | -45.52168 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 6f9c8e33-d8fc-384e-aae4-80ab20643f62 | -5.8927 | -53.63577 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a0925592-ee2c-3345-8f98-532475e7edf2 | -6.58139 | -59.87478 | 2025-08-23 04:51:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5f485b65-b41c-3a4b-9961-704562813583 | -6.55906 | -60.06059 | 2025-08-23 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9300358e-636e-3dbc-a012-7c710cacf677 | -9.21164 | -59.45353 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bf7cf721-c3e6-380e-935f-40d0adbb557f | -5.73698 | -57.60519 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e3d84f4-1a9e-3d9b-bc50-3566cd072253 | -5.81214 | -59.21673 | 2025-08-23 04:51:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43448cb1-cf27-30ef-ba42-2d0e68e30d0a | -11.13583 | -44.76652 | 2025-08-23 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 39922e72-6397-33ba-8e0a-7641e1cdc182 | -9.21231 | -59.47463 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 097f0655-922f-3222-83f0-76cf98cafd5a | -7.29903 | -43.67229 | 2025-08-23 04:51:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 77fc5a91-9a87-38c8-b60f-e287ac5a5ddb | -4.78943 | -45.32541 | 2025-08-23 04:51:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5c8fc55c-c577-3259-a3c4-09861ba5a36c | -7.64163 | -46.28449 | 2025-08-23 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b2391e05-6d51-3dda-921f-40fe4fa1f55f | -3.84041 | -47.41329 | 2025-08-23 04:51:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05d82afc-d417-372f-86a2-26fa6f9099d6 | -9.20448 | -59.469 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5910172d-60c3-3f12-a8b9-310fc40da66a | -6.45902 | -53.38895 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67c84dda-8c8d-3e98-b2f9-73f125df1bed | -9.18575 | -59.58883 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27034924-d5f5-32b3-8e21-85db47bbb543 | -3.66154 | -54.75714 | 2025-08-23 04:51:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aff1859f-f5ef-3dd1-93e2-8bf187445196 | -6.18694 | -45.43367 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 56016eff-c8c8-3935-8920-2ffe96519256 | -10.21267 | -47.56924 | 2025-08-23 04:51:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6e9f6b22-48ce-3bf5-bdd0-94ca9eb89701 | -4.07819 | -48.04156 | 2025-08-23 04:51:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 05256db6-0d7a-3a10-83a4-0d13255678fb | -7.16295 | -47.5722 | 2025-08-23 04:51:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab66d55e-4d1c-3e04-9966-129ef9281042 | -6.73811 | -50.95395 | 2025-08-23 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 212287ef-869e-37d5-899f-5a68e25acbe5 | -2.97047 | -54.65737 | 2025-08-23 04:51:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b27d8392-42ce-3794-9986-f760c49527a9 | -6.796 | -45.0005 | 2025-08-23 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 17e40fb7-4c5e-3d28-9c1b-41ec0487d032 | -6.46124 | -53.39642 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3f00d02-e0f2-3fd1-8761-9fcabbb70082 | -3.64247 | -52.06345 | 2025-08-23 04:51:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aabc72a2-73b0-3180-9973-cdac220297f3 | -6.16411 | -53.76918 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ba1f0f9-38a9-32af-870c-66eb772b3ade | -6.36798 | -45.55846 | 2025-08-23 04:51:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d64a7df7-680b-385c-aa2b-a0b888e3adc7 | -4.43723 | -49.11107 | 2025-08-23 04:51:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c9017c75-fb20-37ed-917b-916bf2fb4c0b | -5.90996 | -43.47039 | 2025-08-23 04:51:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39cdf756-e94c-3e38-807e-7333943a9aa3 | -6.06836 | -53.8805 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6eef4f0c-d018-3799-9ca6-ba3b7033123d | -4.09141 | -46.92374 | 2025-08-23 04:51:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65499985-700d-3ed6-b0eb-2ce5edda19b6 | -7.29141 | -59.63808 | 2025-08-23 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6cd2c49e-7442-353f-95f2-e52d849ac2ac | -9.16569 | -59.68024 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93b29756-b7dc-3e3b-82b1-e34d7f82c83b | -11.06017 | -44.60167 | 2025-08-23 04:51:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9493ba9-5fd0-3fe4-8a00-40e2cc14ef9b | -5.7439 | -57.58842 | 2025-08-23 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c6508c7e-0b88-3908-ac5f-9aa28f3539d7 | -6.12297 | -53.7731 | 2025-08-23 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd3e9a2a-a14e-3164-b4be-b119e4d072d2 | -9.84582 | -56.07734 | 2025-08-23 04:51:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 53646e16-5f4c-39b0-90db-83b8d41de855 | -7.21542 | -45.3133 | 2025-08-23 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 63ae7733-f199-3474-baca-1c23f220a734 | -9.20748 | -59.46112 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0ee8bbaa-a82c-37ee-a1e5-e9f97419df87 | -9.25086 | -59.60873 | 2025-08-23 04:51:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52e2a397-3859-3bb7-852e-5e82dd31611c | -13.02902 | -56.87592 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 677ebcfa-2d02-3e07-898c-9b572594d25c | -12.70905 | -48.10586 | 2025-08-23 04:53:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6bbd4829-b7e5-3f2f-b8a8-fed01d9fffab | -14.76108 | -45.3837 | 2025-08-23 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c77857e4-8ddb-382e-aff0-35d11b5b2257 | -13.45313 | -47.02616 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e335b0c4-1a34-3360-910b-49f6de976303 | -14.9142 | -47.31664 | 2025-08-23 04:53:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 22494923-8a19-3c17-85cb-a5de726da00e | -11.93964 | -58.76525 | 2025-08-23 04:53:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c47bd3c5-7e3c-3f6a-8a95-88c92f57b9b3 | -14.78075 | -45.48172 | 2025-08-23 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README46.md)
