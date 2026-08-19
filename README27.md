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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0430ec7-45e7-32c5-83ad-467b7ac0a8dc | -12.5148 | -47.86042 | 2026-08-19 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae7d7194-cd35-3a5e-b5f0-dd748b98d2a0 | -8.10405 | -51.66 | 2026-08-19 04:19:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 427a339f-31c9-3ae1-9f35-44064221df28 | -11.63446 | -54.5302 | 2026-08-19 04:19:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3d4ee000-2764-39e5-8c66-c49196a07a18 | -13.69247 | -41.6471 | 2026-08-19 04:19:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| cfca605d-803a-3e8e-9293-2331b88bade2 | -7.29045 | -44.08139 | 2026-08-19 04:19:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68c910be-9923-3d7e-a811-595157120d67 | -10.81716 | -50.30113 | 2026-08-19 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ebce85c-0ed6-36e2-8f67-e1ef887db146 | -8.55152 | -54.72935 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f9540e53-2c68-3de2-9725-8682947a7742 | -7.29393 | -44.08195 | 2026-08-19 04:19:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63bd175a-6112-31ed-a058-ef48f8836007 | -7.45074 | -45.14407 | 2026-08-19 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d5097e35-7acc-36d5-ac8f-9c839c9bdbbc | -12.75621 | -48.44859 | 2026-08-19 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea23f550-d2b0-3018-8cc3-6b6bbbaadf91 | -11.23182 | -55.07219 | 2026-08-19 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9c830ea8-7d05-3207-88cf-5ad595755937 | -9.08159 | -50.80589 | 2026-08-19 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1846636f-7e7b-36b9-a9a0-72e12ec13e48 | -12.18925 | -45.15667 | 2026-08-19 04:19:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba12489e-115f-3b8a-aed3-d0a371fa28e8 | -9.03574 | -45.84692 | 2026-08-19 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3ba00464-d7b5-34b6-91c6-a94d72f5dd42 | -12.84001 | -48.41966 | 2026-08-19 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1be97bfe-29ed-31f5-a9f9-cacd0daae61e | -6.39668 | -51.74829 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8e301eb-711c-3316-a4eb-d9e6f8e4aecf | -2.9089 | -40.46203 | 2026-08-19 04:19:00 | NPP-375D | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3f6dfeaf-0762-3f3d-8237-526993774acf | -6.83731 | -44.94639 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e50fb688-c451-3b04-b8f8-f3063d987452 | -9.50814 | -51.63883 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 24d45727-b3cf-3720-b56a-481b355fd1f4 | -8.10342 | -51.66348 | 2026-08-19 04:19:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3d8dfda3-3913-3b50-9bbd-34469b6dcd5c | -12.51177 | -47.85448 | 2026-08-19 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69367672-96ef-3251-9370-fc6f34ccef39 | -8.535 | -54.744 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 311bf088-5712-3f68-b2b1-99a15d912c9c | -9.72974 | -46.78099 | 2026-08-19 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3dcf491b-16f4-3bd8-8486-7f08fd38ff2e | -11.22538 | -55.07095 | 2026-08-19 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 288a7c21-e3ea-3ed2-bf23-07caa73e8ec0 | -9.11446 | -46.04159 | 2026-08-19 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce0795ba-9973-3142-aa07-ac357df4dbc8 | -12.80595 | -48.44478 | 2026-08-19 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09926a6f-792d-32cb-89da-be785c0b6d16 | -11.31593 | -45.21217 | 2026-08-19 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 276313bb-086d-3ec0-abf1-25850a487931 | -9.73474 | -46.83982 | 2026-08-19 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4baf997a-afe4-3862-9c12-0f25cbd802ee | -9.08829 | -50.79804 | 2026-08-19 04:19:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a8d80dd7-f38c-3d8d-8ae9-27318935d5b9 | -8.57986 | -54.68861 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8d44cb29-c473-3fbe-aafa-611e2210ca3e | -8.56464 | -54.76752 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f657e851-9b3c-3b0d-af84-6e4f596e6f19 | -13.44289 | -43.84304 | 2026-08-19 04:19:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0facba49-f0e2-379a-96e8-e191cc519b3a | -6.39098 | -51.74738 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb69c2db-88dc-3b71-952a-c33937638e4f | -7.94386 | -44.63205 | 2026-08-19 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6c8814b-12ad-3a09-9655-1d825d747733 | -6.44313 | -52.73256 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e651ace8-f234-3a8b-a25b-bff8c2bd4a6f | -7.44641 | -45.14761 | 2026-08-19 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 75a7bc91-b9e3-3d66-8e17-10e85f02b893 | -12.51452 | -47.83899 | 2026-08-19 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 90dd32e2-478a-3c0a-890e-963b5651ab10 | -7.44778 | -45.13937 | 2026-08-19 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8673bb68-345b-37fe-8813-5eaccdead87e | -11.16483 | -49.62557 | 2026-08-19 04:19:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ffd84f7c-d152-3613-b4d0-d60e6f9d2b8e | -12.83937 | -48.4232 | 2026-08-19 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7ee2ca46-b6c9-3baf-a5e4-242ea3f52a9d | -6.49613 | -45.81323 | 2026-08-19 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffeb1290-391e-337f-be0f-4fb7fc7523d2 | -10.24651 | -46.99179 | 2026-08-19 04:19:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f0ae6a7-4f80-393f-b9e2-86f27ed1d706 | -9.39149 | -48.24659 | 2026-08-19 04:19:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ecb475cb-9d32-3fec-b5a3-0240ec6c8919 | -8.55259 | -54.75909 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 78a769c9-0a20-3ae7-a99f-a2023199c3ea | -12.24133 | -43.16434 | 2026-08-19 04:19:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| df277a79-53ab-34e2-b563-31e00a046167 | -8.52618 | -54.75413 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fae70f53-426e-37fd-911c-cddc95512a00 | -11.11393 | -47.28868 | 2026-08-19 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c4a371fe-69b9-3908-9707-c70e6fcd5fe3 | -8.56355 | -54.73775 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| f751c8bb-a5f3-3336-ad11-bbbb92d7e740 | -8.08547 | -44.36172 | 2026-08-19 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 56ac9f33-d700-31db-a33d-d3a5f9eae27e | -8.57875 | -54.69434 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8b01ce3f-f822-3df9-8ad5-59817142acf1 | -8.5339 | -54.74964 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0436793b-97ba-3c49-9424-a2c122ae00be | -11.71195 | -54.63475 | 2026-08-19 04:19:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c345eec4-2f93-336b-a9dc-d657ec120a95 | -12.75348 | -48.44024 | 2026-08-19 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f804a35-f291-3fb9-a263-05783596473c | -10.76356 | -42.08829 | 2026-08-19 04:19:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 693127f5-8163-3ba4-a952-7e1febc3f49a | -8.57951 | -54.74681 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 50332e21-a22f-38c7-993b-50c3a052ee6a | -6.84094 | -44.94695 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| edafedf8-88c2-3ea0-96d9-ca876c7e66f2 | -11.63867 | -54.52979 | 2026-08-19 04:19:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fdd97c13-9fb8-3faf-a1c3-4014ba1ec003 | -8.58391 | -54.7247 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a3681cab-d618-3755-85db-6f34114c8f3d | -7.53969 | -55.58952 | 2026-08-19 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 44cdb1ba-0e01-31d4-ae57-8aeb72819fea | -11.62004 | -46.91381 | 2026-08-19 04:19:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 465bf77a-7076-326b-9d28-956f1a55b417 | -11.24014 | -55.06165 | 2026-08-19 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 563ca961-eddf-375a-879d-e525de87585f | -8.21494 | -55.02921 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c1e66e0-978b-3eab-afe0-c6c8ac415ebc | -10.29115 | -48.22881 | 2026-08-19 04:19:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ad1a7ab4-89f3-3309-936f-d1c3ba7198f0 | -8.53292 | -54.71963 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8a714b88-a453-39be-abd0-23814f78d2f8 | -11.31243 | -45.21157 | 2026-08-19 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 957c39ae-8028-3255-af17-60f4697ab8b3 | -6.44147 | -52.74154 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ed0a60e-1a01-3e21-a964-3e5ebe1fe798 | -7.20033 | -43.26429 | 2026-08-19 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| bd018b36-1730-327f-8e04-11f14e9c7505 | -11.20399 | -54.02342 | 2026-08-19 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76d27ce2-ebcc-342e-a300-e890b4ed6dcb | -11.40765 | -47.24041 | 2026-08-19 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8374a439-45d6-3f81-92ef-8976bbd7c4da | -8.56696 | -54.7555 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fe718364-8fc8-30ce-88be-6a5062e06917 | -8.17899 | -44.4356 | 2026-08-19 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 918c4800-0d45-3011-a335-d01e0311d382 | -9.39222 | -48.24249 | 2026-08-19 04:19:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 943c4c65-4ed7-31e2-ac37-358de8dd2bf9 | -0.97834 | -47.49982 | 2026-08-19 04:19:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 452d9951-d520-3a79-a868-38a913ca6158 | -8.57607 | -54.76404 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3d78463c-19c5-302c-9456-deed3d9944c7 | -11.61922 | -46.91858 | 2026-08-19 04:19:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ffd66acc-6457-3ff5-b997-16bbf34ef3b8 | -8.5295 | -54.73715 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5848ea08-4fd6-367c-bba2-30f1165b6f42 | -10.51743 | -50.78882 | 2026-08-19 04:19:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a4aa16ed-ed36-336f-bf82-254f1d3049c9 | -7.2813 | -44.07207 | 2026-08-19 04:19:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 156aa534-863b-3ca5-a811-29e61bdfd1a6 | -8.54268 | -54.73966 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1dbfabb0-e60f-341c-a1bd-62ef4b92537f | -8.58536 | -54.73091 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6925dec0-9358-3ef2-82ae-56f83f5f121f | -6.84023 | -44.95126 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f33428a-8e9d-363c-9c4b-e1c2b00b16ce | -10.24176 | -46.99625 | 2026-08-19 04:19:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7adf0861-203e-3ce0-80bb-d46a7d041064 | -8.56576 | -54.72632 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ba8e5fab-c92c-3bf4-a580-44d155376fd6 | -7.11736 | -47.54245 | 2026-08-19 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c04cb93-738d-35bb-8fd5-3bd97d9580ca | -7.25779 | -44.21441 | 2026-08-19 04:19:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad2c3bd8-2b56-3f8d-a58a-6467d7080d2f | -6.34535 | -54.89872 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e2d80f62-f723-3c60-9a19-f049f839cbbe | -9.11746 | -46.04655 | 2026-08-19 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c62f25b2-205a-3638-8477-f1c4dac1d452 | -11.99646 | -55.52784 | 2026-08-19 04:19:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ad74bbf9-f791-3129-8ecf-5ee3c767f71f | -11.22018 | -54.01034 | 2026-08-19 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| adf166ec-0bf3-3f9a-9b58-e02dd52fb431 | -6.3898 | -51.74577 | 2026-08-19 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f4912a5-eafe-334d-8e62-54c48798f552 | -8.5881 | -54.77244 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| acb08a08-1634-313f-bcfd-d50e5c204514 | -8.53722 | -54.73261 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 909a15f1-d961-3607-9887-fcdbfaf1e4e0 | -11.19648 | -54.81592 | 2026-08-19 04:19:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6a42ca2f-368e-3427-bf27-524ec8ae9914 | -7.18713 | -43.45251 | 2026-08-19 04:19:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1d8a1295-fcf3-3e03-b858-d2ad61784c6c | -11.10967 | -47.26688 | 2026-08-19 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f664cc3-5a9c-3e0a-9bd6-d184b25c9f60 | -7.02253 | -45.8993 | 2026-08-19 04:19:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 76042d9f-e29e-38e8-a68b-09cccf658ae3 | -11.20631 | -54.01692 | 2026-08-19 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b00cb735-2fc5-3780-9e1f-0f4124a4faf7 | -12.04899 | -46.46415 | 2026-08-19 04:19:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2376d4f2-669e-3f5a-a82f-f8a18350517b | -8.53064 | -54.73132 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 44ddc23b-c347-30e9-8f7b-63e73a25d6c0 | -8.58224 | -54.74713 | 2026-08-19 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README28.md)
