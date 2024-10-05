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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8de5d231-f211-3084-a357-3db8b60786a4 | -6.84025 | -42.82304 | 2024-10-05 00:11:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 32.0 |
| 9052c395-259e-35ec-858f-c9a8c51e5c1d | -6.83314 | -42.81751 | 2024-10-05 00:11:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| 7aad7366-827b-3cbd-bf78-133d0be59ae8 | -6.8282 | -42.82463 | 2024-10-05 00:11:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 4d7a0e9e-b0f2-3445-848a-5996c2901b81 | -6.77899 | -35.08977 | 2024-10-05 00:11:00 | TERRA_M-M | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 5fe05bff-90f1-3582-8a72-85a7e996351b | -6.65082 | -43.0566 | 2024-10-05 00:11:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 761df7c1-82c8-313e-8c97-6a455d064ad3 | -6.55587 | -37.75749 | 2024-10-05 00:11:00 | TERRA_M-M | MATO GROSSO | PARAÍBA | Brasil | 2509370 | 25 | 33 | nan | nan | nan | Caatinga | 7.1 |
| d258c3a1-da24-35f7-a323-59d635f51acb | -9.77242 | -36.37218 | 2024-10-05 00:11:00 | TERRA_M-M | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 42.4 |
| 621e6aa9-66bc-375c-b311-55cf7141c6ea | -8.97265 | -40.84043 | 2024-10-05 00:11:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 15.0 |
| a378c211-e3c2-38eb-8378-b641f2cca53f | -8.9744 | -40.85361 | 2024-10-05 00:11:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 36.4 |
| 3e378d16-bdca-33cd-bb2a-690a4461350e | -8.97858 | -40.84681 | 2024-10-05 00:11:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 61.3 |
| e8077106-94f4-32fa-bb2f-e29300b747c6 | -8.98026 | -40.86012 | 2024-10-05 00:11:00 | TERRA_M-M | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 52df5878-a5fe-3eec-947b-ff7daf7730a0 | -9.47907 | -36.05876 | 2024-10-05 00:11:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 98c11f94-894c-3b07-aa78-620ad8072884 | -7.79599 | -43.10861 | 2024-10-05 00:11:00 | TERRA_M-M | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| 6826fe35-4eef-386b-9f0c-d236bf39bdb5 | -6.33516 | -45.69139 | 2024-10-05 00:13:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 6c1c4e37-30d3-3bd2-9d13-9fc55692ce65 | -6.18147 | -45.43984 | 2024-10-05 00:13:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 37.5 |
| 25d93369-0e63-33cb-b216-cc622a2b6e72 | -5.89866 | -46.30385 | 2024-10-05 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| d91e4b3a-7aa4-3232-80d4-e0a1a130f706 | -5.89461 | -46.27244 | 2024-10-05 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 9dccaeb8-d062-3a1a-ba6f-6efaeb252aba | -5.89329 | -46.29977 | 2024-10-05 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| ccbc083f-a11b-362d-89a6-83211934f904 | -5.82578 | -44.13726 | 2024-10-05 00:13:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 214.4 |
| 4bc6c043-06f8-317e-9a6f-748ea4b9d764 | -5.82298 | -44.11636 | 2024-10-05 00:13:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 9010d6e3-7962-3c1d-9f80-5666a55f39ac | -5.82249 | -44.13235 | 2024-10-05 00:13:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 436.6 |
| 491ff97b-32ba-3832-84f7-527112e058ab | -5.81987 | -44.11155 | 2024-10-05 00:13:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 4ea0942b-90ae-3b19-b5aa-afedc6439c59 | -5.8126 | -44.13914 | 2024-10-05 00:13:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 55dc8a7c-a540-36f7-b4a1-af37ebe80b60 | -5.80981 | -44.11814 | 2024-10-05 00:13:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| b4142402-8eac-3203-af60-ed6fe3a7f453 | -5.71214 | -44.82005 | 2024-10-05 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| bd283f08-b361-33f3-aefa-072ae9d4ecb0 | -5.53568 | -44.32412 | 2024-10-05 00:13:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 38.1 |
| bbe3e303-5946-33fa-b728-011c002c5e28 | -5.53286 | -44.30256 | 2024-10-05 00:13:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 222efafb-2af4-309e-8bef-231cf28b3809 | -5.38642 | -46.43723 | 2024-10-05 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 1bb65937-b15d-3fc1-a21c-d1d218cc3931 | -5.38053 | -46.43191 | 2024-10-05 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 1a91da5c-5c10-3f21-a076-95de9f625ee7 | -4.32476 | -46.70612 | 2024-10-05 00:13:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 53f7a33a-f24d-3dfe-9630-101b9abb2e17 | -4.33096 | -46.71065 | 2024-10-05 00:13:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 33.8 |
| c13209a9-7785-3b37-8690-abdfce4232be | -4.59432 | -45.61023 | 2024-10-05 00:13:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| cee9b624-e3de-3553-93a6-5830186d14c8 | -3.80551 | -41.59525 | 2024-10-05 00:13:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 5eab3ce2-7cff-3c02-a0ae-1aa3395bc0b9 | -3.79509 | -41.5966 | 2024-10-05 00:13:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 36.7 |
| f77431f4-d69c-33ca-905c-cecf908ff2f9 | -3.79339 | -41.58415 | 2024-10-05 00:13:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 16.5 |
| af8e8583-0a42-346e-b374-e51060810520 | -3.76989 | -40.42608 | 2024-10-05 00:13:00 | TERRA_M-M | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 5666718a-118b-328a-9eac-86fc4105431c | -3.76683 | -40.43286 | 2024-10-05 00:13:00 | TERRA_M-M | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 204bedcb-90ef-36e6-b21f-d719031fcf0e | -3.76536 | -40.42233 | 2024-10-05 00:13:00 | TERRA_M-M | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| c7876b48-9df0-349e-980a-50c0877bbd8d | -1.197 | -46.57355 | 2024-10-05 00:13:00 | TERRA_M-M | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| bf014ab0-0978-3f10-9b4e-c1a8b0e6da80 | -1.19743 | -46.57887 | 2024-10-05 00:13:00 | TERRA_M-M | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 190532a8-1eb7-354f-8832-b0cde2581633 | -1.20074 | -46.60147 | 2024-10-05 00:13:00 | TERRA_M-M | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 129.6 |
| 84839bc3-1848-3769-a570-708f537fa682 | -1.20138 | -46.60677 | 2024-10-05 00:13:00 | TERRA_M-M | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 7b3ea861-32d3-30a0-898f-b49081f227f6 | -1.26061 | -47.66924 | 2024-10-05 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 95.8 |
| f581fc74-58af-3c61-907d-ae830347a654 | -1.26804 | -47.66223 | 2024-10-05 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| c4da8d30-0717-3950-ad55-98bfd6a9ae50 | -2.01612 | -47.98816 | 2024-10-05 00:13:00 | TERRA_M-M | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 16fab0f2-6a58-34e7-bd2e-0d0cbda69578 | -3.60454 | -47.51773 | 2024-10-05 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 161.4 |
| 247782fc-6224-32bf-9d46-e5c26700501e | -3.6094 | -47.55381 | 2024-10-05 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| be369887-739d-3201-a6b4-73c82ab53d77 | -3.60987 | -47.51048 | 2024-10-05 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 295.9 |
| 01a27c8f-b749-3d37-9100-c3d2b4cbc59b | -5.15127 | -45.23985 | 2024-10-05 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| ae7ba75e-e16e-362c-b222-12113ad4cf70 | -5.40723 | -43.11945 | 2024-10-05 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| e4d041e6-a6a5-373a-a9a7-d9e08650582d | -5.40014 | -43.10942 | 2024-10-05 00:13:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| b7d7812a-0371-3bc5-aebf-a842af052e71 | -5.11883 | -37.57192 | 2024-10-05 00:13:00 | TERRA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 20.1 |
| 926e77c1-b09b-30f0-8e7b-3f07fa48faf5 | -5.11761 | -37.56311 | 2024-10-05 00:13:00 | TERRA_M-M | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 24.0 |
| d2d10fea-f700-332f-81e4-5fa22e78ab53 | -4.95399 | -43.76984 | 2024-10-05 00:13:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| c3d020ec-4829-33b3-a471-66ad6837ec8f | -4.95324 | -43.77641 | 2024-10-05 00:13:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 02ea3206-fff9-35a7-8450-85f57e47b421 | -4.94383 | -43.79092 | 2024-10-05 00:13:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 1f473697-da98-32df-8de1-7b0fa1b674f6 | -4.94139 | -43.7717 | 2024-10-05 00:13:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| b52e10d2-9c6b-362a-bdd9-e54f581ae3d0 | -4.94063 | -43.77821 | 2024-10-05 00:13:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 84.4 |
| ff8fc1f0-23e1-3c88-92a5-67b403234f4c | -4.86161 | -38.43749 | 2024-10-05 00:13:00 | TERRA_M-M | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 71a13f46-9b93-3658-a272-963adbe2e860 | -4.85288 | -38.37471 | 2024-10-05 00:13:00 | TERRA_M-M | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 26bb88ec-eb75-3855-9fff-c876e33c6dd2 | -4.84398 | -38.37596 | 2024-10-05 00:13:00 | TERRA_M-M | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 7b877312-999c-313f-a030-239a96b0d218 | -4.69655 | -43.19328 | 2024-10-05 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| d1346852-6828-368f-93e3-b5c93da8a9aa | -4.69131 | -43.20054 | 2024-10-05 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 3a0708a0-4b56-37e7-a83e-f06fdcda90ef | -4.68897 | -43.18345 | 2024-10-05 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 4d146c1a-590a-3d82-87e3-1abd4dc192c6 | -4.64706 | -42.29223 | 2024-10-05 00:13:00 | TERRA_M-M | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 6e9b16df-9992-3227-86c2-8bb9eb0363d4 | -4.4732 | -42.88415 | 2024-10-05 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| f9d8d472-0c90-32ed-95cc-a09a2c53ee6c | -4.46534 | -42.89153 | 2024-10-05 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 1d5bf840-a6ce-3d25-b3cd-9dc3ea6f2b95 | -4.0192 | -43.24676 | 2024-10-05 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 1820b52d-8e3d-3ed6-919d-41dbea839c6d | -4.00955 | -43.26519 | 2024-10-05 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 1ca9e5e1-506f-3118-99e4-551faa4dba25 | -4.00729 | -43.24836 | 2024-10-05 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 8f82de50-89dd-33b3-a2c4-6904ddee73cd | -3.99763 | -43.26682 | 2024-10-05 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 66ac428d-7539-307a-995f-6f51df0e0c08 | -3.99539 | -43.24999 | 2024-10-05 00:13:00 | TERRA_M-M | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 34.7 |
| c767e74e-62e1-3123-823f-59e2395fae3e | -3.6145 | -47.54665 | 2024-10-05 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 204.2 |
| b9af5107-16c0-389e-a033-b3f2faaf1d91 | -3.62118 | -47.51564 | 2024-10-05 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 192.3 |
| 556ca818-e8a1-3244-868f-0f123d3055d0 | -3.62614 | -47.55211 | 2024-10-05 00:13:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 96e8b69e-94ea-362a-b110-6db48cd09f05 | -4.07586 | -47.93319 | 2024-10-05 00:13:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 175.6 |
| 94c56476-a5ec-32d6-9052-84f3bae03c6d | -4.07803 | -47.9263 | 2024-10-05 00:13:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 29cafb14-2e43-38bd-a801-3a3063bc41e3 | -4.08118 | -47.97201 | 2024-10-05 00:13:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 173.6 |
| 9bb75853-7d1d-3d12-ae5c-4bfbed59fd36 | -4.08309 | -47.96519 | 2024-10-05 00:13:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 276.2 |
| 27cbfd12-c1c4-3ad9-8720-25de96cc33d9 | -4.15965 | -46.83748 | 2024-10-05 00:13:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 26d12348-e64d-317e-b33a-e29846cd49d3 | -4.16648 | -46.84126 | 2024-10-05 00:13:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 45.5 |
| a54ffc31-6cb6-389b-81ed-64538bedc839 | -1.1942 | -46.5935 | 2024-10-05 00:15:13 | GOES-16 | AUGUSTO CORRÊA | PARÁ | Brasil | 1500909 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 261eac65-572a-3edf-9e0d-a50a154fa5bb | -1.2663 | -47.6643 | 2024-10-05 00:15:13 | GOES-16 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| b90cbf46-d850-33a7-805a-3f6d90085e68 | -2.5749 | -49.0782 | 2024-10-05 00:15:21 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| 55365d0d-f594-3e1f-9ff8-84ccab15ca96 | -2.78 | -48.5806 | 2024-10-05 00:15:22 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 6e941d15-9025-3439-915c-f573a7c616a7 | -2.8829 | -50.7147 | 2024-10-05 00:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 2b7bb819-c831-3973-acda-67f411cd9912 | -2.9014 | -50.7142 | 2024-10-05 00:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 128.9 |
| 02cf3d72-f848-3613-8f0c-e5b9d557566e | -2.9015 | -50.6933 | 2024-10-05 00:15:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 4bde3a17-d20f-39e2-824f-53bad0dbc1b3 | -3.1432 | -50.2254 | 2024-10-05 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| b71f3e09-e1e4-3909-8027-6d0a7abbd12b | -3.2349 | -50.3695 | 2024-10-05 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 2fd29af1-f5fd-3e63-95b9-9f5c8f212de1 | -3.239 | -49.3986 | 2024-10-05 00:15:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 40.4 |
| c260d317-85ae-380e-98c8-e632d36555b2 | -3.2534 | -50.3689 | 2024-10-05 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 3caee457-5619-321c-8b2e-8c941beeabec | -3.2574 | -49.4193 | 2024-10-05 00:15:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| cfba380d-3409-36e2-aa88-63bca8e575f5 | -3.2575 | -49.398 | 2024-10-05 00:15:24 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 0ce38bfd-cfd9-309e-bcef-fb6ec97cfb06 | -3.2899 | -50.4725 | 2024-10-05 00:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| ac77fdf5-564b-3b7c-98ae-e16b9becae14 | -3.2899 | -50.4516 | 2024-10-05 00:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 9a4f9451-1621-3f07-9b56-ca2aa21f6491 | -3.3083 | -50.4719 | 2024-10-05 00:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 105.5 |
| a968574f-6d83-3046-bd2f-672201c439c1 | -3.3084 | -50.451 | 2024-10-05 00:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 2513848d-26a8-349e-9544-82f1b4ba5518 | -3.3127 | -49.4599 | 2024-10-05 00:15:25 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 35.0 |
| d762bda1-424c-3383-acb8-32e800fbd9c6 | -3.3268 | -50.4713 | 2024-10-05 00:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |


[Clique aqui para ver as próximas entradas](README4.md)
