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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2452dd0-ff6c-361c-980f-742a7fe31a02 | -7.0378 | -45.5443 | 2026-08-29 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8dd278b4-8113-3802-ad42-fe3b495d136f | -6.34533 | -44.09156 | 2026-08-29 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 99242191-3601-30de-9d75-2c77ba539a01 | -5.3139 | -47.04774 | 2026-08-29 03:55:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e83868b-0c8c-3fbf-8b67-8d2848b075b3 | -6.90201 | -43.65538 | 2026-08-29 03:55:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 836ebf46-1837-347f-bd62-303fc51b871c | -9.46776 | -45.64171 | 2026-08-29 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 4a89a81e-4dfa-332c-a598-5fdaeccde3af | -10.91846 | -46.61034 | 2026-08-29 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 32dc510f-9eb0-3409-85fc-2dcf0661516e | -11.25122 | -45.07784 | 2026-08-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8005b826-e6d9-37a4-b568-d8a1deed52a0 | -10.53809 | -50.47445 | 2026-08-29 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d838cd04-6982-3ced-bae4-2f85badd4398 | -8.01801 | -48.0135 | 2026-08-29 03:55:00 | NOAA-21 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5e9c9997-39d7-3ed9-8c4f-af945d5aac5f | -11.48336 | -45.06765 | 2026-08-29 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8477f77a-675e-367e-9a11-9cc079326645 | -5.64678 | -44.30111 | 2026-08-29 03:55:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c854ede7-1761-3e5b-b586-0aca19f7eed3 | -4.28528 | -48.19174 | 2026-08-29 03:55:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5bf2449e-dd1c-3b49-ba08-38f963d09f34 | -7.07476 | -42.21432 | 2026-08-29 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1d28902d-e5e1-35ae-94e9-e9e89c90c32b | -10.91847 | -46.609 | 2026-08-29 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5fc794e4-d9df-3b0b-8347-ec3c1d935777 | -11.23471 | -45.07507 | 2026-08-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45707f67-c092-3b1c-96ea-5d644ff5ef6e | -11.3757 | -45.13389 | 2026-08-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 18c4767e-f59e-3da5-b70a-1694257f9a31 | -11.35927 | -45.15495 | 2026-08-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b8cc4aeb-f650-3f71-a09e-5e41f5262bbf | -7.07953 | -42.80462 | 2026-08-29 03:55:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0c4b9fcd-be53-3b5a-8dec-722eedf74724 | -7.21249 | -42.75197 | 2026-08-29 03:55:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5d9a643c-a631-3c5f-b8f0-739d445be8cc | -11.25316 | -45.06673 | 2026-08-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 17904b95-6b41-3f4c-9dd5-5e5f3559929d | -10.91386 | -46.60826 | 2026-08-29 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fb8b03ff-bde2-3188-b731-184e9e0244ae | -6.95014 | -45.23372 | 2026-08-29 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a3b7b15-91ea-3932-89cc-945405d28a3c | -8.94907 | -50.80968 | 2026-08-29 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 49a7ad1f-9297-3cf6-a2e3-d6df1ecbb8a3 | -5.80808 | -43.79925 | 2026-08-29 03:55:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c088b845-65f4-3d0b-80bf-6d8e39760cba | -6.62829 | -43.74142 | 2026-08-29 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f12486af-7f3c-37cc-bc86-2a6543575442 | -9.42727 | -51.68745 | 2026-08-29 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ff30cab1-3092-3bc0-8738-6f2507a33472 | -7.30453 | -49.54118 | 2026-08-29 03:55:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 35eaa6af-7ff8-3d2b-a467-4cf8ed93e591 | -8.79882 | -50.49535 | 2026-08-29 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9bff3f20-cf96-38c2-b19e-a6e93684e229 | -12.43339 | -42.89346 | 2026-08-29 03:55:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 08976dbe-86b4-38bf-938c-f83ed908fc40 | -11.23536 | -45.07133 | 2026-08-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48b3ad6f-52a4-32b2-a91e-9dca31cb979f | -11.35859 | -45.15891 | 2026-08-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| dafa15c3-19b5-3cc7-a29a-ad9f940f60d2 | -5.65107 | -44.3018 | 2026-08-29 03:55:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 10d2d56c-550d-3c96-874d-43a88de144cf | -10.91386 | -46.60958 | 2026-08-29 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a1c0f2a5-5f6d-3898-b154-82a58aba2be5 | -10.88832 | -46.62 | 2026-08-29 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f5f81a1a-dfc4-3ef2-8e6e-a5271d4fffb9 | -5.31325 | -47.04665 | 2026-08-29 03:55:00 | NOAA-21 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ebdd373-8292-38b7-96e9-42528ef92ffd | -6.9026 | -43.65188 | 2026-08-29 03:55:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 26ce8a19-9dfb-35e8-bf0c-eb9769542222 | -7.26957 | -45.34927 | 2026-08-29 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0a4aab5c-89ba-3293-a41c-96717c6467d2 | -6.62363 | -43.74432 | 2026-08-29 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 678ef468-1edc-35ed-a15d-6174a525d8e4 | -7.26431 | -45.35301 | 2026-08-29 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21f1d8c6-3a2f-3a14-9476-57f7a76cc587 | -7.12095 | -43.16521 | 2026-08-29 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1e510b18-1ed7-33d7-a5cd-069252326c01 | -11.48304 | -46.93755 | 2026-08-29 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e80b69ae-ee69-329d-8666-e7fea30b8c86 | -11.49235 | -46.93911 | 2026-08-29 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a13d866-4424-3a8d-bbc9-e49e7c287eb4 | -8.82055 | -49.62999 | 2026-08-29 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1902a287-963b-309b-9f98-413ff9887a51 | -6.87767 | -42.87777 | 2026-08-29 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 79989996-bf6b-3d48-a7d2-cf7eda4881d7 | -11.3798 | -45.13479 | 2026-08-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 77852c60-30a1-33a6-afe3-ff77752e30cd | -5.13081 | -42.88132 | 2026-08-29 03:55:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 911ea9f2-3e65-34aa-b8d8-03b07a81490d | -9.68674 | -46.55466 | 2026-08-29 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 20b6a926-a03f-3e37-bbd4-5d4e8b5cfa31 | -9.64255 | -48.2699 | 2026-08-29 03:55:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29809bb7-1795-3890-b6ae-1ac9622158fd | -10.89663 | -46.62662 | 2026-08-29 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b28e4e2e-bb24-3e18-a6c7-75e8864a65f5 | -6.34116 | -44.09079 | 2026-08-29 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a6ad9b96-43e0-3f22-888b-ed53398ba6b2 | -6.91301 | -44.9508 | 2026-08-29 03:55:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 939c9f5d-e1a4-3a60-8524-f3828dece93d | -9.15136 | -49.97299 | 2026-08-29 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 75f7fe69-65c9-374b-bed7-ba92603ef060 | -9.42728 | -51.68378 | 2026-08-29 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4749144b-fd39-3e4c-a249-58e96c447543 | -6.95094 | -45.22907 | 2026-08-29 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2aa9d024-2b89-3708-a64e-122d78a5b680 | -11.03122 | -49.68491 | 2026-08-29 03:55:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7302f908-bb63-3853-918f-97ee3b3c99d3 | -4.36921 | -47.77172 | 2026-08-29 03:55:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| f59291e6-4ac8-364f-bb74-267b6fc0ba95 | -5.29372 | -50.9375 | 2026-08-29 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 205f12e3-ba4f-3e7d-a829-0bb4c0072a65 | -9.46752 | -45.64045 | 2026-08-29 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b7ebc340-d279-31c7-bdb9-b2033d3266cc | -7.06558 | -42.15467 | 2026-08-29 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ca543034-4c8d-3223-a4fd-f21fa9f07589 | -5.28928 | -50.94082 | 2026-08-29 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 68b60e58-26ba-34ea-9408-6b1089128399 | -10.92679 | -46.61683 | 2026-08-29 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a8adbbc-2eeb-3c1f-a1ff-09115dd623ea | -7.12733 | -42.77153 | 2026-08-29 03:55:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4f02eb2d-9a31-3afb-8f61-734ffe9afb02 | -8.97527 | -50.79626 | 2026-08-29 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d587d524-89c8-3c89-9a81-c5405a095033 | -8.28443 | -39.97424 | 2026-08-29 03:55:00 | NOAA-21 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d04cac26-edf3-36c4-b1e5-3c5ad6759abf | -11.2471 | -45.0771 | 2026-08-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bdf665ba-6d25-3b34-af54-df34dd918350 | -11.21736 | -45.05302 | 2026-08-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7f826cd4-867e-31cc-9cf6-53d7b2f22d2c | -7.27413 | -49.84424 | 2026-08-29 03:55:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a9e51c17-5667-3268-be7c-3c9c8f168879 | -6.41134 | -51.67442 | 2026-08-29 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f055e4ac-2ba8-3f2b-b036-f8dd9d13f664 | -7.28018 | -45.85897 | 2026-08-29 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 20.7 |
| da5ae171-8e35-31d4-94b9-bcaed9a65304 | -5.16757 | -45.42492 | 2026-08-29 03:55:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f200d3cc-3f00-3790-acca-93e570f4ccdf | -6.59984 | -44.69283 | 2026-08-29 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 84a847de-a782-3c14-839b-53c505d8317f | -9.46623 | -45.65064 | 2026-08-29 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 47d95e07-25df-3f1c-a8f6-92e8bcc8644f | -7.27814 | -46.69009 | 2026-08-29 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3b94ca0-0586-3390-abbc-ab9f5b8392de | -11.48586 | -46.94853 | 2026-08-29 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e5ba5395-da33-3c9e-b256-f9cd97b84aa6 | -7.60634 | -47.28769 | 2026-08-29 03:55:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| edf5b357-3b7a-3144-8d08-0a133e86ed18 | -7.27338 | -49.84841 | 2026-08-29 03:55:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 81489550-4d71-302e-89ca-bf88c20b5570 | -11.25573 | -45.05195 | 2026-08-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15fab414-f274-3541-ac1e-74bd742197f4 | -11.24362 | -45.07271 | 2026-08-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 59b63028-73c8-376f-897e-de1710d8d953 | -7.09319 | -42.21728 | 2026-08-29 03:55:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7de0915b-fd48-3cb8-9338-5cd7bc60d201 | -6.90318 | -43.6484 | 2026-08-29 03:55:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| dabd3bdc-d4e8-38c3-b9fd-e19ff8ad1ea6 | -8.09738 | -47.59906 | 2026-08-29 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 352fa9cf-c552-36dc-8680-979658e1dae4 | -11.48985 | -45.10343 | 2026-08-29 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1aa77761-ea3e-3e1e-a840-e8ba74e5426d | -6.33827 | -44.08228 | 2026-08-29 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13f44d3d-9c75-3901-b953-8597339fe265 | -11.48639 | -45.09894 | 2026-08-29 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 787aebcc-162d-34e7-9971-a3a81bd1e4c7 | -6.90721 | -43.64909 | 2026-08-29 03:55:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81dbbde6-19c7-3649-b16b-2688d2c1b4ea | -6.63176 | -43.74574 | 2026-08-29 03:55:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67900606-3707-36ee-8689-bbfc0ecae12e | -8.9887 | -50.7934 | 2026-08-29 03:55:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4a2306bd-31c8-34b6-80c1-b88dd799b86e | -11.3634 | -45.1557 | 2026-08-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 05ac1653-07eb-32d2-8fa8-9448008ba449 | -8.95007 | -50.80435 | 2026-08-29 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b7a1c3e7-ed60-3b93-9495-1f25c265b384 | -8.09684 | -47.60214 | 2026-08-29 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b4c2109-6598-337d-a053-b25b32f2ffc5 | -9.7216 | -47.77113 | 2026-08-29 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f40d01f5-68a6-382c-ad6c-9adf7938d57f | -9.46594 | -45.64931 | 2026-08-29 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6cf456bc-8836-3e3d-bbef-d60e9828b5c1 | -6.90662 | -43.65257 | 2026-08-29 03:55:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2c0064c4-2ec0-392b-b2ef-ec9bf80230f1 | -9.43375 | -51.68884 | 2026-08-29 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 53ad78e1-6668-3183-83d2-e10a48767342 | -11.01756 | -45.07198 | 2026-08-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c0001e2-307d-30bb-9f80-cbb0f54249bc | -7.30142 | -49.97524 | 2026-08-29 03:55:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7e61c399-2853-3e12-9f7a-9e01c9e19ff1 | -11.24643 | -45.0809 | 2026-08-29 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 894c75e9-6aa2-32bc-a312-99140a929dc7 | -9.43153 | -51.69641 | 2026-08-29 03:55:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d883e985-c92d-31d8-865d-8e7af50a10c3 | -7.53945 | -44.45922 | 2026-08-29 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f556eda-353b-39e6-9893-f4e5df8540da | -6.49134 | -49.909 | 2026-08-29 03:55:00 | NOAA-21 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README23.md)
