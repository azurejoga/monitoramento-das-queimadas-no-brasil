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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 897a5744-3577-324d-abe8-1643c28ba7a3 | -4.52756 | -38.87392 | 2026-03-03 03:42:00 | NPP-375D | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 11ededbb-5d5d-3ced-b08e-7b059612fb85 | -21.79433 | -52.72068 | 2026-03-03 03:46:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d7ec1210-e9d3-3c61-8974-75e5b35163ed | -21.48825 | -48.6665 | 2026-03-03 03:46:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 024502ca-03aa-31b8-87a8-f562730e97aa | -27.26251 | -51.45613 | 2026-03-03 03:46:00 | NPP-375D | ERVAL VELHO | SANTA CATARINA | Brasil | 4205209 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 9aaa5090-863a-3aff-ac99-24f334a7805d | -21.65912 | -41.32388 | 2026-03-03 03:46:00 | NPP-375D | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ce9237b0-5722-3fa8-ad81-d925c96ea398 | -21.70449 | -48.43867 | 2026-03-03 03:46:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f35d418-4fa0-3508-8f3e-6f707cf9acc1 | -27.26843 | -51.45833 | 2026-03-03 03:46:00 | NPP-375D | ERVAL VELHO | SANTA CATARINA | Brasil | 4205209 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 00ae9b5b-4f9b-3132-8195-73a2b4344a15 | -18.80983 | -51.62054 | 2026-03-03 03:46:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b703f11d-2bde-3ae0-aa9b-b33fd8b428cc | -25.21977 | -53.2832 | 2026-03-03 03:46:00 | NPP-375D | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f02a90a5-a737-34ee-9bf9-f1e41569a3d4 | -21.63638 | -48.98776 | 2026-03-03 03:46:00 | NPP-375D | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a56fba4-454d-3479-aafa-f190ab40b9c2 | -27.26145 | -51.45684 | 2026-03-03 03:46:00 | NPP-375D | ERVAL VELHO | SANTA CATARINA | Brasil | 4205209 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c7b65050-719c-3c0b-9545-feaee26e6802 | -25.21544 | -53.28315 | 2026-03-03 03:46:00 | NPP-375D | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b77f8173-83a4-3250-9997-42e26905a3f7 | -21.79949 | -52.73036 | 2026-03-03 03:46:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2aed36d3-065e-39c8-ac78-8ec36cb44e44 | -20.80658 | -49.84023 | 2026-03-03 03:46:00 | NPP-375D | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| c3c0accb-4058-35b8-9ef4-2901c70bbd69 | -21.70548 | -48.43436 | 2026-03-03 03:46:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82f92e1a-f37a-3204-8ce7-cf93a02752aa | -27.2674 | -51.45891 | 2026-03-03 03:46:00 | NPP-375D | ERVAL VELHO | SANTA CATARINA | Brasil | 4205209 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1fb38486-cd8d-31d0-a22b-4e049a33f168 | -25.21792 | -53.28994 | 2026-03-03 03:46:00 | NPP-375D | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 774fe4c5-378e-3b28-9ab7-a40817d93f7f | -20.17969 | -45.40973 | 2026-03-03 03:46:00 | NPP-375D | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 7cdd27c1-f1de-36c3-b2b4-99f77d625ae3 | -21.80213 | -52.71875 | 2026-03-03 03:46:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a9a1ccf8-dbbe-3c2e-b368-a1e0ae797cd6 | -21.48238 | -48.66522 | 2026-03-03 03:46:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7fae854-5a2d-33ae-9976-a641c7085611 | -18.81172 | -51.61304 | 2026-03-03 03:46:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a7257bf7-7a34-356d-a42f-9e0e24cbec85 | -21.71988 | -47.10079 | 2026-03-03 03:46:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b43b43c3-21cd-3e81-8a55-abc22e99ba9e | -25.22232 | -53.28528 | 2026-03-03 03:46:00 | NPP-375D | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 61344aa6-df3a-3ebf-9531-9eb9e4e7575a | -21.63747 | -48.9832 | 2026-03-03 03:46:00 | NPP-375D | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d32e9f1a-eed5-3b5c-aca8-9184af57d3d3 | -21.79621 | -52.71359 | 2026-03-03 03:46:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f770013-e2ff-3808-885c-183772c57d29 | -21.48606 | -48.6614 | 2026-03-03 03:46:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| acea1f17-2566-3fee-be2d-5dd7484869b1 | -21.80024 | -52.72608 | 2026-03-03 03:46:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 29deb9a3-2402-3461-9d40-b707c369d34f | -21.80144 | -52.72299 | 2026-03-03 03:46:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 41ecf549-9663-344f-9c09-bd788152e6d1 | -18.80949 | -51.61758 | 2026-03-03 03:46:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8b3d9282-13c7-3a1a-b977-ed065de28052 | -21.80336 | -52.71569 | 2026-03-03 03:46:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b54f6294-827b-36ac-b709-0b89ffb8d0a1 | -21.69884 | -48.43689 | 2026-03-03 03:46:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dc25a941-9433-337e-bedb-e07ff41a6ad2 | -21.795 | -52.71653 | 2026-03-03 03:46:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e12fb2af-7aff-3042-9ae0-0ee7b97f3939 | -18.7912 | -57.6519 | 2026-03-03 03:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 161.9 |
| 34baf04f-ad43-3bf3-8ae5-0849971c726e | -18.8115 | -57.6286 | 2026-03-03 03:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 209.5 |
| 952dbe54-a757-32c7-8434-c6bf8cbdb4c5 | -18.7915 | -57.6312 | 2026-03-03 03:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 116.7 |
| 3126550a-bcd1-3586-b7d7-9a4876f385e4 | -18.8111 | -57.6493 | 2026-03-03 03:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 331.1 |
| a5f951bc-803d-303b-885f-96f65f1ab5f5 | 1.5047 | -59.9116 | 2026-03-03 03:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.0 |
| a5441aa5-cb6e-3493-bbfd-c52c5c32d316 | 1.5047 | -59.9116 | 2026-03-03 04:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.9 |
| aff93a2d-6622-36ef-b970-9a7e6e4e4ca9 | -18.7912 | -57.6519 | 2026-03-03 04:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 269.3 |
| 3fab9d1e-4453-3c35-8351-74b1f4b378dc | -18.8111 | -57.6493 | 2026-03-03 04:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 279.4 |
| d7d0eb87-a2d2-3a66-8ec4-6cec22311b72 | -18.8115 | -57.6286 | 2026-03-03 04:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 162.1 |
| b5d756f3-a2f2-324e-9375-57d2bb567c08 | -18.7915 | -57.6312 | 2026-03-03 04:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 159.1 |
| 192ded70-a1b2-3a2d-8063-2593c269c8bd | -4.53103 | -38.87109 | 2026-03-03 04:01:00 | NOAA-20 | ITAPIÚNA | CEARÁ | Brasil | 2306504 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 267a84a4-695d-30a5-8ac6-32ebe629faf0 | -18.80433 | -51.60462 | 2026-03-03 04:06:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23337ad2-bff1-30d1-bd17-afa29e43706f | -18.81052 | -51.59971 | 2026-03-03 04:06:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7beec826-55ab-313f-a878-62b4ff818e70 | -18.8093 | -51.6056 | 2026-03-03 04:06:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57e7d151-4cf3-3d54-ad09-621d902d76d5 | -18.80806 | -51.61158 | 2026-03-03 04:06:00 | NOAA-20 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e7fae74d-94a0-3536-ad3e-fa62fe66a82f | -17.52159 | -53.7046 | 2026-03-03 04:06:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1461fc59-dfac-3c34-9caf-f14c6cd414fb | -20.17907 | -45.4082 | 2026-03-03 04:06:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1129e3f9-0666-320e-929f-80fcf35b6dd8 | -17.52824 | -53.70182 | 2026-03-03 04:06:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c6127b0-38d2-3c9a-b841-b340bdfa547d | -17.52634 | -53.71063 | 2026-03-03 04:06:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 44bd1ae8-1267-3dcd-a44e-41f6461ea0be | -17.52729 | -53.7062 | 2026-03-03 04:06:00 | NOAA-20 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d34e8905-9aa5-3c7f-8f08-29b38e55d8a3 | -20.18249 | -45.40887 | 2026-03-03 04:06:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 52167ac8-420f-3fcc-a179-d8b1300cebec | -21.70175 | -48.43557 | 2026-03-03 04:08:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d99f64c5-20a5-39bd-8611-249d87346f42 | -21.48594 | -48.66169 | 2026-03-03 04:08:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9c563807-0b00-37fc-86bf-818e55d6ed02 | -21.71728 | -47.09863 | 2026-03-03 04:08:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67c31e1a-bedd-3f8f-ab07-9fc00a966323 | -21.12335 | -48.65098 | 2026-03-03 04:08:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5bc9432a-1815-35be-955a-ddb814e118f5 | -21.80274 | -52.71962 | 2026-03-03 04:08:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f2b6f1d8-8c7f-3657-b9b9-3a0c00441723 | -18.80528 | -57.64941 | 2026-03-03 04:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.5 |
| 32c74e8a-eeb9-382a-88ad-a3561deefd1a | -21.6353 | -48.98206 | 2026-03-03 04:08:00 | NOAA-20 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0623992b-7e2f-3d0f-a7f9-d74dc6f6f157 | -18.80173 | -57.64686 | 2026-03-03 04:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.1 |
| 1711dc30-73eb-36e3-904a-6157e9b4315e | -21.70327 | -48.43275 | 2026-03-03 04:08:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6dfee850-47fa-35df-aaa3-89ab22390b27 | -20.80891 | -49.84039 | 2026-03-03 04:08:00 | NOAA-20 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4034fd23-aa3f-307a-8799-b11d37bc9896 | -21.72088 | -47.09933 | 2026-03-03 04:08:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1e07441b-29f1-378b-9998-38d6ad41fae8 | -21.63859 | -48.98661 | 2026-03-03 04:08:00 | NOAA-20 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9041bc4a-6573-3585-89b7-bc7dac8ddc7e | -21.71953 | -47.10148 | 2026-03-03 04:08:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52967b57-1fb3-3cb3-a2b8-281df1e7a279 | -20.80976 | -49.83609 | 2026-03-03 04:08:00 | NOAA-20 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f1b6a564-64d9-37ad-930d-306a17561115 | -18.7965 | -57.63773 | 2026-03-03 04:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.6 |
| e0927e7b-786a-3d32-8910-084fa8d73b21 | -21.70271 | -48.43034 | 2026-03-03 04:08:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4b243490-266a-362a-92b9-6b4d735103cb | -21.65937 | -41.32547 | 2026-03-03 04:08:00 | NOAA-20 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6a6ea32c-cce1-3a45-bad7-0356cb788c94 | -21.80146 | -52.72565 | 2026-03-03 04:08:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 00346fca-1ea0-3cd8-a5dd-ff21e11457b4 | -18.79998 | -57.65407 | 2026-03-03 04:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.2 |
| bd6fadeb-da3b-3b35-8bb0-657aeb3d6a6a | -21.63929 | -48.98293 | 2026-03-03 04:08:00 | NOAA-20 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e3041235-fe43-30ae-bb26-192869c6bd32 | -18.80705 | -57.64225 | 2026-03-03 04:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 0da2491b-2956-34c6-820d-3462f3851106 | -21.71593 | -47.10078 | 2026-03-03 04:08:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2bea6100-3252-39a1-b97b-4ab4d2fb5393 | -18.80347 | -57.63968 | 2026-03-03 04:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.1 |
| fd63f52f-5b29-3085-afe9-effe12cd3f32 | -18.79476 | -57.64491 | 2026-03-03 04:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 21.6 |
| 576a5ece-c8fd-3715-8f66-a583c4ff639b | -21.79777 | -52.71829 | 2026-03-03 04:08:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 969ee1be-f1ae-3e35-91e3-0ec8758ef76c | -23.79512 | -46.6888 | 2026-03-03 04:08:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2341876c-f718-3af1-be9b-67ea9c326761 | -25.46367 | -52.27119 | 2026-03-03 04:08:00 | NOAA-20 | VIRMOND | PARANÁ | Brasil | 4128658 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 763dccd4-45dd-3ff9-955f-011494b35c6e | -21.6346 | -48.98577 | 2026-03-03 04:08:00 | NOAA-20 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f8d88d9-2c00-3704-88d4-ef9d69ef59ca | -25.21877 | -53.2878 | 2026-03-03 04:08:00 | NOAA-20 | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| e66b197b-3253-3fa8-9ba8-39a1a393a290 | -21.80082 | -52.72867 | 2026-03-03 04:08:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee7b34ff-afa4-36a3-81f5-29648971b6b9 | -21.72031 | -47.09706 | 2026-03-03 04:08:00 | NOAA-20 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dbb3cbdc-4932-3dc9-89a4-8b5aac144393 | -18.79301 | -57.65214 | 2026-03-03 04:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 9110d662-eff3-368a-9ee1-deab0895f3f9 | -23.01758 | -49.26761 | 2026-03-03 04:08:00 | NOAA-20 | MANDURI | SÃO PAULO | Brasil | 3528601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6c6940c9-f520-3da1-a928-aacc7ae87b46 | -21.7984 | -52.71533 | 2026-03-03 04:08:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d84bc78a-055d-3a24-bcf5-2f96c0d83ac4 | -18.80349 | -57.6566 | 2026-03-03 04:08:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.5 |
| bc700ff8-c4bf-3d6c-bab3-9262802907c0 | -21.69942 | -48.43187 | 2026-03-03 04:08:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38c2bbd0-2274-36c9-b151-0745f9295cf9 | -25.22003 | -53.28212 | 2026-03-03 04:08:00 | NOAA-20 | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| db16e76b-7f1b-3556-a873-c784d354ebdc | -21.50869 | -49.13795 | 2026-03-03 04:08:00 | NOAA-20 | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7ddd94e4-32b0-322b-b380-adc89b46ba27 | 1.5047 | -59.9116 | 2026-03-03 04:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.8 |
| a232980a-34ac-33db-968c-91e61c4db950 | -18.7912 | -57.6519 | 2026-03-03 04:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 207.1 |
| a9b01816-a362-34d0-aace-595724f8e16d | -18.8111 | -57.6493 | 2026-03-03 04:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 250.9 |
| 82e1f445-ec30-3bd8-b168-b4c16265bd76 | -18.8115 | -57.6286 | 2026-03-03 04:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 153.4 |
| a05980e6-3bd4-3f60-9a43-ee1df8686c10 | -18.7915 | -57.6312 | 2026-03-03 04:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 158.8 |
| f55d14aa-6a74-33e5-a3ea-a39814a7cc35 | -27.16427 | -51.37265 | 2026-03-03 04:10:00 | NOAA-20 | HERVAL D'OESTE | SANTA CATARINA | Brasil | 4206702 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 97cdaa81-ba97-3b09-a8a0-60af5c39809d | -27.26553 | -51.45653 | 2026-03-03 04:10:00 | NOAA-20 | ERVAL VELHO | SANTA CATARINA | Brasil | 4205209 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 10ed1c8d-700d-3294-9ab9-0a4a7166ac94 | -30.45388 | -51.73952 | 2026-03-03 04:10:00 | NOAA-20 | BARÃO DO TRIUNFO | RIO GRANDE DO SUL | Brasil | 4301750 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| 5a822cd6-20cb-35f7-aaac-f6ea31c5074c | -18.7912 | -57.6519 | 2026-03-03 04:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 89.0 |


[Clique aqui para ver as próximas entradas](README3.md)
