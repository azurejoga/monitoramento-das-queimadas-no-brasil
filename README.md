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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 112c3c37-68ae-39c7-a47a-516eb48405f9 | -23.6014 | -53.0085 | 2026-07-10 00:00:00 | GOES-19 | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 70.9 |
| 24f71921-1aab-3b09-a57d-5508475eea5d | -8.5175 | -48.0577 | 2026-07-10 00:00:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| fb7acba8-f982-38d1-a564-cc37ef614c4b | -4.3588 | -47.7636 | 2026-07-10 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 01a8ab5b-fa6f-32b7-9271-acb7a517afe3 | -12.4999 | -43.7858 | 2026-07-10 00:00:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| c2c62e50-218d-3663-900e-5b9d97432968 | -23.6225 | -53.0041 | 2026-07-10 00:00:00 | GOES-19 | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 63.3 |
| b8ec5d15-135b-369e-9cd8-0bbac9c8c457 | -4.3402 | -47.7645 | 2026-07-10 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 4e1a1c42-c2d7-30f6-b760-be901d383283 | -12.5003 | -43.7621 | 2026-07-10 00:00:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 4f34899e-d3ea-3f00-a74a-63fc77ad0b2b | -13.3122 | -43.7179 | 2026-07-10 00:00:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 12b703dc-0b0b-3848-9ccd-67c8cd67a2bd | -18.0182 | -54.371 | 2026-07-10 00:00:00 | GOES-19 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 071c4a98-1a37-3843-b4f4-36c5f4ae4f8d | -12.3561 | -47.413 | 2026-07-10 00:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 823cb4a3-ddf2-31dc-be01-48ffa9030a7e | -18.0186 | -54.3497 | 2026-07-10 00:00:00 | GOES-19 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 52.1 |
| cf1bf233-fe82-3bc8-a27d-d0cf1275928a | -23.6014 | -53.0085 | 2026-07-10 00:10:00 | GOES-19 | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 97.4 |
| 45a2a2da-bd99-3c43-b270-8368e7dfdb76 | -13.3122 | -43.7179 | 2026-07-10 00:10:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| a1b5f81f-fa24-3111-9fec-d2f1e7ef5479 | -4.3402 | -47.7645 | 2026-07-10 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 6a2dcb5f-5e12-36ab-90cf-48c45a694471 | -23.6225 | -53.0041 | 2026-07-10 00:10:00 | GOES-19 | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 105.6 |
| 4daca3d8-3a0a-36c6-a63a-be8c3cc45a1a | -12.3561 | -47.413 | 2026-07-10 00:10:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 234c024b-ddf2-336d-ab46-04f9a32a9dba | -10.1478 | -50.167 | 2026-07-10 00:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| daf45908-5154-374f-9589-a3e2841445e6 | -18.0182 | -54.371 | 2026-07-10 00:10:00 | GOES-19 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 6de5fca9-8a36-3cec-bc0f-7cb751b46746 | -12.5003 | -43.7621 | 2026-07-10 00:10:00 | GOES-19 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 52a7c06b-4224-3592-875d-e3bc3d10cb16 | -8.4987 | -48.0594 | 2026-07-10 00:10:00 | GOES-19 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 82731336-af8c-3ba6-8877-014f174353c1 | -4.7742 | -41.796101 | 2026-07-10 00:13:00 | METOP-C | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a79259aa-cb2c-3a41-ad57-3fbe4dc5a86b | -8.032 | -47.424301 | 2026-07-10 00:13:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b397c136-a781-3240-9dbe-7436af1b8b95 | -8.4938 | -48.067001 | 2026-07-10 00:13:00 | METOP-C | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 42c89527-2068-37d8-b892-5454a589630c | -9.5982 | -40.347 | 2026-07-10 00:13:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 71dbeffd-e2ae-37a2-9d22-147c415e5c6e | -10.1408 | -50.1731 | 2026-07-10 00:13:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a8325ed5-8c3d-312e-939d-03865d97ce4b | -9.4541 | -38.914101 | 2026-07-10 00:13:00 | METOP-C | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f151ec85-c03a-365a-b7b4-419c7894bc1f | -10.6031 | -46.561298 | 2026-07-10 00:13:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 01bb8a90-edc7-3525-b6e9-929bf8a9e435 | -10.6005 | -46.549 | 2026-07-10 00:13:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7e9bb40a-64ba-35b0-92a0-287d34ba2fcd | -12.4409 | -49.570999 | 2026-07-10 00:13:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1a13e7e6-8b8a-3cf4-aeb3-017729d786c5 | -6.4971 | -42.212502 | 2026-07-10 00:13:00 | METOP-C | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4b1b021b-ca30-3445-a264-f9e610c5fca1 | -8.7184 | -47.827599 | 2026-07-10 00:13:00 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e9f53dd9-5415-3851-9146-8ef4fcef6d13 | -4.1599 | -43.082401 | 2026-07-10 00:13:00 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 15153caa-0b83-3ff2-9533-ef2488942fa7 | -20.211901 | -41.243 | 2026-07-10 00:13:00 | METOP-C | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4405d93a-2413-3d43-9a68-d7e20599c549 | -9.3646 | -40.407501 | 2026-07-10 00:13:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| fc310983-3549-3986-9f8d-c3f30082d527 | -10.1463 | -50.1497 | 2026-07-10 00:13:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0bf8dbf0-f78e-3da7-be48-6be93ed3525b | -10.1311 | -50.174999 | 2026-07-10 00:13:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e08cfa68-7b76-319a-bf33-ddb8f6e7f3d1 | -12.4981 | -43.7589 | 2026-07-10 00:13:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| db4b0ea5-8a83-375f-8c0f-9069dc1822a6 | -10.8469 | -45.0453 | 2026-07-10 00:13:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 98f8f7b4-3a4d-392e-9e4f-f697874108e8 | -10.85 | -44.433899 | 2026-07-10 00:13:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ca7bcc6a-ae52-3d50-9c93-e59b482f4978 | -10.8638 | -44.450298 | 2026-07-10 00:13:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cb3280cf-0755-3042-86e9-348278940c0e | -5.4692 | -45.431099 | 2026-07-10 00:13:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 48cf4f4d-d27c-32b6-8355-dc163b5b332d | -8.4908 | -48.052601 | 2026-07-10 00:13:00 | METOP-C | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2ae8d0d7-5c9e-3bad-9d66-ae2b4a6faef2 | -12.7001 | -45.4636 | 2026-07-10 00:13:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 19019d0f-139c-351f-96ef-380c78cb9ad0 | -9.5998 | -40.353901 | 2026-07-10 00:13:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 595aa413-4ed1-398e-a6bc-844376cc5616 | -11.8357 | -48.2295 | 2026-07-10 00:13:00 | METOP-C | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 89aec0b4-ab2d-303c-a0e7-d044d8708439 | -12.5 | -43.767799 | 2026-07-10 00:13:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 221e9bde-ff7b-3f97-a011-57c8199ef886 | -4.3338 | -47.757 | 2026-07-10 00:13:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49e359f6-0f0e-346b-9b46-ddc1e0ddaa23 | -4.7726 | -41.789299 | 2026-07-10 00:13:00 | METOP-C | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0f6352e9-9a29-344f-985b-d33f3ef3f298 | -12.3473 | -47.389198 | 2026-07-10 00:13:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d857f99a-575f-3eee-b099-5d55aee18b48 | -13.306 | -43.707802 | 2026-07-10 00:13:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 06ffe12a-bc62-3b28-8421-f4d15bc2308c | -9.3677 | -40.421398 | 2026-07-10 00:13:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4c40cc94-9781-35c4-a650-12990f225e07 | -8.0293 | -47.4114 | 2026-07-10 00:13:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 30825f6a-08fb-3462-9d18-4726e44e5383 | -8.5006 | -48.050598 | 2026-07-10 00:13:00 | METOP-C | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7c5ecac0-68a5-3674-85e8-fc557b62c724 | -10.852 | -44.443199 | 2026-07-10 00:13:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9c15153e-74d3-3e7b-b0a8-a90a4993047d | -5.7452 | -43.261799 | 2026-07-10 00:13:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8cfbc895-ad99-32e4-bf6f-49457f961f51 | -20.2136 | -41.251499 | 2026-07-10 00:13:00 | METOP-C | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fdd919c2-28a9-388e-a7f2-0d9dbc084190 | -5.4672 | -45.422298 | 2026-07-10 00:13:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0d32ab83-742d-3a2a-a249-5f3cbd71788c | -8.1281 | -47.877399 | 2026-07-10 00:13:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3f1ddcaa-dd23-3e50-9cde-15901992e80c | -10.8598 | -44.431801 | 2026-07-10 00:13:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2ba38486-6ebe-3756-a45e-ae8a085a1448 | -10.1366 | -50.151699 | 2026-07-10 00:13:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 09e3b966-d673-349a-8f29-004b89a76d0f | -4.3461 | -47.766701 | 2026-07-10 00:13:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a24e951-ad18-3038-986e-d96f9d02fc01 | -12.3533 | -47.419102 | 2026-07-10 00:13:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0d7a866e-343c-3094-816f-9a11a900749c | -5.7468 | -43.269001 | 2026-07-10 00:13:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cb3a9ce1-0042-3475-aba4-144a737c1e28 | -4.1517 | -43.091499 | 2026-07-10 00:13:00 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b3574338-0262-31ef-a456-6ee40f80672f | -4.1615 | -43.089401 | 2026-07-10 00:13:00 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 30e99c5e-44c9-36f8-b796-0493b596d8eb | -13.308 | -43.7169 | 2026-07-10 00:13:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1d065f9c-13d3-3ab1-95f9-094e96354709 | -4.3364 | -47.768799 | 2026-07-10 00:13:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b0e5b64-bd38-31b3-be31-57e1f8e8860b | -7.088 | -44.347801 | 2026-07-10 00:13:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8f0281ca-3c03-34e3-87a4-0ac151315596 | -10.1269 | -50.153599 | 2026-07-10 00:13:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 377b9da5-7abb-382e-820c-b58634aadcab | -9.3662 | -40.414501 | 2026-07-10 00:13:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9c610377-89f6-3bee-91fb-c7910541e43d | -12.4506 | -49.569099 | 2026-07-10 00:13:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1973dcfd-1cea-381a-9ae6-040b6117973b | -10.8448 | -45.0354 | 2026-07-10 00:13:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a079ae66-dc80-3cf4-95f6-a4872100fb40 | -12.4902 | -43.769901 | 2026-07-10 00:13:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 787da6d4-4618-306d-a6bd-d512578841bc | -9.4524 | -38.9067 | 2026-07-10 00:13:00 | METOP-C | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9e5a7cea-459e-3279-8606-3bd4444b068f | -8.1252 | -47.863602 | 2026-07-10 00:13:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 67810077-4fb6-334b-82a0-5f60d26b0c24 | -6.5069 | -42.2103 | 2026-07-10 00:13:00 | METOP-C | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a93852a7-b6de-3330-b271-c19c62766742 | -12.3406 | -47.406101 | 2026-07-10 00:13:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 706e1515-9906-35e0-9f69-41390cfb9c8a | -10.8618 | -44.441101 | 2026-07-10 00:13:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d18f1fd1-983f-33b5-954c-8115284cd3f3 | -12.5019 | -43.776699 | 2026-07-10 00:13:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f30dfdbe-971c-3c81-9504-383c6b3db2a1 | -10.142 | -50.128399 | 2026-07-10 00:13:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a4e4dd19-d5b8-34e1-9d05-86b55296bf58 | -4.3435 | -47.754902 | 2026-07-10 00:13:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3371129f-2df8-3b2b-85ba-49f4db699d0e | -12.8483 | -44.354198 | 2026-07-10 00:13:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d0dc2b11-def9-3d4d-9e83-a30202e0e336 | -10.1214 | -50.176899 | 2026-07-10 00:13:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c7229281-a707-3126-818a-af021f9ca740 | -12.3435 | -47.421101 | 2026-07-10 00:13:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6a351165-0e5a-3246-8952-df2d2b75a882 | -7.0862 | -44.339699 | 2026-07-10 00:13:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d7bd6ca7-a0f0-328c-b0a5-777d40338e23 | -12.4921 | -43.778801 | 2026-07-10 00:13:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0bd92a6e-dc03-33ac-bff8-60fcd76dbba2 | -12.4883 | -43.761002 | 2026-07-10 00:13:00 | METOP-C | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1f0f5f8f-a189-357b-bf66-1e5d0940c306 | -12.3503 | -47.404099 | 2026-07-10 00:13:00 | METOP-C | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 66176be0-e198-391d-8fc0-4022f795538c | -8.5036 | -48.064999 | 2026-07-10 00:13:00 | METOP-C | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d5635a8e-6ba6-3e42-8fa3-1744cdbd75dc | -13.3099 | -43.725899 | 2026-07-10 00:13:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| edd2e9c1-1b51-3d17-adb5-9c742e6d4e57 | -17.53308 | -54.0019 | 2026-07-10 00:18:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 576613f4-b7fe-374c-b552-56208ec71489 | -23.61745 | -53.02641 | 2026-07-10 00:18:00 | TERRA_M-M | CRUZEIRO DO OESTE | PARANÁ | Brasil | 4106605 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.5 |
| ac64b56c-429f-3522-94e3-6179b0db8dd1 | -17.54335 | -54.00055 | 2026-07-10 00:18:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 577161aa-4e90-3b46-b5fc-248768f5787a | -16.83325 | -46.31708 | 2026-07-10 00:18:00 | TERRA_M-M | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 15.6 |
| a52811fd-266e-3159-a5db-8a54235c1315 | -23.60699 | -53.02794 | 2026-07-10 00:18:00 | TERRA_M-M | CRUZEIRO DO OESTE | PARANÁ | Brasil | 4106605 | 41 | 33 | nan | nan | nan | Mata Atlântica | 19.1 |
| 5adf433e-f900-329b-9510-9bc075821d89 | -20.70544 | -50.52197 | 2026-07-10 00:18:00 | TERRA_M-M | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.6 |
| 273a65f4-84f8-33b5-9340-3d8ace19fa1d | -22.91881 | -49.20229 | 2026-07-10 00:18:00 | TERRA_M-M | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 8.7 |
| b40bb557-d18a-332a-a582-02d98af31178 | -23.56158 | -47.50461 | 2026-07-10 00:18:00 | TERRA_M-M | SOROCABA | SÃO PAULO | Brasil | 3552205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 2fb55a4b-d1ef-3dea-b6bc-1a273b74c09e | -19.59396 | -47.61094 | 2026-07-10 00:18:00 | TERRA_M-M | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 513e795d-faab-3351-8c60-c7cab30ccc80 | -23.61592 | -53.01291 | 2026-07-10 00:18:00 | TERRA_M-M | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 85.8 |


[Clique aqui para ver as próximas entradas](README2.md)
