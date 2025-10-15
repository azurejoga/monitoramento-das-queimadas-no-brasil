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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f712495-c62a-3aa8-bb2d-65d451d676cf | -4.90127 | -43.45068 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| c4a1a297-97b5-3372-ae93-8cc5e38751a7 | -2.87353 | -50.73049 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bc97b1cf-9246-378e-a08c-5728f839cac7 | -2.95374 | -49.33809 | 2025-10-15 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc0f5d2a-ea94-3c36-9f43-f9274f0a7b30 | -4.72581 | -44.82117 | 2025-10-15 04:55:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2cd1c3b5-cdd4-3ce3-a26e-badd7b0ec858 | 1.85899 | -55.70422 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ea796777-0598-3fa2-a6ea-83ea498d05e0 | -2.88698 | -50.7366 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f22f43c3-e961-31cf-9390-10f413a4decd | -3.78505 | -49.42646 | 2025-10-15 04:55:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3e0bc748-6903-37bb-b8bd-446fdf86f5ba | 1.08151 | -51.01489 | 2025-10-15 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 129c8e04-1994-3965-8469-d143802f9223 | -4.54855 | -45.41946 | 2025-10-15 04:55:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6571b235-b06b-35e4-8d24-a5f27a0d825a | -3.09766 | -50.38282 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0d8157e-f505-3f71-bbd7-4c001ec37542 | -3.0983 | -50.37875 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36028810-6c50-3539-b760-68cc1f1c93e6 | 1.07595 | -51.2197 | 2025-10-15 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d36a790-678e-31d9-a3ed-4ddcc2c6e101 | -4.8885 | -43.45547 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| daff90f1-e287-32ab-a4ef-07997edb978c | -3.83656 | -44.55088 | 2025-10-15 04:55:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a4334e73-2571-3d0b-859c-6d5da0d88665 | -4.25476 | -48.54959 | 2025-10-15 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8eeba469-db8a-37b6-afb6-9a787c78ca87 | -5.05733 | -44.46484 | 2025-10-15 04:55:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0df6561c-6c24-34b8-ad98-7bc3eefa7230 | -3.05368 | -44.46626 | 2025-10-15 04:55:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d346ae79-25ef-3592-bf23-5e9123e8d10a | 1.08488 | -51.01436 | 2025-10-15 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 97444f61-1b17-32d8-b42c-8e6820522076 | -3.07068 | -49.5127 | 2025-10-15 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9c33028e-9ce8-3ac4-bfa4-73540e947812 | -4.80331 | -45.71391 | 2025-10-15 04:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39648762-b3b7-38e4-8a54-ab62baf7ff32 | -2.24335 | -47.87564 | 2025-10-15 04:55:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4866e94d-7e4a-3462-9c49-65982d3d271c | -0.90072 | -47.55105 | 2025-10-15 04:55:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 8913ae82-ae47-3da8-9b01-77e807449e0f | 1.75883 | -55.78698 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c4623f7e-9c0c-3a69-a67f-812d02128df7 | -0.89776 | -47.54298 | 2025-10-15 04:55:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| fc4cee3a-1539-3718-b9a1-92de0c88d0da | -4.35983 | -46.77859 | 2025-10-15 04:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4c6ebee1-9f4b-3371-be44-f0d2315a0619 | -3.12644 | -50.20754 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93a75287-4da4-3408-bf77-e07ac4944c73 | -4.88294 | -45.94578 | 2025-10-15 04:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45645610-3faf-3bcc-87c8-23267dfe15da | -4.64935 | -43.13272 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7e0e47b6-26c9-3ff9-9338-ee93d1f9c177 | -2.30526 | -48.57336 | 2025-10-15 04:55:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef72a981-9e99-32ed-9344-7ee9be9a04a3 | -3.09866 | -51.29728 | 2025-10-15 04:55:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a27f900c-7465-35c7-82db-39d3b125c8be | -3.45963 | -51.09405 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec09888e-0e24-3eee-a0aa-5497fd586cc5 | 1.78953 | -55.76624 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6fc1c151-0cf3-3c6c-821c-ffaa0a31590f | -4.28244 | -48.58665 | 2025-10-15 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| abb5dc30-2007-3927-ae9a-64c18f994e40 | -3.12582 | -50.21172 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 45f1d94e-976c-33ab-83f9-468ac5e0c66a | -4.8583 | -43.2081 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 21e8fa67-3089-370c-9eec-6b5139f34c64 | 1.07256 | -51.04554 | 2025-10-15 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a668f8b3-0323-3fd4-b87c-f5323d94f5ab | -2.64513 | -49.52997 | 2025-10-15 04:55:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5154228b-00f2-369c-91b6-e8e49fb3a4ac | -3.59726 | -51.06769 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 571bcfbe-b2f7-322d-8166-6cb43c3c67e0 | -4.76861 | -45.73569 | 2025-10-15 04:55:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 56d623d8-975c-3300-9e9a-9c3719ba0ef2 | -3.04888 | -44.46218 | 2025-10-15 04:55:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 732c3b36-b7f0-3de7-ba7f-bfbc17783bc8 | -4.4228 | -47.75374 | 2025-10-15 04:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 159f3d9e-fd33-3b29-af60-aa6f45eea775 | -3.94125 | -47.56221 | 2025-10-15 04:55:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 900815db-fec5-3508-a39a-d82312a470e6 | -3.83802 | -44.54099 | 2025-10-15 04:55:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e6b329ca-e132-3798-909c-c60aab990b36 | -4.86982 | -45.6758 | 2025-10-15 04:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 940b86c2-f102-3ad6-bff2-a1561812bbee | -4.82552 | -45.4485 | 2025-10-15 04:55:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a30e75c-0ec5-37e4-9c3b-0d599bf04984 | -3.78544 | -49.42844 | 2025-10-15 04:55:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0c313fdc-0f6c-3ab2-8557-ed476542744a | -4.28702 | -48.58364 | 2025-10-15 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0a3e78e6-029e-37cd-ab73-bc230c340b35 | -4.64875 | -43.13699 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 38bd3166-18eb-3745-980d-774a39216101 | -4.13988 | -42.20849 | 2025-10-15 04:55:00 | NOAA-21 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f658c20a-cb7c-3fbc-b42a-55251f58613a | -2.44037 | -49.37367 | 2025-10-15 04:55:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f0c9ff37-a626-375c-af24-a083badaf218 | 1.85814 | -55.70359 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd36499c-dba4-3fae-a1de-c856340b5232 | -4.65705 | -43.12078 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 5ea41a66-4609-3a37-b600-201443903943 | 1.8015 | -55.74695 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 02bcc564-865c-3ac0-b2ad-b1702309d8ab | -2.88286 | -50.73999 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d50f491e-964e-33aa-a4fb-3835a6ccc3f4 | -3.05847 | -44.47034 | 2025-10-15 04:55:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ed56057f-e374-38ab-8f9d-2e7f1149dbd9 | 1.08152 | -51.03684 | 2025-10-15 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9086d961-5278-335a-a34b-3d468d3d94d7 | -4.89962 | -45.50764 | 2025-10-15 04:55:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1aacd55-92f5-3292-8cbe-f1806e66ac71 | -4.66173 | -43.13028 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 5c249098-7f6b-3807-bea5-c13bac27d5ea | -2.53148 | -47.81091 | 2025-10-15 04:55:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8f46c36-aba4-3896-9f59-cd6f65e5b6ec | 1.85851 | -55.72963 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f4dd722e-805c-3d06-94b7-579158f58449 | 1.29861 | -51.25006 | 2025-10-15 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9b2fb730-2886-3994-99d7-d5e7f0641b27 | -3.83753 | -44.5443 | 2025-10-15 04:55:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 490805b0-126d-332d-ac02-67b08d46247a | -3.60022 | -48.98849 | 2025-10-15 04:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed7b83c7-809d-3707-aba0-d3192595c667 | -4.35246 | -48.19929 | 2025-10-15 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b946716-9838-3a85-96ac-3dc2b4d9de21 | -4.88367 | -45.94066 | 2025-10-15 04:55:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ddb239de-a0c6-31fc-b02d-b7533780b02d | 1.78888 | -55.76197 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 30448dab-6c06-3d63-8817-8fcc617f505d | -3.11647 | -46.77807 | 2025-10-15 04:55:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d692878-7f3f-3fed-9362-9fc7576f8aa2 | -3.07955 | -49.50488 | 2025-10-15 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8f51596e-8ac3-36b6-bf38-5b722cc0684f | -2.24746 | -47.87627 | 2025-10-15 04:55:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 02161260-13e2-3093-b6cf-47c9ff20b4bd | -4.25283 | -45.58229 | 2025-10-15 04:55:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c189898-92fb-347d-b3ad-6c52f4f00189 | -4.88803 | -43.46097 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b7462f94-7f4d-38aa-8b00-0cf9311243ca | -3.42466 | -50.25947 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74623897-7885-3ff0-9247-847f2db46c63 | -3.07124 | -49.38179 | 2025-10-15 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8279ea8a-5c51-3fda-b098-6d583be14858 | 2.05109 | -55.83446 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| aca37061-e18c-3b8c-8362-3fda9ab7380a | 0.98435 | -50.0639 | 2025-10-15 04:55:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc3a82cb-5c9c-36e3-a455-4e3e9f310630 | 1.0748 | -51.03788 | 2025-10-15 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56523a5f-77dd-3c9e-a1ef-c197f53ccc77 | -4.14364 | -41.66043 | 2025-10-15 04:55:00 | NOAA-21 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 0d6696a7-aa60-35e7-8a5a-ebdc66cc90ce | -3.61002 | -48.92393 | 2025-10-15 04:55:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| acaa369e-fe71-3569-883f-a26631cf73fa | 1.81077 | -55.75864 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 91952f6a-1d40-36fb-996a-f7af744531b0 | 1.07929 | -51.21918 | 2025-10-15 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb07859c-ca10-3a4e-b882-83191964f90a | -3.61243 | -50.5878 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb22d248-fb5d-389c-9ce4-22d3d6f2895e | -4.90707 | -43.45154 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 0bb2e8fd-9e49-3ea3-b2bb-75902e99546b | -2.87995 | -50.73551 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70bc0f4d-535a-3a38-b422-36e3607e8db7 | 1.76762 | -55.76947 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a99072c-bff0-32b4-8cb9-ce242b713b68 | -4.30896 | -48.23549 | 2025-10-15 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fbbf6f62-7584-3e1c-bcd0-788e2922fc33 | -3.13367 | -50.20872 | 2025-10-15 04:55:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cfb6be42-2982-3a10-8498-c0e5ab6cc273 | -4.32017 | -44.54146 | 2025-10-15 04:55:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 26d7898d-7c51-3a54-bca1-a6fb86dbc802 | -3.0532 | -44.46951 | 2025-10-15 04:55:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9f52163a-a644-3d7c-8204-ef2244780ae8 | -4.85889 | -43.20394 | 2025-10-15 04:55:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ba40bc89-e68b-38db-8f34-bd62ba38e51f | -2.4474 | -49.00227 | 2025-10-15 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e82a1854-30ed-3d28-8076-d039940bf8cd | 1.80763 | -55.86001 | 2025-10-15 04:55:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 14e09154-a040-380e-9d53-c74911ced58f | -2.44788 | -49.37484 | 2025-10-15 04:55:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c05d9ca-4041-3b3a-8556-3b29ec2715e9 | 1.87395 | -55.6802 | 2025-10-15 04:55:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f550657-15af-3a1d-a291-ba3ec9341e08 | -2.44582 | -49.00381 | 2025-10-15 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8f8ea5f-2af5-3212-b867-34929fc75f20 | -5.00862 | -44.49542 | 2025-10-15 04:55:00 | NOAA-21 | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cead9e1f-8ca6-3c6d-be26-a78d3f6cdfe1 | 1.01106 | -51.08419 | 2025-10-15 04:55:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8d7891bc-2989-3db2-a50e-064619d58d24 | -3.43021 | -50.2475 | 2025-10-15 04:55:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1ac6cac-0f81-3efb-b284-9bb340703b2f | 1.33628 | -50.73235 | 2025-10-15 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 110e96ec-0e68-32f7-963f-c0317c6b4df5 | -3.07649 | -49.49977 | 2025-10-15 04:55:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 227c5711-1ddb-3505-bf0f-5e4a83c5f165 | -4.52599 | -48.04867 | 2025-10-15 04:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README42.md)
