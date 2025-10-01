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

## Dados Diários - Página 141

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3fb54919-ac5f-32fb-9083-7235f2db914f | -5.76882 | -42.86461 | 2025-10-01 11:57:00 | TERRA_M-M | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 82002dc0-a12d-37c5-af9a-61c51dffd7a0 | -5.90017 | -43.91497 | 2025-10-01 11:57:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d0547af8-7b01-3521-9281-85d8efcd0bd3 | -5.49934 | -42.75211 | 2025-10-01 11:57:00 | TERRA_M-M | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 26.1 |
| c23846ae-d35d-348d-929d-b648085a68e0 | -7.7737 | -44.73014 | 2025-10-01 11:57:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8e474189-c9a9-39c2-9b39-e08c970876f9 | -6.7002 | -42.80193 | 2025-10-01 11:57:00 | TERRA_M-M | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 21.8 |
| 2946f40f-793b-35c7-b0df-15605ab79fbe | -5.95559 | -45.86653 | 2025-10-01 11:57:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |
| db058700-f3e1-3cb1-a0e8-37d0b901fa56 | -3.85894 | -40.43674 | 2025-10-01 11:57:00 | TERRA_M-M | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 31.0 |
| 35432545-e916-374e-88db-d6c08d0053ed | -3.80536 | -42.15756 | 2025-10-01 11:57:00 | TERRA_M-M | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 19.4 |
| dc1744ac-1d7e-3692-811e-6e59c374cdb0 | -5.72102 | -42.69199 | 2025-10-01 11:57:00 | TERRA_M-M | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 63d778a6-d33e-3e09-83e8-0a180acf56a0 | -6.33636 | -43.02594 | 2025-10-01 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 5c7f9fb6-fc92-3e45-91f7-e95dec1f9880 | -4.43186 | -44.39034 | 2025-10-01 11:57:00 | TERRA_M-M | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| f60138d0-25f8-3011-ada6-976a9c986a44 | -6.54527 | -43.92149 | 2025-10-01 11:57:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 9ea70487-555d-3477-b12f-ce6717df4baf | -6.06036 | -42.44909 | 2025-10-01 11:57:00 | TERRA_M-M | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| e218dad6-2e3e-3882-9c2f-ae667fc6ca72 | -7.12803 | -40.71731 | 2025-10-01 11:57:00 | TERRA_M-M | SÃO JULIÃO | PIAUÍ | Brasil | 2210300 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 08f28d9c-17b7-350f-aefa-d03ee966c989 | -6.27701 | -44.05435 | 2025-10-01 11:57:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 72978a18-2a16-399a-9c12-4d9d5c5bcb96 | -6.50914 | -44.29028 | 2025-10-01 11:57:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| aac4bb4f-5ea5-3435-9fe5-1e106e713728 | -6.73062 | -44.59378 | 2025-10-01 11:57:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 84768172-c3b8-377c-abf9-6692af51710d | -6.22354 | -44.22015 | 2025-10-01 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| cced7995-0536-3c12-8ef3-a24dfee92b4e | -6.79434 | -43.80323 | 2025-10-01 11:57:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1132e0bf-51ed-34b5-9194-b5d11b1ad589 | -5.89379 | -42.51285 | 2025-10-01 11:57:00 | TERRA_M-M | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 37.9 |
| dd605f22-ea63-3c75-b86c-e179e5e2b1cc | -6.21741 | -44.22337 | 2025-10-01 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 10572368-6dbf-3452-bafd-2be23d027198 | -6.50796 | -42.48027 | 2025-10-01 11:57:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 0a6f8196-e904-3c0d-a83d-e8999159444b | -6.04052 | -36.53571 | 2025-10-01 11:57:00 | TERRA_M-M | BODÓ | RIO GRANDE DO NORTE | Brasil | 2401651 | 24 | 33 | nan | nan | nan | Caatinga | 20.4 |
| ffa36a4d-935b-3b97-a134-4f9808522a62 | -4.59597 | -43.50518 | 2025-10-01 11:57:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b73ba325-8b99-3a6a-a066-48f2ff1f38d8 | -6.54431 | -45.21424 | 2025-10-01 11:57:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| c3917d68-a61d-3150-b072-592fef358fad | -5.85769 | -43.39713 | 2025-10-01 11:57:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 2af07a09-9e4c-3be6-ac1d-c9355d8540cb | -5.86809 | -43.89358 | 2025-10-01 11:57:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 17a3f19b-2adc-33c0-8e4f-98d5ce420c86 | -6.39768 | -44.28946 | 2025-10-01 11:57:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 128a3c3f-d15c-3b39-af42-931ff63b8166 | -5.82995 | -43.95895 | 2025-10-01 11:57:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 5437817a-bd52-326b-8ec5-5d0207133b82 | -5.62381 | -43.23027 | 2025-10-01 11:57:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 1d572add-31da-3001-8600-99a369a93382 | -3.88275 | -42.51318 | 2025-10-01 11:57:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| ac2cbae3-702d-344c-b23f-7112f5d1358c | -6.66302 | -41.40026 | 2025-10-01 11:57:00 | TERRA_M-M | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 1e60ade1-71d4-3f9f-a859-31ec2880475a | -6.10041 | -43.12281 | 2025-10-01 11:57:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 3598bc50-da2a-3ec6-9b81-c0fa17aa83d0 | -5.33574 | -43.75013 | 2025-10-01 11:57:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 0b5fcdea-592d-3080-b39e-4e38de6b171e | -5.85632 | -43.40651 | 2025-10-01 11:57:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 41ac393e-e6c3-3850-abad-9f80bbd0e8ce | -7.79563 | -42.5056 | 2025-10-01 11:57:00 | TERRA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 26.8 |
| 808867ee-0422-32de-810b-c895f3c10e66 | -4.9562 | -42.04125 | 2025-10-01 11:57:00 | TERRA_M-M | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 56.9 |
| be6a61d4-3167-32f1-8a9a-116090428bef | -6.10985 | -42.68081 | 2025-10-01 11:57:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 360de781-431e-3d17-884d-0b388b309e9b | -15.9388 | -43.2979 | 2025-10-01 12:00:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 857f52ce-e841-3042-9eda-01383bafda84 | -7.8193 | -46.7338 | 2025-10-01 12:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| d263ebe6-009e-3ea9-aa49-6da01cd7b8db | -8.8929 | -46.6072 | 2025-10-01 12:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 24a4187a-f098-3e3d-ac9e-dcb0eef67013 | -11.4596 | -45.0433 | 2025-10-01 12:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 067c3be0-c832-3287-b63a-6e38f09e0fb0 | -8.5404 | -44.6975 | 2025-10-01 12:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 27f5fb1f-8b52-3ac9-978f-486e8c09fd7e | -7.5561 | -46.7795 | 2025-10-01 12:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 3acb05fc-0c54-38e6-88f0-6a2e660e8464 | -14.1926 | -46.1091 | 2025-10-01 12:00:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 0ebfe3a0-6cc7-3f5d-873c-9c398e0f08c5 | -13.3274 | -47.8536 | 2025-10-01 12:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 0f0d7dd0-47ba-3c80-b4c3-558f10bfe631 | -14.3519 | -45.9206 | 2025-10-01 12:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 147.0 |
| c2056560-f869-3f5f-bc49-4192ff697414 | -14.3462 | -47.1323 | 2025-10-01 12:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 6d4ab363-84c2-37af-b789-66e4b1be9620 | -8.672 | -47.7144 | 2025-10-01 12:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 811778e4-53da-3ffc-9a9b-e787195b7a9f | -14.9733 | -46.8896 | 2025-10-01 12:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 94.9 |
| ab9940cd-b92b-396a-878a-1d112172c996 | -14.1732 | -46.1124 | 2025-10-01 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 133.2 |
| 7c9143e3-1838-3424-90ff-96eff11566af | -14.8016 | -45.8178 | 2025-10-01 12:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 110.9 |
| a11ff841-de51-3370-b270-6134eb14285d | -10.8421 | -46.6514 | 2025-10-01 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 9496e9a0-cf4b-38ae-9175-fc8f1b7bbc97 | -14.3514 | -45.9437 | 2025-10-01 12:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 182.7 |
| 04d6ab33-7ec4-36d1-8277-748725f9f5cf | -14.4943 | -48.4553 | 2025-10-01 12:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 00942128-e7f8-3964-994f-37368a6a935e | -14.8021 | -45.7946 | 2025-10-01 12:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| ce84419f-0ebb-3bea-98cf-7cbed656df32 | -14.3657 | -47.1291 | 2025-10-01 12:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 82.2 |
| be150e78-0697-3f1d-89b8-9880837aba66 | -7.819 | -46.7561 | 2025-10-01 12:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 823bd365-6cb4-34ab-92d3-2bffe1c895c3 | -11.829 | -48.0619 | 2025-10-01 12:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 15038213-413f-3926-b043-dded91fb0ad3 | -12.8831 | -46.9101 | 2025-10-01 12:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 3b6532ea-1045-3c77-b635-30acb103cd75 | -14.7836 | -45.7516 | 2025-10-01 12:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 72540823-7e43-3375-b393-7fc275922b2e | -11.8482 | -48.0595 | 2025-10-01 12:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 230f1e6f-185a-3129-a46f-90094443ea95 | -10.9769 | -46.5443 | 2025-10-01 12:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 2c8f9d2b-fbd3-3761-9ec3-a662deddde4f | -11.46 | -45.0202 | 2025-10-01 12:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 9a81d396-1f03-3667-8a28-4796cce08e9e | -12.7022 | -45.2715 | 2025-10-01 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| aae9a410-b755-3f0e-8953-53dc7b679223 | -7.8002 | -46.7578 | 2025-10-01 12:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 115.8 |
| dc112633-a8db-38d3-8f48-413cfc7f6ed5 | -14.3714 | -45.9172 | 2025-10-01 12:00:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 193.0 |
| ae2eb512-019a-324e-872d-b349870d55ee | -14.49548 | -42.17105 | 2025-10-01 12:00:00 | TERRA_M-T | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 85abdc91-ad47-3e4b-941e-5fb121cf9e24 | -12.36863 | -50.18703 | 2025-10-01 12:00:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 51.5 |
| cd3dc2da-3002-3a4e-a761-d78c549de992 | -8.55799 | -44.65226 | 2025-10-01 12:00:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f63fd02e-8819-3f6a-b220-f10912a22a5a | -11.9286 | -48.00536 | 2025-10-01 12:00:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 9c7beca6-8a7e-3ecb-b6af-2cbd694f4601 | -9.89444 | -45.96212 | 2025-10-01 12:00:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 7e5ee31b-4d00-3502-a6de-d78aa8bc660d | -10.82794 | -47.96497 | 2025-10-01 12:00:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 961d96c8-3b55-316d-ad82-115768bf708e | -9.13108 | -43.02533 | 2025-10-01 12:00:00 | TERRA_M-T | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 0f7b58b7-567f-3ee2-a8be-14a28a5b3649 | -12.95124 | -46.41957 | 2025-10-01 12:00:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 54.7 |
| f32f9341-97bb-3a96-881b-374c9613c006 | -11.60226 | -45.03978 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c18afb69-ebdc-39cb-a918-a2523f00e14f | -10.8418 | -47.95124 | 2025-10-01 12:00:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 66007085-c616-31c8-8145-ff72e4815cfa | -7.82536 | -46.98246 | 2025-10-01 12:00:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e0352367-8fc6-3d95-9f19-ce862cac386f | -13.92185 | -48.08187 | 2025-10-01 12:00:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| ba7b1037-c47a-383c-ad7b-5f2131aaf1ec | -14.34775 | -45.92686 | 2025-10-01 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 39.9 |
| cd54d821-7cb1-32e6-a4e3-52b18f199704 | -10.90736 | -46.50779 | 2025-10-01 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 4857cb31-09ea-365e-9cae-47283783fbef | -12.7639 | -46.8968 | 2025-10-01 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 15c6c8a6-40e5-39c8-98db-366b6ae95111 | -9.6502 | -45.55108 | 2025-10-01 12:00:00 | TERRA_M-T | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 5d0faa43-257e-3e73-913b-3fb961023a5a | -8.58332 | -44.73893 | 2025-10-01 12:00:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 28d0fb65-5003-3e13-8064-9469b27fcd42 | -13.86831 | -41.91088 | 2025-10-01 12:00:00 | TERRA_M-T | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 8b309343-e12e-3f26-99a0-b35835a1c30f | -12.84871 | -42.62587 | 2025-10-01 12:00:00 | TERRA_M-T | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 14.0 |
| fc0cc95c-c71d-3709-8a85-1517523d3159 | -12.87556 | -46.77371 | 2025-10-01 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2ae24d57-ebaa-33fc-96b6-c29daea4a585 | -10.95206 | -46.54587 | 2025-10-01 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.8 |
| b8fa4e18-4f07-3d5c-9037-dcdc595e1b3c | -8.41793 | -46.81377 | 2025-10-01 12:00:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| eb67888c-73da-377c-b982-85b0a0590871 | -13.93168 | -48.10398 | 2025-10-01 12:00:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 19.1 |
| eea0cd7c-4bf0-32c6-9afd-3cedac1e3711 | -13.97961 | -44.87621 | 2025-10-01 12:00:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 05d26dcc-b7e0-33b2-8eae-06592af2a74d | -13.23826 | -47.33029 | 2025-10-01 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 9e6d2049-ef38-37b4-8590-88423b3c576b | -13.9282 | -48.11208 | 2025-10-01 12:00:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 22.7 |
| e09e9b42-933a-3c9a-affe-2687720d43c1 | -11.60369 | -45.03027 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 17582d79-dbf7-386c-a34c-fe2becfbdff1 | -8.68159 | -47.69748 | 2025-10-01 12:00:00 | TERRA_M-T | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 38.7 |
| efd2ec19-8b84-311f-945e-0524c1e366ba | -10.92472 | -43.6365 | 2025-10-01 12:00:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 3531830d-5006-322e-9855-5a25123c85c0 | -8.15674 | -46.26323 | 2025-10-01 12:00:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 8d709a8b-0ae3-352a-af87-1267715b250f | -9.9319 | -43.67276 | 2025-10-01 12:00:00 | TERRA_M-T | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| e417b6ee-7791-340b-9da5-392ea532e5ec | -14.35556 | -45.93869 | 2025-10-01 12:00:00 | TERRA_M-T | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 132d45a3-0496-3759-b597-1a7753c6f1aa | -11.46364 | -45.03288 | 2025-10-01 12:00:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |


[Clique aqui para ver as próximas entradas](README142.md)
