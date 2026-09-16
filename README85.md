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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ed27720-c4a4-3c82-bff0-85edb6ea1f72 | -7.0242 | -59.2374 | 2026-09-16 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.4 |
| caafef89-e5b0-3a61-9059-ad94e4619577 | -9.1337 | -65.8253 | 2026-09-16 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 0bc72ad7-c1de-356b-ad2a-de422535ac49 | -9.6205 | -61.8259 | 2026-09-16 15:40:00 | GOES-19 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 52.0 |
| c99dd853-e547-3a1b-9314-c59d1c68c5d2 | -6.9871 | -59.2775 | 2026-09-16 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 46cdad16-5ac5-3b4b-9ca2-53d36cbc0ae1 | -11.9543 | -49.7728 | 2026-09-16 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 47.7 |
| 5f736248-ad50-31c6-87f9-37ca0f6bd1c3 | -8.019 | -54.8535 | 2026-09-16 15:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 17c0e7cb-0939-3559-8599-5bc72b05fc78 | -6.8042 | -58.9954 | 2026-09-16 15:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 90a27fbb-c478-3336-bd79-a36f8ab0c3a0 | -9.1725 | -59.4241 | 2026-09-16 15:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 1bd59b51-64c4-326c-a4f3-e91a78281893 | -3.1697 | -58.6437 | 2026-09-16 15:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 2149f731-00e8-3c91-96da-f51d5cc51a71 | -13.3949 | -57.0242 | 2026-09-16 15:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 7311107f-66a7-3d5f-8fd3-3da3fdd96286 | -10.3766 | -58.3171 | 2026-09-16 15:40:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 45.5 |
| d039cb25-3bfb-3455-beeb-d3f80cd12a18 | -11.7357 | -54.5227 | 2026-09-16 15:40:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 7031549d-3b7e-3fff-87e3-b51245fd8ac5 | -9.1523 | -49.9853 | 2026-09-16 15:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 3ca2a883-081d-3d6e-866b-141ba6b62694 | -9.2073 | -65.9536 | 2026-09-16 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.0 |
| aa37adee-8b26-3492-911b-70f1c1cd201a | -3.4279 | -57.9816 | 2026-09-16 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 37e38a53-8ed0-3bb0-89d0-984199450949 | -3.1514 | -58.644 | 2026-09-16 15:50:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 83.7 |
| fc280259-7784-30fd-ae41-78937d48f78f | 2.2186 | -50.9393 | 2026-09-16 15:50:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 9b93596f-bfcc-3f58-a757-517d8102a21e | -10.7839 | -50.6346 | 2026-09-16 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 2bed7da7-0c12-322b-b144-be52f7e4a78e | -11.268 | -54.1156 | 2026-09-16 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 8667f52e-f128-3ccd-a856-6c64f11f0a94 | -11.2491 | -54.1173 | 2026-09-16 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| fbf627f7-cac6-3307-9f0d-c500e80807e4 | -11.2002 | -55.0398 | 2026-09-16 15:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 43.0 |
| dd68050a-ec60-33b8-bc47-4ce50b3609fc | -7.0058 | -59.2382 | 2026-09-16 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 89b21cd0-eab1-33b3-9e8d-5c0cc35c0c59 | -13.4506 | -51.8374 | 2026-09-16 15:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 91bdc3b4-aeb6-34a9-90c5-60e579d96bf1 | -9.0407 | -65.9215 | 2026-09-16 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 38f214ae-9ae3-3729-8f04-ce02bd02fd95 | -8.9239 | -63.3371 | 2026-09-16 15:50:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 2b224113-f9d1-33e1-aec7-23983da670c8 | -6.6952 | -58.7097 | 2026-09-16 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 17098dfd-88bd-33a9-ba8b-c7d76b016760 | -9.1708 | -59.6568 | 2026-09-16 15:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 741df52a-2d85-347a-8f26-e69195c0a306 | -7.614 | -67.2387 | 2026-09-16 15:50:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| c7c6c871-81ca-3fda-a690-6b74f3d063fa | -12.12 | -57.1967 | 2026-09-16 15:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 90.7 |
| f0a41107-adc5-30c3-a725-f39a6143ba8a | -9.3765 | -50.0925 | 2026-09-16 15:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 656e3efa-dca6-3961-9438-ab85ac717f2b | 2.2186 | -50.9185 | 2026-09-16 15:50:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 969712fc-b39c-35d2-a06c-d2cf96afa9ad | -9.3569 | -50.1583 | 2026-09-16 15:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 5787be52-2fed-384f-8554-36ac3c9278f7 | -13.3387 | -51.6389 | 2026-09-16 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 66096784-efc2-3638-9be2-1380c99bc515 | -10.2513 | -57.6952 | 2026-09-16 15:50:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 46.0 |
| c4646e0b-6387-36ae-8147-011fd5393be7 | -9.3763 | -50.1139 | 2026-09-16 15:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 106.4 |
| 6b6c24c4-28ab-3c78-9077-3d285ebbbf93 | -6.8226 | -58.9947 | 2026-09-16 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 2faa6e17-7230-3e25-bae8-19445eb6c449 | -8.5428 | -44.5132 | 2026-09-16 15:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 606.0 |
| b879fc9f-4df6-3989-9a4d-d5317eae0693 | -7.0242 | -59.2374 | 2026-09-16 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| cc528408-cc43-3f5f-ba12-71598c952b7d | -9.3567 | -50.1796 | 2026-09-16 15:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 125.7 |
| cef673cc-9d9f-3a02-9d15-86131805634b | -10.7842 | -50.6133 | 2026-09-16 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.7 |
| fb829221-65da-3e6c-b00e-57850a715e2d | 2.2002 | -50.9189 | 2026-09-16 15:50:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 79.8 |
| ea698cc0-6962-3235-9dd3-afcedcae06d6 | -9.3575 | -50.1156 | 2026-09-16 15:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 72de2599-6ebd-3896-80f2-4b90c318581e | -3.3367 | -57.8673 | 2026-09-16 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| d6b5c7ab-9d50-3d36-be31-52f4fe2f2bd1 | -9.7608 | -60.4561 | 2026-09-16 15:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 41.1 |
| 3bfac55e-e7e5-3dee-b68f-9a21ee9fffb3 | -8.7685 | -61.407 | 2026-09-16 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 45.5 |
| c9553678-45c6-3d96-94c8-c665bb5fa391 | 2.2187 | -50.8977 | 2026-09-16 15:50:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 95569d98-81cb-332a-bdb7-cfde862a9d43 | -8.6311 | -66.5287 | 2026-09-16 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| af041fdd-cb20-36a9-a2ff-e215b9e570d6 | -9.7979 | -60.4734 | 2026-09-16 15:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| f648fb05-3a63-349a-bad4-396e1499b572 | -8.6188 | -44.4819 | 2026-09-16 15:50:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 149.1 |
| 8c313198-af71-3c0e-b2ca-7b7cc9ed5128 | -3.4462 | -57.9812 | 2026-09-16 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 91438f79-26f4-3db9-880a-bb21211f8228 | -9.3577 | -50.0943 | 2026-09-16 15:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| acfe98ed-a036-3a7c-af5e-7cef382e82ac | -9.2072 | -65.9723 | 2026-09-16 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 05c79037-ff95-3bc7-8d5f-aff5322ad5fe | -12.1265 | -44.199 | 2026-09-16 15:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 139.9 |
| d5b053c4-e3e2-3dd0-aabf-b416613bf7b3 | -1.861 | -54.4315 | 2026-09-16 15:50:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| efaadc8a-c23d-38bb-a39c-8f97ffd634c6 | -9.4139 | -50.1103 | 2026-09-16 15:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| a94b0a48-a559-36b6-9fb8-17a462d87de7 | -7.7993 | -66.9018 | 2026-09-16 15:50:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 3026e2fc-76ed-309a-88eb-0628e96e2618 | -13.3761 | -51.698 | 2026-09-16 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 4f9f998e-334d-3fc5-9d70-87fc46687542 | -11.2693 | -54.0129 | 2026-09-16 15:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 60.1 |
| a8868764-9cbc-35e4-bd1f-405c16e36863 | -2.6602 | -57.5119 | 2026-09-16 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| d777ad30-b036-3ee4-9d28-1caac95fc8c5 | -12.1389 | -57.1951 | 2026-09-16 15:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| a9a0d4de-6304-3d94-bba6-463ef110bd7f | 1.1136 | -50.9361 | 2026-09-16 15:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 6454e27e-0cdb-3ed2-8a4f-07cd6b079ff6 | -10.5535 | -57.4567 | 2026-09-16 15:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 7c2d7335-8dd2-376a-bf00-6d20915833d1 | -10.6417 | -46.0906 | 2026-09-16 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 330.9 |
| 80833255-c5c1-3736-b323-827b13788ceb | -10.7463 | -50.6172 | 2026-09-16 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 72.6 |
| f4495acd-a0c1-35dc-966e-5d219cc5ff85 | -9.4078 | -60.3205 | 2026-09-16 15:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 555d5d24-9679-3bf6-98a8-b627d6e53cc1 | -6.6021 | -58.849 | 2026-09-16 15:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 8d886750-ab3d-309c-975f-08c1b06df3a5 | -10.8028 | -50.6326 | 2026-09-16 15:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 7babc8a3-13fa-30d4-a7c4-2e8ca93da475 | 1.0767 | -50.9572 | 2026-09-16 15:50:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 22d534f2-c2c7-30f5-be02-beb013b2d80e | 4.1499 | -61.2374 | 2026-09-16 15:50:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 81.2 |
| dde899fc-dc99-3554-85c4-6211770cb239 | -10.8114 | -46.182 | 2026-09-16 15:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 132.2 |
| 32d65b80-6b70-3ec2-9aaa-847fe7e48e2c | -12.1453 | -44.2195 | 2026-09-16 15:50:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 85c3d26b-6555-3f2d-961c-c8f2e72a5072 | -9.1337 | -65.844 | 2026-09-16 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 125.0 |
| 3f0fe584-0c09-3776-b8e7-a4a562bf8ece | -9.7793 | -60.4744 | 2026-09-16 15:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 5b9ae9bc-28f3-3742-b8e9-07e8205d6494 | -6.9871 | -59.2775 | 2026-09-16 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 7f4b6551-5cc8-3f5e-afd3-0bff6d9d47fe | -9.1725 | -59.4241 | 2026-09-16 15:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| c847ed60-30d7-338c-8a19-86002d6d3e57 | -6.9872 | -59.2582 | 2026-09-16 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.1 |
| dd87ffd0-0e31-3f35-95c4-b3974b7e06dc | -13.3199 | -51.62 | 2026-09-16 15:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.5 |
| f22adb7f-60ce-33f2-a598-f1529ecd0b97 | -2.7149 | -57.5886 | 2026-09-16 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| c783417d-3b13-34ec-a816-8b8c0baf2afd | -9.4325 | -50.1299 | 2026-09-16 15:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 00db797e-2076-314c-94b2-ab13ed5909b5 | -1.861 | -54.4115 | 2026-09-16 15:50:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 1ca06771-d1b9-3c19-8cad-43cc7885cd41 | -6.2731 | -55.2904 | 2026-09-16 15:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 8f85f989-398a-3a1c-89c7-cb60e7dc7875 | -7.0428 | -59.2173 | 2026-09-16 15:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 12f0a737-a5f1-3a68-9c68-298c78daac77 | -8.8456 | -45.8939 | 2026-09-16 15:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 348.6 |
| efdbe386-90cd-3e5c-8508-24bd1402b1c3 | -11.2302 | -54.119 | 2026-09-16 15:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| d0f4bcdd-73ff-3462-8baf-9aa1f6785b27 | -11.7357 | -54.5227 | 2026-09-16 15:50:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 78727474-5454-351c-836b-1c3986a689a6 | -9.6205 | -61.8259 | 2026-09-16 15:50:00 | GOES-19 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 49.2 |
| d32e5981-54da-397a-ba8b-974f2027473d | -6.1362 | -59.8871 | 2026-09-16 15:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 8c89017b-f572-37fb-a048-cc45edca1bfe | -0.821 | -49.1304 | 2026-09-16 15:50:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 3e966265-2a7b-38db-bfdb-baeef4882af8 | -13.3949 | -57.0242 | 2026-09-16 15:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 69a90735-9eab-31a7-8999-f737ad1e5407 | -8.6493 | -66.5839 | 2026-09-16 15:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.5 |
| cbf9bed6-3a89-3a51-a9ba-f2509284c461 | -2.7148 | -57.6274 | 2026-09-16 15:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 8069ef18-10eb-3efe-806a-6cc1a5de70e3 | -13.414 | -57.0225 | 2026-09-16 16:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 9c910f6f-37ec-3a1e-afd7-097596cc5f74 | -10.5535 | -57.4567 | 2026-09-16 16:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| b6c2f4d7-1cb7-342f-8427-f2f6ba29a132 | -11.7357 | -54.5227 | 2026-09-16 16:00:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 1086feac-a708-3b99-8b5c-f2077c75f316 | -12.1197 | -57.2167 | 2026-09-16 16:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 43.2 |
| c7b3a887-0ead-3625-a6f3-e9e619810a1f | -6.3014 | -59.9579 | 2026-09-16 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 100.8 |
| bfd23c91-dc66-351e-9084-3cacb4d2e704 | -13.3949 | -57.0242 | 2026-09-16 16:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 8763cbab-e165-3861-b599-04a3a89ffa77 | -8.5989 | -44.5531 | 2026-09-16 16:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 174.1 |
| d2282cb9-c50f-3b78-8d2d-986f85c0b2de | -12.1453 | -44.2195 | 2026-09-16 16:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 2bd38748-96e9-3a9a-be82-af5d3d22f72e | -12.12 | -57.1967 | 2026-09-16 16:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 159.0 |


[Clique aqui para ver as próximas entradas](README86.md)
