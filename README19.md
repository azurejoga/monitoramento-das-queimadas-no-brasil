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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b1d1050-188a-3942-88f2-05a72e5cbc63 | -4.96666 | -44.18662 | 2024-10-22 04:17:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9d2e746-55ec-3d09-acad-57ebc4868f34 | -4.94859 | -45.42218 | 2024-10-22 04:17:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe7ecc72-853a-3608-9f04-a17305db610b | -4.94803 | -45.4257 | 2024-10-22 04:17:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1d11968d-e592-348f-b247-7826835b6695 | -4.73174 | -45.71186 | 2024-10-22 04:17:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cabfff5-56d4-3765-bfe4-6472f220aa43 | -4.94747 | -45.42924 | 2024-10-22 04:17:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 02e841be-1593-3eb9-b5fa-3d7f61800b5c | -4.94691 | -45.43275 | 2024-10-22 04:17:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d463464d-2ffe-3449-9c9e-5aef58f3e611 | -4.93065 | -45.84932 | 2024-10-22 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15dd5e28-2de0-3e47-811a-1b50e5bfa8ef | -4.93007 | -45.85294 | 2024-10-22 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 356bd520-2d54-30d4-9e51-a0a21c194fea | -4.92728 | -45.84877 | 2024-10-22 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a1fab5a-3f45-3894-80f3-ca0eb8bba2b8 | -4.9267 | -45.85239 | 2024-10-22 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fdda3155-37dc-3c0c-95e9-f4a55c69fb06 | -4.90667 | -45.83839 | 2024-10-22 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e97d7467-70e5-3f24-8c76-f38fdb675435 | -4.9061 | -45.84202 | 2024-10-22 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fce200b1-6d97-3bc0-ab78-62a8aa1c9c94 | -4.90552 | -45.84565 | 2024-10-22 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 157df498-6f8a-3131-938b-0a76d166783b | -4.90387 | -45.83427 | 2024-10-22 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd6b9578-a46a-3261-b6c4-a80d19ffbdc9 | -4.9033 | -45.83789 | 2024-10-22 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c90d7bb2-e842-3095-a159-ec6d625daa14 | -4.90215 | -45.84513 | 2024-10-22 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 62cead8e-8db2-3992-9905-1c2cf897686b | -4.90158 | -45.84874 | 2024-10-22 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 194bc069-8e40-36e2-bbe4-83729dad0e76 | -4.90107 | -45.8301 | 2024-10-22 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39bb45e2-1d1d-31c7-8b1e-b8f7c4d2e9d2 | -4.9005 | -45.83372 | 2024-10-22 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 00c056e3-61fa-3acd-98ff-6b039588997a | -4.89993 | -45.83735 | 2024-10-22 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2729804-e71d-3bb0-8dbe-3e1e13661b6f | -4.89713 | -45.83317 | 2024-10-22 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1dfcae8e-2f90-32cc-99cc-6eb34f5c8517 | -4.89656 | -45.83681 | 2024-10-22 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6bc20db-6b6a-3767-ac0c-137db7d55304 | -4.89598 | -45.84044 | 2024-10-22 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97970e0d-546e-3e01-9c79-e3c0602ec08c | -4.89377 | -45.83262 | 2024-10-22 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93724440-ba07-3903-ab35-01e21a4e6419 | -4.89319 | -45.83625 | 2024-10-22 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4bdb477c-ed24-38de-9955-26ef7bbc940f | -4.89262 | -45.83987 | 2024-10-22 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dcd02746-e5ad-3e47-a899-a520e2cc26ea | -4.84797 | -48.4898 | 2024-10-22 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 528d870d-5d7e-36c6-bc8e-1a33828b8945 | -4.83686 | -45.86426 | 2024-10-22 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b0580f41-52db-312c-b629-5229c5f50c3b | -4.83289 | -45.86742 | 2024-10-22 04:17:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4766511a-c560-3294-a12c-09127f41969b | -4.82262 | -48.09967 | 2024-10-22 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ca4300f-6ebe-3f94-9eb4-44ac1fe26803 | -4.74999 | -45.7918 | 2024-10-22 04:17:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 576431d5-8ca9-327c-8882-e62c415d8d41 | -4.69904 | -46.43946 | 2024-10-22 04:17:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1018826c-4a85-3624-a629-69b42e1f8727 | -4.667 | -46.57397 | 2024-10-22 04:17:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 03ccce01-ee21-355d-9a7c-eac812b4a57a | -4.66354 | -46.57344 | 2024-10-22 04:17:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a2e97c4-5ec5-3056-be78-770a9ebeea71 | -4.65375 | -45.69252 | 2024-10-22 04:17:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 45973d0f-62b5-30c8-a41b-f46ef72417f8 | -4.65038 | -45.69202 | 2024-10-22 04:17:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6358e882-7d84-38be-be9c-7db5b8692331 | -4.64981 | -45.69561 | 2024-10-22 04:17:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3d7dc9b-98cb-3549-82a0-5e9bd66fcd0d | -4.62756 | -46.05197 | 2024-10-22 04:17:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bbc92b1-d69d-30dd-ab06-2945395da34d | -4.62697 | -46.05563 | 2024-10-22 04:17:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d1ba381f-10aa-3d7b-b745-6587b784d307 | -4.62241 | -46.06235 | 2024-10-22 04:17:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 37da28e5-0966-35c5-820b-9c9777999e25 | -4.61803 | -45.78619 | 2024-10-22 04:17:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fea11cc3-52db-3cd1-ac4f-caac832bbe6c | -4.60246 | -46.47517 | 2024-10-22 04:17:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa78e902-9ec4-329d-ad92-3068bb7ac01d | -4.59901 | -46.47465 | 2024-10-22 04:17:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56cb7cb7-faf5-3eb0-9de0-c16bf23de583 | -4.44174 | -47.76977 | 2024-10-22 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03f64560-7c71-3075-8948-f571cb9fc90b | -4.43806 | -47.76921 | 2024-10-22 04:17:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee1196dc-5277-3d26-aded-33bf10881015 | -4.17137 | -48.59224 | 2024-10-22 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47ef13f4-5a62-309a-a200-a5b73645c1ed | -4.17057 | -48.59706 | 2024-10-22 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39fb5256-44ac-3c5f-84d6-fa2d9e65b402 | -4.16976 | -48.60198 | 2024-10-22 04:17:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7a2eec0f-3b1a-34fb-a11c-d32a083ae8de | -1.96923 | -46.61795 | 2024-10-22 04:17:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6242d63d-446f-3a83-8ade-addb68409478 | -1.87965 | -47.02385 | 2024-10-22 04:17:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 02de3e31-482f-369c-97b6-61a36b1a1d15 | -1.83011 | -47.2183 | 2024-10-22 04:17:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 47a0f583-3c76-32c2-aa3f-a92d114aa7f9 | -1.77064 | -46.31438 | 2024-10-22 04:17:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c2978b2-a86d-3a0d-8f5f-8750a9411d2a | -1.77002 | -46.31832 | 2024-10-22 04:17:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5c958e5-275b-313b-b9c1-ed56a177297b | -1.56133 | -47.32763 | 2024-10-22 04:17:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14abbf13-e9ae-3342-b7f2-053a4dd7c542 | -1.48419 | -48.95109 | 2024-10-22 04:17:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 267a729a-bdab-3c9e-8682-82bd0b1b5f48 | -1.48007 | -48.95041 | 2024-10-22 04:17:00 | NOAA-20 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 30a12c57-e28a-3636-8209-b32accf05220 | -1.11569 | -46.83556 | 2024-10-22 04:17:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2880bd8-f60c-30e1-979d-a5e152f50031 | -1.11273 | -46.83076 | 2024-10-22 04:17:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa2fe074-1c93-3c47-880c-848513f3ee78 | -1.11205 | -46.83499 | 2024-10-22 04:17:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b82f0280-6f20-314e-b0d6-2d74bbd392b1 | -1.10909 | -46.8302 | 2024-10-22 04:17:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35d3f7fb-f24e-3410-8d72-a1bb4e252e28 | -1.08447 | -46.77456 | 2024-10-22 04:17:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d14d9e3-f037-3a93-9fcf-4784483fdbea | -1.08363 | -46.77591 | 2024-10-22 04:17:00 | NOAA-20 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45250577-7d7a-309e-a97b-83b1e790dbf0 | -9.10901 | -35.46042 | 2024-10-22 04:17:00 | NOAA-20 | PORTO DE PEDRAS | ALAGOAS | Brasil | 2707404 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 35e3d338-0e42-3305-a96f-01dc68f512c9 | -8.99032 | -37.15338 | 2024-10-22 04:17:00 | NOAA-20 | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0dee5b87-3896-39e8-9d93-4d30b264ef0e | -8.08634 | -38.18612 | 2024-10-22 04:17:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8e2ffb35-f447-3820-b46a-a733e1fbde52 | -7.95841 | -39.81703 | 2024-10-22 04:17:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0d00bd01-c702-3d46-9da2-2cfc3f8f5912 | -7.95788 | -39.82069 | 2024-10-22 04:17:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 617e8d37-678f-37b8-ae59-55eae58d6d17 | -7.55437 | -39.87997 | 2024-10-22 04:17:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fa4dceb7-ca55-3e10-8447-fa9403ca6e9e | -7.25127 | -35.31958 | 2024-10-22 04:17:00 | NOAA-20 | SÃO JOSÉ DOS RAMOS | PARAÍBA | Brasil | 2514453 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3aef2eb1-6682-345d-81dd-9881890f18b2 | -7.25076 | -35.32325 | 2024-10-22 04:17:00 | NOAA-20 | SÃO JOSÉ DOS RAMOS | PARAÍBA | Brasil | 2514453 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9ef73d4e-ad27-3f52-a308-9370005b7e1a | -7.12958 | -44.30233 | 2024-10-22 04:17:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b3812419-9241-3e59-835d-98329cca05fa | -6.93807 | -41.43078 | 2024-10-22 04:17:00 | NOAA-20 | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7404c69d-73cb-3f3b-8a9a-792765fd85d2 | -6.73075 | -40.48307 | 2024-10-22 04:17:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 1000a4cc-39c1-30bf-9339-fdcf6b9c7897 | -6.72954 | -40.48064 | 2024-10-22 04:17:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| d4a9165a-44df-3008-bcaa-a7afbe8a5a02 | -6.72908 | -40.46815 | 2024-10-22 04:17:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a36596d3-994e-30c4-8f5e-f613c8f844d6 | -6.72885 | -40.48543 | 2024-10-22 04:17:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 3bbb3d24-ae91-32dc-93b6-087e71587155 | -6.72763 | -40.47774 | 2024-10-22 04:17:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 3c078db4-00a7-3552-bfb7-95fbd7b31f77 | -6.72709 | -40.47047 | 2024-10-22 04:17:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 07ed770c-f6f5-3d61-9a6e-f6bc95827aae | -6.72691 | -40.48251 | 2024-10-22 04:17:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 83749ef3-e860-385e-be7b-1b244a25a104 | -6.72639 | -40.47527 | 2024-10-22 04:17:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ec20b021-3398-3e65-885d-c7850b4e5f34 | -6.72619 | -40.48728 | 2024-10-22 04:17:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| eb774f89-2c1f-38cb-9030-9e9143a1e981 | -6.72597 | -40.46278 | 2024-10-22 04:17:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fb295e63-cf4e-3522-9cad-24b944f20134 | -6.72571 | -40.48005 | 2024-10-22 04:17:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 5057d954-a389-3361-8737-fb0a8f38e08d | -6.7238 | -40.47714 | 2024-10-22 04:17:00 | NOAA-20 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1668840f-6850-3ae8-abcc-81ac3240ef4f | -6.58078 | -39.71636 | 2024-10-22 04:17:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 97c4df49-c54c-312a-9870-4f0b2ad5f8c3 | -6.28713 | -42.64617 | 2024-10-22 04:17:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3e13d9a4-11c9-3c4c-96a3-4cf39695c956 | -6.21115 | -43.28033 | 2024-10-22 04:17:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 550d44d4-d691-34e7-b7e5-39d8d08f0e30 | -6.20498 | -43.27571 | 2024-10-22 04:17:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5ba36ce-745d-3bc2-82d7-9b1294f8cf85 | -6.20388 | -43.2829 | 2024-10-22 04:17:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d8b8869a-5df6-3118-b344-a3c9ad7620a5 | -6.05986 | -42.71099 | 2024-10-22 04:17:00 | NOAA-20 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b904bb74-7294-3610-ae4d-edb8b5e3fcd0 | -6.05929 | -42.71469 | 2024-10-22 04:17:00 | NOAA-20 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f64ba8a0-3f09-3fd3-939d-29da1c7df77e | -6.05871 | -42.71838 | 2024-10-22 04:17:00 | NOAA-20 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b3184fcd-402a-3395-8186-ca86cdbf5fce | -6.05814 | -42.72208 | 2024-10-22 04:17:00 | NOAA-20 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 5789eb3f-eb75-36a6-9027-7c52313619c5 | -6.02028 | -43.08606 | 2024-10-22 04:17:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 26168746-b157-370d-8995-54f5afbf815d | -5.85626 | -43.88649 | 2024-10-22 04:17:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 277878d3-8eba-3586-b116-afde4bf9bf07 | -5.85534 | -43.73983 | 2024-10-22 04:17:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 450f40a2-e28d-3657-9d7f-db1dcdf3e336 | -5.85479 | -43.74333 | 2024-10-22 04:17:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a2869e81-4684-3cf5-9a86-977e2f847e03 | -5.83124 | -43.65371 | 2024-10-22 04:17:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf74c1fe-8166-39bf-b7fe-60dd2340d2eb | -5.82845 | -43.64968 | 2024-10-22 04:17:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b6d869e6-2446-3c26-b6bf-605653eaa7ca | -5.82791 | -43.65319 | 2024-10-22 04:17:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |


[Clique aqui para ver as próximas entradas](README20.md)
