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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92964fe3-581f-3772-b1a7-ccc52a6281ec | -13.20841 | -54.50832 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 734371ab-d487-345c-98b4-c6456fee2ed5 | -11.56177 | -54.53071 | 2026-05-28 04:42:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67e7c002-8b2a-3ee6-b04e-9778ccc6646b | -12.55486 | -48.35411 | 2026-05-28 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ffd3015-0b64-3cb6-87f2-22e49adda25d | -13.21208 | -54.50897 | 2026-05-28 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6b86cfa4-c67e-379f-962b-18c72cfc9007 | -11.72624 | -56.84579 | 2026-05-28 04:42:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d061c5d2-b280-3ac7-bca9-afcb960c2246 | -19.69137 | -54.35291 | 2026-05-28 04:44:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 14bf0407-22a2-3d5c-9a47-24b73e7a52d7 | -20.73685 | -56.13579 | 2026-05-28 04:44:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6e651c8-f4dd-33c7-ba4d-64aaa5ab0562 | -20.91642 | -46.78678 | 2026-05-28 04:44:00 | NOAA-21 | FORTALEZA DE MINAS | MINAS GERAIS | Brasil | 3126307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ef1acc98-9d19-3fcc-9f6f-423649dea04c | -21.98095 | -57.60461 | 2026-05-28 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3777df0f-5dea-37bd-979e-734b3bdb5099 | -21.54306 | -47.04335 | 2026-05-28 04:44:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 32a17541-2d32-3d4b-840e-3c1713f02a71 | -21.549 | -48.8938 | 2026-05-28 04:44:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 069d337b-a55f-3cdd-8c57-0871414379d2 | -21.54672 | -47.04795 | 2026-05-28 04:44:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5232957f-f149-3bb1-a242-6c78bc12dd0a | -21.43266 | -47.06538 | 2026-05-28 04:44:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 602618a9-1824-3a2f-ab01-f4185017a306 | -21.41874 | -47.07569 | 2026-05-28 04:44:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 189ba64d-957b-3387-878c-e9bc33e6807d | -19.56157 | -50.01689 | 2026-05-28 04:44:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6e38b82-3bcd-3e75-9c29-9a7c6bca3f04 | -20.5214 | -54.60808 | 2026-05-28 04:44:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 665afd1e-6fd6-3856-b23f-db8874e6af38 | -17.95215 | -54.46706 | 2026-05-28 04:44:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b20a1258-c7f8-3136-a7b8-f39801f8bbb7 | -21.54465 | -48.89805 | 2026-05-28 04:44:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 102ae44e-a56c-3ccc-83bc-74a5be096638 | -22.2456 | -46.5814 | 2026-05-28 04:44:00 | NOAA-21 | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7044c4ef-4d8f-37ea-bfd2-dd2088e3f738 | -20.45522 | -46.40189 | 2026-05-28 04:44:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3f4fee2a-784f-32ab-9b05-9c8e146f8438 | -21.54446 | -47.04575 | 2026-05-28 04:44:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7c68889a-5fa1-39c8-8a3d-ea92d7e43a2c | -21.42485 | -47.06028 | 2026-05-28 04:44:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 00f70ea2-8933-3f63-94bb-bf365d3cb717 | -21.90019 | -53.46525 | 2026-05-28 04:44:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03684b39-fb8e-3723-a82b-faa522e92e74 | -21.98475 | -57.6055 | 2026-05-28 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 657e5706-cd2d-3cb4-8180-a1cd7c500f9e | -21.42339 | -47.07221 | 2026-05-28 04:44:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50933a7a-ce94-3ee9-8b80-645e38487cc5 | -21.15892 | -48.60015 | 2026-05-28 04:44:00 | NOAA-21 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 7422d076-c47f-3e4a-81bf-544ffae880c5 | -21.29918 | -48.58893 | 2026-05-28 04:44:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| d26d3c99-559c-3678-a872-5b514b7d91c3 | -21.42288 | -47.0763 | 2026-05-28 04:44:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e17e32e-264c-3162-9fb7-a8c700f4b8a9 | -21.29983 | -48.58398 | 2026-05-28 04:44:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 01d64197-9e53-3e0a-b124-0cf8abafda50 | -22.14302 | -49.42288 | 2026-05-28 04:44:00 | NOAA-21 | PRESIDENTE ALVES | SÃO PAULO | Brasil | 3541109 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 95ac9da3-37f1-3f6f-9e2f-780f109cd1ce | -21.54257 | -47.04737 | 2026-05-28 04:44:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bbac7f16-b01a-379b-bb4a-e80e2f6eba6e | -21.54838 | -48.89861 | 2026-05-28 04:44:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6c7f643-964e-31ad-a2d7-949174e832b1 | -21.42437 | -47.06425 | 2026-05-28 04:44:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6289e67a-b0b2-393c-a3d5-1b0f179ad160 | -20.1915 | -49.5641 | 2026-05-28 04:44:00 | NOAA-21 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6b869e0b-c55b-3e98-92a4-d93634ab95c9 | -21.429 | -47.06086 | 2026-05-28 04:44:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15763435-a7c1-325e-a6cd-5f83e101b194 | -21.81293 | -53.09107 | 2026-05-28 04:44:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b8d7bac3-83f9-32f4-b68d-a900378817af | -21.42753 | -47.07281 | 2026-05-28 04:44:00 | NOAA-21 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9de80684-26ef-39dc-8c93-cb92ff97361f | -27.91639 | -53.69824 | 2026-05-28 04:46:00 | NOAA-21 | SANTO AUGUSTO | RIO GRANDE DO SUL | Brasil | 4317806 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 63909df2-5665-319e-a00e-21c058985f4f | -13.2186 | -54.5182 | 2026-05-28 04:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| b021e87c-ab3c-3e3a-9a9b-b55c8de2292f | -11.591 | -47.4496 | 2026-05-28 04:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 04894537-b053-35aa-b196-0e7579495866 | -13.2189 | -54.4975 | 2026-05-28 04:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 74ce9cbc-c9ad-3e95-85a6-59564b587990 | -11.591 | -47.4496 | 2026-05-28 05:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 0ba95191-eb4c-3edd-9fa9-61ea344bd00a | -11.591 | -47.4496 | 2026-05-28 05:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| f36b93f1-ca02-349c-bded-5cf9210bf071 | -8.09225 | -55.01886 | 2026-05-28 05:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| edb773da-1a22-3a26-b8f1-5ef1d0a867df | -7.00874 | -44.99908 | 2026-05-28 05:14:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1575aa82-6741-33af-b84f-9a1606cb7c65 | -9.3536 | -45.46896 | 2026-05-28 05:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 55d546c2-395e-325a-a527-2769a4e01b34 | -11.58829 | -47.4438 | 2026-05-28 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 55af5ceb-ae9e-3619-8414-af60e41ce1de | -11.96549 | -47.37839 | 2026-05-28 05:14:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da3ae447-0b7d-39eb-9c4f-3010e4aec042 | -11.96939 | -47.37753 | 2026-05-28 05:14:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b177c5b5-4d66-317d-afa2-7dc3829f6c6e | -8.68341 | -48.30831 | 2026-05-28 05:14:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d8c628db-9213-3ead-9d13-b408d8ffeb6a | -12.69252 | -44.78954 | 2026-05-28 05:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 097ab277-fcab-30b2-a099-d643d0518d5d | -11.4743 | -52.92394 | 2026-05-28 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 62194e2b-8524-3c84-9377-6b9a312a1b63 | -12.68851 | -44.78861 | 2026-05-28 05:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9780fa95-be5b-3cdb-ba26-41abd9d0f8b1 | -5.95809 | -43.49622 | 2026-05-28 05:14:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 1f9a9445-bc41-33fb-855a-8671670a40e5 | -8.71385 | -47.80007 | 2026-05-28 05:14:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48b02a15-4047-3ccd-aa5f-ba67f71d4467 | -11.27365 | -53.97392 | 2026-05-28 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 239c5baa-b4b5-303e-8c65-0bf71622143b | -8.3385 | -51.92429 | 2026-05-28 05:14:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 18b5e38a-5a1d-309b-a23a-41b3de777bb1 | -5.79248 | -45.13301 | 2026-05-28 05:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c26b39b-9473-3496-8d11-ccba2b786416 | -11.59894 | -47.44884 | 2026-05-28 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5806bef5-0622-3ec7-941f-2b56a09932f1 | -10.62495 | -46.90591 | 2026-05-28 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ee82729a-a505-3aa9-9621-80bc385b838d | -8.91371 | -51.85568 | 2026-05-28 05:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f45d37d2-5eb2-3a96-a9a4-f1aa5679e64d | -10.82441 | -56.60706 | 2026-05-28 05:14:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a8fd01d-91a7-3769-abdb-36ec19faff56 | -9.14529 | -51.27876 | 2026-05-28 05:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf5e7bdb-eb92-35ec-bf9e-415a5f07634b | -12.69517 | -44.7893 | 2026-05-28 05:14:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b122b199-65b7-3b7f-9386-be9294688d8a | -5.79429 | -45.13676 | 2026-05-28 05:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9f23c9ae-c6c1-3500-b891-f71cdacea023 | -11.45891 | -52.92167 | 2026-05-28 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 31253c17-4169-335f-a166-e596cc92b968 | -5.20491 | -56.04427 | 2026-05-28 05:14:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b95d94a2-a1f1-370e-8176-e5283f2a370d | -8.7271 | -48.32594 | 2026-05-28 05:14:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| cfe7c556-ee2c-35f1-bff5-ad80c90b96b9 | -10.61824 | -46.91314 | 2026-05-28 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 6173dccb-dabb-323a-951c-f2d94115b632 | -11.27727 | -53.97446 | 2026-05-28 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 05042956-9121-3672-8f8b-acda0cc88e98 | -10.63728 | -46.89983 | 2026-05-28 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 554310ed-9a5b-3ce4-af16-e641d11d2ffe | -11.44985 | -52.93014 | 2026-05-28 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe26f8c7-bf27-32e7-9fb5-9b50fda4eeda | -9.35422 | -45.46423 | 2026-05-28 05:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ce4288c-8a1e-30f8-98f9-d2e80ef9f3c8 | -9.38616 | -48.44082 | 2026-05-28 05:14:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 54b83e12-8538-3dc9-9614-82b75acb4857 | -10.63778 | -46.896 | 2026-05-28 05:14:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 535b3f00-75d7-39ee-863b-e35a22445796 | -11.44822 | -55.11314 | 2026-05-28 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4ca73e30-39e4-3685-98c1-d78eedec036b | -9.1489 | -51.28305 | 2026-05-28 05:14:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9632646-9f85-3f39-a4a1-7f718d5a7975 | -9.28268 | -57.84689 | 2026-05-28 05:14:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5beb9a90-4c61-3487-a9e2-30850229f51c | -7.71267 | -45.93965 | 2026-05-28 05:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ca9fd1c-b088-39aa-9b5a-24a516f23d89 | -10.84521 | -53.7552 | 2026-05-28 05:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 258e7fa5-f455-3316-bd00-be01f0f9f11a | -10.63014 | -48.32979 | 2026-05-28 05:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 96c1b113-607c-303f-9343-e28f0237c813 | -9.99075 | -53.62543 | 2026-05-28 05:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 045b596e-faf2-3fc2-9fc4-e39963234577 | -11.58275 | -47.44299 | 2026-05-28 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| be903f36-be63-3d9e-bc59-2bb92593c3c9 | -11.59432 | -47.44074 | 2026-05-28 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 199a2c32-dc3a-33b9-a8bb-207244d333f4 | -9.28055 | -48.58956 | 2026-05-28 05:14:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1f9e21c4-3d0c-3fc7-8755-afab6617968f | -9.73475 | -49.21692 | 2026-05-28 05:14:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23aae8f4-a86b-35f2-9388-23a4dd4e645f | -9.73954 | -49.21765 | 2026-05-28 05:14:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 75cc2976-89bd-34be-b609-35b9cc33e61f | -11.47883 | -52.91971 | 2026-05-28 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e3028c00-6f4c-3cb6-b379-d0b365245876 | -11.29613 | -54.02735 | 2026-05-28 05:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 110efba5-7c15-3e1f-8d98-86192f72c88c | -11.64182 | -52.86143 | 2026-05-28 05:14:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8fda4f4c-5ff5-37ac-a0bd-7d849514095f | -5.80086 | -45.13321 | 2026-05-28 05:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61474764-f9bd-32e7-bf5e-55553ecf7d54 | -11.47498 | -52.91914 | 2026-05-28 05:14:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| af0ef44c-6e67-3fbb-b4c0-011f3d72376b | -9.39622 | -48.44234 | 2026-05-28 05:14:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b05833a8-6bd2-3e5f-b50b-2b27d0b48203 | -8.70822 | -47.80244 | 2026-05-28 05:14:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4810f816-cfaa-3538-9588-aac6c014f954 | -9.44355 | -48.89196 | 2026-05-28 05:14:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e52b588-dce6-31e3-a713-7145cf731abd | -5.80142 | -45.12909 | 2026-05-28 05:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84df303c-ec36-3cf0-9b15-23d8938516c9 | -11.44879 | -55.10932 | 2026-05-28 05:14:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 39d0d183-b560-3b10-8be6-8915b0eadbbc | -9.60348 | -58.34404 | 2026-05-28 05:14:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 778aeb1e-e132-3e5f-8ca7-e9fd3ddcc65d | -12.32529 | -47.8966 | 2026-05-28 05:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9614e369-afc3-3d00-b2ef-88a6c7ec7691 | -11.59478 | -47.437 | 2026-05-28 05:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README11.md)
