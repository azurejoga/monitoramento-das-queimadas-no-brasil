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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fac274db-d30c-3829-bf29-dba07f7e4e96 | -15.29298 | -52.81271 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0902091-f61f-3ecd-ae8d-3ce45ebdf06e | -11.6897 | -54.59181 | 2026-08-24 04:27:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ef0c32a6-48f6-37dc-a249-442e6ff2a84a | -12.89382 | -48.48932 | 2026-08-24 04:27:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d5b4729e-936d-36c4-85f3-7e57e8f99d61 | -15.26903 | -52.85486 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 28235d6f-fc70-3747-9eb1-5bc3c29b6c13 | -15.04985 | -48.69218 | 2026-08-24 04:27:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30eb2061-8275-3b4c-b378-dbc704a976ba | -16.4199 | -49.91333 | 2026-08-24 04:27:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a30992a2-50f6-37fd-8969-fb9da3ef605b | -14.29911 | -53.21639 | 2026-08-24 04:27:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0816e6cb-c785-353a-b408-982da4b55a72 | -12.11336 | -50.61676 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 2b088a0a-3d7a-357e-bb34-bec591d8e82e | -11.59871 | -56.28968 | 2026-08-24 04:27:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b71fe351-2635-30c4-8a16-ccf173cf187c | -16.0645 | -50.45012 | 2026-08-24 04:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2ee4644a-c7b1-3c47-a44f-15e5d9b7426d | -15.51394 | -49.83447 | 2026-08-24 04:27:00 | NPP-375D | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8094ab45-dc1a-383f-8618-0ffc3e7d6669 | -16.05072 | -50.4284 | 2026-08-24 04:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c92737e5-c19e-33d7-8d61-77c62d915db7 | -17.43159 | -48.83134 | 2026-08-24 04:27:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 087ae132-e760-30d8-b08b-f770c42dccbf | -16.05753 | -50.44329 | 2026-08-24 04:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9739ef03-a289-331d-b584-2c89decff777 | -11.1585 | -54.00708 | 2026-08-24 04:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12fbb3f8-8b60-37b2-8679-a8b066048e20 | -14.78394 | -48.77848 | 2026-08-24 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb749e40-5521-3d6a-8bd5-d3b66b58e97c | -11.20354 | -55.0489 | 2026-08-24 04:27:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 15293a29-f9a8-3460-91cb-823bef5f9ba9 | -16.08764 | -52.34043 | 2026-08-24 04:27:00 | NPP-375D | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 913806b5-8f3b-34a5-ae15-169592b1dcb6 | -13.27935 | -51.43106 | 2026-08-24 04:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 864e89ab-59c9-3805-ac7c-ab100a20e143 | -11.91112 | -55.90444 | 2026-08-24 04:27:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fefca82b-e027-3939-9871-c83a4a762813 | -16.46059 | -43.43895 | 2026-08-24 04:27:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97ec3f99-78b2-333d-97bb-7086b78dfc70 | -15.27455 | -52.87731 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4abc8708-5a34-37d8-9ffa-c96da4b137da | -19.02337 | -47.06268 | 2026-08-24 04:27:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 996220f1-cd0c-3b2f-bbec-9ef2fe7d4415 | -18.33414 | -43.90782 | 2026-08-24 04:27:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5556b302-68ad-35f5-a07a-0eeb99dc66c6 | -15.31855 | -46.05709 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7e8adf11-88e1-3379-ae70-0e2e7942cc08 | -12.89009 | -48.48868 | 2026-08-24 04:27:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 479360c2-f1b5-3a8b-84d3-dcb7f8de8956 | -13.17675 | -51.39911 | 2026-08-24 04:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 93f963a4-224c-3ddf-b3fa-4046a936d3d2 | -15.36615 | -45.59253 | 2026-08-24 04:27:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0c588af4-32b5-3832-bce4-75df11d20139 | -15.22858 | -52.78582 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1092c34b-c482-39c4-af13-ab08bbf824ca | -14.40159 | -51.77847 | 2026-08-24 04:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d009cfd8-41df-3d1f-bafc-acf8dee4f340 | -18.52378 | -47.17281 | 2026-08-24 04:27:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f46c2b99-a46e-3d84-9a5f-ab95f7ff33ab | -15.58935 | -56.00851 | 2026-08-24 04:27:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5bffcc2d-f085-3f83-b4cf-23a5f95e2d4c | -14.32229 | -51.75794 | 2026-08-24 04:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 825a3c33-2217-3926-874a-6e9972731161 | -12.74732 | -46.45002 | 2026-08-24 04:27:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4ed52cfb-0461-340a-adbc-ea622645b935 | -15.29766 | -52.81371 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| abd0f014-aa08-32e9-a6e4-a95cd6dbd418 | -15.79283 | -56.06827 | 2026-08-24 04:27:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9dd91726-bf9a-3ff3-907c-3e56dd0da8f2 | -12.86206 | -48.47314 | 2026-08-24 04:27:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d150e06a-ad09-3a08-bd16-b3470ac965d0 | -12.85206 | -48.48646 | 2026-08-24 04:27:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b13cd97d-de53-3b91-a6c6-6e8840984a07 | -16.05256 | -50.44783 | 2026-08-24 04:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7bac5c65-10ee-39c6-ae41-991b279538ad | -17.42651 | -48.83921 | 2026-08-24 04:27:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 53ab7f3e-4f26-3396-bb17-cde102dd80ea | -17.42798 | -48.84576 | 2026-08-24 04:27:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bff01b0d-287a-3b12-b543-eeff20454cee | -12.1098 | -50.61181 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d3474a6e-1a2d-32f5-a7a6-edd7431508ce | -14.34009 | -51.76149 | 2026-08-24 04:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e3e522d2-2d1b-3e11-bd81-bf372b92d762 | -15.26372 | -52.83138 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ee5b18ea-6cbf-3d6a-8dc6-66be96ea4723 | -11.85483 | -51.68531 | 2026-08-24 04:27:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d30c34f-e2be-3f94-9906-812807b54595 | -12.84827 | -48.48615 | 2026-08-24 04:27:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ebc3e5c8-7588-3f4d-b052-9c9b638b30db | -15.40263 | -55.78131 | 2026-08-24 04:27:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1e6054a5-87ae-372d-bc35-5a29c6a70e09 | -17.43648 | -48.84553 | 2026-08-24 04:27:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 56789a90-c030-3602-9c6e-528a5335816b | -16.38916 | -51.82372 | 2026-08-24 04:27:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f71c6304-3f0d-3a30-ae5e-1291161ce639 | -12.89262 | -48.47391 | 2026-08-24 04:27:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c4a3ba95-1e10-3703-8850-b265c0c07134 | -14.79942 | -48.77697 | 2026-08-24 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 214afc07-287f-3fbc-af74-6fc3dd6bc2c1 | -16.20046 | -57.76055 | 2026-08-24 04:27:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3671eed9-7465-3ac6-a470-760b555448c5 | -15.26533 | -52.84858 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7b0e6f6f-3d2b-3455-9fe0-beea50fade1e | -14.77658 | -48.77708 | 2026-08-24 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bcfeeb3f-d79d-3716-8baa-6f66768a37cd | -14.28664 | -51.79135 | 2026-08-24 04:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c054a3d-9922-36b6-b32d-1829f6b2d46b | -16.05085 | -50.45074 | 2026-08-24 04:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3c51f740-9b6a-3269-9ba7-3b1e0c77ef35 | -15.06753 | -45.32679 | 2026-08-24 04:27:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fabfe403-9e9b-313f-b517-4dd86b6b7276 | -14.78763 | -48.77911 | 2026-08-24 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8283830d-e23c-3a06-b4c6-6d904c5592bd | -13.27501 | -51.44164 | 2026-08-24 04:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9bfe694d-e572-3fb3-a857-f61d4d195434 | -12.09973 | -50.61845 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b20aa767-c05d-3bf6-972c-d94480b36b3f | -15.34988 | -52.77032 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cf522e68-4a25-3fb9-9c37-3e09d9190f91 | -14.79278 | -48.77138 | 2026-08-24 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 16418c5f-c1fb-3435-b405-21a7e537e9f1 | -13.17974 | -51.39769 | 2026-08-24 04:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 490129f6-ac50-3db1-98eb-42728df6909e | -19.76509 | -44.24327 | 2026-08-24 04:27:00 | NPP-375D | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42086005-db06-30dd-a66e-977dbe2968b6 | -17.43084 | -48.8356 | 2026-08-24 04:27:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1acd3670-7e6a-3b3e-b13b-b4488223150c | -16.06849 | -50.45085 | 2026-08-24 04:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dac26074-64ed-3a9e-8b4b-1c6edeec4f8d | -15.26267 | -52.83686 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 96e2b7ff-b59d-3577-b008-688deb0bcf11 | -13.16343 | -51.3965 | 2026-08-24 04:27:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bb4a6af4-a310-3359-9e7f-9de11fec1b5e | -15.27131 | -52.87313 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dea05268-83aa-31f5-a7e9-8737021aec73 | -15.27241 | -52.81812 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a6539c38-6ff0-3162-9cda-37ec5b07c391 | -13.09027 | -43.35251 | 2026-08-24 04:27:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16a02cde-4aac-35a9-8056-361da9eb2ee1 | -15.03233 | -48.68433 | 2026-08-24 04:27:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d3870038-8440-3b3c-8086-7cbef4ae34e2 | -18.31875 | -47.20612 | 2026-08-24 04:27:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6bc0837b-b886-351b-83ee-9d569487c393 | -17.43441 | -48.83629 | 2026-08-24 04:27:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7cadcec-d8fe-395d-8a2e-55a023030852 | -16.86733 | -49.44744 | 2026-08-24 04:27:00 | NPP-375D | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82e7d0fc-06d9-3a1d-a093-8db9ff78bcd5 | -15.23219 | -52.79234 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a0bcd3e-aa90-3bfd-8b70-c77f5765f0c1 | -12.11771 | -50.62536 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f2d38c67-b3df-373d-af46-374a39cb63b7 | -12.099 | -50.62259 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0dd92970-13cf-35fa-89fa-59cc8c81fdf8 | -16.41361 | -51.83645 | 2026-08-24 04:27:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ef31962b-9ca3-37fe-8098-7cf70dbe4164 | -16.08586 | -52.34979 | 2026-08-24 04:27:00 | NPP-375D | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b358ea0-b11b-3ea7-9442-dced3869db44 | -15.28177 | -52.81334 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 662836b6-f092-347f-b2f2-ce4363d70c9d | -13.51328 | -42.77292 | 2026-08-24 04:27:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 991d1103-84c2-3860-a14c-6af8b1fb1475 | -14.77946 | -48.78233 | 2026-08-24 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 138485e0-c43a-3fc1-a1c8-5d36776cff13 | -14.34095 | -51.75695 | 2026-08-24 04:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cae154f9-9f5f-3645-ab3b-0eed7acb142d | -16.39859 | -51.82118 | 2026-08-24 04:27:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0638c2d3-da57-3629-ae9a-a19e08711ad0 | -12.71967 | -48.39708 | 2026-08-24 04:27:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cc0d6ed2-b376-3b50-8a50-1ebcb1dd0fce | -13.09703 | -43.35358 | 2026-08-24 04:27:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 600593ec-24d0-3ed5-bc4c-24949d39650e | -19.0127 | -42.1309 | 2026-08-24 04:27:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 6d7833c0-da94-313c-b391-02fc717e23a3 | -15.51315 | -49.8376 | 2026-08-24 04:27:00 | NPP-375D | CARMO DO RIO VERDE | GOIÁS | Brasil | 5205000 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 47a848e2-001e-31b4-a0c0-8eca6dc09334 | -14.32143 | -51.76247 | 2026-08-24 04:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 93b6962c-8441-32ba-bdd1-a90488795935 | -14.78541 | -48.77002 | 2026-08-24 04:27:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ac765201-2788-344e-a7a2-7c1f5c35ec1f | -12.09128 | -50.59124 | 2026-08-24 04:27:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| cf0afe15-0d99-326c-895a-b274cedaaf98 | -11.85945 | -51.68623 | 2026-08-24 04:27:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b5e17c6-516a-3627-8a6d-e9e5c8a40e7d | -11.69248 | -54.59305 | 2026-08-24 04:27:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4df4065c-b3ad-3d19-918d-57a07553e1ae | -18.53111 | -47.1703 | 2026-08-24 04:27:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7ae7e86a-55e6-31f7-a64b-20815926146b | -15.26065 | -52.84753 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf5e04b2-8534-356a-9226-df706af9caf3 | -13.89112 | -54.03442 | 2026-08-24 04:27:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d6ffa677-1dea-3eee-9b6d-46ec8deada72 | -15.26841 | -52.83239 | 2026-08-24 04:27:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7172e431-0968-3d38-8ea8-1aaa6e3f3567 | -15.36947 | -45.5931 | 2026-08-24 04:27:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 960fbc06-e0f5-3140-9475-f0c36ace9582 | -19.15956 | -44.40565 | 2026-08-24 04:27:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README23.md)
