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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21157645-1c57-32ad-b225-704b11313a77 | -14.56126 | -48.07016 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2154094c-5627-3431-8ec0-8da6bf2ff1aa | -12.51186 | -44.72813 | 2025-09-04 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c1c758a-dc8c-3671-927c-26dfabb8f461 | -10.98595 | -46.83218 | 2025-09-04 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 479dc844-ff72-3d0d-adcb-f24c388919f6 | -14.7892 | -48.1586 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e423194-2e48-3bd4-9b65-9631198dc97a | -13.7434 | -46.93503 | 2025-09-04 04:27:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 075eeda0-d38b-3fac-b0f8-06b181872765 | -12.89401 | -48.03238 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1034c7e2-69bd-3ea7-a9ba-4cf21ae69b09 | -15.03772 | -48.11214 | 2025-09-04 04:27:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 07e3b58a-54a1-392e-97de-182b49646a75 | -11.95177 | -58.73228 | 2025-09-04 04:27:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2a1dab98-facb-34ad-b8f3-78d5e570938a | -7.97372 | -46.34514 | 2025-09-04 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aa2b9383-ae1a-3c56-a60c-fb556db630f5 | -11.36354 | -46.87396 | 2025-09-04 04:27:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 766443d7-b48f-38bf-bb3f-b9f47a7de3f6 | -11.38995 | -43.5629 | 2025-09-04 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fbdc0981-1c04-3d46-9d7a-ade77f49ae29 | -15.01812 | -50.035 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20dc51b3-1240-3540-9b16-2fc4a15ae5f6 | -10.11156 | -54.80239 | 2025-09-04 04:27:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b5893fa-f63b-3748-9db9-6490e0926607 | -10.89962 | -50.83025 | 2025-09-04 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 09ae3cd9-5c87-38ff-be59-727ab72bdb21 | -7.70611 | -50.25066 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 44b323cb-af68-31cf-819b-d7edf5d86099 | -12.24239 | -47.01692 | 2025-09-04 04:27:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ccc64b79-b5d0-3e15-9485-f5a4b2e1a8d0 | -15.02505 | -48.10644 | 2025-09-04 04:27:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e2a09cf-3492-3b95-86fc-88d5099968d2 | -11.59003 | -47.75868 | 2025-09-04 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7b3b30c7-0c69-3099-9220-eee434567c67 | -7.97079 | -55.31057 | 2025-09-04 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb5c5d17-fe52-33a6-8da6-29512b782a9c | -11.84451 | -47.54514 | 2025-09-04 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e184b3ad-313b-3e50-90c6-fe011fa019d9 | -15.03958 | -50.08152 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9923c9e5-3a28-3412-bff4-7730d5aae667 | -9.62276 | -40.61573 | 2025-09-04 04:27:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 3568e0ac-9114-37fd-81e2-f16b4a2fa08a | -8.36416 | -48.33527 | 2025-09-04 04:27:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| db442482-6124-39aa-8a32-c715c7b58e44 | -13.30997 | -51.76916 | 2025-09-04 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b0512db-b1a5-31d6-a730-ec1664ff2e1d | -8.08244 | -45.35365 | 2025-09-04 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c5daa503-dc81-30d9-a140-d13e3a261809 | -11.83702 | -51.4248 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8fa1b59-85e8-31c0-b967-7a108f86f496 | -11.59245 | -52.15981 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e9f75f31-db90-3b30-b8f6-be036a2cc4d0 | -11.87429 | -51.55445 | 2025-09-04 04:27:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fb06edf3-5413-345b-abc8-3d96df680491 | -7.69735 | -50.25798 | 2025-09-04 04:27:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 98df3b35-4aba-3a27-bda7-cf37c5d67939 | -12.90398 | -56.94649 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bc59888d-5f69-34d6-b0c9-368834c32576 | -12.90645 | -56.93348 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1e80bf4f-a650-3d31-a692-339dbfda4954 | -15.11968 | -48.19819 | 2025-09-04 04:27:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6f073a7-dbfb-37af-8ed2-ee6f81da36bb | -12.97898 | -54.78077 | 2025-09-04 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3930e94-49ad-3106-878b-6ee8e0de1b5b | -12.90065 | -56.93574 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ef6a216e-4957-36f1-b70b-e64255474151 | -8.91559 | -45.88469 | 2025-09-04 04:27:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e5c8459-82a0-3cc0-9ec2-d8921ace6209 | -10.4931 | -46.7646 | 2025-09-04 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9bf48e39-de8f-31a5-9eb4-47b708f88e33 | -12.9046 | -56.94322 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bbabc953-608e-3776-8096-2e10f4578076 | -12.23994 | -50.15381 | 2025-09-04 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aee62df1-5939-3d94-8f9a-12a062220271 | -13.57582 | -48.12975 | 2025-09-04 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| afee885e-b126-3d5c-a374-ddf24d2cc1e4 | -9.38938 | -48.05357 | 2025-09-04 04:27:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1433daec-a99c-3b2d-a7c4-efdcf7a02a47 | -9.69698 | -48.95888 | 2025-09-04 04:27:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74f76f19-f684-39cc-9228-22bf8d7ab717 | -7.77738 | -50.96088 | 2025-09-04 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c0f149e1-bff8-3775-9065-90886347a48f | -9.71754 | -51.05355 | 2025-09-04 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea42d784-593a-3bf1-ab5d-fb87dbee6a37 | -11.63699 | -52.18626 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6d3463c-b6f2-351a-9ba3-2eadc5657185 | -10.03526 | -46.095 | 2025-09-04 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| eb66b2aa-b3c5-3380-b74c-0ef8678f96a1 | -11.62354 | -46.6429 | 2025-09-04 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 346ba493-d0b7-3415-b319-ee0576454080 | -9.07399 | -46.9889 | 2025-09-04 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 612ce524-e30f-3873-b879-67866209e912 | -15.02615 | -50.03653 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a49d533-8b2d-37ab-a9ae-7a9ebb44a3b0 | -14.78315 | -48.13211 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 50a866b3-3c84-3dd1-b885-92faa3127539 | -11.84295 | -51.44711 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d1a90ebd-54ba-3a7e-be90-cf7e5a2e33ee | -9.96028 | -51.64059 | 2025-09-04 04:27:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4c737dde-c4f4-3582-af03-99320da2338b | -9.9634 | -51.63382 | 2025-09-04 04:27:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 49d2d1c2-c5a5-32ed-8709-276625b8e3db | -9.57073 | -48.23906 | 2025-09-04 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68d73480-37da-37d5-8617-2ff79a5ca962 | -11.85645 | -51.43527 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bab9d87f-2aa4-3e41-9168-9dbe4f33c168 | -9.43427 | -48.09343 | 2025-09-04 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 50aa67cd-4d55-33fe-a145-0f6f7ee16a6a | -7.74272 | -48.7679 | 2025-09-04 04:27:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c50d2305-25a5-35b8-a215-a19fd4850897 | -14.56402 | -48.05244 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a367d6f-4122-3151-96de-39974bbce36a | -7.9748 | -46.33821 | 2025-09-04 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 419e5b67-1252-39ac-9a77-a5999d8d4ce6 | -11.67067 | -57.34951 | 2025-09-04 04:27:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 17.8 |
| f81941cc-c22a-357d-9a4d-0542d1eedd70 | -9.47338 | -47.60968 | 2025-09-04 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f364fff2-403c-3bc9-9ab0-d8980146d961 | -12.89287 | -48.08278 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f06c978e-cf99-3f8b-b22c-58ed98de2600 | -11.60435 | -47.7538 | 2025-09-04 04:27:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00d7760b-5ddb-3357-8fe6-d26471b3de24 | -11.65591 | -54.52098 | 2025-09-04 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c93a95a3-ada2-3218-9c6f-30c6c81c45db | -9.95858 | -51.65039 | 2025-09-04 04:27:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27438ace-2f8d-3195-acdf-f315e8cea8b0 | -14.82429 | -48.34629 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4566a13-6837-3e03-9558-45acd30a2d4e | -11.96828 | -45.78389 | 2025-09-04 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1c308b0d-3a75-3717-b818-4727bd36fc21 | -13.44312 | -46.9398 | 2025-09-04 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f9835680-9a0c-3994-9712-46c2b209264f | -9.4359 | -46.76168 | 2025-09-04 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86f4b282-b3b2-3e24-a8a1-bafd93667927 | -11.88188 | -51.53239 | 2025-09-04 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eb4e8004-7114-30cd-9824-7b22e230afe7 | -14.82054 | -48.24019 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d49d380-1306-3199-9ce3-ae4c36efd6d4 | -8.03765 | -45.37638 | 2025-09-04 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 56e2d504-7c2c-3585-90da-33d37c5157cf | -15.04733 | -50.0556 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1ecef311-23b9-3e5b-afa8-13002d371677 | -10.49256 | -46.76809 | 2025-09-04 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95ea1305-7b28-33a2-8ee4-a4dc6dd6d222 | -12.46775 | -48.08193 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4a231def-ba87-3205-a932-b3f9fa19dcef | -14.60446 | -48.01233 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d57f7c37-381f-3101-bc3c-5b786fe008f4 | -15.05322 | -50.04093 | 2025-09-04 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 458d163e-447c-3d0a-96fc-b2cab8842722 | -11.96259 | -45.7753 | 2025-09-04 04:27:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 991c6532-acd5-3f6d-92d5-428da756cf46 | -10.58047 | -55.41867 | 2025-09-04 04:27:00 | NOAA-21 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0355b350-781a-37ac-8929-aeab8abb3006 | -14.39177 | -53.07415 | 2025-09-04 04:27:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d85e24f-0423-3188-be60-ca7219212f54 | -8.36786 | -52.55062 | 2025-09-04 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7b832055-a19a-3722-aac6-43d5d88bbe8f | -10.97368 | -49.75118 | 2025-09-04 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2c4c69cf-7d17-38ca-9670-c02ac6d3ccbe | -11.8825 | -51.55128 | 2025-09-04 04:27:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| da4e2b98-75a2-3f6c-b712-196a901ab789 | -9.07014 | -46.99185 | 2025-09-04 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05204e0c-5f5f-3fe2-8739-996519be8f61 | -8.36439 | -48.29084 | 2025-09-04 04:27:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fcad74d9-b220-351e-89c0-ed7d0928568f | -7.68882 | -48.73246 | 2025-09-04 04:27:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4da10b88-b627-38d1-8b5e-7eb9fea9dd30 | -8.07734 | -45.34193 | 2025-09-04 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 88b8ef2e-2e38-3781-820f-d63fef3311e3 | -8.04666 | -45.38504 | 2025-09-04 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4739d6a2-3fbf-329e-9df2-f04beeabfdb9 | -12.90522 | -56.93995 | 2025-09-04 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 027e756d-957e-375c-9739-8cd92b2b350d | -11.84506 | -47.54164 | 2025-09-04 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c5cab271-3249-3780-ab55-f7730431dc6d | -14.56787 | -48.04945 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 48788215-e562-3e68-a62c-c32ac8afa385 | -13.30684 | -51.78708 | 2025-09-04 04:27:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e906072-8f52-3d67-9a7b-a231b4cfa7ec | -12.89676 | -48.03644 | 2025-09-04 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eb1a67a7-7eb1-3de8-bf3c-307392dfcf2b | -14.82374 | -48.34984 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9876e03b-0441-3805-a1d2-fbe5fba1f6e7 | -7.70216 | -48.78104 | 2025-09-04 04:27:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9c2041f-7978-3c60-8e58-7243dc8a7e25 | -6.7529 | -58.73383 | 2025-09-04 04:27:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 0a4b1972-0c8c-39ff-a5d1-832723d0fa70 | -14.56182 | -48.04481 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 66d853bd-93ea-304f-825b-84002915a460 | -9.43818 | -46.79406 | 2025-09-04 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 669bc443-ab30-37b9-ba80-917d6a4e1596 | -9.44466 | -46.75226 | 2025-09-04 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7042155-751e-335c-a186-8f45a7c6ac70 | -14.81781 | -48.21427 | 2025-09-04 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5f0dbe09-9733-3c7e-8b7c-538808fe8517 | -9.68919 | -49.00711 | 2025-09-04 04:27:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README49.md)
