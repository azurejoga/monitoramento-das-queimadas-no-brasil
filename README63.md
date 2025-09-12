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
| f6083145-2863-360c-960e-e94f0684ef98 | -10.41419 | -50.59172 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d35ef07-e569-304b-8943-bf91ac16eec0 | -9.74007 | -45.42132 | 2025-09-12 04:25:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12d87163-d6cc-30b1-b32d-6f8098926ebc | -10.66985 | -48.64296 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 169a3555-a376-34c2-90d0-96dba715851f | -10.41713 | -50.5966 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e83a1de-64aa-3f76-8e4b-cd4ec52107e0 | -8.43336 | -47.253 | 2025-09-12 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3323ba1-87eb-3a0d-8fe3-d739a8d8e68a | -10.7453 | -46.08126 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0947d0f-4be0-3db2-84e6-8a6f7a19b2a5 | -8.18876 | -42.41561 | 2025-09-12 04:25:00 | NOAA-20 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 72f92541-3f4b-3b08-b136-59f2e7e6df24 | -9.5686 | -47.99259 | 2025-09-12 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d88f212-3a24-316f-ae2f-4084172c7b19 | -11.08734 | -51.98037 | 2025-09-12 04:25:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3c3019a4-fc1a-325c-8423-a7aa641a7a7a | -8.64691 | -45.71889 | 2025-09-12 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1b180d02-d484-3dd7-b64e-265eb4eb0e14 | -10.59676 | -49.64177 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33ed239e-5b63-3ee4-9b4c-046e80da5308 | -6.83252 | -52.79681 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e42db20b-1db8-3679-853f-ebfadb464425 | -9.78408 | -47.85628 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3214ee2a-f15e-37b3-a5cc-a79732b602f9 | -8.54451 | -45.58948 | 2025-09-12 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9bdcd29f-9fbc-39ec-9432-07855aa32e6d | -6.83296 | -47.87636 | 2025-09-12 04:25:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ccfdc7c8-b947-3104-9a61-7ea311c071f2 | -7.22201 | -55.0572 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3b1e081-3a5e-30f3-8b15-47a84499c9eb | -11.99946 | -47.76914 | 2025-09-12 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b32836ae-5e76-35b5-94c9-9a87926ab484 | -10.40822 | -50.01294 | 2025-09-12 04:25:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 568666d0-fc00-32c2-90a4-20b113a15766 | -9.14106 | -58.91678 | 2025-09-12 04:25:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9501c473-f68d-3a78-853a-04df5a194ae8 | -7.41001 | -50.64529 | 2025-09-12 04:25:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 23032c92-3adb-33a5-ad3e-8885c573d08c | -8.64412 | -45.71477 | 2025-09-12 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 55f81863-17e7-310b-9c15-4169c08e57d4 | -10.84923 | -48.16422 | 2025-09-12 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5b4d06b1-6f4a-399f-8e8c-29cf4ef0fc95 | -11.15483 | -45.29907 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36c312cf-6ab9-3318-8621-775db9874147 | -9.91281 | -51.62394 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 24326590-2531-38a1-afcd-d8faeaccf2f9 | -11.43956 | -49.30021 | 2025-09-12 04:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17611f62-5f28-3834-a479-a7c185c8d599 | -7.32742 | -44.3717 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 6743f138-fcf6-3889-a080-e563643d5303 | -5.58453 | -45.46085 | 2025-09-12 04:25:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 757f02dd-37c9-3bf2-a745-3a5ca909db3b | -11.67933 | -46.60441 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 63fa58a8-dbcb-3989-9665-8cfac13524e5 | -8.64358 | -45.71832 | 2025-09-12 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 92a36c1a-61c2-31cb-ba65-06bbf4e2a346 | -9.68339 | -46.77826 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88b5d0ee-cf69-35d3-a385-ddb09f9ea780 | -6.6802 | -42.44851 | 2025-09-12 04:25:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| cd6305ee-fc7d-32aa-8506-885022d9aef9 | -7.38277 | -44.83184 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f97eb2f8-6c4a-37f0-b462-d02d224b24b4 | -10.34921 | -50.53217 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 8bde8c18-a2b1-3f73-a5a7-eda6936c7326 | -8.4328 | -47.25649 | 2025-09-12 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 424b3089-bef8-3402-89af-41127a13fd7d | -11.67485 | -46.56714 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4c32b9c5-ec45-3a27-bf62-7820062f0357 | -8.8964 | -49.94039 | 2025-09-12 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| ba3be6a1-911f-3eff-87ee-44ae37c7f422 | -10.38865 | -48.57908 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d2c17f8-211c-3b72-aa19-10372a13c76d | -12.08191 | -47.59145 | 2025-09-12 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9fe2d1f-0b51-3280-92c6-a97e8c868e06 | -8.73645 | -47.11895 | 2025-09-12 04:25:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e9f658dc-3aba-3555-b1f6-a642b5720e88 | -9.04719 | -45.80631 | 2025-09-12 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be1e11f6-4f9e-3418-a743-17715a118606 | -6.8375 | -47.86959 | 2025-09-12 04:25:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6b4c0006-c326-3335-bb6e-ab920739e0de | -9.78245 | -47.84516 | 2025-09-12 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e0fcb23-4e46-32bf-b75b-111d45ca4afc | -11.66045 | -46.59404 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71e5b6d1-78e9-36f9-9b58-102ca7779bfa | -6.68918 | -44.12598 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 903a006f-9000-340e-b082-27dcb35ecf1b | -8.60503 | -54.69989 | 2025-09-12 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| af23a524-5d9e-3e64-88b5-0771df4d07d6 | -12.54101 | -44.68592 | 2025-09-12 04:25:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d7efafd-c2c5-3e95-9d15-c56693d0afdb | -12.13605 | -44.83319 | 2025-09-12 04:25:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ab99a2d-f06c-3339-86e9-21f4a25c95e7 | -7.44317 | -44.43885 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8072dc98-a20e-39f5-86ce-0b99543a2691 | -4.55962 | -46.63909 | 2025-09-12 04:25:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1bfc6f3-aeee-3090-ae59-6883347e3e7d | -10.41124 | -50.58689 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5a32b31-f0f4-33d7-8633-1d7f2e8506c1 | -8.43941 | -46.89339 | 2025-09-12 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0a631854-d14f-37dc-b147-76f15efd2791 | -10.41301 | -50.59883 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f1cc2174-c22c-3a10-a4b7-91d2b438fd96 | -9.83668 | -54.53549 | 2025-09-12 04:25:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 46d88d04-b25e-3226-8d80-4596b0c830be | -11.14971 | -45.24014 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa666b32-f8b0-317d-9a8a-2db35a7f3155 | -9.08147 | -47.04279 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8115c9a2-5561-37c5-94d5-6d1db8dbf9d2 | -11.52097 | -50.3838 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6efd888a-13e8-397f-98fe-a2aced4ee262 | -8.08544 | -42.56693 | 2025-09-12 04:25:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8992c738-db53-3bb9-b598-c6b49a36856c | -9.84666 | -43.54327 | 2025-09-12 04:25:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40bb2187-7d75-38d7-90db-204fca9867ed | -10.38806 | -48.58274 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| cfd8a084-ff29-3d1c-ae04-91e773795be1 | -6.41329 | -42.60485 | 2025-09-12 04:25:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| f49fbd1c-3d54-3620-a696-128e43616999 | -7.41995 | -50.65603 | 2025-09-12 04:25:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aa45960a-2d2a-39a0-8176-31b6fb545eca | -7.44318 | -44.41575 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a72cff15-8e73-3b10-ae1c-116a1cbc0135 | -6.54884 | -42.44949 | 2025-09-12 04:25:00 | NOAA-20 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3a927aa0-d2f5-30f2-874d-507d0a54cbc9 | -9.08086 | -46.96067 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce0c40d4-d03b-3a36-a49b-4bcd093f136f | -10.13126 | -47.91647 | 2025-09-12 04:25:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c879af38-75d3-3860-85a4-b96750598a3d | -6.56154 | -43.95966 | 2025-09-12 04:25:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d689e2dd-f9c5-33ff-abae-eafdd4725974 | -11.14623 | -45.30933 | 2025-09-12 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b838b93b-ed1e-329d-85a9-e3e8ef8a4282 | -11.68988 | -46.60247 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c9d2f3c-1764-3ca9-806d-7061d89401f1 | -9.72058 | -46.88817 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2ea2cd0-c075-32e9-afb2-b603584f9b41 | -4.53355 | -55.68344 | 2025-09-12 04:25:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5b5a4da-811c-3668-8c15-4ad8d48fcfeb | -9.03679 | -47.08918 | 2025-09-12 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 48ce92ca-7b2c-385b-977b-6ea54220fc74 | -11.86151 | -46.76435 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85c87cdd-0c59-3dec-bd35-44070277b676 | -8.45154 | -46.90247 | 2025-09-12 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b16bd379-940f-3e8d-b7bb-ea978e972420 | -11.73855 | -46.52613 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 06d7e7cb-60b0-3713-b5c5-31950a648e39 | -9.07165 | -50.50352 | 2025-09-12 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 224c96cb-5b8d-31a9-9ec3-b68caa5e66c5 | -11.67372 | -46.55236 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| aaeeadf5-4b3d-316b-bdd6-843ff530492e | -6.96295 | -44.82818 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e107434-a4a8-30fa-9372-d04d536f5625 | -11.99469 | -47.56258 | 2025-09-12 04:25:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d2edc57-ac6f-3970-b4a2-bf4d47a8ac07 | -4.92821 | -55.78915 | 2025-09-12 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 38cafaae-4813-3786-8f88-638d4d1cc3c5 | -11.68435 | -46.61611 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b96e2324-a5de-3f77-ade6-363dc4ab5213 | -7.80894 | -55.22364 | 2025-09-12 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3b8aa93-83b5-3a3f-a749-5a3352cd2b70 | -4.92457 | -55.77697 | 2025-09-12 04:25:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87009c04-4012-3b2a-a14d-fbbd5cf057fc | -12.18869 | -40.88806 | 2025-09-12 04:25:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 44440a49-0f3d-3ce4-b3ec-7dcf352e033b | -7.44602 | -44.44323 | 2025-09-12 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7293e0d3-123b-37d8-be34-15c3d7cde953 | -9.99997 | -51.72488 | 2025-09-12 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7bcf273e-802b-3dd1-b308-8ad091d4bce3 | -7.4472 | -44.98388 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71abe867-4e0f-39cb-ba79-3626a04f7b33 | -10.08344 | -50.39504 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e9d3e112-67ed-3b60-9212-f5dfae882471 | -8.19302 | -46.10606 | 2025-09-12 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6724fe8b-ee98-3a75-83f8-e1b8d66e4a61 | -11.50453 | -50.37248 | 2025-09-12 04:25:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c590131c-7fc9-3832-ba77-72a61c5a69de | -9.00844 | -46.12268 | 2025-09-12 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 780d1a4b-91ea-391f-ab96-2e4411fd9041 | -11.19491 | -37.23026 | 2025-09-12 04:25:00 | NOAA-20 | ITAPORANGA D'AJUDA | SERGIPE | Brasil | 2803203 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4fa9cfdc-dc33-326d-8601-966f097dd19f | -8.42119 | -47.26536 | 2025-09-12 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7df2249f-e8d6-3290-9bd4-ac8e121c71ea | -6.8306 | -45.6561 | 2025-09-12 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ddb2bc0-0001-30ab-991f-b8a213e01a46 | -10.65121 | -48.65121 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1adef34e-61ae-3ddc-8e44-1ca9de815990 | -10.41809 | -50.61299 | 2025-09-12 04:25:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71bb3cef-4290-38f0-a319-9e39a97ac23a | -10.65517 | -48.64814 | 2025-09-12 04:25:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c8bc8c92-ce3c-3161-b878-12df98a8d94d | -6.97311 | -44.78502 | 2025-09-12 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ef99ecc4-b662-3d10-b0b3-2c8b11793c4f | -10.35746 | -57.4904 | 2025-09-12 04:25:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5f2b5b28-5e51-32bd-ab8f-d061c7e66541 | -11.18857 | -48.35887 | 2025-09-12 04:25:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 67ca8580-5659-34f9-9804-52b16936201b | -11.69152 | -46.56982 | 2025-09-12 04:25:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README64.md)
