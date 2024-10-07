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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70f0fd75-4925-3db7-a0a0-4950865168a1 | -19.15859 | -50.64292 | 2024-10-07 05:21:00 | NPP-375D | SANTA VITÓRIA | MINAS GERAIS | Brasil | 3159803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d0abc369-9192-350c-8a5a-6f7d344847d7 | -21.20159 | -50.97734 | 2024-10-07 05:21:00 | NPP-375D | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0c92498a-4e25-34fc-8d34-66fa2364a497 | -21.20118 | -50.98186 | 2024-10-07 05:21:00 | NPP-375D | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 114915b0-6b43-3d14-8584-54d989776be9 | -19.39398 | -51.69038 | 2024-10-07 05:21:00 | NPP-375D | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 298df2a5-e7ea-32ca-a500-d88ea0405210 | -22.71684 | -53.22517 | 2024-10-07 05:21:00 | NPP-375D | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c5487cd2-d6f5-3cb2-b26e-0b261db2db27 | -22.7165 | -53.2286 | 2024-10-07 05:21:00 | NPP-375D | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 299d257d-cebd-3f26-a456-f0e5530ccb5e | -22.71615 | -53.23203 | 2024-10-07 05:21:00 | NPP-375D | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 296e152d-1a0a-3d04-9d3c-441a28f6d7c2 | -22.71611 | -53.22648 | 2024-10-07 05:21:00 | NPP-375D | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 79e06583-be82-327a-86e3-24a93433d35e | -22.71579 | -53.22992 | 2024-10-07 05:21:00 | NPP-375D | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6ba9483a-4a72-3a58-aa1b-2da80a729082 | -22.71546 | -53.23335 | 2024-10-07 05:21:00 | NPP-375D | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 9346ee34-038d-3bbf-a2ec-602d74445bdb | -22.71157 | -53.22455 | 2024-10-07 05:21:00 | NPP-375D | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 375d3dc4-941e-3b3d-93ff-2fff6f615e6a | -22.71123 | -53.22799 | 2024-10-07 05:21:00 | NPP-375D | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 904d461f-edcb-3773-8aa4-7983d37bf074 | -22.71088 | -53.23142 | 2024-10-07 05:21:00 | NPP-375D | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| c5d7da7a-3845-33be-8a85-3db1a2b71ab8 | -22.71084 | -53.22585 | 2024-10-07 05:21:00 | NPP-375D | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 8ce87c38-88ec-3cef-88b7-769595dda7a4 | -22.71052 | -53.22929 | 2024-10-07 05:21:00 | NPP-375D | BATAYPORÃ | MATO GROSSO DO SUL | Brasil | 5002001 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 5e676903-564b-3833-a4cc-0d60fa011346 | -17.84378 | -53.78874 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dfe40fb2-555d-366a-971d-c33edb7c0ba0 | -17.83952 | -53.78373 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 43629feb-5743-3a21-828e-9a894a45c4eb | -17.83888 | -53.78915 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 77cd94b7-6c9e-3727-8627-2fccf46dc5b9 | -17.83536 | -53.77792 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ece51023-cc40-3bf3-bbed-17e31edf6e38 | -17.83405 | -53.78906 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| fac7fccc-287f-3d73-b640-7902ce257b61 | -17.8313 | -53.7712 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ba82e377-67d8-3273-bc9b-751bf5574334 | -17.82648 | -53.77094 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1bb3a225-060b-343f-85e5-c3667aa4ba6c | -17.81203 | -53.77009 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f683191f-ba8f-3c43-81f3-17b79afb0679 | -17.79595 | -53.78339 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4c3514a5-3e74-3d32-8287-023176ce9d05 | -17.778 | -53.77092 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09809428-cb2f-39e4-bab2-91854628ab9d | -17.77741 | -53.77612 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4fb9f932-2ee8-32bf-af7a-c561e8a245fb | -17.77265 | -53.77534 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 14cbefc4-d8fe-3b3a-8d16-48555a19eb63 | -17.82714 | -53.7653 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5cc4b433-ce90-3656-bf84-946e0b092e92 | -17.81271 | -53.76424 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d4b72d5e-c55b-3e66-aaa7-856e5588285c | -17.80371 | -53.75825 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7b068376-f5f2-34c5-aaf7-fca6a060ee21 | -17.80296 | -53.76468 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7cdd9775-1ae9-3fa7-a18d-b56133684729 | -17.79882 | -53.75856 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a37b4866-c3d9-37d3-b3a7-ebe2ba6caa04 | -17.78932 | -53.75675 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5ae6bd1d-5c14-37ce-ab6a-13ae74df6685 | -17.78877 | -53.76129 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5755e71d-daf6-3558-bbf5-c2d2234a4b97 | -17.78394 | -53.76138 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 03abce91-2582-302b-a416-3be222ebbdad | -17.78334 | -53.76668 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 88c3c5e6-5e39-367e-89e5-6f0075d1160a | -17.77919 | -53.76052 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eaa86677-b938-3c9e-9f93-2ceedd21712e | -17.7786 | -53.76571 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ceaed2af-7595-3f34-8c9d-04a2c719924b | -17.77441 | -53.7599 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3bced79d-fda7-3534-b4f7-7f0d44154345 | -18.46927 | -53.51591 | 2024-10-07 05:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1493ff9f-6f9d-3ccc-a9a4-61f45dd180c7 | -18.46499 | -53.50969 | 2024-10-07 05:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3cd5916d-8aac-3d50-88af-0a0c2864f948 | -18.4644 | -53.51498 | 2024-10-07 05:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7f9ecfac-f06f-3ef7-b87b-5eccae72cb33 | -18.46381 | -53.52023 | 2024-10-07 05:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 294deb87-6ab6-34ac-b597-1e53eb7bb98a | -18.46131 | -53.4981 | 2024-10-07 05:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8797cd3b-2971-3c99-b0ce-7d335b6f460b | -18.46072 | -53.50335 | 2024-10-07 05:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f353a239-b550-3497-8653-01a19f1e4cae | -18.46013 | -53.50866 | 2024-10-07 05:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ceacff3-fd1e-37a8-88aa-d41f71d52114 | -18.45954 | -53.49582 | 2024-10-07 05:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c4b8ef37-125b-3aab-9961-1874a3d621c5 | -18.45953 | -53.51403 | 2024-10-07 05:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8402e386-e3c9-3195-8c02-f69ce425a2bc | -18.45893 | -53.51944 | 2024-10-07 05:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c535409e-ba1a-3be5-8648-7b43d85b9fca | -18.45893 | -53.50101 | 2024-10-07 05:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d76ade75-870a-31c3-a5de-7c5ecece13a3 | -18.45831 | -53.50623 | 2024-10-07 05:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c9e10bbf-c0e3-3a7d-9bcb-3b624770c28f | -18.45767 | -53.51159 | 2024-10-07 05:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ae4c4f8f-cecb-344e-8efc-5713db530972 | -18.45703 | -53.51702 | 2024-10-07 05:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7957166f-2ffa-355f-af34-0bf751b77f04 | -18.45642 | -53.49734 | 2024-10-07 05:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 59defd70-1d93-3010-a2f9-342994174d66 | -18.45585 | -53.50238 | 2024-10-07 05:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 0a0463d4-1a05-3318-9b98-a94dbf45ee1b | -18.45527 | -53.50764 | 2024-10-07 05:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 10.4 |
| f5245e8d-e96d-361b-a5d5-3132e95d2d91 | -18.45466 | -53.51309 | 2024-10-07 05:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6ec3fa49-9f7b-30eb-a155-428a49444f73 | -18.45464 | -53.49514 | 2024-10-07 05:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2cb085a0-071c-367b-9de8-60690341602e | -18.45405 | -53.50019 | 2024-10-07 05:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2964e825-b51e-3383-9980-be81cc336ee9 | -18.45404 | -53.51865 | 2024-10-07 05:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1a637e77-c0f7-3ed8-a629-91ba58d22433 | -18.45345 | -53.50527 | 2024-10-07 05:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 16bf6fa0-2dd4-3be0-946b-79ac7593eacb | -18.4528 | -53.51073 | 2024-10-07 05:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 95edaf30-1d59-3850-83e7-c4afbe5931d4 | -18.45214 | -53.51631 | 2024-10-07 05:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2c174a07-2e70-30e5-8d65-12aecb38d41c | -18.45151 | -53.49669 | 2024-10-07 05:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 23f96df5-955e-3d8d-b0ef-5550ef6f1f87 | -18.45096 | -53.50167 | 2024-10-07 05:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 10.4 |
| a87307d1-173d-3917-8524-183d620badaf | -18.45037 | -53.50694 | 2024-10-07 05:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 9e2f18d2-11c7-3c81-a5a9-ae44053b0a51 | -18.44914 | -53.49959 | 2024-10-07 05:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 31b6b19e-1eae-387e-864e-2c289d77051c | -18.44854 | -53.50466 | 2024-10-07 05:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 177076e0-babb-3855-9229-d2454a6ca8b4 | -18.44547 | -53.50632 | 2024-10-07 05:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c4f700d8-fb1b-32a8-9fba-e74cfd6f5e9e | -18.44364 | -53.504 | 2024-10-07 05:21:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88a6b623-9852-3424-8136-6f4c7680d7dd | -17.83835 | -53.79362 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7a67e2bc-254f-3c67-888e-a28db09e81dc | -17.83778 | -53.79846 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 978e6c03-8cfe-3f39-8069-08bb37ffdef3 | -17.83355 | -53.7933 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 96d81407-9107-358a-b2fc-71f2b3e0599e | -17.833 | -53.79794 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a44b71a2-6b86-32e6-a88c-a028139ab555 | -17.82875 | -53.7929 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 1078582c-b74b-3d9b-bb93-f2534fd4e17c | -17.82821 | -53.79746 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 86c361d9-2dea-39bb-9233-6337ca6bb174 | -17.79838 | -53.80421 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f93ded42-519d-3253-8e07-77346effd37e | -17.79539 | -53.78827 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f079c01a-f2dd-34b3-81bd-52b6cbd85bd9 | -17.7942 | -53.79855 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e5698afc-0aaa-38f5-8ac2-e252e2683770 | -17.79361 | -53.8036 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a65184df-6e5c-3e08-8f88-73b72624d91c | -17.79302 | -53.80873 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 663e89b9-68d6-3cbc-9f12-f58c159fb384 | -17.79242 | -53.81393 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 7a832657-22df-32a8-ae85-c3664ca20780 | -17.7911 | -53.78351 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4c7e2029-2816-3695-b15f-63448f22422f | -17.79051 | -53.78863 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e10a1949-9f26-390f-9df0-e89004eb0a80 | -17.78994 | -53.7935 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d12525e2-9a4f-362c-b351-2905842f5b34 | -17.78939 | -53.79832 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0b304214-251a-3447-81a2-1d267c5bd8d5 | -17.78883 | -53.80311 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 6d17872a-3c47-3e20-aad2-0724efd37314 | -17.78825 | -53.80816 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c0868ce3-2666-3125-97ea-c46a4a4fcab5 | -17.78765 | -53.81334 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e83db8a2-babf-3455-a879-974a886ab0b3 | -17.78705 | -53.81855 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| b61bba34-d841-3c4c-b985-e9f546d39874 | -17.78514 | -53.79321 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a5378fbd-591b-3e83-9558-e878c17a2456 | -17.7846 | -53.79791 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9c3edceb-1b21-38f3-9542-fd65d6900832 | -17.78443 | -53.79685 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7fcd8145-c93d-383e-ace4-31877fe85ee9 | -17.78404 | -53.80272 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 98265305-175f-33e2-bd8c-8d48aa7b8898 | -17.78385 | -53.80164 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 932926ae-25fe-373c-93f1-d536e12f0120 | -17.78347 | -53.80772 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 44cf42c0-1db5-3411-a5c6-87d51f82d858 | -17.78325 | -53.80658 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 2186738a-b0cf-3f90-b684-80234e7dc435 | -17.78289 | -53.81279 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a1fda51c-9a43-3216-bf3b-7bd26bd61fc2 | -17.78263 | -53.81161 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5fde4395-8934-3d58-b263-cdf85de41e37 | -17.78229 | -53.81798 | 2024-10-07 05:21:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README129.md)
