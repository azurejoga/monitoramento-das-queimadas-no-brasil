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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5f243266-0c3e-3754-99e0-db83354cb7ab | -6.68357 | -42.78858 | 2025-09-30 04:38:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c40ca1cf-33c1-34f7-b0d5-1627c01d4f45 | -6.01135 | -43.80322 | 2025-09-30 04:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b45dcdc-5d81-351e-989e-8c8a8103e0ab | -6.20438 | -44.20931 | 2025-09-30 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fe3a408d-852d-37e6-a8de-16fee7420b31 | -6.33941 | -43.75122 | 2025-09-30 04:38:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44af7361-ec15-34ac-99c6-4c69c0c2fd85 | -5.51666 | -43.87564 | 2025-09-30 04:38:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c664aa11-bb79-33e2-9436-f88dd9fb0585 | -6.79322 | -44.08263 | 2025-09-30 04:38:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b4f261d-6695-3125-a341-cfd17d0d5579 | -6.56012 | -43.42274 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 6.3 |
| a2320dcf-e3ab-3ea5-8844-cd651a22aa1b | -6.55635 | -43.41821 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 09453f50-1fd4-3675-9197-ff653b3b193e | -4.81891 | -42.76774 | 2025-09-30 04:38:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ea116fce-0103-3bd8-b215-71860ae4582f | -5.74384 | -42.67996 | 2025-09-30 04:38:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 1a53e173-793a-3828-9208-762099aa5fd5 | -5.51254 | -43.87496 | 2025-09-30 04:38:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 197d98f3-8ca9-3c32-b866-6ab1811455ec | -4.40448 | -44.39304 | 2025-09-30 04:38:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b945ce19-459e-3b52-be96-c542e3de9b90 | -4.48164 | -47.67102 | 2025-09-30 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2606b5ea-0da9-3bd0-b3c5-6dea7001e147 | -5.30019 | -43.16897 | 2025-09-30 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa8ffce3-69a7-332d-943d-2d8bf60eb81e | -6.9917 | -42.80072 | 2025-09-30 04:38:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ba14283d-0475-3c2d-b740-0f0fa803c72d | -5.42431 | -42.28617 | 2025-09-30 04:38:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 9a949ecc-fda3-3106-95c2-d61d2c7dc4c5 | -7.28362 | -42.85904 | 2025-09-30 04:38:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ab07fa0a-34f3-32f9-8d3e-ced136b83323 | -6.38596 | -42.91039 | 2025-09-30 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 9160c580-9d75-3282-bbca-a5f5657fc289 | -5.89048 | -47.59226 | 2025-09-30 04:38:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 089dbe45-e19a-3daf-b2ca-6b8dd56fec85 | -2.44204 | -47.33261 | 2025-09-30 04:38:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6bed424b-4333-3373-a267-90619a948885 | -6.67715 | -44.45318 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2815b7ef-c3ce-3d66-9ac1-abdee6331dda | -5.89553 | -45.88034 | 2025-09-30 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4009ac54-45cf-363a-9daa-dd55978c0c34 | -3.54045 | -52.20316 | 2025-09-30 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a4ff744-e946-365e-b6a8-f9eb96584c31 | -6.29287 | -43.92093 | 2025-09-30 04:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| aefa005a-7d4d-30e0-8484-20d9fb8fc0b0 | -5.87508 | -47.02151 | 2025-09-30 04:38:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3806fcb-58e3-3118-a919-5826464a34c6 | -6.24996 | -43.65467 | 2025-09-30 04:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6f5b44c4-1c4f-34cf-ac37-dee395b84fd9 | -5.22293 | -45.22688 | 2025-09-30 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ff9411f5-43c2-3fcd-a0a5-56d09c4a737f | -5.52491 | -43.87702 | 2025-09-30 04:38:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 3eae5b55-a377-3aee-8cb6-1b40b55b9782 | -6.80428 | -45.98317 | 2025-09-30 04:38:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9d3f461-7c55-37db-8337-5890284fb68f | -5.81725 | -42.86091 | 2025-09-30 04:38:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 93a24c43-1751-3c09-9d9f-213ec65d5cbb | -1.99089 | -44.52866 | 2025-09-30 04:38:00 | NOAA-21 | CEDRAL | MARANHÃO | Brasil | 2103109 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8ccd48a3-2671-365a-94b4-68aabc350284 | -6.52104 | -45.22467 | 2025-09-30 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ac02175-474b-3763-995b-fdf74f371191 | -5.37407 | -42.84963 | 2025-09-30 04:38:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| e85ed57b-c958-32a3-ad3b-1c7cc3e3aa81 | -4.66507 | -46.46849 | 2025-09-30 04:38:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 461720aa-ff36-3f5e-9589-793f45317851 | -4.51131 | -40.72414 | 2025-09-30 04:38:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 507232b2-ead8-3ec9-b32a-1706602912f5 | -6.51094 | -45.21329 | 2025-09-30 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| de498c18-61d1-3856-8055-5c97a2fb5576 | -4.98043 | -46.79725 | 2025-09-30 04:38:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d94778f-3b9c-3618-8c4e-10359e21732b | -4.25976 | -48.55396 | 2025-09-30 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7d243d98-e1c8-363c-aa46-2b70614f9437 | -3.22584 | -47.63396 | 2025-09-30 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f8dbce9a-93b3-3cc1-9a10-833a27f2c8d5 | -2.91706 | -48.19546 | 2025-09-30 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f21bb483-ff48-34cd-8356-90bc02cf1cbf | -2.93302 | -51.94294 | 2025-09-30 04:38:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2089b6d8-fb14-3d97-a4d7-c0fe2e641c09 | -6.79378 | -44.07882 | 2025-09-30 04:38:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 05135913-9232-3b6f-af18-8ae21209d124 | -3.03903 | -48.78717 | 2025-09-30 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8816b2a2-efbf-3e61-9d6f-74f8f3d64660 | -5.83585 | -43.94104 | 2025-09-30 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 50448a7f-8f1d-3cd5-b652-deaa8a51a333 | -4.78343 | -41.04729 | 2025-09-30 04:38:00 | NOAA-21 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3b21f240-db4f-35d0-a1b4-62f8d763d30c | -6.05307 | -42.47902 | 2025-09-30 04:38:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 534bdc95-e82d-3cc9-918b-7ae374b1df5b | -5.18501 | -46.07285 | 2025-09-30 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b43a04ff-b1f5-31bc-a775-ac0d2e1945b3 | -3.8106 | -47.57196 | 2025-09-30 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13a4ef07-b1da-3977-8895-876a984da4cb | -6.94541 | -45.39319 | 2025-09-30 04:38:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 27f0c2dd-5fb6-3817-8c02-68ff5e7db74c | -6.81274 | -44.2087 | 2025-09-30 04:38:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b576bce4-da12-315e-a4aa-4fecd3965b71 | -6.37301 | -45.61943 | 2025-09-30 04:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b84ea8ef-7ba5-331d-b2e4-cef0d4e27b70 | -3.3336 | -50.24721 | 2025-09-30 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97cb00f9-901b-37ea-b32b-eb308840e73f | -3.98607 | -47.88487 | 2025-09-30 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 769327d2-f009-3a8c-b8a5-678ef47973c0 | -3.10199 | -48.60046 | 2025-09-30 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0963c3c-74c7-3271-8cff-eda647169b70 | -6.88736 | -44.52515 | 2025-09-30 04:38:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b24197f0-987f-35f8-8ddc-2def0debacc9 | -6.02036 | -44.75756 | 2025-09-30 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ea6a6ba-b6a4-3bf1-88f6-9a664daf068f | -7.17999 | -41.70182 | 2025-09-30 04:38:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 97ce456e-00d1-3ffc-8729-ef37b03cf36c | -2.25899 | -49.52944 | 2025-09-30 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b92bf5be-cb47-3fba-b982-d16f260eeaf3 | -5.85797 | -45.75412 | 2025-09-30 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 43fd415a-faf0-3963-b5ef-cb15be695935 | -1.29247 | -54.18911 | 2025-09-30 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6ae4cc9d-bbc1-32de-bdbb-c67abeeceb18 | -5.82713 | -42.7904 | 2025-09-30 04:38:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2eef5411-f451-3225-89b2-a1660d1abf6e | -6.69195 | -42.79455 | 2025-09-30 04:38:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2b9ce3f1-020f-3b20-8c44-c089a821d761 | -6.93634 | -45.40162 | 2025-09-30 04:38:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0760d0af-7d07-37f0-b40d-d8a6621c8093 | -4.95877 | -47.6008 | 2025-09-30 04:38:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 408d9259-bf02-3664-8576-2fcea168565e | -1.29308 | -54.18525 | 2025-09-30 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ef856200-3c18-3936-9e10-98693d6cb17d | -6.25054 | -43.65078 | 2025-09-30 04:38:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1958b4ab-9546-3b10-b614-bdaa123ee048 | -5.86644 | -45.77333 | 2025-09-30 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3502ff3a-340a-335f-a341-f6c33f8db76b | -6.10274 | -42.65862 | 2025-09-30 04:38:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.5 |
| ac3c6f7c-8392-3591-a25b-e9351caddb5c | -5.48224 | -48.65681 | 2025-09-30 04:38:00 | NOAA-21 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cca49851-f163-3fb4-9754-712bbb24be5d | -5.57658 | -44.85485 | 2025-09-30 04:38:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 82d01e3f-de57-3771-93cd-3a05d206af03 | -6.29333 | -43.46962 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 292b963a-0ac2-3de2-9e82-88e06e0d2052 | -4.29341 | -48.27242 | 2025-09-30 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cbc7b7ee-69aa-3bca-8b05-4d55c31d7c32 | -3.28271 | -50.03197 | 2025-09-30 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d93ddde3-718a-396a-8a99-fd2448795986 | -4.52169 | -50.52869 | 2025-09-30 04:38:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb276325-00c3-358f-b180-8c562acb6364 | -6.5744 | -43.41572 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2710e362-08dd-3fb5-b78b-9dc683c15656 | -6.45191 | -45.91528 | 2025-09-30 04:38:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea54fff2-3cce-32e5-8d4e-d7c1f5cbf995 | -5.10724 | -43.07094 | 2025-09-30 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca2b2e50-e89d-34e5-bc09-fac8bc13d7fd | -5.66933 | -45.29904 | 2025-09-30 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b395775-b7d4-312e-b692-6e58971416e1 | -2.3194 | -49.16618 | 2025-09-30 04:38:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f3eeeae3-cdf1-38d7-95f6-ef147b0c10a0 | -3.25539 | -50.11839 | 2025-09-30 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9e0966e7-1574-36fc-833c-80b5c7239f7a | -4.6449 | -47.95787 | 2025-09-30 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d8e1bc16-85d7-347b-a153-8dfb3c597f3d | -6.04621 | -44.85345 | 2025-09-30 04:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af32bfb0-6da0-30c9-8d27-f317b4ba6657 | -3.34407 | -43.39454 | 2025-09-30 04:38:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0fd2c6d-577f-37b9-83c4-77a872e88246 | -6.05373 | -44.18664 | 2025-09-30 04:38:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75fcbb64-ccba-3e40-8c67-47f27d7f7a17 | -2.58092 | -48.40671 | 2025-09-30 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ce8f9f5-3d69-3cb4-9e18-e525620b1645 | -5.74068 | -42.68694 | 2025-09-30 04:38:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 563d4bb5-2d80-37d3-b3a4-be9ab4bbcce6 | -5.23154 | -43.69302 | 2025-09-30 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8df69c54-1e55-3d56-9fd4-ee685f9d28c9 | -6.49524 | -44.27002 | 2025-09-30 04:38:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fec9c9ba-4de5-3484-95e2-b0c606e54ac0 | -5.31005 | -43.16205 | 2025-09-30 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 2acad120-52c4-3226-845a-f6ba81b7d157 | -5.23097 | -43.69689 | 2025-09-30 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7e3f9faa-79b8-39ea-a9c5-6a491f224788 | -5.29528 | -43.1724 | 2025-09-30 04:38:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 773a1673-c757-3650-9b0e-594940ea2340 | -4.86863 | -45.05743 | 2025-09-30 04:38:00 | NOAA-21 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 7ff2a0f0-1ea0-3421-93ef-7609211061f4 | -5.17928 | -41.24202 | 2025-09-30 04:38:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| c21f133c-fcc5-33e4-95ac-dd68848310e8 | -3.81005 | -47.57552 | 2025-09-30 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 368df901-9fc7-3da6-b94e-cb8c23adaa62 | -5.73231 | -43.96703 | 2025-09-30 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d47f08dd-82f5-3ee0-9acc-cafe6387d704 | -0.09665 | -51.27989 | 2025-09-30 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a4881b81-05d4-3754-894c-9f45f0101cd1 | -5.96763 | -43.78077 | 2025-09-30 04:38:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4fd53735-c40b-3ac3-8113-2359d1e21538 | -5.53721 | -45.89727 | 2025-09-30 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b90b637a-015c-3082-806c-f1bde79dbdad | -6.64844 | -45.32651 | 2025-09-30 04:38:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de0a371c-a2ae-3bc0-a3fc-58ec999adcc4 | -6.4973 | -44.11687 | 2025-09-30 04:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README51.md)
