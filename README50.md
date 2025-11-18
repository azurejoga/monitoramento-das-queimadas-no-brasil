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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e5c85d71-6e87-3cfb-8b6a-23747b69a1f6 | -7.07886 | -52.62173 | 2025-11-18 05:10:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f1b9abc-f6a5-3f15-8885-0cb57245685e | -3.25113 | -43.04124 | 2025-11-18 05:10:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| dd44717d-15f1-3477-b318-5e040c8d9585 | -3.3898 | -59.40946 | 2025-11-18 05:10:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b73e27fd-9e26-303a-8115-2e47ad9adc91 | -4.71595 | -50.94879 | 2025-11-18 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d44a9e1-898f-3937-956d-56f3a9bc0aac | -3.13649 | -49.90083 | 2025-11-18 05:10:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c6d93974-f8f6-3970-a9b1-8bd7a99dd1d0 | -1.44554 | -55.4619 | 2025-11-18 05:10:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 81235b9b-742d-3ad5-8cdf-eb0419ef90ef | -5.74559 | -49.25826 | 2025-11-18 05:10:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2749c03a-8a63-37ed-a709-6fb2acc37662 | -3.46441 | -54.63856 | 2025-11-18 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef437cf7-629e-3083-90b0-d63477ebffcb | -6.72625 | -46.31866 | 2025-11-18 05:10:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4d739436-3340-34b5-a229-677abbb48b5b | -3.45805 | -54.61466 | 2025-11-18 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eee452b5-13da-3ef1-a832-9f4a55210261 | -3.43932 | -50.34153 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aef007ea-8f1c-3e6d-b249-cd4ea6b8383a | -5.75052 | -49.25903 | 2025-11-18 05:10:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 3952b3e1-c7be-3348-9598-1a9f8305c9a4 | -6.30323 | -43.78778 | 2025-11-18 05:10:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| dbd617fb-d543-3945-999f-7ab5435411c6 | -2.52718 | -51.18844 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d723a54c-bd7a-3cf3-847d-0344d7571a7f | -6.93328 | -45.34691 | 2025-11-18 05:10:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c1e40db-ad6a-3abc-b20e-30b9d98a9264 | -9.40813 | -48.45244 | 2025-11-18 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 89e11ff5-90d1-3d2d-9298-9c598ce9783f | -4.64318 | -47.94695 | 2025-11-18 05:10:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 9183a873-63ae-3766-be43-1a52de1a2caf | -3.28848 | -53.82462 | 2025-11-18 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90b908f0-8588-31f3-a1c2-0414c1e877fc | -3.32653 | -51.51268 | 2025-11-18 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b88e2031-d28f-3d97-afc5-ec66311ca733 | -9.39619 | -48.45807 | 2025-11-18 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 55c07c08-7d13-3053-8ed6-7b4ae20ec9a6 | -3.25572 | -50.6927 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 15d0ab59-ec1d-3929-af3e-bee0a9fa4d40 | -6.15495 | -46.10831 | 2025-11-18 05:10:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6089a585-bbb7-3fe9-bb69-304f97d7fcae | -1.04026 | -57.49213 | 2025-11-18 05:10:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2605a21-5d44-32b9-bfeb-e9d1595025cc | -2.28139 | -53.64695 | 2025-11-18 05:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 943dc9d0-1646-3d5d-92f2-8c500f7796f4 | -3.48639 | -52.35778 | 2025-11-18 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6fd89979-bf9c-394c-a78b-d6c8e2057057 | -6.93565 | -49.67033 | 2025-11-18 05:10:00 | NOAA-20 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc492865-c9cb-317f-ba63-6073483556c8 | -6.21428 | -46.88288 | 2025-11-18 05:10:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3f8e7df9-5183-385b-ab87-ca29b47b63c4 | -5.40234 | -44.06468 | 2025-11-18 05:10:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6236a7ff-2780-3f8d-8a50-2bbe5e24ed7e | -2.51625 | -47.81771 | 2025-11-18 05:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63a53747-5dd4-349f-a9c0-67d3aab48199 | -3.2384 | -50.50503 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b585b35-ffbb-385e-8497-448e8a29994e | -3.14742 | -51.32199 | 2025-11-18 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b53f780-80e2-3d23-8639-4067e2231884 | -2.98025 | -51.08263 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 75ae1075-7128-3a48-a2f9-7f820a9ad180 | -3.2347 | -50.50014 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3af5f271-b232-36d9-85b1-8e82c40f96f4 | -2.83313 | -46.72373 | 2025-11-18 05:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b9ac80a-33d1-3707-b06a-b52cddd6870f | -1.86788 | -50.96236 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49038540-41dd-36ff-b309-ba940423aa7b | -4.25223 | -53.53749 | 2025-11-18 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05c03353-7280-35b5-a6d3-aa9bde5cee52 | -3.18502 | -50.64919 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8fc2ce95-aa3e-30ba-8e31-45e97c00c8dc | -2.52736 | -58.03117 | 2025-11-18 05:10:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3dd440a-ef0e-3a62-a58d-1d89ccad54b5 | -7.4301 | -45.19841 | 2025-11-18 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5887bf6c-7a89-322e-ab19-1c0c86498a67 | -3.58674 | -43.60184 | 2025-11-18 05:10:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea082907-62a1-3f62-928d-0295667a6ccb | -3.66034 | -50.21783 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c8580b3b-e555-328b-98b6-e99bb2d4571b | -5.47921 | -44.6951 | 2025-11-18 05:10:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 76c80dc3-b14b-3f21-960b-a028286418b5 | -1.83881 | -53.81266 | 2025-11-18 05:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91277e8b-3504-3f08-9761-8d4bad4c0cb9 | -2.49327 | -49.34808 | 2025-11-18 05:10:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2badcd62-4021-3a3b-899a-625be664859b | -9.40263 | -48.45165 | 2025-11-18 05:10:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 306323f7-7603-39e1-ba21-f4f5389c9e5b | -1.26595 | -55.39448 | 2025-11-18 05:10:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 032939e8-b922-3585-add3-e9fb2246ce19 | -5.25012 | -50.68268 | 2025-11-18 05:10:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 52970d64-0afb-3b65-8ca4-4b50c3829a1a | -3.08546 | -51.26716 | 2025-11-18 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a090b447-231d-3438-81f3-0a7d30b6d958 | -1.64119 | -55.81522 | 2025-11-18 05:10:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7cd85de-1121-3bbb-a2a2-f5789a7f483d | -5.33309 | -43.75235 | 2025-11-18 05:10:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0355f83e-e3d7-3f71-9bb9-20f5c624cef3 | -5.37834 | -50.4858 | 2025-11-18 05:10:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8ac3f7b9-212e-3b0d-acbd-ab30c92f01fd | -3.23097 | -50.50303 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2971cdfc-ec8e-360f-b07e-cdfabb5449a4 | -7.43476 | -45.20401 | 2025-11-18 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 698f6611-0640-359d-a5d3-f1b749ae6009 | -2.34018 | -55.80022 | 2025-11-18 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4640c5b1-84ea-340b-a3c9-cc960c2ddaa6 | -3.48353 | -52.35953 | 2025-11-18 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e84b539c-218b-3e48-8280-8627900a4fea | -3.02853 | -54.604 | 2025-11-18 05:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35cf5664-9432-3cfd-b0ba-80fc3dc59d25 | -3.08213 | -50.35372 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 735ef894-7931-3dff-8ae4-ad59a2bd72e8 | -3.75298 | -50.94712 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16309036-dd97-32c5-85af-5ca6bafc87b8 | -2.68629 | -49.17139 | 2025-11-18 05:10:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 73ac125d-b6a6-389a-8f71-9b7753dc1ced | -2.52793 | -58.02757 | 2025-11-18 05:10:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 165e6b3c-b8b7-3753-a5fe-fb964bae07f3 | -3.17576 | -50.65205 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36ef4d95-0b3d-3de5-a1e7-65a6b4c79b2c | -8.79561 | -44.39546 | 2025-11-18 05:10:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1a665616-9ffc-3aaf-ad78-f1d74bee5c36 | -5.38284 | -50.48654 | 2025-11-18 05:10:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c7f22c7-31e9-38ac-ba5b-84a1f288d8eb | -4.27329 | -44.25712 | 2025-11-18 05:10:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5d706c4-d590-3d37-80d8-18cc27942b23 | -4.12931 | -52.11809 | 2025-11-18 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7d2f8484-c00d-3068-89a2-81220d34bd63 | -1.62665 | -55.71404 | 2025-11-18 05:10:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9dd42be4-c89a-3843-90d9-12be84befdc6 | -3.83325 | -52.29927 | 2025-11-18 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5291e90-9c8f-3ebf-8b36-094fc4312cc6 | -4.275 | -44.24555 | 2025-11-18 05:10:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8084c160-3885-3520-8608-7c7e0d926d1d | -3.75358 | -50.94314 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28874d66-2f0d-33b3-885a-8b8dbc4c7140 | -4.19455 | -44.23475 | 2025-11-18 05:10:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 73297aca-c7a5-3ecc-86f9-4edfbc769dc1 | -6.1556 | -46.10354 | 2025-11-18 05:10:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c23a1256-bc9a-36fe-928b-8805fbfe9651 | -3.24096 | -50.49574 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c02e5c2d-47f3-364f-b911-59a75edd2856 | -2.89779 | -51.45915 | 2025-11-18 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6e2f89b-9f0a-3695-b63f-c3819218e6e8 | -8.28929 | -55.10919 | 2025-11-18 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 077782ad-6da7-355a-a033-64aac4a5e86b | -3.59783 | -50.71858 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b9a361e-3c7c-3df1-a46e-54073a7067a1 | -3.64345 | -50.84142 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dba530c3-fd0a-3446-ae2e-ac9b35e37a61 | -3.49213 | -54.05327 | 2025-11-18 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70bd243e-9652-32b4-ba4f-596ff10b2fc1 | -1.83531 | -53.81212 | 2025-11-18 05:10:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1e6bf77d-09e5-3634-805a-2c62decda7ba | -3.21213 | -50.92286 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf058276-a393-35e0-9527-72214c4d6a1b | -3.02911 | -54.60032 | 2025-11-18 05:10:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c8d0d9f-83a1-3d81-8255-4b81b3a720a2 | -3.18868 | -50.65401 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13d88ea6-62e4-3236-8a26-b45669654a17 | -3.48252 | -52.35719 | 2025-11-18 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d21d75de-5f25-3708-b97f-06c561b374fd | -6.71539 | -47.79508 | 2025-11-18 05:10:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 946d91b9-85a3-3a43-8472-804b8ed8ad20 | -6.09188 | -57.86553 | 2025-11-18 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 53a0fcae-1be2-3359-a227-5a97548d27fd | -3.23159 | -50.49879 | 2025-11-18 05:10:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 86fabfb7-ce92-3468-8908-ce38415b9c50 | -7.33342 | -46.17429 | 2025-11-18 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9da052bf-5d28-3d3b-b5ec-9b2a876224e0 | -8.5481 | -46.0497 | 2025-11-18 05:10:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 698f4329-65b4-37ed-8415-05c020eae483 | -3.30062 | -50.07639 | 2025-11-18 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 957228c9-29bf-3090-8393-a33c05f9cb43 | -9.7229 | -49.13489 | 2025-11-18 05:10:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b7a0843-4adb-324d-91ee-0e408d4127bb | -2.33752 | -56.07557 | 2025-11-18 05:10:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64e76323-e3c0-336b-bff3-f77e3e9859f3 | -3.0496 | -47.01591 | 2025-11-18 05:10:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d59052e7-13dd-3a1d-9b01-14bcda443f51 | -9.72818 | -49.13553 | 2025-11-18 05:10:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ecc839f-a5f3-3fd8-b334-a7e384787c2b | -4.18035 | -44.23857 | 2025-11-18 05:10:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a0a6a3d7-820c-3b12-a8ff-792efa02cc20 | -2.47486 | -48.22485 | 2025-11-18 05:10:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5b5df667-1676-3537-94c7-6a2275a58c4e | -4.1398 | -46.34922 | 2025-11-18 05:10:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 42e8ee1a-a831-3890-8679-682d01a9af93 | -4.17953 | -44.24437 | 2025-11-18 05:10:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 60f75a4f-f8ed-349c-b9aa-19b5d8449fc7 | -3.17157 | -46.60323 | 2025-11-18 05:10:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 882eb844-2334-37bd-8d73-c37471c557e7 | -1.44222 | -55.46138 | 2025-11-18 05:10:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86de3e30-7e2a-30cf-a0a4-faf0b510058e | -4.17796 | -44.22982 | 2025-11-18 05:10:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c568ddd6-96bd-3dc9-96a8-6c40af18c0d2 | -2.51161 | -54.816 | 2025-11-18 05:10:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README51.md)
