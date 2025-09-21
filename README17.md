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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09b718a4-101e-3b7f-b51c-03ea607f5bf9 | -12.13454 | -44.29848 | 2025-09-21 04:10:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d6dae2eb-fc3a-3447-ab08-4d86ceb066a6 | -13.36287 | -44.28451 | 2025-09-21 04:10:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dc408b53-e4a0-3b29-997c-4f897b347d8b | -12.43475 | -45.10751 | 2025-09-21 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e79b4ff1-ba3c-34d2-9078-f6cecaacc858 | -14.21231 | -44.65702 | 2025-09-21 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b1ee1490-3bee-3aa5-86e5-5650d7e91cac | -14.52404 | -44.87132 | 2025-09-21 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b8e6f7f-0f93-366e-8621-56dd7055c54b | -12.71817 | -46.86353 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea3cf9da-57dc-38cc-b6ad-bdb646cee799 | -17.35741 | -46.81791 | 2025-09-21 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b38e4d80-5d87-3fc7-9416-55c4968e83fe | -13.5419 | -43.00152 | 2025-09-21 04:10:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 55a27210-0b75-3637-9d55-7d42805b6c07 | -11.42892 | -47.32341 | 2025-09-21 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0b321e52-2290-3bfd-9f85-c08ca9221cdb | -17.16511 | -46.83495 | 2025-09-21 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92a09d96-e381-3bcf-8d9d-4de23e2eaf73 | -14.7913 | -51.3621 | 2025-09-21 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2175195c-f9ff-3b65-834f-190b705fbac6 | -12.07356 | -44.82291 | 2025-09-21 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8b2c1f71-a476-303b-8567-21155247aa6a | -14.45689 | -46.5129 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f4d60a99-eb93-34ff-b947-7a21e3a1431d | -18.66519 | -46.54118 | 2025-09-21 04:10:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d2b5deb-24ac-3cdc-8f6d-83158e19dd87 | -17.99148 | -44.04358 | 2025-09-21 04:10:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 392125f8-248b-32f0-bdf9-7b7346da9c01 | -12.07389 | -44.84235 | 2025-09-21 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6db39b80-ff4a-3a4a-a472-22f0ae6d265f | -14.4684 | -46.50496 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2a873243-cef2-355a-8678-9286e90c3e34 | -12.38931 | -45.83895 | 2025-09-21 04:10:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 71b3196b-16d5-3fb1-bc19-ac0935cd6a20 | -12.43095 | -45.13052 | 2025-09-21 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 437d3dc0-e35a-3398-8025-cd2c28a292ce | -11.62719 | -50.59807 | 2025-09-21 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 576a0e06-5b23-344e-8e4b-bdf86f67f15c | -11.62143 | -50.60247 | 2025-09-21 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5177567a-282d-3002-8906-7844c07564be | -11.61088 | -50.606 | 2025-09-21 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3a85dd3d-f001-30bf-909d-02c5315ce932 | -18.97566 | -41.09571 | 2025-09-21 04:10:00 | NOAA-21 | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 652f7d80-5ae8-37a1-9aed-a45672c4f42a | -13.53915 | -42.99746 | 2025-09-21 04:10:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 13.9 |
| b50081fd-314f-3661-b34f-4855e6cfcf24 | -16.208 | -46.68967 | 2025-09-21 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 96ab55f6-6bc0-3662-b77e-7e8608a03db7 | -14.94735 | -42.36951 | 2025-09-21 04:10:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 20c14b4e-7de3-3228-90c5-4524bde2ad4a | -15.99873 | -47.27099 | 2025-09-21 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1050201d-bad8-3bd9-b0bb-61cbfcd3f6a0 | -11.64772 | -52.86594 | 2025-09-21 04:10:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 89907c90-eeef-3fa8-bfb0-d53d04a27cb7 | -15.90814 | -43.04628 | 2025-09-21 04:10:00 | NOAA-21 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 116b90bd-6fdc-3950-94a9-167720eb6ee4 | -14.43462 | -47.56938 | 2025-09-21 04:10:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6000542f-e31b-3c4c-b2ef-031ea2614b28 | -14.9833 | -41.37094 | 2025-09-21 04:10:00 | NOAA-21 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 66046422-2542-32d3-b56c-dc8f1985937c | -14.43357 | -46.52079 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 08db43df-2780-3959-90d8-2ca4192c9201 | -15.99511 | -47.27031 | 2025-09-21 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f0ad00c9-0978-3adb-b2f2-cea3bd109bc7 | -19.22747 | -43.7648 | 2025-09-21 04:10:00 | NOAA-21 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ad473097-86ba-39ad-b27d-69e596750542 | -14.29316 | -47.41661 | 2025-09-21 04:10:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 074515d7-4691-3e00-8ac8-7035ae172331 | -11.61381 | -50.59008 | 2025-09-21 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 479b6243-a345-36aa-a865-756dfccefc31 | -17.63907 | -44.1876 | 2025-09-21 04:10:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ebd382a2-fb9f-3581-8d2b-53e7ab7cbeb5 | -14.47546 | -46.50653 | 2025-09-21 04:10:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0e56b43b-e57f-38da-b9d8-8a48ee51e9bd | -16.20728 | -46.69389 | 2025-09-21 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 588567e4-1151-3154-b1f9-011c379a0cc4 | -11.30972 | -47.50054 | 2025-09-21 04:10:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 973a0c8c-537a-3954-bdfc-47f9176bef6f | -12.71445 | -46.86298 | 2025-09-21 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7efe9647-08c2-3e63-9f21-ff2679f96f1e | -17.44464 | -44.79466 | 2025-09-21 04:10:00 | NOAA-21 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54d61b03-a9a3-35a4-9bca-7402d7e9cf02 | -11.42977 | -47.31847 | 2025-09-21 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5ce99e0a-eced-3aec-a00e-79df24a56319 | -18.90318 | -44.28287 | 2025-09-21 04:10:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c448da68-1ddc-34b0-8fc4-8928fc243c72 | -17.09647 | -45.94774 | 2025-09-21 04:10:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90df56c7-4335-3640-9062-3945c8e42b19 | -12.08227 | -44.85541 | 2025-09-21 04:10:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6db7c6de-6820-34fa-a970-79257fea8131 | -16.6031 | -45.09474 | 2025-09-21 04:10:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16d539da-482c-325c-842a-37f91504f87f | -12.33752 | -44.09827 | 2025-09-21 04:10:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c903e3c3-e65e-34ef-8b32-f4cf1618ceeb | -15.69365 | -46.99279 | 2025-09-21 04:10:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eebe7d48-adb5-334a-b920-f6007276002f | -23.29605 | -45.51537 | 2025-09-21 04:12:00 | NOAA-21 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 419f7041-7363-3d42-9eae-520d41a2bcdb | -20.13798 | -42.4866 | 2025-09-21 04:12:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| fd6244da-426b-3e17-89dc-64698b981863 | -22.47642 | -48.21833 | 2025-09-21 04:12:00 | NOAA-21 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45ca22a2-324c-3993-91c8-9fb6d392f74f | -22.71823 | -51.41964 | 2025-09-21 04:12:00 | NOAA-21 | PORECATU | PARANÁ | Brasil | 4120002 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 5c49484e-245a-3349-b81c-593b1c211237 | -23.15638 | -46.64902 | 2025-09-21 04:12:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 78e2488b-b0de-32e4-b2f9-c3284e9b8057 | -22.27568 | -56.01752 | 2025-09-21 04:12:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3befec32-0eb0-3b38-a43a-226c0ec2473d | -21.15857 | -44.38334 | 2025-09-21 04:12:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4ff66a8b-5fed-3739-bb6e-a6a0c38b101d | -23.29079 | -46.67795 | 2025-09-21 04:12:00 | NOAA-21 | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 180b3d6e-6747-308c-a446-0261f22a85cb | -23.37753 | -45.42952 | 2025-09-21 04:12:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bc446aa7-b6ad-38f8-a417-c0fc9af8a2bb | -20.1276 | -42.48495 | 2025-09-21 04:12:00 | NOAA-21 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4c7449be-ba68-3476-8c4b-185b0f8d8679 | -20.45041 | -45.24271 | 2025-09-21 04:12:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 80c931a6-490e-3e43-98ee-8451a9339ae2 | -23.4176 | -45.71771 | 2025-09-21 04:12:00 | NOAA-21 | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 6d619918-41ad-3892-93df-7194ec818a8b | -22.6558 | -43.97768 | 2025-09-21 04:12:00 | NOAA-21 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fa371581-7669-34d5-aaf7-7e4619bbeaa5 | -23.33439 | -46.95001 | 2025-09-21 04:12:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 91c19987-dadb-3923-96cb-86366f81e0ac | -23.22587 | -47.02927 | 2025-09-21 04:12:00 | NOAA-21 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 890bbb8f-3580-38ab-9519-f2d2a726a5a6 | -22.46941 | -48.21696 | 2025-09-21 04:12:00 | NOAA-21 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 3f6b29f3-7b3a-3fe0-b535-0efbf0ff1ab2 | -18.7491 | -53.32875 | 2025-09-21 04:12:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1032e2f-911b-38b4-9284-35ffd0753b38 | -24.96548 | -48.58321 | 2025-09-21 04:12:00 | NOAA-21 | BOCAIÚVA DO SUL | PARANÁ | Brasil | 4103107 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dc9ffb2d-26b6-37b8-85af-0d88e2596ce1 | -22.63383 | -48.25323 | 2025-09-21 04:12:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f6e5aa76-447e-3849-8a31-03c6465aac97 | -23.22252 | -47.02862 | 2025-09-21 04:12:00 | NOAA-21 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 257c38e6-c377-30fe-a05c-8ed74d9298b1 | -21.21396 | -44.6212 | 2025-09-21 04:12:00 | NOAA-21 | NAZARENO | MINAS GERAIS | Brasil | 3144508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 59810a7f-482a-3dd7-8f0e-e5b89854dfb7 | -23.36724 | -47.14793 | 2025-09-21 04:12:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 724bcd1a-1b95-318a-b8f1-dc1168321b0c | -23.14966 | -47.62706 | 2025-09-21 04:12:00 | NOAA-21 | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 67313f87-23f4-3153-9132-d376e0b2189a | -23.97517 | -46.47025 | 2025-09-21 04:12:00 | NOAA-21 | SÃO VICENTE | SÃO PAULO | Brasil | 3551009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4ac0b6a6-de78-32ce-8747-e91504b99e9b | -24.96899 | -48.5836 | 2025-09-21 04:12:00 | NOAA-21 | BOCAIÚVA DO SUL | PARANÁ | Brasil | 4103107 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f599cc5e-a9ca-34e7-ae0c-ef2dafebbae0 | -22.63032 | -48.25259 | 2025-09-21 04:12:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4119ab9f-7dc1-38e6-aa3c-e3c39a1bdb52 | -19.83542 | -57.30075 | 2025-09-21 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c25ba98e-69e0-3676-b0c4-83070583475b | -19.84516 | -57.29841 | 2025-09-21 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 3b127297-a09a-3c81-97a1-5e1674da1125 | -24.79441 | -49.46655 | 2025-09-21 04:12:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 8d930978-fc4e-3f4d-adf8-b463581ac0c9 | -23.13705 | -47.24099 | 2025-09-21 04:12:00 | NOAA-21 | INDAIATUBA | SÃO PAULO | Brasil | 3520509 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 355cac14-a9ff-3226-8e46-44f096235d6f | -19.74508 | -49.65592 | 2025-09-21 04:12:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 82cb55b4-30e0-32bf-aa04-f788d28b762f | -19.73583 | -50.18183 | 2025-09-21 04:12:00 | NOAA-21 | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 42e952ef-bab7-3e35-af6e-ce2c409d47f5 | -23.73644 | -54.93504 | 2025-09-21 04:12:00 | NOAA-21 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c290e7e6-452b-31ac-976c-dbb8a7fd9d9c | -23.34523 | -46.88468 | 2025-09-21 04:12:00 | NOAA-21 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 80de09b4-7d00-36c0-bbc4-48d0783d701d | -22.96696 | -46.5745 | 2025-09-21 04:12:00 | NOAA-21 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d6076704-3fad-3910-8504-754423f63235 | -23.32386 | -46.91692 | 2025-09-21 04:12:00 | NOAA-21 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| ba2e1605-1264-3853-88c5-ec69618b2831 | -23.41562 | -47.61556 | 2025-09-21 04:12:00 | NOAA-21 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| b0f97383-51c7-339f-be46-8f78a23ba6ea | -22.47091 | -48.20844 | 2025-09-21 04:12:00 | NOAA-21 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9946d6ea-d8fa-31af-a1a2-845073f23942 | -22.91311 | -43.48401 | 2025-09-21 04:12:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 17751461-51f5-3bf0-853c-a80644529360 | -22.63661 | -48.25809 | 2025-09-21 04:12:00 | NOAA-21 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7bfea501-6dda-39f1-b22b-24c46264bf5e | -23.4757 | -47.27681 | 2025-09-21 04:12:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 67dbfef2-95b9-3287-aafb-6a4f73888faf | -21.759 | -45.09831 | 2025-09-21 04:12:00 | NOAA-21 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 920d7fed-f505-3fc1-a50c-36ddd326ea1f | -22.47716 | -48.2141 | 2025-09-21 04:12:00 | NOAA-21 | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e2019e8b-486d-3100-b6f1-beb58e02d660 | -23.41902 | -47.61619 | 2025-09-21 04:12:00 | NOAA-21 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 9ea1298d-adee-363e-893c-db7a820b8560 | -20.6058 | -56.71706 | 2025-09-21 04:12:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 27dd2185-db5c-3a2e-9323-22facfdf90f6 | -23.16534 | -46.61092 | 2025-09-21 04:12:00 | NOAA-21 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 831203db-d27a-3368-b36b-f6d2827fe696 | -20.24753 | -44.36173 | 2025-09-21 04:12:00 | NOAA-21 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| ad02dfeb-3a1e-3e79-851e-ab55ec544599 | -21.11927 | -42.9879 | 2025-09-21 04:12:00 | NOAA-21 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ea12a086-a9e2-3635-beee-4e11cfdd8e76 | -23.4231 | -47.61282 | 2025-09-21 04:12:00 | NOAA-21 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 06ba602d-6f93-31dc-94a4-0b06c7d03eb4 | -23.26562 | -47.52534 | 2025-09-21 04:12:00 | NOAA-21 | PORTO FELIZ | SÃO PAULO | Brasil | 3540606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 46401606-11b3-3876-a8ff-2567512585a7 | -23.43462 | -47.60689 | 2025-09-21 04:12:00 | NOAA-21 | IPERÓ | SÃO PAULO | Brasil | 3521002 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |


[Clique aqui para ver as próximas entradas](README18.md)
