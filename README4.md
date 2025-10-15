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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f347facd-95b5-34c8-ba28-d71791ba40f1 | -5.79785 | -43.88694 | 2025-10-15 00:35:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 4d8e95d8-5f5a-38b6-9790-5c4cf44deab8 | -8.18975 | -44.08049 | 2025-10-15 00:35:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 8d2e92fc-9a1c-3d8b-a4bd-2236ba698338 | -4.59122 | -47.03145 | 2025-10-15 00:35:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 15.9 |
| bc7f086e-afda-307d-bb57-07d06cbbd1f2 | -8.22142 | -44.07042 | 2025-10-15 00:35:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 21.4 |
| b13697c6-150d-3491-9f81-5dfba2ff86d0 | -4.86891 | -45.67294 | 2025-10-15 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 78.0 |
| d1ad9973-1dc5-3583-b14f-c4453a7c0fbb | -5.87112 | -43.876 | 2025-10-15 00:35:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 52.4 |
| f8d62c2a-888d-3add-86ae-1d68b2bf3119 | -4.11065 | -48.72979 | 2025-10-15 00:35:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 5e1a4f39-9024-326a-8fcd-5c8cbb208ec8 | -5.06042 | -44.44663 | 2025-10-15 00:35:00 | TERRA_M-M | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 403cbdf3-a9db-37b3-9e39-da12bf744b75 | -5.24562 | -44.48347 | 2025-10-15 00:35:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| bf404045-d2f0-3973-9bb3-9bffeb98ea38 | -8.21284 | -44.07746 | 2025-10-15 00:35:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 30.6 |
| bfaf8588-261d-3154-848b-b8ef2275a800 | -4.54664 | -45.42717 | 2025-10-15 00:35:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 26.9 |
| ce9182f4-350a-3251-8f68-1b538facbe79 | -3.06828 | -49.51517 | 2025-10-15 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| f962e843-b8a6-337f-9bd8-36448aca2ff8 | -3.08361 | -47.72543 | 2025-10-15 00:35:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| aea099db-18d5-3a92-a865-c74ffee6db32 | -5.11908 | -46.06207 | 2025-10-15 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 66817e65-8d25-3cef-99a3-2fafab72584a | -4.7748 | -45.73457 | 2025-10-15 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 54.6 |
| f764b2b0-5aad-3693-b134-5a31611997ec | -4.36097 | -46.77846 | 2025-10-15 00:35:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| c3374919-0c70-31a6-bf80-d23600874953 | -3.60249 | -48.98288 | 2025-10-15 00:35:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6b55e973-a33b-3a92-8328-aa0e1ead9454 | -4.88547 | -45.93996 | 2025-10-15 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 7111cbd3-aed6-3cbf-bf23-94e7b3dadffd | -3.4632 | -48.97745 | 2025-10-15 00:35:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| ff347bab-e814-3ab9-8643-036b0f9e276c | -5.31114 | -42.92818 | 2025-10-15 00:35:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 40.9 |
| 25f04b23-9dbf-34d0-97df-13900d4d139f | -6.26112 | -44.34552 | 2025-10-15 00:35:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 02ed7e25-9928-30c7-8a11-d7e05c060f37 | -5.99654 | -44.1002 | 2025-10-15 00:35:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 82fc4937-3161-313c-934c-c9d2fc377f7f | -5.50286 | -47.30592 | 2025-10-15 00:35:00 | TERRA_M-M | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b37a1f7f-1db1-36f3-a271-e3ef1dfbe743 | -5.6515 | -45.87468 | 2025-10-15 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e37c8bc6-b78b-3919-8c7a-64e6ab997a5b | -5.92158 | -42.82958 | 2025-10-15 00:35:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 34.4 |
| 7ee85d6e-6de7-3fa3-b126-53828a1884b9 | -6.58563 | -42.96036 | 2025-10-15 00:35:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 58460b2d-d919-3884-84b4-d8411bfde0b5 | -6.17693 | -42.61433 | 2025-10-15 00:35:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 25.4 |
| 333a0052-d441-3530-8573-420bdfe83099 | -2.8633 | -49.17037 | 2025-10-15 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 531e8c19-3ed8-3c3b-b665-9c04ac3d3ce5 | -4.04251 | -45.27995 | 2025-10-15 00:35:00 | TERRA_M-M | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 20.7 |
| aa1649ad-85df-3a52-af4a-7074fae1e864 | -4.79705 | -45.32827 | 2025-10-15 00:35:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 8aa4edaa-d6eb-34f9-b7fb-7cdf32012d00 | -7.25787 | -44.91572 | 2025-10-15 00:35:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 57ed5347-7fa3-3e74-a24f-b613f16fbe7d | -3.61272 | -48.92539 | 2025-10-15 00:35:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 01efb745-fe67-3aaa-94ec-8b8089bfe760 | -3.46448 | -48.98661 | 2025-10-15 00:35:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9f253dad-7167-38f4-bb4a-4880e527ebf5 | -5.02368 | -45.06721 | 2025-10-15 00:35:00 | TERRA_M-M | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| f4522b7a-8126-3f5b-87ec-98e61b74b3bc | -4.66846 | -43.12981 | 2025-10-15 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| e036dfbc-997f-388b-bcbc-a4dec6960ad5 | -6.16702 | -44.38887 | 2025-10-15 00:35:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 1ffd241f-be06-3b51-9fec-c1ef7f6caa55 | -4.91386 | -46.70858 | 2025-10-15 00:35:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 50.2 |
| e0b1a2ae-b447-389a-81c9-a11c119ebfff | -5.20183 | -46.14489 | 2025-10-15 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 54bf53ca-7414-3938-b709-8b70c88d56aa | -5.94662 | -43.76536 | 2025-10-15 00:35:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 6c789467-c444-3f45-90c7-f8a8e8f56eb0 | -7.94582 | -44.13852 | 2025-10-15 00:35:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 167.6 |
| 1165b457-1026-329e-933a-5dce6fcfbde0 | -4.87423 | -45.67922 | 2025-10-15 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 386a8b39-c114-302a-9d36-f859340c7cf4 | -5.24193 | -45.6003 | 2025-10-15 00:35:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 6a5a4594-6607-39d2-a393-9b02046c2b41 | -4.79977 | -45.72531 | 2025-10-15 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5e4669b0-13af-3894-8f03-0d2671df327c | -4.39385 | -43.47272 | 2025-10-15 00:35:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 76f9381e-3e8d-3724-abbd-83b70b1efc88 | -4.30859 | -48.23205 | 2025-10-15 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c33f98ed-aab5-3e1c-83e5-062a6c144c29 | -2.87868 | -50.74199 | 2025-10-15 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| dcbb9e66-1dd2-3022-8b3d-02ea3dcdd926 | -4.11208 | -48.02781 | 2025-10-15 00:35:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| a24409d8-f90a-37a0-bfea-d558919ca778 | -2.95246 | -49.34589 | 2025-10-15 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 01340ea7-2cb6-38a4-b1b8-28b571de7d46 | -2.81459 | -49.21441 | 2025-10-15 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| ea2d37d5-9f24-3ed9-94c2-b916022d06a9 | -4.25812 | -45.57465 | 2025-10-15 00:35:00 | TERRA_M-M | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 16.3 |
| a704ea67-e8a0-3f4d-9cab-5884c5f3768c | -5.71952 | -44.41615 | 2025-10-15 00:35:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 36190023-a81c-31b8-b5d1-5deea4dcc037 | -4.30992 | -48.24154 | 2025-10-15 00:35:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5d143236-a9be-3d0f-9c44-925d1193b7f0 | -3.73325 | -44.15992 | 2025-10-15 00:35:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| a8b3a5f3-9678-3779-b9cc-b442771c0fc0 | -4.40289 | -43.6211 | 2025-10-15 00:35:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 103de9c5-89d3-3fdc-b90e-5f9069db5430 | -8.461 | -46.16533 | 2025-10-15 00:35:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8d5489ca-d1be-37db-b8df-58cf5d6158f3 | -5.42642 | -44.22273 | 2025-10-15 00:35:00 | TERRA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 49.5 |
| b1d2e7df-4c62-3773-ab0e-eb65f5390c06 | -2.4395 | -49.3721 | 2025-10-15 00:35:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 8472199a-d818-3117-8fa3-c497629097ad | -6.89635 | -43.96803 | 2025-10-15 00:35:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 188a89b7-4b7a-358e-a063-43c2be56cda4 | -3.62043 | -48.91492 | 2025-10-15 00:35:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| eba6801b-cd5f-35a5-af0d-97f4497c58e9 | -8.72063 | -43.86118 | 2025-10-15 00:35:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 0339fe90-05f1-3740-8819-21b82807b4c0 | -4.42712 | -47.76128 | 2025-10-15 00:35:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| e03e314a-259d-34fb-80ae-4a10ea93294b | -5.2481 | -44.47282 | 2025-10-15 00:35:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| c1069a8a-e583-32f5-a851-4233c133a623 | -5.49306 | -45.83236 | 2025-10-15 00:35:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8922754c-390b-34b1-b97b-43240e9af966 | -7.94346 | -44.12273 | 2025-10-15 00:35:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 31.7 |
| b9e0786b-280b-392d-b242-3090e48c8bb4 | -8.18252 | -44.03303 | 2025-10-15 00:35:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 19.3 |
| a857b62b-8c5b-3731-a28f-578ade2206f7 | -4.90083 | -43.44141 | 2025-10-15 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 39f7fcc9-8e15-3750-af79-03cb20fddd29 | -5.42897 | -44.23962 | 2025-10-15 00:35:00 | TERRA_M-M | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 690429f7-7bc9-33d7-a464-534e71880df5 | -5.39955 | -45.44552 | 2025-10-15 00:35:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 29b7d19f-c4ba-3c35-92cc-d2beb73c46ab | -5.88685 | -44.2262 | 2025-10-15 00:35:00 | TERRA_M-M | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 507a91a5-aff6-3428-b390-3e026f8198ea | -6.57269 | -42.96262 | 2025-10-15 00:35:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 8dfbc54d-c3a8-3d9e-a42c-bb984cc86120 | -4.04035 | -45.26509 | 2025-10-15 00:35:00 | TERRA_M-M | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 261b1e0c-cead-3727-ae32-f68e919dde19 | -5.02837 | -45.0205 | 2025-10-15 00:35:00 | TERRA_M-M | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 0ee80b68-31f4-3986-a944-a0fea64d3ead | -4.99614 | -47.28915 | 2025-10-15 00:35:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1b2d1030-397e-3956-8585-bccbe70bb0ea | -2.87747 | -50.73319 | 2025-10-15 00:35:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| e6063365-1332-32a6-8476-a1f536284462 | -5.89182 | -43.76145 | 2025-10-15 00:35:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 20.0 |
| f8c95c1d-4bf4-3cc6-9b83-9379ee06932a | -4.11069 | -48.0181 | 2025-10-15 00:35:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| a6638f92-5bb0-3caa-9113-16cadbb3967d | -4.89321 | -45.50904 | 2025-10-15 00:35:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| c5704a70-352f-3297-b961-1d255b7de35d | -5.92246 | -42.81387 | 2025-10-15 00:35:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 17.7 |
| eaffd7ca-4b89-3304-b716-682706895a75 | -4.31676 | -44.55549 | 2025-10-15 00:35:00 | TERRA_M-M | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 3611e8d6-2e66-3caa-9e2c-06d73889523f | -3.15861 | -49.17538 | 2025-10-15 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 1a6b8b1c-9e1c-39fe-96af-2f32fdbe762b | -2.71871 | -48.3347 | 2025-10-15 00:35:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5312c02b-4732-3a0c-810c-b4de9cb2bddf | -7.25421 | -44.90758 | 2025-10-15 00:35:00 | TERRA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 9d408748-b11e-3abf-8cf6-0af2bf0d5fb7 | -4.54458 | -45.41281 | 2025-10-15 00:35:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 874c07cc-62aa-3e03-8dcd-cc9f01e18c96 | -4.80846 | -45.71004 | 2025-10-15 00:35:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 46182f76-2e74-31de-8230-64389234848c | -3.97308 | -48.08018 | 2025-10-15 00:35:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| fa693b52-55e7-37e0-844e-da13f53b168c | -8.45783 | -44.17999 | 2025-10-15 00:35:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 04248cb4-6f2a-3013-a09a-5a1ea20d0299 | -3.61143 | -48.9162 | 2025-10-15 00:35:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b5cee632-8994-3122-ac99-700376e5eaf9 | -3.07592 | -49.50502 | 2025-10-15 00:35:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 18aa261d-fe54-3f80-b8cb-8f2f1b543c6e | -4.01448 | -48.96496 | 2025-10-15 00:35:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 37355bbe-5b7c-373d-8f39-b41b0af2c3bc | -3.66606 | -45.22202 | 2025-10-15 00:35:00 | TERRA_M-M | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 2e1e4df6-b7ac-35f4-aad2-fbf934672c65 | -7.36261 | -43.64667 | 2025-10-15 00:35:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 9a41fdc6-cc3f-3fd5-9773-2ebe497c0f1f | -6.05042 | -41.90548 | 2025-10-15 00:35:00 | TERRA_M-M | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 24.7 |
| b4b2aa69-87c9-358d-8362-c7366da6dd4f | -5.85897 | -43.87822 | 2025-10-15 00:35:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| ee5defc7-6a00-3f5c-8b95-10e9251ed9f5 | -5.91244 | -42.83768 | 2025-10-15 00:35:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 21.2 |
| f847c28d-e69b-315f-8fe1-92318764acfa | -5.31424 | -44.62161 | 2025-10-15 00:35:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| a26bca1c-1c25-3fbd-905f-d70931d5568d | -4.90193 | -43.44807 | 2025-10-15 00:35:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 150.5 |
| 7749018b-1d98-3832-89a1-7bc2e3ef7eeb | -8.21964 | -44.04416 | 2025-10-15 00:35:00 | TERRA_M-M | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 53bdc66d-2efc-32ee-b8ae-236efb3158ea | -5.03082 | -44.73163 | 2025-10-15 00:35:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 38.6 |
| bf3b730a-2010-3653-9877-487237138c3d | -5.89459 | -43.75447 | 2025-10-15 00:35:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 25.3 |
| f17c9860-8210-365c-aa45-5e339e846411 | -8.73466 | -43.87546 | 2025-10-15 00:35:00 | TERRA_M-M | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 22.5 |


[Clique aqui para ver as próximas entradas](README5.md)
