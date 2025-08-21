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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 316bfec3-f2fe-33c2-accb-4220efb9d29a | -23.67951 | -51.68071 | 2025-08-21 04:19:00 | NPP-375D | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| c5e1cd5e-d5bf-3f3f-990f-cf801c282378 | -23.67567 | -51.67989 | 2025-08-21 04:19:00 | NPP-375D | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 32196587-5b32-399d-adea-947a9d93aa7c | -20.31879 | -46.6013 | 2025-08-21 04:19:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e4537df-f1ae-33c2-9816-af48614dee1a | -23.31143 | -46.90122 | 2025-08-21 04:19:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 26a2659f-8cf7-3ca6-af68-4a022da96728 | -22.96102 | -47.10563 | 2025-08-21 04:19:00 | NPP-375D | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 80de17e8-3c31-31f9-b6f9-50a9f447ccb3 | -23.45922 | -46.97426 | 2025-08-21 04:19:00 | NPP-375D | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| add6ee79-ee3a-306c-b41d-cb6002eaeea3 | -21.38377 | -46.94168 | 2025-08-21 04:19:00 | NPP-375D | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 301b3a62-bdf4-3750-badc-8c7cfdac23f9 | -23.3081 | -46.9006 | 2025-08-21 04:19:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d677b745-443d-3c80-b6b0-8add6a3d8caf | -23.23211 | -47.52669 | 2025-08-21 04:19:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ec363b25-05c9-35ce-8e01-a7d61572be99 | -20.3182 | -46.60498 | 2025-08-21 04:19:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1bc7de33-a065-3fe3-97f9-87055da549c1 | -22.59985 | -43.68027 | 2025-08-21 04:19:00 | NPP-375D | PARACAMBI | RIO DE JANEIRO | Brasil | 3303609 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5e06f6f0-4096-3b9f-bba3-89a5c2df06e4 | -23.99694 | -48.61308 | 2025-08-21 04:19:00 | NPP-375D | TAQUARIVAÍ | SÃO PAULO | Brasil | 3553856 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 29f483fd-4037-360a-a46f-07cf8ed39a80 | -20.0589 | -45.39022 | 2025-08-21 04:19:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 25deca69-3f67-377b-84ca-64a64098bc8f | -20.24918 | -46.67248 | 2025-08-21 04:19:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36a4cae7-ab56-3a6a-bf7e-ef7b3f61d2c7 | -20.22142 | -41.78252 | 2025-08-21 04:19:00 | NPP-375D | DURANDÉ | MINAS GERAIS | Brasil | 3123528 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 5ed4b61a-e17c-3373-ab3b-967612a69f44 | -23.2231 | -46.4763 | 2025-08-21 04:19:00 | NPP-375D | BOM JESUS DOS PERDÕES | SÃO PAULO | Brasil | 3507100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ae64bfbd-0eb0-3700-941d-efcd0234798e | -20.32395 | -46.60547 | 2025-08-21 04:19:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 441cbace-6456-3d0b-8f8c-8f4fc6e2d460 | -23.10159 | -45.74398 | 2025-08-21 04:19:00 | NPP-375D | CAÇAPAVA | SÃO PAULO | Brasil | 3508504 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9bdc961a-1dfa-3b5b-9a9c-16bf5a89a49a | -19.29134 | -48.43422 | 2025-08-21 04:19:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93543971-7eb2-36b5-b60f-86c821ac7d5c | -20.25251 | -46.67308 | 2025-08-21 04:19:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 781aac44-1e2a-3ff0-be7f-dba52b8f9589 | -20.32062 | -46.60486 | 2025-08-21 04:19:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 091083ca-eaf6-33ce-bed7-5cd5f4d4c014 | -21.97877 | -42.87371 | 2025-08-21 04:19:00 | NPP-375D | SAPUCAIA | RIO DE JANEIRO | Brasil | 3305406 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 69c36086-40a0-3cd9-95eb-4d94093fca94 | -22.69728 | -43.72953 | 2025-08-21 04:19:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 62b107c0-3289-396c-9a5c-0ff006fd29f8 | -23.31472 | -46.90178 | 2025-08-21 04:19:00 | NPP-375D | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 96fd84c5-cee3-35b9-a6b7-b7324ef27240 | -25.42289 | -49.16516 | 2025-08-21 04:19:00 | NPP-375D | PINHAIS | PARANÁ | Brasil | 4119152 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| da3f2229-acfa-3013-bd5b-03cd2eac1394 | -20.50614 | -43.95136 | 2025-08-21 04:19:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| c35094b5-80fa-35b7-b794-bd5c8509d8aa | -23.36811 | -47.9989 | 2025-08-21 04:19:00 | NPP-375D | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f72ce26c-437a-341f-93dd-e139a91b8f8b | -20.24644 | -46.66818 | 2025-08-21 04:19:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bdd2b4ff-2e66-3ff7-8738-79e3d3bf350d | -20.24585 | -46.67188 | 2025-08-21 04:19:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33ea0135-016c-3a65-bbeb-b0d8c58b0506 | -20.50817 | -43.95287 | 2025-08-21 04:19:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b2d027d3-6e51-3f94-895d-a124f0bce101 | -23.45982 | -46.97049 | 2025-08-21 04:19:00 | NPP-375D | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b3f2ec7c-1f64-36a4-9d8d-11dac7db4596 | -19.29553 | -48.43081 | 2025-08-21 04:19:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cbed94b4-4e14-30c8-af10-79147b1a6251 | -20.32121 | -46.60118 | 2025-08-21 04:19:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9bc654ee-f076-348a-970e-e15a26bbda0c | -20.25584 | -46.67368 | 2025-08-21 04:19:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1860a3f2-54d1-33cc-b71b-aa2c0607d966 | -22.69669 | -43.73389 | 2025-08-21 04:19:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a7f6ef78-2e6c-3d0a-a2c6-3953572f727e | -23.40005 | -46.30793 | 2025-08-21 04:19:00 | NPP-375D | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 386c2317-75c2-3fca-8273-922024603219 | -20.08383 | -46.13615 | 2025-08-21 04:19:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 418d1550-0012-3518-84a9-11b0cc3fb552 | -21.38044 | -46.94107 | 2025-08-21 04:19:00 | NPP-375D | ARCEBURGO | MINAS GERAIS | Brasil | 3104106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 36a991d3-f44d-385e-b0d5-97742954578d | -22.55706 | -45.25972 | 2025-08-21 04:19:00 | NPP-375D | DELFIM MOREIRA | MINAS GERAIS | Brasil | 3121100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 351fa541-cfbe-380d-acc4-4a68ff84f500 | -22.94141 | -43.70529 | 2025-08-21 04:19:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f37bbeaa-d8d5-3acb-b407-82374b254f90 | -23.23483 | -47.5311 | 2025-08-21 04:19:00 | NPP-375D | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6a3d39ce-bb76-3e15-8746-a37322ebe715 | -20.74451 | -43.48432 | 2025-08-21 04:19:00 | NPP-375D | LAMIM | MINAS GERAIS | Brasil | 3137908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 24f7bc6b-8965-356e-a1f1-819df2e101e3 | -23.6799 | -51.68233 | 2025-08-21 04:19:00 | NPP-375D | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| b74c49da-469f-3bd3-97fc-55243df6690b | -22.69487 | -43.7356 | 2025-08-21 04:19:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f8960911-6521-3af2-849f-ed80f53ae484 | -22.78772 | -43.71221 | 2025-08-21 04:19:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bef2bcaa-bd6a-3a88-9c5b-c60994eff22f | -22.71285 | -45.05382 | 2025-08-21 04:19:00 | NPP-375D | CANAS | SÃO PAULO | Brasil | 3509957 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2e28f3da-35b3-3e0c-a0fd-4714319e8fe2 | -23.71337 | -47.37761 | 2025-08-21 04:19:00 | NPP-375D | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 40483d52-323d-34c1-85f0-d18da5427018 | -19.29972 | -46.03104 | 2025-08-21 04:19:00 | NPP-375D | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b8bc211c-419a-3183-ae65-dee331f161f4 | -14.47256 | -48.37489 | 2025-08-21 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a5f23cd5-1878-3322-b1b1-df63bf91e9c5 | -14.46886 | -48.3743 | 2025-08-21 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a60ef709-1cdc-304d-8b0a-9b8e47c8f150 | -13.56933 | -47.05043 | 2025-08-21 04:19:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 011a50c5-f6cf-3f8c-bc4d-516bd1485dc7 | -14.49407 | -45.96268 | 2025-08-21 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4db1b7f-7eb5-31fc-b937-518e607142f2 | -14.12309 | -45.37717 | 2025-08-21 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3411c54b-ce67-39cd-ba63-5b6512a653c4 | -13.54132 | -47.04563 | 2025-08-21 04:19:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68e5670a-1908-3fc5-9ee7-8dab2414b60e | -14.12528 | -45.3849 | 2025-08-21 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1a6a6287-bff0-30ff-b904-2143d1280ed0 | -14.85421 | -47.95624 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5844c5ea-f958-3880-9050-140bac3cb3b9 | -14.12589 | -45.39258 | 2025-08-21 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 412a545e-03b1-3506-80c1-76b39f50edd6 | -13.65083 | -45.71317 | 2025-08-21 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e5e0a4b2-b98c-399e-a54e-bd0115e98897 | -12.94545 | -46.23927 | 2025-08-21 04:19:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1eaccc55-3476-3d33-93ee-979030758b43 | -14.47622 | -48.37564 | 2025-08-21 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 43c35316-f99c-350b-8089-202596e9d855 | -13.86472 | -45.55202 | 2025-08-21 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e12ce0d0-bc6a-3c76-a0f6-dc4350a7ba76 | -14.12585 | -45.38132 | 2025-08-21 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ed0c251f-03f5-390d-b7f2-f6874feb5bd4 | -14.47699 | -48.37115 | 2025-08-21 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a05b521c-5e78-319a-90f6-bdf89e055fb0 | -13.51016 | -50.81758 | 2025-08-21 04:19:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88eafc9a-097a-32a8-b1fb-621c2b3cf87b | -13.03662 | -45.16368 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 524e45ab-61db-3018-b32d-3fcfa0c82c6c | -13.04556 | -46.83275 | 2025-08-21 04:19:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22b164b9-d01f-3519-93cc-d8aab35c626d | -13.041 | -45.17911 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c515cafa-d4b4-3d69-a829-1db3c72ab96c | -13.17408 | -46.90651 | 2025-08-21 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c436c993-fa63-3552-8b35-9affd233b6c4 | -13.55384 | -47.03552 | 2025-08-21 04:19:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e30f3215-d66e-371a-8a01-c3e423a1e15c | -13.48958 | -47.04983 | 2025-08-21 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b25a4c15-b6af-32af-b857-e5cbe0cb2a43 | -13.38242 | -46.2395 | 2025-08-21 04:19:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1bf9181d-b3fe-358e-bb50-83a86ba26efb | -13.04032 | -45.20468 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dbb304ff-fcc7-3820-a182-4dd418014004 | -14.85851 | -47.95268 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5e946b0a-e983-33a9-b6a3-0b75204f04ad | -13.3893 | -47.49379 | 2025-08-21 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b3a16f6-ba53-3d1e-80f7-719385da6c6f | -14.84851 | -47.94633 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85bed7cd-69a1-39fd-adcb-c00b19377d95 | -15.04849 | -42.46887 | 2025-08-21 04:19:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fc492b05-21ef-3dec-87d3-3bcfcbd06851 | -13.04089 | -45.20111 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d34a4047-17ba-3bce-9978-bc61c717ff4f | -13.14176 | -54.92089 | 2025-08-21 04:19:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3b33f046-456a-31bc-a8fe-13fc55e115d2 | -12.95284 | -46.23704 | 2025-08-21 04:19:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 199b0268-49ac-3181-90c3-6fc7b227340e | -13.63611 | -46.88685 | 2025-08-21 04:19:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ca037091-1616-3f59-94b3-94d1b0de4d77 | -12.21816 | -53.60547 | 2025-08-21 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 342b06b5-0b5d-3fd2-a3f5-bb1284fee88f | -13.14095 | -54.92498 | 2025-08-21 04:19:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 829d0b97-cf56-304f-9648-c86bbf231114 | -12.21881 | -53.60205 | 2025-08-21 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a62b5846-905f-381f-8ba1-e1c11f2597f5 | -13.03422 | -45.19998 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8888b816-e842-31e3-97d1-4752a9a892c0 | -12.88708 | -46.06475 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54547973-eb2c-3199-8194-da9af87d39ce | -12.9482 | -46.24383 | 2025-08-21 04:19:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dc9c8bab-198f-3839-8239-a2eed7597822 | -14.46515 | -48.37387 | 2025-08-21 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bf80171e-64ff-324c-8959-e86a6a64bdae | -12.95562 | -46.2415 | 2025-08-21 04:19:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f155d106-0873-3b33-a93c-b4a6fcf169ab | -14.49923 | -45.95226 | 2025-08-21 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6c49664-3d8e-3fbb-89d9-b29850fe4362 | -12.95345 | -46.23331 | 2025-08-21 04:19:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8ed4e799-6a45-375c-8d1a-be9ef1924ba2 | -14.85494 | -47.95194 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 4b600c3e-f594-3307-8e7c-4ef80c0301c7 | -13.32491 | -54.42408 | 2025-08-21 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 734c0958-d1f6-37f3-b2bc-598e99d28314 | -12.90724 | -46.09111 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 28bec05f-1467-3d3b-a054-1769123ef352 | -13.51145 | -50.81637 | 2025-08-21 04:19:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 596a9e72-9d97-3388-8cf5-37bd538ee068 | -13.47842 | -47.05195 | 2025-08-21 04:19:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8f877cc8-48ef-3881-b2e6-2b39ed14e301 | -13.38645 | -46.23632 | 2025-08-21 04:19:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bfff5fff-5135-3700-88c8-cb1db60f63c1 | -12.88368 | -46.0642 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8be75a63-b1c1-391b-a718-43b7c1609cf0 | -12.94793 | -46.22424 | 2025-08-21 04:19:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e9240e7c-b45f-3445-a67a-f915adafcb14 | -12.89886 | -46.07821 | 2025-08-21 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 30f152cd-0c62-361f-a731-75501cf9ebd0 | -14.85567 | -47.94767 | 2025-08-21 04:19:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |


[Clique aqui para ver as próximas entradas](README34.md)
