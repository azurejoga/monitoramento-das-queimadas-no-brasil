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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d37ffa68-ae2e-3e08-93e9-36593efd1166 | -10.80698 | -50.77633 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e109c653-84d4-3ca6-ba2b-a1f5a885fa4d | -10.78238 | -50.82748 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4abeda9a-ea68-3617-9d62-7c6d3b4e478b | -10.47141 | -50.29398 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 74e221d6-bcce-33f2-b7a7-898f4008c891 | -14.23011 | -44.63723 | 2026-09-21 04:02:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 41d90910-a2e5-3b60-8ab4-6c5f9171f7a4 | -7.41002 | -44.77626 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3a92bb21-0b08-3cd9-85a0-13a0b2d612d6 | -11.8019 | -49.81261 | 2026-09-21 04:02:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 62fe7a67-81b2-358f-a9c7-9412cb346480 | -9.81773 | -48.41582 | 2026-09-21 04:02:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 558e31ec-cdd5-3e8e-90cb-592dd01fd1e8 | -7.41975 | -44.76253 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 77302435-d184-3dea-b456-5937a6063793 | -9.53201 | -45.40023 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b98a6f91-e5a6-3d46-b439-1c707a68018e | -11.0925 | -48.30749 | 2026-09-21 04:02:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fddfbc38-e42e-333f-ad6a-9eca3e223819 | -7.59009 | -43.44081 | 2026-09-21 04:02:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0238952-2b11-3bb2-94db-8035d4b154e0 | -12.41688 | -47.02676 | 2026-09-21 04:02:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0371ed40-7e37-3c3a-826e-552efa254be6 | -10.8258 | -50.78659 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f840c722-a8dd-3ae3-ad93-c54673f57dc1 | -7.4276 | -44.77461 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| efdbbeb0-47ff-3808-9d10-8c7651ab7d0f | -9.4635 | -45.41522 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b7fed5ff-7fe2-3a80-84e4-e5b47e7382e6 | -8.41963 | -45.86681 | 2026-09-21 04:02:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0324319a-2dcf-39ee-ae55-8b8d91ee6c16 | -7.31814 | -46.77015 | 2026-09-21 04:02:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d02f606-62e0-3190-ae7e-55e0c58593b1 | -7.88615 | -44.84723 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d4ae2d73-abc3-322f-9678-07f58932612c | -10.79764 | -50.77851 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 99258946-0b5c-3adc-b464-49e2b0e74a46 | -11.09755 | -48.31103 | 2026-09-21 04:02:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 085e6879-a06e-3ffa-a4aa-e36e98661309 | -8.96527 | -49.15131 | 2026-09-21 04:02:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3ac09432-5f6a-37a4-a5a4-34bdde30d90d | -7.53405 | -45.87981 | 2026-09-21 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a82d3a5-5f3e-3a64-924e-fc979f812821 | -10.48219 | -50.308 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 424959ea-242c-37c5-aa5d-fac2b6ac9aca | -7.88707 | -44.84205 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b9047af1-9614-3c76-86d5-a048dd898416 | -10.43197 | -50.26479 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 570b3cfc-20cc-31f0-a9e2-071cc33ea637 | -8.30782 | -46.00345 | 2026-09-21 04:02:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a48194d-e292-3c7a-9896-1935231d3bbc | -9.46456 | -45.40953 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aefcc2c3-55f3-37e7-8a41-b4270f302a43 | -12.36529 | -43.85939 | 2026-09-21 04:02:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8f23c08-3f2a-3103-afc3-165039179b67 | -11.62113 | -47.78139 | 2026-09-21 04:02:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5984533b-9452-3090-9fbd-b4016c5511b8 | -9.24019 | -46.1767 | 2026-09-21 04:02:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e93ceeda-1c15-322b-97ed-970515ea0b44 | -12.53132 | -50.07906 | 2026-09-21 04:02:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4bbb5c1-e583-3123-9108-d8cd051431d6 | -7.3879 | -46.03714 | 2026-09-21 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7acda3d4-04d2-3736-881a-be82e7c02e9e | -10.4635 | -50.27738 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 32e98e38-8ea6-3f32-baf4-76f43b45f114 | -7.59524 | -43.43739 | 2026-09-21 04:02:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c119ca02-ddf8-3a7f-b383-2cb8e531ee34 | -11.62878 | -47.77159 | 2026-09-21 04:02:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97cd3697-5de5-37a7-8c69-9d81355f8c50 | -10.47003 | -50.27878 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 87c2f4d4-c991-384a-8787-7a5e84a25633 | -10.45043 | -50.27459 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 7a29723d-67ab-37b2-8fd5-87f0918ead04 | -9.02567 | -44.91818 | 2026-09-21 04:02:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 780abca3-5d40-32c4-8652-7575ae702fc7 | -10.47833 | -45.10381 | 2026-09-21 04:02:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d655218f-882c-3afe-88ac-555e60b4a397 | -9.44779 | -45.43963 | 2026-09-21 04:02:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 19582505-8d8e-3d47-90fa-e17b6327d114 | -10.09455 | -48.41184 | 2026-09-21 04:02:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ac01739e-bbc1-3aea-9aa9-417415ae8b97 | -7.88221 | -44.84128 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3f31263b-78c8-33f4-8f07-d6c7adbf7a01 | -9.44677 | -45.44535 | 2026-09-21 04:02:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e18160ea-16fb-38e3-afd5-74e24dbdac35 | -10.09231 | -50.25563 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 933edb97-4e8a-3dd0-ab5d-43e4d3712892 | -10.37412 | -50.22197 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7467f097-e4df-3a6a-9d65-3dcb5b08b381 | -13.93789 | -47.83722 | 2026-09-21 04:02:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9fde5d3d-f034-34b2-bba6-77dcdb93cda6 | -8.42074 | -45.86081 | 2026-09-21 04:02:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c08b10c9-d97a-3dba-ac03-2a5bc4d49e0c | -14.61942 | -42.91635 | 2026-09-21 04:02:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2bb1d88c-7663-376a-8a67-468324416699 | -11.477 | -47.76802 | 2026-09-21 04:02:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 606fc380-4248-3f75-9812-da3864d28b09 | -11.1983 | -42.86486 | 2026-09-21 04:02:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2d9845a7-bc42-3bab-abed-1b9f0e4334dd | -10.47909 | -50.28975 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| a0739564-23de-3da4-b2c3-042157e9a87e | -13.06359 | -50.62616 | 2026-09-21 04:02:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5c98b89-5125-3bc8-a44d-323f3484f250 | -13.91022 | -48.57664 | 2026-09-21 04:02:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 42c213f7-f56d-33cb-8042-592bf8952fa6 | -11.95066 | -46.4918 | 2026-09-21 04:02:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abbc4472-e9d2-3383-a2c7-15077c555c66 | -11.94958 | -46.49762 | 2026-09-21 04:02:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa6f36d0-248e-345d-9907-89b5056a9b13 | -10.67215 | -50.73141 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 914b4054-c2cd-3cbd-928a-0e0c15a3147f | -8.13389 | -46.82176 | 2026-09-21 04:02:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a7c92325-a9f7-3474-b226-39327bdc36ac | -9.45205 | -45.38757 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 7f78bf83-d7e4-33c5-a7b1-8d7d5c171b1d | -10.46718 | -50.28136 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 30fa253b-3974-3810-9e08-dd0e25b357b8 | -10.80565 | -50.84321 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee51c7d4-ff0a-38be-85cc-ff17f0e308cd | -13.28425 | -43.55111 | 2026-09-21 04:02:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 25746fad-6206-33c3-b8db-e7162509c1d4 | -10.76353 | -50.81711 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 674ba7cd-94eb-3118-83df-bd1275fa759f | -9.46278 | -45.39194 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 0ebd001d-7974-3937-a910-9e81c4d1ccef | -11.34105 | -43.38576 | 2026-09-21 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b753bd6-dbbb-30b2-a4d5-21070f8e3233 | -12.30848 | -49.1876 | 2026-09-21 04:02:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f38afe4-1ff4-380a-8e69-3642b9eac5eb | -10.47026 | -50.29961 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 0e2c4c38-d7e3-3bf8-b378-50269fe0559b | -7.30161 | -46.76632 | 2026-09-21 04:02:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6c62513-623c-32c2-9c28-aa5ae50f31e4 | -7.42159 | -44.76729 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7eabf556-43cd-3224-b808-76fb6673f676 | -7.41095 | -44.77092 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| eb3b3f6a-e18e-362f-80d9-ae1a6f30fa37 | -10.48873 | -50.30939 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e31a0aa0-6307-34a0-83db-e948da7d47e0 | -10.81769 | -50.78289 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55b3a492-9be4-3138-8f2c-b44149e301d5 | -11.79795 | -46.84729 | 2026-09-21 04:02:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8c2794c-5e9b-3bbc-a570-45af22bb1070 | -11.11706 | -47.51753 | 2026-09-21 04:02:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d7b3b83-1996-3367-a607-89a4a3227c3d | -7.42068 | -44.77256 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a188f5a1-85c5-324b-ba53-c7635f6b2f3b | -10.76239 | -50.81474 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1f8705bb-90a0-3761-beaf-a5ec14fa74c1 | -7.44793 | -44.74505 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d787ed27-ce64-334d-b49b-044229c2fe69 | -7.41884 | -44.78318 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| c379a9fa-1465-362e-99f7-4d05db99518b | -7.41985 | -44.78975 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| cfa5bd30-3a75-3861-bd10-af57dd8949a9 | -11.04742 | -46.56748 | 2026-09-21 04:02:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce516eec-ea6e-3a01-87c9-3fe76a2c1d26 | -9.7552 | -46.24109 | 2026-09-21 04:02:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 642ca6d2-ee7c-3baf-95b6-87e8b0107d6a | -10.79735 | -50.75554 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 88634ff5-c8b4-3fcb-a047-92674f5cc266 | -9.45578 | -45.40232 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0e121384-4942-368e-a420-65018c400465 | -7.42367 | -44.76856 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7dc2433e-4918-371c-8985-b7f6aad02d3e | -7.38204 | -46.03939 | 2026-09-21 04:02:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cdc88100-1e29-3c25-b907-662392a8755f | -9.25961 | -46.18743 | 2026-09-21 04:02:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d7c270f-ee37-39bf-958b-9e183ae64f19 | -11.32285 | -47.3019 | 2026-09-21 04:02:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ae4a5b55-3492-31f8-b863-c1d9d182ca1c | -10.44989 | -50.26601 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 0f8777a7-f55e-3c58-9540-43fd9bd423c3 | -14.98119 | -43.09096 | 2026-09-21 04:02:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 16.2 |
| 66228132-932f-30de-a17d-4b3e61e07cd2 | -11.67389 | -43.42068 | 2026-09-21 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8e2c139b-cab9-3c6a-b554-926fa35d793a | -9.75027 | -46.24328 | 2026-09-21 04:02:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| baaa9428-8a3c-301d-ab52-47bb2d615640 | -12.41626 | -47.02991 | 2026-09-21 04:02:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 774ff22a-7c27-3581-b57e-3c71d550630b | -7.75593 | -44.8339 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 466468c8-0143-374a-a2d9-7438e43a636b | -12.02884 | -47.81736 | 2026-09-21 04:02:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38e94041-1c10-38dc-97ee-dd9b6c1fb9c4 | -11.93344 | -46.50012 | 2026-09-21 04:02:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 621ce5db-e3b0-386d-ba08-7360389c74c9 | -7.05939 | -49.91005 | 2026-09-21 04:02:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3f85b1c1-3408-321b-951d-9b426764ac45 | -10.81367 | -50.77777 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ec011251-f023-304b-844a-1ce8d397fb64 | -7.4188 | -44.76778 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 98c78f1c-83a5-3f63-af72-46712b162ed9 | -10.36585 | -50.22161 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 879745b3-22d7-35c4-8fa1-abe296bcc9da | -8.78452 | -48.74149 | 2026-09-21 04:02:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 389e58a5-1335-3d74-beef-3c530af73875 | -7.07878 | -46.28406 | 2026-09-21 04:02:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README25.md)
