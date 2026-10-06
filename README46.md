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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c913a158-3fef-3dca-b0be-4a895df456d6 | -6.45652 | -55.43625 | 2026-10-06 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f03b37f2-0dbb-3c39-acf1-cc3717d49ef6 | -4.4593 | -54.97564 | 2026-10-06 04:40:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c568bd4b-0365-3d15-af6e-6cbbe9002b44 | -8.98846 | -46.76196 | 2026-10-06 04:40:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 18697a73-12bf-39eb-b5b3-57f17439f424 | -6.00179 | -47.39827 | 2026-10-06 04:40:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| fefccaf9-bc4e-33b3-8339-11b3fc4e9d74 | -11.23211 | -45.26723 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ea010295-f534-367e-b8c1-a55838d63815 | -6.4471 | -55.43459 | 2026-10-06 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb5ea2f2-4614-3e67-88ed-0944b46e9d19 | -6.2085 | -55.67029 | 2026-10-06 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56eda751-dd7a-38e2-8afd-38cfde3d6fb4 | -11.53246 | -44.89531 | 2026-10-06 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aceaf252-1583-3a1a-b98a-69405cc604d4 | -4.80976 | -54.73115 | 2026-10-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4881189-daba-3d96-9beb-e058f4add351 | -8.69761 | -45.21001 | 2026-10-06 04:40:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db0e9097-1870-327b-a752-33f8744ecc20 | -11.29252 | -45.51343 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| b1ffd1f6-d256-3b03-9189-74ee87cb03fc | -8.27706 | -47.91764 | 2026-10-06 04:40:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b6a5361d-2c72-3de5-b4d5-c4d3ba268a21 | -11.82427 | -44.69537 | 2026-10-06 04:40:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| ee518f6a-51d3-32c5-ba56-c89e59d5294f | -3.54109 | -59.48714 | 2026-10-06 04:40:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e26884c-0f90-3396-b066-515f5fe06c25 | -11.58365 | -48.59461 | 2026-10-06 04:40:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 728feef2-3e69-3b51-ac42-48ae4c6e0e84 | -7.72845 | -45.46205 | 2026-10-06 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 341ea3fa-f9aa-3410-8fb7-721c24daf507 | -10.70478 | -48.54765 | 2026-10-06 04:40:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c524ddaa-3c12-3705-a6b5-fd5dbc0aa895 | -5.82181 | -53.8591 | 2026-10-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fb65e8d-11a7-3df4-80b3-ab764a19df91 | -6.45377 | -55.44362 | 2026-10-06 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5cedf38e-b99b-3a39-96b8-3c630d7d2dac | -11.28206 | -45.50743 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.7 |
| 8777f3cd-f7b3-342e-92af-cf291c818f9c | -9.13907 | -47.9856 | 2026-10-06 04:40:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| df229ede-f822-3708-b1c2-65d100245ff6 | -4.46175 | -54.96085 | 2026-10-06 04:40:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9e869e77-9cae-3801-be29-b2614d2f2399 | -6.04993 | -45.23013 | 2026-10-06 04:40:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a92f54c-9546-39be-ab7c-a4cc034b249f | -6.44606 | -55.43179 | 2026-10-06 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 18971641-e72d-3a80-9669-5248413ed57f | -5.59025 | -47.2726 | 2026-10-06 04:40:00 | NOAA-20 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7ca5055-c6e3-3adc-95e1-41f27a88e133 | -5.58748 | -47.2686 | 2026-10-06 04:40:00 | NOAA-20 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33f61b35-846b-3fbf-9f59-8d3b5fb2639d | -3.70713 | -58.93439 | 2026-10-06 04:40:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f193ddcd-3666-3a20-8cb5-ec8750185e0c | -6.22684 | -51.81802 | 2026-10-06 04:40:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8304cfcd-ca46-3b17-bc4e-4e160339bec0 | -8.70363 | -45.21962 | 2026-10-06 04:40:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a3079e04-c719-32a1-8d8b-03de3d1ec720 | -7.71607 | -45.44769 | 2026-10-06 04:40:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eab985c8-ae6f-3e52-bf01-06fae985a6c6 | -6.36968 | -42.54511 | 2026-10-06 04:40:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 962cc66e-f520-350c-815c-e04a010b3fee | -5.67857 | -53.49569 | 2026-10-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eb77ada3-950d-324c-9ee4-84a9a0dd6e96 | -5.89382 | -53.63753 | 2026-10-06 04:40:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5c0c4c21-65f3-3842-a171-f3e8b5dbd448 | -6.33686 | -46.94863 | 2026-10-06 04:40:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce432eb6-f80b-3653-93f3-0a6dfd5e3027 | -11.6927 | -43.67537 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 807e1c7c-51fe-3fac-9d7b-46e4d1e7f085 | -11.26967 | -45.51464 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| f27d529b-b89b-3efe-a10a-8d1b66869d3b | -11.35966 | -46.65968 | 2026-10-06 04:40:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc636a06-6223-32d3-b718-1e1fb8104d88 | -10.19638 | -36.24476 | 2026-10-06 04:40:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| bd393951-5856-3f59-b3c8-d92e858f27d1 | -11.22611 | -44.85414 | 2026-10-06 04:40:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 997bb220-8eab-3ea8-a4b7-06ccd7f1333f | -8.70427 | -45.21535 | 2026-10-06 04:40:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a121db48-182f-3600-9700-220c525d4efd | -11.36248 | -46.68821 | 2026-10-06 04:40:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7334fedf-e226-35ff-a820-ece0a1e80837 | -7.7653 | -44.58191 | 2026-10-06 04:40:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bde07632-abcf-32bf-80f5-5551a9d0c86c | -8.69999 | -45.21908 | 2026-10-06 04:40:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0ce9ac4a-83ed-34c0-9024-d4358b290541 | -9.80014 | -44.78424 | 2026-10-06 04:40:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc5441d3-bda6-3b8f-9f3a-d9b28a3e2790 | -6.88419 | -43.678 | 2026-10-06 04:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c160e077-66a7-3035-9739-cad443b20871 | -11.67443 | -43.67375 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f462562-10eb-3647-8463-21d129b18dc7 | -11.27337 | -45.51521 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.7 |
| cb693338-cadd-3ae2-b1f5-509dd0fdabe2 | -11.27902 | -45.50243 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.5 |
| bb68c518-3782-3a48-bd26-bd992199b669 | -7.10387 | -42.5419 | 2026-10-06 04:40:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2b37d29f-99cd-3f29-94e8-9fe7b0d64e57 | -6.18858 | -42.96054 | 2026-10-06 04:40:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 615bbddb-48cb-3d3c-9621-6493b0d45e60 | -6.82136 | -39.30684 | 2026-10-06 04:40:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0bb94da1-ae06-3c9f-b0e0-830b69b04994 | -6.31948 | -55.767 | 2026-10-06 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fa48cc5-d8b0-3903-bc89-a679bf1ba01e | -7.10441 | -42.53813 | 2026-10-06 04:40:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5d748664-b408-34fb-a137-6b1bb70fa86d | -11.63077 | -43.65188 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce26e453-8285-32b0-9630-53cf2f91c24c | -5.8277 | -45.00677 | 2026-10-06 04:40:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f51583f2-221a-369d-bfd6-b84a5900f6b9 | -6.18355 | -44.85539 | 2026-10-06 04:40:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 65ecb642-3ea9-3122-9f8a-933cd42e31ab | -11.69275 | -43.66444 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec382c9a-bbc7-36f0-aab6-fa4cea79eb5c | -6.93656 | -43.67789 | 2026-10-06 04:40:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3108f800-47f9-38db-9014-6a7131edd059 | -10.49615 | -44.41661 | 2026-10-06 04:40:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5eab9791-8291-30c9-ba03-2899010e037b | -6.43697 | -47.69824 | 2026-10-06 04:40:00 | NOAA-20 | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4af27a08-5a80-3b7a-8a26-831eec80c9b1 | -9.8619 | -44.81011 | 2026-10-06 04:40:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 044e4172-b3ba-330d-89b9-748f0e1f3054 | -7.37685 | -46.22196 | 2026-10-06 04:40:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7376f47-1a2c-3d7c-90d5-27a0eb80fd5c | -4.29255 | -54.80672 | 2026-10-06 04:40:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 548cbb4c-5285-3d0a-9317-4e4c08518af7 | -8.74146 | -47.8798 | 2026-10-06 04:40:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 94c42ef8-5220-33bf-b13f-64f5ea637cf8 | -4.467 | -55.07664 | 2026-10-06 04:40:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 00f98f25-1a40-3b32-b700-908330c570f4 | -11.3638 | -46.68785 | 2026-10-06 04:40:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 324517c2-8b65-3fe4-ab94-f2eb3efcbb3f | -5.83065 | -45.01133 | 2026-10-06 04:40:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| bbd701de-7c4f-398d-bdba-808587aae3d7 | -6.46232 | -55.45049 | 2026-10-06 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bba93335-c3de-35fa-a1f1-cf062b0b7f60 | -6.71781 | -45.97469 | 2026-10-06 04:40:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0f12577-a617-3e4a-be21-c66c1174dcdf | -11.24208 | -45.25717 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 246dc590-8a56-307b-b514-dc42de5c4e41 | -6.17187 | -46.74476 | 2026-10-06 04:40:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 087c26e6-60d5-3b8e-bfe3-8de0997f12b9 | -7.72182 | -47.06499 | 2026-10-06 04:40:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2948b0aa-1dd2-3a50-871d-207d32e11b26 | -10.19784 | -36.23302 | 2026-10-06 04:40:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| b1dfadef-5b89-300e-b214-d73f91419703 | -7.75286 | -49.20826 | 2026-10-06 04:40:00 | NOAA-20 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 061ada1e-7a8c-35be-8f15-d3dde6d5d46f | -6.00842 | -47.3993 | 2026-10-06 04:40:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 7ee51cbe-b0e2-364f-8a12-b0be7be1b26c | -4.46574 | -54.97331 | 2026-10-06 04:40:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7ec32a4c-8ecf-399a-8051-16696f3604c5 | -11.26727 | -45.50523 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 37ee47a0-c218-3afc-87b5-16af6ed7f096 | -11.26357 | -45.50467 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d9dbf980-6a48-3ad1-a5c3-5b7ee4811d8e | -12.19425 | -44.65485 | 2026-10-06 04:40:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5d6d3f4-a3ed-363b-8190-8eb353844ae6 | -6.4452 | -55.43686 | 2026-10-06 04:40:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f8a53bc-1713-3404-8590-099537668bd1 | -11.26164 | -45.51796 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 14b8d29c-0b32-3867-9b57-65a996d07b79 | -5.83715 | -45.01646 | 2026-10-06 04:40:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| e450f966-6a1a-3db2-9616-309c54bfbebc | -5.85077 | -45.02269 | 2026-10-06 04:40:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4d2a1e2d-1e48-3687-934c-b050e3750704 | -9.86948 | -44.81108 | 2026-10-06 04:40:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2bdcf20b-f927-3a10-aa64-275fb7397d7f | -4.46401 | -54.97646 | 2026-10-06 04:40:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 37358b8e-2761-3c2c-8a02-1db6bae62dbc | -11.29119 | -45.52241 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 33.1 |
| d75ee7f1-3137-3230-ae25-3266b19dbc6a | -8.58072 | -45.65746 | 2026-10-06 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13e61388-82bb-37f4-959f-b265c905b891 | -12.53204 | -47.57866 | 2026-10-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fac96349-aa07-33e8-a824-cca0631530a8 | -3.96719 | -56.12902 | 2026-10-06 04:40:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c87820d4-3771-3fe3-b098-4c465073d83f | -5.83421 | -45.01189 | 2026-10-06 04:40:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 6e6a75d4-7e1f-38fa-90a0-1b8e58c5eb86 | -10.97455 | -45.41702 | 2026-10-06 04:40:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a3d278f-4020-3bb8-bb11-841e4cbc6894 | -6.19011 | -44.86068 | 2026-10-06 04:40:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3551d191-f54b-3be6-beea-a9f303ad66ca | -12.93338 | -47.44539 | 2026-10-06 04:40:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4484d417-065c-3be2-aed6-736f3ec2428c | -11.76721 | -44.92962 | 2026-10-06 04:40:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa5bbd49-b8bb-36ca-9d32-7ee23082091f | -11.6922 | -43.66829 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d214e74-2172-39f6-bf59-d42fb3a764dc | -8.58367 | -45.66198 | 2026-10-06 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f29d23bf-956a-38dd-9d69-9ebf19a966e6 | -10.36257 | -45.0333 | 2026-10-06 04:40:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a4409e9-d85a-3423-a2bb-971f361a9e15 | -11.6911 | -43.67597 | 2026-10-06 04:40:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e61deceb-a85d-3194-b687-365038a70895 | -8.58133 | -45.65345 | 2026-10-06 04:40:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cdd63959-f27f-3270-bfaf-bfe0be87b5d3 | -7.46593 | -43.00066 | 2026-10-06 04:40:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |


[Clique aqui para ver as próximas entradas](README47.md)
