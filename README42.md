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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40dc3a6a-ef3c-3a79-8c7f-cc863895bc6a | -10.7968 | -50.93168 | 2026-08-25 04:27:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| daadba85-ddf6-3bc0-8c01-b02ea38c6549 | -11.43865 | -44.54512 | 2026-08-25 04:27:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1292c8d3-3bce-3f7f-b63e-e41625fd2a9c | -15.47747 | -53.98548 | 2026-08-25 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc99e5e5-09da-3c13-8e63-b9a5a3f80d1a | -21.16319 | -46.78152 | 2026-08-25 04:29:00 | NOAA-20 | GUARANÉSIA | MINAS GERAIS | Brasil | 3128303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3e4b05e1-3037-3cf3-9f20-3ecc248656ae | -21.06539 | -48.46115 | 2026-08-25 04:29:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f43eb6cc-514d-3229-9667-e2d163e4ade7 | -20.98376 | -47.37089 | 2026-08-25 04:29:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 00c5d6dd-09ff-37fc-ac46-381c1e38998d | -19.34281 | -48.94172 | 2026-08-25 04:29:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6aa76763-eaa2-352a-9c03-18e2e8806bb0 | -21.27195 | -49.16166 | 2026-08-25 04:29:00 | NOAA-20 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ecd137e8-d0c1-3ed5-90fa-95ef64dae8fe | -21.13877 | -50.23784 | 2026-08-25 04:29:00 | NOAA-20 | BREJO ALEGRE | SÃO PAULO | Brasil | 3507753 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e5181f45-61e9-3df5-87d1-319ee0bbabab | -22.15696 | -46.65209 | 2026-08-25 04:29:00 | NOAA-20 | SANTO ANTÔNIO DO JARDIM | SÃO PAULO | Brasil | 3548104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d416a9dc-b3cf-30a1-a485-48296b1fd2d4 | -21.50885 | -45.75481 | 2026-08-25 04:29:00 | NOAA-20 | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| de3b9f98-caf0-3072-be59-ea2d5ef39f21 | -19.67865 | -47.17179 | 2026-08-25 04:29:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7f4c219-fd52-3b18-93eb-fe734703cd05 | -20.98491 | -47.36337 | 2026-08-25 04:29:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9488ac16-627a-32d7-9d55-7c1c3a51a7ea | -20.98434 | -47.36713 | 2026-08-25 04:29:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fa2c855c-1879-3aa2-a13a-89ee73eb5e65 | -19.8768 | -46.21317 | 2026-08-25 04:29:00 | NOAA-20 | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7821ad64-1d82-3921-a673-47a631d98701 | -18.90526 | -47.47403 | 2026-08-25 04:29:00 | NOAA-20 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09510978-1ef7-361e-8b9d-141f6da2c821 | -23.31255 | -47.53363 | 2026-08-25 04:29:00 | NOAA-20 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e1808347-647c-3a18-b793-51c54d7d32d9 | -18.5539 | -48.29549 | 2026-08-25 04:29:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb2e61fa-50de-3ad5-9f14-5d5b4279df9e | -21.13811 | -50.24179 | 2026-08-25 04:29:00 | NOAA-20 | BREJO ALEGRE | SÃO PAULO | Brasil | 3507753 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1fa9eef7-9e56-3f92-bdcd-763121b8fa8b | -18.55743 | -48.27363 | 2026-08-25 04:29:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6569bdca-0507-3457-8be0-4ed07590c405 | -20.95504 | -47.46954 | 2026-08-25 04:29:00 | NOAA-20 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a9ef4793-08ce-3c62-863b-a7baf88ef9b7 | -20.44889 | -46.57673 | 2026-08-25 04:29:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6cfc17a1-a500-375a-bea4-03cc36d0cf37 | -21.33766 | -45.3358 | 2026-08-25 04:29:00 | NOAA-20 | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4ed725f3-a635-32d5-973a-d8a2bc32dcd5 | -23.03841 | -47.40827 | 2026-08-25 04:29:00 | NOAA-20 | ELIAS FAUSTO | SÃO PAULO | Brasil | 3514908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1721f53c-5cb7-307e-abce-e9bdf37e8c51 | -18.96361 | -48.17962 | 2026-08-25 04:29:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 47a21df5-c805-36d9-b428-4309099ee0e9 | -19.68259 | -48.05703 | 2026-08-25 04:29:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 04ba4874-8213-3be2-9edb-559020abce32 | -19.67922 | -47.16809 | 2026-08-25 04:29:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6537eac8-6b31-3fb7-9363-f415027099d5 | -21.24513 | -44.98587 | 2026-08-25 04:29:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2e295218-14c1-3f97-b348-0a501e0cf8c6 | -19.6859 | -48.05761 | 2026-08-25 04:29:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95d341de-4a03-3008-80a4-00f93d722cb8 | -18.90583 | -47.47039 | 2026-08-25 04:29:00 | NOAA-20 | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ddfb12d8-5b6a-3b03-a6e9-3fe77f916432 | -22.44983 | -47.40978 | 2026-08-25 04:29:00 | NOAA-20 | CORDEIRÓPOLIS | SÃO PAULO | Brasil | 3512407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 819e00d6-be4c-3edb-a589-2698d365caa0 | -21.13537 | -50.23718 | 2026-08-25 04:29:00 | NOAA-20 | BREJO ALEGRE | SÃO PAULO | Brasil | 3507753 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5b7b2f25-06dc-31a2-808c-c7c72dfed040 | -18.56075 | -48.27422 | 2026-08-25 04:29:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11deaa96-b171-3d99-9803-9f46a3e9078c | -21.50825 | -45.75901 | 2026-08-25 04:29:00 | NOAA-20 | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| c90bf813-ce3e-3cfe-8225-0a60e553083b | -20.4636 | -46.57109 | 2026-08-25 04:29:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6e1a483-88c4-32e3-9736-1d4b76fac239 | -20.98157 | -47.3628 | 2026-08-25 04:29:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7e24760-38fa-312a-9aa4-97e967dc35ff | -20.46418 | -46.56722 | 2026-08-25 04:29:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb815921-eed4-3426-b799-9eec4d254f8a | -6.641 | -58.4987 | 2026-08-25 04:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| a860493f-1976-3923-a200-ac654315f06c | -10.7799 | -50.9325 | 2026-08-25 04:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 99.5 |
| ee2fc917-db14-3eda-94d9-ab61757fd3e9 | -11.1447 | -44.4632 | 2026-08-25 04:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 201.7 |
| a51297bd-0da1-3d43-aa38-9cc7dd1cd6be | -10.7988 | -50.9305 | 2026-08-25 04:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 954e1f8a-d122-3742-a33e-58df310652ec | -11.1443 | -44.4865 | 2026-08-25 04:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 132.0 |
| 0fb529db-3b1b-353f-bb2d-f1d18f225287 | -10.3727 | -45.0537 | 2026-08-25 04:30:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 5c29bde0-9149-3def-a032-fdcc918ad50e | -10.7801 | -50.9113 | 2026-08-25 04:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 007de923-8a14-3dd6-8ef8-27df16732a62 | -7.0057 | -59.2575 | 2026-08-25 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 169.1 |
| bc72e880-836b-3ef7-b4d0-7056e14825a7 | -11.1256 | -44.4659 | 2026-08-25 04:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 7d826a4b-abb4-3349-8536-e5940fd7409c | -6.9872 | -59.2582 | 2026-08-25 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 152.8 |
| 55c9e67f-4461-33c5-9f2a-0d58db86f0b9 | -3.5407 | -48.1673 | 2026-08-25 04:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| cc992c58-6f9b-3b8c-acc5-4fdbf5a588fd | -7.2903 | -45.3456 | 2026-08-25 04:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 6e303319-59c7-3a97-a6b9-6eac48b11046 | -3.5222 | -48.168 | 2026-08-25 04:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 465bd52e-54f7-3400-bbd0-703cba52c251 | -7.0058 | -59.2382 | 2026-08-25 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 218.9 |
| 0d949e9c-371e-35f7-a3c5-22754c06ef7b | -7.2901 | -45.3683 | 2026-08-25 04:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 68.3 |
| c15d33c5-f782-39d7-9fa8-6362733ebab6 | -3.5221 | -48.1896 | 2026-08-25 04:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| acb1be0a-3475-3d13-8a84-edf5ef79fb7f | -10.7991 | -50.9093 | 2026-08-25 04:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 39330bdf-8385-3c84-98e5-b1e61280db4b | -6.9873 | -59.2389 | 2026-08-25 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 211.5 |
| 5468de3f-57ac-3919-9dd6-51000bd2aaf5 | -6.6226 | -58.4995 | 2026-08-25 04:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 988efba2-e3b4-35ba-b592-5b7691187b1d | -3.5406 | -48.1889 | 2026-08-25 04:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 2a28eea1-2aa2-36d4-96b8-bfdfc36e59b9 | -7.0058 | -59.2382 | 2026-08-25 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 231.8 |
| 69a5edc1-1f02-3b91-abb1-251bfeca9278 | -10.7988 | -50.9305 | 2026-08-25 04:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 2b6df347-b91b-3df8-b815-a8ac691623af | -10.9297 | -51.0442 | 2026-08-25 04:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 9e6fd494-5d17-3d57-80f3-9c7005a1e8d7 | -3.5406 | -48.1889 | 2026-08-25 04:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| ec0c196a-3d5b-3aed-aa7a-7b4aa7600e8b | -10.7799 | -50.9325 | 2026-08-25 04:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 108.6 |
| fde96660-f1a6-3adb-86dd-49b82e774c66 | -10.3727 | -45.0537 | 2026-08-25 04:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 0a9fccbb-945e-3560-8a9f-11793e592767 | -7.0057 | -59.2575 | 2026-08-25 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 151.4 |
| efb84f16-c017-3709-a834-8ab383f231f2 | -11.1447 | -44.4632 | 2026-08-25 04:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 163.1 |
| 0b444ba0-02bc-3e19-b89f-1617096aedd0 | -10.9104 | -51.0674 | 2026-08-25 04:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| e76c29ed-b9f3-3de2-b1db-5f3b5d4992a8 | -3.5222 | -48.168 | 2026-08-25 04:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 4d0be254-4735-3adc-bc8f-d0c62758215f | -14.3561 | -52.8872 | 2026-08-25 04:40:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 72.8 |
| f4beb331-864f-39d9-833f-2dfb6fbc6e6c | -6.6226 | -58.4995 | 2026-08-25 04:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 768ab67a-1b54-3056-b2ec-2aae508828f2 | -11.1443 | -44.4865 | 2026-08-25 04:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| ed81e45c-6741-38d3-899e-21a8e4b52952 | -6.9873 | -59.2389 | 2026-08-25 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 264.0 |
| 37d9930c-163e-3994-9216-aa1286b5e2fc | -3.5407 | -48.1673 | 2026-08-25 04:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 181.7 |
| 631b077e-4b7d-3899-a5e0-7f7d6651bfc3 | -6.9872 | -59.2582 | 2026-08-25 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 143.4 |
| b5c6337e-14ee-3675-9c7e-eb53236c82fa | -7.2903 | -45.3456 | 2026-08-25 04:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 4ff628a8-1d05-34e5-8f6a-61144e30681a | -10.9294 | -51.0654 | 2026-08-25 04:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 128.1 |
| fda557ac-3568-3329-944b-225e444ae713 | -7.2901 | -45.3683 | 2026-08-25 04:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 047c0b07-9851-3d0f-a8f1-d926f1b56678 | -11.1256 | -44.4659 | 2026-08-25 04:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 5826ac6e-b5cf-3417-a168-797bc6ee66a0 | -10.7801 | -50.9113 | 2026-08-25 04:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 15709c0e-eb3a-3b62-a7dc-d386749f059f | -6.641 | -58.4987 | 2026-08-25 04:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 99650eca-c209-3a73-a50e-6a611e115264 | -7.2194 | -60.6125 | 2026-08-25 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| c4153da3-f7ba-387c-84f0-8c0fd9ebee7c | -7.2903 | -45.3456 | 2026-08-25 04:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| 3c474075-eae3-30d9-8c9c-7258de48a2c5 | -3.5406 | -48.1889 | 2026-08-25 04:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 111.5 |
| b7c97025-498d-3a65-b54b-1c02d148d3e6 | -6.9873 | -59.2389 | 2026-08-25 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 135.5 |
| bd33a8c8-8735-3051-b70b-99a6e8eb53a0 | -6.641 | -58.4987 | 2026-08-25 04:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 08a57833-557b-3141-8e17-40888fd59d93 | -6.6226 | -58.4995 | 2026-08-25 04:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 6896c63d-e680-38bd-b9c7-56a29357ebe9 | -7.0057 | -59.2575 | 2026-08-25 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 163.0 |
| 2e9282ff-f11f-3fda-a549-c557ec7f397f | -10.7799 | -50.9325 | 2026-08-25 04:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 57.8 |
| e1ff8194-4e59-33e1-82a6-bafd90b6a129 | -11.1443 | -44.4865 | 2026-08-25 04:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 0cb0b131-bc88-3824-8e10-2ab0ebaa52a5 | -7.0058 | -59.2382 | 2026-08-25 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 197.8 |
| 4d36491f-a712-3a98-8083-87ff6fa26619 | -6.9872 | -59.2582 | 2026-08-25 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 5bd9751c-fba3-39b3-a8e8-538e0a2ef156 | -3.5222 | -48.168 | 2026-08-25 04:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| f28561e7-8d53-30fd-8500-8160f395fc4c | -11.1256 | -44.4659 | 2026-08-25 04:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 56.5 |
| bb917235-02e3-3089-b3e9-07b78b50e4e2 | -7.2901 | -45.3683 | 2026-08-25 04:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 57.2 |
| a87a8565-74bb-33d6-bfe1-41796636ceee | -11.1447 | -44.4632 | 2026-08-25 04:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 167.0 |
| dfaf947e-12ce-39fc-a09b-b2087f0816a7 | -3.5407 | -48.1673 | 2026-08-25 04:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 156.5 |
| 672c584f-1387-3033-afcd-118ef3e745b8 | -7.0057 | -59.2575 | 2026-08-25 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 136.3 |
| 5b74ab61-e5ca-36ad-9320-1d997febc2f0 | -7.0058 | -59.2382 | 2026-08-25 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 155.6 |
| d5e8d40b-3868-38b3-874a-ea1351c13bd9 | -3.5406 | -48.1889 | 2026-08-25 05:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 7eccef56-abda-3a92-8ec6-1d6c8a81fac8 | -7.2903 | -45.3456 | 2026-08-25 05:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| 531dd230-4447-3682-8fe7-2b52a0d9b876 | -6.9872 | -59.2582 | 2026-08-25 05:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.6 |


[Clique aqui para ver as próximas entradas](README43.md)
