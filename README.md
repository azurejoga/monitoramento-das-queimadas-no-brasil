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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0f260b1-5d40-313b-a04b-d55f827263e3 | -12.37 | -50.0242 | 2026-05-03 00:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 647abe2d-21ba-3b48-883c-8117c53e0012 | -10.9815 | -45.0874 | 2026-05-03 00:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| c61a092b-b70e-3ca1-813a-7e2d8e4dbd25 | -12.3508 | -50.0266 | 2026-05-03 00:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 7d4a9969-21ac-3514-9978-5d470138f171 | -12.3508 | -50.0266 | 2026-05-03 00:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 0c5752b6-1467-36ba-b436-135017718d4c | -12.37 | -50.0242 | 2026-05-03 00:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| 12863e9b-1764-3580-8f9e-f96e945a0d9b | -10.9815 | -45.0874 | 2026-05-03 00:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 7ffb6899-2bd4-3270-b8b2-2c68c7fe32bb | -17.99469 | -53.00282 | 2026-05-03 00:11:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 913f80ec-f7ad-3882-93b2-da0d0c36a0d4 | -17.97512 | -52.99351 | 2026-05-03 00:11:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 426.2 |
| 44c5630f-f79e-33a1-8393-d214eebf7730 | -21.57395 | -48.36386 | 2026-05-03 00:11:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 18.9 |
| eeed8613-4962-337c-9688-cbf389c12087 | -17.98906 | -53.00976 | 2026-05-03 00:11:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 9fa0ec73-bfbf-34fc-98b9-d02dcc0eff17 | -17.98707 | -52.99206 | 2026-05-03 00:11:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 255.6 |
| 59b7781d-1e60-3280-9faa-71296ca7c36b | -17.94932 | -52.979 | 2026-05-03 00:11:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 153.1 |
| ba35a7de-857d-32b7-8a45-cea6f08f06d8 | -17.94737 | -52.96126 | 2026-05-03 00:11:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 4ceb9c25-6c9a-3057-8f32-775616ea189b | -17.96318 | -52.99509 | 2026-05-03 00:11:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 576.4 |
| 0d10c33f-f938-3321-a0da-50419ea37a44 | -17.97316 | -52.97591 | 2026-05-03 00:11:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 45.4 |
| df5bb441-571a-37d5-8e72-982231491d79 | -17.96124 | -52.97744 | 2026-05-03 00:11:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 822.4 |
| 30dc4cbd-894e-32e2-bd2d-59c696035a77 | -20.18706 | -46.45515 | 2026-05-03 00:11:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 0c1c0743-f4b7-3a58-a9d9-126a8838f4c6 | -20.18575 | -46.44579 | 2026-05-03 00:11:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 944982c5-480c-314f-b00d-c03a185af678 | -17.99282 | -52.9851 | 2026-05-03 00:11:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 353b1c2e-dcb8-35cf-9db8-b6d1af2663f0 | -10.59221 | -44.33371 | 2026-05-03 00:13:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 25541f0f-661e-388e-9a43-fd6bcb4922b1 | -12.35636 | -50.02868 | 2026-05-03 00:13:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 136.7 |
| 68d4d96b-ee8f-3833-a8a7-bffadca597e8 | -12.45863 | -44.30652 | 2026-05-03 00:13:00 | TERRA_M-M | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b7113c4f-7560-3e22-b50b-9b12300babcb | -11.95559 | -43.96853 | 2026-05-03 00:13:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e7ed7670-2aee-337e-8a68-e8570909fe1c | -10.57924 | -44.32149 | 2026-05-03 00:13:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 28.4 |
| b4cad1aa-10e3-358d-a6a7-a1176ab8f776 | -9.67986 | -43.79369 | 2026-05-03 00:13:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 202c7cff-9ea9-345d-8b99-089777597666 | -10.64224 | -48.00255 | 2026-05-03 00:13:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 7aab6f96-541a-3ee4-b70d-b0b1aa41a6cc | -13.21424 | -54.56908 | 2026-05-03 00:13:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 49.0 |
| 45b80a0c-7184-3fdb-a007-91a83f022d8b | -10.97924 | -45.09205 | 2026-05-03 00:13:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 75165bcd-ae6c-3b0f-8b74-f152d20021e8 | -13.22231 | -54.52876 | 2026-05-03 00:13:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 23b6fa7e-b6cc-376a-a846-caf4de4dc0a6 | -11.30356 | -54.73478 | 2026-05-03 00:13:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 91af57a4-7897-34de-9570-fcb50a000e74 | -13.21198 | -54.5495 | 2026-05-03 00:13:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 586.3 |
| c83db455-e5cc-3c16-9be8-f4140aa71b5c | -13.20972 | -54.5301 | 2026-05-03 00:13:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 286.0 |
| 58181fca-af07-3106-9df7-d1a67129c110 | -10.97178 | -45.09896 | 2026-05-03 00:13:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| b2b40ef4-012e-35e2-9dbc-d0ab7dac2567 | -13.23488 | -54.52735 | 2026-05-03 00:13:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 6f6249b9-c131-3ed5-b496-136ed1def321 | -12.28495 | -44.6316 | 2026-05-03 00:13:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 26.1 |
| daae3164-c8f1-32b6-8cf1-296bc005d731 | -10.58347 | -44.32864 | 2026-05-03 00:13:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 40c88d1e-b005-30eb-a3bd-31b8f131d47e | -11.64174 | -52.5641 | 2026-05-03 00:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| abc7b57f-ede9-3f62-9f06-3494557e6f49 | -10.98946 | -45.0905 | 2026-05-03 00:13:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b3872ef4-2c6f-38f6-83f3-32086bbd7d25 | -10.65821 | -46.37444 | 2026-05-03 00:13:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a1d7285d-eecb-3ff3-a3d5-4128ddf41a41 | -15.45333 | -43.32547 | 2026-05-03 00:13:00 | TERRA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 0e69e2af-b9b0-34b5-947a-84fcbd347ecb | -10.98201 | -45.09745 | 2026-05-03 00:13:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.1 |
| f2d55cc2-ae17-3af5-bb88-c29ad4212436 | -12.36672 | -50.037 | 2026-05-03 00:13:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7d689bf0-2c77-385e-8524-921f52b0e322 | -12.36545 | -50.02741 | 2026-05-03 00:13:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 251ca8bb-7913-37d3-b0a2-25fb74c70290 | -10.9802 | -45.08513 | 2026-05-03 00:13:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 99f4833a-0555-3b36-bca7-77d4ea8301ac | -13.19717 | -54.53165 | 2026-05-03 00:13:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 494.1 |
| 436368ef-8860-3734-a634-a06a0bc510f0 | -16.1075 | -49.24295 | 2026-05-03 00:13:00 | TERRA_M-M | PETROLINA DE GOIÁS | GOIÁS | Brasil | 5216809 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 34637b30-6d54-30f2-b14a-779050180308 | -13.1994 | -54.55107 | 2026-05-03 00:13:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 393.7 |
| 8ac63be7-b1de-339c-bcf2-0fb0b5899f2a | -12.37455 | -50.02615 | 2026-05-03 00:13:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6f947927-123c-3cfc-a5b3-938b72ec81b4 | -12.35762 | -50.03827 | 2026-05-03 00:13:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 345f63e0-cb82-32cc-8515-41e7ed83cf6b | -10.32648 | -47.91858 | 2026-05-03 00:13:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fe70d952-b98b-3b9a-bbfd-9fcab05b3afd | -10.98112 | -45.10425 | 2026-05-03 00:13:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 31.8 |
| d725fb56-cafe-3cfd-b35f-e336b0c21d82 | -11.64898 | -52.57056 | 2026-05-03 00:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 43e4a775-07ea-310d-af1e-da7feca9ecf4 | -9.66834 | -43.79565 | 2026-05-03 00:13:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 625c40ba-f64e-3627-b63d-e34723b2ce40 | -13.23717 | -54.54678 | 2026-05-03 00:13:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 12615c45-93fd-3228-8e11-d6fe01f8b7ed | -12.27463 | -44.6334 | 2026-05-03 00:13:00 | TERRA_M-M | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 8728ea37-a64b-339a-8f23-5d01fc654ee9 | -11.63849 | -52.57193 | 2026-05-03 00:13:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 09c30c7c-16a4-37b8-b90a-f06f35518cb6 | -10.65668 | -46.36399 | 2026-05-03 00:13:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ff44708b-f261-374c-9691-688f94e8dc22 | -13.22457 | -54.54814 | 2026-05-03 00:13:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 132.1 |
| f0fd97b4-adfc-3ce5-9a79-12bd7cb4679e | -10.58134 | -44.33546 | 2026-05-03 00:13:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 36.0 |
| d96d2ac9-9339-33e1-96ce-dcdec6cc699d | -10.6435 | -48.01155 | 2026-05-03 00:13:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| b82536f5-0d7c-3c42-a110-b41c229177de | -12.37709 | -50.04532 | 2026-05-03 00:13:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 50c1edfe-bb57-3342-a081-d37f84c622ef | -10.59013 | -44.31974 | 2026-05-03 00:13:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a61bc7d2-af48-3f71-9588-066ac777ea41 | -9.46929 | -47.79014 | 2026-05-03 00:16:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 34932bc8-300a-3016-815a-9dc925b16a20 | -9.57124 | -50.68214 | 2026-05-03 00:16:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 0a414781-04f9-3cfc-a865-967fba9c6a98 | -9.6719 | -43.80072 | 2026-05-03 00:16:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| e0d48c94-a99d-3d9f-a644-6d16d0cc7dff | -9.47061 | -47.79944 | 2026-05-03 00:16:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 11cd4201-24c5-368d-bb01-a70a83eb8ed4 | -8.32614 | -45.35591 | 2026-05-03 00:16:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e4bc0268-3069-34cc-beaf-1f6352118deb | -10.9815 | -45.0874 | 2026-05-03 00:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.1 |
| e9c4c0e5-8a00-3422-8ca8-8db07dd374d2 | -12.37 | -50.0242 | 2026-05-03 00:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 9d3bcac9-624c-3f16-85b8-d5244ecf0ef7 | -10.9858 | -45.103699 | 2026-05-03 00:20:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ade31f1b-b291-32ea-890a-2f9bb7f5c3c6 | -21.5746 | -48.370098 | 2026-05-03 00:20:00 | METOP-C | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2e77f535-43d2-3ab0-b71a-b2d8daaa212d | -10.9725 | -45.0896 | 2026-05-03 00:20:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e0ad9045-5819-3454-89f7-7bd008560d39 | -17.9827 | -52.9697 | 2026-05-03 00:20:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 41c73511-cce4-340e-b938-8d910704cb6e | -12.3588 | -50.0186 | 2026-05-03 00:20:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0c9167ad-c888-30a8-b870-324fc218793e | -12.4651 | -44.3036 | 2026-05-03 00:20:00 | METOP-C | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0d738407-5186-3459-a32b-fae283b518ed | -9.6791 | -43.787399 | 2026-05-03 00:20:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 4b7ddd85-4bac-3a74-b6fa-253a4e49bf74 | -12.2784 | -44.626999 | 2026-05-03 00:20:00 | METOP-C | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 52f6415a-3381-391c-ac0a-5d81c693d7ea | -17.9538 | -52.974602 | 2026-05-03 00:20:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1aa5fd2e-5402-3ded-af6d-adcc34ae3763 | -9.472 | -47.789398 | 2026-05-03 00:20:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e423ac32-5038-32ca-b1c0-9ba1e3bbab8a | -17.974001 | -53.039299 | 2026-05-03 00:20:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 624c1c3d-dd0b-35c3-87b0-36d7ee6699e5 | -17.944201 | -52.9762 | 2026-05-03 00:20:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bf2949b3-2dc5-338c-bf9d-6a7608b1ef97 | -17.9389 | -52.943298 | 2026-05-03 00:20:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f685f1dd-de99-33bd-b18f-1c31da8105ca | -17.9687 | -53.006001 | 2026-05-03 00:20:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 40e455c6-7749-33d6-bd7e-2b5aa8dd2b7b | -17.973101 | -52.971401 | 2026-05-03 00:20:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c20a5410-9365-3bfa-a2e8-1f931221b1dc | -12.3525 | -50.037701 | 2026-05-03 00:20:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7230ce07-cbdf-3ce9-8d93-d4413298d89d | -12.3555 | -50.001499 | 2026-05-03 00:20:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d6c76e83-4d6f-32a3-9403-764c85827790 | -10.5814 | -44.3325 | 2026-05-03 00:20:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 52e32fdd-6573-3166-b97c-5688ccf5a0b5 | -10.5781 | -44.317402 | 2026-05-03 00:20:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 53f7c13e-deab-3b77-8bde-f564932a127c | -12.3622 | -50.035801 | 2026-05-03 00:20:00 | METOP-C | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 20f7994d-af19-3f99-a10d-02ee26141098 | -9.6807 | -43.794601 | 2026-05-03 00:20:00 | METOP-C | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| af566ef2-05cd-326b-9dba-a32d97ccc3e2 | -17.988001 | -53.0028 | 2026-05-03 00:20:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 22dd1cc8-29e6-3c7c-9ebb-935f2acaacfb | -12.2801 | -44.634998 | 2026-05-03 00:20:00 | METOP-C | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 87c645b6-92d0-3eb5-b733-21d440d94e35 | -10.9841 | -45.0956 | 2026-05-03 00:20:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dc4b0ebf-dbf9-3cfb-93a0-96f8e836cb2c | -8.3302 | -45.356899 | 2026-05-03 00:20:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fda0a06a-ce9c-368d-b694-92ba07d6816a | -17.9923 | -52.968201 | 2026-05-03 00:20:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 70ee51ef-27b6-39b6-9f68-f5adadc155e9 | -17.9634 | -52.973 | 2026-05-03 00:20:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e9c5c970-1bd2-3797-98fa-40bb520f8a63 | -10.6406 | -48.006699 | 2026-05-03 00:20:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6667d623-66df-3ef6-a0ab-1d073ac30fb8 | -10.9743 | -45.097698 | 2026-05-03 00:20:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8fa92f82-2fc5-3d72-8313-9eb178533c3e | -10.9823 | -45.087502 | 2026-05-03 00:20:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f8f363c4-bfd7-37f5-8dec-43cdd1e4c23b | -17.959101 | -53.007702 | 2026-05-03 00:20:00 | METOP-C | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
