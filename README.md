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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d7d0058-6dbc-3f82-a3da-2374506918d5 | -6.0638 | -35.2745 | 2025-02-27 00:00:00 | GOES-16 | SÃO JOSÉ DE MIPIBU | RIO GRANDE DO NORTE | Brasil | 2412203 | 24 | 33 | nan | nan | nan | Mata Atlântica | 80.2 |
| b32905cf-6be3-3b9e-8474-2b133a18dd18 | 2.9092 | -60.4268 | 2025-02-27 00:00:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 6beb88c9-9c78-3c8d-8493-f36a5ba1a835 | 2.9092 | -60.4458 | 2025-02-27 00:00:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 50.4 |
| c9ddfb12-059b-3bed-a223-4853be35bd0f | 2.9092 | -60.4458 | 2025-02-27 00:10:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 52.0 |
| c89c902b-9276-3dd0-845e-177b23f410ed | 2.9092 | -60.4268 | 2025-02-27 00:10:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 989e00ce-4ee8-3374-bac7-661d21bc6847 | 2.9092 | -60.4458 | 2025-02-27 00:20:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 1c994363-31ff-34dd-b71e-1274e0fed366 | 2.9092 | -60.4458 | 2025-02-27 00:30:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 46.9 |
| de31ef57-6258-3abd-8037-6b639fb710e7 | 2.9092 | -60.4458 | 2025-02-27 00:40:00 | GOES-16 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 24e98fff-44c0-3323-852e-2895735dedd7 | 1.28774 | -60.43286 | 2025-02-27 01:34:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4dc2b3aa-dba2-3afa-8926-adbb771263f3 | 1.27774 | -60.10519 | 2025-02-27 01:34:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 838c421e-b68d-3752-8f09-4a495175d1ec | 1.29672 | -60.43412 | 2025-02-27 01:34:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1eff0c30-5dc7-3d39-82eb-99736f0bad27 | 1.34126 | -60.04403 | 2025-02-27 01:34:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 097c719d-ab09-3103-b906-7f496f33f895 | 1.27255 | -60.07585 | 2025-02-27 01:34:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 23373c06-af9f-345b-a3fb-1d2de8eff4a4 | 1.31157 | -60.06222 | 2025-02-27 01:34:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 724a8be7-9c6c-34da-95e8-e551d25a3b56 | 1.31025 | -60.0716 | 2025-02-27 01:34:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 259a690f-1341-37f6-b1d9-8218d555d8ec | 1.28648 | -60.44199 | 2025-02-27 01:34:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 11babd35-4f78-36ec-b3fa-6b61b98fb620 | 1.12685 | -60.52779 | 2025-02-27 01:34:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 6eb59b20-208e-3136-84a4-a59c641e3d82 | 2.10972 | -61.81945 | 2025-02-27 01:36:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9ff5d045-1c91-39d8-abb2-35b1cbb89835 | 2.0415 | -60.57808 | 2025-02-27 01:36:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9b9b35a6-cb2c-3d4f-be18-532f17785093 | 2.67253 | -61.40974 | 2025-02-27 01:36:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2d164c6b-1f49-3716-b895-f69ea5e28e1e | 1.717 | -60.72682 | 2025-02-27 01:36:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4791ce11-1917-305c-930f-1e96aadaa46e | 3.54343 | -60.77952 | 2025-02-27 01:36:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a96429e5-23d0-36bc-a5ed-f95f3d3144d0 | 2.71859 | -61.20837 | 2025-02-27 01:36:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0602d8ba-132a-39c9-9f25-d88b3330e26b | 1.88794 | -60.42284 | 2025-02-27 01:36:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e33309b3-5e3c-3a8e-8c04-530f1c244143 | 2.90935 | -60.43383 | 2025-02-27 01:36:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 9be6b908-5bcc-39dc-8618-a17534175402 | 2.11853 | -61.82069 | 2025-02-27 01:36:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 28508bf6-befd-3b33-bf63-2f45023eeb11 | 1.70806 | -60.72557 | 2025-02-27 01:36:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fcf70ff0-b3b0-3bc1-a807-0ea95ba23a1c | 2.44641 | -61.32072 | 2025-02-27 01:36:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4cc924d1-7713-389d-af9f-3f8529ba9dbd | 2.90805 | -60.44319 | 2025-02-27 01:36:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 86c696ff-8aba-3222-b816-774cde19becb | 3.3827 | -61.21389 | 2025-02-27 01:36:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9a92bd33-6506-30f7-9da4-58589921bf97 | -5.29748 | -35.9887 | 2025-02-27 03:27:00 | NOAA-21 | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 07af3225-c263-35b1-986c-8476c12c56b1 | -7.8088 | -44.18736 | 2025-02-27 03:29:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1013b01a-aefb-3b5b-82ba-548a7ed49dc2 | -10.49802 | -40.39426 | 2025-02-27 03:29:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 93fa4bee-df1d-310d-984d-aba1f5c5a736 | -7.80546 | -44.18918 | 2025-02-27 03:29:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4311ceef-114a-31de-91df-951f51694572 | -9.81393 | -36.99479 | 2025-02-27 03:29:00 | NOAA-21 | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 04de349c-89ed-30eb-91bc-99b903ec3352 | -8.11296 | -43.14014 | 2025-02-27 03:29:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 5c620f4f-1bac-3847-8e07-4a1bcc10ce2c | -8.11771 | -43.14137 | 2025-02-27 03:29:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a4a005d2-57ec-390a-9844-5dba7c78b5bd | -7.06161 | -44.35442 | 2025-02-27 03:29:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 15862696-998a-3fab-ad8b-3289dd22a5a6 | -7.41337 | -35.19856 | 2025-02-27 03:29:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 28e51924-96d1-33b0-bc6b-ffafb091f3e4 | -10.48305 | -42.42202 | 2025-02-27 03:29:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4ef6a48d-0750-3693-8dd9-9b9151309630 | -8.11805 | -43.14546 | 2025-02-27 03:29:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 9da18c6a-5cc0-3fde-b800-20a5cd5b2469 | -8.11691 | -43.14561 | 2025-02-27 03:29:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1481e5c4-d3cd-3643-b9f8-6f2209389269 | -10.23544 | -36.53986 | 2025-02-27 03:29:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 95cd4080-8595-32b3-9911-be8849520f61 | -8.88616 | -37.95823 | 2025-02-27 03:29:00 | NOAA-21 | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fc7a1972-a943-3f97-8f2b-9432f65f190f | -10.4837 | -42.41857 | 2025-02-27 03:29:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9620e364-f841-3aca-83ba-075b88fefc87 | -7.05523 | -44.35305 | 2025-02-27 03:29:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0bf5b090-e37c-3e5f-8e4b-d4be581d7644 | -6.96796 | -43.01192 | 2025-02-27 03:29:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 2ba7bfd5-5b87-3552-b8f2-161ccfebdae4 | -6.76547 | -35.22453 | 2025-02-27 03:29:00 | NOAA-21 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 41ed6b03-f8f3-3de6-bd49-c817e1b293de | -7.05626 | -44.34749 | 2025-02-27 03:29:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 64fda567-ada5-3d66-9e42-0cca599c352d | -8.12277 | -43.14668 | 2025-02-27 03:29:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ba02c295-7227-3fca-a930-1af8c6167766 | -6.96877 | -43.00755 | 2025-02-27 03:29:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 94cab0c6-6c2e-3baf-a3a0-fe0e0efe9406 | -7.8064 | -44.18427 | 2025-02-27 03:29:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 40dbb0ea-bc68-3c3d-b199-2f9248a59bdf | -7.41693 | -35.19915 | 2025-02-27 03:29:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 31bde2a2-a397-335a-b6d8-dc737c3f8854 | -8.11186 | -43.14032 | 2025-02-27 03:29:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8184cb0e-e55e-3fb0-af01-b39ffd5d65d2 | -10.53423 | -42.43009 | 2025-02-27 03:29:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 78b61f24-d451-3187-9300-d8c53be94cf8 | -8.11265 | -43.13609 | 2025-02-27 03:29:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5b9df9e1-1bf6-30e3-96bb-c77479269594 | -16.6823 | -43.8859 | 2025-02-27 03:32:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c2ba991-0e84-3046-ac5a-54de5a19246c | -13.81151 | -43.34245 | 2025-02-27 03:32:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9001c20e-bae8-36fc-a672-0eb19c1783e9 | -16.68293 | -43.88282 | 2025-02-27 03:32:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7f43a54-4834-3214-90d2-7a9e5d5760ee | -11.58155 | -37.65385 | 2025-02-27 03:32:00 | NOAA-21 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ca7f02ed-3c4e-3e8c-ab52-acaf35407fd7 | -14.04213 | -41.45809 | 2025-02-27 03:32:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e3c49abf-ca87-3170-851e-a1bced3cd7af | -16.35044 | -43.69687 | 2025-02-27 03:32:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e75202b-a693-3225-8cfc-bdbd8a4e8e8e | -14.04352 | -41.45637 | 2025-02-27 03:32:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a044c63b-7c7b-364c-95cb-5c7c5defbf0b | -11.58273 | -37.6565 | 2025-02-27 03:32:00 | NOAA-21 | JANDAÍRA | BAHIA | Brasil | 2917904 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9f517286-b2ac-3766-a472-05c97ba2e97b | -20.43085 | -42.70971 | 2025-02-27 03:34:00 | NOAA-21 | JEQUERI | MINAS GERAIS | Brasil | 3135506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 44c43089-0372-37fa-ac9b-3eea8a2e4662 | -22.55578 | -42.79115 | 2025-02-27 03:34:00 | NOAA-21 | CACHOEIRAS DE MACACU | RIO DE JANEIRO | Brasil | 3300803 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6ad4bf50-b5ef-35f2-bb79-dcbbb9136d2f | -22.64693 | -42.24938 | 2025-02-27 03:34:00 | NOAA-21 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9e6652e3-7519-3e4c-9c1b-7bc8c81a6fdb | -21.86276 | -43.08429 | 2025-02-27 03:34:00 | NOAA-21 | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 4283fc4a-a3aa-3bd8-8f47-55028c4c4655 | -19.90825 | -45.23991 | 2025-02-27 03:34:00 | NOAA-21 | ARAÚJOS | MINAS GERAIS | Brasil | 3103900 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79e98d76-704d-38b8-8302-336af0493cb4 | -23.47083 | -46.28591 | 2025-02-27 03:34:00 | NOAA-21 | ITAQUAQUECETUBA | SÃO PAULO | Brasil | 3523107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| baa7a1f7-f020-31b7-9927-5f24193bb222 | -22.85164 | -42.54437 | 2025-02-27 03:34:00 | NOAA-21 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| abc33a0b-fb11-34fc-86fb-04874b083b4f | -22.90047 | -43.7529 | 2025-02-27 03:34:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 55558fe3-90ed-3b42-bac2-01cc0b8c04bb | -21.17612 | -43.52515 | 2025-02-27 03:34:00 | NOAA-21 | DESTERRO DO MELO | MINAS GERAIS | Brasil | 3121506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 27394924-c04c-3166-9264-958f8e5cc4ac | -21.62589 | -43.46892 | 2025-02-27 03:34:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 27d59c78-0190-3d34-ab53-114a3802cbb5 | -21.04843 | -47.7786 | 2025-02-27 03:34:00 | NOAA-21 | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 30b424ac-70a4-3e9a-8d05-c565327aaf4f | -20.31422 | -46.73031 | 2025-02-27 03:34:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 59f84ce8-ca28-38ca-a9bc-13dfd9e0642c | -22.64269 | -42.24844 | 2025-02-27 03:34:00 | NOAA-21 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 72e21c07-b400-3042-9caa-dc5fc5544e0f | -22.74123 | -42.84673 | 2025-02-27 03:34:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6a57f623-70e6-3d27-b3ed-9c1ca9ae8f85 | -21.17504 | -43.53031 | 2025-02-27 03:34:00 | NOAA-21 | DESTERRO DO MELO | MINAS GERAIS | Brasil | 3121506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| d85bd952-e4dd-352a-be5a-7ae7748c3519 | -22.84513 | -42.31545 | 2025-02-27 03:34:00 | NOAA-21 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 073dd747-483f-39b7-96a8-f98fbb833988 | -21.17479 | -43.52828 | 2025-02-27 03:34:00 | NOAA-21 | DESTERRO DO MELO | MINAS GERAIS | Brasil | 3121506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| ecb9c0db-9a96-358d-82ed-7f4741f8a905 | -22.67512 | -42.85597 | 2025-02-27 03:34:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 2d8b91da-bef1-334a-a83a-7b13805d9cbf | -22.85075 | -42.54881 | 2025-02-27 03:34:00 | NOAA-21 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| bf098934-f1c9-3a1e-997b-aa7e01fde80d | -22.85478 | -42.98178 | 2025-02-27 03:34:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 951ef7f9-5894-3f72-8aec-c30690b3883c | -21.04727 | -47.78356 | 2025-02-27 03:34:00 | NOAA-21 | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 19.7 |
| feb58ea1-23f3-3902-9840-e8bd377b77b0 | -19.83442 | -43.0895 | 2025-02-27 03:34:00 | NOAA-21 | BELA VISTA DE MINAS | MINAS GERAIS | Brasil | 3106002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 16e3626d-0266-3f7d-a153-51d34e346a11 | -22.74087 | -42.84554 | 2025-02-27 03:34:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dc2f651d-6ef2-361a-99b4-10d677efe189 | -22.69866 | -43.34887 | 2025-02-27 03:34:00 | NOAA-21 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4b33afa3-37a3-3d14-ac74-6d058485de4c | -22.54132 | -48.816 | 2025-02-27 03:34:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f6e004c4-ef7e-3797-85b2-eb0c67b95aa9 | -21.86727 | -43.08539 | 2025-02-27 03:34:00 | NOAA-21 | MAR DE ESPANHA | MINAS GERAIS | Brasil | 3139805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1beb0d7c-ff64-3ff2-ad47-3b3234ab70f5 | -21.0533 | -47.78532 | 2025-02-27 03:34:00 | NOAA-21 | JARDINÓPOLIS | SÃO PAULO | Brasil | 3525102 | 35 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 08c449f0-730d-3052-8215-5ec46f9b1c14 | -22.64355 | -42.24416 | 2025-02-27 03:34:00 | NOAA-21 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 05a2d3ec-3dbd-30b9-9400-990c461f3ceb | -4.80629 | -43.00349 | 2025-02-27 03:53:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba20e346-0cf7-314d-b8ed-74c095c9ba12 | -5.2953 | -35.98926 | 2025-02-27 03:53:00 | NPP-375D | PARAZINHO | RIO GRANDE DO NORTE | Brasil | 2408805 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ad61cee8-ce02-346e-af4b-156652ddada1 | -5.01284 | -38.54432 | 2025-02-27 03:53:00 | NPP-375D | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 00e4343d-6af2-32c3-bb43-a59d53bf858c | -5.80424 | -35.43499 | 2025-02-27 03:53:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3f46cc7e-a1b4-3bbb-b4d7-6676573348ad | -4.80587 | -43.00389 | 2025-02-27 03:53:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e67cd1a7-7984-305b-b4db-5a5382977218 | -5.96184 | -42.32023 | 2025-02-27 03:55:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 50ae4fc3-a6c1-304d-bb35-049d22999a2c | -7.80576 | -44.18267 | 2025-02-27 03:55:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8568407e-78d9-34cd-8c59-f0a81c9b112f | -7.05631 | -44.3457 | 2025-02-27 03:55:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README2.md)
