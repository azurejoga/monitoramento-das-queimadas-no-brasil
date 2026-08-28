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

## Dados Diários - Página 118

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4f935a8c-7ff1-39fa-b747-c93cee48bbca | -8.597 | -54.8311 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e44de3b9-97e3-3476-8a46-f883f3475298 | -9.42116 | -50.43628 | 2026-08-28 17:28:00 | NPP-375 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 142.3 |
| eb626644-f172-3b8d-a989-a5ebdd8f9660 | -9.23101 | -51.53219 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 1115d759-28a0-343d-9637-3d790600f94d | -6.54343 | -55.24582 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 64f74650-a367-3677-9149-5215300bc9da | -6.67291 | -59.07393 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| a65a6cf1-f229-3c69-a333-42c8b602fc30 | -11.42729 | -61.42653 | 2026-08-28 17:28:00 | NPP-375 | CACOAL | RONDÔNIA | Brasil | 1100049 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 82de2bb1-8df5-39b7-b79b-42325f09d6cc | -7.61623 | -61.34055 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 904c4f60-048b-3e7d-a8bd-a50f246c3f0a | -4.97668 | -56.29457 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a2a0148c-c667-3330-9354-0c1c54a761a7 | -5.80831 | -57.63377 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ceb1fc24-e5a9-35e3-86b0-118b8d4d86d9 | -7.5539 | -57.73178 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 014f2443-06bb-3bcb-b294-317c5b2b9745 | -9.15526 | -49.97281 | 2026-08-28 17:28:00 | NPP-375 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 59b6aa1b-c681-3f7f-a173-51fa5d8181ba | -3.94099 | -54.83804 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 64759a62-2c91-3af6-a887-9031d2d68d00 | -7.92625 | -61.36707 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 5c841232-c374-3247-8a7d-7f56765e6fb6 | -8.02113 | -51.80948 | 2026-08-28 17:28:00 | NPP-375 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8fc0472d-b6ab-3491-ae04-3f6a358c47b4 | -7.59718 | -61.3485 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 4cebc5e9-67d0-3b83-9486-2211ed6bdff1 | -7.5578 | -57.73483 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9384a7f5-4f52-3a33-8bc3-d45974b82379 | -6.40797 | -51.67732 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 74e71cf6-fb34-3b2f-9b9f-ee7a5490432f | -10.27577 | -64.49774 | 2026-08-28 17:28:00 | NPP-375 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 6622063a-428f-32ff-b1f1-3b8cdc5c4496 | -8.93519 | -62.40075 | 2026-08-28 17:28:00 | NPP-375 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 660ff85f-53cd-3cbc-aa93-84f908148b18 | -7.48578 | -61.40837 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 62723dff-2bd3-3afb-b245-e0db9294876e | -6.26473 | -53.34065 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4654bb90-210d-3891-b94a-36617b8576dd | -7.57919 | -61.39256 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8eebe252-9dfd-33cf-802f-0f7d2f60caed | -9.08258 | -50.60011 | 2026-08-28 17:28:00 | NPP-375 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2c6499df-af9a-3cf8-a91a-84b25b626d41 | -6.65066 | -58.4976 | 2026-08-28 17:28:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 82ebf0d9-0e26-39ce-afe5-57b07517c0f0 | -10.49885 | -64.49545 | 2026-08-28 17:28:00 | NPP-375 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 5fee5291-3b0b-308b-a553-ba515181e55e | -7.56712 | -61.19451 | 2026-08-28 17:28:00 | NPP-375 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7b69a527-e4b1-3755-bb2c-92f10fe2619e | -8.67023 | -49.53347 | 2026-08-28 17:28:00 | NPP-375 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 033a60ee-6da8-3b31-a676-614cce28c752 | -7.7827 | -61.1134 | 2026-08-28 17:28:00 | NPP-375 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 23df2fa4-5989-3149-abf9-54ef35d295ac | -6.03818 | -57.8131 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 2b95500a-071b-3554-ac1b-af814b5fd34d | -6.27427 | -53.13667 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| f64f42a5-99bf-3879-abcb-a6166c6126c9 | -10.35522 | -53.88312 | 2026-08-28 17:28:00 | NPP-375 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| d3f66543-9863-3527-a6b6-c7f7eeb35496 | -6.32812 | -57.7462 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 9667f398-b8c8-39c5-bf1e-080db2b15810 | -8.77491 | -49.95438 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 626fa5a9-986d-30c2-9308-ec468c36d8ce | -9.35988 | -70.44489 | 2026-08-28 17:28:00 | NPP-375 | SANTA ROSA DO PURUS | ACRE | Brasil | 1200435 | 12 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 25c8c323-9792-3dc1-82d6-3d2f7bd0f760 | -9.23243 | -57.07753 | 2026-08-28 17:28:00 | NPP-375 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d010bf5e-074c-3437-977c-8bc5f2e505de | -5.43497 | -49.17775 | 2026-08-28 17:28:00 | NPP-375 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1031dc84-52e4-3061-8092-9ee7bcd8e6a3 | -8.11365 | -45.47334 | 2026-08-28 17:28:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 79db2693-9150-34ff-89eb-5861f973e1a1 | -6.20876 | -57.7608 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| 5b17821c-fc5d-39c9-886d-94b8bfbb8c64 | -9.22306 | -59.76802 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 0ab397ac-774a-3260-9ab8-c798a91a64f2 | -5.81729 | -52.35508 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 63159c3c-18cd-3eda-8921-fa5497e6d439 | -6.75233 | -55.68813 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| c2b65662-7a5d-3206-b17d-5e0dafd823de | -6.75495 | -59.14761 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6926e894-cdbc-37aa-8d30-a95dcfd542bf | -6.58522 | -55.44513 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 50a11d22-d253-3576-b43e-e61a72b98b37 | -6.81311 | -59.71074 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| c575ee90-3ff2-3fca-956f-ba0b68530602 | -6.94517 | -58.95153 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 18.3 |
| d703a8c1-75b2-3e35-988d-e6be53820571 | -8.82208 | -68.96395 | 2026-08-28 17:28:00 | NPP-375 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 6266e830-f3eb-3199-a469-5ea59bac3d3d | -6.25508 | -55.40819 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f33227fd-1c11-33ae-9664-16545dc621d8 | -6.26759 | -53.11905 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 78d5a842-5f2d-31d8-a0a8-5ecc0188b098 | -7.99962 | -61.41155 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 2bb70a28-6cf4-3df4-b618-cda3e9e99a29 | -4.9022 | -56.26695 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ea3d7614-c345-3551-b45d-b40c70e736c0 | -10.7619 | -54.04369 | 2026-08-28 17:28:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 141be85b-9f96-3351-8e56-6e04861d8d7e | -6.56141 | -56.53098 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7387aae3-d69c-3a81-bf54-43808df783ab | -10.4714 | -64.48386 | 2026-08-28 17:28:00 | NPP-375 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 5b186134-936f-3720-97c7-5de996500eef | -7.60978 | -61.35184 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 34.4 |
| a2070436-1242-30fb-a4fd-4b4aba5201ad | -6.94905 | -59.48203 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.2 |
| 739290e9-e559-31ba-b56e-406cbde2ed67 | -6.90949 | -59.63121 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d85a38ed-1357-3344-85bb-919113a23dd6 | -7.93065 | -70.66131 | 2026-08-28 17:28:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 50.0 |
| a5a4c250-b342-3a57-b3c2-2530134bcc62 | -8.43563 | -70.69709 | 2026-08-28 17:28:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 725d8cac-997d-321c-9c44-9384b2577f55 | -6.5241 | -55.25636 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 96942bda-98b8-3462-a305-b8eb90aec23c | -7.58638 | -61.3294 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 3e13e91d-fb88-3cda-83ce-5fb895e25611 | -8.76767 | -50.49712 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 26a30093-47ee-3a08-9c83-c76ed7306239 | -9.28028 | -65.5498 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4fb0781b-a7a3-3924-954e-d03054761c61 | -10.58287 | -63.54279 | 2026-08-28 17:28:00 | NPP-375 | GOVERNADOR JORGE TEIXEIRA | RONDÔNIA | Brasil | 1101005 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 62811a4f-3c85-3eeb-ac53-bd58287a850c | -6.03551 | -57.79554 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8c9cc1c6-0c19-36fd-8061-2f7d68c3c7e2 | -7.69584 | -55.36401 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 81efa339-0c3d-3e6e-aeb9-32328608af91 | -5.79884 | -57.63879 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a99790f4-e833-3601-8bb0-b1038fd1476f | -5.14402 | -56.27617 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ad25b888-c450-36bb-8e04-47a1cec03a9d | -6.78015 | -59.43797 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7614b30c-6b21-3920-903c-6bb6490a4dc0 | -8.83472 | -62.32159 | 2026-08-28 17:28:00 | NPP-375 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c1431f37-316a-3c67-896e-01924c53f153 | -6.73983 | -59.64713 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 91df28f9-5873-3e2a-b84b-d0acd3ddd3cd | -8.60313 | -54.78083 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| bc197142-de1d-3fa6-9e60-df22899ddc0c | -10.27946 | -68.86298 | 2026-08-28 17:28:00 | NPP-375 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 85e68eaa-9ac7-3aba-af0f-a2ba435ada87 | -8.19093 | -54.95691 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e01efa2b-b3b3-3274-ac7b-b06c04126391 | -9.22243 | -59.76368 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 31924ebb-3090-3e29-8caf-2d17be4f466b | -7.58028 | -61.31489 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3df380a9-eda2-306e-974f-870b90ff3bf6 | -6.76864 | -55.68196 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9daab909-0383-39e8-9c6a-e40c17b00315 | -5.82085 | -57.63527 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7719d772-c6c8-3ed2-a8b5-387669073a53 | -6.73686 | -59.65165 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 12464785-2686-3c61-8680-ef06ed3be910 | -6.14106 | -53.51532 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a8c8fa34-f031-3167-a326-65efbbdc2596 | -6.9482 | -59.48227 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 521d9b1e-f8b9-3636-b473-48c52fa9406d | -6.21346 | -55.47847 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 1dffd6e5-6f05-3de2-b711-426f5055b5fb | -7.50529 | -55.27964 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 1b2b4c54-5055-3b49-a112-7227fe34be2d | -8.04896 | -45.86158 | 2026-08-28 17:28:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| efbd9fb9-a05f-348b-98a3-58c799f970e1 | -9.38918 | -66.51353 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 7cb3f657-f60a-3693-86b4-9e79eb20b49c | -6.94965 | -59.486 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.8 |
| 20f6408f-28a8-3dda-81c6-c5fd765d9c36 | -7.04851 | -56.53559 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 317d240b-122b-353f-8a11-aa2b1a67806a | -6.26956 | -53.39423 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8178e7e4-a9e0-3061-9131-3a2c7c42de8d | -4.17509 | -55.44279 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c7ea4e86-13ff-354b-806b-047c9b87f08d | -9.13673 | -59.40291 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fb1bc686-fa18-3830-922d-4af6ab840350 | -6.79525 | -59.71347 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 0f3c9aa9-ea6d-3a74-8a22-114f7ce274a0 | -7.60222 | -63.37317 | 2026-08-28 17:28:00 | NPP-375 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 79d16c3c-84d2-3a64-bd19-43e5e300fa4d | -8.5923 | -54.77874 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| cc4b2ae3-69db-3b6f-a2e0-7d63dc8a25bb | -9.22674 | -59.76748 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 2a14fb4d-57a0-37c8-b6fe-3793ef4068c7 | -9.91799 | -60.43805 | 2026-08-28 17:28:00 | NPP-375 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 0b243a4b-a766-344d-93af-6482974a423b | -7.69922 | -55.36347 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 17db74f9-5c6b-3b87-8e46-5cb0787a4a4d | -5.98459 | -57.75302 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d50122f3-3dc7-304e-a569-26a0814de3a9 | -5.97164 | -61.46424 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 25.4 |
| dc4cac85-6a2f-3727-9abb-9aa9c06d5073 | -2.99475 | -48.95033 | 2026-08-28 17:28:00 | NPP-375 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| af963df7-2122-38fc-bbfc-45f1b7a97824 | -3.53344 | -44.31833 | 2026-08-28 17:28:00 | NPP-375 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 411263db-e864-3209-a837-b2f604454b5a | -5.81633 | -52.32375 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |


[Clique aqui para ver as próximas entradas](README119.md)
