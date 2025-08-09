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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7128d4a6-8a90-3cb3-abae-36ca6d0f27a0 | -6.12291 | -42.95982 | 2025-08-09 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 48e3140c-58ce-3c6a-b874-0d10d9b8e90e | -6.32212 | -42.35718 | 2025-08-09 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5f2e6b31-3796-3b22-a71e-488e93555617 | -6.12452 | -42.94947 | 2025-08-09 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| ad8bd4d0-d0a3-3ea3-ab47-7ee8f2d5946d | -7.90484 | -45.55482 | 2025-08-09 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cb56afe2-1cb6-3396-9a28-65e42851855b | -7.37219 | -44.6641 | 2025-08-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9426fa38-f69c-3375-a298-c6d940ab5304 | -3.42631 | -49.04208 | 2025-08-09 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 897bcdcd-0ea3-38e4-b669-16bd96a6bdf7 | -7.2056 | -44.65974 | 2025-08-09 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2822b851-7fa1-30ad-b14b-69094fec3aae | -7.29812 | -39.63769 | 2025-08-09 04:14:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8a14d518-6c02-369c-a0bb-f06a09b33eb4 | -6.70818 | -43.63305 | 2025-08-09 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 53221d13-35d2-399d-b876-a9515103c12e | -6.65475 | -42.00619 | 2025-08-09 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b7a1942d-3bcb-3f66-b1bf-b9df116061f2 | -5.28498 | -41.10321 | 2025-08-09 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 813505fc-8778-35be-9673-c2fddd4e9bf1 | -5.46888 | -43.96344 | 2025-08-09 04:14:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ddc6459d-e29a-38a4-9414-39a0a17fda5c | -8.32825 | -45.00068 | 2025-08-09 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 7fea2fd9-0baf-3b52-9451-4e917c9a25d0 | -4.78428 | -45.34578 | 2025-08-09 04:14:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bc4f24c9-70be-3851-ba9d-c51eb70b63a5 | -3.82232 | -41.55261 | 2025-08-09 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| adb298f6-e0b6-37f7-8e88-2591f57aa68f | -8.93427 | -46.73565 | 2025-08-09 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ad033676-e14a-3392-a4e5-a69685ae1158 | -6.83812 | -44.31809 | 2025-08-09 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7c4702fa-90e7-31eb-9f7d-50ce8c09bf6b | -3.64993 | -48.32445 | 2025-08-09 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 698767be-092b-35ba-9f96-c32dbb1daa55 | -9.07843 | -40.4771 | 2025-08-09 04:14:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 8.1 |
| a10173f7-b5a6-30b5-8c0b-93a6831ac996 | -7.25422 | -44.65633 | 2025-08-09 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f010230-2a77-3127-9718-fbbacf557eaf | -7.57597 | -44.40688 | 2025-08-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93a34169-daed-3b3f-8a0d-ee7cb6a585e0 | -7.11019 | -46.10526 | 2025-08-09 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8124e90c-ba25-3bc4-bd35-799486400486 | -6.57754 | -44.56652 | 2025-08-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30b2219d-59aa-39c5-96ce-adfe7ee29fa8 | -3.82067 | -41.5632 | 2025-08-09 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| e66a159d-a7fc-36bf-8b6b-63746c6cb3ef | -7.5793 | -44.40741 | 2025-08-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55b77955-75ad-38ce-ac0d-e5086bf61c92 | -7.25757 | -44.65684 | 2025-08-09 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b7eded7-8ae3-3c17-848a-2dcffee8ac03 | -6.32436 | -42.3647 | 2025-08-09 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ebc0dd3f-4169-3687-851f-03c93834bf0c | -6.13925 | -42.96595 | 2025-08-09 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e700d5d4-d80c-38c4-b200-36a04549359f | -9.52292 | -45.4072 | 2025-08-09 04:14:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 18737036-026f-3567-875d-68044ef6ba5f | -7.5871 | -44.93309 | 2025-08-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c191804b-0bde-3c6b-b3fb-c1f23ed9d58b | -5.41963 | -41.22931 | 2025-08-09 04:14:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| dc9c6a9b-4f24-30d1-9db0-f24886c71bce | -8.31819 | -44.99902 | 2025-08-09 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b11aeff-2591-33cb-911b-3dc747be4487 | -5.27318 | -44.94895 | 2025-08-09 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9fcd822-4d41-3a77-a70c-9abf1f85b9ed | -7.8974 | -45.55742 | 2025-08-09 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 686226d3-9957-37f1-8023-196f93965750 | -7.90423 | -45.55856 | 2025-08-09 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f91237f7-a809-3dff-877b-3fc2580e268a | -6.92895 | -44.69205 | 2025-08-09 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5a73879-f5fa-3596-9ef9-7afb901d3f77 | -6.68167 | -43.3243 | 2025-08-09 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0698ea13-8bde-340f-bedf-cf3014ec79f1 | -9.65717 | -43.84714 | 2025-08-09 04:14:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3aba6276-2e42-350f-8d75-675c6d8e6070 | -9.08447 | -45.05984 | 2025-08-09 04:14:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42e36ee3-0ec7-3a66-af7f-673b9793639c | -8.87671 | -47.4683 | 2025-08-09 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d6e9900-bb14-38ac-a6cc-b83bdf59056f | -9.07915 | -40.00246 | 2025-08-09 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 0e52788f-3d0b-341d-9141-eecb27bb5c37 | -6.08663 | -42.23054 | 2025-08-09 04:14:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8fc1a205-0c6a-3b27-a760-792e9baa56b8 | -6.252 | -42.74245 | 2025-08-09 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a5f7586c-28eb-3f3c-b87d-3522eb6a1e47 | -7.22795 | -44.67043 | 2025-08-09 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d141d27-8d03-3371-9717-173ad1565e37 | -7.73361 | -45.52727 | 2025-08-09 04:14:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 499d1a27-55c0-3ae4-b2b2-ae1473df849f | -7.4896 | -44.86251 | 2025-08-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8b19c85-6d7f-397d-bf40-caa39506872c | -5.13186 | -42.88149 | 2025-08-09 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eaf0e030-f2a9-3bc5-8a55-2e8932b74313 | -8.11289 | -47.43494 | 2025-08-09 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4abfe847-d138-37f4-be6b-55defe1d275f | -6.12398 | -42.95292 | 2025-08-09 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 03dda066-78f5-3e69-acd5-f89993a672e0 | -6.6503 | -42.01283 | 2025-08-09 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2448be58-f3fb-3f29-8c88-8fb4d6082599 | -3.07025 | -40.8146 | 2025-08-09 04:14:00 | NOAA-21 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 6.3 |
| a371be42-bbf1-3503-8cf0-63b849269cc8 | -5.39008 | -41.33018 | 2025-08-09 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bcc3febd-ec80-39bc-87aa-0e1d1a3152f5 | -5.83845 | -42.95384 | 2025-08-09 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f6820f5e-2a13-32df-927f-7b6041dc761a | -3.82177 | -41.55614 | 2025-08-09 04:14:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e444faad-7b12-307e-8256-ac92a61b3a19 | -5.82407 | -42.93747 | 2025-08-09 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 39cd225c-e479-32ef-97be-e338c28eaf3b | -6.58424 | -44.56761 | 2025-08-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| a5ec626b-b8bd-3ac6-87df-60b578328047 | -3.84484 | -47.75361 | 2025-08-09 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 225ff5c4-3cd0-3524-bce2-987e72652213 | -7.9002 | -45.56173 | 2025-08-09 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55a46ca9-8b3b-3517-979c-3b3a28fb2d34 | -6.05711 | -43.7496 | 2025-08-09 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 0459e6d8-05f7-3212-aafb-79ce12fe37fe | -5.08527 | -48.31113 | 2025-08-09 04:14:00 | NOAA-21 | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5cf2bb8-5a16-3368-81d5-a7eec5bb3d83 | -6.26622 | -45.19559 | 2025-08-09 04:14:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e0eecd7c-301d-3825-bdd2-f19a48f61538 | -6.4931 | -45.00818 | 2025-08-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 207bfed2-eb94-3bd8-a048-59c8b0a3d49d | -6.05766 | -43.74612 | 2025-08-09 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| afbffe2c-05b9-3257-910a-e9aacda6a4d2 | -4.34048 | -49.35732 | 2025-08-09 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a153c563-68fc-3a98-a33a-b37165e8c2a8 | -9.3834 | -40.2532 | 2025-08-09 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6dc0fcd9-1100-3104-a907-5a10ec21a56c | -8.06388 | -46.33191 | 2025-08-09 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a15b8098-c667-3554-a062-c4483ef7499f | -5.46832 | -43.96694 | 2025-08-09 04:14:00 | NOAA-21 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 97180b0c-3ee5-3414-bb77-0d09646f41a6 | -7.11371 | -46.10582 | 2025-08-09 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6ea015bb-193c-3a42-8029-2d69264b9762 | -7.90826 | -45.55536 | 2025-08-09 04:14:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 16aa0716-5985-3322-a1c2-8f9399054561 | -3.49094 | -42.84855 | 2025-08-09 04:14:00 | NOAA-21 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b011e068-5b14-3bf0-9c1f-69013a58ce44 | -3.23156 | -46.78708 | 2025-08-09 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7ccfd4d-1558-3ced-818a-77519c66ca9d | -6.13186 | -44.54385 | 2025-08-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| abd825f5-d253-3647-a6ca-45808e1e9f2b | -6.13972 | -44.53772 | 2025-08-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3114a6a-c885-30d3-a02b-a5448f10d7aa | -7.9612 | -49.39785 | 2025-08-09 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fa25a57d-ed2c-3ead-a365-b749c1e04ed4 | -8.8636 | -47.27351 | 2025-08-09 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c759aed-4d82-3987-b48f-f05bcc6f9c46 | -7.04082 | -43.55118 | 2025-08-09 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a572aa07-9e7d-3f14-9be6-74ae3d49236a | -5.27688 | -44.94926 | 2025-08-09 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a18c5ea5-e2ee-3c49-b35e-0766c2d3d653 | -9.07772 | -40.00418 | 2025-08-09 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 40c0fb8e-3229-3365-9941-7695e2f32809 | -7.26349 | -44.31736 | 2025-08-09 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e8c31498-1d16-3417-92ae-d50669489944 | -7.04467 | -43.54824 | 2025-08-09 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bf1c556f-bf59-38da-b23f-d453b8f643b1 | -5.27406 | -44.94501 | 2025-08-09 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ecc3302-1de7-3e90-a4a9-a9160d176de6 | -6.13979 | -42.9625 | 2025-08-09 04:14:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b371eafc-2e8f-3133-840f-07e146d03e17 | -6.59552 | -43.39523 | 2025-08-09 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a951b526-6a04-36e2-a09c-61c02525b0d3 | -8.87599 | -47.47272 | 2025-08-09 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e476b682-db9c-3975-b8c4-f008b9cb233e | -4.7083 | -40.63382 | 2025-08-09 04:14:00 | NOAA-21 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 92748abf-4b8c-38bd-8216-cef29361f013 | -6.5496 | -44.0136 | 2025-08-09 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e01c8555-c63a-34f6-b7e2-af9f21608166 | -6.13487 | -42.97234 | 2025-08-09 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 47ab19cc-7307-35fd-89d0-7914a40956e1 | -6.4399 | -44.59623 | 2025-08-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ab9ce5ec-89a8-3b68-a751-d16aaf0691b6 | -8.86653 | -47.27844 | 2025-08-09 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6f17acfc-c723-38c5-99f1-95cb6e65624e | -5.81915 | -42.94732 | 2025-08-09 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c3375623-373c-3bf9-ba66-5fed56e0ecfa | -6.06207 | -43.7397 | 2025-08-09 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 55cbae60-4a12-313f-b2fd-dd9ca5348625 | -6.94318 | -46.06277 | 2025-08-09 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c23d7ac-7050-3cd1-81f8-5e253063103d | -7.21344 | -44.65368 | 2025-08-09 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5dd428af-30ee-3a0b-a61e-2c196ed8087d | -6.96379 | -44.49339 | 2025-08-09 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 260d3caa-b8e1-33eb-a011-5c5b476d320a | -3.83999 | -47.75249 | 2025-08-09 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 164ea4df-7dbc-3922-80a5-2c2f7a972335 | -6.06429 | -43.74716 | 2025-08-09 04:14:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23fc1a44-bf88-3be3-b41f-259c7bab8beb | -5.22268 | -43.19196 | 2025-08-09 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| baab7f2c-8ffe-32f2-9807-7e138d7c59bf | -6.58145 | -44.5635 | 2025-08-09 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 77f840aa-9209-3ae2-bd90-5792ba79aeaf | -6.1354 | -42.96889 | 2025-08-09 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6c840043-b7e1-3603-abe5-62aeea97dba5 | -5.27628 | -44.95298 | 2025-08-09 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README11.md)
