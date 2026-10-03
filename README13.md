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
| 37961125-6ae1-37ab-ba09-09b8ab8a5898 | -5.9571 | -43.6467 | 2026-10-03 01:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| d1769c0d-925b-3e35-8852-17d65cafba00 | -5.7376 | -45.1533 | 2026-10-03 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 5c4ea858-6729-31b9-895a-f398ac7dd130 | -3.1299 | -53.7633 | 2026-10-03 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| b128cc54-a849-3271-9ab4-9e686ac550e9 | -3.2951 | -53.8395 | 2026-10-03 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 6546d48e-d8aa-385d-9dda-8cfa5a2d5fdb | -3.1838 | -54.104 | 2026-10-03 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 4fd75e2c-bac5-34cc-b8cf-b4f9143a4a2b | -3.2767 | -53.84 | 2026-10-03 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 659d2cc1-d7df-305a-ac72-d816910852a4 | -5.6134 | -44.3876 | 2026-10-03 01:50:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| d916b06a-7d9f-37f3-9d8c-2430a3743759 | -3.2952 | -53.8194 | 2026-10-03 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| d97e7d7b-8b90-31d9-9f04-f2aa4f75df0f | -3.13 | -53.7229 | 2026-10-03 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| fefbf13c-1a9c-3fa0-8ace-9f437a878f98 | -3.1116 | -53.7436 | 2026-10-03 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| c5b1b3cc-be10-388d-88bd-5d351a963122 | -5.9384 | -43.6482 | 2026-10-03 01:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 400712aa-209e-3db4-b11b-3438a2b17e59 | -3.2768 | -53.8199 | 2026-10-03 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 94513be2-a6bd-3f94-9516-35c93cebb1b2 | -10.9881 | -59.1197 | 2026-10-03 01:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 55.3 |
| d4228258-faef-3a93-ac1e-d160385092d9 | -5.9381 | -43.6714 | 2026-10-03 01:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 9ed7ed6b-277e-3a12-824e-ac5d53699b89 | -3.1299 | -53.7431 | 2026-10-03 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 168.8 |
| 6728403c-b1d1-342a-a7b1-876b6c3d26a7 | -3.1655 | -54.0844 | 2026-10-03 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 911b866e-dff0-3d18-b7dc-3018b9481299 | -5.9569 | -43.67 | 2026-10-03 01:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| ea0524a5-a754-3426-bff8-e5c421a51bb8 | -3.1839 | -54.0839 | 2026-10-03 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| b5c3a8b9-959d-3563-8860-00065fe84cca | -3.1483 | -53.7426 | 2026-10-03 01:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 67b80424-e128-3e87-b2d8-87273a53046f | -5.9381 | -43.6714 | 2026-10-03 02:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| f76509ae-6de4-3f1a-9645-63fc2a320c60 | -5.9384 | -43.6482 | 2026-10-03 02:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 75e172d3-af89-3c66-b7d5-2d3ded519159 | -3.1116 | -53.7234 | 2026-10-03 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| b7ecba1f-e7e0-30a3-8caa-eac5fac832a2 | -3.1655 | -54.0844 | 2026-10-03 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| e2c06807-7c43-3989-b555-72f921d1c3da | -6.9295 | -49.6325 | 2026-10-03 02:00:00 | GOES-19 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| bbb4bd5b-1ac7-3e51-93d6-da1fa8950f58 | -3.2767 | -53.84 | 2026-10-03 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 113bcb2e-c100-3844-a14e-c6cf2013fa1f | -3.1483 | -53.7426 | 2026-10-03 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 49d098a5-eef3-3aac-8c89-f7b6c61d1bb6 | -5.9569 | -43.67 | 2026-10-03 02:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 4f456c8f-3b5c-3af6-84f5-4d6fd1a5d028 | -3.1299 | -53.7633 | 2026-10-03 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 5cb5cced-1fca-3662-8781-f70fade4f389 | -5.7376 | -45.1533 | 2026-10-03 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 7a744796-9bee-342f-8a50-85a82f0f749d | -4.4506 | -47.9329 | 2026-10-03 02:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| b3f20178-659d-3629-8319-dae4a61556d0 | -5.9571 | -43.6467 | 2026-10-03 02:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 4aba66f1-be3e-3503-8dd3-ea5a0824b60f | -3.1839 | -54.0839 | 2026-10-03 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 88584794-634c-3f6f-ad2e-64289735ff20 | 1.7854 | -55.6054 | 2026-10-03 02:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| f98027ef-afb4-3817-ae28-3e9208f8a5ca | -3.2952 | -53.8194 | 2026-10-03 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 5760c88e-2b74-3b60-93b7-95f6e34f9ec1 | -3.1299 | -53.7431 | 2026-10-03 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 150.3 |
| b33f4848-952f-33fd-9113-b77a21f3339c | -3.1116 | -53.7436 | 2026-10-03 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 87bb1f06-65d2-36b6-93b6-d1f552c0946d | -6.4933 | -58.5242 | 2026-10-03 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 83.9 |
| e6c3f267-b541-37f5-b414-1bbda1f88b19 | -3.2951 | -53.8395 | 2026-10-03 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| a72c68f3-0ecc-33b7-94dc-1c0c2509a71a | 1.7854 | -55.5856 | 2026-10-03 02:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 529a305b-cb91-367a-92b6-e30d72e5b1a5 | -3.13 | -53.7229 | 2026-10-03 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 6b503303-73e2-35c4-8eee-c60d33a541e6 | -3.2768 | -53.8199 | 2026-10-03 02:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 6f99d44d-eb95-39f9-9b58-7ffeda4b78b6 | -2.8897 | -54.1313 | 2026-10-03 02:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 52e56073-704d-335d-a04e-ed9d36a421ba | 1.8037 | -55.5854 | 2026-10-03 02:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 1d468131-4ae9-3d98-b184-28b7bb848366 | -5.6134 | -44.3876 | 2026-10-03 02:00:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 2433ffcf-e376-3010-9da6-00d470c65c90 | -10.9879 | -59.1393 | 2026-10-03 02:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 31706430-05bc-3728-b5ca-325c844da163 | -3.1116 | -53.7436 | 2026-10-03 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| d3028cc1-822a-3f0c-8921-8d63517196fb | -3.1116 | -53.7234 | 2026-10-03 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 575e7d9c-b423-3704-8ba0-4bec74f5ff04 | -3.1839 | -54.0839 | 2026-10-03 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| dbc4da00-a84c-3aa3-9a06-71b2c5a5ca0b | -3.2767 | -53.84 | 2026-10-03 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 0af14426-744e-382d-975a-6ee65cc989bf | -3.1299 | -53.7633 | 2026-10-03 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 6e1ee272-0d10-3c90-8c31-70af7e89a1b0 | -3.1483 | -53.7426 | 2026-10-03 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| ccf6005d-2b2f-36b5-bb3a-0583f0121822 | -5.9381 | -43.6714 | 2026-10-03 02:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| d939af99-c5c7-31e3-965e-b08ef99e20bd | -3.1655 | -54.0844 | 2026-10-03 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 4039aa6a-28e9-3d3a-ab2c-1f224a44c722 | -3.2768 | -53.8199 | 2026-10-03 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 91dc4022-83fd-3d3c-8bd9-1a7a43960148 | -3.2951 | -53.8395 | 2026-10-03 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 973ae140-5a39-386f-afaf-9696e6a8950d | -5.7376 | -45.1533 | 2026-10-03 02:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| b47df114-ea57-3d5a-8335-3c24740bbf62 | -5.9569 | -43.67 | 2026-10-03 02:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 2aac9ff0-d620-3860-a45c-4fb600adf1d2 | -5.9384 | -43.6482 | 2026-10-03 02:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 117.9 |
| ed8f0ee0-c454-33c7-b644-2bef1d1e25e1 | -3.1299 | -53.7431 | 2026-10-03 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 163.1 |
| 5d9bd516-02b0-3f5b-b86b-b1774c03a4b0 | -2.8897 | -54.1313 | 2026-10-03 02:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 8cd2c622-0978-3c20-802d-bf724ee3903b | 1.7854 | -55.5856 | 2026-10-03 02:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| baa666a4-d001-3e97-867d-94b49bfb2cbe | -5.9571 | -43.6467 | 2026-10-03 02:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 37d9a0e6-068d-3bc2-b8fa-11736712d443 | -3.13 | -53.7229 | 2026-10-03 02:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |
| f241e9db-e29b-3e21-8bcb-49a55b2eaa8f | -5.9571 | -43.6467 | 2026-10-03 02:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 005c5f45-bfb7-3798-8ac1-fa11936e7956 | -5.9569 | -43.67 | 2026-10-03 02:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| c0f5d36d-18e6-3047-b4a2-7af1ab3a0b6d | -5.6134 | -44.3876 | 2026-10-03 02:20:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 71b0bc65-d07c-38fc-9477-76ad6d11afdc | -5.9381 | -43.6714 | 2026-10-03 02:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 0412899c-bdd2-3a2d-9d80-c789aa39c9e7 | -17.3989 | -40.0451 | 2026-10-03 02:20:00 | GOES-19 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 79.7 |
| 0b2ffd88-a9a1-3fbc-ab92-0dbb1a37eead | -3.1299 | -53.7633 | 2026-10-03 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 780efec3-d7de-3ac3-8c67-3806fb6dae1c | -3.2767 | -53.84 | 2026-10-03 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 14a7d929-b615-3db6-a015-49e9fd12e599 | -3.1483 | -53.7426 | 2026-10-03 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| fa107a53-42f5-3852-b77d-d0afbb59288f | -3.1299 | -53.7431 | 2026-10-03 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 165.3 |
| 0d9d3937-8de5-332c-9bda-31986836b2d5 | -17.3996 | -40.019 | 2026-10-03 02:20:00 | GOES-19 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 120.1 |
| 2d3e0201-79dc-3f5e-a84e-2a4315ab3f8d | -10.9879 | -59.1393 | 2026-10-03 02:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| fec7f60d-91f6-38c7-a790-0d8f7fc23fa4 | -3.2768 | -53.8199 | 2026-10-03 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 974f5221-59e4-3a91-adfa-073765880c73 | -3.13 | -53.7229 | 2026-10-03 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| e652ff87-a8ec-39e9-8c7d-453ac2b7057c | -5.7376 | -45.1533 | 2026-10-03 02:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 10ca5db8-a940-3f04-860f-c3dd4975f0e4 | -3.1116 | -53.7436 | 2026-10-03 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| bfea15db-9600-3a74-8c38-6f3261608b7b | -3.2951 | -53.8395 | 2026-10-03 02:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 63b25d5f-089c-3d64-84a4-7ca654a75f11 | -6.4933 | -58.5242 | 2026-10-03 02:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 827df2a6-16e1-3986-8006-bf503596894f | -2.8897 | -54.1313 | 2026-10-03 02:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 5926207b-e5a0-3b8d-ac4d-b9fddc76e2d8 | -5.9384 | -43.6482 | 2026-10-03 02:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 117.3 |
| bcc2f31d-6758-303a-ab0d-e7b5d1962e9c | -3.2767 | -53.84 | 2026-10-03 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 2b9d4a86-dfbc-310e-9bd6-65a58c322d58 | -5.9571 | -43.6467 | 2026-10-03 02:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 87a1c7ef-9053-361a-8eed-32600e9c9cd0 | -6.4933 | -58.5242 | 2026-10-03 02:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 496ee0fa-f385-39b0-ab0a-c2e573df7518 | -2.8897 | -54.1313 | 2026-10-03 02:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| e650d3a4-e2db-3814-811d-b17e444609fe | -5.9569 | -43.67 | 2026-10-03 02:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 5bbdba32-bd51-366e-998b-8c87f78ceaa7 | -10.9879 | -59.1393 | 2026-10-03 02:30:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| c1fac8fe-8eab-3f60-b533-502642e3a8ca | -4.4014 | -49.9677 | 2026-10-03 02:30:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| aba1bfcc-cce4-39a4-b821-904ab52137cb | -3.2952 | -53.8194 | 2026-10-03 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 449b3c7b-60bb-3cfa-97ca-125d3ca91ac3 | -6.9295 | -49.6325 | 2026-10-03 02:30:00 | GOES-19 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| bbb42d7d-bf60-392b-a99c-86a2c5e1342a | -3.2951 | -53.8395 | 2026-10-03 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| fb306108-aece-3b6b-9c2f-de684a8d40f3 | -3.2768 | -53.8199 | 2026-10-03 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 95f8a3f8-b57f-3551-8bc5-61f897e21b79 | -5.9381 | -43.6714 | 2026-10-03 02:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 190ecb73-d0e4-3a23-a72d-d3bd52839389 | -5.6134 | -44.3876 | 2026-10-03 02:30:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| a92d3395-e23a-325d-93ca-8e081c8fb7e7 | 1.8037 | -55.5854 | 2026-10-03 02:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| e83100e8-9e15-3b79-a433-3ce5dc66fb31 | -3.1839 | -54.0839 | 2026-10-03 02:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 3dff7725-5e7f-3374-8bb7-bc2ef99dc168 | -5.7376 | -45.1533 | 2026-10-03 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 99.2 |
| cbe95d4f-1b28-3c4b-be12-63e676913715 | -5.9384 | -43.6482 | 2026-10-03 02:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 5855ecb2-0521-3c5b-9d40-2f2ee596d388 | -5.9569 | -43.67 | 2026-10-03 02:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 84.2 |


[Clique aqui para ver as próximas entradas](README14.md)
