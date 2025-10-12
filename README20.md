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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dcd98f0f-e7c9-3632-96e4-88b71a4c099f | -6.30339 | -44.74202 | 2025-10-12 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 315d36c3-2ce8-361d-b55f-42a8128d8c67 | -6.43418 | -43.37437 | 2025-10-12 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b4af59f-68e0-3a57-816e-f452b76eb84e | -3.8359 | -50.67307 | 2025-10-12 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4ec777eb-b235-3d91-9ecf-259d07788930 | -6.49543 | -42.44007 | 2025-10-12 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 53f605ee-6f7e-3029-8ef9-7b8acdaa07df | -5.42493 | -41.33464 | 2025-10-12 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0ea97d13-1121-3d2c-8cdb-1fecc3f31f18 | -7.1965 | -45.92049 | 2025-10-12 04:14:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f29978a-40ec-386a-816c-1599ea27a24b | -7.25076 | -44.09121 | 2025-10-12 04:14:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a7a7101-d4ef-3820-bdf1-81d4e707e04f | -5.16426 | -44.59651 | 2025-10-12 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a090644a-5b15-3121-a09f-4bee22c564b1 | -5.32315 | -45.247 | 2025-10-12 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a30b6692-4200-3a62-a828-a50ad2943fa0 | -7.33657 | -44.04393 | 2025-10-12 04:14:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c1594be2-abc4-3fdc-8ecf-43c0439edfe6 | -7.88353 | -44.45889 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20c95382-b584-39b3-8b95-8e7433712cec | -3.81851 | -51.05458 | 2025-10-12 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de63428f-a3ad-305b-ab4a-9d123feb1090 | -7.67913 | -42.5717 | 2025-10-12 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 55620d1b-e853-3d8d-8795-8e342e230da3 | -6.76932 | -42.82386 | 2025-10-12 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 26c2e0b6-81f3-3189-b227-8b10fd7538d3 | -7.01385 | -42.73847 | 2025-10-12 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 24f05bb8-a53b-30f3-8d1c-39af95d3a95c | -7.40101 | -46.94564 | 2025-10-12 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 206cc69d-4f4a-3838-bc08-9ec477282a09 | -8.10187 | -47.24572 | 2025-10-12 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e48cfb3f-3297-3843-a8e4-818bb20dd2f8 | -9.52974 | -47.86663 | 2025-10-12 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f5efaa3-d039-36ce-9e1b-85db5503eca2 | -5.31104 | -42.87511 | 2025-10-12 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e4457c1f-7dd5-3189-a9da-c388db6a2180 | -7.89478 | -47.07481 | 2025-10-12 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7009a80f-f297-3835-aa14-6de621d9db95 | -6.46867 | -44.63835 | 2025-10-12 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6b26ddd-9835-377d-b653-14c12539e71e | -8.70101 | -47.05912 | 2025-10-12 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e409c8a2-41d8-350d-bc89-c8f0855f19e6 | -6.26517 | -42.99804 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be8a4f9a-d851-3781-89a2-c25c68d3bd08 | -6.24627 | -42.92455 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6a58fcf-2914-3d4a-9869-825cd7a7159f | -9.75718 | -45.23709 | 2025-10-12 04:14:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 94b28fab-8f32-3366-838b-ff12af0ad684 | -7.79455 | -42.39529 | 2025-10-12 04:14:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 10a36a6e-0b6f-3918-bdc7-164ca1fbe34c | -7.867 | -44.87986 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e93819ac-eeec-3a36-92fa-1c70971ab319 | -11.75195 | -43.30689 | 2025-10-12 04:14:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e7468b4-b9a0-301c-9e25-81c6ac242f42 | -7.85954 | -44.52405 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ceb8ed83-1dfe-36ea-b89f-7a130741d96d | -6.26565 | -42.97342 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89d1d4b8-f8d3-3c99-97d6-1fcef075e148 | -6.58739 | -44.62019 | 2025-10-12 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd08bf91-9336-3553-9b14-a3d963a06437 | -6.75689 | -44.65133 | 2025-10-12 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 11767fbe-b143-358d-bd39-b9e175e89bc3 | -6.2587 | -46.01702 | 2025-10-12 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9d7a15f-64bf-328d-90b8-b185e27d99f5 | -6.16738 | -44.67247 | 2025-10-12 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3b7b206-42b1-3833-b2c4-d14f4645db21 | -8.02946 | -44.46102 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0941a9d9-28d6-3ed7-8cd8-3714589efe29 | -9.52597 | -47.86596 | 2025-10-12 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35db58ef-4236-394d-9d82-ea6a35d6349e | -7.93164 | -47.21163 | 2025-10-12 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a3a81bb-0977-3426-b5c8-17ce02f1ea59 | -4.67589 | -43.258 | 2025-10-12 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 83a00385-25af-3fb5-9011-d3726a9cbded | -7.37061 | -45.19007 | 2025-10-12 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d81bd93c-95e3-31ea-ad9c-c538885908e9 | -5.42605 | -41.34971 | 2025-10-12 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 739e66f0-e976-3e4d-a191-24982245d1dc | -5.84127 | -42.31276 | 2025-10-12 04:14:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 5dc61231-4a0e-3f43-87ab-b75f2e8420c0 | -5.61654 | -42.57826 | 2025-10-12 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4ae7b776-7015-3ad8-832d-7e60e9e94838 | -5.83959 | -42.30185 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 574af38d-6db5-347f-9412-b531097ae1f2 | -7.05394 | -46.72901 | 2025-10-12 04:14:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 110f458a-30ed-3ac9-a2e7-ebdea90c66c2 | -8.02053 | -44.47416 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 058250ee-40a1-320b-9236-49a9bcc22cd8 | -5.25593 | -46.15327 | 2025-10-12 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bb5f3037-a83e-37b0-a06d-c76665922334 | -5.37535 | -44.92167 | 2025-10-12 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 403d4d83-89f3-30e6-bad8-133da2cc4034 | -7.43565 | -42.9786 | 2025-10-12 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 8488806a-0028-315b-a01d-729de86d517a | -8.76697 | -47.29201 | 2025-10-12 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 69c7df75-b00d-3357-99a2-e64d03d92fcf | -7.81439 | -44.12099 | 2025-10-12 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7dc53119-7c39-3822-8f7c-6794d2d998bb | -5.77847 | -42.47679 | 2025-10-12 04:14:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e9ba7694-57e2-3e53-be32-a3fd4c022d05 | -7.14452 | -42.50949 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 07023574-5ef4-31f6-a033-539b6597a0a6 | -7.68245 | -42.57222 | 2025-10-12 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 58894bf1-06ef-3ed8-a239-7effe00f008f | -6.31564 | -44.25525 | 2025-10-12 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 247d2a05-7442-3db1-bc6a-269fc819fa32 | -6.33497 | -41.60601 | 2025-10-12 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b454e5ef-a235-3228-8663-274cd0da0ac6 | -6.5252 | -41.49105 | 2025-10-12 04:14:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dad6b8cb-a838-399a-8571-db367602fe2b | -7.74056 | -42.4159 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ae2552b9-79e2-3bbc-9d34-41fe902e82b6 | -8.70172 | -47.05486 | 2025-10-12 04:14:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92a2f299-f6df-39ca-bf75-dc526bd81f57 | -11.36241 | -44.00338 | 2025-10-12 04:14:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7e8c955-bd32-3701-bb39-1ba7062510dd | -6.64629 | -43.73787 | 2025-10-12 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce2e9d15-8684-3b99-af52-9099bbe77e36 | -4.42528 | -47.75586 | 2025-10-12 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c1bcd78-71a9-3e48-a2fd-51b0d60f38f3 | -5.60718 | -42.57328 | 2025-10-12 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3fca43fa-0a9c-3dc1-8082-69ecb730b2dd | -9.35248 | -46.88464 | 2025-10-12 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31796c34-9c0d-30b0-8f6d-1d44cc3e91e8 | -9.55968 | -43.0139 | 2025-10-12 04:14:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e9332069-7990-34d1-be3e-97368eaf3508 | -9.0604 | -40.24731 | 2025-10-12 04:14:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| d744dc7d-f961-3e4e-88be-40a6271410ac | -7.49 | -42.7598 | 2025-10-12 04:14:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 1ca6ac5f-1b6e-3fee-bf56-7bd9ea7789e4 | -7.18912 | -43.31412 | 2025-10-12 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a4e5b67c-918a-35b0-a04f-36fb6ef98784 | -5.83 | -44.03381 | 2025-10-12 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 82129c63-cefe-34a1-9261-63d8fb17fa89 | -8.48649 | -46.15931 | 2025-10-12 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9fe9493b-f471-38b4-9c5e-61ead946e570 | -8.21716 | -43.35794 | 2025-10-12 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fec55b3e-1ca2-3912-831e-ac66556a7281 | -5.47552 | -43.39169 | 2025-10-12 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cda7a9ee-f39d-336b-a062-a91da600c04a | -5.31548 | -42.88988 | 2025-10-12 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9dc4bdaf-aab1-3ab8-b9ad-fcc2efafe629 | -10.15278 | -44.55202 | 2025-10-12 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0f1bba66-d86d-34cd-9519-e1219dfb5c87 | -6.65454 | -43.7285 | 2025-10-12 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 77c70b90-6a08-3a9a-9c49-75a404682b65 | -5.62527 | -42.71713 | 2025-10-12 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0d9f9a99-c2d1-3ddb-84c4-b5b77081e533 | -5.06109 | -40.45743 | 2025-10-12 04:14:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 73fbc1db-fa48-3d21-8fd7-26ae91a80cb3 | -6.16626 | -42.54458 | 2025-10-12 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1753cc07-12c4-3611-bbc6-c624b732a945 | -10.18841 | -44.60818 | 2025-10-12 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 58993ba6-eec8-3c34-882d-02462f285d1d | -7.73308 | -46.66285 | 2025-10-12 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c5520030-d71a-3ba6-a07e-35576751bb25 | -9.52894 | -47.87127 | 2025-10-12 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5bed73b3-c29d-37c4-aa33-420bfed576e3 | -7.87184 | -44.48959 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e4b77efc-4a7e-35e7-830f-dd49b5714b62 | -6.65785 | -43.72903 | 2025-10-12 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fcba8efc-8791-338e-82d2-5594ca26b83f | -7.80687 | -42.42612 | 2025-10-12 04:14:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e0cdfea8-b0f8-3730-b623-c3ebe99fef75 | -5.65351 | -44.47968 | 2025-10-12 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a7e69f8-e735-375f-ba3a-745cdba574bd | -7.6922 | -42.37586 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f64c96ab-18b1-333f-a0d6-de461d213849 | -4.26958 | -46.92688 | 2025-10-12 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| b2e7e21a-45e6-3882-aeb9-b35967c0ab9d | -3.41219 | -52.18251 | 2025-10-12 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| fe19865e-e147-32eb-b6f4-1c2134c8f2f3 | -7.6255 | -47.50703 | 2025-10-12 04:14:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a4089cb-ab57-3667-abaa-8b171f7ee593 | -5.29392 | -42.53096 | 2025-10-12 04:14:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b760f571-e05b-32db-9d88-d1b5c8940a8c | -9.00888 | -47.35235 | 2025-10-12 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1781c4e4-35b4-3295-af12-f4544b81e7f1 | -7.50943 | -42.14814 | 2025-10-12 04:14:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 1fcdac0b-0dbc-3bb4-abef-4cf693c3b20c | -7.67475 | -42.40162 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d9cd9ef4-fe96-3076-a808-aa60226102cd | -7.01769 | -42.73552 | 2025-10-12 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c6ee6a87-e73f-37de-8ff7-4a32e11eb9df | -7.08632 | -43.51715 | 2025-10-12 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| deca3389-62a4-39c8-8267-8a166d7c2f2d | -7.29324 | -41.96534 | 2025-10-12 04:14:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a5851be8-2297-3cb7-9d0f-fbf5b857db96 | -4.61451 | -45.77274 | 2025-10-12 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a3baf81-7856-31f5-8040-b207e116fb14 | -5.34627 | -43.43502 | 2025-10-12 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 28936de4-49dc-3d69-ac23-bf814ddecb0c | -7.656 | -42.58959 | 2025-10-12 04:14:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2d97f22d-65b7-3872-95e7-183adaa5d870 | -6.27116 | -42.98134 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 084faff0-096f-3c55-8804-846a68055ead | -7.85678 | -44.51994 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README21.md)
