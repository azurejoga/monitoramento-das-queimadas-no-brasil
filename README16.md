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
| 8afcc35b-dd6b-3375-bf43-6a5161b14e8a | -6.43848 | -43.30842 | 2025-09-16 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| caf5aca3-13f6-3257-bf3d-120bc5b807bf | -10.74826 | -48.18085 | 2025-09-16 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44a694e8-e502-376f-a476-4a8c4dd704ff | -5.67221 | -43.49747 | 2025-09-16 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1531ebb4-f8b1-3ae7-968d-6f0aea5e10ce | -6.14432 | -41.18132 | 2025-09-16 04:02:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8e076dbc-7471-3d8e-9f55-75c98dfe704f | -5.78553 | -43.95046 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b6d75672-4263-3997-a518-8a40004be2a6 | -8.00653 | -45.66207 | 2025-09-16 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 474b0abc-c735-322b-a1ff-2be48feb0af5 | -10.72661 | -44.74603 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e482dd9b-ee80-3867-b953-82297eb72606 | -6.41381 | -44.36293 | 2025-09-16 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa5c6590-21ac-306c-a699-8d0af373c5f2 | -8.34043 | -44.7165 | 2025-09-16 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b5cdf7d6-2bf4-3fa8-866e-7d5dc2df3bfd | -7.04144 | -44.16077 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1420977d-2fee-38e4-9119-ac432e38010c | -7.83485 | -43.86056 | 2025-09-16 04:02:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 76b59783-19e1-32fa-9f5b-29ac4e0544f5 | -7.59692 | -42.25246 | 2025-09-16 04:02:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 56d19731-890d-3054-887b-8d8ca1bde12d | -11.45488 | -43.5588 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 859f7611-567b-38e8-b30e-d99c91140775 | -9.47729 | -54.44011 | 2025-09-16 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 58a1a96f-205f-3cd6-8491-29e8e3088488 | -6.35033 | -43.15897 | 2025-09-16 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c7797b74-cb1f-35d1-9a6b-28acd1bb6012 | -11.34617 | -47.36156 | 2025-09-16 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 330f92ad-a4ef-3431-8499-028d90b4cc85 | -6.18769 | -41.18494 | 2025-09-16 04:02:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 55c97710-a54d-347f-bd5b-c7c735f8ebaf | -6.16593 | -45.1142 | 2025-09-16 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4f1c754c-bb4d-36f0-b4cc-1f2b4e0c9683 | -10.42022 | -50.64396 | 2025-09-16 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d3fcaa7-fa2a-35c0-9a7d-f1a558110d4f | -5.91726 | -45.72661 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c15e491-4e84-33b0-8044-e1bc5e6176a1 | -11.39971 | -43.67789 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a41aed25-4bb2-3300-af92-e2588fb0c744 | -11.13316 | -45.34042 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 270e07f2-879a-3095-9d8d-e3389a177326 | -8.615 | -45.72632 | 2025-09-16 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c6fa121-8cb6-3a82-955e-78961abc5979 | -11.91259 | -46.74864 | 2025-09-16 04:02:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4edee2cf-713f-3150-a0dc-d3e3c05d806c | -5.77423 | -43.92497 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 053d42f2-749e-3dbb-a0df-ff2a1f7e7df6 | -10.16824 | -46.1397 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a979e95b-48db-3f95-a631-cd09a4922d59 | -8.9298 | -45.51914 | 2025-09-16 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28940907-b96a-3c47-a006-2b508b2e2fd3 | -5.75004 | -43.93068 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d4e7b0d-a115-3d47-ad8c-6844ba8a3fa4 | -10.03637 | -45.29303 | 2025-09-16 04:02:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9a26a3e-2a1e-3d37-865e-7f1dc64ad88b | -5.34841 | -44.82341 | 2025-09-16 04:02:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cbfa6088-6a28-3170-9a8c-81eb942cf2a7 | -6.44384 | -46.11216 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b872b436-d837-3248-9e45-8af573f44e76 | -6.35684 | -43.16425 | 2025-09-16 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6099c806-8707-33cc-8bd2-f211cc5c8e65 | -8.59514 | -46.34052 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 128b4f56-cab6-3846-b435-5fb3933dadbc | -8.36476 | -37.60562 | 2025-09-16 04:02:00 | NOAA-21 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4abb8765-1255-32eb-81be-783b00c51c45 | -10.47464 | -45.1622 | 2025-09-16 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cab50f1c-3b8d-3a7f-ac73-b61714f1bc46 | -10.71988 | -44.76378 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 193f8f73-76ee-34df-a33a-cad786bc5374 | -11.44859 | -43.55371 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e436b96b-e1f8-3317-8d47-b99e94b3d5b5 | -5.89142 | -45.75105 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eed2f1a6-ae45-3861-b34e-adb5ca72da08 | -11.46117 | -43.56385 | 2025-09-16 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9bb083a6-9699-3d01-9625-e978c1b15ea3 | -6.63472 | -44.73727 | 2025-09-16 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9257ce86-e456-363a-9d04-9d34d7700551 | -7.71602 | -45.30466 | 2025-09-16 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a6137ce4-c40b-3523-8c4c-1c4730b34a36 | -7.6325 | -46.55401 | 2025-09-16 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f70820bd-f11c-39bf-8203-597fd1cfbc38 | -7.85165 | -43.84991 | 2025-09-16 04:02:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc4ac160-ec9c-31d0-aec5-a9174cd07b67 | -6.96731 | -44.44049 | 2025-09-16 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d9f75c1c-f785-3bf2-836d-a4c873fc1f0d | -5.66908 | -45.06225 | 2025-09-16 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb161c47-ce23-3bc0-85cf-b2d533218ba1 | -5.91207 | -42.75027 | 2025-09-16 04:02:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e9f9a0e3-0e5b-3281-ac35-c66c36d3a9a9 | -8.15784 | -43.67518 | 2025-09-16 04:02:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1ede2c7f-0ebc-3a59-a826-4ac81c1466f3 | -5.78039 | -45.89378 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef47ad99-f5cb-339a-a56c-10e691470594 | -7.316 | -43.95649 | 2025-09-16 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0b4b2a6e-15a4-347d-bcb1-bd4962aae01a | -6.1415 | -41.1991 | 2025-09-16 04:02:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9aca5c73-2af9-3425-a2fa-13237bcc0a82 | -11.11633 | -45.34742 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| feb9bc3b-b8d4-3e63-ab33-3c652dbc05d4 | -5.73949 | -43.92422 | 2025-09-16 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e5b7dd0b-be57-35c6-84f7-71a50f809d42 | -10.23163 | -46.7401 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d170b3c-4ee2-3f93-acf6-c9d123003115 | -11.1117 | -45.35161 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cb11b840-a282-37f9-8c17-306493bd9d21 | -8.96033 | -45.76285 | 2025-09-16 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e31e9858-0eea-3377-953e-b99e7fcb3360 | -6.17736 | -45.14572 | 2025-09-16 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c054f6cb-3ef6-3fd6-a3d9-13bf8f146314 | -5.99813 | -43.70224 | 2025-09-16 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8a7a74c-934d-3801-a47f-a3bd89c68f46 | -7.98803 | -45.64801 | 2025-09-16 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d9ed823-a453-38d7-9bd6-7e731e653196 | -7.15044 | -44.32351 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d22b2196-502b-3937-9e01-ff3176069790 | -7.69143 | -44.66631 | 2025-09-16 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8767bcbb-0132-3d01-903e-f2a006f1d15b | -7.66589 | -45.14998 | 2025-09-16 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f92ba3df-00d2-36f9-961b-df5c71c4a5f8 | -12.11195 | -44.83841 | 2025-09-16 04:02:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 43d4dd84-e7ea-36d3-b4bc-4f5f4d0e8e83 | -5.98577 | -45.83482 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 18f1d41f-8ff1-334e-8814-53eba23e369e | -7.70715 | -49.55735 | 2025-09-16 04:02:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 764b2df7-62e5-3bda-a368-7f4620907b5d | -8.20935 | -45.55374 | 2025-09-16 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aad3120f-5661-3899-abac-75cb4e2fff4f | -7.39604 | -50.00108 | 2025-09-16 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 56d42eca-00f1-3418-9953-a3bea07d4a05 | -6.35325 | -43.16368 | 2025-09-16 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ff8cfe3b-97be-3d25-bdb5-2c5c3b7a1a8a | -5.80475 | -44.86657 | 2025-09-16 04:02:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8475ef16-c32e-3c18-b32e-c272e0f688cf | -8.66462 | -46.36758 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| add149f3-c214-332e-af64-fd30be974df0 | -7.83847 | -46.11287 | 2025-09-16 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e803f18b-4e97-30ff-85ce-1b41d18bffc0 | -6.4421 | -43.30895 | 2025-09-16 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1f0db32b-d1b4-33e2-bcb6-2aede274a7f2 | -10.72408 | -44.7532 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c09572b4-d80c-3f63-bbb9-f542bf8d99be | -8.00939 | -45.66987 | 2025-09-16 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 73dfe138-f64d-353d-ae6e-016d548197db | -9.85868 | -46.45509 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0491b83c-cf65-330e-8839-0a930e70bbe9 | -6.40767 | -43.33788 | 2025-09-16 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3a44a820-7012-396f-a853-72475cba62c1 | -12.07008 | -43.47017 | 2025-09-16 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5fc4a4af-482c-370d-b3be-574612f69a0a | -6.46443 | -46.01466 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b38782c-5fe2-38ee-aaef-c9addf2a9b94 | -6.25935 | -43.46393 | 2025-09-16 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ca17e81d-fced-3e5c-b8f0-cc02e6ce35e4 | -6.17401 | -45.11549 | 2025-09-16 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bbea5d55-5550-32c3-a3ae-952c38cd66b4 | -7.99491 | -45.65667 | 2025-09-16 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 4b23228e-f1b2-3819-8c7d-87d9d723672b | -6.18152 | -41.20211 | 2025-09-16 04:02:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2fa7ed9b-9821-3ec9-80da-f0863135891d | -11.43302 | -46.93747 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f9841fe1-95d3-3dfa-9beb-6708ef9304fe | -8.03424 | -49.83723 | 2025-09-16 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc90957e-fb45-3771-be8d-897ca095472d | -10.71587 | -44.75665 | 2025-09-16 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| affcddd0-3e10-3cf6-bca3-14ecf2707218 | -12.17626 | -44.10136 | 2025-09-16 04:02:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7125c6c8-050b-3972-bd38-6cf2771f2a8b | -8.0889 | -50.16256 | 2025-09-16 04:02:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bb18a247-df2e-330e-92d0-18335b3ae9c4 | -6.40836 | -43.33364 | 2025-09-16 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4604ec16-916d-3601-8988-231747f011b2 | -4.79563 | -49.54631 | 2025-09-16 04:02:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da5779e9-818b-359f-9fe6-c56a935a9f1e | -10.95683 | -49.57199 | 2025-09-16 04:02:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 821b80c4-6bf8-30b2-837f-da4e9c1b89e5 | -6.66841 | -45.54101 | 2025-09-16 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| efec0e8b-ea4d-34a7-88c9-062ec932fed6 | -9.87252 | -46.44922 | 2025-09-16 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5ad6f53e-0977-3bd5-b3e0-a29e3b4f47b1 | -7.05198 | -44.16706 | 2025-09-16 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 07ca5758-7255-3774-9e69-4ce91ef62ccf | -7.00329 | -44.57931 | 2025-09-16 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 83117b3d-7d65-3d29-9e71-c3c457ca4fb4 | -6.16386 | -45.99637 | 2025-09-16 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b9919da1-c129-3a1d-a028-cc38d459e824 | -10.71564 | -46.50771 | 2025-09-16 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 64cb89c9-974a-321d-8fb5-6ae8b9517c46 | -6.29191 | -42.39503 | 2025-09-16 04:02:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e92e32eb-9890-3d63-b193-218e2ab1e79c | -11.71874 | -46.87575 | 2025-09-16 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7867779a-770b-3cb2-877e-038a9150cf4d | -6.40997 | -44.36228 | 2025-09-16 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0a2ad65-25bf-3498-8d1e-c2033e6a52e7 | -10.74367 | -48.18002 | 2025-09-16 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c27ca033-3b09-3a56-a2b1-dbcc12cff1e6 | -11.02455 | -45.06506 | 2025-09-16 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |


[Clique aqui para ver as próximas entradas](README17.md)
