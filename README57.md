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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec78d299-4dbd-33a4-a586-08c2443b0afd | -7.36684 | -43.32457 | 2025-11-16 04:57:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9d0495f6-c0ce-3721-8c13-6d43d8581b45 | -9.64809 | -46.02814 | 2025-11-16 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a2d1225-b146-3809-b4f9-3cb961fa0404 | -10.66412 | -49.36889 | 2025-11-16 04:57:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 073fc775-dc97-37b8-b2c5-50ed665312f9 | -12.00914 | -49.27973 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.4 |
| b664e579-06f9-345b-a7a8-45c5995f7018 | -7.71427 | -47.29586 | 2025-11-16 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 64c28e94-2648-3945-8dbb-c2f6eecb85ba | -8.55861 | -47.7903 | 2025-11-16 04:57:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d670c041-f299-3945-a60b-26f1f2969462 | -6.50978 | -47.62935 | 2025-11-16 04:57:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ccf9d30-6932-3859-a4e4-57cc0b66fad4 | -8.20789 | -43.56197 | 2025-11-16 04:57:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd63b5b4-2d4c-30b9-9397-32cb25e71ce7 | -9.44335 | -59.20553 | 2025-11-16 04:57:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8cbec706-ffb8-344b-95bd-ddbcfabac796 | -7.57775 | -46.30326 | 2025-11-16 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04f3459c-c7fa-365e-9f6e-5d4ebf9d6fef | -9.5111 | -47.27042 | 2025-11-16 04:57:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9c9dc6fd-d98d-3a6e-a4a8-a9bf9f127376 | -7.04128 | -45.92927 | 2025-11-16 04:57:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a1c657f-47cd-337b-a85c-cd69eac2b0f0 | -12.03549 | -47.67645 | 2025-11-16 04:57:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4c321729-0a3b-3b2f-bcfa-be300b6a1db4 | -10.00689 | -44.77257 | 2025-11-16 04:57:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cccec97b-6af5-32fb-9a2d-28c0713108fb | -11.84675 | -56.89608 | 2025-11-16 04:57:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cde0df0c-fb9f-3c22-aca3-21321eeed1cd | -11.41114 | -43.32891 | 2025-11-16 04:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0faab251-1141-394b-b13c-4fc2600ed689 | -10.84767 | -44.09491 | 2025-11-16 04:57:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 83d799b7-b3f5-301c-8244-f1d7e941f3f1 | -9.72289 | -48.8973 | 2025-11-16 04:57:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f5134ef5-0dcd-31c6-826a-883145e944c1 | -7.05623 | -43.95078 | 2025-11-16 04:57:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 173b8955-3ffe-3888-bb95-8ef813044cfb | -7.04712 | -45.92409 | 2025-11-16 04:57:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e72010e5-35cf-3262-9ae7-50adb47f66c9 | -10.86221 | -44.88958 | 2025-11-16 04:57:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46ac948a-9053-3636-ac79-0d0cdc41c457 | -6.71741 | -42.94449 | 2025-11-16 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 53837af3-536f-31a5-aeb0-8bf741c1999a | -7.09539 | -42.73682 | 2025-11-16 04:57:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 0ff442ce-8ff3-3b99-920d-7082b888b939 | -6.7837 | -44.29463 | 2025-11-16 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3498d607-a491-311a-810d-0ac5eff8b57a | -7.71958 | -47.29156 | 2025-11-16 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 97a88ac1-9c8e-3300-9dc6-af694a817dfc | -11.91245 | -46.22705 | 2025-11-16 04:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef910c76-d85c-3569-8d34-c27677b693bc | -12.06062 | -46.97158 | 2025-11-16 04:57:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9cbff23d-b7ff-37c1-977d-c0dac9286eec | -12.87825 | -46.44834 | 2025-11-16 04:57:00 | NOAA-21 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d983c2dd-f0de-39fc-bb6d-5d365f4570ca | -9.69191 | -48.93857 | 2025-11-16 04:57:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1db916fe-4c7e-312a-8516-2c6831e74060 | -7.26759 | -48.02446 | 2025-11-16 04:57:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 88e59a05-286b-3897-b45d-6f7243655103 | -10.70657 | -44.52235 | 2025-11-16 04:57:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 658f594c-ccf8-3839-be90-d1366d8a121f | -9.74811 | -43.9503 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4f14756a-9019-381b-bc64-8a0133234733 | -10.00021 | -44.77982 | 2025-11-16 04:57:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c1fdbac-9666-32f8-a0c3-10e1b655873d | -12.80926 | -46.44548 | 2025-11-16 04:57:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3a0e4055-45f5-374d-9b59-c3fad55beb66 | -12.68312 | -47.17202 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 15bf51cf-65df-3693-a29a-68fe959eabd6 | -7.01655 | -45.16758 | 2025-11-16 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 78bfbb1c-2aaf-3862-9246-707f9c1de20f | -9.72179 | -48.90549 | 2025-11-16 04:57:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e5ce609-264e-3374-b06c-36239893a78b | -12.65473 | -46.74652 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5160babe-d231-3ebc-811d-87fcc7214dcf | -9.83754 | -47.06163 | 2025-11-16 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9564f910-9880-3ea4-8327-12df34807382 | -10.6261 | -44.59838 | 2025-11-16 04:57:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 373203e8-37c7-3ac8-af21-29b0691a46d6 | -12.80885 | -46.44876 | 2025-11-16 04:57:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 41ef3f3a-b33d-39e8-bfb4-8e88460ec1e4 | -6.77807 | -44.29404 | 2025-11-16 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7870eaea-309e-3256-8012-8f88e5ed2d2b | -11.16291 | -49.44694 | 2025-11-16 04:57:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2e325720-46b8-3b81-83db-1c681e0dd2e1 | -9.08092 | -51.16098 | 2025-11-16 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27ebc413-e835-3ceb-8bfa-d44e43875b26 | -12.65841 | -47.16557 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c6aea39e-e366-334b-9825-ba1ec3a00bef | -6.49609 | -52.82873 | 2025-11-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cc45879-924a-320f-89ba-374a7e4de351 | -11.96659 | -44.94769 | 2025-11-16 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bbedc9f9-2e2d-3f81-b755-4ef75d4b4ce6 | -5.26971 | -49.31708 | 2025-11-16 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e31215ab-2978-335b-bac0-493b07f5a44a | -12.20584 | -49.61001 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9d25f92a-41c7-3b28-a59e-b01007fe804b | -12.4008 | -47.55938 | 2025-11-16 04:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f85fbda4-757b-321e-8f65-c4331d566979 | -12.66342 | -47.16629 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a7c19ba-e008-3864-8ba2-43fc04ffd167 | -9.65969 | -43.90263 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5e43c26a-154b-3657-9959-9ac42a0ad4e3 | -6.68336 | -42.04531 | 2025-11-16 04:57:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 28224c42-808e-36aa-829c-43fab2ad3189 | -8.9007 | -44.43479 | 2025-11-16 04:57:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 06b12c43-0c5a-3910-b308-a0158928d1a2 | -9.02746 | -46.87956 | 2025-11-16 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c1478b52-64a7-3bc5-b7b4-65df58957eb4 | -10.66465 | -49.365 | 2025-11-16 04:57:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1d3bdd7e-de39-3240-b405-e4bb83f81619 | -8.32262 | -45.4066 | 2025-11-16 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83ce5f5d-d1c3-37cf-be32-e89a5b4e5160 | -11.96014 | -44.95262 | 2025-11-16 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0c122fd-450d-3772-8d6f-6afff5fc6152 | -11.48832 | -48.51771 | 2025-11-16 04:57:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fccfa87a-faf0-3a27-a41f-a38d6f0521c6 | -12.6781 | -47.17141 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c54fcd3f-8b5e-37c4-b40d-4ad76ebb885b | -10.16386 | -44.51229 | 2025-11-16 04:57:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c008cb7f-01e5-3ef7-8a60-43b7df356aea | -5.52307 | -51.22989 | 2025-11-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae9063ee-077b-3edc-99af-d6aeff3d6722 | -8.05953 | -43.10488 | 2025-11-16 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.6 |
| e3d93065-a2c0-3d24-ba8f-e0527cbfe48b | -6.72412 | -42.94087 | 2025-11-16 04:57:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 81b0609a-1031-3de0-8718-c8e5b60361cd | -11.16166 | -47.45435 | 2025-11-16 04:57:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18f9ff99-37ac-3744-82da-82fef13b3ef6 | -11.97148 | -44.96619 | 2025-11-16 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 1b09c6db-6594-3301-a380-58aa1371e734 | -7.04674 | -45.92683 | 2025-11-16 04:57:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6169a572-dddd-322b-9993-7be319307689 | -9.35328 | -46.59418 | 2025-11-16 04:57:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c3904e60-9579-31d6-b113-90e08b9931ca | -10.3298 | -44.60701 | 2025-11-16 04:57:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 368cf275-a08c-3255-aaec-7d99c1852c61 | -11.9729 | -44.95409 | 2025-11-16 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4a29076b-8c96-38a6-aa04-be27d29eaa6b | -11.05904 | -45.15796 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d03d09d-d2b6-3110-bcec-687fc758508a | -9.32409 | -56.13593 | 2025-11-16 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5c73e45-feed-3416-bdd8-80588db960bb | -6.15645 | -55.97088 | 2025-11-16 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 453e1313-7a80-3478-b536-72edaef96fc4 | -12.2146 | -49.54632 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e6d77e30-d35f-3164-814e-2283d5fba072 | -5.27288 | -49.32262 | 2025-11-16 04:57:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2dae2c7e-b7a4-336f-9ab7-ca9a462eaf78 | -11.96746 | -44.9506 | 2025-11-16 04:57:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70c01a04-678d-33bc-8173-3e6643d9c87a | -7.44167 | -45.22428 | 2025-11-16 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92e18781-8540-3faa-8b42-3fe1e8c4bd42 | -13.55923 | -44.10147 | 2025-11-16 04:57:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| f719ff49-98b2-3b85-8a49-40202dd5378c | -12.85865 | -46.78424 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4def278a-8a68-3ab9-ab51-ba57ea9219c8 | -12.6928 | -46.79456 | 2025-11-16 04:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd1ff8de-76bc-3058-b983-befba3078bb3 | -9.74488 | -43.94931 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 361e6987-dbcf-36e1-8648-85949afe56cd | -8.90354 | -50.22961 | 2025-11-16 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3205ee4e-df07-3120-a34f-3d7024145211 | -12.9554 | -48.81374 | 2025-11-16 04:57:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1486576-7262-3b1c-9197-af247b13a34a | -8.06569 | -43.10574 | 2025-11-16 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 09b65c4a-7946-3632-b070-81b2f86895ed | -12.00484 | -49.27911 | 2025-11-16 04:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 55ec2318-4d5d-3bde-af63-bd031a9f41f2 | -7.4421 | -45.22103 | 2025-11-16 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6057ce34-1325-3905-937a-72a505cc0102 | -6.71162 | -42.13581 | 2025-11-16 04:57:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 46e72d43-101b-37ef-b164-f1e8f0d455d6 | -11.41688 | -43.33492 | 2025-11-16 04:57:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 95a6c2b9-0f06-34f5-9554-7fc999b3028d | -7.0117 | -45.1636 | 2025-11-16 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c34c120-d577-36d4-8711-1a2df8ac7348 | -11.70986 | -48.40254 | 2025-11-16 04:57:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12b6ed63-b54d-3e06-a943-09bbddc72972 | -9.02587 | -46.88014 | 2025-11-16 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5133cdfe-f835-369b-9996-00da0ec101be | -6.05732 | -46.60789 | 2025-11-16 04:57:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c80d5b96-93d8-3397-b420-e905c5212e16 | -7.92098 | -47.09829 | 2025-11-16 04:57:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4a2a775-2bdc-34b1-bef2-1ae1130b90f0 | -9.7465 | -43.9635 | 2025-11-16 04:57:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1008ead1-9429-3b24-a4a8-566e69a4da53 | -12.87143 | -46.46042 | 2025-11-16 04:57:00 | NOAA-21 | COMBINADO | TOCANTINS | Brasil | 1705557 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 16824819-06c5-3b0b-9bfd-a9055a05dae0 | -7.04976 | -45.94228 | 2025-11-16 04:57:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| faf3fe48-0fed-3cae-9ef0-c4a6eec94422 | -12.15522 | -54.28741 | 2025-11-16 04:57:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a08f9ceb-f008-3526-8e90-9a11db2fbf9a | -7.27136 | -48.02946 | 2025-11-16 04:57:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0350a462-1715-3f3e-8b07-d141ceb7b551 | -12.15912 | -54.28433 | 2025-11-16 04:57:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1a7dd81-481f-3201-92f1-2112d3d6c983 | -7.05051 | -43.94977 | 2025-11-16 04:57:00 | NOAA-21 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README58.md)
