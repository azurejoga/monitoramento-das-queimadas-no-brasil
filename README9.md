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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c6fd1e9-d841-318c-9827-013460b5d5f5 | -5.3795 | -42.86031 | 2026-09-04 03:42:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4b6a5cd4-7977-3f6b-b512-f2bfa64202f7 | -5.80119 | -43.65042 | 2026-09-04 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a2980a29-178f-39b7-9e74-7e8566f11fed | -3.7735 | -47.55211 | 2026-09-04 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b6b53fa8-0b84-3427-b735-e4566446d4f2 | -3.9369 | -42.98952 | 2026-09-04 03:42:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 81bb59cf-6ba9-330a-999b-6627b0ac333a | -4.90462 | -43.47099 | 2026-09-04 03:42:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bb98f4be-55aa-36dd-ad61-a141c5ea4eb2 | -3.2475 | -47.2501 | 2026-09-04 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| acff4eb0-a504-3cab-9693-7c0eceecc650 | -3.42917 | -43.20736 | 2026-09-04 03:42:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6643745a-b2e0-3a24-ac19-486c35626fed | -5.38435 | -42.8611 | 2026-09-04 03:42:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| ded860d1-4598-372a-8ab1-e9486c223fd6 | -4.45238 | -40.20823 | 2026-09-04 03:42:00 | NOAA-21 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 59a6132d-16cd-37d1-a9ff-bb10323512ad | -0.92818 | -47.19664 | 2026-09-04 03:42:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 83152e3e-ddf1-36cb-b98d-9250c00d4658 | -5.55053 | -43.42852 | 2026-09-04 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6b29cb20-07bd-3e56-b6e9-629d11af415c | -0.92921 | -47.19023 | 2026-09-04 03:42:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e1ecae04-7790-393e-b3ea-ec66b147e9e1 | -5.8017 | -43.64743 | 2026-09-04 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 97c66925-a755-32e7-bdeb-4a7149aba939 | -4.36692 | -47.77914 | 2026-09-04 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| d00c2588-195c-33ed-985a-749697dff3d5 | -3.59369 | -43.01176 | 2026-09-04 03:42:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ebf75f0d-8c7c-3bd0-84f4-e80ee225f3b4 | -5.80422 | -43.63263 | 2026-09-04 03:42:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8f51e560-43e4-38ee-8b29-318cb4a76ef7 | -3.42966 | -43.20433 | 2026-09-04 03:42:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0bb0213-f431-3c2e-8e30-a669364e7826 | -3.89791 | -38.65041 | 2026-09-04 03:42:00 | NOAA-21 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8c1ce3a1-6195-3a38-ab66-3c01ca73f233 | -4.91705 | -40.66513 | 2026-09-04 03:42:00 | NOAA-21 | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 21a1e8f5-deef-3ead-959f-cacd4c241d75 | -5.8778 | -45.56954 | 2026-09-04 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16dfc21e-8892-3baf-81ee-4fe7812562f7 | -5.29957 | -43.06376 | 2026-09-04 03:42:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c1eb4d42-5a00-3216-8f18-88f1d699c941 | -0.92999 | -47.19112 | 2026-09-04 03:42:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 47a33f53-700a-385a-8735-b9a7620e0c4f | -5.20853 | -38.02982 | 2026-09-04 03:42:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f4755d5a-b050-315f-bc8e-d8875059681a | -4.49548 | -42.55827 | 2026-09-04 03:42:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ca3803d6-40e4-3b9d-9e2d-f61761e40f71 | -3.43226 | -43.20447 | 2026-09-04 03:42:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 972b0490-2369-3d21-a498-e36c9cacad8a | -4.368 | -47.77316 | 2026-09-04 03:42:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 2cbecba5-acf0-30e9-a868-ebb3ab333d37 | -3.24085 | -47.24903 | 2026-09-04 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5725ea85-b72a-35ed-ab1b-78f8dbd4dbeb | -11.27787 | -45.72123 | 2026-09-04 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9b80e6f1-d6e7-388d-ab0f-0c4fe857d63a | -13.40535 | -41.88743 | 2026-09-04 03:45:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 6d4abe7c-cb59-3778-9148-cce83388dfc7 | -9.57773 | -40.34313 | 2026-09-04 03:45:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 43.3 |
| dcdf2dab-634b-33bf-810b-b37223c73b3c | -13.40913 | -43.87534 | 2026-09-04 03:45:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| dd67265b-b8a5-3643-9b5e-0440d3e808f4 | -12.99648 | -44.11155 | 2026-09-04 03:45:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47620852-baec-39a0-b354-ed9cb7752201 | -13.41365 | -43.87617 | 2026-09-04 03:45:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f518ddf1-7dcf-3fe0-96f9-bbf78af9ec89 | -11.35797 | -41.60008 | 2026-09-04 03:45:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c72f9771-a5e5-359b-a991-a50612707a25 | -6.35376 | -46.11234 | 2026-09-04 03:45:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ae5d30d-03d0-3fc8-8d42-1e5c0a6324f6 | -7.45612 | -46.14511 | 2026-09-04 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a47f38ac-304a-3e53-bb60-382b3a519cbd | -9.58075 | -40.34858 | 2026-09-04 03:45:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 43.3 |
| dbc0e757-770f-38e5-a722-8c9cc805e3b3 | -6.31159 | -46.08818 | 2026-09-04 03:45:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 40d14ff2-2f0a-35f9-979a-9e16bbce31b0 | -7.4559 | -46.144 | 2026-09-04 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78ec9cfa-dad5-3a89-9fc4-eff0e809f99b | -9.58238 | -40.33899 | 2026-09-04 03:45:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 2403dbd8-8d05-3608-a441-de156af26d95 | -8.84927 | -36.86933 | 2026-09-04 03:45:00 | NOAA-21 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f1cc31cb-c6c2-3b2e-8a01-49e006d02d48 | -10.2669 | -50.03426 | 2026-09-04 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6d04c84d-9e25-341d-ad07-f69673d43bc7 | -10.25852 | -50.03964 | 2026-09-04 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 41ab4b17-ac62-3e1d-8f75-775df0223415 | -11.54256 | -50.49983 | 2026-09-04 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f68d3dc0-6600-3cde-829f-9fd67a664339 | -6.8364 | -41.66963 | 2026-09-04 03:45:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7c06ba7a-98bf-390a-9d97-16ec8c7f9dfe | -8.82478 | -44.55072 | 2026-09-04 03:45:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ab029e2b-880b-3289-a835-bddbdfe6c112 | -6.31078 | -46.09269 | 2026-09-04 03:45:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5116633a-42ac-39ba-94a8-b8a19b81fa06 | -7.4602 | -46.15326 | 2026-09-04 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c6201cf-acb2-3cbb-a8b4-efe554a746b8 | -6.35578 | -46.11376 | 2026-09-04 03:45:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0a92e721-e439-3abd-a2f8-03e69dbead98 | -7.45515 | -46.14805 | 2026-09-04 03:45:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3088766-0b15-3197-b9d6-7f0eb5a88328 | -14.09295 | -42.57369 | 2026-09-04 03:45:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 389bc410-e624-311b-82eb-ac1ae8ebbcb9 | -10.63463 | -50.40157 | 2026-09-04 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 332225f1-5481-3be8-9d99-7bb31e998f5e | -14.09706 | -42.57439 | 2026-09-04 03:45:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 20636150-9ac4-3fe0-b740-0eb54a2c0b6a | -10.63754 | -50.38747 | 2026-09-04 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| cf17f422-bfc3-3a2f-b537-fb52f3710a30 | -10.63608 | -50.39453 | 2026-09-04 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 900779ea-a019-3201-8389-6fbcc4014d8e | -13.40203 | -41.88297 | 2026-09-04 03:45:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| aba74f22-6777-3270-a50e-f3b271abb02d | -10.64463 | -50.38891 | 2026-09-04 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 37d1893e-e730-3355-b212-e6c5cb57273b | -9.01795 | -40.99823 | 2026-09-04 03:45:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| a0da7330-9f1f-3e58-b2e4-e14bc4501486 | -11.59047 | -50.48104 | 2026-09-04 03:45:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| d266cfe9-9535-3d13-8ff2-aec46b735955 | -9.58156 | -40.34378 | 2026-09-04 03:45:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 43.3 |
| de40f763-682f-3017-90eb-103341884dd4 | -8.81967 | -44.54977 | 2026-09-04 03:45:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 38a6cbac-98fc-3aad-9005-6fc6a5f47be1 | -10.25992 | -50.03284 | 2026-09-04 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| 3f38086b-7d81-3228-83f7-70cecddd91c1 | -11.5191 | -46.89862 | 2026-09-04 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc1225f3-20c9-327f-8bdc-872faca31174 | -10.629 | -50.39305 | 2026-09-04 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 5e9bb222-5ea7-3af1-a09f-d19bc763a56c | -9.01392 | -40.99754 | 2026-09-04 03:45:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| f782aa5b-a2e3-3068-9b12-016bc03a933a | -9.0099 | -40.99685 | 2026-09-04 03:45:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 78274742-fba6-3f26-83bc-d27c5923bd63 | -11.04263 | -44.34518 | 2026-09-04 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| f6c1e2b6-ebb5-3c7e-959a-3030710e76a2 | -12.99559 | -44.11646 | 2026-09-04 03:45:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c1ca0d5e-652e-30c8-8409-e6d2887c5d87 | -9.57855 | -40.33834 | 2026-09-04 03:45:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 12.2 |
| b8f161a3-1033-3f15-a4a2-0c021b7f1cd9 | -11.52483 | -49.20847 | 2026-09-04 03:45:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bdcde374-360c-3e51-a8f6-223ac17fa514 | -11.27246 | -45.72082 | 2026-09-04 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f982b2c9-b41b-33c3-adbc-b3f763ca6b7f | -13.40141 | -41.88656 | 2026-09-04 03:45:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1dc11e39-0299-3ea4-aa23-4f12bd17ceea | -9.5739 | -40.34248 | 2026-09-04 03:45:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4adbef69-e4c5-3b8e-bbdb-5a575b7ee38c | -10.64317 | -50.39598 | 2026-09-04 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 7d04c9a5-b0d1-3c13-a537-5cc3b669d43d | -10.26174 | -50.03327 | 2026-09-04 03:45:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 32.9 |
| dc4c87c6-a7db-3566-b116-d23143d7fa12 | -6.83134 | -41.67302 | 2026-09-04 03:45:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 3719f1ee-5389-3630-9530-b717a24ce686 | -6.83207 | -41.66874 | 2026-09-04 03:45:00 | NOAA-21 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 585b15c2-1ff0-3910-b6d9-b2b3d536f7b0 | -11.27117 | -45.7277 | 2026-09-04 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43955ba0-5583-3cad-aeb1-f30182cd1210 | -11.51346 | -46.89731 | 2026-09-04 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e10ccd55-088b-3e1a-a8be-4ec3d3d8cd4d | -7.25017 | -42.76978 | 2026-09-04 03:45:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| c94d8375-f7c0-3e6a-a9c1-e3ea6eb55456 | -10.48359 | -39.6499 | 2026-09-04 03:45:00 | NOAA-21 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e8384645-0441-33c5-b673-17be4b95589f | -11.54958 | -50.5013 | 2026-09-04 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3c84e822-07e9-362d-8ad0-013ddf9a9c77 | -8.31552 | -37.26791 | 2026-09-04 03:45:00 | NOAA-21 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d1a8efa0-f428-3e96-9614-6e9c095470b0 | -13.4008 | -41.8901 | 2026-09-04 03:45:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d7f53d38-5dc6-3092-bd37-66e42d24a53a | -11.51704 | -46.89904 | 2026-09-04 03:45:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db4b33bd-69ea-3d09-8289-3a601a525bad | -13.41278 | -43.88083 | 2026-09-04 03:45:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5fc2448-7103-3b3c-87e0-0bb5c8f30ce5 | -9.57692 | -40.34793 | 2026-09-04 03:45:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 43.3 |
| 2ea5fb0f-6ad5-32a0-82fe-d6e63846a17b | -18.13614 | -51.80219 | 2026-09-04 03:47:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 521257f4-4ca3-307a-973c-80ea1b5d51d5 | -14.79887 | -47.13765 | 2026-09-04 03:47:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 272704bd-d687-3d8c-8984-6ca11a4e0f3e | -19.31569 | -47.0916 | 2026-09-04 03:47:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00ad9b37-82cd-33b7-843e-e70664f3343e | -15.77077 | -43.31641 | 2026-09-04 03:47:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd7484dc-d6aa-3c2f-a0d2-40535cfe585d | -18.80388 | -47.55285 | 2026-09-04 03:47:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86016438-ae3c-3f77-a2fc-b45b5056ede9 | -15.84072 | -46.02701 | 2026-09-04 03:47:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bae32705-493d-3e4d-8968-3ea0067a4a1f | -19.62654 | -46.96832 | 2026-09-04 03:47:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c070858-b69b-3371-bbd7-14980108661c | -18.73639 | -48.91643 | 2026-09-04 03:47:00 | NOAA-21 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e40de31d-b4db-3845-a353-35e6364b40cb | -13.58496 | -47.87894 | 2026-09-04 03:47:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 36d80006-7430-3e05-9c23-bd7a92a24447 | -14.79959 | -47.13405 | 2026-09-04 03:47:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 94944080-e1d9-3576-b111-6cfd4b4841f5 | -17.31634 | -49.61596 | 2026-09-04 03:47:00 | NOAA-21 | PONTALINA | GOIÁS | Brasil | 5217708 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3363447f-6995-3605-803b-e8190accea3c | -15.83254 | -46.01609 | 2026-09-04 03:47:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8d165ad0-29cf-3f0f-a912-a0b811d17718 | -14.19431 | -51.24418 | 2026-09-04 03:47:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README10.md)
