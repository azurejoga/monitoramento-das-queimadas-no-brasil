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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75023807-d750-35ab-a088-b9dd13bda91e | -15.96431 | -40.51667 | 2026-10-01 15:26:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 34.4 |
| e23f119a-479a-3705-b6a8-c1b8dc945121 | -17.67022 | -39.22655 | 2026-10-01 15:26:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| d7f7dcb4-9ace-3624-bbf3-66e490454ac0 | -15.68675 | -40.58982 | 2026-10-01 15:26:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 9d5388e8-42a6-3f8a-83f5-5321856cc490 | -15.6842 | -40.5899 | 2026-10-01 15:26:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| c05f138e-ea34-3718-b911-0244c0599a6f | -18.34367 | -40.05282 | 2026-10-01 15:26:00 | NOAA-20 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 33.9 |
| b92087b3-f33f-35d9-9aac-2d1dc3f27d77 | -15.90841 | -38.94104 | 2026-10-01 15:26:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 1880ddff-c57c-3154-a704-187bee510b46 | -18.34132 | -40.06025 | 2026-10-01 15:26:00 | NOAA-20 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| b3efd506-8531-3d73-9dc2-d629e52e1a27 | -15.9617 | -40.52186 | 2026-10-01 15:26:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 51.0 |
| 69598c2e-74c1-39e6-a2e4-3a98a20f06f5 | -16.86948 | -39.25727 | 2026-10-01 15:26:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| ee52a850-8d8b-3e78-ba20-b00b9b7fda08 | -18.34849 | -40.05964 | 2026-10-01 15:26:00 | NOAA-20 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| ed50a828-f22e-3626-b806-66084d1edae1 | -17.66856 | -39.22758 | 2026-10-01 15:26:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 254397d6-e4b3-35fa-9eb5-672746692391 | -13.67247 | -40.55726 | 2026-10-01 15:29:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| af620671-454e-3da1-aa03-9ba7895f7f23 | -8.68711 | -36.73841 | 2026-10-01 15:29:00 | NOAA-20 | VENTUROSA | PERNAMBUCO | Brasil | 2616001 | 26 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 993428c4-d692-32b1-bb8a-ee3a0c990985 | -8.49727 | -36.88319 | 2026-10-01 15:29:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 5.8 |
| dd71aa64-1ddc-39ec-b446-167e352cb79c | -14.97714 | -40.27962 | 2026-10-01 15:29:00 | NOAA-20 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| ebf17ee0-04ea-3736-8abf-9281a5a06ab4 | -14.31092 | -40.2482 | 2026-10-01 15:29:00 | NOAA-20 | BOA NOVA | BAHIA | Brasil | 2903706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.3 |
| bb272671-4cc2-3ba7-83f2-eca6a5d50cb9 | -14.53407 | -40.84964 | 2026-10-01 15:29:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 2d9011f9-f4d5-3cdc-a5fd-d87bfd94c600 | -9.38476 | -38.82232 | 2026-10-01 15:29:00 | NOAA-20 | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 2185bfdc-44d1-3226-a0ee-7979cc6b7b6f | -12.18296 | -40.98792 | 2026-10-01 15:29:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 85a43471-487b-304c-9613-10c878c5b4fb | -13.63134 | -40.01536 | 2026-10-01 15:29:00 | NOAA-20 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 8666780e-65fe-36c8-a78a-f5316f7e878e | -10.68946 | -40.84552 | 2026-10-01 15:29:00 | NOAA-20 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 21.1 |
| f5f39a94-393e-3dbb-97d9-948bf5126d33 | -8.01966 | -40.37017 | 2026-10-01 15:29:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 86b6e8d3-1315-3ce8-9cbd-2fd5392eeeb2 | -8.10815 | -39.59406 | 2026-10-01 15:29:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 9ebf2e89-0421-3af9-baef-76c8204f0955 | -12.75458 | -40.40343 | 2026-10-01 15:29:00 | NOAA-20 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 493a2d0d-ec44-3ba9-b2a2-996ed7f80d29 | -9.87458 | -37.52173 | 2026-10-01 15:29:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 84b4145c-de3d-3a70-aa33-3131bd224c03 | -8.42882 | -39.84848 | 2026-10-01 15:29:00 | NOAA-20 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 33b8ee65-7c0e-3f11-955b-1cf0f2942108 | -9.3906 | -37.81711 | 2026-10-01 15:29:00 | NOAA-20 | OLHO D'ÁGUA DO CASADO | ALAGOAS | Brasil | 2705804 | 27 | 33 | nan | nan | nan | Caatinga | 6.4 |
| b309bb5d-d16e-3ee6-9769-542ffca0a24e | -11.97853 | -39.48121 | 2026-10-01 15:29:00 | NOAA-20 | RIACHÃO DO JACUÍPE | BAHIA | Brasil | 2926301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 3c4892e1-7853-35db-9ba4-02fbf544e105 | -10.39203 | -37.70638 | 2026-10-01 15:29:00 | NOAA-20 | CARIRA | SERGIPE | Brasil | 2801405 | 28 | 33 | nan | nan | nan | Caatinga | 3.0 |
| cddb144a-c961-3130-ac38-9bc16493a1af | -7.79641 | -37.12218 | 2026-10-01 15:29:00 | NOAA-20 | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 21ad54d9-e402-3ef7-9d07-df6b9b59fe11 | -13.6294 | -40.01451 | 2026-10-01 15:29:00 | NOAA-20 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| ee967c11-ca23-3249-a21a-d2bd3550d5cf | -3.81138 | -38.67982 | 2026-10-01 15:29:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| f2c327f6-ddb1-32e8-9a6a-5230ca729708 | -8.28596 | -37.64362 | 2026-10-01 15:29:00 | NOAA-20 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 5fdc0d4a-fc42-3f47-a452-e98f7cd5f4a4 | -3.70585 | -40.43751 | 2026-10-01 15:29:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| c59a61ea-35c5-397c-bda0-b324b3260f65 | -5.23187 | -40.5708 | 2026-10-01 15:29:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| cff436e6-6e65-3e88-817e-bad8b6614f2f | -13.65912 | -39.19217 | 2026-10-01 15:29:00 | NOAA-20 | NILO PEÇANHA | BAHIA | Brasil | 2922607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 8e6bcd05-8ac5-3838-8620-0615aabd87a4 | -9.53311 | -37.74163 | 2026-10-01 15:29:00 | NOAA-20 | PIRANHAS | ALAGOAS | Brasil | 2707107 | 27 | 33 | nan | nan | nan | Caatinga | 5.0 |
| ce2857f6-1ed2-3947-89e4-69f469796874 | -12.4085 | -39.08101 | 2026-10-01 15:29:00 | NOAA-20 | ANTÔNIO CARDOSO | BAHIA | Brasil | 2901700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| eeb35be4-7331-3e27-8399-c474e966ad27 | -8.86724 | -38.00193 | 2026-10-01 15:29:00 | NOAA-20 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 10a173ac-ec05-33e0-ac8f-8214038a1eef | -8.71802 | -36.85509 | 2026-10-01 15:29:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 3.4 |
| c0955d06-042b-36ee-8577-e073cc6c42d9 | -12.69944 | -40.54055 | 2026-10-01 15:29:00 | NOAA-20 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 38c9f67c-a639-321d-ac53-b93be89484a1 | -14.12004 | -40.01686 | 2026-10-01 15:29:00 | NOAA-20 | ITAGI | BAHIA | Brasil | 2915106 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 4f8f781d-8bb5-3759-85c2-4da05142dc9e | -11.18254 | -40.56675 | 2026-10-01 15:29:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 17.6 |
| b42e1fc5-8178-33f7-a184-6523cb6336a6 | -3.69007 | -42.1955 | 2026-10-01 15:29:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| c21cfae4-3833-323a-afa2-79d86fa7da03 | -9.98601 | -37.37933 | 2026-10-01 15:29:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1560f3c5-48ed-35cf-a995-d9fd4be532af | -14.30347 | -40.51585 | 2026-10-01 15:29:00 | NOAA-20 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 5e270980-90f3-3dd2-b1f5-c50c83d64c9a | -9.38421 | -38.81778 | 2026-10-01 15:29:00 | NOAA-20 | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 6.4 |
| d0251654-31db-3fbb-a99d-f6ff11fd780c | -14.77329 | -40.33486 | 2026-10-01 15:29:00 | NOAA-20 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| c70483e2-eee5-399f-9b7b-0dd3aa4a580a | -13.45216 | -40.38734 | 2026-10-01 15:29:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 744d28f5-8eb3-316b-8164-ae6cd38c7b32 | -7.66354 | -37.77977 | 2026-10-01 15:29:00 | NOAA-20 | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0d276b78-7084-3386-821a-4180194bf992 | -12.85342 | -40.67159 | 2026-10-01 15:29:00 | NOAA-20 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 42ca146d-d0a9-319d-b4b0-2917a067cf31 | -12.17452 | -39.76474 | 2026-10-01 15:29:00 | NOAA-20 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 232a6b41-44db-32e7-acd4-3fa4cca0ad83 | -8.28532 | -37.64499 | 2026-10-01 15:29:00 | NOAA-20 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 6.8 |
| c2680b17-8db3-37e4-931c-e6ba0e0203d8 | -11.33642 | -39.80622 | 2026-10-01 15:29:00 | NOAA-20 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f16b4256-6b6b-3ffb-b2bf-9783c1b81e9b | -3.16503 | -41.33685 | 2026-10-01 15:29:00 | NOAA-20 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 55883a5f-aee0-38c1-971e-1b6fcbfa322a | -3.51315 | -40.35827 | 2026-10-01 15:29:00 | NOAA-20 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 79eab526-457c-3b0c-ba1d-02fbee95bbbf | -11.1818 | -40.56041 | 2026-10-01 15:29:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 13.5 |
| f245d55b-f48d-316f-bf78-54c5c00b959b | -11.16278 | -38.41336 | 2026-10-01 15:29:00 | NOAA-20 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| feb9908b-f636-3367-99c7-1efe5527229b | -12.67785 | -38.80494 | 2026-10-01 15:29:00 | NOAA-20 | SANTO AMARO | BAHIA | Brasil | 2928604 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 3eafd9ed-db96-34f9-9790-d87a244517fc | -9.74327 | -38.32829 | 2026-10-01 15:29:00 | NOAA-20 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1aa4e14f-d9df-3c51-85c2-41737ccaf850 | -9.73185 | -39.6818 | 2026-10-01 15:29:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0abf50b0-f0f1-32fe-9e89-2a42cb198952 | -10.18955 | -38.06772 | 2026-10-01 15:29:00 | NOAA-20 | CORONEL JOÃO SÁ | BAHIA | Brasil | 2909208 | 29 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 6dd5a9c2-ce6f-3692-999e-f23e11ab67b7 | -3.6893 | -42.19389 | 2026-10-01 15:29:00 | NOAA-20 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 236bfae9-7167-3ade-9b3b-7e2a35cc1175 | -13.51608 | -40.82153 | 2026-10-01 15:29:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| b6d6bad0-bb32-3395-af2d-96240035a40f | -11.5807 | -38.10504 | 2026-10-01 15:29:00 | NOAA-20 | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 1ae49914-2581-3972-a58c-7017c005cc86 | -8.2855 | -37.64006 | 2026-10-01 15:29:00 | NOAA-20 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 8.4 |
| db692a98-a965-3fce-9273-6060a71924e8 | -9.41853 | -36.94158 | 2026-10-01 15:29:00 | NOAA-20 | CACIMBINHAS | ALAGOAS | Brasil | 2701209 | 27 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 67ba7fc8-45bf-372c-be24-5a2e96358015 | -3.48841 | -42.16535 | 2026-10-01 15:29:00 | NOAA-20 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| a5bfe004-b327-353e-8324-f8e8267e0071 | -3.81146 | -38.67996 | 2026-10-01 15:29:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| bc77f3a5-7940-3247-bfcf-424bd63f25fc | -8.73561 | -36.8266 | 2026-10-01 15:29:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 6efc6d2b-7604-31d3-b7a8-f6c3df6f91de | -14.37787 | -40.35463 | 2026-10-01 15:29:00 | NOAA-20 | BOA NOVA | BAHIA | Brasil | 2903706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| bb376085-9690-39d3-8baa-cc8e39abe562 | -10.15782 | -39.18036 | 2026-10-01 15:29:00 | NOAA-20 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b866d08f-cc0e-3c62-b479-02377ecadd6c | -10.91095 | -40.16414 | 2026-10-01 15:29:00 | NOAA-20 | PONTO NOVO | BAHIA | Brasil | 2925253 | 29 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 1929e92b-83e3-3e0e-b1c7-52b682b7c5d4 | -10.2938 | -40.01775 | 2026-10-01 15:29:00 | NOAA-20 | ANDORINHA | BAHIA | Brasil | 2901353 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0f4f972e-ec8f-3a0a-b1b5-b525f6048559 | -13.65895 | -39.19129 | 2026-10-01 15:29:00 | NOAA-20 | NILO PEÇANHA | BAHIA | Brasil | 2922607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| a5e2bbcc-3c9c-337c-88ed-287d534cdcf4 | -8.15357 | -36.66475 | 2026-10-01 15:29:00 | NOAA-20 | JATAÚBA | PERNAMBUCO | Brasil | 2608008 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 87645728-eb10-3545-80c2-14207aeb4a67 | -3.34306 | -42.61847 | 2026-10-01 15:29:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b92eb4bc-735a-3179-a263-6ea9602e6d27 | -14.5334 | -40.84231 | 2026-10-01 15:29:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 48c4bad6-4f23-3d1a-be34-e0fea2444ae8 | -10.33685 | -39.49125 | 2026-10-01 15:29:00 | NOAA-20 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| efeec8a5-b42a-3733-855e-ed0beac6bef0 | -10.69056 | -40.85292 | 2026-10-01 15:29:00 | NOAA-20 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 36.5 |
| e21a8131-eace-3200-8fc5-dbfe6b20f2e7 | -11.97845 | -39.48331 | 2026-10-01 15:29:00 | NOAA-20 | RIACHÃO DO JACUÍPE | BAHIA | Brasil | 2926301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8362d5cf-0443-3cb6-90e6-09f744eba4d0 | -10.33471 | -39.49385 | 2026-10-01 15:29:00 | NOAA-20 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| a4af047f-9ddd-37a8-8b67-cac651c5b46b | -8.01897 | -40.36472 | 2026-10-01 15:29:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 475c6aba-24b6-3d15-b8de-458e25742141 | -14.31168 | -40.25136 | 2026-10-01 15:29:00 | NOAA-20 | BOA NOVA | BAHIA | Brasil | 2903706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 604a2d59-9a5a-3c43-9a44-af11bedd7b5b | -12.75525 | -40.40949 | 2026-10-01 15:29:00 | NOAA-20 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 12.5 |
| b7e05004-e626-3aab-ad5a-e613c2c66d4f | -14.2228 | -40.7934 | 2026-10-01 15:29:00 | NOAA-20 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 88c48b01-e0c5-302d-a84a-9aa6e5086810 | -8.30593 | -39.38134 | 2026-10-01 15:29:00 | NOAA-20 | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 6edb1fc7-bc10-3f85-9f5e-9295330bdd3e | -9.82858 | -37.24115 | 2026-10-01 15:29:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 61173308-c9b0-3412-9487-31d343226303 | -13.53519 | -40.72499 | 2026-10-01 15:29:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| ace4e210-806e-3d50-a29e-e8fbfbc2453a | -12.75517 | -40.40862 | 2026-10-01 15:29:00 | NOAA-20 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 196db156-f50a-3447-8e06-2ecfabf5d749 | -14.53124 | -40.84792 | 2026-10-01 15:29:00 | NOAA-20 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 457bc7ca-a3a1-3f71-b52b-c98a7d569cfe | -11.79682 | -40.92324 | 2026-10-01 15:29:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0e2befe7-710a-3a5c-aad1-f59e49e1507f | -14.49649 | -40.64122 | 2026-10-01 15:29:00 | NOAA-20 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 1ba7821c-721b-3a3e-9915-980cb1420ab8 | -3.34124 | -42.6179 | 2026-10-01 15:29:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 20fff5fd-33a8-3469-b985-cec7f1fda554 | -7.72771 | -37.67622 | 2026-10-01 15:29:00 | NOAA-20 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 42915d5f-cde7-357d-ac74-b5294887c305 | -10.85165 | -40.49444 | 2026-10-01 15:29:00 | NOAA-20 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 36f02cd1-413a-3d4f-949e-1a027b6cc799 | -8.10754 | -39.58914 | 2026-10-01 15:29:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 10.5 |
| ae69193f-5e47-35e4-97f7-9a264898c238 | -14.31175 | -40.25668 | 2026-10-01 15:29:00 | NOAA-20 | BOA NOVA | BAHIA | Brasil | 2903706 | 29 | 33 | nan | nan | nan | Mata Atlântica | 25.6 |
| d6e4cfc4-5da6-336b-a015-d3883f967498 | -7.56079 | -38.4946 | 2026-10-01 15:29:00 | NOAA-20 | CONCEIÇÃO | PARAÍBA | Brasil | 2504405 | 25 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 62b70586-2dd6-3d4b-bccf-0fc5c5b63d3c | -10.84667 | -40.49495 | 2026-10-01 15:29:00 | NOAA-20 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |


[Clique aqui para ver as próximas entradas](README106.md)
