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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15eca2cf-e6bf-369f-b786-c6c367164207 | -2.32073 | -48.5803 | 2025-10-31 04:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| b3e1b006-aa74-32bc-ac5f-398d492bbade | -4.79647 | -46.46142 | 2025-10-31 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d3a0a54-2402-36bf-9820-5356cde07b49 | -3.88195 | -51.19102 | 2025-10-31 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fc6ad6cf-4d83-3b42-9f11-8f66bb30c84a | -3.54511 | -52.45731 | 2025-10-31 04:55:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eec44baf-b595-356d-bc18-1ba05ecb7deb | -5.60634 | -47.12615 | 2025-10-31 04:55:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 162f2024-f14f-3073-a742-c49fca9f2b0c | -3.301 | -51.92823 | 2025-10-31 04:55:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44d60020-984b-3673-96ad-9a3f83e325fe | -5.71707 | -44.53408 | 2025-10-31 04:55:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52cf6541-c458-3059-a1cd-142f976a87e6 | -3.60166 | -50.62555 | 2025-10-31 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1d807d83-939b-3bfe-a1a1-85108fbef27b | -4.81996 | -47.08615 | 2025-10-31 04:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b5513d7-a594-3bc1-83fc-969748710245 | -5.21873 | -43.75496 | 2025-10-31 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be6b5e71-885c-3ea0-ba94-68af30e5a1fd | -3.2982 | -51.92416 | 2025-10-31 04:55:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8ce757b2-6060-3fdc-9c45-63fc49784fd3 | -5.88403 | -43.19563 | 2025-10-31 04:55:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ebb3a148-5f6c-3dd2-87be-b807ddebdd27 | -4.48156 | -46.56791 | 2025-10-31 04:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 6bb4b9ef-a672-396a-bc73-caa3ed5322a7 | -2.44953 | -49.01553 | 2025-10-31 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9f80fb56-83f4-3a80-b120-92a0c7b34422 | -2.91729 | -48.72259 | 2025-10-31 04:55:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85108d2f-ef82-38b6-b83a-872a2dfcbf81 | -4.95846 | -45.87844 | 2025-10-31 04:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c7fab47f-acd5-32e3-8252-b1b1f2679143 | -4.75678 | -45.78491 | 2025-10-31 04:55:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82f4d681-75ea-3db2-8043-62d18c596c34 | 1.29443 | -60.41766 | 2025-10-31 04:55:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2ae92cc1-dfb3-3512-80b1-ae264d972372 | -3.30211 | -51.9211 | 2025-10-31 04:55:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc9253a0-0632-3bc0-9366-e30f9943fb8a | -4.69225 | -56.06388 | 2025-10-31 04:55:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 504ac489-b0d5-30f7-bc18-a306dbe0f0bc | -4.55637 | -48.47811 | 2025-10-31 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 11d7e8be-5ab0-38ec-afe4-3d7659d74bea | -4.47175 | -43.43969 | 2025-10-31 04:55:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 005b5f31-1da3-36ec-bdfe-20be07bee996 | -6.5545 | -44.01889 | 2025-10-31 04:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8bc4c5fc-6c78-3b46-a8ca-192df630bd6c | -5.20767 | -46.14872 | 2025-10-31 04:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a32d49a6-e0a8-3ebc-b7ce-587b4422d1b6 | -4.08524 | -48.91621 | 2025-10-31 04:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8e47979-64cb-3ed3-a7fe-8750dd2b5194 | -5.95768 | -45.55603 | 2025-10-31 04:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed6f8e5e-2830-31b9-b176-4cf3fcfcefb3 | -2.31562 | -48.583 | 2025-10-31 04:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| d58c5a49-8a3e-3dfa-a415-d9d31765f578 | -2.31609 | -48.5846 | 2025-10-31 04:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6ba81ded-6f94-3849-ab98-486d213ce14e | -4.56854 | -45.68221 | 2025-10-31 04:55:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| da929a75-8095-3a5c-ab73-e12bfdf996f4 | 3.22009 | -61.19796 | 2025-10-31 04:55:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a6d4e36-f4a1-3fa7-93f7-bc7d90b1798f | -4.30749 | -49.82965 | 2025-10-31 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b51df353-fddf-3a84-9d11-70e4b1665392 | -5.48285 | -48.48891 | 2025-10-31 04:55:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92359cd0-e5b2-36a9-b052-da6c7c78efcd | -5.78957 | -40.80896 | 2025-10-31 04:55:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 780527de-2ad5-3765-8a1b-8fae72ab3b9a | -1.96276 | -52.04409 | 2025-10-31 04:55:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e1ab28d1-2d9b-339b-8a1f-e6ff7ea3b204 | -4.66369 | -55.95396 | 2025-10-31 04:55:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fca1846-baad-3888-b764-64c51a482bd3 | -2.421 | -49.2973 | 2025-10-31 04:55:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| fbe3a213-58a0-31cd-b9bd-7a1b6c3259b1 | -4.6753 | -46.52173 | 2025-10-31 04:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 815e93e2-4514-3569-b4a9-3cf9b963c4e7 | -1.17028 | -49.26216 | 2025-10-31 04:55:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f476620-55ec-3c6f-a9bf-ad9df29a44cb | -6.53047 | -43.7101 | 2025-10-31 04:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b3f66f95-dbdf-3c35-892f-1cfd68123477 | -5.17519 | -45.33197 | 2025-10-31 04:55:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a4db4b5-1dc4-374a-8d91-31398c7f44ba | -3.66788 | -51.71458 | 2025-10-31 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 944c3660-3cb4-3b3d-9712-c1e2e1c11091 | -6.10751 | -41.72626 | 2025-10-31 04:55:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 82b4bbc6-51ee-3ce9-8c13-ead656ae9c8e | -5.48339 | -48.48516 | 2025-10-31 04:55:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 003abac4-6208-3044-8050-af666f88c494 | -4.84155 | -45.80379 | 2025-10-31 04:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab44c784-706e-3222-8ac7-6845923d4e14 | -3.19927 | -52.8653 | 2025-10-31 04:55:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eda1c240-2951-34dd-be06-47485c868c1f | -3.29764 | -51.92772 | 2025-10-31 04:55:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc24de9e-1c75-388d-a8a0-93bfd26f923c | -3.01866 | -49.44918 | 2025-10-31 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 996e3971-1305-3da6-83fd-8126d2028dcd | -4.81147 | -43.01767 | 2025-10-31 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 06230fe1-4aaf-3aef-ac33-27038241b6c3 | -3.87409 | -52.11114 | 2025-10-31 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e0f5196-c9b2-3932-add6-aeae77947c49 | -4.82061 | -47.08154 | 2025-10-31 04:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eadb8e01-2ae7-335f-a686-e2fe895f2a5b | -1.2131 | -54.07196 | 2025-10-31 04:55:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ce3d306-0e80-3385-9688-b427ec897b57 | -5.50249 | -46.38081 | 2025-10-31 04:55:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e426e34d-fb9d-3adf-95c9-89e3e9795766 | -4.41314 | -48.95168 | 2025-10-31 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e007b8c1-083b-387f-94c0-ca17ee4d504a | -4.7029 | -46.49483 | 2025-10-31 04:55:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e000ff24-cfa0-3d8a-a14e-4f3cc14ab32e | -2.32029 | -48.57868 | 2025-10-31 04:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 9cc8dc6e-ef5a-3808-8b16-f5f6335be0f2 | 1.01347 | -51.29465 | 2025-10-31 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 48fd5bec-2a81-3527-937d-abb5fbc1766e | -6.6651 | -44.691 | 2025-10-31 04:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ea45fb0-a1c3-35d2-b1c4-f25ac091e516 | -2.09678 | -54.40223 | 2025-10-31 04:55:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d8f62559-4680-3ac6-89d1-f854a80a8235 | -2.90804 | -45.40915 | 2025-10-31 04:55:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 71f75a60-68d1-30af-a9f7-2222204f6a3d | -7.04861 | -41.47102 | 2025-10-31 04:55:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| b7658c86-a5de-38c2-9396-59185583227e | -5.79016 | -40.8133 | 2025-10-31 04:55:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7dbf754c-5026-3152-81d2-2e964c56dc85 | -5.47212 | -44.31976 | 2025-10-31 04:55:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b4260dfc-654b-3f28-bfce-cbd836b8a4be | -4.79576 | -46.4664 | 2025-10-31 04:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| acdd30d5-6a31-3a96-9889-d31a1eda4304 | -4.39206 | -50.43387 | 2025-10-31 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c8e94e8-d4a0-313d-8097-ad0fd1845fd5 | -4.26222 | -48.60014 | 2025-10-31 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 835b4f13-912d-370e-a051-8f606ce7fe07 | -5.01898 | -45.56845 | 2025-10-31 04:55:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05c666e8-361d-326d-98e2-05a54a9d28ad | -1.95343 | -47.85818 | 2025-10-31 04:55:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c7a2d859-b8bd-3964-9e41-e163911aeb29 | -5.96273 | -45.55686 | 2025-10-31 04:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40ef0a6c-efcd-3b96-aa0c-0b2f6c5ce5b9 | -3.5302 | -47.55079 | 2025-10-31 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 7c266d6b-fc94-3b7f-acdd-1396f8c6f757 | -3.44104 | -54.63803 | 2025-10-31 04:55:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9967eabc-d5f1-3884-892f-dd71a13f9b23 | -5.0645 | -45.11348 | 2025-10-31 04:55:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 842c8cf7-ece1-3251-a4d6-5eb1ba4fa64b | -1.64813 | -55.15027 | 2025-10-31 04:55:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99be65fc-ecb4-3559-9af8-7259f4d58913 | -5.6177 | -45.97673 | 2025-10-31 04:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 92d380d5-1b35-3d70-83c0-044cc38c3697 | -2.91355 | -53.94971 | 2025-10-31 04:55:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b831afcb-3cf0-3f89-bab6-17d46bcc74e6 | -3.66731 | -51.71821 | 2025-10-31 04:55:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0c69f5ad-43c5-3a12-8b4c-18e5e814a709 | -4.63759 | -49.48685 | 2025-10-31 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6f165510-e9ba-3e30-b0b9-761ddfbd94ae | -5.61941 | -45.98218 | 2025-10-31 04:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2876392-96cf-3442-b25f-95b0d4c86355 | -4.05278 | -47.49961 | 2025-10-31 04:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 581a4e1c-1a95-3fe0-b145-b33379ce9321 | 0.79207 | -51.96826 | 2025-10-31 04:55:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7911795b-6760-3c10-9197-6289ad956d70 | -5.27736 | -45.12775 | 2025-10-31 04:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 432c3c5e-d5ad-35af-9e49-2e863efbd7fb | -4.68385 | -50.44025 | 2025-10-31 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 626ee748-93d8-3b5b-82b8-111997cdc1bb | -6.62009 | -43.34494 | 2025-10-31 04:55:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d6628b55-73e3-3917-8008-95f3ceef761d | -3.77441 | -48.92419 | 2025-10-31 04:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34970228-f028-3c43-9856-b15ec3bd0b30 | -5.34033 | -45.3638 | 2025-10-31 04:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0206d26-1a4c-37e5-ae48-3ad0b9bfe264 | -1.75313 | -52.10067 | 2025-10-31 04:55:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e861b595-505e-397b-b061-a47956751158 | -5.17011 | -45.3312 | 2025-10-31 04:55:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8f7b04e9-3fa0-3f1c-a6da-acdd2333fdc6 | -5.93666 | -49.76372 | 2025-10-31 04:55:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ba92188-3f81-3c3d-a576-5c3bd520cbea | -4.90789 | -45.728 | 2025-10-31 04:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67751cbb-66d1-3939-9b3a-2363b1cad05c | -5.54571 | -48.37605 | 2025-10-31 04:55:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b8d926f-bf95-3357-8285-c7026ef08b22 | -4.492 | -55.79911 | 2025-10-31 04:55:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 228f7534-6ff9-327a-946a-5ff8397a588d | -2.34608 | -47.16197 | 2025-10-31 04:55:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 509c559f-4d9d-3b0d-9559-e7c5670e201b | -5.93589 | -49.7687 | 2025-10-31 04:55:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e62a1ea3-d803-3291-88a8-60b9daeb803f | -4.6643 | -55.95015 | 2025-10-31 04:55:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de07a5c4-7118-31c2-9748-072a0e3c951b | -4.87396 | -47.52535 | 2025-10-31 04:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a45007fc-0984-3646-9c0e-2dbcbe30a581 | -3.48281 | -46.02039 | 2025-10-31 04:55:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53ea85ed-83ec-335d-afdb-19100660a835 | -1.36513 | -49.02643 | 2025-10-31 04:55:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5ddabdc-a0da-3ca8-8190-de461a935be9 | -6.20223 | -42.52223 | 2025-10-31 04:55:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 2b2caefe-7531-3f16-9d73-378cc05458ea | -3.87791 | -51.1943 | 2025-10-31 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f93a7151-6947-3c60-bc76-bddb980891bb | -3.54453 | -46.43276 | 2025-10-31 04:55:00 | NOAA-21 | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c9fc59a-56b9-312a-bcb4-0c0b6a17c207 | -4.01061 | -50.4849 | 2025-10-31 04:55:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README32.md)
