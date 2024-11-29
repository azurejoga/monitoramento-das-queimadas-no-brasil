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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80b10066-5e98-3f0e-aecc-ffef8e1382e1 | -4.85539 | -41.26411 | 2024-11-29 03:17:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 475e4eea-9d2e-349b-9304-b38935f0e254 | -4.85515 | -41.25534 | 2024-11-29 03:17:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 2b8df3f5-9bff-3c36-a263-6ad369d2dc5d | -4.86625 | -41.26905 | 2024-11-29 03:17:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| e1152bb7-3812-3246-90ff-c5df3e713374 | -4.86107 | -41.27048 | 2024-11-29 03:17:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 14033cb6-34dc-3d7f-b94e-1f666f22b475 | -7.02142 | -39.37286 | 2024-11-29 03:17:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 33fea806-ee81-3292-b58a-c3c4e4195c8d | -7.02214 | -39.36895 | 2024-11-29 03:17:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0f9738fe-e2f9-33d8-ae2d-1a5d3dc6504c | -4.6636 | -42.38178 | 2024-11-29 03:17:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| a8fc0eb6-4175-3258-a354-3df1457a8f7a | -6.85907 | -39.43404 | 2024-11-29 03:17:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7c4191cc-021e-327f-80f6-d14e0f45c8d0 | -6.90397 | -39.42397 | 2024-11-29 03:17:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 199015d7-6784-3a38-8935-069239f047d0 | -6.90765 | -39.4252 | 2024-11-29 03:17:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 66ab4c2a-f657-381e-b5bb-91afed11f45c | -5.48157 | -42.07359 | 2024-11-29 03:17:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 361b01e2-0791-31e9-9eac-4cc830ed5422 | -7.01922 | -39.36958 | 2024-11-29 03:17:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1d583056-09c3-3be1-bb5c-724c6545d218 | -4.86542 | -41.27362 | 2024-11-29 03:17:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 03fe2929-e89c-3cf6-89fa-821f322f4081 | -4.87173 | -41.27631 | 2024-11-29 03:17:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 12.1 |
| cba4018e-431e-38e0-a88e-d55d50e3062d | -6.82489 | -35.06851 | 2024-11-29 03:17:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 70debe45-5a3c-32d1-b1e3-98cba1820050 | -4.66505 | -42.38857 | 2024-11-29 03:17:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d7b2c8cd-3f57-3260-96dc-3bee612ee094 | -8.07491 | -34.97579 | 2024-11-29 03:17:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 37ca3d37-9ec4-3c3c-bddf-f49f232360e6 | -4.84967 | -41.25803 | 2024-11-29 03:17:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| fd95d261-ddbc-3aea-b5ab-d7328a1e9e6b | -5.85371 | -40.80532 | 2024-11-29 03:17:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 69d330fb-a248-3aeb-8cbb-95e86846d3ec | -5.1494 | -37.73993 | 2024-11-29 03:17:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0b4b941c-93b2-3833-b1d8-235117511b1d | -4.66627 | -42.38165 | 2024-11-29 03:17:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 2db5892f-84a4-36e0-b006-9a54f82df857 | -5.56111 | -35.52974 | 2024-11-29 03:17:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 332d6547-4069-31c6-b1c8-490d9ae785ba | -4.84192 | -41.26348 | 2024-11-29 03:17:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9f60f01e-5c2d-3f93-9302-f52ff36d2ace | -9.10695 | -43.10641 | 2024-11-29 03:19:00 | NOAA-21 | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 29d73f2c-0535-388e-bf67-df39ea4fbfcb | -12.05087 | -39.07286 | 2024-11-29 03:19:00 | NOAA-21 | TANQUINHO | BAHIA | Brasil | 2931103 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 889bd88f-2f56-3473-a412-e5699e7e345f | -7.98468 | -38.27634 | 2024-11-29 03:19:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 15858b63-9cc2-395d-ac2f-b256f3f3288f | -9.55177 | -35.84419 | 2024-11-29 03:19:00 | NOAA-21 | SATUBA | ALAGOAS | Brasil | 2708907 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 6e4f125e-7ae3-37f5-b3a7-a5944ad76d51 | -12.12781 | -38.17278 | 2024-11-29 03:19:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 9c4f19a6-293f-3886-a01d-3af2ec15e14a | -12.12438 | -39.40865 | 2024-11-29 03:19:00 | NOAA-21 | SERRA PRETA | BAHIA | Brasil | 2930402 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d73b362b-a7ba-3310-b587-dcc150e38766 | -9.5014 | -36.00524 | 2024-11-29 03:19:00 | NOAA-21 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cf0ad925-9394-3d2b-b270-b3e40af8b0dd | -9.44495 | -35.91028 | 2024-11-29 03:19:00 | NOAA-21 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 2ce210d1-6faa-37e7-a7b3-3f231bc13edd | -9.10824 | -43.10005 | 2024-11-29 03:19:00 | NOAA-21 | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 97c8a844-ea9b-3f89-bc23-c4754888d995 | -10.19421 | -36.34019 | 2024-11-29 03:19:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f7c3244b-8721-3424-9f0e-c89eeef693ae | -9.10785 | -43.09929 | 2024-11-29 03:19:00 | NOAA-21 | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| c83ba9ac-5d32-3b5b-9a66-49f0bec97439 | -10.20107 | -42.47764 | 2024-11-29 03:19:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3f42f5fb-e3ef-3bd5-b7ff-cec78b2fdfc0 | -10.66106 | -36.81967 | 2024-11-29 03:19:00 | NOAA-21 | PIRAMBU | SERGIPE | Brasil | 2805307 | 28 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 441f58eb-5c84-3230-89c2-39a217130e85 | -9.1066 | -43.1057 | 2024-11-29 03:19:00 | NOAA-21 | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| bb48f4a0-678f-3c9c-a89b-2af500c713eb | -7.91587 | -38.41612 | 2024-11-29 03:19:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4b102432-f669-3dd2-8936-ceec3cbe4f8c | -12.12876 | -38.16753 | 2024-11-29 03:19:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 6795b72d-b53f-3b47-9943-d710ee4f72ba | -12.05144 | -39.06979 | 2024-11-29 03:19:00 | NOAA-21 | TANQUINHO | BAHIA | Brasil | 2931103 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| de06c29a-aa53-3e2c-8bb3-40f10c1abd34 | -7.91529 | -38.41935 | 2024-11-29 03:19:00 | NOAA-21 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 478b316e-fe59-3686-bfea-155cc4a7648b | -9.72586 | -37.06193 | 2024-11-29 03:19:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 9ccaf554-c482-387f-b77f-484e75d3d910 | -7.69107 | -42.97588 | 2024-11-29 03:19:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| b81198b6-cceb-308c-b97a-6b4c31b46d50 | -8.90817 | -35.61755 | 2024-11-29 03:19:00 | NOAA-21 | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ed8c360d-2c8f-3ef3-9fb1-002b8c3f3e64 | -9.55676 | -35.84087 | 2024-11-29 03:19:00 | NOAA-21 | SATUBA | ALAGOAS | Brasil | 2708907 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 23f396ae-e602-3a24-a2c8-1c8d680c4a6c | -12.12801 | -38.16945 | 2024-11-29 03:19:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 702c7046-309d-3823-91ac-25292255d1db | -9.72478 | -37.05916 | 2024-11-29 03:19:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 5289feb0-69e2-3e11-8477-54ed960db545 | -2.6684 | -48.7767 | 2024-11-29 03:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 275.9 |
| 4655311a-6757-34bd-8223-40420ddc2b89 | -2.6498 | -48.7986 | 2024-11-29 03:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 149.8 |
| 8c3e80e9-5121-3351-b08b-98c27669def4 | -2.966 | -53.2824 | 2024-11-29 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 1f1533de-cc77-3983-b955-414200410168 | -4.2225 | -45.7634 | 2024-11-29 03:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 167.9 |
| fb737a1e-bc8c-3c6a-a7ac-3659c578e5e1 | -1.5869 | -53.8336 | 2024-11-29 03:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| c931e64c-83f2-3813-bc5e-0d993ff04074 | -4.2409 | -45.7848 | 2024-11-29 03:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 3c03f0d9-7196-3ffc-947e-38d44114feef | -2.966 | -53.3027 | 2024-11-29 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 097e0c46-4d14-34f4-a89e-aa7ecc93b6b8 | -2.9844 | -53.3022 | 2024-11-29 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 161.3 |
| e6c731ba-1ece-3168-9765-2e6cb4fa9bbf | -2.3419 | -46.8781 | 2024-11-29 03:20:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 125.1 |
| 19fe8e96-0222-3379-b08e-494af528820e | -2.6683 | -48.7981 | 2024-11-29 03:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 309.0 |
| 9d4b8c0c-919a-3a69-a5a9-12e0944cbfdc | -2.9844 | -53.2819 | 2024-11-29 03:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 272.5 |
| 0367b47d-d68c-3eeb-a3e8-e6c770e2de3c | -1.092 | -53.3954 | 2024-11-29 03:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 84e6acf8-fd7f-3094-8b6b-100c24bcb87a | -1.6997 | -52.4535 | 2024-11-29 03:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| d1021bee-b739-39b6-9fa8-c54758d76dfd | -4.2223 | -45.7858 | 2024-11-29 03:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 86.7 |
| a10b6e93-c5c7-394f-b9db-99180d14e284 | 1.8583 | -55.8216 | 2024-11-29 03:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 9d57a9ce-6f6d-3930-964e-fb37171bad28 | -4.4405 | -46.5754 | 2024-11-29 03:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 92.3 |
| 3da548c9-a7b7-309f-a32f-ab1bb177b073 | -2.6499 | -48.7772 | 2024-11-29 03:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 138.6 |
| 49d36962-d426-3616-b417-ee72bb409b29 | -17.5805 | -42.7483 | 2024-11-29 03:20:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 91.1 |
| ff1265b6-2e8f-3309-a260-93315792acb7 | -4.4404 | -46.5975 | 2024-11-29 03:20:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 20c911b6-285e-3aa3-b53a-054db762bca5 | 1.8399 | -55.8218 | 2024-11-29 03:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| ea0faffc-d7cf-3c19-ac3d-0bb652a8a27d | -2.3419 | -46.8562 | 2024-11-29 03:20:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| aab344db-a87e-30ca-a707-c94f28a163e6 | -4.2411 | -45.7625 | 2024-11-29 03:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 119.4 |
| aff13759-605e-395f-8197-1cad0de7be83 | -17.60007 | -42.73119 | 2024-11-29 03:21:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 15d94bab-7c40-3a33-8131-923dc5944559 | -17.58298 | -42.75442 | 2024-11-29 03:21:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 5dcd72c6-d272-39e0-9e3d-a129509a4218 | -17.57533 | -42.76179 | 2024-11-29 03:21:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 369a0a12-49e9-3bb8-b81c-e5f923805cb7 | -17.58113 | -42.76306 | 2024-11-29 03:21:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 3143c7e9-4b5d-3a1a-8dda-1688d6c9ea5f | -17.60597 | -42.73088 | 2024-11-29 03:21:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3a23f926-cebe-3748-85a5-42f2f7a35b3b | -19.48032 | -41.6128 | 2024-11-29 03:21:00 | NOAA-21 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 206c8c7d-6fd7-3462-9e20-342f5e98724d | -19.17661 | -40.13409 | 2024-11-29 03:21:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| c1d946a8-c2a1-32f8-94de-e1cf4adec159 | -19.47959 | -41.61631 | 2024-11-29 03:21:00 | NOAA-21 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| f21ab092-6195-305e-b285-8b33b1dcd954 | -19.17772 | -40.12862 | 2024-11-29 03:21:00 | NOAA-21 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 72af76fe-cc72-36a1-b24a-dbc573df578c | -17.62634 | -42.74852 | 2024-11-29 03:21:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 620b53b9-0d73-34f4-8fbf-de8f4a9839ed | -17.57627 | -42.75745 | 2024-11-29 03:21:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 26.6 |
| d4153ca6-cfbc-3f3e-90cf-27e3804fb923 | -17.6254 | -42.75282 | 2024-11-29 03:21:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f2283792-124e-396a-b77f-d00f229c8e46 | -21.18163 | -44.27523 | 2024-11-29 03:21:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| dd391db4-6b7e-3239-8ee1-7c9959bdb1e6 | -18.30954 | -42.19081 | 2024-11-29 03:21:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1b6b1dec-9f79-3695-b74b-4a77d1b583a1 | -17.62626 | -42.75046 | 2024-11-29 03:21:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b9cc9205-ac69-37df-b0b1-5bba64aa5218 | -17.60094 | -42.7271 | 2024-11-29 03:21:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bf0a7bcf-b807-3da1-b3c7-57dc3694d529 | -15.95769 | -38.91533 | 2024-11-29 03:21:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 2d8fe32b-105a-32a8-a264-222da7730048 | -15.96139 | -38.92145 | 2024-11-29 03:21:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| ba93976d-49d1-3c8e-a1ca-49a69b222d2a | -17.60507 | -42.73497 | 2024-11-29 03:21:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d2990a1d-7f38-30a1-a8bc-332ca1ae54b1 | -17.62533 | -42.75481 | 2024-11-29 03:21:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1aafdc47-aa84-36f8-bacb-925f5e00491f | -17.60582 | -42.73262 | 2024-11-29 03:21:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 83af1ebe-eae9-357f-82e5-116f015364fd | -15.953 | -38.91438 | 2024-11-29 03:21:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 49b052b1-afd0-3a61-9269-ee4e3b0cd113 | -15.96238 | -38.91629 | 2024-11-29 03:21:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 84fdbc28-cce1-35cd-af0a-ffaa2fde31f0 | -17.76347 | -42.22546 | 2024-11-29 03:21:00 | NOAA-21 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| a4f90754-d756-3688-9123-b361e40f0597 | -17.58207 | -42.75867 | 2024-11-29 03:21:00 | NOAA-21 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 8c54f89b-a814-3b31-97b5-980254698bd2 | -15.96608 | -38.92241 | 2024-11-29 03:21:00 | NOAA-21 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 872f14c0-b089-3013-bfdd-76beddd38edf | -2.6683 | -48.7981 | 2024-11-29 03:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 253.1 |
| 2999c63d-5daf-30e0-9b41-e24f611c43dc | -2.9844 | -53.3022 | 2024-11-29 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 153.0 |
| 0a296969-eb3a-397b-8edf-f7b31c3b54cc | -2.3419 | -46.8562 | 2024-11-29 03:30:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| a2089810-ec5f-3f8a-a6e9-9736c1cbe7ef | -2.3233 | -46.8786 | 2024-11-29 03:30:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 5d8b72b4-f61d-3100-8b68-61d2f1ae1991 | -2.966 | -53.3027 | 2024-11-29 03:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |


[Clique aqui para ver as próximas entradas](README17.md)
