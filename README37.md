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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2080bb5-f8d0-3bab-a5e8-26ea5d3e0b0c | -19.543 | -56.887 | 2024-11-15 13:50:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.5 |
| 5660f390-49e3-30f9-a225-c7bff727728c | -6.2819 | -37.7738 | 2024-11-15 13:50:00 | GOES-16 | JOÃO DIAS | RIO GRANDE DO NORTE | Brasil | 2405900 | 24 | 33 | nan | nan | nan | Caatinga | 132.5 |
| ae204a68-0d39-393c-b562-95ba5d6f5499 | -16.9577 | -57.6473 | 2024-11-15 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.8 |
| b312a841-a076-3cba-ad0a-2ff3ac8a874f | -14.8165 | -58.1758 | 2024-11-15 13:50:00 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 116.4 |
| a819da03-d967-3f4b-95af-42ef0fe308a8 | -17.274 | -57.4675 | 2024-11-15 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 120.4 |
| 0bacc069-a6e2-39f0-af6c-dd2295c4d5c0 | -4.404 | -43.6833 | 2024-11-15 13:50:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 6c14c620-71aa-35cb-916b-e77f7df6260e | -6.3009 | -37.7718 | 2024-11-15 13:50:00 | GOES-16 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 105.9 |
| 64ef8004-853a-3ab1-96d4-81e342f94c65 | -17.2936 | -57.4652 | 2024-11-15 13:50:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 110.0 |
| 680e7656-dae1-30b1-9524-db24c7fcebbe | -19.5426 | -56.908 | 2024-11-15 14:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.3 |
| f7105a24-54b2-3e94-a943-1c59c8466350 | -19.543 | -56.887 | 2024-11-15 14:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.3 |
| f2da2cb6-0a2a-3867-ad24-57308a42febd | -16.9384 | -57.6291 | 2024-11-15 14:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 109.1 |
| 75919839-e959-33f3-bf1f-502fa8734d3a | -17.219 | -57.228 | 2024-11-15 14:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.7 |
| d86916bc-6ace-3c76-9de5-c037abe52d91 | -16.9577 | -57.6473 | 2024-11-15 14:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 85.1 |
| da2f3570-e22d-31fb-897d-c7a9c7efb7dc | -23.9517 | -54.0521 | 2024-11-15 14:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 103.3 |
| 1fa14ef9-4254-365b-9fe3-b56c7c5488e0 | -17.2963 | -57.3008 | 2024-11-15 14:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 128.3 |
| 2a74bfba-f498-3439-8ecf-f264da6414da | -3.442 | -42.1892 | 2024-11-15 14:00:00 | GOES-16 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 96.5 |
| e23fc5e3-fed5-3e07-9f6a-78570fb25459 | -23.9306 | -54.0564 | 2024-11-15 14:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 107.3 |
| 76eb80bf-d5cf-3775-a6c5-2207c57eedc0 | -17.2959 | -57.3214 | 2024-11-15 14:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.8 |
| 840268cd-cd59-3acb-a769-aa76d618434e | -4.5333 | -38.9243 | 2024-11-15 14:00:00 | GOES-16 | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 315.4 |
| 623f3ef6-7593-3d4f-a46a-2b2e0862cfa0 | -3.49 | -40.3559 | 2024-11-15 14:00:00 | GOES-16 | MASSAPÊ | CEARÁ | Brasil | 2308005 | 23 | 33 | nan | nan | nan | Caatinga | 100.3 |
| 4b12f054-d523-359b-bae6-eaeab3f0dd2b | -16.958 | -57.6269 | 2024-11-15 14:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 88.1 |
| a9e19d85-cfa8-3f69-8e4f-edc8cd5a1127 | -17.8066 | -57.3625 | 2024-11-15 14:00:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.0 |
| 3677b68b-1fe5-3f67-a3fc-275e22459a2c | -7.7105 | -37.4495 | 2024-11-15 14:00:00 | GOES-16 | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 134.5 |
| 9f9b0d9c-7554-3115-a0d6-9c18c911e7d5 | -3.4467 | -41.3533 | 2024-11-15 14:00:00 | GOES-16 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 193.6 |
| 67dea917-41c6-35a8-a9c2-0cb4ed0e55fa | -17.8454 | -57.3989 | 2024-11-15 14:00:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 87.4 |
| 021fa02e-812c-3956-ac53-4c46cb277a62 | -14.8165 | -58.1758 | 2024-11-15 14:00:00 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 118.9 |
| af01d9a9-a5f4-39c7-b49e-442576d97d35 | -3.8926 | -41.8807 | 2024-11-15 14:10:00 | GOES-16 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 87.2 |
| 2433a98a-e171-32cd-b56c-6101e5978d2e | -4.5333 | -38.9243 | 2024-11-15 14:10:00 | GOES-16 | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 135.1 |
| e0beb3b1-b18c-392b-a2e4-40510a8360c5 | -19.5426 | -56.908 | 2024-11-15 14:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.0 |
| e4a083f3-6876-3fca-b020-2c386ae95669 | -17.2963 | -57.3008 | 2024-11-15 14:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 134.9 |
| 0ed15b6d-4c91-36c3-a6ef-b9daa3faedcc | -23.9517 | -54.0521 | 2024-11-15 14:10:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 106.4 |
| afaf43bf-9a10-3494-b29d-6ae9755e7d7f | -17.8457 | -57.3783 | 2024-11-15 14:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.3 |
| ac109025-6bb7-35f0-86ff-9b1136d903ce | -19.543 | -56.887 | 2024-11-15 14:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 75.4 |
| 42d1b595-0efa-3e4e-b0a0-b74b8b07a72f | -17.8454 | -57.3989 | 2024-11-15 14:10:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 94.1 |
| 5b320d61-5727-3617-ac4b-bcdaa9596dec | -3.0764 | -44.3456 | 2024-11-15 14:10:00 | GOES-16 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 77.8 |
| a6d12295-9fe1-39e8-b951-454c03a33a5a | -17.2959 | -57.3214 | 2024-11-15 14:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 94.7 |
| 26fe32ff-b039-35f9-9c24-938c9c084950 | -16.9384 | -57.6291 | 2024-11-15 14:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 116.2 |
| 71f24997-b1da-3921-ad94-cae47b9dba7b | -16.9577 | -57.6473 | 2024-11-15 14:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 87.0 |
| dba9eb18-e410-325c-81b6-2698ad22440b | -17.8066 | -57.3625 | 2024-11-15 14:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.0 |
| ddcd5f9e-4aa9-3037-9e63-d533030f36a4 | -17.219 | -57.228 | 2024-11-15 14:10:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 111.9 |
| 595b7285-c105-3b1e-9db8-a6775dc53c5d | -16.958 | -57.6269 | 2024-11-15 14:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.4 |
| 6d2396ec-7f72-347a-8a41-9bec96faca69 | -23.9729 | -54.0478 | 2024-11-15 14:10:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 75.4 |
| 8ce0203c-3676-3114-8792-7fc03bd493c0 | -16.9577 | -57.6473 | 2024-11-15 14:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.4 |
| 071e7191-112b-35c5-a7cd-60704e5f288d | -19.5426 | -56.908 | 2024-11-15 14:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 121.0 |
| 436d5d7d-2ae3-3d39-a54e-20180de7ea40 | -17.826 | -57.3807 | 2024-11-15 14:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.5 |
| 52484209-8600-3708-a698-2a87ebcb9dc4 | -16.9384 | -57.6291 | 2024-11-15 14:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 114.7 |
| 9c517600-4afb-3dce-839c-9ccb4730bda4 | -6.9749 | -38.4694 | 2024-11-15 14:20:00 | GOES-16 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 121.0 |
| f977edaf-435c-3ce4-925a-5969541b0599 | -3.4468 | -44.7176 | 2024-11-15 14:20:00 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 2e8679b9-7a00-349d-a421-5b4ea29d288b | -17.8457 | -57.3783 | 2024-11-15 14:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.5 |
| 2b82e147-dfb0-3f6c-887f-55892f01a122 | -17.8066 | -57.3625 | 2024-11-15 14:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.8 |
| 51736e80-76b9-32b6-8e6b-6d920f62d4dd | -23.9517 | -54.0521 | 2024-11-15 14:20:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 107.2 |
| 7b08de3a-a278-3f96-b5b0-09c04e265860 | -23.9306 | -54.0564 | 2024-11-15 14:20:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 114.8 |
| dbaf971a-ca01-3ee1-8a13-d949cbd0d12b | -17.8454 | -57.3989 | 2024-11-15 14:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 91.9 |
| 98c5c12d-5e62-304d-a1c0-eda3f4e6fcf8 | -3.614 | -44.7783 | 2024-11-15 14:20:00 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 80.6 |
| 4bb021a6-318d-3630-8547-dfa7263e5783 | -23.9729 | -54.0478 | 2024-11-15 14:20:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 78.0 |
| 3a478f96-4033-3a11-9113-654dccadd693 | -16.958 | -57.6269 | 2024-11-15 14:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 92.8 |
| 10233e2c-c5c1-3680-beea-1205c5a096f0 | -19.543 | -56.887 | 2024-11-15 14:20:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.0 |
| e37393ae-9f00-3b4d-881a-ef4533932747 | -19.5426 | -56.908 | 2024-11-15 14:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.8 |
| bdc03458-23fa-39df-ad50-1a53b5b0b9ed | -17.8454 | -57.3989 | 2024-11-15 14:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 101.3 |
| 89710390-13dc-3a3c-a966-ba483affbfe4 | -19.543 | -56.887 | 2024-11-15 14:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.3 |
| e2cd64d5-f33e-3f11-90d4-6bd5b5b3e4fb | -17.8066 | -57.3625 | 2024-11-15 14:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.4 |
| fa145855-2710-30b8-9e0a-783aebf61675 | -17.826 | -57.3807 | 2024-11-15 14:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 85.5 |
| ef58efd8-cbf6-30cf-b681-5c45e5ee8d8f | -14.8165 | -58.1758 | 2024-11-15 14:30:00 | GOES-16 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 129.7 |
| a5c931ad-29c0-36fb-a600-dbfca3711646 | -16.958 | -57.6269 | 2024-11-15 14:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.8 |
| 70ff4ebb-c347-3322-88b7-f754eefb80ee | -3.4659 | -44.6258 | 2024-11-15 14:30:00 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 6baff9f7-e4ea-3135-af34-05a2280c4db2 | -16.9384 | -57.6291 | 2024-11-15 14:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 116.4 |
| 9a21a3ca-ee27-3dca-8f68-7a456ac03c13 | -18.3019 | -56.1386 | 2024-11-15 14:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.7 |
| 7b2792bc-2c48-3c13-a42e-016642f007fd | -17.8457 | -57.3783 | 2024-11-15 14:30:00 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.3 |
| 95c1ab2e-01da-3c06-a773-3326dd4688b3 | -23.9517 | -54.0521 | 2024-11-15 14:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 113.4 |
| e9c571c7-520e-3ee7-8128-67d1499f748f | -17.235 | -57.4516 | 2024-11-15 14:30:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 112.1 |
| 1daad552-4fa0-3074-be21-3ccb0de43d98 | -23.9306 | -54.0564 | 2024-11-15 14:30:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 120.7 |
| 93177626-57e7-3651-b937-3958a68f4b36 | -3.161 | -42.3205 | 2024-11-15 14:30:00 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| ca939c3c-3d78-3cc0-8756-c13a187b1a65 | -3.6195 | -43.7939 | 2024-11-15 14:30:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 3e418b89-d4ac-3936-b3f2-f562cae948d5 | -17.8263 | -57.3601 | 2024-11-15 14:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 102.6 |


