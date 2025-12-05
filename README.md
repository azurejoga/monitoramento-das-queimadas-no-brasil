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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8abb504-fd3c-3ad2-9c11-18798594d548 | -6.0002 | -41.1538 | 2025-12-05 00:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 150.6 |
| ac109bab-a8fa-38f5-b112-9e72dac55837 | -1.4532 | -46.7217 | 2025-12-05 00:00:00 | GOES-19 | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 54c5066c-82e5-333e-a224-a74ecf5d3fe1 | -21.3821 | -48.5382 | 2025-12-05 00:00:00 | GOES-19 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 86.1 |
| d7e232d3-187a-35d7-9909-567c3bca2f88 | -6.0192 | -41.1278 | 2025-12-05 00:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 123.0 |
| d3038f8b-d4a2-305f-8898-78110cef8024 | -10.5969 | -53.4573 | 2025-12-05 00:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 47183231-e4fb-30fb-8a6d-440ca6d3056a | -1.7884 | -54.0117 | 2025-12-05 00:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 668cbe81-6826-35ee-8108-5adf75789337 | -6.019 | -41.1521 | 2025-12-05 00:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 135.8 |
| 63acacb0-8913-350a-bbdf-226d66fb56a3 | -2.9049 | -45.2368 | 2025-12-05 00:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 89.4 |
| bd6ec80e-347a-35cc-b438-61ca919096b6 | -6.0004 | -41.1295 | 2025-12-05 00:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 141.1 |
| cac4c836-d0d7-3295-aea6-e335ab1681ee | -6.6382 | -43.1423 | 2025-12-05 00:00:00 | METOP-C | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f5366ed9-cca8-3cd6-a51e-5036f61776f0 | -7.3603 | -39.005699 | 2025-12-05 00:00:00 | METOP-C | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ab98deba-b844-302f-9509-9219bda14590 | -4.6132 | -38.672901 | 2025-12-05 00:00:00 | METOP-C | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6e66c784-136b-3102-a8ba-23892f9fc873 | -6.3019 | -39.655701 | 2025-12-05 00:00:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 095e4648-90af-3d7c-a51c-c505eb04d176 | -6.7901 | -39.263599 | 2025-12-05 00:00:00 | METOP-C | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 73bbd550-e0fe-3173-8ca4-faecc2ffed7a | -2.9081 | -45.231602 | 2025-12-05 00:00:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1c3f2d7c-8797-3c29-a768-b0654e601e7c | -3.7701 | -40.8508 | 2025-12-05 00:00:00 | METOP-C | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 7ca8596c-98ea-34f6-8b10-41ea0e3be8dd | -4.9086 | -44.5037 | 2025-12-05 00:00:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5718c336-dc79-3e41-8e48-28cb0525f944 | -6.527 | -39.1493 | 2025-12-05 00:00:00 | METOP-C | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 98246d1b-5bf0-3f25-8e7f-19cc01faf202 | -2.724 | -45.188202 | 2025-12-05 00:00:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| be579831-3e57-33ab-a3d3-6ea3ad4ea441 | -6.7885 | -39.256802 | 2025-12-05 00:00:00 | METOP-C | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 8543ff2b-2709-329b-88cc-cf324c1e7986 | -6.7787 | -39.258999 | 2025-12-05 00:00:00 | METOP-C | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c731a903-048c-3b73-8e49-b080356b7523 | -4.5864 | -44.3913 | 2025-12-05 00:00:00 | METOP-C | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1425a68b-37ce-3ed8-a0fb-91829f00cd94 | -6.0033 | -41.162601 | 2025-12-05 00:00:00 | METOP-C | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f26f3520-d21f-399e-948e-73521c659bc0 | -4.8988 | -44.505798 | 2025-12-05 00:00:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6a409e15-c3ee-3984-afbb-1e8a62f74c32 | -2.5464 | -45.3106 | 2025-12-05 00:00:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f768ed5f-d2a2-3b44-bd6a-ff933a180f87 | -5.2226 | -39.2617 | 2025-12-05 00:00:00 | METOP-C | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 264c8d15-1c02-37a9-86aa-7a3f37c7c95f | -6.6578 | -40.868801 | 2025-12-05 00:00:00 | METOP-C | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f79ec95d-e43b-387a-911d-30771a7d555d | -7.8918 | -39.395699 | 2025-12-05 00:00:00 | METOP-C | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 356b8cb8-35e6-3d88-b997-a7c535cda7ee | -2.8957 | -45.222301 | 2025-12-05 00:00:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5769e22e-1584-3af4-9a32-73228a9c5ec3 | -4.5316 | -44.236801 | 2025-12-05 00:00:00 | METOP-C | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d7d4e398-fd6e-3305-8e9c-506b6c464fa8 | -3.3711 | -44.095402 | 2025-12-05 00:00:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f20f24e0-9b72-3bcd-8bcd-ae3aef6548ca | -7.3588 | -38.998798 | 2025-12-05 00:00:00 | METOP-C | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f869e40b-8b9d-3715-aded-1371bf1c1eb6 | -2.9543 | -40.2565 | 2025-12-05 00:00:00 | METOP-C | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a3a22da3-cfa8-3cfd-97d1-50cdab405f0c | -5.9999 | -41.147499 | 2025-12-05 00:00:00 | METOP-C | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a673aa00-b6e0-3feb-9aa3-74123c7e8c55 | -2.9008 | -45.245201 | 2025-12-05 00:00:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 74698e49-32f5-3d30-ba40-9c7544c12a00 | -6.2772 | -39.683102 | 2025-12-05 00:00:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 15d19e93-9547-3232-ad0f-9856ca66d392 | -7.4277 | -40.7229 | 2025-12-05 00:00:00 | METOP-C | MARCOLÂNDIA | PIAUÍ | Brasil | 2205953 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3989a9ba-0003-3ec9-b90a-1df5f4d9c130 | -6.1402 | -39.669899 | 2025-12-05 00:00:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 3572bd1d-d6a5-3e94-a9c7-054daa4ed976 | -6.0114 | -41.152901 | 2025-12-05 00:00:00 | METOP-C | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 925e33a7-5e79-39e3-8493-c6ed80a63853 | -2.9055 | -45.2202 | 2025-12-05 00:00:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8d0a8475-22d0-3ce5-801d-bc057c81b46c | -4.5066 | -40.5093 | 2025-12-05 00:00:00 | METOP-C | HIDROLÂNDIA | CEARÁ | Brasil | 2305209 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2ff760de-36d1-3112-a061-3e90fa634a00 | -3.4365 | -45.5774 | 2025-12-05 00:00:00 | METOP-C | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3a47cbaf-df5a-3c59-b966-2e6444c9f309 | -2.8983 | -45.2337 | 2025-12-05 00:00:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c5179bfe-e701-31dd-bd5f-fd2efea773f7 | -5.9982 | -41.139999 | 2025-12-05 00:00:00 | METOP-C | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 82158b89-f3b8-3786-b825-3aa4d626a644 | -5.0125 | -41.0145 | 2025-12-05 00:00:00 | METOP-C | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1e2e9c65-e707-356c-9513-a63c9f39682c | -5.9918 | -41.1572 | 2025-12-05 00:00:00 | METOP-C | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f324db29-23d5-3f1f-9738-3934e40b0ccf | -3.3437 | -42.1502 | 2025-12-05 00:00:00 | METOP-C | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| 8890c4fb-256d-3cad-a5ed-8ed960bdb2bc | -7.7188 | -37.6866 | 2025-12-05 00:00:00 | METOP-C | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 04d6af4a-5a0f-3229-9e47-6373c5bfab2d | -6.008 | -41.137798 | 2025-12-05 00:00:00 | METOP-C | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8eb4ee8d-849d-3de2-a7c1-8ac39dc1318e | -5.6381 | -39.456402 | 2025-12-05 00:00:00 | METOP-C | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 3e5839ab-ff26-3ae2-9a75-f116e0e3a2d0 | -4.7034 | -44.456402 | 2025-12-05 00:00:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 88d64538-7737-31bf-832a-c10ba663cbac | -4.7156 | -44.465099 | 2025-12-05 00:00:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7d0f8ea-5d1e-39ff-8f1c-7b6882021d97 | -4.1574 | -39.249199 | 2025-12-05 00:00:00 | METOP-C | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a8beaea0-8505-3d90-bbe6-4b17dc5553a5 | -3.0603 | -40.089001 | 2025-12-05 00:00:00 | METOP-C | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a965005b-8648-3467-88be-217697b27a27 | -6.2989 | -35.227798 | 2025-12-05 00:00:00 | METOP-C | GOIANINHA | RIO GRANDE DO NORTE | Brasil | 2404200 | 24 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9e0d0717-93c1-3aa4-aea5-4ee47f4d09ef | -4.9021 | -43.457901 | 2025-12-05 00:00:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5dc05d35-da4e-3b29-993f-e8e5ef09c915 | -4.539 | -44.2243 | 2025-12-05 00:00:00 | METOP-C | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aa1b2261-e5a1-332f-b6a1-8d76173a5810 | -4.6049 | -38.681999 | 2025-12-05 00:00:00 | METOP-C | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 98e423ce-ba8a-397a-9cef-d0da4de8f43a | -4.4553 | -38.3895 | 2025-12-05 00:00:00 | METOP-C | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| b314715b-aa23-3019-b546-b584d2eb8ce7 | -4.5818 | -45.526699 | 2025-12-05 00:00:00 | METOP-C | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ce806ac1-fa3f-3374-8c4b-ff47f231cfbd | -4.6034 | -38.675098 | 2025-12-05 00:00:00 | METOP-C | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f116bd0d-eb5f-3074-bea0-61ecd18ca0bd | -7.7172 | -37.6796 | 2025-12-05 00:00:00 | METOP-C | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 79bd9853-72d0-3d75-9802-9bd58df9a8b8 | -3.0587 | -40.0821 | 2025-12-05 00:00:00 | METOP-C | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 4884c3df-6fc5-3b41-866e-b1f4462309be | -6.3655 | -39.481701 | 2025-12-05 00:00:00 | METOP-C | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 0dabda09-0f7b-3048-be09-350224549885 | -2.5366 | -45.312698 | 2025-12-05 00:00:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f9d2a00a-0264-3dfa-a768-362dd8cf2ea8 | -6.787 | -39.249901 | 2025-12-05 00:00:00 | METOP-C | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| df0c5111-df67-3bbd-acf3-9ab2a6bec1a8 | -6.947 | -35.131302 | 2025-12-05 00:00:00 | METOP-C | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d3804abe-aa69-306e-a2ee-d96a8e432315 | -4.5293 | -44.226398 | 2025-12-05 00:00:00 | METOP-C | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a5afb16d-be4a-3929-8a3f-e23b6088a4a8 | -3.7764 | -40.561001 | 2025-12-05 00:00:00 | METOP-C | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a85c8580-afc8-3b56-91aa-2ec12e366d89 | -4.4537 | -38.3825 | 2025-12-05 00:00:00 | METOP-C | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f7d2b569-c836-3515-bdcd-f73e26a81095 | -4.6147 | -38.679798 | 2025-12-05 00:00:00 | METOP-C | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 498e8fc6-b792-3947-b2ed-59113b87ba49 | -2.5392 | -45.3242 | 2025-12-05 00:00:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 011d1690-042d-357b-bc0c-d1de2c82dec8 | -5.9157 | -42.983501 | 2025-12-05 00:00:00 | METOP-C | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a2161a1c-947e-3693-b067-93d51fdf857f | -5.0279 | -43.977699 | 2025-12-05 00:00:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a7f351e4-9d16-31aa-ba43-497c9ba97e7f | -3.6666 | -44.818802 | 2025-12-05 00:00:00 | METOP-C | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3e245b4a-b1d4-3b51-9a2d-c9c7426f29ae | -4.7056 | -44.558998 | 2025-12-05 00:00:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8de89983-9a0b-3c5a-aa10-31dc8ef14b9b | -3.5061 | -44.5145 | 2025-12-05 00:00:00 | METOP-C | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9782cd63-24fd-30e3-b10b-9b39873a1777 | -4.1672 | -39.247101 | 2025-12-05 00:00:00 | METOP-C | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 071203d2-3192-380a-a0ac-e6d233fc4515 | -4.3784 | -43.365799 | 2025-12-05 00:00:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 100f22e5-bfab-3342-9911-c3b6b2f542c0 | -2.534 | -45.3013 | 2025-12-05 00:00:00 | METOP-C | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7ea72575-cbb9-3ac9-8541-cd4f3988f248 | -3.669 | -44.8298 | 2025-12-05 00:00:00 | METOP-C | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 89a55b58-c21c-3c8c-b917-8ee88c8664c1 | -2.7167 | -45.201698 | 2025-12-05 00:00:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9041bea6-0db4-3eac-b984-f7437cbe5d4c | -6.9491 | -35.139999 | 2025-12-05 00:00:00 | METOP-C | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d4403d6b-00c7-3999-b9f8-ae7879a3058a | -3.1498 | -45.349499 | 2025-12-05 00:00:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5a07e65a-504f-3ce0-a8d2-c4b00c14bd78 | -4.1688 | -39.253899 | 2025-12-05 00:00:00 | METOP-C | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 48210c1a-72cf-3bde-b70f-5fd7fd01cd7f | -5.0223 | -41.012402 | 2025-12-05 00:00:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1db9e658-1858-3304-b687-8d6b765f2047 | -4.527 | -44.2159 | 2025-12-05 00:00:00 | METOP-C | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3544df49-9f8e-3f14-bbe9-46100ab86c97 | -6.5518 | -39.122101 | 2025-12-05 00:00:00 | METOP-C | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| ea7abfeb-45c6-36a0-8b21-672e67b8415f | -2.7142 | -45.190399 | 2025-12-05 00:00:00 | METOP-C | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ad12489c-4e97-330f-a1f5-5dca50073fc1 | -2.9527 | -40.249699 | 2025-12-05 00:00:00 | METOP-C | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f4e800d8-098c-3345-9e95-f21cbe7f6447 | -5.0109 | -41.007198 | 2025-12-05 00:00:00 | METOP-C | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| af29be02-6b34-3014-a974-7a29d8d3b505 | -4.7377 | -44.4263 | 2025-12-05 00:00:00 | METOP-C | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0370fa13-ff58-3a93-924f-1b6a6f2700c8 | -3.3733 | -44.105301 | 2025-12-05 00:00:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c93f2aec-401f-3877-bfc0-6ce11c46b337 | -3.7748 | -40.554001 | 2025-12-05 00:00:00 | METOP-C | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 0f4e922e-d3b5-343a-901b-cecd98ea2f6a | -5.4678 | -39.523201 | 2025-12-05 00:00:00 | METOP-C | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| a6331d1d-5d9f-366c-932c-394aadc21785 | -5.0499 | -40.906799 | 2025-12-05 00:00:00 | METOP-C | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f263ee2e-678b-3321-8293-89e34c20972a | -2.8931 | -45.210899 | 2025-12-05 00:00:00 | METOP-C | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 86c7a55c-3800-3f0c-8af0-24ec530cef4a | -6.1894 | -40.616798 | 2025-12-05 00:00:00 | METOP-C | PARAMBU | CEARÁ | Brasil | 2310308 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| bd5bfb18-9dc5-3a99-9431-b20c4d4e9f17 | -5.9965 | -41.132401 | 2025-12-05 00:00:00 | METOP-C | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9f5e053e-0236-3397-883d-93903113fb7c | -6.0016 | -41.155102 | 2025-12-05 00:00:00 | METOP-C | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README2.md)
