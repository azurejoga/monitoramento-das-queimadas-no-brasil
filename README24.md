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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f9f58d5-2419-38cf-8a8b-4c6977110bca | -10.2849 | -45.8183 | 2026-08-08 08:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 2e94b1ce-0878-395e-9421-da02f1ef65a9 | -18.0178 | -50.6101 | 2026-08-08 08:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 333c8878-7273-396f-b7ce-c1e6f5d45e91 | -10.2659 | -45.8206 | 2026-08-08 08:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| b7d24fed-0b78-3b84-bb24-c1b6cd61d1b4 | -18.0378 | -50.6065 | 2026-08-08 08:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 385f6353-7b91-3c8f-a914-cfa65eeb3614 | -18.0378 | -50.6065 | 2026-08-08 08:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| db9257bc-56d8-32d4-ab65-e29eddb4136a | -18.0178 | -50.6101 | 2026-08-08 08:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 50.5 |
| d5a412d8-52b4-386a-b590-c83433c574a7 | -18.0378 | -50.6065 | 2026-08-08 08:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 62.5 |
| a660d919-d98b-30ae-90f0-e35c264aa800 | -4.2634 | -48.2016 | 2026-08-08 08:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 0d6dd484-98c6-33ec-9e8f-782c907d656e | -18.0178 | -50.6101 | 2026-08-08 08:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 5bc3f4a5-a47d-386c-9a8d-f9176e4d4eda | -4.2634 | -48.2016 | 2026-08-08 08:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 3626b558-08a3-37c7-b85f-a55a5c5df2e1 | -4.2635 | -48.1799 | 2026-08-08 08:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 3088c519-65c8-3302-8bda-2e68085a95c5 | -18.0378 | -50.6065 | 2026-08-08 08:40:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 6dd1f34b-dc20-3c2b-913b-d114b8852fc2 | -18.0378 | -50.6065 | 2026-08-08 08:50:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 78fc33bb-792d-360c-aaa4-6faf3bea7782 | -18.0378 | -50.6065 | 2026-08-08 09:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| d1639f5d-5252-3e3e-9833-f77da3b21d76 | -10.2659 | -45.8206 | 2026-08-08 10:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 0e0c4328-4b21-3679-b134-605f453997a8 | -6.9791 | -42.9034 | 2026-08-08 11:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.7 |
| 292f126e-374f-3aef-9b2a-4802bfd67b70 | -10.2472 | -45.8002 | 2026-08-08 11:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 6b995a02-6dc6-3aa0-b882-903905bd75a6 | -10.2472 | -45.8002 | 2026-08-08 11:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 116.1 |
| d1c59542-4a36-3d11-928e-38c3885ecf08 | -6.9791 | -42.9034 | 2026-08-08 11:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.8 |
| fde9cffd-fa69-33bf-9f6b-c5073a6ef085 | -10.2472 | -45.8002 | 2026-08-08 11:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 2121d7bc-8ea1-3b32-bc5c-673e20eaa936 | -6.9791 | -42.9034 | 2026-08-08 11:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |
| 1923f405-123d-375c-9a25-6c4267524780 | -10.2472 | -45.8002 | 2026-08-08 11:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 124.8 |
| fa1b9103-78c0-3a98-82d4-0266600c2bf5 | -6.9791 | -42.9034 | 2026-08-08 11:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 101.5 |
| 36b25d48-d27b-347e-9b66-2e3191581a36 | -6.98866 | -42.89424 | 2026-08-08 11:57:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.6 |
| f30d07d1-5f2b-35ee-937a-6ed4196f931d | -3.31571 | -41.43591 | 2026-08-08 11:57:00 | TERRA_M-M | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 169.9 |
| e6635035-a562-30de-b862-94613a443a5b | -8.65975 | -51.29639 | 2026-08-08 11:57:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 2bf97e40-ca9b-3e05-a146-8e7fbf534bc1 | -7.18937 | -42.33863 | 2026-08-08 11:57:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 23.4 |
| b9903ddb-5136-36f6-a910-7415bd8d06fd | -8.07659 | -45.58847 | 2026-08-08 11:57:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 0b41fbd2-c4fe-3479-a9ea-be3e6e6db52e | -6.99015 | -42.88777 | 2026-08-08 11:57:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 49.2 |
| 943a87c8-99ac-3db2-afee-ce59080866c6 | -6.98751 | -42.90791 | 2026-08-08 11:57:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.4 |
| 7aaa718d-d771-3d0f-970e-267b810d6852 | -8.07834 | -45.57529 | 2026-08-08 11:57:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 18.8 |
| c1a2736f-d9f8-3329-a799-d72b297e9942 | -7.37094 | -42.86312 | 2026-08-08 11:57:00 | TERRA_M-M | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 20.2 |
| 809d6e7f-279d-3fd9-b99a-f68a3298c81b | -6.91854 | -42.42318 | 2026-08-08 11:57:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 56.2 |
| 3885745b-1417-3652-9d26-88840011f137 | -6.91582 | -42.44457 | 2026-08-08 11:57:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 37.2 |
| 92957775-7d59-3afd-91be-b9d17643980d | -8.84515 | -46.71193 | 2026-08-08 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b0dcd0f5-e957-32af-845f-5af21fb2d0d7 | -3.09222 | -49.35711 | 2026-08-08 11:57:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 824e05b8-ce06-3548-b611-931c899b2695 | -5.88264 | -51.72186 | 2026-08-08 11:57:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| ed4e1025-65af-37d7-a85b-bd98791c778a | -6.98618 | -42.91432 | 2026-08-08 11:57:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 43.7 |
| 81a499b5-964b-3856-aecd-3bc4c113736a | -6.9791 | -42.9034 | 2026-08-08 12:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.0 |
| a34ab0f9-1365-3b71-aa2f-7a99c98e7364 | -10.2472 | -45.8002 | 2026-08-08 12:00:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 209.6 |
| 44b52224-31fb-38fd-98ac-181ef0ea3751 | -6.9278 | -42.4354 | 2026-08-08 12:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 91.9 |
| 713ba92d-f57a-39d4-b1c0-51e5b15f1488 | -15.82199 | -49.14197 | 2026-08-08 12:00:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1d10da2f-d52b-3485-a1d6-97fbdf2175ab | -12.33008 | -53.15965 | 2026-08-08 12:00:00 | TERRA_M-T | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 9d7d0acb-df9d-3f16-a20a-4dd79df526bc | -10.27266 | -48.25644 | 2026-08-08 12:00:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3538f094-2e9f-306b-b959-d617cd9104f6 | -14.94062 | -48.2683 | 2026-08-08 12:00:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 967314e9-43e6-3725-a390-fa2903849099 | -11.81438 | -47.34283 | 2026-08-08 12:00:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| abe2d7c6-27f6-3ea2-b348-3c4f1de0c2b7 | -15.16489 | -52.73122 | 2026-08-08 12:00:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ba140512-5c49-3eb0-888e-15aad3b43ba6 | -14.57485 | -48.9612 | 2026-08-08 12:00:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 21.3 |
| e73e5ab3-1d79-3f8b-b65c-8a7d2b42b3d8 | -20.09569 | -43.95887 | 2026-08-08 12:00:00 | TERRA_M-T | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.4 |
| a3fcbd27-7ef7-3491-beed-a3907be024dc | -10.95131 | -43.56151 | 2026-08-08 12:00:00 | TERRA_M-T | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| b9713fb6-a1aa-3ed8-b215-7ebcfaf22097 | -15.16343 | -52.74088 | 2026-08-08 12:00:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 171749c7-cb9e-33fe-a93f-3d7f59e0c35d | -12.77205 | -47.12607 | 2026-08-08 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 9a8a5359-3aa6-3504-9506-3da8b8d8bb7b | -15.38194 | -53.79012 | 2026-08-08 12:00:00 | TERRA_M-T | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 58fb0c16-e954-3faf-9fdb-67e58f6f6bb8 | -14.35718 | -54.88433 | 2026-08-08 12:00:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 69adfcf2-de40-3352-8a7f-6360fa687c94 | -10.48873 | -46.63691 | 2026-08-08 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| c6035f0c-8bbc-3c0f-8ca2-47e6e4d2d726 | -19.12212 | -45.41393 | 2026-08-08 12:00:00 | TERRA_M-T | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| cb61f739-5d87-3d68-867e-0d9249d2eeec | -14.92877 | -48.26071 | 2026-08-08 12:00:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 00c41511-6973-3d98-a000-16e5ecc4e925 | -10.24053 | -45.80126 | 2026-08-08 12:00:00 | TERRA_M-T | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |
| aebda3ec-b03a-3e4d-b9b6-68ab255eb813 | -10.25113 | -45.80391 | 2026-08-08 12:00:00 | TERRA_M-T | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 9ee71a3e-900e-3e0e-88c6-7f7fe61a5c0f | -19.72106 | -44.92123 | 2026-08-08 12:00:00 | TERRA_M-T | CONCEIÇÃO DO PARÁ | MINAS GERAIS | Brasil | 3117603 | 31 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 3f48ff51-d96d-30e8-a769-9637f3bca6a9 | -14.33104 | -54.93936 | 2026-08-08 12:00:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 867f24f2-a335-37ee-9039-f32846eec5c6 | -15.70817 | -54.84993 | 2026-08-08 12:00:00 | TERRA_M-T | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 35.0 |
| ccce4d26-1a1e-3d0d-98ad-147710c20b28 | -19.71644 | -44.92733 | 2026-08-08 12:00:00 | TERRA_M-T | CONCEIÇÃO DO PARÁ | MINAS GERAIS | Brasil | 3117603 | 31 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 742dc8e1-3c2a-3708-97a7-4d6e9ae526d9 | -11.26714 | -49.32337 | 2026-08-08 12:00:00 | TERRA_M-T | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c05e410d-cdee-3d56-960a-2ded6d97efe5 | -10.23882 | -45.81453 | 2026-08-08 12:00:00 | TERRA_M-T | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 48.2 |
| e3de8ffc-3181-330c-a303-7b26975414f7 | -11.81589 | -47.3315 | 2026-08-08 12:00:00 | TERRA_M-T | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 21.0 |
| d721c58e-f336-3006-80c0-f9bd18ae267d | -11.31233 | -44.85158 | 2026-08-08 12:00:00 | TERRA_M-T | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| fa47cef1-3df9-316c-ad14-261eba90a788 | -15.1272 | -52.73936 | 2026-08-08 12:00:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 18e14f56-4446-3606-9674-932751bc98f0 | -10.51062 | -46.62774 | 2026-08-08 12:00:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 3ca9d9e8-9be8-39e8-b9fd-76564404ca6f | -15.37239 | -53.78862 | 2026-08-08 12:00:00 | TERRA_M-T | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ca715d8b-6fe7-35e4-b3d6-25f161986dd8 | -12.54212 | -46.92232 | 2026-08-08 12:00:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 3001e22b-485f-3cdd-916a-59de838f318c | -14.34045 | -54.98779 | 2026-08-08 12:00:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| daca7415-28fb-3f43-9c08-03749172986f | -18.12879 | -43.98944 | 2026-08-08 12:00:00 | TERRA_M-T | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 18.5 |
| ff5571fc-68f5-3f58-b338-42f29bacd50c | -14.3259 | -54.94521 | 2026-08-08 12:00:00 | TERRA_M-T | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 20c7b0ac-46e6-3e68-9fc7-b159fe5f2a66 | -15.70623 | -54.86227 | 2026-08-08 12:00:00 | TERRA_M-T | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 3dfb3e60-46ff-3df8-b511-f738b28fbb72 | -14.93922 | -48.27924 | 2026-08-08 12:00:00 | TERRA_M-T | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 25.2 |
| f13a1be2-f83f-383e-baf7-319725346b17 | -14.42299 | -45.65827 | 2026-08-08 12:00:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| dab3ac49-5c05-3773-abfc-82f24c6e6151 | -22.32354 | -49.52738 | 2026-08-08 12:02:00 | TERRA_M-T | FERNÃO | SÃO PAULO | Brasil | 3515657 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 0c01a466-c86f-37b1-a1da-cb743bdaf786 | -10.2662 | -45.7979 | 2026-08-08 12:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 66b5152b-4751-336d-a6ee-8781dd50e0b8 | -6.9791 | -42.9034 | 2026-08-08 12:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.0 |
| 018aaaca-e289-36dd-9a64-cdbaf5efa8ec | -10.2472 | -45.8002 | 2026-08-08 12:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 4995bb71-09ea-3e27-b5c0-871ee093d450 | -10.2662 | -45.7979 | 2026-08-08 12:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 948f411d-2874-320e-94c7-988a58966114 | -10.2472 | -45.8002 | 2026-08-08 12:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 9cda7e80-3adc-3505-bfc0-cca938c15c37 | -6.9791 | -42.9034 | 2026-08-08 12:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 114.4 |
| 49f17fbf-b534-3426-8b87-f2c0215f1ed2 | -8.5501 | -45.4044 | 2026-08-08 12:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 77.2 |
| c1ff4853-5954-37c3-bf03-cf7efdd215b6 | -10.2662 | -45.7979 | 2026-08-08 12:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 103.8 |
| f3be008c-b2e0-3a1b-9b72-a17b552b731c | -6.9979 | -42.9016 | 2026-08-08 12:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.9 |
| c5414895-ff37-33c5-becf-dd84c7328a01 | -6.9791 | -42.9034 | 2026-08-08 12:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.5 |
| 03567999-4b66-3a57-a2bc-42b48a2fd79c | -10.2472 | -45.8002 | 2026-08-08 12:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 169.0 |
| 2b38420a-5aa3-34d5-8d79-2fa61016cda2 | -8.569 | -45.4024 | 2026-08-08 12:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 71.8 |
| b10102dd-75c2-34f1-b443-ac44f0a1d58f | -10.2662 | -45.7979 | 2026-08-08 12:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 193.7 |
| f2df6e9b-9cda-31c9-8f1a-cb4b34afeb3d | -10.2472 | -45.8002 | 2026-08-08 12:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 211.4 |
| 4b8c02da-48aa-360c-bd42-68615fe5581a | -10.2659 | -45.8206 | 2026-08-08 12:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 834ee373-7d0e-34de-a773-fee412fc3612 | -15.6968 | -54.8534 | 2026-08-08 12:40:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 9ab88741-ed98-31fd-a705-f500a79b7860 | -6.9791 | -42.9034 | 2026-08-08 12:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 110.9 |
| 3ba22aa4-90c0-3a43-a2ca-ff06fda2f944 | -8.569 | -45.4024 | 2026-08-08 12:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| 47b1433f-df52-30cc-9359-7c973b8727c6 | -11.3099 | -44.8569 | 2026-08-08 12:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 8e6e5993-7380-3e43-9b4e-71849ace945d | -10.2472 | -45.8002 | 2026-08-08 12:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 1a4ab90d-a18f-3b6a-8873-8af992107c52 | -10.2468 | -45.823 | 2026-08-08 12:50:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 58.4 |
| e950dc83-8b74-3c88-aa98-c2fa04b2441d | -8.569 | -45.4024 | 2026-08-08 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 86.4 |


[Clique aqui para ver as próximas entradas](README25.md)
