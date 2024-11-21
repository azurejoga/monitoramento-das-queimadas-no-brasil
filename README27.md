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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 475ff64f-eb3b-37e5-8db0-3e9d2419022c | -3.46467 | -50.00984 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 338d9acb-11f3-39b8-b499-f26f04bb1b70 | -2.63348 | -46.57076 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c9e1573-b572-34a1-979e-9cf56f7e2d4e | -2.58735 | -51.72206 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cea14d93-7de2-3e63-a06c-7625235e73e7 | -2.51352 | -47.22673 | 2024-11-21 04:29:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33628121-afdf-3fda-bc45-6b4a64b2aa2e | 0.4009 | -50.79951 | 2024-11-21 04:29:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6cf88857-bf59-3aed-8c78-b94c8a0ba4cf | -1.74161 | -50.48037 | 2024-11-21 04:29:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a49fce07-dbf4-3cd1-8bc5-6008de68f60b | -2.84179 | -46.68849 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 65a324db-4049-3120-946d-79d16f1472b9 | -2.60928 | -48.24511 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afa2e80f-fe31-3b38-82e1-c51439009bf0 | -2.43314 | -46.5326 | 2024-11-21 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 480838b3-ae1f-32fb-8e0a-dac7790ba804 | -2.10358 | -46.62556 | 2024-11-21 04:29:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03893a96-fd17-3f25-acc5-62d0747d7a02 | -3.60245 | -49.86855 | 2024-11-21 04:29:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94272de4-098f-34ea-8852-f8b80a20e33a | -4.07377 | -46.83815 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 381c2b05-e4b7-37c7-99cb-cb17a8ef8172 | -3.35442 | -46.63768 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aa477521-76bb-3dcf-ba4d-0a8590b7cddc | -4.18629 | -46.83442 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c1a4dfb-d96a-3712-9b85-9970d9922aa1 | -2.54352 | -46.22025 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae2c2c24-b0c5-3c36-a88c-f8a036466eae | -1.74154 | -52.05638 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d65528d1-c723-3c04-8d07-417d93648de0 | -2.69445 | -46.24703 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d7451f62-e372-332f-937a-cb85080cd7ef | -3.41869 | -50.25296 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a51b3b5-2ebf-3df6-93e0-83fe5f6e496e | -2.74428 | -51.82954 | 2024-11-21 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19bd3af1-a023-3416-aa98-8c4ef45c9ac5 | -1.19571 | -53.67946 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b1de8583-e256-3462-a627-c32d54e816b0 | -1.21126 | -51.75849 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f67694aa-4054-33a5-a3b1-16d31cfb1f7a | -3.09862 | -53.2156 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ac69b3c9-fb2f-3355-ae97-6f31b1c29b2a | -2.40111 | -48.61081 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13644a1e-cd7b-33d1-84be-4fb6a931e69b | -2.6307 | -46.56678 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 342986df-5db1-329d-af73-cfe60720da4d | -2.40391 | -48.6113 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ffb150b-94fa-32e1-9368-1c4fb3f9a056 | -2.63402 | -46.5673 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0860b407-b573-3380-8a67-b2282aa28c4f | -2.75016 | -52.1004 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 592eb1d6-b666-3590-bc61-7a77c6df2402 | -3.57151 | -50.41712 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5835e596-386c-3cc2-95fa-9fcf249f19bf | -2.62696 | -48.06868 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f1521d8b-8428-3538-a564-ea52afb8bee6 | -3.55372 | -50.24717 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4ebd9d93-6433-3971-8a29-fbffb2513895 | -1.73849 | -46.68843 | 2024-11-21 04:29:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dc6ed62-a2ce-381d-a791-16694295155f | -2.11734 | -48.54834 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f88ed095-77c2-3332-bce4-9ac2e85953aa | -1.49555 | -49.68233 | 2024-11-21 04:29:00 | NPP-375D | SÃO SEBASTIÃO DA BOA VISTA | PARÁ | Brasil | 1507706 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 09d6c464-81df-30c1-a0ea-51c86d182ffe | -2.37026 | -53.8275 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5aeb8104-b88b-389a-a9f5-442dc0267d50 | -0.91375 | -51.77957 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ac03965-f246-3d27-845b-707db97b7165 | -2.61978 | -51.80225 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2a22d7c0-6cae-36b3-b505-c9e8224d3149 | -3.74773 | -47.3604 | 2024-11-21 04:29:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae9fd997-8aa4-3a1f-a7d9-4e3976cd35c5 | -1.52635 | -55.37975 | 2024-11-21 04:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b45d2a0e-33d8-332b-a20f-dbbf4727417b | -1.56285 | -55.11912 | 2024-11-21 04:29:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8970e169-bfb4-36f0-b323-0b5b9aaf365b | -1.51198 | -52.0635 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffc1abb2-cac8-3998-a2d7-acb3c4248499 | -3.08495 | -49.4707 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02ed22cf-bfdf-36bd-b12c-edf9d69c7683 | -2.24874 | -46.8246 | 2024-11-21 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3c4c36bf-155a-33c2-a961-31b6a322d7eb | -2.06421 | -53.43492 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2436669f-20cd-3808-ba85-9c6b2e9518f0 | -4.16466 | -46.82043 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b168ec6d-5884-362d-bbaf-d1355b64e383 | -2.26944 | -53.75484 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 39f516a1-7e5e-3f3f-bbab-32624b996eee | -1.22233 | -51.7416 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 975086a9-f902-3ccf-9786-96bde3976b54 | -1.64946 | -52.67283 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bba843dc-3280-31c3-847a-3330fbe8823b | -2.57955 | -47.0214 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89fd655b-bfc2-386a-973e-df4f06a078ca | -2.28062 | -48.48697 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4aa003dd-dd11-3544-bae1-da5b1a4d080b | -2.78989 | -48.60293 | 2024-11-21 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1805fe1-a75f-30fa-b2fb-c6ddacaa1d18 | -3.8469 | -46.6435 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0b88c488-6e00-3d18-a483-89a76e03611e | -1.41522 | -52.82269 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e9944d9-029a-372e-8d6e-aee8fb6df632 | -3.07177 | -51.25504 | 2024-11-21 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53c060c1-3940-3981-b319-c2a010f64cd5 | -2.8296 | -46.67952 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62244b4d-ddf8-3110-9af7-0ec1cf73aca8 | -2.20295 | -46.38313 | 2024-11-21 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59df8d52-96a1-3639-aae7-becebb08a6ac | -2.4264 | -49.02473 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df8f8abf-1ae2-3971-a170-5afe43c7e8ec | -2.91621 | -46.8377 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c998f86-b928-3c94-92f6-6c2e8aca7571 | -2.60989 | -46.80727 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f36b9228-945f-3316-8c0a-00650b4567f8 | -0.8971 | -51.72417 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1e680abb-0def-383b-ab57-8f1472713418 | -1.20283 | -51.97337 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ac8b07bb-6e64-3af0-8f33-ae85a2a01317 | -2.82682 | -46.67556 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eadd15e7-b17a-3eb1-b1a6-c81a79b79735 | -3.06831 | -53.28924 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 70387f54-01f3-30bb-a6fc-8ea4003ca67f | -2.91899 | -46.84166 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26b9f1ab-79b7-3174-9dc0-53090eb09618 | -2.19651 | -53.65882 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| fed0a980-4866-39cc-9196-5096cd62fd13 | -2.44892 | -53.68615 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a29ace84-8fdd-3199-8204-bbd49605b38d | -2.40345 | -47.64374 | 2024-11-21 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5675e57b-bd6f-3d47-9cf3-e1c99dca063a | -4.18683 | -46.83096 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8c4da90-8782-3a36-9b9a-aabdcf4c6228 | -2.59947 | -47.0245 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c7d909c-61e8-3fd5-8d98-3addb1a2dde7 | -2.83661 | -51.8224 | 2024-11-21 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| da6f904a-cec9-3d70-a3e1-e3b448677fd4 | -2.30239 | -46.05057 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4d08be56-2f2d-33d5-91d0-8894edac8aea | -2.69336 | -46.25397 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d1efcd9b-807a-3ce0-aa27-c0b89431562a | -1.14009 | -51.68441 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f53751bb-d0d2-32b4-a66d-e16733c0f59f | -2.39545 | -49.06276 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07b57d8c-1007-3492-bf58-4292f98b7532 | -1.47144 | -52.80817 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1a3a56a0-1959-37c9-ae40-d282323ac08d | -1.64115 | -52.61268 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2a7d0f61-55a7-3e79-9296-1838768eb0ed | -2.19938 | -49.54865 | 2024-11-21 04:29:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17f2810b-38ba-3d11-8362-945fed52877d | -3.88571 | -46.65664 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8961b705-a4e7-39ae-9165-27797bca2514 | -0.17083 | -51.6239 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e5c3558-6454-3961-87aa-838a69fafc23 | -2.6152 | -51.8051 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 93ee8f40-ecfb-33b1-9690-3942e2c91b7c | -1.11045 | -52.12245 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| afec1bde-147e-3b00-aa6e-5ed1ac0b1840 | -1.79036 | -47.19529 | 2024-11-21 04:29:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 782ccaea-6fb8-389f-bf56-faf5d8f75acc | -2.27166 | -49.09443 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ad61c05-9e7d-397a-8888-f9dfa35b35fb | -2.14965 | -53.57147 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0ae3b989-aa30-360f-b742-26bfbb535060 | -2.94536 | -45.19475 | 2024-11-21 04:29:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0db28b5e-37c3-36f9-b04a-6226ab48ba9e | -3.41936 | -50.24876 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7100237-2815-3cce-8894-cb322ff73093 | -2.19717 | -49.74756 | 2024-11-21 04:29:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b985df3-861f-3efe-a9ba-81dd63ba95cf | -1.41035 | -52.1095 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4c5bd23d-a212-3529-b7ed-fc0b897fffb7 | -2.55198 | -47.28239 | 2024-11-21 04:29:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 219ab05a-e3c9-3193-8cb6-3fef5c31086e | -3.02682 | -51.5284 | 2024-11-21 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 65acdca6-7a16-37ff-bd0a-8d7d8adbd9f9 | -1.65456 | -52.52756 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71c979a0-455e-3abb-9440-1dd173fa7aba | -2.59834 | -54.01333 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73d6226d-c607-36a6-aaad-56638eb0dc3a | -1.7807 | -53.59715 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 39973df9-0697-37fb-a9ed-d42a8795b1d5 | -2.83768 | -54.01115 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa37bfc6-20dc-33be-bde5-01dc479adba8 | -2.60988 | -48.21951 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8ab2650-5859-3e75-a586-e3d351bec4bd | -1.60159 | -46.86819 | 2024-11-21 04:29:00 | NPP-375D | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 86279157-7dfd-3bc9-a381-efcf7b2a746a | -2.01969 | -51.17425 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 950817b8-f79c-3a16-a312-e1c70fab24d4 | -3.96015 | -46.72136 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be1cd37d-3e43-3fe0-a7b3-f74871b1c6c9 | -2.42185 | -49.00845 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 870205c9-6de0-39f3-a0b3-e222c53c19db | -3.36275 | -50.18401 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40580441-aa55-36da-a8de-7b2f0caaef5b | -2.73734 | -48.64723 | 2024-11-21 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README28.md)
