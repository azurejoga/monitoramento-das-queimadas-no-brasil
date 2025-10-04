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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47314854-ff81-308e-87cd-30ffcd9562fe | -3.8459 | -41.58894 | 2025-10-04 04:12:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 24180a20-2d47-3a87-80f8-f60a6070e254 | -6.19997 | -39.69828 | 2025-10-04 04:12:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6b1b2dd8-4637-3cf2-ae42-b81af5690893 | -4.61423 | -43.15726 | 2025-10-04 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0b5eef16-e633-3a32-a585-5a19f62585a2 | -7.02502 | -45.9547 | 2025-10-04 04:12:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 76f367b2-74f9-3546-aadf-15e74ede315c | -6.43582 | -44.45867 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8fd12e51-d46c-3e48-bf5f-0c4d4d641d09 | -5.93148 | -47.31577 | 2025-10-04 04:12:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 359f0035-769c-3160-be9b-cd986ff18993 | -6.23556 | -44.26449 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3e80c90a-d6b7-3ff3-b54e-acc2e293f6e2 | -2.90054 | -50.73475 | 2025-10-04 04:12:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94164a4c-9bd5-3d13-ae56-5a2a7dbf8fff | -5.33135 | -43.34897 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7c953135-cbe9-3826-830e-14e743a9a914 | -6.35422 | -43.43289 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77941e5a-75c0-376b-a78f-71c1304d20cc | -5.67564 | -44.19442 | 2025-10-04 04:12:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4f871fa-8ad5-3cb5-b430-d81dbe6e8d06 | -6.29148 | -42.45203 | 2025-10-04 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 45c344b3-2c4d-32e7-af20-ae207fa1f1aa | -4.65381 | -47.54905 | 2025-10-04 04:12:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f93d409e-2356-39f0-8029-d0b2b6cd4363 | -5.29856 | -43.1055 | 2025-10-04 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d59760c8-e166-379f-985b-c85b1ff5b367 | -7.45835 | -47.18607 | 2025-10-04 04:12:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 389a8bb2-4899-37e6-8fba-a44e3085acb9 | -6.22932 | -44.65702 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 802d02fa-50ea-3c2b-a48a-2624ac0e5565 | -7.02697 | -46.98166 | 2025-10-04 04:12:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 668da246-ca6f-37b9-846c-7436fc6dce01 | -3.9452 | -50.62396 | 2025-10-04 04:12:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5ce37f1-df46-378f-821a-c76303cf8499 | -5.73503 | -42.92393 | 2025-10-04 04:12:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 93962dd8-691b-3fbc-82b7-e887902d7016 | -5.79016 | -45.77538 | 2025-10-04 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a7be2bed-fecf-33be-aac5-c13ab97628ac | -7.54098 | -42.4077 | 2025-10-04 04:12:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a0920a49-7b0a-3d56-a28f-63615581b877 | -6.28595 | -42.44404 | 2025-10-04 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bbf9fa1e-4f2a-3c06-8cf2-a89b6a8e5c7c | -6.29599 | -42.48823 | 2025-10-04 04:12:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cc541dd6-8e23-3372-ba52-bee87834ba21 | -5.42888 | -47.09624 | 2025-10-04 04:12:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b4c8ec5a-5afb-3ebc-b7e0-9cec0d63cad6 | -4.43262 | -43.2315 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a764673b-196d-3d69-bca8-efcc03ffb1c8 | -7.37063 | -39.20287 | 2025-10-04 04:12:00 | NOAA-20 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| d8ca724a-2333-3246-8f2e-db53d1c0ac7b | -5.25681 | -39.26456 | 2025-10-04 04:12:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ba57f178-6d81-31c7-8707-8175e75ee4b2 | -6.00785 | -44.57385 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d9f7caae-79b0-38f9-9779-f308fc50331c | -7.50899 | -44.26709 | 2025-10-04 04:12:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7397b199-2f0c-3cf2-aa33-4c73860f2c76 | -5.66778 | -42.70468 | 2025-10-04 04:12:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 6c0bc988-6d49-3d4b-85bc-cf64c7f211f3 | -6.88341 | -47.23459 | 2025-10-04 04:12:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 07cd2f32-c775-3024-aa4b-957778d898ce | -7.69731 | -42.58324 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 00bbf1ae-8241-321b-b259-9932216ba0fa | -6.34481 | -43.40653 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ef04b6d2-ee86-3d8a-a78b-a3101f573529 | -5.98864 | -43.03802 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9b9910ab-70a5-31af-aeca-876a1137407c | -5.23337 | -43.70933 | 2025-10-04 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 559ce23d-b213-370b-a5cf-59e9894dd326 | -6.65003 | -41.95942 | 2025-10-04 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d93db09e-bcea-30a3-b7b1-ecfab459a526 | -4.95184 | -45.06933 | 2025-10-04 04:12:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7e0e49e4-9a52-322d-8a6b-7587c46fe3ca | -5.6739 | -42.73039 | 2025-10-04 04:12:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5a6ea76e-074d-369f-9ce1-461a2dece673 | -3.663 | -50.27635 | 2025-10-04 04:12:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 39974c1a-700e-3df3-9208-c24ea4cb4208 | -3.64486 | -48.32136 | 2025-10-04 04:12:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 832fbbf3-17de-3a08-bc56-eb1e7a17c13f | -6.64779 | -41.95174 | 2025-10-04 04:12:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7cec7475-1fb1-3217-99ed-c2795269577b | -5.71556 | -42.63797 | 2025-10-04 04:12:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5fb16ef1-5e28-3ea9-8546-ec7d8a95a4ab | -6.33876 | -43.44466 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b199290e-da95-31ac-91ee-c15139f68727 | -5.32914 | -43.34152 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d777f8f3-6247-3a78-8626-41a6aeaf6d5f | -6.01294 | -43.78654 | 2025-10-04 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ec6e65a-7f85-3502-ad9c-47892624c38b | -4.44426 | -43.24401 | 2025-10-04 04:12:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 30.3 |
| a1a62465-52db-383f-8d3e-9529cc178d06 | -7.72388 | -42.58742 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c7e16ea2-3d03-363c-b811-38f411db8297 | -3.35955 | -40.71982 | 2025-10-04 04:12:00 | NOAA-20 | URUOCA | CEARÁ | Brasil | 2313906 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 74eb3254-061a-37ec-ba9a-2cfa99bb32f5 | -7.45989 | -47.17688 | 2025-10-04 04:12:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d69fd551-9152-3c1b-9158-bde374e2d650 | -4.70036 | -48.1716 | 2025-10-04 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 431b8aa0-74fa-35da-aa36-ee3f9a148064 | -6.34757 | -43.41052 | 2025-10-04 04:12:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 143637c4-0b58-3d06-9814-154630672cf9 | -5.68768 | -43.02959 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e2ed1839-7726-3458-ad57-7cafc0fcac13 | -6.29511 | -43.65503 | 2025-10-04 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 370d5b0b-d8f3-340a-ae69-a715058434dd | -4.21495 | -51.12648 | 2025-10-04 04:12:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 380320c2-5f78-3cd1-830e-85501daca709 | -7.79159 | -42.56576 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 98338340-d7da-3250-ac0a-bca38adf94d8 | -6.70482 | -42.82576 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3aaa5b7e-7f18-3ea0-ad77-bf9ad8a709b2 | -7.71389 | -42.56432 | 2025-10-04 04:12:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7189425f-9ac6-383b-839e-520a2820466a | -6.71249 | -42.79859 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| fb88e12f-210f-3e3a-b17a-65e15867bedc | -5.91113 | -49.29904 | 2025-10-04 04:12:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed515726-2259-3598-8711-61897df558b9 | -5.60878 | -45.19516 | 2025-10-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 550db845-7cad-30c7-bfeb-4e1e0c75a694 | -5.88308 | -44.25687 | 2025-10-04 04:12:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1125d7c-e296-3de9-ba35-9707a1cf7b28 | -6.24571 | -44.24401 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d744f1f2-ed5e-32bf-a049-ecf87eb60637 | -5.41268 | -41.34291 | 2025-10-04 04:12:00 | NOAA-20 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a18a0290-97db-3684-8c11-3bd79c4a43bb | -7.4319 | -46.96949 | 2025-10-04 04:12:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee2cfa43-0aef-3167-b1f3-00da17978347 | -6.77172 | -43.60678 | 2025-10-04 04:12:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7107f10b-facf-3135-a9d8-d151efb92800 | -5.73725 | -42.93135 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 3a51e50b-0690-39c4-86d6-ada0c666df87 | -5.85528 | -45.81852 | 2025-10-04 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69cb0b05-8d7a-367a-a7d1-b413c6945ae7 | -7.79601 | -42.55927 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 847b3ac4-7eda-3bcf-813d-f818df331c45 | -6.35366 | -44.37943 | 2025-10-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c7169a8-6159-33d4-9636-ec950cfc5406 | -7.05048 | -42.7667 | 2025-10-04 04:12:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7c62857f-c2bc-3ae0-bc27-a28645cfdcb8 | -6.69656 | -42.83511 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| d462858e-9500-3cc3-8d14-f09c9df127d2 | -5.67336 | -43.03442 | 2025-10-04 04:12:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fc2fae3a-070a-3018-894d-39af5c808b27 | -6.87121 | -47.23729 | 2025-10-04 04:12:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 620f142f-c405-300c-91d6-f6f7d5605e8b | -4.16252 | -42.16705 | 2025-10-04 04:12:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f20fc37e-fb34-3316-955e-d63da10f6973 | -7.47235 | -43.04291 | 2025-10-04 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 380e29db-4c0e-385e-a532-b5b2da881a97 | -7.72666 | -42.59143 | 2025-10-04 04:12:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ab94435c-61eb-3214-99db-366c27b1e173 | -5.72666 | -44.51003 | 2025-10-04 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8548f83f-4c02-3b77-98f6-270e7ef53d72 | -5.32495 | -43.77466 | 2025-10-04 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15f8c50d-ee73-3dc1-ad8e-64c4ae016bb7 | -5.64986 | -43.58898 | 2025-10-04 04:12:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bfa3ead3-2a5a-3a97-918c-1a3ce3874180 | -6.376 | -43.89445 | 2025-10-04 04:12:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| c4596cb0-e6e3-3a11-affa-5e512c15c714 | -5.71834 | -42.64188 | 2025-10-04 04:12:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a758addb-5df3-3ee8-9729-58d02967388c | -5.83517 | -44.98763 | 2025-10-04 04:12:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d65af926-62a2-3831-8d0f-e674c5af470e | -6.87802 | -44.4992 | 2025-10-04 04:12:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| e654d255-4687-3bab-8254-80f97d68876b | -5.3828 | -45.93692 | 2025-10-04 04:12:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f144fc4-2413-3d30-af3a-7865266c5379 | -6.17041 | -43.92723 | 2025-10-04 04:12:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5ea48b10-c0e9-3be4-84c7-20c82711e02b | -5.13697 | -46.04233 | 2025-10-04 04:12:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 18476ccf-58b1-39e1-87dd-203badbe810c | -5.87859 | -42.52908 | 2025-10-04 04:12:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 08013edd-7b6d-3470-a958-f226752ea027 | -6.09405 | -43.48791 | 2025-10-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a579c070-0b48-33de-92dc-2aa518e0bc02 | -6.72615 | -45.96744 | 2025-10-04 04:12:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 27580e32-0c78-3d13-ae03-33bc63236d0b | -5.45989 | -43.15965 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ae000056-a899-3e20-82b5-e72fd5e521d5 | -5.78237 | -45.77827 | 2025-10-04 04:12:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89d96c0d-3a70-37f3-abb6-c3cb52d149ea | -5.97439 | -44.15021 | 2025-10-04 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0ca4d32c-e10b-3bc5-a373-6d34e3b24923 | -5.64974 | -41.23865 | 2025-10-04 04:12:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4b01f96a-0797-395e-b88f-c964f50a19c2 | -6.70068 | -42.6796 | 2025-10-04 04:12:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 23cc4da5-7c57-3b62-8ad3-d436eafdcfc5 | -5.67059 | -42.72987 | 2025-10-04 04:12:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 86719115-025b-3939-9d1f-e62d058ab61e | -5.32803 | -43.34845 | 2025-10-04 04:12:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9737579d-cff6-34b2-97fc-0d6dc3baba07 | -6.66018 | -42.82936 | 2025-10-04 04:12:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9780c522-daf3-318c-80ae-573706dfafa4 | -4.60593 | -43.14529 | 2025-10-04 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 92aad416-b0d8-30e8-863f-073471a86865 | -4.26091 | -48.5551 | 2025-10-04 04:12:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52343195-4b66-35c8-ba52-794fa25bf28b | -5.90921 | -42.53009 | 2025-10-04 04:12:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README64.md)
