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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e82e4ae-505d-3316-bece-6ce23ef1e9d9 | -9.1117 | -45.752 | 2026-09-17 03:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 56.9 |
| f9f7e41b-e809-32f9-8e4e-64544d6f388c | -9.6091 | -45.3544 | 2026-09-17 03:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| fabd0869-706e-3c6e-bfa2-4dd3a8cb0e3a | -9.6277 | -45.375 | 2026-09-17 03:40:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 31166a0f-a71c-35f2-b591-ebc493decf1b | -8.4982 | -57.6468 | 2026-09-17 03:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 6c350446-f28f-3af0-a53e-3ab79b77eae7 | -9.1123 | -45.7067 | 2026-09-17 03:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 150.4 |
| 5894feba-3d06-3e45-b3d4-d8f75e18b6e4 | -3.4757 | -54.7171 | 2026-09-17 03:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 1a53c7a7-6c9c-347a-b0f0-5ea886053caa | -9.131 | -45.7273 | 2026-09-17 03:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 77cea1b1-13f6-3a04-a84f-b27b83bfa905 | -8.4983 | -57.6271 | 2026-09-17 03:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| ccdc632d-dcfb-34a2-82cc-cc19aa76d653 | -9.0931 | -45.7314 | 2026-09-17 03:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 52.3 |
| e20d19f7-0883-3c11-9855-c57708633944 | -21.46193 | -48.67526 | 2026-09-17 03:40:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bc768fd5-82d4-3085-99ce-34fcae9d795f | -21.46012 | -48.68242 | 2026-09-17 03:40:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 4b9f0e33-fa0b-38f3-8d01-d7afc2f98886 | -8.4796 | -57.6478 | 2026-09-17 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 2529511c-1ee7-3205-a3d9-5f11f772a7cf | -8.4982 | -57.6468 | 2026-09-17 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 6bba10cf-8981-3395-9f0b-dc0b08208aa1 | -11.8941 | -47.5876 | 2026-09-17 03:50:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 0b5f0cad-1837-3184-a67d-4ff11aed3d87 | -8.4797 | -57.6282 | 2026-09-17 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 0d138f43-8b4e-3f39-89f4-f17111274eb9 | -0.91307 | -47.21089 | 2026-09-17 03:53:00 | NOAA-20 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b0b6708-aab6-3b16-80ab-92e21c72279a | -5.45557 | -44.96206 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c3b7b8d-888c-3256-b54b-a621afc46a2a | -5.73603 | -43.27822 | 2026-09-17 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7408044a-ab2b-33b9-9763-1081b903f7ae | -6.82249 | -41.11312 | 2026-09-17 03:53:00 | NOAA-20 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3cd17ff3-17f2-3bd7-8a85-e1136f284ed8 | -5.76014 | -45.10629 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48f6a2f0-8329-3be8-9135-22c3465075c9 | -6.12946 | -43.74928 | 2026-09-17 03:53:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 546a3376-3d01-3c15-b92b-3c7de21d718f | -6.04168 | -44.03567 | 2026-09-17 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| b3a8af84-cc5a-3456-b44b-42b382115d70 | -6.94004 | -41.68727 | 2026-09-17 03:53:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4fc34c13-1577-3a72-95f9-7d4eff4c1d57 | -5.46107 | -44.96004 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 86b267ab-c642-3aa3-9187-2a0a39e98b79 | -5.64684 | -44.80773 | 2026-09-17 03:53:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| b610377a-4277-37e4-aa37-78987e559141 | -5.98199 | -46.62944 | 2026-09-17 03:53:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c2ff986-1db0-3be0-ae40-7b2078fc291c | -6.03831 | -44.03816 | 2026-09-17 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f11632a5-c8c6-3460-935e-2b2fef3dba25 | -4.55603 | -42.9466 | 2026-09-17 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 584dc9a1-7246-33f0-9d4a-f7de143016b9 | -6.16575 | -43.35974 | 2026-09-17 03:53:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ffbd831c-1127-3cc0-a20c-d0cdfe4fcbd2 | -7.4403 | -35.24811 | 2026-09-17 03:53:00 | NOAA-20 | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0e6599d5-4d9d-3c01-9db3-492b0f225996 | -5.29162 | -43.63837 | 2026-09-17 03:53:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 33024650-0ea6-363e-b3cd-bddb1716aabf | -5.4783 | -45.12831 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac7a468c-b167-3e3b-8ff2-3dd92a0d2a82 | -5.76384 | -45.11176 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9f3af1d0-acb4-3cdd-87e7-dc88701f1aaa | -6.57735 | -34.98523 | 2026-09-17 03:53:00 | NOAA-20 | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6ddd8ce6-07b4-3de6-b328-a17766807734 | -5.80797 | -43.72995 | 2026-09-17 03:53:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 765bb7e9-87f1-3b08-944b-2d659d0df4a9 | -5.75985 | -45.10506 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| bad434f8-e98c-3374-b40c-c2149cbe9675 | -6.16617 | -44.62018 | 2026-09-17 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e06f9fd0-a3f0-3b13-9df0-158a43da3300 | -7.33537 | -38.13844 | 2026-09-17 03:53:00 | NOAA-20 | ITAPORANGA | PARAÍBA | Brasil | 2507002 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 19b81c3f-7103-3a7d-afd7-5106e6b9ad63 | -5.46088 | -44.96204 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 47cbbf5a-0aca-3248-a6e3-1358a1f63e40 | -6.51559 | -44.04854 | 2026-09-17 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bfbd8092-95dc-3b98-832d-e3ed143a59ee | -5.61797 | -45.24819 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 440f4696-a4fd-32e7-8409-c5adbd51a346 | -5.58025 | -42.73235 | 2026-09-17 03:53:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ea31a383-6979-3d9f-8af0-32847c9fb84d | -4.35888 | -47.77928 | 2026-09-17 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b4299e0b-66f8-339b-b8ef-f9634fb609af | -5.76782 | -45.11854 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1c1d7178-c6f2-347d-b39d-ca1445539772 | -5.76992 | -45.10659 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 5b06e3d8-6d0f-3c36-90ee-60eafdd39201 | -5.45588 | -44.96119 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6aecaaee-be6a-336d-b9af-138044c66da0 | -6.32372 | -41.76112 | 2026-09-17 03:53:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c26dda79-d704-3bee-b030-e241f40944c7 | -5.73687 | -43.28039 | 2026-09-17 03:53:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2c359b8-5a32-3a6e-85f6-c08aa834f5a6 | -5.46181 | -44.95582 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 174f0241-1b89-370f-83f5-3d02e82b456e | -4.58043 | -47.16344 | 2026-09-17 03:53:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2aa582b8-d0c8-3285-bec8-8c6641113765 | -5.13553 | -35.59984 | 2026-09-17 03:53:00 | NOAA-20 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d98d1c1b-449c-3456-be4e-c3d701ce54f2 | -4.94487 | -42.91484 | 2026-09-17 03:53:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f8493ca-d78d-396f-95c7-81e1da0365f3 | -5.76939 | -45.10958 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 5d7cf3a9-601c-38ff-bdeb-98c77cdb461c | -6.93198 | -41.71128 | 2026-09-17 03:53:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e75eae9f-d7ab-31af-b874-8deffebaafaf | -6.78341 | -41.46782 | 2026-09-17 03:53:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 3f009824-f10e-392b-8d91-9986bbe58548 | -5.61637 | -45.24554 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4f57dee7-a631-3c7e-9243-2e69f67ae5f6 | -4.34095 | -46.61995 | 2026-09-17 03:53:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f20902d-c7df-3ef9-b778-29c3910db0de | -7.37924 | -38.9805 | 2026-09-17 03:53:00 | NOAA-20 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| caf29cd2-90a5-3150-a62e-1d61423ec3ed | -5.45608 | -44.95917 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be80e569-4813-3cab-8495-d9b4c77bab96 | -6.93452 | -41.69615 | 2026-09-17 03:53:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1b753ee7-3738-3fdc-9d1f-63b04d3f2858 | -5.86511 | -41.35788 | 2026-09-17 03:53:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6e6d777f-a69c-3c34-a6ed-b25dcbd3820c | -4.84624 | -37.44949 | 2026-09-17 03:53:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 9099be87-933b-3d69-8721-537b2b7ea232 | -6.82784 | -41.10437 | 2026-09-17 03:53:00 | NOAA-20 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0adcbb23-2860-308c-8864-492a369aac20 | -5.87677 | -41.36003 | 2026-09-17 03:53:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 47ca6b99-adf8-3484-a467-864e17fca8c8 | -6.76505 | -42.77722 | 2026-09-17 03:53:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b699953a-a93b-3f23-8462-48d3a4c3712c | -7.37643 | -38.97628 | 2026-09-17 03:53:00 | NOAA-20 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6745be4d-bd60-3a1c-802b-ad9ccbade612 | -4.33525 | -46.61909 | 2026-09-17 03:53:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 16df4f0b-55b0-3a35-acbd-ba9c84df4fcf | -6.93369 | -41.70108 | 2026-09-17 03:53:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| a604997f-9a0f-3789-b95e-f5d894170428 | -5.61744 | -45.2513 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2249dafa-d462-3080-b8b0-866afb2be2bb | -5.77496 | -45.10733 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 70f09b90-feff-345b-8ffa-9fa9dd84d592 | -4.54649 | -42.94934 | 2026-09-17 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| cb6c7065-7f70-332b-a9df-95c9976dda13 | -7.36841 | -38.98261 | 2026-09-17 03:53:00 | NOAA-20 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c4a54caf-bd06-38b7-99d8-40acbe5dd00a | -3.14428 | -40.71864 | 2026-09-17 03:53:00 | NOAA-20 | MARTINÓPOLE | CEARÁ | Brasil | 2307908 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| fd737554-357f-3e0a-901e-9d80123f1263 | -5.76436 | -45.1088 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 13c0fb5e-90e2-3f4a-b20a-4b6d0a36495d | -5.76064 | -45.10333 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b0139c64-98fd-311a-b59c-25a23da1999b | -3.5457 | -48.18365 | 2026-09-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 52c776ce-5a13-378e-b940-5034a0c03cdf | -5.77338 | -45.11634 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| e5b65228-0416-3f56-867c-d42e4f095c1d | -4.84014 | -43.55514 | 2026-09-17 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 687c049e-aaab-3537-9d01-8e8767798bb5 | -4.9085 | -37.42024 | 2026-09-17 03:53:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 862503fc-ed92-393d-8c07-09dc3202f708 | -5.67355 | -44.82971 | 2026-09-17 03:53:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8fba2183-87ae-39c6-af92-b1d5b0d05c6e | -6.94621 | -41.69849 | 2026-09-17 03:53:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f71f55d8-807b-3e22-955d-a391b71b52a3 | -5.46557 | -44.96375 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dcf69b1d-29c8-3245-af98-0d1257706ff2 | -5.32262 | -43.40177 | 2026-09-17 03:53:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c72c4836-02a1-3c75-a706-c015ba40d052 | -4.35808 | -47.7838 | 2026-09-17 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8678e497-e77c-3190-a921-708b40230a2c | -3.54661 | -48.17843 | 2026-09-17 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c212102d-3b35-30b3-b40a-e9924ddf19c1 | -1.78234 | -47.83895 | 2026-09-17 03:53:00 | NOAA-20 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec8462ae-3c0f-36f8-ba19-fd0139a8005c | -6.31457 | -40.14996 | 2026-09-17 03:53:00 | NOAA-20 | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a9940af9-6f3c-34e5-9972-358315e2ff11 | -7.365 | -38.98206 | 2026-09-17 03:53:00 | NOAA-20 | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c67c450d-8046-333b-b0dd-1885390e65a4 | -4.33593 | -46.61518 | 2026-09-17 03:53:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bbd4c300-27ce-3e4a-9dce-7b9540d3fef1 | -6.0391 | -44.03346 | 2026-09-17 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 22f2312e-009c-3032-bef8-abb3d5f5c825 | -5.47777 | -45.13137 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35f4b096-2039-38d4-a521-7f7a75140a5e | -5.75964 | -45.10921 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ebcc31b6-fba7-3f5a-a9cb-0f150b14b966 | -6.9359 | -41.71198 | 2026-09-17 03:53:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 345b7958-a97e-32be-a4cc-f770dd2418ff | -5.48281 | -45.13236 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46da2f8c-4843-3119-afff-fef06df0c745 | -5.77549 | -45.10433 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 2cf185a0-783a-3846-9365-d2fb05a25e0a | -5.45684 | -44.95486 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4dcf4819-a73b-330c-b71c-df163166a7e1 | -5.75933 | -45.10799 | 2026-09-17 03:53:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f82072dd-d913-366a-83a2-218175393ccc | -6.82327 | -41.10842 | 2026-09-17 03:53:00 | NOAA-20 | FRANCISCO SANTOS | PIAUÍ | Brasil | 2204204 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7e24356c-9093-39bf-bd46-9c3c671e1583 | -6.99611 | -40.33816 | 2026-09-17 03:53:00 | NOAA-20 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 64001e0e-2036-37ee-8b51-9af2e816e5ed | -3.76008 | -41.03102 | 2026-09-17 03:53:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |


[Clique aqui para ver as próximas entradas](README20.md)
