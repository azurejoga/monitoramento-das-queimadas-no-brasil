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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51055855-4f04-3866-91c0-27866a0494a8 | -11.35567 | -45.21062 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ecc80b47-60dd-3d9f-b012-2e97b27befaf | -11.34886 | -45.21837 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04eb638c-11b9-3d2d-a3ac-03cfa8378593 | -11.67636 | -47.61589 | 2026-08-31 03:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 315d22e1-7ea3-31fe-8aa3-3c6b3cbd3022 | -11.21879 | -45.1399 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0431fdf3-f8ca-3c70-bdb1-b7a91132a4da | -9.43185 | -45.67982 | 2026-08-31 03:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 122c6856-2bb6-3aa8-b0b5-170bd99371c0 | -15.19856 | -46.23161 | 2026-08-31 03:55:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d8af2a4-b91b-3b57-94b0-254ae4b003b1 | -11.36432 | -45.19304 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 56897de7-fa1b-3a81-beee-7f949aa734b3 | -11.358 | -45.19823 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dcb1e497-63a0-31fa-927d-2a2763f182f2 | -10.54956 | -46.21068 | 2026-08-31 03:55:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 879aacdb-752c-3f46-9f31-acfc9e059fca | -10.73805 | -47.96056 | 2026-08-31 03:55:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 73ae0bb2-1e25-3cd8-b584-34d3fcc06eff | -11.36371 | -45.22476 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d21df2da-c715-3302-a586-2d2587296a6e | -11.36489 | -45.18999 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| afa9cf12-0e72-3690-95d7-d5d1cdeba5e7 | -12.1337 | -47.26098 | 2026-08-31 03:55:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b5d01a0d-bd56-3041-9df0-64fb7bafd887 | -10.74734 | -44.86436 | 2026-08-31 03:55:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43326a84-e57f-39ae-88d4-f1addac2e281 | -10.81334 | -50.66072 | 2026-08-31 03:55:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| cc4468e8-b987-3121-965a-8a2a8bdbaec5 | -10.14781 | -45.75501 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2735fefb-ab95-356c-a273-7537c08b380a | -16.29047 | -42.5803 | 2026-08-31 03:55:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 117c3bba-2c0f-3f1b-9326-37b755c83b4d | -9.42632 | -45.64843 | 2026-08-31 03:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5bf3c90a-952c-3fc3-8dcd-f992f31736cf | -11.88186 | -45.81829 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8c545024-d2ad-3f17-a6bf-eaba38a418fc | -11.36025 | -45.21471 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd94c08f-f078-35ca-bb9c-7eb93ae1b882 | -10.13261 | -45.74566 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00a5f88c-ac5d-3a2d-be03-722cde3112cb | -12.90152 | -45.84415 | 2026-08-31 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5e4ef2d-21bb-3ea0-86a7-e8ec61c184e7 | -11.79299 | -47.6627 | 2026-08-31 03:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b401a6a-2bf6-359c-bbaf-b7f3a5cfe3cf | -11.20739 | -45.06044 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b0857591-1fb1-3dc5-a56f-831c2be31e99 | -11.36257 | -45.2308 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a26f27c-bb7e-35b2-812e-865ffe7b1cdd | -10.13338 | -45.74162 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b55bb3d4-cfc0-3a61-8bc2-dc7933eacea7 | -12.10261 | -45.0353 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 516222b9-719b-3f7d-ba7f-89d2ac90023e | -15.67291 | -45.93299 | 2026-08-31 03:55:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d8abdbc8-15a6-32a9-a7ca-9eb0fc1404b3 | -15.19026 | -46.24609 | 2026-08-31 03:55:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2799a1e8-7fd7-3bff-a379-2c8972d1a209 | -12.08723 | -44.97986 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 04caba1f-cc50-3ab9-9331-b52b8ff0be97 | -11.36485 | -45.21869 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6de905e3-bad2-3b2a-bbd0-3516b5928e12 | -10.14638 | -45.76253 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b54aba89-a722-3e43-86ca-f58470c7f099 | -12.39404 | -46.45664 | 2026-08-31 03:55:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 58247e5c-0e25-3706-b458-03a34e1fce09 | -10.81324 | -50.65882 | 2026-08-31 03:55:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ae2b52ff-2157-3cb4-b4b0-5563ae9ab872 | -11.33624 | -45.20026 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8b3f452c-1521-3834-af09-821bd810ed41 | -12.78495 | -46.4593 | 2026-08-31 03:55:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b563c895-6ff4-309f-87d3-db2b6535d43d | -10.74949 | -44.88107 | 2026-08-31 03:55:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f6e61bc-e6de-3a2f-bb16-9561d9b50d85 | -11.35054 | -45.20949 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64c72338-adc6-35fc-badb-511dd091c55c | -10.12776 | -45.74147 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c52ffe22-6b05-3728-9cc3-21f5f12dcb9f | -11.22316 | -45.0891 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0a4abe3-4163-325a-8b0c-35fb2669cafb | -10.84718 | -45.36179 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc20795d-7773-3193-bcce-f2bfdeaed4e3 | -11.21173 | -45.0932 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| abeaf765-1ef3-332d-83b4-12b13befeb0c | -11.34997 | -45.21247 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 26ae48c7-ecc3-310c-a6cb-734bb57567a6 | -11.3483 | -45.22134 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62ca629c-da5c-3e86-a441-e31722e80f80 | -10.84655 | -45.36509 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba044661-5b0e-39c9-80cc-623a4c50321d | -12.1129 | -45.03605 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c2fbc62-2be8-3ef0-99d0-16b1a86d34c7 | -10.01444 | -46.39206 | 2026-08-31 03:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7bd9921-909e-3db2-8d76-d65bc1c9489d | -11.87527 | -45.82389 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3bf46842-cd6f-3605-a1b4-409619f1c9cb | -13.38909 | -41.32549 | 2026-08-31 03:55:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 82cd8404-e0f4-323f-ba1a-053b6cceb8f6 | -12.11844 | -45.03437 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f83afe40-6479-3676-8add-d0ab4ac36543 | -10.0081 | -46.39429 | 2026-08-31 03:55:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| aa0b6e1a-37a5-3cc4-9f13-604624566468 | -11.6796 | -47.60746 | 2026-08-31 03:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 70eee77b-9d6f-32a0-90a0-86c9f9557c60 | -15.19277 | -46.23376 | 2026-08-31 03:55:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b8e763c-7edb-357b-83ea-d1cf43b71846 | -12.94651 | -45.9485 | 2026-08-31 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3baf5055-6a30-30ae-ae32-fc3f3c764db2 | -17.58899 | -39.49646 | 2026-08-31 03:55:00 | NPP-375D | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f947251d-1795-3e22-aef9-273cf1dcc472 | -11.32933 | -45.18044 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b20202e3-8880-3c87-b981-766f1d3c5ef9 | -11.22205 | -45.0949 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1db4996-c1e8-3e90-84f5-003c4b6edf77 | -12.08828 | -44.97927 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 803e75ea-8eb3-3ce8-9de7-73399f587290 | -11.3322 | -45.19341 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ca6e4ef-57cb-3b34-837e-8874a46be71c | -14.20094 | -46.56839 | 2026-08-31 03:55:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 694a90e4-4840-3e0f-a3a4-fdec08753278 | -11.37121 | -45.21326 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b772a2c3-3859-3c03-bd39-9025c34a3a15 | -10.74675 | -44.86748 | 2026-08-31 03:55:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 664734a7-f9b6-32df-a9d3-a89ef12b122a | -11.68336 | -47.61185 | 2026-08-31 03:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b269e6bb-9eee-3ffe-a8c0-11d1e0530e90 | -15.20037 | -46.24909 | 2026-08-31 03:55:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 114ef184-029f-3e3c-97fd-629d0df51866 | -11.37174 | -45.18192 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| de86e3cd-21b8-3a6f-b654-f3ba51e8dc05 | -15.11474 | -40.04688 | 2026-08-31 03:55:00 | NPP-375D | ITORORÓ | BAHIA | Brasil | 2917102 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| aab22634-dcc3-3056-9603-dd60c36c7c7f | -12.94713 | -45.94526 | 2026-08-31 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 772b14bd-7ace-381e-b305-1cff0ed6b33e | -14.45557 | -42.64932 | 2026-08-31 03:55:00 | NPP-375D | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f14df8c3-8431-38c8-92b0-4c463e8c6bb3 | -11.20796 | -45.05748 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ef5e872-156e-3d23-8a06-f04da017e232 | -12.08736 | -44.98417 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 50fae509-852a-3a6e-819c-1c4b732388b6 | -11.22715 | -45.09605 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8fb50b2c-291f-3937-851f-8c8988675970 | -10.55305 | -46.21107 | 2026-08-31 03:55:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 18ff5e04-a9f6-36e7-838a-91dee1f212ee | -10.7552 | -44.87877 | 2026-08-31 03:55:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93775040-f885-3c1c-9a61-7d19f404398a | -15.66413 | -45.92472 | 2026-08-31 03:55:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9a9eaf01-106d-30c0-bd64-375c93f50383 | -14.19946 | -44.58712 | 2026-08-31 03:55:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dbdc86a1-af4c-3d0e-a875-f5c7ef9dc3c3 | -11.20145 | -43.37482 | 2026-08-31 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d290c63d-56cc-3d47-af00-5f136418c3ed | -11.21633 | -45.097 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c6e9eb6f-0be7-3a5d-b101-ce16aad701b5 | -11.2176 | -45.14614 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fcd1488d-0e66-3e71-a123-aa8a84cb6ae8 | -10.83082 | -45.31152 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44149540-f5f1-3eca-a064-444a8e6a7c32 | -10.74117 | -50.64285 | 2026-08-31 03:55:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 190a0c38-eb4d-3c1c-9ef1-0173be41046c | -11.33334 | -45.18743 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 68eeaf5b-8215-3912-9cee-58872e29efb9 | -15.20104 | -46.24577 | 2026-08-31 03:55:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ee966a39-b3db-3038-9066-5823a7b59e67 | -11.35228 | -45.2286 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 324dabb6-2852-3ac4-a376-78a5edee3555 | -15.6714 | -45.93454 | 2026-08-31 03:55:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| c7b03944-b669-32b4-8e63-67f8fa97728d | -13.19607 | -44.06411 | 2026-08-31 03:55:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87ebad49-5ab0-350c-8570-b8cbb3c549d2 | -16.28546 | -42.58522 | 2026-08-31 03:55:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0197c2b-e6ac-321c-93d9-5327f70434b0 | -12.91491 | -45.91447 | 2026-08-31 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c25b8f9f-7b62-326f-b1b5-9e45028ca487 | -12.95298 | -45.94326 | 2026-08-31 03:55:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 913cf6a0-6e10-3118-973a-9aa693807523 | -11.2169 | -45.09402 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c832ac04-5627-320f-9867-57838175b43d | -10.73418 | -44.87814 | 2026-08-31 03:55:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a0b814e-8b96-3853-b175-4d70b8e2c6b4 | -9.43454 | -45.66536 | 2026-08-31 03:55:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48865619-aad8-3c1b-b596-a9b46a1f6f12 | -12.09742 | -45.06236 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a43ef10-da7e-36f1-b8d5-6562293c0125 | -11.35286 | -45.22555 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fa3d27e3-57b9-3ee0-8b51-eee8c394cead | -15.6691 | -45.92587 | 2026-08-31 03:55:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9e49c672-2854-3927-8eae-5110a7e737df | -11.35968 | -45.21772 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5bea2cc1-cfd7-3370-8c71-f7a4a57cbf3f | -13.36294 | -46.92089 | 2026-08-31 03:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 92f344fa-0a2f-3e26-bc3d-345258a742a7 | -11.3425 | -45.19547 | 2026-08-31 03:55:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b1fea01-2336-33fb-8022-5e7b65af46ea | -12.09311 | -45.0576 | 2026-08-31 03:55:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 657d3ce9-f4d1-3b2f-ba98-21181263fd4e | -17.5255 | -40.24271 | 2026-08-31 03:55:00 | NPP-375D | LAJEDÃO | BAHIA | Brasil | 2918902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 32b6b39d-6cd8-333c-8246-ddadd05de5e8 | -11.6901 | -47.60916 | 2026-08-31 03:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |


[Clique aqui para ver as próximas entradas](README22.md)
