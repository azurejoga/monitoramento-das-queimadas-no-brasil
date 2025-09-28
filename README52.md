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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 88fb2673-f0dd-36a0-9d79-02dd4ec4d4f3 | -4.77698 | -41.04491 | 2025-09-28 04:23:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c33fc934-73da-35fe-b2be-7fa9444394a6 | -5.79905 | -42.78794 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 72d789bb-7820-3433-bcc5-16c073f991e2 | -3.79012 | -48.86592 | 2025-09-28 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4fe9c878-0772-3863-bf7b-c6f01d887d81 | -4.86915 | -42.95565 | 2025-09-28 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d54cc15-2004-3b01-a9b5-b4fa74bc6f1a | -5.33871 | -45.64455 | 2025-09-28 04:23:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8bcc35df-71b4-39cd-8e4f-e7a86a889e5f | -5.29056 | -43.15606 | 2025-09-28 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4d978afc-30df-32f6-910b-2e105be6c51e | -5.7596 | -42.80334 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| d57527d9-e127-3d0d-bf7f-58045ba76776 | -5.15257 | -46.4142 | 2025-09-28 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef86f5b9-2a01-3408-8bc3-93b412c0e977 | -4.88557 | -43.37004 | 2025-09-28 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 66be9103-6ca4-3796-851d-e12da2bf091f | -3.79017 | -48.86872 | 2025-09-28 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8fc11e42-de05-3d14-900f-1af4e1d7e75f | -5.22337 | -45.92295 | 2025-09-28 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e29561dc-5fd5-3788-96ca-1770dab012e1 | -5.81034 | -42.81117 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| dab51106-19e6-33e6-946d-c6ffc0f73963 | -1.13491 | -46.32518 | 2025-09-28 04:23:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 14979f2b-956a-332d-8bfb-45fd36a7b4e7 | -5.28867 | -42.77257 | 2025-09-28 04:23:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 59c61683-c649-3740-ba7b-fbe343531d24 | -5.24704 | -42.70629 | 2025-09-28 04:23:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e1efe51b-9f22-3860-bd93-1fcb1a9e8035 | -5.30035 | -45.32598 | 2025-09-28 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| afae572f-3d24-30ae-99d8-b8c5cea1ce49 | -5.81075 | -42.83261 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 376936e1-7c1a-394e-b1b3-d0507afc9c1b | -5.36048 | -42.28428 | 2025-09-28 04:23:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| dac5c7dd-b358-3e9b-9fd1-56d5bdf0989f | -5.07514 | -44.85807 | 2025-09-28 04:23:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34f8c054-55f4-395a-ab5f-943e1cb685a0 | -4.44772 | -43.98723 | 2025-09-28 04:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6669c1a2-9dc6-3c7c-ab23-93532fcc14a7 | -5.70716 | -42.60556 | 2025-09-28 04:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8d8faba7-1ef1-37ac-822d-75eb5abde25b | -2.58449 | -48.40169 | 2025-09-28 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 202887a4-eb4c-34a8-9c4c-bbf888938d32 | -4.87334 | -42.95212 | 2025-09-28 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| ec265cd3-672b-3a91-9960-54d9bc09b86a | -4.87761 | -45.85463 | 2025-09-28 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b72e0b4e-6378-3bba-89f1-166f1d2b645f | -5.81755 | -42.81249 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 688f592f-9929-3633-ba92-ae9ba9c8d406 | -4.18969 | -46.16637 | 2025-09-28 04:23:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ac86be7-5fa1-3ee4-8ec0-8154b4ba7acb | -3.33446 | -46.54542 | 2025-09-28 04:23:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b613aa36-c566-37ff-bb7f-4da6971975f8 | -3.79241 | -48.87498 | 2025-09-28 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90e2d1bf-1a65-318e-b831-aa7a9cbceb42 | -4.14817 | -40.00751 | 2025-09-28 04:23:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 4900502a-e5d4-3060-94e3-7957adff7168 | -4.9722 | -43.2032 | 2025-09-28 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b33e11c-f316-378d-ae8b-818b1dab9a26 | -5.71392 | -42.65935 | 2025-09-28 04:23:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a9b93d3b-0014-3680-b34b-3b4b00cd6438 | -5.80712 | -42.83212 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 09bd72af-d667-3db8-aac4-2fb08f8c6ce9 | -5.81885 | -42.80404 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| c360fee9-33ad-3f2a-ab19-e0739a5fd72d | -4.87628 | -42.95671 | 2025-09-28 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 27795ef0-93db-3250-8c08-b76f01354e8b | -5.15203 | -46.41765 | 2025-09-28 04:23:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95b495ec-16dd-3ecf-9cec-cc6a92bcba99 | -3.67587 | -38.81327 | 2025-09-28 04:23:00 | NOAA-20 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2a52a5c0-a5b7-3023-8cbb-195d3d28f8b8 | -5.35577 | -45.03787 | 2025-09-28 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 074a896c-bc3e-3e98-a8c8-54df1e2be59f | -4.67632 | -43.24859 | 2025-09-28 04:23:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f72f6ee5-a918-35e0-a00a-ee82ca43c29e | -4.14875 | -40.00371 | 2025-09-28 04:23:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 19af45ab-5c67-3509-8b88-90da0759a307 | -2.44637 | -48.60767 | 2025-09-28 04:23:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a1708280-04bb-3cf3-a4b1-ff1028b4d85a | -5.74637 | -42.89089 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| fc1eb059-17f6-3847-8a7c-00991c6f4835 | -5.23117 | -35.59916 | 2025-09-28 04:23:00 | NOAA-20 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 3.1 |
| eb6efd0e-2d89-3fe7-92c0-da7918827629 | -4.25604 | -48.59704 | 2025-09-28 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0aad69b-243a-3f84-b41b-83db3d58874f | -5.45962 | -41.07901 | 2025-09-28 04:23:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8a872052-9527-3ec8-8bea-f2d7651c30fd | -5.31731 | -42.76314 | 2025-09-28 04:23:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| d19a797d-3048-3b7a-b1aa-7e330ea65bac | -5.80969 | -42.81537 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 33.8 |
| bb132123-56bd-317f-80dd-8c4492614eff | -5.33926 | -45.64109 | 2025-09-28 04:23:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4e92d5c3-fe1b-347f-a352-4456d2d4c56b | -5.80264 | -42.86126 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 400fdfb3-2f15-3e55-a14e-d7fb762735f5 | -5.747 | -42.88673 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 171d3b4f-295c-349f-afd2-33c153505b07 | -5.80991 | -42.78975 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 7112ff82-5aac-38cb-8aaa-e05e1f25370b | -5.51546 | -42.73884 | 2025-09-28 04:23:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 1ea97570-d482-3855-bd4d-d564e100a830 | -1.40316 | -48.05253 | 2025-09-28 04:23:00 | NOAA-20 | SANTA IZABEL DO PARÁ | PARÁ | Brasil | 1506500 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52d7775e-78ef-35ba-bd3e-5d85f42122f4 | -5.08823 | -37.60818 | 2025-09-28 04:23:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 08acb470-c271-3491-a34d-798f5ae98c42 | -4.77228 | -41.04914 | 2025-09-28 04:23:00 | NOAA-20 | PORANGA | CEARÁ | Brasil | 2311009 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9f4c83ca-1f86-319d-8762-a78e97f1828b | -5.61637 | -43.36487 | 2025-09-28 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6ffd69fc-78dc-3f60-b1a1-fc83069d8f0c | -5.36281 | -42.28312 | 2025-09-28 04:23:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| ebc62004-53a5-3cfb-a89d-14f751789949 | -5.73642 | -42.65873 | 2025-09-28 04:23:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f92294b2-b4f4-3b14-b6c0-5fcc9cf2f244 | -5.61576 | -43.36882 | 2025-09-28 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 65b208ce-22b9-33e5-a802-6172912de87c | -5.8182 | -42.80828 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 82032005-c9c5-3511-82e6-a7a420ca9eb1 | -5.81691 | -42.81664 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| f5e6c6ef-aa91-37da-a198-09e9d36d11c8 | -5.10065 | -46.07667 | 2025-09-28 04:23:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c602811-9fad-332d-aec7-32ba40e28fa3 | -5.7765 | -42.88708 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d0e8293f-883c-39dc-8603-d005eed2e78d | -5.81949 | -42.7999 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| fa8c1dbf-fa93-303b-90b0-8572cebd3263 | -5.30348 | -44.78806 | 2025-09-28 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 97d49dc8-196c-3f1f-9ece-51ac8a06d52f | -5.60459 | -43.37108 | 2025-09-28 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 920c5ba5-c4be-3a69-bb0e-7616fd6f65ff | -5.39994 | -42.28871 | 2025-09-28 04:23:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 749c1531-dc76-3fa0-996a-c90d0dce1035 | -3.31883 | -52.53672 | 2025-09-28 04:23:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 825ce386-a91a-3dc4-8fd0-1e73a04c1413 | -5.41747 | -42.27316 | 2025-09-28 04:23:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c9b2c7fe-7bf7-3d62-8e63-465cfd47793d | -3.0822 | -52.92213 | 2025-09-28 04:23:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1d5dc623-4642-3900-8b26-c4ee7cbf0cee | -5.07959 | -44.85154 | 2025-09-28 04:23:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 967f8eda-2f7a-376b-87ab-f4c9a3dcc955 | -5.70024 | -42.62651 | 2025-09-28 04:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| decd5733-2e29-3a12-8620-d2a0af417147 | -5.67185 | -43.05303 | 2025-09-28 04:23:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 41885340-5f29-32c4-b9b8-1b84a7f3ac8e | -2.97943 | -39.93173 | 2025-09-28 04:23:00 | NOAA-20 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cbb1a9b1-abcd-3793-8381-6cc30c604a31 | -5.61989 | -43.36542 | 2025-09-28 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cee2b044-3251-39a1-989d-b2d15884850b | -2.91531 | -48.19454 | 2025-09-28 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04d6b14b-3922-30da-ae0d-c60dd29b0f05 | -3.02837 | -50.44291 | 2025-09-28 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 159e347f-8bd8-3ff5-bddb-65a3c889eede | -4.90486 | -47.14096 | 2025-09-28 04:23:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0cc29d0-f9dd-3d6f-8996-22f91593025e | -2.72839 | -48.59817 | 2025-09-28 04:23:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0516bc81-23af-314c-8925-073577d89490 | -4.62166 | -43.10849 | 2025-09-28 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31f60fae-499d-31a8-a32d-03c7fb509d94 | -5.26416 | -42.88312 | 2025-09-28 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8cf5ad52-7bd4-38e9-907c-64b9abaa8000 | -5.19762 | -43.71469 | 2025-09-28 04:23:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9b317383-ebea-321d-9441-568010f46963 | -4.26139 | -44.76017 | 2025-09-28 04:23:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bf5eb9c7-dcc8-3c22-b0fe-9cc83726edbf | -3.3053 | -52.58908 | 2025-09-28 04:23:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5319976-b270-39d3-bb30-06f30984da93 | -4.75479 | -42.69425 | 2025-09-28 04:23:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 432e4e41-318f-3688-8e34-7b3b10b3f663 | -3.92635 | -49.1381 | 2025-09-28 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f847d52f-090d-395a-b83f-56a6f20ce760 | -5.35855 | -45.04189 | 2025-09-28 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fad6edab-b23e-3d43-a2e7-17456186c267 | -5.5415 | -42.73839 | 2025-09-28 04:23:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 0b476bd2-c5a5-3db6-9261-7ef64edffb93 | -3.80742 | -47.58043 | 2025-09-28 04:23:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3bf2fa7-2059-32a2-a016-f7a95768c9c6 | -5.14559 | -45.70575 | 2025-09-28 04:23:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c418cb6-1385-3501-ad1e-4a1b4e482ffb | -3.27139 | -51.15474 | 2025-09-28 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f91d5a2b-27bd-3bdf-8e5d-ad1174dca9fa | -3.21159 | -51.28158 | 2025-09-28 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 986eb8a5-164a-3fd7-be25-1a22550382e8 | -5.71815 | -42.60723 | 2025-09-28 04:23:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e0a9a1ed-95cf-3bb8-abba-f03ffdc1677e | -5.22443 | -44.6339 | 2025-09-28 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8cd9f1ee-479f-3c00-9c59-f112f4db0780 | -3.08195 | -47.84952 | 2025-09-28 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b131a80-9946-3f17-94cc-a0d6990980f2 | -5.51936 | -42.73189 | 2025-09-28 04:23:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a4bff6d1-0aec-3cc9-8a1b-da672796cf73 | -5.29702 | -43.16119 | 2025-09-28 04:23:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 362b2996-038c-38dd-b988-77bb8c5affd3 | -5.70596 | -42.66255 | 2025-09-28 04:23:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7b112137-5a5a-30da-8a37-a85593eb107f | -4.81029 | -42.79827 | 2025-09-28 04:23:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d1f03a84-8671-3fdb-aa70-065a73082e44 | -5.27048 | -44.73581 | 2025-09-28 04:23:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cd340307-f972-343c-a784-fd73c52c5b38 | -5.78667 | -42.89301 | 2025-09-28 04:23:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |


[Clique aqui para ver as próximas entradas](README53.md)
