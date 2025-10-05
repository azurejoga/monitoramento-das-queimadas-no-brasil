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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 62c393e7-4d66-34c1-8036-aee74ac4f4df | -4.63365 | -43.18404 | 2025-10-05 03:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| aaf77067-a782-3228-a01c-42d19ed3ea31 | -2.68006 | -48.40173 | 2025-10-05 03:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4c7b3358-8325-30b0-8209-5f3cb65a7ea0 | -2.68655 | -48.39128 | 2025-10-05 03:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 82492334-6815-31ef-afe6-3055bbb40d95 | -4.1317 | -47.65785 | 2025-10-05 03:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a84c9f30-f024-343b-838a-d04070312a36 | -3.67077 | -41.75664 | 2025-10-05 03:51:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 97c07291-ee88-3d26-8fbf-2b4bdbef9307 | -3.66853 | -41.76376 | 2025-10-05 03:51:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b006e96f-0750-3ee8-844f-4b3cdb5985ef | -4.50482 | -40.73536 | 2025-10-05 03:51:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9b05eee7-e580-3a40-b9d5-777a0a5916c1 | -4.43704 | -43.24016 | 2025-10-05 03:51:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2df067fc-6df5-3f79-9aa7-8cb49c3743a1 | -3.67004 | -41.76129 | 2025-10-05 03:51:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7b16cca5-6cff-37e5-9a6d-c7ba50f111a9 | -4.44595 | -43.23777 | 2025-10-05 03:51:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 27c76f96-aa6f-3558-bcb4-35544ebdafb8 | -3.87255 | -40.91008 | 2025-10-05 03:51:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 309eb914-5e96-3a50-a48b-a99fc05daf52 | -2.29909 | -47.99386 | 2025-10-05 03:51:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e127087c-e295-3bc2-9dfd-b1e725dcce45 | -3.64267 | -48.32327 | 2025-10-05 03:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a7f4439-0ad8-3a2a-b7ad-920ddd5393c8 | -4.6324 | -43.19147 | 2025-10-05 03:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 641b4d8e-6ad7-3a37-a1df-142942e9096f | -5.09174 | -37.60467 | 2025-10-05 03:51:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a68f1317-5d43-3dd0-a6cc-4523752ad9f3 | -2.88052 | -44.33615 | 2025-10-05 03:51:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba6f9d34-7fe2-3a4a-a8a8-5ac0a2f2bd4a | -3.83647 | -44.55379 | 2025-10-05 03:51:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eec32f9b-31e3-35c4-bb3f-b0744c535eb1 | -3.83397 | -43.50298 | 2025-10-05 03:51:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e139f78-2c1e-36ff-8348-2bc5f6afaaaf | -3.84524 | -41.5856 | 2025-10-05 03:51:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 0324766d-939a-365f-beee-c8ab2e2e5991 | -0.90712 | -47.5494 | 2025-10-05 03:51:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8be849c7-a671-3b02-b411-abebe12a8e48 | -2.90312 | -48.0803 | 2025-10-05 03:51:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 21b228b0-c5df-3fc9-8c35-68f59db64714 | -2.68164 | -48.39249 | 2025-10-05 03:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 445eb298-0b21-3139-b1c3-49bdcb78adf3 | -2.33765 | -45.74507 | 2025-10-05 03:51:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df596335-fe80-34b2-b129-6502a9618c9a | -4.82432 | -42.76971 | 2025-10-05 03:51:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 62b09ec6-1585-3c50-84aa-218e87fb7d69 | -4.22676 | -46.76187 | 2025-10-05 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| dcba62cd-aa43-3d68-b72d-4f3fd87ac95a | -3.8445 | -41.59018 | 2025-10-05 03:51:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 70438582-0be6-38ae-a3e4-0da4fe989d7b | -4.23263 | -46.7593 | 2025-10-05 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 17c27927-562c-3d9a-aad8-92d29b24e35f | -3.64862 | -48.32413 | 2025-10-05 03:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 184bdd40-7a8c-3ebc-ad3e-718bac14fb71 | -4.94512 | -42.57466 | 2025-10-05 03:51:00 | NOAA-20 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 55a8a281-9326-3d17-86ba-d5d32b235519 | -2.91469 | -40.46541 | 2025-10-05 03:51:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 913145a1-f3dc-33a6-a47e-afe54f727b91 | -4.63302 | -43.18776 | 2025-10-05 03:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 76feb953-ca81-3463-98fd-d4dd5731d02a | -5.26359 | -39.26894 | 2025-10-05 03:51:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 472c8f93-5661-3ec8-8c4d-16582f169a5a | -4.13734 | -47.65871 | 2025-10-05 03:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d3c050b1-2bae-3bcf-9494-00430a71ea41 | -3.77057 | -40.79922 | 2025-10-05 03:51:00 | NOAA-20 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e37ae6b7-c7dd-3f26-a774-ce81f427be4a | -3.09132 | -47.02125 | 2025-10-05 03:51:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 399996ad-5ff5-35b8-b3bf-3ae50f95007c | -4.6495 | -43.19049 | 2025-10-05 03:51:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 72851576-9de8-3b82-b061-c340534fe213 | -4.82947 | -42.76348 | 2025-10-05 03:51:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2353c283-1136-34a5-887b-3d939d1a878e | -3.6693 | -41.75911 | 2025-10-05 03:51:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 25ee7409-86dc-3357-a498-6d9d7087d4ce | -2.68689 | -48.39808 | 2025-10-05 03:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 668aadd5-9b94-3ac1-8288-115002b85ad7 | -2.68503 | -48.40056 | 2025-10-05 03:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b13454f8-4d4f-3826-a557-a6aa8d166aeb | -4.50839 | -40.73595 | 2025-10-05 03:51:00 | NOAA-20 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7d7f4e8b-caab-3339-9165-be2625fdd581 | -0.90871 | -47.54947 | 2025-10-05 03:51:00 | NOAA-20 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 901cb40b-dd30-3aa6-9b9b-2b59a34cf5f3 | -4.4309 | -40.76926 | 2025-10-05 03:51:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 477be378-66b9-3983-a70c-073dce261ff0 | -4.13671 | -47.66238 | 2025-10-05 03:51:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 56f3c9b7-1e3d-304d-b123-8b33371e1303 | -3.4407 | -43.3399 | 2025-10-05 03:51:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 81cd2358-e9bb-3645-9999-79f584dcbf83 | -4.57614 | -41.30806 | 2025-10-05 03:51:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5f272c4c-dd35-34e4-9f34-ecf4fd0b40ed | -4.43766 | -43.23642 | 2025-10-05 03:51:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2e1e60ef-cfa7-354a-ba0e-834a996dfcde | -3.67311 | -41.75975 | 2025-10-05 03:51:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 53338a76-5086-397b-8cab-8fad4438bbc4 | -4.44658 | -43.23402 | 2025-10-05 03:51:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| d28d4195-7130-3650-88f8-6d492e7699b1 | -4.27004 | -41.76314 | 2025-10-05 03:51:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 65c9a3b5-2b33-3f16-b38d-85fdd6f831c8 | -5.26598 | -39.26546 | 2025-10-05 03:51:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 18ea7eef-f47e-30a8-b4ab-3d64715f7fc1 | -4.23208 | -46.76259 | 2025-10-05 03:51:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 41b8be5b-b1f6-3b22-8466-83c2567ec4ec | -3.8319 | -44.55299 | 2025-10-05 03:51:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 1c017a06-9f03-3a3a-b047-5dc40abb4a05 | -4.82489 | -42.76629 | 2025-10-05 03:51:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 07358777-995e-3fe8-9e5f-a649db339b41 | -6.29296 | -43.9167 | 2025-10-05 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 82a517ac-7fbd-36dd-b373-40d3fc3a309d | -5.84248 | -42.86499 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d77066c6-ff60-384e-a8d6-65d08bf8f240 | -5.97025 | -44.35756 | 2025-10-05 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64d6cfd5-6104-351b-aa20-60dbb4020ac3 | -11.13067 | -43.37097 | 2025-10-05 03:53:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0294956d-0aee-32f2-ae87-16e288d64fde | -6.62891 | -42.41855 | 2025-10-05 03:53:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9a081155-cb07-3f6d-a1e5-45a7eda29c3e | -7.72003 | -42.39367 | 2025-10-05 03:53:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 257fec1e-dbd2-382b-8ef0-35162dd32117 | -6.12644 | -42.87185 | 2025-10-05 03:53:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 4bb0a82c-3e2f-3ee3-8984-488541456302 | -10.28122 | -44.35286 | 2025-10-05 03:53:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb9eb1a7-3da7-3a73-8a73-078aef53bf75 | -9.12385 | -44.39773 | 2025-10-05 03:53:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9bbdf341-9fd8-3dcb-883f-172d90511ef4 | -6.62589 | -42.4132 | 2025-10-05 03:53:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| efb01098-3ae3-3bf7-b7ea-39bd61401f15 | -7.43802 | -46.5219 | 2025-10-05 03:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d91aadb4-d3ff-3188-9775-dfbe0d4b7212 | -6.40277 | -43.48912 | 2025-10-05 03:53:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3041cb0d-52af-3116-8636-0bc3f087e979 | -9.55006 | -42.96038 | 2025-10-05 03:53:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cb2747ba-f566-3a73-b9c0-d809846d6989 | -9.29458 | -45.99497 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d0c81f02-267d-35f6-b3d2-ecd4d4a831af | -5.18148 | -42.87611 | 2025-10-05 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32e2c1ee-3bd7-3f5e-a4a4-f6175023dffe | -8.59926 | -46.2763 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 6cb5f31b-6e8f-3814-b3bd-cb918ec0cc44 | -9.90573 | -45.95381 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ec3748c9-89ef-3e70-b790-3795a129e381 | -5.94557 | -42.87381 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6cf60cf7-29df-3267-a945-b417923d21a0 | -7.61057 | -45.47017 | 2025-10-05 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6e592121-234a-3e77-8b80-d7f387fa31d0 | -6.98952 | -44.20995 | 2025-10-05 03:53:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9222c08b-e710-3c30-805f-bbde4dc874f2 | -9.57766 | -46.12407 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 430838d2-cf63-3608-935b-e05c9f467807 | -5.58955 | -43.40821 | 2025-10-05 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab57d5e4-6bb8-31d6-85da-ed938d035dad | -5.77749 | -42.93669 | 2025-10-05 03:53:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| f5d32b86-2c80-3db1-bd43-c9f7141fc6f7 | -8.53938 | -46.30818 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 95cb1ab2-6e01-3d65-b469-a1b2d2eccba1 | -7.61139 | -45.46531 | 2025-10-05 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 989f1ee9-b17a-3ac0-a7e2-cf4b2ddeb6f6 | -7.29146 | -39.26816 | 2025-10-05 03:53:00 | NOAA-20 | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2f68eff7-4f23-30c6-8714-7996981ec59d | -7.51165 | -41.27453 | 2025-10-05 03:53:00 | NOAA-20 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| e8be73c3-2388-3069-bf28-da1d72d71265 | -8.54952 | -46.27803 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| da17791a-6610-3b03-960d-5b938a88edeb | -8.58417 | -46.33353 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 781cc95b-fef7-395f-8da0-063bbfc4cda2 | -7.76818 | -44.14868 | 2025-10-05 03:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b8d93a85-6d7b-34e9-8d3b-8905aa7d4040 | -6.69466 | -41.95642 | 2025-10-05 03:53:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6d5fee30-8414-3608-b090-f31031f1c893 | -4.31338 | -48.09115 | 2025-10-05 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| b6fe3eef-774b-3dc6-a139-294e0d291923 | -8.4602 | -40.61769 | 2025-10-05 03:53:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cd2d22e8-33fd-3253-b394-e3cd8e8c639e | -10.11687 | -45.69276 | 2025-10-05 03:53:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cdc37e67-2f80-33a4-89d1-1dda5f36534a | -5.25962 | -43.16261 | 2025-10-05 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af73fba9-5d8c-3c25-809f-fae89a647c6f | -5.85256 | -42.80371 | 2025-10-05 03:53:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a39e7a1c-ae66-3a21-947d-0007d58d179c | -4.31845 | -48.09628 | 2025-10-05 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 80309640-8344-3864-ad50-c6c82b5df1f5 | -5.24065 | -42.63893 | 2025-10-05 03:53:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 57eea40a-0849-3403-990b-a8122326527a | -5.89823 | -38.47814 | 2025-10-05 03:53:00 | NOAA-20 | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3694b660-c74a-38ba-97cd-4d6c8aa13892 | -6.72169 | -42.16327 | 2025-10-05 03:53:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 50cf69bb-bae5-3ac4-a916-a8c276192164 | -6.63295 | -42.8004 | 2025-10-05 03:53:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 356f3957-664c-350f-9077-4c3ac227732d | -6.14394 | -44.66166 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| c9a1f392-4c3a-364b-b14f-5a5daa4d6235 | -6.46029 | -44.58255 | 2025-10-05 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| af8c7e53-253c-30cc-9aff-c4346c0c010a | -9.30181 | -45.98103 | 2025-10-05 03:53:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a597006d-e735-35e9-8205-608e0fe08636 | -7.79441 | -42.57383 | 2025-10-05 03:53:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 12049531-b722-3ddd-b82b-ca0f79ca8b2a | -8.54144 | -46.3247 | 2025-10-05 03:53:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |


[Clique aqui para ver as próximas entradas](README39.md)
