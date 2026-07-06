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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 666ef67c-812c-3d54-91aa-9a88a55d298e | -10.4707 | -50.0267 | 2026-07-06 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| f4303c3d-3b5c-3661-bb3f-9f8fcd847047 | -11.6851 | -46.382 | 2026-07-06 15:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| aa81021c-857d-3c44-83ea-f8524234d6da | -11.666 | -46.3846 | 2026-07-06 15:50:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 182.2 |
| 4676b9b0-b7fe-3d08-991f-9d022120109a | -2.8816 | -42.1666 | 2026-07-06 15:50:00 | GOES-19 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 50543184-8e82-3f52-a6ba-afb1b99c3c3e | -6.8947 | -43.7299 | 2026-07-06 15:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 62e67a3f-2eea-36d8-97cf-d95815aa7129 | -10.4521 | -50.0073 | 2026-07-06 15:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 071a088e-05fa-32fd-bad3-321b8c3cf07a | -2.9003 | -42.1659 | 2026-07-06 15:50:00 | GOES-19 | ÁGUA DOCE DO MARANHÃO | MARANHÃO | Brasil | 2100154 | 21 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 061789ce-172e-35a8-8fa4-6c654aeb3f22 | -8.7294 | -54.5645 | 2026-07-06 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 431.9 |
| 6a6a6e5e-de9f-31d6-87ef-c174a5b93260 | -8.7108 | -54.5657 | 2026-07-06 16:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 767059ef-f93e-32f9-9da1-0f9a4fedd785 | -13.2975 | -54.3448 | 2026-07-06 16:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 119.2 |
| 8eefe326-80ed-34a3-aa1e-cb8666a0b24d | -13.2972 | -54.3655 | 2026-07-06 16:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 117.3 |
| fbd5298a-9a3a-3bec-a43f-ce4352f1b668 | -13.2969 | -54.3861 | 2026-07-06 16:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 7d6ea55e-0b9b-3971-9b4f-52c1b91e8894 | -10.4707 | -50.0267 | 2026-07-06 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.3 |
| ccd94eb7-02c6-32e7-8e6d-07ca41afee0e | -13.2783 | -54.3469 | 2026-07-06 16:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 193.3 |
| d4eb568d-8c28-3171-a85f-c451ed4f8e11 | -10.4521 | -50.0073 | 2026-07-06 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| ab93cf5c-41f7-3ccf-b984-0dc7b5986959 | -13.278 | -54.3675 | 2026-07-06 16:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 156.3 |
| ef20224f-c721-3304-849e-44d42e96a2f5 | -13.2972 | -54.3655 | 2026-07-06 16:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 111.9 |
| a7bc5e83-3027-39f0-bb07-3de8b4a13ddc | -8.7108 | -54.5657 | 2026-07-06 16:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 4e3e0df6-be93-3bcc-a18e-812d4c0b1fe8 | -8.7294 | -54.5645 | 2026-07-06 16:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 195.8 |
| 50614072-fda4-34ca-a717-13e68fa1d118 | -13.278 | -54.3675 | 2026-07-06 16:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 132.3 |
| f1678fd0-8dd5-34ea-9cd1-246742b63389 | -10.4521 | -50.0073 | 2026-07-06 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 7aecdfc0-3f23-3c11-ade7-c5bbadd458e2 | -13.2975 | -54.3448 | 2026-07-06 16:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 82cd6def-6897-36f3-9a2d-6942e73555ed | -13.2969 | -54.3861 | 2026-07-06 16:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.1 |
| c1800b99-8234-326b-a0d0-57011bbf9503 | -8.7106 | -54.586 | 2026-07-06 16:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 3166e304-6a59-3074-9be2-fce5c74867db | -13.2783 | -54.3469 | 2026-07-06 16:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 146.4 |
| 3c72448e-a21a-3b6d-a172-45eb0fddc0e5 | -11.666 | -46.3846 | 2026-07-06 16:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 127.7 |
| 1403ce85-4684-30f1-9a2b-982ff13b863d | -8.7106 | -54.586 | 2026-07-06 16:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| f877fc8b-4fc4-3dd7-a774-f2bebd72fce7 | -13.2972 | -54.3655 | 2026-07-06 16:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 131.7 |
| f538ca04-2e28-33f1-831d-b590eff295f2 | -11.4139 | -46.622 | 2026-07-06 16:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 69.0 |
| a8d099eb-4dde-3622-bad8-9bef6ebcec2d | -13.278 | -54.3675 | 2026-07-06 16:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 123.3 |
| 8503ed44-caf1-36cd-a04a-f5583b47047d | -13.2975 | -54.3448 | 2026-07-06 16:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 122.0 |
| c6b06721-f5c2-3b58-a617-dae8d457b2e3 | -13.2969 | -54.3861 | 2026-07-06 16:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 4cab342e-4420-386b-aa90-150f4f378896 | -14.3096 | -53.3761 | 2026-07-06 16:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 8f9c99a3-f273-32f6-9b28-621543b005e4 | -13.2783 | -54.3469 | 2026-07-06 16:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 139.3 |
| d957484a-cb5b-3a3a-a5d6-91a99675dcdd | -6.895 | -43.7066 | 2026-07-06 16:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 40cb2e3a-b7f7-3b2a-ab32-dd1e8c8718b2 | -13.278 | -54.3675 | 2026-07-06 16:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 119.0 |
| caf756da-50b7-3769-9135-eb52e41db192 | -13.2975 | -54.3448 | 2026-07-06 16:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 96.2 |
| ff10c343-556b-3062-84ba-d5c65567f8b5 | -13.2783 | -54.3469 | 2026-07-06 16:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 926adac6-9032-3721-ac0f-526eb6818ee0 | -13.2969 | -54.3861 | 2026-07-06 16:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 1a1eeba8-4aa8-32fe-be2b-1bca60d0b2e9 | -6.9138 | -43.7049 | 2026-07-06 16:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 104.0 |
| df856852-e680-3bea-b0fa-81436c47049b | -11.4139 | -46.622 | 2026-07-06 16:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| c7a89aa5-b34b-33e6-879a-ed9088b99dff | -13.2972 | -54.3655 | 2026-07-06 16:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 120.1 |
| f97280cc-f138-3fec-8e96-a79ee1d1cc1d | -13.2777 | -54.3882 | 2026-07-06 16:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 892c2588-e518-33d5-9443-221edb493c6a | -6.9138 | -43.7049 | 2026-07-06 16:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 106.1 |
| e6fb0481-06c8-3057-8f6d-e09c51598557 | -13.278 | -54.3675 | 2026-07-06 16:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 249.5 |
| 1e71fdc5-bbdc-399f-8677-c90e5013dd3e | -13.2975 | -54.3448 | 2026-07-06 16:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 87a0b67a-36c2-340d-b651-cf1f91cf9ef3 | -13.2972 | -54.3655 | 2026-07-06 16:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 136.6 |
| 6fc8c6f4-700a-3419-8acb-e77565133af9 | -13.2969 | -54.3861 | 2026-07-06 16:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 133.3 |
| 168d67e6-f19b-3427-ac38-b75f8b176d5b | -8.7294 | -54.5645 | 2026-07-06 16:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 93552978-c784-3fd6-af14-ef41524415f4 | -13.2783 | -54.3469 | 2026-07-06 16:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 158.1 |
| 6d8ec4a1-837a-3ddb-ad1d-dbda9c08a246 | -11.666 | -46.3846 | 2026-07-06 16:40:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |


