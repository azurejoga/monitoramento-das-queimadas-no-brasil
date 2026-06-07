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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62c27ccd-2f5b-3133-b931-598026c39851 | -17.99955 | -54.28337 | 2026-06-07 05:29:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e29f681-e9dd-3f4f-b9dc-743957363eb9 | -17.99543 | -54.27754 | 2026-06-07 05:29:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c99c5c4-a71e-3ea3-83d0-e306928af688 | -18.46433 | -54.70105 | 2026-06-07 05:29:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5dbe299-5b45-3910-88da-78585967615a | -18.00429 | -54.28396 | 2026-06-07 05:29:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27fb163f-8902-3afc-9f89-3121a6101931 | -16.59773 | -58.23613 | 2026-06-07 05:29:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 47e320c1-ee7c-374d-bfa6-bea5e8a3aa30 | -16.79885 | -54.16771 | 2026-06-07 05:29:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c68f6348-b610-3b11-a4b2-df043efb4467 | -16.78885 | -54.17146 | 2026-06-07 05:29:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ceeb2e59-1d96-3636-a478-5fad6d7618ed | -18.46372 | -54.70615 | 2026-06-07 05:29:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 919ce5db-3f98-3b52-a8fa-0093a2f802b9 | -16.18567 | -58.46523 | 2026-06-07 05:29:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 38d43b07-8238-399e-abff-65d885e0caf1 | -21.98887 | -57.61116 | 2026-06-07 05:31:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0dd612a1-b3ec-3051-b98c-05109aadd465 | -21.9886 | -57.61237 | 2026-06-07 05:31:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0649afca-a5ba-3843-8aa2-1c8b43349417 | -21.98963 | -57.60524 | 2026-06-07 05:31:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4dadc12e-7b0e-30f3-88c7-d6434f3476b5 | -21.98482 | -57.61066 | 2026-06-07 05:31:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2c993923-71dc-3d00-87e1-f6506664aecb | -21.98557 | -57.60477 | 2026-06-07 05:31:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0433cbbe-fc59-363c-89bb-b3c7cff3dca4 | -30.39715 | -54.25922 | 2026-06-07 05:33:00 | NPP-375D | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 369bdefb-39be-31ab-bd81-ac60fcf20dba | -30.40266 | -54.25982 | 2026-06-07 05:33:00 | NPP-375D | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 86a38c7f-a319-36d7-907b-c7eac88c8e94 | -30.40182 | -54.25735 | 2026-06-07 05:33:00 | NPP-375D | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 1056b569-c637-30d8-8af8-ef0d6a12dae6 | -10.82777 | -60.76412 | 2026-06-07 05:46:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2bde1c2-1257-3b79-9cec-9434acb2ddbd | -11.55552 | -52.79208 | 2026-06-07 05:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b3e4d978-3d14-3353-ba64-14a4b3d68c73 | -10.57292 | -57.32196 | 2026-06-07 05:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbe61c58-ff66-3980-b106-fb6f46ae652d | -11.72342 | -56.84539 | 2026-06-07 05:46:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c66cc3a8-8574-350f-93b5-e67abcfead1c | -10.86303 | -53.74043 | 2026-06-07 05:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99455051-fab4-37ef-b31e-09e9a6bb2d5b | -11.05723 | -56.92225 | 2026-06-07 05:46:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ac69e32-fab7-3033-95e5-a5d6c6e62169 | -10.83246 | -60.76091 | 2026-06-07 05:46:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 18e7229f-b82c-3bc7-9a8e-9fb70b4cfcea | -11.55605 | -52.80996 | 2026-06-07 05:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8d4f5b4-2f06-39b1-bafa-7b24544410e3 | -10.85341 | -53.74633 | 2026-06-07 05:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4afbcdac-d583-3ca3-88b8-3359d3c55bb7 | -10.8283 | -60.76029 | 2026-06-07 05:46:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 6ae2c796-49be-3347-815a-270625a70a12 | -10.59751 | -55.41973 | 2026-06-07 05:46:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b9a8f2ae-d183-3ee1-a976-88e977691929 | -10.83769 | -60.75388 | 2026-06-07 05:46:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 41d2b875-df3b-3724-a2b5-609d0877fe32 | -11.54352 | -52.79449 | 2026-06-07 05:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8163cf6c-e2ec-3e98-9bc8-75557cd5c592 | -11.55056 | -52.79546 | 2026-06-07 05:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c6e762b0-1c12-31f1-a194-e3acf478b12c | -10.85641 | -53.73962 | 2026-06-07 05:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1732ba08-fba1-371d-a955-16f6942ca5cd | -10.57334 | -57.31876 | 2026-06-07 05:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 190586b5-fe6a-37a3-bc18-ce873772e643 | -10.86072 | -53.74116 | 2026-06-07 05:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a322914-32b3-30aa-adce-4697507f8c57 | -11.72297 | -56.84897 | 2026-06-07 05:46:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 822338f4-2531-371a-8cb9-7a9512684290 | -9.21006 | -64.08451 | 2026-06-07 05:46:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f90ceed-be2c-3351-82eb-b4a0a65073ff | -10.59696 | -55.42408 | 2026-06-07 05:46:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d573797c-f07b-342e-a943-da36305faf92 | -10.833 | -60.7571 | 2026-06-07 05:46:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d58cba1b-a04e-35d7-9cfa-1e84a951670d | -11.54428 | -52.78778 | 2026-06-07 05:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0d46d594-4189-3634-90c7-d4481e456e70 | -10.83353 | -60.75327 | 2026-06-07 05:46:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a8a78ee8-4dbc-3f56-b265-f4b99635bb87 | -11.55405 | -52.80577 | 2026-06-07 05:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1954c4a9-9ef0-30b6-b023-b3c7d0c6d8cc | -11.5611 | -52.80659 | 2026-06-07 05:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6fed71e-4ee0-3ced-be46-08d14747ce45 | -11.54903 | -52.80894 | 2026-06-07 05:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7651b06e-7550-3bf9-9fa2-f093793571a0 | -11.55839 | -52.78945 | 2026-06-07 05:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d9ca38d9-2e7f-391d-8b36-85cf26c0612b | -10.8541 | -53.74031 | 2026-06-07 05:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a91844ce-f30a-32a1-afd8-694a7aca3e33 | -11.55133 | -52.78869 | 2026-06-07 05:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1f8e27cb-32b7-3da3-aa69-27d728af2e9f | -10.82724 | -60.76796 | 2026-06-07 05:46:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 841a1288-5740-3854-ac88-e3f8ef3f1c7f | -16.79264 | -54.16925 | 2026-06-07 05:48:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 319fa20c-180e-3b06-9845-ed06b018814d | -17.99574 | -54.27987 | 2026-06-07 05:48:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d973aff-29fd-3df6-9dca-515f7841ce5f | -16.79955 | -54.1697 | 2026-06-07 05:48:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6fa90582-8255-3b34-8f6c-567363923f5a | -16.79298 | -54.17046 | 2026-06-07 05:48:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e0efcda9-4c0e-3ff2-8ddc-3d4c727b635d | -16.80045 | -54.16484 | 2026-06-07 05:48:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1ae0ebe-6302-32db-935b-4a51ac0aab8d | -14.28902 | -57.54293 | 2026-06-07 05:48:00 | NOAA-20 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b34bf23e-e655-3fa2-b7d5-11a873b114dd | -16.79212 | -54.17456 | 2026-06-07 05:48:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9040e409-fc18-3134-b828-fc638eb59174 | -16.78606 | -54.17008 | 2026-06-07 05:48:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aee45563-2673-33ef-8288-f70190b14a13 | -16.7857 | -54.169 | 2026-06-07 05:48:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 949da0ae-a4f6-3c6c-a26d-76711bce6bb2 | -16.78525 | -54.17371 | 2026-06-07 05:48:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f560ff89-dda5-34f1-80a5-af48e056ce9e | -21.98539 | -57.61234 | 2026-06-07 05:50:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 255b4a5a-d81a-37a2-b159-151449fdafc4 | -21.98586 | -57.60711 | 2026-06-07 05:50:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0192b492-bf80-3a18-8d0e-2c6a05875b84 | -21.99182 | -57.60747 | 2026-06-07 05:50:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7c38fa4-ed40-3070-9a0e-15389f62a9f4 | -10.8236 | -60.7633 | 2026-06-07 07:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 41.2 |
| d49915dc-5bba-3eaf-9a56-5ce0dbcf38ae | -11.5516 | -52.79399 | 2026-06-07 07:01:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 6938399a-d6e8-385e-9676-a3ea35518328 | -10.82106 | -60.7526 | 2026-06-07 07:01:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 2c905afc-a8e4-3ca9-b742-11405ec25bfa | -10.83244 | -60.74323 | 2026-06-07 07:01:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 39a4b196-ff4a-3215-aac5-5402f9ae73a4 | -11.54199 | -52.79257 | 2026-06-07 07:01:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 144a077c-d732-3074-bede-1407ff878f2e | -10.83268 | -60.75454 | 2026-06-07 07:01:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 764c4c81-a800-3552-bcf9-fa2d056ca495 | -11.55311 | -52.7832 | 2026-06-07 07:01:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e3c8c295-98ab-38c4-a636-51f0fd23d16c | -10.82962 | -60.75951 | 2026-06-07 07:01:00 | AQUA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 4b8ca216-656a-378e-a33b-906b2081a106 | -21.98222 | -57.61111 | 2026-06-07 07:03:00 | AQUA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 095aecad-f811-3503-9c37-2c0b15a9e4c8 | -21.98363 | -57.60165 | 2026-06-07 07:03:00 | AQUA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 89c574ac-164b-34d2-88b7-9939fe504dfd | -16.79437 | -54.16676 | 2026-06-07 07:03:00 | AQUA_M-M | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1d8f978c-4825-3236-8e12-2c7e22601fee | -10.8424 | -60.7622 | 2026-06-07 07:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| ad0d1744-7d25-3796-8505-bf74f2c64ec6 | -10.8236 | -60.7633 | 2026-06-07 08:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 5272e26c-c2dd-36b8-ab58-4d7bc4b7e5cf | -10.8236 | -60.7633 | 2026-06-07 08:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 90657b3e-b4bd-3445-a8ee-7eb726608f95 | -10.57424 | -57.32008 | 2026-06-07 12:32:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| a28509d0-b0cc-34ee-ab5b-85e4d2ee9781 | -14.29796 | -57.53382 | 2026-06-07 12:34:00 | TERRA_M-T | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| f79aaa8f-e037-3082-a22a-b23663025919 | -14.7292 | -52.69234 | 2026-06-07 12:34:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 29.9 |
| af008213-ea6a-310f-a1b0-26b471f4ad54 | -10.82958 | -60.76484 | 2026-06-07 12:34:00 | TERRA_M-T | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c2115e1a-c165-3226-b733-138b7f34ff00 | -10.83141 | -60.75291 | 2026-06-07 12:34:00 | TERRA_M-T | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 36.6 |
| d0eeb4b6-a1e8-3c85-aec7-ca7ac95a9f13 | -11.05392 | -56.92198 | 2026-06-07 12:34:00 | TERRA_M-T | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a7a66a94-702a-365a-8dda-2f1b115a50cb | -14.28684 | -57.53508 | 2026-06-07 12:34:00 | TERRA_M-T | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 141.8 |
| 27d9b490-9079-3476-bd22-316a5960d021 | -11.54991 | -52.79336 | 2026-06-07 12:34:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 20.2 |
| be4926d8-7222-3751-9b29-b4af9162da6f | -11.26764 | -53.97146 | 2026-06-07 12:34:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 40266537-a57f-317a-9caf-c64403136d66 | -14.7339 | -52.68642 | 2026-06-07 12:34:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 38.0 |
| c66d228a-0efb-3467-b37a-89beb7a7dde0 | -14.28813 | -57.52597 | 2026-06-07 12:34:00 | TERRA_M-T | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 33aa106f-437f-3c83-b2f5-9bfe32f1066b | -21.99179 | -57.61137 | 2026-06-07 12:36:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 10.8 |
| c21a1a1f-5768-30a6-81d9-bec154f35558 | -21.99321 | -57.60054 | 2026-06-07 12:36:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a2a141f4-a519-3415-b465-924c6cd6ea4d | -21.98247 | -57.61003 | 2026-06-07 12:36:00 | TERRA_M-T | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a7bb8045-966a-3f04-9a5d-11bca4455cbf | -14.287 | -57.5434 | 2026-06-07 12:40:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 04cffe83-e7fe-3d20-89b2-8137f1c00fab | -14.2873 | -57.5233 | 2026-06-07 12:50:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 0655608d-9425-38db-9707-f0b4b9809ac6 | -14.287 | -57.5434 | 2026-06-07 12:50:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 81960461-bfbc-3030-8419-2ee96ecb919b | -14.287 | -57.5434 | 2026-06-07 13:00:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 148.4 |
| a8da1b0b-5489-340c-965a-9b15a8fd258e | -14.2873 | -57.5233 | 2026-06-07 13:00:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 964ece02-be73-3e44-b612-a2606f1d86b9 | -14.287 | -57.5434 | 2026-06-07 13:10:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 95.3 |
| cbeaca26-c5ff-3074-869c-38d88d930ab2 | -14.2873 | -57.5233 | 2026-06-07 13:10:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 93a9b9bd-27ad-345b-b8e0-a2d7e1ecabc7 | -14.2873 | -57.5233 | 2026-06-07 13:20:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 5455b3bd-bf7a-3d74-bcfd-74166934e990 | -14.287 | -57.5434 | 2026-06-07 13:20:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 7aced4bc-b809-39f6-afeb-a7f628696d5f | -14.2873 | -57.5233 | 2026-06-07 13:30:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 7373fdb2-1121-310d-8899-28b6c4325aa5 | -10.8573 | -53.7425 | 2026-06-07 13:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| a349e549-f71f-373b-9005-682790b63355 | -14.287 | -57.5434 | 2026-06-07 13:30:00 | GOES-19 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 117.7 |


[Clique aqui para ver as próximas entradas](README9.md)
