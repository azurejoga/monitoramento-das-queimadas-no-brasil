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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 884799d7-baa8-3111-ad27-8bdb6aebf94f | -6.25608 | -48.03734 | 2025-03-15 04:17:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99b446ba-c4f6-3995-b011-6462d98ba194 | -6.20274 | -48.04189 | 2025-03-15 04:17:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4bdcd257-f12b-3e27-bf5e-60fac1190ea4 | -9.8219 | -40.56785 | 2025-03-15 04:17:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 73b304d5-d4c8-39a0-8c7f-009c7656267f | -6.25604 | -48.0356 | 2025-03-15 04:17:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a05d325-da3d-3311-bc36-4c2c366962f1 | -10.05723 | -44.64061 | 2025-03-15 04:17:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb6a3bd4-c7ba-31fc-bfa2-4ddcd3c55a32 | -6.19908 | -48.0413 | 2025-03-15 04:17:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 453b8601-0e40-3dc6-a67b-749ea451b655 | -6.70946 | -47.60156 | 2025-03-15 04:17:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 316ce08c-8e20-3666-a92a-f33d8ac5b709 | -8.3975 | -43.84806 | 2025-03-15 04:17:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| af23e202-05c3-3a5d-841f-7687e69a2a32 | -6.20204 | -48.04619 | 2025-03-15 04:17:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 408989d0-c886-3a2c-963f-885a29014f46 | -9.26126 | -47.03457 | 2025-03-15 04:17:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8103a94-2c8b-38bb-bfd4-86d8b9d553a8 | -7.06049 | -44.3876 | 2025-03-15 04:17:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82f9777d-db3e-3c6e-9697-57ffdbbaf75b | -7.2432 | -44.78124 | 2025-03-15 04:17:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2c9e4047-2bbc-34fe-9cc0-e22c1a0fc766 | -7.28081 | -43.73456 | 2025-03-15 04:17:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 511eb108-28b9-384f-a63a-b53eacf7edf1 | -6.22765 | -48.05053 | 2025-03-15 04:17:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f7bf260-616f-3da4-9915-e752918c98a1 | -8.10656 | -43.14258 | 2025-03-15 04:17:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0cca8faa-3684-32f9-812c-b8f8385908c3 | -9.33025 | -37.8384 | 2025-03-15 04:17:00 | NOAA-20 | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 718d2d7a-6a6b-38c9-a799-9ef93661915c | -6.19542 | -48.0407 | 2025-03-15 04:17:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 859d766c-01c0-3343-b739-198ff9d75c26 | -8.10714 | -43.13887 | 2025-03-15 04:17:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 1594e698-b240-3daa-8253-ecb5ad926674 | -7.0526 | -44.39344 | 2025-03-15 04:17:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f519815-2f4e-34f5-81f9-bf8e1a84cfd8 | -6.2064 | -48.04251 | 2025-03-15 04:17:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0ca0527-7364-378d-afc4-c9abf4fc0e77 | -9.09262 | -40.43755 | 2025-03-15 04:17:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 12.8 |
| d1aafeff-eb4c-3e81-be49-995f6b11a9c4 | -7.05718 | -44.38708 | 2025-03-15 04:17:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61e4a840-ca25-3731-b7b7-a0c2174a66ad | -7.9805 | -43.14215 | 2025-03-15 04:17:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 4f3db80c-cd09-315a-8dc1-5f7a0932b975 | -8.83268 | -50.33811 | 2025-03-15 04:17:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8120b5b5-d3c0-32d7-8e2b-5be4032af105 | -7.24428 | -44.77433 | 2025-03-15 04:17:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec3e417a-e9d0-3a9f-9430-157de814355b | -8.171 | -41.04339 | 2025-03-15 04:17:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8ac9337a-86fb-3c14-a40d-9af8b1ce7b93 | -8.82863 | -50.33742 | 2025-03-15 04:17:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f71f3241-93a4-3c94-aec3-56e764b496af | -7.24813 | -44.77139 | 2025-03-15 04:17:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e384a3dc-0da2-33ef-9cd0-6e78494eae1d | -9.09335 | -40.43242 | 2025-03-15 04:17:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 00484509-995d-3720-abeb-655250460799 | -6.19837 | -48.04562 | 2025-03-15 04:17:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f5a4544a-0f3e-36d6-a7fc-5f8790114acd | -6.2057 | -48.04678 | 2025-03-15 04:17:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3e39ca11-9a21-3abd-8bbe-cc8926a2f081 | -9.14235 | -37.67489 | 2025-03-15 04:17:00 | NOAA-20 | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5256cdf5-353c-3406-a6d6-dd562d2c4e78 | -6.20936 | -48.04741 | 2025-03-15 04:17:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 50db5aad-d7d7-35e0-81e7-8ba6927f1f2e | -6.19978 | -48.037 | 2025-03-15 04:17:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5a336e64-059c-3811-b210-8d5b3f8af042 | -7.24759 | -44.77485 | 2025-03-15 04:17:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2f1fac45-589a-3e9d-8fbd-a078aef83df7 | -7.24374 | -44.77778 | 2025-03-15 04:17:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e54103d1-04dc-3e5a-9651-9f6f9e908740 | -14.20755 | -47.01831 | 2025-03-15 04:19:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e79d14df-f76f-3199-ba5a-7630065b5724 | -10.60274 | -45.10538 | 2025-03-15 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 9256117f-3e4a-3802-94d9-fd26f537ff38 | -11.88394 | -46.94416 | 2025-03-15 04:19:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4cb80d21-209a-3461-a6d7-0700272dca1e | -10.573 | -45.14375 | 2025-03-15 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 694c9ff6-7cb3-3cd2-8b18-126cde9c53a0 | -10.65789 | -44.39606 | 2025-03-15 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3d9d4b1-d70e-349f-986d-fb6a6c346557 | -11.56573 | -47.62283 | 2025-03-15 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 820ec6c1-0ab6-3d2c-81f4-1ca1fd158267 | -12.1639 | -45.48079 | 2025-03-15 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f7363c1-d1e4-3111-beb2-28675d9721d9 | -10.60219 | -45.10889 | 2025-03-15 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1ea506b7-fdc6-30cb-80b7-e6389be10a23 | -11.57037 | -47.61592 | 2025-03-15 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9b36694b-4577-3e9c-be1f-0687f1d773ec | -11.10901 | -54.49869 | 2025-03-15 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 81bcf1db-f3c9-33b2-a5b6-e7f576a69791 | -17.77813 | -42.80891 | 2025-03-15 04:19:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d0d459f-9a02-3ec3-a8ee-e50a6b684578 | -10.6055 | -45.10941 | 2025-03-15 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9ee3fa1a-4021-339a-a299-1f2ceee37356 | -11.79341 | -46.6432 | 2025-03-15 04:19:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41898e44-82cb-3f71-93f6-8b7ed60e071c | -11.56295 | -47.61853 | 2025-03-15 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c9cb313d-091b-38a5-a6b5-b24323b05d9f | -15.60627 | -42.33469 | 2025-03-15 04:19:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0ba4f6f-0376-3f54-8c86-22274bf66289 | -12.7158 | -46.29151 | 2025-03-15 04:19:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5c998de0-bf92-30a2-abf7-c064e225b811 | -17.75073 | -42.8952 | 2025-03-15 04:19:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f296248b-b818-37f6-813a-eca17a47fe8e | -4.80954 | -48.37503 | 2025-03-15 04:19:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f876108c-9e24-3e07-9b65-381aab554e4e | -11.79284 | -46.64675 | 2025-03-15 04:19:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 026073e6-190f-32b5-9724-c23e4b7f21a4 | -16.07151 | -53.75293 | 2025-03-15 04:19:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b332fde5-23b9-3872-bb20-843dbe7f0037 | -11.57316 | -47.62023 | 2025-03-15 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d8fa404-5595-35a5-a843-8188127e7774 | -15.91418 | -43.91359 | 2025-03-15 04:19:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ef911708-f504-3751-9282-0d3f3fb35560 | -11.8806 | -46.9436 | 2025-03-15 04:19:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 12863819-707b-3e17-b2c0-b4288c666742 | -11.25981 | -52.46555 | 2025-03-15 04:19:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8aacf66a-b32c-37b4-b2b1-4c13a9fa6f35 | -10.60936 | -45.10643 | 2025-03-15 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3ea75ea1-b9a1-3754-95cd-f99601cacaff | -15.63053 | -57.31258 | 2025-03-15 04:19:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a46e0cf6-6845-3b12-80f3-47c2402e4937 | -11.88786 | -46.94112 | 2025-03-15 04:19:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea17680d-4a46-3f72-b68a-1531265851fa | -11.56233 | -47.62226 | 2025-03-15 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d0c64586-a0d2-3b6a-a081-be9841ac0114 | -10.66459 | -44.3971 | 2025-03-15 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ed4bb6a-377c-38ff-9512-a2197d8ce65c | -14.13506 | -41.69213 | 2025-03-15 04:19:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 407b4d2b-49d5-34c0-afe1-eb063af429a3 | -11.56975 | -47.61966 | 2025-03-15 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a375e6e1-cae9-3a5f-9dee-dc80d4e51212 | -15.62795 | -57.31575 | 2025-03-15 04:19:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 108e2468-31ef-3ad7-a05a-b7599a06394e | -12.16059 | -45.48026 | 2025-03-15 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48909703-ddde-3c7c-a40c-01224c9b9239 | -5.4411 | -45.43195 | 2025-03-15 04:19:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c2a4dcc-0180-3d1a-8ea3-71985ddb6d2b | -15.6288 | -57.31159 | 2025-03-15 04:19:00 | NOAA-20 | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 429763f9-27b9-30f3-828b-6e843cb8ee28 | -15.26492 | -51.47704 | 2025-03-15 04:19:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6884302b-d54e-3b4f-a046-622508932d16 | -10.60605 | -45.10591 | 2025-03-15 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0cd007e9-9140-32d8-bc95-5fd526914f27 | -17.09535 | -43.80551 | 2025-03-15 04:19:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc7bfc5e-6697-3582-b952-20045fb7d52b | -5.07308 | -47.21461 | 2025-03-15 04:19:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec3eeba8-5107-385f-8592-c34df6bd38c7 | -5.88669 | -42.68133 | 2025-03-15 04:19:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ca9c2972-d5e3-3f91-9f33-07e5a93de6b7 | -15.261 | -51.4763 | 2025-03-15 04:19:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c7c9da83-b93c-3379-9232-8f63f9e01e0a | -10.57631 | -45.14427 | 2025-03-15 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 126bd09b-dcb0-3976-b95b-821148dc2002 | -5.97067 | -43.75398 | 2025-03-15 04:19:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c4d03cbb-e5ce-313f-892e-2867afec04d0 | -15.26585 | -51.47187 | 2025-03-15 04:19:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0df3d849-90d6-36a0-9fc6-74bda64923a8 | -4.81648 | -42.98787 | 2025-03-15 04:19:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34e9b63a-34af-3cc7-b12e-ae55cbcaa363 | -16.07063 | -53.75754 | 2025-03-15 04:19:00 | NOAA-20 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ca2555cf-fb43-31a3-b54e-0c5392655b10 | -11.88728 | -46.94473 | 2025-03-15 04:19:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b54fc14f-d10c-3807-98e1-c6adb0468eac | -16.679 | -43.88316 | 2025-03-15 04:19:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99394f35-9151-364e-8ea5-4fb6f480c13b | -14.85003 | -46.80341 | 2025-03-15 04:19:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe8d86ee-7b07-3987-b516-6dd00cc8d664 | -11.79009 | -46.64265 | 2025-03-15 04:19:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2348bdac-21f9-3bfb-a07e-575f9440df5f | -17.9143 | -43.38845 | 2025-03-15 04:19:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 485c3690-e9ec-3b14-9f72-c2be2e64530a | -15.60469 | -42.33248 | 2025-03-15 04:19:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d0e49668-445a-3572-bea1-9bda5f56e24e | -14.62175 | -45.30393 | 2025-03-15 04:19:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b2a63c9-cade-3f16-8f23-aebb2accb51a | -5.88328 | -42.68081 | 2025-03-15 04:19:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 608cba58-80ba-3079-b0be-3401af5762ce | -15.91456 | -43.9147 | 2025-03-15 04:19:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| aff11661-baf7-3546-93fe-8ed9d89eb9fd | -15.68037 | -41.58208 | 2025-03-15 04:19:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9a8b2a4e-9ca0-3f56-8211-5d0d02186051 | -11.11413 | -54.49976 | 2025-03-15 04:19:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0bfe786c-6c4d-3b22-8023-ff08aaedc441 | -11.56635 | -47.61909 | 2025-03-15 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78480950-e31f-3cb8-bd39-0cf5ac716eca | -11.57254 | -47.62395 | 2025-03-15 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6b79036-b1b9-3cb5-8500-fc81f4b0bbc3 | -12.71328 | -39.08518 | 2025-03-15 04:19:00 | NOAA-20 | CRUZ DAS ALMAS | BAHIA | Brasil | 2909802 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3eb2dfd4-5cd2-33cf-a21c-ba8bd53d14aa | -10.57962 | -45.1448 | 2025-03-15 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dcaf668a-6ea3-3eff-9537-9fd62daaeb1c | -6.15801 | -44.42247 | 2025-03-15 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d3361b98-6bfe-39ea-b765-f686f9451e01 | -14.21086 | -47.01887 | 2025-03-15 04:19:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2172f36-f2ce-34db-9ab8-89e2b46593f5 | -12.37288 | -47.3256 | 2025-03-15 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README5.md)
