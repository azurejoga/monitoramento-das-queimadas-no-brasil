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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54b0bb6a-f9e5-3b38-9cb9-416c12944e81 | -5.19916 | -45.48228 | 2025-07-26 04:25:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6897b541-2154-3613-8e30-ab701a2bfa26 | -6.8726 | -43.67513 | 2025-07-26 04:25:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4f71907-f80f-3dc6-8bc3-cb0a45657b28 | -6.65708 | -58.83903 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 2b702f73-7426-32d6-9d09-0e8cf5aafbcc | -10.35329 | -46.64245 | 2025-07-26 04:25:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7075aec-e9a4-3ac9-801e-0a66a7ed1395 | -6.10816 | -57.72425 | 2025-07-26 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb0b6814-8850-3aa8-92d5-69d0f64c2d03 | -3.75209 | -49.04821 | 2025-07-26 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d35701c-4db4-3322-9e18-0bb15003ef73 | -6.67344 | -58.85941 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 4c4a6564-e601-367a-a7f7-7b1f3f5c0da7 | -6.65683 | -43.04839 | 2025-07-26 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b95e6c47-5eb8-3478-83bb-c8b8debba83f | -6.1534 | -42.59332 | 2025-07-26 04:25:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 0c784c8e-ad37-37e3-88ee-2b6ce252f898 | -6.22469 | -44.52374 | 2025-07-26 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 05f2a7c9-2ab5-318a-bd60-06c1c1d1a029 | -6.65161 | -58.83236 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 0995e150-049d-35f6-b129-54e98d518e79 | -8.56728 | -47.24331 | 2025-07-26 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c518a6e8-2ddf-31f1-a08a-a263b2c5accd | -13.24461 | -51.14948 | 2025-07-26 04:27:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dbb34733-2fea-3b57-b3cc-2c4e4729421d | -14.13641 | -45.28222 | 2025-07-26 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f35a44cc-f220-37f7-8170-7c79d6715a3b | -12.68478 | -46.99728 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 20eca741-a6a1-3492-bc3c-fc7b3570f33b | -13.70236 | -45.68441 | 2025-07-26 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2ea1172b-d045-3c5f-8d17-a8e68eb124f9 | -10.29597 | -57.05438 | 2025-07-26 04:27:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2afdf758-3bf1-3a52-a046-c7e57426d7ee | -14.37507 | -50.32969 | 2025-07-26 04:27:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55ec4d58-e374-34ac-a2a2-c0fde3cfc72c | -18.25144 | -44.78868 | 2025-07-26 04:27:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 0e7f8175-d29c-384d-8f48-c5ba18b611c3 | -16.09918 | -42.27613 | 2025-07-26 04:27:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 36bf4dc8-e51f-3912-8943-68dc5b378c22 | -15.78609 | -41.33201 | 2025-07-26 04:27:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a517dd0a-b8f7-34e5-b4a5-205e933a483c | -13.10036 | -47.33702 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6675dceb-6085-38fb-8ec3-0930d5757b58 | -13.23743 | -51.1482 | 2025-07-26 04:27:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 76c9ce2d-0862-3dd7-aab1-438c67acaff1 | -13.11804 | -47.33259 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcbf6984-1786-3021-bca6-eca4c71192c4 | -11.3151 | -55.21798 | 2025-07-26 04:27:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1748040d-08cd-31c1-975c-16a049d39d41 | -14.93736 | -46.95001 | 2025-07-26 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 578edc17-4b59-372a-9ac7-411962104330 | -13.11748 | -47.33619 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 78ed3fd4-a651-3f18-8082-156bbd62803c | -16.12397 | -47.40538 | 2025-07-26 04:27:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de37fde1-b1df-38db-a783-d83f364fd9c6 | -13.69715 | -45.69567 | 2025-07-26 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ff685ea3-c3fa-3ee1-a3a2-21589722a236 | -14.94461 | -46.94772 | 2025-07-26 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3c5bb337-12df-309e-b8fa-eb1c7a0c5170 | -13.23858 | -51.13211 | 2025-07-26 04:27:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 10d4e96a-e43e-31a5-a9bd-db3128492499 | -15.6277 | -48.54715 | 2025-07-26 04:27:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 121770bd-fbfe-3cd1-af36-e82da31dae62 | -13.12634 | -47.32283 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 711d26e4-8a57-3013-8025-c9bfef814484 | -12.71465 | -46.27522 | 2025-07-26 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 2bec2738-23ce-32d5-87c9-118ed4c25276 | -13.10261 | -47.36634 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42cc2c70-d09a-3e56-9d2e-0203a5c13c22 | -11.73738 | -48.18455 | 2025-07-26 04:27:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4b7afd83-92da-37df-853a-82c1a5fb5f14 | -14.93791 | -46.94635 | 2025-07-26 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 192f71a7-8a5b-3fdc-bcb3-30cf91d1e2d1 | -13.09448 | -47.35436 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b38fd679-749b-3f71-a44d-b53b86d811e3 | -14.96426 | -46.97729 | 2025-07-26 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5f624011-0808-368b-9714-840ebe2e1654 | -16.12062 | -47.40483 | 2025-07-26 04:27:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bc37e9c3-c7ef-34c0-935e-e31cf609f1a1 | -13.69308 | -45.67492 | 2025-07-26 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2886ee29-8f8f-3b5d-a02c-b923573a18be | -13.64023 | -45.70741 | 2025-07-26 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62628e96-e571-3cbe-92f5-cba996056952 | -14.9435 | -46.95506 | 2025-07-26 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a25407e4-ee3e-351f-9e88-36886999724f | -15.78325 | -41.32375 | 2025-07-26 04:27:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| de7a5c7c-3e2c-39ab-a1bf-fd1715a38727 | -13.70003 | -45.676 | 2025-07-26 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dfe0a534-4fb5-3cb6-a119-29e6aa5fab45 | -14.21222 | -43.94898 | 2025-07-26 04:27:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4858fc9d-fffd-343f-9a42-6b630efc46f0 | -15.16341 | -49.5758 | 2025-07-26 04:27:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0de5140-b2ce-3775-be75-1f26d236bce0 | -13.24534 | -51.14525 | 2025-07-26 04:27:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02276cb4-2a08-3881-a1a5-f396cf1f1ef7 | -14.93011 | -46.97521 | 2025-07-26 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4d978d00-6a29-3a71-bf95-065b16ec1fda | -10.8478 | -54.03633 | 2025-07-26 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9e6362d2-3382-3e24-9201-4448687bb3cf | -13.2367 | -51.15242 | 2025-07-26 04:27:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b7f7b23d-f23f-329a-9024-87d3c1ee92fa | -11.92546 | -44.55103 | 2025-07-26 04:27:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6471acc6-3f81-3e12-8da1-f86bd8a9e6db | -15.7872 | -41.32961 | 2025-07-26 04:27:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 87ad9252-7e85-388e-8e7c-efb7928c45e1 | -13.24388 | -51.1537 | 2025-07-26 04:27:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 57bb7abd-c884-346b-92fd-be31fa52228d | -13.09227 | -47.34671 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| acb8290d-5d2c-3ec8-9e9e-8692b12129d7 | -13.69656 | -45.67546 | 2025-07-26 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 990a372b-b887-3d79-baab-2c0615c847b2 | -11.92906 | -44.55157 | 2025-07-26 04:27:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 472d7f3b-a974-374a-b57c-81f7e71f2082 | -18.24696 | -44.79306 | 2025-07-26 04:27:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 45.3 |
| e8adc71d-8f0c-379a-90fe-7cde0525b4ee | -15.78259 | -41.32887 | 2025-07-26 04:27:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 01258787-4bd9-3d95-bd07-6f3e48c5126f | -13.11693 | -47.33974 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 55fc991a-2891-3de7-82f1-d8abe008e31c | -13.24316 | -51.15792 | 2025-07-26 04:27:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 32f68323-26ca-3972-afb2-97b948f28527 | -13.69888 | -45.68387 | 2025-07-26 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72215883-1879-3f54-b291-6ea8855a85e4 | -13.69018 | -45.67044 | 2025-07-26 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c45028f5-8b1a-3053-a6d9-b661ce830048 | -12.68866 | -46.99428 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 720eca82-190f-3def-bdf2-594d0b3724c6 | -14.21604 | -43.94954 | 2025-07-26 04:27:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66eaa131-75d8-3434-a51c-50a4d92a414b | -14.37229 | -50.32522 | 2025-07-26 04:27:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 558e470c-ef3e-311c-8601-3328a6b129fe | -13.09283 | -47.34316 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b74298a-1039-3ce4-8e3d-043de223ea3a | -14.95578 | -46.96501 | 2025-07-26 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 048cd7ff-2ea6-3049-8ed1-7c170de5667e | -13.18227 | -42.32488 | 2025-07-26 04:27:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 81585cf5-e9c1-3652-9273-b7952f5e643f | -14.934 | -46.94942 | 2025-07-26 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8170c899-5fff-3769-b371-a0fdc1c23fec | -13.11142 | -47.35336 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0810443-f14d-32d9-b357-20c97f8fb9e5 | -17.04464 | -45.67047 | 2025-07-26 04:27:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38cbf695-16c9-3789-8017-60d9b6469a55 | -13.6414 | -45.69958 | 2025-07-26 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 018fc5d7-c25a-3f4e-9994-4fdbbf516102 | -18.25079 | -44.79362 | 2025-07-26 04:27:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 35.3 |
| c9314ba4-c2bd-381c-a9f7-6668e32c2067 | -13.11195 | -47.32799 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a064983e-8fc6-3914-8925-ec05d27350cc | -13.96901 | -49.72966 | 2025-07-26 04:27:00 | NOAA-20 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a0818b88-04fd-3b41-9216-34723ca1d096 | -13.67479 | -44.22334 | 2025-07-26 04:27:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ac0978c-db03-37a7-9e22-6b84d62c263e | -12.68756 | -47.00139 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f50a9181-7baa-3a22-bfac-979d4467a4a3 | -11.74069 | -48.1851 | 2025-07-26 04:27:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3b7c00c5-bf2c-3a06-b23c-e8ebba119a22 | -13.12247 | -47.32591 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce8b37b5-47a7-38f8-af8f-7394d820e49c | -15.03681 | -47.10138 | 2025-07-26 04:27:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2497afd8-945b-3f5e-bbdd-d4ab0cdb66f5 | -13.11529 | -47.35037 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f9de28f-bd21-3c03-ab35-375e380f2b57 | -13.6954 | -45.68333 | 2025-07-26 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f49311f7-1313-3ddb-bbda-0d6d1eb83d9a | -13.22137 | -51.14645 | 2025-07-26 04:27:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 56277d1f-303d-3c9d-99e9-578d0fc8b2a7 | -18.24761 | -44.78813 | 2025-07-26 04:27:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 45.3 |
| f5d6573d-ebfc-3086-afec-6e929a7e9232 | -15.76119 | -47.77622 | 2025-07-26 04:27:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8756369-13c0-3b7c-a578-330a637d88a1 | -14.04535 | -47.91862 | 2025-07-26 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 18304655-d81c-3d62-94ce-5f031d856058 | -13.11197 | -47.34983 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0212ec03-b816-3654-a363-00d158188138 | -12.70142 | -46.99998 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f0adb40a-5222-3c3f-aac2-51f6bd5b5a96 | -11.74013 | -48.18862 | 2025-07-26 04:27:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f9252690-fbd1-373c-b2d4-fff2ab4b11e1 | -13.69365 | -45.67098 | 2025-07-26 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1f2b2961-ff5d-3ace-b99e-3f7ae8af2598 | -13.24116 | -40.5996 | 2025-07-26 04:27:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 58459529-dede-3d53-87ea-27bdf3f468d3 | -13.11307 | -47.34275 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 92762138-ace1-362c-aba2-d6b94b59639c | -15.72895 | -41.15313 | 2025-07-26 04:27:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| eade7c15-4b35-3c43-aef0-0a4538b1ae62 | -16.09482 | -42.27554 | 2025-07-26 04:27:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 03930bcd-3e17-35de-83c2-7dfd41d1d699 | -14.93064 | -46.94886 | 2025-07-26 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| aa394085-127f-3133-91a6-9da342137ead | -13.12136 | -47.33311 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 891404a6-a20c-35c0-87da-3de9afcf316f | -14.37164 | -50.32909 | 2025-07-26 04:27:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0004887d-331e-30c6-8d56-6e631ccc32a3 | -13.10702 | -47.35984 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 270137bb-1cbf-353f-bb43-6b0a27374ed2 | -13.09117 | -47.35379 | 2025-07-26 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README21.md)
