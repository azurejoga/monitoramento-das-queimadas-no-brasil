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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d276b04-b0b8-3fdb-9e2a-0d7b1b8a1bf0 | -8.43102 | -35.29542 | 2024-11-28 00:09:00 | TERRA_M-M | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 20.7 |
| 50b9cca6-be98-31cb-a939-5c560de9e4d7 | -9.1161 | -35.37887 | 2024-11-28 00:09:00 | TERRA_M-M | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| 5babe13b-f1eb-3d6d-8b83-c42f5d908c1a | -9.17954 | -44.71873 | 2024-11-28 00:09:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 3ca14137-69d2-3106-abfc-ebbe88514d22 | -6.90177 | -38.10479 | 2024-11-28 00:09:00 | TERRA_M-M | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 907a2e69-77cd-378f-ab3c-a76bef94a69b | -7.69228 | -42.99201 | 2024-11-28 00:09:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 24.9 |
| a081b38b-1dff-36a0-920e-d6b0ffe5f48a | -7.69011 | -42.97475 | 2024-11-28 00:09:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 35.6 |
| 5d375dd5-9513-3728-bc8b-011698d4c75d | -8.49586 | -35.10703 | 2024-11-28 00:09:00 | TERRA_M-M | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 42.8 |
| a695be5f-0472-3a42-9251-ab822b771dd0 | -7.89976 | -36.0245 | 2024-11-28 00:09:00 | TERRA_M-M | TAQUARITINGA DO NORTE | PERNAMBUCO | Brasil | 2615003 | 26 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 7836b449-1ea1-3467-a738-2ed7af358433 | -9.6556 | -36.12752 | 2024-11-28 00:09:00 | TERRA_M-M | BOCA DA MATA | ALAGOAS | Brasil | 2701001 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| b0b34d47-cb04-3934-8f51-4d716e64e936 | -10.01546 | -36.46273 | 2024-11-28 00:09:00 | TERRA_M-M | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 280c4a8b-6424-34c8-a9c4-0323520c8da4 | -5.73441 | -35.69564 | 2024-11-28 00:09:00 | TERRA_M-M | SANTA MARIA | RIO GRANDE DO NORTE | Brasil | 2409332 | 24 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 8be7c0e2-a97f-3716-ba2b-89cfee3c4450 | -9.87278 | -36.23166 | 2024-11-28 00:09:00 | TERRA_M-M | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 35.7 |
| 79156b74-92d2-351b-9d6c-cc69cce228b7 | -5.98148 | -39.04155 | 2024-11-28 00:09:00 | TERRA_M-M | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 47c3539b-1182-3390-8356-010fef38f5eb | -9.83831 | -36.18116 | 2024-11-28 00:09:00 | TERRA_M-M | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 187.4 |
| da165d10-e211-357c-936d-0b213af6bf12 | -8.50522 | -35.10555 | 2024-11-28 00:09:00 | TERRA_M-M | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| ea24cc42-0c4b-3997-9b80-f4539b31ac9d | -9.1069 | -35.38025 | 2024-11-28 00:09:00 | TERRA_M-M | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| fc450b3c-ebd4-3c42-8128-c9e5c4f748d8 | -6.90623 | -42.47443 | 2024-11-28 00:09:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 24.1 |
| 771d21e7-ca40-361f-8bdd-c046371a335f | -9.00631 | -35.96729 | 2024-11-28 00:09:00 | TERRA_M-M | SÃO JOSÉ DA LAJE | ALAGOAS | Brasil | 2708303 | 27 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 6cc92487-a150-360d-ad6c-f1940354cf4c | -6.66161 | -39.23918 | 2024-11-28 00:09:00 | TERRA_M-M | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 25.0 |
| df433f09-621a-3cff-851c-00242823b534 | -8.43244 | -35.30526 | 2024-11-28 00:09:00 | TERRA_M-M | ESCADA | PERNAMBUCO | Brasil | 2605202 | 26 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| a3f7b5b8-81f1-3007-8df4-5c69cea01d89 | -7.43203 | -35.19546 | 2024-11-28 00:09:00 | TERRA_M-M | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 4ecd25e5-5548-3090-8e18-9818413af016 | -7.226 | -39.0559 | 2024-11-28 00:09:00 | TERRA_M-M | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| ef8858a8-7e27-3944-902c-0820267cd528 | -8.53966 | -35.21245 | 2024-11-28 00:09:00 | TERRA_M-M | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 26.8 |
| 7ddb4f67-cb3c-311e-aa64-bb7bf0a29599 | -7.70428 | -42.99031 | 2024-11-28 00:09:00 | TERRA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 13.7 |
| b0a3f8ee-4650-3069-b0e1-dda979b2b1e4 | -7.17731 | -35.10962 | 2024-11-28 00:09:00 | TERRA_M-M | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 44dbbdfc-a044-3128-b5d0-abe8adf75dd2 | -6.83581 | -44.39259 | 2024-11-28 00:09:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 38.7 |
| 5af57a50-5e3e-3673-80ee-898ed1165fe2 | -9.1756 | -44.72445 | 2024-11-28 00:09:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 1f39e5fc-9f06-3dcc-9eb3-825bc00c692e | -6.82654 | -44.40008 | 2024-11-28 00:09:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| 9d654cf2-b00f-3e55-a5e7-460fbf5ddaaf | -7.17579 | -35.09924 | 2024-11-28 00:09:00 | TERRA_M-M | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 27.4 |
| 396928c7-0421-3207-b2a7-a9bdc83658db | -10.09597 | -36.50891 | 2024-11-28 00:09:00 | TERRA_M-M | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 8.2 |
| b5e2607f-04cf-38ed-b153-d06ab0d5a321 | -10.09471 | -36.49995 | 2024-11-28 00:09:00 | TERRA_M-M | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 5.5 |
| b065c78d-6600-3806-937b-b6d189fac88a | -8.99939 | -35.59801 | 2024-11-28 00:09:00 | TERRA_M-M | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 6ef71188-cc70-3c0d-af19-3abb458340c0 | -9.86514 | -36.24206 | 2024-11-28 00:09:00 | TERRA_M-M | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 24.8 |
| de6e5b15-2f1b-3d22-8bd8-cab46e42e032 | -6.73367 | -35.02499 | 2024-11-28 00:09:00 | TERRA_M-M | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 17.5 |
| 8f0eb266-712c-3a08-b572-82ed4c12772a | -3.093 | -53.8045 | 2024-11-28 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 4185e232-89fe-3b3b-bc78-b169513aa796 | -3.6644 | -45.7676 | 2024-11-28 00:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 11bdbeff-af68-3be8-82ed-6425bd3c26e4 | -3.2406 | -53.6393 | 2024-11-28 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| e3fa861a-07c0-3c63-b426-2ae69e3fbe88 | -3.1114 | -53.8041 | 2024-11-28 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| cef6a4bd-6553-343f-a991-b2c0121cf079 | -1.3329 | -51.9463 | 2024-11-28 00:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| 1531b37e-2498-3c32-a219-d2fbb051c10c | -6.1039 | -43.9824 | 2024-11-28 00:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| acabad26-28a8-314e-a3a4-d0e9edcbff69 | -20.6907 | -49.111 | 2024-11-28 00:10:00 | GOES-16 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 8dc2f264-c282-380c-a578-6daf3961bcde | -6.1735 | -42.6221 | 2024-11-28 00:10:00 | GOES-16 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 107.0 |
| bef32d59-b64a-3833-95e5-16a645978af7 | -1.5898 | -52.2505 | 2024-11-28 00:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 401e9d4b-791f-3cfd-b642-3ff911e9a071 | -2.5963 | -53.9771 | 2024-11-28 00:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 5a1391f3-cd0b-3fdf-a1cf-5c0a139c339e | -2.7234 | -48.9034 | 2024-11-28 00:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 1d056f31-3120-3bf5-b39c-5a5ffe149304 | -3.1113 | -53.8242 | 2024-11-28 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 676980e7-e29d-3c37-ad7c-7f55e0d9d699 | -3.6963 | -43.4199 | 2024-11-28 00:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| d427d079-b33c-3926-ae45-782a0ba97ec7 | -3.6643 | -45.7899 | 2024-11-28 00:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 202.8 |
| c19b33d8-194c-3897-90cf-ced3d1a8d66e | -2.8347 | -54.1125 | 2024-11-28 00:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 43fb5714-0c3b-38f8-9957-3820928f2c00 | -6.1048 | -48.0327 | 2024-11-28 00:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 153.3 |
| 177f7cd5-a0fd-37b2-a15f-18e1396681a6 | -6.1737 | -42.5985 | 2024-11-28 00:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 65.4 |
| 6f7547ea-2254-3a4e-90ab-7a358f8c2bc3 | -3.3837 | -50.1125 | 2024-11-28 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 109.3 |
| ceac2fa4-562c-3775-ab31-21f75b964748 | -20.6702 | -49.1155 | 2024-11-28 00:10:00 | GOES-16 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 8f73edea-1434-3ea2-be2a-275365cd0733 | -6.1047 | -48.0544 | 2024-11-28 00:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 818b4fce-d923-3f0f-a649-2ce3cf7a3d99 | -3.4022 | -50.1119 | 2024-11-28 00:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 2c2815c0-e91f-3b94-b131-9bb1e2a9a667 | -6.0862 | -48.0339 | 2024-11-28 00:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 186.3 |
| 719f46b1-1866-3afa-a1b6-b85fd42390c8 | -1.5897 | -52.271 | 2024-11-28 00:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 577a95f6-a56a-34d9-901a-55ac13cba393 | -1.3145 | -51.9259 | 2024-11-28 00:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| ec7bf858-dfc2-3c64-bdba-4cfab59052e6 | -3.6829 | -45.7891 | 2024-11-28 00:10:00 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 117.1 |
| 66935721-d553-377d-bfe7-06ab17bc587e | -6.1041 | -43.9593 | 2024-11-28 00:10:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 159.7 |
| ba354f52-95da-3758-b34d-890222a88f75 | -3.9674 | -48.0851 | 2024-11-28 00:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 30.4 |
| 5100d807-0135-300a-9bf8-724de61fb1a4 | -18.764 | -55.8444 | 2024-11-28 00:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.7 |
| aaab3820-fa2a-38c2-8016-33baf593dc0e | -5.979 | -45.3395 | 2024-11-28 00:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 3a4a693f-daab-3285-b554-e205a507699c | -6.086 | -48.0557 | 2024-11-28 00:10:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 363ddb73-eea7-3765-8d0b-cb72dd5907da | -5.9788 | -45.3621 | 2024-11-28 00:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 189.6 |
| 8706d754-a65b-3eab-8eed-2dd6e1da9c52 | -1.3329 | -51.9257 | 2024-11-28 00:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 070b746c-b210-399e-b42a-44607aa833ad | 0.9857 | -50.1224 | 2024-11-28 00:10:00 | GOES-16 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 27.2 |
| f0e3b3f8-c637-349c-997f-41b63deeab92 | -6.1547 | -42.6237 | 2024-11-28 00:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 54.0 |
| 1c43bb3c-7bf9-3d3b-9249-bf87e0d5afcf | -5.9975 | -45.3607 | 2024-11-28 00:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| c2937842-55ab-3232-b91b-ba46a49621f1 | -4.1272 | -46.1253 | 2024-11-28 00:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 675bc450-c309-3db7-8c1d-af1026b675a7 | -18.784 | -55.8416 | 2024-11-28 00:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.1 |
| ba363243-f6e0-3ea3-8913-0fb5211b658c | -3.31667 | -46.37324 | 2024-11-28 00:11:00 | TERRA_M-M | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 2108faac-332b-3d4b-9b22-e2452699da90 | -5.97848 | -45.33979 | 2024-11-28 00:11:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 57.9 |
| a24d7a80-98c4-3739-9038-e4dabde9c0b7 | -4.15231 | -43.8264 | 2024-11-28 00:11:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 548cffdc-9c13-34f4-8a95-52cdbdbc07e3 | -6.58965 | -44.18658 | 2024-11-28 00:11:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 33763917-043b-3d8a-8670-b70dea09dd8c | -4.14998 | -43.80883 | 2024-11-28 00:11:00 | TERRA_M-M | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 450380e1-ea54-3905-9d3e-ccd7357f1ed9 | -2.84803 | -46.84057 | 2024-11-28 00:11:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 6e75fd5b-a571-3604-9a3b-0608ccad3af7 | -6.18939 | -44.4157 | 2024-11-28 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 6288f097-db1f-3e9b-832b-9a53b159220f | -6.09326 | -48.05107 | 2024-11-28 00:11:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 265.8 |
| 84f66f1a-16d4-3fa5-82db-b21b2ff1ff20 | -3.96479 | -48.10104 | 2024-11-28 00:11:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 3b5a935c-3f08-30fd-9707-998c9574e8c0 | -4.53125 | -44.61897 | 2024-11-28 00:11:00 | TERRA_M-M | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 6ed81561-e796-3da8-9d57-798726a55c9f | -2.62801 | -45.32688 | 2024-11-28 00:11:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 7cf5c651-d824-3b0b-b13b-ad23a1537456 | -3.69648 | -43.42162 | 2024-11-28 00:11:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 6b373d09-b0ea-34b6-ad62-bef80564a5cc | -3.68872 | -43.42828 | 2024-11-28 00:11:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 15c99391-c43a-3e0f-9425-0c3735fe9593 | -6.08983 | -48.00566 | 2024-11-28 00:11:00 | TERRA_M-M | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 6198e084-cca8-3cb4-9757-1b67c0836bd4 | -2.0109 | -46.39986 | 2024-11-28 00:11:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| fc24f8a2-da2f-35cc-9f2f-1e778505f8b6 | -5.97765 | -45.36987 | 2024-11-28 00:11:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 219.3 |
| 5eccafb0-6f51-3376-8e32-9f25a012604f | -4.65991 | -42.39749 | 2024-11-28 00:11:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 1042267b-468d-3fc4-9a25-b60f68185f2b | -3.24608 | -45.43222 | 2024-11-28 00:11:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 4b47b2af-ac69-3528-add3-3d8b456af111 | -2.86858 | -46.89145 | 2024-11-28 00:11:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 34.7 |
| ebb3d2a8-23b5-3db4-b8de-f36427f15f94 | -3.54272 | -40.37743 | 2024-11-28 00:11:00 | TERRA_M-M | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 5929c597-75ee-3c24-89a6-ad5ecc3d3d3d | -5.9487 | -39.66771 | 2024-11-28 00:11:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 5665c108-72d3-3e53-a11a-933b519fc9e9 | -2.50581 | -45.19838 | 2024-11-28 00:11:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 20.9 |
| ca037cb6-3bbd-3942-bf38-328f649cae9d | -2.86711 | -46.8672 | 2024-11-28 00:11:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 298.9 |
| 9da4936c-ed90-30e8-a87b-e85718208366 | -4.65801 | -42.38374 | 2024-11-28 00:11:00 | TERRA_M-M | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 77ce4109-60dc-3313-89b3-4720d17a4829 | -2.88232 | -46.86536 | 2024-11-28 00:11:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| c82c0f40-0ed7-314b-9ef3-1c7ba602c5dd | -4.76532 | -44.41158 | 2024-11-28 00:11:00 | TERRA_M-M | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 161.2 |
| 43e05857-4f49-30a5-9dfe-206a9f9bb4f1 | -3.71021 | -43.43582 | 2024-11-28 00:11:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 93.2 |
| 1ca5fddd-264d-3df1-9b03-0a0a1bd05514 | -1.44476 | -47.12754 | 2024-11-28 00:11:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| d84cbbd1-ca05-3d59-9a87-a0f9f8a215dd | -3.21931 | -45.64608 | 2024-11-28 00:11:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 22.2 |


[Clique aqui para ver as próximas entradas](README6.md)
