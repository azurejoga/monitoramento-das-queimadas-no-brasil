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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7cfd4d93-f041-3810-a09f-68311b2f0fbe | -6.63778 | -58.49707 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b34a76ef-5ba2-3680-ad3d-d1c9a3690205 | -7.38753 | -55.18501 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8db7d329-0b84-3329-aaad-8bffd1289eea | -10.77401 | -50.92711 | 2026-08-25 05:48:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 32.9 |
| a965d787-5c41-3c69-9675-a7262d416730 | -6.22408 | -55.92479 | 2026-08-25 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88ae7cd0-4eca-3a80-8107-74fef0a7de60 | -7.43497 | -59.77949 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7962a27-e19b-3c20-a903-4742dfa0e685 | -6.80334 | -59.59861 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2f67da03-8806-307f-a2dd-c154453cb2e3 | -6.13442 | -57.85366 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ff4b9d0c-324c-38db-b098-67a7ec912235 | -6.18317 | -53.48996 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2381a40-ae13-3532-ae2a-47469d5d34a3 | -6.98794 | -59.24335 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 26f1260f-33f9-3f66-8cd8-b9fe954c2715 | -6.1812 | -55.43935 | 2026-08-25 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 514c5392-db49-3621-b2a1-0abd57cd4bfa | -6.79237 | -59.64612 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b190582c-3b08-3cb7-a2b1-c39b7190e923 | -8.56813 | -63.0254 | 2026-08-25 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33515354-5de3-309a-9513-81e12c476c54 | -6.85636 | -59.40198 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 68366b43-c6d8-3290-88cd-5f8ab2a77de1 | -6.7263 | -59.44631 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a77d9317-a4f2-386e-96c8-6c5fd1fb087f | -11.16263 | -54.00362 | 2026-08-25 05:48:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c5dc44b-ed84-37b5-9814-81090d4fd136 | -7.32318 | -64.69756 | 2026-08-25 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| af28d246-325c-3f83-9f89-f9a79d6b9b4c | -5.77998 | -57.55468 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70312a60-8285-3596-a0a0-739ef00cd116 | -6.3471 | -54.7697 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bc9cbf9a-6562-376b-bd6d-b0c58e452f2d | -6.95668 | -59.08423 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25802a87-7604-37be-8e72-38a0ab3fe7af | -5.78244 | -57.56789 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bfaf2c59-a408-3052-85ce-0fe7ad732dd7 | -6.25481 | -55.42062 | 2026-08-25 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d96fe2ee-ec83-32b4-9fef-db0b0a172a5c | -6.4406 | -54.97416 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 671b7591-78b3-3025-9ba2-05ca3681c276 | -5.77626 | -57.54982 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| da9cf4bd-9439-3723-b438-6aeaedb0fe04 | -6.72168 | -59.4506 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 388edc46-b057-3fb3-b690-95a274b2d5f7 | -6.32812 | -54.74987 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e67425be-f846-36bb-8621-e5f348e33869 | -5.78637 | -57.60488 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ba0e630-c4b9-3518-ba5c-71f44c69ac9d | -6.80595 | -59.68736 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9e1377a6-9b92-3bcc-a0ea-9f1bd22c73d7 | -8.5982 | -54.73988 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| acbc281f-e29b-32f4-a65c-45bb519ba7d9 | -6.33159 | -54.764 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e590102c-cfa2-32d4-b7d1-a91a3bd997a3 | -6.14756 | -57.70516 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6744601a-eec8-36ec-b9dd-4b8f174e4592 | -6.80263 | -59.60341 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a55f3438-f954-35a1-aa01-0a82fcdcbd07 | -6.61415 | -58.38651 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 85d1139d-e6ae-3438-8cc2-d251ab6b9569 | -9.16287 | -59.40231 | 2026-08-25 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75cce0e3-a472-3eec-b6de-1544ac9e2def | -6.82251 | -58.64877 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a20db39-11ea-3608-99d2-4e93f460e0a7 | -7.29364 | -60.67827 | 2026-08-25 05:48:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8ebce345-9340-355f-90cf-180d3f037289 | -6.6331 | -58.50015 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| a419a8c9-911c-3278-8b69-81e790fc7e46 | -8.56757 | -63.02901 | 2026-08-25 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fcbec9d-732e-3322-9714-3915076a0d60 | -9.16391 | -59.39524 | 2026-08-25 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 621641dc-0aa3-3a6e-85e2-1a1f550efde0 | -8.57245 | -55.28045 | 2026-08-25 05:48:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 96b054c4-954b-381d-8509-48ddaa6717b7 | -6.54189 | -55.08997 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63315033-4998-39ec-bf73-fba47ec1b8f0 | -10.78598 | -50.92329 | 2026-08-25 05:48:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 21.1 |
| ba890273-e2c2-31f5-b241-09c36251bb19 | -5.78549 | -57.60644 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 229c5275-9380-3eb3-930f-09703533770a | -9.20439 | -59.57117 | 2026-08-25 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2dddaafa-b7f6-3bbf-b686-8d96a2ad2cb5 | -7.43569 | -59.77465 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc5b7ee2-03d5-3e67-bc5c-d796ebe7c954 | -8.17445 | -54.96855 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67cf5e2c-e23d-36b0-9932-1ac2975d809d | -6.35542 | -54.78767 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fadaea9a-0e7c-340f-b25d-1325aeca5551 | -5.775 | -57.55818 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8fd6d5e8-4b29-36f3-a01a-953087e9187f | -7.00301 | -59.251 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 7c9cc21f-e357-3fca-b18a-0da045c5a7b5 | -6.83428 | -52.50759 | 2026-08-25 05:48:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 390f8871-b914-3d24-bba3-d3205828594b | -6.79624 | -59.64666 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0347067a-5d0e-31bd-8cea-3a26f0bac814 | -6.8181 | -59.60574 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea181a8f-b2b3-3823-8376-8dbbf756bd44 | -6.80404 | -59.40759 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3df27db-aaac-3f1d-8c77-3db68007881f | -10.80034 | -50.92502 | 2026-08-25 05:48:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 6a65479b-b6c9-33c9-b1c8-995c1167c1ab | -7.38312 | -55.17819 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eea5f7d2-969d-3f18-a26c-9e353f3bcf1f | -7.01094 | -59.2522 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e50d8773-5bbd-3bb2-a157-d18c8839f087 | -6.81951 | -59.59624 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52111837-03cc-3789-83e3-608a10da5846 | -6.14761 | -59.91643 | 2026-08-25 05:48:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ba86831-7b01-3dc7-aac9-c39ef8f139c7 | -6.68693 | -58.72504 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c763d7b4-e331-3f18-98b8-12350c3f98c3 | -6.00956 | -57.66944 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 210ab551-bbbf-3b73-ae7b-7aa1e891361e | -6.96869 | -59.08604 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d57d6af1-49c3-3455-bdb4-87b1610a53e1 | -6.43533 | -54.97347 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f0724db-4da3-316a-ac44-6e236a596831 | -7.21287 | -60.62418 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea34f11b-0b10-36cb-9667-376c297345c8 | -6.80014 | -59.40696 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f839ed0-3a20-3e66-9ba4-6f2fc8313411 | -9.03263 | -50.81276 | 2026-08-25 05:48:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 28579c79-69ff-3ada-bf0b-a58f16d05886 | -10.7804 | -50.93514 | 2026-08-25 05:48:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 8d6d71e8-74f1-3bbc-a9c8-a320b12c914e | -6.54144 | -55.09315 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6dfdf1a-7300-3c6f-bdb3-145292f0b6e1 | -6.80018 | -59.59317 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a42c5333-dbed-340c-baf9-54a9eaefb3cb | -6.24336 | -55.42807 | 2026-08-25 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a9e9a69-8073-34c8-b0cb-8aa715528254 | -6.14749 | -57.94189 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2a11eb25-8733-3d22-afe5-b95d53235b6b | -7.01246 | -59.24204 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3de10ada-92d6-37a0-8d6d-917752d834a1 | -6.89135 | -59.02738 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5b1c9f94-0959-37ed-9c50-19867f6b0a17 | -6.36453 | -54.76183 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc4b4828-81cc-3242-b961-0b6cb688e208 | -8.16908 | -54.9676 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2087256a-9e7e-3382-807b-59daf8b5b42e | -7.2092 | -60.62364 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e09923c5-3a2f-33db-a35c-3bc2174e02e6 | -7.54021 | -61.36322 | 2026-08-25 05:48:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f9300345-0771-33cf-bdde-e7818ebdc29d | -9.16745 | -59.39935 | 2026-08-25 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ef07be4-71f4-38d8-9b11-ff519b620d92 | -10.42577 | -61.2263 | 2026-08-25 05:48:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5e3ed24-108b-3080-a2f3-e515f74f1ee4 | -6.43672 | -54.96371 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6584f2aa-e967-3a87-97be-2f8ea1fd9844 | -6.86345 | -59.40814 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 05643a5a-f8ef-3960-a141-bd26a6e5de6d | -7.49523 | -55.3707 | 2026-08-25 05:48:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac5611e8-7add-3c2d-b932-bab3c28c3ef6 | -5.78245 | -57.57037 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f91c2181-de97-3415-81f1-4ff7f56916e6 | -6.99433 | -59.2549 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.7 |
| f6a00aba-fee4-3593-971b-708bc89d439c | -6.1394 | -59.91982 | 2026-08-25 05:48:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da252bd1-9f8f-3206-a7cb-ed72f19fe635 | -9.15085 | -59.56713 | 2026-08-25 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ede9ed4e-5bb1-3887-9305-1cab3498fc86 | -6.79308 | -59.64132 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 844dfdbd-ef59-3f1b-aee5-837703fd02ae | -6.14809 | -57.93787 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bef341cc-ebf0-3b11-9863-fb556a2aedea | -6.95746 | -59.07905 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d23e5cf6-1c01-39a6-ae38-a63a2c4deaa7 | -6.14323 | -57.70446 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6e247dcc-d49b-30e2-8dbc-116275a81165 | -6.26029 | -55.41858 | 2026-08-25 05:48:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41537a01-81f9-33e5-b9f1-065b424355ea | -8.66595 | -62.84355 | 2026-08-25 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d143817-78b7-35f7-84a4-cdeb11a568db | -9.05898 | -60.43402 | 2026-08-25 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| acab79c8-1537-3342-9163-817708531e1d | -6.6295 | -58.49579 | 2026-08-25 05:48:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 9900e63c-bedc-3192-8cdd-39a72ff01adc | -6.12632 | -57.81927 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 8d1a0ac0-a370-3d89-af32-fa5711aa58b8 | -8.56531 | -63.02127 | 2026-08-25 05:48:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bd487917-f606-3a32-9d53-881c474fa48f | -7.49694 | -55.35807 | 2026-08-25 05:48:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5bf5e15-18c9-3ffc-8833-0f72b991d682 | -10.80118 | -50.91794 | 2026-08-25 05:48:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 17.1 |
| df6f4724-2c40-3ae4-9820-36cdc8f530aa | -6.84754 | -59.46123 | 2026-08-25 05:48:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 331766fb-12c8-3736-ba84-9893bb763d65 | -8.60325 | -54.74409 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5c02989-896a-3e88-a7d3-ef18b17191c3 | -6.15115 | -57.94656 | 2026-08-25 05:48:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 823881c6-c0ce-390e-9cfe-8b5b2e368ec9 | -6.34663 | -54.77304 | 2026-08-25 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README63.md)
