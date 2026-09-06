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
| 51b58d7f-fff6-3284-91fb-03efe2a2551e | -4.45275 | -46.1332 | 2026-09-06 04:00:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0f8e9da4-23b5-381d-9f05-e6f9a43206de | -2.76474 | -48.57616 | 2026-09-06 04:00:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7cf6da99-9676-397a-91c9-d919b3f2394d | -6.87653 | -41.04315 | 2026-09-06 04:00:00 | NOAA-20 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| cfc888cc-f390-3033-bb92-f9b23ede4b08 | -6.23741 | -35.1497 | 2026-09-06 04:00:00 | NOAA-20 | TIBAU DO SUL | RIO GRANDE DO NORTE | Brasil | 2414209 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e20ef55f-f2ec-3320-8cec-5146af382c0c | -6.18572 | -40.87455 | 2026-09-06 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 3478d11c-ed45-35d2-ac71-16b700e4ceb4 | -3.55246 | -48.18922 | 2026-09-06 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9b27385a-75ac-39e2-87f1-dd796848c334 | -5.89668 | -44.73406 | 2026-09-06 04:00:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04fef806-bb82-3972-a731-3408dc35caff | -3.33692 | -39.77155 | 2026-09-06 04:00:00 | NOAA-20 | AMONTADA | CEARÁ | Brasil | 2300754 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| cc120cd8-2c7e-31bf-ba35-fbfcf13f0aea | -3.54098 | -48.18716 | 2026-09-06 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8ae3c8b0-df65-3e74-b327-a7795266dc2f | -3.16196 | -50.82818 | 2026-09-06 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 92db5b91-ed88-3e59-9c20-cdf3bedb3e1a | -1.1994 | -47.7606 | 2026-09-06 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 52229303-7121-34b0-8fcb-a3bcd7f5c802 | -5.03908 | -44.46542 | 2026-09-06 04:00:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27b3aeac-dd4e-3f4d-943c-b46ca7f261a8 | -6.26906 | -43.27071 | 2026-09-06 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6747cd9-90d5-3676-8448-0fbedd31c167 | -5.89229 | -44.73332 | 2026-09-06 04:00:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf1ce56c-d64f-3075-9964-df215410cc94 | -3.8541 | -44.05152 | 2026-09-06 04:00:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18427d16-50f1-3312-bba9-a338eec805a5 | -5.05412 | -38.38925 | 2026-09-06 04:00:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 79b2d344-91c5-31cb-a65b-7293c9d21e05 | -5.63654 | -44.36815 | 2026-09-06 04:00:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d7c5ef02-dc9b-35d1-b0d4-3dced5b87ff4 | -1.20493 | -47.76304 | 2026-09-06 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d37cc4d9-584d-33d1-ac68-aff69a896637 | -5.1543 | -37.34339 | 2026-09-06 04:00:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8b79f580-4e92-3f7b-bdbf-c66943613da1 | -2.25013 | -46.12365 | 2026-09-06 04:00:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72623947-ae3f-3601-b315-b189077e5abf | -6.18509 | -40.87844 | 2026-09-06 04:00:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| e08c6008-2902-3014-a20c-372f064d3048 | -2.85717 | -50.4665 | 2026-09-06 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fb3bc405-e7af-3293-a0e0-d4d7ec36ec6b | -7.14002 | -38.28068 | 2026-09-06 04:00:00 | NOAA-20 | AGUIAR | PARAÍBA | Brasil | 2500205 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 11f8cb7a-5b4e-3550-a031-f45fd89b912c | -3.54742 | -48.18402 | 2026-09-06 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b6dba78d-a638-3b3f-9b98-13abbc0588c4 | -5.04345 | -44.46611 | 2026-09-06 04:00:00 | NOAA-20 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f45c20f6-dfd3-39a3-aa8a-d7fc0b83709c | -2.87488 | -50.46412 | 2026-09-06 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 98a6c018-2729-3588-875f-b821824eba67 | -1.86589 | -47.98021 | 2026-09-06 04:00:00 | NOAA-20 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0255ae8-dece-319b-b922-ef120729c809 | -6.23779 | -35.14854 | 2026-09-06 04:00:00 | NOAA-20 | TIBAU DO SUL | RIO GRANDE DO NORTE | Brasil | 2414209 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5ecc0f40-4da0-353d-890e-ea1c5dfeea4e | -4.11358 | -49.08309 | 2026-09-06 04:00:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 599f0822-3ba2-366c-8784-a48b2c1298f6 | -4.45675 | -46.13941 | 2026-09-06 04:00:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 40b26a7b-03ba-33e4-ab34-65e31c79ce54 | -4.23894 | -44.61008 | 2026-09-06 04:00:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ee29c823-8573-399a-b106-d1d25f1ff61d | -5.46918 | -37.33151 | 2026-09-06 04:00:00 | NOAA-20 | GOVERNADOR DIX-SEPT ROSADO | RIO GRANDE DO NORTE | Brasil | 2404309 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e682f4b3-3266-35e1-a736-6f04f31c61a9 | -4.36806 | -47.7785 | 2026-09-06 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 0fdd40da-2f99-3fd1-9090-323988e1ac76 | -3.54167 | -48.1831 | 2026-09-06 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 328948fa-9669-3643-9b94-ffe0af271f03 | -2.86052 | -50.46764 | 2026-09-06 04:00:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f6453992-6210-32eb-a35b-f7769ebcd17c | -4.63177 | -48.64138 | 2026-09-06 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ee35ae07-ac09-3fdc-9f74-16203e2c0322 | -5.54582 | -44.25339 | 2026-09-06 04:00:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1163e12d-cb87-3fcf-b477-02b1bd6099cd | -4.3465 | -48.97702 | 2026-09-06 04:00:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cec0816f-8f75-30b2-9a6d-97405b08dc73 | -3.55318 | -48.18498 | 2026-09-06 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 48c9a68b-f214-3e1d-909d-b88761ca1e75 | -2.76776 | -48.57753 | 2026-09-06 04:00:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3250e00d-0640-3827-8c7c-fe50753bcbb3 | -4.36315 | -47.77396 | 2026-09-06 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 89f4ab55-42bd-3c0d-8001-8b1b64560d16 | -1.19913 | -47.76211 | 2026-09-06 04:00:00 | NOAA-20 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 96202965-fba1-38a2-9c62-0c16c1708cba | -4.45577 | -46.13725 | 2026-09-06 04:00:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 05e3e2aa-d529-3577-8595-aa069e95056b | -7.13947 | -38.28415 | 2026-09-06 04:00:00 | NOAA-20 | AGUIAR | PARAÍBA | Brasil | 2500205 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a445efbc-6711-3c08-aad8-04cfa8363578 | -9.5741 | -40.35906 | 2026-09-06 04:02:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 91.6 |
| 58bd1ca5-64f8-3dcc-8f79-ff3267b46aa6 | -11.32531 | -45.72361 | 2026-09-06 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98fd20c3-2cb9-365b-a44b-0ae057b716b8 | -8.94792 | -44.41148 | 2026-09-06 04:02:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0bd95c53-1b0b-3d53-9334-59bc2e74cc99 | -6.86725 | -41.64869 | 2026-09-06 04:02:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 983a32c9-426e-3a19-b068-627590a29ef2 | -13.42899 | -41.88615 | 2026-09-06 04:02:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 48b10e53-f6f5-31fb-9913-98092776c7c5 | -12.94781 | -42.41539 | 2026-09-06 04:02:00 | NOAA-20 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c3f73c90-f2a1-3cdb-9c96-70b381f5ede4 | -11.29407 | -45.70096 | 2026-09-06 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 01f18431-0a3f-36ad-af9e-888d2b5c4abd | -10.03431 | -48.2166 | 2026-09-06 04:02:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 400969de-a282-3ab8-aa18-386da8a27213 | -13.32187 | -44.04126 | 2026-09-06 04:02:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 96fabbaf-12ab-356f-891c-38d470f96133 | -13.42959 | -41.8825 | 2026-09-06 04:02:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 573c67c2-6b88-3091-b8d5-aa9cb3b282ec | -5.92376 | -47.89256 | 2026-09-06 04:02:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0a59daa1-55e5-3770-9ff4-820f6e24cf04 | -11.9448 | -44.86397 | 2026-09-06 04:02:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e266db1-634a-33b6-965f-d88605274747 | -11.28911 | -45.70406 | 2026-09-06 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7a4259aa-2772-377d-8651-0d30d1e38a19 | -8.10676 | -40.08116 | 2026-09-06 04:02:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ba785644-c0d7-3151-a640-d9fd87741684 | -13.41881 | -41.8844 | 2026-09-06 04:02:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 362d7806-57aa-378b-8c2c-84e1457b899d | -8.9702 | -44.404 | 2026-09-06 04:02:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbd91da1-7df8-3428-86db-1175b15c5d70 | -8.97718 | -44.41231 | 2026-09-06 04:02:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9597d278-4234-3c6d-a436-fba28e229d4b | -10.69069 | -45.93346 | 2026-09-06 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8c68e3e-6a33-3953-9199-e900efcb4208 | -13.43517 | -41.89103 | 2026-09-06 04:02:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| fc3ffbaa-7655-3078-adf2-c4a8994d4561 | -7.19789 | -43.60515 | 2026-09-06 04:02:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 268ee57b-0a44-32f9-ba7e-6e6152b3a40f | -8.31472 | -37.26903 | 2026-09-06 04:02:00 | NOAA-20 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cd39bea0-0a6f-3ee7-9a63-d403dcccb458 | -14.28685 | -42.69654 | 2026-09-06 04:02:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 33d1d875-9964-3a55-aa55-dffe396b0e7d | -7.37166 | -47.76006 | 2026-09-06 04:02:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 333db2d9-8a4c-3ed4-9c13-fde8c191715a | -8.11528 | -40.84743 | 2026-09-06 04:02:00 | NOAA-20 | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 94b4385f-820d-3940-92f4-8d9343b239e2 | -11.32679 | -45.07582 | 2026-09-06 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54780aa6-5547-3d10-9ebd-5ad3264f54f1 | -13.43238 | -41.88676 | 2026-09-06 04:02:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 17255b5d-443c-368e-b024-170b65f44b0b | -14.28341 | -42.69579 | 2026-09-06 04:02:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 3f7d398e-b91a-33d8-9eb0-939bbdff3fe7 | -13.43178 | -41.89042 | 2026-09-06 04:02:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 22.7 |
| 473f53a8-0f8b-30aa-9457-e2a2eb4325cb | -13.14395 | -40.21908 | 2026-09-06 04:02:00 | NOAA-20 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 720fac7a-f0fd-3227-8498-5e443fcb1d3b | -13.42281 | -41.88129 | 2026-09-06 04:02:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dbe0f56a-63dd-3476-a7ca-86949f5df7d6 | -9.76608 | -39.24495 | 2026-09-06 04:02:00 | NOAA-20 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c3bfd693-b782-3206-ba30-0578145a824f | -11.28554 | -45.69937 | 2026-09-06 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb055bfc-1097-33e1-9b28-9eada2965573 | -13.86652 | -44.3045 | 2026-09-06 04:02:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| df8482b5-3767-31c7-a157-721a4253c3f7 | -7.3769 | -47.76103 | 2026-09-06 04:02:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2650c6d-d6d5-3031-a64b-1e459810a079 | -7.89604 | -47.69859 | 2026-09-06 04:02:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6ca0719d-bb3e-3d50-9d2a-39c458ca820c | -11.28981 | -45.70014 | 2026-09-06 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f90e2e58-e9a5-3627-9cd5-8949133cb197 | -13.72451 | -41.96836 | 2026-09-06 04:02:00 | NOAA-20 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5184d429-5957-32fc-bbce-c44a4bf3230a | -9.56741 | -40.35797 | 2026-09-06 04:02:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f63c9b7b-292d-366b-bc54-dfd4e37f9577 | -11.10637 | -38.64334 | 2026-09-06 04:02:00 | NOAA-20 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a08a574c-c8f2-324a-a75d-a6ca2a8f9e45 | -11.27553 | -45.70591 | 2026-09-06 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 6e6e8526-3078-3a42-b17e-8f67ac351df7 | -7.66836 | -46.05627 | 2026-09-06 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad8c6129-2bed-370a-8cb7-3cf86bef59fa | -14.19239 | -42.82302 | 2026-09-06 04:02:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 59d654c0-95c7-3ff1-bf44-9d3b341b613d | -12.70885 | -42.3401 | 2026-09-06 04:02:00 | NOAA-20 | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e6298485-dda5-34a1-85f2-0ab593c31e5f | -14.28572 | -42.69316 | 2026-09-06 04:02:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4c7e8939-aca7-39cd-967d-1e00358e9916 | -10.70487 | -45.90512 | 2026-09-06 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f6b4c868-b83a-31a1-a10d-5d631a26b922 | -11.29072 | -45.11221 | 2026-09-06 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 680017b7-87a6-3896-a761-832ddf867e9d | -13.42718 | -41.89716 | 2026-09-06 04:02:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 204e47d8-2876-31a2-9d0f-b1626151afb7 | -9.52164 | -41.99519 | 2026-09-06 04:02:00 | NOAA-20 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9ab1ae5d-cfef-3699-8b10-926447cff198 | -10.03948 | -48.21753 | 2026-09-06 04:02:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e733daca-f6ac-38af-85ca-bf0e6f897d53 | -11.28793 | -45.10404 | 2026-09-06 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce5363ae-0cec-34c5-bed7-2e5e00bdb2a8 | -13.43146 | -43.82749 | 2026-09-06 04:02:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 950d8bf3-bc5d-3f71-ac93-bda859b3d547 | -14.28507 | -42.6971 | 2026-09-06 04:02:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e74bb378-54f4-30f3-a898-3f3bcf6f3819 | -13.53544 | -43.9995 | 2026-09-06 04:02:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a48537f8-0d16-36d6-aa89-7274b30e389a | -11.33161 | -45.07241 | 2026-09-06 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 68b2fd5f-642e-31e3-869b-a21776299bb6 | -13.42379 | -41.89653 | 2026-09-06 04:02:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e3928d96-cfce-35bf-8762-9c24d53afdb8 | -11.33573 | -45.07303 | 2026-09-06 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |


[Clique aqui para ver as próximas entradas](README14.md)
