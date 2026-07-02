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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 97d473dd-f54e-3919-9079-0b62abbf5fe7 | -10.78693 | -53.54659 | 2026-07-02 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0935b389-2359-3a6e-ab56-2c191cf8be70 | -4.94214 | -48.24575 | 2026-07-02 04:19:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4277a383-1570-3faa-ba3c-1f8a1fc20811 | -10.82806 | -44.96368 | 2026-07-02 04:19:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d05b90d0-dfa4-35aa-af4c-406691412cc2 | -10.37024 | -46.68711 | 2026-07-02 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 33887eac-ed15-3bdf-9b37-34eb1cf56d0f | -4.34829 | -47.76629 | 2026-07-02 04:19:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 81443e87-5907-3033-be45-1530642d2cec | -12.7668 | -44.49924 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| af6debb6-2545-3082-9714-eee8d48c876d | -10.94498 | -43.05099 | 2026-07-02 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 301e375c-5e7a-34e1-96cb-c01f0ae42eb7 | -5.29613 | -43.71109 | 2026-07-02 04:19:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 96d9d9c3-2a09-340f-851a-dd1a6ffa15bc | -10.12442 | -52.0965 | 2026-07-02 04:19:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a0f63ab3-09bb-3e33-bacd-f40c213f5746 | -12.86899 | -44.34398 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 9ac0910b-a102-3c80-86aa-dec998e56147 | -10.9461 | -43.04396 | 2026-07-02 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b1161036-dea2-361e-95bc-1ff75a3cd95a | -5.78823 | -45.04931 | 2026-07-02 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9b30a15f-ad29-3e6f-8769-770d52e774b1 | -5.79333 | -45.04132 | 2026-07-02 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a157dd41-36ec-34ae-8f31-af0e6dd22bae | -11.42266 | -56.05724 | 2026-07-02 04:19:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0d6c30fa-6db0-326f-ab05-0d4e3afb3704 | -5.79404 | -45.03699 | 2026-07-02 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5bf3bc88-ba55-3433-b947-a349a3a27a54 | -4.58033 | -48.02755 | 2026-07-02 04:19:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b7eb987-310d-365d-9474-28a82935eb23 | -12.86622 | -44.33979 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 57adca4c-ca87-3f70-9504-778e009c0e61 | -11.40661 | -49.01053 | 2026-07-02 04:19:00 | NPP-375D | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00c29c1b-ad4b-3e64-a06a-c86eb1217ec4 | -11.04057 | -56.93209 | 2026-07-02 04:19:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ac47a6a1-c41d-30a0-94f8-c12575e76479 | -12.74835 | -44.48485 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 49626145-d46e-38d7-a0e0-062d00dd93cd | -12.76958 | -44.50348 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| fdcc1a6c-2be5-3545-b9f3-79971139880c | -11.00147 | -47.18594 | 2026-07-02 04:19:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 73f310c9-239a-3884-9099-3ee4de7a7063 | -11.79535 | -56.99857 | 2026-07-02 04:19:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 3be7c272-3991-39e4-871a-2dda4ff0c2b4 | -5.12576 | -49.33234 | 2026-07-02 04:19:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 645ecd0f-6021-3055-9b0e-1f82ecb4f47c | -11.413 | -56.06141 | 2026-07-02 04:19:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fe00202a-f55c-33db-9e06-7836bdefd9df | -12.75628 | -44.47868 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 39.0 |
| a4dd3779-72e5-3e53-94d3-72bbb28c60eb | -13.29751 | -43.55284 | 2026-07-02 04:19:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ac5e89f2-ffc0-34ef-be7b-de81409ce408 | -12.76858 | -44.48829 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 40b0e667-500b-3c5f-a0b7-4a1fd4be78a1 | -11.86997 | -45.60855 | 2026-07-02 04:19:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd9cf0db-b817-3e6b-a000-36dbf73cab3d | -12.51484 | -48.28452 | 2026-07-02 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6cddfba3-ba52-3a04-874d-f8cdde089fa1 | -11.79738 | -57.007 | 2026-07-02 04:19:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 239473d7-5c64-3226-9526-d8b29cec4548 | -10.76927 | -53.54336 | 2026-07-02 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e86304f-2a1c-3190-8dc5-1e97cf94ee38 | -10.9476 | -43.05191 | 2026-07-02 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 45fdf184-5184-3120-a19c-8b0516679162 | -11.8009 | -57.00723 | 2026-07-02 04:19:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| e5caef60-4725-33ff-aff2-7df935b895ce | -12.45166 | -46.91423 | 2026-07-02 04:19:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42ebc5c8-eee4-3c20-90c1-af2ea582ef9a | -11.41051 | -56.07374 | 2026-07-02 04:19:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a4a1e4a3-c169-308e-b614-da7f1c1279f0 | -10.1251 | -52.09301 | 2026-07-02 04:19:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ec219fc-c145-35ac-b95e-5f4d2594e37c | -5.81292 | -43.79516 | 2026-07-02 04:19:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c4d6823d-58b2-3809-b93b-77e475f2468a | -12.85656 | -44.35676 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7e7cba85-bfd0-32ac-8207-b9a3e300cbfb | -10.37863 | -46.68377 | 2026-07-02 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 02dc451a-5d2f-35a6-92ed-d3b3f1af26f2 | -10.37105 | -46.68245 | 2026-07-02 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b4650a36-e321-3872-addf-1d1b016ab50b | -3.66891 | -48.98222 | 2026-07-02 04:19:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8fc5c9e-21ba-32b5-973c-ab343c24a1a2 | -5.80883 | -43.79842 | 2026-07-02 04:19:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4055b5ff-0815-3280-95ae-d2113905208a | -6.98533 | -39.81363 | 2026-07-02 04:19:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e22ae7d0-5af9-3cfc-b5bb-446243b6cf4f | -10.37403 | -46.68776 | 2026-07-02 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 638ca7fe-0b44-38a9-a897-99573cc1279e | -10.84542 | -45.06115 | 2026-07-02 04:19:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8bbde80-84d6-3623-8d3d-0d43d74f0a5a | -11.41456 | -56.06235 | 2026-07-02 04:19:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6a0d8d37-db66-3e49-9d3b-af826f9dcea4 | -13.73564 | -47.8938 | 2026-07-02 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8da20ad3-39bf-3527-8699-650744ec3428 | -12.75847 | -44.48656 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 4ce3850b-3653-3321-b664-350ed1ae439d | -3.51618 | -48.03635 | 2026-07-02 04:19:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 5f5b2854-79c7-3785-9bad-838d29449983 | -5.37649 | -43.37949 | 2026-07-02 04:19:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9e32aad2-0041-320b-ae8e-b9cf27c81325 | -5.81639 | -43.79572 | 2026-07-02 04:19:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0ea06345-b7d1-34ec-813d-356c76c7b044 | -12.85556 | -44.34168 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 1ba1213c-ba9a-3847-a97d-472e91bac45b | -12.78902 | -44.4949 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 85249e42-6517-376f-b616-483630791b80 | -12.86958 | -44.34037 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| dc48f60e-974e-311d-9151-fc1c73e9e220 | -11.80444 | -57.00851 | 2026-07-02 04:19:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7e52cc36-3d8f-3c1e-8332-4fc5b13c015a | -12.75787 | -44.49022 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 965cb2be-b199-3076-bcb8-48beca2c41e7 | -12.5142 | -48.28814 | 2026-07-02 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0e901739-343b-340e-ac5b-295df4015a93 | -11.3581 | -55.43222 | 2026-07-02 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f78efd52-e604-3188-8a44-7df9ebe4fa70 | -11.85093 | -48.24534 | 2026-07-02 04:19:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 328c289d-066e-3abc-a9a0-36a6385198d8 | -10.69634 | -49.61305 | 2026-07-02 04:19:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a766b0ae-61a2-39a7-8d31-868099c5e58d | -5.14826 | -37.91228 | 2026-07-02 04:19:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d2f19444-ffcd-3b69-819e-41490ab2b45d | -13.72494 | -47.88659 | 2026-07-02 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e3e5663-3581-3143-9800-0520904913c5 | -10.12917 | -52.10102 | 2026-07-02 04:19:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 788e60ba-8ed7-3845-9c50-121aa07d225e | -5.12693 | -49.33555 | 2026-07-02 04:19:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a3164726-7860-3894-80a7-f500138ef7db | -12.84766 | -44.3478 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 8f7f5145-dbe1-3a93-a254-5cff13992535 | -5.88363 | -46.96644 | 2026-07-02 04:19:00 | NPP-375D | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0e324586-d52e-3c9c-8515-e99b56a225cc | -12.85161 | -44.34474 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 8469b52e-ae14-310b-bb22-925442bd915f | -12.77831 | -44.49683 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e5d88ba0-6e57-31c0-8fe4-efcde020cd4e | -13.29418 | -43.55229 | 2026-07-02 04:19:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 943340dd-1d71-3cab-bbde-5cabc48bc7c4 | -12.62126 | -44.66303 | 2026-07-02 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8df19aef-8f37-34b2-8788-b7e336edaf62 | -10.12288 | -52.10076 | 2026-07-02 04:19:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 72734ee5-7bcf-38dd-9088-2e1b0069a040 | -10.95092 | -43.05245 | 2026-07-02 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.5 |
| c1b18d30-d0af-312c-8a66-9e860dfe3744 | -12.75927 | -44.52429 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f061c325-c44b-338e-bb9d-474d36f042d3 | -5.55873 | -43.82972 | 2026-07-02 04:19:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c9749ac-2f92-3707-9029-d1cad86dbc6e | -12.85261 | -44.35982 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 815b0eb3-0b4b-3544-8ec5-ccb123e553d0 | -16.44934 | -44.76655 | 2026-07-02 04:19:00 | NPP-375D | CAMPO AZUL | MINAS GERAIS | Brasil | 3111150 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8a44b16f-71f9-34a3-91cd-29f4a1be68b1 | -12.52292 | -48.28604 | 2026-07-02 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3cad3e18-47c6-35e2-8dd8-41faecafab8b | -12.87118 | -44.35179 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 34.0 |
| bb162039-94f0-3713-89d5-2bec54d8bb43 | -10.94222 | -43.04693 | 2026-07-02 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 06656f93-acde-3568-bb08-e0a6cfa25746 | -12.61787 | -44.66245 | 2026-07-02 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb0ede4d-b532-31c0-888d-ef8b5861e06a | -11.31527 | -46.47808 | 2026-07-02 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3a39a71e-f310-3dfc-97c3-1b1011934f93 | -5.14649 | -37.9099 | 2026-07-02 04:19:00 | NPP-375D | QUIXERÉ | CEARÁ | Brasil | 2311504 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3fd524a4-d2de-33f8-94e2-5474983b1452 | -5.34865 | -45.1822 | 2026-07-02 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3b3cd3c-3ea0-34b7-919d-d73719388d24 | -12.76205 | -44.52853 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c0a7062a-af57-3bcc-8411-8bfb4f55c9d8 | -3.51523 | -48.03308 | 2026-07-02 04:19:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 5b31a73e-60b3-3b94-a79a-10da7623331b | -12.85497 | -44.34531 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 439704d8-0b4a-3aa5-a400-c8e4ce13a4b8 | -3.50694 | -48.03489 | 2026-07-02 04:19:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ba12161-9736-3694-8f90-ab22727f09a1 | -5.79476 | -45.03268 | 2026-07-02 04:19:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d83152fb-b5c4-303a-9469-5878c202d621 | -11.04768 | -56.93366 | 2026-07-02 04:19:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8d6968d-0e94-3bbe-a4ff-3ce28a119f8d | -12.78288 | -44.4901 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 0fe42bf5-8f3e-3371-80bb-70f24e1afe5b | -12.75291 | -44.47811 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 68.4 |
| e5f90722-ed4a-3148-8aab-b4a947fa693a | -10.12482 | -52.09025 | 2026-07-02 04:19:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a897d7c7-799a-3e60-b470-9bec4459ea41 | -4.28593 | -48.3597 | 2026-07-02 04:19:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fdc972e1-2231-377b-a7c3-edd572c0904b | -12.75509 | -44.48599 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 160.2 |
| 4a22a15e-9a59-3210-ade6-fa2b7084932d | -12.51888 | -48.28528 | 2026-07-02 04:19:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b41da618-2cb0-3bf8-b2dd-cf12f9c9d21c | -15.95626 | -45.99781 | 2026-07-02 04:19:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 604b6ab7-ec7f-39a4-b2f8-141fc1bed590 | -12.78228 | -44.49375 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 71ec2157-c96f-385a-b6ef-80b7acf949ac | -12.84648 | -44.35505 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e924b088-bf4b-3bbc-b47b-311eb135d43f | -12.74895 | -44.48119 | 2026-07-02 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 126.4 |


[Clique aqui para ver as próximas entradas](README14.md)
