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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75ac3c25-1f1a-3641-aeb4-5b2993ce604b | -21.07644 | -49.99285 | 2025-08-06 04:00:00 | NPP-375D | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 4bf752a5-b331-3fa5-aee9-abb9a59c05b0 | -15.68908 | -48.96731 | 2025-08-06 04:00:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0cb650ea-49f8-384e-b456-47fc1de5f773 | -15.69422 | -48.96763 | 2025-08-06 04:00:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 41d0a5d3-924e-3961-97ac-adcbf13a2347 | -16.33606 | -50.35415 | 2025-08-06 04:00:00 | NPP-375D | SÃO LUÍS DE MONTES BELOS | GOIÁS | Brasil | 5220108 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d85e48e9-154b-3ee3-8f16-4127c53987dd | -21.08125 | -49.99401 | 2025-08-06 04:00:00 | NPP-375D | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 91563325-d152-3487-8836-a59ae9878c4b | -17.82833 | -55.10357 | 2025-08-06 04:00:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 5401014c-3cec-3251-9751-696acceccfae | -19.84261 | -51.20048 | 2025-08-06 04:00:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4cd51ae-20dd-3347-9603-2d7c01cb2cd5 | -17.8268 | -55.10308 | 2025-08-06 04:00:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 50c75a6f-38b0-35bc-afb0-2da00b2b28ff | -23.31566 | -47.48741 | 2025-08-06 04:02:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ccbe5de0-9b0a-31f8-bff2-4ae4f4c5199d | -22.66163 | -47.31964 | 2025-08-06 04:02:00 | NPP-375D | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2ef7999a-5379-34e0-8bf1-bb006884815c | -22.79034 | -46.9875 | 2025-08-06 04:02:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0c6f3adc-02d7-389d-b9b3-220045891ff5 | -23.31061 | -47.49214 | 2025-08-06 04:02:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| a19b2106-c50b-35fe-a43b-dd48253abca7 | -29.90047 | -54.66593 | 2025-08-06 04:04:00 | NPP-375D | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| c070e565-29fb-3008-9234-2dbed9c7187d | -29.90246 | -54.66958 | 2025-08-06 04:04:00 | NPP-375D | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 9d70f69d-d355-3733-ba10-0d398b5dc9ab | -29.90339 | -54.66584 | 2025-08-06 04:04:00 | NPP-375D | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| b5f05e6d-54e2-398a-9095-e9d47f1c7dbb | -29.90572 | -54.66754 | 2025-08-06 04:04:00 | NPP-375D | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 05a8e23b-6192-3c3c-9560-b32447d0a225 | -29.90482 | -54.67131 | 2025-08-06 04:04:00 | NPP-375D | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 43378641-f322-3a1b-ae4f-8902a30ed1d2 | -13.0731 | -56.8527 | 2025-08-06 04:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 18fb8a27-8755-309c-97b0-a60cc8fb5a8a | -8.9213 | -60.7489 | 2025-08-06 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 0a908bdd-12b5-3ce3-960a-c317550f1f7d | -8.9028 | -60.7498 | 2025-08-06 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 7f1f463c-e3e7-3582-8442-7fc4edcdc471 | -11.4393 | -45.1154 | 2025-08-06 04:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 55.2 |
| a96c8424-1595-3107-84a1-4e16d0da7837 | -13.0728 | -56.8729 | 2025-08-06 04:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 5a50f5bd-689f-3284-a440-175ffcd48c5b | -8.9215 | -60.7297 | 2025-08-06 04:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.3 |
| ddabdbfa-d547-32fc-b6e9-58d61ec06b1e | -11.4389 | -45.1385 | 2025-08-06 04:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 4bc8a24c-13fc-3480-bfff-364fa4bfab47 | -5.50909 | -35.58029 | 2025-08-06 04:17:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 6001a1bf-cb04-3fc3-aaa9-cc718c8436d9 | -4.02136 | -48.06797 | 2025-08-06 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9231ca1c-9216-371c-9a8c-17d647d39016 | -3.10834 | -47.01043 | 2025-08-06 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3aa7227b-8f11-3df7-9630-be5bf9edb0e2 | -4.02883 | -48.06918 | 2025-08-06 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e2ebd162-8032-312f-b2c2-17ce75132b7c | -5.51439 | -35.58104 | 2025-08-06 04:17:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| e7c4a6f5-2cd9-37f7-9b0f-63c4d2660fea | -3.03838 | -49.4311 | 2025-08-06 04:17:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 91be77b2-381b-356d-8317-ff8632abfe33 | -3.09266 | -46.74538 | 2025-08-06 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 296bfd27-c85f-35b7-951e-52f333235794 | -5.04774 | -45.04584 | 2025-08-06 04:17:00 | NOAA-20 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f9ae778-4d96-3d78-9d61-344e510dbe47 | -3.86429 | -48.03637 | 2025-08-06 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6b50ca3-0ca0-3c5d-b73a-9edcfabe511f | -4.62249 | -46.52961 | 2025-08-06 04:17:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cac0b062-eb09-3e07-a6c7-bcb0cf5bdd1f | -2.8844 | -40.38923 | 2025-08-06 04:17:00 | NOAA-20 | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b06cdbf7-5345-352d-9c88-d9d2ca85cae4 | -3.09202 | -46.74935 | 2025-08-06 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| defa475c-923c-3f14-ba39-3c94977f966b | -4.02581 | -48.06408 | 2025-08-06 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0aab6067-3579-349b-b472-8ddf108e27ab | -4.13894 | -46.45871 | 2025-08-06 04:17:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f155a5d-9b4a-3121-a0a4-1d507dc9ca03 | -4.77871 | -45.34982 | 2025-08-06 04:17:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0679e1d8-9e2c-3f4e-b443-d877dda4cfd5 | -3.80328 | -51.1506 | 2025-08-06 04:17:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fb3159f-898d-329d-a7a5-9be3619fd5b7 | -3.01927 | -46.91095 | 2025-08-06 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d4598b93-c9ea-326e-bf78-59937e91eedb | -4.30316 | -48.10355 | 2025-08-06 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 355674f9-3dd8-3979-8ad3-7f809cfa2d76 | -4.191 | -38.37236 | 2025-08-06 04:17:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2a2812e7-b6df-3c2d-9687-b9c16a7ef8dd | -4.03641 | -48.09368 | 2025-08-06 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a270b24d-2db5-3b24-b7e2-57a3b92e2eb3 | -4.02653 | -48.05965 | 2025-08-06 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 294e87bc-f26e-3656-a1e0-b4419abae7b1 | -3.1828 | -48.8118 | 2025-08-06 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a22cf53c-9d5d-3c01-afe8-ed46d567ebf7 | -4.28965 | -48.06936 | 2025-08-06 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 55fd7e73-1af0-3ef8-9f47-2a4ee64d1550 | -4.09323 | -46.92138 | 2025-08-06 04:17:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f326b98-0244-3161-a09d-fbb107c48051 | -3.12262 | -47.01272 | 2025-08-06 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d51f6fed-a0df-3c7b-a718-45efb92ff0e4 | -4.77483 | -45.33123 | 2025-08-06 04:17:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dd659a3b-99e7-360c-900e-86f8a1d73092 | -3.94143 | -48.44223 | 2025-08-06 04:17:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 889afa3a-5e2c-3f5c-95c2-d042a5698589 | -3.18613 | -48.809 | 2025-08-06 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bfe37476-f645-315a-9cc9-30e50e792768 | -3.97796 | -47.03008 | 2025-08-06 04:17:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ac2a344-9dac-3967-8417-125d8ccbad4a | -3.18217 | -48.80837 | 2025-08-06 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4429eef2-b450-3d24-b40a-9ab783f67fb9 | -3.02283 | -46.91152 | 2025-08-06 04:17:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3ac9429-4d3a-3828-bf50-96e81d39b2c4 | -4.02208 | -48.06348 | 2025-08-06 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| baeb7660-f4c5-364d-bb12-9eac8337d4d0 | -4.77427 | -45.33473 | 2025-08-06 04:17:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 30767b93-3720-37b4-9ebd-755e7906a310 | -3.18134 | -48.81342 | 2025-08-06 04:17:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d1eaf8f-311d-3bac-bec4-942ade58bb59 | -9.7006 | -48.87634 | 2025-08-06 04:19:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f01e29d5-46b0-36c8-af04-f5b1b6d2adb7 | -6.41153 | -53.37671 | 2025-08-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 29a5c152-442b-308a-9f27-3a4e690c657c | -6.79142 | -43.25141 | 2025-08-06 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d0c3c11d-db4c-381e-abf1-ecd65776d053 | -8.06678 | -49.7155 | 2025-08-06 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1aa932a9-e2b7-38ca-ab53-175b6cfeee72 | -5.80241 | -46.99653 | 2025-08-06 04:19:00 | NOAA-20 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 10744c52-c4b9-3383-90c1-d5232838ac2b | -10.48213 | -44.34559 | 2025-08-06 04:19:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bbdc9455-f940-385b-96d4-e6182031c3ed | -6.67991 | -49.78534 | 2025-08-06 04:19:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60bac35c-6ddb-3497-9fe1-0c1d98bc254d | -7.24369 | -44.60717 | 2025-08-06 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e918452b-1165-3fba-8862-16ae9b42550f | -10.48157 | -44.34921 | 2025-08-06 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e3ba261e-653e-33e3-abd9-b5c96d75bb22 | -12.55487 | -44.73888 | 2025-08-06 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a574fdd8-634c-3214-9ac7-b3cbc7161120 | -11.43642 | -45.13253 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| e597a631-5cf6-379e-8441-84cea3979cd8 | -7.50983 | -44.8591 | 2025-08-06 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fcbaa356-5bdd-30a8-9757-b0c227b2909d | -7.55441 | -45.17838 | 2025-08-06 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 784da372-cae6-327b-b388-5aa74c2a00b2 | -6.39081 | -44.50134 | 2025-08-06 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f32ff596-0d73-3dd9-9f88-ceca2e0b02cd | -7.63547 | -44.57665 | 2025-08-06 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1bcabc13-d67d-3321-a794-3d86860020c5 | -6.27633 | -45.26949 | 2025-08-06 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 659ddb71-301c-3b22-bacd-f990fcae35f9 | -8.19609 | -49.50051 | 2025-08-06 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c486939b-5bb0-304d-aafc-6cb356774ece | -11.76313 | -45.01643 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c373c605-df86-3fce-80aa-db5dea30bf97 | -8.60581 | -45.49233 | 2025-08-06 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 926b48b2-4c85-3e10-9b20-f5752c33984c | -6.42037 | -53.37037 | 2025-08-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ef952d2-df04-3d72-8220-78e0ead7dac6 | -6.70797 | -43.33534 | 2025-08-06 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c5498119-2b0f-3736-b2ec-2cbdbb0c0846 | -12.55543 | -44.73521 | 2025-08-06 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1443a19-a6f1-3511-ac94-4ead29a5419e | -11.73516 | -47.53333 | 2025-08-06 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4c2db6de-0947-36e2-bdb1-726e6283eb6b | -8.37 | -45.80027 | 2025-08-06 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6858c9e-bce1-3b6a-b10c-ccafb30fa4a8 | -7.30886 | -44.66721 | 2025-08-06 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4b69709-191e-309d-b232-9ad3decc47b9 | -6.13197 | -44.43937 | 2025-08-06 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e47e561d-90da-3148-a06a-cc193694e0bd | -7.58183 | -45.30729 | 2025-08-06 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b441223-f2b5-3172-8215-8592fd2323d2 | -8.62346 | -50.01487 | 2025-08-06 04:19:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c9edf337-bf6c-391f-8ef5-726bb88e147d | -10.43792 | -44.36444 | 2025-08-06 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a1906ec4-d8e5-34c5-adbb-b857fa9cd320 | -6.48786 | -45.92339 | 2025-08-06 04:19:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c574a305-bdce-319f-a1b2-bd65854268cb | -9.47446 | -49.81777 | 2025-08-06 04:19:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 18e32ca1-2115-35fe-8e91-68c189b22840 | -12.40567 | -44.70149 | 2025-08-06 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9e19b6c-a663-305f-9c48-27225adcdf56 | -7.11072 | -44.0218 | 2025-08-06 04:19:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aebb3939-942f-34eb-a771-77bea5854148 | -6.41632 | -53.36328 | 2025-08-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 29feaa0d-25bf-33a9-a1c3-0d9861a82389 | -6.41721 | -44.02834 | 2025-08-06 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a910dd98-def3-3ff2-9850-ed6737edcd87 | -8.51226 | -44.74707 | 2025-08-06 04:19:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a618ce4-e39e-36b3-a795-57ba4dd5191e | -6.41475 | -53.37247 | 2025-08-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc073328-cf2b-3914-bac6-18c5aad8f7c8 | -7.57822 | -44.89821 | 2025-08-06 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c0de1be8-0286-3e99-8bd4-602a403bb9e1 | -10.96836 | -47.39651 | 2025-08-06 04:19:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59931505-4c3d-36f4-9fe7-b1973cb8ec5e | -10.43346 | -44.37111 | 2025-08-06 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4e609443-9e55-30c0-a302-c20d60c06649 | -7.08561 | -44.35834 | 2025-08-06 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6823a73e-d27d-360e-9956-b6e6c277e051 | -7.18714 | -45.48209 | 2025-08-06 04:19:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README14.md)
