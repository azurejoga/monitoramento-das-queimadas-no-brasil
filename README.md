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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed51acb5-1272-323a-9c34-249e8d4d0961 | -10.9922 | -44.7155 | 2025-03-16 00:09:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 23e28fd1-3760-31e2-bd1f-2f7bf400a777 | -10.9824 | -44.7178 | 2025-03-16 00:09:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 277cd0ab-3928-3ed7-9642-a66e1822ea6d | -10.5825 | -45.138901 | 2025-03-16 00:09:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 29203114-4a1d-3cc3-b28a-9a365d3d2511 | -11.0959 | -40.197899 | 2025-03-16 00:09:00 | METOP-B | CALDEIRÃO GRANDE | BAHIA | Brasil | 2905503 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 58b2139a-8e8c-3a39-94d9-ec6f89ea6349 | -10.984 | -44.7248 | 2025-03-16 00:09:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ed858a09-2f41-3eaf-9644-d52c93527802 | -10.5794 | -45.125 | 2025-03-16 00:09:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 17ae0fa0-e608-3c01-b12d-4890dcb345e9 | -6.201 | -48.023499 | 2025-03-16 00:09:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5fe12c81-6339-3466-8021-b1c53572d7e4 | -10.9938 | -44.7225 | 2025-03-16 00:09:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bdb74df3-ff6a-37b0-992d-1e9eeb125b58 | -10.8775 | -44.161999 | 2025-03-16 00:09:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cc6bb21e-1b18-38e5-adff-9d05bad1f331 | -10.5809 | -45.132 | 2025-03-16 00:09:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5951ab85-2414-3dd4-a7e4-ae92316f8ad4 | -6.2026 | -48.030701 | 2025-03-16 00:09:00 | METOP-B | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5620aa02-5f96-3704-930e-33a204866f8f | -10.8873 | -44.159801 | 2025-03-16 00:09:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7d443c9b-7ab8-3258-af85-c22313422984 | -15.8905 | -45.996899 | 2025-03-16 00:13:00 | METOP-B | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9ae2f530-6f83-3e21-8883-3989a94a8919 | -15.8077 | -41.325802 | 2025-03-16 00:13:00 | METOP-B | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b8464130-fbee-357a-b23b-5fdd4c4f3f13 | -13.9012 | -44.272999 | 2025-03-16 00:13:00 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3ec865f7-54a8-321d-97d2-23a44ab96b60 | -17.0259 | -41.055 | 2025-03-16 00:13:00 | METOP-B | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 037452be-f698-3154-85c5-515bb131d030 | -15.4812 | -39.059799 | 2025-03-16 00:13:00 | METOP-B | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 426dee39-03be-385d-9e71-04c8c7318a5b | -14.5385 | -45.486198 | 2025-03-16 00:13:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d786da97-9899-32f5-9503-1e95cd27e1b3 | -13.4365 | -41.304798 | 2025-03-16 00:13:00 | METOP-B | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 250126ac-67d2-331f-a73a-72b8a32ee700 | -15.8097 | -41.334099 | 2025-03-16 00:13:00 | METOP-B | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 483e84d9-abb6-3f46-b528-d2257a6b1333 | -13.4267 | -41.307201 | 2025-03-16 00:13:00 | METOP-B | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 55d28e4f-98aa-3ad4-962e-a017e4c25958 | -16.415001 | -43.765999 | 2025-03-16 00:13:00 | METOP-B | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 2c436cb5-99fd-36f9-8f64-79ac7a2564df | -15.8889 | -45.9893 | 2025-03-16 00:13:00 | METOP-B | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a1ed940b-c513-3349-ba64-3850cb1b9672 | -15.8414 | -40.723202 | 2025-03-16 00:13:00 | METOP-B | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3099f8a4-bf18-3b9e-b449-f8e116431fa7 | -17.7157 | -54.080101 | 2025-03-16 01:04:00 | METOP-C | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 89eb658c-b44f-3c65-9c21-2c2ce6c35f5d | -20.4181 | -51.356998 | 2025-03-16 01:04:00 | METOP-C | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 707ff88b-0494-3b2b-9949-b775d8f52911 | -19.493299 | -54.8493 | 2025-03-16 01:04:00 | METOP-C | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b2fd5fd7-17f6-32e8-b2a6-78d9bac702f2 | -15.6406 | -57.305801 | 2025-03-16 01:04:00 | METOP-C | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cc00668d-58fa-334f-a064-6ace5a101b2a | -21.89737 | -55.37607 | 2025-03-16 01:15:00 | TERRA_M-M | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7b2c97bf-0a86-33c4-a5b2-ad0e290288b9 | -17.71462 | -54.08191 | 2025-03-16 01:17:00 | TERRA_M-M | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 1abf3a6d-1e22-3379-b6ec-68ff482614cb | -20.40958 | -51.35458 | 2025-03-16 01:17:00 | TERRA_M-M | ILHA SOLTEIRA | SÃO PAULO | Brasil | 3520442 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| c649a9b3-7ac2-39ff-b21a-f5ce484934ac | -19.48639 | -54.85133 | 2025-03-16 01:17:00 | TERRA_M-M | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d615dc1d-1a25-3ecb-a514-d1e8bdb63cc7 | -15.63713 | -57.31438 | 2025-03-16 01:17:00 | TERRA_M-M | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 47d02243-327d-3bc2-b0ce-3f98fec2e5ae | -6.5631 | -51.1126 | 2025-03-16 02:50:00 | GOES-16 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 51d3cb38-a94d-3eb3-92a6-7362bbc52438 | -6.5631 | -51.1126 | 2025-03-16 03:10:00 | GOES-16 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| d33c7155-6696-3e51-871d-1da294c75e7d | -8.39047 | -35.02738 | 2025-03-16 03:10:00 | NOAA-21 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 69caa2df-0ca4-35aa-9675-7ee880cd385d | -8.39322 | -35.02651 | 2025-03-16 03:10:00 | NOAA-21 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 4e03966c-698d-376a-8d62-340bc4f9d5b3 | -7.47794 | -34.84245 | 2025-03-16 03:10:00 | NOAA-21 | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bf9bb753-64a2-3059-b0bd-211b22f7f679 | -5.07115 | -37.71526 | 2025-03-16 03:10:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 775fe9cf-93c3-33e5-8f5d-2158e67c69b7 | -13.42612 | -41.32415 | 2025-03-16 03:13:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 002043bd-de21-31a3-af09-9b079795d03e | -17.01733 | -41.07037 | 2025-03-16 03:15:00 | NOAA-21 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 3bb487a1-a306-3506-852e-970b5e1dfbff | -17.01823 | -41.06624 | 2025-03-16 03:15:00 | NOAA-21 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f0cf2513-5c6e-32a6-ae3a-64572a14e9d8 | -15.47123 | -39.07162 | 2025-03-16 03:15:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 13aae80b-c9b0-3838-99a2-79c98b1da233 | -8.39183 | -35.02344 | 2025-03-16 03:36:00 | NPP-375D | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 2f29cd39-96a7-329d-8a93-27f9cf860182 | -10.24638 | -38.31649 | 2025-03-16 03:36:00 | NPP-375D | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e9e4c7a2-3568-3019-8780-7bd7c5a1b188 | -9.22937 | -40.42352 | 2025-03-16 03:36:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a2d4281c-0497-366e-a3b8-544aaf16ab9d | -7.4766 | -34.8438 | 2025-03-16 03:36:00 | NPP-375D | PITIMBU | PARAÍBA | Brasil | 2511905 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 326355c5-bd9f-3757-a7fc-4f867e5c88a2 | -8.07441 | -34.9756 | 2025-03-16 03:36:00 | NPP-375D | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| fc085966-b817-3db2-88a3-a91ee550d71e | -13.42819 | -41.32287 | 2025-03-16 03:38:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bc15d045-89e8-30ba-a699-a028e6e166d3 | -15.88715 | -46.00848 | 2025-03-16 03:38:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6d3a0f8-b12c-3c80-b345-2e91cfb195a5 | -13.42449 | -41.32466 | 2025-03-16 03:38:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 84b0170f-5930-3d1f-9ee4-d391242555d2 | -10.98356 | -44.72852 | 2025-03-16 03:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 068390af-4482-3c14-9623-f4a3385b7dc6 | -15.83366 | -40.73634 | 2025-03-16 03:38:00 | NPP-375D | DIVISÓPOLIS | MINAS GERAIS | Brasil | 3122454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9867978d-e4c1-3e10-b88b-b36ee9dd21a3 | -12.8609 | -38.36512 | 2025-03-16 03:38:00 | NPP-375D | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 08b6e3f2-d71c-3282-b660-928ce3b1e07d | -15.80411 | -41.34365 | 2025-03-16 03:38:00 | NPP-375D | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 92e5da5d-160e-3fbc-894b-0c7d6633ca2e | -12.82845 | -45.00517 | 2025-03-16 03:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a94c849-06ab-373f-bd0f-6dcb898f7717 | -11.64184 | -37.79315 | 2025-03-16 03:38:00 | NPP-375D | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3b85d75e-9dab-37cf-98c8-ca61abfae309 | -11.26287 | -37.71384 | 2025-03-16 03:38:00 | NPP-375D | ITABAIANINHA | SERGIPE | Brasil | 2803005 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4a5c91f4-935b-3e92-bc97-2295151b5719 | -12.30063 | -47.26945 | 2025-03-16 03:38:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a902c856-6a26-3b6c-98bb-93d3adcd992f | -17.0208 | -41.06673 | 2025-03-16 03:38:00 | NPP-375D | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 61f268eb-500a-3783-8189-b634c9336334 | -10.69564 | -37.04781 | 2025-03-16 03:38:00 | NPP-375D | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d7de7a1a-4eff-3bf5-80fc-2e81a64c230e | -17.01987 | -41.07184 | 2025-03-16 03:38:00 | NPP-375D | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5c424b76-1451-3208-a526-9b23d317c255 | -12.46771 | -44.33103 | 2025-03-16 03:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| adf5e9a7-4128-3ebf-99f6-2028eb2b7e49 | -12.47307 | -44.33201 | 2025-03-16 03:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 51c249fb-9a99-3a0f-adb0-2e42665a0e86 | -11.77408 | -37.94277 | 2025-03-16 03:38:00 | NPP-375D | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d79525d0-c099-3003-b78a-c763f5ba0681 | -12.47375 | -44.32853 | 2025-03-16 03:38:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0b7dfde3-484d-3c2d-b7ce-9d0f837ff859 | -16.01494 | -38.94236 | 2025-03-16 03:38:00 | NPP-375D | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6d96b1c4-11af-307a-a984-0e2ab5a54422 | -15.47249 | -39.07226 | 2025-03-16 03:38:00 | NPP-375D | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 1422f51f-1d38-32b8-8688-5174eedbd8a2 | -10.65177 | -44.39811 | 2025-03-16 03:38:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 840babec-8a9b-391e-82ec-e1cb701c73f5 | -12.30702 | -47.27097 | 2025-03-16 03:38:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66d405aa-b116-3887-9c27-0277e16e722c | -16.01133 | -38.94172 | 2025-03-16 03:38:00 | NPP-375D | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2c1e2e44-e68f-38c5-9fa9-bb8eea6c59f0 | -12.46839 | -44.32753 | 2025-03-16 03:38:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 7fbfb035-9d40-3a7d-9924-2d9d2d48679e | -15.89353 | -46.00588 | 2025-03-16 03:38:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c898ad7-22e3-3bf1-8b2f-bf4989651588 | -13.42388 | -41.32205 | 2025-03-16 03:38:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| e4a07ca7-601d-3be3-b60d-e42a65a61775 | -15.83766 | -40.73701 | 2025-03-16 03:38:00 | NPP-375D | DIVISÓPOLIS | MINAS GERAIS | Brasil | 3122454 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 44fc4424-6773-3d09-8936-a03367857c54 | -12.05327 | -41.29303 | 2025-03-16 03:38:00 | NPP-375D | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bf77909e-a891-368b-81c3-98acee9d05ec | -15.80289 | -41.34461 | 2025-03-16 03:38:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 74142e9f-0fb3-3442-b6a7-b1f598051f43 | -18.91963 | -41.49043 | 2025-03-16 03:40:00 | NPP-375D | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ebffa5db-4e55-340c-86df-c56b2ad111c1 | -18.03958 | -39.92459 | 2025-03-16 03:40:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0f450827-09bc-3787-8327-a852ba9dadfe | -18.91819 | -41.48843 | 2025-03-16 03:40:00 | NPP-375D | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 92a2b49b-d56a-3459-a944-3cb568afd4f7 | -17.67651 | -42.74623 | 2025-03-16 03:40:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e0c21b87-b86a-30ce-b915-46291faea21e | -19.94242 | -40.7353 | 2025-03-16 03:40:00 | NPP-375D | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 82e0f032-b2fb-3a99-8754-271d10c1bd69 | -17.75171 | -42.89533 | 2025-03-16 03:40:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02912c2a-2e9c-39bd-9d92-3519b7f553c5 | -18.11615 | -39.68469 | 2025-03-16 03:40:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 22ca4ea0-ceda-3478-bb93-9d6ce2cf1464 | -19.89211 | -44.06866 | 2025-03-16 03:40:00 | NPP-375D | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 73003d5a-54c0-3bfa-98fc-c1e4bed4cfbf | -19.94248 | -40.73311 | 2025-03-16 03:40:00 | NPP-375D | SANTA TERESA | ESPÍRITO SANTO | Brasil | 3204609 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e4f4cb13-323f-3375-a1cf-5e60b38e33dc | -17.77699 | -42.81104 | 2025-03-16 03:40:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60af3fbf-c106-32bb-a80c-b7f22a31b754 | -27.33494 | -50.57711 | 2025-03-16 03:42:00 | NPP-375D | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 59cc3439-7179-3a5e-a06e-f91b4a63ea78 | -27.337 | -50.57672 | 2025-03-16 03:42:00 | NPP-375D | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 6b5d5bce-2565-35eb-a187-8ad88a21dfff | -29.87282 | -51.15935 | 2025-03-16 03:45:00 | NPP-375D | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| d521f2ad-ca02-3131-8aa5-0930150bac66 | -29.86498 | -51.16632 | 2025-03-16 03:45:00 | NPP-375D | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 99c9ea39-720f-3d01-a197-cc5422bd68c5 | -7.05208 | -44.39241 | 2025-03-16 03:57:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8fd61ecb-8501-34f1-bea5-1c01ffff9b81 | -6.19778 | -48.03677 | 2025-03-16 03:57:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 568171b2-f646-3085-b8ce-8ebcb71e86a2 | -6.19826 | -48.03399 | 2025-03-16 03:57:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46dc0e51-b54d-316c-a663-9e9e7cff013a | -6.20275 | -48.03775 | 2025-03-16 03:57:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a563445e-8ef4-394b-b349-7cc567475c5c | -6.19728 | -48.03965 | 2025-03-16 03:57:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c875f577-f252-3337-b033-2c2cf904ef16 | -12.29762 | -47.27019 | 2025-03-16 04:00:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a2e47d4-406c-3564-83dd-03f5925b4428 | -12.32593 | -42.83658 | 2025-03-16 04:00:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a0ef4bb3-bd00-3ec9-a9a1-8941be72932e | -12.38511 | -47.68806 | 2025-03-16 04:00:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 634c8037-fd28-340c-9d95-814423b3eaf3 | -12.42504 | -46.72515 | 2025-03-16 04:00:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README2.md)
