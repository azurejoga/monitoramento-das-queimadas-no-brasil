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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5826bcc4-dd87-33cd-a2ed-21ad91f4fda5 | -11.8377 | -58.8445 | 2026-08-20 14:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 5f57f96b-424f-36cd-b9ce-019da06b3ee4 | -14.5465 | -53.0317 | 2026-08-20 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| a98e3da2-754a-3d5e-b248-869e1172dd3f | -13.6044 | -51.8182 | 2026-08-20 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 146.6 |
| af1f8bf5-bb17-3f7e-b42c-f2c5f8556306 | -14.5086 | -52.9943 | 2026-08-20 14:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 97187050-71ce-3c66-bfcf-76a8a715081a | -11.2189 | -55.0585 | 2026-08-20 14:10:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 764a9b0f-6312-306c-b1ea-4b6c6ff3b5d9 | -14.3146 | -51.9183 | 2026-08-20 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 60f9819a-1630-386a-a182-5b9fb9af1e88 | -9.4257 | -60.416 | 2026-08-20 14:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| c323de46-5d80-3e2c-81ae-1301e3024996 | -6.46 | -52.75 | 2026-08-20 14:15:00 | MSG-03 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6353490b-1979-3042-97a7-f9a3cd03f43c | -6.43 | -52.74 | 2026-08-20 14:15:00 | MSG-03 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6409580-ec87-3138-945c-0c2f2df7c0dc | -7.4444 | -60.0092 | 2026-08-20 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 26818e4e-a87b-3224-bbf8-c42ebf83d172 | -5.9425 | -52.2066 | 2026-08-20 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 5ec1ea1b-3281-3b36-8aa3-142b1f53543e | -15.7151 | -47.8036 | 2026-08-20 14:20:00 | GOES-19 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 8d99a82d-a05f-34a4-8a3a-75da9fe90743 | -11.3606 | -46.381 | 2026-08-20 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 172.8 |
| 3dca8dd9-0558-3a4b-9c0f-6ec0f0d710bc | -11.2189 | -55.0585 | 2026-08-20 14:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 94.6 |
| a778f016-9d9c-3cd1-941f-49cdb6631be5 | -6.4576 | -52.7332 | 2026-08-20 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 127.6 |
| ddfca7fb-df65-3c0e-a049-6ea127253db0 | -3.5491 | -60.3203 | 2026-08-20 14:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 06a880fb-9232-3d31-b0a2-040553baa1fd | -7.7702 | -61.1634 | 2026-08-20 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 7ce08c36-ecbc-3cc7-a95a-0dd2d7d36062 | -6.7647 | -59.4601 | 2026-08-20 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 106aa106-9461-31ee-9ee6-2c929ea9d7a3 | -22.7796 | -47.509 | 2026-08-20 14:20:00 | GOES-19 | RIO DAS PEDRAS | SÃO PAULO | Brasil | 3544004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 153.9 |
| 806f48cf-dd8c-3345-9e80-e17ebc0c72c1 | -8.4742 | -46.9609 | 2026-08-20 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 109.7 |
| a9867fe6-01cd-3b21-bc6d-af750ae226a9 | -9.4256 | -60.4353 | 2026-08-20 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 126.4 |
| 20149e48-d0ff-3f7b-a3b2-ae361d40fdef | -11.1747 | -54.0216 | 2026-08-20 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 131.3 |
| 8ef7aa94-5c4a-35fb-aeb5-e1bd2ddaef43 | -14.2967 | -51.8354 | 2026-08-20 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 00df8fd1-ff47-31ad-adba-76b8f9255fba | -8.4554 | -46.9628 | 2026-08-20 14:20:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| cf97ac47-e98b-3d57-a393-b2201010e92f | -10.4085 | -61.1915 | 2026-08-20 14:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 8deb567d-b536-30bc-9579-7de1124afb69 | -6.6929 | -59.0966 | 2026-08-20 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| caf88503-b20f-3ecf-b0c8-4a0130d62170 | -11.2191 | -55.0382 | 2026-08-20 14:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 86.6 |
| ffd2e564-c98e-3ed1-8e5d-13fe96eb3fbf | -22.7788 | -47.533 | 2026-08-20 14:20:00 | GOES-19 | RIO DAS PEDRAS | SÃO PAULO | Brasil | 3544004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 191.9 |
| 349fbad4-ed98-38ca-8c63-42c5b788e904 | -5.7903 | -55.7301 | 2026-08-20 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| b513c734-bdf9-3fd3-b145-2b086b829888 | -14.1611 | -53.0377 | 2026-08-20 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 93f405a3-c33d-3a8e-99c9-0679ca7f4428 | -6.4391 | -52.7343 | 2026-08-20 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 874.8 |
| 981543a1-b1c7-3aab-b3b0-753f82a0cfff | -14.3537 | -53.0348 | 2026-08-20 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 200bb346-d479-3e57-9e51-18cfaa222583 | -11.2128 | -53.9976 | 2026-08-20 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 9d4cf331-029b-31b7-bd3e-35b94ab9c506 | -6.4392 | -52.7138 | 2026-08-20 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 489.7 |
| a5f9bc45-bb0d-3f58-8fe3-56288225efad | -11.1939 | -53.9993 | 2026-08-20 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 323.8 |
| eb0744d9-e491-3524-9d7c-299c5ab6d5ae | -9.2256 | -59.7894 | 2026-08-20 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| a5782726-2dbf-3ce7-abd2-4277b0565647 | -13.738 | -51.8651 | 2026-08-20 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 147.1 |
| d7d64c01-1533-32ab-b525-b0027514a379 | -8.2782 | -62.9086 | 2026-08-20 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 7ba3d789-4e9f-351f-af6a-f73678fb0d65 | -8.2967 | -62.9079 | 2026-08-20 14:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 2530e074-2ce1-34a6-9338-2b5c0da84f30 | -6.6142 | -45.4486 | 2026-08-20 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| b849deb1-289f-33c0-a08e-40912739b812 | -11.3797 | -46.3784 | 2026-08-20 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 202.6 |
| 79825694-d6e9-39da-98aa-d2a4996b9dfe | -11.3801 | -46.3558 | 2026-08-20 14:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| bd36d2e0-8ea9-3fc5-ae73-44458935ba16 | -11.8377 | -58.8445 | 2026-08-20 14:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 24ed8afa-bb02-3d75-adcb-4e296ef9e609 | -8.3292 | -46.5077 | 2026-08-20 14:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 134182e9-603e-3c45-83ae-63419160d9b3 | -11.9102 | -50.1663 | 2026-08-20 14:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.4 |
| b5c87ae8-9ad8-3d25-ac83-a9766b8c0233 | -9.2258 | -59.77 | 2026-08-20 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 263266c5-8a42-3e7d-99ac-47c9d3c6c98b | -14.3347 | -53.0162 | 2026-08-20 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 3a4450a2-d3a9-3b44-b2c8-cd44cefec083 | -10.3898 | -61.1925 | 2026-08-20 14:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 28dfcae5-4fc0-399a-8fe7-d188e5eaff26 | -5.7904 | -55.7103 | 2026-08-20 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 107.2 |
| b6234ed4-c711-31c5-929a-09c91f0acd77 | -14.3335 | -51.9371 | 2026-08-20 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 425a2631-73e3-3795-8be9-6d2c390642a6 | -9.2071 | -59.771 | 2026-08-20 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 132.0 |
| 48b76a54-412f-39b4-be8b-38dea29f5b60 | -6.2353 | -55.4118 | 2026-08-20 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| a311b1a2-d1de-3ec0-b63e-5d2e2e7edd63 | -6.4578 | -52.7127 | 2026-08-20 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| bd941d6f-2dff-35b6-a738-e4155a991ae6 | -9.4257 | -60.416 | 2026-08-20 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 3b41cc9f-47aa-3e05-9de5-f5048df78d07 | -11.4418 | -47.2461 | 2026-08-20 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 101.7 |
| e06058cf-2e6a-3916-a923-aad336311877 | -5.8088 | -55.7095 | 2026-08-20 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 209.0 |
| 49b7eee9-492c-3d14-a30f-f03305194122 | -5.8087 | -55.7293 | 2026-08-20 14:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 238.0 |
| 7ad08b7a-3008-3b41-993e-567f54cf4f32 | -6.8991 | -55.7176 | 2026-08-20 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 4def2833-769f-38ae-ab4c-e0acfd564775 | -6.6015 | -58.9651 | 2026-08-20 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| dab1fd68-9aef-3639-adfa-7b35a32656ef | -6.6938 | -58.942 | 2026-08-20 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.8 |
| be41c52c-2de0-37df-a8e5-0ca197a6d114 | -6.7114 | -59.0958 | 2026-08-20 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| f398f5b4-042c-36d0-a54a-2dfaa0b572cb | -10.4084 | -61.2108 | 2026-08-20 14:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 148449ec-8f74-3e8e-adf6-b21f79083252 | -13.7377 | -51.8864 | 2026-08-20 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 147.3 |
| 1f400964-77a6-37d8-82f0-17cd941861f2 | -8.9748 | -50.7232 | 2026-08-20 14:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 45b01da5-9de6-393f-9478-1686ee6ae33d | -11.3849 | -47.2312 | 2026-08-20 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| c6a8fde0-c19f-35eb-b9b1-464d71a80cbe | -9.4071 | -60.417 | 2026-08-20 14:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| db1fe872-05bb-3b5c-9201-9159cb1f377a | -13.6047 | -51.7969 | 2026-08-20 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 96.2 |
| f0c9edb0-689f-3345-9166-bd1045b4564b | -6.7123 | -58.9412 | 2026-08-20 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 577bf915-7a3b-361b-a08e-ae92bf464e32 | -9.207 | -59.7903 | 2026-08-20 14:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| c7323ff4-32f0-3d7d-b8dd-184878569c3d | -15.0164 | -52.6749 | 2026-08-20 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 92.5 |
| b245926f-1412-35b3-bebf-8c43e546a601 | -14.3532 | -51.9132 | 2026-08-20 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 55387ab6-c8fd-3e62-9ebf-81e50b44fb77 | -10.3897 | -61.2118 | 2026-08-20 14:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 156.8 |
| 5249e52e-336e-3fd6-a790-f0024e3991a2 | -10.7883 | -50.3142 | 2026-08-20 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 143.9 |
| 938c1c35-99de-393c-8852-365fb82fc6a1 | -10.8451 | -50.3081 | 2026-08-20 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 142.8 |
| e08fe2db-a9a2-3b22-b132-5ee92e632c68 | -14.5275 | -53.013 | 2026-08-20 14:20:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 74.8 |
| e6e85d19-3915-3094-956a-2959f62bc478 | -7.7703 | -61.1443 | 2026-08-20 14:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 46083ba7-3aa7-3b70-9022-d1866b595e7e | -11.1936 | -54.0199 | 2026-08-20 14:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 232.2 |
| 03e0a16c-13c2-3615-83e4-d3f908c21542 | -19.5213 | -46.6147 | 2026-08-20 14:20:00 | GOES-19 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 95075588-3c22-34e5-93c9-5bda22fd601a | -13.6044 | -51.8182 | 2026-08-20 14:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 205.4 |
| 5c935d9b-86b1-38f2-a4e2-e135b234c7be | -11.4227 | -47.2486 | 2026-08-20 14:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 202.5 |
| 88548b08-de89-3a2d-b968-8d52407e921f | -9.0349 | -45.8509 | 2026-08-20 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 75.5 |
| b840c3d8-ed54-3633-bbad-f4c6c14f1ec2 | -14.2373 | -51.9284 | 2026-08-20 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 59dd9310-5172-39bf-9316-eb82fd296812 | -15.2069 | -52.8613 | 2026-08-20 14:30:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 126.8 |
| 4c52e623-1685-3062-a341-b4ec1640b1b6 | -7.7703 | -61.1443 | 2026-08-20 14:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 145.4 |
| d8a5f095-9fc6-39fe-82b7-da56597d8c9f | -6.4391 | -52.7343 | 2026-08-20 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1044.7 |
| 9f7163d1-a765-35f8-9932-5599781667cb | -6.6142 | -45.4486 | 2026-08-20 14:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.1 |
| dc6628ac-627c-36b4-a481-be21f822d14b | -8.9748 | -50.7232 | 2026-08-20 14:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| c45ceb8b-49b5-3a31-961c-c676aeff32f0 | -14.3537 | -53.0348 | 2026-08-20 14:30:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 147.7 |
| fec3f004-6983-38e3-af6b-27f92ed90b07 | -5.8088 | -55.7095 | 2026-08-20 14:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 164.1 |
| ef67472c-b32b-3932-9dc3-ae7b2e2f7f8c | -6.7462 | -59.4608 | 2026-08-20 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 5909a4f3-4caf-3452-90c0-da0e69e91abc | -11.1936 | -54.0199 | 2026-08-20 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 236.4 |
| 17f3f860-ffab-34d8-b045-dac808c7a9e2 | -10.7883 | -50.3142 | 2026-08-20 14:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 222.8 |
| 858d27a3-c4af-3ba4-a8d9-e3630c8fe49d | -14.218 | -51.931 | 2026-08-20 14:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 9c85eb7a-8e72-3807-9f10-59cd4f254c28 | -22.7788 | -47.533 | 2026-08-20 14:30:00 | GOES-19 | RIO DAS PEDRAS | SÃO PAULO | Brasil | 3544004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 149.9 |
| 03fcebe7-b6ed-382d-92ee-f38b1503a5a6 | -10.3897 | -61.2118 | 2026-08-20 14:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 143.1 |
| 9e568736-11b8-3e1c-93eb-d9ce1f9a34e0 | -11.2191 | -55.0382 | 2026-08-20 14:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 7cbac53b-2b68-3e39-b3c9-aa1141e146e3 | -6.583 | -58.9658 | 2026-08-20 14:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 145baba9-24ee-3ef3-9aac-d2fe5e61e253 | -9.4257 | -60.416 | 2026-08-20 14:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 114.2 |
| 992f5d3a-a879-3a63-b06c-251dfe19676f | -9.207 | -59.7903 | 2026-08-20 14:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| fd35a8a7-b1ef-3699-9a46-b05961b15e4a | -11.2125 | -54.0181 | 2026-08-20 14:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 115.0 |


[Clique aqui para ver as próximas entradas](README75.md)
