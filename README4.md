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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1af313c6-24fd-3157-908b-61db5a2f769b | -14.14227 | -52.96722 | 2026-08-19 00:09:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| d40be6cd-196e-3b04-9a8b-ec78d159eb60 | -8.17817 | -44.4371 | 2026-08-19 00:09:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 742beeeb-dfa0-3e9e-931e-461c4f87aed1 | -8.1004 | -51.65514 | 2026-08-19 00:09:00 | TERRA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| a95ccc98-02f9-3920-a962-b8b661ba3c35 | -13.57251 | -51.68711 | 2026-08-19 00:09:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ac9d45c3-a8bb-32b5-b9a6-6b6f7f6c5987 | -9.01863 | -60.51962 | 2026-08-19 00:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| a5661bc0-fcf8-3ae5-803f-99b7a19c5d71 | -6.41757 | -54.93809 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 7b269f7e-9457-30a0-ab2f-a992476e8a06 | -13.27238 | -51.64432 | 2026-08-19 00:09:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 280351f9-96dc-3984-ba5e-96451df16dd4 | -6.86481 | -59.01738 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.5 |
| f3bfd83f-8b05-3838-9134-fbe3fa661600 | -5.66661 | -43.57228 | 2026-08-19 00:09:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| ce6ac61f-b98c-3242-868f-c7e0c0fc7519 | -9.46 | -51.62378 | 2026-08-19 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| d5ec29bb-9d1a-3198-b026-c1542663453c | -13.41358 | -54.38991 | 2026-08-19 00:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| c52362a0-995c-3127-a3a3-9a8c4b5a488c | -6.88826 | -56.43779 | 2026-08-19 00:09:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| fd6d83a2-1e18-33cd-90fe-5f08c04f5fef | -8.533 | -54.74742 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 0e05f685-78d6-3f78-979e-1f44b98c4b24 | -7.55786 | -55.56345 | 2026-08-19 00:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 2dc99d93-aece-30e5-89e8-916527882cc7 | -9.08122 | -50.80707 | 2026-08-19 00:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 17.8 |
| de121530-a8f3-38a2-ae1a-b050019e0531 | -11.19414 | -54.02038 | 2026-08-19 00:09:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| f029837b-4730-3fcc-8f8e-0c60b453c773 | -11.38303 | -46.39255 | 2026-08-19 00:09:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| e15fce00-be91-33ae-8780-5a976c738f18 | -5.90565 | -43.61904 | 2026-08-19 00:09:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 77.0 |
| d679bd97-77bb-31ed-8d7f-89901a917f35 | -6.83425 | -56.45093 | 2026-08-19 00:09:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 30c39436-d2fa-3ca9-9fc0-2b6e654bd98b | -6.40718 | -54.93945 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| cbaa07b8-f9ee-3ddc-bfc6-eb10585aab17 | -6.45158 | -52.74068 | 2026-08-19 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9761f19b-2140-38ff-a79b-2c7ceba4fd93 | -14.2056 | -52.90326 | 2026-08-19 00:09:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d6ca6806-dca7-369f-89d7-8889cd305066 | -6.74713 | -59.18003 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 22.2 |
| bd982ef4-97b9-33c8-9938-8e8bb4a9fdfa | -13.41415 | -54.38339 | 2026-08-19 00:09:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| f9607b76-5f91-35f0-ab3b-5c406cfa007f | -8.18768 | -55.0055 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 3fd385ca-c9c3-3fb9-af86-9ea9321ae7a2 | -6.89726 | -59.04076 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 6f76fc7e-0a2e-38da-886a-8d988817dc5b | -14.93526 | -49.0043 | 2026-08-19 00:09:00 | TERRA_M-M | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 13.0 |
| ecdaa69c-7d4a-32f7-8d3d-c599a7942c96 | -8.56983 | -54.7827 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| d62b9c24-6cfb-39a3-88c0-f7cc2d2ecbfb | -7.53749 | -55.58089 | 2026-08-19 00:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 141.5 |
| 4ab8bc6e-a566-3626-831b-ba824bd648f5 | -9.08759 | -50.78809 | 2026-08-19 00:09:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d0b47433-3260-3638-bec8-8dcadb824d43 | -13.40674 | -43.86741 | 2026-08-19 00:09:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b117f679-6229-3f9c-a7cd-30e54299b50b | -15.71379 | -47.80217 | 2026-08-19 00:09:00 | TERRA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 4995e078-9875-3dd7-83e2-cdd092ad8578 | -12.83329 | -48.42344 | 2026-08-19 00:09:00 | TERRA_M-M | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| a5c9f342-61b3-3bd9-baa9-30c41366ff8f | -6.88264 | -59.04239 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 39455f4c-605d-34f9-ab4d-4311af74c2f0 | -14.14069 | -52.95477 | 2026-08-19 00:09:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 050c8822-fcd4-31be-bc39-82b697b97966 | -8.5297 | -54.72123 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| db7b4e20-17eb-3c5c-aa16-9b1e685ba3ed | -6.33881 | -44.08715 | 2026-08-19 00:09:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 8e038286-5b53-3302-b575-465e0813baf1 | -5.91731 | -49.26581 | 2026-08-19 00:09:00 | TERRA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| ac3e1d32-f227-3645-a61b-bfd8a413a6ed | -8.55583 | -54.75759 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| b463d359-b605-3f73-b35f-40ad32f8a51c | -11.69721 | -54.5701 | 2026-08-19 00:09:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| f6b05845-0881-3307-9be7-0a206e4d6694 | -5.91572 | -43.62308 | 2026-08-19 00:09:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 366.0 |
| a334a518-eea5-34b8-a15b-439c91a3f5a4 | -8.53465 | -54.76046 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 4d7acd65-4dee-3e9e-b78e-aeec0be94c11 | -6.67202 | -56.15806 | 2026-08-19 00:09:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 63144e3f-f130-35d7-931d-4c0ca16c4ed9 | -9.41963 | -60.41262 | 2026-08-19 00:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 878bde7e-b999-3826-8ca7-e29449054e74 | -11.48666 | -45.1063 | 2026-08-19 00:09:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 66bf59e5-09b9-31e3-9573-d4726978061b | -6.68829 | -58.94369 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 32acdd25-15ff-36c8-8f07-2912c08d3354 | -8.22345 | -55.02913 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 508bff25-371b-3411-8f3b-74144b47b74d | -9.38577 | -60.57166 | 2026-08-19 00:09:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 71.9 |
| efe95f19-00f5-32d1-8e56-8eef47675218 | -8.55752 | -54.77085 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 44378830-57f2-3ded-a584-e1d23222971c | -7.05722 | -59.86548 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| a0aa1cd1-47b2-3ec6-b513-f68891557bf7 | -10.19325 | -54.25683 | 2026-08-19 00:09:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8e97fe7e-ae23-3e25-9965-3a8df308382f | -6.70601 | -58.96841 | 2026-08-19 00:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 202c6f7b-f4cd-3124-93e4-30fb46bce8ca | -8.5859 | -54.7404 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 365afd15-754e-3bea-91b8-22c7b50600d9 | -11.22048 | -55.07775 | 2026-08-19 00:09:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 31.5 |
| 8ec68442-a661-3efd-9f32-c262b8b21703 | -11.04038 | -51.05042 | 2026-08-19 00:09:00 | TERRA_M-M | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 18e45fc7-2b65-3e64-8be0-a1d99811115e | -5.74092 | -51.71028 | 2026-08-19 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 4cea4a5f-dd74-32c3-9b8c-c4cbee56dc1d | -9.45876 | -51.61458 | 2026-08-19 00:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| e1a46d43-4b63-3295-a0f0-dd7733591b02 | -10.11573 | -54.28527 | 2026-08-19 00:09:00 | TERRA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| e55fa13e-bf3f-33f8-b892-ab536c7a7396 | -10.51812 | -50.79599 | 2026-08-19 00:09:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| cada0c87-4dd7-3627-af8b-f6aa27ae9a1f | -5.42914 | -48.41345 | 2026-08-19 00:09:00 | TERRA_M-M | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 6df017bc-ff16-3358-b9a1-2b9f9d90e048 | -7.41283 | -49.60972 | 2026-08-19 00:09:00 | TERRA_M-M | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a4f6ed0f-2d3a-3c5e-a1f8-0c72b0bcb13e | -8.55082 | -54.71846 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 381441e5-da40-3c24-8dee-e4b776764aea | -6.40886 | -54.95204 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 55eef88e-a6f9-3942-aac2-723681b2487f | -8.57701 | -54.75484 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 106.6 |
| bb598f2f-6f2f-3c8f-ba35-20416d02b426 | -8.17767 | -44.44355 | 2026-08-19 00:09:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| ebe6ce6f-f043-3273-a2b2-2d38ed4794e4 | -11.21743 | -55.0568 | 2026-08-19 00:09:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 5a7d912a-339a-31bf-9e96-34bb047c49e8 | -7.53932 | -55.59541 | 2026-08-19 00:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 418ee1ce-903b-369e-bee3-2eabab1aaf88 | -14.20714 | -52.91558 | 2026-08-19 00:09:00 | TERRA_M-M | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f5f9370b-99a0-3026-b344-cab921213a5a | -14.45502 | -45.63812 | 2026-08-19 00:09:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 24.8 |
| ceb5297a-caa5-3015-8b31-ef22abff08bb | -8.56305 | -54.73008 | 2026-08-19 00:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 7f4ee931-eba6-3e73-959e-8fe939bfdf26 | -12.47592 | -54.18806 | 2026-08-19 00:09:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 732f3fdd-6187-3b15-976c-b3bbbd178944 | -14.46331 | -45.62373 | 2026-08-19 00:09:00 | TERRA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 31.2 |
| c6097003-b136-327a-9264-fa1305cb19e1 | -6.6938 | -58.942 | 2026-08-19 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 144.1 |
| 785c55f6-aaba-3920-a15f-6dd1892c1b75 | -5.9995 | -57.8444 | 2026-08-19 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| c58100a1-2ccf-3db0-bedd-7520289a8603 | -19.7639 | -57.9607 | 2026-08-19 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 95.0 |
| 5a05cf25-7ba7-3c0c-a695-cee13ebeef64 | -9.3873 | -60.5721 | 2026-08-19 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 93.1 |
| ec8d692c-bb80-3f41-a01e-80a5a642eccc | -6.0179 | -57.8437 | 2026-08-19 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| e9526326-137a-3834-b5f9-4a77252517cb | -7.5488 | -55.5629 | 2026-08-19 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 93d27f01-85b3-39d5-a5a5-362bd19f3515 | -19.7643 | -57.9399 | 2026-08-19 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 100.7 |
| 5cd407d8-d2ad-3f7a-ae97-03a52e81fbc2 | -6.8961 | -59.0496 | 2026-08-19 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| a375e4a0-d522-3c72-ad30-98a3bddd8937 | -6.0912 | -57.9187 | 2026-08-19 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 122.6 |
| 9cfe51c5-c25b-34b7-af17-ff762662c5ab | -9.4254 | -60.4545 | 2026-08-19 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| b838ccc8-2bcc-394d-b4b8-ed8bf5ee6f0f | -6.8593 | -59.0318 | 2026-08-19 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 2f907664-d70f-39dd-9af5-ba3bc6ff5b03 | -5.92 | -43.6032 | 2026-08-19 00:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 51a16ef3-9319-38ab-bd37-a49b04479bfc | -9.406 | -60.5711 | 2026-08-19 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 131.2 |
| 47398ec0-50ff-37d1-acd1-c5496ae022f9 | -6.3496 | -54.9068 | 2026-08-19 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| c1bd027e-0caa-30e5-9c4f-d285afbf5472 | -8.5792 | -54.6758 | 2026-08-19 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 08e9814c-9220-35c3-bf84-73bb7932be7f | -5.9994 | -57.8639 | 2026-08-19 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 175.3 |
| 3d4ea1c3-0f21-3285-b8f2-05a10d2b5606 | -5.9198 | -43.6264 | 2026-08-19 00:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 189.7 |
| f73c80fb-1d8b-3c1a-9f3f-427c8be831ff | -6.6937 | -58.9613 | 2026-08-19 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 0af641d4-19b2-333b-ba6e-a62ef1b90274 | -6.8962 | -59.0303 | 2026-08-19 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 3ddcdb5d-4853-301a-9f9a-88f989354b36 | -19.7438 | -57.9633 | 2026-08-19 00:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 159.7 |
| 85878cbb-a08a-3c27-b9cc-14d4d38966f1 | -6.8777 | -59.0504 | 2026-08-19 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 31bee762-a115-33f4-8d02-897e4796b51b | -6.0728 | -57.9194 | 2026-08-19 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 44.6 |
| cff94917-bd31-3147-8678-c5811099c741 | -7.0576 | -59.8523 | 2026-08-19 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 119d8b3c-a386-3085-8bf8-9fcc1e8117a8 | -9.4069 | -60.4362 | 2026-08-19 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 676325a2-8c28-37a1-b728-63b030f03949 | -6.8594 | -59.0125 | 2026-08-19 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 04f98a52-c85e-37ba-92bd-3a01f1c1b225 | -9.4061 | -60.5518 | 2026-08-19 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 30e7554d-92d5-39b5-9f5f-aecf9ac0ba82 | -6.7123 | -58.9412 | 2026-08-19 00:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 116.5 |
| 807d3ffb-b05f-345b-9841-572970f67afa | -9.4257 | -60.416 | 2026-08-19 00:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |


[Clique aqui para ver as próximas entradas](README5.md)
