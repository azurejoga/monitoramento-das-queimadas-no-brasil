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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 225808b0-bfdc-390f-a1f6-b7ca2dec40ed | -7.70238 | -50.28743 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e5e94774-1c3a-3d4b-8587-c0900628eb92 | -6.78755 | -44.09563 | 2025-09-04 04:53:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a7e11394-8359-33a0-9af7-0aac424a0c3e | -6.87162 | -45.58076 | 2025-09-04 04:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2871d716-7841-3e18-af98-19c57eb635cf | -7.51117 | -45.36766 | 2025-09-04 04:53:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 462a4617-eb7d-3361-bebb-39d7086af483 | -5.6141 | -57.3626 | 2025-09-04 04:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95c510b5-0591-3cd9-b05d-b44cc7a01203 | -6.23252 | -43.56105 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8b13e459-3793-3c55-8bd9-5f788ad06232 | -5.90461 | -45.56555 | 2025-09-04 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9dd72f0-0c2c-32e9-b739-20dcec9f9820 | -9.4337 | -46.77202 | 2025-09-04 04:53:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3390d11-ff33-3139-ab20-1192c9431645 | -6.78257 | -44.08394 | 2025-09-04 04:53:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| b2b1cb29-61d2-314e-a89d-0b47533e8ba6 | -6.69848 | -48.41228 | 2025-09-04 04:53:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c828dc8f-88a6-391d-9bee-47bebaf9549c | -6.25935 | -43.28729 | 2025-09-04 04:53:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 570c150e-9469-3b2e-bfac-ec586e7473e5 | -9.06882 | -46.99027 | 2025-09-04 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb13928a-6326-3430-b879-5f7f862beed5 | -5.97245 | -44.11999 | 2025-09-04 04:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 641d5128-c9a6-3da2-9e81-d7ed6c75faca | -7.9778 | -46.35374 | 2025-09-04 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ec489d0-cf4e-39a1-98b6-77f646e4a4b3 | -8.00596 | -44.77636 | 2025-09-04 04:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d12de96-c086-3a29-9f9b-9f20d78e2848 | -6.73843 | -45.92213 | 2025-09-04 04:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a516700d-c753-37d5-82ea-b97acf34fb13 | -4.61179 | -56.16961 | 2025-09-04 04:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6de6bf13-de34-36da-9834-c2a3e159c470 | -9.48053 | -47.61045 | 2025-09-04 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2fce01de-da6c-32ec-ad51-a8632a240c2e | -7.77569 | -50.96088 | 2025-09-04 04:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ef4974b-96aa-3542-bae3-e7da578e60d8 | -8.0089 | -50.09435 | 2025-09-04 04:53:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 512d9d5e-4fe6-3d41-94aa-e45757cd6b31 | -6.54548 | -42.95544 | 2025-09-04 04:53:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 794d646c-8a71-3426-ad5f-447410bf2988 | -6.22732 | -55.93387 | 2025-09-04 04:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a8740ce3-5576-3cf8-ac6c-1acd1d247a04 | -6.49288 | -44.10362 | 2025-09-04 04:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2108974-f0f3-3f3e-8862-3a0d9227f315 | -6.77811 | -44.08784 | 2025-09-04 04:53:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9388e76-81b7-3497-9116-c8c87fca16f3 | -9.04359 | -47.01204 | 2025-09-04 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37ba1d9f-ef26-3aba-bbd9-b66ec23765b7 | -6.22576 | -43.54695 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 46ed1fef-6e14-3ff7-9aa7-66e3e1aa80f0 | -6.83821 | -46.39192 | 2025-09-04 04:53:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bfb0839a-aa5f-36e6-90c0-813600af6639 | -6.28594 | -43.60348 | 2025-09-04 04:53:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9dee53db-559e-39ae-b44e-c31be885ba2c | -7.7119 | -50.24773 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8a877ff-a0bb-33b0-924b-dd0f471ad12a | -5.97791 | -44.11805 | 2025-09-04 04:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1f70678b-4b76-3091-984e-307e09ccb63f | -7.80118 | -46.08297 | 2025-09-04 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7e760be-ca28-3666-90cc-ce24b3df3ef7 | -11.05417 | -45.15129 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6991f490-6bda-3036-a795-f9fa20af0aa6 | -6.3382 | -45.68526 | 2025-09-04 04:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b83cb092-4ff0-344e-a725-06dc8375b350 | -11.13116 | -44.63507 | 2025-09-04 04:53:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d126a58-c3e5-372d-ba1c-6ec37eb5ebf2 | -7.72857 | -48.72892 | 2025-09-04 04:53:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c17c0db8-fafc-3314-a02f-d3c5917a6ecf | -9.05136 | -54.95433 | 2025-09-04 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 218b98ae-dc76-3c41-ad47-a2ee85adfa9b | -8.05981 | -52.37417 | 2025-09-04 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9a5e8f0d-bed6-3d49-8ace-fe5c22d9f4f3 | -9.69028 | -51.04471 | 2025-09-04 04:53:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5b6df18-f680-3008-adf6-15a2ef54219d | -6.842 | -46.39677 | 2025-09-04 04:53:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 379f3ca5-d91f-329e-8e76-b95ef8a974cf | -8.07854 | -45.34846 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b9583923-b146-3360-ad6b-b9e9078119fc | -8.89612 | -45.82576 | 2025-09-04 04:53:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5e79bcbe-a0f6-3cb1-9f59-3f72bba16f47 | -6.79115 | -44.44246 | 2025-09-04 04:53:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 586c3bab-c240-3f69-8b71-412eb8698142 | -5.70205 | -45.15835 | 2025-09-04 04:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aca9f94e-cfa1-3bff-9195-bc7f5dc63552 | -6.28753 | -43.51625 | 2025-09-04 04:53:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 85a96973-6b06-3a82-805f-6413b16ff2b0 | -7.6959 | -50.25872 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 22d94db0-2e61-3cac-8aec-06692cc6bb1a | -6.34412 | -45.67643 | 2025-09-04 04:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e07873a-2a08-30aa-b8e1-d5ac93c065c9 | -5.60844 | -45.0288 | 2025-09-04 04:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 688b6920-cda2-3873-8a45-ff720176431f | -10.43301 | -50.38353 | 2025-09-04 04:53:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ace2aeee-3e36-32ef-a00c-71ca73edf79e | -6.87227 | -45.57625 | 2025-09-04 04:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9097b5dc-66c6-319c-90e1-5dcb369ede30 | -6.76925 | -63.13672 | 2025-09-04 04:53:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d563dc04-79ef-3887-9a2e-a21d1e15d11f | -5.18933 | -46.06945 | 2025-09-04 04:53:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ec66f7a7-6987-3fe1-9d59-813045fde33e | -9.07321 | -46.9907 | 2025-09-04 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0470adbf-ee60-328e-bebd-a2ad975e9b16 | -11.03091 | -45.13044 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 302423db-8c2e-3e6a-a6a5-da12608b8e9e | -6.8824 | -45.55925 | 2025-09-04 04:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21daf7ad-15c8-3284-9caa-110adf1b7516 | -6.1655 | -43.31928 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2e0707dd-7660-3715-b5d6-327e1c0afc62 | -10.43186 | -50.36623 | 2025-09-04 04:53:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2e2d1e0c-f582-3ad7-b9c1-76189bf5091b | -11.04151 | -45.1287 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f452a3cf-5743-3454-9ce2-8585711471e6 | -8.08598 | -45.35525 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fabf870a-f127-323c-acd0-eb59433b6eda | -8.35496 | -48.29918 | 2025-09-04 04:53:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52bb9950-f38b-30c9-9261-e01594800c29 | -11.03053 | -45.13337 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a88b0791-9fb4-3c69-9875-1c2c07c432f1 | -6.68237 | -48.41475 | 2025-09-04 04:53:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1df3c4c7-87e2-3940-8f90-34db6806c14a | -7.54955 | -45.72127 | 2025-09-04 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d258663-1999-34b7-ad27-751adb1e094c | -9.06446 | -46.98963 | 2025-09-04 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 484f8ba2-7f02-3913-a06a-ba64506e7479 | -8.86147 | -52.0205 | 2025-09-04 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2dffd6e-f480-38ef-85f9-145446c63e56 | -7.68818 | -50.26196 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0237c09d-a686-38e4-8f88-83270c4c5a37 | -6.59378 | -44.06743 | 2025-09-04 04:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4fdc73bc-93b8-364a-bb27-18a4d4b6cde5 | -7.55023 | -45.71641 | 2025-09-04 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bdd20d33-00e3-33d0-883e-d09f89ffbf01 | -6.76159 | -59.67276 | 2025-09-04 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf513162-054e-354e-80d3-c84cf0c2d093 | -7.7042 | -50.25177 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b581faa8-1245-3b36-92e1-96c1cb2d6243 | -6.88175 | -59.08294 | 2025-09-04 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 881a8210-37ad-360f-b9b0-0a3b3c3d6286 | -7.7153 | -50.29747 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b7cf1c45-e677-3ea2-998f-e964d01a7ad7 | -8.04534 | -44.13827 | 2025-09-04 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a26e520f-266a-3dbd-91eb-9e71d17f8933 | -6.83012 | -44.27693 | 2025-09-04 04:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 873737c7-f842-35cf-b491-a307b98db737 | -7.70006 | -50.25521 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cc5cbd4d-c259-38e0-9a19-12277e94c5ad | -6.73452 | -42.2646 | 2025-09-04 04:53:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8e5a00cf-0b3a-3f9b-bb75-ae19b76d8af5 | -6.27866 | -43.84679 | 2025-09-04 04:53:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e206515-f64a-3aa3-b263-375048188a38 | -6.46685 | -43.97757 | 2025-09-04 04:53:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e5b7261-cc91-3168-9027-c3eb1620262e | -6.73981 | -58.72795 | 2025-09-04 04:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| c6e1eb2e-6265-311c-b402-898847170d1c | -6.83836 | -59.36374 | 2025-09-04 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 65970355-5940-31d9-9d35-1b0764165193 | -7.71129 | -50.25188 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f9c7c884-6ed8-3617-a9da-56518dd14000 | -8.73147 | -47.0048 | 2025-09-04 04:53:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1459caf1-b295-3c25-af26-f126c2f32d51 | -8.026 | -44.04638 | 2025-09-04 04:53:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f17590ab-d8fe-3028-805a-81cf2c78dfcd | -6.54148 | -43.10625 | 2025-09-04 04:53:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 121e4f5f-83df-377c-8918-00d025dfd7ec | -9.96768 | -51.63119 | 2025-09-04 04:53:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3c1080b-d163-3e0f-a857-c47ca9ad9aef | -9.97565 | -51.62484 | 2025-09-04 04:53:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9b3d3f6-84d6-3b39-8c8a-9d897104e1bc | -6.22913 | -43.41118 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f24d813-d989-3b36-95e5-066fa7e28fe1 | -6.87093 | -58.93452 | 2025-09-04 04:53:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75b8ff64-9b3b-3d38-bd05-6975edc5139c | -5.70604 | -45.16401 | 2025-09-04 04:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 500d70b6-06ce-34d5-b149-6ac777bb8ae1 | -6.16059 | -43.31512 | 2025-09-04 04:53:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.2 |
| af9d5c09-223d-3585-98eb-949a194e6926 | -7.77513 | -50.96453 | 2025-09-04 04:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5864624-ae95-33c0-a63e-418763808af5 | -5.98396 | -44.14809 | 2025-09-04 04:53:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a9a49e3-5bd5-3c4e-a5d2-57ef8ebae63c | -7.69877 | -50.2635 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 557a9dcf-0f99-334b-881b-7f1a3aa768fd | -9.61721 | -47.02782 | 2025-09-04 04:53:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b7b102f-4353-3f62-a5d5-dc74f95e2d72 | -6.29168 | -43.60101 | 2025-09-04 04:53:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f67ed338-fc03-3d32-9d8b-d6f7102089f3 | -6.3389 | -45.68027 | 2025-09-04 04:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ab4e1cf4-0aca-3e97-af00-aac4ecf7468a | -7.38841 | -49.39645 | 2025-09-04 04:53:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdcd7a36-89fd-3172-8cf5-2e8d21627c57 | -5.696 | -45.93936 | 2025-09-04 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cfd2d1ed-16bf-3a0f-ad6a-23ee1cfa7107 | -7.70824 | -50.29651 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3481f143-d4ed-3a1e-a4c3-7828d524290e | -8.02264 | -44.14822 | 2025-09-04 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a60e6fd0-c81a-38f8-a871-afe2d0e6e253 | -7.71187 | -50.24888 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README59.md)
