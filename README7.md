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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1bba4aa6-697f-33db-92d2-05a214e8c2eb | -21.62557 | -56.13154 | 2025-12-05 04:06:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 9.2 |
| abb7315a-55f2-33ea-82fb-23af00d6cd3d | -21.63173 | -56.13313 | 2025-12-05 04:06:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1780a4c3-a8c0-3d45-a1e8-2672308c861e | -21.6244 | -56.13652 | 2025-12-05 04:06:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1a65fb64-a7f9-3c92-964e-890a084bfab8 | -23.08724 | -47.59652 | 2025-12-05 04:06:00 | NOAA-21 | RAFARD | SÃO PAULO | Brasil | 3542107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 26ebc828-f448-34b7-86a8-39554e7b790c | -20.96073 | -48.7689 | 2025-12-05 04:06:00 | NOAA-21 | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e147dddb-2da5-348b-ab73-882799e6ecc0 | -21.36964 | -48.53254 | 2025-12-05 04:06:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6c13c611-eba7-3e70-a4ed-f9c065161c5f | -22.60916 | -46.27129 | 2025-12-05 04:06:00 | NOAA-21 | MUNHOZ | MINAS GERAIS | Brasil | 3143807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 197efb3d-edd1-369f-9bd6-c4001805f076 | -20.86099 | -49.2265 | 2025-12-05 04:06:00 | NOAA-21 | CEDRAL | SÃO PAULO | Brasil | 3511300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0829279e-cd93-3c4d-9287-9e429c5b8ed0 | -20.97019 | -48.76296 | 2025-12-05 04:06:00 | NOAA-21 | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c3724827-801f-307c-92d2-e9f3debb1b56 | -23.60435 | -48.34747 | 2025-12-05 04:06:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 81188ff4-81cf-3db9-8c42-2e8a4963b78a | -20.91436 | -56.38274 | 2025-12-05 04:06:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 007dc674-7764-33cd-9e32-4341ebc507db | -21.62919 | -56.13476 | 2025-12-05 04:06:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4f01f872-2794-32c2-8d28-1a71c70db690 | -20.96546 | -48.7659 | 2025-12-05 04:06:00 | NOAA-21 | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 78d09ec8-38dc-3c6c-bfdf-263cf9396ade | -21.37255 | -48.53891 | 2025-12-05 04:06:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e155cfee-5b9f-3cfc-9576-3fc8b741d6ec | -23.71944 | -47.45428 | 2025-12-05 04:06:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fb7fa633-5ec3-33a9-b0b7-a2fc0e52a553 | -23.60093 | -48.34462 | 2025-12-05 04:06:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 11bc81b5-29a8-334e-bb8e-96a26548fe18 | -22.95248 | -48.7053 | 2025-12-05 04:06:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8070158b-b0f6-3bdf-aee7-ec0ffca1b6c1 | -22.49325 | -46.93583 | 2025-12-05 04:06:00 | NOAA-21 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af976eac-455c-3c0e-ac12-7d19c46d2a71 | -21.36823 | -48.53492 | 2025-12-05 04:06:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ce777f3-dc8d-3dec-ba6e-f9dc954a3d6c | -21.86082 | -48.80734 | 2025-12-05 04:06:00 | NOAA-21 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e8b87e2-e8c2-36a7-9989-8cdb0ce0c10c | -20.72091 | -47.34249 | 2025-12-05 04:06:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1d15052a-684e-380d-999b-c9cd03f3c5bd | -21.33252 | -44.95367 | 2025-12-05 04:06:00 | NOAA-21 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 579e218a-9d90-3263-8ef0-7b946ba6252f | -21.62421 | -56.12823 | 2025-12-05 04:06:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ab97d667-2689-3ded-a56f-14ebbb25f4b8 | -21.37215 | -48.53582 | 2025-12-05 04:06:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a47416c1-b8e4-3496-8a43-c4ec9b53b301 | -22.55095 | -46.81664 | 2025-12-05 04:06:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 657d3859-5c52-3d76-94c1-20e7ca088977 | -21.18377 | -45.61185 | 2025-12-05 04:06:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 00b85441-b11b-301c-bb89-acb64a26f01e | -20.92067 | -56.38449 | 2025-12-05 04:06:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 357cfa6f-4a0f-3646-a22a-5cc701faf048 | -31.59669 | -53.62411 | 2025-12-05 04:08:00 | NOAA-21 | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| 53257e88-ef83-3778-a300-ac1d5942ccf8 | -30.8979 | -53.49728 | 2025-12-05 04:08:00 | NOAA-21 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| bf813358-3080-3cc8-9697-a9b7104eebe9 | -27.01773 | -51.61417 | 2025-12-05 04:08:00 | NOAA-21 | CATANDUVAS | SANTA CATARINA | Brasil | 4204004 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5a267f77-b172-3bb9-9b6c-eb44a6645a5b | -30.89679 | -53.50228 | 2025-12-05 04:08:00 | NOAA-21 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| e7dc255c-3b0a-3875-a2b4-9ad630b0b396 | -30.89816 | -53.50045 | 2025-12-05 04:08:00 | NOAA-21 | CAÇAPAVA DO SUL | RIO GRANDE DO SUL | Brasil | 4302808 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| 37c6f1b7-d315-3caf-9067-4eecfef9fca2 | -31.59134 | -53.62757 | 2025-12-05 04:08:00 | NOAA-21 | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 11.5 |
| 33ac0bd2-52dc-322e-9515-c5c97564b460 | -31.59565 | -53.62891 | 2025-12-05 04:08:00 | NOAA-21 | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 11.5 |
| 3ceeab53-2d43-378b-ad9d-21b84242b966 | -26.31449 | -52.02075 | 2025-12-05 04:08:00 | NOAA-21 | CORONEL DOMINGOS SOARES | PARANÁ | Brasil | 4106456 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8771649c-d11f-3dfa-a291-6aa588cb397f | -6.0192 | -41.1278 | 2025-12-05 04:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 58.0 |
| 88d9d7a2-db43-3c15-bf63-316ad62058bc | -6.0004 | -41.1295 | 2025-12-05 04:10:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 77.7 |
| 3b8c0ff3-2c72-39a1-968b-291d7af888fb | -6.0002 | -41.1538 | 2025-12-05 04:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 67.6 |
| 63cde52c-086d-30d4-bb12-36cd162460dd | -6.0004 | -41.1295 | 2025-12-05 04:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 80.8 |
| 896f60cb-8322-39a7-ae22-6d501b721ecf | 2.52793 | -50.84255 | 2025-12-05 04:27:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07248c71-e1ba-3576-8d8b-062cccad3b64 | 0.44446 | -50.93812 | 2025-12-05 04:27:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| daa86d8a-3b2e-390c-b3f0-c2ac3ca58e5b | -1.02534 | -46.65135 | 2025-12-05 04:27:00 | NPP-375D | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2d34545-d747-3561-914f-d7295d4d401d | 2.52478 | -50.85209 | 2025-12-05 04:27:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7d11f624-294c-3207-aea9-aa3a8d19a294 | -1.42321 | -46.76472 | 2025-12-05 04:29:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e014960a-ab1a-3b49-9a15-5db3be4ba7eb | -5.1832 | -43.08504 | 2025-12-05 04:29:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b664874-f572-33d5-8ca5-ca686a885704 | -3.77887 | -40.55764 | 2025-12-05 04:29:00 | NPP-375D | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 38f482ae-3b13-35e9-a70e-22bb0161f217 | -4.61213 | -38.68033 | 2025-12-05 04:29:00 | NPP-375D | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6926cd0f-b4f9-34e7-912b-1f9e4ab5b26a | -1.23495 | -46.73898 | 2025-12-05 04:29:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 59d58f68-da41-355d-a86c-f16ec1fa0018 | -4.91446 | -43.80079 | 2025-12-05 04:29:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 421dda96-e1da-3af0-9bd8-e4e0ff8b20f8 | -7.05687 | -39.3172 | 2025-12-05 04:29:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 1a834bf4-4930-313a-ae5a-91c9b007d96a | -5.17898 | -43.08855 | 2025-12-05 04:29:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45ceb8f5-435b-3e55-a164-a6ade2caf39c | -4.73665 | -44.42967 | 2025-12-05 04:29:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d16dfac6-62e1-3d75-beda-59fba5ddabb3 | -2.44319 | -47.16064 | 2025-12-05 04:29:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18e99a29-5c29-360c-8aa1-bfd1be95bb16 | -3.50856 | -44.51632 | 2025-12-05 04:29:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91ea1294-49c8-3bdb-96ef-251ae1c5c869 | -5.17602 | -43.08393 | 2025-12-05 04:29:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0323426-0760-3dc6-876f-8f10fbfa6943 | -4.73948 | -44.43382 | 2025-12-05 04:29:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24bcf9e4-f2e1-30b2-826c-927de1219ed6 | -3.34524 | -42.14997 | 2025-12-05 04:29:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b9ecc7cd-4b45-37b9-b70a-bd3676039076 | -6.42681 | -44.78391 | 2025-12-05 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 66d11dca-8791-3ce5-be31-3c9d867fa320 | -4.70909 | -44.56187 | 2025-12-05 04:29:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 70b20fb4-4b0b-35a7-933b-9f7d387355c0 | -2.06546 | -45.36296 | 2025-12-05 04:29:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bc6d4a8a-d439-34aa-a6b2-d2ea5da9d7ad | -5.68883 | -43.51741 | 2025-12-05 04:29:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2153d1cf-f4a3-3781-a5c2-1421bfc1f581 | -6.42398 | -44.77977 | 2025-12-05 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c41f8d71-acf2-3f12-80ad-527573574f30 | -5.35202 | -42.11481 | 2025-12-05 04:29:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f943330d-a27e-307d-8126-0447ef72e42a | -5.22251 | -39.25872 | 2025-12-05 04:29:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e25ebcca-3931-3720-a68b-45eec0fd9ac1 | -3.60502 | -46.00769 | 2025-12-05 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aed59866-5683-30bc-9489-21578ac712b0 | -3.07332 | -46.64866 | 2025-12-05 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd77362c-e06a-3b52-9683-defcb4bec98b | -6.42568 | -44.79119 | 2025-12-05 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b99471bf-9bf6-3e97-a2f0-0cf666fee6ed | -0.64492 | -52.38039 | 2025-12-05 04:29:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 818f9e15-607f-3ed1-9bb4-b5ceb1ef3aac | -3.097 | -44.489 | 2025-12-05 04:29:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f410df9e-7553-3832-801f-ca4ccd803d0b | -5.06531 | -40.47602 | 2025-12-05 04:29:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 000be9f1-1457-3e90-b8ff-857c0b9d7b0b | -3.0257 | -41.13225 | 2025-12-05 04:29:00 | NPP-375D | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| e414318d-f6d0-3791-9947-731041f35180 | -4.90621 | -44.50754 | 2025-12-05 04:29:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2261c4ab-9383-31c8-812d-040d716a0db4 | -1.78822 | -54.01085 | 2025-12-05 04:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b4215f0-3fb9-3119-becf-9407ae96c912 | -4.60742 | -38.67961 | 2025-12-05 04:29:00 | NPP-375D | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 677e9ef5-9527-358f-98ae-7676e566f0bf | -5.99979 | -41.13788 | 2025-12-05 04:29:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 16.0 |
| 0608286f-5261-37da-b9bd-6e0d2259432d | -5.18257 | -43.0891 | 2025-12-05 04:29:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2574433b-2894-3c85-a437-0ad65ac1634f | -1.68999 | -46.15482 | 2025-12-05 04:29:00 | NPP-375D | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bbe693e0-6618-3322-92ee-8a6bb5b38e74 | -1.94877 | -46.379 | 2025-12-05 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bb224f64-4b30-3ffd-b826-ea8f1d07e098 | -4.78627 | -44.56253 | 2025-12-05 04:29:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b872e54-502b-3de4-ac30-b7f25c7fe9b3 | -1.45721 | -46.72568 | 2025-12-05 04:29:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 22316171-357d-32a0-86e8-44e2f2ccf5b7 | -1.46059 | -46.72622 | 2025-12-05 04:29:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e3543389-9760-38b9-a42c-41d1a623470a | -5.99874 | -41.14491 | 2025-12-05 04:29:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 9aaf4dc0-de42-32c9-b65a-21cf36917787 | -5.12757 | -36.42773 | 2025-12-05 04:29:00 | NPP-375D | GUAMARÉ | RIO GRANDE DO NORTE | Brasil | 2404507 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7a66cca3-881f-3fe2-8693-860ca837836c | -4.53481 | -44.22419 | 2025-12-05 04:29:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8521aca6-9932-3b90-87d8-726441cd0a48 | -6.42342 | -44.78341 | 2025-12-05 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 463db8e6-a4df-371d-9b10-bf044196a2f1 | -5.3513 | -42.11692 | 2025-12-05 04:29:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0cc436d7-452a-327c-ae43-fca6a7e65800 | -2.40087 | -47.13941 | 2025-12-05 04:29:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 00ae6f90-60ec-3ea3-a7b5-aa90905aa1ff | -4.91016 | -44.50446 | 2025-12-05 04:29:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 892873a7-cd47-35c6-9d3f-a29364e10b92 | -4.73615 | -46.38906 | 2025-12-05 04:29:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c710822e-8072-37ed-8bd3-a722873fe713 | -6.01494 | -41.14768 | 2025-12-05 04:29:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 645fd8c2-8d8e-3e48-b401-b95a216b9602 | -4.74004 | -44.4302 | 2025-12-05 04:29:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea6ded32-e744-3a8f-b1dc-f1471c111d2f | -1.17847 | -53.90174 | 2025-12-05 04:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e7347a1-5d43-3140-82bf-4566b029d177 | -6.41549 | -44.7897 | 2025-12-05 04:29:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a31ba3ae-4faa-3142-903d-43e6c92994f0 | -6.00823 | -41.16471 | 2025-12-05 04:29:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c4729d51-d1d9-313c-9815-95d6c3bb2a27 | -4.9096 | -44.50807 | 2025-12-05 04:29:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9624689d-1296-3701-82e4-f51c8d2e1c76 | -1.17416 | -53.89522 | 2025-12-05 04:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b8f1143-0694-3dca-889a-f8e82a55fe15 | -4.91388 | -43.80458 | 2025-12-05 04:29:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fecdd18f-2901-3ae7-b86d-0ee52f0270a5 | -7.05978 | -39.31396 | 2025-12-05 04:29:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d869600c-5412-3753-a126-2340036f4bd0 | -4.98805 | -43.83916 | 2025-12-05 04:29:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fae86d0d-eef2-394e-bd53-4d2ac58d443c | -4.72895 | -46.39146 | 2025-12-05 04:29:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README8.md)
