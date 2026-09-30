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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28431029-ecee-3d9d-bab6-d951d33cb990 | -14.11836 | -46.26666 | 2026-09-30 04:55:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f33dc1c6-8677-3a75-97be-08caf2312cff | -11.80295 | -50.4354 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54985139-f122-37e9-8601-8478345d8ae8 | -12.77498 | -54.02247 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 430553d5-88ee-3833-870c-5d954a2433ae | -18.50246 | -45.15018 | 2026-09-30 04:55:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b300f159-23bc-3e19-9d59-4175bfdb4a0a | -18.88373 | -43.8109 | 2026-09-30 04:55:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4a8e63f-c159-3a3f-929a-5568937da797 | -11.80469 | -50.44732 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 4c8f9320-2bba-3b7e-8c3b-9775c2a5751b | -11.39086 | -51.01082 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b8f79fba-03d7-3685-9346-d5c3f57514ca | -11.40036 | -50.9937 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5e6324b9-f23a-3f74-952e-761569008519 | -11.82644 | -50.46624 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 27c077da-c75c-370c-a547-ca09a3f1d33b | -11.83903 | -50.47596 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b2e2da75-560f-333b-be2e-d63c1380bc46 | -20.54495 | -49.59767 | 2026-09-30 04:55:00 | NOAA-20 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 469f2dc6-0199-3bf9-86bf-3991c40c0900 | -13.53368 | -49.18344 | 2026-09-30 04:55:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f719f963-de12-3c4e-9f7b-0934f78020ad | -11.39303 | -50.9739 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88d25010-5191-35b9-b722-215c4cc6d8bf | -11.337 | -51.03576 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7fb85728-2130-3e8d-a7eb-0a580adf2a82 | -13.37937 | -44.02334 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7a308dc3-406c-3c29-b07b-eecdcee5bb48 | -11.79307 | -50.43518 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3a249b23-3200-3cee-a242-77c6d69443ce | -18.27806 | -53.03806 | 2026-09-30 04:55:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 903c6678-8896-388e-b17f-7e3b627e8431 | -12.77737 | -54.00789 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22810d28-1296-325d-9d34-e1de8f375110 | -11.79952 | -50.43487 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d6724a7-d34b-3d8c-ade5-a04a5b669461 | -11.84338 | -50.95725 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02fc2773-bac2-32ee-92c3-1c75b4ef72f0 | -11.3117 | -50.97601 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0e4a6253-5399-3546-8a0e-80283daf832e | -13.32895 | -43.96173 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5df90b31-9cb3-3412-a765-b296cb83c3bf | -11.54503 | -54.49913 | 2026-09-30 04:55:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e36f6189-a92e-3ac3-a36c-e23b4fefc9c6 | -18.88079 | -43.81665 | 2026-09-30 04:55:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f0660992-356e-32dc-90cd-ce16edee1904 | -13.42632 | -43.81463 | 2026-09-30 04:55:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 82f27103-8921-3e61-a9e5-47c05aed3fa2 | -11.34709 | -51.03736 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 46a0e0e6-c281-3a8c-8c63-cfb59d265402 | -11.39977 | -50.97496 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de82e6e7-f41b-370a-b206-2a40b69b35ca | -12.08102 | -46.46007 | 2026-09-30 04:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 330ac549-29ba-3b9f-b2e3-500a482566ed | -11.3903 | -51.01445 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7885812c-e074-3100-b35a-290cf92070da | -11.79249 | -50.43897 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36f8b2ac-406d-3180-b34b-fb5c5fd832d6 | -18.25912 | -53.05 | 2026-09-30 04:55:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 94cc9eaa-91bd-33da-abd7-c45dbe730092 | -11.31114 | -50.97964 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0d66f26-627f-3190-b75b-50358207d99b | -11.81496 | -50.42561 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ef628597-33a4-3c58-856b-3506539c34ca | -11.3583 | -51.0317 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d282055c-b737-3e34-8469-48f8abd4c25c | -12.76959 | -47.24895 | 2026-09-30 04:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 119bec85-ccd9-3cba-95fe-80fde6e1c9b1 | -11.7982 | -50.44763 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 78eefef0-0ae2-3cc0-b9f5-d052f5201d3c | -12.77797 | -54.00425 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ce25173-51be-3607-b975-866c12194155 | -20.7412 | -46.38288 | 2026-09-30 04:55:00 | NOAA-20 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6599a957-aa95-3fb4-a4cd-dbad8c3f4deb | -10.89877 | -56.17384 | 2026-09-30 04:55:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3268e163-16c4-3e21-9040-dff8b1b4c291 | -12.14564 | -47.20456 | 2026-09-30 04:55:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b3491d6-ac85-31e8-8097-54be62a3592f | -11.80812 | -50.44786 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 0f4dbf27-2567-3dbf-a38b-85ecdfbfced6 | -18.26913 | -53.05167 | 2026-09-30 04:55:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e0797bf3-9c9b-32d7-bb1c-a658ecd93a8d | -11.39478 | -51.00772 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 78543f48-5d73-35ad-b82f-895f1eb089d1 | -11.79476 | -50.44709 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8af11ec7-9cc5-33b9-852b-5faebe88b961 | -11.83889 | -50.96406 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f6ba64a-8955-3ae1-b96b-fe31ad951029 | -13.54668 | -49.1718 | 2026-09-30 04:55:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0ed02d3-6f8a-3a20-b598-d24b5b0e2e72 | -12.78865 | -54.00234 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 274f5eb2-e4e7-3d8d-8231-be710e30cd6f | -12.62451 | -48.35983 | 2026-09-30 04:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b91ccbb4-edc5-3518-85af-0b94b6a31828 | -11.79418 | -50.45088 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9041e3fa-1b6b-344f-a970-14fafdeb2e38 | -11.84308 | -47.78382 | 2026-09-30 04:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 768655a3-645d-3abf-a71d-6d3b93cf0df3 | -11.29768 | -50.9775 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e8e4e673-7136-3d0c-915e-49e41a806a6b | -18.26579 | -53.05111 | 2026-09-30 04:55:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ac3cefc5-79ba-399b-8d56-5ed0a84bfa44 | -11.30948 | -50.99054 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 35f4782f-0d4f-3c08-a7b3-bd72eb2f4944 | -20.15092 | -50.61282 | 2026-09-30 04:55:00 | NOAA-20 | URÂNIA | SÃO PAULO | Brasil | 3555802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 86b4a866-e393-3e07-b79e-dffceea1c9d0 | -12.77558 | -54.01882 | 2026-09-30 04:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1625685d-8cca-3081-bace-f976f244fbc8 | -20.45384 | -46.22179 | 2026-09-30 04:55:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80dd69c6-f324-34ca-9f91-e5804fb1b883 | -14.1992 | -42.07374 | 2026-09-30 04:55:00 | NOAA-20 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 9d2a6c08-190f-3a71-a253-8bea33f90fc4 | -11.83617 | -50.47163 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3569487d-fe5f-3205-b89a-6bea91135d77 | -11.31059 | -50.98328 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04a257cc-90da-3099-8839-b7e0ac4f867f | -12.14616 | -47.20086 | 2026-09-30 04:55:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e2c0aa3-e780-30c1-bd49-3a26ca9b52df | -14.20197 | -42.07199 | 2026-09-30 04:55:00 | NOAA-20 | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 4b0a9ad1-d3ba-39d3-8895-74aad3fe892a | -20.54424 | -49.60307 | 2026-09-30 04:55:00 | NOAA-20 | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 420cd7d3-c28a-3ae9-abe2-97133447299c | -18.8956 | -43.8064 | 2026-09-30 04:55:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2db8f07f-48d4-3042-910c-a654c1469694 | -11.32854 | -50.97866 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1933a44b-cb12-3794-bb63-b0baf1983ff6 | -18.28694 | -53.04711 | 2026-09-30 04:55:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3b513431-89c7-3701-a146-3e0c55afe985 | -11.83959 | -50.42554 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 69c279db-38e2-35f3-bd2d-e191d8945a52 | -18.89871 | -43.80813 | 2026-09-30 04:55:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 8b0c8bf3-b3c2-36e5-a2a5-eb9fef6baab7 | -18.2719 | -53.05592 | 2026-09-30 04:55:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| efcb0700-b696-34c2-85bc-90fae6d8c8f5 | -13.07128 | -43.28064 | 2026-09-30 04:55:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 946eaad9-a394-375f-8946-12bf76c1f81f | -11.82301 | -50.46571 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 165b329c-ef4e-312f-8bcc-998e6524c07e | -11.81728 | -50.45705 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d2293298-6e42-3733-b546-38f17257e1e1 | -11.40258 | -50.97914 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a5d31d5f-f342-3605-96fe-8a88883e6d61 | -12.34471 | -48.19992 | 2026-09-30 04:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4730fb01-0a79-39c1-afad-b0f2d2d1d49b | -12.76496 | -47.25208 | 2026-09-30 04:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 306644af-fe64-31de-9630-789c574de3fa | -11.85014 | -50.95831 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2cd1ef95-d1a3-37b4-83df-e32fa29fffe0 | -11.81099 | -50.45219 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dd31b8fd-86af-321b-85da-3b4bd593379c | -11.84589 | -50.47702 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4ad97a86-62cb-36c3-a4f0-4516f6987470 | -11.35324 | -50.97509 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a89ab8d9-c6a0-30c6-b10d-2f455c893e2a | -10.89502 | -56.17321 | 2026-09-30 04:55:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45133ad2-5bca-3088-a6ec-e1a0d566a2d9 | -11.38132 | -50.97206 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c4e391aa-f626-3140-9e21-f458a8e7f6d3 | -19.21515 | -44.75754 | 2026-09-30 04:55:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b64bc234-9f26-3417-b1ed-6bde52b839f2 | -13.07085 | -43.28413 | 2026-09-30 04:55:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f92abc30-5b20-3b89-8af3-70b348f67774 | -11.80182 | -50.443 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| dc9c6ea0-9697-3615-84cc-384be131e0e5 | -19.21479 | -44.76103 | 2026-09-30 04:55:00 | NOAA-20 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b164a9bf-ac49-35ab-a3b5-6e462261ebef | -11.8396 | -50.47216 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef2a69b8-58f2-33a9-bef0-7c1d3cb82084 | -14.12344 | -46.26287 | 2026-09-30 04:55:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4acfc410-ff04-343b-8678-a9798513fad5 | -10.07273 | -63.08825 | 2026-09-30 04:55:00 | NOAA-20 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 681bd944-5f83-3f67-891c-e09ee10616f6 | -18.25023 | -53.04095 | 2026-09-30 04:55:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 22761b20-8769-3591-9c15-02557e6d16ab | -11.36222 | -50.98396 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27bcb781-9fb7-3c2b-a0c5-e2d323c6eabc | -11.96512 | -51.00608 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f36ad439-986e-3e38-95a6-d73a69d9f7fb | -11.84189 | -50.48028 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ac1ec1b4-b512-32df-9fb0-f3ce0da785ff | -10.89425 | -56.17767 | 2026-09-30 04:55:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5b6b0699-1d74-3ab7-86f5-76efb45fb8aa | -18.25301 | -53.0452 | 2026-09-30 04:55:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 58e4ae15-054f-37e5-b54a-10a8be12b6fc | -11.83902 | -50.42934 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fcdcd6bb-1b0e-3717-9df9-dd67749548a9 | -11.38862 | -50.96948 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d8fdbb6e-892a-308b-982c-af5c7ea65b86 | -11.39589 | -51.00045 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 146a789f-3f1b-3722-ae6e-8609314dbf46 | -11.80698 | -50.45545 | 2026-09-30 04:55:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 62b728e2-f082-3f76-a365-b925870cb56c | -11.32971 | -51.03833 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78a89bf3-97bc-3f09-8612-0bc673358f61 | -18.27857 | -53.05704 | 2026-09-30 04:55:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aa186f29-4426-3058-8493-e089897910fa | -11.40032 | -50.97132 | 2026-09-30 04:55:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README55.md)
