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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 886d6891-2e0c-3b9b-a720-9c76141ea922 | -5.71565 | -44.83775 | 2025-10-07 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ca711c2c-0106-35e5-8248-a0c3075b299f | -8.55856 | -50.08235 | 2025-10-07 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9ae3061-403a-3c8d-a754-0d9634262295 | -9.67636 | -45.66925 | 2025-10-07 04:08:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10652256-51a0-38da-b4ce-f98a215dc2a8 | -10.09453 | -50.52183 | 2025-10-07 04:08:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f47d856-825a-3e19-9735-acd01e69ba29 | -10.33767 | -54.18899 | 2025-10-07 04:08:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 06c5b720-db2a-37f6-8d15-e381dad00dce | -5.31091 | -43.37185 | 2025-10-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 86cc86a3-05a9-3536-af9d-67acfd46d043 | -8.6216 | -54.96895 | 2025-10-07 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bde6d1a0-178f-35b1-8ccc-d6631025aa23 | -5.21994 | -43.67629 | 2025-10-07 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4da2d4b6-d922-330d-8d16-a406a17aafff | -7.6831 | -42.57733 | 2025-10-07 04:08:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ae687c5c-d01d-3859-9030-d9c51defd1fa | -10.18318 | -45.53181 | 2025-10-07 04:08:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e261efd2-1033-3978-bfb7-aeecd2821883 | -12.61547 | -44.75734 | 2025-10-07 04:08:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7462b383-a1b2-325d-98a9-926e370a4756 | -6.25731 | -43.27763 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 08c34ef2-54f5-31c6-95d3-b193529ad10f | -7.02692 | -42.29375 | 2025-10-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8013e0b3-0982-3381-bcc3-58b4501cf9fc | -8.61613 | -54.96141 | 2025-10-07 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a7c313ba-f836-3d0d-86d6-155a608449e2 | -5.92919 | -40.88944 | 2025-10-07 04:08:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 617635e9-e13a-3e9d-a266-d1bcd2c465e9 | -8.55755 | -50.08792 | 2025-10-07 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0a0bf154-62e9-3919-9956-2d31e77b6301 | -10.19111 | -45.52835 | 2025-10-07 04:08:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c26b655-d10f-39c4-88a8-332b9f98258e | -10.80249 | -48.59225 | 2025-10-07 04:08:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d18e7b11-72a6-3d7f-8e4d-0561ef498566 | -5.64186 | -45.96642 | 2025-10-07 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 70210763-aa13-39c4-929f-d2bc1bdc8e8f | -11.80872 | -45.13126 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 22095103-0a40-3d63-aaa9-ab34c451c3b8 | -10.17297 | -45.9802 | 2025-10-07 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b687b53d-4c01-377d-9e6c-01919419a3c1 | -8.66397 | -46.27919 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 99baaca3-9e7d-30a2-b353-0be94bfc79b4 | -6.52756 | -42.47879 | 2025-10-07 04:08:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 45dc48fb-b499-3049-a1e7-a86f9d6975e3 | -5.03518 | -45.56266 | 2025-10-07 04:08:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58b0e5e3-f506-3d15-9fbd-43f0d3991816 | -9.70011 | -45.9299 | 2025-10-07 04:08:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f9217611-f54c-3190-8eed-d33ad29003a9 | -6.07547 | -42.56113 | 2025-10-07 04:08:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| bfbd27d4-752d-3e58-bd8c-a7c43ba1c29a | -8.53034 | -46.23959 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| af62f882-92dd-3336-a9e1-819c76c34033 | -8.93907 | -49.86153 | 2025-10-07 04:08:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d06681aa-aa08-3f3b-b513-39b6c5f11e90 | -6.45916 | -44.58878 | 2025-10-07 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2b066df0-9867-3c58-890a-879acb6c8e22 | -8.49703 | -46.3218 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7fa999cd-ca83-350f-8039-f0b57609eb08 | -8.65654 | -46.29529 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4ca75b89-e8d6-3657-9c34-8471bc802190 | -11.02571 | -50.91737 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6efed6d-3ec7-3034-880d-51a2cf78139d | -5.2388 | -46.56789 | 2025-10-07 04:08:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8568e936-9e06-3dd4-803f-f77c0cd9da77 | -5.03807 | -44.45135 | 2025-10-07 04:08:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 541af397-cf6c-3fe5-8284-36c6cc906962 | -5.98306 | -43.51944 | 2025-10-07 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0abb366b-0ce5-3479-91da-6413a4cb71ac | -11.03618 | -50.91634 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d097847b-bdba-3fbf-b3e8-e1cff1ae9132 | -5.84908 | -44.30034 | 2025-10-07 04:08:00 | NOAA-21 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d6b0400e-593d-3eeb-a166-5897103d863a | -7.69301 | -42.40754 | 2025-10-07 04:08:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| bb3a241a-c3ff-3af4-b1f4-533a2a9f45e3 | -9.33789 | -54.52389 | 2025-10-07 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea793312-fd25-3ca8-b70e-39f103620f5b | -7.00669 | -42.78563 | 2025-10-07 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9c6423f4-9877-35bd-a0ef-43fd8c255e7d | -7.02118 | -42.75891 | 2025-10-07 04:08:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 64790298-fc4d-39f7-8650-f3760a830c63 | -4.9104 | -48.0186 | 2025-10-07 04:08:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9264b80c-5c9b-37f9-a63c-b0a3461a5f1c | -8.86627 | -46.78763 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| d0f31eaf-2751-389c-b904-216439a35b03 | -10.8888 | -47.1317 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 856b18c5-eece-3a51-a42c-5e421b6ddd53 | -8.18744 | -50.30529 | 2025-10-07 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 37d7a00b-6e7f-32d7-b86f-9c71b7dca1b7 | -6.64731 | -41.98126 | 2025-10-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 016fc742-a316-3f75-920c-cf3679d19847 | -8.52796 | -46.25394 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 63b53bd6-5e51-36bc-a800-3e4bdfd82e36 | -11.77666 | -45.13842 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c81e7b97-68db-3231-913a-ce9d4a846ecb | -12.01904 | -47.78119 | 2025-10-07 04:08:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7779c482-85e3-3823-95a3-faa144e486a5 | -6.71785 | -42.80478 | 2025-10-07 04:08:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5747035f-5dff-3f31-8cce-0bc4edfe6957 | -11.95269 | -45.48218 | 2025-10-07 04:08:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2ae68e85-c8eb-308c-ae57-51287337dcfb | -10.25877 | -44.37822 | 2025-10-07 04:08:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2327894-82df-3292-9ea4-9887f4fd374c | -8.60843 | -44.92577 | 2025-10-07 04:08:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b43b7bfa-a737-3e18-beaa-fd7f941fe98f | -10.37315 | -48.13629 | 2025-10-07 04:08:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4dd40b5f-699c-3d26-8b0a-7f957444f84b | -8.38187 | -41.85431 | 2025-10-07 04:08:00 | NOAA-21 | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| fbb90154-1641-3aff-b1df-0a101f2e6a1e | -6.98302 | -42.01004 | 2025-10-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 52d4d79a-6fe6-3be2-bd36-00a4335c9cee | -8.96229 | -50.79535 | 2025-10-07 04:08:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0aa18795-a0c1-3cde-bf4e-fec340c75b9e | -6.69828 | -42.86356 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6d26c4a3-fd08-372f-ba41-e2dc505d20da | -10.80679 | -48.59279 | 2025-10-07 04:08:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d7d4530-a329-3fc2-93d9-f2d0691f269a | -7.51982 | -49.91135 | 2025-10-07 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f3a17d97-a307-3caa-8a94-2bed3abd7d83 | -5.61385 | -43.93587 | 2025-10-07 04:08:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ff25f5e3-ec91-33df-ae7c-ab3cc3361256 | -5.4748 | -43.24892 | 2025-10-07 04:08:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 38c7f0f9-33c0-378c-859f-f8a1bba783f0 | -11.73105 | -45.37305 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c8335f4e-c564-3898-a6dc-b26001087b12 | -5.1482 | -49.84945 | 2025-10-07 04:08:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69c30972-2398-3df6-8f7a-a7047427f637 | -8.49624 | -46.32651 | 2025-10-07 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fe786207-80ee-35b7-83a3-4355cc22e21e | -7.51489 | -49.91049 | 2025-10-07 04:08:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5c62fb16-794a-3545-80ab-765b51870978 | -8.61763 | -54.97215 | 2025-10-07 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ca65a44d-d182-32a8-9c9f-ce5e1794d336 | -10.7982 | -48.59163 | 2025-10-07 04:08:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4bb8ebd0-22ab-3cea-89cd-b5f33d7972f8 | -5.95515 | -42.76352 | 2025-10-07 04:08:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f6cbb19d-85c7-37d4-9666-4b77caaf207d | -10.92292 | -47.0712 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0d1217d6-bf46-3213-bd7a-95d02fbcfb0c | -10.4524 | -50.41446 | 2025-10-07 04:08:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bd621a59-dfc9-30c2-ad9a-0fbd71ce153e | -7.77453 | -44.20113 | 2025-10-07 04:08:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 961c4341-811f-3a54-a3b5-31204246ae34 | -10.25536 | -44.37767 | 2025-10-07 04:08:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95a20ea0-3d49-3c31-98c7-1ab214320492 | -10.92894 | -44.25504 | 2025-10-07 04:08:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 913dfac8-4861-3670-9474-9134b7af8e39 | -6.24387 | -43.25309 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d21e0ec1-22ad-3f5f-8944-d5b2f9768726 | -7.5175 | -42.97659 | 2025-10-07 04:08:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| aaa50aee-140e-39cb-9c97-199488e47d2f | -5.55651 | -42.67504 | 2025-10-07 04:08:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d4b977bd-497d-3d66-b259-0f0394c149ed | -6.10753 | -43.09005 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7cd4d673-c4c9-376c-bda0-2db3075edacd | -7.25483 | -42.97805 | 2025-10-07 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a0d3c4da-cc5e-311d-904d-d8abcb1997b8 | -10.90164 | -47.10303 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 453c47a3-d08c-3e14-8a7b-f400fddacd2f | -12.24197 | -43.77416 | 2025-10-07 04:08:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4ac36a86-3b6a-393e-9692-d896bfbed571 | -11.71212 | -45.35718 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e738fbb-446e-35a8-97f2-39bc23e549a1 | -7.4644 | -43.03017 | 2025-10-07 04:08:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| cedb07f4-f752-3e26-9d4f-6a9e19267d58 | -6.65278 | -41.96798 | 2025-10-07 04:08:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 72314f92-b331-366a-98fa-f0924972af9a | -5.74813 | -44.98389 | 2025-10-07 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 435823e1-7f3d-361a-be35-7590e62ed8b6 | -11.86602 | -44.93507 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d01ac71d-0ef7-31a0-b0f6-4382bfeb649f | -6.23754 | -43.27082 | 2025-10-07 04:08:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e279bb0d-94c7-3558-b2ed-caa29ebd68d4 | -10.87609 | -51.02545 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 290665a0-407b-3150-84fb-b4aeb06802b0 | -6.52324 | -43.5694 | 2025-10-07 04:08:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ffc2459-34c2-3886-af33-50c7100a09ee | -5.61953 | -43.22214 | 2025-10-07 04:08:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4b832301-ebee-3ee0-96ad-c093358351a2 | -4.69309 | -48.62291 | 2025-10-07 04:08:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e1048c6-9054-3a58-bc69-043910631168 | -7.67229 | -50.21319 | 2025-10-07 04:08:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3d62b1e-0e80-3547-b989-d02642cea3a1 | -11.78204 | -45.12723 | 2025-10-07 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b13aeeb-c7e0-3c9a-92ab-17ffb216073f | -10.89657 | -47.13301 | 2025-10-07 04:08:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2317d70c-9dcc-3f07-a0b4-64aae73d6829 | -11.0406 | -50.92014 | 2025-10-07 04:08:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 9a579cb4-b0d5-3493-8c23-568b6baf4de9 | -5.76536 | -45.75348 | 2025-10-07 04:08:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2e94a03c-b4ad-37b9-b660-15536a940580 | -8.17796 | -50.30059 | 2025-10-07 04:08:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c54dc188-9cf3-3d23-bfff-19c7ef716e5e | -6.0704 | -43.47903 | 2025-10-07 04:08:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d5de8c28-7593-3821-93e8-7aa9b9e0be04 | -10.80606 | -48.59691 | 2025-10-07 04:08:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ca0079c-3e8e-3d1d-9968-98b6a0dc986c | -7.69966 | -42.55852 | 2025-10-07 04:08:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |


[Clique aqui para ver as próximas entradas](README31.md)
