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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3e19367-5e82-39d4-a6a5-5c6ea545f785 | -3.65124 | -41.1174 | 2025-09-20 03:34:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 4.1 |
| be8806a7-36af-3528-b1b8-271f1d6fef31 | -5.53216 | -43.87083 | 2025-09-20 03:34:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f2d144f1-0bf6-3398-a6e8-8aeaba001612 | -5.95914 | -42.91714 | 2025-09-20 03:34:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c710c997-174d-3e68-8417-cd475dcbe353 | -4.07468 | -40.47566 | 2025-09-20 03:34:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 55feef3f-5eac-3f6e-9f3c-233f0815f206 | -5.93172 | -45.07748 | 2025-09-20 03:34:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb1f3dc5-03ef-30ac-a463-00386b0f120c | -6.19727 | -41.22968 | 2025-09-20 03:34:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 4e998a54-ef03-3ed6-92fd-82a8ed3cfb4e | -5.73801 | -42.58675 | 2025-09-20 03:34:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 292e61dc-1fa4-3b16-923d-85146bb9379c | -5.96457 | -42.9181 | 2025-09-20 03:34:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| bbd854ee-81a0-3b56-9ef5-de692d316335 | -6.36508 | -43.46622 | 2025-09-20 03:34:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f5ac772-a421-3012-970d-d3bafb82f89c | -5.23314 | -37.67436 | 2025-09-20 03:34:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 482a9b86-753e-370b-b257-3e5fe5bfb665 | -3.65622 | -41.1183 | 2025-09-20 03:34:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cb6d7cdc-df3a-3723-a71f-697d09622735 | -6.40127 | -44.28927 | 2025-09-20 03:34:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b47fe61-c8c5-39fc-a424-07ca9e387dec | -5.10364 | -43.21141 | 2025-09-20 03:34:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| e0a5dc06-bdf8-33fd-a17a-38070046dc3e | -5.79191 | -43.6488 | 2025-09-20 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 958a214d-1ff1-3cc0-b28b-171036687e4d | -5.7926 | -43.64487 | 2025-09-20 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f18f6d24-3f5d-3213-96d9-104c5d1ba6db | -5.55394 | -42.15554 | 2025-09-20 03:34:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 25856294-0504-3777-a530-bc406f7e4628 | -6.40203 | -36.22863 | 2025-09-20 03:34:00 | NOAA-20 | JAÇANÃ | RIO GRANDE DO NORTE | Brasil | 2405009 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 431439df-3d2a-3f5e-acf6-30be745edf1f | -5.55751 | -42.16573 | 2025-09-20 03:34:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| f5f95fd1-71e7-3ace-b136-9a0fa9ddba6a | -5.79312 | -43.65103 | 2025-09-20 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b1b4a5b-9fa5-339f-a906-313eec0a07e0 | -3.65169 | -41.11421 | 2025-09-20 03:34:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8c6217b5-d0dc-35ad-b633-fcbc5f35cf3e | -6.95602 | -42.43556 | 2025-09-20 03:34:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ebe08c8b-5b4c-30e2-87ca-ca0cfc86a450 | -3.24663 | -39.30405 | 2025-09-20 03:34:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2068c538-ba5f-3711-99cb-792cb1a1746f | -4.07489 | -40.47749 | 2025-09-20 03:34:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fd7075d6-b14d-3acd-868b-f14eaeab8437 | -4.91865 | -38.68239 | 2025-09-20 03:34:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c97d98f7-5741-3709-aca6-2d497c175401 | -5.53183 | -43.87533 | 2025-09-20 03:34:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0078ef06-4e8a-3e0d-b2e1-a87c2e9b9a26 | -5.55284 | -42.1618 | 2025-09-20 03:34:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d62fbc81-5ae8-35a5-a951-b83c0046e233 | -5.73863 | -42.58319 | 2025-09-20 03:34:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1be6c4d4-27ec-3fbb-b3f5-faebe4f36a8e | -5.16029 | -45.42629 | 2025-09-20 03:34:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc09596f-d2a2-3160-a304-a854e7e6f845 | -5.04053 | -45.57624 | 2025-09-20 03:34:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2521a8fa-5933-3d35-9e1d-8de5226f7648 | -6.40048 | -44.29374 | 2025-09-20 03:34:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd17e0f6-2e10-3265-9f76-19f5924b09a8 | -5.54873 | -42.15469 | 2025-09-20 03:34:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 12171bb3-fdb0-3c27-b877-499d7c506d65 | -5.19059 | -45.48182 | 2025-09-20 03:34:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 11d9b516-1c72-368a-9be2-1fedcfa7fe8b | -4.07012 | -40.4768 | 2025-09-20 03:34:00 | NOAA-20 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dd6daee1-f912-365e-ba7f-362ec3006339 | -6.67805 | -43.58703 | 2025-09-20 03:34:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85690bf4-b853-3538-9824-eef429cbdf10 | -6.17734 | -45.42471 | 2025-09-20 03:34:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f3fb99e-7dcf-346e-b65a-21866ab098f9 | -5.78885 | -43.64208 | 2025-09-20 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5489fe3-5a5e-3a41-aa8a-11fd624e6327 | -5.55339 | -42.15867 | 2025-09-20 03:34:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| be96e4bf-4a8b-3d11-b077-8709db21388d | -5.78814 | -43.64595 | 2025-09-20 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e6006fa6-b2e0-3804-a573-13ed4692b6b7 | -5.29921 | -45.5845 | 2025-09-20 03:34:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d53e1a66-9ec2-3fc8-a9d7-3e591baae50c | -5.51714 | -43.8564 | 2025-09-20 03:34:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0caf12e9-dc06-38d8-a53b-dbc06a1dbaca | -4.86791 | -46.83661 | 2025-09-20 03:34:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d006df4d-f481-3369-8b1c-7d76a269124a | -5.96392 | -42.92179 | 2025-09-20 03:34:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b59edb28-c74a-3449-bfd9-b99e42c68551 | -5.54818 | -42.15781 | 2025-09-20 03:34:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 00b00da4-b482-3c57-9ca5-203638323c5d | -5.73477 | -43.63874 | 2025-09-20 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09c7d216-fffa-346a-97cd-9081a49b3453 | -5.5891 | -44.09361 | 2025-09-20 03:34:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bed2629e-062a-3121-a1f0-5a64fa13ec98 | -5.53254 | -43.87122 | 2025-09-20 03:34:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 38cf1741-e201-3fb1-9275-6796ed212e8b | -6.36572 | -43.46271 | 2025-09-20 03:34:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6057c0c-09b7-3c21-8ccb-12e7e8294954 | -6.48417 | -39.69146 | 2025-09-20 03:34:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7914422d-cd90-3bd8-9202-763c01a1654c | -4.91667 | -38.68225 | 2025-09-20 03:34:00 | NOAA-20 | QUIXADÁ | CEARÁ | Brasil | 2311306 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6aaac791-328a-3a3a-bd31-330f5326e10b | -3.65123 | -41.11703 | 2025-09-20 03:34:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2765b07d-b9f8-3900-885e-65df161b5683 | -7.1678 | -39.7683 | 2025-09-20 03:34:00 | NOAA-20 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 57657e9f-0a29-3e64-bbb7-e04f4e31cf20 | -5.78671 | -43.65387 | 2025-09-20 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d85eb167-e057-3861-95ee-d86976c59fa9 | -5.93081 | -45.08252 | 2025-09-20 03:34:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6d8e2ad-aeac-340f-88ad-65f63aab4a72 | -3.65622 | -41.11794 | 2025-09-20 03:34:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 655b3863-c84e-307e-a70f-a9100f63e9e0 | -5.19497 | -45.49456 | 2025-09-20 03:34:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9f8ff9f7-bd4d-3be1-af83-ee0204b82e19 | -5.30577 | -45.58528 | 2025-09-20 03:34:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f23caa8-8a02-322e-b096-28ac0d02011d | -6.90325 | -44.76911 | 2025-09-20 03:36:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 99f4dc05-098a-3f8c-85ee-474b22012ed7 | -11.47338 | -43.57308 | 2025-09-20 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cf008a9a-d0e8-3f72-8992-8778341ab0e0 | -11.26237 | -41.50338 | 2025-09-20 03:36:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bbb50c0a-d841-3d03-beb1-f65759fa3db0 | -6.95519 | -44.75718 | 2025-09-20 03:36:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4465bfb8-cf76-34e4-b328-fc4a01c0f5e0 | -6.91525 | -44.77158 | 2025-09-20 03:36:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84667f32-132f-37fd-8a84-324c9dce101d | -6.90213 | -44.76573 | 2025-09-20 03:36:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 209fad00-0f2f-3f6c-a41d-61d8769819a7 | -7.18515 | -42.24023 | 2025-09-20 03:36:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| bd10e88a-354a-35f4-86a5-7c7eda56ba32 | -6.9483 | -44.76091 | 2025-09-20 03:36:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8c5fccb-7870-3f7b-ad22-fb54524b26e5 | -12.44281 | -44.3093 | 2025-09-20 03:36:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b901bf5-f8dd-312d-84d7-cec5f0466c9b | -10.86983 | -47.79935 | 2025-09-20 03:36:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 58b587a9-bc1d-31e3-b4ee-469d4dabb405 | -11.42646 | -43.52999 | 2025-09-20 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f460d60-e814-35ab-a837-90cc798dbbf6 | -7.60623 | -45.4771 | 2025-09-20 03:36:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b8ff751-a970-3e77-840c-b522b5771c19 | -11.67122 | -44.88586 | 2025-09-20 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a0eda534-307b-38dd-8908-57066e2c004e | -11.765 | -44.8992 | 2025-09-20 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c18276c7-00df-3107-98aa-e4d52a1ef560 | -11.46823 | -43.57207 | 2025-09-20 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f616075-b35b-35b9-aa56-b140f39685b9 | -13.07226 | -42.14253 | 2025-09-20 03:36:00 | NOAA-20 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1b169f6f-7a8a-302d-91f4-5ecbe27d19ca | -10.27298 | -36.3358 | 2025-09-20 03:36:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 97a86d4b-f157-3a6e-9ca3-2661272323c6 | -11.50623 | -43.62601 | 2025-09-20 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b4698266-9f78-3f7d-a6ab-433add8b7ff3 | -7.44107 | -42.62373 | 2025-09-20 03:36:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 63404ada-6c16-3f69-a0e0-e068e32652ec | -11.47397 | -43.56998 | 2025-09-20 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0527d979-244c-30a1-a6e3-1ec1f70ecc67 | -11.75932 | -44.89857 | 2025-09-20 03:36:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb07affa-5401-3189-b2a9-d66778d625a6 | -7.3256 | -44.55952 | 2025-09-20 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74ca82f9-ba32-39a2-98cb-902d29f4c05a | -7.20295 | -44.44307 | 2025-09-20 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 937a88ee-1ead-35ca-ab69-c7752a1be8b1 | -7.19779 | -44.43814 | 2025-09-20 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0be2bf28-c8c8-305e-973c-bc28bd4690d5 | -11.67253 | -41.74371 | 2025-09-20 03:36:00 | NOAA-20 | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cde0e4c7-333a-3619-bef9-397617acb654 | -9.22748 | -43.31585 | 2025-09-20 03:36:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ecbcfed8-8cda-355f-8666-f822636ce2f8 | -7.60006 | -45.47569 | 2025-09-20 03:36:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9f2b85b8-0e3d-3608-b249-d1f2190bca0b | -11.08061 | -45.95717 | 2025-09-20 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a4cab32b-4b0e-39cd-b486-a22e969fb1f6 | -10.27579 | -36.34012 | 2025-09-20 03:36:00 | NOAA-20 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 33cd43cc-c0ff-3a73-9855-0bde2f416df8 | -13.07674 | -42.14384 | 2025-09-20 03:36:00 | NOAA-20 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 47c4764f-c836-31a9-8bf3-a6902d3ec6a3 | -11.08119 | -45.95915 | 2025-09-20 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8fcf9aa3-e384-3232-b044-b1ecf6713b35 | -13.07761 | -42.13906 | 2025-09-20 03:36:00 | NOAA-20 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 2fc6d15f-df65-38a0-a0e4-d27a107b1f65 | -9.49533 | -43.06737 | 2025-09-20 03:36:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1203f26a-62ad-3681-b991-74f5b48ba41e | -6.90739 | -44.77107 | 2025-09-20 03:36:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd412a3b-3523-361c-b79f-17a7c32cec2d | -11.33531 | -43.47687 | 2025-09-20 03:36:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 102347db-3fa1-331b-8ed8-9be68d8af58d | -9.28215 | -41.05033 | 2025-09-20 03:36:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a0676d02-109a-359c-aecf-09cea438ba80 | -10.8764 | -47.80162 | 2025-09-20 03:36:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fb95783-3c78-3d4e-86ce-73bded97d670 | -7.51239 | -43.67762 | 2025-09-20 03:36:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d5f255ee-035f-33d1-b2e5-ff8d6e4f3980 | -7.19697 | -44.44261 | 2025-09-20 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bbb2e46-13f1-3864-8364-5305dc38e3fd | -7.33221 | -44.55667 | 2025-09-20 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 355d1b3a-bfe2-3dc3-aab8-7db1d9234f5a | -7.19617 | -44.44696 | 2025-09-20 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95f730bd-abd0-30f1-b01b-57aedf5ec502 | -12.41048 | -40.9259 | 2025-09-20 03:36:00 | NOAA-20 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 488ea556-44db-3143-ba42-f224e6700343 | -7.18568 | -42.23724 | 2025-09-20 03:36:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 59572496-62f0-30b4-bb61-37e1be01f700 | -9.21344 | -40.24229 | 2025-09-20 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |


[Clique aqui para ver as próximas entradas](README8.md)
