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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5aa33ec4-5f6c-32d4-8db2-e2f94ccd71d4 | -2.95572 | -48.58799 | 2026-09-25 04:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3247475e-2fe6-3c10-ac97-3d3d0b59bda5 | -10.40753 | -46.26239 | 2026-09-25 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| f3f95133-53b9-3231-81de-903062fc4714 | -6.82909 | -43.56496 | 2026-09-25 04:25:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b5313bb-c067-3fde-a3ec-ae3f2336e2bd | -10.92666 | -43.8567 | 2026-09-25 04:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6f56a6f7-0308-338e-8fd0-859990699ecd | -9.6315 | -43.94294 | 2026-09-25 04:25:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d1943e53-f399-337f-b280-bc31103e7f7d | -3.39549 | -44.50286 | 2026-09-25 04:25:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1f5c201-b387-36ff-ad19-1df4ba18ed08 | -7.59304 | -41.78944 | 2026-09-25 04:25:00 | NPP-375D | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c352c86b-de2f-3f7f-aaf3-8eddb1c83d1f | -8.32993 | -44.15051 | 2026-09-25 04:25:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 75e9721b-4c48-3c70-b588-2a2543176e2e | -3.62515 | -42.75694 | 2026-09-25 04:25:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0709dc6c-fddf-303b-8179-a4f7e11e5a14 | -7.39252 | -44.7712 | 2026-09-25 04:25:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f198d936-b29b-37ef-be64-24f2b0a7fa79 | -7.12903 | -43.57021 | 2026-09-25 04:25:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2cdab6fc-4abb-3975-87bb-9301209a0b0d | -9.62873 | -43.9389 | 2026-09-25 04:25:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e65bfba0-3c9a-323d-a2c7-da8dee48deee | -8.33576 | -44.14765 | 2026-09-25 04:25:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 70849f1a-d75d-3359-b561-a3b867129982 | -5.10007 | -45.52282 | 2026-09-25 04:25:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2b0a15ce-94bb-31e6-8209-8437fbc98a09 | -4.61394 | -42.79633 | 2026-09-25 04:25:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93287187-fbcf-3f84-96e0-faa1d970d8e8 | -7.16715 | -45.04047 | 2026-09-25 04:25:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7470c305-3453-3dab-ad25-d6e27ffb5dd5 | -8.24864 | -54.68958 | 2026-09-25 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 74dbd938-b254-3dd0-8fd1-c571668fac7f | -10.40405 | -46.26178 | 2026-09-25 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 093b893f-b455-3b17-b2ec-2fe58ec2572c | -9.63481 | -43.96502 | 2026-09-25 04:25:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e8534137-ca71-33a1-a317-777562360638 | -8.3391 | -44.14819 | 2026-09-25 04:25:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2481f4ac-4497-3158-8b8c-c94f5e81b23d | -9.00934 | -49.64255 | 2026-09-25 04:25:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d445d0db-2e72-3ddd-9672-d1b5277b84f2 | -8.32772 | -44.14295 | 2026-09-25 04:25:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9764c436-d401-368e-b04b-ceaa27051840 | -9.63204 | -43.96097 | 2026-09-25 04:25:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bf73c8be-36aa-314d-835c-2ec9bba347ce | -9.6265 | -43.9529 | 2026-09-25 04:25:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ec000ba9-541a-3db7-8a89-e42b1a10f18d | -2.8564 | -48.56513 | 2026-09-25 04:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 254b12cb-0c04-3677-bfa6-6836a9fa0ae0 | -2.89711 | -54.09753 | 2026-09-25 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 613f3820-d385-3674-acff-2195599b9728 | -6.82964 | -43.56148 | 2026-09-25 04:25:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ef90cff-03f2-30f5-9de6-f652113d6ff3 | -3.00689 | -51.53476 | 2026-09-25 04:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1f8db82-4369-3b93-8700-8356e0fb6f56 | -5.09651 | -45.52224 | 2026-09-25 04:25:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 984d0bd1-435a-3c22-9a7b-21e8ec6789c7 | -10.40817 | -46.2585 | 2026-09-25 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 55777359-3fc6-3004-9694-7860becc07fa | -9.62983 | -43.95344 | 2026-09-25 04:25:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 086626d3-3948-3738-a67d-454f1ffd26df | -7.59361 | -41.78577 | 2026-09-25 04:25:00 | NPP-375D | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ccbf279b-5b4d-32a7-9482-237fad121e1e | -8.59525 | -48.36838 | 2026-09-25 04:25:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 96fcbab6-8431-3f0d-8c13-9590fb52ca3c | -8.33439 | -44.14402 | 2026-09-25 04:25:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 71015c08-c4be-3567-9a93-e74cd2bb5fd9 | -2.56297 | -49.08501 | 2026-09-25 04:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4ddedbd-9f22-3316-ba38-6e12ef42fcdd | -9.47716 | -40.32582 | 2026-09-25 04:25:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 638b6127-b10f-3844-9413-865d1d97bbd9 | -7.12507 | -41.72548 | 2026-09-25 04:25:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ff49856f-a078-36b3-a097-4b5da8bc0a80 | -4.32304 | -44.72778 | 2026-09-25 04:25:00 | NPP-375D | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3fd703a6-f733-34a9-9de9-a55e8397b71d | -4.60784 | -42.79182 | 2026-09-25 04:25:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 6b620d48-86e7-3de0-9ca8-86da3a830ce4 | -10.4047 | -46.25788 | 2026-09-25 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29922b01-7460-3703-a58c-7caaec046a76 | -8.92158 | -43.87186 | 2026-09-25 04:25:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d31a8cf1-618f-306b-9306-b099443c5708 | -3.23696 | -46.93227 | 2026-09-25 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 13e12d65-9b53-36f7-9081-f389cf3f7d45 | -4.27383 | -48.63315 | 2026-09-25 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 153d2347-e147-3536-92ec-69d12ba9da89 | -8.92414 | -44.5286 | 2026-09-25 04:25:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2b003d9d-f3bd-3b01-a6c0-5b97439012b2 | -6.83297 | -43.56201 | 2026-09-25 04:25:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4527db1b-d6b4-309b-83ef-b88e526ebb43 | -3.77041 | -47.54268 | 2026-09-25 04:25:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9de8bff7-411a-3427-a95a-72fdf4c7438d | -10.41383 | -46.2675 | 2026-09-25 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d7c93ee-643c-3861-9964-bb2eb2807d8c | -4.70404 | -48.30844 | 2026-09-25 04:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fed5e9b5-1065-398d-a26c-3ab6b2fb9c7a | -8.34791 | -45.61629 | 2026-09-25 04:25:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 28dd914d-34cb-3078-b591-37e0c7f5ea6e | -3.79553 | -52.36998 | 2026-09-25 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bcb249fb-aff0-3177-a5b3-7d4f384348a6 | -8.24843 | -54.69068 | 2026-09-25 04:25:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 2373966a-debb-3cc6-9946-c021c791debb | -6.42959 | -35.24708 | 2026-09-25 04:25:00 | NPP-375D | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 74fccf60-7358-30bc-9dab-14b42f066af9 | -8.33383 | -44.14753 | 2026-09-25 04:25:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a88ccd06-132f-3ea8-909c-bd71982d4160 | -10.40688 | -46.26628 | 2026-09-25 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ccfbeea6-3b56-388f-a5d5-73406263b13a | -6.89422 | -43.74756 | 2026-09-25 04:25:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d795e165-7880-3c42-bece-4e7c46c7af56 | -10.41667 | -46.27196 | 2026-09-25 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6144d36a-e4f9-33a0-93e1-1d133dde85a0 | -9.91486 | -48.12314 | 2026-09-25 04:25:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e9584b0-bb46-3c11-9fbc-c649ee5925a9 | -2.90179 | -54.09709 | 2026-09-25 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 44104b3e-8bb5-3fc5-aea1-7343b291b8cf | -3.23303 | -46.93161 | 2026-09-25 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 0ed16034-c4b1-33bd-8969-b25e859a1a29 | -5.19766 | -42.76497 | 2026-09-25 04:25:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f2af659e-0e19-3181-878c-b863d1297c84 | -6.42764 | -35.25139 | 2026-09-25 04:25:00 | NPP-375D | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 32675c79-f559-3db5-9c67-f9e1aa690f32 | -3.24053 | -46.9299 | 2026-09-25 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 16b7e84e-22dc-3657-98c0-b7e061c78bc0 | -2.90346 | -54.0987 | 2026-09-25 04:25:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1a31a570-b44b-3073-a382-344d34ad4a4d | -3.98381 | -48.42929 | 2026-09-25 04:25:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ae6ea5df-90d2-3114-b8fa-6c9aeb5bb501 | -9.02429 | -49.63275 | 2026-09-25 04:25:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d3874c2-f783-389d-b1a3-4a84db90aacc | -9.01791 | -49.6441 | 2026-09-25 04:25:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a9dffbce-98b2-32eb-b549-fd9fba9f3ebf | -3.5012 | -50.74522 | 2026-09-25 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4893b17a-43d4-3f36-9b2d-5c028fb36db0 | -10.41602 | -46.27584 | 2026-09-25 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0466f7aa-961b-38ec-bf07-174c706b74bc | -3.49709 | -50.7387 | 2026-09-25 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d610962-bc9a-393e-9ab3-59e1d819a1f9 | -8.32937 | -44.15403 | 2026-09-25 04:25:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 274b5931-5db4-34c7-bdf9-b43d187f693b | -4.61006 | -42.79927 | 2026-09-25 04:25:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7d4a8ff9-a456-32d7-bbb3-2ccaa54f7869 | -4.46082 | -47.92177 | 2026-09-25 04:25:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 54733e27-d3dd-3d0b-aea2-1a6d09b138cc | -5.42576 | -36.75933 | 2026-09-25 04:25:00 | NPP-375D | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 18524cd7-4362-3868-a0d8-fc7a787ca797 | -3.2283 | -46.93592 | 2026-09-25 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d34c199b-1d63-388b-82e9-d809924c0eb6 | -3.97953 | -48.42853 | 2026-09-25 04:25:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46a200be-faa0-37b7-b477-dc4c9aa88dcd | -7.02645 | -41.54955 | 2026-09-25 04:25:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 192d5426-8c01-3c73-b509-54a14a486f09 | -9.62927 | -43.95694 | 2026-09-25 04:25:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 3fa5eb0b-2938-3397-9382-9efa6c8aefaf | -6.63012 | -41.72077 | 2026-09-25 04:25:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a3a2ede8-f80c-3bde-bf27-623baac9629d | -7.04409 | -41.50304 | 2026-09-25 04:25:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b6f3a52c-1ca7-3d1c-a7ce-11923dd56769 | -3.23382 | -46.92664 | 2026-09-25 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 1307ff72-3003-3aec-812c-7b32cac2cded | -4.60839 | -42.78836 | 2026-09-25 04:25:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4430d998-b8f6-3732-95a5-9fe8e5a499de | -3.2366 | -46.92925 | 2026-09-25 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| eb675ceb-736f-3a64-bd20-2ecd04861b49 | -8.32329 | -44.12784 | 2026-09-25 04:25:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2affb1be-c721-39d8-8cac-993e311c7b00 | -2.85569 | -48.56284 | 2026-09-25 04:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 80ae0222-5383-3b89-a725-b511118e899b | -7.40203 | -42.63783 | 2026-09-25 04:25:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4f497044-6f90-3ee0-bbe3-d9be959d3a80 | -3.50169 | -50.74233 | 2026-09-25 04:25:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 210ccf29-ebb0-3980-9bd5-40b27aef8e2d | -7.40647 | -42.63133 | 2026-09-25 04:25:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ab387322-0174-3ba7-9fb7-49a27aa7aac1 | -9.63094 | -43.94644 | 2026-09-25 04:25:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b9fc783a-4858-3a27-8a44-b91aa387ccad | -3.27369 | -48.53671 | 2026-09-25 04:25:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3b37acc-d4bb-36a5-83e8-6f9e919d6593 | -9.63149 | -43.96447 | 2026-09-25 04:25:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 85dfd343-e629-3b50-8359-84b79d7ad7fe | -4.37423 | -46.23862 | 2026-09-25 04:25:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fa8d1de-75c7-354e-a9b5-84c34156ddc8 | -2.85199 | -48.5644 | 2026-09-25 04:25:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d68ae5f-237b-3087-a9b8-f79cb7bcb2c7 | -8.32716 | -44.14646 | 2026-09-25 04:25:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c954bfd1-fff8-310b-8656-dbb3ff3e7222 | -9.62595 | -43.9564 | 2026-09-25 04:25:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 35b4526a-35e9-379a-bab7-3f8a675f85ec | -8.38672 | -36.70822 | 2026-09-25 04:25:00 | NPP-375D | PESQUEIRA | PERNAMBUCO | Brasil | 2610905 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ccf93216-839b-3f67-88f0-77ab8bd77329 | -5.12441 | -42.6895 | 2026-09-25 04:25:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bd824ebd-a7ac-37f4-8b8c-2aa0e6879d52 | -3.7291 | -48.90701 | 2026-09-25 04:25:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2eb28f35-c07d-3ebb-9eea-a2bd24387b98 | -9.0193 | -49.63603 | 2026-09-25 04:25:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6e384a9-d14f-3480-95bf-8ed4429bd20e | -6.81965 | -43.55988 | 2026-09-25 04:25:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eadb5d7d-8a0e-34be-8ab8-13b390769e06 | -3.73548 | -47.9776 | 2026-09-25 04:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README17.md)
