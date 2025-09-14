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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed0543d8-32ed-366a-8dbf-d86d341425d8 | -13.89827 | -48.30201 | 2025-09-14 05:08:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d134f5ca-318f-39e2-8d47-2b7db8ec0d6e | -12.78228 | -48.03719 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 518e3e5d-85d6-38c9-8fd4-13e7738e5423 | -14.3159 | -46.08506 | 2025-09-14 05:08:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dd804dda-29b2-324d-9b2a-031e848a7c58 | -12.79374 | -47.13987 | 2025-09-14 05:08:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cfd96b95-2f05-35da-a3f4-a7a53522dba9 | -11.24449 | -44.76927 | 2025-09-14 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98b22c24-6181-33fd-878d-71ee431f15be | -13.93951 | -44.8289 | 2025-09-14 05:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 32520314-ff54-39f1-8827-b2603ae9650e | -13.00669 | -47.98064 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60c21346-61ef-3fe8-864c-ec3d80d8b44f | -14.63073 | -46.37036 | 2025-09-14 05:08:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a805979d-e4ca-32c0-82ce-e8effbdd059a | -12.80167 | -47.96656 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d563059a-0197-3d39-bbc5-bd410d148f31 | -12.96854 | -48.04532 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 042982b9-d08a-3228-a8b7-1f093df2a479 | -11.25605 | -44.77568 | 2025-09-14 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 9b331077-0597-395a-bc3f-48c974878670 | -14.17716 | -46.15891 | 2025-09-14 05:08:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4ee0098e-46a5-3f5d-abc7-6fe01964db84 | -11.37546 | -47.342 | 2025-09-14 05:08:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a3175815-b9b1-3dc7-97f5-7f2a875a97b3 | -12.77927 | -48.03376 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 12a3cef5-aa61-34fa-96fc-0015c24165ee | -13.91157 | -48.30677 | 2025-09-14 05:08:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9923e8a8-3b36-3dfe-b710-8b172ab6ab85 | -12.97135 | -48.04874 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 64d5b295-adb2-3139-bf01-e779a864c762 | -14.18945 | -46.16031 | 2025-09-14 05:08:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 986ad204-98c7-3d17-8730-0d312b5c764a | -12.08284 | -44.72952 | 2025-09-14 05:08:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0466aa41-9772-329d-9896-e6d5de5294a5 | -12.76868 | -48.01477 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b6727e7-f93a-39a7-9d3c-54f3eea585ee | -11.39842 | -50.4499 | 2025-09-14 05:08:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61b36cd7-8f66-3ec4-b8f8-51538e66fdcc | -14.15438 | -46.2545 | 2025-09-14 05:08:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| be258df0-96a2-32c8-8495-c329bcddaf56 | -12.69419 | -54.69734 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7cd6d838-25df-3d9a-8319-b800dff6f31b | -11.89472 | -50.54048 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| dd96bcd9-a298-3e74-8b52-55640d0f2ff9 | -10.97268 | -49.59594 | 2025-09-14 05:08:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ef1a59d-ab50-348b-a265-f4c56525be16 | -12.87179 | -52.96077 | 2025-09-14 05:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d51b3bf7-c4fd-33ba-87a6-c914f0ceb9e9 | -8.77041 | -46.04319 | 2025-09-14 05:08:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 69caa6f6-0bb4-3971-a624-7adcdcb9385b | -10.76264 | -44.78385 | 2025-09-14 05:08:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18c2b05f-d16e-3876-b6f0-cbe46bd21b5c | -7.38914 | -49.98323 | 2025-09-14 05:08:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b00bde1-3477-3ef4-a852-e388936c9968 | -12.93308 | -54.73573 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c9a3536a-24ee-337d-995c-5654a6617e92 | -8.93689 | -46.16055 | 2025-09-14 05:08:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75a87460-ccdb-30f5-8bd5-bd5c6c052ccd | -13.93713 | -44.85108 | 2025-09-14 05:08:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 21.1 |
| eb7c628a-e9f9-31f3-805e-a838db7bc310 | -10.89764 | -45.57244 | 2025-09-14 05:08:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7be99bd-9a70-3515-8709-3b880d19d85a | -11.86122 | -50.48612 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 80176827-84fc-3aae-b953-01ade11dee0b | -11.45343 | -50.79233 | 2025-09-14 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88da7149-dac0-3837-8807-6975f0824d68 | -7.71144 | -55.45378 | 2025-09-14 05:08:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3133d886-fd64-3263-b429-6635574dc20d | -10.34191 | -48.83066 | 2025-09-14 05:08:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 119c3fa3-ee46-31e0-b0dc-3a08fae15173 | -11.78516 | -46.62614 | 2025-09-14 05:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 16440fe9-92c0-35cb-b1ca-80572f7ee34b | -10.90025 | -47.21157 | 2025-09-14 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 57e96d8a-6206-378f-9259-8e128331c927 | -12.86186 | -62.14751 | 2025-09-14 05:08:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d08c94c-2eca-37c9-9fcb-6678cc2e35c1 | -8.76983 | -46.04773 | 2025-09-14 05:08:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d20df0af-5fb4-398d-b541-6460c0622356 | -12.68537 | -54.70827 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ce8a32f7-21a9-3931-bf7c-b2f2cdad545c | -12.92054 | -47.94804 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dbd3b10c-32e7-3f2a-b764-7330d1a9ee1c | -12.93338 | -54.73458 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7bb52720-1ae5-3d8c-99cd-0765b65fec9f | -11.16143 | -57.18258 | 2025-09-14 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c57c867-adfd-3bbc-b9d6-d82fc5691b1e | -15.6372 | -44.37558 | 2025-09-14 05:08:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1911f34-180c-3b2a-b673-af2e8563c785 | -12.7752 | -48.00565 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2eb71142-3d2c-3b41-a3b8-96b178e38469 | -12.08218 | -44.72983 | 2025-09-14 05:08:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 871eff13-87fb-3b0a-980d-5fef2310f6f0 | -8.77009 | -46.04002 | 2025-09-14 05:08:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1482fcc-c98e-32cc-9ed6-9c55bba965f6 | -12.94631 | -54.74469 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8b9937b5-38c6-3254-84b2-d13c8982ccc7 | -12.45303 | -57.7866 | 2025-09-14 05:08:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| fbe7df6f-3f80-3b54-966b-c3de3994493e | -12.69771 | -54.69786 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 379e871c-64c2-389b-8d63-f86568ae1e16 | -12.69951 | -54.68586 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 2e553533-3623-3ded-a345-f2e06253ecfd | -12.77521 | -48.02302 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 404a1050-5448-3929-b4ed-a33749778626 | -10.75625 | -44.78283 | 2025-09-14 05:08:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f0124531-bc50-3676-a4ff-de02143e8be8 | -12.70529 | -54.71935 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 527fad2a-2b59-3e8b-a20e-1dc7616e5fef | -11.85676 | -50.48549 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 4a157f50-9979-3d60-8809-15b36f49ad3e | -12.91591 | -54.80215 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6fe5e19c-69f3-3d99-bf70-31d7eb8d70ce | -11.28902 | -51.10285 | 2025-09-14 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ece4fae2-0281-300b-808b-01f754103164 | -11.1581 | -57.18204 | 2025-09-14 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62389cfe-9df6-3c55-af50-92442e9e0c1d | -10.74348 | -46.44326 | 2025-09-14 05:08:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d93f9ea-3da5-3fcc-9b3c-784a30d505d4 | -12.70064 | -54.70238 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 9dfd5217-9953-3a28-b4d0-9fc0257ec563 | -12.75596 | -48.00329 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 570fca9c-023a-3454-85a4-f48091e9cecc | -12.93035 | -47.95727 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2bd7304c-d240-3219-9be2-53ed19cddc9e | -12.7366 | -48.02776 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df92ccfa-e25f-3ab5-8680-989b86f98881 | -12.7802 | -47.98363 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 355f1181-bad7-38cd-a538-f6de4358bd1f | -12.67427 | -54.68611 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 378c589c-ef43-3592-bc1a-257a0abee795 | -12.97366 | -48.0044 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b673e10d-3895-3c91-b7ae-56a084e37f94 | -12.94043 | -54.73565 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 9d4879a7-7ad8-3e5e-9fae-3b64d25b16a2 | -12.04121 | -46.54839 | 2025-09-14 05:08:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 06b520f8-1e96-31f8-8cd8-a50a99336211 | -12.94279 | -54.74416 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8ef42cf1-c07e-3c6c-be40-c66d912fa7d2 | -11.77964 | -46.62579 | 2025-09-14 05:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 66d40e1c-7c23-3e2e-b059-428c181615da | -11.27787 | -50.83704 | 2025-09-14 05:08:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5556eb02-75ba-3b21-b879-2fb9ef4ae92a | -12.77563 | -48.0197 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c3827b0e-ce3a-3eec-8911-9f851a09bde7 | -11.85617 | -50.48994 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 7c80e1af-43e7-37c5-a201-2983cf7d8f13 | -12.80826 | -47.9571 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 87d9b5b7-4de5-3fed-a839-b8c144aa778b | -14.20629 | -46.17674 | 2025-09-14 05:08:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73274546-b5f7-3f36-88c0-045c8ff79bff | -10.32298 | -48.82305 | 2025-09-14 05:08:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 90ae68a0-313e-3e94-b1b1-c6a042d470b3 | -12.08871 | -44.73065 | 2025-09-14 05:08:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 293bb4a8-d866-3ac0-b1f4-611e8fcd283f | -12.93927 | -54.74363 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2cbd83b7-b6f0-3287-8e2d-d86babf58d2c | -12.78631 | -47.97836 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 03de038a-d30d-3d64-a7ad-690d33fb3442 | -12.67952 | -54.69921 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| dd065553-a7f4-32eb-b663-8c8c7206fc65 | -10.76322 | -44.77893 | 2025-09-14 05:08:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5d586bb-ce83-3f04-8b7e-ddb780a6107c | -8.17232 | -46.77862 | 2025-09-14 05:08:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b258db13-b465-37da-a346-c757f33a2f55 | -10.93181 | -47.35641 | 2025-09-14 05:08:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 283f7dc9-049c-36da-8f14-db40e7ff1556 | -12.94795 | -48.036 | 2025-09-14 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8da15000-532b-3eee-82c8-f3c2ade9a4b2 | -12.12234 | -44.84369 | 2025-09-14 05:08:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d55d37c-05e1-347a-bf8c-9538e8e37fdb | -12.85289 | -52.98274 | 2025-09-14 05:08:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f07e6511-024b-3ece-a62c-801d1af6f8fc | -13.88912 | -48.24408 | 2025-09-14 05:08:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05e8fc4d-43e2-35e0-aa0b-4652f86b44a7 | -12.66137 | -54.67598 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96ee06ac-59bc-3f3f-9bd9-0aae2ade567d | -12.693 | -54.70534 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| eb444ed3-4096-3b73-af6d-d6ebc827ac65 | -12.68835 | -54.68827 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 185b1fa4-c225-3108-96d3-e57a019f678c | -14.33154 | -46.61802 | 2025-09-14 05:08:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88c55fd6-c347-36b2-9ddb-bf2e6ce3811b | -12.69241 | -54.70931 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 67bb4d41-311f-3df6-b467-99a8da15853e | -10.60032 | -44.33914 | 2025-09-14 05:08:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| adff8b1d-abea-31dc-973b-4104ece03c50 | -12.9165 | -54.7982 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9eadc54e-26de-3c0b-9301-a0184908c1e8 | -12.93691 | -54.73513 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 17d86e02-ba63-3a08-80dc-f45d4ae5db1a | -11.86972 | -46.75857 | 2025-09-14 05:08:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 83e8c43e-8532-3af1-b7e8-a7a2dd9c02a2 | -12.06944 | -45.63382 | 2025-09-14 05:08:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 11c2f5d0-7350-3d6b-948d-6e1ffb728cce | -12.67253 | -54.67359 | 2025-09-14 05:08:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d268b8a2-4ea6-352e-873e-b4372ee0c01b | -11.82014 | -50.49961 | 2025-09-14 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README55.md)
