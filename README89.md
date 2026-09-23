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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0067eb8e-71a3-3799-9e80-fc3f80c7d2dc | -11.47108 | -47.36797 | 2026-09-23 05:04:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 175314b1-e6d6-38eb-a88a-cf8704600d16 | -6.61612 | -59.91905 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 00f2dc5f-6263-337c-8c2c-af17617a40d7 | -3.98039 | -59.78252 | 2026-09-23 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee30cb07-30fe-3dd1-9bd0-ba93ee623666 | -6.93082 | -46.54971 | 2026-09-23 05:04:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 894c5743-6bf7-3f02-bec4-5f421b126a0c | -6.37618 | -42.78129 | 2026-09-23 05:04:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a28f6902-2dac-3153-a42b-1dce4008a6b8 | -9.09846 | -61.44187 | 2026-09-23 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| fa67969a-cc8d-3610-a102-df71790a00fc | -6.53019 | -55.35282 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db77189e-6fd0-31e4-ac09-40b210463c88 | -5.99658 | -57.71843 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23977caa-a958-3739-857c-8c63f8af4598 | -11.34947 | -43.3788 | 2026-09-23 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f277cc87-7c48-3430-91b4-0f80266c26c3 | -11.4717 | -47.36337 | 2026-09-23 05:04:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fbc8daf7-1608-3546-8c5a-a3caed2252d2 | -6.66526 | -55.05945 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a029816d-67e8-3f82-903d-daa5543c54ef | -6.9244 | -62.91187 | 2026-09-23 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e2447b2-e340-39f2-84d8-c22f1ac05aa4 | -8.48649 | -46.86464 | 2026-09-23 05:04:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| df0e356b-b7de-3c48-89af-adbc615d8044 | -3.85048 | -58.67051 | 2026-09-23 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2d8db9c-6210-3bfe-b203-4cad5533a8b6 | -8.48776 | -44.75381 | 2026-09-23 05:04:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b72313e-6484-3dec-8c9e-479063dcc59b | -6.63157 | -59.93575 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 091f6d08-6a9b-3864-a744-efad62cd78fd | -6.17521 | -53.28959 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c55c3fd-980f-35d2-9357-7a226895f99e | -6.97453 | -47.49136 | 2026-09-23 05:04:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1436f8a0-624f-332c-adba-0e1799e347ff | -8.74042 | -47.59762 | 2026-09-23 05:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ec19090-fbb4-30d3-8128-b3397e87ac02 | -6.66265 | -50.88353 | 2026-09-23 05:04:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 928ede26-4194-34a2-9ae0-7f580e895de9 | -6.58169 | -51.49112 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 07c552d7-92b8-3b1e-8dc2-19f49a52f273 | -6.67896 | -58.56437 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 32ef0b77-87b9-36dc-a3ae-c98862f1abab | -5.80355 | -52.08977 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf3c5111-f943-3879-94df-a50d82f73d4d | -5.40815 | -49.18752 | 2026-09-23 05:04:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e9e41d2c-5abe-32d5-849e-dc7483f88703 | -10.70391 | -48.71889 | 2026-09-23 05:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d53ceefd-2d6f-3686-96a5-f2178e22726a | -3.61019 | -60.56772 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1c199a8-0ea8-335d-ab8f-cf1eb92069a0 | -10.89491 | -53.96365 | 2026-09-23 05:04:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5cd68755-96fa-3b17-a6f8-31ba2097bccb | -6.18156 | -52.80437 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2163f85b-922d-331e-9837-9d8b73ff6145 | -8.19259 | -54.72825 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aa1115cd-c9c5-3030-89ce-ce5b7060a7fe | -6.92943 | -46.55588 | 2026-09-23 05:04:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16785dd0-cbac-3973-b0cc-7346f089002b | -12.12586 | -47.37723 | 2026-09-23 05:04:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02716bd5-a257-3a01-8772-a64a74d44fc9 | -6.67927 | -55.0617 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1df4e47d-962a-3834-a90b-06a8e3435054 | -10.45205 | -51.28475 | 2026-09-23 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 14c55339-73e9-3c14-8cb4-ab2696a57a3b | -8.28044 | -54.76877 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d540aa11-e10d-315f-8ee7-c71c1b7a12e4 | -10.31225 | -58.50758 | 2026-09-23 05:04:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5b7c268-c2ba-33a6-86cb-e8924ea0fa22 | -3.68607 | -60.59011 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 202274cf-56e7-3e45-8220-11b5ff79f00b | -11.75204 | -51.01806 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3eb470a4-9d40-3c5d-a402-fe446a1fa9dd | -10.47045 | -45.11066 | 2026-09-23 05:04:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43f0d18d-bb30-3e0c-af84-9142089d9c0e | -11.44149 | -46.72731 | 2026-09-23 05:04:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3bd6d237-78b7-3e4f-b447-0c69bcd94f92 | -6.6723 | -50.93412 | 2026-09-23 05:04:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ebbaad47-1eac-3218-8a2a-80cc97df79cc | -8.58779 | -53.1171 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d8ab8ee0-61cf-307b-bf9d-7cef5037792c | -10.00829 | -45.18902 | 2026-09-23 05:04:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 34be71a9-a413-3481-bdf8-23da86917c8b | -4.51772 | -54.97905 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 917e2726-0648-30c7-8093-0952e7dea2a3 | -6.00109 | -45.23342 | 2026-09-23 05:04:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 583e7d2f-03dd-31c1-9935-e3e4e9e55f9e | -3.85775 | -54.08241 | 2026-09-23 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d62861ad-2021-3560-8f54-75339ee33535 | -3.6876 | -60.58092 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8b7a540f-74f0-33a5-942c-82677c8cad9f | -6.33834 | -43.36922 | 2026-09-23 05:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9563ee32-803f-3de1-86ad-531a8538961c | -9.71478 | -48.32887 | 2026-09-23 05:04:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6785bccd-afb9-3a2f-b375-71292f5a9ecf | -5.34944 | -45.16022 | 2026-09-23 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3242a0b5-75f6-3007-8cfd-676ec5f576e1 | -6.16392 | -57.70857 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6769f787-a76e-3727-852d-a0f4cd4dc66f | -6.62001 | -59.91825 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 6a4c6a99-e019-30f4-b923-268c5e117eab | -6.34589 | -49.87571 | 2026-09-23 05:04:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c097f7b9-3b68-371c-86f8-b3df05fc7d47 | -3.68709 | -60.58398 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c51f250d-65b6-3e4b-9572-4144ed5e914a | -10.00179 | -45.19957 | 2026-09-23 05:04:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2e928aa4-1fd3-3314-aeb5-d4f24fb04553 | -11.6629 | -50.9793 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0b46855d-adbf-3394-997a-a9b2fc3659fa | -5.86896 | -52.06445 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44b53178-2c0b-3587-98ec-41f2ad7db8cb | -10.53823 | -43.97638 | 2026-09-23 05:04:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db8e369c-7359-3a9e-a91c-56c6207e3870 | -8.72813 | -54.98193 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 383f3112-c8dc-3348-83a5-4693e3a1d47f | -5.35413 | -45.16098 | 2026-09-23 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 464dd0c2-3114-3ef6-a894-9075fc680ada | -7.13357 | -48.42966 | 2026-09-23 05:04:00 | NPP-375D | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d93765ad-2fe2-35dd-b934-f3a2a0d71ece | -8.46391 | -48.6852 | 2026-09-23 05:04:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 274dba3b-1415-3303-ad5f-20256bbd0ee5 | -11.89058 | -45.78194 | 2026-09-23 05:04:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 020a6a16-ae59-3b4a-8421-f8f0de7a9527 | -8.37702 | -50.72427 | 2026-09-23 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 56b31663-4618-363e-b896-462aeced1613 | -3.71328 | -60.55403 | 2026-09-23 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2401e15b-bc20-310f-a525-895c1600a9fc | -6.29856 | -57.75133 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06d04587-3fbf-3ab1-a94b-1faa01011d3a | -10.70613 | -48.70374 | 2026-09-23 05:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c1328f00-f8e1-3ba9-9fc0-921e91e92e5a | -6.92757 | -46.56828 | 2026-09-23 05:04:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bea975e3-9a70-3871-921c-d27256738303 | -6.81407 | -47.87288 | 2026-09-23 05:04:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 64841b50-04ce-3fb5-8721-bb51b2c226ec | -6.67468 | -58.5636 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| af61cf26-f765-30f1-b764-33636c60a128 | -8.73217 | -54.97873 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fe5a8876-6b58-30ac-97bb-89273c249a21 | -3.19361 | -59.70293 | 2026-09-23 05:04:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c956b240-863f-3419-8928-73b4735e45bd | -4.13029 | -54.29452 | 2026-09-23 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1af7d4ce-2edb-380d-a864-3b0466ff7379 | -5.87773 | -52.04801 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1b492bd-b13f-310c-8c48-88db16658256 | -5.75302 | -57.53312 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0ef87c19-57da-32d1-99da-031ba20cb095 | -4.51708 | -54.98309 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 324b926c-c310-3b7b-a987-17cd2f27078e | -7.4032 | -44.73078 | 2026-09-23 05:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dcb7f9af-97c4-3225-84ac-7feb733c4375 | -8.83421 | -50.48408 | 2026-09-23 05:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7dfa117e-fe5f-3494-830c-6e43a15302f5 | -5.6211 | -45.2413 | 2026-09-23 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 66d694bd-3564-386e-b49e-fa42cf59b374 | -9.70556 | -58.1399 | 2026-09-23 05:04:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81acba94-1bc8-38a5-abce-bac5f9b96c2c | -5.76028 | -45.11605 | 2026-09-23 05:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 22464d7b-00a3-3c2b-9b11-6f42394cd8ec | -6.84356 | -55.53403 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dabf8a92-fd3d-3653-a960-bd85f27dc25c | -11.88635 | -45.77557 | 2026-09-23 05:04:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d9fc3cfa-ea7d-3b65-9040-95f51d546d07 | -9.04791 | -65.40962 | 2026-09-23 05:04:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8e569ec4-df6e-33bb-a545-aaad210e7f21 | -5.73934 | -51.76831 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00efa808-f047-3083-beeb-88a63c4c00a3 | -9.16421 | -51.52962 | 2026-09-23 05:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c3bbf14-e603-38e5-a989-6253dae57370 | -4.42419 | -55.08049 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6fa5303-c221-37ec-b58c-4d9ce91098ab | -10.71464 | -48.71173 | 2026-09-23 05:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8cb6c17b-3af6-385e-89ac-fc96c1c58c07 | -5.29877 | -56.09832 | 2026-09-23 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31770ce6-cd17-32cd-9453-a449f45eb3d0 | -5.80578 | -52.09727 | 2026-09-23 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2fb0897-4b21-3582-8223-e238b8b7d560 | -8.73624 | -47.59697 | 2026-09-23 05:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b51231ce-0259-3f51-b8b8-1474f4051e5d | -6.37451 | -42.79295 | 2026-09-23 05:04:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| fe474ef3-a382-3e18-b319-2167bb4e0994 | -6.61992 | -59.9249 | 2026-09-23 05:04:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 5a608311-cd86-34d8-92d6-909f4fa7788a | -8.6041 | -54.6053 | 2026-09-23 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9cc2f379-c8cc-32e0-8a68-f040e590bffb | -6.084 | -55.54166 | 2026-09-23 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0f1d596-8722-327c-9594-8fe78cbc522f | -8.79981 | -48.76101 | 2026-09-23 05:04:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8182d56-d8ba-3b0d-b597-0a5457eef534 | -6.30386 | -57.74478 | 2026-09-23 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50708c28-f089-3c29-8502-f62bcaa4a763 | -4.54105 | -54.94061 | 2026-09-23 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32ce3c17-9ffe-3272-89ab-88d72396870b | -3.28443 | -57.85803 | 2026-09-23 05:04:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f50fa143-926a-30d1-a9fc-f0615559cca0 | -6.5642 | -55.41198 | 2026-09-23 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1544390-fbcb-3115-914e-2685e264e344 | -11.65182 | -47.8062 | 2026-09-23 05:04:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README90.md)
