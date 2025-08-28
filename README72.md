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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f368a730-d153-391c-8ed9-5c52f0fadc9e | -9.48602 | -62.39177 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb8f7661-56b2-3e02-b1f4-6e487b739f04 | -8.9199 | -65.92598 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d854516-5384-3fa1-8a9e-86412ed936c9 | -9.81177 | -63.07782 | 2025-08-28 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4875bc6-0143-31ec-9f93-3412cdf98523 | -6.65268 | -53.19017 | 2025-08-28 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 649d709f-f91a-324a-93ed-2b2d67f1790b | -8.91911 | -60.71757 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e63b3dbb-22bc-34ba-806b-8eefb166040a | -9.3959 | -60.52344 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e7988f1-e0c5-3f4f-a8ce-7a2aeb3cb596 | -13.38347 | -51.75534 | 2025-08-28 05:25:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0a0e4001-75cc-31b6-9444-bfdb64c28c71 | -8.90216 | -60.55011 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3938da77-8a6d-3c89-a0e2-ad1f16637ca4 | -9.45537 | -51.94931 | 2025-08-28 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4e7dcd75-67c1-3767-b6c6-697295637292 | -9.44808 | -51.96354 | 2025-08-28 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c48214c-0e7f-36bc-b816-ade8432d37cb | -8.55814 | -62.64282 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1c4a3371-8743-3c66-ba7e-f19d2abb5fac | -9.41258 | -60.52608 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5733d1db-fb07-397d-8410-6307d613b12b | -9.13076 | -65.78393 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| ed35d0b4-7ae6-3839-96bf-49796295e59c | -9.25867 | -65.89487 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c20958be-4416-383e-9ea0-b1bff55414e9 | -9.40312 | -60.52098 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 65be2d34-199d-307c-a797-27ebb6ae8c40 | -9.48718 | -62.38456 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba294666-a69c-354a-bc85-6566943748e1 | -7.54283 | -63.85069 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53adaf67-f46e-35d9-986e-46b58e8ce836 | -9.1814 | -60.85989 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d2d5401-b6b2-3eec-91e8-237203e10910 | -9.1189 | -65.78178 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.9 |
| ca22aea6-3cd4-361f-8a83-81c465847776 | -10.47213 | -57.94715 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50354324-00fd-3130-ae0a-b0fab2820abe | -9.4187 | -60.53067 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1aed112c-64dd-3835-ad48-97c357e19922 | -8.57854 | -63.93077 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b75e90e0-8b22-3f60-88dd-358a21e9048b | -8.25837 | -61.4575 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b13605b2-8b76-392a-9e26-c3273fcf262c | -9.80458 | -61.19944 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db22f5f3-32c7-3f1f-bd92-6b22c77d1c6f | -9.16382 | -59.56092 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f55e9b3-1ada-32e0-bf38-b220af77c1e5 | -8.90351 | -62.47255 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6b4e0f53-6f01-3b9d-af95-afece9d5d402 | -6.01072 | -57.85288 | 2025-08-28 05:25:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 429d6905-8761-3066-8e5c-1a7a7198992e | -9.13821 | -65.28564 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 98041f27-3c1d-3ba2-b5a2-ef63f66ac72c | -10.48249 | -57.95327 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8a4836da-06bc-3f6c-9c61-72a5b748b0c7 | -8.94413 | -65.95264 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce223bcb-52df-3d67-9c1d-0938a70462c4 | -7.81757 | -62.33977 | 2025-08-28 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5679bb68-c6b9-38fe-832d-1cb72a16611e | -9.13053 | -65.28436 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f26681f0-5b89-3958-8f9a-ada7dc1f8f5f | -13.63239 | -48.24573 | 2025-08-28 05:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 804479df-b93c-37a2-a2b7-0f86201af6f1 | -12.68215 | -48.18515 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 134d2e2a-e70e-3b8b-946f-16d053bcf673 | -9.17115 | -59.51332 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5f6fabe-7882-33b1-9bff-8c9f43f9357a | -10.79938 | -60.76309 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 76bd5a54-326c-34bb-af22-5f9f7f4fc183 | -9.24521 | -64.41307 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 821354ea-112f-3151-bb24-e135003dc8f0 | -7.42063 | -60.0086 | 2025-08-28 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80968b1d-8ba6-35c9-8c52-51a6984ccf4e | -9.41811 | -60.51253 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a1f565c-68b0-38e5-ab58-de0d62152930 | -12.81636 | -48.14281 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 68b3654c-5b0d-3692-a006-61346e9a3af8 | -7.46497 | -61.40248 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4b2a80a-6d09-3cfd-ae65-5efb93c13f3b | -9.13027 | -65.76286 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a9374db2-087f-3e3e-b74d-780d7d641d62 | -10.60219 | -55.40178 | 2025-08-28 05:25:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 118570c6-fceb-30c4-b6ad-653eab3548f6 | -11.36254 | -63.27203 | 2025-08-28 05:25:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ac8e17a1-5c8d-3936-9c08-ef806a8a502f | -9.24886 | -64.4137 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 43db3003-363a-3816-b3dc-905dd4486bd5 | -10.8083 | -60.77178 | 2025-08-28 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0f81afe1-887a-39c9-8625-9030f68ee2e0 | -13.00761 | -56.91218 | 2025-08-28 05:25:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54f1592c-17e9-3c76-9db3-3acfda527b5a | -9.12508 | -65.79336 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 926c9b6d-21d3-33d6-8440-dd47e5968d44 | -9.22068 | -60.80523 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0e4c31b4-a734-3429-b4bb-b6fa795b1e75 | -13.61523 | -48.23399 | 2025-08-28 05:25:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 599954d2-173f-3daf-b971-9226372dafaf | -13.39014 | -51.75396 | 2025-08-28 05:25:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c5608069-8b59-3890-92de-bc1a00a5e87f | -10.4691 | -57.94223 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1d137a70-da41-3529-a919-cabe4d2174eb | -9.53687 | -62.4033 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 87526de5-ff14-3bd5-8bc4-4afc2078eeee | -10.27739 | -64.49509 | 2025-08-28 05:25:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| faea06f4-bd82-3f81-bc5f-5e40d9cb5bd0 | -9.31112 | -57.70291 | 2025-08-28 05:25:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 92b1373d-8120-35cc-b783-9dc779686ee9 | -8.90737 | -60.71237 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c8c43dd0-1c5f-3e66-8365-49f72f2e1fd8 | -8.89135 | -60.74923 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 18e65591-c665-3d4c-8a53-a698c8371088 | -8.96176 | -65.97014 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4717d6bd-01a5-36ae-a40d-65c2f4da25eb | -7.47333 | -61.39301 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5de34273-9dd8-3dcf-b766-7dbb1e771a3d | -9.45585 | -51.94562 | 2025-08-28 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5fb97110-1f27-3b08-9f4f-52d81fd30827 | -9.06641 | -66.06447 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cbefc958-14fb-3ef4-b573-95aaabbf51da | -9.17743 | -59.6078 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec94f679-140d-3e03-bd2b-e44ca9c5a088 | -12.82353 | -48.14294 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5cba4266-24ef-3892-90f6-9d70cdae7b25 | -5.9198 | -61.30463 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 060258c1-4720-3b9d-8990-c5652ab8f6be | -8.89673 | -62.47144 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4097f53c-258c-3c2d-9497-c9196943ec8e | -9.16379 | -59.51592 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6392172a-3675-3fc0-ac94-3cf26c9c935b | -6.6488 | -59.08524 | 2025-08-28 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b30f5262-ae27-3b84-b8c8-f1e1b550795c | -9.41642 | -60.50143 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fc3020cf-9b62-35ef-a88b-165f1cc0e239 | -7.35141 | -59.65864 | 2025-08-28 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d2246213-e99b-38ec-89e4-b08b75484603 | -9.46124 | -51.94619 | 2025-08-28 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0753693e-d2b6-38cb-b65e-8871e8cf1647 | -9.48102 | -62.37986 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ee06080-3c5a-3d80-ae64-430a763852cd | -9.14638 | -60.77906 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9850ff4-4173-3969-8440-c32ed00a0fd1 | -12.7935 | -48.18189 | 2025-08-28 05:25:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e787568-151b-34ef-b311-7b05e9ba104c | -6.92963 | -62.93183 | 2025-08-28 05:25:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d28f0325-380a-3c0a-b9ee-77530a193667 | -9.40375 | -60.56076 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf9986ab-f3d3-3aaf-a3b9-601fc2845e6d | -8.94875 | -65.94983 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0088b358-5e1e-331e-b8f9-e33cc0cf86f2 | -9.16495 | -59.55358 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1dfb8936-5cd5-3009-b822-ff593ff0069d | -8.96016 | -65.95545 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab78e5fd-7be7-3a58-9282-ef25036ea7bc | -8.69146 | -63.83444 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b0fe6f95-6e5b-3416-ac14-3546c3b58b1e | -7.35086 | -59.66218 | 2025-08-28 05:25:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86f92116-3a4e-3621-a0b0-a53758630481 | -9.45289 | -65.42314 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 07c66f2f-f2e4-3430-b556-b1d83afb4f80 | -7.54353 | -63.84651 | 2025-08-28 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| be43135f-8c41-381e-8c7e-a796fe8b24a2 | -10.03546 | -59.3549 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0aac6b1e-e2b2-3551-be86-63400da0af12 | -10.47406 | -57.93403 | 2025-08-28 05:25:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 773b085f-99e0-3bfc-b4e9-c30460dd08eb | -9.50976 | -62.78442 | 2025-08-28 05:25:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 818225fc-e547-39f3-b31c-f26e2138c62a | -9.46336 | -60.30975 | 2025-08-28 05:25:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f492a05-b4ec-3ff4-bc67-64489a7da5f6 | -9.66013 | -48.31059 | 2025-08-28 05:25:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| de041f55-1c6e-3b1d-b706-feeceb9ce53e | -8.63283 | -62.65444 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 87827404-98c2-3c70-8139-099f95b04b6c | -9.16861 | -65.80098 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ce39a03-3d67-3dc5-9804-176d6b34c795 | -9.48881 | -62.39594 | 2025-08-28 05:25:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ef15921-92c3-33fa-b0db-9819866c9070 | -8.93191 | -65.92803 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8ca32351-b9f9-353c-8f93-58ae4f0af348 | -9.08117 | -65.71751 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d386e2d-1310-34d5-8185-e906d971fcad | -8.55832 | -62.62011 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1607f14-38e7-3fa5-9892-4266dbd532e9 | -8.96056 | -65.97713 | 2025-08-28 05:25:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e06ddbd-691d-331b-b6a0-90a74d039453 | -8.91735 | -60.71395 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3e038134-4b59-3460-baa4-2cab52ba0f00 | -9.15594 | -59.58953 | 2025-08-28 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ce96e8f9-9e8a-3dea-9cf1-8c3b58ed7ba5 | -6.23621 | -60.01258 | 2025-08-28 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c190f4e7-85dd-338d-be13-a0c9dfe78357 | -8.26138 | -61.45431 | 2025-08-28 05:25:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 89dd80c3-7c5c-39da-af19-054783a3ccb9 | -7.8106 | -55.22542 | 2025-08-28 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 66595cce-5509-32ce-ac84-383d1429e0fa | -9.78943 | -64.24268 | 2025-08-28 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README73.md)
