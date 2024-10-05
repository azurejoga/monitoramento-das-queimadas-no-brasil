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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5655e9c6-fb37-3795-b7ba-3108e5fa6bc0 | -2.20262 | -48.15944 | 2024-10-05 04:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 828ae02a-97bb-3632-90e2-2425305047e8 | -2.13723 | -50.99214 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb4ab9bb-f65c-3f68-8f81-1f07adb87a30 | -2.13539 | -50.99145 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54db605b-a4c9-39b5-bc12-6949a1af2e4b | -2.13485 | -50.99463 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e76898f8-b604-3190-9d30-4fc701699802 | -2.1314 | -50.99459 | 2024-10-05 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2b56ad0-a9ff-3aa8-b91e-7889226c04a6 | -2.02286 | -47.99321 | 2024-10-05 04:12:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4263d10-6294-335b-a919-a84c8e8bed20 | -2.01854 | -47.99253 | 2024-10-05 04:12:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e324c96f-5540-38d1-a2ee-6935e4ff981b | -2.0099 | -47.99116 | 2024-10-05 04:12:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a02e338-6305-3e89-9462-79fc1f43e3d8 | -9.25665 | -43.51587 | 2024-10-05 04:14:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1e3ac42a-869a-3e67-863d-9e79d6de0dd0 | -7.74647 | -43.07252 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 89f3a268-28c4-3464-af52-ac0fc8037295 | -7.74626 | -43.05839 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 231362c8-4905-3433-bf6e-a85059750910 | -7.74592 | -43.07599 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 3ea70df4-2bc5-3152-ae25-de4aa627b5a4 | -7.74572 | -43.06187 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6f6e6d36-03e8-37ff-9dbf-9d6b52772b20 | -7.74517 | -43.06535 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c7d52023-2f56-37cd-a08e-d379385e7643 | -7.74463 | -43.06883 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 0176e448-ec12-3238-a5d1-cdd3ded33ff7 | -9.19108 | -45.56397 | 2024-10-05 04:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d81288b-fca6-3544-868d-3303e98909cf | -9.18098 | -45.56677 | 2024-10-05 04:14:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 262740ab-a0d3-3eff-96b3-2ca6b052b99d | -8.99464 | -45.20536 | 2024-10-05 04:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55586876-1aef-3190-8e24-eb40a6be6834 | -8.89829 | -44.91681 | 2024-10-05 04:14:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0b3d823-6a5f-3973-997e-92d3c0c9fe1c | -8.86668 | -45.17694 | 2024-10-05 04:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad611bbd-8682-3157-8c9c-e0e634061dd2 | -8.83505 | -45.15672 | 2024-10-05 04:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f762ca2d-6c97-383b-a39b-f003707dd01e | -8.77771 | -44.81934 | 2024-10-05 04:14:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9e0187cd-8855-356b-950c-f88b28f6b3d5 | -8.77712 | -44.82295 | 2024-10-05 04:14:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 37.0 |
| d51d872c-cbdd-3294-98ef-716119b23f68 | -8.77654 | -44.82656 | 2024-10-05 04:14:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 37.0 |
| eea7b3d7-a5d0-3c4f-a714-a623a9ea9ffb | -8.77492 | -44.81518 | 2024-10-05 04:14:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 67841866-e64f-317e-a5e7-f53fac4325a0 | -8.77434 | -44.81879 | 2024-10-05 04:14:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0262d151-98c8-3660-bab6-9070f5d50261 | -8.76818 | -44.81408 | 2024-10-05 04:14:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 2fe34f60-0322-377f-8176-81b98397c723 | -8.76759 | -44.81769 | 2024-10-05 04:14:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 476cc1c7-7e20-3eea-a6f2-0978b41eb3dd | -8.7673 | -44.81435 | 2024-10-05 04:14:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 077cd5d8-33b4-3a49-8818-eda8a3952eef | -8.76701 | -44.8213 | 2024-10-05 04:14:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 53c12fae-c99f-3da5-a133-931cdd491120 | -8.76673 | -44.81796 | 2024-10-05 04:14:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 94e22823-e4ac-3907-a2b8-3be8a4a5f02d | -8.76642 | -44.82491 | 2024-10-05 04:14:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 033457c3-288c-33fa-b5ad-2f78ee495035 | -8.76615 | -44.82158 | 2024-10-05 04:14:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 61663e0d-e9e3-3be0-9815-980c907408b3 | -8.76584 | -44.82853 | 2024-10-05 04:14:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 15.7 |
| a3152882-1daf-3d69-b211-0f0ab430e037 | -8.76558 | -44.82519 | 2024-10-05 04:14:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 508022fc-1c98-3878-962e-30e0c0ff01d6 | -8.765 | -44.82882 | 2024-10-05 04:14:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 9edc484b-3605-30cb-831b-bf46d328c53a | -8.76335 | -44.81741 | 2024-10-05 04:14:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e7a2733f-e862-397d-aee4-22509c7a65f6 | -8.76278 | -44.82103 | 2024-10-05 04:14:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 19.3 |
| fc8d3b86-c7f9-361c-b836-d8d2a5ea7eec | -8.7622 | -44.82465 | 2024-10-05 04:14:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 9a2f193f-c100-323f-a94d-04e09a8b4828 | -8.75883 | -44.82409 | 2024-10-05 04:14:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 159c96dc-ebe1-30cf-94d3-b2e6868fd522 | -8.30161 | -45.43049 | 2024-10-05 04:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca7946b6-354e-3f13-86fc-c95a30a55c7e | -8.15844 | -44.40857 | 2024-10-05 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0d4eb0af-c3ca-3cb7-99d1-98cdbce7962d | -8.15509 | -44.40802 | 2024-10-05 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c44bda2-901f-33c7-a4f9-aa1eff876a5d | -9.95249 | -44.08184 | 2024-10-05 04:14:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 33a42af9-e466-3063-b68f-e02db7bb72d2 | -13.53279 | -48.60466 | 2024-10-05 04:14:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e6ef2317-9da4-39ba-a7be-5b580c5d8e99 | -13.52825 | -48.6085 | 2024-10-05 04:14:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f18d3667-c866-38bf-b53b-0adcf1f919f1 | -13.52667 | -48.61773 | 2024-10-05 04:14:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0a17977e-ae1f-3c30-851b-4c89eedc8b8b | -13.32988 | -49.31645 | 2024-10-05 04:14:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 03e1fdcd-e99b-31ce-b395-ceb487ae5ddd | -13.30475 | -49.32076 | 2024-10-05 04:14:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0207b46a-2eb7-39df-bc88-76b746296e22 | -13.2168 | -48.66013 | 2024-10-05 04:14:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 152c17d1-e8db-3995-9775-c9de89e6d205 | -13.2097 | -48.52449 | 2024-10-05 04:14:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 470289b8-a430-3acb-979a-a3cd9e8a74bd | -13.18988 | -48.66264 | 2024-10-05 04:14:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c4f86a95-5a02-37de-9b2d-967d7ea86504 | -13.18909 | -48.66725 | 2024-10-05 04:14:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bf804f74-efac-3478-8692-151d4051f198 | -13.18294 | -48.61218 | 2024-10-05 04:14:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f7d020d-9e02-390e-bf9e-62e68994e8ee | -13.16604 | -48.6873 | 2024-10-05 04:14:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d1fe7935-c648-3614-88a1-471b44ef1e17 | -14.4839 | -44.96297 | 2024-10-05 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 302b160f-cfed-33ac-9cb7-03235178ae84 | -14.48124 | -44.96276 | 2024-10-05 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6f4aae12-464e-3b0a-b172-3d5bd0ee601f | -14.47791 | -44.96221 | 2024-10-05 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d1cb9377-6135-39c8-abb3-413aa0273169 | -14.47459 | -44.96165 | 2024-10-05 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ea836331-40e1-3440-ab68-aab1f26c8929 | -14.32528 | -44.70343 | 2024-10-05 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fbc5821b-d503-3348-be11-585c86b76dd0 | -14.32473 | -44.70699 | 2024-10-05 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8be2b6de-2ac4-3725-8da4-6d3f4d5b138e | -14.07048 | -43.95479 | 2024-10-05 04:14:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 437626cd-6f58-3a31-b53c-74556463f3fa | -14.06057 | -45.13816 | 2024-10-05 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04c90b4f-f2b3-34f1-8cd3-b82ceda17bc9 | -14.06 | -45.14173 | 2024-10-05 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2345724-7706-3a9a-af1d-3e7533b52bea | -14.05781 | -45.13405 | 2024-10-05 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22504a2f-ff5e-3075-85d7-23265b15abcf | -14.04945 | -45.14362 | 2024-10-05 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 707927af-c446-3a4a-99a8-bb0ac8a7b4f0 | -14.04889 | -45.14719 | 2024-10-05 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 38193d95-fb0a-3db2-bcb7-5674a46d4811 | -14.20863 | -46.46735 | 2024-10-05 04:14:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 06d18f96-e3eb-3612-86ef-e573131f989f | -14.20522 | -46.46677 | 2024-10-05 04:14:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2b22b3f9-1272-30c7-a6d9-2d8ccc6d1afb | -14.20399 | -46.47429 | 2024-10-05 04:14:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a180b2d9-2e11-382c-b07a-8d2eca111305 | -14.20338 | -46.47801 | 2024-10-05 04:14:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f980e67a-19da-3014-8fd2-6240e6f49528 | -14.20306 | -46.45861 | 2024-10-05 04:14:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4936271d-6622-3ef7-ba9b-8d458754419b | -14.20277 | -46.48174 | 2024-10-05 04:14:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13b5809b-65d7-3fe8-9675-c8184453d690 | -14.20244 | -46.46238 | 2024-10-05 04:14:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ab35b46-999c-3e60-ad12-2c45888de39f | -14.20058 | -46.4737 | 2024-10-05 04:14:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f370bfa4-7cfa-3b77-8890-13486bff1cfc | -13.10688 | -46.36441 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6b6acef2-8c37-3391-b3b9-6e1b46f68a96 | -13.10626 | -46.36819 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fd0b464a-2c91-3ece-9dd4-352cabe9ed44 | -13.10597 | -46.34861 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b95401ec-3032-35bf-862e-30cd449b8657 | -13.10563 | -46.37196 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6682b106-be98-3ed1-bf84-bd38099f8355 | -13.10533 | -46.35245 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3c8dde2d-281a-37a9-9e16-dfc34b93bacf | -13.1047 | -46.35626 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 175f7400-5a24-3cb5-aaef-74c61eaba102 | -13.10408 | -46.36005 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ed94ea6f-163b-3369-b25d-c1c25db59e1f | -13.10382 | -46.34031 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3096dcc0-3115-3388-ae6d-e62cea081a27 | -10.7596 | -46.18709 | 2024-10-05 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7fa2efe1-e1f5-36ed-b4f2-bb594deae1f0 | -10.75613 | -46.18652 | 2024-10-05 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cddfc5f8-1b41-3454-9372-1c14900f5f55 | -10.7555 | -46.19035 | 2024-10-05 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5630183-7e8b-3220-9469-3a87b0dfeba3 | -13.72891 | -48.15559 | 2024-10-05 04:14:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 96c586ae-fb2c-39fd-8f44-e3ba35f99fc1 | -13.60615 | -48.13002 | 2024-10-05 04:14:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7bf31b7c-1239-3252-94b9-abf397aec0c9 | -13.60106 | -48.13772 | 2024-10-05 04:14:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5934d95a-abc8-319e-a983-73f544e3a7a9 | -13.59739 | -48.13705 | 2024-10-05 04:14:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d3ad830a-1565-3380-87c8-c1d3f448d934 | -13.5966 | -48.14172 | 2024-10-05 04:14:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7b57d839-58b9-39e8-bbdd-01b4d8908886 | -13.59371 | -48.1365 | 2024-10-05 04:14:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 0c35ae17-66d0-3837-9181-acf9e13f27f1 | -13.59293 | -48.14109 | 2024-10-05 04:14:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4a374974-3293-30f6-bdc5-9ce76e1c3394 | -13.59292 | -48.11903 | 2024-10-05 04:14:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 22d9aaa2-7cdf-31a6-855d-7acc6cf4b0ea | -13.59074 | -48.13178 | 2024-10-05 04:14:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5d4cfb09-67c2-36ab-925e-f06fa2b260f9 | -13.52903 | -48.60394 | 2024-10-05 04:14:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96376d56-d0e5-3209-9289-3dbb277c1e9a | -13.52526 | -48.60332 | 2024-10-05 04:14:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 68086148-fcbe-3971-97a0-0a9b40bdbc55 | -13.52288 | -48.61716 | 2024-10-05 04:14:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 303226a3-cf7d-33a0-bbf7-366bfeb529d8 | -13.50826 | -48.63437 | 2024-10-05 04:14:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b57ccc61-235b-3847-a772-1bfd1057f078 | -13.39669 | -48.08792 | 2024-10-05 04:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README62.md)
