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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0a1dae7b-95ca-3257-9b22-227471915d43 | -13.84505 | -44.51542 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| b39f4501-b5e6-3b67-ae1f-f9b08b9d7468 | -13.84446 | -44.50776 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 847da9d3-4515-3bf8-a090-f1a8bcd0a0e3 | -13.84418 | -44.52026 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 88a7fb23-3e5a-33de-beb2-e84f547818ae | -13.84363 | -44.5456 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ce448f18-b38c-39b8-9e55-4c9d45a4baa1 | -13.84362 | -44.51265 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2bb55270-d456-3744-9f7f-66f080a27bf5 | -13.84332 | -44.52513 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c871bd07-b357-326a-9f3d-080359ceabda | -13.84295 | -44.50498 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb75cf22-3cb1-3fc7-a685-a96767d2ce3a | -13.84278 | -44.5175 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b69d89f-8d91-3410-a9f6-6a889160acf5 | -13.84244 | -44.53001 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c4f77846-2b4b-3568-98e4-76d21fafd032 | -13.84207 | -44.50985 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f68c8b0e-7abb-3b1a-bfd7-1be8ecf8b04f | -13.84195 | -44.52236 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 74ae48a7-a136-3335-8875-4c7a255a7bc4 | -13.84121 | -44.51471 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11dc0905-1142-3033-906e-c5b491f37aed | -13.84111 | -44.52725 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a08714f9-e6ec-392d-a852-668c0e037838 | -13.84034 | -44.51955 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4ef8bd39-14e6-30cf-bdd7-38a176a98c44 | -13.83979 | -44.54488 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a338e469-47fb-3fb6-a9f2-468f4876e74e | -13.83947 | -44.52442 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ecbb9a3d-d749-377d-8cf2-877a97dfe7df | -13.83894 | -44.51678 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 063012d1-bbaa-3b47-892f-6a0455094a61 | -13.8386 | -44.5293 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 92ae4e10-5bd0-36f3-bad7-a9ae4f042c25 | -13.83811 | -44.52165 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4ef7f40-2399-363b-9dc3-0281c5eaa46d | -13.83727 | -44.52654 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2d9cf939-d5e3-3429-ac24-44db7ad8bcfa | -13.8365 | -44.51884 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12d208b0-397f-3dd7-93f1-f09c27454385 | -13.83642 | -44.53146 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 429b699d-d2e9-32ad-915b-c6051aad1b5a | -13.83563 | -44.52371 | 2024-10-10 03:57:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03900573-4bbc-3305-815c-4d8b9044463e | -16.54221 | -45.26885 | 2024-10-10 03:57:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 511e8066-f5ad-32ae-8e54-352ff66babe0 | -16.54133 | -45.27386 | 2024-10-10 03:57:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18344921-780b-3d30-8123-1d2515529e38 | -16.54044 | -45.27888 | 2024-10-10 03:57:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d59711a4-3830-381b-8f60-8f02ef1122da | -16.53934 | -45.27056 | 2024-10-10 03:57:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 45fbd60b-f392-3ac5-8e33-a5327b467e5c | -16.53835 | -45.26812 | 2024-10-10 03:57:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1e044c8-fc41-3916-aad6-c63e178a269a | -12.98978 | -46.24051 | 2024-10-10 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3b65e3de-fca7-3be9-ad47-9e8871d07044 | -12.98892 | -46.2451 | 2024-10-10 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b4012e20-a204-36ac-9c2f-53c169d09e38 | -12.9886 | -46.24077 | 2024-10-10 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19e838b9-2c80-3817-9053-d0bf7c779d8d | -12.98778 | -46.24537 | 2024-10-10 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e42378e-27a4-3e93-baaa-78e5ad70c89a | -12.98618 | -46.2357 | 2024-10-10 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b0cb5a38-3f37-33a7-bdde-9d3b523e44d3 | -12.98497 | -46.23595 | 2024-10-10 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b29da075-4207-3908-91d1-ee1c02770108 | -12.98174 | -46.23537 | 2024-10-10 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f3238855-00b1-3400-8f57-2e1b77d53038 | -12.98088 | -46.23998 | 2024-10-10 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4af356a3-1aa0-36ac-b931-7bc5f7bcc0fc | -12.98056 | -46.21759 | 2024-10-10 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 73663e89-821b-3b2a-973a-80b06a0ebc39 | -12.98004 | -46.24449 | 2024-10-10 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25421098-d544-3de1-a1a5-8e3bcb700e57 | -12.98004 | -46.21328 | 2024-10-10 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6ac28b3a-072d-3aac-8f60-cc5bf1d1a22f | -12.97971 | -46.24022 | 2024-10-10 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f972478-d1ec-39fc-84c7-c29031930607 | -12.97924 | -46.21774 | 2024-10-10 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 64bf48dd-1fe3-30f4-bf2c-40bc58018f88 | -12.97892 | -46.24469 | 2024-10-10 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 11d8ce79-81df-3aa1-8d54-bc360445a67f | -12.97775 | -46.22609 | 2024-10-10 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f3a0456b-8ac9-3f87-bef9-4c6eeda7a3c6 | -12.97726 | -46.20377 | 2024-10-10 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 675042c1-a472-3a31-91f9-6ae406f7c856 | -12.97698 | -46.2304 | 2024-10-10 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 912d203a-0969-31ec-a1db-0f9e6dfa6a49 | -12.97648 | -46.23946 | 2024-10-10 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ada3f608-5ce4-3e6f-b4da-76e8197f5010 | -12.97645 | -46.20831 | 2024-10-10 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9fd4ca9d-2f72-3c63-b727-0640fa9affab | -12.97564 | -46.2128 | 2024-10-10 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d96ab343-4447-3056-a730-5078dc1df43c | -12.97486 | -46.21716 | 2024-10-10 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f5912c70-bb1e-3f11-8cfb-15cc16e27772 | -12.97334 | -46.22568 | 2024-10-10 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 9be86f5e-857f-3464-83ac-f3946a5255d2 | -12.97256 | -46.23 | 2024-10-10 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 32.0 |
| c0e95d1c-56f4-3afc-8ffc-d14bab881e13 | -12.57853 | -53.06866 | 2024-10-10 03:57:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6decf74f-df58-3b82-b8d9-56cf12a48fd8 | -12.5718 | -53.06728 | 2024-10-10 03:57:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 254eaf9f-5ae7-3446-8158-5705cb7a2771 | -12.97048 | -46.21658 | 2024-10-10 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b0cfa76c-b4f0-3de1-b05c-cb8ca40bb44d | -12.96972 | -46.22085 | 2024-10-10 03:57:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 8e4444a9-e1d6-3437-ba41-0ead7fef2b9d | -12.71279 | -45.46853 | 2024-10-10 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d0ab4ffb-7743-3c88-ac22-c9250abcb66a | -12.70934 | -45.46393 | 2024-10-10 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 3a6dd53e-52ca-34d9-adb8-f09277562628 | -12.70863 | -45.46781 | 2024-10-10 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7b9510a3-c5e7-30c3-93c8-9b9e34d976fe | -12.70793 | -45.47169 | 2024-10-10 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| eca23fa3-77ab-374c-b7f8-59fd36ce3676 | -12.70448 | -45.46709 | 2024-10-10 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b49bff0a-4663-3c22-85d6-5f66b7c4c0c0 | -14.20431 | -49.74632 | 2024-10-10 03:57:00 | NOAA-21 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0aaf7fed-0ed5-3374-8bfe-22c9cb819cce | -12.28166 | -46.78527 | 2024-10-10 03:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c6608fb-39f9-3957-b26a-f6d271e8ee5b | -12.20776 | -46.72291 | 2024-10-10 03:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c32aaf7-7220-34d6-9fa4-3a857f93cd83 | -12.20603 | -46.73241 | 2024-10-10 03:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad096f5f-916b-325d-aa88-8d3697459474 | -12.20322 | -46.72203 | 2024-10-10 03:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 984741ae-cbb1-3a76-be42-99a47c321a3a | -12.20235 | -46.72678 | 2024-10-10 03:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c0a2efda-67f8-374d-83eb-97f3b321095a | -12.20148 | -46.73154 | 2024-10-10 03:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 3df44da7-a035-33e2-96f7-31fb0d235cbd | -12.19961 | -47.15089 | 2024-10-10 03:57:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc96bd66-2697-39bd-90bf-284cb85cfca3 | -12.1978 | -46.72591 | 2024-10-10 03:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0270908b-7065-3f40-9394-bc80672c97b4 | -12.19693 | -46.73067 | 2024-10-10 03:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| fe7ad26f-e163-3a83-aa28-c430133f653a | -12.17538 | -47.57358 | 2024-10-10 03:57:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 56feefed-94f2-3ef9-afc6-f958e0bb914e | -12.17056 | -47.57269 | 2024-10-10 03:57:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 556c0d4c-50ff-3b1f-83c1-64fc8de51206 | -11.79401 | -47.38977 | 2024-10-10 03:57:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 30a0375e-bb90-3c9d-a11e-a33af62c2d4d | -11.7939 | -47.39325 | 2024-10-10 03:57:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 65ec608e-966a-3f98-9227-2eba0f90f22e | -11.79299 | -47.39516 | 2024-10-10 03:57:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e6bbb35e-19c8-3ab9-90ce-8e5f38b8a9b0 | -11.79008 | -47.38698 | 2024-10-10 03:57:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e329079e-5f38-3996-9ba9-656d5dc5b314 | -11.78921 | -47.38892 | 2024-10-10 03:57:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a483e6c9-8fa8-3f0f-bd34-d27615db1d7e | -11.78911 | -47.39233 | 2024-10-10 03:57:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| af273ccb-7cdc-3863-afff-9745d680d735 | -13.5017 | -47.98411 | 2024-10-10 03:57:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8cb9c023-e36c-37a0-b8b0-357025c6532f | -13.44364 | -46.71214 | 2024-10-10 03:57:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30617781-2d0c-36e6-9e54-946b1766ab8c | -13.44233 | -46.71025 | 2024-10-10 03:57:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d55bee91-b47b-39d1-be1f-11f614587895 | -13.40447 | -46.91071 | 2024-10-10 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d18399f4-027a-3fb0-8ab8-f98aa8771c92 | -13.40363 | -46.91516 | 2024-10-10 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 83d1f4cd-4c42-33ba-89a3-d2b04f7b345f | -13.40273 | -46.91244 | 2024-10-10 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a44285eb-2385-39e8-a13d-e7c57c780514 | -13.39026 | -46.70197 | 2024-10-10 03:57:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8477335a-93df-3a9e-8ed7-5cc8cec7822e | -12.48573 | -47.49747 | 2024-10-10 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e17e7ac8-6db3-3add-be1f-24a5fca547f6 | -12.48473 | -47.50282 | 2024-10-10 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1ad61b20-d6ae-3ab5-a179-a80972c8a746 | -12.47996 | -47.50191 | 2024-10-10 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 372a5303-b4d5-36a4-92da-7f70c3ae5be5 | -12.45744 | -47.30883 | 2024-10-10 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ba17ee35-ac26-3e4f-870e-0d093ed98d28 | -12.45646 | -47.31396 | 2024-10-10 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4de45cf1-ecbf-3319-be02-4d9100c53d31 | -12.45572 | -47.31032 | 2024-10-10 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6bc60ad9-a3d4-319b-8cbc-f9c92dc4ad6b | -12.45478 | -47.31548 | 2024-10-10 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d2aba127-f1e8-3d26-b267-435587189a8f | -12.28622 | -47.64269 | 2024-10-10 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fca09564-afe3-3b8e-870e-f43a4c80b4bb | -12.28463 | -47.64412 | 2024-10-10 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b373097b-9f72-3733-8cf4-37ed0c0d8527 | -13.6283 | -48.49063 | 2024-10-10 03:57:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85e60a27-92b3-303d-9356-85dace3a5608 | -13.62768 | -48.49389 | 2024-10-10 03:57:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6cc2e98c-cf0f-3f46-b75f-013b76a010ad | -13.6226 | -48.49341 | 2024-10-10 03:57:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1d0323d-49e8-3d2b-8140-4c31f69282c2 | -12.72446 | -48.42613 | 2024-10-10 03:57:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6d8aafa-18ab-31a6-a4c0-dd220892da5a | -12.71938 | -48.42532 | 2024-10-10 03:57:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffc82bde-1d3f-359d-b7ce-68258622a524 | -12.7188 | -48.42833 | 2024-10-10 03:57:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README54.md)
