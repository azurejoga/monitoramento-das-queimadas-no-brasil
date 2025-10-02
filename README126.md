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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e7d4e4d-0d7b-3da1-8272-c0486967c9a2 | -13.47031 | -47.25426 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd76b54c-6b22-305d-b3e4-aa5990b08534 | -11.45941 | -51.50929 | 2025-10-02 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e4d947f2-c849-3c16-86e6-ae2ce163f20a | -10.94543 | -48.56255 | 2025-10-02 04:51:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 11137763-94f5-3d11-a4ee-6f72ca63ce78 | -15.35181 | -47.0887 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ca41a48a-0000-3dd7-9344-32f61ac53e6d | -11.15291 | -54.12679 | 2025-10-02 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e715ae24-3977-3a95-9a6b-74df34af01f5 | -13.96112 | -48.1274 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7036083a-1659-3b56-8d33-e9a4f939edcd | -11.17237 | -47.26295 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5ba1d695-9233-3764-9e59-b0cbc789da14 | -13.74769 | -48.01369 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5f35dfc6-5186-3f6b-a7a4-ba2d803df574 | -13.86329 | -51.24435 | 2025-10-02 04:51:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5410905-1c31-3358-97d2-dca6219dc589 | -14.43654 | -46.35283 | 2025-10-02 04:51:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9f27c6e2-fbe6-326e-91d5-6b641cdb6ed6 | -10.8172 | -46.59224 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f6a5334-5967-350a-a8f7-dcf5f5abfb48 | -10.8394 | -45.38547 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c93b7508-8926-3c83-8e61-96c0f88a0f7d | -11.00459 | -46.55509 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a7daa1d1-8afb-3215-8f1f-09b0ae8f3ec7 | -9.93011 | -43.74774 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 30.0 |
| c96f6e54-a2cc-3da2-8cb6-56d21570f2e0 | -15.93689 | -43.33868 | 2025-10-02 04:51:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a5a9f0df-6b94-32f7-8f3c-fce6101088e5 | -13.42151 | -47.79638 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 3ba56c6d-d974-3486-9236-6627b52226bd | -9.93366 | -43.63107 | 2025-10-02 04:51:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c50ddca-7b89-3f75-bdd4-e2ebf358758b | -13.79372 | -47.99854 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a3f38594-c1e7-3ec7-b58d-5234534860cb | -15.22567 | -50.11272 | 2025-10-02 04:51:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2b174c3d-b9bc-35c1-9cc2-2ab1fbf20263 | -13.4221 | -47.792 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 3e2bc80b-49ff-3b7a-aa62-ffd649e2df17 | -12.70617 | -48.57439 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 12cf9aef-6456-3a91-ab46-5190268228e1 | -12.65563 | -46.95279 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 327ab8b1-643b-3342-8f51-cf6cce9c212e | -10.2434 | -50.3116 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 108431ad-7f56-3476-9679-4bc182a78752 | -9.94052 | -43.70964 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5490e48a-fb57-3b12-a46f-61740001c0c9 | -11.81331 | -45.01994 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e586969-5c8f-3998-9bc5-4031e4f1b591 | -11.86779 | -45.00431 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0311dc31-0bcb-3520-bf53-662f9ebe7f60 | -10.84993 | -46.59344 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d24bd176-29ae-3427-afd0-321fdcc1f6ec | -12.6785 | -48.57101 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0fe0ed9e-4c7d-39fa-a703-77cb7afeb12e | -12.86288 | -47.0093 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b730b1c5-0f82-3a3a-ab91-537ec2365f58 | -12.49951 | -50.24442 | 2025-10-02 04:51:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90f427a6-f167-33df-bb2c-5e4cd242832e | -12.85933 | -47.0364 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 60c8c58a-608f-3e40-a4b7-49c34c11cdbc | -15.26237 | -49.28416 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a959d7f-ec16-35d8-a6d7-a3497bc58438 | -13.74966 | -47.99846 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 895065ef-70ca-3046-a385-e3b5270ec3e7 | -11.18343 | -47.82127 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 51194edd-cc99-3a33-96ec-f1816bb027fe | -12.81075 | -46.90682 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 54758c11-bbfc-3aac-bc61-f992f2520202 | -10.70623 | -48.58304 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 24.9 |
| c05ecae6-2e5a-34d1-893e-e0f207d9dcb5 | -10.42607 | -48.30305 | 2025-10-02 04:51:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de46ff04-bf71-3aa5-8839-0d58a05e4bec | -15.59836 | -46.90836 | 2025-10-02 04:51:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4e8795cf-b180-3da6-bfd3-cdcb0733892c | -11.83523 | -45.01248 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 003184e0-67b6-3ffb-9c5e-80bc85162b8e | -9.81037 | -48.28072 | 2025-10-02 04:51:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fddd9a89-c1a1-31e0-997f-47f1ff98a9b5 | -15.14427 | -48.38876 | 2025-10-02 04:51:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbdef24e-fc10-3179-a2fe-eae46077a90c | -11.17338 | -47.28874 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ea3eaecb-0299-3e83-97fc-b509f0a7bb94 | -11.08938 | -47.84869 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 58d18a61-bdd4-3b47-8352-de745e2bbd64 | -15.69892 | -46.26139 | 2025-10-02 04:51:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 53e2f98b-9510-3a41-aaf7-f5365cc6207b | -14.57701 | -48.31741 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 392c8519-f0bf-3160-89fa-c60bc2d386ef | -11.47403 | -45.0021 | 2025-10-02 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fdb8777-60f1-3b84-9b64-5106701c5b57 | -10.18248 | -50.23952 | 2025-10-02 04:51:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b5489181-9fb7-3502-8780-36c9a8cead82 | -11.1496 | -54.12624 | 2025-10-02 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ca8fca0-0e36-3956-bda6-fc88d0f2de55 | -9.84421 | -49.95597 | 2025-10-02 04:51:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a104f49a-d823-38c2-a1ef-783c662ee025 | -15.50584 | -45.91002 | 2025-10-02 04:51:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7f33f527-cb4a-353b-8ea7-935c89eaf788 | -14.58555 | -48.31884 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9d21198-53e7-3796-9d51-2d0c6ef55eae | -15.50766 | -45.91205 | 2025-10-02 04:51:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 302d1bae-bdf7-36ee-be65-2229a9bc22c4 | -14.89609 | -48.09184 | 2025-10-02 04:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dc373278-10da-3786-8693-6abe919c1445 | -11.17563 | -47.27192 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| a55bd26b-3f1c-3e92-8bc1-4f64abc7a3fa | -12.18836 | -47.90522 | 2025-10-02 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c3053a4d-7684-34ff-a4f9-6b39ff93f2d1 | -14.90037 | -48.09312 | 2025-10-02 04:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 670477e5-5f9a-36f1-a331-52429411568e | -15.55181 | -48.17896 | 2025-10-02 04:51:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2a52228b-45ef-3614-a705-6921c2e9fa0e | -12.68566 | -48.57966 | 2025-10-02 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0de2137d-98b5-3b16-bcf0-cc169e245faa | -15.2559 | -49.30151 | 2025-10-02 04:51:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5bec537f-f550-3ef3-9578-f758af5aa2cd | -11.15679 | -54.12381 | 2025-10-02 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a3583d1-a4c9-3523-8056-e05c37042e2b | -13.96268 | -48.11539 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1391fcf4-ad2e-3efb-a35a-dd8c718f0b63 | -9.92764 | -43.71915 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 60d66b48-1bac-37bb-ba3b-fdf980980e6c | -11.00529 | -46.58431 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 88fc6c7d-6e3f-3ec0-96d4-fa2c2f76e6a7 | -13.36808 | -47.28461 | 2025-10-02 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3fdf382e-f559-382e-a9b2-0040dcbb3016 | -10.98895 | -46.60166 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f5a65f76-534d-3669-9326-9c3d91fe39c7 | -14.31034 | -45.8877 | 2025-10-02 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63fab95a-9b90-3e35-b328-48aeacf0de09 | -11.51207 | -43.56531 | 2025-10-02 04:51:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 668d8d0f-b295-3c0b-a7a2-109e7ec0e5d1 | -13.68612 | -48.06504 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a23691f-48cf-3ba6-a02b-098e4f29edc6 | -16.37201 | -47.06406 | 2025-10-02 04:51:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f6e0b9a-5854-3b6b-92d7-79863af41c30 | -12.58321 | -49.89849 | 2025-10-02 04:51:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef78aff9-0044-3c24-af96-a20e121434f2 | -15.23336 | -50.11401 | 2025-10-02 04:51:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 93120237-be16-3c52-8981-63f8398faa95 | -15.15552 | -48.40316 | 2025-10-02 04:51:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c1606a1-c328-337a-b1a7-7348f2a6ddec | -15.18738 | -46.41274 | 2025-10-02 04:51:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c1bc7b1e-88e3-3267-a186-d70db558a9f4 | -13.96541 | -48.12815 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e7d072a7-c6c5-39a6-9d1e-e3daed5318cf | -11.08472 | -47.84892 | 2025-10-02 04:51:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1ec948e2-c487-3f06-aca6-ae85060ea69a | -9.94696 | -43.65893 | 2025-10-02 04:51:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef574905-edf5-3e6c-afd9-95a3be37cc73 | -11.14577 | -47.19503 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8669570d-bd05-3416-ac75-3201ec12fd22 | -9.92577 | -43.73317 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 37.4 |
| c1a9fde5-2b42-35e6-90f5-bb4bec3d2f80 | -9.94057 | -43.75303 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| db6bb919-84ac-3485-9fed-1c93da615de5 | -13.78998 | -48.06039 | 2025-10-02 04:51:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7950cbba-0ad4-32a2-ae25-432f836e83db | -13.56952 | -47.28023 | 2025-10-02 04:51:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81bf15ef-7800-3401-818a-762e13ff9924 | -15.19954 | -48.16723 | 2025-10-02 04:51:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4327cd17-f97e-3d55-a922-392d31f8c356 | -13.17696 | -47.38194 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fab2c9da-4036-32be-b331-eea4730fb34f | -14.65439 | -48.1269 | 2025-10-02 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96d4672a-0445-3750-a550-51668754af9c | -12.90721 | -47.17288 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9d92d0b9-dc88-3847-b0d5-9ca898864ae4 | -13.81347 | -47.54518 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 292db57a-7b03-3625-bf0b-fbfbbfb4c457 | -10.83709 | -46.62009 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d88bfd0-b033-3af2-8f17-b9fc04fdd507 | -15.28059 | -46.40271 | 2025-10-02 04:51:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d7320da1-2b5c-3be3-87ee-b334ce34cd77 | -14.30391 | -45.98067 | 2025-10-02 04:51:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 82e19cd9-0384-3829-b1da-3db68efa903d | -11.17619 | -47.26774 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6aa774e2-b7a2-325c-983e-9631b7273723 | -11.15347 | -54.12326 | 2025-10-02 04:51:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48d14596-7864-341e-bc7e-5aa4ac574236 | -11.59715 | -47.23392 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 80cd967f-419e-352d-baa9-bad53dd2f864 | -13.67369 | -48.09279 | 2025-10-02 04:51:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe8558e4-e7ad-3f44-bb93-da9f5f69027c | -15.04198 | -48.07326 | 2025-10-02 04:51:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f34ddcd3-9ea6-3998-9b54-cdc775191035 | -9.92685 | -43.72947 | 2025-10-02 04:51:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| f21d0a10-d580-3123-8c55-d009c2d516cf | -10.22715 | -48.21302 | 2025-10-02 04:51:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| eb16c310-dea0-32a1-9022-dc0d555eecce | -10.82503 | -46.63618 | 2025-10-02 04:51:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f39731a0-ee5e-388f-919e-fc212bf1395e | -12.81486 | -47.02126 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7496ef1a-385f-3679-8d80-ade89a2a377c | -12.88301 | -46.92698 | 2025-10-02 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c8b84a94-3309-3fe0-ae2f-9c346c431e11 | -11.1777 | -47.18913 | 2025-10-02 04:51:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README127.md)
