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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aaf65062-e847-30a7-92a2-266e7dc8ef9a | -19.58466 | -40.79939 | 2025-07-20 03:51:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 09757ec7-5618-3512-acf9-2c2fc2d0f458 | -14.75613 | -48.25526 | 2025-07-20 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 44b99db4-356f-3743-aaf4-62c357fbfc5b | -16.05387 | -48.10872 | 2025-07-20 03:51:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ffc2a192-b17a-39b3-9228-34fa7945072d | -16.71079 | -49.35844 | 2025-07-20 03:51:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b6d3aef-cb2c-34c0-af6a-1ea689ced0b5 | -20.09897 | -44.077 | 2025-07-20 03:51:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 199e52ff-f6b7-3623-86ae-c810efde6276 | -19.22365 | -42.31459 | 2025-07-20 03:51:00 | NOAA-21 | NAQUE | MINAS GERAIS | Brasil | 3144359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8c3f1b4e-61af-30c5-9a96-f2effbf0ae0d | -19.40057 | -43.24498 | 2025-07-20 03:51:00 | NOAA-21 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 1296a74c-c6bb-377c-8b2f-a0819213736e | -14.7554 | -48.2589 | 2025-07-20 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7435b784-dc45-3a55-8724-22b526faca80 | -18.89755 | -43.34228 | 2025-07-20 03:51:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 98e5a6fd-ae12-3462-95b4-1f6157537b65 | -13.45356 | -48.0266 | 2025-07-20 03:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84ad83d6-14bf-3134-91f8-f4cd4021e942 | -21.50611 | -43.91985 | 2025-07-20 03:51:00 | NOAA-21 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5fded36d-bff8-3bd8-a04b-7aa271896bb2 | -14.78798 | -48.28847 | 2025-07-20 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 420102f3-ccdd-3ba9-8464-dd41977c97a8 | -17.77943 | -44.25325 | 2025-07-20 03:51:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fcdc41ce-19d3-34ee-883d-bb0ba029f9a2 | -16.05888 | -48.11023 | 2025-07-20 03:51:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 945d84de-0002-34c8-89b1-e55e5510be38 | -20.2297 | -43.75049 | 2025-07-20 03:51:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 58223b5d-606b-369f-9a51-c16f7920537a | -20.10065 | -44.07904 | 2025-07-20 03:51:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| eca3f8a1-af9c-33ba-95d3-eb77fc0802b8 | -19.22433 | -42.31058 | 2025-07-20 03:51:00 | NOAA-21 | NAQUE | MINAS GERAIS | Brasil | 3144359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a5bf65fb-d34d-3a52-9d3e-6a1a430b4887 | -19.70595 | -42.16997 | 2025-07-20 03:51:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 346ca857-2573-38e8-ace7-b17e201b5a1e | -19.34101 | -40.83209 | 2025-07-20 03:51:00 | NOAA-21 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d6d8d181-b193-3db1-a051-0b5201255e11 | -17.83851 | -44.35269 | 2025-07-20 03:51:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7656fc1-7cac-385d-b7cd-34ad9f7d1a49 | -17.77667 | -44.25048 | 2025-07-20 03:51:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f9433d4-25ff-33d9-90d4-c7f410ade497 | -18.4061 | -44.18582 | 2025-07-20 03:51:00 | NOAA-21 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b29243b6-d13a-312f-bda2-92c5cb0c2cd3 | -16.74904 | -49.33865 | 2025-07-20 03:51:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f2977df-4859-3d85-974f-4be6e7b04402 | -14.71105 | -48.23895 | 2025-07-20 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c73a7bc5-8950-3a49-a814-187c91936bf9 | -20.09998 | -43.90956 | 2025-07-20 03:51:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c421fe9d-73b5-3331-916b-73a43ed6e5b4 | -14.84579 | -49.02759 | 2025-07-20 03:51:00 | NOAA-21 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 75965784-5ebd-3d2d-95d4-f8de33ee2071 | -16.05658 | -48.10863 | 2025-07-20 03:51:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 17f724ac-1284-3901-8f7f-a6394883689a | -20.13066 | -44.8663 | 2025-07-20 03:51:00 | NOAA-21 | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d2c43500-005d-3f28-9c75-e93f9c12abe9 | -14.84659 | -49.02368 | 2025-07-20 03:51:00 | NOAA-21 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 72d85d0b-54bf-3272-adb6-8cc6724aedd2 | -14.48498 | -46.35484 | 2025-07-20 03:51:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 385c9522-b3c7-32a1-aa95-96e985169c25 | -13.45437 | -48.02258 | 2025-07-20 03:51:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79239a81-1b27-30cb-a48f-b499ee18ff86 | -17.77575 | -44.25546 | 2025-07-20 03:51:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e611ad2-5f20-34c2-bfa5-27f5d5db00ba | -19.73767 | -43.91256 | 2025-07-20 03:51:00 | NOAA-21 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e89453e-6c36-3055-938d-c1e59041d577 | -20.53738 | -42.49679 | 2025-07-20 03:51:00 | NOAA-21 | SERICITA | MINAS GERAIS | Brasil | 3166303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 13e24590-9777-35e1-a623-705f6f3c89f1 | -20.10369 | -43.91005 | 2025-07-20 03:51:00 | NOAA-21 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e102fda1-819d-3aed-a05b-3ac5d4888ac1 | -16.05449 | -48.10568 | 2025-07-20 03:51:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0d4f3b05-204b-3ae2-9e3b-dd43358bced4 | -19.90041 | -45.04153 | 2025-07-20 03:51:00 | NOAA-21 | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 282ce8c5-7b03-3ef3-beb0-41ece2e3b787 | -16.70533 | -49.35731 | 2025-07-20 03:51:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab996891-69aa-3c9b-b0fc-a44e8cc0c7de | -16.05597 | -48.1117 | 2025-07-20 03:51:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5db25267-af28-371f-95cc-e60d96942a53 | -14.7925 | -48.29344 | 2025-07-20 03:51:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0866b926-1dc8-3d17-bdc2-2ec3d6b1407e | -20.34532 | -42.79348 | 2025-07-20 03:51:00 | NOAA-21 | PONTE NOVA | MINAS GERAIS | Brasil | 3152105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 095648b8-3919-3c99-9d64-837beccb7408 | -14.48398 | -46.36009 | 2025-07-20 03:51:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d17d9231-2239-3dd7-892c-7e7c30256e20 | -16.08967 | -45.16962 | 2025-07-20 03:51:00 | NOAA-21 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f38ce5d-28ae-3a25-bd2a-74d9f23ef8c5 | -22.50512 | -44.59248 | 2025-07-20 03:53:00 | NOAA-21 | ITATIAIA | RIO DE JANEIRO | Brasil | 3302254 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 888572c2-91fe-39e9-9f68-d57fe98da6b6 | -22.84301 | -42.30169 | 2025-07-20 03:53:00 | NOAA-21 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 6fdab3f5-7009-3dd6-81af-2073b8a603fb | -23.32759 | -46.97073 | 2025-07-20 03:53:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f5194f98-94d0-3d42-af2c-1766d60d96b6 | -23.25084 | -47.11688 | 2025-07-20 03:53:00 | NOAA-21 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| aaf1ee5c-a7c8-346a-842a-09611a05aaeb | -21.07905 | -50.63199 | 2025-07-20 03:53:00 | NOAA-21 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| da049794-4851-3ba5-ad4a-4323f25e1584 | -22.688 | -47.71217 | 2025-07-20 03:53:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e5959e2e-4736-35cf-a859-92ae11c703ce | -22.24874 | -43.33532 | 2025-07-20 03:53:00 | NOAA-21 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d3ec7076-4113-34fe-bd3c-082c459e0b8f | -21.07988 | -50.62818 | 2025-07-20 03:53:00 | NOAA-21 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 44dfd712-93ab-34e7-aece-4ee9cfe38146 | -22.96367 | -43.59788 | 2025-07-20 03:53:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ff34c7bd-f63c-34bb-ae46-c036b480b094 | -23.25165 | -47.11282 | 2025-07-20 03:53:00 | NOAA-21 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e4292de6-cc9a-3643-a5bc-214d38175eae | -22.13182 | -43.19255 | 2025-07-20 03:53:00 | NOAA-21 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 88c9e2e1-05b8-337c-96c7-637241810667 | -23.34174 | -51.90567 | 2025-07-20 03:53:00 | NOAA-21 | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 92453603-d678-3d4f-befa-f1fa139d764d | -22.68778 | -47.71105 | 2025-07-20 03:53:00 | NOAA-21 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 342ff297-830c-33da-9447-9cc032ba4790 | -22.43521 | -48.99147 | 2025-07-20 03:53:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6be2ffc4-a7f6-3993-ae4b-172771a4db39 | -23.25582 | -47.11383 | 2025-07-20 03:53:00 | NOAA-21 | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 72fc61da-c22a-3874-adf4-b0902fcd6cbb | -21.0804 | -50.63035 | 2025-07-20 03:53:00 | NOAA-21 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 96935aca-6006-30a8-be3d-57016c8b3820 | -22.13531 | -43.19317 | 2025-07-20 03:53:00 | NOAA-21 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a8d8a7ea-bc49-3b93-94e2-b5c3ac475660 | -23.33617 | -51.90424 | 2025-07-20 03:53:00 | NOAA-21 | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| cff0971d-6ff3-3db9-9ff2-b285436be9f0 | -22.92837 | -43.19173 | 2025-07-20 03:53:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| ef1197ec-0624-3e9a-a8f1-ea090d843ef0 | -23.10081 | -48.97386 | 2025-07-20 03:53:00 | NOAA-21 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e4d05453-527c-3efe-b32b-07e4ed1cb72e | -22.52554 | -52.01516 | 2025-07-20 03:53:00 | NOAA-21 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 145cf10b-4099-3812-8d09-2765c4468f2d | -22.24802 | -43.3395 | 2025-07-20 03:53:00 | NOAA-21 | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6f2e1714-4045-3a7f-9fcf-43177945ef8d | -22.5969 | -44.88844 | 2025-07-20 03:53:00 | NOAA-21 | LAVRINHAS | SÃO PAULO | Brasil | 3526605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f697ce06-e23f-3368-bd85-5ea770cd2066 | -22.13879 | -43.19386 | 2025-07-20 03:53:00 | NOAA-21 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| b376619a-d40c-32d4-bbd8-2ccec613f93c | -22.83501 | -43.5643 | 2025-07-20 03:53:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 872d28f1-ce08-372d-9b34-32ec13b193e9 | -23.10168 | -50.10509 | 2025-07-20 03:53:00 | NOAA-21 | BARRA DO JACARÉ | PARANÁ | Brasil | 4102703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 907b026d-480c-398e-9e82-c4be13f6a0c0 | -23.69347 | -45.48241 | 2025-07-20 03:53:00 | NOAA-21 | CARAGUATATUBA | SÃO PAULO | Brasil | 3510500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b5a1896c-73e0-3f8f-8c1f-4a83c1650458 | -22.52507 | -52.01415 | 2025-07-20 03:53:00 | NOAA-21 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ccc7d87a-d18b-39dc-813f-516c9ddac494 | -22.43536 | -48.98854 | 2025-07-20 03:53:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3823c12a-97a4-3b66-99fe-17b7b523209f | -22.52091 | -52.00914 | 2025-07-20 03:53:00 | NOAA-21 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9f42603f-db93-3afd-a62b-4abf35d2cc6c | -21.63687 | -49.84364 | 2025-07-20 03:53:00 | NOAA-21 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d0b40546-5141-351d-8060-898a105721e9 | -22.52042 | -52.00813 | 2025-07-20 03:53:00 | NOAA-21 | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 52d73cec-f7ed-3460-8e7d-698e5eef06e8 | -22.13951 | -43.18968 | 2025-07-20 03:53:00 | NOAA-21 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e643e618-1d95-35d1-ba18-59b20705a87f | -22.7128 | -43.84602 | 2025-07-20 03:53:00 | NOAA-21 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 71930011-7b7f-3145-b923-e3f5ba0711ae | -10.6686 | -46.8077 | 2025-07-20 04:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 265.1 |
| 523ab74c-77c3-3ec3-b591-f5e5669bd4f4 | -9.5343 | -40.3282 | 2025-07-20 04:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 136.9 |
| 27e76c8c-3c57-3013-b06f-5f91f9eeb042 | -9.5534 | -40.3254 | 2025-07-20 04:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 145.6 |
| 8e1bf2de-ec2b-375e-8dbd-13ac930411b2 | -10.6499 | -46.7876 | 2025-07-20 04:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 11f98d70-2c64-3bc5-a7be-da8e2f44d1b1 | -10.6689 | -46.7853 | 2025-07-20 04:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 145.0 |
| da7aaf71-e653-38f1-a4a6-359424878513 | -10.6496 | -46.8101 | 2025-07-20 04:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 222.0 |
| 88b40ffe-d445-335e-a88a-8dc27aa09431 | -10.6686 | -46.8077 | 2025-07-20 04:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 3464786a-22e4-3ab1-a228-6f8d8b8ecfa0 | -10.6496 | -46.8101 | 2025-07-20 04:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| d0592ff4-0ec9-343a-bc77-dfccfb9fa887 | -9.5343 | -40.3282 | 2025-07-20 04:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 74.9 |
| 376459e9-ab80-332e-8433-4780b5535692 | -21.0789 | -50.6188 | 2025-07-20 04:10:00 | GOES-19 | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 56.2 |
| 65e7a883-a174-3b25-92f1-089ba6583cb6 | -10.6689 | -46.7853 | 2025-07-20 04:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| fe701b70-7ae9-31b7-be33-eb96e453158a | -10.688 | -46.7829 | 2025-07-20 04:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 46.1 |
| a136fa46-b66f-33bd-9794-9b4904aa5662 | -3.98694 | -41.80061 | 2025-07-20 04:14:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 590ac9f8-ee92-37fb-8830-6d0db71792f4 | -3.58803 | -47.5211 | 2025-07-20 04:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f9b2a7a3-de85-311e-8631-115a47266d99 | -3.13914 | -47.01164 | 2025-07-20 04:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 79efef7c-4e34-3597-966f-632b14fbe3ff | -3.03843 | -47.86638 | 2025-07-20 04:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| bcaf956f-a4fc-38d6-a4e1-e0665803c895 | -3.12727 | -47.00975 | 2025-07-20 04:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65d300e1-c309-37c9-97b7-88ae50dfc541 | -2.98348 | -49.10766 | 2025-07-20 04:14:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31329bfc-e25c-3cdb-b748-5b3fc904c48c | -3.51838 | -47.21165 | 2025-07-20 04:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6467c591-dd73-382b-a53d-11883de629f5 | -3.94275 | -48.09436 | 2025-07-20 04:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00dfb0a2-a0aa-3cfd-b7ff-5569424e22ae | -3.79117 | -40.9999 | 2025-07-20 04:14:00 | NPP-375D | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 06d61b19-05de-347e-8972-062fbc4527e8 | -3.03906 | -47.86248 | 2025-07-20 04:14:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 49bc8d97-6eed-33e2-89f6-2c3217f532f9 | -3.58744 | -47.52469 | 2025-07-20 04:14:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |


[Clique aqui para ver as próximas entradas](README8.md)
