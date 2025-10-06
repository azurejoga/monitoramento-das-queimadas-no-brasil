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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 60d6db41-a113-325a-b7d5-bb25031bb915 | -11.95148 | -51.47441 | 2025-10-06 04:27:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b8c8c9f3-5b97-3d36-9f0f-0f0d5a50ced3 | -10.40058 | -51.59232 | 2025-10-06 04:27:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 042e1b5c-a755-3fad-a18e-6dcc9911b772 | -15.99617 | -50.85368 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c47a41c6-3190-346e-af0b-498cfdd5ac07 | -14.75261 | -54.68539 | 2025-10-06 04:27:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| adc0bd6c-c669-31ee-88ce-8f7a999b6f73 | -14.93602 | -47.12928 | 2025-10-06 04:27:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d7668f6c-06e5-3f76-be54-7256e036e720 | -11.70808 | -45.40972 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b011cb2-086f-315a-b87c-135b2e02999c | -13.10408 | -47.92057 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1add50e4-13c9-376c-a593-340ac2389d05 | -12.57669 | -46.73487 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f9563b00-26f4-3522-b971-826462019162 | -8.8831 | -50.78781 | 2025-10-06 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 897c0630-41fe-3335-85f0-fd879a3275be | -11.91534 | -46.2304 | 2025-10-06 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6f44373f-4a3c-3a67-b47b-9944fe02d882 | -14.69376 | -48.28398 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f90feeba-e221-3c97-b964-7a19e8fec444 | -14.91845 | -46.86488 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b51209c-e9cb-35b1-b3de-57b49b26b003 | -15.21544 | -56.82365 | 2025-10-06 04:27:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 929c95e0-f5f3-38eb-a6ba-0f10d32ef0f2 | -15.29017 | -46.3225 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c612b19-0d6a-30d0-b2aa-dcbfff036e58 | -14.6546 | -48.36102 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fcc01d78-0757-35ad-9de9-81f41d9775f7 | -14.55958 | -46.65822 | 2025-10-06 04:27:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4d8323d1-58bd-3d26-bb67-99dd5b6eecd9 | -11.52735 | -47.6883 | 2025-10-06 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63666d98-b096-3615-8356-1d888dc911f0 | -15.58149 | -52.43749 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| df4e94f5-4a5c-3721-a804-bc5ffb797699 | -13.2646 | -47.84935 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 621fb97a-8211-3c37-9674-3f85e2d1c989 | -14.89975 | -51.50336 | 2025-10-06 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 2c18da75-1786-39de-b05c-86862e88d3ee | -13.62022 | -48.70212 | 2025-10-06 04:27:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78c7173f-195e-36d9-96eb-46d077295e20 | -11.90807 | -46.21793 | 2025-10-06 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29528646-e765-3582-9dcd-3732635b4969 | -13.34539 | -48.05059 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7e57623f-04f8-3b2c-a857-4a13718a0b26 | -10.19008 | -45.52921 | 2025-10-06 04:27:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 6.3 |
| cd375a53-dba2-347a-a2d1-f7dda3acf755 | -13.09142 | -47.87171 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0742dcc2-1efb-316e-81c5-08e4f73f3b69 | -13.11388 | -48.0088 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78bee53f-9bcd-311c-ad6f-5b00fb0dd17f | -11.80346 | -45.1204 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 39df7f14-69af-31a1-822e-b3ae8686999f | -15.92895 | -48.6099 | 2025-10-06 04:27:00 | NOAA-21 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4aa178c-d7e6-34bc-9560-7a3f538bff0a | -13.2813 | -47.17209 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3fd11184-326c-33d0-8040-900725c3eb01 | -12.4839 | -45.54011 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53842889-ed1f-39b1-ad1a-ffa2f7bea584 | -10.37533 | -48.14921 | 2025-10-06 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f0c25aa-489e-3182-bc45-1a57ca9b1e9b | -9.97021 | -48.74686 | 2025-10-06 04:27:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 315a395e-d074-3722-8c2c-377ee45bbc4d | -13.17287 | -50.86297 | 2025-10-06 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7262dc8-bd71-3d08-9577-9b68c1c1df26 | -11.44897 | -44.95201 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b51d4b4b-f1fe-32bc-83fd-e802ff79bbb9 | -9.04365 | -50.69509 | 2025-10-06 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 704b2ce2-3225-3056-92e8-7814d94f5fa1 | -9.25799 | -51.80928 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5a46ffe7-fb06-3b12-93f2-8f221131db9b | -8.61575 | -54.99189 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d645b9ca-a39a-3264-8c9f-608433d503c0 | -11.80234 | -45.12803 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e7ce9a20-f054-3e3e-93cc-a5da8c355713 | -13.30908 | -48.06633 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09f03a69-180e-3dda-9ad6-ecb15e619edd | -9.24043 | -51.81693 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3262200a-e45a-3648-b06e-2ca20a939447 | -14.69474 | -48.364 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59cada94-6f40-3466-a6cf-769917fc007c | -14.46837 | -46.33467 | 2025-10-06 04:27:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d09857f-07c3-3294-9554-55521b901874 | -15.51049 | -46.84037 | 2025-10-06 04:27:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ed0d16c-1645-305c-8e17-1753973261c6 | -11.48075 | -59.09342 | 2025-10-06 04:27:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75f22d37-7a14-344d-b77d-b0b168c7fdf6 | -10.61881 | -46.35441 | 2025-10-06 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8bdda4e8-8157-3553-9249-014e59e5d986 | -11.7495 | -51.51477 | 2025-10-06 04:27:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 199697b6-750b-3b70-b97f-c6ebd084d3af | -10.47652 | -50.44728 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2ebe0ac0-eb07-30f5-8b18-0b9f8c714a53 | -13.08044 | -47.94196 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 537c6b47-2ea2-30de-b367-e82b1bd4d868 | -15.28838 | -46.31092 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8296d339-de14-3bf9-b4ca-4f0ca5e665d7 | -16.05344 | -50.93673 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| edc1f566-2bed-31e1-8ff5-7c675521f9c8 | -15.99461 | -50.92628 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2684bb1e-e82d-3feb-891f-608bf0cf6d14 | -14.6398 | -48.32591 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba9bfb5d-cd72-346a-b5c4-7c527b1594b2 | -9.25404 | -51.80857 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 972006c8-592c-3c21-be7d-faa839419d58 | -13.27554 | -47.62738 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a32d3670-1762-3fb8-9acd-01c4ec9b4a2c | -14.63645 | -52.54093 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2ab08c59-76bd-3082-b7d6-eed27fe01090 | -12.91552 | -47.29454 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c12fadc-c97f-3b81-88db-58a2261f52c4 | -13.11006 | -47.9901 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 997a767c-2e25-3262-95d7-29e7c0e97e77 | -12.61506 | -49.15204 | 2025-10-06 04:27:00 | NOAA-21 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4cf4ad2d-b33e-3148-9d7a-f0b25ad6080b | -14.67216 | -48.37843 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 32228833-bc7a-3d1d-9810-a3dc50f9ae00 | -10.67135 | -48.47149 | 2025-10-06 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 586ca127-a8de-398c-b135-59e17b3d9912 | -11.95226 | -51.46989 | 2025-10-06 04:27:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3b075c58-ef75-30e2-9832-2b153449c5c8 | -14.34417 | -47.71122 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3af0af9-d31a-375f-9e98-6ad4d71343a1 | -15.24222 | -46.67246 | 2025-10-06 04:27:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69b9aa6d-e718-3b1a-9e35-ac17ca1de3b3 | -11.06945 | -47.91545 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b8092dae-6486-3ad3-ab9e-447c938a03e1 | -9.32942 | -54.52171 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f8b8b04-5937-3bba-aec4-2baaac1d4ad7 | -14.28251 | -45.86133 | 2025-10-06 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96ea0907-8a3c-389e-8b04-d8c3ed407a48 | -9.44139 | -49.23672 | 2025-10-06 04:27:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aaedf07c-0ee8-3bfc-9dd4-69a202489d9f | -13.25877 | -47.23014 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1ef58b8-4728-3f01-aa76-dec26a200460 | -12.48852 | -45.5565 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.5 |
| d9964079-44fe-3734-b731-40c6eabefd4b | -13.72273 | -48.07645 | 2025-10-06 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a97db888-3e21-3207-a3ed-2e9791113814 | -11.49895 | -44.97598 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 182cc433-3aae-36e1-89eb-b3c64232cc19 | -9.95554 | -48.7519 | 2025-10-06 04:27:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b97ebe5-d9a4-394e-b6e3-221d26a553d7 | -8.63191 | -51.08077 | 2025-10-06 04:27:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3c7c10b3-4dad-3f4b-9c8d-ec40b1a2c7a9 | -17.07684 | -43.38333 | 2025-10-06 04:27:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed343c25-c579-3622-97c0-9f0423a86caf | -12.4202 | -51.10909 | 2025-10-06 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 299931b5-3df9-3986-a5e9-91ecfc296c9d | -14.91003 | -46.85224 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 35d65784-87ec-32bc-8482-b26dbb8b5dec | -13.61144 | -48.69329 | 2025-10-06 04:27:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 108f9d74-3097-30e2-a136-7f9b9729847a | -12.18883 | -51.42929 | 2025-10-06 04:27:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab6e168f-4285-3625-b7da-8cca51e7dfd5 | -15.20822 | -56.8076 | 2025-10-06 04:27:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 78d2e3eb-ada6-32e8-996c-63073cf37cc9 | -15.58731 | -52.44846 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4cce8d60-596b-37ee-b3d0-68c67e1f4e97 | -15.16176 | -45.75918 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5b8cb7c-dedf-35f5-8e1d-d144c15f2679 | -15.18803 | -56.83215 | 2025-10-06 04:27:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 015e2c79-cea6-34ff-9f9c-76271fde4085 | -11.83484 | -45.10059 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bdd28a3-435b-3586-8a73-1005b5c8c557 | -12.9086 | -54.73903 | 2025-10-06 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 40b27944-2d92-312d-b910-25d62e3096e6 | -15.23547 | -50.07924 | 2025-10-06 04:27:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 715a0cfc-90dd-3241-a7cb-5c7b7fdf48d5 | -16.03781 | -50.96636 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f36ab284-3439-38bb-9c34-e1858a95ec40 | -15.18583 | -52.7658 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d00d833e-349e-3afe-8acc-18ddcfd8342a | -12.44701 | -45.55481 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1162899-acbe-3cf0-bee9-b9423a3a7962 | -11.64485 | -47.02216 | 2025-10-06 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 98030a55-3694-394f-8334-8a3bcc5e7132 | -16.06503 | -47.77456 | 2025-10-06 04:27:00 | NOAA-21 | CIDADE OCIDENTAL | GOIÁS | Brasil | 5205497 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 63b52fb9-871d-3798-84c9-93099bf49aa6 | -11.82804 | -48.87619 | 2025-10-06 04:27:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| afbac65a-4cba-3e1d-a00f-e3cc286b9491 | -9.26609 | -51.80311 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc857db2-b62f-3888-93ec-c345a9b3d27e | -9.67518 | -48.3975 | 2025-10-06 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bf62aa32-699a-303f-bccd-8875ca6f0391 | -10.28762 | -50.28195 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 675e4701-9b55-3af4-b3a4-e134c5e4da78 | -11.04812 | -47.77186 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f13085d-3da3-38c1-843b-65e084ff6117 | -11.02037 | -46.52966 | 2025-10-06 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90f9dbd5-2477-31ba-93a6-45dd91416a6f | -11.87378 | -57.81552 | 2025-10-06 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 545878f8-3d2c-3121-971c-3faeb5c4dc52 | -11.22762 | -47.77555 | 2025-10-06 04:27:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 231214d5-e2c6-3e22-8588-32b1b8a0ebd4 | -13.26865 | -48.47238 | 2025-10-06 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8df700fd-ccdf-327e-b182-c461c7199ba0 | -12.92833 | -46.8125 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README43.md)
