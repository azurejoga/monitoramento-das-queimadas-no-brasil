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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eadd5884-046a-37fd-a278-c0c7aaacd3c3 | -4.53853 | -46.56443 | 2024-10-15 04:49:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd8fb0ee-d626-3e73-b53b-c2dbcc243e6a | -4.53572 | -46.58369 | 2024-10-15 04:49:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91650577-e2bc-3def-9e27-69eafa20a730 | -4.53518 | -46.58742 | 2024-10-15 04:49:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c06ca6ff-530c-3552-91fc-05a2fa65d376 | -4.52603 | -46.55476 | 2024-10-15 04:49:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 102c5d36-ddec-3ad8-9565-aaa8bb994c2e | -4.52544 | -46.55863 | 2024-10-15 04:49:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea842dc8-9090-36b7-a658-f6e24afa2463 | -4.47435 | -47.73736 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c293ee06-e8fb-3a0c-b035-aeaac9a2d656 | -4.47357 | -47.73523 | 2024-10-15 04:49:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ba8caeea-f9c0-35c8-b8ec-9d45b4014380 | -4.38219 | -46.73405 | 2024-10-15 04:49:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 681ceb8c-4143-3bc1-b550-86df42a88272 | -4.36316 | -47.27348 | 2024-10-15 04:49:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fa5eed36-9607-360c-b502-d60e9b98850f | -4.36265 | -47.27685 | 2024-10-15 04:49:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d0d64f8-3d6d-35fb-9d62-ef59a71bc35c | -4.36214 | -47.28024 | 2024-10-15 04:49:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41e77ae5-e0c9-34ce-bfde-8348015637ba | -4.35816 | -47.27961 | 2024-10-15 04:49:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe37f1d8-9dea-3413-b2cf-ff787f8b023f | -4.35418 | -47.27898 | 2024-10-15 04:49:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fbcc428-3ca8-3288-b844-699ae18b5e08 | -4.33642 | -46.70101 | 2024-10-15 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5cfadc6-9ed3-39c6-a342-ef41aae3d0e8 | -4.33606 | -46.7318 | 2024-10-15 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae9000df-fc8c-3270-85d0-85542a33b92a | -4.3355 | -46.73555 | 2024-10-15 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0203f31a-a385-396f-9bb1-c8590eef99ee | -4.33226 | -46.7005 | 2024-10-15 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 89ff021b-c6d4-3db3-b6b5-a900afdb3bfc | -4.31546 | -46.28939 | 2024-10-15 04:49:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aace127c-7a48-303a-9769-77807b878fe1 | -4.2698 | -47.00917 | 2024-10-15 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42cde9fd-30e1-371b-97ef-f156248d1f31 | -4.26927 | -47.01277 | 2024-10-15 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c7ab755-c32a-3257-a73d-f26b060e80ee | -4.15381 | -46.86759 | 2024-10-15 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b5159ff-11a6-3ea7-a2b0-6c6454ca6a73 | -4.15185 | -46.25864 | 2024-10-15 04:49:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e60edbe4-1847-3070-9b12-7793409b8cd3 | -4.14972 | -46.86703 | 2024-10-15 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5de17e58-6857-358f-a54f-aa24ede3f847 | -4.14848 | -47.18027 | 2024-10-15 04:49:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01a5dd60-d8da-3b26-9a2a-b25a4c1075e8 | -4.02702 | -47.21553 | 2024-10-15 04:49:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0423e28b-080c-32e4-830a-e3286a528d36 | -4.0265 | -47.21902 | 2024-10-15 04:49:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dc19764-4717-37ef-a3cf-075123c89ece | -4.01152 | -47.50705 | 2024-10-15 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a8ca964-3d0a-3166-80e0-5dbea28c501d | -3.97164 | -47.10801 | 2024-10-15 04:49:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43ec5d66-2cd1-307d-87a8-bee08f6f4906 | -3.9519 | -46.43821 | 2024-10-15 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |
| dbae50e2-3d30-3f34-9389-81b5725a6c20 | -3.95134 | -46.44192 | 2024-10-15 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 56af98fc-98d2-30bc-995a-d6b2a6ce266f | -3.9477 | -46.43765 | 2024-10-15 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71b15118-7f73-3a96-bf97-d0aa92fa6625 | -3.94713 | -46.44148 | 2024-10-15 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 60fe719c-b8ce-38ea-b167-85e37d791ccc | -3.94351 | -46.43706 | 2024-10-15 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ac194867-e42b-39a3-bf98-1c73dbc74324 | -3.93445 | -46.41148 | 2024-10-15 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7f197e0a-cec6-3e0e-bc1e-f79e35567cef | -3.93386 | -46.41549 | 2024-10-15 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| f2fd1659-311e-3bd2-b626-cb2d3fff5acb | -3.93025 | -46.41091 | 2024-10-15 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 65f9fc9c-f9eb-3d5a-ad37-c42bbb32d97c | -3.92966 | -46.41488 | 2024-10-15 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 1c1af6c3-f5cf-33f3-a6af-af86489f0ad8 | -3.90531 | -46.42718 | 2024-10-15 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa15d225-bc32-3f35-b3d7-6c5f84b7ab89 | -3.90228 | -46.4263 | 2024-10-15 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 93420f54-df0f-3917-8d28-d5f7355a8ffc | -3.90114 | -46.42642 | 2024-10-15 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df398e53-fa1f-3b52-840f-9b111ea9c7b4 | -3.87624 | -46.47735 | 2024-10-15 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c204a16-b670-3986-801d-b7c76f3f4165 | -3.87205 | -46.47682 | 2024-10-15 04:49:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5590abf-8b0a-3de1-9579-ee2aef10c72b | -3.85907 | -46.9187 | 2024-10-15 04:49:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfe2af12-a1b9-34f0-8af4-5ffb6fcc88ae | -3.85658 | -46.9076 | 2024-10-15 04:49:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 98e9aecd-0800-3b9e-867e-7f40a2664bfc | -3.85604 | -46.91122 | 2024-10-15 04:49:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7edc3ba0-66c6-339c-9880-6b25741aa407 | -3.85551 | -46.91475 | 2024-10-15 04:49:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a94f3661-26c5-3dd3-a7f7-aed42e581706 | -3.855 | -46.91823 | 2024-10-15 04:49:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 021a7c37-686f-3b97-a04e-6ad0da228079 | -3.85304 | -46.90351 | 2024-10-15 04:49:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c6564b35-4e1a-3c4e-9c7d-2be760f1f37a | -3.85251 | -46.90711 | 2024-10-15 04:49:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd28786b-7dfa-32f8-9a4d-eee56dc66e0e | -3.8499 | -46.92465 | 2024-10-15 04:49:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fdfbb841-103a-3171-9a08-31350f4a100e | -3.84899 | -46.9029 | 2024-10-15 04:49:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11deb5da-37b8-3b1b-b131-71f889abc1a0 | -3.84845 | -46.90651 | 2024-10-15 04:49:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aacd87a6-25e6-33b8-91cf-8f18e941ccfc | -3.84792 | -46.91008 | 2024-10-15 04:49:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f3561e21-8fec-3efa-ab85-535f8b336710 | -3.8474 | -46.91364 | 2024-10-15 04:49:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 969360dd-d515-39b1-9db1-276f72c97319 | -3.84584 | -46.92411 | 2024-10-15 04:49:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf6181d7-bc5b-3684-9f65-2a3d3b014208 | -3.84334 | -46.91304 | 2024-10-15 04:49:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04304baf-6dc6-3ead-a35c-d38ffbe1fbb9 | -3.8423 | -46.92008 | 2024-10-15 04:49:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f30bc4e5-1274-3114-bd86-6fd250deebe0 | -3.84179 | -46.92353 | 2024-10-15 04:49:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f8a5dcb9-d550-300c-8a13-e2a058b190b7 | -3.83929 | -46.91245 | 2024-10-15 04:49:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06e7cdd6-d3f6-3c8c-a8a6-d1c14290a26d | -3.83877 | -46.91597 | 2024-10-15 04:49:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a5d4682a-1015-367c-bd1f-1a81ce59df88 | -3.83524 | -46.91179 | 2024-10-15 04:49:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e289b2c-88e8-3ba7-b15e-7e025ab0018a | -3.83472 | -46.91144 | 2024-10-15 04:49:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28b9f190-3f38-3374-8f49-42258ad31a71 | -3.83174 | -46.90741 | 2024-10-15 04:49:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6419075d-d4b7-3b7d-8b8c-e3ac626a420b | -3.83125 | -46.90709 | 2024-10-15 04:49:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cac8cd06-f6d9-312f-9e7f-f3bcd17c252b | -3.82951 | -47.48992 | 2024-10-15 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 037b23f7-9d0a-3963-8d54-2f476f0e3d80 | -3.82875 | -47.4949 | 2024-10-15 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5aaddb0c-a6fa-3593-8825-03b610f69fd6 | -3.82723 | -47.50477 | 2024-10-15 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77f3611b-44fa-3145-9968-bab0f6c61144 | -3.82715 | -47.47932 | 2024-10-15 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b37b0929-7092-3098-9c71-deca63ff847f | -3.82638 | -47.48432 | 2024-10-15 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 017d8b2a-52ea-3c03-a70c-73f12ab61fa8 | -3.80293 | -47.48095 | 2024-10-15 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1baef3b7-e516-3647-8e0b-4c320b44e7f6 | -3.75881 | -47.50919 | 2024-10-15 04:49:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e3969b9-3ea6-3ae7-9472-81127db45859 | -6.07598 | -47.05692 | 2024-10-15 04:49:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d44a428f-363a-3b54-a101-f8fc392784fe | -6.07542 | -47.06069 | 2024-10-15 04:49:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a3605113-7c8f-374a-b43c-b27e12598d68 | -5.94488 | -47.62932 | 2024-10-15 04:49:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5c0f9de1-7716-30fd-99a6-92f3f5c0a131 | -5.60254 | -47.96149 | 2024-10-15 04:49:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ea6726d7-b926-320b-a853-050e4ad97aed | -7.87281 | -47.74775 | 2024-10-15 04:49:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a17dffd6-b3aa-34b3-ab2f-a320a5bcf05d | -7.46307 | -47.1791 | 2024-10-15 04:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a5144a7a-67ab-3af4-b3a3-13a315745667 | -7.46215 | -47.17931 | 2024-10-15 04:49:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 492f92bd-5bbb-3c33-afa5-d6f427955b0b | -7.45974 | -47.67413 | 2024-10-15 04:49:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 439ed425-ab10-38ff-81b1-162424ccaa9b | -7.45569 | -47.67343 | 2024-10-15 04:49:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0318d9df-cffe-3f9b-a96f-4f1564a03587 | -8.44707 | -48.03137 | 2024-10-15 04:49:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf986985-b4c6-3f29-ab36-4cadb52991fb | -8.28484 | -48.13989 | 2024-10-15 04:49:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bdbf9dc0-fa63-31b8-9b6f-6fda30113b50 | -8.28085 | -48.13929 | 2024-10-15 04:49:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ba19219f-921f-344d-9524-7d00bbafd908 | -8.28034 | -48.14277 | 2024-10-15 04:49:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 588f24d2-8d6a-340c-bef8-dd6acb1be552 | -9.3291 | -47.37097 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 314cdfc3-416e-3fc6-896b-493c3f877aa8 | -9.32484 | -47.37033 | 2024-10-15 04:49:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a1b64e6-f3c7-3bd5-b794-627e2be0e5cb | -9.20235 | -47.56699 | 2024-10-15 04:49:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c66d7ad-249d-3f27-a4c4-382f26a59faf | -9.20091 | -47.5469 | 2024-10-15 04:49:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 251a97dc-c00c-3481-be20-f584d03f0299 | -9.19815 | -47.56641 | 2024-10-15 04:49:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e1c1acc4-e520-344d-b7bf-ff606707eecd | -9.16338 | -47.60091 | 2024-10-15 04:49:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| acffd583-1085-3749-be7f-6e2e18f308b9 | -8.92428 | -47.91578 | 2024-10-15 04:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a639a68-f6b7-3054-9649-21ed52988d3c | -8.90746 | -47.91686 | 2024-10-15 04:49:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff79fae8-4491-3a22-bf2e-abe8a47d7b55 | -8.74737 | -47.55251 | 2024-10-15 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ffaa37b-f916-33ea-bcb2-5e8209a6d77c | -8.70619 | -47.54259 | 2024-10-15 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7684d830-40e4-3fbc-8f78-fe7550b699e3 | -8.46892 | -47.8181 | 2024-10-15 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c800417-f512-31da-bf94-c8e7a5ad776a | -8.46588 | -47.81009 | 2024-10-15 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7ca00ff6-9830-3944-b4e0-a3109fe979c9 | -8.46536 | -47.81378 | 2024-10-15 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d6be4c92-d0b6-32e8-a36a-0ce31e7220f9 | -8.46485 | -47.81743 | 2024-10-15 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ea8e1db8-7214-35fb-86b6-459bb2d0d910 | -8.4618 | -47.80946 | 2024-10-15 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ebaf8970-d054-3f9f-9cae-07710ba51465 | -8.46128 | -47.81316 | 2024-10-15 04:49:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README59.md)
