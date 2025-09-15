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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7e9e5ca-bcef-3c7b-b938-b629da2a526c | -7.8945 | -43.5623 | 2025-09-15 01:20:00 | GOES-19 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 183.6 |
| 7e038541-f1c5-3715-8c2a-7e18ffc71aba | -7.9819 | -45.6657 | 2025-09-15 01:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| c9b6e2a2-6553-392f-bc7e-0d0dfab99bf1 | -12.006 | -47.7505 | 2025-09-15 01:20:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 83.0 |
| b4dbe36d-d3e8-3bf8-9fa9-56464fbf16d6 | -12.1861 | -44.0958 | 2025-09-15 01:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 4a7551bd-1a1e-3052-9adb-f03f5e32c575 | -10.9365 | -45.5063 | 2025-09-15 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 54.6 |
| b3d89163-bef6-3163-a797-ba9d164d0bcf | -12.1668 | -44.0988 | 2025-09-15 01:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 129.0 |
| 83a44290-299f-33f5-81a5-2e49bee2f240 | -7.9819 | -45.6657 | 2025-09-15 01:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 82cf50a5-3f2d-3405-ba43-598a85ad824e | -15.7985 | -53.4582 | 2025-09-15 01:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 45146d1d-6e0a-30b9-8b61-9adf19e603e7 | -12.1663 | -44.1224 | 2025-09-15 01:30:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 4558c7b9-b715-3850-b50d-3fae92d77852 | -17.3435 | -42.6581 | 2025-09-15 01:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 24bb69c9-999b-31ce-a29c-01843f8f4440 | -8.9787 | -45.8118 | 2025-09-15 01:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 5ee8c7a8-3768-33cf-b0be-07afbe96da16 | -11.7916 | -50.4592 | 2025-09-15 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 2ad762f9-db34-382a-9ad4-3981537a4b20 | -11.7919 | -50.4378 | 2025-09-15 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 50f678f1-d3ea-395c-b1d3-1c5fa36de4e7 | -12.006 | -47.7505 | 2025-09-15 01:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 5964ee3b-a150-3160-baa9-8f119d3c035f | -12.6636 | -54.6782 | 2025-09-15 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 58.5 |
| bceb9da9-2115-3b0a-8d6a-9ed16332e9fa | -15.779 | -53.4608 | 2025-09-15 01:30:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| b1fd3632-8042-346b-9c4e-6b2206092d22 | -17.3442 | -42.6333 | 2025-09-15 01:30:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 102.6 |
| b1973e37-c36e-31a2-9de0-f705fc26377c | -11.8478 | -50.517 | 2025-09-15 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| f7498de5-b948-3836-bec4-2716f7a94990 | -12.6633 | -54.6988 | 2025-09-15 01:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 8fbe1ea2-8097-30ef-93f2-ae3316dc49b1 | -18.0502 | -50.935 | 2025-09-15 01:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 1b9d4dd6-49a1-398f-a137-2543ed29e893 | -17.3435 | -42.6581 | 2025-09-15 01:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 4787a652-006f-34b0-8a62-6dc528be07ab | -12.5607 | -45.639 | 2025-09-15 01:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 6738efbf-32a2-3304-bcdd-fe24c54f8f85 | -18.0303 | -50.9385 | 2025-09-15 01:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 28c40941-708d-31e9-8ffa-1f5dee2b11d3 | -11.8297 | -50.4548 | 2025-09-15 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 76fe060a-a10d-306a-abde-a2ae55c1a686 | -11.8669 | -50.5147 | 2025-09-15 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 7509dadc-8d8d-3585-8b72-7347a72e2bf6 | -15.7981 | -53.4793 | 2025-09-15 01:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 108.8 |
| 04fffd1e-144c-36f5-b369-30c43dc6a453 | -6.1065 | -43.7045 | 2025-09-15 01:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 0405d9bc-42cb-3638-b03b-e9054c597dbc | -6.1063 | -43.7277 | 2025-09-15 01:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 590623c2-1aff-332b-b4ed-d90b8386607d | -11.8475 | -50.5384 | 2025-09-15 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 50.7 |
| cc7dd3f3-c672-3b25-91bc-2dd9b3e2866f | -7.9819 | -45.6657 | 2025-09-15 01:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 412cd658-f43a-32c4-a592-ae7c97a40555 | -15.7985 | -53.4582 | 2025-09-15 01:40:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 131.2 |
| aca6187a-b993-3588-9090-6b896a444dc8 | -11.8107 | -50.457 | 2025-09-15 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| b613bf6f-9274-3ba8-8a40-dd3331847c72 | -11.811 | -50.4356 | 2025-09-15 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| c73e2ca5-ddc0-374e-b9f4-56308af82884 | -11.8665 | -50.5362 | 2025-09-15 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.1 |
| bf3fec87-5f6e-374d-ad50-0ac00929baa0 | -12.006 | -47.7505 | 2025-09-15 01:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 01ef3c67-7f0b-3757-a7fe-b35634e987cc | -17.3442 | -42.6333 | 2025-09-15 01:40:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 4d2e304a-1906-3457-af3d-d39cba54b2de | -11.7919 | -50.4378 | 2025-09-15 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 40217322-8eff-3306-9085-1e2d2973029a | -12.6636 | -54.6782 | 2025-09-15 01:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| f66b8606-ba3e-328c-af55-72f5f1dad289 | -11.6957 | -50.5131 | 2025-09-15 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 4ccfaf47-440e-3858-9fc8-cb338c4b8a90 | -11.811 | -50.4356 | 2025-09-15 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 83.4 |
| 64df3799-ce5e-3131-a63b-23dcbc5060b3 | -15.7985 | -53.4582 | 2025-09-15 01:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 93.3 |
| d2b9d3e6-a3b8-392d-81ae-4b06c9ff22a8 | -17.3435 | -42.6581 | 2025-09-15 01:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 70.2 |
| a578d317-5244-39b6-8c40-bc4d51c3cbdf | -12.006 | -47.7505 | 2025-09-15 01:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 174fe86d-bab8-38c9-abb2-455e0087ad9f | -14.4973 | -47.3336 | 2025-09-15 01:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 2ec80741-b397-3674-9092-dcc07d811eab | -11.7916 | -50.4592 | 2025-09-15 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| ab7a7ee2-77b5-3653-a976-671d5b15f894 | -11.8107 | -50.457 | 2025-09-15 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 3dd0cd41-48a3-3bdd-a3f3-9af7244e2737 | -15.818 | -53.4556 | 2025-09-15 01:50:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 81.7 |
| d6daa394-71f3-3417-9555-aec54eeb07ea | -18.0502 | -50.935 | 2025-09-15 01:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 0af7e455-bbaf-39d8-be50-ae3fbd8aa58d | -11.7151 | -50.4895 | 2025-09-15 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 79975fbf-df3f-3a84-83d0-5737031bda79 | -12.0055 | -46.6537 | 2025-09-15 01:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 38.5 |
| dc052795-1e11-3bb8-b346-00490494fd6b | -10.6889 | -50.6658 | 2025-09-15 01:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 4f3be42c-508c-37b0-a83d-6313a991f4e4 | -11.7529 | -50.5065 | 2025-09-15 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 8d97c896-f9c8-3f70-a917-d6d09403681c | -11.8669 | -50.5147 | 2025-09-15 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 3a2bc7d1-f326-3bff-8b14-16fddf33d128 | -10.6892 | -50.6445 | 2025-09-15 01:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 10c23c9b-daa9-3ade-99e5-81e7bd7c04ca | -11.7919 | -50.4378 | 2025-09-15 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 88403248-447b-382f-80b4-9ba1238dfabf | -10.7078 | -50.6638 | 2025-09-15 01:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 123.2 |
| a4d74200-b91c-356f-82fd-cdfe1e577200 | -17.3442 | -42.6333 | 2025-09-15 01:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 34324eab-d0f3-35ad-8037-d8069b5a1150 | -10.7268 | -50.6618 | 2025-09-15 01:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 770f1a65-ab09-3aa4-b90b-60b832c4c16e | -11.8297 | -50.4548 | 2025-09-15 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| e2904525-44b1-3d85-800c-462c0bb4154d | -10.7081 | -50.6425 | 2025-09-15 01:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 5065fbc5-ea9a-3565-9a6f-e025be8c9c69 | -11.8665 | -50.5362 | 2025-09-15 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.4 |
| ebff1a30-b3a6-32cb-8925-b92938933a6f | -6.1063 | -43.7277 | 2025-09-15 01:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| c596ec1c-71c5-3228-b512-3e69f245db82 | -11.696 | -50.4917 | 2025-09-15 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 784c1d68-1259-3ad3-a43a-aacfee9dcf53 | -10.7076 | -50.6851 | 2025-09-15 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 218c29b1-6a11-3dd0-bdf6-bad60c33aea4 | -11.7916 | -50.4592 | 2025-09-15 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| d97a2203-6c87-30ed-9de5-a17efdb0a5f9 | -8.9787 | -45.8118 | 2025-09-15 02:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 7c5f5435-ff07-35b4-84ec-cfecc798f7b0 | -10.6886 | -50.6871 | 2025-09-15 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 56.4 |
| b100132d-81d5-3701-b826-5571372c15f5 | -11.8475 | -50.5384 | 2025-09-15 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 6c41783e-1219-3ae0-be4f-bf15b1ac454c | -10.7078 | -50.6638 | 2025-09-15 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 195.5 |
| 334c96c5-13ae-3765-b651-75b8f9db2e15 | -17.3435 | -42.6581 | 2025-09-15 02:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 74.6 |
| c1610f56-8679-3d60-bb06-17d3e9affcb9 | -18.0507 | -50.9129 | 2025-09-15 02:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 340437e8-e9ea-3835-932a-53f0d38142c0 | -15.7985 | -53.4582 | 2025-09-15 02:00:00 | GOES-19 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 90.2 |
| e481b404-06e1-34f2-9536-e3065408b7d0 | -11.7919 | -50.4378 | 2025-09-15 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| f28ac0fc-dc86-3040-92b5-33e7512c56c6 | -11.8107 | -50.457 | 2025-09-15 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.2 |
| d98b01da-10b7-341b-a8df-854510510a27 | -18.0303 | -50.9385 | 2025-09-15 02:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 95.3 |
| d399f6e3-bc02-3d04-813f-5065035f5637 | -12.006 | -47.7505 | 2025-09-15 02:00:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 53d33999-cff0-34e1-bf2a-17b9ddc85697 | -17.3442 | -42.6333 | 2025-09-15 02:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 23a34128-b6df-3110-84c4-f8e4e2b12adb | -11.8665 | -50.5362 | 2025-09-15 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 6c063130-690c-3902-8493-f5a053c3d0d9 | -11.7759 | -46.663 | 2025-09-15 02:00:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 82197bce-017b-360a-bdce-885304d63add | -10.6889 | -50.6658 | 2025-09-15 02:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 0014225b-2b4c-3b3a-86c4-58e256565eca | -10.9365 | -45.5063 | 2025-09-15 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.4 |
| cc2ecc76-6c8e-3907-b615-b079f3713db7 | -11.8297 | -50.4548 | 2025-09-15 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 1791e6a3-0477-3877-a261-03bc8acd77b4 | -11.8669 | -50.5147 | 2025-09-15 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 1d3ef058-41e0-380e-a448-cd439a3ea8ac | -18.0502 | -50.935 | 2025-09-15 02:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 4141b0d8-7e1e-32f4-b5c1-78b8acd70e4e | -9.44528 | -67.14896 | 2025-09-15 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 8aed7e2e-41ff-3f15-a0f3-5638422da070 | -9.44271 | -67.13229 | 2025-09-15 02:09:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| d2119a1c-e6fb-3be8-96ce-a1372d66963c | -7.79341 | -66.93171 | 2025-09-15 02:09:00 | TERRA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| bfcbef0a-0f74-35ce-ae48-a0f07c7c2277 | -9.01493 | -67.49992 | 2025-09-15 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 1f894af0-62fb-3938-8a28-fecb3f546d05 | -7.79562 | -66.92567 | 2025-09-15 02:09:00 | TERRA_M-M | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 16.8 |
| b1fdd09d-8f84-3c24-bf1d-e8dd11d8b00a | -9.00338 | -67.50177 | 2025-09-15 02:09:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 8d7f010e-fe92-39ba-9a89-61e378afedc0 | -7.79737 | -71.99126 | 2025-09-15 02:09:00 | TERRA_M-M | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f703715b-dd1f-3787-8137-7b268fff18bd | -11.8475 | -50.5384 | 2025-09-15 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 580b120d-98e3-3b24-bc52-912dd74f9b7b | -17.3442 | -42.6333 | 2025-09-15 02:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 100.4 |
| de8f891e-3a2a-3831-8f08-b919d8444001 | -18.0303 | -50.9385 | 2025-09-15 02:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 153.4 |
| 8fd694d8-db35-3e91-a7d8-9637b5dc2fa6 | -10.9365 | -45.5063 | 2025-09-15 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 4528d65a-66c0-3ced-b3ea-61dc739c6882 | -18.0308 | -50.9164 | 2025-09-15 02:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 96.4 |
| e32657b0-97c7-352b-bda1-17d29591c7db | -11.811 | -50.4356 | 2025-09-15 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| e1d9a7de-eabb-39aa-a39b-49d7149f6907 | -18.0502 | -50.935 | 2025-09-15 02:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 259.0 |
| 6ad306b6-eb6a-3326-80a2-7a19bea37280 | -11.8669 | -50.5147 | 2025-09-15 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 35cdf590-529a-3342-ab4c-d3046645f06b | -12.006 | -47.7505 | 2025-09-15 02:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 77.1 |


[Clique aqui para ver as próximas entradas](README8.md)
