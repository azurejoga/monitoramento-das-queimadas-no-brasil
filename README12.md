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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c9a941d2-2a58-3e1d-99b5-4d1037917c1c | -6.53362 | -55.15968 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7bef496a-71db-3992-bcac-356ce6f60d3e | -5.40606 | -49.24006 | 2026-08-04 05:04:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bc24b800-873f-38eb-97e3-e38a953979a3 | -6.54358 | -55.16124 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b28e909d-e1f8-31b4-a644-188c505e5f66 | -6.58311 | -52.22176 | 2026-08-04 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c16cdb4f-b08f-394e-bc57-3e7d0aedd5bb | -6.53748 | -55.15671 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c8b3ccc-6535-39fc-82be-622d5d08be55 | -8.34388 | -45.98055 | 2026-08-04 05:04:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 3ba09606-c777-3529-a606-f4cc88e66305 | -5.62757 | -45.91763 | 2026-08-04 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9f6cf6cf-c3ed-3b35-88e1-ea3c466a6cac | -8.9301 | -45.20458 | 2026-08-04 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c0301ac-a13d-3dad-8d78-d10fff4fc01f | -6.54582 | -55.16871 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 39ab1f5c-cd12-3e79-a3df-cf2a6447fd6c | -8.27372 | -47.54647 | 2026-08-04 05:04:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0bcb5e05-0a9f-3464-bd1e-95bd5c41d745 | -1.54761 | -53.69765 | 2026-08-04 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57fde613-b033-3ad0-bb10-be9b684dea88 | -6.55353 | -55.16278 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dea0f7ee-32a6-3fe4-9ec8-298a14ca09f4 | -6.55909 | -55.17078 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d4a8cfa4-e93f-3003-877f-7ab70ccde0c1 | -6.56854 | -56.52759 | 2026-08-04 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| efa110cc-64b9-3289-b41b-5a0334d1616f | -6.95647 | -52.80441 | 2026-08-04 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02c3e3ba-41e5-3761-95b0-6c9d6820ff78 | -6.56233 | -55.14986 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af41f552-0e79-3bef-aaf7-7179a77a5338 | -4.2757 | -48.60778 | 2026-08-04 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3e5655d7-dcb6-3dae-ae48-ce2be0fd2b60 | -5.42206 | -43.4281 | 2026-08-04 05:04:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a86abdb4-8c64-38cb-87a4-e90d3ba1b65e | -7.626 | -45.31355 | 2026-08-04 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 25044a98-de76-3705-8b4a-41de7c8bd030 | -4.36604 | -47.76404 | 2026-08-04 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a5d9b734-5bd2-3a99-9e97-6cec68043dde | -3.57859 | -50.26067 | 2026-08-04 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a1d0f59-70d4-3cc0-885c-c62eebe8af31 | -6.56905 | -55.17231 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05664d86-343f-372b-a456-b9c1c963cf71 | -7.60693 | -46.467 | 2026-08-04 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 19ee6a1e-ccdc-3e1e-908d-81adc18047cb | -5.14795 | -46.20099 | 2026-08-04 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1c0bfc8f-adb6-36e1-9cea-561b9eac8670 | -3.66667 | -49.47123 | 2026-08-04 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 6f0b3a54-79ce-3dc1-8bd3-f7da7e3d5e74 | -6.56187 | -55.17477 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 47907a24-3cf8-37c5-98ba-17593d3407bf | -8.34337 | -45.98452 | 2026-08-04 05:04:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 740c2876-f46a-35bf-a45e-1bf3b532d6e6 | -6.54914 | -55.16923 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1206f7da-5205-3fca-a2b9-23f13f585edb | -2.31184 | -48.58339 | 2026-08-04 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8dc38efd-f202-35e9-81a2-63544871ecaa | -7.60105 | -46.46775 | 2026-08-04 05:04:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 997d7802-fc2b-3670-b607-cbf62a8810c2 | -8.34961 | -45.98145 | 2026-08-04 05:04:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 3eee994d-fa49-328c-989a-e1c2a1d85d45 | -3.9235 | -59.4047 | 2026-08-04 05:04:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34a641f2-b81b-3596-8251-54e01e259aca | -4.64729 | -43.13341 | 2026-08-04 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f5b9e6d-da91-36c3-9bc4-699bf963fd97 | -3.66609 | -49.47515 | 2026-08-04 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 129bd731-84b7-39bf-8eb7-6416720172dd | -5.14203 | -46.2038 | 2026-08-04 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4c717bea-8a5f-3825-977d-2d47ec7f9d60 | -6.96184 | -52.81797 | 2026-08-04 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c6c97bbf-88df-366b-a61b-014bef9f72a0 | -6.56349 | -55.16432 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec3a6264-0f35-3894-8b2d-dc806ec528e1 | -6.55407 | -55.15929 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01ea5764-fae0-3cbf-830d-ef8bf4f43de5 | -6.55299 | -55.16626 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e6272d97-9e34-3796-b90e-1b470916723d | -6.54412 | -55.15775 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fb97aae9-c728-3bd0-baa0-8ee206953f28 | -6.41205 | -55.78984 | 2026-08-04 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e500995-8bb3-3746-8847-f15ae2bab1d6 | -3.67032 | -49.47578 | 2026-08-04 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b4598729-8173-3c70-8595-498501cd6e11 | -3.11174 | -47.9207 | 2026-08-04 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da82a33d-3eb8-3814-bfc7-e5a4eb9dd5ae | -6.56341 | -55.1429 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 338a2777-ff56-3e0d-a0b5-c5d9fb454687 | -8.3491 | -45.98542 | 2026-08-04 05:04:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 2a4bfb90-9173-3197-b05a-cecffb0f526e | -8.34859 | -45.9894 | 2026-08-04 05:04:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 47854bdc-67d6-3a87-a9b9-6d4eef3beef6 | -7.04495 | -55.43589 | 2026-08-04 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 81b8f517-85e6-3c2c-88ec-2efa3ddb0e42 | -1.63638 | -54.4594 | 2026-08-04 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2d4502b-da19-3898-9481-c298f2239a7b | -1.65067 | -54.45456 | 2026-08-04 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62fe80d2-4bfa-3aee-bf2f-ba234a681f90 | -5.04691 | -43.26385 | 2026-08-04 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d6979fa0-43c4-3023-be6a-069f381c94d0 | -3.03141 | -48.41597 | 2026-08-04 05:04:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f38bd971-a3da-3ad9-8686-f92f798efd71 | -8.27889 | -47.54726 | 2026-08-04 05:04:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 862a7fa3-c04d-3d8b-8b34-53bb95ce6bc2 | -7.62007 | -45.31262 | 2026-08-04 05:04:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c71e18e5-b627-37c1-8407-745b5f0d4387 | -3.11038 | -47.917 | 2026-08-04 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 57d179ec-c4ec-3181-86bd-3688f5ea8f5a | -5.14702 | -46.20757 | 2026-08-04 05:04:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| aad19725-bd37-37fd-9cbd-d511efe75481 | -8.35534 | -45.98236 | 2026-08-04 05:04:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| efb637a2-4d8d-37a5-b35d-a84fe1c6aeb7 | -6.57067 | -55.16186 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 806b4f4e-30e3-3d48-9f66-ca5c3e6c6f29 | -6.57997 | -55.1675 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a0e8bb92-3aac-31fd-b0da-82bb8baa67f5 | -6.09908 | -55.81113 | 2026-08-04 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3087c584-4f55-3358-a04c-ea4620621ae6 | -6.56241 | -55.17129 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2f2f9f4e-f758-32db-866d-4044d5ed8521 | -8.93547 | -45.20243 | 2026-08-04 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e7f24058-9f51-3c35-8dbe-7e0b07914979 | -3.97074 | -48.12743 | 2026-08-04 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c4a3d6ca-59e8-3bd4-9d20-0e2a1009da5c | -6.56735 | -55.16135 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b88e7171-da4f-3e3f-b6ce-9228f1a177cb | -6.57121 | -55.15837 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f925fb2-73b2-302c-91d0-72b2df90d808 | -6.57561 | -55.15192 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1e329573-05e4-3b3f-afd6-2b61b4d21eb6 | -3.11248 | -47.91583 | 2026-08-04 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7b83ece8-3ea3-38b4-adc0-ecb5c978cd99 | -3.57912 | -50.25714 | 2026-08-04 05:04:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d094247-14ba-30ee-a00a-f6c00261f58c | -5.63711 | -47.10603 | 2026-08-04 05:04:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5eea3b40-c28f-3076-85f4-e89b355bd649 | -6.10623 | -55.80872 | 2026-08-04 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54993e82-a159-32f7-91ef-2e51a63f067d | -5.04646 | -43.2633 | 2026-08-04 05:04:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d78ba58c-d207-3f9d-9516-af3c62173264 | -1.63862 | -54.46678 | 2026-08-04 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1df97975-23f8-3898-8afc-56bd03128144 | -6.56511 | -55.15386 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efa3e094-5f4d-3a8e-9426-1cc4a29dca45 | -5.42454 | -47.38167 | 2026-08-04 05:04:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23d37c35-99d0-3a80-a95e-4beecdbdf89d | -3.94881 | -56.01035 | 2026-08-04 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aa8eeff0-6c9e-3e3a-af74-a8a7b457807c | -6.06884 | -44.87518 | 2026-08-04 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef493f03-9f92-3ad2-8ed4-6a6ffbc547e3 | -6.54636 | -55.16524 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ea838093-4b90-33e1-976f-26745e0613c6 | -6.5364 | -55.16369 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9af8fd6b-59ed-3200-9526-adaba7a87e4b | -6.56573 | -55.1718 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b76178f6-4abc-3e4b-b20b-0540be89749c | -6.56457 | -55.15735 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e08fd230-3458-33ed-8920-3a6c113156f6 | -8.92881 | -45.20609 | 2026-08-04 05:04:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d1fc57f1-7bdd-3754-9d57-b5657ef627b1 | -5.64225 | -47.10669 | 2026-08-04 05:04:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fe17c9f1-dcea-3969-8f40-a29fa750d96f | -1.63915 | -54.46334 | 2026-08-04 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 98cc28af-fd8a-3d84-822a-56fb83493411 | -3.67454 | -49.47643 | 2026-08-04 05:04:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5d9e10b0-ac03-3b65-b5ab-e11ece61556f | -6.54466 | -55.15426 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19530a88-b4a2-37e1-a96f-3d886b5afe37 | -8.56261 | -47.75107 | 2026-08-04 05:04:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| acda779d-d3d3-34fb-8041-8f9039cfdeae | -3.24519 | -47.92857 | 2026-08-04 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d72406ef-a2c0-3047-bee0-0e8467e7a4a2 | -6.53416 | -55.15619 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da12deb9-0b71-3f12-b6ab-21c80447ef2c | -6.57507 | -55.1554 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6358c1b2-1567-3f6b-bde3-7d30dd7a3ffc | -1.63692 | -54.45596 | 2026-08-04 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3ff6e05-2809-302a-9a6e-8c6114ee3012 | -4.46121 | -47.9171 | 2026-08-04 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e6561cbb-c681-35e0-abd4-4d8b4be090c3 | -5.40576 | -49.24187 | 2026-08-04 05:04:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e11dc62f-0b88-3bd9-876a-38fc3d58f29a | -2.73545 | -48.70159 | 2026-08-04 05:04:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c0b4290b-f0e2-3e66-9936-0593f9d845e3 | -6.57013 | -55.16534 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6d040355-a7fc-3378-ac93-e78325895d81 | -6.56959 | -55.16883 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c97b9ddd-f4e1-3173-891f-cbbb9b2484eb | -6.65352 | -56.182 | 2026-08-04 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1426cb11-798c-3f6d-890e-16d50786223c | -6.09962 | -55.80769 | 2026-08-04 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7198953a-4a24-3d5e-9597-a65c30454eb1 | -6.54297 | -55.29652 | 2026-08-04 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53994f56-7dc5-3ff0-887e-5fcede019fe4 | -6.57665 | -55.16697 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ac812c73-142d-3409-8e3a-b8cc6d938e47 | -6.55577 | -55.17026 | 2026-08-04 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5e996e47-16a2-3441-8f4b-c3c1d70a1d87 | -5.42855 | -43.42899 | 2026-08-04 05:04:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README13.md)
