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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3bcf46a-3860-379b-ad4b-76b787758a8e | -8.86422 | -50.19076 | 2026-06-07 05:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5c2d3b3-85c2-3d89-a296-d6edd659393a | -8.86879 | -50.19392 | 2026-06-07 05:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e8ce4d1-957d-326e-a7b3-c30e31f8722b | -8.86922 | -50.19519 | 2026-06-07 05:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 398a78f0-bad2-30d9-bff2-1d7176452176 | -5.80957 | -45.12408 | 2026-06-07 05:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 207b9683-3a11-3bb4-acba-f098e9fcc8fe | -8.02937 | -46.05877 | 2026-06-07 05:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f25c0fb-d60c-3ed2-adf1-03f76d09a831 | -8.03024 | -46.0518 | 2026-06-07 05:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9120acf-d3a2-3998-a41d-0f3d129b1da6 | -5.80832 | -45.1186 | 2026-06-07 05:25:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 07e0ac90-f474-3c28-8cf3-da44b7d3d6f5 | -8.94225 | -45.67176 | 2026-06-07 05:25:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36b34b54-8861-3038-8478-e7f7a238f608 | -5.94317 | -45.50652 | 2026-06-07 05:25:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 55524622-5e42-364b-9f4c-358ccba49a6e | -8.94136 | -45.67908 | 2026-06-07 05:25:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e7896db-1f85-354b-bb8f-6f982ed742ac | -8.86373 | -50.19432 | 2026-06-07 05:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac47ce80-ea49-3ea8-8a18-eeb97ad5c661 | -11.63125 | -54.1579 | 2026-06-07 05:27:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e382dba8-da67-3a27-abea-6145b2697b90 | -9.81022 | -57.82127 | 2026-06-07 05:27:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e19a42ad-4b0c-32f9-be3d-87ed8d3a99d1 | -9.21011 | -64.08727 | 2026-06-07 05:27:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b97e5b57-6d7f-37e0-9932-0d54e661952f | -9.09303 | -50.60575 | 2026-06-07 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef049e54-2b1e-3e9f-ba4e-b692d425d5d7 | -10.83718 | -60.75462 | 2026-06-07 05:27:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 838e147c-dbc0-3998-a835-8634de773a81 | -10.83328 | -60.75762 | 2026-06-07 05:27:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 412957e2-4062-3e3d-a224-228fcab0f1f6 | -14.63896 | -54.5138 | 2026-06-07 05:27:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56defe9f-e82b-3c60-8e91-80cb3293b8d2 | -11.5471 | -52.79238 | 2026-06-07 05:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 64a88344-75f1-3a6a-bef7-15079edd49e9 | -12.06738 | -48.43018 | 2026-06-07 05:27:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7c43f495-12fb-30cb-8867-ee7ddec53ad3 | -10.18738 | -52.65174 | 2026-06-07 05:27:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ece8778c-35a3-3dcf-b8dd-26f3d469b1f5 | -10.57381 | -57.31943 | 2026-06-07 05:27:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ba6036c-1b1a-37b3-a8bd-67ba16301982 | -14.29017 | -57.54389 | 2026-06-07 05:27:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82edd4d7-3273-3439-82e7-bc778967e13e | -14.53694 | -58.82065 | 2026-06-07 05:27:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 800bbe95-74d4-39e7-8bba-a9296aafb363 | -10.86277 | -53.74034 | 2026-06-07 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ce2e110-31da-32a0-b5ad-b4d96fc7e229 | -9.09887 | -50.60303 | 2026-06-07 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a90ed70e-9513-3a78-8cca-36561ef76222 | -11.26859 | -53.97195 | 2026-06-07 05:27:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3f815100-039d-38b7-811b-2d0503a323e0 | -11.0522 | -56.924 | 2026-06-07 05:27:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7462bfa-b5a9-3a3c-bded-149dd6346f32 | -11.97832 | -47.361 | 2026-06-07 05:27:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2880f92f-c510-3424-bb88-e77ba82c6394 | -10.83101 | -60.77178 | 2026-06-07 05:27:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31a67519-0079-369f-86c6-0b79c99cab15 | -11.47453 | -47.98998 | 2026-06-07 05:27:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65e8152e-f7d0-31e0-897f-6c3857444f2a | -9.24904 | -57.7739 | 2026-06-07 05:27:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85cf0bd0-bab4-30d9-810f-071a117ebbc2 | -15.41768 | -55.8828 | 2026-06-07 05:27:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5ffe8a2f-ee1c-383a-982f-0922bd6d1dbd | -14.64341 | -54.51445 | 2026-06-07 05:27:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20ce7170-2e18-3ece-a23b-5ad375a69dd4 | -9.07199 | -50.5995 | 2026-06-07 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ad3be829-2f80-393b-8768-9d428dbe0581 | -11.05157 | -56.92833 | 2026-06-07 05:27:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 062203bb-82ed-36a9-a8c7-acbbff95e126 | -9.08719 | -50.60848 | 2026-06-07 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b33ef50a-ef44-3fd6-bcea-804dc7145972 | -10.85892 | -53.73524 | 2026-06-07 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 18fdb178-46c5-3727-814a-ceab79660bbb | -11.89559 | -57.78758 | 2026-06-07 05:27:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5cd1075c-1409-3e88-9eb5-91f4878cfb54 | -12.06094 | -48.07723 | 2026-06-07 05:27:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 04ba676b-2a36-3dbb-820c-135fd54dbce1 | -10.5987 | -55.42385 | 2026-06-07 05:27:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55c9b4c0-523e-3168-b479-08e70042848a | -15.42182 | -55.88321 | 2026-06-07 05:27:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42b7c253-4a89-3b93-9a15-434768938c5e | -10.84319 | -53.75113 | 2026-06-07 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4147efeb-1f51-364a-b641-5c491a20d62d | -10.59782 | -55.42005 | 2026-06-07 05:27:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e140779a-2f14-34fc-b88f-692b1354bfad | -13.11588 | -53.53207 | 2026-06-07 05:27:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6af4184e-ff1a-3afe-8596-2163ad63b3c6 | -11.55189 | -52.79306 | 2026-06-07 05:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2bb1cdd4-284b-36b6-ad05-bdc0287107db | -10.85832 | -53.7397 | 2026-06-07 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4d52aab1-78b0-3b0e-8dec-4c48392f6a42 | -11.61725 | -55.1833 | 2026-06-07 05:27:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96d4dfab-2f2f-3148-a2ba-c3d3a09529de | -10.85387 | -53.73906 | 2026-06-07 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ac915fa-833d-35c6-a51f-1db563156bac | -9.08765 | -50.60503 | 2026-06-07 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 16c5e825-4d19-36e6-a838-991b1d6b4009 | -10.77258 | -54.10002 | 2026-06-07 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 920a5232-efd2-3f6a-a5fa-727bc6baee66 | -11.55669 | -52.7937 | 2026-06-07 05:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8eee0cde-2c0d-3dcb-b6d7-70101496c201 | -9.09349 | -50.60233 | 2026-06-07 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f6d23c6-c108-34c2-b1aa-bfad5978c489 | -10.85267 | -53.74801 | 2026-06-07 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f0a8e5c3-eee7-3627-ba64-dfa9561ec96b | -14.28774 | -57.53452 | 2026-06-07 05:27:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 68ac0909-6bee-3cbe-9737-7d07dab850f3 | -12.81061 | -54.86512 | 2026-06-07 05:27:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9e8e7f2-872f-3759-adff-12644e49489d | -10.85771 | -53.74418 | 2026-06-07 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7bf4a6e4-6f0b-3b5d-8f70-3773342ddd55 | -11.55461 | -52.80933 | 2026-06-07 05:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 39b13e7c-ee01-3bc9-b114-febf43d7eb95 | -14.28649 | -57.54333 | 2026-06-07 05:27:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8c359ed8-61fc-3af8-9fab-9cf7b3cba149 | -10.12467 | -57.76952 | 2026-06-07 05:27:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec3e7e08-bf8a-3eb4-8254-7665151d6ce3 | -10.83959 | -53.753 | 2026-06-07 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1bc5d85-e11e-369c-94b1-7ad29bfaa163 | -11.63196 | -54.1561 | 2026-06-07 05:27:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1bcd628-fa79-3000-adcb-e1f904123105 | -14.06638 | -58.90581 | 2026-06-07 05:27:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1db3831-cbf6-34f2-8d5b-106e61a8213e | -11.89618 | -57.78357 | 2026-06-07 05:27:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c6f6e3a9-1e89-3762-85b0-ccdb0ecc74db | -9.8121 | -57.82063 | 2026-06-07 05:27:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a409e5ca-cb29-3e8e-9638-54592a4aadfb | -15.36931 | -55.88331 | 2026-06-07 05:27:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10bcc31b-1a79-3ec2-8f3b-d2818678ffb7 | -10.82937 | -60.76061 | 2026-06-07 05:27:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 48573fff-a75e-3265-b549-52ed525d7904 | -11.54232 | -52.79163 | 2026-06-07 05:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 53d69427-b98b-3596-a9a6-4c3b0a6b8370 | -9.09256 | -50.6092 | 2026-06-07 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b1e73e7-4e27-3625-ac70-3571b4e374c0 | -11.26477 | -53.96702 | 2026-06-07 05:27:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc59f142-a328-3696-92bf-45367e1e9532 | -10.83384 | -60.75408 | 2026-06-07 05:27:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 425ae8ee-a325-342a-81a0-ec2ac6b09b36 | -14.28711 | -57.53896 | 2026-06-07 05:27:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2eb3d37f-d1fb-30fa-bffa-bf285d532712 | -10.82824 | -60.76769 | 2026-06-07 05:27:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7686dd6c-8cfb-3cee-8ac6-7980f9723e9c | -10.82547 | -60.7636 | 2026-06-07 05:27:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 607eaac5-9f26-3f2d-a946-73953a1d2dbc | -10.57321 | -57.32349 | 2026-06-07 05:27:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09e876fe-9554-349a-a4a8-be61eba90e00 | -11.46798 | -47.98917 | 2026-06-07 05:27:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2dc2afe7-01e3-35f7-aced-eaa1005ef834 | -11.55258 | -52.78785 | 2026-06-07 05:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 992d694f-bc9c-3679-98cb-5e0990cc0938 | -12.81116 | -54.8611 | 2026-06-07 05:27:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74e1db73-3a30-36a3-a201-770d65122133 | -10.82881 | -60.76416 | 2026-06-07 05:27:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 396d8f9f-c2d6-3351-b0c8-7e91ec3e5fd1 | -11.05648 | -56.92027 | 2026-06-07 05:27:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12b46333-7728-3aad-9ae8-8801e7245397 | -10.91889 | -54.1131 | 2026-06-07 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 068873cf-b2e1-3d69-b8d8-11cdedbb9ad4 | -10.83271 | -60.76117 | 2026-06-07 05:27:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dc9f9921-ee4b-3893-8821-048ee20877a2 | -10.83874 | -53.75053 | 2026-06-07 05:27:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e7f649b-50dd-348c-91fd-d7cd2fe5cdcd | -11.56489 | -52.80541 | 2026-06-07 05:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ac3f43c4-b5c7-3539-9d0b-885c8df52688 | -13.49793 | -56.57121 | 2026-06-07 05:27:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31418f61-998e-31e1-ab9e-fdd27f4f108c | -10.83214 | -60.7647 | 2026-06-07 05:27:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 50e444a6-d383-3fea-82ce-ba77850cb900 | -11.55738 | -52.78849 | 2026-06-07 05:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 48a15e25-65c9-3e95-ab6b-433575a0b8ed | -12.72771 | -54.1997 | 2026-06-07 05:27:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e12e3527-8dbe-3595-9ccb-f7862ac6038f | -16.04134 | -50.56317 | 2026-06-07 05:27:00 | NPP-375D | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9de4d9ce-3b4a-3803-a340-028ac0a5d483 | -11.54983 | -52.8086 | 2026-06-07 05:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 514fed37-95bf-3c8e-a1c5-709a9139d5f2 | -11.7915 | -57.35429 | 2026-06-07 05:27:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56e9cb5c-725d-3386-8c46-840d1502105d | -9.07735 | -50.60027 | 2026-06-07 05:27:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d10e2793-3567-3787-8279-8114352893aa | -16.04178 | -50.55901 | 2026-06-07 05:27:00 | NPP-375D | NOVO BRASIL | GOIÁS | Brasil | 5215207 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef037e99-0a6e-3611-8899-48baf2108a8a | -10.59473 | -55.4233 | 2026-06-07 05:27:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 497c0a43-1a10-3f5b-98d7-b6203a964b18 | -11.26917 | -53.9677 | 2026-06-07 05:27:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43a71a92-3f32-3c48-83c3-58ab107d21c7 | -10.59385 | -55.4195 | 2026-06-07 05:27:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 076b8417-98e3-3f1a-9c0c-afd374b95e50 | -11.54642 | -52.79755 | 2026-06-07 05:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1b7e1897-29f6-3216-bcfa-f96dc31d9b14 | -11.5594 | -52.81001 | 2026-06-07 05:27:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b08bd1a1-b93d-312f-83a9-61ebfcd43b46 | -16.18744 | -58.46363 | 2026-06-07 05:29:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f6b34649-96fe-32ef-ac8b-704a217e0546 | -16.79357 | -54.17193 | 2026-06-07 05:29:00 | NPP-375D | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README8.md)
