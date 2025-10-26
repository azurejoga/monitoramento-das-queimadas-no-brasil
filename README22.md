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
| ba166f8d-0d1d-35a0-919b-3051efb9d49d | -6.47523 | -47.55122 | 2025-10-26 04:00:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7df57a73-c067-39d8-8189-69bae986bf4e | -6.13045 | -41.72673 | 2025-10-26 04:00:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 236c4e44-7bac-337c-8ab0-d309259964da | -8.41458 | -41.1654 | 2025-10-26 04:00:00 | NOAA-20 | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b242fb17-1fc5-3bc3-8868-0fe6e1ddee70 | -6.01915 | -43.30503 | 2025-10-26 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fcc75efa-c23e-3adb-a30e-6d44e964a709 | -6.15612 | -43.1346 | 2025-10-26 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e004e0e8-1d47-37e3-bf4a-1e4c2b350f14 | -6.36068 | -38.3702 | 2025-10-26 04:00:00 | NOAA-20 | LUÍS GOMES | RIO GRANDE DO NORTE | Brasil | 2407005 | 24 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a90f0561-808c-3c39-96d1-dc7494556f3c | -2.91737 | -52.72462 | 2025-10-26 04:00:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7aa9524-e07f-31dd-a70f-b06b1903bc65 | -7.15663 | -44.49478 | 2025-10-26 04:00:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6e9d5d13-9f09-3c07-bfec-dd7ceb16f3ca | -5.05488 | -43.69688 | 2025-10-26 04:00:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f282cb0b-feb6-34d1-8ecf-74bf7bcb49e1 | -6.39 | -45.77854 | 2025-10-26 04:00:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5a01d075-71c5-3472-b8ae-d316742f0077 | -6.31145 | -42.80677 | 2025-10-26 04:00:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 70ae5f78-24b9-3dfd-abc8-83c93fb0541f | -6.15375 | -43.10365 | 2025-10-26 04:00:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9796988-9626-3816-b28c-ccf2ed79b9a4 | -6.12882 | -41.71494 | 2025-10-26 04:00:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bd444343-9a8a-34ab-b5ec-777f7e8ff1ad | -5.83225 | -42.93529 | 2025-10-26 04:00:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2465bcf2-4490-3fea-8cfd-1aa1ebc272c5 | -7.84171 | -46.43396 | 2025-10-26 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 1f262f70-1d74-31ee-89d8-517a1c26afc4 | -4.16032 | -47.6643 | 2025-10-26 04:00:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 09fcf40f-ae1a-39d8-b37a-06104a275d42 | -8.33058 | -48.18898 | 2025-10-26 04:00:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 106e77de-368e-37a2-8c25-ad04beb12d4b | -6.12361 | -41.72555 | 2025-10-26 04:00:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 70700ec9-c256-3c9e-a09b-26bbfeef15e5 | -4.3197 | -41.79602 | 2025-10-26 04:00:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a0422dee-149f-3eaa-ad2f-521d529079cf | -6.59967 | -42.05924 | 2025-10-26 04:00:00 | NOAA-20 | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fea881c1-22d8-3e7e-9ffe-1c9647c13467 | -8.53402 | -47.20727 | 2025-10-26 04:00:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e90e15dc-8d4a-3c3a-9f1d-90bfcf3ee500 | -6.5531 | -43.78207 | 2025-10-26 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 53b7f244-bb88-3d0d-aded-6061e6c4bca5 | -6.7114 | -44.6329 | 2025-10-26 04:00:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7b2ca6ed-7528-3b0b-9e3d-ad83dff62409 | -5.85838 | -39.26303 | 2025-10-26 04:00:00 | NOAA-20 | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cb9748e9-249b-3597-ace6-f5c59abbf4cd | -4.93073 | -48.56201 | 2025-10-26 04:00:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8492331b-21cd-3bb1-ad2f-6499eb5e1acc | -6.70707 | -42.04496 | 2025-10-26 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| afaf14f9-6a52-36b7-880e-2f63cf1a33aa | -3.93193 | -41.02185 | 2025-10-26 04:00:00 | NOAA-20 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6ab30a81-3996-36e9-b1d7-91ba8fad9c2d | -5.89306 | -41.28621 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c9300740-1c3c-3094-89bd-d605b22ca824 | -4.70997 | -46.43949 | 2025-10-26 04:00:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ce7dd202-d9bb-3cce-abe0-b9aa0fb98836 | -7.69755 | -42.1862 | 2025-10-26 04:00:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| facdc394-9731-3947-8138-fca33f36979e | -6.432 | -42.02862 | 2025-10-26 04:00:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 553a1470-853f-3232-aaa8-402cf6e10098 | -5.5484 | -41.39984 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7fe1d02c-d0e5-3ba8-a9e3-23e729e3b6c7 | -6.529 | -37.98158 | 2025-10-26 04:00:00 | NOAA-20 | BOM SUCESSO | PARAÍBA | Brasil | 2502300 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 385101cb-c779-3ee8-80a5-7e745eb35843 | -4.02464 | -46.00473 | 2025-10-26 04:00:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 361b391b-8f21-32b5-841b-bf5cf126ecdd | -7.00902 | -49.5223 | 2025-10-26 04:00:00 | NOAA-20 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f607def2-2c61-38b0-9f2b-7a5d20b43d7b | -4.79994 | -47.8853 | 2025-10-26 04:00:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 789f1371-8d08-3fb7-822e-c66e9d51f044 | -4.02381 | -46.07228 | 2025-10-26 04:00:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a7b5f0d2-b4c8-3b0b-a700-4b102d0c9f6a | -4.90441 | -43.2334 | 2025-10-26 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 915ea029-29d8-3267-a785-66180829657e | -4.27329 | -40.6876 | 2025-10-26 04:00:00 | NOAA-20 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 84a8c8a8-81cc-397d-86db-127bd9f4f037 | -6.10973 | -41.74646 | 2025-10-26 04:00:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 330e570c-a865-3f9e-9fe1-ffa27212a67e | -5.00843 | -37.84153 | 2025-10-26 04:00:00 | NOAA-20 | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7e995b69-455e-32c2-b2dd-7c6534afaaf5 | -5.4089 | -45.29251 | 2025-10-26 04:00:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0baec4d-6564-304f-85fd-9dc4928bcdd1 | -5.8963 | -41.30909 | 2025-10-26 04:00:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a7cde0f7-6c42-30b5-8692-3c8078786360 | -3.76807 | -47.57701 | 2025-10-26 04:00:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4c601a8-a455-3294-b7f9-03f9d11f9b4c | -6.90486 | -46.14957 | 2025-10-26 04:00:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d23748ab-ec9e-361d-a753-cf782acdfc92 | -5.39302 | -47.61113 | 2025-10-26 04:00:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| df9e7a1d-4290-3990-b249-e3eff2079840 | -6.42903 | -44.13186 | 2025-10-26 04:00:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 45db68e4-9a26-3d50-aab4-b8527aad0879 | -3.11575 | -49.10816 | 2025-10-26 04:00:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b89bd695-ec87-30a5-a33a-79eb84b530ce | -6.07923 | -42.14709 | 2025-10-26 04:00:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 111df493-5803-3a36-bf33-080d6cdb372c | -5.41163 | -46.01072 | 2025-10-26 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fd82a4e9-dfe0-36cf-845f-fa15e6c3ebe0 | -7.47445 | -47.3744 | 2025-10-26 04:00:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2101a4af-a8db-3eee-aa0b-8d1d210fab44 | -3.73587 | -42.29764 | 2025-10-26 04:00:00 | NOAA-20 | MORRO DO CHAPÉU DO PIAUÍ | PIAUÍ | Brasil | 2206670 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f210b9c7-6ce3-36fd-aefe-ce90ec5a5bd9 | -7.80358 | -45.39367 | 2025-10-26 04:00:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e14cab2-5d14-34c3-8250-4f7bfd53730d | -15.45507 | -50.483 | 2025-10-26 04:02:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 629baefc-1619-30c4-9efc-1bbbf3d9626d | -10.21076 | -52.66286 | 2025-10-26 04:02:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 105bca27-2d46-3b0a-9fe9-ec6c498f0183 | -13.9166 | -48.38136 | 2025-10-26 04:02:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3643ab26-e229-3f83-89e1-136141e6bf1d | -9.4431 | -46.3004 | 2025-10-26 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfe42ee2-9e42-3238-81dc-7d795703cdac | -14.83709 | -52.44469 | 2025-10-26 04:02:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fa1b3492-a3f8-35e0-bd39-30de917fcfc6 | -14.16752 | -47.31607 | 2025-10-26 04:02:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf5e5bb4-f6dc-3ee1-96c0-7ea49280a67b | -10.45287 | -44.99797 | 2025-10-26 04:02:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a638aecb-b697-3508-b628-185c4a15a2bf | -14.16895 | -47.30819 | 2025-10-26 04:02:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e29c4cae-4701-34ee-9755-59fcf668149c | -13.87896 | -48.44853 | 2025-10-26 04:02:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9aecffa-5578-3f07-9596-8039dc7e50f8 | -13.89432 | -48.44094 | 2025-10-26 04:02:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f86c665-c9af-3b3b-8b81-cdea01d7a1f9 | -15.21995 | -47.93867 | 2025-10-26 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9a51ee39-ea25-3e46-a0cc-e6daae1031a7 | -10.60174 | -47.85813 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f89ecae8-8708-3070-9211-15a99806a3fb | -11.95717 | -47.64029 | 2025-10-26 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f9b741d-f808-3c99-9e9b-74f44b043aae | -13.53557 | -47.55733 | 2025-10-26 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4fdcc2a1-476d-33b0-82fc-e0c1374e238f | -14.4389 | -49.96202 | 2025-10-26 04:02:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f77a8169-80d2-30d5-83e0-ff1540423ba1 | -10.61453 | -46.60877 | 2025-10-26 04:02:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fb99e354-6910-362e-b90c-7d22d434db58 | -9.19979 | -46.34985 | 2025-10-26 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e41c1091-f360-3dae-b56a-1d9eb24986d2 | -13.30298 | -47.09318 | 2025-10-26 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e9c51d8-0e2a-3c71-841b-970fcc2308f8 | -13.89242 | -48.41075 | 2025-10-26 04:02:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3e46ff9-37d9-3163-860e-32f4e4675ba9 | -12.13221 | -43.48041 | 2025-10-26 04:02:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08b3b9a8-e0bb-36d9-b178-77bbf1a57af2 | -15.21887 | -47.92091 | 2025-10-26 04:02:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a784efc0-7756-3185-a244-bb1f68ae105d | -15.27178 | -43.17759 | 2025-10-26 04:02:00 | NOAA-20 | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 0561d163-31a0-3b2a-ab37-52adaae1c9a3 | -12.29585 | -47.49259 | 2025-10-26 04:02:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8a0e3158-9932-3ecc-89a8-6b28e37cead8 | -15.18746 | -47.23226 | 2025-10-26 04:02:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 709a0a51-a2c8-3703-b187-60128ebbead5 | -10.83264 | -47.62473 | 2025-10-26 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f1cdf1c-c4d6-3e06-af26-8944390c0b16 | -13.89514 | -48.43649 | 2025-10-26 04:02:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| acc84e05-bd4a-3e50-8e99-19d689bffce1 | -12.99963 | -43.80988 | 2025-10-26 04:02:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 61fcbce4-757e-33fe-bcb3-7ce8d318aa00 | -15.23884 | -46.0629 | 2025-10-26 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a03c839f-192b-3c9d-ae24-8d74a67d5d11 | -15.14173 | -49.59485 | 2025-10-26 04:02:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d86f7736-f12a-3566-b284-1e0d75cbd480 | -11.21421 | -54.84911 | 2025-10-26 04:02:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23b144d9-4322-33d9-9ca8-6bbb1c1aed31 | -13.09023 | -43.05328 | 2025-10-26 04:02:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7ac9ec74-f724-38d5-9943-9ce41417a0fb | -13.32531 | -47.93449 | 2025-10-26 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2d3eaa08-7df0-3061-b63e-c944116917f1 | -15.33544 | -42.80955 | 2025-10-26 04:02:00 | NOAA-20 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 19e9d175-df51-3f28-a7db-77f7a92ba76a | -11.65329 | -43.3138 | 2025-10-26 04:02:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0b0307e-a7f1-30c4-b8a1-e7f523166e62 | -15.12443 | -43.29749 | 2025-10-26 04:02:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ca889833-a617-320e-90a1-f702cf9fe2c7 | -14.77144 | -44.97784 | 2025-10-26 04:02:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88d72c45-a00d-330c-b21e-b889d48995ea | -13.0574 | -50.29128 | 2025-10-26 04:02:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3da3732-6c79-3da5-bd28-78f1d8047569 | -13.88246 | -48.48024 | 2025-10-26 04:02:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1867728e-ba98-3bed-8232-2597686099d6 | -9.84069 | -49.6356 | 2025-10-26 04:02:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1969070-b7e4-3714-86c8-e66f39beafd0 | -9.43618 | -46.34007 | 2025-10-26 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 48d808ce-682e-3859-8e5f-d3ab67244306 | -10.80163 | -47.8744 | 2025-10-26 04:02:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 580c8cbd-6ec1-3ede-94e8-9a7f62c8e07a | -10.85158 | -47.75325 | 2025-10-26 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2401554d-7e79-3a31-b00f-d0c5d9933a8e | -9.43888 | -46.29972 | 2025-10-26 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ea43463-8215-3b57-90d9-48436a378435 | -13.05803 | -50.28801 | 2025-10-26 04:02:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2b27373-b686-3b9e-b35a-7b3e36ba8556 | -15.83201 | -49.07919 | 2025-10-26 04:02:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 984714a6-40aa-35e2-a247-356bbb4986a7 | -16.22313 | -45.6602 | 2025-10-26 04:02:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 284d2096-54f5-3e87-8022-22939ffee3dd | -13.00624 | -43.85592 | 2025-10-26 04:02:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README23.md)
