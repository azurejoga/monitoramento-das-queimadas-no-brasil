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
| 3b6bc64d-afac-3634-ad8e-23679f060587 | -12.875 | -44.3122 | 2026-07-02 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 54.9 |
| a1cfe0ef-61e6-3740-af04-b092fbe60da7 | -11.8007 | -57.0032 | 2026-07-02 03:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 89ec1db5-1d42-3120-b5f1-a99bb2fb7964 | -21.7823 | -56.2976 | 2026-07-02 03:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 8aa0bf1e-6505-3f5a-ac8c-afafd290b54e | -21.7827 | -56.2762 | 2026-07-02 03:40:00 | GOES-19 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 4c480985-0516-37c2-bda1-5b4d57020323 | -12.8741 | -44.3593 | 2026-07-02 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 250.5 |
| 4750b5a0-2ca7-3dbc-b01a-1b76f97869aa | -12.8548 | -44.3625 | 2026-07-02 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 242.1 |
| 55c82338-89d7-3c9e-9fad-6c29342c04aa | -10.9397 | -43.0593 | 2026-07-02 03:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 6f084edc-5306-3282-ab50-e11ef29ba136 | -12.8746 | -44.3357 | 2026-07-02 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 374.6 |
| 5a4576f6-bf5f-3688-b9d9-deb16b061221 | -6.91576 | -43.72108 | 2026-07-02 03:42:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 11f8a0fe-9d80-3b5f-8acb-5219836bb2c2 | -6.9203 | -43.72501 | 2026-07-02 03:42:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| bc1f2c4d-a9f8-3107-b0ea-21a0fb86be99 | -5.80993 | -43.79845 | 2026-07-02 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 911a1108-39b0-3657-8513-bd3efdaa068e | -7.00659 | -42.77639 | 2026-07-02 03:42:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f54c42d4-ea34-39cf-909f-2643a7869831 | -4.34857 | -47.76466 | 2026-07-02 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c198fdba-547a-3a5c-b5d0-a5f384e4e0a8 | -3.41696 | -41.70354 | 2026-07-02 03:42:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 24.1 |
| d1c573c6-7590-300b-a8b1-b6e617b07253 | -7.0945 | -46.50798 | 2026-07-02 03:42:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 39f18045-75d3-3c78-abbb-cc167d43ea59 | -4.00601 | -48.05806 | 2026-07-02 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 307dcc6b-0614-35bf-9453-d8fcfc5cc660 | -5.7894 | -45.0446 | 2026-07-02 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 49fce23e-63c5-3925-9655-000bd809daa6 | -3.47508 | -39.58014 | 2026-07-02 03:42:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| d4ce584b-5f1c-31c3-a269-e87cc3269400 | -5.836 | -35.52081 | 2026-07-02 03:42:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bd722b2b-d0e0-3828-b7dd-71d3212e52be | -3.41907 | -41.70677 | 2026-07-02 03:42:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| c97ab0b1-d830-319b-ae5a-d76059a73cdb | -5.37304 | -43.38044 | 2026-07-02 03:42:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d2c08ecb-b886-3cfd-83c6-28ac5e088ba5 | -5.56106 | -43.82966 | 2026-07-02 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 033c39cc-f278-37e4-8f99-61632c7f1a27 | -5.14989 | -37.91154 | 2026-07-02 03:42:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ff01b30d-3b76-374f-8ad4-67106c5f2d40 | -7.10059 | -46.50896 | 2026-07-02 03:42:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5c9cf805-7f0f-3cd5-b445-941a6c9f9cb7 | -3.51082 | -48.03978 | 2026-07-02 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| c71c0bdf-8c8a-325d-a99b-4b34edc6ea1a | -3.51207 | -48.03279 | 2026-07-02 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 5b53bfa2-8317-36ed-b511-866a13653fd6 | -3.51203 | -48.04443 | 2026-07-02 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 50ddbffd-738f-3ced-be79-e86860b9048a | -5.14629 | -37.91096 | 2026-07-02 03:42:00 | NOAA-21 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e1fd660a-6edb-3986-9adf-9a7b1e34f02f | -4.01191 | -48.06546 | 2026-07-02 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9cdaac0e-98fc-39c5-9701-1b80b6051143 | -5.81515 | -43.79926 | 2026-07-02 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0e6d2137-dbea-33d5-99ce-269acea39053 | -5.81571 | -43.79609 | 2026-07-02 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 06045692-bb6a-371a-b08b-2e71ce0157fa | -5.29603 | -43.70641 | 2026-07-02 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c45152aa-6015-35e9-9fcb-0b7f530aa25b | -3.41612 | -41.70852 | 2026-07-02 03:42:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 24.1 |
| 398fea38-b5f8-3262-af56-8da430ab1953 | -6.34672 | -43.65379 | 2026-07-02 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10e1e25a-3adc-3cf4-99f8-c5cc198bd3f2 | -3.5178 | -48.04122 | 2026-07-02 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 145c31c8-ef5a-3f36-b0ff-5255319a1729 | -6.92645 | -43.71983 | 2026-07-02 03:42:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1ca2e3ef-787b-3461-b6f2-907e200b9f7b | -3.41827 | -41.71177 | 2026-07-02 03:42:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 15e25714-0b4f-30bd-956e-1be49a306ad2 | -7.00272 | -42.77036 | 2026-07-02 03:42:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6b475334-dc0e-3eb5-a543-d1a181c80115 | -7.00957 | -42.78767 | 2026-07-02 03:42:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e3b27f96-8fac-330b-90ad-d1ebdcb47b1e | -5.5387 | -35.52688 | 2026-07-02 03:42:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1ba5970e-826b-3b4d-b624-f83fb2f4bae0 | -3.50631 | -48.03566 | 2026-07-02 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 04c6c38f-94d9-3cd8-be66-b4239390f7a7 | -4.15765 | -43.08488 | 2026-07-02 03:42:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f05fd31d-8c0f-3575-bae5-e09f787f2781 | -6.92137 | -43.71893 | 2026-07-02 03:42:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 437b52b9-aa2f-390a-a32b-960398d20c98 | -5.7901 | -45.04071 | 2026-07-02 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f41c6d3e-b3fa-3526-984e-5bf21fce0e16 | -5.34497 | -45.18597 | 2026-07-02 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 479a7ac2-c2c2-30d9-aa3c-f947e2f87786 | -5.34568 | -45.18198 | 2026-07-02 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0ddfef13-74ed-330d-949e-8382c196548b | -5.79402 | -43.63388 | 2026-07-02 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb62a365-b5b8-3a90-b9a4-7fd3bdec440e | -3.41438 | -41.70599 | 2026-07-02 03:42:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 22.8 |
| 74066aee-5825-30f1-81fe-e134f25b676d | -4.34927 | -47.76583 | 2026-07-02 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| cafb8156-8cee-3cc5-ab8e-3152e3b66cb6 | -5.79573 | -45.04179 | 2026-07-02 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6315e87a-3381-3c54-81b4-2b1dba9f781f | -5.56157 | -43.82835 | 2026-07-02 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4064e66e-64d2-378a-8ffe-5e306664b878 | -6.92592 | -43.72285 | 2026-07-02 03:42:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 89b8e212-4a8a-3f15-8b1e-bab850e7b4ac | -6.59383 | -43.8879 | 2026-07-02 03:42:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f20c84e-6dcf-3824-ae50-9cb2a0d05664 | -7.09974 | -46.51367 | 2026-07-02 03:42:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2e3ff70f-6a56-36a8-94b8-cf40515b0ae0 | -5.02427 | -37.04114 | 2026-07-02 03:42:00 | NOAA-21 | AREIA BRANCA | RIO GRANDE DO NORTE | Brasil | 2401107 | 24 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 7569088e-0cb5-3b31-978a-fc85fc48ad10 | -4.57982 | -48.02756 | 2026-07-02 03:42:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ec1f7de1-3a0c-3160-9fec-c597331710c6 | -3.41518 | -41.70099 | 2026-07-02 03:42:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 9ac531d3-3f92-3f80-83d1-781a62b82ef1 | -3.41987 | -41.70179 | 2026-07-02 03:42:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 4ca4baba-e2ce-3f5f-8fb8-b083b69a1890 | -6.30756 | -39.33511 | 2026-07-02 03:42:00 | NOAA-21 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2308d074-cfb6-35ac-a885-421b19e209da | -5.35071 | -45.187 | 2026-07-02 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 901a256d-6c23-30fd-b5b7-1ac624759b5b | -5.79712 | -45.03399 | 2026-07-02 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c198f469-7fd3-33a9-bee9-7c5658e54e36 | -4.00473 | -48.06533 | 2026-07-02 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| dbf9a885-30ab-3ac2-863b-5af1ff2b226b | -3.50377 | -48.0387 | 2026-07-02 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 08a83690-b988-3f60-a2dd-248029300530 | -3.51913 | -48.03382 | 2026-07-02 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1decb655-e53f-3d59-8a68-e044c57e20d2 | -3.51338 | -48.03664 | 2026-07-02 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 0f45d075-292d-3910-b045-9ab960a802c0 | -5.78872 | -45.04843 | 2026-07-02 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0f03d8e2-5e40-350b-974b-7bb550a416c9 | -5.81049 | -43.79526 | 2026-07-02 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8566c89b-cbbc-33b6-98fd-9af3313580a4 | -2.94858 | -40.49978 | 2026-07-02 03:42:00 | NOAA-21 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 557da7e6-b8ec-39a1-9712-5a4cba8edf21 | -4.94637 | -48.245 | 2026-07-02 03:42:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2e99155e-c0de-31d0-95fb-82c40eb183fd | -5.79643 | -45.03787 | 2026-07-02 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9918c36d-4614-37af-99ac-6084a7ad89cb | -4.01312 | -48.05859 | 2026-07-02 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 731bdcb4-a421-3375-bbbb-b572dd7c62b6 | -5.37867 | -43.37818 | 2026-07-02 03:42:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 26089550-4e56-3d8a-9a43-0ab8d4c307b0 | -3.42165 | -41.70433 | 2026-07-02 03:42:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a3887876-d2b9-3f66-9a52-323a48a1491e | -6.72305 | -38.2378 | 2026-07-02 03:42:00 | NOAA-21 | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 17d0cd6d-6083-33c2-ba53-7e302a7d2505 | -5.79596 | -43.63511 | 2026-07-02 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e311c0e5-b43c-3399-b9f6-5429bcc7e060 | -3.41226 | -41.70277 | 2026-07-02 03:42:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 24.1 |
| 75dc9732-0332-3057-9346-207c642b03ab | -6.931 | -43.72375 | 2026-07-02 03:42:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5445f1a8-8ab3-3edb-9f3b-15de58c987c5 | -5.79504 | -45.0457 | 2026-07-02 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce3ec323-9952-355a-aaf8-091cf3dc25f2 | -5.29547 | -43.70962 | 2026-07-02 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 456c154e-eca5-32f5-9fce-5d0265b95d91 | -3.47102 | -39.57949 | 2026-07-02 03:42:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 0b682673-c050-3154-b4f6-d2051f070af8 | -7.0057 | -42.78164 | 2026-07-02 03:42:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 5123c5f4-3652-3b4a-8914-935b9fce2df2 | -5.37815 | -43.38123 | 2026-07-02 03:42:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c94f90c2-c6bf-3b8f-979c-885c20ab792e | -3.41357 | -41.71098 | 2026-07-02 03:42:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 22.8 |
| c9befed4-c54c-3ae0-b1f0-b04dd68aced2 | -5.561 | -43.83161 | 2026-07-02 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3740d840-0661-37aa-aae6-baaa5e48c320 | -6.92084 | -43.72197 | 2026-07-02 03:42:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3eb369f0-64be-3ab1-a28c-dd6b5b9c482e | -8.49894 | -47.19753 | 2026-07-02 03:45:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 39bb23b6-11a0-3e44-b77a-c7aca5846607 | -12.79081 | -44.4934 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1fe013d9-090b-3b0e-b56b-b51c072d1375 | -8.31489 | -45.37667 | 2026-07-02 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a82688a-44df-3c6a-906e-9b821b48590c | -9.74736 | -49.03643 | 2026-07-02 03:45:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24945bcd-2183-3eda-a1f5-3d22a1827757 | -10.94604 | -43.05092 | 2026-07-02 03:45:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 32.1 |
| e2b51bae-2edc-31ee-857b-904fed8e2701 | -12.86752 | -44.35179 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 985f81dc-8844-31a3-b213-3f6bccd0fb56 | -12.74511 | -44.47684 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 151.4 |
| 2ac4fe16-4e4b-3faa-9a24-849038a84ac8 | -12.76134 | -44.49699 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 053426d8-bb87-393b-9898-a7282c6e3080 | -12.51802 | -48.27653 | 2026-07-02 03:45:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| abfd30fa-9f7a-3aad-9d6c-896df39f2cdc | -12.12711 | -38.16788 | 2026-07-02 03:45:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 09ed9ca3-c0c7-3d6b-91c7-f6a465dd1a92 | -12.85119 | -44.35965 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 32.3 |
| ab43261d-4b2d-383d-99cc-c201e483fdfc | -11.91029 | -43.39106 | 2026-07-02 03:45:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb006646-8c4e-3779-8151-d62469f5aae6 | -12.50931 | -48.28202 | 2026-07-02 03:45:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bb9f9b5c-2e0b-3b8b-99ea-5c7f5b549615 | -12.85998 | -44.33931 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 8059e8da-928f-3eb0-9e4b-fa3a3b2c7c5c | -12.75856 | -44.48509 | 2026-07-02 03:45:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 705.9 |


[Clique aqui para ver as próximas entradas](README8.md)
