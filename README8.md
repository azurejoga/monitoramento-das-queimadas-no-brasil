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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a04d23ad-1931-3fb4-84fc-3c11f1c6cb04 | -3.25303 | -47.53582 | 2025-06-08 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 280f7a50-dcf8-3d71-b083-5e1a6aab5b1b | -5.77818 | -43.62067 | 2025-06-08 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f6159155-1e75-3dfb-b2cf-f460246f4350 | -6.4488 | -45.72988 | 2025-06-08 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1e60ebe-7687-35bb-bdb9-4527251e9a2a | -6.231 | -48.539 | 2025-06-08 04:23:00 | NOAA-20 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 506fa69d-8648-3477-a1b1-bc1d566d460d | -6.40816 | -43.64007 | 2025-06-08 04:23:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa733c47-71a6-303f-891d-093e65cac294 | -7.01978 | -44.58612 | 2025-06-08 04:23:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c0a177c1-fbdf-3d4a-8835-a2f50742aec4 | -6.44548 | -45.72937 | 2025-06-08 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc01c876-0411-3dd3-a933-f05f3416ad6c | -6.20278 | -43.3246 | 2025-06-08 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bed033ce-25e7-34f2-8690-b1d5ec8dd1fc | -4.33917 | -46.37785 | 2025-06-08 04:23:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 139c6025-f8e9-3d6d-a5e6-c16c76237be7 | -6.44934 | -45.72641 | 2025-06-08 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3243a2ef-15ff-3d6d-867c-b0f407d0b04e | -3.25585 | -47.54015 | 2025-06-08 04:23:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8930c221-2d9b-383d-88d1-20ecaff28fc2 | -6.66166 | -47.732 | 2025-06-08 04:23:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b035962-bbdc-30ba-9286-3eb8958da610 | -6.49554 | -47.4968 | 2025-06-08 04:23:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 369f781e-e19c-3563-915d-94eba02b8465 | -3.72154 | -49.07948 | 2025-06-08 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 31bec439-438a-3be7-8b59-2aa50f2247c9 | -5.63631 | -43.7224 | 2025-06-08 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dc4c0918-3fa1-3b43-aed7-c12250f95f05 | -5.77468 | -43.62012 | 2025-06-08 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7a89ac77-fa92-37c8-9579-3baf51ed4ff2 | -7.02148 | -44.57505 | 2025-06-08 04:23:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 702e4827-5403-381d-a05f-3f2899e42f33 | -6.53202 | -45.69665 | 2025-06-08 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 39ba9c7f-532c-3938-9a15-bbffec340b9d | -4.4213 | -47.66393 | 2025-06-08 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 152a6d88-263b-3a74-bd0f-8059d859552e | -7.12438 | -43.66116 | 2025-06-08 04:23:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 610f3474-da73-3aef-b91e-487c6f8c6db5 | -3.7252 | -49.08008 | 2025-06-08 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 07620992-f3cb-3d75-8746-2ab5e22e6a79 | -4.41788 | -47.6634 | 2025-06-08 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c6ca8af0-025c-3312-a3ab-8d6963159469 | -6.44825 | -45.73335 | 2025-06-08 04:23:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65736937-49b0-3f50-8563-2e21c0f06459 | -4.48709 | -43.77406 | 2025-06-08 04:23:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a1952f18-bcdc-3d3a-a46f-2ca694b262b6 | -2.91913 | -48.23392 | 2025-06-08 04:23:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a1043750-9fa2-3f2a-93d8-9ab6375c5f7b | -6.20217 | -43.32865 | 2025-06-08 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 641d41b2-a391-38cf-a72a-d79bf664ad78 | -7.0215 | -44.59769 | 2025-06-08 04:23:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4bbc4910-d6f6-3d0b-a8b3-35eac770e33b | -7.01922 | -44.58981 | 2025-06-08 04:23:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| eecd154f-4553-3b5f-9fc1-5571dd2cbd2d | -3.984 | -48.41367 | 2025-06-08 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3cc93e0d-1f92-33e6-9551-8b45733018c2 | -6.63874 | -47.34522 | 2025-06-08 04:23:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 27476a99-f55d-3190-a574-954950a40f37 | -6.49611 | -47.49324 | 2025-06-08 04:23:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fcf5f06b-6721-3d1b-b642-7d00feccc35b | -4.60452 | -38.52703 | 2025-06-08 04:23:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |
| c6727f52-8608-3f7e-8d97-3626b074af22 | -4.20277 | -47.53918 | 2025-06-08 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c60b594f-a0dd-3faf-a6f2-cb31abee6052 | -5.78167 | -43.6212 | 2025-06-08 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2297459d-baf5-3998-ab65-7b0e417aaf84 | -6.49667 | -47.48969 | 2025-06-08 04:23:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 51165d4e-13cf-33af-8834-202134202604 | -5.57419 | -45.20022 | 2025-06-08 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 260697e7-0fc8-373e-9aee-1eca73c8568d | -7.12612 | -43.67368 | 2025-06-08 04:23:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 965aacf2-ea97-3b16-af22-53be6feba405 | -4.60924 | -38.52774 | 2025-06-08 04:23:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |
| b1a21749-ee0a-37b1-a6d0-62a3980de56d | -7.02546 | -44.57188 | 2025-06-08 04:23:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 67060b22-3bbe-3999-a6e8-fc5effa9ed07 | -4.60378 | -38.53204 | 2025-06-08 04:23:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 994de815-3c27-39b2-8950-596290fb2aa5 | -5.77937 | -43.6129 | 2025-06-08 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d9fb760-75d7-386b-adda-2a6134b18d94 | -3.04396 | -49.43599 | 2025-06-08 04:23:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f698f6a1-a910-3ec7-9e36-54136e5a0387 | -9.40223 | -48.44292 | 2025-06-08 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| baf06d5b-f7a9-338c-aff4-8d4cf9f42dd5 | -7.73935 | -44.18353 | 2025-06-08 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aaa7636a-2eca-3bef-bc0d-f15c932de0bb | -11.80293 | -48.08925 | 2025-06-08 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 45b70753-2d3b-3ccd-ae29-4aec79669428 | -12.5281 | -58.34475 | 2025-06-08 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e2afcc2a-758f-352b-aef7-064134593787 | -13.18971 | -43.55314 | 2025-06-08 04:25:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8b556594-4bfc-3c76-8a1b-e582f6789efc | -11.37877 | -56.54857 | 2025-06-08 04:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d512fb5-c712-349a-badd-11026633e301 | -13.06563 | -49.23995 | 2025-06-08 04:25:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c910017-6554-380c-bdc6-05abd09a06b0 | -7.73066 | -44.17035 | 2025-06-08 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8e48a77d-3d5f-30d4-b2b7-06ec6c164ed9 | -12.53049 | -58.36417 | 2025-06-08 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9c9bbea-871f-3400-b3f7-726a1136e883 | -8.5242 | -50.02583 | 2025-06-08 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6fb3852b-9b1c-39a8-9e8c-78661296ad5f | -12.52135 | -58.34945 | 2025-06-08 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7683218a-7166-33e8-afe0-aed6cf9c807f | -9.40502 | -48.44712 | 2025-06-08 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 2a71c5aa-3a50-3a01-a804-3e01ee5b9ea2 | -12.98472 | -47.12051 | 2025-06-08 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a48d1cf6-ef4c-3185-9e2c-3f78c1df2874 | -9.0198 | -47.87932 | 2025-06-08 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1b7cb56d-3dbd-3643-b790-77ad0b9a3a08 | -9.38944 | -48.41468 | 2025-06-08 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a9d0bfb-f3c8-31d2-86a6-2b945e53283a | -7.86661 | -47.89177 | 2025-06-08 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa0b8e70-55fd-3de2-bdb2-54a4998d8222 | -9.05591 | -47.91082 | 2025-06-08 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41cfcdec-d4b7-319a-b454-63ab61cb1193 | -11.6269 | -48.48756 | 2025-06-08 04:25:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4728006b-8543-37e2-8b79-751df8d90429 | -9.4131 | -48.44846 | 2025-06-08 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 35c5e377-8f5a-3b37-b097-ae56c0352fc4 | -8.59015 | -45.86802 | 2025-06-08 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05f7372e-7bf0-3cac-abf0-34add906082f | -11.54288 | -56.45565 | 2025-06-08 04:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 84ef72f7-844d-3d6d-ac52-97881d4a24f8 | -9.50765 | -47.39841 | 2025-06-08 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04f75afd-960f-3c3f-9332-e430373ee786 | -12.96333 | -46.75116 | 2025-06-08 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11f67864-afb9-30cf-8fa2-ebe26c0037d1 | -10.29799 | -57.13563 | 2025-06-08 04:25:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dea21ded-3c7f-3d79-8757-76d3f39a5ecb | -9.84022 | -48.60373 | 2025-06-08 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| daa12516-38cb-31ce-bbdb-6c7ea954e077 | -8.52491 | -50.02161 | 2025-06-08 04:25:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 46104517-8bc4-3cc8-9d3f-208783719e23 | -8.40794 | -47.04991 | 2025-06-08 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9aed41cb-f5f2-38ee-b75f-0850a2e34cc2 | -11.44176 | -49.10734 | 2025-06-08 04:25:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4efa56fe-a490-3877-930a-9c4a5afd319d | -12.37455 | -57.40717 | 2025-06-08 04:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 26480a64-1f97-3a65-bd23-7fea09b4453e | -7.73356 | -44.17475 | 2025-06-08 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 80ffe448-0061-3065-928f-1fa122a032e2 | -7.73415 | -44.17088 | 2025-06-08 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 228dc33d-f465-3e13-8823-9eeee7fa860e | -12.52471 | -58.36147 | 2025-06-08 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e0ae173c-29ad-348e-b89d-c48c21f544d5 | -8.54785 | -48.26056 | 2025-06-08 04:25:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 620991ca-c013-38bc-8fea-080d56909506 | -7.73876 | -44.18738 | 2025-06-08 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c1a1332f-172a-3d8b-b5cd-c797abb748c0 | -12.94889 | -46.75611 | 2025-06-08 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3bbaea2c-b601-3178-b368-8d958bce7ddf | -12.98581 | -47.11343 | 2025-06-08 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0de52eb0-d492-3563-954f-ac0fa8bfeb06 | -10.23203 | -52.23841 | 2025-06-08 04:25:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c5a046d6-f529-318c-ba00-d54c61b4b296 | -12.37528 | -57.40348 | 2025-06-08 04:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2dcbcd33-fc4d-3b11-8793-539dbcc50e2b | -7.86604 | -47.89536 | 2025-06-08 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5cb5a1e3-6b65-3171-b271-05f0d0b91e82 | -7.86781 | -47.89541 | 2025-06-08 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eba44863-086d-30ac-af58-bbd422d190a2 | -12.51805 | -58.3663 | 2025-06-08 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f89e3ddb-662a-3ed8-b8ab-335de3d13b32 | -12.52714 | -58.35055 | 2025-06-08 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e94a5c11-7e55-329b-a9c0-4fe2459971d7 | -11.79297 | -48.08762 | 2025-06-08 04:25:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5004822c-b421-381f-b203-68dad12e984a | -7.82202 | -46.50146 | 2025-06-08 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 48358822-be09-3136-b426-d9189849ce47 | -11.3889 | -54.77242 | 2025-06-08 04:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d70d338b-125f-3136-9dc2-89707b1b61f9 | -12.98139 | -47.11998 | 2025-06-08 04:25:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7df0800d-a742-365c-9ad8-478bbc534bff | -13.95327 | -43.52007 | 2025-06-08 04:25:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ba8e7e00-a9d1-3326-a014-b40d1b9965b3 | -9.40119 | -48.42779 | 2025-06-08 04:25:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3ed888a7-067a-3bb5-be0e-d86641ecf623 | -12.37842 | -57.41327 | 2025-06-08 04:25:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5d0db600-dae3-3bbb-bbef-272de849e4f3 | -12.66105 | -58.21701 | 2025-06-08 04:25:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0df46ec-7bf1-3ea5-b517-65ca9be55828 | -7.72718 | -44.16983 | 2025-06-08 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f3f42130-dae0-32a8-b14d-4ceb4e9ea785 | -10.64316 | -47.47796 | 2025-06-08 04:25:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 26189a36-bf62-3f6f-990c-a6cacded717c | -11.36598 | -56.56341 | 2025-06-08 04:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1ef2bd7-9c09-38dc-9524-2c9f0d429f96 | -12.77902 | -48.71829 | 2025-06-08 04:25:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84161fc2-86ea-3a1c-bfcf-32aeb3b0d755 | -11.54226 | -56.45892 | 2025-06-08 04:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f1945e24-9c05-3328-a561-3ad65ec1abc8 | -7.81495 | -46.56785 | 2025-06-08 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 978c0661-7efb-322b-9be7-72ec903200e0 | -11.38983 | -54.7674 | 2025-06-08 04:25:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1a7aa325-7f63-3ecd-98ab-707eac7e7d9d | -11.36661 | -56.56004 | 2025-06-08 04:25:00 | NOAA-20 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README9.md)
