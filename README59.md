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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c20c4f5b-00b9-380e-9d1d-809a5e87bfb6 | -11.33464 | -43.54606 | 2025-08-28 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2ea4bd8-6b51-3784-b404-f06aa9ce2b88 | -9.15996 | -59.58694 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3dcfff7d-01bd-3ef6-9f6e-84d631c86179 | -10.54536 | -46.6952 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8e0c9fc-bbf9-3b75-814e-a5c579ee6531 | -14.13095 | -53.97365 | 2025-08-28 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9b571324-292a-3c55-94c6-74c19e4092ab | -14.3208 | -60.36763 | 2025-08-28 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0dc98e3-f0f4-3860-9702-1d747411c771 | -15.66536 | -52.74492 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fb10e240-8da1-3e95-a549-49727772e79d | -14.26338 | -53.07183 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f608ea3-6e15-3de8-bb03-aa8a67fce340 | -9.24733 | -59.78497 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 449f1b98-7adf-39a1-aa57-beb1476d003c | -12.89051 | -48.09962 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8db16143-3d1d-30c1-873c-639812cfb5a8 | -14.33656 | -51.93097 | 2025-08-28 04:59:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d4ff0a59-ddb9-3490-9019-202e1738fb87 | -9.49544 | -60.54075 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60825492-a814-34e9-881d-2c71ff4dadce | -9.40952 | -60.52209 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9448d0c-e16d-30d7-9a18-c8060c3b66f1 | -9.13184 | -65.28324 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7643a17c-2e14-3d50-a818-119555085772 | -11.60552 | -46.21835 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 98b70e4b-ad2e-3c42-99d6-1e2d030e45e2 | -8.9575 | -65.96536 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 57c27307-8c8d-369f-b2eb-1c7f52852340 | -10.4745 | -57.93521 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 00ecce19-cd39-3fe6-a605-a446ef9fbb68 | -9.58182 | -55.3872 | 2025-08-28 04:59:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f7cb4f8-c3e5-31b4-bd45-37bd99274992 | -12.80918 | -48.16332 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0df9f8b7-eaea-31ca-8fa6-decb88ed5cdd | -9.31838 | -57.70562 | 2025-08-28 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9abea251-8829-36ef-876b-c060373e49e7 | -9.19429 | -60.8065 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de04276c-55f0-362e-a765-a75c5056d42b | -9.2649 | -59.77698 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 203a213d-250d-3a90-940f-f20915e038a4 | -15.61787 | -52.71736 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f49677c2-a3ae-3201-ad82-77ded634f94d | -14.15155 | -53.9718 | 2025-08-28 04:59:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99ab2754-9069-30c6-a52c-f2c5e491d75d | -12.95168 | -46.33252 | 2025-08-28 04:59:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 775718e9-3580-30df-8aa7-7c698b194653 | -9.16893 | -59.55769 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f631c7e2-7acb-3add-80bc-f9840a502a5a | -15.08888 | -48.51839 | 2025-08-28 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| cfbd0568-09ba-33be-ab00-957fd9a51f0e | -14.26758 | -53.06816 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 158.2 |
| cb2e9a32-3f01-3917-9f80-66ccc13f2ff7 | -12.89401 | -48.11034 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 155301d6-745e-3e4a-8b12-ee7a90baafa2 | -14.31818 | -53.06135 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9cdd945b-43eb-3f0f-8b34-a1e3f68e81b0 | -9.15556 | -59.56564 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aa9f105f-c485-3012-8d6f-14a5147e02b6 | -13.4656 | -46.85165 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ae0cff6-0f85-3147-80d1-fc006f849263 | -9.41168 | -60.53408 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5dd7e580-3541-37df-b3b9-c1418702971a | -10.60572 | -54.90471 | 2025-08-28 04:59:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3bb1df50-5052-3592-99d1-2cd8c2659381 | -12.82102 | -48.10764 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5fcfacbe-7bdf-3d1d-b912-baa027097e89 | -10.52299 | -46.7072 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7fb5fbfb-d307-3739-ba26-66edf980af1a | -14.27695 | -53.0677 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 0222aaa6-f2ca-35ca-8661-034934118e3f | -9.40408 | -60.52893 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe017f99-f2bf-38d9-a1fb-57fb29b01e5b | -14.29426 | -53.04885 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| a9903ba6-5a08-3f11-9340-1f464d690c3a | -9.55311 | -65.69041 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3311c289-771a-3d59-af89-cd9b43bfe369 | -9.49444 | -62.39644 | 2025-08-28 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 176a4f75-bdd5-3839-a2a0-cf04d99975e8 | -10.52338 | -46.70414 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6eb35f9-a85b-3e3a-91ca-dbf5eb1fe96d | -14.59768 | -54.50737 | 2025-08-28 04:59:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc07af3f-5e49-3c48-814e-9c9b4ec8d822 | -13.66704 | -46.91041 | 2025-08-28 04:59:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1efec074-6446-3fce-807e-b4ea0c167bda | -12.82038 | -48.11272 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1be0392c-7cbc-3bb5-a157-94740f86db17 | -10.81419 | -60.77545 | 2025-08-28 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd029957-9d4e-3d75-af41-c35ac0ba35e3 | -10.82366 | -60.76951 | 2025-08-28 04:59:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 387a9b44-c084-3a37-89a3-98c1a8f48bc7 | -9.1564 | -59.56073 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6e3f7b3-2a4d-3b85-bfb9-e02167dac560 | -9.12033 | -65.78977 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 7bb012f9-bc39-3a8f-8523-7c2f9580f969 | -13.52525 | -46.93552 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5d1d40d5-d81d-390a-aec5-e21c847955c4 | -12.79233 | -48.18139 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2ba801de-7c28-3f8e-8a82-3a55e4224b85 | -10.47748 | -57.94297 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e1e6c148-9118-3cba-abab-a82af89fb6ed | -15.61902 | -52.736 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce8cc06c-4efd-35ee-bfd8-3542cb97bcb7 | -10.45946 | -57.96112 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 977a36b4-af41-361c-8ede-6f9dde0c2893 | -11.22576 | -55.05035 | 2025-08-28 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a22b4dd2-090f-359c-8fb0-2ba297ac9da7 | -13.4207 | -47.00414 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 747b87b9-2012-31c3-aba6-0b9b95dab63d | -10.4902 | -51.58634 | 2025-08-28 04:59:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ede40cd2-6b6d-3995-b8ca-8f8f38b4c085 | -9.1421 | -62.35703 | 2025-08-28 04:59:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 66d66a27-a5d0-31fa-8849-bf63ba231532 | -16.37038 | -43.78755 | 2025-08-28 04:59:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bd84a40d-b738-3cc6-b178-18eacdda9f21 | -11.84219 | -46.80203 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67b7466c-2e9a-3643-9582-b4a414cd7f5a | -11.22136 | -55.05685 | 2025-08-28 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f4218839-a7aa-3ae4-bd95-c0505c3fcca0 | -12.1855 | -47.18814 | 2025-08-28 04:59:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f5690079-45a0-3789-984e-e7fd1d04ee72 | -15.63757 | -52.75452 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 898ee076-2d52-330c-86d3-d328bbc7d826 | -11.79471 | -46.80281 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f2937ce7-d0be-3959-897b-58378fb8c00f | -13.42434 | -46.97421 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a738d515-3a5c-3e08-b12d-c81cf4661d1f | -13.41997 | -47.01017 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17ce2d54-a93b-3c39-ad9e-5ecd0ea0ce32 | -10.32535 | -46.78085 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 935cf5c6-dae5-3447-8273-bdf8cea12592 | -9.12272 | -65.77718 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 942e2d44-1085-36e6-afaf-1e3378072680 | -15.08557 | -48.51165 | 2025-08-28 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5e06d0d1-b090-3ef8-9269-0172526b5b39 | -13.52178 | -46.91985 | 2025-08-28 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 27160685-b00a-3a09-93bf-24b496a56d41 | -9.7184 | -56.17724 | 2025-08-28 04:59:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| baa33b56-7ae0-3cbf-b4d3-1538f2d03565 | -14.33227 | -53.26825 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8da90991-2f92-395c-a82e-af358c9be745 | -10.5253 | -46.68892 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e1ac22e-43bc-3759-a132-f0a7349ecbfe | -10.27937 | -64.49628 | 2025-08-28 04:59:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1ea16865-dae0-3915-92aa-f6e492a12774 | -14.26882 | -53.05966 | 2025-08-28 04:59:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 04a6144b-6596-3bf4-a2bc-ae525736acde | -10.60903 | -54.90523 | 2025-08-28 04:59:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd286a9f-87f1-38cc-b04d-f982c7587b26 | -13.62271 | -48.242 | 2025-08-28 04:59:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3bb606a7-dde1-3ceb-83de-84a6c634bb83 | -9.10912 | -60.32474 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f1eb48e-4073-3700-9527-2a2aff482c27 | -9.08999 | -65.73289 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 113d2974-e8a9-3199-87af-eb7b446b04fe | -11.32195 | -43.54435 | 2025-08-28 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7aa2d389-2954-341a-8b2e-822d76bb7282 | -11.22635 | -55.06843 | 2025-08-28 04:59:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6bf78481-8f83-3df1-bc0d-a10efc99cc59 | -15.68574 | -52.76163 | 2025-08-28 04:59:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1dbf1ab-a0f1-37f1-bd6d-2ef3964888c0 | -9.08577 | -65.72301 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e3aae51-2f32-3561-a959-35d4636454d5 | -10.52847 | -46.70505 | 2025-08-28 04:59:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98132795-8b55-3706-a634-8aa6184ef54b | -11.81353 | -46.82076 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8661fd0-f6c7-3ffa-8956-3fae8b73730e | -10.59081 | -54.89156 | 2025-08-28 04:59:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 208eccab-4ace-3c67-b7c0-12b82dcfcc5e | -9.78789 | -64.25483 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64480af6-8b5d-3693-b4c5-298d090de4d6 | -11.55811 | -46.33719 | 2025-08-28 04:59:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d31f73f-3bda-3c3e-ac16-89eb7b7d5a02 | -15.09676 | -48.53463 | 2025-08-28 04:59:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 36dc4aad-0771-35e2-ae5d-8e4ce88f9dcf | -9.3965 | -60.52374 | 2025-08-28 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2652507-d9ff-3015-b88c-d8fc495c8652 | -9.19952 | -60.28748 | 2025-08-28 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0876a45a-6beb-30cb-b15f-597b59ce6414 | -9.06882 | -66.06018 | 2025-08-28 04:59:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6c5732de-7e25-33e5-a2fd-9cc809a5a524 | -11.33704 | -43.52502 | 2025-08-28 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9329b7e2-8f38-303d-b24c-e2a6998fad29 | -10.4755 | -57.95483 | 2025-08-28 04:59:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 770e6cc4-cb41-37d9-a182-6db1510f88bc | -8.23143 | -61.46066 | 2025-08-28 04:59:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e6a43e7b-f50a-3a0f-a81a-e5f4814172ab | -9.31839 | -57.70177 | 2025-08-28 04:59:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7f316f2f-cccf-3ae3-a544-0a01019f96af | -11.34733 | -43.54777 | 2025-08-28 04:59:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 9a6341bd-7ae9-3ca6-b445-891052db064e | -9.66491 | -64.98778 | 2025-08-28 04:59:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 96edf27d-68df-342c-ad0e-fc40402954f0 | -12.89982 | -48.10051 | 2025-08-28 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a642f254-8534-31f5-9caa-8c7348c11eee | -10.84919 | -54.02974 | 2025-08-28 04:59:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e19ceea2-6c24-3d25-99e5-34e08d3ea6d1 | -9.54012 | -62.39801 | 2025-08-28 04:59:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |


[Clique aqui para ver as próximas entradas](README60.md)
