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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 78873eda-9866-3569-89cb-e2e5e60bcc5b | -9.56671 | -44.56744 | 2026-04-30 04:17:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b47919a-c06d-3ff1-84c0-d4eb5d4a56a0 | -13.69759 | -55.68984 | 2026-04-30 04:17:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5de62049-3576-3aae-a3ad-0754e9c93021 | -8.58153 | -39.42149 | 2026-04-30 04:17:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1768d5bb-f2db-3942-9925-378fc2bc49bf | -13.4102 | -43.75422 | 2026-04-30 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 16260fe5-8b51-320a-afa3-69e826a331db | -14.72021 | -47.50971 | 2026-04-30 04:17:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a31a957e-c51f-36dc-83fb-daa8f5008250 | -12.72211 | -47.72824 | 2026-04-30 04:17:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a7e99f69-1848-3332-9a84-9c2188469389 | -10.59334 | -44.33057 | 2026-04-30 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3dc66962-85e6-3e18-a6c1-5c58387ca568 | -9.56614 | -44.57097 | 2026-04-30 04:17:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1548769d-a9be-3f67-8c48-73adc247682f | -14.71902 | -47.5102 | 2026-04-30 04:17:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 11ed0340-83b2-36c3-a3ce-7400d42205e6 | -17.38476 | -42.62994 | 2026-04-30 04:17:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebb4bc70-5b4b-3c7c-8f83-acd682031c50 | -16.2275 | -45.49115 | 2026-04-30 04:17:00 | NOAA-20 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3b465b41-52ae-3545-813f-d22bae20b16b | -8.57772 | -39.42095 | 2026-04-30 04:17:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a7d33a5f-7c66-3242-8ba7-e303a33aca1d | -13.45404 | -44.03982 | 2026-04-30 04:17:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a7ee2de8-c19b-3b48-ac56-57dfdd8044bc | -13.49709 | -43.61299 | 2026-04-30 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1cf0fbff-935a-3a37-b443-f42c9d648df0 | -13.68304 | -44.29172 | 2026-04-30 04:17:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2b951e9-c91b-3cf4-ab8a-8bf649c62dc0 | -13.63207 | -44.44342 | 2026-04-30 04:17:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bfc6fa25-4e74-39e7-8359-4211b3417e9e | -13.49765 | -43.60937 | 2026-04-30 04:17:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbc5cc93-4426-338d-81da-6ebd6be7498a | -12.05491 | -57.42079 | 2026-04-30 04:17:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 25a62c43-c6ca-3516-8de9-6201177e7119 | -13.37749 | -54.26735 | 2026-04-30 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6cc5c2ad-8ee0-3906-a5da-ef0fc2eb766b | -12.37173 | -50.02792 | 2026-04-30 04:17:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c53906ab-328d-3a48-9f2f-0610afb49ffd | -14.05755 | -44.08952 | 2026-04-30 04:17:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 805644d3-b88c-3084-b158-baadbfd792c3 | -10.59279 | -44.33406 | 2026-04-30 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 594cbce6-c6a3-34dc-9889-c60c27da959c | -10.58948 | -44.33353 | 2026-04-30 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 4b4560f5-8623-337c-985e-2f07420cc15a | -17.38893 | -42.62627 | 2026-04-30 04:17:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c25d646d-468d-32bc-8e65-2a3c7240b1b2 | -16.22692 | -45.49474 | 2026-04-30 04:17:00 | NOAA-20 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8588ff7-84b3-31ad-8d4f-2143a9c4546f | -9.4633 | -46.12432 | 2026-04-30 04:17:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d73c1d63-2df1-34e3-b79b-f5b1211c5fa9 | -17.38536 | -42.62573 | 2026-04-30 04:17:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5947a11f-df7e-320d-a2ca-90cef2e1ee63 | -10.59003 | -44.33003 | 2026-04-30 04:17:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 4970134b-e6c0-3811-8eeb-531bc2b41eaa | -11.41708 | -39.52723 | 2026-04-30 04:17:00 | NOAA-20 | VALENTE | BAHIA | Brasil | 2933000 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f02f8703-c699-3e12-9d51-20473ee95ff8 | -10.82751 | -42.6987 | 2026-04-30 04:17:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 87da7b99-a584-3af6-9a2a-a925213b8295 | -6.44135 | -44.58303 | 2026-04-30 04:17:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8758f273-aee9-3933-969a-e72013fb80ef | -10.56718 | -46.48981 | 2026-04-30 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8764310a-86af-361e-9ebe-f9f9e15440c1 | -18.03379 | -53.01609 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93f26f4b-bb80-31a8-bb2b-655d7edfd7d7 | -17.99752 | -53.00808 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1cdec78b-3e0e-375d-b533-9aac720f38ba | -10.98709 | -45.09388 | 2026-04-30 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb56a322-a65d-30df-bd73-26d2cfbbca74 | -18.0493 | -53.00931 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8e7a4cdc-04d3-37da-a0cb-de96c3f963f3 | -12.72434 | -47.72986 | 2026-04-30 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 59d36a3a-1766-3b55-867b-8a08de95a01c | -13.20766 | -44.48676 | 2026-04-30 04:19:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 605f1013-047f-3d56-8cae-1389bff7175b | -18.08922 | -53.00073 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a02cbe12-4be1-31af-a9cf-fdec11107676 | -16.92099 | -48.22208 | 2026-04-30 04:19:00 | NOAA-20 | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c82a266e-7f54-364e-bcea-5cf09d91a385 | -18.03285 | -53.02092 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d14e51a-2cae-36a6-ac70-27f6823191f5 | -18.0302 | -53.0103 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f85f8e1f-ccda-315a-9514-d31d1a553813 | -18.03928 | -53.01221 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 3995373c-05e7-3cbb-a6f5-90647750d892 | -11.1301 | -45.13568 | 2026-04-30 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 4f14eb06-ce74-3208-aa8a-477db18058f8 | -17.50995 | -44.73341 | 2026-04-30 04:19:00 | NOAA-20 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60b1b8bb-7732-3a4c-a34a-6bda4f7d2f55 | -18.03474 | -53.01126 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| c68872a0-d082-3c47-b850-0049bb340804 | -18.03568 | -53.00644 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| f68438ec-5d43-3ee0-80ab-82188c39b377 | -20.01336 | -44.18104 | 2026-04-30 04:19:00 | NOAA-20 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 17103d84-77bf-3165-ab36-cfe98cce31a3 | -16.35994 | -52.42049 | 2026-04-30 04:19:00 | NOAA-20 | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b02c043-d663-328e-9a45-af0dedd0bc1c | -10.56653 | -46.49374 | 2026-04-30 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 806848b7-a5b9-3988-9e32-053c4195a2f5 | -12.34777 | -43.8222 | 2026-04-30 04:19:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 26186bcd-0be8-3757-9c8a-4fd063454caa | -18.08381 | -53.00175 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c6f0bd73-570d-3f7e-9527-6ccbc78b30bd | -13.2071 | -44.49029 | 2026-04-30 04:19:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5ba8160e-86da-3d20-b018-876ae0aac714 | -18.37045 | -39.9562 | 2026-04-30 04:19:00 | NOAA-20 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 37960852-cf30-3dbe-92a0-55611df56d61 | -11.55583 | -48.26041 | 2026-04-30 04:19:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8ca549b9-d3b6-3d7a-9279-d6c6aedfda04 | -18.05117 | -52.99968 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 42.7 |
| bd886187-5bd9-33af-a490-7280bc35430a | -17.98035 | -52.99926 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7465189-cc9b-3ce2-a8b0-e2982aa1cedf | -18.02567 | -53.00929 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7aae883a-4dbd-34f3-9bf2-2a91a148531e | -10.98825 | -45.08675 | 2026-04-30 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 90be1597-ae37-3104-a1e8-c69513630abb | -12.34833 | -43.81865 | 2026-04-30 04:19:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f240d007-2627-3e8b-9238-cb62804c911d | -11.40717 | -48.42733 | 2026-04-30 04:19:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 44ce6f80-e303-3e6f-bad4-12ce6f5ea73a | -19.7431 | -43.99321 | 2026-04-30 04:19:00 | NOAA-20 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6dd5d1a0-e5cc-396a-9348-5b8632de9db5 | -12.82599 | -43.77819 | 2026-04-30 04:19:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb248530-ac69-3dfe-bcb4-209ea946f0db | -18.05024 | -53.00449 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 9001d268-9021-3f34-b706-f716564cb901 | -11.95419 | -43.38398 | 2026-04-30 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3d142860-1690-37d7-af32-b898202c9779 | -16.32345 | -50.04515 | 2026-04-30 04:19:00 | NOAA-20 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e35056d3-e5d6-3f23-9212-2c6926338dbb | -21.24843 | -46.95454 | 2026-04-30 04:19:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ee1f4517-a1c3-3a07-a74a-046b41784565 | -11.93373 | -43.97226 | 2026-04-30 04:19:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aaac09c2-3e36-3181-b55f-f7c5a6d7d791 | -11.40797 | -48.42257 | 2026-04-30 04:19:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c91dc07a-2988-3f9e-80f3-102c3c06b646 | -17.2511 | -47.08009 | 2026-04-30 04:19:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| a0e6ef13-b27c-3e10-a154-13c25d9ce1a7 | -18.05477 | -53.00546 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 05dac8df-ac69-3441-b101-76328b2f11c0 | -18.0847 | -52.99973 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 99d22cd4-78ed-3f51-8683-0ddd070e0023 | -17.99848 | -53.00325 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 25226193-b1c1-31c0-8bf6-4fc6631ad6b6 | -10.99158 | -45.0873 | 2026-04-30 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 533bdc23-0e4f-3bbc-abf6-3178eea1d27e | -18.0283 | -53.01996 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2b036a6e-72d6-3a4c-87b1-117749befd1c | -10.9955 | -45.08429 | 2026-04-30 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 32.6 |
| 9a8f34ef-b811-36f0-9287-bd96f129d84c | -18.02376 | -53.01899 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c110d0a3-1e1c-3485-bfe3-8e87c0b6ba5f | -11.13344 | -45.13623 | 2026-04-30 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3a247aa8-bb8b-38b7-920e-6aebf1619566 | -18.02736 | -53.0248 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bbd79bd7-15bb-3544-807a-21bd9b639bad | -18.04022 | -53.00739 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 4bf6425a-a2ab-320e-8eb8-a9e2856798a2 | -18.05383 | -53.0103 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| aa90d460-1883-31b0-8463-f5511f2cfea3 | -18.0593 | -53.00645 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 34.2 |
| 3cfc3d2f-636c-3b6b-a49c-26e1937df90b | -18.04476 | -53.00834 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f74c5ba9-0a5a-398d-850d-15edf954a52f | -11.40724 | -48.41978 | 2026-04-30 04:19:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22998254-d6e3-3b9b-b82e-c92af89d2674 | -10.99332 | -45.07663 | 2026-04-30 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 9a0b77a4-e25c-3ae2-b252-b9bdba465c7f | -17.25447 | -47.08072 | 2026-04-30 04:19:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 70d1d0ba-f976-325c-9e20-b34597c72cee | -10.93254 | -44.14167 | 2026-04-30 04:19:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 224ea43d-dca8-3301-b1fd-e9c74a22fd4a | -18.0074 | -48.17604 | 2026-04-30 04:19:00 | NOAA-20 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 608cf449-b3e0-3cca-891c-638a4bd3a093 | -12.01447 | -45.34369 | 2026-04-30 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b41eeb12-807e-3ca1-8546-e8ff52c7b6d7 | -17.25048 | -47.08385 | 2026-04-30 04:19:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 6f8494b6-f8b1-36f8-a46b-1fa2a6eaa1d1 | -11.40641 | -48.42452 | 2026-04-30 04:19:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ecb78f0f-fd3f-3a6b-b718-b5dcadcc525f | -18.00301 | -53.00425 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f76bd367-c3d8-328d-a323-f09fde456a28 | -20.64185 | -43.98609 | 2026-04-30 04:19:00 | NOAA-20 | SÃO BRÁS DO SUAÇUÍ | MINAS GERAIS | Brasil | 3160900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3f542fd9-7744-3618-a133-cf0aec4f0a96 | -12.00465 | -38.66881 | 2026-04-30 04:19:00 | NOAA-20 | OURIÇANGAS | BAHIA | Brasil | 2923308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2426719b-d5c7-3aac-8cd5-9454037dcc71 | -17.24773 | -47.07947 | 2026-04-30 04:19:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 836e786d-c8f6-316f-8518-1f48c66fd88e | -17.98489 | -53.00024 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d368550b-976b-361f-90ca-2136f7c88bf1 | -17.25784 | -47.08134 | 2026-04-30 04:19:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07dc1608-4c9a-379e-8165-859bce45a27a | -18.00809 | -48.17207 | 2026-04-30 04:19:00 | NOAA-20 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d0c1730-ffae-355e-bea0-a8d418d45cfa | -18.02925 | -53.01514 | 2026-04-30 04:19:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 159110a6-9a5d-3e37-a51e-7f988e0b7924 | -10.96614 | -45.10129 | 2026-04-30 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README3.md)
