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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ae884e1-bd21-325a-b35e-49ed9d28bd02 | -4.69769 | -45.68453 | 2024-10-30 00:33:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| fa514538-aaa4-3119-bcd1-6ecc805a81fc | -4.6962 | -45.67348 | 2024-10-30 00:33:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 25.0 |
| a2c88660-249a-309f-8262-fa02f6359b56 | -4.66511 | -46.6518 | 2024-10-30 00:33:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 468414b7-c6bd-3f55-b53c-e89791369b64 | -4.65703 | -45.38354 | 2024-10-30 00:33:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a39eeb35-35df-3688-8815-1d9f295aac2c | -4.64414 | -46.19222 | 2024-10-30 00:33:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6b481f9f-71a0-3c20-a8f6-f8fb9efe6706 | -4.64227 | -46.18665 | 2024-10-30 00:33:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c3ff775a-79be-38c7-a5e3-7e15cab86a59 | -4.62931 | -44.3664 | 2024-10-30 00:33:00 | TERRA_M-M | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 528e48cf-2599-3da0-8df7-4f0d3f33cfbc | -4.62892 | -46.54116 | 2024-10-30 00:33:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2fc30d35-5a6a-3275-a355-2616ca08a915 | -4.62569 | -45.61182 | 2024-10-30 00:33:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 5c163c42-a5bd-3965-b903-c2807f18eef5 | -4.62421 | -45.60101 | 2024-10-30 00:33:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 3aa358d2-bb3e-30aa-8f39-eddbe50766cd | -4.61855 | -46.54284 | 2024-10-30 00:33:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 26fd7da5-60d0-3954-8f37-d684b4b25489 | -4.61445 | -45.60228 | 2024-10-30 00:33:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| cf7a86db-cecb-345a-8b95-05ab16306b52 | -4.60691 | -45.33231 | 2024-10-30 00:33:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9f0f6aa2-58dc-3ce4-a65e-47e5feda0c4a | -4.60547 | -45.32188 | 2024-10-30 00:33:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4f87ac41-f409-3e3b-9e90-1cecf2ddce8b | -4.6033 | -44.31239 | 2024-10-30 00:33:00 | TERRA_M-M | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e4527cc5-3be5-3ae5-b31e-8e1f89ed2851 | -4.60201 | -44.30298 | 2024-10-30 00:33:00 | TERRA_M-M | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 18.9 |
| ffe24be7-8c1d-36a6-b545-6099d4d3823d | -4.52702 | -44.75568 | 2024-10-30 00:33:00 | TERRA_M-M | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 04d6a492-60c9-32a9-8311-03d9c81d11e4 | -4.52567 | -44.74591 | 2024-10-30 00:33:00 | TERRA_M-M | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 66c566c7-e13f-32cf-8d91-bbd8e346bb39 | -4.50559 | -46.46366 | 2024-10-30 00:33:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 3ae107ad-fd78-3eda-ac6a-a56597af85d5 | -4.504 | -46.45161 | 2024-10-30 00:33:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 682f3748-10cf-323d-b9ca-ec9534c86bc4 | -4.49714 | -46.45831 | 2024-10-30 00:33:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 5cf1ac4f-5e5d-3aef-bf09-a737615d2044 | -4.4953 | -46.46535 | 2024-10-30 00:33:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 24.4 |
| d52ddd92-948b-3e2f-9ffe-1b8ebcf1df4f | -4.49368 | -46.45311 | 2024-10-30 00:33:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 25.6 |
| ad8c2d7b-1ae9-399e-bcf0-8322df7f3cfd | -4.48331 | -48.11551 | 2024-10-30 00:33:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 6a264571-59c9-3011-981d-eccfe9b47e91 | -4.47659 | -48.84977 | 2024-10-30 00:33:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 7d76a413-9603-396c-9a80-43efd5af13bf | -4.4455 | -46.46519 | 2024-10-30 00:33:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 12.8 |
| ee8d6e33-7fe6-39ae-adae-ceeae428d611 | -4.43148 | -45.83107 | 2024-10-30 00:33:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 02261e3f-7680-35cb-902d-fe83acdcea75 | -4.43023 | -46.42972 | 2024-10-30 00:33:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| cb470eb2-5b59-370c-af8c-f87820da31e2 | -4.43 | -45.82005 | 2024-10-30 00:33:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 106.3 |
| d5ca6346-69cb-34b0-917c-e1be63657c8c | -4.40838 | -45.96584 | 2024-10-30 00:33:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 1bfefebe-a655-3949-8dcc-e43dc247aad5 | -4.38312 | -45.1856 | 2024-10-30 00:33:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 7164e9d8-b314-3370-9fd0-c7b3c0500b83 | -4.33925 | -45.68077 | 2024-10-30 00:33:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 2a5a7d98-9e5d-330e-ac9e-963b5483feeb | -4.31681 | -45.66188 | 2024-10-30 00:33:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ccb226a5-7d93-3a0e-a160-64f9878bcc93 | -4.2934 | -45.72713 | 2024-10-30 00:33:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 1c37838a-56cc-3884-90d8-2de63afe1fac | -4.28581 | -45.67237 | 2024-10-30 00:33:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 1ff6bd55-a7a5-3e0d-9efc-2f32523d3c98 | -4.28431 | -45.66156 | 2024-10-30 00:33:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 95937c6f-f0c1-3d09-b14c-7ce0d8f85816 | -4.25657 | -45.67652 | 2024-10-30 00:33:00 | TERRA_M-M | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 7a6e26f4-da81-337f-bd8a-1f582830c240 | -4.2336 | -46.10695 | 2024-10-30 00:33:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c156000e-19cd-365a-8043-145c89b7ea9c | -4.19363 | -46.72094 | 2024-10-30 00:33:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 40.9 |
| ebc0b7fc-3e8e-3ad4-a39e-11526234f6fa | -4.19193 | -46.70825 | 2024-10-30 00:33:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 13647aa2-3c3d-3c77-80c3-8a1f18a8f9e4 | -4.15146 | -46.84997 | 2024-10-30 00:33:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 782b7a72-e978-38dd-a1c5-94b349ec2d2f | -4.14966 | -46.83677 | 2024-10-30 00:33:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 5fd0f059-6586-3bfb-aca3-79e501431261 | -4.14562 | -45.60998 | 2024-10-30 00:33:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| c4e2b4c4-aae5-3a70-b2e5-537942cc1f83 | -4.13652 | -44.19867 | 2024-10-30 00:33:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e9de22a6-1eab-373c-b59b-c6a3dc5fd147 | -4.13144 | -48.1378 | 2024-10-30 00:33:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| bed102c5-2f77-394f-b8c8-19a141b9613c | -4.12875 | -44.20921 | 2024-10-30 00:33:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d5cb3def-4feb-3eb0-908c-cb3484b8b984 | -4.12747 | -44.19994 | 2024-10-30 00:33:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c09b7975-5316-3ccb-92c3-a59fc2e81274 | -4.12403 | -45.05825 | 2024-10-30 00:33:00 | TERRA_M-M | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6c39d518-46cb-3a68-bd79-274ce9b4e0e5 | -4.12268 | -45.04822 | 2024-10-30 00:33:00 | TERRA_M-M | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 8106878a-8ff7-3321-bcf4-cf65a16adeb7 | -4.11767 | -45.05481 | 2024-10-30 00:33:00 | TERRA_M-M | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 70ca3d82-0867-3825-baea-576a522e76b3 | -4.0994 | -45.94674 | 2024-10-30 00:33:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 53b65251-1eaf-3aec-a992-ef150526f740 | -4.09788 | -45.93555 | 2024-10-30 00:33:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 5f995caf-cf5e-32db-840f-8e0d7457c015 | -4.08949 | -45.94807 | 2024-10-30 00:33:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 20.2 |
| ff54d9c9-1e53-3e5b-b136-cc12b75c3fc9 | -4.08798 | -45.93687 | 2024-10-30 00:33:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 682bd8c0-8655-3403-96ba-45f5131ed0df | -4.07958 | -45.94941 | 2024-10-30 00:33:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3736516f-c31b-38c8-ac07-70a540019ad9 | -4.07389 | -46.2836 | 2024-10-30 00:33:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 8220ad81-e2dc-3518-925f-30b90ced3c0e | -4.07245 | -50.01032 | 2024-10-30 00:33:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| cc7013f2-d914-34d7-bf4f-87cb4ac936fb | -4.07228 | -46.27183 | 2024-10-30 00:33:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 6bc70685-ee8d-3fb1-a887-1c11e1f5d2eb | -4.06885 | -50.02835 | 2024-10-30 00:33:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| b1d681ad-fb48-3489-b486-528ed9235991 | -4.06589 | -50.00563 | 2024-10-30 00:33:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 966bcce6-332d-37d5-8e42-92caa4b142fc | -4.06375 | -46.2849 | 2024-10-30 00:33:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 13.6 |
| e6824715-1634-38a9-b468-545623b2c9ff | -4.06216 | -46.27327 | 2024-10-30 00:33:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 90e6cb0e-f2f4-3c93-ab17-8fd926edd8c8 | -3.96408 | -48.93628 | 2024-10-30 00:33:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 5e66c5cf-cc61-35ad-9f67-777a50214a12 | -3.94872 | -48.1424 | 2024-10-30 00:33:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 575bc2ce-34e3-3bf7-ac9c-23a8829eede5 | -3.94661 | -48.12674 | 2024-10-30 00:33:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 124.9 |
| b3e31bdc-9be7-3f47-950f-608dff67a8a6 | -3.93341 | -48.35081 | 2024-10-30 00:33:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 9fc4ac69-7c79-3f60-8fc5-85a894399a57 | -3.90719 | -44.93441 | 2024-10-30 00:33:00 | TERRA_M-M | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 634f7037-5571-3f51-9ba3-b6e7250897d3 | -3.90583 | -44.92458 | 2024-10-30 00:33:00 | TERRA_M-M | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 75f2637a-04ef-399d-a7c0-ac4624091a62 | -3.90522 | -49.08303 | 2024-10-30 00:33:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 1fda5127-b8e1-37bd-a98d-8c165a508914 | -3.8346 | -44.14673 | 2024-10-30 00:33:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0a9db748-3440-35df-9382-e41d5eeb921c | -3.82559 | -44.14799 | 2024-10-30 00:33:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9be84bbb-b578-3ba8-bfa4-728da288ec84 | -3.8101 | -51.19418 | 2024-10-30 00:33:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 44da5c30-2e88-377d-ad00-122e897d5ffb | -3.80615 | -51.16462 | 2024-10-30 00:33:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 235.9 |
| 18dc532c-057f-3fd7-98c9-5221fd1c0ef5 | -3.74777 | -45.46323 | 2024-10-30 00:33:00 | TERRA_M-M | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 592d988f-92f7-3cb6-a02b-7163fd603110 | -3.70176 | -45.44418 | 2024-10-30 00:33:00 | TERRA_M-M | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 745cb09a-ca15-3eba-9d41-9c9d8061e4dd | -3.68797 | -45.6279 | 2024-10-30 00:33:00 | TERRA_M-M | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 42978207-19e8-30e2-b3b1-498b0ba95827 | -3.66835 | -45.09062 | 2024-10-30 00:33:00 | TERRA_M-M | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2340bc1a-e53f-3fb6-90ca-1b472b6e8279 | -3.667 | -45.08068 | 2024-10-30 00:33:00 | TERRA_M-M | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5cf776ac-be97-35b7-a852-e1ea394d4725 | -3.66577 | -44.19186 | 2024-10-30 00:33:00 | TERRA_M-M | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8e364a83-581c-33fb-b804-fa9471640d6b | -3.6574 | -50.15916 | 2024-10-30 00:33:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| f917b375-b7ff-37c5-939c-a2839b63f812 | -3.58061 | -47.3785 | 2024-10-30 00:33:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 8cc89704-c9a9-3085-aef6-2bbbdf52238c | -3.57743 | -50.03833 | 2024-10-30 00:33:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 1b9958a6-8f7e-3cc9-95f2-8c3b8eb44498 | -3.57159 | -47.39389 | 2024-10-30 00:33:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| e6b5bf84-e76d-3cca-b2db-495de4015ae4 | -3.56969 | -47.37996 | 2024-10-30 00:33:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 758.3 |
| 9ef56936-deed-3a5b-98c2-d93cb813bc7a | -3.56781 | -47.36617 | 2024-10-30 00:33:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 31.4 |
| 8a91e5e4-cb3e-3845-93b0-a28901c06075 | -3.56387 | -50.04015 | 2024-10-30 00:33:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 155.0 |
| c17ddeda-ac33-3bce-9087-fb488ea975e3 | -3.56087 | -50.0179 | 2024-10-30 00:33:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 39bda795-bf22-37bb-9a1f-f2e71ba5fe98 | -3.55879 | -47.38152 | 2024-10-30 00:33:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 06cbb816-4806-37ce-8a76-1ea872ad6b06 | -3.54417 | -47.35551 | 2024-10-30 00:33:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 668641a0-cd87-35cc-9cfa-2915647259eb | -3.52111 | -49.23732 | 2024-10-30 00:33:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 101.6 |
| fafc5ddf-e438-3de7-9988-3ec393952558 | -3.51858 | -49.21828 | 2024-10-30 00:33:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| d2d18ad4-49df-3885-a12a-3874442b28e7 | -3.39758 | -49.7651 | 2024-10-30 00:33:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 7f82246d-e02c-3f45-9104-2d23f39b7297 | -3.39411 | -49.75911 | 2024-10-30 00:33:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 0da1d994-7f70-3c26-a8a6-687e5ddcd411 | -3.37707 | -44.8404 | 2024-10-30 00:33:00 | TERRA_M-M | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 921d9f25-02cb-3ea6-bc2e-5439281cdca8 | -3.33749 | -45.36613 | 2024-10-30 00:33:00 | TERRA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3771b3fe-c441-3baf-8dfb-690dd9446e3d | -3.33492 | -44.06745 | 2024-10-30 00:33:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 9c177310-a689-3ff2-b5bd-85c09d57716b | -3.33366 | -44.05841 | 2024-10-30 00:33:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 59.3 |
| a822f33c-379e-3796-8a33-ebce85d9ee79 | -3.32408 | -44.3862 | 2024-10-30 00:33:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c6bb53bd-7ec9-3087-96b9-d44a3d1c20d4 | -3.3228 | -44.37697 | 2024-10-30 00:33:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a93cef7e-fe30-3807-9cf9-290f6febd36f | -3.28778 | -50.23339 | 2024-10-30 00:33:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |


[Clique aqui para ver as próximas entradas](README9.md)
