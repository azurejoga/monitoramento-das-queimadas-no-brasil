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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c4f1510-9a91-3f36-b46d-c7b3b8a849bb | -14.95494 | -46.61167 | 2026-08-14 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8fbbf0b1-ead9-3abf-a394-8b6bda383433 | -14.95657 | -46.6027 | 2026-08-14 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c75e8a0-6b91-3f72-b061-f2b861bbc9c4 | -12.722 | -48.43576 | 2026-08-14 04:14:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 09734733-4a99-3570-a322-ca2c109806be | -13.56307 | -46.25917 | 2026-08-14 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 58b71f83-80af-3a6f-a129-11c3bafd165d | -10.97039 | -50.5382 | 2026-08-14 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c645e8ea-4057-364b-8f38-c7056641bf9e | -13.55713 | -46.24741 | 2026-08-14 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 831532cb-efe9-3b5a-9203-49eedea4073a | -12.64677 | -47.64391 | 2026-08-14 04:14:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43e2ca17-4934-337b-9070-ec9e85bd86d9 | -14.96066 | -46.60189 | 2026-08-14 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f76cc2f-3a67-3840-9a86-abb8ee188162 | -14.62887 | -42.51722 | 2026-08-14 04:14:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5fdb40c5-c2e2-3407-b66c-ecac42d5e7ec | -12.75935 | -44.55313 | 2026-08-14 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1631039c-4447-3606-a838-b4181861b3c7 | -11.31643 | -45.21927 | 2026-08-14 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 843bc33f-12ab-35b1-b43d-661f74c13c3e | -14.47106 | -45.68103 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 783e07e9-db32-358a-8eee-1460c85c98fb | -11.47121 | -54.61652 | 2026-08-14 04:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 60037ef7-1c3f-3fcd-a84d-b8c4bfce4f41 | -12.493 | -43.7745 | 2026-08-14 04:14:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 821c69da-f4c2-3587-9ced-2d9d52b608d2 | -11.80216 | -51.87904 | 2026-08-14 04:14:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8a2f243-1335-34c2-9cd8-5095dd7f01e7 | -7.80437 | -44.11636 | 2026-08-14 04:14:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed42fab7-b964-3bdd-8009-ae409c750498 | -11.49298 | -54.61448 | 2026-08-14 04:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 69e8f549-568f-3616-b1b1-7dde01f2e24c | -13.2807 | -54.21416 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 53ba7de2-5aea-3a05-8d62-67f304a4183e | -14.96047 | -46.60332 | 2026-08-14 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5bd7a0bc-64d9-3e28-81b7-ff83bbb216a9 | -7.80562 | -44.11414 | 2026-08-14 04:14:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dd39481c-e111-30bc-be9c-1e53854942b4 | -12.51693 | -55.78331 | 2026-08-14 04:14:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76809f71-f9ee-331e-804d-df6b0a2dc04e | -7.71493 | -46.23822 | 2026-08-14 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| efa883b6-5098-3cb4-a2df-9dc94834948b | -11.67092 | -46.75709 | 2026-08-14 04:14:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c625cba-193e-3418-9152-150d36af2184 | -14.29318 | -45.27091 | 2026-08-14 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61a1c8fe-d5f5-3334-a89b-53cccc0f5d5c | -11.06918 | -50.94365 | 2026-08-14 04:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54e4f4e9-a532-3662-957b-6f7c7a619b86 | -11.49016 | -54.62878 | 2026-08-14 04:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dccc72a8-c9ba-3dd5-8644-486dec54e40a | -11.88154 | -45.9576 | 2026-08-14 04:14:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f6c4c4a-cfc3-37cb-90e8-45fa09acc7f9 | -14.95574 | -46.60723 | 2026-08-14 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c80eed6-112f-36c7-b830-c2f1a7b3d3a0 | -8.55376 | -54.59847 | 2026-08-14 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b21eaab3-e045-3d68-9744-a54e244c6c82 | -15.01049 | -41.65005 | 2026-08-14 04:14:00 | NPP-375D | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9996f6a5-45cd-39c3-9fc7-bab6e312be8e | -14.47252 | -45.68842 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f3d4a41a-5b4b-3dc1-aa2a-5a9576b72ed9 | -9.05532 | -50.62645 | 2026-08-14 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ca939fb4-c9ad-37a6-a7f7-a93a03618100 | -11.49712 | -54.62868 | 2026-08-14 04:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 4dc9811e-475a-323f-8229-44cd068b7174 | -7.60295 | -46.46897 | 2026-08-14 04:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 53112547-8a66-3ba6-8ecd-5a0a13f8a603 | -11.48145 | -45.09502 | 2026-08-14 04:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e45a68f8-48d7-36ac-bf3e-74b9ad63f05f | -13.28278 | -54.23186 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 65a5b80f-8656-3224-8bb8-f0f6f2d6d735 | -14.45611 | -45.69473 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10441170-b848-3541-9a04-e5bb4882e63f | -9.97589 | -53.95693 | 2026-08-14 04:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e25adb5-e11a-3c33-a059-fcb2d2e60b6e | -12.71039 | -48.4477 | 2026-08-14 04:14:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 65261ee4-f4f8-3f1a-a128-3f85abccadf8 | -14.6283 | -42.52079 | 2026-08-14 04:14:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ab9443d8-d7ae-3fc2-ae19-a0eb97553057 | -10.97576 | -50.53928 | 2026-08-14 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61c6a1de-3eda-3071-8699-b881997e00ec | -14.94569 | -46.61851 | 2026-08-14 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52a0cd42-45c5-3d25-9152-2a5d51ac1fff | -13.56786 | -46.25477 | 2026-08-14 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 9e4ce5fd-327a-39b6-ab3b-6c546ede4d1c | -9.12568 | -46.38678 | 2026-08-14 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ed64252-29e2-366e-a6cd-cd99e3a800b8 | -11.07397 | -50.94842 | 2026-08-14 04:14:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 01acb561-c79f-3ba4-8b34-8025fe1334ef | -14.99142 | -46.60954 | 2026-08-14 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 84ce1ca3-e757-31d2-8a34-f5efee42d024 | -13.23567 | -54.26815 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8b38e9c4-647c-3d11-865f-3c7b7684c458 | -9.59669 | -49.32595 | 2026-08-14 04:14:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf2d8a72-dab5-3686-9950-42cb1b478288 | -11.46988 | -54.62278 | 2026-08-14 04:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f8b96fe-ab08-35ba-978f-60fd4d423c3e | -14.6322 | -42.51777 | 2026-08-14 04:14:00 | NPP-375D | LICÍNIO DE ALMEIDA | BAHIA | Brasil | 2919405 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 13c0f083-951a-32bf-8511-ad04640bcea7 | -14.95432 | -46.61509 | 2026-08-14 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 188ba23b-807d-38c7-b0de-c48b88381833 | -14.47916 | -45.69432 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 851548b7-a195-37a8-b94f-6ff72814cc76 | -13.75381 | -53.41608 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0714eb2-1ec8-3c0e-a784-9950d98623a4 | -13.56009 | -46.25334 | 2026-08-14 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 60d9cbf1-0c13-3e93-afd7-ccb10f1da79b | -13.25488 | -50.37935 | 2026-08-14 04:14:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 521d9b5c-5561-31c0-9791-b64eda5c9578 | -13.38696 | -42.39016 | 2026-08-14 04:14:00 | NPP-375D | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 337970eb-fcb6-359d-baca-03209c32fcac | -12.03318 | -47.81506 | 2026-08-14 04:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 59ffa0df-0714-34a3-9945-9592259a8d12 | -10.73131 | -47.92752 | 2026-08-14 04:14:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7833b406-2dc2-3ac5-ace3-7fdea8f9757d | -14.47623 | -45.6891 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| edb7d5d6-c213-3d65-9518-49556794439f | -7.71067 | -46.2375 | 2026-08-14 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9bf353b2-2022-3a4c-b580-2da1a138d9af | -11.48883 | -54.63533 | 2026-08-14 04:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 56b35450-b314-3d0d-a649-188627a9cdff | -13.28604 | -54.22096 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0c9f0723-505c-3fbf-aa74-8483b3ae6be2 | -14.29029 | -45.26589 | 2026-08-14 04:14:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 923c310d-59cc-3e4e-9a69-80fd60975389 | -14.94092 | -46.6228 | 2026-08-14 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dd2aa9e7-9381-31b1-b102-dd1a8d597d14 | -13.24812 | -54.23575 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a866dfb7-518c-3f05-8bb2-7201b023edb5 | -14.46881 | -45.68774 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f0132efa-0e77-33d2-bd91-09a69d01c4ed | -11.32939 | -46.23064 | 2026-08-14 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 15e8554f-d513-336c-b0ed-7a0ae644b0d3 | -12.02402 | -47.81924 | 2026-08-14 04:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22af52f2-35c2-3aee-85e7-5a5319245012 | -14.9361 | -46.62738 | 2026-08-14 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a1bd2cd1-a82e-3c70-be9d-499bc23c98a1 | -13.27331 | -54.2129 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f2fb875-76b0-3eac-aed8-155655e5e588 | -14.47687 | -45.69144 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d38f8680-b3e8-349c-9d2b-0db942631b68 | -11.49033 | -54.62712 | 2026-08-14 04:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 5a7bd811-7891-30da-9f7c-c771fd8e0392 | -15.52887 | -40.85212 | 2026-08-14 04:14:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4207180c-919c-35a5-b7e2-c578d3d7f60c | -12.55895 | -48.34882 | 2026-08-14 04:14:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a1711b9-117a-3273-b687-0ea6471ec958 | -11.50119 | -54.64326 | 2026-08-14 04:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75ad6df9-b1e4-3617-95bb-74d2e6932806 | -13.23435 | -54.26819 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 894d7608-99dd-3b78-9c0b-fcfe4d74ffe4 | -9.12304 | -46.40205 | 2026-08-14 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b74a6605-7950-3b41-a1a2-037b3c174eae | -13.28267 | -54.23728 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| a1f87b4c-75ba-35ce-ba9e-31515425d59c | -10.82594 | -50.3223 | 2026-08-14 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 004b63ae-22b9-38e2-852f-972b0cea6422 | -14.46959 | -45.6832 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0f41a4e8-e43b-38cb-b1f2-2c6ad652eb51 | -13.27746 | -54.22511 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| cd1b3e46-d4e9-3551-b35b-339a2b2237b3 | -9.12859 | -46.39498 | 2026-08-14 04:14:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6ec5efc-9878-38b6-acea-0840f285bd75 | -13.74657 | -42.57138 | 2026-08-14 04:14:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2238f22e-519f-32b8-8741-bbec603b50a3 | -13.24212 | -54.26971 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1c3e8c2b-d246-3260-a7b5-0291d3ffbae7 | -15.13583 | -41.56405 | 2026-08-14 04:14:00 | NPP-375D | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 269bf13d-8d4a-305a-8cf0-2b6124dc5fdd | -14.19826 | -46.21253 | 2026-08-14 04:14:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e89c9713-b8ee-34d5-b553-86b08fed50d2 | -15.14028 | -41.55743 | 2026-08-14 04:14:00 | NPP-375D | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a5c1bf51-0a28-358d-b8bf-ea21d8e62df8 | -7.4566 | -46.15175 | 2026-08-14 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c0b5314-3f5f-3d11-acf0-d480fd9b131e | -7.80935 | -44.11474 | 2026-08-14 04:14:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72ae121d-e30d-35ba-a800-bc7ec3dc35c8 | -13.6521 | -46.25684 | 2026-08-14 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b7fd78f-2bed-3590-b038-19a4a01bd5de | -9.98385 | -53.95232 | 2026-08-14 04:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 66670060-a678-3862-85d4-0b4580250f52 | -14.95404 | -46.61661 | 2026-08-14 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d7696b4f-8bd7-3b51-9f3c-5dc388c9eb8e | -10.9816 | -50.54671 | 2026-08-14 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b20e062-3d78-36ef-99be-70633930839c | -12.51756 | -55.7889 | 2026-08-14 04:14:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 68b2083d-6c77-3a36-b33c-1c95775474cc | -11.46973 | -54.62431 | 2026-08-14 04:14:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dffd6132-ee12-320c-8e39-655bec123c08 | -12.49365 | -43.7706 | 2026-08-14 04:14:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8f69f2f4-5855-3b04-81df-fe7378d93d3e | -13.27844 | -54.22508 | 2026-08-14 04:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 50d8ea13-9e6b-3118-8275-b90e7e9a5d8c | -9.05602 | -50.62273 | 2026-08-14 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41b3b163-9f0c-3e1b-9040-89fc633d2787 | -14.47467 | -45.69818 | 2026-08-14 04:14:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 34453a53-ce5d-3f16-b700-275081cedbe2 | -14.97241 | -46.60337 | 2026-08-14 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README14.md)
