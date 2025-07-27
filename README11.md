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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4036f007-209e-3183-b7d8-31c836e463c4 | -7.22778 | -45.38126 | 2025-07-27 04:08:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d0d93a96-d17c-3262-b291-687e125264b7 | -7.10226 | -44.91367 | 2025-07-27 04:08:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| def49bd4-76d1-3aa8-baee-01ceee1754e1 | -12.04105 | -45.84758 | 2025-07-27 04:08:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| e3b85915-5527-3d70-b6e7-8c4b2d9f731e | -9.06848 | -44.36705 | 2025-07-27 04:08:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 669840b7-2b1a-3fa5-b38e-44d6bebb7451 | -8.01087 | -48.16762 | 2025-07-27 04:08:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a6cc50da-ac9f-34f9-abdb-01a4d1d2f659 | -9.66031 | -40.59638 | 2025-07-27 04:08:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 54f39436-b3b5-301e-82cd-bb81b24a9c82 | -11.96301 | -46.71179 | 2025-07-27 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a28fc528-4245-3360-9ac3-5b89590710a9 | -13.08164 | -47.35204 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e3cec7d-ff7d-3905-949e-128e13ceb586 | -9.43589 | -51.75391 | 2025-07-27 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ab0463f9-f7c6-356a-a19d-ad676e9dcf41 | -7.2448 | -49.61982 | 2025-07-27 04:08:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f4931f7-0824-3c70-99fc-45e69a024c7c | -7.74881 | -51.12151 | 2025-07-27 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4616d201-1815-342f-aad1-38638e360dd5 | -12.70604 | -46.28952 | 2025-07-27 04:08:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6b1d1001-fc12-3070-87ce-bf8bedd4d1a2 | -8.99937 | -45.36828 | 2025-07-27 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 28f31a73-cfb3-3312-9e99-8c29912bf5f5 | -10.51734 | -42.55362 | 2025-07-27 04:08:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 7b0bbae6-e51f-35d4-9b33-4534f5732eb7 | -7.09751 | -44.87521 | 2025-07-27 04:08:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 42c2574a-888e-36cd-abf3-76af35cc285f | -12.70954 | -47.01033 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fd366e70-28b0-3f5d-8644-e71ef0ea8de4 | -13.08405 | -47.33828 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 26d99193-cfef-3f26-a4c2-4af145b4186a | -12.71411 | -47.00617 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8cfdfd96-a877-34a5-ac36-7d69bcea1cad | -11.29583 | -55.11715 | 2025-07-27 04:08:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3ea1f828-ffe2-320b-8c30-b7f7b7e76a4b | -6.89103 | -52.87214 | 2025-07-27 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0ff00380-af7b-319b-99fb-3b8e4865c79a | -10.84906 | -46.68716 | 2025-07-27 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b309cf99-6e59-31a9-80c6-13653e2c027c | -12.04598 | -45.84 | 2025-07-27 04:08:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1334834-85b9-3b40-a6c6-94ee9b943102 | -9.95626 | -46.29898 | 2025-07-27 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 03968d7a-90ca-32d5-806a-5c1375152a82 | -6.89188 | -52.86753 | 2025-07-27 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 999fd82b-9c81-34d9-9a1d-a70b4c5f9d58 | -12.70677 | -46.28524 | 2025-07-27 04:08:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1220c07-83a5-3b7b-ae56-4f608c72400f | -7.91605 | -43.09749 | 2025-07-27 04:08:00 | NOAA-20 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 55ee1918-c1c7-35dc-bf30-961474013197 | -12.67647 | -47.02313 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a3c57c8a-e835-3a1a-a0a6-5eec2311ff81 | -13.12137 | -47.34819 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6fdd08ee-f1af-3de6-98f3-3b09a8fdb715 | -8.17364 | -43.2114 | 2025-07-27 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7c867c02-5ee0-39f8-80c9-7617bd3f4a1b | -13.0802 | -47.33796 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dd8a998c-4b9a-302d-9a22-3a6bf7a27149 | -9.57918 | -43.855 | 2025-07-27 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b129e5bb-bee9-35f4-ba46-7718689d7b86 | -8.30777 | -42.21669 | 2025-07-27 04:08:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2e7cf6e1-cbe9-3c73-8c42-77e124dc2d61 | -9.03354 | -45.39394 | 2025-07-27 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa4a372a-a16a-3d2e-b1a3-dd5df35042e3 | -12.67597 | -47.00393 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0e57ba3d-8c40-3680-a3bc-56b90455f980 | -9.95553 | -46.29632 | 2025-07-27 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e8f33b04-ac01-3b45-83fb-068b247da3c3 | -9.55767 | -40.64893 | 2025-07-27 04:08:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9c6db6d8-434a-30ff-9d85-bfeff48f5dbc | -13.44543 | -43.62887 | 2025-07-27 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72b80879-3341-301b-b655-9f7f792d1f92 | -13.7141 | -45.67193 | 2025-07-27 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8585c75a-71f1-3a49-9934-95955088bde3 | -10.00907 | -48.22204 | 2025-07-27 04:08:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75b0957e-9d5f-3ff7-9d94-216634833792 | -8.30498 | -45.00603 | 2025-07-27 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dbcf1c27-a864-3ad5-8765-0c3066f52d64 | -6.98988 | -47.07941 | 2025-07-27 04:08:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3d26ab0-4ce0-3184-8e6b-4b31d1281d78 | -7.154 | -44.37627 | 2025-07-27 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 051fed49-0347-3a63-a485-e595ff33ec08 | -14.30314 | -44.17294 | 2025-07-27 04:08:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d031bbd8-d644-3b23-a005-c8b0bc35f9a7 | -12.68393 | -47.02458 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 147be2fb-13f4-3f45-ab77-8f7e0a59a4e3 | -13.0879 | -47.33856 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 30e9f1eb-8e87-3a5d-b123-b703bf545236 | -6.99016 | -45.61912 | 2025-07-27 04:08:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9254624f-7cac-3db5-a07d-87aa5da17a67 | -12.04174 | -45.84349 | 2025-07-27 04:08:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 35247cc1-cf5e-3804-9712-f0f352579e58 | -13.44599 | -43.62533 | 2025-07-27 04:08:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3e749860-1b34-3be2-a88f-3866fd651f03 | -7.34053 | -44.36117 | 2025-07-27 04:08:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f8e095a2-6767-3631-b3be-3b70e75b6725 | -8.98869 | -40.74945 | 2025-07-27 04:08:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 0ed1c90d-8948-306c-a299-aa824e1c70be | -13.71972 | -45.68097 | 2025-07-27 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a3dcd11-f6b7-36d6-971e-33e13ea28e5d | -9.99839 | -44.36615 | 2025-07-27 04:08:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a54cb8bc-7d15-3a0e-aefb-a9c97ae52c18 | -12.67535 | -46.98547 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4754e02-f9f1-350e-8866-c2a096a3cca3 | -14.21697 | -43.96862 | 2025-07-27 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dde117a9-18d5-38ba-90d9-053e06d9d36e | -8.16979 | -43.19251 | 2025-07-27 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6d00dfb4-f73b-3e60-952d-591889c37d02 | -11.5691 | -44.84619 | 2025-07-27 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa6e7069-09b6-316b-9ddb-33b55c69cc77 | -13.07939 | -47.34258 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6b2833c-7f24-3641-8b75-ff73b62535f6 | -12.04529 | -45.8441 | 2025-07-27 04:08:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de794dd5-4865-3335-a44e-fa8435d5bf2d | -13.72253 | -45.68552 | 2025-07-27 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 419dd101-c2d0-36a9-a23a-71cc5d9db7b3 | -7.2894 | -44.6785 | 2025-07-27 04:08:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e7d05c74-45ae-3f37-a509-2234e73ecfca | -12.67892 | -47.00914 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 722d298b-ba65-3e78-8e5b-96f52aa309ca | -14.02514 | -44.61179 | 2025-07-27 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0b658c6f-5f16-3223-b5f7-84d0a7301f96 | -7.55481 | -44.09429 | 2025-07-27 04:08:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 93e6008a-25a2-30e5-9dc9-6c4514419bc2 | -9.43516 | -51.75779 | 2025-07-27 04:08:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9759c688-6bb6-37d7-96b2-71afea808525 | -9.10468 | -46.39222 | 2025-07-27 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b13abdc4-5279-3b78-9c4b-8a45a845ca8d | -11.57252 | -44.84677 | 2025-07-27 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56faeec2-8a6d-32db-92ac-b6ff111a8eef | -14.20838 | -42.01966 | 2025-07-27 04:08:00 | NOAA-20 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0e41d61f-89b2-3ae1-95ae-001f789aacba | -8.2943 | -45.00423 | 2025-07-27 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39f61db8-3a6c-3292-85d0-0c19f4fb4298 | -9.57683 | -43.86956 | 2025-07-27 04:08:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2561349d-05fe-357b-a9c1-771523c6348d | -13.10195 | -47.32511 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4ee589a-5570-376f-ae77-525eca3e76c5 | -12.71101 | -46.2821 | 2025-07-27 04:08:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10af4b61-6c62-30d0-b6fe-a685e39d749a | -13.12352 | -47.35838 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9634d590-6459-399e-b5bb-193af234b6e5 | -13.09146 | -47.36296 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee9f0aec-d64c-35d0-a657-38b13581da99 | -10.43248 | -44.18142 | 2025-07-27 04:08:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5c5c1c13-2955-3705-8e25-170f7b374065 | -6.98928 | -47.08307 | 2025-07-27 04:08:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5982386-5f51-38a2-b518-2f97de85c628 | -12.67911 | -46.98599 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed335ec1-21e9-387c-a5fa-78a4102fda14 | -10.67049 | -46.61725 | 2025-07-27 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fb693b5f-cc8a-3266-bf6b-f3fe1f7a829c | -12.67456 | -46.99001 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 53e744c7-e9f3-3493-beb1-5b658cbe7ba7 | -8.1742 | -43.20784 | 2025-07-27 04:08:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2522f4d0-2c27-39ea-9e36-10ab0d01043d | -13.07779 | -47.35171 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3445fdec-0735-393f-a3b7-bad5ef488aa4 | -10.85205 | -46.69245 | 2025-07-27 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2974fd46-5877-3a66-806f-0d12b1bf7de9 | -7.89869 | -42.633 | 2025-07-27 04:08:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f87044f4-c337-3833-9720-b6a173f5c1b7 | -7.75282 | -51.12967 | 2025-07-27 04:08:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 337f0ba5-a900-3af8-b9f4-40f56c6e1996 | -13.71821 | -45.66866 | 2025-07-27 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d953227b-e8cd-345b-8ab6-38f8d2b50585 | -14.02179 | -44.61122 | 2025-07-27 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ad4313ab-a5fb-3e48-a85d-bd2787de8bc0 | -11.96952 | -46.70646 | 2025-07-27 04:08:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a2f0edc-4396-3f9f-b515-9e2d36a94586 | -13.72188 | -45.68941 | 2025-07-27 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0573d4c9-8bc6-3e86-b462-1e2658d55a11 | -7.08857 | -44.9071 | 2025-07-27 04:08:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e65472b6-ea12-3453-b77f-e8a8e06ea69c | -7.48303 | -45.38022 | 2025-07-27 04:08:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87ff065a-c3a5-3e80-9966-72c6af60b339 | -11.10983 | -45.12221 | 2025-07-27 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1ea38550-6a1b-385e-bc48-6a83dce8a137 | -9.10455 | -39.28271 | 2025-07-27 04:08:00 | NOAA-20 | CHORROCHÓ | BAHIA | Brasil | 2907707 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4a53d8e5-dbda-3f77-8d38-6db822874c65 | -8.0091 | -48.16827 | 2025-07-27 04:08:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3694b86b-1981-3d09-ab79-9163f653f565 | -14.21981 | -43.95082 | 2025-07-27 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7697616a-ac8c-3065-98f5-23760a070155 | -8.01014 | -48.17177 | 2025-07-27 04:08:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f40676e0-38c9-3646-93d0-51d480d5620d | -14.21375 | -43.94615 | 2025-07-27 04:08:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4e6fa5d-3232-3c9b-b348-fb05f5f45570 | -12.6746 | -47.00695 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd8273ce-44d1-3f6c-a06d-e8b1066cfda5 | -14.02455 | -44.61544 | 2025-07-27 04:08:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| fba9b411-656d-3cd6-81ee-5e41909aeb24 | -13.09389 | -52.13602 | 2025-07-27 04:08:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99932329-f494-3d75-8dc6-e3176b150e97 | -12.67831 | -46.99059 | 2025-07-27 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f6b2d3b6-ce8c-3820-ad94-6ec5d7be8523 | -13.48582 | -45.50134 | 2025-07-27 04:08:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README12.md)
