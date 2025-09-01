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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4b70515-467e-382d-8757-7b534c532aa4 | -11.01904 | -47.05234 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| df22de34-87a4-386f-b247-aa114ae9b645 | -6.29813 | -43.78982 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2bd1b174-7e47-332e-9755-170e7f11527c | -7.23634 | -45.4195 | 2025-09-01 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4a8f0291-4c9b-30b8-bedd-da154c5aba25 | -6.29249 | -43.82493 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ad9a150-725c-3b1a-ae14-4959bd207ff1 | -6.30427 | -43.64038 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 08410c2c-a12f-38ae-8241-170ea198a141 | -7.0034 | -44.3559 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97a6ad0c-7268-313e-aa10-8dcd2ae45598 | -6.34354 | -53.4292 | 2025-09-01 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 354c1577-4155-3df1-9c9e-9c7235a563f4 | -7.56061 | -45.69761 | 2025-09-01 04:10:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 777058a7-54af-3383-a33f-3372e6a9ea67 | -11.32682 | -47.36352 | 2025-09-01 04:10:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4838e7d5-e10b-3efb-8da2-4d8b95a4a410 | -6.16281 | -43.32795 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3be2cd92-4f3e-3005-ba48-044b8e60b918 | -9.27317 | -47.08629 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5dc3437-67bc-3dee-9ff6-1aaaba0df01e | -9.0148 | -50.12138 | 2025-09-01 04:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4464380c-5c1d-3d98-b06a-77b26b3d4a85 | -11.3743 | -43.60985 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28ea275a-ee2b-3560-886a-76f778d335db | -7.39527 | -47.44376 | 2025-09-01 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c8dba5f-ec4c-37ce-b893-8513eed28103 | -7.42312 | -44.08468 | 2025-09-01 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3adf4ba9-9d15-3b63-a157-e322f51cc082 | -7.55969 | -45.93924 | 2025-09-01 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 784b2b74-c547-3a5d-95ec-f023eff4e6f8 | -6.9645 | -42.00702 | 2025-09-01 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 65b30117-e331-3e89-8257-48962ceaf044 | -10.24344 | -51.10786 | 2025-09-01 04:10:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86060f19-3173-3985-957e-56b665b0f5f9 | -6.54139 | -44.57505 | 2025-09-01 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ce42fc0-1ba7-3190-b7db-834e4b900120 | -6.15653 | -43.32308 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1512cc04-3188-3b87-a2d7-d8e3ba6b7f3e | -10.23713 | -51.11309 | 2025-09-01 04:10:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2d0022b0-71c7-3a6a-8a30-0de928a54fdc | -6.31042 | -43.78287 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e46a3833-c437-30a4-920a-71061430ca3e | -11.25174 | -44.12807 | 2025-09-01 04:10:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 64bbc75a-7c92-3e1d-b83a-5eee7d582986 | -6.28402 | -43.28945 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 72b8bd4b-45bf-3306-b178-790e60276ea5 | -7.73318 | -50.25832 | 2025-09-01 04:10:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| babe2d07-cc88-397c-9411-5fab3c5882b3 | -6.0927 | -43.19461 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f0dcc370-ef75-3ef7-85ac-6c07301f814d | -6.23571 | -43.39277 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 379c7e80-322d-315a-8187-e4f3d4cc6459 | -12.09428 | -44.72435 | 2025-09-01 04:10:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 55c1b05e-7e0d-3fc7-b5c2-5b07e8fa5c99 | -6.96395 | -42.01051 | 2025-09-01 04:10:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3644a7e0-417d-30da-90df-f278a38411b2 | -8.29729 | -46.32204 | 2025-09-01 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 68d6f400-1cb2-3b35-8d0a-bbd358515bb7 | -6.82122 | -43.33248 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 774f9d2b-4112-3b0a-85fc-8830af60905a | -7.64743 | -44.77054 | 2025-09-01 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b24cfe81-76bc-31c1-9b29-16c930b85b0d | -7.07848 | -44.3435 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6881377e-6e49-35d9-b9b2-6778a8cee0b5 | -7.95714 | -46.34307 | 2025-09-01 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a18b23d1-0ff7-3b3f-b818-59e8d1eedc99 | -6.16722 | -43.33567 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79e40a3a-c5d4-33eb-b451-f733cecdf8fe | -6.86886 | -44.32365 | 2025-09-01 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 25b28236-e090-336a-8df1-e80b701d4149 | -6.2877 | -43.30539 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9db049a4-9190-3116-bb8f-df884f5bd13d | -7.63058 | -46.54317 | 2025-09-01 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8117daf8-3011-3a36-8035-a9347615c1a2 | -6.19573 | -43.99855 | 2025-09-01 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 345f954a-7958-30a6-b983-f9f3fce93250 | -6.50839 | -43.56316 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0fe200fd-f7af-39e2-8a87-5e16b0952c5e | -6.82233 | -52.83118 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 34e24460-b559-32af-b62c-d2dce1beee50 | -6.74995 | -43.78891 | 2025-09-01 04:10:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d178d440-b89a-3333-ba8e-a32309b477d5 | -11.37591 | -43.62118 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8400e3bf-77ef-3d95-9d68-e79bb7504912 | -11.07752 | -44.65632 | 2025-09-01 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 49f4243a-2422-310b-b22c-92a943f6987d | -7.37895 | -47.43698 | 2025-09-01 04:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 89c81760-3d64-3ba0-8633-acbe6e4f838f | -7.94605 | -46.45499 | 2025-09-01 04:10:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 056606fd-38f6-3a95-9fe1-16814aa1d3dc | -6.51309 | -43.55605 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce1825ae-a067-3b35-876a-3c7c9a2f7bc6 | -11.42681 | -46.91805 | 2025-09-01 04:10:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a1724693-be99-31f6-9112-68b91626a41c | -11.89642 | -46.69551 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c047ce3b-0784-35db-a2dc-39beb522c7e8 | -8.16188 | -42.30868 | 2025-09-01 04:10:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 286a3289-5e73-32ce-925d-feb91e405a1d | -11.03636 | -47.04528 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbf6212b-cf85-3733-bc74-468f1f14e899 | -6.74549 | -43.78928 | 2025-09-01 04:10:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7bcfcc01-14d5-3481-97f6-bb7d2aee2828 | -7.4548 | -44.80826 | 2025-09-01 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4825f67-28b3-31a8-b4bf-bf5bba46d2d6 | -11.89865 | -46.68796 | 2025-09-01 04:10:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0e21a1a6-e5c4-3fde-bf87-cf7d0c0473a2 | -6.36954 | -43.55301 | 2025-09-01 04:10:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49d5220e-9a6d-3f28-8b1d-6479076ffb31 | -6.08988 | -43.19037 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8239ab25-24cc-3635-92ca-19dbff14ebf1 | -6.20387 | -42.74431 | 2025-09-01 04:10:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ede3673c-22fc-3c65-8bea-df66071a25a7 | -11.95783 | -45.84531 | 2025-09-01 04:10:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0a8beb21-a84f-37c9-b11d-e2321d555b4a | -9.92432 | -51.62659 | 2025-09-01 04:10:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ed102ba-7da3-3a70-b219-c7fcce546de5 | -6.80657 | -52.81566 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ccf72c4-5f28-39f0-8e38-d4013f2ecd57 | -6.16425 | -44.12367 | 2025-09-01 04:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 34d555cc-75f7-363d-a977-2817081af008 | -5.31798 | -45.45177 | 2025-09-01 04:10:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e862872-bd2c-3165-841a-c95a773dc52f | -9.39063 | -48.01059 | 2025-09-01 04:10:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 712122de-4160-3ebc-a850-83b272950805 | -5.49542 | -43.19681 | 2025-09-01 04:10:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5842f447-f73d-3983-a035-4f3e2199dca0 | -7.72254 | -50.25884 | 2025-09-01 04:10:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef98c4fd-2528-3f20-9a89-1a72a50d0e56 | -6.53725 | -44.60011 | 2025-09-01 04:10:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9345e9fd-5e0a-33bb-8144-9090d5f5f27c | -8.82201 | -47.49079 | 2025-09-01 04:10:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dcbe2f49-3d45-34df-ad0c-55f348812e94 | -10.04617 | -46.02333 | 2025-09-01 04:10:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65b593af-bb91-3947-91a9-af299be3f5ab | -6.76835 | -44.82995 | 2025-09-01 04:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 94957c01-eb0c-3237-a7fa-c47c57aae37f | -7.29043 | -43.69849 | 2025-09-01 04:10:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e7886c2-93aa-3f0d-848a-8d9c04c84b09 | -11.01806 | -46.96514 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9b537bef-ac64-3432-8cc5-4abb5f9c562a | -10.84048 | -47.2705 | 2025-09-01 04:10:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47ea1682-c047-300e-8d19-759c7501a82a | -5.75268 | -43.68192 | 2025-09-01 04:10:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8b6cffd-7cd0-3e1d-941a-46fcdee149b4 | -7.08498 | -44.3397 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 7c872ac8-2ba2-30fc-9544-88ca3273ab5c | -6.28265 | -43.29313 | 2025-09-01 04:10:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 22558819-c715-3879-83af-0bf58d11429e | -6.46219 | -43.95871 | 2025-09-01 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 82c6e7f6-6cb6-3f5c-b2f8-c8971e466fb8 | -6.2928 | -43.6231 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf6bf286-de01-30ea-a263-c51d0c7a405f | -6.16966 | -43.32071 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84924967-bf25-3772-b0e4-6cc771a771c6 | -6.54115 | -42.96855 | 2025-09-01 04:10:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 501aa60f-bab7-3bdc-8b7b-cb2825e34403 | -11.37222 | -43.58004 | 2025-09-01 04:10:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87e46d5c-a6dd-3853-9b12-f20618813da9 | -6.20065 | -45.3713 | 2025-09-01 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f3a8d7a-f10a-3275-ac00-638cd6a26cc3 | -11.57198 | -44.65129 | 2025-09-01 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f262820f-a461-3194-a90e-3fce12415c4c | -7.09274 | -44.33692 | 2025-09-01 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 75ac64be-6d43-33e2-92b7-aabdc063c4e8 | -9.63954 | -47.81749 | 2025-09-01 04:10:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91703339-60cd-3ef0-a617-40c7eb806bf3 | -7.53695 | -45.03308 | 2025-09-01 04:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ab8689c-4ea0-38e8-9ea8-ff74611240ce | -7.45842 | -44.80887 | 2025-09-01 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f31b2ed8-c814-3284-aa3f-f07e97a4cc15 | -11.33078 | -47.36427 | 2025-09-01 04:10:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5aa2424f-dfc7-3181-9345-e11cd596b320 | -10.04381 | -48.10241 | 2025-09-01 04:10:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 194fd48e-5077-3015-ba32-3d58114dadcc | -9.64854 | -46.62896 | 2025-09-01 04:10:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| beb434b9-f420-3e4d-9332-8e56d1ae8ba4 | -10.24651 | -51.12197 | 2025-09-01 04:10:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01a5f243-ed5c-368e-b5b0-0099d45add4e | -6.4504 | -45.60699 | 2025-09-01 04:10:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72761454-f476-3fa9-9e93-3b3b0bd0eb5a | -6.83955 | -43.32782 | 2025-09-01 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 89bace37-4431-3f59-9b83-2565907917d9 | -6.30488 | -43.63656 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 52bf03d3-8a9e-3744-a13d-3e17b1e23f81 | -10.23284 | -51.10928 | 2025-09-01 04:10:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6e6d7faa-6f52-38be-a72f-ac6cd0b00899 | -6.30897 | -43.63331 | 2025-09-01 04:10:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 920e2164-feb6-3d4c-8703-9d1d9ac47668 | -6.44871 | -43.95284 | 2025-09-01 04:10:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79cb6e22-8ac5-3aad-85d1-aedbf7d639f9 | -6.32982 | -53.43189 | 2025-09-01 04:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0de7756b-cb1d-3ce3-90a4-d30cdb5dacef | -6.15413 | -43.33806 | 2025-09-01 04:10:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d67245f0-50d0-3931-8c2e-421a3b89b960 | -6.57769 | -43.71428 | 2025-09-01 04:10:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 320136fa-bd4f-3f70-babb-d42ff3f7d2ba | -7.8759 | -45.173 | 2025-09-01 04:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README35.md)
