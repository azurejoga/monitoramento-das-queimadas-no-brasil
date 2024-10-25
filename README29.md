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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 326d2596-de22-343f-ab16-8ea8b7400d83 | -4.65835 | -46.85786 | 2024-10-25 04:14:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f04bab7-df39-3c82-a6f6-dac76f9e989c | -4.47393 | -47.73159 | 2024-10-25 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 56933c27-98b5-3a1a-808c-955146563634 | -4.47334 | -47.73525 | 2024-10-25 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e018ceb5-6e1e-34be-b92d-1215d5d7c2aa | -4.37127 | -46.809 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 365b291c-e0f5-3b13-9fd2-883cccd64421 | -4.18552 | -46.80647 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0c73b9c6-3c96-370c-a461-74d952282866 | -4.16398 | -46.86645 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39aced5f-f354-32ba-8179-bb318efb710c | -4.14562 | -46.8343 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 43.4 |
| db3c397c-4ec3-3f3e-9ce3-498219da6d6d | -4.03004 | -47.21996 | 2024-10-25 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2073fb3-04c9-3843-90e5-d0d4fd2e5b96 | -3.91802 | -47.53164 | 2024-10-25 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1cf95bb1-febb-36d4-bd01-8266c1eef267 | -3.81927 | -46.93223 | 2024-10-25 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19c938c6-0d94-3ed9-a7f3-79b78da5fc51 | -3.81539 | -46.93159 | 2024-10-25 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 590a27db-279a-3822-9fef-139cd6721ebc | -3.81231 | -46.92612 | 2024-10-25 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35476ab6-c78c-37e1-ac2b-87b095f2f533 | -5.00309 | -46.48371 | 2024-10-25 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b5831952-4015-3620-aadf-c668fff175ac | -5.00013 | -46.47852 | 2024-10-25 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 828814ef-a99d-3d3b-8eb1-852077b06ec9 | -4.99272 | -46.47727 | 2024-10-25 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ac4777b-749c-3c73-83eb-3312d00db512 | -4.9757 | -46.48816 | 2024-10-25 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b270d63d-de09-30c6-9c7d-80f8f18f1719 | -4.7695 | -46.41761 | 2024-10-25 04:14:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| b9ddf02f-d0ba-314d-96ad-33ed5221aa9d | -4.76579 | -46.41705 | 2024-10-25 04:14:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fab4ee1b-ee40-38d8-8ea2-ddae6ca37f5b | -4.76426 | -46.40313 | 2024-10-25 04:14:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 23915af8-4aa0-3b87-a43d-d86cc57a0fc9 | -4.69522 | -46.61277 | 2024-10-25 04:14:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 21bc49e7-0bdb-30b7-90ee-e01445f3f5a9 | -4.69499 | -46.84915 | 2024-10-25 04:14:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa44f94e-7bd7-32bc-9c79-4998df2e4584 | -4.69472 | -46.61002 | 2024-10-25 04:14:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 28a3e775-b53e-362d-8ce4-fc21858646b4 | -4.65869 | -46.86023 | 2024-10-25 04:14:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08d02ca1-f562-348a-91cc-20874b0808e2 | -4.61876 | -46.55628 | 2024-10-25 04:14:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38065d38-bade-3c4f-92d3-937ae878582b | -4.61066 | -46.69971 | 2024-10-25 04:14:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| adc5fbd5-c185-3405-8d0c-39ce6f416b95 | -4.53557 | -46.73154 | 2024-10-25 04:14:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b469c087-6cc0-38bb-84bf-18ed25b576c7 | -4.53006 | -46.62207 | 2024-10-25 04:14:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7166a514-2e50-38bf-b40c-56de5bedab07 | -4.49742 | -46.38802 | 2024-10-25 04:14:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67d775cd-8d90-3043-90ba-0a8d32bb3a8c | -4.43352 | -46.64196 | 2024-10-25 04:14:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 301f6754-fedd-38ad-a147-eef6e5875839 | -4.42974 | -46.64138 | 2024-10-25 04:14:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8aa2debb-2115-3065-8e8c-e2dc3f668314 | -4.18704 | -46.87005 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d344ce1-f177-33b0-8375-0be74d71c8d2 | -4.18167 | -46.806 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 846ddf37-3654-3378-b17c-b5027fe88e17 | -4.14945 | -46.83489 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ffa3c188-5ef2-3de4-9106-f0eebc2754e9 | -4.14859 | -47.10838 | 2024-10-25 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 869aa438-39ff-370b-873f-d5347bc6d068 | -4.12932 | -46.88544 | 2024-10-25 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1d17269d-7ea8-3b1a-b675-635286dc275e | -5.84611 | -47.03322 | 2024-10-25 04:14:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 174f9800-f2d8-34a9-abef-56d5330d1ab1 | -5.83258 | -47.18514 | 2024-10-25 04:14:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9ff4124b-c5fc-3be0-b858-25d484864d42 | -5.82876 | -47.18451 | 2024-10-25 04:14:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 12baa890-23f6-3443-8460-57e84a13dd26 | -5.71681 | -47.10926 | 2024-10-25 04:14:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 276d82d3-a8e6-3b81-b1ac-ff9af2e8e44a | -5.65031 | -46.97134 | 2024-10-25 04:14:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb843c9d-0c9f-3aef-aa0c-19393c194f62 | -5.64955 | -47.51089 | 2024-10-25 04:14:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6261d2b2-d61d-398a-b4ca-7125adaaf616 | -5.64797 | -47.91237 | 2024-10-25 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eb1f6d85-49b8-3638-a6be-6df7d962fa09 | -5.64681 | -47.9194 | 2024-10-25 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64c6ff93-2353-350a-879d-a38afe0d34e5 | -5.63896 | -46.96951 | 2024-10-25 04:14:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| f1c8efdd-7751-3430-98b5-8b42250ad897 | -5.6172 | -47.26663 | 2024-10-25 04:14:00 | NOAA-21 | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3b6b788c-4430-3598-b831-a05a6355635c | -5.44419 | -47.68048 | 2024-10-25 04:14:00 | NOAA-21 | SÃO MIGUEL DO TOCANTINS | TOCANTINS | Brasil | 1720200 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5805dc0a-5142-36b7-9d8c-311d231b2f27 | -6.28281 | -47.82018 | 2024-10-25 04:14:00 | NOAA-21 | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f11da5f-a3f9-35e5-9842-5bc07f9f43a6 | -5.65256 | -47.90949 | 2024-10-25 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4548a2ba-66c7-3654-838c-b396e6b5e8a8 | -5.65199 | -47.91298 | 2024-10-25 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 99d0235d-68c9-333e-aa66-fba7a1dda891 | -5.64854 | -47.90886 | 2024-10-25 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c6d40a3e-29bf-31fe-9fd6-debee4b73da2 | -5.43495 | -46.55126 | 2024-10-25 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd21d556-18c3-36b0-9a56-b13ceb3bdf73 | -5.43423 | -46.55568 | 2024-10-25 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 330e7fc1-7257-3012-9946-2bcb35a00967 | -5.43124 | -46.5507 | 2024-10-25 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ff08a19-f272-3c58-9f96-0a256eefbceb | -5.42753 | -46.55013 | 2024-10-25 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 41546349-48b5-3a34-a949-1059db76f96a | -5.42609 | -46.55896 | 2024-10-25 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7601c4b4-b1db-3763-9fa0-eb66e7b6e291 | -5.41653 | -46.57098 | 2024-10-25 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 90b7cb03-afdf-388d-babe-5125d2600f38 | -5.27775 | -46.7071 | 2024-10-25 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdc2153a-39e2-3136-a207-07f4977a7264 | -5.274 | -46.70654 | 2024-10-25 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef70d1e4-66f0-34f6-9e1f-71f5b6e999c6 | -5.24556 | -46.69247 | 2024-10-25 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 59bc773b-3aa6-3261-a173-cec6f158637c | -5.24405 | -46.67836 | 2024-10-25 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ac2e8b1-ca0c-38e1-a1fd-4d2353cb0846 | -5.23449 | -46.68256 | 2024-10-25 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 88c7f074-fa91-30af-af02-2c64f4e8453a | -5.21438 | -47.19058 | 2024-10-25 04:14:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc77ab8f-98dc-37ae-8603-dd984982ba9d | -5.21051 | -47.18998 | 2024-10-25 04:14:00 | NOAA-21 | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24b41985-f0ac-304b-ad74-bfc2cff2d393 | -5.13929 | -46.88877 | 2024-10-25 04:14:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 85f32c6f-58f1-3c1c-a103-7e7569db2aab | -5.43352 | -46.56009 | 2024-10-25 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c9870cb-6cbf-3bea-b451-f39254aa3c2d | -5.42238 | -46.55839 | 2024-10-25 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 60d870de-00f2-32f6-868e-52ea699fdbcc | -5.41425 | -46.5616 | 2024-10-25 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3a028d8-0d4d-3161-ada2-26dc0df702fc | -5.41353 | -46.566 | 2024-10-25 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d22d1cd4-c57c-37f1-83d1-2cfa16f2dcf2 | -5.2433 | -46.68291 | 2024-10-25 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf68f7b8-b2d0-34ab-8835-a7df59cdf737 | -5.23207 | -46.68113 | 2024-10-25 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 66917d68-106f-3f27-9f4a-9a716e44ab4d | -6.29604 | -46.6791 | 2024-10-25 04:14:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f11e05ea-7c24-36a1-b4cf-c474d69550a0 | -6.23571 | -46.79232 | 2024-10-25 04:14:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e72d8973-c72f-3e04-b5df-0dcd14e73d78 | -6.23121 | -46.77334 | 2024-10-25 04:14:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33d2a637-33dd-3edc-b730-8b935d52c3c1 | -6.12064 | -47.27438 | 2024-10-25 04:14:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b632f018-61bc-394c-b40f-ce1eefae8329 | -5.83563 | -46.62395 | 2024-10-25 04:14:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be312691-f719-3a24-85a7-0cd538e17570 | -5.71602 | -47.11399 | 2024-10-25 04:14:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7f38465e-4e93-3c04-9f65-9f0847dab043 | -5.70467 | -47.34816 | 2024-10-25 04:14:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9f503ab4-fdc0-3f31-8c8c-c4c9f398a2da | -2.81 | -49.26278 | 2024-10-25 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b3c93b28-7ec8-34ef-b8fa-952291d69b9a | -5.7008 | -47.34753 | 2024-10-25 04:14:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 044b288b-8ff7-30a3-b0f5-79192ba1c584 | -5.69693 | -47.34689 | 2024-10-25 04:14:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f2267479-0d00-3097-8b61-f792323c0d35 | -5.63517 | -46.96892 | 2024-10-25 04:14:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 4b170f2a-950d-3e6d-a873-9c0c5c310aad | -7.89996 | -47.35344 | 2024-10-25 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0950db44-e226-3434-9351-cdad70bc6a29 | -7.71282 | -47.58779 | 2024-10-25 04:14:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9c62fb8a-9032-37ea-a74a-f76b66fff06a | -7.65739 | -47.52631 | 2024-10-25 04:14:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a49414e-a121-33aa-99cb-ce6444781798 | -7.65359 | -47.52571 | 2024-10-25 04:14:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22864567-fb27-3f31-bbac-871fda4617fe | -7.63111 | -47.82758 | 2024-10-25 04:14:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 76fc75dc-77cc-3be4-b523-58b1208ce084 | -7.60946 | -47.7192 | 2024-10-25 04:14:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fbbf40ea-bf9f-3d2e-abc0-56610e53881c | -7.59477 | -47.08599 | 2024-10-25 04:14:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f9ed840f-fff3-3b43-8920-fc948653af06 | -7.5435 | -48.30642 | 2024-10-25 04:14:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d92e3b34-f9b2-3d75-8dce-67483224929f | -7.543 | -47.41889 | 2024-10-25 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f315eee-3cc1-3e75-aae2-6b5c79e80045 | -7.54011 | -48.30215 | 2024-10-25 04:14:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffedcae2-eedb-3a0a-84c1-85a985c769f6 | -7.53952 | -48.30568 | 2024-10-25 04:14:00 | NOAA-21 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d53cd7fa-fb7b-3d15-8e1f-41b6715b0409 | -7.47656 | -47.16497 | 2024-10-25 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d1691d7-267a-3460-ae8b-8d0f739750a2 | -7.47314 | -47.39512 | 2024-10-25 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b068ea9d-2ad9-3afa-87b8-beaba701a0f7 | -7.42698 | -47.10724 | 2024-10-25 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0bb723a6-6558-3ab2-98b4-201b3d40c322 | -7.3494 | -46.98609 | 2024-10-25 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30ab24bc-f60e-36d6-8350-cc4119062e2f | -7.28807 | -47.87986 | 2024-10-25 04:14:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6708e140-cf38-3e2f-ad55-6aedf3a8c15b | -7.28134 | -47.19141 | 2024-10-25 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 89365c5d-3ccb-3cd7-9756-458b52d7a70e | -7.27307 | -47.63587 | 2024-10-25 04:14:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5e4e5d8c-2ae6-3de7-b902-6f89dfb18e24 | -7.25012 | -47.91456 | 2024-10-25 04:14:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README30.md)
