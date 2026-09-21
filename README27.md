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
| b6978ea1-a4e2-3889-82d7-240ffe1c4bd2 | -11.79313 | -46.84644 | 2026-09-21 04:02:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1abdd37b-e699-3d2b-8d8b-aa9622e8a900 | -10.40385 | -50.23543 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| b274cfc3-f09d-359e-90f5-d12fdf9158ba | -8.38576 | -47.18133 | 2026-09-21 04:02:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40992691-1871-3954-b273-61118f72ab9e | -10.45156 | -50.26896 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| da804d52-1716-361b-a221-597c6624ba18 | -8.7733 | -44.29564 | 2026-09-21 04:02:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b370dff9-4782-3898-8064-f12d6f96d467 | -12.30253 | -49.18642 | 2026-09-21 04:02:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4a753ee0-b8f2-3e24-a388-d54fb9a6ac9d | -9.45574 | -45.4235 | 2026-09-21 04:02:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fc6ddf6e-27ba-349f-95f9-a8bb3c2ba256 | -7.48188 | -45.47748 | 2026-09-21 04:02:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7c6ee8dd-2123-36c0-90f3-0f40d1f2ed07 | -10.36871 | -50.21494 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| bd525c96-6745-30fd-a325-519ca04224dc | -10.15107 | -47.6785 | 2026-09-21 04:02:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34d3d4a3-b847-337e-9aed-9cc369a13e16 | -13.03871 | -46.96174 | 2026-09-21 04:02:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5000d7f-389a-3fa2-91c2-a20a2f0ee9b2 | -12.3062 | -50.68945 | 2026-09-21 04:02:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d4c53ca5-0094-3331-93c5-6fe5edb880d7 | -10.69487 | -50.76887 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cbf4b597-14dc-3a65-8665-fc52fd09d508 | -7.48753 | -45.47525 | 2026-09-21 04:02:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4ac00c4-c010-34f8-a76b-a1671df9bc83 | -9.44699 | -45.4158 | 2026-09-21 04:02:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a5b24fe4-4576-3f4c-804b-72b71d688862 | -8.30704 | -46.86821 | 2026-09-21 04:02:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 545dfc4f-d20c-3239-8336-2e015f34d9c2 | -11.79951 | -51.11508 | 2026-09-21 04:02:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e7b3b04a-0fe4-3338-9088-8f9e32930078 | -11.47016 | -47.7738 | 2026-09-21 04:02:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 2b70f21c-fed9-3ebb-b864-b9a29360bddd | -9.46764 | -45.41351 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5c88693b-7d79-3c55-9dcf-bbb0df115223 | -9.82961 | -48.44992 | 2026-09-21 04:02:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 21b7a6f4-7a7f-3f6c-bc50-1237a77a78e6 | -10.40924 | -50.24241 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| e0c78fa5-4f01-396f-9e2a-6d481caf9366 | -11.78848 | -49.81485 | 2026-09-21 04:02:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5ebf3ea6-6f71-3e05-bd01-26399caf58af | -8.8279 | -50.49137 | 2026-09-21 04:02:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad4c871d-99b7-3dcb-abeb-0e616f9ee2fd | -7.41765 | -44.76117 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 377dd1c4-dce0-31f6-85dc-6e5b6b88f963 | -10.47256 | -50.28836 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| e0984d74-6f05-3adb-844a-544ddd6c39f7 | -7.07817 | -46.28744 | 2026-09-21 04:02:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a0a6d0a0-a0df-3686-83fa-5e558269d26a | -10.76479 | -50.81114 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5aae3346-f8e4-3e8e-83f9-f35a9eae5899 | -11.99549 | -44.89542 | 2026-09-21 04:02:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d995c43-020f-39d0-9429-64892d1e32f8 | -11.67457 | -43.41692 | 2026-09-21 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91632168-c440-3444-88fe-1b3545c639be | -7.29727 | -46.76937 | 2026-09-21 04:02:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df1b8239-2d10-342a-bee4-5d0157c567fd | -7.44565 | -44.74381 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 30932590-df60-356a-ad8a-c5c560a0e00c | -11.94904 | -46.50046 | 2026-09-21 04:02:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4f368cf-26a1-35a1-970a-17cc71a1c30f | -10.77568 | -50.82604 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f43ac9bb-af8a-3c2d-aef6-bf38207d0300 | -11.80812 | -49.81396 | 2026-09-21 04:02:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| bb167305-9e1f-35ed-bffd-db2830ca61c9 | -11.47566 | -47.77497 | 2026-09-21 04:02:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 93561b30-6ed8-3e6f-8de5-a8055684c433 | -8.76409 | -44.29408 | 2026-09-21 04:02:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2899eba1-4ac7-3256-82ef-84c7b7708db7 | -10.80278 | -50.76295 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e0248ca5-9fb0-35af-a8df-e650849600a2 | -11.04799 | -46.56445 | 2026-09-21 04:02:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8451f4f-4514-3019-9fd6-5a7a344660bc | -11.47633 | -47.7715 | 2026-09-21 04:02:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 4a3013c9-850f-39db-ba4a-1463fd1be287 | -7.45378 | -44.74036 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 35115851-0068-36be-a893-832b57810279 | -13.00446 | -46.92018 | 2026-09-21 04:02:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f5eeccee-f0d2-3aae-aedd-632e52c42970 | -9.9778 | -50.26071 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3b545610-246a-330d-9447-1097219a3b6c | -8.41841 | -45.86419 | 2026-09-21 04:02:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98fa2fea-8783-378f-9ad6-a4cebbc5a241 | -9.44604 | -45.42111 | 2026-09-21 04:02:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4f995f34-5fcd-3361-ba9b-28b22f0adc09 | -11.78931 | -46.83853 | 2026-09-21 04:02:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62bb9c83-5aac-362a-8fba-b150cf2d994e | -10.6731 | -50.73924 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1d1a6efb-a92a-3b67-88ff-47efa2746c8f | -7.2956 | -46.76772 | 2026-09-21 04:02:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88da545b-f796-3284-8bc4-c11b3e3ed42e | -9.02214 | -44.99158 | 2026-09-21 04:02:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d7033a6-17dd-3b78-b34b-4937d648f7fa | -7.42272 | -44.77385 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| da7a1233-89fe-3116-9a4f-9f146269c446 | -10.70033 | -50.77629 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fed105a6-582e-3c53-81d9-0c81d91c14e3 | -8.01038 | -44.81248 | 2026-09-21 04:02:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a8529b78-244f-3122-88a0-11644cd1b777 | -9.44312 | -45.40918 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5ed45f64-181b-3bb2-af74-68758a20fd92 | -10.13583 | -45.55445 | 2026-09-21 04:02:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d3b5861-a566-369a-b981-ba3e6ebbc7a0 | -9.10875 | -44.7025 | 2026-09-21 04:02:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 97642040-ea9f-37f1-a4ff-d7b5dc608c64 | -10.77022 | -50.81861 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f9588adf-762d-379b-8952-1b9d69bd2956 | -9.75084 | -46.24025 | 2026-09-21 04:02:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2123b5e2-b380-30a2-bed3-0180e75b2fbe | -13.03187 | -46.96983 | 2026-09-21 04:02:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb8dcfd1-47bc-33e6-8a8e-342cc0a66204 | -9.26542 | -46.18495 | 2026-09-21 04:02:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a63cfc21-9a4b-3294-adba-b499eb016475 | -9.82109 | -48.43025 | 2026-09-21 04:02:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5359340a-8a58-3a5d-9dbb-e2187edc7b5c | -14.22582 | -44.63646 | 2026-09-21 04:02:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b6b4bdc2-d55a-3f70-8146-882c6f456eb9 | -9.98324 | -50.26781 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb40b1a2-5617-3606-bb44-5d9a1c20237c | -10.70504 | -50.77613 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8020eeb8-725d-343a-9ac8-df6c07c1093d | -9.76657 | -46.06134 | 2026-09-21 04:02:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf997e13-50a9-39f6-a99e-9f45aeaf4f1b | -8.73481 | -36.8269 | 2026-09-21 04:02:00 | NPP-375D | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4dfc067d-88dc-36b6-9e20-a854f3229abd | -13.93058 | -47.84632 | 2026-09-21 04:02:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e184b78-042a-3b5f-acdc-79bbd72394d3 | -14.18059 | -47.86866 | 2026-09-21 04:02:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b3eccf81-7171-36cf-8d95-c969f44a79e8 | -10.83249 | -50.78801 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e2bed53-a2a2-398c-ba42-b069f7a0bc92 | -8.76038 | -44.28827 | 2026-09-21 04:02:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 91d37f3b-aefd-3ae6-a9f1-f186a6bb25e8 | -10.75021 | -50.80584 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3030d7fa-101e-34bd-bf46-8dd74c2cb7af | -13.88811 | -48.57144 | 2026-09-21 04:02:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d13c2544-fd01-3ee4-8467-e50d6130c643 | -10.73033 | -50.71912 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a1824efe-79d2-3d18-910b-4fb09193ab7a | -10.398 | -50.23878 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3ba55918-b6dc-3589-b068-539b843c9a70 | -13.03752 | -46.96796 | 2026-09-21 04:02:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 21a365e6-5553-342a-a17e-55b27d681ad3 | -8.77667 | -44.27648 | 2026-09-21 04:02:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 75d8a957-acd4-3f3f-9bf3-b88079be88d3 | -8.37514 | -45.63599 | 2026-09-21 04:02:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f10c7ec8-cb62-3573-a59c-1a5453a5a172 | -9.46174 | -45.3975 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 83771cd7-4f91-3f9f-b457-0e4c367ba5b0 | -13.2883 | -43.55186 | 2026-09-21 04:02:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b281d8e8-2550-30bd-86bf-de94723752ed | -11.67802 | -43.42143 | 2026-09-21 04:02:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f65b280-9603-36b9-9b6b-2276103c4764 | -12.90151 | -50.97431 | 2026-09-21 04:02:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb75cb1b-4814-31f9-9d7d-b78b7e18415f | -12.3108 | -50.69316 | 2026-09-21 04:02:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 22cf758c-6013-3c6e-b943-2180c3404df3 | -10.47322 | -50.2971 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 4416af78-b146-3ba1-aedb-d504b676e5ad | -10.3908 | -50.23267 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e0a10c6a-ac71-35dc-beac-74ab4bf44228 | -8.78276 | -48.75065 | 2026-09-21 04:02:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 76f132cb-70ab-3e69-b8be-c0e20be4279d | -11.95121 | -46.48886 | 2026-09-21 04:02:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 212f9926-1dfc-375e-bf44-c373af8cb808 | -11.43429 | -47.31304 | 2026-09-21 04:02:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b00e799-6193-3f80-b933-70e8f1266f2b | -11.43819 | -47.29268 | 2026-09-21 04:02:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87c792ae-79c1-376e-a48a-e1971f659219 | -9.45684 | -45.39667 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b19fef23-497b-3be7-9f43-c9045bd28e08 | -10.45179 | -50.28986 | 2026-09-21 04:02:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 059298ff-322a-3178-b77f-59483b1f6289 | -10.67763 | -50.73884 | 2026-09-21 04:02:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4bde4cfe-9a60-3ebf-b03d-0262449e8876 | -9.7502 | -46.06455 | 2026-09-21 04:02:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7639740-c0fc-36cb-8e23-f28e67c81923 | -11.95405 | -46.5016 | 2026-09-21 04:02:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f363cf0-4948-3c67-b2d9-cae7debcfb9a | -11.09182 | -48.31103 | 2026-09-21 04:02:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0e2f0dee-8d20-3686-b6a4-abe31ec6f02a | -11.89546 | -48.99474 | 2026-09-21 04:02:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd892bfc-6925-3f49-a87f-88dbb1acfc6c | -8.78884 | -48.75219 | 2026-09-21 04:02:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5ede47d0-ffcd-3f82-aae9-4f9d99f39f6c | -13.90475 | -48.57506 | 2026-09-21 04:02:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fa4b5549-cce4-36d7-88fb-b178a51a55dd | -7.08418 | -46.28508 | 2026-09-21 04:02:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 606191fc-30a1-3da4-9f7b-7b51206a358e | -11.80291 | -49.80764 | 2026-09-21 04:02:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| eae9e980-4fbe-3a53-8189-6f3064180c0e | -13.33731 | -51.29979 | 2026-09-21 04:02:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 402eb090-a4c2-3c0e-9fe4-a9bdf19778f1 | -9.44798 | -45.41032 | 2026-09-21 04:02:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 878ca460-e520-31ce-b276-0051f87d0825 | -10.47547 | -45.09264 | 2026-09-21 04:02:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README28.md)
