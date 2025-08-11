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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4722c79f-3f38-3dfe-b4cc-1b825e818fd0 | -14.82857 | -51.22625 | 2025-08-11 04:06:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf690269-9ba1-3680-a0ae-075c572d0a87 | -15.42427 | -53.91997 | 2025-08-11 04:06:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 33a6740c-01de-33fa-bc96-eed29b923f91 | -16.39194 | -42.59207 | 2025-08-11 04:06:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a765c61-9acf-3318-86a1-2c37c64c4c98 | -16.53267 | -47.57905 | 2025-08-11 04:06:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e746ed6-06f4-3005-a883-9424c96f9ae9 | -15.44401 | -53.93726 | 2025-08-11 04:06:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| afe1544e-5a80-3953-8e13-0c55472c1797 | -15.09514 | -46.54058 | 2025-08-11 04:06:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 083a247a-f4e3-3a92-b3af-25147a05052f | -15.45314 | -53.93698 | 2025-08-11 04:06:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a4ee29dc-2627-38a0-b07c-3fdbb5fb734c | -16.04446 | -43.8279 | 2025-08-11 04:06:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b2dafaad-8b25-32e2-b743-400636455643 | -15.41294 | -53.9122 | 2025-08-11 04:06:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15610d03-8877-3a3f-8056-3868e7b3062b | -15.45206 | -53.94207 | 2025-08-11 04:06:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 911f98e4-eaea-3b15-b61a-10670219d89d | -15.92912 | -42.22234 | 2025-08-11 04:06:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| defd4ed9-74f5-3e67-8a2e-490faf8dfd0c | -15.4418 | -53.92919 | 2025-08-11 04:06:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 82064549-3749-3573-8fef-c048f999a673 | -15.10404 | -46.53619 | 2025-08-11 04:06:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac2d999e-d086-3e27-b4a1-86541da9a584 | -15.57512 | -43.41125 | 2025-08-11 04:06:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 88ebfec6-2145-3e39-b291-2bc272d07108 | -15.44291 | -53.94226 | 2025-08-11 04:06:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 29080139-e89b-31cd-b2d0-8725573c1242 | -16.6904 | -47.63192 | 2025-08-11 04:06:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8aa36757-decc-3231-afd8-d15f72e6cd7a | -16.68971 | -47.63571 | 2025-08-11 04:06:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38c57c4d-791f-35f0-a67f-66ad5a1636f0 | -16.39527 | -42.59264 | 2025-08-11 04:06:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d81343b3-15ff-3297-87a9-e9a6c3d6a315 | -16.408 | -42.59063 | 2025-08-11 04:06:00 | NPP-375D | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 00236690-849f-3308-b4cc-972385c7a910 | -15.4356 | -53.9278 | 2025-08-11 04:06:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 1791019f-2901-3e0c-be0c-fca21b4b1d78 | -22.51112 | -46.79023 | 2025-08-11 04:08:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a458a952-dba9-365d-b8b4-3ff610b479eb | -21.63512 | -49.8418 | 2025-08-11 04:08:00 | NPP-375D | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f9513ddd-a798-3872-b09b-43a91d9cad53 | -22.06409 | -46.81954 | 2025-08-11 04:08:00 | NPP-375D | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 59d986c7-8029-366a-b792-23790458bed2 | -24.86996 | -52.06829 | 2025-08-11 04:08:00 | NPP-375D | PALMITAL | PARANÁ | Brasil | 4117800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 42ab5979-65bf-39b0-8c06-39453e160f8f | -21.78138 | -44.68196 | 2025-08-11 04:08:00 | NPP-375D | AIURUOCA | MINAS GERAIS | Brasil | 3101201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 92c52659-faaa-3ae0-a1e3-33706cf83f3e | -24.86817 | -52.06655 | 2025-08-11 04:08:00 | NPP-375D | PALMITAL | PARANÁ | Brasil | 4117800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 33728f4d-74dc-3005-84ea-54941d1f3419 | -22.51393 | -46.79535 | 2025-08-11 04:08:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0ef0dcf5-1223-36a6-8411-d45ccce1a3d9 | -24.73576 | -50.91827 | 2025-08-11 04:08:00 | NPP-375D | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 284fe514-463e-39a1-958b-ec3711e12f30 | -22.5147 | -46.79097 | 2025-08-11 04:08:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4de27a4b-91d2-3984-9ec1-364b4f48ab08 | -22.70252 | -47.35658 | 2025-08-11 04:08:00 | NPP-375D | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30c86c79-9037-35a6-99c3-492eec7a1638 | -22.87063 | -46.6199 | 2025-08-11 04:08:00 | NPP-375D | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 400c8ea4-45da-37a3-8f0a-22645e5a34b6 | -21.4754 | -44.6931 | 2025-08-11 04:08:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| cb7e9f9c-a0e1-3465-b641-59a34cc4eb0f | -23.64262 | -51.62646 | 2025-08-11 04:08:00 | NPP-375D | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 20.0 |
| 333ea12d-9751-3917-b486-29a5d27c66c3 | -24.74009 | -50.91923 | 2025-08-11 04:08:00 | NPP-375D | RESERVA | PARANÁ | Brasil | 4121703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1d2629d8-ea05-3d16-baf7-0ad87cb17f39 | -27.30878 | -48.68502 | 2025-08-11 04:08:00 | NPP-375D | TIJUCAS | SANTA CATARINA | Brasil | 4218004 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 55353f28-c663-3b34-8d10-31e98e35d293 | -21.63355 | -49.84367 | 2025-08-11 04:08:00 | NPP-375D | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8b3398db-343a-3c5c-9354-c9562d432f7a | -21.77802 | -44.68132 | 2025-08-11 04:08:00 | NPP-375D | AIURUOCA | MINAS GERAIS | Brasil | 3101201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d3b3aecc-1008-3d44-bde4-02cd3571af90 | -5.4824 | -44.3969 | 2025-08-11 04:10:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 169.9 |
| 104ebeb9-71bb-36b8-ba3e-f0d9d74b585f | -15.4216 | -53.9073 | 2025-08-11 04:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 223dafdd-02dc-39aa-9b22-25242f955c0b | -5.4825 | -44.374 | 2025-08-11 04:10:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 50e71356-488d-3824-b57e-36c65e5729e3 | -15.4212 | -53.9283 | 2025-08-11 04:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 6b4892db-292f-3090-9cd4-b0c224ff422d | -7.0799 | -59.1964 | 2025-08-11 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| e769f4ff-e6ff-3656-809e-677c32365a49 | -7.0614 | -59.1972 | 2025-08-11 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| b82a83b2-59fb-3978-afa2-f693a9173fed | -15.4403 | -53.9468 | 2025-08-11 04:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 39.4 |
| e22c425a-d5d9-3ce0-848f-97efe74e67b4 | -15.4407 | -53.9258 | 2025-08-11 04:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 194.3 |
| ab5d5f07-3e62-3ef9-9ff5-fd8d65343ae3 | -15.441 | -53.9048 | 2025-08-11 04:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| ef8dd750-556d-33f3-98eb-eecabe2251af | -6.5856 | -44.564 | 2025-08-11 04:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 129bb5df-3539-3ede-ab0b-0276fd1d6759 | -29.16426 | -51.96139 | 2025-08-11 04:10:00 | NPP-375D | ENCANTADO | RIO GRANDE DO SUL | Brasil | 4306809 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b1d38fbe-1294-371a-8607-9a16bfec3073 | -29.1626 | -51.96349 | 2025-08-11 04:10:00 | NPP-375D | ENCANTADO | RIO GRANDE DO SUL | Brasil | 4306809 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4865c3e7-d41e-375d-a52b-176d8335e203 | -15.4407 | -53.9258 | 2025-08-11 04:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 3f1a1313-4a55-3b20-9463-85d8c94f2e88 | -8.5604 | -54.6973 | 2025-08-11 04:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| d49c4dda-dfdb-35f2-9dfc-0a0b3209a628 | -7.0614 | -59.1972 | 2025-08-11 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 69237880-ce73-360d-9623-bfc883661770 | -15.441 | -53.9048 | 2025-08-11 04:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 57.8 |
| a403fb38-c763-33ec-bf02-7e4f4f7d709b | -15.4216 | -53.9073 | 2025-08-11 04:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| bcb3aafb-92eb-3bef-8602-ddad5985568c | -5.5011 | -44.3956 | 2025-08-11 04:20:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 8e29c887-92fb-33ed-bdf9-73364e5c94ad | -5.4825 | -44.374 | 2025-08-11 04:20:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 73.2 |
| a21531df-33f9-3d86-9081-2577c771e2e2 | -5.4824 | -44.3969 | 2025-08-11 04:20:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 99.6 |
| e46cf5ce-8e80-302a-a079-282c27240fb3 | -7.0799 | -59.1964 | 2025-08-11 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 3c0c2fe7-e94d-317a-ae4f-11fcddefaa3a | -6.5856 | -44.564 | 2025-08-11 04:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| f93718a0-cfce-39c0-b6bf-20373eecba0e | -15.4212 | -53.9283 | 2025-08-11 04:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 2d4fbc0f-93e2-3401-96e1-654efcdc5b32 | -5.07145 | -37.71741 | 2025-08-11 04:23:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fb7730fb-8281-367d-9cb9-12bd84a6c313 | -2.3342 | -48.62008 | 2025-08-11 04:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11e4ba17-975c-3fcc-b415-33e501142a18 | -3.22522 | -49.34109 | 2025-08-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e04f46bc-0a7a-3a83-9560-3f49fb5e0812 | -2.9588 | -49.06619 | 2025-08-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ad6bf833-0b6c-3284-87cb-5da94cb50b24 | -2.81509 | -48.65377 | 2025-08-11 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| acc991bd-4d21-3c79-be35-128dced6f1b5 | -3.42624 | -49.04691 | 2025-08-11 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 72f3c487-6108-3e09-bef9-ff0bd9ee6b24 | -3.42692 | -49.04268 | 2025-08-11 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| daf578d6-0ab8-338e-8d8f-68f0ea6dcb12 | -3.07937 | -48.85361 | 2025-08-11 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d16ec2ef-d5b9-375d-b961-449a797c91a3 | -3.2245 | -49.34549 | 2025-08-11 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c7b64e7f-3254-3e40-bc65-1de79d5abce8 | -2.58706 | -51.92453 | 2025-08-11 04:23:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74d2ca0a-8d3c-36a2-93cd-24d527b28c98 | -2.67378 | -52.16718 | 2025-08-11 04:23:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e30a7c5a-118b-3d9e-9803-b21d33078d8c | -7.35447 | -45.27559 | 2025-08-11 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 76e051ef-9c9a-3267-8989-b241031dff0f | -7.08142 | -59.20329 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5fc6958b-fc4a-33ec-bd63-8c9b11bea633 | -8.13367 | -47.43203 | 2025-08-11 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be54d0b9-b9f0-3e6f-91f1-8af48c4e760d | -7.61522 | -45.19439 | 2025-08-11 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 853cbb92-6736-305b-a62e-f62476ef1dbe | -7.27091 | -44.16979 | 2025-08-11 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 98bb5a58-6374-3586-af84-45a46a5ff1af | -8.55849 | -54.69666 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 270a45ed-a2e5-3ecc-8e9a-d43f816efd7a | -8.57004 | -54.68774 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 504d1ea0-3b7b-3a1b-a504-810a97f328ef | -8.96288 | -46.61251 | 2025-08-11 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e69d6b60-2d93-3b31-987b-122d64e199d2 | -7.04957 | -59.19059 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3dfed969-fc46-32da-8f44-a3ad4b5d64ee | -7.3315 | -45.26835 | 2025-08-11 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 231a7c2a-3aad-3de0-baa8-5b3690c27250 | -6.28805 | -43.70992 | 2025-08-11 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69245d78-abcb-3a22-a9d3-68c0d7d615e6 | -6.95997 | -44.21489 | 2025-08-11 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 41b7dcc2-ddb3-3146-a5b9-db9bbec72ed3 | -7.0485 | -59.19634 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40596481-9011-36d1-a244-0e2b83fd4188 | -7.21686 | -46.24696 | 2025-08-11 04:25:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| adc81e8e-26a8-3aff-8e91-d589f676ace8 | -6.30983 | -42.35337 | 2025-08-11 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 60e11f3c-148f-3d9d-b1fc-a7b2c4d437b3 | -4.06694 | -47.96961 | 2025-08-11 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5654df0a-3f0f-3123-8c0b-cad6621d5ea6 | -7.60681 | -45.20415 | 2025-08-11 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| de5b48b0-389a-3811-bc97-753b41f81eb8 | -7.12921 | -44.21316 | 2025-08-11 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52ffba9e-4c6e-3d5a-871e-0cce5f56df5e | -7.1704 | -42.93589 | 2025-08-11 04:25:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8babaed1-edb2-346c-8055-d12ac0cc7669 | -4.21183 | -48.16272 | 2025-08-11 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ce9bc80-1189-36ff-941a-484937e525fe | -3.51041 | -50.74282 | 2025-08-11 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| da99cd3c-8cca-30e0-a71e-54eeb1ea7fb6 | -7.21795 | -46.24002 | 2025-08-11 04:25:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a9d1725-43a5-3ef8-b419-a4b69f18d31a | -7.0825 | -59.19746 | 2025-08-11 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6dcb27db-a4d7-39cb-abbf-f5f7f59c03d5 | -8.56723 | -54.70379 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d27a830c-039e-379d-af91-e0b16bfd49de | -7.16695 | -44.28078 | 2025-08-11 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4b6454b1-b2ca-3b91-bca8-7ff1802c2253 | -6.97825 | -43.09715 | 2025-08-11 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51db5ba2-1d7c-306f-a62f-a23e3155d465 | -9.21299 | -48.53773 | 2025-08-11 04:25:00 | NOAA-20 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48526417-14f8-3db7-b30c-caad61650e75 | -9.15497 | -44.42228 | 2025-08-11 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e538236-c70a-3f37-bdf4-930de745f2b4 | -8.56436 | -54.68346 | 2025-08-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README15.md)
