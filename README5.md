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
| 38b5d856-c534-3aba-86ad-b6ec63d07161 | -7.0797 | -59.2157 | 2025-08-11 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 06570478-241f-37bd-8cb5-67584814ce14 | -8.9213 | -60.7489 | 2025-08-11 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.4 |
| e6ac29eb-42e4-3f8a-87df-30937f1fba53 | -8.9399 | -60.7481 | 2025-08-11 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| bc88fcec-6008-35fb-8054-7b18da57772f | -8.579 | -54.696 | 2025-08-11 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 031d9bde-ac68-3fab-a1dd-bb8ce0254072 | -8.5604 | -54.6973 | 2025-08-11 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| bd546bea-7b73-3a52-9975-831698b79895 | -9.3806 | -61.5315 | 2025-08-11 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 15933d91-60bd-35b8-9901-cd1002e5e46c | -7.0613 | -59.2165 | 2025-08-11 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| cd1572ae-e58e-304f-a17c-a16034592821 | -7.0614 | -59.1972 | 2025-08-11 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 9fc7f8ff-8652-35a8-b301-eef8b72f971b | -18.6287 | -46.8629 | 2025-08-11 01:30:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 645dd7c4-3388-383e-b984-9ab4add53a0e | -8.9215 | -60.7297 | 2025-08-11 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 99224ddc-43a6-32b7-ba94-602202c634d2 | -8.9401 | -60.7288 | 2025-08-11 01:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| ea274562-79ec-3657-946f-d0912d543dcd | -8.5604 | -54.6973 | 2025-08-11 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 0eee4b9d-5bdb-3872-898f-2583ca798bf4 | -8.9399 | -60.7481 | 2025-08-11 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 00164568-9711-3946-8457-5cb211756412 | -7.0797 | -59.2157 | 2025-08-11 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.3 |
| e9762208-e424-3206-89d7-d75a30d98f28 | -8.9401 | -60.7288 | 2025-08-11 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 3950abaf-3861-3af0-a7bb-12c8683d1a99 | -18.6287 | -46.8629 | 2025-08-11 01:40:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 43.6 |
| f1b26160-56c1-376a-ac8c-069b8c2580d2 | -8.579 | -54.696 | 2025-08-11 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 6d1872b3-cb1d-3c4b-ba1b-fefa61abab95 | -7.4564 | -43.9554 | 2025-08-11 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 52.7 |
| f15c38a6-f4f6-3aa5-989f-9939abcb3571 | -9.3806 | -61.5315 | 2025-08-11 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 964bc6ba-2b91-3113-b4e9-6d175c357326 | -7.0613 | -59.2165 | 2025-08-11 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| fdbf1dc5-8b14-39a2-8131-8a9664cc3ff5 | -7.0614 | -59.1972 | 2025-08-11 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.3 |
| ad3c587a-5f64-30c3-be4b-9fa0b42f60cf | -9.4761 | -40.3862 | 2025-08-11 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 56.6 |
| aaa4f440-5669-3047-9e77-e012f44aaf96 | -7.0799 | -59.1964 | 2025-08-11 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 122.1 |
| 56d0c077-e7b6-3b00-94c1-ea9a780fadae | -18.6293 | -46.8394 | 2025-08-11 01:40:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 64.2 |
| d532a317-7fff-3d2c-b12f-e5d944281460 | -7.2508 | -59.994999 | 2025-08-11 01:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 46930f2d-08a0-31b8-88ba-93d51999b600 | -8.9319 | -60.7248 | 2025-08-11 01:42:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8903ea6b-e90e-3c90-98cd-7e285823d837 | -8.9199 | -60.761501 | 2025-08-11 01:42:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f04b7e80-22bf-35c8-858a-510f23d0c066 | -7.0643 | -59.172401 | 2025-08-11 01:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6f2bf8f9-ae33-3e5c-aad7-94d63aae9d12 | -8.9357 | -60.740898 | 2025-08-11 01:42:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7f31820b-0070-3497-98e5-d861e8fa4de7 | -8.555 | -54.692402 | 2025-08-11 01:42:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43234666-4962-371c-82fa-ae6f12c4779a | -7.0741 | -59.2132 | 2025-08-11 01:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b56a4a30-5dbe-332b-847e-a03e2dfcbe91 | -7.0644 | -59.2155 | 2025-08-11 01:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a1db4a80-216c-3546-80ef-d68b6b4632af | -9.3796 | -61.531101 | 2025-08-11 01:42:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d7d13664-cc99-3dd6-b14f-f6846cead65e | -9.3779 | -61.523701 | 2025-08-11 01:42:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 85b1ee38-b755-3baf-a6ec-361078181b9c | -8.5695 | -54.709202 | 2025-08-11 01:42:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bf9c946-5a29-3a91-b871-b3d26cb0a1e4 | -9.3761 | -61.5163 | 2025-08-11 01:42:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 499d66d7-8e15-3e53-9535-68c313e14011 | -7.0668 | -59.182598 | 2025-08-11 01:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ed8c5f91-402a-36f9-8ad5-a646dd530871 | -7.0815 | -59.200699 | 2025-08-11 01:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4f9bd40b-3526-309d-831d-a4681d1fc99f | -7.0595 | -59.195202 | 2025-08-11 01:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5fd1b88f-ff8a-30f3-9937-7642d8682579 | -7.0717 | -59.203098 | 2025-08-11 01:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c5942632-488d-3cbb-a036-94d15d1d840d | -7.062 | -59.205399 | 2025-08-11 01:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2d06c822-3aa5-37b8-b010-15a51a1508aa | -10.1502 | -68.597 | 2025-08-11 01:42:00 | METOP-C | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| fcc8a5b7-e9a8-3ae1-9bbc-82d2cffe4c50 | -8.5646 | -54.689899 | 2025-08-11 01:42:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2105f18-45d1-31cc-94bc-2a58795e36a8 | -8.5597 | -54.670601 | 2025-08-11 01:42:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78395ecc-7370-3a8e-8e11-77cf09f73d2d | -7.0766 | -59.180302 | 2025-08-11 01:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3579e269-8106-326c-8512-18edd4b57461 | -7.0692 | -59.192902 | 2025-08-11 01:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2ba4bd3e-f2be-39d7-b439-437a2b7e359c | -8.5743 | -54.687401 | 2025-08-11 01:42:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 820d28d6-8a92-321b-90e8-2d13b084927c | -8.9338 | -60.7328 | 2025-08-11 01:42:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 90f41424-b7c1-3723-9148-fdc96a9a3bb1 | -8.9436 | -60.730499 | 2025-08-11 01:42:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 943c2f28-6f0c-3d15-a0cd-4dbe5ab69721 | -8.9376 | -60.748901 | 2025-08-11 01:42:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d399e23d-c069-3317-a91c-ffa55d36e331 | -8.9278 | -60.751202 | 2025-08-11 01:42:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8147175c-7cc0-3a75-bd42-4933d2a51002 | -9.3813 | -61.538601 | 2025-08-11 01:42:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e52c622a-7d45-3343-8ebd-964b7a2ea856 | -8.9297 | -60.759201 | 2025-08-11 01:42:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 79e0f743-096a-367c-a50b-b098faeb1f01 | -15.4189 | -53.902901 | 2025-08-11 01:42:00 | METOP-C | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| dbd7e7fd-b390-3c40-9ace-4e919c3e2929 | -7.0888 | -59.188202 | 2025-08-11 01:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ac1e2033-33b9-3e03-804d-cbdc67eb2b83 | -8.9259 | -60.743198 | 2025-08-11 01:42:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5134e0cc-24f7-343a-83ea-bde422a4d5b0 | -8.9395 | -60.756901 | 2025-08-11 01:42:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 70046c4f-4280-30e5-a224-47da9fa36b88 | -15.4093 | -53.905602 | 2025-08-11 01:42:00 | METOP-C | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ae64997b-98bc-3b1d-beb2-73429a404c8f | -7.079 | -59.190498 | 2025-08-11 01:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fe4f6f90-232f-3c40-8764-42be30c19e7d | -7.0571 | -59.184898 | 2025-08-11 01:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3de6e629-20b3-37aa-b5ec-00d6930804c1 | -7.2605 | -59.992699 | 2025-08-11 01:42:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 73c78ead-af64-3de2-8bb7-444efb22b6e0 | -7.0797 | -59.2157 | 2025-08-11 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.4 |
| db1e6584-0a9a-3146-b366-a8fa60788ad8 | -23.5564 | -51.5961 | 2025-08-11 01:50:00 | GOES-19 | CAMBIRA | PARANÁ | Brasil | 4103800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 50.5 |
| 9c2cad53-9e79-3289-b3a1-160b4707ebbb | -21.0336 | -50.0172 | 2025-08-11 01:50:00 | GOES-19 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 51.2 |
| caef52c9-074d-325c-ab0b-9e8179109e37 | -8.9399 | -60.7481 | 2025-08-11 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| eb53e986-c228-3052-8b2c-c3e5ec516438 | -8.9215 | -60.7297 | 2025-08-11 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 58ab028f-1322-3667-8033-0c6a581ac798 | -18.6293 | -46.8394 | 2025-08-11 01:50:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 5590e18a-5913-3059-ab2d-9d567a164f87 | -7.0613 | -59.2165 | 2025-08-11 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 313b69a9-9afc-38f1-ae01-8ed4d2691198 | -15.4216 | -53.9073 | 2025-08-11 01:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| cdff42d9-3948-368f-a5b4-9e3b5efc31a2 | -7.0614 | -59.1972 | 2025-08-11 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.0 |
| b1eb5e84-e757-333c-82fb-0057a0c0e48c | -8.9401 | -60.7288 | 2025-08-11 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.9 |
| c0bea579-a007-3ec2-8e0f-eb38b9e2b3fa | -23.5558 | -51.619 | 2025-08-11 01:50:00 | GOES-19 | CAMBIRA | PARANÁ | Brasil | 4103800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 54.2 |
| d2945660-c4eb-3f7b-8d65-3e31ba8740c6 | -9.3806 | -61.5315 | 2025-08-11 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 041d70d2-e6a3-31df-8083-a847208da6af | -8.5604 | -54.6973 | 2025-08-11 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| dfbed381-d96e-3454-afb6-68fd2b9ba111 | -7.0799 | -59.1964 | 2025-08-11 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 2e5f8bce-c0a6-34e7-98cd-f1f3f4160071 | -8.9399 | -60.7481 | 2025-08-11 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| c547049d-f4ce-3150-8b55-4fbdbd2c03c2 | -8.5604 | -54.6973 | 2025-08-11 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 3742918e-8a14-3f4c-8420-127ac313c057 | -8.9401 | -60.7288 | 2025-08-11 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| d32ec364-b72a-3839-81b1-ef0a3350f5e2 | -7.0799 | -59.1964 | 2025-08-11 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 132.8 |
| 1d8d76f1-a8df-312d-8ecd-8408bb3c8a2a | -9.3806 | -61.5315 | 2025-08-11 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.2 |
| c3c47422-ba2d-3561-8904-21f12bb6e8c7 | -6.5856 | -44.564 | 2025-08-11 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.5 |
| fcf9522a-5f3f-3edf-9066-a2d1f3c0c413 | -7.0613 | -59.2165 | 2025-08-11 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 3738cd6c-7afb-39e6-83e9-43fd9ee20fc9 | -21.0336 | -50.0172 | 2025-08-11 02:00:00 | GOES-19 | ZACARIAS | SÃO PAULO | Brasil | 3557154 | 35 | 33 | nan | nan | nan | Mata Atlântica | 115.6 |
| 544f3126-1bea-3a3c-84ce-bc64d8d9c099 | -14.4834 | -47.0642 | 2025-08-11 02:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 045f50e2-e98d-36a4-a81f-f6482d6b6d47 | -7.0614 | -59.1972 | 2025-08-11 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 5c2fa0f0-7b96-3281-9878-8f42db625f2a | -8.9213 | -60.7489 | 2025-08-11 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 03f0c230-8caa-3a9f-8ca0-bb00a088e2b8 | -7.0797 | -59.2157 | 2025-08-11 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 452e9067-84e0-320b-afb8-f2c168136faa | -6.5858 | -44.541 | 2025-08-11 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 43b24677-fe28-3cb6-a147-862e059cc226 | -6.5668 | -44.5655 | 2025-08-11 02:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 903cf416-4b12-380d-8d1b-fdf483cd45f2 | -21.0342 | -49.9944 | 2025-08-11 02:00:00 | GOES-19 | PLANALTO | SÃO PAULO | Brasil | 3539608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 58.8 |
| a61730e0-4829-3436-a1c0-16de8bb980da | -14.483 | -47.087 | 2025-08-11 02:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 16644367-1b33-3260-a236-d7358479d402 | -8.92681 | -60.73235 | 2025-08-11 02:06:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 3a061348-70e6-34c7-8c7c-30a9a5f3fc2c | -9.36784 | -61.53556 | 2025-08-11 02:06:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 2371ced8-f0cd-3936-8d22-1cc3dd559ef6 | -10.1446 | -68.60483 | 2025-08-11 02:06:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 12.0 |
| dc601dfe-4f8b-32db-a613-4a5b472e2645 | -8.92608 | -60.73965 | 2025-08-11 02:06:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 73e08860-6999-3044-95b6-09e3a8787421 | -9.37429 | -61.52926 | 2025-08-11 02:06:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 5397ca13-6c8f-38b1-82e1-6de9ae131f1e | -8.94339 | -60.73638 | 2025-08-11 02:06:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.4 |
| be94270e-03ee-3395-8e3f-348851eb60bd | -8.93389 | -60.77258 | 2025-08-11 02:06:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 180fb2bd-16b4-3c65-8a3a-c8802bff079b | -9.38409 | -61.53266 | 2025-08-11 02:06:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 8650fe74-8b5c-3143-a64f-e6d885537e87 | -9.3806 | -61.5315 | 2025-08-11 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |


[Clique aqui para ver as próximas entradas](README6.md)
