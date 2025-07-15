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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b64bc3c9-c15d-3b4a-9885-ddea377c399a | -6.38065 | -43.72522 | 2025-07-15 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 3be3a93a-ab3e-3c55-b396-c22f3527141c | -5.37306 | -43.92601 | 2025-07-15 03:42:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6fdc5927-989c-3a4e-a5a4-1b6ddb059a24 | -5.53747 | -43.88621 | 2025-07-15 03:42:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1bce99fd-ff34-3df0-84e2-46102d08a511 | -3.58322 | -47.51482 | 2025-07-15 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d0f10f46-a375-3794-96f5-bc2aa50192cf | -5.70144 | -44.24688 | 2025-07-15 03:42:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6ba09ab-2cd7-32dc-92b9-178d6dc06c90 | -6.2921 | -44.23283 | 2025-07-15 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 449ea4e4-1170-3cf6-befc-92fb38baa312 | -6.36525 | -44.74908 | 2025-07-15 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f34fe9b5-387b-3aa2-b024-32ff32a96bc3 | -7.49577 | -37.29034 | 2025-07-15 03:42:00 | NOAA-21 | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3cfc14d1-c0ae-35d0-bd95-354acdad52a4 | -6.29728 | -44.23403 | 2025-07-15 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63597ff8-bedc-3e03-b9fc-19f86806b6e0 | -4.78138 | -45.33891 | 2025-07-15 03:42:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fa0cdd52-bd5d-3e27-88e7-485eceddd2bc | -6.38219 | -43.71635 | 2025-07-15 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 98b9f280-4404-3350-8634-60ad1d7fe1c3 | -5.207 | -42.5056 | 2025-07-15 03:42:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ac183399-ca59-3e20-a797-795e21ec6db0 | -7.08741 | -43.69358 | 2025-07-15 03:42:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7c65e816-88f6-3646-ab45-c5b665bf420b | -4.00415 | -43.23558 | 2025-07-15 03:42:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3e02ec5-3d13-3b3c-bb63-6a7557fbb2fe | -3.38448 | -47.47028 | 2025-07-15 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 74347815-c20e-3348-8b79-e41fddaae8a1 | -7.27808 | -44.04154 | 2025-07-15 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 8dbbf6e4-907b-3c7e-9322-d7e6a0beb693 | -7.27861 | -44.03856 | 2025-07-15 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7e5b7dd5-5976-3f3d-b8a9-777335725fa8 | -6.29153 | -44.23613 | 2025-07-15 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d273d615-df83-36f4-b380-30cb9544924a | -7.20265 | -43.10152 | 2025-07-15 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 8ed579ba-039d-3b70-8a3c-5f7d9abbe6ee | -7.27914 | -44.0356 | 2025-07-15 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| a4921efe-a9dd-30a0-b2f1-0ef28f52e11f | -3.42977 | -43.34857 | 2025-07-15 03:42:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0756ddcd-c6bc-3e60-9a28-e942e501fdff | -7.09756 | -44.3862 | 2025-07-15 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc72e50c-2046-3516-8e58-57cda171b58e | -7.19767 | -43.10399 | 2025-07-15 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 5d0815b5-7f85-372e-96a9-ed7cd3800562 | -6.38167 | -43.71933 | 2025-07-15 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| a7913285-5a8f-3801-9582-0b512eb5dec6 | -5.54071 | -43.88889 | 2025-07-15 03:42:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 796139bc-44a4-35d0-bef6-e4feb0144f20 | -7.09637 | -41.48016 | 2025-07-15 03:42:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 512a6c69-d542-303b-8573-ade871882f9c | -5.1844 | -37.63847 | 2025-07-15 03:42:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 59837924-b5f6-3cbb-8e59-f28c8daeed93 | -5.70093 | -44.24547 | 2025-07-15 03:42:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2cbf3a9c-3fa3-3798-ba3f-c70ca7a9051b | -6.85697 | -39.75836 | 2025-07-15 03:42:00 | NOAA-21 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6eed72a2-0af7-35a6-b598-75cc4e8fcdcd | -7.0935 | -44.37891 | 2025-07-15 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7059900-26ab-32f5-b6ee-e3f8455880cc | -5.54125 | -43.88568 | 2025-07-15 03:42:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f725b553-cf9e-3be3-b447-153f89dddf93 | -5.53803 | -43.88303 | 2025-07-15 03:42:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e30aa957-1984-3a03-8cac-8a6c6a85fdab | -6.17926 | -44.38541 | 2025-07-15 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8a29ce99-2f3b-3a2c-8e46-304c1cb476f2 | -5.4834 | -42.14807 | 2025-07-15 03:42:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 48b77f0b-3190-37b2-853e-f47f28172696 | -5.23528 | -40.87117 | 2025-07-15 03:42:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| eb79dd0d-f639-3f32-968d-4b855db490f3 | -6.723 | -44.33288 | 2025-07-15 03:42:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dbfcdb91-4955-3d83-a724-10861d4f5756 | -7.09295 | -44.38198 | 2025-07-15 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cdd9574b-99fd-3fe4-a8d6-ba2670689539 | -5.54265 | -43.88703 | 2025-07-15 03:42:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 31cfb73c-bf98-3898-b6ed-a2eef7f85a7d | -7.20177 | -43.10674 | 2025-07-15 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 5627a752-a34b-33a1-9b3c-286ea405a315 | -5.7903 | -45.1171 | 2025-07-15 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ec42455-2e07-3257-bb28-02186f622c04 | -5.5366 | -43.88168 | 2025-07-15 03:42:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 85afddf9-b27c-35f3-893f-38ea5126c1f5 | -3.92529 | -43.1532 | 2025-07-15 03:42:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 37f4ac74-c305-3185-9c3c-a382d4a66697 | -4.78063 | -45.34315 | 2025-07-15 03:42:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 93a798bd-6be8-3db9-8869-03ba3ebdf2b0 | -6.378 | -44.7515 | 2025-07-15 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d7de0f1-3b10-3372-83c5-3e7e01b424de | -6.63116 | -44.57554 | 2025-07-15 03:42:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a05f57b1-7efb-3fec-a8ed-c2d95928304c | -4.4563 | -38.61002 | 2025-07-15 03:42:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2b16c56a-ef83-37a6-8447-e8ab8783a0cc | -5.78401 | -45.12006 | 2025-07-15 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7e40ae2-0c87-3e13-8263-68411a660807 | -7.16205 | -42.96761 | 2025-07-15 03:42:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f8790203-2b9e-343a-97ed-ffaff773c84b | -7.09801 | -43.50966 | 2025-07-15 03:42:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 99f7c4b6-7ba3-34e6-b8df-dea1a022e1b7 | -12.09882 | -44.7404 | 2025-07-15 03:45:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a17cab19-855c-3d03-acaa-8bcd86fd226f | -12.40723 | -45.3773 | 2025-07-15 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f2e40c4b-6399-3513-b8f3-515fbca1132b | -10.27762 | -47.61685 | 2025-07-15 03:45:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ab1f84c4-2ae8-30b8-9370-c073fa568680 | -11.9051 | -46.76103 | 2025-07-15 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62b899ab-1556-38c3-890c-552207a1a8a9 | -13.65876 | -45.73133 | 2025-07-15 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cac977ca-8457-33b3-8385-7cf6d90d83be | -11.36349 | -48.72786 | 2025-07-15 03:45:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 536c0f28-dcab-366c-b21b-db1b494a059c | -7.1025 | -49.1785 | 2025-07-15 03:45:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3d96305-ae16-3b77-8fc5-33847853cf08 | -11.46327 | -48.52607 | 2025-07-15 03:45:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5bbbec68-2714-32f4-bf42-2389a1586748 | -7.88937 | -44.49314 | 2025-07-15 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3fd3a6a5-d032-3411-a9c1-35c41695d4e9 | -11.44646 | -45.12573 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c1a061a6-bca3-30f3-b29d-263325f1d9d3 | -8.87189 | -37.01991 | 2025-07-15 03:45:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b42cd9f1-2676-30b6-8341-1b5c8976f8f3 | -8.60726 | -47.44113 | 2025-07-15 03:45:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6c84c75c-bcc2-33e1-8709-0bd128d35ae4 | -6.70602 | -47.80211 | 2025-07-15 03:45:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b63ce00d-5b30-3bcd-89b5-349257d8a33b | -7.0955 | -49.17722 | 2025-07-15 03:45:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 640247a8-f9eb-38f6-829e-82e7dc51ef06 | -9.1545 | -44.42036 | 2025-07-15 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dde265ba-c831-3e14-b613-175dd8ed252d | -12.69434 | -47.87479 | 2025-07-15 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 81fef3b4-2ba3-3454-8ef8-4ef1c9c3321f | -9.49213 | -40.38598 | 2025-07-15 03:45:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 8e9eddd1-8c43-338d-a81d-c917d5bc2fd4 | -13.13461 | -47.26875 | 2025-07-15 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df23bf57-62f7-3ba1-aabb-bda5321acc14 | -13.13511 | -47.26622 | 2025-07-15 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 07f8009b-da7a-31d2-a0b9-1244bc607284 | -11.44139 | -45.12476 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| b0520ee4-ac7d-3890-80c8-b0dc72e18c92 | -10.649 | -44.48852 | 2025-07-15 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65a0d837-0076-3caa-8945-5b3f9c0d4d94 | -9.48829 | -40.3853 | 2025-07-15 03:45:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 21748942-6b08-383c-b22d-b7a49cb4ae20 | -7.20622 | -45.32872 | 2025-07-15 03:45:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7b267616-a7cc-3716-864e-017ef8921391 | -7.08849 | -49.17596 | 2025-07-15 03:45:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e2c4b5ee-edf9-342d-b761-417b5e226690 | -9.16981 | -43.13671 | 2025-07-15 03:45:00 | NOAA-21 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e0b19f8c-da4d-3145-9e7e-b7450aa980aa | -9.62187 | -49.10402 | 2025-07-15 03:45:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e6c928f-a6c4-39e8-9327-8a9a6c9ebd01 | -9.80987 | -47.74569 | 2025-07-15 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2beb788c-74fd-3a77-8484-ca6b0938775a | -10.65 | -44.48291 | 2025-07-15 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dcd7a4ea-75ec-3de4-8db9-b19843eeacf6 | -11.4555 | -45.10543 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 5c88b00b-36f3-3b6f-953a-ac98223a23cc | -12.82011 | -41.95739 | 2025-07-15 03:45:00 | NOAA-21 | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 67d29914-fb46-36c9-9c4d-cccf19039973 | -9.80858 | -47.74779 | 2025-07-15 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 864f7a6c-a808-3485-86c2-3edc8e1dd7c7 | -12.4078 | -45.37425 | 2025-07-15 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf576704-b19a-3d5c-8cd1-25f32e06225b | -10.55967 | -49.14381 | 2025-07-15 03:45:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d073a6ec-c961-339e-bb53-783efdacee07 | -10.27899 | -47.61447 | 2025-07-15 03:45:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1fd89a62-63fb-3a2c-ab5a-f87c43b3d8a4 | -11.43969 | -45.13388 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| f6e9e505-eee0-31a2-b6fa-e41d241320de | -11.45773 | -45.09346 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| fce6cdf1-a9a5-3959-acaf-f13b316159ab | -13.65716 | -45.73041 | 2025-07-15 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4b386075-4f49-3527-a465-8fb0279c311f | -13.66164 | -45.7344 | 2025-07-15 03:45:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 025c28b0-5b0a-34a4-a721-1fa740c381d9 | -12.69525 | -47.87037 | 2025-07-15 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b1659a4-b6cb-39f6-a5fa-a4ecf106e9dc | -9.15397 | -44.42327 | 2025-07-15 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a1a6030f-2fa1-3fd5-89e4-a23b60bc6ddb | -7.88881 | -44.49634 | 2025-07-15 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2d732d48-d90b-39c5-b27e-bf169e2679d4 | -9.79756 | -47.74322 | 2025-07-15 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f7f86d17-0c12-3094-90d8-d725de87d317 | -9.61718 | -49.02205 | 2025-07-15 03:45:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f77848f4-e1a4-334b-b7db-06fd1d6cf964 | -9.80895 | -47.75052 | 2025-07-15 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 300a925c-4865-3b4b-b4ab-7cd0ad663140 | -11.73523 | -47.04885 | 2025-07-15 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b60419e-0b77-3628-bac2-994e1cae7fd3 | -9.80338 | -47.74174 | 2025-07-15 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 91dabb2a-791b-3ace-bb43-5c7b6367dfd7 | -11.46669 | -45.10161 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 02968d63-6c4f-3604-98ed-3734fe5541db | -7.81451 | -46.56761 | 2025-07-15 03:45:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2532af81-6fea-3669-bd47-110cbaf81034 | -10.69485 | -48.30141 | 2025-07-15 03:45:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b5fe5be8-edf5-376b-88c8-fd61c29dad23 | -7.08991 | -49.17921 | 2025-07-15 03:45:00 | NOAA-21 | SANTA FÉ DO ARAGUAIA | TOCANTINS | Brasil | 1718865 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d825ae00-69b9-33df-8daf-ca679dc8ad7a | -11.73443 | -47.05293 | 2025-07-15 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README7.md)
