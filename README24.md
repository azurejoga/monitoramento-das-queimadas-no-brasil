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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13cb8ec3-ffd8-308c-897e-1bc492fc6391 | -1.68728 | -52.43757 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f10e2f8-da9e-3ae8-a4c6-89a13f2057af | -2.67776 | -46.26962 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2aca4b77-488f-3b7a-b8c5-3e5d22f5d3ce | -4.93011 | -43.03495 | 2024-11-29 04:04:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1fcc09c-55b4-30fb-b41e-5be243469087 | -2.87152 | -46.87062 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8759cd0-4247-3bd2-b5af-6ef242a492fb | -2.84504 | -46.84032 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9e81b7e8-160c-340d-83bf-84512f2bae62 | -2.83491 | -49.89033 | 2024-11-29 04:04:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b3b647d-01c9-3ac1-80c0-c170582b6584 | -1.70662 | -52.76733 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c13a7909-a8ca-30d7-920c-9b1c1c911890 | -2.7537 | -51.66603 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e07aa11b-7034-3ea2-863d-8c94dd1d81c9 | -3.22572 | -48.82262 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 53e9b38a-6574-3557-88e5-af32b24555c5 | -5.75698 | -46.26679 | 2024-11-29 04:04:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a8c06e64-92a7-3955-a2b4-15d0673c28c3 | -3.41626 | -50.16273 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91f5c529-8a37-3434-860a-9eb186ff7c8f | -3.68282 | -44.70379 | 2024-11-29 04:04:00 | NOAA-20 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b58aab7-1b38-3298-b268-1a62e96f9a97 | -5.02246 | -45.07263 | 2024-11-29 04:04:00 | NOAA-20 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7eef689d-bbc7-3132-b277-c27841d88683 | -3.35543 | -43.17215 | 2024-11-29 04:04:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d0e5b1ee-b51d-3416-8c55-de315745cf5e | -3.25334 | -53.63559 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 882ce400-472a-3d78-a992-dd06627a23e3 | -0.99534 | -51.72819 | 2024-11-29 04:04:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3bccd418-1f72-3fe0-a122-4950a3cadd4e | -2.73041 | -48.8983 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 951a9855-379e-35fb-957c-744c214481a6 | -3.46166 | -50.53833 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a28c65b5-9491-3025-bc45-dcfc9d68a887 | -3.68152 | -42.9487 | 2024-11-29 04:04:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5aede2f4-a100-3b1a-89a0-1a11b90ff1a0 | -3.61506 | -50.19343 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 610cdf74-223a-39c2-9c2f-9d63b42b6029 | -5.04542 | -43.61973 | 2024-11-29 04:04:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0f48754a-7d63-35f8-a386-a74995625524 | -3.36746 | -50.82613 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 082682b7-2732-352c-bb7e-e3f8da4b3c4b | -3.31186 | -50.28027 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54380867-6a19-3880-9289-036a328bc6b5 | -1.5283 | -52.67091 | 2024-11-29 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3c2c7141-b2cf-3f0a-8e41-eb74833b1d4c | -3.6768 | -54.45166 | 2024-11-29 04:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfd72037-d4cb-3dbc-8411-c0de3bb10e9c | -4.81862 | -44.35707 | 2024-11-29 04:04:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 807d3f00-ccd7-3807-b1c3-0fe5169866f0 | -5.71887 | -43.84374 | 2024-11-29 04:04:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18533ba0-1af1-3657-ba21-1af415ff24bd | -1.30757 | -51.95821 | 2024-11-29 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f062365-3fa6-3f78-83f1-b7b034b54148 | -4.05738 | -46.68309 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38cd6e98-dcc3-38d0-9c79-3439cf96ac88 | -6.09371 | -43.96921 | 2024-11-29 04:04:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| acdbca05-d1eb-38d6-959c-d8c4036aa69a | -4.17272 | -48.62753 | 2024-11-29 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c2e7b97b-e011-3d35-97ed-c18173b185a2 | -3.12161 | -53.26508 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 973faa6e-5ddd-369e-b1e6-120ef532f1e5 | -4.50355 | -42.07695 | 2024-11-29 04:04:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ac1509db-c337-3783-b825-d59d8198008a | -3.38526 | -50.11461 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| faef166c-e6e1-3e0c-a9e9-c461de5e1278 | -1.91864 | -52.8974 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5217d4ce-8236-3b79-adb1-12e542951f36 | -3.32241 | -50.22217 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1a364e3b-7ba5-3a2b-8020-063dedc4ae11 | -3.30659 | -50.28189 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ee7d20ff-4c0f-3f74-b587-31bad2a9efe6 | -1.59649 | -52.29335 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| ed582eb8-0a95-3483-836b-d58fe0d00a0a | -3.99768 | -46.3095 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3075158e-2282-3b47-ac92-b804fff58153 | -2.83813 | -49.8893 | 2024-11-29 04:04:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c8fcf051-a5ce-3aaa-895e-1f717d63a24d | -5.02441 | -44.45193 | 2024-11-29 04:04:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 075c4bc0-2b90-3b4e-b6f7-37d30ac31551 | -3.10742 | -54.48187 | 2024-11-29 04:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 525c87e5-c2f7-3a76-8be3-738f99d650bd | -3.26651 | -45.37651 | 2024-11-29 04:04:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ab6a0e3f-6a5d-3189-bde2-dd03034146eb | -2.8521 | -46.82441 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6838df10-14e4-34e9-aab4-8fe9462214ea | -3.33329 | -53.2206 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f1930194-b875-39db-bd71-e83d97eb1644 | -2.22389 | -46.39406 | 2024-11-29 04:04:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0d3ae015-be6e-38a4-9e98-50407cfc5695 | -1.62439 | -53.87009 | 2024-11-29 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8c1f0576-6297-31f6-a090-56de69d6bf21 | -2.57142 | -50.00338 | 2024-11-29 04:04:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| da1cf9ff-0e03-3e58-a8c8-e4cc617b556b | -2.84324 | -46.87909 | 2024-11-29 04:04:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d04ec80d-7023-3ec0-9d17-78e21eb8202c | -2.66135 | -48.78667 | 2024-11-29 04:04:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 3f3d3b39-6c86-306b-8d3d-8bf7ebeb962d | -4.68942 | -46.66331 | 2024-11-29 04:04:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0794d2ef-66e6-31fb-b103-f4ddf94ff69d | -3.9188 | -53.66981 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 445cd508-0484-3e83-b4ae-3ee5e522141d | -3.56733 | -53.02995 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 58328932-3227-3ee7-ac6f-e9d523500f82 | -2.67097 | -46.1463 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40526e5f-4109-340c-a833-5e068e59b8b8 | -4.76936 | -44.96085 | 2024-11-29 04:04:00 | NOAA-20 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3fa2a07d-eb18-333e-940b-faef2cfb4375 | -3.2455 | -53.64051 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 0a2c53f4-1463-3f4b-9558-dfa3565515df | -3.36821 | -50.18313 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 09bddfed-22f9-3c8e-a98a-aee4afcb2bf5 | -1.82535 | -46.23508 | 2024-11-29 04:04:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f264b22c-836f-3ca0-abbe-8ee4491b2e90 | -5.38401 | -43.35481 | 2024-11-29 04:04:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46f1eb72-ca46-3873-97dc-61be780de3dd | -2.88734 | -45.08897 | 2024-11-29 04:04:00 | NOAA-20 | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0845e0f6-6508-391f-bfd6-231c11736d1a | -2.6787 | -46.15151 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c38954c-b4ab-3d1b-82fc-2e04d3edda5e | -2.57629 | -50.00781 | 2024-11-29 04:04:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e883537a-3010-3f36-b9f1-f357a780f5df | -1.59177 | -52.28178 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 3865f1eb-e3b7-332d-b612-1695f0708bfc | -2.9855 | -53.30151 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| daffb03c-20a1-3eba-aed9-22e8023cc9be | -3.72357 | -50.18697 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 515185ef-e04c-3114-b1a5-19c528d9c48f | -3.91683 | -46.53448 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 874233ce-af60-3f89-ab67-45436cb3761a | -5.9812 | -45.35366 | 2024-11-29 04:04:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8566a997-01ec-3c0f-97e0-e1b9aba0a77a | -3.24315 | -53.64305 | 2024-11-29 04:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 16e2cb97-1943-304b-9d64-64473cfa28e3 | -4.5041 | -42.07343 | 2024-11-29 04:04:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 630bcc2b-3e81-306e-bff6-4f66c91fc89a | -3.33585 | -53.2174 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 31515feb-abc5-382a-9c4f-8ba5c5c6dfc9 | -3.53802 | -50.18745 | 2024-11-29 04:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7416a9a0-c4e3-3e22-8d4d-fcf11bd128bb | -1.57907 | -53.85079 | 2024-11-29 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| c9f9fb1d-6caf-3d1a-a31f-8fcab3c85306 | -2.7314 | -54.14122 | 2024-11-29 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 54f2d603-b5cd-321f-ae20-3a5c83a1796b | -3.6397 | -44.56141 | 2024-11-29 04:04:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6bdc64f8-fa64-30fc-8be0-caeddf3503cd | 0.98014 | -50.13095 | 2024-11-29 04:04:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 82dd465a-4701-3670-aba3-2ccf2be91a43 | -2.69818 | -46.11951 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6229a1a-9411-3fae-8b56-0ed2f94e3f9e | -5.18639 | -40.52329 | 2024-11-29 04:04:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 164260d6-5fa7-319d-9c5a-aa786c405a7e | -3.27738 | -50.55336 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70c30c06-1265-361e-af40-4e12db1fae0f | -5.04006 | -43.62338 | 2024-11-29 04:04:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| f96d2770-7d5b-310a-a9a7-2621d724aa7b | -4.08458 | -46.83012 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e729f5f-2923-388b-b15c-59c1f905fbf3 | -3.61231 | -40.49015 | 2024-11-29 04:04:00 | NOAA-20 | MERUOCA | CEARÁ | Brasil | 2308203 | 23 | 33 | nan | nan | nan | Caatinga | 6.9 |
| e238e1be-a0ae-3533-81f1-26967062b4e0 | -3.52722 | -44.94842 | 2024-11-29 04:04:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 747b6232-1d00-3623-ab7c-5b91bea3bbc1 | -3.94632 | -46.72679 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| da985747-017e-3e61-b3df-1425caae9ff7 | -2.97987 | -53.29459 | 2024-11-29 04:04:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 7ceccee7-941f-3523-bc3f-f98e4a8d2030 | -1.53268 | -52.69339 | 2024-11-29 04:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46c4c2a0-3ec3-30ab-8495-5c9ab307c6b0 | -2.49 | -49.05066 | 2024-11-29 04:04:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 59469e1b-0490-38e8-8e3b-b49997eba86e | -3.76008 | -49.90149 | 2024-11-29 04:04:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb574fa3-b88d-305b-b590-b441865d7a2c | -1.96117 | -46.4455 | 2024-11-29 04:04:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 8aacc1fa-fe32-365e-8033-48ca7f7a2d9a | -4.08148 | -46.83019 | 2024-11-29 04:04:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9afb36d0-c450-3eb5-8594-fc77d7e389cf | -3.24804 | -50.59054 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5f23168-353c-3810-a0aa-93153acaf0e1 | -1.71347 | -52.63807 | 2024-11-29 04:04:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 25a6915e-736e-3e3e-9893-e0c4c647ca33 | 0.99019 | -50.27077 | 2024-11-29 04:04:00 | NOAA-20 | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9cbb3109-1ebd-33f3-9a43-fe1048210719 | -3.17598 | -50.28273 | 2024-11-29 04:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ed79d83-3078-3b0c-821d-68c0c27e5a02 | -3.17318 | -46.31153 | 2024-11-29 04:04:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c28d4cd1-d125-3fae-80ec-a1a0f4a1f8a1 | -4.17535 | -48.61177 | 2024-11-29 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fdeb1128-00f4-3657-a514-8517f1c8381e | -4.31407 | -48.08543 | 2024-11-29 04:04:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa0f1358-869b-3fad-96e6-7bd99a158098 | -2.73346 | -54.14208 | 2024-11-29 04:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 482dbf62-814d-3da9-8e09-e0eb110b1bfd | -2.68777 | -46.15668 | 2024-11-29 04:04:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 26f83ac7-80a4-3feb-be3a-a1d4fdadad90 | -1.58722 | -53.84512 | 2024-11-29 04:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0648ac4e-d52d-31c6-b158-6b2945310c6b | -1.58833 | -45.58826 | 2024-11-29 04:04:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README25.md)
