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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a201d948-0328-3d9a-bb28-8b0dabf0cb7d | -14.859 | -41.36145 | 2026-08-22 11:17:00 | TERRA_M-M | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 8.2 |
| cb12fc65-f73b-3402-9168-fa8ecf9d9567 | -16.84918 | -46.34488 | 2026-08-22 11:17:00 | TERRA_M-M | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| e035f223-67be-39b7-adaa-f3bf125e94be | -18.27718 | -43.30586 | 2026-08-22 11:17:00 | TERRA_M-M | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 667f9ec0-2b9b-3fab-b82e-6a4161f8d8a7 | -19.3309 | -44.95358 | 2026-08-22 11:17:00 | TERRA_M-M | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| fe80e87d-9c65-33d5-9f4a-91c4135ba878 | -14.86034 | -41.35228 | 2026-08-22 11:17:00 | TERRA_M-M | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 635a63c2-1e5d-3793-8314-ac04343a70f3 | -14.13361 | -48.06798 | 2026-08-22 11:17:00 | TERRA_M-M | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 80c02f06-9d71-397a-8375-0c1c54a1ab60 | -18.56435 | -43.30128 | 2026-08-22 11:17:00 | TERRA_M-M | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 9acbd7f7-2f80-3053-8ad4-03b5f6d2fd0a | -15.44544 | -41.38401 | 2026-08-22 11:17:00 | TERRA_M-M | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 4748c930-a81a-351b-85fa-8e70bb651cce | -17.60673 | -44.63199 | 2026-08-22 11:17:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 62.9 |
| fc6368b6-3d6b-32e3-b9ff-a8c27ce1e0c7 | -17.12366 | -40.54127 | 2026-08-22 11:17:00 | TERRA_M-M | ITANHÉM | BAHIA | Brasil | 2916005 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 01991f4e-7609-3168-a5d3-44d292854bc8 | -19.83621 | -46.98845 | 2026-08-22 11:17:00 | TERRA_M-M | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e7b32634-00f7-38b8-a6bb-93d5d93fe56a | -18.28483 | -43.3175 | 2026-08-22 11:17:00 | TERRA_M-M | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 075d77e3-6caf-3e3a-898c-a2f4e0ebdc9d | -17.8485 | -44.46597 | 2026-08-22 11:17:00 | TERRA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| bea24efe-f2a5-36bf-850e-61d6e1a232f6 | -16.84084 | -46.33641 | 2026-08-22 11:17:00 | TERRA_M-M | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 03f6ee7f-51c8-3906-8bba-21d9a63bcb80 | -14.37894 | -42.83872 | 2026-08-22 11:17:00 | TERRA_M-M | CANDIBA | BAHIA | Brasil | 2906600 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| cd8a3c29-4e41-3bdd-96a6-0617674eee06 | -16.13135 | -43.63805 | 2026-08-22 11:17:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 15.0 |
| de70668f-f8e2-305e-a0d2-85274c056169 | -18.27413 | -43.3257 | 2026-08-22 11:17:00 | TERRA_M-M | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 34.6 |
| d540ae06-d1f2-35be-9102-cb8469405e05 | -14.19835 | -41.58674 | 2026-08-22 11:17:00 | TERRA_M-M | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| ab129da0-6f3e-3a69-8d22-5c59392b0159 | -16.13303 | -43.62721 | 2026-08-22 11:17:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 18.5 |
| d7f170ee-ac5a-31cd-a93a-1242a06d8260 | -18.88942 | -43.6511 | 2026-08-22 11:17:00 | TERRA_M-M | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 6cfdd2c1-43f4-3dc4-b06d-b2d5f8269789 | -18.92656 | -43.59523 | 2026-08-22 11:17:00 | TERRA_M-M | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 4456e79b-5ac5-366a-b42e-9210665512d2 | -18.27565 | -43.31578 | 2026-08-22 11:17:00 | TERRA_M-M | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 52.8 |
| f66745ea-a172-3251-8a48-ef33b72cbeab | -18.28329 | -43.32756 | 2026-08-22 11:17:00 | TERRA_M-M | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 30468995-27ef-3e65-96ea-be64bd282af8 | -17.95922 | -42.72728 | 2026-08-22 11:17:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5e50cf1f-b468-3a7b-8dfc-2d592bd45564 | -16.83819 | -46.35254 | 2026-08-22 11:17:00 | TERRA_M-M | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 3079d151-34f4-3564-8323-c53c6bea38a2 | -18.9173 | -43.59358 | 2026-08-22 11:17:00 | TERRA_M-M | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 75d12de8-dabb-3c84-8208-aadf60304f86 | -16.95655 | -46.12182 | 2026-08-22 11:17:00 | TERRA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 31.0 |
| be05782b-bf25-3f0e-900e-dea045109df7 | -16.95566 | -46.12764 | 2026-08-22 11:17:00 | TERRA_M-M | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 9e5fb773-742e-3f4a-bcb9-65acaab0d3c9 | -21.61908 | -46.48064 | 2026-08-22 11:19:00 | TERRA_M-M | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 8d2f1cff-a5d1-3df1-9a10-4c9df26bfc7a | -21.24336 | -45.38534 | 2026-08-22 11:19:00 | TERRA_M-M | COQUEIRAL | MINAS GERAIS | Brasil | 3118700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| b5c31017-c42c-3503-82dc-df3d830ce471 | -21.24136 | -45.39741 | 2026-08-22 11:19:00 | TERRA_M-M | COQUEIRAL | MINAS GERAIS | Brasil | 3118700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| ca69b590-3ef9-360d-940c-69029099f52c | -20.97738 | -43.63798 | 2026-08-22 11:19:00 | TERRA_M-M | SENHORA DOS REMÉDIOS | MINAS GERAIS | Brasil | 3166204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.1 |
| a400f373-3482-3f1e-9598-66f5a629fded | -21.2418 | -45.39082 | 2026-08-22 11:19:00 | TERRA_M-M | COQUEIRAL | MINAS GERAIS | Brasil | 3118700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.8 |
| a9339bc4-2f62-364d-a93d-079a37ea1671 | -21.6231 | -46.48795 | 2026-08-22 11:19:00 | TERRA_M-M | BOTELHOS | MINAS GERAIS | Brasil | 3108404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.5 |
| 7ccf314c-d339-37ef-9f8d-7e6bbb1584ec | -21.19246 | -45.50683 | 2026-08-22 11:19:00 | TERRA_M-M | COQUEIRAL | MINAS GERAIS | Brasil | 3118700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| f64e0592-a00d-3e9a-848d-96267c6038a5 | -8.522 | -54.8209 | 2026-08-22 11:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 72012ed6-1e04-33f5-a752-7dc7a0b929f0 | -11.5864 | -46.5762 | 2026-08-22 11:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 133.2 |
| c0ec11a6-b22e-3e79-a4bb-afd1e5dddc53 | -6.8018 | -59.4201 | 2026-08-22 11:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| ef1fed63-d5ab-310d-8653-ff0efd018fa4 | -8.5406 | -54.8197 | 2026-08-22 11:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 43fe2b92-9198-346b-ae92-b0562771f35a | -18.2855 | -43.3119 | 2026-08-22 11:20:00 | GOES-19 | COUTO DE MAGALHÃES DE MINAS | MINAS GERAIS | Brasil | 3120102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 125.8 |
| b704bb6e-f9a4-3afa-a331-6d0bef4e9764 | -11.4494 | -44.5353 | 2026-08-22 11:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 408.4 |
| fed0aeca-20e6-3dff-a494-bd75886010d3 | -11.6059 | -46.551 | 2026-08-22 11:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| fcb581f5-b320-3b76-b9a4-948b85722a40 | -13.9967 | -53.7062 | 2026-08-22 11:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 86.7 |
| c7563ba4-e89e-3c76-b58e-7cd89c8d175e | -11.449 | -44.5587 | 2026-08-22 11:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 08a8ba57-0150-34fe-880a-4fa451a6290f | -14.3937 | -51.8012 | 2026-08-22 11:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 26862408-ff9a-3690-89f2-865a665b5ee7 | -11.6055 | -46.5736 | 2026-08-22 11:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 9d7e0fcf-621f-3416-b90d-83a7ad69c30b | -11.6055 | -46.5736 | 2026-08-22 11:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 180.7 |
| 0f51819c-1dca-39a2-90a9-32c6a36f5e35 | -11.4494 | -44.5353 | 2026-08-22 11:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 305.0 |
| 14c51219-703d-305e-a55c-f1ebbbf20d76 | -11.6059 | -46.551 | 2026-08-22 11:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 5156bf9d-0c47-35e0-960e-9d01f570e771 | -8.522 | -54.8209 | 2026-08-22 11:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 432277a6-afc5-3b9c-8ab1-ba9adadc6378 | -11.449 | -44.5587 | 2026-08-22 11:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 9ffb257c-d42e-339b-a424-1d2033905bfc | -11.5864 | -46.5762 | 2026-08-22 11:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| b3b00d7e-7041-3634-a694-84069323ece7 | -6.8018 | -59.4201 | 2026-08-22 11:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 5c320ee8-ded3-32bc-b34d-bd7a966b38ca | -6.8018 | -59.4201 | 2026-08-22 11:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 4552f601-91bb-366c-9087-535ffec93d6c | -11.6059 | -46.551 | 2026-08-22 11:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 0aacb996-75a5-3b8c-8a75-c89dbbdf5687 | -11.4494 | -44.5353 | 2026-08-22 11:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 547.5 |
| d498ffdb-8e5c-35d7-988e-760a04a3d399 | -11.625 | -46.5484 | 2026-08-22 11:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 80.5 |
| ec7931f9-35c3-36b8-a5b8-7114982911de | -11.449 | -44.5587 | 2026-08-22 11:40:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 114.5 |
| a4c21fb6-33f8-3a3f-9581-c2941dd0c6ce | -17.6092 | -44.6119 | 2026-08-22 11:40:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 55c24f56-bc9e-3198-8970-2ef4d596ea8a | -11.5864 | -46.5762 | 2026-08-22 11:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| bf75135a-f3b1-3385-821f-5f3fc875e77d | -8.522 | -54.8209 | 2026-08-22 11:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 81b377a9-69ec-31f0-9ef9-10f13a9afea6 | -8.5406 | -54.8197 | 2026-08-22 11:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.5 |
| b4ba4cd8-fb96-3132-81be-f13571aa1d0a | -11.6055 | -46.5736 | 2026-08-22 11:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 118.1 |
| a50cc37e-74b9-3845-aba6-d076eb870efa | -5.9997 | -57.8054 | 2026-08-22 11:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 9ba342ad-b288-3d5d-8347-b23309c8f280 | -8.5406 | -54.8197 | 2026-08-22 11:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 119.8 |
| bab60732-cf98-3537-b601-a9d6ec83fcb3 | -11.449 | -44.5587 | 2026-08-22 11:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 5438aa64-bf0a-310f-a59f-070fc2111afc | -8.522 | -54.8209 | 2026-08-22 11:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| d7257c9c-0122-365b-b1a3-c7a9c0fbc3ca | -11.6055 | -46.5736 | 2026-08-22 11:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 5448eaf4-8b08-3699-9010-659f86ce0b27 | -11.4494 | -44.5353 | 2026-08-22 11:50:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 713.3 |
| ad086bd1-d45a-3d98-b3f8-78eb5a5618c0 | -8.5408 | -54.7995 | 2026-08-22 11:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| b57f8649-79df-3ca5-9016-cead328fdc7f | -6.8569 | -59.4564 | 2026-08-22 11:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| fefef4e8-6537-344b-9ac1-66234f7c7e56 | -17.6092 | -44.6119 | 2026-08-22 11:50:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 0768b368-4e90-37e9-81e0-cac4c15d5d43 | -6.8018 | -59.4201 | 2026-08-22 11:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 0349459b-0a55-35b5-9de6-004fc081096c | -11.625 | -46.5484 | 2026-08-22 11:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 629721b3-d4a4-3873-b17a-034b4dc1d9ab | -11.6059 | -46.551 | 2026-08-22 11:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 147.1 |
| d5b14f84-c5b7-303d-819c-713ee465c8dd | -6.7692 | -58.6679 | 2026-08-22 11:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| dc1a4164-1421-3ecd-972c-2d458519525e | -11.4494 | -44.5353 | 2026-08-22 12:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 495.7 |
| 55b703a6-a15d-3b98-9b42-f95b27408a2d | -6.8018 | -59.4201 | 2026-08-22 12:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 56e622aa-e593-33e7-b588-efd8f6d6c5ad | -11.6055 | -46.5736 | 2026-08-22 12:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 6933a7c4-eefc-3309-89df-986d51ae5fcd | -8.522 | -54.8209 | 2026-08-22 12:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 216e2cff-ad37-3e97-85b4-2ff7cfc3a129 | -6.254 | -55.391 | 2026-08-22 12:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 429f39f6-944e-3a4b-bbdf-de48f2285389 | -6.8568 | -59.4757 | 2026-08-22 12:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| c373c1a9-d638-3912-90df-bdf2edd203ed | -8.5406 | -54.8197 | 2026-08-22 12:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 3908fd70-c25d-31f4-aeb4-9ae5c80d3e92 | -11.6059 | -46.551 | 2026-08-22 12:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 136.0 |
| 0f9fe1e6-3b30-3f6c-9005-e2f92f9c180d | -6.8569 | -59.4564 | 2026-08-22 12:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 6eac66ca-5641-374b-a399-62321fa9b0db | -17.6092 | -44.6119 | 2026-08-22 12:00:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 6ee80165-c0df-3c3e-bd08-acb73025fbc4 | -11.449 | -44.5587 | 2026-08-22 12:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 180.1 |
| 467b6c07-220f-3b24-8ac4-9a72c0694313 | -11.4298 | -44.5615 | 2026-08-22 12:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 74.2 |
| bfebe64a-d9e6-301d-9da8-4f69cc4fac55 | -6.7692 | -58.6679 | 2026-08-22 12:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| ad3f6954-7629-3909-ac7b-9d78eb510364 | -14.3937 | -51.8012 | 2026-08-22 12:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 102.5 |
| 8be08d72-26b8-384a-873f-a22dcef76403 | -11.625 | -46.5484 | 2026-08-22 12:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 73b2e63a-76fa-34a2-8a92-b5fa5e44297a | -6.8568 | -59.4757 | 2026-08-22 12:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 0087c772-a09d-3866-8c12-8ef1b87a3a2e | -6.8018 | -59.4201 | 2026-08-22 12:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.2 |
| b10f19c2-2a20-3b6a-8f52-2d6977610ad7 | -6.8569 | -59.4564 | 2026-08-22 12:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 696b2b5b-bd43-3cac-b29b-48870f7914df | -11.4494 | -44.5353 | 2026-08-22 12:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 529.2 |
| ebc54bf6-ba19-3cdf-89d4-17e5682a9632 | -6.7692 | -58.6679 | 2026-08-22 12:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 816f34ea-f44d-395f-be47-76ad7a7667eb | -8.522 | -54.8209 | 2026-08-22 12:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 102.9 |
| 31db7150-3653-363c-b6f6-a4d8527914c3 | -11.6059 | -46.551 | 2026-08-22 12:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 148.1 |
| 644fad04-f175-32b8-ae7a-d9db8fba08eb | -11.625 | -46.5484 | 2026-08-22 12:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| c58ab109-9527-3a70-b317-57096b87caeb | -11.449 | -44.5587 | 2026-08-22 12:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 164.0 |


[Clique aqui para ver as próximas entradas](README85.md)
