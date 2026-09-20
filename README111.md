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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6e7fd68d-8ef1-3e88-b02d-1cf27b1de24c | -17.57118 | -44.95392 | 2026-09-20 12:06:00 | TERRA_M-T | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 31.6 |
| fec27003-a59b-3797-8ad6-f0b9ff82951a | -11.65647 | -50.20394 | 2026-09-20 12:06:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 1ab1eea4-0b28-3135-b851-bd577c146adf | -10.87204 | -50.18628 | 2026-09-20 12:06:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 66975ed6-5eeb-3762-a99e-2b5282d1b813 | -14.66669 | -46.67147 | 2026-09-20 12:06:00 | TERRA_M-T | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 5cfe4a2f-8849-337e-a5ea-c233aac0509e | -13.28186 | -51.33956 | 2026-09-20 12:06:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 13e949e2-d749-3370-b366-f90c873a43b8 | -11.04162 | -54.92789 | 2026-09-20 12:06:00 | TERRA_M-T | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 33.0 |
| cdf7389a-36c4-3632-bd8e-c081c77eb494 | -10.77862 | -50.87177 | 2026-09-20 12:06:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 81ee6609-5c01-39dc-a634-282d840174c4 | -14.91682 | -49.9063 | 2026-09-20 12:06:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 478b92d6-469a-331d-bd95-331efe9dfe90 | -10.34714 | -50.2236 | 2026-09-20 12:06:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 62ad849a-311b-3a8b-9d7a-bf385f08909c | -10.34419 | -50.24592 | 2026-09-20 12:06:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| ffe41d31-e726-35b5-990d-43034df694fe | -10.85528 | -50.1608 | 2026-09-20 12:06:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 3c96d018-5a1f-3dd1-aed5-16651c97cc3e | -11.48414 | -47.76159 | 2026-09-20 12:06:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 6567eb79-ed4d-311d-b497-3d60bb2e7c26 | -10.78044 | -46.35019 | 2026-09-20 12:06:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 0ded8bb7-8f5f-3c2c-9d4d-fe7db2fd2402 | -11.65494 | -50.21561 | 2026-09-20 12:06:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 74e6677a-da91-3fcd-87b0-a59c6966d4d6 | -15.87772 | -49.9277 | 2026-09-20 12:06:00 | TERRA_M-T | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f590f40d-0b1f-3b77-b5b6-37eac4ae41e1 | -10.9245 | -53.96873 | 2026-09-20 12:06:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7240948d-c629-3daa-93d7-e4b7ef40719f | -11.4567 | -45.38415 | 2026-09-20 12:06:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 42.8 |
| e59af8d5-b3ea-3c65-873e-3125c0df3a44 | -14.9151 | -49.92012 | 2026-09-20 12:06:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| d91f49af-ae57-3459-a8dc-525ccf6fe96c | -10.33879 | -50.21113 | 2026-09-20 12:06:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| fbe0f1bb-01f0-3296-90e5-ce214b5ecf52 | -12.75994 | -46.20369 | 2026-09-20 12:06:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 439.2 |
| 20dedebe-a3a6-3dbe-ba96-42b55120d427 | -12.27957 | -47.10605 | 2026-09-20 12:06:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 95c8aca6-216a-3e02-bf29-70c25a383117 | -17.01428 | -47.137 | 2026-09-20 12:06:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 27.6 |
| 07e635ca-fee9-3f0c-9afc-efdc05527171 | -9.67328 | -54.32 | 2026-09-20 12:06:00 | TERRA_M-T | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| bde8a5b1-51b9-3c66-a3a4-fa525f5ac842 | -11.04348 | -54.15871 | 2026-09-20 12:06:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 24.4 |
| efaca902-dfa5-35b5-aeae-045a50021783 | -10.28296 | -50.55958 | 2026-09-20 12:06:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 2160b92f-bde5-3472-bf7c-2cf3316d24fa | -12.15481 | -47.05893 | 2026-09-20 12:06:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 42.6 |
| a7fcd52f-2822-36ad-8d1b-74d2befce189 | -11.48199 | -47.77927 | 2026-09-20 12:06:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 37.0 |
| ca870346-bf34-3dfc-ba66-1c5076490365 | -11.11855 | -54.02782 | 2026-09-20 12:06:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 09d199d1-d964-32a0-835c-c648f0b3bc2d | -11.10083 | -54.02525 | 2026-09-20 12:06:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| cd924960-4539-30c7-b437-715e75b4c03f | -10.354 | -50.24723 | 2026-09-20 12:06:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| d8233559-4cbd-37da-9d79-36adedf9c85f | -14.67798 | -46.69699 | 2026-09-20 12:06:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 528.5 |
| e21d92fa-6ecd-38f6-be54-4a0c7b19e053 | -10.38824 | -48.91567 | 2026-09-20 12:06:00 | TERRA_M-T | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 2b4607e1-d47c-33a3-9090-47336ca8e66d | -11.81665 | -50.06877 | 2026-09-20 12:06:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 67f08316-342f-3575-801c-af61279db243 | -10.31033 | -50.25821 | 2026-09-20 12:06:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 9630880c-5680-3c03-babe-8992e1abe4c0 | -10.78283 | -50.87848 | 2026-09-20 12:06:00 | TERRA_M-T | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 704a2d66-12cc-3c8a-82d3-942eb6ed443b | -11.13757 | -54.02137 | 2026-09-20 12:06:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 07673cb5-3d1e-382d-bab3-9e7de1f5bc99 | -12.16914 | -47.04556 | 2026-09-20 12:06:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| bbc5385d-688c-371b-996d-3dfd5bdd1353 | -11.05353 | -54.91029 | 2026-09-20 12:06:00 | TERRA_M-T | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 4ee3938e-12e9-33f4-a4ec-763db4c8dc09 | -10.28694 | -50.20976 | 2026-09-20 12:06:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 3c551af1-d69d-33c0-bf4e-295607d0a0eb | -11.66401 | -43.4188 | 2026-09-20 12:06:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 066f11fa-e530-38af-a66e-1d65c5ae976c | -11.87679 | -50.00301 | 2026-09-20 12:06:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| f72be885-2b17-3984-b954-adca49174544 | -14.05585 | -52.07116 | 2026-09-20 12:06:00 | TERRA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 368d229e-3621-3374-9853-30dda1c322fb | -12.1419 | -47.05753 | 2026-09-20 12:06:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 40.7 |
| e5f9f76f-8c4a-3da4-ad16-43638fc9e994 | -10.92442 | -48.32051 | 2026-09-20 12:06:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 27.0 |
| cceaf726-d9be-3131-9a8a-7e4ed5076809 | -12.90176 | -50.99048 | 2026-09-20 12:06:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| eba35d57-211d-339b-9456-16a565a6536c | -11.04974 | -54.17817 | 2026-09-20 12:06:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 772d0e99-f618-3c3e-8f8c-78102e4df8be | -12.31339 | -50.72264 | 2026-09-20 12:06:00 | TERRA_M-T | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 16.6 |
| c49098a4-a6c9-324e-ae02-423b07c877e6 | -14.67167 | -46.68948 | 2026-09-20 12:06:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 926.6 |
| 12946764-7de1-30d1-86fb-0f63dc9d3f65 | -11.05069 | -54.9293 | 2026-09-20 12:06:00 | TERRA_M-T | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 8d28ac6b-2457-34f6-b5f6-6b7450b77767 | -12.16684 | -47.06587 | 2026-09-20 12:06:00 | TERRA_M-T | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 5c488492-96ff-3aef-8b2f-8e3d8983ee1f | -12.48209 | -50.05087 | 2026-09-20 12:06:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b160bcfe-094e-3314-a878-fb5886dc91b4 | -10.87394 | -50.18097 | 2026-09-20 12:06:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 33.0 |
| ae0ecb52-4e31-3fec-9582-a13902b1043b | -12.64585 | -50.91519 | 2026-09-20 12:06:00 | TERRA_M-T | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 6584cc7d-6bc3-3480-ab97-9f12b30c2070 | -10.92711 | -53.95071 | 2026-09-20 12:06:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| a5460e7a-50f7-361a-8812-dfab06778eef | -10.87247 | -50.1924 | 2026-09-20 12:06:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 36662383-99ba-3724-a81d-a6e1da448555 | -11.86073 | -47.66965 | 2026-09-20 12:06:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 33.9 |
| bc89f028-be33-3edf-b229-dee436d6058f | -10.41105 | -48.93898 | 2026-09-20 12:06:00 | TERRA_M-T | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| b69f5e12-1c05-3621-b527-b86f39d3e394 | -13.25439 | -51.73164 | 2026-09-20 12:06:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 5ab46920-3e04-337c-bef1-f68e493427c0 | -12.75753 | -46.17163 | 2026-09-20 12:06:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 55dfc4af-f7e9-38c3-8089-c83687f87a3d | -10.48611 | -51.31562 | 2026-09-20 12:06:00 | TERRA_M-T | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 321884b5-2c25-323d-af46-5e4b8946d6d7 | -10.78316 | -46.32779 | 2026-09-20 12:06:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 87239ee0-a006-3587-9020-ef42760d1c39 | -10.86213 | -50.18497 | 2026-09-20 12:06:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 33.9 |
| e7351a54-a2cc-3b4f-881b-c218abf30cad | -12.33734 | -50.69183 | 2026-09-20 12:06:00 | TERRA_M-T | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 4e9ac7d7-a666-3073-a7a3-110abd07f477 | -11.11986 | -54.01879 | 2026-09-20 12:06:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| cf751775-4549-3252-8557-cda3c57d52bf | -11.13888 | -54.01233 | 2026-09-20 12:06:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 8db61481-02fe-3ddb-a2eb-c7454925b85f | -11.09065 | -54.033 | 2026-09-20 12:06:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 9b9a3cc6-a9ca-3f5e-94fe-cd14b72e7349 | -10.87867 | -54.08506 | 2026-09-20 12:06:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| cbf491cd-ad2d-3301-ad50-06e85477ae81 | -11.95677 | -50.09358 | 2026-09-20 12:06:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 4f777b8f-8fed-39b3-8fa4-8a7392fd001f | -10.48749 | -51.30548 | 2026-09-20 12:06:00 | TERRA_M-T | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| fb456d4d-edd4-3e21-8acc-dfeb2e4eb157 | -13.01797 | -46.90561 | 2026-09-20 12:06:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 03b7615a-72c1-304f-956d-9baa752022f5 | -10.79225 | -46.33424 | 2026-09-20 12:06:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 610207d9-ae93-31d2-b7ad-4462833e531c | -11.04304 | -54.91841 | 2026-09-20 12:06:00 | TERRA_M-T | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 9adfb7a7-94ca-36c7-bc42-2c88f54f97b5 | -11.09196 | -54.02397 | 2026-09-20 12:06:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 423421c0-a008-3a99-97b2-02a0c0007d66 | -11.84988 | -46.87932 | 2026-09-20 12:06:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 8cce31aa-b6cd-30a2-b14c-23f4fd1e3f99 | -10.39292 | -48.9087 | 2026-09-20 12:06:00 | TERRA_M-T | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| bc7a8d91-7864-315e-a7b2-3743dd717658 | -11.49067 | -45.3662 | 2026-09-20 12:06:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 68f034db-3a80-3850-9483-754ecb764128 | -11.05211 | -54.9198 | 2026-09-20 12:06:00 | TERRA_M-T | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 081fef03-38fa-3592-ba6d-fd284bb5aeeb | -11.37397 | -51.41663 | 2026-09-20 12:06:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| b456dbca-6606-3ac2-8f50-f31453e7512e | -12.75719 | -46.22831 | 2026-09-20 12:06:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 5bb6ebfa-bb13-3633-bcdb-26116975a1a0 | -12.50639 | -50.95061 | 2026-09-20 12:06:00 | TERRA_M-T | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ae67988f-9820-3a7f-bd00-86a319926751 | -17.56775 | -44.98968 | 2026-09-20 12:06:00 | TERRA_M-T | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 39.5 |
| 91fd1f46-4a48-364e-b984-24071a4a6fcd | -10.32896 | -50.20981 | 2026-09-20 12:06:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 465bf638-127b-3181-ba67-ebb088bc7a10 | -12.02639 | -47.81238 | 2026-09-20 12:06:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 45.2 |
| f886d168-d878-3bc2-8a8c-6e4f5c170f4c | -13.95339 | -47.83977 | 2026-09-20 12:06:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 19.5 |
| b8e7415a-3f39-3dad-b04d-a9806ff38e9c | -10.473 | -51.27332 | 2026-09-20 12:06:00 | TERRA_M-T | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 80ebf20c-8122-3323-8a32-8f6a8338cde5 | -14.05451 | -52.08117 | 2026-09-20 12:06:00 | TERRA_M-T | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e4f045c9-f551-3cd7-b588-2995a8079631 | -14.67437 | -46.66555 | 2026-09-20 12:06:00 | TERRA_M-T | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 130.3 |
| a8e9b00d-1019-3d35-9a7a-b400a4335367 | -14.92749 | -49.90808 | 2026-09-20 12:06:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| ce3b75d7-0031-36ec-9891-5dbe7fbec2d9 | -11.10214 | -54.01623 | 2026-09-20 12:06:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 14.4 |
| d99ae98b-b74e-38db-ac60-12160db0866f | -12.23546 | -50.14828 | 2026-09-20 12:06:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 0d3a7ff1-af4c-32e7-819f-990f4bb94a85 | -10.3934 | -48.99214 | 2026-09-20 12:06:00 | TERRA_M-T | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| bcbf0951-6b6c-36bd-890b-f3ff76481ab3 | -11.85167 | -46.87393 | 2026-09-20 12:06:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 22.4 |
| e9882209-7084-3dc6-9546-d43ff7e828d0 | -11.24789 | -48.38584 | 2026-09-20 12:06:00 | TERRA_M-T | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| eaf080e0-f44e-319b-bbfd-e0ae8ee7778b | -11.31866 | -47.28163 | 2026-09-20 12:06:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 5b269052-610c-3eaa-84ef-da1ec2a1e631 | -11.99626 | -50.01847 | 2026-09-20 12:06:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 1569289b-ebf0-33db-80bf-b13692e623da | -12.7546 | -46.19627 | 2026-09-20 12:06:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 6a275ae6-9a68-30d8-afea-f8705cca8e0e | -10.91564 | -53.96744 | 2026-09-20 12:06:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 18.7 |
| ee1f0798-ec4c-34d6-ba22-2991294c5302 | -11.92815 | -49.77096 | 2026-09-20 12:06:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| ef5e0695-54b4-30a9-92c9-ef1c1719a74b | -11.47679 | -51.47723 | 2026-09-20 12:06:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c90ce407-2bb4-3e47-9257-2647269eaf89 | -11.39119 | -51.42913 | 2026-09-20 12:06:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |


[Clique aqui para ver as próximas entradas](README112.md)
