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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b493f3f-4425-3c61-81dd-94a25340378d | -17.94529 | -57.22031 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 85b4905e-1008-32cb-8b82-799f3e08e009 | -17.94348 | -57.20497 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 04dcc984-65b0-30f7-bf4a-2639139099d4 | -17.93964 | -57.2044 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 05907acc-b104-3eaa-9435-552ff99a6b6e | -17.93829 | -57.21426 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| b457ac77-6989-310c-aadf-7908e6e362fb | -17.79612 | -57.49168 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d4375553-4ddd-3017-a5cc-326b477e2dcc | -17.79234 | -57.49111 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ca1a1507-afaa-33a0-86b9-c1214f2ebb04 | -17.78857 | -57.49054 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d154e4cb-9908-3657-904a-8124f71da45c | -17.78333 | -57.52836 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 29056522-6de6-3b7e-b1f1-81401219608f | -17.78122 | -57.57124 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9cd181d5-0379-3a5a-b107-2936f4174495 | -17.77942 | -57.5566 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7c354d3f-166e-388d-9fd2-4a1aca1cb3a9 | -17.77746 | -57.57067 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 674204eb-a7a2-3415-83f1-906f346c005a | -17.7766 | -57.4936 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| aa106802-91e4-3e76-bffd-5badd7732eb5 | -17.77631 | -57.55134 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| c9f0e5fd-e465-3237-9658-0b18c9a021c8 | -17.7745 | -57.53667 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 00039004-6fbb-3a88-8295-2b87f40ff139 | -17.77385 | -57.54137 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 625da5fe-d333-3a47-9da3-37bd645992d3 | -17.77074 | -57.53611 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| ef9393c4-1039-3da9-8b05-92b0fe8d454d | -17.77009 | -57.54082 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 78200536-f56b-381e-ba30-135cd2e45258 | -17.76879 | -57.55022 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 802a51c7-ace1-3636-9522-0380c04f3c4e | -17.76633 | -57.54025 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| 3216df4e-ebaa-3ef3-b567-6ff3a1908a09 | -17.76568 | -57.54495 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 4ccefcd4-94af-3ece-9a60-9005c3827b6f | -17.76503 | -57.54965 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 267e2bbb-8963-3e90-a0f5-a5038aa6efd8 | -17.76192 | -57.54439 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 45916e9a-3617-381f-a8e8-419479feb80f | -17.7618 | -57.57311 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2881c106-68ee-38bb-adf1-8d792d626d33 | -17.76066 | -57.38425 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9ae7c455-eef2-3e48-990c-01a96af0d473 | -17.75933 | -57.56318 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| a0eb4165-50d7-30d3-b6f9-d122c178fea0 | -17.75869 | -57.56786 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 94708dd6-ab4a-3898-b8b7-8d95e5ff926e | -17.75804 | -57.57255 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| b5c4418e-e8c0-3097-94be-683152c36420 | -17.75739 | -57.57724 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 2273ed14-5355-3ce4-bb54-05eb5db4e0b8 | -17.75622 | -57.55791 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 6271937c-aaf0-3c9e-a346-12cb266741e3 | -17.75558 | -57.5626 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 33329355-2e90-330c-81e2-b19d8a192a92 | -17.75493 | -57.5673 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| 99f2a7ed-93be-37a0-a4af-5f8b46a130db | -17.75429 | -57.57199 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 6ad20b4f-73a6-3004-9349-3c7408ffdc25 | -17.75364 | -57.57668 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| eb22b39c-5f3d-3875-a31e-00cd5cd4b31f | -17.753 | -57.58136 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.0 |
| dcdffe68-be65-37f4-82ca-e97da3bbbe3d | -17.74989 | -57.5761 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 39.2 |
| 04451994-acb8-32e2-b0ac-5b1461d94cc0 | -17.74925 | -57.58079 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.7 |
| c772f48d-fdce-39f9-a775-ac37eb8d82cc | -17.71092 | -57.47138 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 77a94065-e41a-3d22-b044-2b319c510c56 | -17.70999 | -57.47397 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e19feaa9-e3d2-3dba-bd3c-bd709dea6881 | -17.70715 | -57.47081 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| ae73b1c3-9ba3-3f7b-9ca4-6b71c8a775d4 | -17.70338 | -57.47024 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 346db4bd-ba2c-3cc5-a865-e0d16f3dbf39 | -17.70308 | -57.46809 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 20fad15e-b707-3c1b-891c-59c319b35f01 | -17.70244 | -57.47284 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| dc91e616-c03f-3b98-8f13-1da3c61689e4 | -17.70082 | -57.37756 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| ae205692-3332-37a4-85f3-e5ed516d36dc | -17.69961 | -57.46969 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 0079e48e-7394-36ff-927c-e52b63f85023 | -17.6993 | -57.46753 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 662fa20f-011b-3a7e-bb1a-9b2bd5367fdf | -17.69894 | -57.47442 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 07c6c952-ff2c-3c46-9e91-b02b8a8dcbef | -17.69867 | -57.47228 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 159ef651-320e-3903-a3fc-0fb850187caa | -17.69583 | -57.46913 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 09ccaea2-a724-39a2-8bcb-0fa1c611badc | -17.69338 | -57.45909 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.1 |
| e9395ab2-5f51-3c06-b550-1cd34da92f03 | -17.69272 | -57.46383 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.1 |
| 3c55a1fc-a1e5-3956-acdc-d47659083aeb | -17.69206 | -57.46856 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.8 |
| 907683c0-3ba1-37a3-8559-8ef5c0c441e5 | -17.68895 | -57.46327 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 1a1bf5e5-faac-3125-995b-75fdf530313b | -17.68517 | -57.4627 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 0c35f68a-dc73-33f2-b8be-f6bb98a0d70d | -17.68451 | -57.46744 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 8fd540ca-6202-353f-8731-3946956bedb3 | -17.6814 | -57.46214 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| bb5b9e9a-5918-3156-8bf6-b7b85b2bbc1a | -17.68074 | -57.46688 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| d59c239b-34cf-3cba-bc34-4c6222e129ef | -17.68024 | -57.44261 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| a76af0bc-2782-3056-82eb-0f6ee06cbc37 | -17.67959 | -57.44736 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 11c6be8c-6ad1-3eea-b3ff-cf17990230dc | -17.67893 | -57.4521 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| fdd59db8-347e-3e0a-9917-4aa5d16343e8 | -17.67762 | -57.46158 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 963781a0-6ab4-3d15-bc3f-ec875a1c2f65 | -17.67647 | -57.44205 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 0f20663d-3c38-3e95-beb4-e8e7283904ae | -17.67632 | -57.47105 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 5ef37a74-a6f7-35e9-ade4-9b15bb940d84 | -17.67581 | -57.4468 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 088d1d7a-196e-3848-a4be-ac03c3418c21 | -17.67516 | -57.45154 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 69041968-fa8f-3cdd-a1b9-15021f5e94b7 | -17.67451 | -57.45628 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| abed0984-2d08-3807-83f4-dff42a6d19f9 | -17.6732 | -57.46576 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 88f4be49-aa7e-366b-84f1-1742e1b315cd | -17.67254 | -57.4705 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 27096777-533c-33f7-b7e1-b33768821e08 | -17.67203 | -57.44624 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| dc087d2b-c650-376a-9206-21de68b66588 | -17.67138 | -57.45097 | 2024-10-23 05:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 4119c4d0-7fe4-3e07-93db-01dc77c3b331 | -18.6586 | -57.33316 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 27966bec-75c8-3227-8757-b69fda972162 | -18.65475 | -57.3326 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| f5320ee8-807a-392a-bc63-134e867fc934 | -18.65408 | -57.33755 | 2024-10-23 05:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f7074445-8ac2-3f7a-9653-6bf3dc99514c | -18.16982 | -51.63578 | 2024-10-23 05:21:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e6193880-2846-3fa2-bfc9-ef04fa91e5e3 | -18.16428 | -51.63523 | 2024-10-23 05:21:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78acb3ea-e350-3f39-8e79-8cbb83deb54c | -24.00462 | -54.10446 | 2024-10-23 05:21:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 2a85a834-6c85-36dd-b5e1-1dabc26c9025 | -24.00016 | -54.09751 | 2024-10-23 05:21:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| aa99a336-f752-3a9d-9702-771f6808a8d8 | -23.99955 | -54.10384 | 2024-10-23 05:21:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| ce7f8fe9-fad4-3593-8f0d-d4bfe625e9c5 | -28.81122 | -51.17656 | 2024-10-23 05:23:00 | NPP-375D | CAMPESTRE DA SERRA | RIO GRANDE DO SUL | Brasil | 4303673 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 022ab269-94a7-3cfd-82f4-65a1bacda78d | -28.81094 | -51.18154 | 2024-10-23 05:23:00 | NPP-375D | CAMPESTRE DA SERRA | RIO GRANDE DO SUL | Brasil | 4303673 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2ce0c4fd-a7b9-3005-ba8b-8d79acaaea6a | -28.80884 | -51.17669 | 2024-10-23 05:23:00 | NPP-375D | CAMPESTRE DA SERRA | RIO GRANDE DO SUL | Brasil | 4303673 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7269e0a1-84f1-3b21-a668-2bc382f5da70 | -28.80852 | -51.18186 | 2024-10-23 05:23:00 | NPP-375D | CAMPESTRE DA SERRA | RIO GRANDE DO SUL | Brasil | 4303673 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 770751b8-3864-3ef2-8599-26694dfe2cbf | -3.1101 | -54.1661 | 2024-10-23 05:25:25 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 3fed2d03-26fc-3f47-9c7e-77217f711215 | -3.1102 | -54.146 | 2024-10-23 05:25:25 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| a1679f43-bb53-3af8-bd17-671c89a9df98 | -3.2542 | -50.1799 | 2024-10-23 05:25:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 9e186d97-8423-317e-8e0b-27dd9d3803ba | -4.1305 | -45.5888 | 2024-10-23 05:25:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 06b8914d-2895-3134-99a0-47f2d2754d15 | -4.1719 | -47.9894 | 2024-10-23 05:25:31 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 95694d1c-22cd-3a2c-a1f4-cd3b262f721e | -4.1905 | -47.9885 | 2024-10-23 05:25:31 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 681fa3c7-a103-3166-b6e6-1f6629023030 | -3.0917 | -54.1666 | 2024-10-23 05:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| f9742bde-adb5-3b13-9992-9cc88fcddaba | -3.1101 | -54.1661 | 2024-10-23 05:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 65912265-84e3-3a86-8fa9-8b0c739f598e | -3.1102 | -54.146 | 2024-10-23 05:35:24 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| e9b0f677-300f-3f63-b5e8-0429b9bf94a5 | -3.2542 | -50.1799 | 2024-10-23 05:35:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 26bdf7db-39d4-3772-a3e2-3bc534ebdba1 | -4.1305 | -45.5888 | 2024-10-23 05:35:30 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 408c4f5e-2b79-3926-a69c-226e6f5dd94b | -4.1719 | -47.9894 | 2024-10-23 05:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 544f876e-ecf1-3831-a651-17eb5ea3d4be | -4.1905 | -47.9885 | 2024-10-23 05:35:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| fe3a1065-6215-3071-af35-e0baceb71f92 | -0.11737 | -51.64289 | 2024-10-23 05:38:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 00ee4014-df84-3b05-b55a-8e486745fa61 | -1.39176 | -51.99866 | 2024-10-23 05:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6aa50f05-09c1-317b-bd84-79b48471ab06 | -1.39144 | -52.00117 | 2024-10-23 05:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ef37b77a-7ab9-3645-b01c-f9cf03caa695 | -1.39092 | -52.00406 | 2024-10-23 05:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a5712c61-25e7-3628-a222-7931f8b1f9a3 | -1.38612 | -51.99216 | 2024-10-23 05:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2b6350e6-6fec-3a84-8f1b-db5c098d1ea7 | -1.38527 | -51.99759 | 2024-10-23 05:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README60.md)
