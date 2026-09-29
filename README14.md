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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b845941b-aba2-3a10-876e-23ed70303267 | -7.26851 | -43.38017 | 2026-09-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 28f23465-2148-3c7a-a110-8d139c205ea4 | -3.01553 | -53.87291 | 2026-09-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c9a97b6-4c0d-35ae-8963-30559d6c6d9b | -5.36288 | -36.84954 | 2026-09-29 04:14:00 | NOAA-21 | CARNAUBAIS | RIO GRANDE DO NORTE | Brasil | 2402501 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2bc8f137-e8d6-3cc3-adba-8e822069ec2d | -5.7291 | -43.43373 | 2026-09-29 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3245e9b-5a92-39db-8d89-32c6b767bdbe | -4.81987 | -45.63529 | 2026-09-29 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 713b3845-8c71-37a8-b1c3-1b3c6bd1492b | -7.47916 | -45.8165 | 2026-09-29 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 21fb911b-1b9a-3f3a-8ada-3a2e5eacafa8 | -3.97982 | -38.6129 | 2026-09-29 04:14:00 | NOAA-21 | PACATUBA | CEARÁ | Brasil | 2309706 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 30f962d2-f68f-32d0-a102-a95023308f17 | -4.50131 | -49.64249 | 2026-09-29 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5613c001-8b42-3821-8485-d6107ed4acdf | -4.56216 | -44.08043 | 2026-09-29 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84be5e71-8511-3841-89b4-e73b59ee9512 | -7.51839 | -47.34013 | 2026-09-29 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b92a12dc-5c8a-33b9-b062-a67152d76d7b | -6.31492 | -52.62949 | 2026-09-29 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 40559fad-661d-317d-8b28-5682d765fc25 | -7.56877 | -47.36976 | 2026-09-29 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2486bbc9-14d3-3fc6-94f3-02f2b0bfe9b7 | -8.97369 | -44.1595 | 2026-09-29 04:14:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0c6db3e5-8686-34aa-a086-a2e12213f6cb | -5.43411 | -43.44704 | 2026-09-29 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5fbd8df-4185-38e6-8468-05e59ddd18b4 | -5.80383 | -43.62938 | 2026-09-29 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1288b1c6-3047-30f7-ac0a-01950c7fbc82 | -8.23788 | -45.46761 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c850d8d9-5a4f-3cda-8b61-4c2733fa971d | -8.73443 | -44.89632 | 2026-09-29 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad6d142f-5c8d-37f6-9807-4cf24aeec71e | -7.67624 | -44.89441 | 2026-09-29 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| efbceaa5-be53-3e32-8897-e124bf833963 | -6.02637 | -42.57202 | 2026-09-29 04:14:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9450c5a2-248e-37ba-b5c7-6ff4760f6000 | -7.60437 | -46.45946 | 2026-09-29 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b70f09f-8c08-3754-a514-19ec57ced5d2 | -5.73622 | -45.18286 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a43628e2-37a6-38ed-9778-5290e423bb89 | -7.90582 | -45.45635 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1d4fba14-bdcf-3577-8ec2-a55c6b199f27 | -7.46372 | -45.8022 | 2026-09-29 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e6da3611-289a-3226-9c61-4b0175c5b9da | -7.71837 | -47.05988 | 2026-09-29 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f3d0d0fb-00b9-33d0-a809-fd2b3c7dc629 | -6.95582 | -41.60349 | 2026-09-29 04:14:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 390084bb-0153-3ee9-814d-400f5d835067 | -5.48204 | -45.12458 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cbd78259-eaea-3d08-8116-f5ee516efe6d | -8.35144 | -46.88665 | 2026-09-29 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 279a28be-4350-3ce4-b8f9-f5d83da9b43a | -3.5046 | -50.47936 | 2026-09-29 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 434d822f-339c-37a7-958b-22b3abda32d9 | -5.73585 | -45.03028 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 498d2b10-9a06-35ea-a140-dcd8f7a041f8 | -3.71063 | -54.22943 | 2026-09-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c08f5c0a-2261-3c8b-bd7d-cd5f70c95fc5 | -4.8648 | -44.05934 | 2026-09-29 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| daa4ff9f-3e7d-386e-a8d6-66ee45809a5e | -5.61476 | -44.99657 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 46ca1036-18f1-33af-b7e1-5e70ef87a5dc | -7.24399 | -45.2645 | 2026-09-29 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 67724fc8-9a6a-344b-8ebe-c85adbee94c1 | -6.99976 | -45.34286 | 2026-09-29 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cf65c4c7-af68-36a8-822a-4bfee5e86075 | -5.87422 | -43.59077 | 2026-09-29 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d17c5849-3eca-3378-9c21-200fc89166b3 | -6.95111 | -41.60647 | 2026-09-29 04:14:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 8df587ad-e282-3514-8a24-1a6061cd7967 | -7.24756 | -43.36275 | 2026-09-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 9c97c864-a50a-364b-9988-98cc4f1ec1b0 | -7.26575 | -43.3762 | 2026-09-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 30689eba-c5c1-347c-a4dd-2fd196e8c9a7 | -6.91226 | -47.00876 | 2026-09-29 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd3d745b-f600-303b-b4cd-be49c0ba2974 | -4.50146 | -42.55596 | 2026-09-29 04:14:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0ad129cf-045b-357c-a9a9-7c844218d091 | -5.73175 | -45.05613 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 5e45a487-8746-3870-9975-80ccd99fda2d | -7.82931 | -47.9255 | 2026-09-29 04:14:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 801873ff-630c-3e48-b980-06734c603965 | -6.15808 | -52.91156 | 2026-09-29 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffddde51-21be-37b0-b174-fce53e1df1d3 | -7.9976 | -43.26143 | 2026-09-29 04:14:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| df5caa67-1feb-3099-950f-52758a248691 | -8.7372 | -44.90036 | 2026-09-29 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| acdb6666-6af9-3178-80e6-7fca077d6058 | -3.51294 | -50.31045 | 2026-09-29 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2098ac89-8bd5-3b33-87bb-44e1bf81dd22 | -3.04976 | -46.92298 | 2026-09-29 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e17948d9-59bf-3b2e-b55c-78e7eeb59efe | -3.35942 | -54.74324 | 2026-09-29 04:14:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 46216de0-a74d-36a4-a5b0-61379c1c77d5 | -7.61882 | -47.83558 | 2026-09-29 04:14:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f0c1f5c-702e-33d5-a74f-14e56649dbd4 | -7.83391 | -45.81304 | 2026-09-29 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d649e53-9cec-3c70-903e-15b702258817 | -5.02717 | -43.57041 | 2026-09-29 04:14:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 712c0c30-8fc5-39af-8fa0-e046b50c857b | -6.16707 | -52.82752 | 2026-09-29 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 012b6f2e-cf3c-320c-9d0f-acf0fb18f6fb | -5.738 | -45.17158 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5ff9d2dc-9648-3184-a816-84cbfc570449 | -8.37374 | -45.45123 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3fc2d660-e584-39dc-b018-da7872a784d3 | -6.32363 | -46.34248 | 2026-09-29 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62935c82-23ae-3e7a-bc84-f41a9d17b61b | -6.16295 | -52.91611 | 2026-09-29 04:14:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17da38e8-5dba-31eb-be5d-0b7000896eb3 | -7.83266 | -45.82068 | 2026-09-29 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 04899b77-f824-31e0-bf7b-35d380306e05 | -7.24871 | -43.37708 | 2026-09-29 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| ac37699b-291d-38c6-acd1-6704ab03c46e | -8.4336 | -47.89355 | 2026-09-29 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b75e4657-b0a1-3eb4-a318-ba85e9e41c50 | -3.01535 | -53.8729 | 2026-09-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c589918b-ac8b-3920-ae1a-e96144ae3c90 | -7.83046 | -45.8125 | 2026-09-29 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 07685660-00b3-3cf0-896c-fd913c95bb02 | -7.89962 | -45.45156 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 019494ba-c823-37cf-b9f2-ddfb4428602d | -5.74426 | -45.17643 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 17f354c5-58cb-3a62-9752-03edf292a888 | -3.70858 | -54.21195 | 2026-09-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 17a1aed2-dfdf-3892-b240-802504285f45 | -3.71238 | -54.21944 | 2026-09-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 843c6478-5e0c-32eb-bb88-0955f57f6169 | -3.70532 | -54.22326 | 2026-09-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8bb0322c-a0df-3f02-83e1-7fa223d094ce | -1.99385 | -47.63191 | 2026-09-29 04:14:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90f05aab-da23-3f28-814e-4b6e3cddcc8b | -8.03025 | -43.33764 | 2026-09-29 04:14:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 09c30b20-9a08-37ee-894c-269803b9abfa | -5.73398 | -45.17479 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2c9b5a15-a57c-355b-8bb4-053ebea92107 | -3.27136 | -50.13597 | 2026-09-29 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f817c2b0-94a4-3216-b126-e7fa45967ec4 | -7.69546 | -48.86434 | 2026-09-29 04:14:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 6.6 |
| f3f9e3f5-76d7-3577-8e3c-5ac8b7394725 | -4.25376 | -51.04812 | 2026-09-29 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5aeb93c-333e-35af-8074-47830536a0b2 | -6.05248 | -46.1593 | 2026-09-29 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd0af6b4-f880-32ed-a7e9-3f64ebef11c5 | -5.72964 | -43.43029 | 2026-09-29 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c7f14b8-82f3-3976-8142-d879b8421b20 | -5.73633 | -43.27962 | 2026-09-29 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a782da8-8d23-384c-8a0f-da650ff7ba80 | -5.57894 | -42.73607 | 2026-09-29 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| eb326f60-1283-3b64-96a0-227b853437d0 | -8.23863 | -45.44137 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 27fc97ec-da16-3c4a-ba58-9e76f21b9a7a | -4.29516 | -49.08964 | 2026-09-29 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b711ab5d-3b1d-3d1a-a727-232c3130bef4 | -6.68575 | -46.99268 | 2026-09-29 04:14:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4c161b0b-8905-3733-9d52-286a5e671c79 | -5.14061 | -35.70226 | 2026-09-29 04:14:00 | NOAA-21 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 6e22e6c0-271f-3f55-b1be-169aa5af5654 | -7.84708 | -45.81901 | 2026-09-29 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a7c03da1-208e-3985-b73e-19c7e62c893a | -7.48523 | -45.94689 | 2026-09-29 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3646a768-b267-34c2-bbd5-87cdd7ee955c | -8.3653 | -45.4388 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| efd94b8a-796f-3426-84a9-1eae21146d88 | -8.23921 | -45.43773 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6605ba5e-b92d-3899-a973-9356a24e3609 | -7.51541 | -47.33503 | 2026-09-29 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2dcb0d58-3056-3319-91e7-e07d57937a4b | -7.40739 | -42.61526 | 2026-09-29 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| da9500eb-ce58-3745-bb25-757e88873a7a | -3.60317 | -49.4563 | 2026-09-29 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3385cd9-dd4c-3cc3-8cc1-b8c12726925f | -5.73702 | -45.02291 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f542f288-5740-3e52-81e0-570c798e7ed9 | -7.56952 | -47.36528 | 2026-09-29 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 207d12c4-d6ac-3a29-a650-217bbb0db9c1 | -8.23727 | -45.47139 | 2026-09-29 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e4f8c2a-4751-3cf0-8acb-42ae760cb700 | -3.4199 | -48.33927 | 2026-09-29 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a45ac8d9-05f4-3966-a554-212049835ab7 | -7.07903 | -41.73783 | 2026-09-29 04:14:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f53be5fc-0d59-31b8-8b2f-49db30deccbe | -7.38022 | -42.12828 | 2026-09-29 04:14:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 939b8bde-bf3c-360d-941d-03d7ee7f771f | -5.4385 | -47.27287 | 2026-09-29 04:14:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e6d65533-6123-36e2-b7be-53293f095906 | -7.51862 | -44.55959 | 2026-09-29 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a617001-9a78-3741-b4c9-dfc7fc054577 | -7.69179 | -44.92625 | 2026-09-29 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a25c0f2e-0358-32ae-b65c-f85ae53e8b77 | -5.73516 | -45.05667 | 2026-09-29 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| fe71d4d3-1875-3724-8b4c-c3915fc8aad2 | -3.60393 | -49.45164 | 2026-09-29 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5317171-c831-3a75-8e50-f4697392f65c | -7.27586 | -44.30836 | 2026-09-29 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3468d5a-8635-3985-a39a-4aba20b95cd1 | -3.71314 | -54.22289 | 2026-09-29 04:14:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |


[Clique aqui para ver as próximas entradas](README15.md)
