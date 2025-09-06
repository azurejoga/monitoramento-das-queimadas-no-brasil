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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bcd08091-73af-3f9a-9e2e-51a2569e1892 | -17.96452 | -46.90097 | 2025-09-06 04:42:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 889b2118-b041-336d-b698-b36824694c06 | -18.59423 | -43.64519 | 2025-09-06 04:42:00 | NOAA-20 | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 549fb3b9-7ee0-3fe4-997b-05e5da2b15c2 | -22.25167 | -48.76218 | 2025-09-06 04:42:00 | NOAA-20 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| a12211b8-9d5c-3cff-8fe5-67ea08f4b010 | -19.75718 | -57.9527 | 2025-09-06 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 3c90ebc2-2bcd-3e6a-b0b0-ef4a019057a9 | -19.8008 | -57.94262 | 2025-09-06 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| ed4a42ed-8719-3386-9ff3-18a965f94f27 | -21.83857 | -46.46175 | 2025-09-06 04:42:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fc2612f3-4977-3d5b-9ee2-4f7c4bfe3755 | -21.49153 | -46.19137 | 2025-09-06 04:42:00 | NOAA-20 | DIVISA NOVA | MINAS GERAIS | Brasil | 3122405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 79bff535-d5a0-343e-9a44-35535e04482c | -19.4076 | -44.31843 | 2025-09-06 04:42:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b1220c1-5a6f-39c5-8afa-ee7f1bc7c63b | -22.24576 | -48.75913 | 2025-09-06 04:42:00 | NOAA-20 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| a40a45f7-40cb-3a70-9a7d-e3540939626c | -19.90786 | -57.93007 | 2025-09-06 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7a048bf1-6044-31b1-9613-8398e54a9a4d | -16.30112 | -58.10634 | 2025-09-06 04:42:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 295f72b1-c9b2-3884-ae57-d02fd3d7bbec | -20.91652 | -44.0147 | 2025-09-06 04:42:00 | NOAA-20 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 636c744f-373d-381c-baee-689de900384d | -20.52719 | -46.11444 | 2025-09-06 04:42:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 872d78ec-0ecb-3c00-a8bf-6b77606a04bc | -18.59389 | -43.6483 | 2025-09-06 04:42:00 | NOAA-20 | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ea20ea60-6ba8-3088-9c93-d9482a463dfe | -20.24034 | -51.31457 | 2025-09-06 04:42:00 | NOAA-20 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 11484873-36e0-3197-94a2-f9abe8f9d58c | -21.83422 | -46.46089 | 2025-09-06 04:42:00 | NOAA-20 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 477c6c5a-dd6f-3623-ba67-5969a291e077 | -23.32567 | -50.87854 | 2025-09-06 04:42:00 | NOAA-20 | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| b81074a5-0cd4-31b1-8025-b7a7b88b76ae | -23.33854 | -50.86348 | 2025-09-06 04:42:00 | NOAA-20 | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0c151742-e8ea-391e-aa2b-40381d8b16ac | -23.34203 | -50.86412 | 2025-09-06 04:42:00 | NOAA-20 | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2c7c6c52-0836-30cc-98ab-53323d08f1eb | -18.44161 | -45.93196 | 2025-09-06 04:42:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e37947c0-f486-3de8-b2e7-d00dd70a5d01 | -22.24784 | -48.76168 | 2025-09-06 04:42:00 | NOAA-20 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| 4fbe55cf-ed85-39d5-9909-339d0136b0e8 | -20.53493 | -46.4638 | 2025-09-06 04:42:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bebe355e-eff5-3d63-a3b2-86d69ae35972 | -22.27394 | -49.56553 | 2025-09-06 04:42:00 | NOAA-20 | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f142da2c-8205-3fd1-ad41-e195ecbf2099 | -19.81129 | -57.95583 | 2025-09-06 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 1d897e28-5da7-3d2a-80ab-e3eff7ccd3d0 | -22.73991 | -47.03381 | 2025-09-06 04:42:00 | NOAA-20 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 745231d7-d179-31aa-9832-5e388aaa7e99 | -21.7662 | -47.27761 | 2025-09-06 04:42:00 | NOAA-20 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| cc4759ee-79e4-34a7-8f42-cf44692baa08 | -18.81436 | -53.2704 | 2025-09-06 04:42:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eb5086b7-2734-314c-acc8-97ad55c19d9d | -22.78241 | -50.61563 | 2025-09-06 04:42:00 | NOAA-20 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 695665a2-525b-3c20-95d3-84092c70f4ea | -21.9961 | -49.91662 | 2025-09-06 04:42:00 | NOAA-20 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 02dcac7b-04a6-3348-9db8-d86391473c49 | -23.32626 | -50.87432 | 2025-09-06 04:42:00 | NOAA-20 | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| f6bd295d-9999-3da0-a4c9-f69b9227adf9 | -20.35532 | -48.64351 | 2025-09-06 04:42:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1820d24-caec-3fae-8dd7-6f7e7b06c4f2 | -18.26756 | -43.02399 | 2025-09-06 04:42:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| edcb6091-a825-3be6-af09-755aea02e8c1 | -23.42141 | -47.04034 | 2025-09-06 04:42:00 | NOAA-20 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 21568365-fd16-35ec-9998-de2097ba3c14 | -19.80413 | -57.9472 | 2025-09-06 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 3720562d-a46a-36b5-a1e1-12f0520cb253 | -23.42288 | -47.04309 | 2025-09-06 04:42:00 | NOAA-20 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1b001f6b-e4e4-38e0-bb87-51442d1eeee6 | -21.76671 | -47.27353 | 2025-09-06 04:42:00 | NOAA-20 | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 25b602ba-cbf6-3447-8915-a057c95ca25e | -22.26126 | -48.74816 | 2025-09-06 04:42:00 | NOAA-20 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 3c61b572-90ce-30a5-8e09-c2e8e169cd17 | -18.26198 | -43.0265 | 2025-09-06 04:42:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| ca957cb5-1bf1-3ecf-98bb-4582854be53e | -22.24337 | -48.76609 | 2025-09-06 04:42:00 | NOAA-20 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 4b534313-7f7e-3f9b-a8e4-45c90d33b4a7 | -22.661 | -46.83037 | 2025-09-06 04:42:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 131c6d63-1168-355c-81b3-473d5667b749 | -23.34144 | -50.86834 | 2025-09-06 04:42:00 | NOAA-20 | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e8c13cec-4b62-38e1-b86d-18abcff16606 | -19.88922 | -57.9184 | 2025-09-06 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| b7682789-2a8f-3cf7-90e4-de63d9f9c445 | -20.53106 | -46.45952 | 2025-09-06 04:42:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc0db036-147c-39b0-8447-fde359e298bf | -18.01026 | -49.26228 | 2025-09-06 04:42:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 243111e6-8969-3998-8f66-549ad7d1dd6d | -20.1087 | -44.31964 | 2025-09-06 04:42:00 | NOAA-20 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c6381a4d-5592-3ac1-a280-0be4debdc385 | -22.25678 | -48.75269 | 2025-09-06 04:42:00 | NOAA-20 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 2d4c550d-b7d4-3813-a52e-707ad179a496 | -20.53835 | -46.47178 | 2025-09-06 04:42:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b4c30a2e-3ed8-396d-ab34-8f6fb2b92a77 | -20.46282 | -48.78875 | 2025-09-06 04:42:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 1344fd7a-d331-373d-911a-3ab5dea2d8a8 | -22.65718 | -46.82545 | 2025-09-06 04:42:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 186e9f78-9078-3c4e-9e29-4323a5795a00 | -20.18277 | -44.23784 | 2025-09-06 04:42:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| de3de6f8-5567-319c-b7b2-f6ecfe074632 | -19.47106 | -53.97171 | 2025-09-06 04:42:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 72468fac-ceba-36a9-979e-4a3293bf7e6f | -19.80482 | -57.94347 | 2025-09-06 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 5ccbda31-9eab-349c-a330-63c8002d0887 | -21.34574 | -51.05073 | 2025-09-06 04:42:00 | NOAA-20 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 40289e2a-e377-3ca2-b306-35cb440b4bfe | -23.41857 | -47.04241 | 2025-09-06 04:42:00 | NOAA-20 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6dcd74dc-eb01-3940-b241-00d0cd143910 | -21.1379 | -46.27399 | 2025-09-06 04:42:00 | NOAA-20 | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 96aa5206-6c1d-39e4-903f-65ca1cdeb75d | -22.78592 | -50.61619 | 2025-09-06 04:42:00 | NOAA-20 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 4cebe9ca-846a-3339-ad44-82cce950790a | -20.53542 | -46.4597 | 2025-09-06 04:42:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8230c858-06a6-357a-a268-c31c056f8e85 | -22.908 | -49.69189 | 2025-09-06 04:42:00 | NOAA-20 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2b05eeb7-dfb5-3944-8010-e2e43d819d75 | -20.53396 | -46.47183 | 2025-09-06 04:42:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 617583f6-b2a9-32f3-a871-18e0d61475ed | -22.24708 | -48.7492 | 2025-09-06 04:42:00 | NOAA-20 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3f966593-ef63-37e1-b804-8be79863afef | -21.83051 | -47.99067 | 2025-09-06 04:42:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c322d228-afa2-35df-87e5-3ad0afe2a191 | -18.14502 | -51.7756 | 2025-09-06 04:42:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 42184691-8d87-344f-b8ad-aa474a760a2b | -22.12201 | -46.63468 | 2025-09-06 04:42:00 | NOAA-20 | SANTO ANTÔNIO DO JARDIM | SÃO PAULO | Brasil | 3548104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e2897153-abdd-3f80-ba3d-deb2b9244469 | -19.62418 | -46.01535 | 2025-09-06 04:42:00 | NOAA-20 | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 713f2d0a-5551-3f69-a3ae-10c21f187a96 | -19.91118 | -57.93463 | 2025-09-06 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.7 |
| de932f12-f296-362a-ba0f-56956bf9d8ba | -19.40822 | -44.31289 | 2025-09-06 04:42:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58db9161-2787-3897-b0de-85e3a901cc27 | -20.18214 | -44.24354 | 2025-09-06 04:42:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 97c3d0ff-69a6-3991-9ce6-762497cd54f5 | -18.5366 | -47.41906 | 2025-09-06 04:42:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c99aee26-345b-38a3-a293-8f85c25e15a8 | -18.69074 | -44.60709 | 2025-09-06 04:42:00 | NOAA-20 | MORRO DA GARÇA | MINAS GERAIS | Brasil | 3143609 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 111ef55d-ac88-3059-99f1-6cd81c36889e | -19.79339 | -40.84921 | 2025-09-06 04:42:00 | NOAA-20 | ITAGUAÇU | ESPÍRITO SANTO | Brasil | 3202702 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 4a1a5530-53a0-37c5-886e-a3352572a4f6 | -20.5277 | -46.10992 | 2025-09-06 04:42:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f84008d7-2a65-3ca8-83f2-9993472530bf | -19.80468 | -57.9467 | 2025-09-06 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7e817ed1-a998-3bbe-aed5-6740260e4870 | -18.43622 | -45.94012 | 2025-09-06 04:42:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e34ad845-bd12-3f8e-9375-f8041221519c | -23.32916 | -50.87916 | 2025-09-06 04:42:00 | NOAA-20 | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 4d22ebcc-e32e-37a9-b894-549e2a3b39b4 | -20.35155 | -48.64296 | 2025-09-06 04:42:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 340c8f1a-fefd-3b13-9313-fa5f75b0623c | -19.97671 | -43.39404 | 2025-09-06 04:42:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fe8d22bd-d10e-37ce-be72-06bb94135fbc | -22.24909 | -48.75176 | 2025-09-06 04:42:00 | NOAA-20 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e0b4cb63-20bc-323e-9ed5-f13204b275c5 | -22.84888 | -49.17471 | 2025-09-06 04:42:00 | NOAA-20 | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b80cee4-5688-3ac8-8eb0-9a2a5b020684 | -19.50411 | -45.93565 | 2025-09-06 04:42:00 | NOAA-20 | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41002bd9-2837-336b-a980-5c992116afba | -20.24091 | -51.31079 | 2025-09-06 04:42:00 | NOAA-20 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d5806554-445e-39ae-9ae9-a5c4d386ee19 | -17.86445 | -51.72524 | 2025-09-06 04:42:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9d03e743-e68a-34c1-8ff1-ce698e33e4eb | -19.63294 | -49.38485 | 2025-09-06 04:42:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0fe65f36-1ca9-376e-9d2b-276a2583b908 | -20.53882 | -46.4678 | 2025-09-06 04:42:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f084167b-f0c4-35a7-86f4-d687e2191802 | -22.24973 | -48.74674 | 2025-09-06 04:42:00 | NOAA-20 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1470f722-2718-38a4-b77c-54edd771dbce | -20.52789 | -46.11227 | 2025-09-06 04:42:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a7f81d2-8faa-3d1e-875f-c124f1b5f1f3 | -19.81648 | -57.97243 | 2025-09-06 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 08cca348-246d-3445-bbfb-a9c797c130f0 | -21.93352 | -46.13537 | 2025-09-06 04:42:00 | NOAA-20 | SANTA RITA DE CALDAS | MINAS GERAIS | Brasil | 3159209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e1ee30d8-d71a-3fac-ba21-3ff0dd3b6d23 | -17.96513 | -46.90101 | 2025-09-06 04:42:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ccb4a105-5d28-32a1-95b2-c5006991e7fc | -19.80138 | -57.94213 | 2025-09-06 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 1cf68244-664f-3d66-bbf5-01354e4f8134 | -19.79342 | -40.85015 | 2025-09-06 04:42:00 | NOAA-20 | ITAGUAÇU | ESPÍRITO SANTO | Brasil | 3202702 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| e31b8349-dddf-38c2-ac8c-012d205e375b | -18.44108 | -45.93632 | 2025-09-06 04:42:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e8b8def2-45e2-3910-b3a2-59cdedb0e0bb | -18.90337 | -46.60908 | 2025-09-06 04:42:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a06c92b2-cb52-34ca-b778-187f57dea8c6 | -19.812 | -57.95211 | 2025-09-06 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 4ad8fd26-0fca-322f-aaaa-a8c8d2e9e1bc | -19.90717 | -57.93377 | 2025-09-06 04:42:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 21b4c344-5d15-352c-8e85-fce1c3c8f229 | -22.25093 | -48.74968 | 2025-09-06 04:42:00 | NOAA-20 | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3e40ccd4-01d5-3b74-a4ad-1bfd330707cd | -23.09912 | -49.84873 | 2025-09-06 04:42:00 | NOAA-20 | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 477625a8-228f-3f48-bfb1-3a476921667e | -22.76623 | -46.45937 | 2025-09-06 04:42:00 | NOAA-20 | PEDRA BELA | SÃO PAULO | Brasil | 3536802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2b78fbbc-540b-3cfd-ae1a-49983a544016 | -19.41256 | -44.31836 | 2025-09-06 04:42:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 013e79f8-1fd3-393c-9c56-07e741aeac78 | -19.6959 | -47.24142 | 2025-09-06 04:42:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2bf86edd-1eb3-3745-89f2-75e02dcd5760 | -19.79387 | -40.84539 | 2025-09-06 04:42:00 | NOAA-20 | ITAGUAÇU | ESPÍRITO SANTO | Brasil | 3202702 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |


[Clique aqui para ver as próximas entradas](README77.md)
