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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a8f29429-2c88-3b1e-a31f-bcb9d4faf1c0 | -15.99352 | -46.74192 | 2026-09-20 04:21:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a8cf5d57-b113-3687-a34d-7597c018bfcf | -11.95149 | -50.09699 | 2026-09-20 04:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bab464af-2d76-32bc-ad7c-a446408d378c | -10.88108 | -54.09459 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 67cf2857-260f-3a78-836b-bafa951cd248 | -11.23144 | -54.07454 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.6 |
| fd3a14a6-496c-3117-8d6a-21eae0528d38 | -11.21925 | -54.07202 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cf3a3536-8d2a-33ed-93c8-ba99788cc214 | -11.72552 | -54.55888 | 2026-09-20 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 511bea25-1e40-36fb-af62-b8a4aedf430a | -12.75593 | -46.19714 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e0108868-e09d-3dc3-be6f-a16faf04db46 | -11.86492 | -47.44701 | 2026-09-20 04:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e7e1f9a0-3708-32aa-ad97-25b6ba5d78f4 | -13.00113 | -46.91778 | 2026-09-20 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ba101912-1681-354b-b67a-b5dd0eb144e8 | -12.13281 | -47.03716 | 2026-09-20 04:21:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fe1c046d-44ff-30a6-8bb4-eb6a0a330345 | -12.12982 | -47.03169 | 2026-09-20 04:21:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 69624a77-45a0-30b7-a5fc-9e56818ce8ff | -13.02724 | -46.92326 | 2026-09-20 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3def2902-42bf-36fb-af18-a8d7edb2950f | -11.03203 | -54.15791 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 862550c0-1e6f-360d-94db-07a6660c2da2 | -13.01984 | -46.92134 | 2026-09-20 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9933f1b0-278b-38f3-8a08-6cb7c42c1630 | -15.32093 | -49.56192 | 2026-09-20 04:21:00 | NPP-375D | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5355d032-0143-34f9-ba1f-dfb44e28b27a | -13.74336 | -48.78151 | 2026-09-20 04:21:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 20a9c29a-9098-397b-9549-cd758ab95949 | -11.85988 | -47.67113 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4078c8a8-ee10-3180-b139-e6ce67924338 | -11.85874 | -46.87813 | 2026-09-20 04:21:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f0bde5d0-b306-3f9a-93f4-678d2255b278 | -11.8826 | -49.00516 | 2026-09-20 04:21:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22dcaaa5-cefd-3cd0-acb1-5f55ebf28706 | -12.15823 | -47.02684 | 2026-09-20 04:21:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 536ba3e0-786a-3b49-ab95-a797b6e401da | -13.26229 | -51.73021 | 2026-09-20 04:21:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06a2888d-75b5-39c0-8f82-c86055499ec4 | -14.67731 | -46.69607 | 2026-09-20 04:21:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 072bf31c-5a44-383c-8328-1a2372e9bef4 | -17.44156 | -44.72165 | 2026-09-20 04:21:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1084d031-314f-3795-b78b-8a3adfe25656 | -11.86578 | -47.65419 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8f651b4-193c-3ce1-b536-511ad4146ee8 | -12.74289 | -46.18602 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 383ba09d-0d79-3349-914a-bea85ede09c2 | -12.1612 | -47.03244 | 2026-09-20 04:21:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f76a3a58-a084-3dc2-98b7-fb2a80ccc554 | -11.85656 | -46.86802 | 2026-09-20 04:21:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 308dbb6c-29bc-33a7-9de2-1b6f050ef231 | -10.87517 | -53.99437 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f1a4a6fc-155f-3ff5-a573-a07e63e89857 | -14.79377 | -48.53244 | 2026-09-20 04:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2357c560-d6d0-3d64-93fc-270226baf42a | -14.1198 | -45.60234 | 2026-09-20 04:21:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ce30f07-5eda-35cd-bd11-5afec71e5223 | -13.02216 | -46.90795 | 2026-09-20 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2f241d5-5d52-3d4b-879c-87c083845f02 | -11.21299 | -54.07325 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c720773e-4add-3c2d-91b8-2747e1bd7eba | -13.64507 | -46.95525 | 2026-09-20 04:21:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd112f96-7406-3e53-a952-a74948c95652 | -11.87866 | -47.65816 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e98f077a-8e7c-31fb-ab64-ce8a2d55c157 | -12.34287 | -50.69023 | 2026-09-20 04:21:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9c05114-13ed-3ae6-870a-e73f34390665 | -11.85495 | -47.67567 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ddaa9065-f74c-3a54-b471-e350d27e0db7 | -14.68605 | -46.68878 | 2026-09-20 04:21:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e6410176-2959-390b-a34c-bd6f061ba93f | -13.94748 | -47.83443 | 2026-09-20 04:21:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4169aa41-20a4-3ca3-a3cd-2fe4ef1c631a | -11.72448 | -54.56392 | 2026-09-20 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f72a9ad-1c5f-306f-8643-8645a05f38e4 | -14.03021 | -52.09083 | 2026-09-20 04:21:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37b146bc-3de8-34d7-82a2-6c2377f7145c | -17.02209 | -47.14791 | 2026-09-20 04:21:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 7d281036-208a-3723-a38c-96fbf71bc111 | -17.01203 | -47.14161 | 2026-09-20 04:21:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bccb7e8f-8692-37e7-a323-a0c8a6e218cb | -16.49611 | -49.21568 | 2026-09-20 04:21:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff4f8f1e-188f-3f27-9f1b-3dc9f69775bd | -11.12925 | -54.01588 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a73eac34-7af0-34eb-b7b0-aaaaaa97798a | -11.84027 | -46.82642 | 2026-09-20 04:21:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 15570eba-ee26-3f08-87d7-a37747b05a6d | -11.86254 | -46.87883 | 2026-09-20 04:21:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 03fe4d85-1dcd-35c1-b7fb-4bee378b6b6c | -14.91385 | -49.91893 | 2026-09-20 04:21:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5499c117-b3da-3fb9-896d-ffeb35b33568 | -11.76442 | -47.44769 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba04d3ba-cd1e-3c68-90bd-9219fba2b1e3 | -11.85688 | -47.65818 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3d4d9172-7565-32d7-b8b4-e47a74ed4484 | -14.04602 | -52.09164 | 2026-09-20 04:21:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 830b0aa4-0b93-3b36-916b-a7222e87959f | -13.96428 | -47.8533 | 2026-09-20 04:21:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86a6e8bb-a565-3212-903b-2bf92d5b8e00 | -14.05168 | -52.08992 | 2026-09-20 04:21:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f77dfbad-fe60-3e04-a5b9-0fb1b3653be6 | -10.87772 | -54.07903 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fb14d3d6-b101-3460-b254-218e4904ab44 | -10.86627 | -56.17721 | 2026-09-20 04:21:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4b8e740d-7a8b-3a71-8c17-84aa61ca18db | -14.6933 | -46.69011 | 2026-09-20 04:21:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 1df5a2cc-7b4c-3e4c-8c6f-1680272cfcc6 | -11.76705 | -47.43253 | 2026-09-20 04:21:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e96d0b46-b612-3589-a3d1-19a36d7185be | -12.74898 | -45.95356 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 386d5efd-7eeb-3839-8976-a7b61ff24303 | -11.87101 | -47.67155 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9771566a-5c9c-3345-96a4-b5ddf14ac665 | -12.74071 | -46.17689 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 745a2bb7-d114-32d7-9e74-d12bb263032e | -11.86294 | -47.67704 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 0a4d147f-c4e1-30c9-b118-01bcde15edfe | -15.46052 | -48.44565 | 2026-09-20 04:21:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0f7d00ae-24b8-35c9-9c8b-0d9473cc9983 | -18.37396 | -49.39626 | 2026-09-20 04:21:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e4e331d-6daa-37eb-8445-287a3d0695a5 | -16.43283 | -40.55339 | 2026-09-20 04:21:00 | NPP-375D | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d1cc7665-326a-3bc1-9aed-d5f223e6e563 | -10.87408 | -54.08949 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a4d4e60a-fa08-37d1-8ff4-f6e21e9bf378 | -12.47695 | -50.04817 | 2026-09-20 04:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9a2f5ab5-d23d-32ed-8565-8b7b20046244 | -16.82909 | -47.63561 | 2026-09-20 04:21:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 15a0f51a-c5bd-38e4-bd83-c0c7867af6ab | -11.13437 | -54.02196 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ac554824-91fb-3f48-b2e8-3de63b36cf21 | -19.87665 | -44.0525 | 2026-09-20 04:21:00 | NPP-375D | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bd2601be-b3b0-3695-80d1-5733b657447d | -14.91902 | -49.91546 | 2026-09-20 04:21:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f7f6bc4-717b-39ca-8a78-b5f4645819ef | -13.03096 | -46.9241 | 2026-09-20 04:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8a7dd6ca-43a7-35af-adac-bd8250a0b7e1 | -13.39641 | -49.46045 | 2026-09-20 04:21:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c08b2bc-cad4-30cf-b1d6-7f6dc0001350 | -11.87313 | -50.00026 | 2026-09-20 04:21:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44ee68da-06a6-3db3-b8e5-d2686bededf1 | -12.75438 | -46.14016 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9468890-8c7c-3186-9dc8-01eecbf5ee37 | -12.75589 | -46.17531 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e5239ce7-70e1-3330-ad07-48b59f7e31cf | -11.85904 | -47.66944 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 95781520-3365-3eb3-8cc0-0089e0ea023b | -11.77492 | -47.43395 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 34488783-55c1-3659-a70f-cc5824e5e515 | -14.68531 | -46.69308 | 2026-09-20 04:21:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a1fa96e7-7cbf-3e68-a50e-1a57d9b34c62 | -13.73019 | -48.78317 | 2026-09-20 04:21:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 04f970d7-481f-3509-82fd-826ffffd16e3 | -12.75089 | -46.20494 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 44ff58cc-4cfa-3277-b2d6-1662853e6be8 | -11.09401 | -54.03739 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 25bb6617-dfbb-36ff-ad0f-a8c408c532fb | -12.41452 | -47.46876 | 2026-09-20 04:21:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa4b1b31-6508-3ddf-a22c-8746bfdc5ef1 | -17.01563 | -47.14228 | 2026-09-20 04:21:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f1a7359c-9586-3a09-95ad-2f42e88f5369 | -10.8688 | -54.09204 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2be9a1a7-c145-33b5-9b3d-f2c47d21b128 | -15.86908 | -49.90363 | 2026-09-20 04:21:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 15546f54-92f7-3c09-9e0c-25ea140d7a2f | -11.22866 | -54.08838 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bf45981e-a66b-3b4b-8d34-2c08b131b465 | -11.11324 | -54.03244 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 93e7a56e-3c99-3661-bb7d-ef5c4662698e | -15.4722 | -48.42617 | 2026-09-20 04:21:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96999c4c-5392-3145-bd32-625bdf037117 | -14.69256 | -46.69441 | 2026-09-20 04:21:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 92ef27ed-bbec-376c-89e6-2ec8aa9c4b04 | -14.78787 | -48.54211 | 2026-09-20 04:21:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0cb5a0ae-6fc9-3fc8-a143-693c09be26b1 | -11.85723 | -47.67992 | 2026-09-20 04:21:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8e93bfc6-5647-3405-bd0f-5ac9217b2cd7 | -12.75298 | -46.17044 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11b64093-9a65-312c-a74e-4095c9d95d58 | -15.88181 | -49.90701 | 2026-09-20 04:21:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28adf761-340a-3a39-9412-0af433cee2dd | -11.04425 | -54.16079 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2fcb38cc-2c6a-3bbc-8d54-9e72e91cb3c2 | -12.64925 | -49.4727 | 2026-09-20 04:21:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| be0b1eb1-2b7f-3a5f-89d7-b0b1731fa779 | -11.73897 | -54.55659 | 2026-09-20 04:21:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b5b4b1f-99e7-32f0-b5f8-ee584278de10 | -10.86975 | -54.08721 | 2026-09-20 04:21:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 88cb8881-5797-3ec8-9a54-bdb6e5f8c04a | -11.39048 | -51.42075 | 2026-09-20 04:21:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 893b7069-981f-340e-9a81-b0073cdc68f5 | -14.67369 | -46.69541 | 2026-09-20 04:21:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 090a12c9-433a-3ada-ac45-224cbefd9431 | -12.75017 | -46.20919 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4756663-3cec-320f-a6c3-6e7c1bd37ab9 | -12.75665 | -46.1929 | 2026-09-20 04:21:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README43.md)
