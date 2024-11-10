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
| 687cdc98-4d55-35de-9227-fbdaf3de3fcf | -3.1091 | -45.2968 | 2024-11-10 01:10:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 1cd3eba5-a516-31f1-8fc0-cdff1f290edf | -4.8655 | -46.9938 | 2024-11-10 01:10:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 57.3 |
| b44104e4-a3d3-3554-be67-70d1a6b96e94 | -4.6922 | -45.153 | 2024-11-10 01:10:00 | GOES-16 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 106.7 |
| eb5ccf9b-e9f1-3423-acd0-f9a6eaf5995f | -3.4383 | -50.2999 | 2024-11-10 01:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| daf03890-b3e1-3faf-8d1a-37855d54d1d3 | -1.5347 | -52.2104 | 2024-11-10 01:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 340.0 |
| 0b959f95-c9f6-34fa-8b14-46e755d8bbf7 | -1.5163 | -52.2106 | 2024-11-10 01:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 104.2 |
| 4330dfec-8c32-3786-8ab0-90c8b5edf947 | -3.5818 | -47.3621 | 2024-11-10 01:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 78ae1609-fb86-39af-bd7d-a6b13c10ec90 | -8.3967 | -44.1365 | 2024-11-10 01:10:00 | GOES-16 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 1bde9153-0be5-3238-966f-4248ff968b0d | -2.0768 | -48.8342 | 2024-11-10 01:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 1a4c20e5-06bd-30a1-aab0-35c2836fa52f | -3.5819 | -47.3403 | 2024-11-10 01:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 47bc4ac6-0a65-3655-95fd-26c83bcedc64 | -2.8337 | -49.0496 | 2024-11-10 01:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| db7da772-ee7c-380f-9bc0-115233bb9f91 | -3.2167 | -50.3071 | 2024-11-10 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 691b0f52-d708-341f-8e91-77b8b03202cb | -2.7586 | -49.371 | 2024-11-10 01:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| e1e1c7aa-7234-3cbe-bcc7-4f8f59568404 | -4.1112 | -45.7018 | 2024-11-10 01:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 52.7 |
| b6f4fdec-9191-3856-9850-be50bb336750 | -3.6003 | -47.3614 | 2024-11-10 01:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 118.3 |
| 06b2a152-05f3-3eb3-8ac9-730d728951fd | -3.9671 | -48.1283 | 2024-11-10 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 487f4b6f-57ac-30c3-bda7-8fc311352f2c | -3.2352 | -50.2855 | 2024-11-10 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 258.6 |
| 7bbdf386-f29b-3b2d-8d27-c55ed18fd961 | -4.2083 | -48.1176 | 2024-11-10 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 7c2981ff-99c2-3c0a-b8fb-ea412d07cb87 | -2.2672 | -47.0556 | 2024-11-10 01:10:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 956bcb83-f385-353f-b590-655b3cfb52c8 | -2.9494 | -52.7545 | 2024-11-10 01:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 6961d45c-2501-3261-bec7-85c0fd07ef40 | -3.1238 | -50.4568 | 2024-11-10 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 128.4 |
| 6c71a9ff-2a2f-3207-80d1-b110ce50e1db | -3.2168 | -50.2861 | 2024-11-10 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 240.2 |
| b41c0bd3-31b5-381f-8cb3-5a57cbe3aa1f | -2.0954 | -48.8125 | 2024-11-10 01:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| f31002e1-4f59-326b-8eed-fc2cce5624c5 | -3.2353 | -50.2645 | 2024-11-10 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 117.4 |
| c99926c8-1964-3abf-b309-43994217db62 | -3.525 | -44.0286 | 2024-11-10 01:10:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 7caca19c-e0c4-369f-a8f7-0422ec086a30 | -17.313 | -57.4834 | 2024-11-10 01:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 101.9 |
| 606f1c13-11dd-30f8-bd8e-71b9b5011cb3 | -3.2428 | -53.0519 | 2024-11-10 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 565193c6-2280-36d6-9ea7-818d47df8bf4 | -3.5064 | -44.0294 | 2024-11-10 01:10:00 | GOES-16 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 102.7 |
| e0e9a3e8-0047-330d-819f-87f8f6b87e9f | -3.2244 | -53.0524 | 2024-11-10 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 214.0 |
| 15dbda05-13af-3540-b891-006b84d052ed | -3.619 | -47.3388 | 2024-11-10 01:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 13defbbd-2704-3181-82b8-bc9eba67d067 | -3.2984 | -52.9486 | 2024-11-10 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 98c093ab-8303-3cd7-a172-8399cb26576f | -4.8657 | -46.9718 | 2024-11-10 01:10:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 128.9 |
| c4e8afa8-bd0e-314c-aa23-2b65b0fb0775 | -2.7587 | -49.3497 | 2024-11-10 01:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 122.2 |
| e8bef074-93b9-3101-b778-1d93d3a39598 | -2.9494 | -52.7748 | 2024-11-10 01:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| a2da9a44-7962-33e3-8cf4-c8474aa05bb7 | -2.6203 | -46.7602 | 2024-11-10 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| bbc2ab6b-62e4-30fd-a0c2-7141e58597f5 | -3.2427 | -53.0722 | 2024-11-10 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| cb0cb08c-cf5c-3fe4-9038-9abf7960b134 | -3.2352 | -50.3065 | 2024-11-10 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 153.9 |
| 7db4b351-31c4-3dae-a186-a3b398d360d1 | -1.5347 | -52.1899 | 2024-11-10 01:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 114.6 |
| 9dade820-88bd-3c3c-afca-32e70dbae52d | -3.1096 | -49.4029 | 2024-11-10 01:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 642a140f-46e8-393c-9ac9-5c7d0f28088e | -2.2487 | -47.0561 | 2024-11-10 01:10:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| c9713781-99c9-333f-b974-28985ba7cc92 | -3.1239 | -50.4358 | 2024-11-10 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 209.1 |
| 7379400c-1dac-3929-a4b7-2509f9f14ab6 | -2.931 | -52.7753 | 2024-11-10 01:10:00 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 39e404da-7719-3653-819b-34e04e94eece | -2.8803 | -51.4628 | 2024-11-10 01:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| bb5688ac-c693-3fbc-a85d-0c1eabea5f21 | -2.2095 | -47.733 | 2024-11-10 01:10:00 | GOES-16 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| c9720a0b-0958-3b1d-9951-1855d569d013 | -2.7771 | -49.3704 | 2024-11-10 01:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 27d39484-b866-3e0c-a167-5cd0568fcbbb | -3.1422 | -50.4562 | 2024-11-10 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 155.5 |
| fc3f0e32-aba1-3ce9-808a-60ca4c8aca97 | -1.5531 | -52.2101 | 2024-11-10 01:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 89597aa1-65bd-3864-b0b7-659297111539 | -2.2075 | -48.3811 | 2024-11-10 01:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| a2e98098-7d0e-3c7b-a9c3-2b4452569edd | -2.0953 | -48.8338 | 2024-11-10 01:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 142.7 |
| e3b4951c-9ef1-386c-8e5d-a930f5214b73 | -3.2169 | -50.2651 | 2024-11-10 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.9 |
| fa081764-902c-3090-9e77-2d32298a061d | -1.5346 | -52.2308 | 2024-11-10 01:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 98ebdbb0-12d3-3208-8525-0920c988d3e7 | -2.6388 | -46.7597 | 2024-11-10 01:10:00 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 28248187-d304-346c-b0d8-884c76a6e287 | -3.9485 | -48.1508 | 2024-11-10 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 122.2 |
| b24725ca-fdc8-3114-a28c-1e3bf3d17d8c | -2.8802 | -51.4835 | 2024-11-10 01:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 2708189e-8c5c-3a50-aff9-cc4be4250cf5 | -2.9171 | -51.4825 | 2024-11-10 01:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| f292f26b-467d-3f50-a82a-4f122949ac60 | -3.3117 | -45.6706 | 2024-11-10 01:10:00 | GOES-16 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 90.1 |
| b5425e4b-7c5e-34b7-9ad8-815c36c9069a | -2.7772 | -49.3492 | 2024-11-10 01:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 9a97e168-c9c6-32b5-b5d2-e1d8843de068 | -1.5163 | -52.1901 | 2024-11-10 01:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 701774da-fb3e-3ed7-9bbd-19f9611c6be3 | -3.091 | -49.4247 | 2024-11-10 01:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 50a47f07-36af-3acb-8e1c-cc492d098f64 | -3.1423 | -50.4352 | 2024-11-10 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 215.6 |
| e9535a15-abb1-35df-928a-39aa0d0ebafc | -4.8469 | -46.9948 | 2024-11-10 01:10:00 | GOES-16 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 5917ebc2-8960-3f02-bfff-96ab59e01d5f | -3.1095 | -49.4241 | 2024-11-10 01:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 9c0f52b2-5ec6-327d-9df6-0f02603d7462 | -2.9355 | -51.482 | 2024-11-10 01:10:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 119.5 |
| ff607110-dd1d-3eeb-b83a-70dc7e102b21 | -10.9419 | -40.8053 | 2024-11-10 01:10:00 | GOES-16 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 84.7 |
| eae46282-0ea8-3dd4-9700-57ae7cce578c | -17.293 | -57.5062 | 2024-11-10 01:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 115.2 |
| 0eedbeaf-edb0-3dfc-8469-fabf62e6508a | -17.2933 | -57.4857 | 2024-11-10 01:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 167.2 |
| cdf96c71-3e20-3188-b854-5631b498b649 | -2.2076 | -48.3596 | 2024-11-10 01:10:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 776ff69f-0f01-3dcf-8964-d2712246c026 | -3.2243 | -53.0727 | 2024-11-10 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 167.3 |
| fc4b55e3-53e8-3d4a-a9fe-49d43a709dae | -3.8413 | -44.1283 | 2024-11-10 01:10:00 | GOES-16 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| a73154bd-c9d4-37ff-bee0-17e8406a7a16 | -3.6004 | -47.3395 | 2024-11-10 01:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 217.3 |
| 151d79c1-9d85-32f3-ad68-cbae2b9dbddf | -23.86736 | -54.0623 | 2024-11-10 01:13:00 | TERRA_M-M | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| e0dc2ad7-1b10-3964-9fcb-ac891da48945 | -23.91614 | -54.04983 | 2024-11-10 01:13:00 | TERRA_M-M | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 19.7 |
| f47b8503-de58-38ba-b36b-39e2297dcd71 | -23.90746 | -54.06403 | 2024-11-10 01:13:00 | TERRA_M-M | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| 41558644-7bd3-35fd-adbd-b50ad6b3c2af | -23.90943 | -54.06943 | 2024-11-10 01:13:00 | TERRA_M-M | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| 4a0de627-7574-3d32-9873-b1b047dd28df | -23.89929 | -54.07084 | 2024-11-10 01:13:00 | TERRA_M-M | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| 6eb3211b-0d4c-3a38-9f57-c33a63a9b307 | -23.9176 | -54.06261 | 2024-11-10 01:13:00 | TERRA_M-M | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| f1e2f138-809e-3064-9d48-26035e98e852 | -17.29312 | -57.47726 | 2024-11-10 01:15:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 46.8 |
| 07dbf8c4-bf9c-3631-a063-a7f6cef43427 | -17.29502 | -57.49427 | 2024-11-10 01:15:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 220.9 |
| dd06f81c-c404-352f-aa62-ea614ebcb23e | -17.61805 | -57.50641 | 2024-11-10 01:15:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 273.7 |
| fdb0cc38-bd58-335c-a1af-e7f7a55200ec | -17.25098 | -57.48894 | 2024-11-10 01:15:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.9 |
| 9ce55ac1-dc66-3134-9eac-f5f679615294 | -17.28511 | -57.51279 | 2024-11-10 01:15:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 20.3 |
| fec2fdaa-dee2-3d96-9762-5610b433c60c | -17.60029 | -57.45628 | 2024-11-10 01:15:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.5 |
| c87bdac5-f29a-33ec-b878-3d8e8edfabe8 | -17.60618 | -57.50787 | 2024-11-10 01:15:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 154.4 |
| 9a564fef-366c-3a26-bf64-8d5b29c6be71 | -17.62416 | -57.49935 | 2024-11-10 01:15:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 54.5 |
| fd05828c-45ac-3696-96a0-3515b7e66d9a | -17.62203 | -57.54105 | 2024-11-10 01:15:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 71.0 |
| f45ca7cc-9207-303a-aacb-d09e7856d505 | -17.62603 | -57.51666 | 2024-11-10 01:15:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 285.7 |
| f29d65f2-3415-3d70-9135-cb76075035a5 | -17.62004 | -57.52371 | 2024-11-10 01:15:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 504.4 |
| e19c2ddb-a4f6-397e-8ab2-1e02f9440a1f | -17.62993 | -57.50496 | 2024-11-10 01:15:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 79.2 |
| 0f3e5b50-58de-3b3e-9005-16f0012ebe5d | -17.61012 | -57.54251 | 2024-11-10 01:15:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.5 |
| f550772b-ff71-3da9-8e10-9e7a23e8dfcf | -17.63792 | -57.5152 | 2024-11-10 01:15:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.8 |
| deefea25-df9f-30e4-ab8d-4a4c49854171 | -17.63194 | -57.52226 | 2024-11-10 01:15:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 147.7 |
| e90e78d7-dd49-3314-a8c3-10c22c8b1a9c | -17.82713 | -54.54051 | 2024-11-10 01:15:00 | TERRA_M-M | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 8.2 |
| c6ea67a8-9493-3223-91fe-f18f294cd775 | -17.6279 | -57.53402 | 2024-11-10 01:15:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 109.7 |
| 1f7d43a4-e9e7-39dc-ac13-208b3f674655 | -17.82975 | -54.53378 | 2024-11-10 01:15:00 | TERRA_M-M | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2a73a8e7-b413-331f-a287-c65e52d68160 | -15.27448 | -57.69162 | 2024-11-10 01:17:00 | TERRA_M-M | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 66a120f2-e6b7-35ee-8196-4b57ecae806d | -15.31572 | -56.51291 | 2024-11-10 01:17:00 | TERRA_M-M | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| ac48f039-cfdb-3556-89f9-a9c85b7b1968 | -15.3051 | -56.51431 | 2024-11-10 01:17:00 | TERRA_M-M | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| f5d8b067-5112-3e87-8238-1de2ee793600 | -15.27262 | -57.67517 | 2024-11-10 01:17:00 | TERRA_M-M | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 23.5 |
| b0dff6c4-eef9-31b2-84b7-08935cc2c7bb | -15.26456 | -57.68244 | 2024-11-10 01:17:00 | TERRA_M-M | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 585890ae-d224-3974-ba0f-a3b1281a6b00 | -14.83112 | -55.90527 | 2024-11-10 01:17:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README8.md)
