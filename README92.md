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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b386f462-2794-3dde-a92f-63237942c9d1 | -6.65948 | -43.66222 | 2026-09-14 15:48:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| bf5dd3fc-f547-3ecf-9448-2b32225ea2e3 | -7.09318 | -42.11839 | 2026-09-14 15:48:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| daca7b8c-0f8a-3215-b8aa-af40a1156271 | -3.74554 | -40.4225 | 2026-09-14 15:48:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 13.6 |
| ca0ae61f-8b26-3f17-9014-6dca0653b41c | -9.86672 | -45.99222 | 2026-09-14 15:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 37.0 |
| c91614e0-d97b-3b01-aed7-5bae0455927d | -8.58151 | -39.49392 | 2026-09-14 15:48:00 | NOAA-20 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 18.2 |
| ef99b20c-377e-398a-8636-6868fccc21d5 | -5.81879 | -42.74076 | 2026-09-14 15:48:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| eda56a5e-6abc-30db-a21c-240e778709dd | -8.56493 | -44.50046 | 2026-09-14 15:48:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ba3e86a0-294f-3fbc-818d-7ed7c6fb6654 | -8.2378 | -37.40145 | 2026-09-14 15:48:00 | NOAA-20 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 5.1 |
| fefd16bf-af3f-3c9c-a5e4-8ecf12e5a6a8 | -6.56782 | -45.3247 | 2026-09-14 15:48:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 16bbaae6-4749-395e-9248-8496bd8c9532 | -6.76103 | -43.66776 | 2026-09-14 15:48:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6983afa-8bca-36f9-98a3-2fab7a2430c8 | -7.96689 | -43.97983 | 2026-09-14 15:48:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cc95cc29-e44b-3ae2-9935-66ca35362c92 | -8.47938 | -44.86655 | 2026-09-14 15:48:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| fc0931a3-5839-3181-beab-1e03688ec0c9 | -6.299 | -41.69165 | 2026-09-14 15:48:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9378ed96-6797-3d43-b8ff-e378603f08b1 | -7.47048 | -45.96394 | 2026-09-14 15:48:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d9d99b6b-c0c9-3f59-945b-c6c1a9407dcd | -9.74135 | -45.27057 | 2026-09-14 15:48:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6334f7b6-2325-3e3c-bdbb-a2a8f97d8c0d | -5.66908 | -38.83536 | 2026-09-14 15:48:00 | NOAA-20 | JAGUARETAMA | CEARÁ | Brasil | 2306702 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 81748cb7-26ab-3986-befa-e3291c5979b6 | -7.97248 | -44.0225 | 2026-09-14 15:48:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5a48a433-8de8-3cbd-a30e-5fe9a149c5c2 | -4.95293 | -42.69359 | 2026-09-14 15:48:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 40f2fa8a-d36b-3871-912a-eb6b2462e0e4 | -6.52983 | -44.0926 | 2026-09-14 15:48:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2cd190f5-0349-306d-8d03-ac85f24f358b | -9.86264 | -46.0041 | 2026-09-14 15:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| c93ab817-1c23-353d-b17f-7edaf4dcf000 | -6.19848 | -42.45326 | 2026-09-14 15:48:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 60421f2a-46a5-3816-af44-f1ead150ba0c | -9.48247 | -45.46438 | 2026-09-14 15:48:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f45a33b7-467c-3e1f-a0b3-c044f1deae06 | -6.16108 | -35.14484 | 2026-09-14 15:48:00 | NOAA-20 | SENADOR GEORGINO AVELINO | RIO GRANDE DO NORTE | Brasil | 2413201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| db9eb175-8c45-36cb-91d3-33445603b9e1 | -9.48323 | -45.47076 | 2026-09-14 15:48:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0371f760-fb41-31aa-b0be-f048db76136e | -7.02779 | -44.63086 | 2026-09-14 15:48:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c4efc7d5-404d-3b11-a9b9-24c771cf40e1 | -5.02324 | -41.95599 | 2026-09-14 15:48:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 11a3bafa-a41f-3732-9b13-b508a6c5bae4 | -7.08828 | -43.95101 | 2026-09-14 15:48:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d6b69524-bd37-37d3-bfef-5418a9e93dc8 | -9.12269 | -39.99976 | 2026-09-14 15:48:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 75317696-6bfd-375f-8c90-2e3d4c766489 | -6.63982 | -45.12692 | 2026-09-14 15:48:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 79b84868-8632-3dca-9dd7-86fc667ba6c8 | -6.85585 | -43.75882 | 2026-09-14 15:48:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77cd71fd-6aa2-3287-ab03-7e64c949959f | -8.77267 | -37.28088 | 2026-09-14 15:48:00 | NOAA-20 | TUPANATINGA | PERNAMBUCO | Brasil | 2615805 | 26 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 9cc6c2db-6d59-33a9-8143-88fbe9ff41a7 | -9.86228 | -45.95395 | 2026-09-14 15:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| b8ef6358-63a8-3389-805d-c4e09152bbf8 | -9.15006 | -44.78106 | 2026-09-14 15:48:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8e531643-98b5-3b7b-ac0f-b33fcb8d1a70 | -3.73028 | -38.80299 | 2026-09-14 15:48:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| cf395ee1-4acc-30ca-971c-22f0eb524bb6 | -6.63411 | -45.13281 | 2026-09-14 15:48:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 4f792240-35a6-3788-aa30-7cfed0a6cb74 | -6.79594 | -43.75766 | 2026-09-14 15:48:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 60.7 |
| bdb9bfbb-c48f-3c35-8529-45cde465454d | -9.93977 | -45.77552 | 2026-09-14 15:48:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 8af561e5-9e4e-34e7-9616-16cf64cad1bd | -6.79704 | -43.76611 | 2026-09-14 15:48:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 8489284a-5b02-37ef-83c9-1068fdbaeee4 | -5.81663 | -42.73974 | 2026-09-14 15:48:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 2a9d7285-6902-30fb-a276-1ead7816bd39 | -9.8683 | -46.00581 | 2026-09-14 15:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 4224d2a5-0a61-3be6-93ff-0046d6f00d8d | -7.96749 | -43.98441 | 2026-09-14 15:48:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 13e05e1b-8cb8-3a61-ab62-997b0e20b948 | -3.66474 | -40.57305 | 2026-09-14 15:48:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 5e9bda0c-1ca7-384c-be7f-279da4ec3431 | -3.42569 | -39.61843 | 2026-09-14 15:48:00 | NOAA-20 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 32.5 |
| 1d2bc8c0-860b-3b1d-aafb-a358af6d3004 | -9.32355 | -44.3565 | 2026-09-14 15:48:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7e49fa3b-c083-3c40-9fc5-6f3955d361d3 | -9.86753 | -45.99911 | 2026-09-14 15:48:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| e9ff4386-a9e7-3fff-907b-5827353d929f | -8.04985 | -43.75449 | 2026-09-14 15:48:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| b858e29a-55fc-3ff4-b83f-490276800f89 | -7.52064 | -36.25758 | 2026-09-14 15:48:00 | NOAA-20 | CABACEIRAS | PARAÍBA | Brasil | 2503100 | 25 | 33 | nan | nan | nan | Caatinga | 5.4 |
| f12309c6-6864-3459-b891-142f8d7eef99 | -7.17171 | -44.53493 | 2026-09-14 15:48:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7d11d03f-f0c5-3fdb-a251-42d73e15b8e5 | -6.67028 | -43.65442 | 2026-09-14 15:48:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 992671a0-892d-3e4e-872a-0f24b96cb318 | -6.1108 | -57.7035 | 2026-09-14 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 127.6 |
| c9a9e468-33b6-3bd2-a31c-239aa43c47f5 | -6.2959 | -41.6824 | 2026-09-14 15:50:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 369.9 |
| 41eb20bd-21da-325a-a3a4-21d384b1f787 | -13.5719 | -51.4605 | 2026-09-14 15:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 345951fe-aaeb-3f3c-902f-9d2f3d2b9188 | -6.8446 | -55.5611 | 2026-09-14 15:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 03a7c90c-665a-3f47-a945-52fb2342dd77 | -11.8365 | -50.0028 | 2026-09-14 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.9 |
| c557496d-3ab7-3a46-ba05-5474564de68e | -13.3185 | -51.7051 | 2026-09-14 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 484a7b4f-a35a-3e1c-b52a-fc220bc4fb72 | -10.5667 | -51.3349 | 2026-09-14 15:50:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| a974a697-953d-349b-97c0-c3c9db2b9d0f | -2.6601 | -57.5702 | 2026-09-14 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 165de8c4-7c78-3de0-92b7-c28608b6525e | -3.6076 | -59.0769 | 2026-09-14 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 1f3760e9-1219-3877-9f9d-d59f00a78b3d | -3.3 | -57.8875 | 2026-09-14 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 57d72257-4c50-3f8a-9d1c-251e3a2a6693 | -13.3059 | -51.3022 | 2026-09-14 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 457.0 |
| 539e29e0-32f5-31d1-9ca4-39ccd9566c79 | -3.3138 | -59.4472 | 2026-09-14 15:50:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 3b9c5ecd-c6e1-3586-9e84-4e9b0ee4b04d | -3.6077 | -59.0577 | 2026-09-14 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 96dd9557-fa68-3857-8f72-c7d8c41bb70a | -13.3251 | -51.2997 | 2026-09-14 15:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 175b70ae-db7d-3354-9fab-29cbdbe68335 | -6.9183 | -55.617 | 2026-09-14 15:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 406ce234-eae1-3ece-810c-9610627db5f9 | -9.3852 | -49.3847 | 2026-09-14 15:50:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| fbb17de5-eb4c-3caa-ae3c-83641a44461a | -3.5893 | -59.0773 | 2026-09-14 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 101.5 |
| 776cdc41-bc95-3de2-a426-a0af094137a4 | -10.7715 | -46.3001 | 2026-09-14 15:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 84.0 |
| dc8f7e44-e561-3ca0-9cdc-82ae33d86d92 | -10.7015 | -54.1663 | 2026-09-14 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 19d9d816-122d-391c-9eb0-03915ae1e7e8 | -13.5526 | -51.4629 | 2026-09-14 15:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 08a7b11e-31ba-3e86-986e-661ea83d753f | -9.1339 | -51.5927 | 2026-09-14 15:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 73.7 |
| fa40ff2c-9be5-3645-b7cd-2c70ec2253e1 | -6.2917 | -55.2695 | 2026-09-14 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| b3a0feba-db69-3b98-b8f5-6aa9ef80221b | -10.2926 | -45.3161 | 2026-09-14 15:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 144.8 |
| b96bc31f-b2ae-3d37-a62c-248177b07ab2 | -8.5417 | -54.6985 | 2026-09-14 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 8b6e6c1a-ceda-3115-af5a-5eb6fba80489 | -6.8445 | -55.581 | 2026-09-14 15:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| bc31138e-aeed-3836-834e-f1e6cd9f48af | -4.115 | -60.6886 | 2026-09-14 15:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 104.8 |
| fe568703-01cd-3928-bf1e-40ca42c9142b | -3.1462 | -60.6506 | 2026-09-14 15:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 49.8 |
| e6ff1b1d-1103-3e8c-aa6b-a8e43da8db5f | -9.3753 | -50.1992 | 2026-09-14 15:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 92.6 |
| ddb238bc-28e7-33de-8098-4e56aefb8bb7 | -3.5894 | -59.0581 | 2026-09-14 15:50:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 8ca5b572-1812-343d-b670-284c794c8fe1 | -3.6997 | -58.8827 | 2026-09-14 15:50:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 42.1 |
| bcd1dadb-5f39-379e-b858-e018ecdddb33 | -14.1856 | -47.407 | 2026-09-14 15:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 94.6 |
| eaf87ddd-f5bb-3df1-9a13-6d1c5ee5701f | -2.6601 | -57.5507 | 2026-09-14 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| f272f546-57b7-381a-965e-9b4715b043e1 | -11.8362 | -50.0244 | 2026-09-14 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 5975bdcd-e297-3224-bcd9-8a93101946b7 | -10.312 | -45.2907 | 2026-09-14 15:50:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 403.2 |
| cb3af0c6-4dcb-3601-9c7c-3e71c23891df | -8.043 | -43.7565 | 2026-09-14 15:50:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 104.2 |
| b2369e35-e648-3404-aa13-d5d5ec07b447 | -10.7719 | -46.2775 | 2026-09-14 15:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 843f8919-098c-3087-8478-8179c0d35355 | -11.5095 | -50.2559 | 2026-09-14 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.0 |
| bbe37d01-8818-34f3-af3a-119b6b41a358 | -9.4581 | -48.0965 | 2026-09-14 15:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 844fb207-a7bc-3925-83c3-891daf49759a | -3.1514 | -58.644 | 2026-09-14 15:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 7e610459-0109-35d2-98fd-1107fecfb2e0 | -13.2867 | -51.3046 | 2026-09-14 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 493.2 |
| 908fe7ee-dffd-3b0e-956f-d18ddc6245e6 | -12.0273 | -49.9799 | 2026-09-14 15:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 2914ae0b-f8b4-34b0-b24b-93860df1963c | -6.3434 | -55.8442 | 2026-09-14 15:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 958cfa83-d4af-3d2f-a718-cfaa9b7482f8 | -6.6226 | -58.4995 | 2026-09-14 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| a6ff41ac-8f0a-3c5b-880f-ecb1968b8bad | -2.6602 | -57.5119 | 2026-09-14 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 285e28bc-53ce-3060-b1b8-534195a8d23a | -6.0731 | -57.861 | 2026-09-14 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| f8b77f60-bbac-3091-b6ad-67e7fb459863 | -6.6233 | -58.383 | 2026-09-14 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| b1995c37-1b54-3ca6-a940-42ce4b3e09ed | -3.4632 | -58.4062 | 2026-09-14 15:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 3f4c9a1c-6724-307b-a40a-3c1cac3b5ba5 | -13.2863 | -51.326 | 2026-09-14 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 7b238b90-5b8b-3ac4-a3cc-80f958e77ab6 | -6.5838 | -58.8304 | 2026-09-14 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 7a897f87-8f48-3dbb-802b-ddda5294ffb3 | -8.4112 | -54.7073 | 2026-09-14 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 6c566201-90fc-3701-8130-3272fb27d38a | -6.1111 | -57.6645 | 2026-09-14 15:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 143.5 |


[Clique aqui para ver as próximas entradas](README93.md)
