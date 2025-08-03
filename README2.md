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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b19a0968-3eda-3dd0-acf6-53b66a861619 | -6.51638 | -42.80563 | 2025-08-03 00:09:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| f693e201-b3bb-3abe-9123-f036f770a4ba | -7.12336 | -44.08801 | 2025-08-03 00:09:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 75eac5f3-7ad6-32ca-b181-be463c1746da | -8.00098 | -43.16644 | 2025-08-03 00:09:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| b0bd5194-eee6-31e4-8faf-be4baf365f7a | -8.00885 | -43.15544 | 2025-08-03 00:09:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 243.8 |
| 17a07930-157b-3be5-a621-d51baa42f094 | -7.8882 | -45.52142 | 2025-08-03 00:09:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 25.7 |
| e0632371-ab80-37c9-a58c-faa5962aef79 | -8.04855 | -43.11427 | 2025-08-03 00:09:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| dce75fb2-0339-3815-962b-404fc4a91cca | -8.03403 | -43.14571 | 2025-08-03 00:09:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 35b6137b-28f4-3208-ab60-386af394844f | -8.04727 | -43.10467 | 2025-08-03 00:09:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| d1f38fbc-8e99-3780-97b2-90cffb2154d2 | -6.35745 | -46.15627 | 2025-08-03 00:09:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 19.0 |
| b525cd2b-5f77-319c-ae03-f27c4f3321ed | -8.02461 | -43.13362 | 2025-08-03 00:09:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 46.4 |
| 742c7db0-bdec-3508-8f56-a5708d50c8d4 | -8.03809 | -43.10594 | 2025-08-03 00:09:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 213156b4-5a2c-3bb4-878e-f8f5366f671b | -6.68076 | -44.36103 | 2025-08-03 00:09:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c8fbbe4a-7746-3535-806a-aa3d8a420c35 | -6.49871 | -42.81457 | 2025-08-03 00:09:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 1ba0d38c-a2c7-3548-a7eb-f7a87925847b | -7.96556 | -45.12151 | 2025-08-03 00:09:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| ee5d300f-f5fd-3120-bde8-dd49f7f9bc5f | -8.0128 | -43.18447 | 2025-08-03 00:09:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 158.5 |
| a13ce176-b947-3e19-8b98-26d4ef36345a | -8.94968 | -46.75042 | 2025-08-03 00:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| b74d3599-ffa7-3a67-9d4c-490b0e66278d | -6.35928 | -46.17021 | 2025-08-03 00:09:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| ab97d4fe-72db-3521-86f7-175e0323c72a | -4.55419 | -44.20833 | 2025-08-03 00:09:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| fe0a8c2a-82e6-3baf-a727-eafd9c55bc09 | -8.03147 | -43.12644 | 2025-08-03 00:09:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 77e38614-533d-3405-a3f8-defc4c715dfe | -3.81005 | -42.54165 | 2025-08-03 00:09:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| ec36fe05-e654-3bd4-8258-a761a69f773b | -5.89024 | -46.52914 | 2025-08-03 00:09:00 | TERRA_M-M | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 972acc6f-7771-3c0c-91b9-e528f5a3f122 | -7.88996 | -45.53458 | 2025-08-03 00:09:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 0b8a278d-3074-35ee-a420-cab04da7898b | -5.51032 | -35.57673 | 2025-08-03 00:09:00 | TERRA_M-M | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 24.2 |
| aa5596e3-7ab3-31dc-9a18-41354ba3f4cf | -8.02069 | -43.17356 | 2025-08-03 00:09:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| ffc7d3d3-fcc8-3251-bf96-88ceaf752001 | -8.31759 | -42.85537 | 2025-08-03 00:09:00 | TERRA_M-M | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| ac2b25d6-db30-3f19-865d-ebe5337f302e | -8.03937 | -43.11554 | 2025-08-03 00:09:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 50.6 |
| 55262545-6a57-3e49-a374-b2a11ffd2c12 | -7.12306 | -43.47762 | 2025-08-03 00:09:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 62fd6b0a-4fab-348a-96d2-8a09fac41474 | -8.01412 | -43.19418 | 2025-08-03 00:09:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 1e396917-409b-3cc7-8060-27aa0f11f9f1 | -7.88512 | -45.54277 | 2025-08-03 00:09:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 683f42d5-9a08-3eba-b652-254dcc742efe | -7.97267 | -45.09542 | 2025-08-03 00:09:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 887ffaa8-5301-3644-9077-75ae40e46670 | -7.78125 | -45.19658 | 2025-08-03 00:09:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 93dc6e84-5c44-3f16-80ca-c8f8551c4b28 | -4.31007 | -48.10181 | 2025-08-03 00:09:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 3e47068f-e682-3aef-9fe9-c8ed00bef824 | -8.00754 | -43.14581 | 2025-08-03 00:09:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 50.9 |
| 55f3c749-45ad-3b59-abfe-738f38062124 | -8.01673 | -43.14452 | 2025-08-03 00:09:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.2 |
| 7b273253-b9f7-35e1-92bb-1ea03f8ed1be | -8.01937 | -43.16385 | 2025-08-03 00:09:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 335.4 |
| e3df4096-af13-3493-9d20-d014145d54f2 | -4.78003 | -45.33979 | 2025-08-03 00:09:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 359fb0ba-4916-3f95-b15c-bac56fd2f659 | -8.94176 | -46.73982 | 2025-08-03 00:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| ac7986d1-8e42-3706-a7ef-d026c5e99226 | -7.88347 | -45.52972 | 2025-08-03 00:09:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 45942d77-f7bb-3fce-90a1-6ffd6b34deca | -8.34318 | -46.9231 | 2025-08-03 00:09:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 6b496fa1-3218-39a6-81ab-954aaff95317 | -4.77001 | -45.34119 | 2025-08-03 00:09:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| cef4099a-4d5b-3b3d-a20d-10d66046b68f | -7.96235 | -45.09687 | 2025-08-03 00:09:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 7330cfc2-d918-301c-a50d-726e70b72ef1 | -8.01805 | -43.15416 | 2025-08-03 00:09:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 225.3 |
| 515ccdb5-e4d2-3f51-b3b5-cdfc88743ad0 | -8.03275 | -43.13607 | 2025-08-03 00:09:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| df109e23-f373-3767-b153-d5aff4260065 | -8.00228 | -43.17606 | 2025-08-03 00:09:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 441.0 |
| ac90653b-a1fc-3d32-a376-a046a1896b0a | -8.00359 | -43.18572 | 2025-08-03 00:09:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1129.0 |
| 74b6cafb-acdd-3e1d-8890-ad59a19b4d72 | -8.0233 | -43.12402 | 2025-08-03 00:09:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.7 |
| 6a17bd43-e435-35c4-9f0d-6f53b4d39492 | -4.56353 | -44.20701 | 2025-08-03 00:09:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 108.8 |
| d864a4bb-559f-38c4-9bda-ca2194a49607 | -8.94388 | -46.75638 | 2025-08-03 00:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 191882e9-6ba4-3901-af09-a242e5de79ad | -3.8189 | -42.54041 | 2025-08-03 00:09:00 | TERRA_M-M | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 411da3c5-a71f-3bcc-a97e-383c3c075e36 | -3.9851 | -48.00197 | 2025-08-03 00:09:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| df88db94-8ec9-39cb-86d9-18066f81f77a | -2.65527 | -42.72005 | 2025-08-03 00:09:00 | TERRA_M-M | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4a2c0e60-1b1f-3140-9341-50f6a0c1739f | -7.11514 | -43.48873 | 2025-08-03 00:09:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 22.9 |
| d18dd8f2-2299-3a46-a06b-9fd0c48b5df9 | -8.01148 | -43.1748 | 2025-08-03 00:09:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 997.9 |
| 727b04ef-6b12-3bad-8192-84cc249aca22 | -7.78285 | -45.20889 | 2025-08-03 00:09:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 70a4592a-40fd-3a8b-bc6b-8b85465975c7 | -5.71829 | -44.50526 | 2025-08-03 00:09:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 4f2741c3-9b9e-33ee-8dd9-f45185df68d0 | -7.56749 | -46.29663 | 2025-08-03 00:09:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 8a518728-8749-3d0d-9a1e-af18574d95b9 | -7.95523 | -45.12297 | 2025-08-03 00:09:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| d1a6bbc3-7889-33f1-a8ab-108a1b1d9d82 | -4.3012 | -48.0917 | 2025-08-03 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| fb159643-aa6b-3181-9f06-4cf7f90bb926 | -8.0324 | -43.1022 | 2025-08-03 00:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.8 |
| 3a7b3524-4a12-3764-b944-c638cf2371b7 | -22.029 | -47.5843 | 2025-08-03 00:10:00 | GOES-19 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 53329730-c2a4-3554-b822-58ec86beb01a | -22.0297 | -47.5605 | 2025-08-03 00:10:00 | GOES-19 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 70ee95e5-4b41-3e78-8bd7-651f5473d27e | -4.7656 | -45.3293 | 2025-08-03 00:10:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| ad232b43-9cd5-34fc-9054-25dbec6eb467 | -7.0208 | -59.8346 | 2025-08-03 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 2c5fc190-da10-3b95-a723-98733c2c8c91 | -6.6144 | -59.9656 | 2025-08-03 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 358df1b6-8c36-3e4b-b150-e8982d4e015b | -4.5497 | -44.2047 | 2025-08-03 00:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 7c545afc-7b33-39bf-97fc-76a5b4198f80 | -18.8407 | -46.4417 | 2025-08-03 00:10:00 | GOES-19 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 94.1 |
| 89f53f2f-13ee-32f7-89e5-4ad0700a25c5 | -4.3197 | -48.0908 | 2025-08-03 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| d71f51a6-9b98-3c18-8c32-9fc005495d12 | -21.4603 | -55.1063 | 2025-08-03 00:10:00 | GOES-19 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 53.2 |
| c44ea678-77c5-3f89-8369-e67628002272 | -6.656 | -59.0981 | 2025-08-03 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| c5cbff7a-f543-3819-afee-aff3da7eaa5a | -4.301 | -48.1133 | 2025-08-03 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 9a6a2589-9c9f-3dff-ba8d-74fb7a925588 | -4.5684 | -44.2036 | 2025-08-03 00:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| a213a53e-fbc6-3ce5-8260-d3aafb8d676c | -4.3196 | -48.1125 | 2025-08-03 00:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 1864fee8-ac3c-30ef-9ae5-5296d4a12c4f | -6.6559 | -59.1174 | 2025-08-03 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 607c1757-a849-33ef-8255-aea95cc09180 | -8.9244 | -46.743999 | 2025-08-03 00:18:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ddf6d95-5510-300a-89c4-b8f8d88e5eae | -6.3351 | -46.158699 | 2025-08-03 00:18:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 91a00d16-3834-3380-926e-b24e54dc5f65 | -12.6076 | -44.486599 | 2025-08-03 00:18:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b3549d55-cd50-3d6e-8049-575175bdb7af | -7.8687 | -45.528599 | 2025-08-03 00:18:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e41277c2-e601-3ca1-98e5-e2be7274d345 | -7.761 | -45.201099 | 2025-08-03 00:18:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e696c705-a896-3d60-8a82-9ddb9893551a | -4.2989 | -48.105701 | 2025-08-03 00:18:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec0e5c1b-9beb-3c29-bbae-f801048a8b93 | -10.799 | -50.468899 | 2025-08-03 00:18:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cad662aa-0aa5-38cf-aaf5-7c0a543045c1 | -22.0084 | -47.579498 | 2025-08-03 00:18:00 | METOP-B | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2fbdd9f3-e573-3840-bbbe-f62bbb02d31f | -8.0187 | -43.120998 | 2025-08-03 00:18:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b4d00ce6-747a-3ad0-833a-c86d76a785d9 | -11.784 | -44.934101 | 2025-08-03 00:18:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 90253d1a-5a37-3b5d-89d6-290b8d709cfe | -14.1212 | -45.434898 | 2025-08-03 00:18:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 798240fa-1e15-3ec1-828a-fd7e980143b3 | -12.0116 | -44.022999 | 2025-08-03 00:18:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8d5c7add-d3ab-3c17-85bc-a24f2fca9694 | -14.1193 | -45.426998 | 2025-08-03 00:18:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bf1ee503-4121-39ed-957c-27d76ad4ea1b | -12.6259 | -44.5205 | 2025-08-03 00:18:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 54eb8d93-0281-332e-9913-bcf8739cbc92 | -4.2874 | -48.100399 | 2025-08-03 00:18:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adf00e30-6e9c-39fc-8982-8f70a35b5dde | -12.6216 | -44.502399 | 2025-08-03 00:18:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 48bb4287-8146-3548-8537-4d2e9deb3afe | -10.3199 | -44.897701 | 2025-08-03 00:18:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f2e151b4-8a68-3201-937e-928dd90bc5b7 | -8.3245 | -46.915699 | 2025-08-03 00:18:00 | METOP-B | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a3720af6-4503-3dab-9629-575ec3027078 | -7.9755 | -43.198399 | 2025-08-03 00:18:00 | METOP-B | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2c531a0f-672a-3da2-baad-684317f4dce7 | -4.7525 | -45.332199 | 2025-08-03 00:18:00 | METOP-B | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6a903959-6c1f-3628-8b50-994c6f45c908 | -13.6641 | -41.359901 | 2025-08-03 00:18:00 | METOP-B | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b34c5bf0-1405-3db2-a118-7b32e6d85730 | -8.9261 | -46.751801 | 2025-08-03 00:18:00 | METOP-B | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c2a71611-c8cf-3b0d-9865-ced7c1ee6787 | -12.6119 | -44.504799 | 2025-08-03 00:18:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d52cff2a-d1de-3ef7-b506-ed6bacf817e7 | -12.6434 | -44.506699 | 2025-08-03 00:18:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 68ed2f5b-65e3-352f-904c-b93f18cd7691 | -11.9213 | -44.947399 | 2025-08-03 00:18:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bb026887-3316-370c-b21b-a8e967f2dadf | -22.264799 | -52.0956 | 2025-08-03 00:18:00 | METOP-B | MARABÁ PAULISTA | SÃO PAULO | Brasil | 3528700 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 68baef92-e758-33b1-be1a-ed0f1261771c | -11.7819 | -44.925301 | 2025-08-03 00:18:00 | METOP-B | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README3.md)
