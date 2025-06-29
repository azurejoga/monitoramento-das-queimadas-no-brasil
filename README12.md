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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0ff945f-219b-3e98-9051-f8123ebdfa8c | -11.55734 | -52.80151 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3e7b049c-5169-39ca-be87-526754a1d834 | -7.55299 | -45.84832 | 2025-06-29 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c022ec6-1c1f-3cfd-a920-034f4028062c | -10.92931 | -44.15851 | 2025-06-29 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e64dd11e-98a1-3471-9122-00f5b1e43fd8 | -11.2753 | -52.73894 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 24018750-e859-3c78-a5a7-f41252b6c192 | -11.01646 | -56.23244 | 2025-06-29 04:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ec0e37f-9d3a-3441-83e3-9be784749ebb | -12.12998 | -45.575 | 2025-06-29 04:10:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7993624-1dbd-365c-b956-5d6002908f2f | -7.49347 | -45.45724 | 2025-06-29 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a083652-560b-34c5-84e9-e9983de94f7b | -13.6906 | -47.13091 | 2025-06-29 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0317ff3-5b9d-3d0b-b494-ebdf55a5a648 | -12.10995 | -54.57563 | 2025-06-29 04:10:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0c8987a-0f2b-31b5-b5ce-e70fa9849277 | -11.54689 | -52.79544 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 732e6c79-9f29-383e-b783-58ac3c1015a0 | -10.87519 | -53.74582 | 2025-06-29 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d7908de5-c304-3e86-a11b-445846a62dbb | -11.26681 | -52.75296 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2f6a1e6e-8ac0-33f1-86ff-161fa5dfae79 | -10.94535 | -45.59936 | 2025-06-29 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1007423a-fca5-3510-a992-f2dc3d3ffe84 | -10.85453 | -53.75534 | 2025-06-29 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b08b25c-4c11-3925-9ce5-5016a9d546b3 | -7.1908 | -43.44322 | 2025-06-29 04:10:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 35ddd61a-05eb-336c-86c6-20a79e214be2 | -11.03491 | -55.37461 | 2025-06-29 04:10:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1f321c4-9d08-3ad2-a8aa-4d675c727e6e | -8.68991 | -47.50622 | 2025-06-29 04:10:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5e86c89-16f8-35ca-88fc-9d0356902b62 | -10.56984 | -52.03381 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3fa5a289-d772-3cc5-8c5b-d0447bb83d1d | -10.56443 | -52.0327 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5ecaf6f-093a-3363-8c12-00a4c620c8f9 | -10.97563 | -45.10841 | 2025-06-29 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 0e5decb2-caf3-35ab-9d76-5ef7dce04d82 | -7.19076 | -43.70261 | 2025-06-29 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| abb7e1d3-b85a-3b6d-8d7c-032b53dbd083 | -12.11034 | -54.58533 | 2025-06-29 04:10:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| eec84a15-b5e0-3121-8933-ae75ba523eb5 | -10.56495 | -52.03598 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c2bde0e5-a139-361d-bf7c-a6a132df9af4 | -10.56658 | -52.05145 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d5683471-eba9-3382-bdd9-76ab9d9ea2e8 | -12.05002 | -48.07858 | 2025-06-29 04:10:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a08a5a7c-2948-3b8e-b602-57f99277176b | -9.79269 | -48.56056 | 2025-06-29 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d68170eb-467d-3cc1-929d-a01f9b16821b | -9.27341 | -40.44521 | 2025-06-29 04:10:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d9d8273c-afb7-3061-9416-aab04a3ef294 | -7.05861 | -41.44118 | 2025-06-29 04:10:00 | NPP-375D | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5983c9dd-1dc8-379f-91c4-7fa23ba09349 | -11.54764 | -52.79159 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f01b3508-ce6a-39c4-b5f8-c78753f3a94f | -7.55223 | -45.82908 | 2025-06-29 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d08c178-e6f5-3d90-8463-0ba0368bb766 | -6.62543 | -47.28497 | 2025-06-29 04:10:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 3c57fb52-cbb2-37bb-819a-b9bc4112807e | -11.02556 | -56.28631 | 2025-06-29 04:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 17a355f0-3a6a-3ef9-9426-35d3b217fff7 | -11.55323 | -52.79271 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 159f103f-75d3-37f8-8892-6c4e60ee1b42 | -7.5445 | -46.29208 | 2025-06-29 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 39b04d13-2281-3335-b6c4-62b3a35e2369 | -7.55756 | -45.84422 | 2025-06-29 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 58c6e360-61b7-3a37-9f3b-34607bc1c672 | -10.65135 | -44.49148 | 2025-06-29 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0bd5c778-a302-36a5-9613-69b1d9acdab3 | -7.12663 | -45.52605 | 2025-06-29 04:10:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 689e2d53-22fe-33e3-b7d9-0c7b7a499e7b | -7.17559 | -43.66566 | 2025-06-29 04:10:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e83083a6-ee48-3817-bcb5-8b683212aa43 | -9.98351 | -47.80333 | 2025-06-29 04:10:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84128462-1b38-3f6e-a8e0-fa5f4a0d2382 | -10.55031 | -52.04819 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ede16e51-2a08-3376-9e33-ed0415adc88f | -11.53791 | -52.78186 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| b36ff322-17b9-39a0-9650-732b8acb7777 | -7.21242 | -44.89251 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59a1f13f-76e5-318f-9e43-aac2f84f9e2b | -10.95712 | -48.15377 | 2025-06-29 04:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa036767-8f64-3893-867a-8a6c26da9c0e | -9.6443 | -48.79358 | 2025-06-29 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 831742a6-6554-3c23-9825-3f0af6ea1cd2 | -6.67555 | -44.2498 | 2025-06-29 04:10:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 87d76db7-0437-3527-8861-5104595729d7 | -6.89629 | -43.9832 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b7db11e0-77db-356a-aefc-598e23c939b8 | -10.86919 | -53.74458 | 2025-06-29 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 085fb4ca-7718-3ab9-9992-a59b5aecfdf5 | -9.98004 | -47.79875 | 2025-06-29 04:10:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fef75ad5-2f6c-3942-9d66-07915d5c0909 | -7.49047 | -45.45224 | 2025-06-29 04:10:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e10dfdd6-85f3-3287-82bf-b3b875f7f661 | -10.92591 | -44.15794 | 2025-06-29 04:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dfd9e0db-92d0-3e6b-8cd7-61efddd345fd | -10.56855 | -52.0408 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40a2e0c8-e20b-3ab2-a5bb-b64a71cdbe7a | -12.05715 | -48.46906 | 2025-06-29 04:10:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd54df70-33de-345c-bb5a-c3a1428d4dee | -10.56291 | -52.04656 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 43c1cf43-7301-3ef8-960f-c0f392943049 | -11.82219 | -47.51173 | 2025-06-29 04:10:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b28d32e-b3c3-31f9-afec-03253f563528 | -10.96127 | -48.15458 | 2025-06-29 04:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18fe8030-766e-3221-b447-73b312daa695 | -10.56049 | -52.05394 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1f2e2d5c-578e-333b-8d9e-7cf5c222afba | -7.40064 | -44.56403 | 2025-06-29 04:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9eb46852-35be-3454-934f-9df38ab4cc04 | -10.62468 | -48.69744 | 2025-06-29 04:10:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6fd917e8-c309-354d-922b-b3493245b9b6 | -11.27458 | -52.74271 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| afdf66ac-6f5e-3485-b6ce-75241645b934 | -11.55618 | -52.77746 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| b675a0ce-997a-381e-92fd-dfd45813415e | -7.18955 | -43.71009 | 2025-06-29 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a07345ca-2b7a-3fa1-a967-4edd6a1e4ed8 | -11.54574 | -52.77148 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 58dc3b5e-c15b-3680-924e-c48927ea1432 | -10.83297 | -53.76219 | 2025-06-29 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 825e3dfd-0750-35f7-875a-56708e763a36 | -10.87248 | -53.7518 | 2025-06-29 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a76c7727-02b4-3280-9c12-6173e4255e76 | -7.19299 | -43.71065 | 2025-06-29 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 497b7dfd-7050-33ea-8637-1ab52ca41682 | -7.21835 | -43.07823 | 2025-06-29 04:10:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| ee819b9c-e8a0-311f-b035-fdff9463b102 | -11.53716 | -52.78572 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 68dcb252-3c34-3683-b7dd-541cf5f5df8d | -13.69362 | -47.13586 | 2025-06-29 04:10:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5e35e1b1-7175-3979-8a99-92c09bd7d740 | -11.55026 | -52.80809 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5b79c632-dabc-3f33-9e69-9b72ae547973 | -11.5506 | -52.77634 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| c3027d64-ca5d-34ba-b994-67d4a3085474 | -9.97938 | -47.80252 | 2025-06-29 04:10:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4985cf0e-b33f-304e-8679-a8548938c561 | -11.83972 | -43.804 | 2025-06-29 04:10:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d0def034-067f-3e67-81bb-41d746be5f5b | -10.56182 | -52.04681 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d9d9bbb4-21e0-33e9-9f66-756d3507adb4 | -9.79149 | -48.567 | 2025-06-29 04:10:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 67b422f2-e900-36a3-ac21-e6ffd3613470 | -11.00947 | -56.23126 | 2025-06-29 04:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b28b544b-265b-3c1b-a00d-4b30337700fb | -11.25707 | -52.74299 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b43d7acb-d7b4-388b-9389-cf18831325e3 | -7.54789 | -45.84978 | 2025-06-29 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 297eebe2-49be-3b85-a85b-276d7037f5d3 | -7.26271 | -43.12928 | 2025-06-29 04:10:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a175ff05-9dfe-3ebc-b364-04062adf4bcf | -9.15739 | -40.99398 | 2025-06-29 04:10:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7cbb121a-b9d7-31c4-afdc-a90c0e306dc1 | -7.19238 | -43.7144 | 2025-06-29 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49ee7ae4-bff8-3702-a6f8-bba31e9747f1 | -7.17964 | -43.66246 | 2025-06-29 04:10:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d5c45a7-982e-3685-8eac-721343c1f81e | -12.06482 | -48.47445 | 2025-06-29 04:10:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 678b3a83-05f1-38aa-9a5e-1a3585e8e325 | -10.83987 | -53.75888 | 2025-06-29 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e1d6a8e-6647-3689-9d5a-a84ec7b51d36 | -11.27143 | -52.74538 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 015f1839-bf65-3648-a613-676a4dda630c | -7.18894 | -43.71384 | 2025-06-29 04:10:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f49884a1-b224-375b-a435-450ae33431e4 | -10.56313 | -52.03971 | 2025-06-29 04:10:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58f5ed7a-60ad-39d7-972d-5d5a1905055b | -7.18919 | -43.56066 | 2025-06-29 04:10:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 767504d9-951a-34ba-aba5-4b4b972633ae | -11.03251 | -56.28775 | 2025-06-29 04:10:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 041e0576-2402-35f9-88db-0588f688a99e | -10.97145 | -45.11181 | 2025-06-29 04:10:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 15.3 |
| a9b51534-d54e-33cc-80c8-17a3177030f9 | -11.59074 | -44.66503 | 2025-06-29 04:10:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 019e8bc3-c12b-349e-bffb-ee9e471b00f6 | -7.10363 | -44.37011 | 2025-06-29 04:10:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 62325611-8898-3d9e-a1f1-ef2f94254be2 | -9.71037 | -56.18687 | 2025-06-29 04:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 9f1fbba9-a453-347b-bfb9-a82ab3377bca | -11.49584 | -48.07746 | 2025-06-29 04:10:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 52e7988b-2418-3185-8671-24080eb2a0fd | -9.4345 | -47.95053 | 2025-06-29 04:10:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d31607ee-d2b0-387d-840f-7ed9cb9f09c5 | -9.71564 | -56.18055 | 2025-06-29 04:10:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 764c0832-ba77-36de-87a1-0c56fd699928 | -11.54014 | -52.7704 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 325de7e8-d207-3ff6-bf87-497dd05f6225 | -11.26828 | -52.74525 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b23fd9ab-9d07-396e-97c8-08763c19c542 | -11.5622 | -52.80649 | 2025-06-29 04:10:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4afa78fb-6187-3ca4-81cb-fa6920a8661f | -10.83475 | -53.75311 | 2025-06-29 04:10:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc6e876a-01da-30db-9dcf-d280886e0af6 | -7.55028 | -45.83577 | 2025-06-29 04:10:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README13.md)
