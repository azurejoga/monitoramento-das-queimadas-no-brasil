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

## Dados Diários - Página 185

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9dff7eef-39e2-33c7-bc6c-d5faca553b0c | -6.94672 | -45.27519 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c66af86e-0c88-343a-92b4-5048a48407e8 | -7.84462 | -45.52242 | 2026-10-07 16:37:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e445bc6b-6d90-30ce-b69f-d489a1735dd2 | -8.04263 | -45.61372 | 2026-10-07 16:37:00 | NPP-375 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 913d281d-71c1-30bf-967e-2bc2c40a4d96 | -7.34795 | -55.02016 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 66c15254-7c4a-387b-8642-af0d6e98efeb | -15.08823 | -41.44099 | 2026-10-07 16:37:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 6c89a8e0-d937-35ac-87b3-6a6ffc7160dd | -15.89212 | -42.85571 | 2026-10-07 16:37:00 | NPP-375 | SERRANÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3166956 | 31 | 33 | nan | nan | nan | Cerrado | 24.9 |
| f790429c-f0bc-38fe-a6fc-4f337ce5b915 | -6.32107 | -43.34295 | 2026-10-07 16:37:00 | NPP-375 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 55eddf1e-a942-3230-83b0-d15d8d6b8e38 | -3.40022 | -42.83585 | 2026-10-07 16:37:00 | NPP-375 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7c51bd7a-af34-3066-945d-fbad8aa4d2ee | -6.37507 | -42.90673 | 2026-10-07 16:37:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 5c899067-e4b9-3600-9e63-0ab36ebca728 | -3.47524 | -44.78033 | 2026-10-07 16:37:00 | NPP-375 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d2fd7750-8c94-35c9-86de-60ccef707ef1 | -7.17631 | -44.30852 | 2026-10-07 16:37:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 65326350-8e93-3865-aff2-fdcf606beb7e | -14.30506 | -39.85599 | 2026-10-07 16:37:00 | NPP-375 | ITAGIBÁ | BAHIA | Brasil | 2915205 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 9145e73d-fd76-329f-80f1-fbf958494ba2 | -9.03322 | -44.36377 | 2026-10-07 16:37:00 | NPP-375 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 57b2ba74-355c-3a9e-abb9-b394dbca955b | -16.61275 | -42.52296 | 2026-10-07 16:37:00 | NPP-375 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1f7a2cb1-23d9-3a45-9aa9-2ec445f370eb | -4.14735 | -43.19448 | 2026-10-07 16:37:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 59ac1973-ab43-378a-a4e4-5da6e3062450 | -7.29757 | -49.28087 | 2026-10-07 16:37:00 | NPP-375 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6579bf59-6ede-33e3-9e11-376f70e3aedd | -10.98387 | -45.40761 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 54076f8d-b9f4-3c8e-b67f-45e1303a9860 | -7.3436 | -38.73438 | 2026-10-07 16:37:00 | NPP-375 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f51c0ee1-ea51-3bbe-9709-e21a44211eb5 | -4.84856 | -40.41002 | 2026-10-07 16:37:00 | NPP-375 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 8c550b96-030c-33fa-abdd-74c500942964 | -4.93209 | -45.10781 | 2026-10-07 16:37:00 | NPP-375 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 72577921-75d1-37a9-8ded-4a9812820330 | -11.16951 | -49.48437 | 2026-10-07 16:37:00 | NPP-375 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4636e0a-bfc8-3313-bb3a-4f50a1077d4b | -7.77717 | -43.82015 | 2026-10-07 16:37:00 | NPP-375 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 0255e39a-12ee-3997-9c47-528283d1258d | -11.00178 | -45.48134 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 57109f50-254f-3bed-8c89-a15f3d276519 | -5.64431 | -42.78826 | 2026-10-07 16:37:00 | NPP-375 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 498fd66a-d499-3a88-bd8b-eeb1c56a104d | -9.83978 | -45.65518 | 2026-10-07 16:37:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| cccbe7e2-649f-3ae6-bc43-0a587b7eeb75 | -6.68132 | -44.94828 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 16316bc2-06e1-3bb0-b094-ba247b373d5f | -3.77329 | -38.74246 | 2026-10-07 16:37:00 | NPP-375 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 0a7ba822-1093-3d0e-900a-4a594af971ab | -8.76982 | -45.76899 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 22c6a2ae-acf6-39a7-83b6-0838d387b9ec | -6.00236 | -44.12788 | 2026-10-07 16:37:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 02a950c1-ac37-3659-be63-99d276368ba8 | -6.24951 | -53.45886 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| aea5eb11-0205-30a4-893b-f3356bdc260c | -6.48112 | -46.62246 | 2026-10-07 16:37:00 | NPP-375 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 44.8 |
| ce433fe6-63b4-35f0-9aed-18486af3f377 | -8.07333 | -38.23222 | 2026-10-07 16:37:00 | NPP-375 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 8.3 |
| ee89f7d9-b754-32e9-988a-7115b9fb4ac3 | -4.7722 | -50.81465 | 2026-10-07 16:37:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| bcaa0dac-0c6c-3cdb-8515-8f5c49d240b8 | -5.96664 | -53.59549 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5683c910-ee11-33d2-9e95-dc9525643278 | -4.96801 | -37.96722 | 2026-10-07 16:37:00 | NPP-375 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| d6ac5e22-4a29-3fe5-bc39-2904b6e373bf | -5.49169 | -39.72382 | 2026-10-07 16:37:00 | NPP-375 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 05dc32d0-be53-3215-b9ff-95b9437907f4 | -7.46893 | -42.82696 | 2026-10-07 16:37:00 | NPP-375 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 154.8 |
| 090b4cd6-b7ca-3a46-a6c9-239f74e2fa31 | -9.86936 | -46.0552 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 6245f131-5679-3f7c-b03e-1f6fff06fa93 | -10.95256 | -45.3885 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3f9aa2b3-fc05-34a7-9d25-c05de344611f | -9.35171 | -45.41801 | 2026-10-07 16:37:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 81a3ad8b-5e63-34fc-947a-90a7183b11f4 | -3.48966 | -39.50497 | 2026-10-07 16:37:00 | NPP-375 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 7.9 |
| bc55a8ab-54ca-3677-bf89-166f75cf58e1 | -5.7201 | -41.63094 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 7e6f86e7-7410-3192-9d22-d99bf75769ce | -4.32375 | -43.00363 | 2026-10-07 16:37:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| b5d6814c-4e04-3070-9c5e-bc13d0925e61 | -11.22635 | -46.23796 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 8db98eda-1f2e-39d0-bea9-85cdd72d0754 | -5.67838 | -42.58121 | 2026-10-07 16:37:00 | NPP-375 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 1cb3a657-247e-383d-9464-eaefdbf9aad8 | -5.692 | -53.47852 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| fc5fc8fc-2890-3610-8eca-73559d8a819a | -16.92826 | -42.11003 | 2026-10-07 16:37:00 | NPP-375 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |
| 6a5648d4-58c7-3380-8380-2e51d0fb031b | -7.30423 | -43.97433 | 2026-10-07 16:37:00 | NPP-375 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 8b1bda46-aadb-31b2-b186-afcd38614153 | -7.21028 | -44.29179 | 2026-10-07 16:37:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7aeeaa9c-93f6-3439-961f-de0481490cbe | -6.95186 | -45.26346 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| b0e3c3f2-7cef-3e21-985a-1f872d8e8ffb | -4.32104 | -41.23142 | 2026-10-07 16:37:00 | NPP-375 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 2c3dd282-8e09-3d91-80cd-a79aa484b31a | -7.10495 | -45.24015 | 2026-10-07 16:37:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| af99915d-d673-3df8-9f1e-f1b1afcd801a | -7.55903 | -47.78789 | 2026-10-07 16:37:00 | NPP-375 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a6a33d2c-940d-3dd6-92d4-b9db8f9bfa35 | -9.10321 | -45.10447 | 2026-10-07 16:37:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 354.5 |
| 7ac16438-0ebb-38d6-8f1c-ecf457de1f93 | -6.81654 | -38.53139 | 2026-10-07 16:37:00 | NPP-375 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 48.8 |
| 46eef4a6-9e35-37b7-bd91-8ecd4ad8d09b | -8.65693 | -54.55884 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1c8ebb34-0db5-3cb5-9db7-5c12d8da9aaf | -5.65377 | -43.13886 | 2026-10-07 16:37:00 | NPP-375 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 176942d4-c4ff-34ed-9410-a9ea0f0ee6f0 | -15.02738 | -39.39524 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DA VITÓRIA | BAHIA | Brasil | 2929354 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| fe800d5e-7d7c-3d68-9193-d459557783a5 | -7.80364 | -45.50245 | 2026-10-07 16:37:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d6fe514f-1824-3b01-bade-d47059a3602d | -6.15211 | -51.72944 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e6d16771-8fb0-3c5c-913d-dd5fe2d39773 | -5.68009 | -49.21627 | 2026-10-07 16:37:00 | NPP-375 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| a28ea8ea-fc63-36fe-b801-3d744fff1738 | -5.17387 | -42.67955 | 2026-10-07 16:37:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| eccfef79-c08b-3922-854b-9e2be681ea2b | -11.0053 | -45.43214 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| f4d37b9a-d990-3673-85f1-1d0172e46389 | -6.94564 | -45.26801 | 2026-10-07 16:37:00 | NPP-375 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 494934f6-9041-3313-bec2-23f54199a809 | -6.31829 | -53.30522 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 0f8deb83-3f41-3f94-ba55-dd3e8630c2d2 | -6.37057 | -42.92208 | 2026-10-07 16:37:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 8e417f5b-7488-3336-a1b1-73300d790903 | -6.22509 | -44.83673 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 9cc09f87-ee6b-3232-bae4-7fb69232bec9 | -6.33198 | -38.85501 | 2026-10-07 16:37:00 | NPP-375 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 75d5ca3c-6485-37ad-a5f8-69a02dffd025 | -6.15022 | -51.75126 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| e9f277d8-b265-3ebb-ab49-fa43e2db3da4 | -6.15041 | -52.65287 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 09e21b7d-8821-3fa4-990c-6e6e7f911897 | -14.90421 | -40.33153 | 2026-10-07 16:37:00 | NPP-375 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 19.1 |
| f463be84-7bcb-3642-804c-c105015585e8 | -7.87111 | -54.98085 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 3801b3e4-d6c9-37a0-89a3-c1bfb6179168 | -7.20416 | -44.2963 | 2026-10-07 16:37:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9dd4e667-0a3a-3f4b-ad93-7c28f7311fc8 | -6.15287 | -52.65345 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 4381f79f-3ac6-3cb3-9424-11f77357978a | -6.98241 | -45.12368 | 2026-10-07 16:37:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 96786997-0e9d-3d60-816a-ce6c712d0d5f | -9.376 | -45.92642 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 39941539-7855-32c6-a8f4-a18847614f5f | -7.18528 | -55.10701 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| c535805d-7a3c-3767-8385-f722cf1431ea | -3.81432 | -42.21604 | 2026-10-07 16:37:00 | NPP-375 | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9ed1b796-5d3d-36ed-9620-b25f3e785e04 | -3.77154 | -41.77515 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| 1b06a4fb-792d-38da-a818-525a5ce71435 | -9.4429 | -45.84414 | 2026-10-07 16:37:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 2e7fc811-3c46-3545-9b9e-0265472f4c92 | -5.73119 | -41.74577 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| c506b587-cf22-323b-83db-ec7609330548 | -14.88619 | -42.36263 | 2026-10-07 16:37:00 | NPP-375 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| b965e47f-845e-30bf-8a8b-6feb89db2345 | -14.71878 | -40.00408 | 2026-10-07 16:37:00 | NPP-375 | IGUAÍ | BAHIA | Brasil | 2913507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| b97f2345-47e1-3d4a-9e96-65f72065e2f4 | -14.90386 | -41.03374 | 2026-10-07 16:37:00 | NPP-375 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 73a54415-843f-3584-9b11-abef75fdd320 | -6.60012 | -37.89077 | 2026-10-07 16:37:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 15.7 |
| 7e248674-680e-3d06-9761-4f7d85ee7431 | -5.20873 | -56.07896 | 2026-10-07 16:37:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 75cfdc8d-5b6b-3ea8-88c4-ecf2844e458b | -6.92026 | -44.56242 | 2026-10-07 16:37:00 | NPP-375 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5e0668f1-2cd8-37cb-925e-3274577d41a3 | -5.49056 | -42.83095 | 2026-10-07 16:37:00 | NPP-375 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 542dccb8-f45a-332f-bd37-2d057510c7dd | -6.62229 | -37.88726 | 2026-10-07 16:37:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 1b3d4651-36b6-3cef-a6a7-0d9e5318dcca | -7.5539 | -47.77925 | 2026-10-07 16:37:00 | NPP-375 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3b39be66-90f5-365d-9f5f-9998ab116b58 | -6.37167 | -42.92917 | 2026-10-07 16:37:00 | NPP-375 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 3.9 |
| d0dcfd32-e26a-3c9a-94aa-c679de457c81 | -5.74567 | -53.45694 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| cb8ac070-d9df-3be4-bf7d-d96ef8ebad38 | -6.56345 | -46.04189 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 96bda95c-c610-3aa1-ae31-a270ff9b0a80 | -6.48014 | -52.82584 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 13c7aa92-e891-3703-8f4f-bb989d3599f4 | -16.93105 | -42.10586 | 2026-10-07 16:37:00 | NPP-375 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |
| a9b3ae47-4c85-3c6f-ab73-b9ae14a67659 | -9.97393 | -43.50514 | 2026-10-07 16:37:00 | NPP-375 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 73.4 |
| eb5b8040-c2a6-3731-849e-41c4451df21f | -5.96923 | -40.9259 | 2026-10-07 16:37:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 55.2 |
| 992c3145-6c19-375f-b888-82a3df5a82c3 | -3.77543 | -41.76646 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| ecf0bb7e-a724-3b40-9126-25f0c9b5a706 | -8.9611 | -45.10766 | 2026-10-07 16:37:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 30ce4746-0360-3fd4-a139-9c54afa3e0fc | -6.33137 | -38.85139 | 2026-10-07 16:37:00 | NPP-375 | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |


[Clique aqui para ver as próximas entradas](README186.md)
