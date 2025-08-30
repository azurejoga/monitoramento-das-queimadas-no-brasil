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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce8a0d38-ef0b-37d8-9589-fceb7fed1e5e | -9.31852 | -56.90128 | 2025-08-30 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6803460b-97b9-3d3f-8ae0-56affc2dbb94 | -10.84092 | -53.7729 | 2025-08-30 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be3d94ab-0f9b-3f3b-a67c-f858a3927699 | -9.44937 | -60.53972 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5ddbbcfc-73e3-3f59-a31e-d6762f715ba2 | -7.15206 | -44.91356 | 2025-08-30 05:10:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 030fa258-f9e0-3592-9488-065c7dc5b536 | -8.34516 | -62.93296 | 2025-08-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ba4addd-01d1-33ca-915c-155347c934fd | -5.43004 | -45.52016 | 2025-08-30 05:10:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d027284e-ba2c-324a-ba34-475a84a57724 | -9.4509 | -62.36536 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e6a7c10-803f-32e1-8fab-60e29a07b255 | -11.21725 | -55.05865 | 2025-08-30 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a51a09e9-3815-3a29-aa0d-b9deb2143f11 | -9.32076 | -56.90898 | 2025-08-30 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d001ec6d-3765-31d2-8d29-04bc05609ad2 | -7.11718 | -44.58897 | 2025-08-30 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6077723a-ef58-322e-bb76-2eb119fa6caf | -7.62518 | -60.85291 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6220b1a5-62e4-38cc-8a48-f377a4e70232 | -9.43881 | -62.3437 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 83cd4420-895a-33d1-9537-f2608731485a | -9.46331 | -62.33813 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 891a3bea-83f7-35d1-863a-573c6363e93e | -9.44537 | -60.55554 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 57fd8e28-1547-3cac-bd96-d9df235d82c6 | -9.24157 | -59.77698 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df62e75e-bf42-3b14-b672-2e1d3db07e23 | -9.27835 | -60.45319 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd6bbdfb-8bf5-33ce-a5c4-9c16638e375d | -7.39313 | -45.92889 | 2025-08-30 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4445a796-b37c-3bcf-bf4f-9cb6e184e52b | -8.67103 | -62.43385 | 2025-08-30 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1602575-64e1-3488-b822-c24c4d404a83 | -9.45012 | -60.54834 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d89fb4b2-d113-3a87-ba18-dfd2caa132f9 | -9.69156 | -48.31433 | 2025-08-30 05:10:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a61e7145-25af-3bdd-aa20-938d24b54867 | -8.88444 | -60.72937 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 553cf64f-18c5-3536-a90c-1e69c1cf7c79 | -11.00437 | -46.86307 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e4d407f7-bd4c-3ce3-bd1e-d909db0e90ca | -9.08282 | -59.48455 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4b1a2990-f71a-3f1d-9965-588e2297ca39 | -9.45527 | -60.56881 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5fed313e-ce07-3e60-bae2-a321659efe51 | -11.82929 | -46.46348 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 392cc325-3b0d-3313-bbf8-90e371ad7039 | -7.89763 | -63.01087 | 2025-08-30 05:10:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c501cf12-3232-3b8d-8d51-d4b0e5ee6fd6 | -11.83333 | -46.86475 | 2025-08-30 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fe32407b-a58d-38f3-b0f4-f20f2962f7dd | -11.87191 | -46.38319 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2f67c052-f017-373b-800a-a9fbd112eff8 | -10.3785 | -57.83584 | 2025-08-30 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2b359e2b-d060-34d4-b5d5-ceefe7e52c52 | -5.69453 | -45.96544 | 2025-08-30 05:10:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0f50c1b1-f38c-34c4-95e9-10a0f0cb4db7 | -9.32021 | -56.91256 | 2025-08-30 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59dacc67-902d-31c2-81b5-07ccce792855 | -8.95741 | -65.96922 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6fb120fb-8aee-3156-ae89-ed42c4184480 | -9.45633 | -60.5409 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0448622f-2629-3a0f-8ae1-d54a0fba6725 | -9.32187 | -56.90181 | 2025-08-30 05:10:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d1515e73-44ca-3c2b-afbf-f253e6ab5765 | -8.87738 | -60.7282 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e5bfad4e-b7ca-3a9b-a63a-03663ec213bd | -11.88552 | -46.72182 | 2025-08-30 05:10:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5107578e-d9ee-3b3f-9d72-fe77b3f1fad4 | -11.15182 | -47.14089 | 2025-08-30 05:10:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 6da43c15-3704-343a-a61a-1a70e31c4da1 | -9.12437 | -65.81155 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34531560-c019-3841-a3e1-49add4b6484e | -5.82655 | -46.35792 | 2025-08-30 05:10:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fd8fc0c4-578b-3860-893b-a660872f9079 | -11.86433 | -46.39223 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aca18c4c-4930-3d58-84da-a82e7087d134 | -10.37673 | -59.39195 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ca5b84a-0935-307e-aa5f-0fa4591f7b4b | -9.56993 | -55.38718 | 2025-08-30 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f84fefb5-1faf-3aef-9e51-ae000ddce472 | -9.17242 | -59.5813 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a93e65fe-d017-31c2-8acb-dd9b6d4edb5f | -7.90171 | -63.01157 | 2025-08-30 05:10:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6d6c25de-816d-3de5-9c82-14aa5ffeaa1c | -6.80208 | -59.96635 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e1da5fa6-e3ce-3f1e-b3bb-b03b80dbc46b | -7.76034 | -45.46505 | 2025-08-30 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 763c6e07-4bc9-34d5-8302-2d5d1d527461 | -11.84468 | -46.38773 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 89137b18-9651-3906-a045-21c27a8504f8 | -9.95659 | -46.35307 | 2025-08-30 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 10e079da-5b77-3e6b-acf0-86cc812664d3 | -9.61859 | -45.96764 | 2025-08-30 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 025fca05-bedf-3a01-bc6d-e67495469cb1 | -6.09216 | -43.99931 | 2025-08-30 05:10:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 82618563-dca6-354d-bc8c-6610dffaff81 | -9.95712 | -46.34852 | 2025-08-30 05:10:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2aa4a4a8-7054-3d94-8a57-a3e392037ea5 | -6.07728 | -57.93132 | 2025-08-30 05:10:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0abf4c27-e9b3-3133-9690-c0002822827f | -9.44201 | -62.3247 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 118e2112-bc37-3374-abb8-fa82242337a0 | -9.24438 | -59.78123 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b1ba8f3-040d-33f1-8cb8-5d4731ebd794 | -11.87807 | -46.38685 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c3dba9e8-641d-326c-824b-03e7b1e47ae7 | -11.8714 | -46.38777 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 595e9c1f-d207-3edc-b453-5a1ba54cb931 | -5.82222 | -46.35936 | 2025-08-30 05:10:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3c2da06e-4b6a-3362-814b-9c5d510255ef | -9.44188 | -60.55497 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| af38a6bf-a5db-3e05-82c0-b7adcdebb9db | -9.43943 | -62.36338 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 235dda6f-a0be-381d-9ffe-92b0ed217f70 | -9.44093 | -60.53882 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 9b0ad582-f52a-3f1c-bfc0-f039d561d1de | -6.67632 | -58.75928 | 2025-08-30 05:10:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45c7b60b-7928-3459-b86c-30687f046d13 | -8.55641 | -63.01654 | 2025-08-30 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9409c356-0cbf-3b09-8586-52c6b9cad0d0 | -7.75363 | -45.46381 | 2025-08-30 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 893a2b45-8af8-3912-ae17-6f861e7a7eb5 | -9.57923 | -54.4714 | 2025-08-30 05:10:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a9fff335-19ae-396c-899a-f10254a93e31 | -9.60301 | -55.38393 | 2025-08-30 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3a6861b6-732e-33a8-afbb-83160cac001d | -9.15826 | -59.57515 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72cb8d1e-981b-3497-b27f-569a3e37126e | -9.43839 | -60.5544 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 04fc22e8-d54c-3be9-83f3-619b229becc1 | -10.07589 | -58.35759 | 2025-08-30 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4f39584-ffaa-380c-a1a8-4836748ac2a1 | -7.43346 | -44.81755 | 2025-08-30 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 44a2fa24-d6b1-3bc1-8ecf-df0dab539846 | -7.95361 | -46.39171 | 2025-08-30 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ba386eca-c0b9-393f-a010-0d74f2c78da9 | -7.39184 | -60.59187 | 2025-08-30 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5e1491dd-ceff-3d27-a596-edeb3b97aefa | -9.16456 | -59.55756 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f3b40670-fe5c-39d7-82fd-3fb7c6de4bff | -7.77385 | -45.46139 | 2025-08-30 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aeb3b2e6-91ae-31ad-84ce-ee3267ceadcb | -9.43649 | -60.56612 | 2025-08-30 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 840b1382-dfde-36ba-87bd-dff740ef257a | -10.02131 | -48.05658 | 2025-08-30 05:10:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 22c48905-39d0-3d99-b6e5-7e9cad05375a | -8.87551 | -60.74138 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54370b60-54ef-3a2d-88a9-11042e4c49ce | -11.87873 | -46.37796 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 81936553-70c5-34bd-9bdd-7b3c7081fa3f | -11.83632 | -46.87049 | 2025-08-30 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 17f4f4b3-d666-373b-b21d-62ef39e7b0ec | -9.44726 | -62.34018 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 959f3d0b-9ad4-3172-bcc3-c1d3e04d3213 | -7.68371 | -61.09077 | 2025-08-30 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d26d1c5-ac31-3eae-8cbc-dd695568e9af | -10.38182 | -57.83636 | 2025-08-30 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| edb54ce0-4f08-3625-a699-78e97ac01a03 | -10.37129 | -57.81671 | 2025-08-30 05:10:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c1dc15d-57a8-3711-abd4-7780eb365a4a | -11.86287 | -46.45636 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| c8534d4c-5d5e-3a0b-ae87-1ee6427c18bf | -7.34901 | -70.12796 | 2025-08-30 05:10:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3d0a73d8-8930-3c2a-aec9-0117acd411d0 | -7.39116 | -60.59595 | 2025-08-30 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9739b3ef-03f3-3814-96b1-b3d84ec8595e | -11.87149 | -46.38355 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bbbb2aae-e12b-35cc-9c4c-3e10fc428235 | -8.63818 | -67.26038 | 2025-08-30 05:10:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf93492f-1252-31be-aad8-77321a1a881a | -11.88416 | -46.38766 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 21318da7-4ccb-3730-be12-2099edbd2e26 | -9.21949 | -60.87402 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 73c7f270-407f-3f94-9c75-7bf485bcf7a2 | -11.87095 | -46.38812 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dea606b0-fbe0-38d4-8866-775a30c85fcb | -9.70987 | -61.30511 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d831809f-c4d1-3284-90aa-d42f5aa6db92 | -9.80736 | -61.19645 | 2025-08-30 05:10:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c21aa10d-a84d-3334-9781-c8fd70e7ed86 | -7.39609 | -60.58836 | 2025-08-30 05:10:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4d84e1b-d2fc-3eba-98e9-229d058c78aa | -9.44547 | -62.37424 | 2025-08-30 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c480ca5-368e-3422-88e0-af50b76ffec3 | -9.11186 | -65.77093 | 2025-08-30 05:10:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 81cf3d00-2746-3d01-947c-4309bcb964b4 | -11.85112 | -46.39279 | 2025-08-30 05:10:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4e9c7f6c-02f3-3568-946f-7607b4a2ec36 | -11.0644 | -52.04089 | 2025-08-30 05:10:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29a11a65-6d4a-3d72-b621-85a414310b31 | -4.89639 | -55.84803 | 2025-08-30 05:10:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 763611ac-711d-3c00-801c-9c7a354f7bfb | -9.56286 | -55.38606 | 2025-08-30 05:10:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 547ac27e-61ef-31ea-bab2-6edb6a3a3566 | -5.70136 | -45.96159 | 2025-08-30 05:10:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README65.md)
