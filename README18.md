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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce33499f-32fa-3ffc-967d-ce0d74b02b79 | -11.29083 | -55.13631 | 2025-07-29 04:49:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db4f9712-1c09-32b4-89d9-f976c39e75de | -7.72301 | -51.11389 | 2025-07-29 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5683580d-9814-364d-b2c5-7f0b44eb1dc4 | -8.95878 | -46.7516 | 2025-07-29 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f8f056ee-1825-3cdb-9b82-b92abc2c1c5f | -9.11728 | -47.64499 | 2025-07-29 04:49:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2a915f7-b671-3675-b3b6-174296967c07 | -6.49609 | -56.20061 | 2025-07-29 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0b963ce-b642-364e-b32c-2c73af712dae | -6.49016 | -56.21084 | 2025-07-29 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 84390f5c-153c-310a-bf0b-f7f061ccd151 | -10.5193 | -42.55367 | 2025-07-29 04:49:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9e66335f-57f8-3e2e-81eb-33d2beaf2785 | -6.90087 | -52.86537 | 2025-07-29 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d05b43b2-9104-372b-9ac8-2004dbe9e2e1 | -6.49671 | -56.19697 | 2025-07-29 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d1e846b-cd3b-32db-a255-2c9ece61d9fc | -13.0086 | -44.88162 | 2025-07-29 04:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e3348376-10a4-3c38-b4d9-37ad9878ad20 | -13.49453 | -45.60123 | 2025-07-29 04:49:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e33f6d5-a439-3128-9333-c7fd6c117662 | -13.49605 | -45.62593 | 2025-07-29 04:49:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 445fa8ad-77ec-3692-b4fe-0322479f644c | -11.99845 | -46.95782 | 2025-07-29 04:49:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 388f2bf8-c726-3da1-992c-46c935697fbb | -13.48575 | -45.56898 | 2025-07-29 04:49:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 275cdc4e-cde5-3c79-b43f-79422e1c73a1 | -9.36623 | -45.73388 | 2025-07-29 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 288d9b62-b6db-3425-baf2-8e4d71673013 | -10.51975 | -42.55017 | 2025-07-29 04:49:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 17abe73c-d621-31e9-98bb-ab87b92dd810 | -12.94634 | -44.73173 | 2025-07-29 04:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe84fd73-a407-3370-8ef3-a539c195e7be | -11.99906 | -46.97201 | 2025-07-29 04:49:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1dc1cdb0-c967-3cb2-8196-e0a41fd96c27 | -11.42715 | -45.13006 | 2025-07-29 04:49:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 58d14bfd-e955-34ad-9d99-44d6d6eb330b | -6.50651 | -56.21361 | 2025-07-29 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da96608c-e656-3608-aaf8-9242fd92eb20 | -6.49834 | -56.2122 | 2025-07-29 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1dcd297f-561a-3dd8-9859-49c25e02b491 | -11.42776 | -45.12538 | 2025-07-29 04:49:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 27.1 |
| fbe0819e-094a-3a96-83b0-835135c966ad | -13.13381 | -47.34522 | 2025-07-29 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bc1d5e8c-696b-3c10-8ecd-de1a3227ec4e | -7.72632 | -51.11443 | 2025-07-29 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c55a5c39-15b5-3dfa-be48-93ea72816cca | -10.95107 | -54.37008 | 2025-07-29 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15896d5e-4078-3803-a7a1-197e3c8d4ee8 | -11.98407 | -46.69835 | 2025-07-29 04:49:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4da11259-ba97-3609-93be-222556100c12 | -8.74708 | -48.04824 | 2025-07-29 04:49:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7e17b7ad-4ae8-3b1b-9bf5-4c3e1b4f7796 | -9.3966 | -45.49066 | 2025-07-29 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d62f4ed3-9efb-3c14-873b-bd6b24f28f04 | -13.48252 | -45.59308 | 2025-07-29 04:49:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d00663a1-a4ae-30df-8e1e-2642ce71cdfd | -7.86058 | -46.73554 | 2025-07-29 04:49:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| de91e465-7ef5-3f8c-a6be-3179a506e5f7 | -7.81448 | -50.23021 | 2025-07-29 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dad3232a-65e0-323b-a318-6463559a29bc | -8.637 | -45.51347 | 2025-07-29 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af22495a-cb16-3da9-8a1c-1f541da76695 | -7.75174 | -51.10418 | 2025-07-29 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1202f7e6-8e1c-335c-9f2d-18acf2c04154 | -10.05211 | -46.56736 | 2025-07-29 04:49:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7c1450e2-9cd9-3e30-9232-b28756a2730c | -11.74473 | -48.18267 | 2025-07-29 04:49:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 85df1274-f584-3891-aeb5-6deaf2c70890 | -12.70822 | -47.79029 | 2025-07-29 04:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94cbb426-adac-3d3b-86bf-a8bee472b7ab | -9.08392 | -50.84809 | 2025-07-29 04:49:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d33b4e0-2b81-32d3-bb3e-27b9a6cb8e07 | -9.72923 | -48.30024 | 2025-07-29 04:49:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0ce5e08-a2af-3571-a48d-85eeb7b74a99 | -12.00256 | -46.95839 | 2025-07-29 04:49:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6e53b39e-37df-39b3-afe6-ea39d84ebdc4 | -6.89686 | -52.8685 | 2025-07-29 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c348557-59a8-3c44-bef0-d9d0b26dbd83 | -13.49667 | -45.62112 | 2025-07-29 04:49:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f5b51f0-1303-34d9-99b3-8dfefc0fc79d | -6.54689 | -56.19811 | 2025-07-29 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7feba38-07ea-3e85-9a68-2c31feb81cbe | -6.492 | -56.19995 | 2025-07-29 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e968444-313f-306c-b6ce-5d05df8fc3fe | -13.00105 | -44.90217 | 2025-07-29 04:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eda40aad-bd58-39e8-964a-c21d0195c0a3 | -10.5143 | -50.25829 | 2025-07-29 04:49:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bfdcd472-6ac8-344c-bdfc-15d1ab7a09a8 | -12.00046 | -46.97312 | 2025-07-29 04:49:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd84ce8d-ca97-381a-b1cf-f7d838e9e0e0 | -9.36136 | -45.73736 | 2025-07-29 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cf2e80d6-9e8c-3489-b460-ae93826ca425 | -7.4612 | -49.40109 | 2025-07-29 04:49:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3ebff57-8a71-3f18-9f03-c55f59567a2f | -11.68731 | -47.4318 | 2025-07-29 04:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1b71761-2cf9-3e20-b2ef-293731680dc0 | -8.74772 | -48.0439 | 2025-07-29 04:49:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5d6308f-fa02-38c8-948f-db700d116cae | -9.62498 | -48.55047 | 2025-07-29 04:49:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 76b68b53-d051-38fb-b01d-b33a901b9223 | -11.33879 | -51.24969 | 2025-07-29 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 908a751e-da3e-3d2b-b0ea-6f99e60b5a81 | -8.3691 | -51.07712 | 2025-07-29 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04c0d878-f747-3413-8cff-43b83dc89c4f | -12.70751 | -47.79531 | 2025-07-29 04:49:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56c32463-0f3e-3071-833b-7a5df38fec80 | -11.74028 | -48.1868 | 2025-07-29 04:49:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 094b4966-d74c-3644-ab9c-e0106ec67308 | -11.42839 | -45.12064 | 2025-07-29 04:49:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 54476acf-9d67-3ace-98d5-071733096131 | -7.7451 | -51.10315 | 2025-07-29 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abe9eb98-d268-3de7-8822-e3e9ba818583 | -10.62822 | -45.2305 | 2025-07-29 04:49:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf6ff1a4-ed26-3c46-8504-a79f5e54cbe2 | -10.62634 | -45.23291 | 2025-07-29 04:49:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 60e34543-13ca-341a-8cff-c9922ab484ec | -9.21654 | -48.59621 | 2025-07-29 04:49:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4df73ce6-77c7-37bc-a099-f66eb4c53552 | -10.6315 | -45.22888 | 2025-07-29 04:49:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e49f97fe-6316-38f7-be79-ad8f888fe20f | -13.09385 | -47.30616 | 2025-07-29 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 175ce146-4812-3eb8-b3f1-a0f1f90aee03 | -9.396 | -45.49487 | 2025-07-29 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8efa7f30-02af-3659-8add-4fc72bd4e40b | -11.42256 | -45.12931 | 2025-07-29 04:49:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 30.1 |
| baf2e598-7edb-39eb-adae-9e6bd17a3642 | -12.00415 | -46.96521 | 2025-07-29 04:49:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| abc3ebda-7f6f-3b97-a5d0-c47a40dc454f | -7.7346 | -51.10506 | 2025-07-29 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 616c8d0e-f389-3c22-adb5-a19b814ccdf0 | -13.10768 | -47.38548 | 2025-07-29 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93314a59-07d0-38f6-a3c1-27d853d93514 | -11.98048 | -46.96663 | 2025-07-29 04:49:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 288ea6de-c89b-352a-b082-d281b256b585 | -10.5247 | -42.55448 | 2025-07-29 04:49:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| e809259c-0954-3ec7-b12a-0adb37c08dfb | -11.27104 | -44.65457 | 2025-07-29 04:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc94abec-1e5e-34e0-aad2-df98f430e091 | -11.74407 | -48.18737 | 2025-07-29 04:49:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 2af54505-f0a8-34cb-a043-e519b05629fd | -13.09331 | -47.31007 | 2025-07-29 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 943d17c6-a9af-32b6-aca6-5a28b205128e | -13.00722 | -44.8922 | 2025-07-29 04:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1e9796f7-4d05-382c-992e-d1dc202a3203 | -8.9468 | -46.75004 | 2025-07-29 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 82aede97-51d6-3e70-bab0-964283feca3c | -6.50243 | -56.21289 | 2025-07-29 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 922530f7-8653-328e-9665-9d94a69a05f7 | -13.13792 | -47.34543 | 2025-07-29 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d925bcb2-a8ab-34cb-92cf-e9334ff767a6 | -12.00154 | -46.95355 | 2025-07-29 04:49:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d7585feb-553d-3071-8d67-ebf371a59a14 | -13.00242 | -44.89169 | 2025-07-29 04:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6bfc41a9-9ffb-3779-91b2-834f5fd22159 | -10.5512 | -50.24511 | 2025-07-29 04:49:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8a780694-0ed5-3215-bd4d-b043a4ffe72b | -7.72742 | -51.10748 | 2025-07-29 04:49:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c4c5ac03-5b74-3bb4-bbcc-a5b7d36360c8 | -13.11634 | -47.38267 | 2025-07-29 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1c9aa340-e262-352e-adf1-f463efb22b51 | -12.57929 | -49.79804 | 2025-07-29 04:49:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4f048fa-701b-384a-8796-d27f453db542 | -11.34213 | -51.25022 | 2025-07-29 04:49:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 49840b2c-9b06-3b57-9878-d937875424fa | -9.36369 | -45.72111 | 2025-07-29 04:49:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 772d0152-5de3-3572-b7bb-c91a60ec60cc | -9.62488 | -48.55376 | 2025-07-29 04:49:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b70b2522-13e8-3dc0-925f-ccd9647ff60c | -6.90489 | -52.86224 | 2025-07-29 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a5cd878-95cb-351c-93f4-b1be4d7d98b3 | -12.99694 | -44.89638 | 2025-07-29 04:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ec4b0e10-ea7b-3d9b-a6af-8e78aeba5faa | -9.72559 | -48.29954 | 2025-07-29 04:49:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8cf450b-af78-3105-9eba-82ae3c55864e | -9.62549 | -48.54952 | 2025-07-29 04:49:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc5a7a52-c519-3508-8baf-1aa9b18079b3 | -6.49486 | -56.20789 | 2025-07-29 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e996b5a0-4736-34e4-b512-2f7b7be0806f | -6.54808 | -56.1909 | 2025-07-29 04:49:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9956caf7-8da5-33ae-8db9-dddb58b27de7 | -7.46177 | -49.39738 | 2025-07-29 04:49:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4946aa44-7306-3d3d-82e0-22c4752294d5 | -8.95479 | -46.75105 | 2025-07-29 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 683cc1d7-5177-39f9-bd61-62c9f5614da6 | -12.99626 | -44.90163 | 2025-07-29 04:49:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8943654b-2443-36ca-88a7-d7021ddd4992 | -10.00246 | -48.12889 | 2025-07-29 04:49:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0a3b4203-0666-3ade-95ac-0532e856b54b | -12.12338 | -56.91494 | 2025-07-29 04:49:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d55efac6-ef2d-3fcc-a0f2-b3bd94f64407 | -8.94756 | -46.74478 | 2025-07-29 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 89895353-521a-3fe5-9b01-0095fecd417e | -7.81504 | -50.22665 | 2025-07-29 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed7fc0de-38cc-3f55-8dec-aefa6a321e08 | -13.06374 | -47.37451 | 2025-07-29 04:49:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e5262d0f-d59b-3630-8f78-95785905b52c | -10.00047 | -48.13066 | 2025-07-29 04:49:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README19.md)
