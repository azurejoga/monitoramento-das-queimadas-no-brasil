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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3882b573-af2d-3d54-a7c4-d7d1028bde31 | -9.86813 | -48.35348 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 82d8e393-02d4-384a-9c27-c6c98fa9ba63 | -10.39442 | -46.63416 | 2026-09-17 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bace3a69-d803-3356-9687-06fc9f622169 | -4.51961 | -54.94567 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8af0c29b-dbb0-34f5-9913-250a9aadb808 | -6.04509 | -44.03403 | 2026-09-17 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f5f71b7a-e9d6-3a3b-a23c-a34658b163fc | -11.34006 | -47.24623 | 2026-09-17 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a9841575-4c28-34dc-9bfd-6c4c3b6660c1 | -6.79831 | -58.7921 | 2026-09-17 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 15b3b914-8ee1-3f54-b859-2aa61c07cf76 | -8.70121 | -45.28995 | 2026-09-17 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b4c4ce37-6ec7-3c7a-b3f9-b785e1c81c6f | -9.96191 | -45.31734 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7ce9bef-b9d2-3d37-a7aa-cd0cbb1c4aef | -11.88966 | -43.82735 | 2026-09-17 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1be4ed7f-dfe8-32e8-a069-4bc40233ae10 | -8.1395 | -44.8548 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2112b1bb-20a3-3df2-8a88-8f3958b67558 | -8.60937 | -44.47658 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6c0733d2-f61e-39b0-a72f-fe2155b6b705 | -5.79771 | -47.24697 | 2026-09-17 04:40:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| fac0e998-c83c-33da-8b7d-47caf6034ed8 | -9.76492 | -46.09235 | 2026-09-17 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 268b6450-f14b-32d4-99d8-6783b1c64017 | -6.77537 | -48.12473 | 2026-09-17 04:40:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76429bc6-0cc8-3f11-a4d8-5bd3b396f31f | -7.19308 | -41.80823 | 2026-09-17 04:40:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| f571dd6f-a612-301b-ac91-662755a6eee8 | -10.34927 | -47.59815 | 2026-09-17 04:40:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6888249b-2afc-3141-80a6-563b6cb8af8a | -6.78802 | -48.66122 | 2026-09-17 04:40:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1097d065-c5ab-33a7-998c-c54c03469de7 | -5.14824 | -55.93708 | 2026-09-17 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f0ca207e-56b8-3c7c-89bc-5f9790316498 | -7.45664 | -42.11143 | 2026-09-17 04:40:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9a272070-65f4-33f2-bc23-428bfa02dd74 | -4.88404 | -50.91365 | 2026-09-17 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a301eb12-5328-3827-a720-05b04715a8dd | -7.1355 | -42.17493 | 2026-09-17 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| e8cd2acd-6d28-3f8a-810e-f8b0cd312624 | -9.77808 | -46.59564 | 2026-09-17 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cdcad6b3-6049-3ae0-add2-1b8898603a26 | -11.33444 | -47.65352 | 2026-09-17 04:40:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1599c03-c11a-3e14-9c5a-f6e02e7467ac | -7.58346 | -44.93018 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d4bd9303-98bd-3fc6-b63e-6ea5da90576e | -8.83206 | -44.89738 | 2026-09-17 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3da09a0d-411d-3694-9d13-c9e193fc3d69 | -8.49531 | -57.64809 | 2026-09-17 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b16de2af-b0b2-3fad-a45e-a8f2179434c0 | -10.83562 | -46.17297 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 96b682b1-9ba7-39fe-8557-c21e96ea9ad6 | -9.88536 | -48.37904 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 989feab1-6dff-3fc8-af92-bd473c366c58 | -7.03234 | -42.0759 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| cca034f3-efb1-303a-aaf6-bc198ac0d333 | -10.30248 | -45.31792 | 2026-09-17 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9238e64-33d7-35a9-937e-9c53686f7966 | -5.22216 | -49.33034 | 2026-09-17 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb16f6bf-0a23-34c2-badc-c228f3e89ddf | -7.46334 | -42.10644 | 2026-09-17 04:40:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4e00f9ed-ac68-3fe4-9b9b-6bc8a8bcbfaa | -5.78562 | -47.28004 | 2026-09-17 04:40:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e5affe96-47a5-3b52-b569-ee44401c9240 | -10.29385 | -45.32043 | 2026-09-17 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd0937e5-e618-3051-b870-7ba44c02c854 | -9.10914 | -45.71979 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 30c57950-cf03-33b3-83ce-43b8ba9d2733 | -8.69385 | -44.87418 | 2026-09-17 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cff02f4f-5383-38c7-bb9b-de945f7b12b6 | -5.83833 | -52.11153 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62a26963-e6ab-303d-b7c8-bb8c327afe51 | -6.77801 | -48.65967 | 2026-09-17 04:40:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 55c1e5dd-a87a-3942-a30a-b2736bde388c | -10.31971 | -45.34267 | 2026-09-17 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 959762f6-4545-3709-ba56-6d1dfc321b91 | -7.44642 | -45.28922 | 2026-09-17 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aa4ec57e-21f8-3970-9a10-0888988c8c81 | -5.77714 | -45.1045 | 2026-09-17 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 65f29ed9-a183-35fc-8443-bb42fa01919a | -6.03269 | -44.03175 | 2026-09-17 04:40:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c144f7aa-60a6-339f-8b5d-0d115c3c676f | -11.20391 | -42.82432 | 2026-09-17 04:40:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 65031a29-b241-3262-ad6d-09168285714e | -10.80126 | -50.84786 | 2026-09-17 04:40:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73424f25-6abb-3c3c-98a2-8dfda506213e | -9.87049 | -48.38455 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7af8d10-39cb-35dd-92ce-a2becbbdc2ad | -8.95017 | -50.85003 | 2026-09-17 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed5e6850-2efb-3d0e-8b06-c0b0deb83780 | -10.78441 | -46.20061 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 51d9739d-4956-357c-a252-296a6fc8370d | -11.34443 | -43.99328 | 2026-09-17 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9678663e-966e-393a-8dcb-ff52e8e1c108 | -5.77189 | -45.11337 | 2026-09-17 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| cca96673-3b24-3859-ac1b-1e64a4a158da | -3.81473 | -58.89357 | 2026-09-17 04:40:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba08135d-8796-3e25-a223-900a564b3ddb | -10.41745 | -48.63855 | 2026-09-17 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2707355b-f890-3afa-a9e4-1f8715ecbcc4 | -8.58262 | -44.57521 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b7715670-8525-3e0d-9cd3-76f9096ff6d4 | -9.9569 | -45.32372 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 05e1fa82-d3c7-3c3e-bc73-371870e8fe65 | -7.9496 | -44.81916 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cc9121ca-7c54-3b55-9163-8264622b8d91 | -5.98168 | -53.5945 | 2026-09-17 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3890333f-a126-3e12-84ad-696c74a65021 | -12.73698 | -43.45558 | 2026-09-17 04:40:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dd0befd3-45f0-3e72-938a-eab828fc60a1 | -8.26428 | -42.17513 | 2026-09-17 04:40:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 195a20e4-7dde-340d-b3eb-ed56eab26a7e | -12.45759 | -50.84632 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ee56a5be-9c75-3c6f-bceb-f05740859243 | -15.63709 | -52.73055 | 2026-09-17 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ecd87d4-121c-37ee-aeb2-e5f39e928119 | -13.30916 | -43.71602 | 2026-09-17 04:42:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28094b9a-2491-3dd6-ab7d-cfebf64ed410 | -12.46144 | -50.84334 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21285faa-45d1-3096-b520-f51a4b537f6c | -12.45256 | -50.79144 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d3601d64-1a30-3b17-829a-7667d57e43c2 | -12.47131 | -50.80166 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a06916e9-9936-3e97-9ae6-8549ebc9340d | -15.64492 | -52.72444 | 2026-09-17 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 534af698-54de-349d-baf5-f61bbea2e579 | -12.44816 | -50.79794 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 89e19e57-b6e8-33a6-b036-8c7a52809c33 | -14.57638 | -46.59234 | 2026-09-17 04:42:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ed79675e-e153-33bf-8c79-7ea58362c5e1 | -17.77889 | -46.47847 | 2026-09-17 04:42:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1fea9d34-85ae-3711-b7bd-4479b2995855 | -12.46035 | -50.85037 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 53c281a2-cd70-39ba-b8d8-3efdc7d6a4ba | -11.98662 | -52.46817 | 2026-09-17 04:42:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f6d5fb3f-06f2-3419-b7e7-7f5c9a216e29 | -12.45316 | -50.83119 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| afc7ef4e-b824-35be-9fcf-74683cbe771e | -12.45973 | -50.78897 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e40ae5d1-a6d2-3013-be84-1b30a7dffca3 | -15.64376 | -52.73166 | 2026-09-17 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a15f6f3-425e-3f8a-94b1-b166aef9dc27 | -12.47298 | -50.81275 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dc3450c3-707c-3207-afcd-a297614c836e | -12.45751 | -50.78141 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf9c68a9-a005-3280-85f0-8c0385e41ab5 | -15.65158 | -52.72558 | 2026-09-17 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e4b3140-2702-3369-8905-34996c678fee | -12.4603 | -50.8071 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2238c5ab-7f51-3ea2-865a-9458847e3824 | -12.37391 | -48.46228 | 2026-09-17 04:42:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b23cb5ae-a5c0-3d80-b05b-eae0be57cd23 | -12.47957 | -50.79216 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c88374eb-e393-3a5b-9a71-da0c22e33f27 | -12.44158 | -50.81852 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f1e827ae-35d8-3b02-8398-b83f2a9c081e | -14.22838 | -48.51668 | 2026-09-17 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f6c0a4d0-6df8-3182-86b4-b69b62a4900a | -12.99346 | -46.92941 | 2026-09-17 04:42:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6866a067-06f9-3d87-a201-5a6381b09c47 | -12.64024 | -54.70617 | 2026-09-17 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 191cc8b9-302f-32de-9e1d-e0c59ae17693 | -13.68188 | -48.5935 | 2026-09-17 04:42:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 35917e21-2211-36c6-98a5-7b406e4cc4e5 | -17.77472 | -46.47788 | 2026-09-17 04:42:00 | NOAA-21 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 33e56e16-7b19-3666-89b6-bb15ef035dfc | -12.44819 | -50.81958 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 98d5f732-c1df-30d2-8647-9fda7d25e12a | -12.44491 | -50.84068 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 447c5fe5-8660-3171-85f3-28904393a4e9 | -12.46413 | -50.78247 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 12.0 |
| ff2ce397-7279-3a4c-b5e8-1d280137aa9b | -12.45373 | -50.84931 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 115c9e16-a550-33f5-b69f-e6f43b03762e | -12.44327 | -50.85123 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fecbada2-a2f6-301c-a9b7-7f9c8c56a25b | -15.83881 | -56.19938 | 2026-09-17 04:42:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7a6d1b58-3760-31d9-b42b-f4c4ef0e5bb7 | -12.70873 | -48.27629 | 2026-09-17 04:42:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aec7332c-7cc4-3078-a7f6-ebee9f87d9d4 | -15.47665 | -53.78331 | 2026-09-17 04:42:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 29f7ff7c-cbaf-3bee-b891-6649a6e53add | -12.44983 | -50.80903 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c9cb98ca-8f0d-37a3-9916-092d66dcffa2 | -12.47347 | -50.76595 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a4c6b39-7e64-324d-8783-139250022b87 | -15.48846 | -53.79728 | 2026-09-17 04:42:00 | NOAA-21 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76aa26fa-244c-30d9-8a7f-6ef5d51f4f4c | -15.83758 | -56.19723 | 2026-09-17 04:42:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 18c964db-ab4a-34eb-bba7-926161167cce | -12.78208 | -51.27405 | 2026-09-17 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8cc24823-8d3d-3931-8cf0-ca2b04e61958 | -15.64825 | -52.72501 | 2026-09-17 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a8ff17f-213c-363d-991f-44d8564f23c2 | -12.45592 | -50.83524 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b3814cfd-bfb7-378c-9f37-51e0eccc73f7 | -12.45868 | -50.83929 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README50.md)
