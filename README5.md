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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37c92fe3-8f3b-3346-b946-35021835e231 | -10.1902 | -49.10623 | 2026-05-30 04:36:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11f20645-3362-3009-86c7-8d575afd0183 | -10.76481 | -46.96634 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| f68ed0db-e60e-30c4-845c-11fbb75beee9 | -6.99654 | -42.88351 | 2026-05-30 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| ef952a7f-d125-3a82-8931-c0e26de29956 | -10.7641 | -46.9339 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca360ce9-87d0-3ebf-8a8d-7674c4f62c75 | -10.77088 | -46.92749 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b2ba80e-537a-3048-abe2-27263b9e2b79 | -8.03218 | -46.58557 | 2026-05-30 04:36:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b82cc2ac-c156-33e6-94dd-0097f42f8a75 | -10.57387 | -48.02595 | 2026-05-30 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ddb34306-274b-3022-bff1-1f61708387cf | -8.8442 | -46.71481 | 2026-05-30 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c4e1e938-c185-325d-84b0-c4b62ca3cc03 | -10.76202 | -46.96227 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 26f3e8f3-fa94-3021-95a8-385122a18f72 | -8.72863 | -48.31958 | 2026-05-30 04:36:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ffb292e8-fba9-364f-9fc2-3bfe1382309e | -6.75282 | -45.01259 | 2026-05-30 04:36:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3782988f-ffab-34a6-b991-5af44c94eff5 | -6.75622 | -45.01313 | 2026-05-30 04:36:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f71e0bfb-2e99-3dcf-aa74-922a5c14aa71 | -6.23668 | -48.45763 | 2026-05-30 04:36:00 | NPP-375D | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 965b04d8-e064-3090-ab47-d6ae4f9ce04a | -5.29328 | -43.95794 | 2026-05-30 04:36:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 46a5bbb4-e374-380f-b139-0d468cb6db6b | -7.84094 | -46.25827 | 2026-05-30 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36e266ed-36a1-3ba7-a3ba-fd5c3ba2afd9 | -10.76244 | -46.9445 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d826cd4d-c25d-30c3-ba8e-3d3486816f56 | -7.50527 | -55.00566 | 2026-05-30 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5e636bca-b99a-39a7-8928-44193af10962 | -7.71405 | -44.56535 | 2026-05-30 04:36:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04b77aa2-431e-3b13-9ce3-295931dfcd0a | -8.72525 | -48.31903 | 2026-05-30 04:36:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| afff4462-44cf-304d-8554-a79c011b2b95 | -7.84667 | -46.25912 | 2026-05-30 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94c79add-faaf-371b-92b7-0ce0683bed61 | -7.3393 | -49.85996 | 2026-05-30 04:36:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 749a9396-1311-35d5-b76e-53198fd10aca | -5.92435 | -43.48081 | 2026-05-30 04:36:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 78a9b3b5-67fb-3e7c-98eb-56cce18919f5 | -7.43495 | -43.2561 | 2026-05-30 04:36:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d5a9981-6d65-310c-998b-c794666c5e7c | -5.28572 | -43.9607 | 2026-05-30 04:36:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| da8e4cca-d3d2-3bfb-918f-588221acbc9f | -10.77198 | -46.92044 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 43a3139f-221e-3c60-988f-1f23a06469f5 | -10.76867 | -46.94162 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ec9dace-01ac-3f30-b2b8-f801a21610fe | -8.84087 | -46.71428 | 2026-05-30 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c61fcd9-5985-3cbc-aa65-8ca0fff61920 | -9.44681 | -51.82667 | 2026-05-30 04:36:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ca632a7-8e7d-3438-8a5b-960fee74d3c6 | -9.83319 | -39.43148 | 2026-05-30 04:36:00 | NPP-375D | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c31ab23d-9e07-3a25-a7df-9db4dd19c8da | -7.33704 | -49.85102 | 2026-05-30 04:36:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0f6542e-f93d-3b17-b648-02409eaab64d | -8.38164 | -46.88092 | 2026-05-30 04:36:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf014169-c5c1-3775-8f45-1b47331847f6 | -8.72535 | -47.8423 | 2026-05-30 04:36:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 033cc5a0-8c23-3f09-a7cb-0377313ed413 | -9.39798 | -48.45447 | 2026-05-30 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff91ad07-befb-3f28-8513-8707c784c3cd | -10.76147 | -46.9658 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| ac4bdc98-4584-3bb2-ac39-bc05dc69e59f | -7.84278 | -46.2621 | 2026-05-30 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9cf70b42-65f0-3102-8347-f4c8c85ea937 | -8.722 | -47.84175 | 2026-05-30 04:36:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b99a2b40-9688-3706-9499-f2db98c04721 | -10.76188 | -46.94803 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3fbb9d4a-c86c-307c-827a-c2e160620131 | -6.75679 | -45.00947 | 2026-05-30 04:36:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4a87153-a791-3b36-86ec-adfac6c5dc1c | -9.21428 | -48.59917 | 2026-05-30 04:36:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87d9ff12-94a0-362f-8f99-b805b0567575 | -10.50741 | -48.09857 | 2026-05-30 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 29402cd9-ea9a-3ad0-8bb4-531a0124f373 | -10.76299 | -46.94097 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be7548e2-8300-3624-b4b7-6b58a8dd1346 | -10.76757 | -46.94869 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b98a3a87-a3d1-3f6f-b6e0-921b0e47dae8 | -7.50423 | -55.01147 | 2026-05-30 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 135ffe40-4c0b-3140-8021-2b5b59d91c8f | -9.9296 | -48.68974 | 2026-05-30 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 28ea58b3-de04-39d9-b4fe-4ec8dbf3226f | -8.72257 | -47.83822 | 2026-05-30 04:36:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7bffc176-332c-3fce-8429-7ab5d4cc3b8e | -9.17514 | -48.62294 | 2026-05-30 04:36:00 | NPP-375D | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 73cede9d-d51b-3562-a4a7-cb7ccc833a92 | -10.77253 | -46.91691 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9847f077-0d93-34c1-b5eb-71317ea7aaa8 | -8.72592 | -47.83876 | 2026-05-30 04:36:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b8a4c01-dac3-3fba-9669-1eee9d1fec15 | -9.92622 | -48.68919 | 2026-05-30 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6cf7daa9-ce4a-33ee-9e09-7713f80aee4e | -10.14279 | -48.07911 | 2026-05-30 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8af35807-43f1-3a1b-8275-6972d535f4fd | -7.84333 | -46.2586 | 2026-05-30 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e1b49c5-5546-3605-ab4c-1bae4dc85fc0 | -8.0222 | -46.58398 | 2026-05-30 04:36:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17b0cfed-ac42-31a5-86c7-f4c65a8e92bb | -6.53127 | -43.67849 | 2026-05-30 04:36:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84d0a4f7-834f-31c1-aaf0-3a56e8c876b2 | -9.93019 | -48.6861 | 2026-05-30 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6cca89cb-25f2-3df3-9a62-d84d5365c9da | -10.76037 | -46.97286 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e48f6b42-5b05-397d-bd89-043408736762 | -9.17794 | -48.62714 | 2026-05-30 04:36:00 | NPP-375D | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db0288a7-78f9-3659-bf06-5a19ac2347f4 | -9.36552 | -48.41948 | 2026-05-30 04:36:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d79aab8f-44c4-3be2-bd74-4699b26f4c0f | -10.50407 | -48.09801 | 2026-05-30 04:36:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 98d0ef67-fe3e-32fd-95f3-877ef35d76fd | -10.76589 | -46.93755 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc7e341a-326a-38f1-8710-01e012b85ed7 | -10.76092 | -46.96933 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 9754b610-7e96-335b-96ff-d055d5470531 | -9.80047 | -48.92481 | 2026-05-30 04:36:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4173dc40-2801-3fb7-a278-cc3ab29989fd | -8.03273 | -46.58208 | 2026-05-30 04:36:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d83277c7-a487-3d5e-91dd-6516c87b5e60 | -10.77035 | -46.95275 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc1c7f05-7254-3409-9147-cbca4a022a10 | -9.86167 | -48.24542 | 2026-05-30 04:36:00 | NPP-375D | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 897cb902-d677-3753-942e-0549b4c66622 | -10.76646 | -46.95575 | 2026-05-30 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cfe75f20-267c-34b4-bc74-6d9004afb029 | -12.0068 | -45.35574 | 2026-05-30 04:38:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ac9f884-ca87-3151-b13e-ba1c0ad4f752 | -11.58862 | -47.4496 | 2026-05-30 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 67e590bf-de65-3bf7-bc90-14bdbcc0094a | -10.99008 | -49.04273 | 2026-05-30 04:38:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18368612-25d9-30a0-8405-faba59e8e92f | -10.81702 | -46.89497 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 592f2fd0-e159-3c1d-95ac-5f33b6db36a2 | -11.75893 | -47.07384 | 2026-05-30 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d6c98ab1-3ce0-3673-8831-b8b53f89509e | -11.59584 | -47.44715 | 2026-05-30 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2383606a-d18e-3cb5-bac4-e7352926c75c | -10.84096 | -46.91694 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ddf85f6e-cbb0-37a4-8194-ae2d4d025b5d | -14.13311 | -58.93151 | 2026-05-30 04:38:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5343d65b-63f2-374a-aee5-1dc887462c6d | -10.84375 | -46.92101 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 87ec7b76-45bc-334a-b640-e1c4f77da581 | -11.59362 | -47.43955 | 2026-05-30 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2fe8bc5-0914-3bb1-8ce0-43f10afa3f26 | -10.8432 | -46.94632 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 8e71d1f4-bfb9-309e-af47-ef71f01bb479 | -11.58974 | -47.44254 | 2026-05-30 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b88e13b-3191-3267-9568-2df5e7fb80d4 | -11.46897 | -57.10705 | 2026-05-30 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dbb0dc53-9a2d-397a-b7f1-8a62f65d7915 | -15.82534 | -58.6197 | 2026-05-30 04:38:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 70e3a2d6-032d-3245-bdfc-e96dc5845841 | -14.1314 | -58.93998 | 2026-05-30 04:38:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 780b9fd7-336b-3979-bbdb-c473a560260a | -10.80149 | -46.9505 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a167581-deb7-3401-aea8-ee3a90cab74b | -10.80094 | -46.95403 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7909c0d4-140c-3d60-9fce-ce1c53a97880 | -10.84265 | -46.94984 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 18cb9eda-28fd-357a-9da9-fc9247d6b99b | -11.58918 | -47.44607 | 2026-05-30 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4149e9ef-c8a0-3fc4-9ab2-167f0194846e | -11.5964 | -47.44362 | 2026-05-30 04:38:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c54a925-f756-3ac4-94e1-bc00b49760cb | -10.76816 | -46.98859 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 215d4367-8ff0-34dc-93fd-d8a058fce52a | -10.78478 | -46.92607 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03daaebd-d6a4-3d2e-a5dc-7de4d8911329 | -14.13173 | -58.93599 | 2026-05-30 04:38:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d68bd49-ba11-38a1-9977-514f990bf1ba | -15.82212 | -58.60739 | 2026-05-30 04:38:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 6d78522b-91d5-39fd-9dca-4128c51b54ca | -11.76394 | -47.0637 | 2026-05-30 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0a620331-440b-3a47-afa7-d553dc0aeaf4 | -10.7815 | -48.5428 | 2026-05-30 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc99fdd8-d0f2-34c5-9346-0ddae38a7ded | -14.12912 | -58.94843 | 2026-05-30 04:38:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| efcc2257-cd17-37b3-a5c7-20e1dfd64c0f | -15.82609 | -58.61598 | 2026-05-30 04:38:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 984a3306-9acd-3fff-b26a-9a0c09f601c1 | -14.71011 | -43.20965 | 2026-05-30 04:38:00 | NPP-375D | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a2a6d57e-6f1a-3ba2-b637-833fd93e9fc9 | -10.77371 | -46.97501 | 2026-05-30 04:38:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ee7a711-9c8c-336b-a3e9-af193e100137 | -11.76728 | -47.06424 | 2026-05-30 04:38:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f49b583b-fbae-3626-8c86-da84580dae30 | -11.6307 | -56.87044 | 2026-05-30 04:38:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 833ab68c-268a-314e-89c7-f881de06acd6 | -15.78823 | -58.66141 | 2026-05-30 04:38:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e092c3a6-e14c-30d0-9ae5-0cd651f3689d | -11.69934 | -44.16361 | 2026-05-30 04:38:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 255d27d2-2e6e-3586-b707-3905b5fcdec2 | -11.9088 | -43.83641 | 2026-05-30 04:38:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README6.md)
