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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5135c084-939b-372f-988c-b4cfbfefcf56 | -11.8872 | -45.29159 | 2026-02-19 04:08:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa576e0c-e476-3473-a770-7e0c93beb58c | -12.39294 | -43.66086 | 2026-02-19 04:08:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da0923be-fbd6-3944-9b72-511196a99f99 | -13.32406 | -40.89495 | 2026-02-19 04:08:00 | NPP-375D | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 46f1d441-f8c0-38a3-8db5-f95bd318e201 | -12.49225 | -43.64975 | 2026-02-19 04:08:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2c57d5f1-5f27-34d7-961a-11ecac79706a | -12.06621 | -45.35224 | 2026-02-19 04:08:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0029b803-d8a2-3a42-8e88-eadf11c30688 | -13.32072 | -40.89444 | 2026-02-19 04:08:00 | NPP-375D | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 057362dd-88dd-3830-8709-45fb108234ef | -11.89557 | -45.28823 | 2026-02-19 04:08:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 26438277-6dbe-3fa8-bc4e-473a980b79a2 | -15.91189 | -41.73085 | 2026-02-19 04:10:00 | NPP-375D | CURRAL DE DENTRO | MINAS GERAIS | Brasil | 3120870 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5533ded8-cc9d-3f39-9e29-a0150a8a5df8 | -18.35216 | -39.799 | 2026-02-19 04:10:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b6756795-25ac-3655-84de-d196bb759aa3 | -13.41169 | -43.7507 | 2026-02-19 04:10:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44608e71-d656-3206-a24f-500a3a05441a | -15.85723 | -43.50953 | 2026-02-19 04:10:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 670c27f6-b5f0-3f21-8acd-b09ed4404638 | -14.23043 | -45.41845 | 2026-02-19 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ccf75270-74a9-33db-b9ae-c7468b674936 | -13.8259 | -42.42397 | 2026-02-19 04:10:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| c5b40bea-ac32-359e-999a-06508e61a664 | -18.53006 | -39.76808 | 2026-02-19 04:10:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 0dad1351-3d10-3fc7-b5a3-c4f9606e7de3 | -15.90272 | -44.79497 | 2026-02-19 04:10:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 89299720-a903-3be6-bc68-53a6f90486ed | -17.71981 | -42.21216 | 2026-02-19 04:10:00 | NPP-375D | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| efb16aa1-1fd2-3dfc-a133-20ca7d8598de | -15.90248 | -44.79354 | 2026-02-19 04:10:00 | NPP-375D | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 41a0f868-818a-35aa-b8c0-2db2228bafba | -14.51593 | -43.62962 | 2026-02-19 04:10:00 | NPP-375D | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| afc0e820-e6bd-3779-8977-474173be7439 | -16.60814 | -43.36431 | 2026-02-19 04:10:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0e97f5d7-69e8-36b9-9fb2-6535f8e1626f | -15.85385 | -43.50894 | 2026-02-19 04:10:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 113c6bad-5a98-310e-a37f-f54f1f784ad3 | -17.30389 | -39.22814 | 2026-02-19 04:10:00 | NPP-375D | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 9daf4d4e-ecc6-32e4-80ad-97386f23bb2f | -14.23412 | -45.41916 | 2026-02-19 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e449e9b-a558-3795-8de5-c485dd517111 | -16.48869 | -39.86602 | 2026-02-19 04:10:00 | NPP-375D | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| cffdf7fe-3ec7-3fa2-aac5-1ec44fefa44a | -13.26817 | -43.93821 | 2026-02-19 04:10:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc3e2fd5-2a78-3d90-9a39-559cc2d08558 | -20.04429 | -41.34765 | 2026-02-19 04:10:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9131bb7d-2c72-39d9-9955-71ab2d751161 | -21.1724 | -41.86428 | 2026-02-19 04:10:00 | NPP-375D | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 9eb62863-9b8a-3fb2-8f52-c6232f7a7ebe | -14.22675 | -45.41777 | 2026-02-19 04:10:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ea7cdb2-75fa-35d6-9244-ed9c92c10acc | -13.54516 | -43.70563 | 2026-02-19 04:10:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17273c80-f86b-33f6-9546-5c541284c492 | -17.71648 | -42.21159 | 2026-02-19 04:10:00 | NPP-375D | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b60cd213-f3e5-3629-8d9c-87094c52a4c1 | -16.60479 | -43.36374 | 2026-02-19 04:10:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b57444a6-c56d-32aa-899f-0ab301269b07 | -18.53105 | -39.7708 | 2026-02-19 04:10:00 | NPP-375D | CONCEIÇÃO DA BARRA | ESPÍRITO SANTO | Brasil | 3201605 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 39a07579-1fae-30be-af29-6b9b3ecf6f27 | -22.78345 | -49.35798 | 2026-02-19 04:12:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6eab825-7a89-3a41-9e84-dcb63570e72d | -22.78417 | -49.35419 | 2026-02-19 04:12:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1fb2a194-1ab0-37ff-b478-3849fba2c843 | -22.78748 | -49.35817 | 2026-02-19 04:12:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b2aa063f-8ed2-3ea8-9e77-585995a8e6e2 | -22.78748 | -49.35885 | 2026-02-19 04:12:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80f20a92-7aef-3782-872b-e11f20694b0a | -20.80103 | -44.6262 | 2026-02-19 04:12:00 | NPP-375D | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 10d99c79-a0ea-3b93-9b86-f1bdbd777ea7 | -21.70161 | -48.42804 | 2026-02-19 04:12:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a14c1a42-dff8-34af-bfe8-71bc809eec14 | -27.68747 | -48.75232 | 2026-02-19 04:14:00 | NPP-375D | SANTO AMARO DA IMPERATRIZ | SANTA CATARINA | Brasil | 4215703 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f1a8599f-3eff-3acd-989e-3df80d4badf3 | -27.26437 | -48.72777 | 2026-02-19 04:14:00 | NPP-375D | CANELINHA | SANTA CATARINA | Brasil | 4203709 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 98a39265-4a12-328f-ad3b-59244f2091e2 | -30.73146 | -54.98531 | 2026-02-19 04:14:00 | NPP-375D | DOM PEDRITO | RIO GRANDE DO SUL | Brasil | 4306601 | 43 | 33 | nan | nan | nan | Pampa | 1.6 |
| 90d11833-1093-3b2a-a197-b0c104f64ddd | -27.4572 | -48.45252 | 2026-02-19 04:14:00 | NPP-375D | FLORIANÓPOLIS | SANTA CATARINA | Brasil | 4205407 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| da95f460-2d65-3c68-9e7b-481ea91ded01 | 2.6905 | -60.2401 | 2026-02-19 04:20:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 624da0da-f3f3-392b-abff-933a77851457 | -11.00097 | -54.00864 | 2026-02-19 04:29:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 52b81453-eabb-3df0-ad26-4c56974563aa | -12.30973 | -57.36905 | 2026-02-19 04:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c1094ca6-f38f-3ba5-b244-3e6f4e308e44 | -12.2436 | -44.23204 | 2026-02-19 04:29:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cc85c1c8-3468-355c-866f-7a7eac554b66 | -12.30905 | -57.37264 | 2026-02-19 04:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 789fdf33-0e2f-379b-9268-e961b730fea4 | -12.16204 | -46.67385 | 2026-02-19 04:29:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7850145f-f590-3a9b-971a-2b12453637d2 | -12.1587 | -46.67332 | 2026-02-19 04:29:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8df96e56-c93c-3c3c-afd7-9cec0ccff3ef | -12.31159 | -57.37029 | 2026-02-19 04:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a8a080b-fd46-3a5f-be46-412297f956df | -12.31577 | -57.3667 | 2026-02-19 04:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b0d44778-714a-3077-867c-812a0296d79d | -13.26912 | -43.93668 | 2026-02-19 04:29:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fcec1880-0089-3a16-8f58-07052a23131e | -14.23506 | -45.41697 | 2026-02-19 04:29:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d0e9864-0482-3d29-8bb3-14d972457623 | -12.80984 | -44.82551 | 2026-02-19 04:29:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a0ab8bf-87f8-3d18-968b-cdb2b1d7c132 | -12.16259 | -46.67026 | 2026-02-19 04:29:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d8327a0b-c8c1-3373-9960-74821bf71d78 | -12.39337 | -43.66188 | 2026-02-19 04:29:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af92cf79-5f3c-3dc4-98f2-d60803be67b6 | -11.89245 | -45.28757 | 2026-02-19 04:29:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2314dabd-a0f8-33d0-983c-1673d5f00937 | -13.41049 | -43.75085 | 2026-02-19 04:29:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 019061a6-99be-3308-a387-4d80b54c03bc | -14.23152 | -45.41644 | 2026-02-19 04:29:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 335589d8-97bf-3f0a-8d2f-21c8458ba587 | -12.0352 | -49.87671 | 2026-02-19 04:29:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c58904bb-98c6-3689-88a6-8875ead057a9 | -13.82617 | -42.42439 | 2026-02-19 04:29:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ed4317d2-6724-38b9-b3f1-c3b698e0e83d | -13.7648 | -53.39942 | 2026-02-19 04:29:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f65e0a32-3d5a-311a-98a4-e7000b6f3c0e | -12.08071 | -43.52717 | 2026-02-19 04:29:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1f63b548-c008-3364-a2b9-9f8ebbd6815b | -12.03584 | -49.87288 | 2026-02-19 04:29:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7885560-8676-3de8-8fb5-6bc0e7470440 | -12.48784 | -43.64926 | 2026-02-19 04:29:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 146540d5-898c-33b2-aec3-437e794ded20 | -12.06647 | -45.3491 | 2026-02-19 04:29:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f30b73c7-1f44-3986-9456-bc83b2d24e16 | -12.24298 | -44.23644 | 2026-02-19 04:29:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 839fdfcb-f60c-37d8-99f2-242ee38c238a | -12.49164 | -43.64982 | 2026-02-19 04:29:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df1c174f-f809-3993-98b4-dc7527cfb3a7 | -14.22798 | -45.41591 | 2026-02-19 04:29:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79dc5648-bf11-3188-bdbb-fed85ce104ed | -12.4847 | -43.64395 | 2026-02-19 04:29:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dcde41a8-8966-353e-83df-4168334e93f0 | -12.49545 | -43.65039 | 2026-02-19 04:29:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7421c46c-7ae5-336a-8d53-e9b477fcc98d | -12.80922 | -44.82968 | 2026-02-19 04:29:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ead48b5-0889-3646-90aa-f61a898eb13c | -13.69153 | -52.58469 | 2026-02-19 04:29:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d783f328-5c90-329a-b1f4-e9289bea28b5 | -11.79527 | -44.1367 | 2026-02-19 04:29:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ad83b43b-ed78-3822-84ec-ac61c9a11b49 | -12.27653 | -54.09364 | 2026-02-19 04:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4572367e-96a0-318f-b726-edf384797e7e | -11.88145 | -45.2898 | 2026-02-19 04:29:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b0b34e8-2dfd-3397-827f-2aafb2a10c55 | -12.06994 | -45.34965 | 2026-02-19 04:29:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c1381144-6a63-3ee1-8f7f-cb8ad4a780dc | -13.26535 | -43.93609 | 2026-02-19 04:29:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1977349-7d3d-3b12-be61-62b1751bef68 | -12.15925 | -46.66973 | 2026-02-19 04:29:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c3b009f-2a26-30be-945f-5706313a5c64 | -12.27531 | -54.09453 | 2026-02-19 04:29:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 81296ef7-469f-313a-bb11-d86f0f649d1e | -12.07688 | -43.52671 | 2026-02-19 04:29:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6b537a5f-0ef4-329d-b3dd-508a8acd314b | -12.24397 | -44.234 | 2026-02-19 04:29:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1b190c6e-8432-359a-914d-8aaa161a747e | -11.88492 | -45.29037 | 2026-02-19 04:29:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4d2bab1d-a1d8-37f7-84cb-2efe80bab7a8 | -12.30624 | -57.36903 | 2026-02-19 04:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 650b4549-2b4f-3dd0-aea2-6bbfc42af01e | -12.20025 | -47.96954 | 2026-02-19 04:29:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0542fd4a-1413-3004-98ab-0c283250afe1 | -11.89303 | -45.28367 | 2026-02-19 04:29:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51109608-2b4f-3e29-b22c-892addcb48bf | -12.24333 | -44.23838 | 2026-02-19 04:29:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9cfa5ac-4e96-39cd-b37f-86b9d08f3ffe | -12.19969 | -47.97305 | 2026-02-19 04:29:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56823688-739b-3119-b4db-f124c8050c92 | -11.88202 | -45.28592 | 2026-02-19 04:29:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc26ccfc-4141-3575-b4f4-b89eae8d7040 | -14.22737 | -45.42001 | 2026-02-19 04:29:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 54631fcc-581e-31a9-8fe5-b2534991a3d3 | -12.69051 | -46.70159 | 2026-02-19 04:29:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1add81f4-2ba4-334d-bc72-56a92d94f985 | -14.12056 | -47.39717 | 2026-02-19 04:29:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e2f70ce3-fd38-3ee3-b9f3-fb6de21bf6ca | -12.48403 | -43.64871 | 2026-02-19 04:29:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a1ae98a-147d-3d45-ac2b-e406f790e362 | -12.3123 | -57.3667 | 2026-02-19 04:29:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7298f350-931d-379b-8898-9e923f054a26 | -22.92955 | -48.67504 | 2026-02-19 04:31:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a6e04e5-da58-3399-87a2-6ca891e62c5d | -23.99079 | -50.4595 | 2026-02-19 04:31:00 | NOAA-20 | CURIÚVA | PARANÁ | Brasil | 4107009 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 19a401ae-c715-351c-862f-44bffd112c52 | -22.92897 | -48.67895 | 2026-02-19 04:31:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed48cdd8-a7a2-3c8c-a8be-77685c0b6698 | -22.93294 | -48.67559 | 2026-02-19 04:31:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ccb0dd73-7d10-3dbb-9901-1271e86d9efc | -20.80317 | -44.62621 | 2026-02-19 04:31:00 | NOAA-20 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4053391c-22f6-3e51-84e6-1f00742e3dc3 | -22.78961 | -49.35716 | 2026-02-19 04:31:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef5d42b2-e5f3-35c2-8843-7160358928af | -17.31202 | -44.93058 | 2026-02-19 04:31:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README4.md)
