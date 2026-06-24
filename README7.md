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
| 9ecc97d3-8cf2-33ab-a91f-bd0547e19d0f | -20.61952 | -42.27313 | 2026-06-24 03:32:00 | NPP-375D | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e66f5695-95b4-3567-b8c4-f81488329a09 | -20.61875 | -42.27666 | 2026-06-24 03:32:00 | NPP-375D | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| a4884acb-ae35-3d65-973a-f151687b1155 | -12.8548 | -44.3625 | 2026-06-24 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 303.0 |
| 4b795f00-aa69-3353-8ed1-f469d4185f37 | -12.8349 | -44.3892 | 2026-06-24 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 8f2ac115-3883-32df-aac5-faa5c3a51417 | -12.8359 | -44.3422 | 2026-06-24 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 271.7 |
| 29d97488-2796-3c21-b8d4-304f339927e9 | -12.8552 | -44.3389 | 2026-06-24 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 1419d6bc-3c33-3c53-a4af-cd4b1a2f5aeb | -12.8354 | -44.3657 | 2026-06-24 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 495.7 |
| acf86033-ee19-3bea-b1af-d42b0e5e2334 | -4.66279 | -43.12645 | 2026-06-24 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8df07abb-7dc8-3dea-bccc-fd8d5efdc86f | -12.86849 | -44.37215 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| feefc822-716b-3583-898d-c2c50b3b33b9 | -6.9957 | -42.89414 | 2026-06-24 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| e7aaf76e-4381-3207-9e8e-2e95956d1b7f | -7.92244 | -48.29114 | 2026-06-24 03:47:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2502481e-6379-318e-bc8e-dbcfdcefcdff | -12.8421 | -44.35606 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 05d51b78-9af4-385e-a794-318a062ad959 | -6.99009 | -42.89834 | 2026-06-24 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 5fceb6f4-4541-35cf-ab0a-ad8f5c3c75ca | -12.85057 | -44.36312 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 1a68e864-d0a4-3b8c-91a5-48f710c15878 | -4.6617 | -43.22588 | 2026-06-24 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8cf61606-8005-35a0-8bd0-371b09749fe7 | -13.18391 | -43.40275 | 2026-06-24 03:47:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 55c3cc85-64ee-32f5-8371-f81f0e33f80e | -12.77678 | -44.44071 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e0a9bb04-60ab-3023-82e6-1c2ee37d95fb | -14.89451 | -40.8972 | 2026-06-24 03:47:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 09843911-bd75-3a23-b66f-17f75846aea4 | -12.77303 | -44.43454 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| eb3d4585-b55f-3122-9c00-625d91d8cd7b | -4.66027 | -43.22738 | 2026-06-24 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d3e4c4d-8157-3ad0-9c58-92e157eec4d0 | -12.78427 | -44.45314 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cef5abb5-3437-3ebd-8ca9-e80d8579c7bb | -9.2125 | -47.92919 | 2026-06-24 03:47:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 55463c5d-fb45-3332-b385-7ee15c318ada | -8.61047 | -46.00222 | 2026-06-24 03:47:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 8dbf7206-b15a-3644-9eff-2274f76b519a | -8.60334 | -45.99857 | 2026-06-24 03:47:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 08cb4327-0a3a-3546-96c5-6fad58eafa19 | -15.01437 | -42.37122 | 2026-06-24 03:47:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c579398d-b673-39ff-a4c5-b58db52aea45 | -15.3645 | -47.36077 | 2026-06-24 03:47:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff7b57f3-3e74-33fe-b809-f0fc8448675f | -4.66635 | -43.22237 | 2026-06-24 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d70ff80f-1655-31c7-9758-6ad5a81706d4 | -5.50731 | -40.76045 | 2026-06-24 03:47:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4991a6a4-e6d7-37ae-a328-7baae8f5b4ea | -15.1104 | -41.08354 | 2026-06-24 03:47:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 585967ff-08f2-352d-9e15-6e3c91d520c5 | -6.83915 | -47.87563 | 2026-06-24 03:47:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1302cb7-597e-37f3-ae24-b8035c259613 | -15.30979 | -42.01585 | 2026-06-24 03:47:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4da32de4-fef1-3921-a860-0196dc7c8904 | -12.83914 | -44.37174 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 4f8ae1ff-f68d-3fbf-aa9f-3998c47df89f | -12.7809 | -44.44542 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 95c3bb01-66ac-3649-b9b4-f5903169c11c | -8.61054 | -45.9912 | 2026-06-24 03:47:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 70f45b3c-0a1c-37ff-ad17-8aa1ca8317f9 | -7.91734 | -48.29542 | 2026-06-24 03:47:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9e551439-bb8c-3311-ad85-fb9f61e91350 | -9.22344 | -45.3375 | 2026-06-24 03:47:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4f5af19e-5973-3c23-b03f-46f8f25ff859 | -14.84214 | -40.8331 | 2026-06-24 03:47:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1d1ae42d-5d99-33cd-b315-c800650dcd13 | -6.74756 | -39.17696 | 2026-06-24 03:47:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 65a69892-4298-3ad3-9e66-443da50b00f1 | -7.91074 | -48.29411 | 2026-06-24 03:47:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 81f93b97-9fb0-3dd8-a478-8c422df670f1 | -13.54939 | -42.483 | 2026-06-24 03:47:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bd69057f-a143-31ee-bede-44bbd83da63b | -8.6041 | -45.99436 | 2026-06-24 03:47:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 555d0906-206a-31ab-802e-67fd911a9d6f | -3.96499 | -43.11752 | 2026-06-24 03:47:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd4521c6-0214-3d70-a64d-22db26c82b58 | -8.60628 | -45.99331 | 2026-06-24 03:47:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 052ccfd6-9802-3f86-8543-884a2add9579 | -6.99679 | -42.89069 | 2026-06-24 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 29c19dc1-4bf4-3f0c-93d3-f01dac0f7091 | -6.83947 | -47.86637 | 2026-06-24 03:47:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0516f81a-0164-389b-96a7-e987ce20cbf3 | -9.20842 | -47.92878 | 2026-06-24 03:47:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bbf2d13b-7489-38fe-9d21-7c77a7f70027 | -14.28302 | -42.70908 | 2026-06-24 03:47:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| eb747fc4-1e02-3b0d-8795-90b176b7788c | -15.24206 | -40.62702 | 2026-06-24 03:47:00 | NOAA-20 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f4d2e5e6-b17e-32ed-8892-2b8fafe901ba | -12.19135 | -47.9682 | 2026-06-24 03:47:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| efff6698-216c-3174-8c62-184f1cc9aba2 | -7.37618 | -42.8037 | 2026-06-24 03:47:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 99bf529e-8617-3b23-a583-6e6a70289340 | -11.62319 | -48.49199 | 2026-06-24 03:47:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5f933689-e0b2-3dc2-aed3-3f9607851255 | -6.36627 | -43.59507 | 2026-06-24 03:47:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| e54eb23a-c262-397c-af61-1d29e708be4f | -3.96043 | -43.11366 | 2026-06-24 03:47:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44795bcf-fce6-3a9b-8542-86071346b5f6 | -6.50315 | -42.21826 | 2026-06-24 03:47:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| c475cff1-1bbe-3924-87fd-7d495f2b01ab | -6.99292 | -42.76793 | 2026-06-24 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a3ff8045-5bb7-3e78-b7c9-b28355ff0905 | -12.83264 | -44.35425 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 052701f7-a06e-3e60-aa09-39db4e831635 | -4.65777 | -43.1256 | 2026-06-24 03:47:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0fe97f5b-2c75-30a1-a3e0-c597b7ef4af0 | -9.38107 | -41.22034 | 2026-06-24 03:47:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| feb4eaa3-d2e7-3cdf-93c7-4520d0e2c41c | -4.66268 | -43.22 | 2026-06-24 03:47:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 505dbcfd-62bb-3a9f-ab20-8c2f4ae311e8 | -9.21206 | -45.33883 | 2026-06-24 03:47:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 188a8fd3-c95c-3e41-89b8-3758eb779a5c | -6.37126 | -43.59621 | 2026-06-24 03:47:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 4983a32d-ebc5-3427-8b27-086e3f97c7e1 | -8.6055 | -45.99744 | 2026-06-24 03:47:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| b766cd8b-7bcd-3b09-9372-0e2ec6e1f9fb | -7.29067 | -46.24194 | 2026-06-24 03:47:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba0eee7e-77f9-3666-b20f-ae0e977fea70 | -3.9589 | -43.12262 | 2026-06-24 03:47:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a1ebbbc-2bcb-3984-b740-9aa1a2cc5c97 | -12.83639 | -44.36035 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| dbdc4951-2ece-347f-b3bd-446aab73c44b | -12.77992 | -44.45068 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 39c3e6b3-ec91-334e-ab5f-357ba41b5d40 | -12.77951 | -44.45216 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 93032aa9-13cc-3cac-8352-1daf655cbd45 | -12.86946 | -44.36696 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3809e022-9146-30af-8993-075dc91e2462 | -15.75562 | -43.23294 | 2026-06-24 03:47:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 6fc50320-eb19-3001-9442-748e64ba416a | -12.78661 | -44.44118 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 941d2958-d05d-37ba-946f-69727ea40719 | -9.76509 | -41.88171 | 2026-06-24 03:47:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f93ec2f8-47be-33bd-9f89-6a58bda73f70 | -13.84779 | -47.04478 | 2026-06-24 03:47:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd774a14-e6a8-3268-9c57-26e0511c14a2 | -6.99023 | -42.90002 | 2026-06-24 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 979ed90c-2093-3a46-9471-5b3d307826e5 | -12.78283 | -44.43493 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 26a76cf3-081d-3664-a565-3875733f6bea | -12.78468 | -44.45168 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e63cebbf-9aa3-3128-a861-98638286ca24 | -15.01691 | -42.37238 | 2026-06-24 03:47:00 | NOAA-20 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2862f0ef-4c2e-30c3-a60e-dd39518e81ca | -6.99588 | -42.77895 | 2026-06-24 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| af2db999-ebb2-3981-bfc2-653a3f0d4ff9 | -4.12859 | -38.18671 | 2026-06-24 03:47:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e3f4530c-96c1-3733-bf61-26c0cd0ed794 | -13.40125 | -44.12096 | 2026-06-24 03:47:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3dc8796f-c3ab-35e6-9cef-c60fa4856e4c | -13.55007 | -42.47916 | 2026-06-24 03:47:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2409a6b2-a78c-3d5b-b54c-56b66174faf5 | -8.85493 | -46.94869 | 2026-06-24 03:47:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c3131cb-35fa-394d-a8f3-1da677e7b0d7 | -4.34884 | -47.76314 | 2026-06-24 03:47:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b3f00fac-a0fb-3009-932c-f8df54291ff3 | -9.22281 | -45.34093 | 2026-06-24 03:47:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f42c50f3-5153-3bbf-a3bf-d67c55db406d | -12.83166 | -44.35947 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| a465d113-1d25-35c5-87ac-ee16c3e43755 | -7.92505 | -48.29087 | 2026-06-24 03:47:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 834ebca1-ceff-366f-9ead-97fc30233528 | -4.35951 | -37.92282 | 2026-06-24 03:47:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c7433b16-ebb5-3ba3-81c3-30427f16200c | -12.82693 | -44.35854 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 68551a1a-4095-3170-9f54-70772e06e1dd | -15.72481 | -41.35102 | 2026-06-24 03:47:00 | NOAA-20 | DIVISA ALEGRE | MINAS GERAIS | Brasil | 3122355 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3043dea9-fe74-3431-b6e6-6cdc60871472 | -7.2891 | -46.2504 | 2026-06-24 03:47:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 976c73b3-7b34-385c-8493-85a1c1019f69 | -6.99206 | -42.88976 | 2026-06-24 03:47:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| bc9abb9d-2b4d-36b7-bbda-c6f32204f6ad | -6.99675 | -42.77388 | 2026-06-24 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6eed9eb5-6a71-3c4b-9e20-96d946308e69 | -6.9938 | -42.76283 | 2026-06-24 03:47:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 68773eaf-6c55-3b78-9637-397b34702128 | -6.75786 | -44.742 | 2026-06-24 03:47:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bcc11288-a4f1-36da-a4a2-e447098a8387 | -6.84025 | -47.86965 | 2026-06-24 03:47:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15ef3df8-9c12-3167-a9d7-93761f9bbb66 | -3.86727 | -42.96671 | 2026-06-24 03:47:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 77eccf8f-a0fc-32ed-a2bb-8ebc7ac38f2e | -3.87181 | -42.97046 | 2026-06-24 03:47:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07e64f17-684b-36d7-958b-5e52b744b0f8 | -6.83837 | -47.8721 | 2026-06-24 03:47:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3f91f3a-d7cc-36fe-beb3-bf0b85203777 | -12.84487 | -44.3674 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 38.8 |
| c85b6864-a76a-3f9d-bdb0-e33a807a21d8 | -8.8189 | -47.07026 | 2026-06-24 03:47:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ddebb34-6ceb-3e06-8955-f700f1947506 | -12.85155 | -44.35793 | 2026-06-24 03:47:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 58.5 |


[Clique aqui para ver as próximas entradas](README8.md)
