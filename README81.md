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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e2f12fa-ba4b-3aee-9dda-4931cfa373d2 | -9.0728 | -65.42051 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9228cca4-8ca5-3fa5-b726-4de197f7c82e | -8.64074 | -62.82702 | 2025-09-01 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 671cc3da-0bb6-3229-8efb-918da31572ec | -8.35526 | -70.26585 | 2025-09-01 05:23:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 062da01a-9619-33b7-9804-e40794567fe5 | -8.09804 | -70.22073 | 2025-09-01 05:23:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d86801e-83be-32ba-8c12-3bc38ef2d34a | -2.44384 | -49.36136 | 2025-09-01 05:23:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b6235ee-e13f-33de-9aa3-29018ca57f6d | -8.84626 | -47.50617 | 2025-09-01 05:23:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2c5fdd8b-8e03-318d-87eb-fac5b4bea1e0 | -6.91208 | -62.93998 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 77c1e9da-5ccc-3256-bb2a-3157433d0b0e | -9.06365 | -65.42859 | 2025-09-01 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 962bd951-b325-30bd-8aa6-9e220084e143 | -9.44727 | -60.57603 | 2025-09-01 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5ca7405c-b288-3dea-becb-e6d190a3b168 | -7.93576 | -63.01718 | 2025-09-01 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f85f2ec1-238f-378c-8dd0-1ccc17cd1a4a | -18.65839 | -52.59315 | 2025-09-01 05:25:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c1aed5f5-7636-381c-aa96-049682120649 | -12.87584 | -48.1693 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d045b066-d893-33e1-9283-dae14912acef | -11.58749 | -55.55277 | 2025-09-01 05:25:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93f3441c-d619-3940-bdd9-6ce81fb5ca5e | -6.82594 | -52.82958 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 75c673a0-77fe-33d7-ae6b-7cdba7f7a880 | -6.34592 | -58.18112 | 2025-09-01 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bafb389f-5c24-3434-a329-3b047ea7c2ee | -6.86002 | -52.80116 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5a2164fa-feda-3e17-9eff-4d9909943c06 | -8.34176 | -47.44881 | 2025-09-01 05:25:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 94574028-e2ca-3f0e-9181-b91f472c0a0f | -6.34242 | -58.18058 | 2025-09-01 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b589e56-ef90-317a-aad6-02cdc6813268 | -10.52043 | -69.23309 | 2025-09-01 05:25:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 774bc219-9939-31df-9a81-049f7235e740 | -6.81584 | -52.81645 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bf7d1812-b893-36cb-aac7-92f9620b5d7f | -6.80353 | -52.80972 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ede529de-eb86-3ed3-94c2-465e4ce0dfa1 | -14.48924 | -52.98871 | 2025-09-01 05:25:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d47283f-fb9f-3a25-b57a-d4094d7138e8 | -10.10182 | -68.47517 | 2025-09-01 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a326881-5c82-3f0f-9b8e-e8336a2cc254 | -6.83314 | -52.81374 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a0713731-da6a-38b5-ba30-1c7f436a922e | -15.29959 | -56.11008 | 2025-09-01 05:25:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2c357493-0e87-36b3-b94e-1fde9bf298c2 | -14.42198 | -51.66795 | 2025-09-01 05:25:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| adddc76e-d9e6-3165-b98e-0627625656eb | -12.87231 | -48.17128 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 0e75b7fd-d1ef-3bdb-990c-cb0063a0a9a0 | -16.29401 | -52.93752 | 2025-09-01 05:25:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7ca89e74-575d-3b41-b1fd-ab950ff73f02 | -12.42345 | -63.92565 | 2025-09-01 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5f78d244-3d27-3628-b26e-657af9443237 | -6.34182 | -58.18447 | 2025-09-01 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c154b74b-f32d-3642-9b5b-bb0d94d2ec09 | -15.7023 | -48.91299 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 4a9eeba5-f74a-37b4-be8f-0b03db77fd86 | -12.86856 | -48.0681 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 461ba69f-5e57-377b-825c-a2242399f41f | -14.31012 | -60.34374 | 2025-09-01 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cff35bc2-77c5-363e-8b3c-0d12370dfffa | -6.24564 | -60.01754 | 2025-09-01 05:25:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36d17c7b-db07-36c7-a240-abea3722e7bf | -8.33964 | -47.44258 | 2025-09-01 05:25:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1312459d-5247-32ba-9b33-deb784b24118 | -10.62626 | -63.49959 | 2025-09-01 05:25:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 691237fc-5242-35b2-9844-259db3fc1c06 | -12.57168 | -48.21531 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ecefabb7-6428-3d8c-ba66-e70f5c44aca9 | -14.4179 | -51.66661 | 2025-09-01 05:25:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fa8c60f6-396a-36de-bc4a-68b2031bf056 | -10.26436 | -68.78566 | 2025-09-01 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b9aaa61f-de66-3dab-84b5-40f47b44dac8 | -15.72721 | -49.00696 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| aca8d806-6c69-3993-b1f0-a29016224ba6 | -5.76085 | -53.40238 | 2025-09-01 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3743a044-621e-39e5-9a03-a81c5c3b3e44 | -15.71043 | -48.90229 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8d64766f-73ad-3c28-a146-fb2a898f3b6d | -8.05887 | -48.42485 | 2025-09-01 05:25:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 89aeabeb-0760-308b-a6f5-b98d7ae8709c | -6.80108 | -52.81425 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3cb50505-969d-33d9-b442-c87333943b0d | -12.60262 | -48.22242 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 073d7a60-0140-3089-a2f1-c270664fd7ab | -15.62809 | -55.92242 | 2025-09-01 05:25:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83400584-ab56-3f09-af9e-af8092a76d97 | -10.0845 | -68.46726 | 2025-09-01 05:25:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 85653689-ee42-39f0-ae4d-8de0d655f118 | -16.97184 | -49.30417 | 2025-09-01 05:25:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 64316574-fd8a-334b-9fb4-efc48a8b3322 | -15.52632 | -59.80501 | 2025-09-01 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3fd4c79-ed10-3b3d-9871-09dd3281a247 | -11.52594 | -54.46346 | 2025-09-01 05:25:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22df2c07-5d33-3347-8558-da9f0d051556 | -5.9976 | -57.75824 | 2025-09-01 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25dc87b7-341f-37c6-92f5-7227462e1407 | -6.43819 | -55.6215 | 2025-09-01 05:25:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b930e6a-38a3-35f6-8f8c-37edbfa4f0c7 | -11.65517 | -57.36069 | 2025-09-01 05:25:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94b8bd2b-8caf-3720-925a-ee96bca423f0 | -15.7224 | -49.00214 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| dc80a07c-6c94-3cf1-b270-c415e1037cc2 | -14.31356 | -60.34433 | 2025-09-01 05:25:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d57febb7-33ba-3b19-936d-a8d3f25e16a8 | -18.65881 | -52.59493 | 2025-09-01 05:25:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2b45162e-75a7-3b33-87c4-017e99370b71 | -12.60148 | -48.20537 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b5973d54-8130-3b23-ba2e-7acfcfa19b0c | -6.81012 | -52.82124 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae153c4a-e976-3f07-92b5-38b03f2d69ef | -6.43517 | -55.6138 | 2025-09-01 05:25:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d03f6ad9-2710-31ad-a924-ddfc2d8fcf65 | -15.72897 | -48.98707 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 32.5 |
| ff8a7df4-bcd5-387f-b1b5-f49082587c4a | -12.43707 | -63.92794 | 2025-09-01 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d8bb72c-90ef-3c89-a526-f53eaf3f55bc | -12.96884 | -48.1095 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 33c6a268-15a1-3c18-8331-658bb5c08c65 | -10.62567 | -63.50326 | 2025-09-01 05:25:00 | NOAA-21 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a833d2f-06f3-3066-864d-0c7ce68ec42e | -12.56793 | -48.21054 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2ca3e893-92f9-311b-9d9e-fb32242b7a0d | -12.44728 | -63.92966 | 2025-09-01 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3a127779-4731-3dc7-9025-86d5ba450b54 | -9.02436 | -70.66079 | 2025-09-01 05:25:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3b86b44-d6bd-3547-91a3-34f95170883f | -14.42153 | -51.67218 | 2025-09-01 05:25:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 5986eb38-5e99-3250-af0a-377d6bfc65cb | -11.59186 | -55.55342 | 2025-09-01 05:25:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f08632e5-28ee-3b91-92c9-8d48db26e498 | -15.72949 | -49.00219 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 22.1 |
| dfdaa7ac-cff5-3dd5-8d93-fed11b1a9d6f | -6.83237 | -52.8193 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 470a0ad0-cffe-34a2-bab4-763392f65cdb | -9.95683 | -66.87148 | 2025-09-01 05:25:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f41b61f6-c3ef-3172-9928-766a76e726b6 | -15.29689 | -52.79154 | 2025-09-01 05:25:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7d68f76f-dc1e-3361-a983-75b97a2e4c34 | -12.58212 | -48.21246 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.3 |
| b7ff6315-5e3e-3ab4-8900-6fe991bc4def | -6.79695 | -52.80791 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 49e6598c-7811-33e0-9b22-000b94fedfa3 | -15.72071 | -49.00032 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| b50cc368-bd72-36cc-a425-8453d5b75377 | -9.9562 | -66.87516 | 2025-09-01 05:25:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8bd939e0-efe4-34cf-b541-9dce0924ae0b | -15.72181 | -49.00839 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| eedea0c6-0495-3084-bca6-a3a6cefd38a0 | -12.42314 | -63.90636 | 2025-09-01 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8065a0fa-2bc8-3123-88d0-f01dda4df92e | -11.96233 | -51.36535 | 2025-09-01 05:25:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3b8c8161-de88-3f79-9a4a-20c95775b1de | -16.97132 | -49.30989 | 2025-09-01 05:25:00 | NOAA-21 | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b1f2ca3c-eac4-3e02-8633-5fd0e5eaefc2 | -11.51759 | -54.47664 | 2025-09-01 05:25:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6ae3a3cb-ee06-3c66-825a-a6539b0056b9 | -5.76393 | -53.40393 | 2025-09-01 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b514607-3db7-3afc-a305-86ea4e941003 | -12.44851 | -63.92217 | 2025-09-01 05:25:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6f783b4d-20ac-3408-9355-6ca6cf5b136f | -6.79617 | -52.8134 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 348a009f-0eb8-31ea-86ad-eb99c34e2241 | -6.85358 | -52.81134 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1a1fbe30-52f3-3798-bb54-8c07f330e1f0 | -6.34302 | -58.17669 | 2025-09-01 05:25:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0612511d-03eb-3cee-95dc-8e14b4276df9 | -8.34263 | -47.44181 | 2025-09-01 05:25:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 95036e17-d620-331b-a8de-7cd8a44d09d4 | -15.69162 | -48.9515 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d7d50442-0d8d-3dd3-ba10-2c3371dd5cd0 | -15.71805 | -48.89697 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ae3f6816-0801-3efc-a3ef-33c1ed8a71d3 | -6.83162 | -52.82479 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7dd46561-2cb2-37b8-b8f4-29e757a8b184 | -5.8251 | -51.37711 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b6b626da-dcd7-3476-af87-a0efc10c7dc5 | -6.82326 | -52.81248 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| aea90e81-4614-3c68-b8d5-4e091ab5296e | -16.15872 | -49.63708 | 2025-09-01 05:25:00 | NOAA-21 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d524cdd8-29ff-3b67-9166-173ed943bc05 | -6.43716 | -55.62859 | 2025-09-01 05:25:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ec17c4f-ffef-38df-8aa5-848e50ed5d9a | -16.20897 | -55.95033 | 2025-09-01 05:25:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 14207b54-74b4-3bda-b810-e04db97d00ce | -12.948 | -48.10028 | 2025-09-01 05:25:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aac3cdd6-999a-30e5-8c9f-990f5afad6f9 | -6.34577 | -53.43368 | 2025-09-01 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7d8275ce-a67a-3204-9b7f-d87f78e9f376 | -15.72779 | -49.0004 | 2025-09-01 05:25:00 | NOAA-21 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 049a5905-47c7-3a82-8461-65943819783e | -6.33709 | -53.4274 | 2025-09-01 05:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 76739ab0-8890-3362-b0ae-e9ded8282dab | -6.82821 | -52.81304 | 2025-09-01 05:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |


[Clique aqui para ver as próximas entradas](README82.md)
