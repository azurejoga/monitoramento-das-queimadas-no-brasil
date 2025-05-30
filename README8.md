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
| b774af0b-6198-33af-b4e8-c8be828a1459 | -9.98454 | -48.49804 | 2025-05-30 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cfc7fbd2-b095-3dae-a06d-4054597fc862 | -12.01747 | -53.53839 | 2025-05-30 04:46:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e96149a4-640d-35c9-ba8f-40b994aa3212 | -11.8143 | -44.26706 | 2025-05-30 04:46:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33080847-ab48-3af9-aae2-c9ef06a401fd | -11.80338 | -47.37733 | 2025-05-30 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ce078a57-7e61-3916-9f82-bb9a3a97493a | -8.16986 | -49.79907 | 2025-05-30 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92933052-400b-3d4d-a944-1f4294428977 | -10.45664 | -47.94914 | 2025-05-30 04:46:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 057b90ea-43ad-3b03-b894-1ccd381c5316 | -10.78726 | -48.66275 | 2025-05-30 04:46:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2266886-0b01-3e6f-a760-cc81e248b1f8 | -7.95846 | -46.17798 | 2025-05-30 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 542f2669-0d0f-3ae4-bb24-8174c6b0e759 | -7.96756 | -45.94413 | 2025-05-30 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e33a9c7-067b-3ba1-af0a-b3d5d187cc08 | -13.53531 | -43.68076 | 2025-05-30 04:46:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c637ca0c-b231-3f5a-be5a-64ea64a23395 | -9.25589 | -48.86976 | 2025-05-30 04:46:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1981bf9b-8baa-390e-8f31-1dfce9b72497 | -12.39681 | -50.00344 | 2025-05-30 04:46:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e149cd82-7a2f-39fd-ace5-0473f123c990 | -7.53737 | -43.32618 | 2025-05-30 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5e5f5f3-25c8-3c94-9740-80bc7eac9f31 | -10.29771 | -59.09848 | 2025-05-30 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4942ac9-4c70-3fce-849d-b3cf7a45cc34 | -7.6211 | -45.74402 | 2025-05-30 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8b666b8d-927d-30b9-8861-784c37b08f5e | -12.39332 | -50.0029 | 2025-05-30 04:46:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3315def8-55a6-3c53-a22f-3e29a17388a9 | -12.06949 | -48.47006 | 2025-05-30 04:46:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 840a1b77-4b3b-3cd0-bda9-e302784279c9 | -8.00131 | -45.68211 | 2025-05-30 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9478bed9-5b02-3520-b262-b93a93775d10 | -11.81216 | -44.28384 | 2025-05-30 04:46:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1a3b3d8-8043-38ef-8958-91b19217cf58 | -11.7994 | -47.37672 | 2025-05-30 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3d05833d-6bb9-385f-9b7e-f24df3d32bc0 | -7.23638 | -43.09644 | 2025-05-30 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 28d6b6ac-fe3c-353a-a601-69de0a973373 | -11.79744 | -44.28175 | 2025-05-30 04:46:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5bb702ef-3fcf-345d-b61e-581b74771b52 | -10.6304 | -49.43966 | 2025-05-30 04:46:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1a171dc-cd25-3835-8537-95d80a23ccb4 | -12.30098 | -50.0858 | 2025-05-30 04:46:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 384bb59f-952e-356d-9fd5-a13d00ce84d9 | -9.42236 | -47.44511 | 2025-05-30 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 93e24df1-e772-3183-a155-4ea4ce955d18 | -7.5537 | -43.31721 | 2025-05-30 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ae39eec3-ba72-3cc5-938b-e3f2f15f7442 | -9.39883 | -48.41351 | 2025-05-30 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 234fe06c-e024-3afa-9c7f-2ebd863c53db | -7.18924 | -43.10696 | 2025-05-30 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9c32b20a-6733-3a04-8d9b-42fa13666728 | -12.39092 | -49.97042 | 2025-05-30 04:46:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f1a155f-6fb4-3686-9fa0-095ac45aece8 | -9.97492 | -48.67295 | 2025-05-30 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0d74fd3-f17c-3a58-9fd7-6b2d63627962 | -9.79643 | -47.75131 | 2025-05-30 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7c54a427-0272-3301-9ab5-a83f296376e7 | -7.18963 | -43.10406 | 2025-05-30 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 656aedca-6980-3215-a9cd-e94ecfa3f07e | -7.89942 | -55.41406 | 2025-05-30 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca6b8700-6db9-3170-8183-f0fb0091d5e1 | -10.80194 | -49.25566 | 2025-05-30 04:46:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f31f7dc6-c945-321e-b4b1-fd7560f49666 | -10.05253 | -49.65446 | 2025-05-30 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3f85b66-2de9-3b34-80f3-19e1d907a2a5 | -9.00969 | -48.72251 | 2025-05-30 04:46:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00c0bb02-0e5f-3bcb-893e-d8524e7f69c2 | -6.60379 | -44.73254 | 2025-05-30 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1f54910-d600-3330-940f-f00705a4b543 | -7.59148 | -45.95176 | 2025-05-30 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f6e911c-50ce-3f36-af7e-85615ccab633 | -8.70529 | -50.0371 | 2025-05-30 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a1a5fa4-3a67-339d-959d-1bb3ea68c021 | -7.5332 | -43.31998 | 2025-05-30 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8f9640a7-0e9c-3d42-be6d-ff872335d8cf | -10.29333 | -57.14151 | 2025-05-30 04:46:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 79cc94ec-60c1-3e06-b68d-71eb6e22d46c | -8.74142 | -48.75203 | 2025-05-30 04:46:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aee5ea2d-ea66-3867-91fb-2e4e0a9a5a2a | -9.39395 | -48.42154 | 2025-05-30 04:46:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 478de08c-bd5a-3afe-a9e9-0080881843bd | -7.49715 | -43.13254 | 2025-05-30 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dcd4e732-fa92-3173-a67f-cc0047d95db4 | -12.0111 | -49.52015 | 2025-05-30 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 63c8a5dd-d3f9-3928-9747-73d81375f465 | -13.09613 | -52.04745 | 2025-05-30 04:46:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c244ebca-34a2-3d99-99af-b033c49e2ed6 | -7.60773 | -46.64727 | 2025-05-30 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 80614e84-ce21-3716-88a6-0ddb013eb8c6 | -8.19528 | -49.81428 | 2025-05-30 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 49385fc8-c70f-3cd3-bdbc-83db8c16dc3c | -10.16727 | -53.91935 | 2025-05-30 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1ddb341e-591c-36f9-a71f-23ebbf05e7d3 | -12.40086 | -50.00005 | 2025-05-30 04:46:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3962d02-e439-3834-aa8e-f845eb6c5691 | -11.20531 | -47.82248 | 2025-05-30 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eedbb4d3-82fb-3760-9dad-a77f2a3e76ab | -11.97763 | -52.45766 | 2025-05-30 04:46:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9dc403c3-609f-317e-9109-37d686086604 | -13.22353 | -49.83709 | 2025-05-30 04:46:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0ddf232-6b1d-3f56-8311-7431a4c2f0ed | -7.07472 | -44.93293 | 2025-05-30 04:46:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c24eafc-f6e6-3e7f-a16c-14a29db70f0f | -9.06162 | -51.19655 | 2025-05-30 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31ed7dac-fcde-33fe-a297-d5866601c6c8 | -7.22802 | -43.26688 | 2025-05-30 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 816ffbbd-32fe-3347-a6fe-5ef18f13521e | -10.35768 | -48.73456 | 2025-05-30 04:46:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41fdc600-750e-3a29-88c8-c1c779bedb6e | -7.49675 | -43.13539 | 2025-05-30 04:46:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 97328e3d-e1e9-38da-b91b-d5c03b4480d3 | -7.58306 | -45.86259 | 2025-05-30 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| abb98f9d-7e19-36c0-9013-2ffa41c7774c | -12.01818 | -49.52122 | 2025-05-30 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bac64c47-22a4-3ab8-b1a4-a2065cec6601 | -7.5784 | -45.86568 | 2025-05-30 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 462c7432-b519-3e73-8c91-9cbde9b327d5 | -6.6957 | -44.1581 | 2025-05-30 04:46:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9f08e7d0-8ce3-33d4-9dc6-d8bc431f76d3 | -9.84881 | -48.14481 | 2025-05-30 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ac26b295-6365-3a92-bcea-d7757afff990 | -13.00644 | -42.66896 | 2025-05-30 04:46:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2086ca3e-0a20-31b1-8d34-dce055068df3 | -13.22766 | -49.83355 | 2025-05-30 04:46:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b6aa84d-ef67-39fa-8410-1453c6abbfbe | -7.5879 | -45.9474 | 2025-05-30 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 89a9a1f7-da5c-3cd5-aebc-9009c7f7a44e | -8.55099 | -46.425 | 2025-05-30 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b838d4e-d81c-3a37-a413-18649933cca8 | -8.41615 | -47.10244 | 2025-05-30 04:46:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7454f42-479a-32fc-b46b-4a0fec005539 | -8.3194 | -47.91822 | 2025-05-30 04:46:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7845f5e-75c2-32de-a053-0299802a664a | -11.68924 | -46.21015 | 2025-05-30 04:46:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04b1142e-7a32-3741-bc8c-2f02dbbb7dd4 | -12.01762 | -49.55031 | 2025-05-30 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0ea44a31-d866-3a96-a851-a0d91c32cc59 | -7.61747 | -45.73949 | 2025-05-30 04:46:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d4198bea-d193-3605-a61b-860fc15c2029 | -6.63616 | -55.01245 | 2025-05-30 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55fefb6d-75cf-33d2-afbe-702da26b31c9 | -7.32765 | -43.71143 | 2025-05-30 04:46:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c89e50b0-8778-3a08-bb9a-56e5d069a8c7 | -8.19977 | -49.80748 | 2025-05-30 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eb39c818-c2ac-3dcb-89f6-40ee33d1ecd1 | -7.18465 | -43.10336 | 2025-05-30 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 95cde11b-8d87-3bc4-833a-9a68b46697b8 | -12.60092 | -48.37273 | 2025-05-30 04:46:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3464400e-ca27-383e-a7ca-57245a7e5539 | -7.58683 | -45.95484 | 2025-05-30 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 58d81432-0c40-3516-814a-63eb88c83062 | -7.7048 | -49.39331 | 2025-05-30 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3db7cf29-f34f-363c-9c06-2a010de858bd | -8.51862 | -50.016 | 2025-05-30 04:46:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0211f4ac-f91f-3efb-943a-7cf8d0c90a38 | -10.26918 | -46.48238 | 2025-05-30 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32b5579f-d420-328e-9267-84aa1dbc65dc | -11.69355 | -46.21066 | 2025-05-30 04:46:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2a85432b-bdec-3801-88dc-eaa7ff1730a1 | -7.18387 | -43.10918 | 2025-05-30 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5e139719-0aa7-31fb-a8ed-8a68bd602dea | -7.24097 | -43.10005 | 2025-05-30 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 4710f7a7-65d3-3b52-b565-001131a6e5ba | -7.59042 | -45.95918 | 2025-05-30 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 07a99fe4-2cfc-3067-b929-a59b17ec912b | -9.20087 | -49.46686 | 2025-05-30 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c267c88a-31d4-37a3-925c-158707282f50 | -7.23678 | -43.09354 | 2025-05-30 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 147554c1-c290-32e9-8cbe-fcc737e66a23 | -11.40027 | -52.94711 | 2025-05-30 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e4a08011-6f0a-3345-a4cc-0344731e0a1b | -12.29592 | -48.80264 | 2025-05-30 04:46:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d9c7f0bb-df46-3c50-9681-8fb832a8a94b | -7.27178 | -44.22555 | 2025-05-30 04:46:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d0f8711-f866-31b8-981c-e6dac4f5d018 | -9.25648 | -48.86575 | 2025-05-30 04:46:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fc3b9831-99b9-3a87-af28-7c96d1111062 | -12.39738 | -49.99952 | 2025-05-30 04:46:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 384ab70b-cd63-3ba6-9052-1b6fe1118d82 | -11.79893 | -47.38021 | 2025-05-30 04:46:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| edf26f63-41de-3dac-836a-8405a2d1b6ab | -11.72658 | -56.43606 | 2025-05-30 04:46:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5b17626e-e9f3-353d-8df2-e12d474b2d6e | -13.54056 | -43.67883 | 2025-05-30 04:46:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 2550778d-75ee-3f3d-afbf-352413651ad9 | -9.60574 | -49.02476 | 2025-05-30 04:46:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ed6e3a22-ce6f-3b82-b910-bf21f739a00e | -11.20463 | -47.82735 | 2025-05-30 04:46:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aaa2cb85-06c9-341c-b6ea-65c09dcbf720 | -12.25947 | -44.60371 | 2025-05-30 04:46:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2527ae70-df66-367d-9d15-0f8ef50a69b5 | -8.19583 | -49.81062 | 2025-05-30 04:46:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 07f35441-cb98-3571-b696-f2946bef745e | -7.959 | -46.17412 | 2025-05-30 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README9.md)
