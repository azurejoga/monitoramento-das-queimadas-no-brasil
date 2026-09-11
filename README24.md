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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9689b47-ec25-3428-aeb8-1c87c9942489 | -3.70894 | -58.87166 | 2026-09-11 05:27:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b7f10f03-dbb9-3d1b-a962-5e203e183e9b | -3.38052 | -50.762 | 2026-09-11 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e6c1685-bb13-3841-9443-722027d91d2a | -1.77544 | -54.94396 | 2026-09-11 05:27:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 49b3707c-bad0-3d98-bfb7-21d9da6285bf | -2.72474 | -57.63272 | 2026-09-11 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1d9da4f-b270-3071-9740-c4260b60b079 | -3.09558 | -51.2883 | 2026-09-11 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63910d0a-70c9-388d-badf-c564e25396d3 | -8.39172 | -46.30114 | 2026-09-11 05:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c54f5c3c-791b-32e9-90d0-264901bd7751 | -2.71859 | -57.60687 | 2026-09-11 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 767c021f-399d-3d8c-8d62-7ac6e448decc | -4.35856 | -54.77203 | 2026-09-11 05:27:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9eefb24-498a-3719-a5c3-0637ccddbfdb | -6.12616 | -45.11549 | 2026-09-11 05:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 622a89f9-4b39-390a-a9d2-8ce50744f524 | -2.73971 | -57.6244 | 2026-09-11 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c085af0c-e4b5-3898-9740-6dd857cc1ae7 | -6.40545 | -54.97336 | 2026-09-11 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52d2662e-7923-332b-b117-9b2a5556af65 | -4.52312 | -54.95756 | 2026-09-11 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8bdeb4a-a15c-3992-96bb-198145ca7fa9 | -6.20129 | -55.27507 | 2026-09-11 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74f995db-258c-3f5d-8f1b-6cf7160528ba | -2.72415 | -57.61486 | 2026-09-11 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dff8ac8a-1205-3323-86c2-db72557d675e | -6.83919 | -59.35836 | 2026-09-11 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 44d979ce-6279-3370-83f6-0bf2f6a9bb25 | -3.24621 | -50.81839 | 2026-09-11 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a8eabb31-da1f-31b1-968d-b4e5a4818cc3 | -6.83974 | -59.35489 | 2026-09-11 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 435c0c85-3e43-317f-8f70-6a3a56fe38ba | -2.72529 | -57.62926 | 2026-09-11 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f22f4ff-46b9-3844-ae82-7911030df493 | -3.59635 | -59.07156 | 2026-09-11 05:27:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 654b2da3-9e30-312c-8ae9-d043442182a0 | 0.11581 | -60.62467 | 2026-09-11 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2b0ea330-152a-36d3-8b57-586e8be6df37 | -8.62659 | -47.41484 | 2026-09-11 05:27:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ae172d44-58bd-3834-9afc-3252c63fdbe3 | -3.54367 | -60.58368 | 2026-09-11 05:27:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9f998022-9260-3a97-b78e-4e7c03c72a9c | -3.28252 | -57.86905 | 2026-09-11 05:27:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d34477bd-c906-35ea-8d5e-51315b97c912 | -6.76394 | -58.61618 | 2026-09-11 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1fee6b0b-22ff-3bd7-a505-0cde7461eddb | -6.76339 | -58.61966 | 2026-09-11 05:27:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7eccdcac-95ad-3b8d-85ac-eebba69338af | -7.01859 | -59.78368 | 2026-09-11 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0bbb5338-4c9a-397d-893f-fcb9119b123c | -2.72693 | -57.61885 | 2026-09-11 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d1697b3-76b6-3a1e-bb19-71820395a7d1 | -4.30417 | -49.10606 | 2026-09-11 05:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f478b441-d1a9-39d8-831e-82e71b62ef5d | -2.73693 | -57.62041 | 2026-09-11 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d5970529-b388-3421-95ce-f3593b3cd479 | -6.84251 | -59.35889 | 2026-09-11 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7db4ba50-6333-3bb3-84cd-c776dd2bfe35 | -3.35962 | -61.28247 | 2026-09-11 05:27:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b11a5adb-8337-348b-8c85-785518f3b104 | -8.63307 | -47.41573 | 2026-09-11 05:27:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ea098130-dc7f-3403-bbe5-8292b7c81ae8 | -4.29362 | -49.10186 | 2026-09-11 05:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dde6b278-3d76-361f-ade8-334519114ec7 | -6.18222 | -57.73853 | 2026-09-11 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e3d2ae6-fc9d-3cb7-a6dc-22686a54f63e | -2.86402 | -49.53819 | 2026-09-11 05:27:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 14bf90da-f96b-3b4e-9831-70798591e608 | -3.53885 | -48.18384 | 2026-09-11 05:27:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42aab9f8-2dac-3c03-acac-265ad5b6d8bb | -3.73859 | -61.75632 | 2026-09-11 05:27:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 4c76b7d1-badf-33ce-95bf-f8840c5276a9 | -5.97823 | -57.76883 | 2026-09-11 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0609aa42-6903-3ba6-8e27-7e017bc3edce | -2.93805 | -50.47065 | 2026-09-11 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fc3245e6-fa4a-3387-b367-b8625f684901 | -4.29321 | -49.10446 | 2026-09-11 05:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 8731d3e3-67a0-3afc-89a9-e97f13584ab6 | -3.16206 | -58.65029 | 2026-09-11 05:27:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 14d03e60-de33-3684-9fa4-edbf522df5ef | -6.1945 | -55.26946 | 2026-09-11 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2debf5c0-e979-3651-bcd0-0c8c9ce5da01 | -6.39696 | -55.2045 | 2026-09-11 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 94837a1e-5f89-3717-b634-2b9269a8f695 | -6.05499 | -57.79188 | 2026-09-11 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57d64b4f-3e13-36f2-9c0e-fe0f38aa02b3 | -3.77041 | -58.84575 | 2026-09-11 05:27:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2d817d4-dc43-326e-8541-96baafdedbdd | -4.53361 | -54.96357 | 2026-09-11 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4ca93131-0f98-32a2-8955-e6b67676def4 | -4.36467 | -47.77668 | 2026-09-11 05:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 3923729e-0f4d-3ec0-9d3b-0d04b0faf8d6 | -2.7236 | -57.61833 | 2026-09-11 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 5166c8b6-5f38-31cd-a159-a0bea501b34b | -5.98046 | -57.77652 | 2026-09-11 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 682350da-3f5f-3a7d-ae5b-0d96ccab15a6 | -6.81933 | -58.99564 | 2026-09-11 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 45e3b645-28fa-3759-832a-d6cab2699eb9 | -3.35897 | -61.28658 | 2026-09-11 05:27:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 041f5ae0-da92-3db9-93f2-c5841117fba6 | -8.38497 | -46.30005 | 2026-09-11 05:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 312528da-2c4b-31fb-a56c-a8afedebb0fc | -4.08211 | -56.30096 | 2026-09-11 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c45378df-993d-3924-9f2e-623a591de6ce | -3.4113 | -59.22894 | 2026-09-11 05:27:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 156fb3f1-2326-3ea5-b152-39b58a35647e | -3.3782 | -50.75545 | 2026-09-11 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| acab3f0e-7dda-3f22-b014-7143505facc4 | -6.19009 | -57.75439 | 2026-09-11 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a6f6cc56-13e9-3bda-ba21-d17e46b1f888 | -5.369 | -56.01949 | 2026-09-11 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3af6066-ff0a-3e86-930c-dd578d73dc31 | -2.68844 | -57.5167 | 2026-09-11 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 59001873-4c37-3895-8ac3-785f7e12968b | -4.85892 | -56.00721 | 2026-09-11 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78683bf0-13c7-304b-b67a-8feeff891a52 | -6.9593 | -59.75639 | 2026-09-11 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ae08adf4-4bf2-3942-b143-2385c421c991 | -2.94374 | -50.46602 | 2026-09-11 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c4e6127e-0557-3232-9b8a-db26ecc77210 | -6.39763 | -55.2 | 2026-09-11 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a9224c9-c459-3b71-8049-cfaf8f3e2e9a | -3.06985 | -51.33235 | 2026-09-11 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b36eff6e-17c2-3fe6-a9e8-069b5337b4bd | -2.25521 | -47.98562 | 2026-09-11 05:27:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dcbc60ba-e0ca-3332-b165-93357b55c6f5 | -5.9771 | -57.77598 | 2026-09-11 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e6cff691-c90c-39ce-9c38-968797619475 | -2.72082 | -57.61434 | 2026-09-11 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e975f6fc-78da-32e4-8e2f-69e5a2f1d723 | -6.84307 | -59.35542 | 2026-09-11 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 562fc49d-88c1-3442-ab83-449c022e5a19 | -3.36857 | -50.75393 | 2026-09-11 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 26828d35-335c-352c-9c8e-c867c9f1cff5 | -3.16261 | -58.64682 | 2026-09-11 05:27:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23e0959d-9b3c-3437-ad0b-864a85e61adb | -2.72196 | -57.62874 | 2026-09-11 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 289f9732-3169-3323-b061-8069254e4458 | -3.09413 | -51.28612 | 2026-09-11 05:27:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1449771b-b3e5-375b-9aa5-32f4c5a61641 | -6.95653 | -59.75236 | 2026-09-11 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9baade0d-ac2f-3aee-a5e6-f06b65a90043 | -2.85882 | -49.53741 | 2026-09-11 05:27:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f44e7bc4-217c-3cdc-852b-cfe588ce01e8 | -6.10718 | -57.65736 | 2026-09-11 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6ec44408-1c82-3427-a363-b6d7f7a825e2 | -2.25462 | -47.98956 | 2026-09-11 05:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8afc306a-4ed8-3643-b1b3-62d4e86129d4 | -4.30468 | -49.10253 | 2026-09-11 05:27:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 6cba0e46-b661-3601-97d1-540ecd6d352e | -6.62554 | -55.2986 | 2026-09-11 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b2869e8b-446f-309d-be35-04320c69307e | -6.68152 | -59.9247 | 2026-09-11 05:27:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78703dd3-2903-35ce-9764-c4cc5858eae6 | -6.62928 | -55.2992 | 2026-09-11 05:27:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9c107cd3-cbd7-338e-890b-eb90b7212910 | -2.72748 | -57.61538 | 2026-09-11 05:27:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c433248-6b65-3f29-93d0-ac87716c2095 | -3.37259 | -50.7599 | 2026-09-11 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e8e3d7af-030b-3c92-8192-54747e2c3800 | -8.63241 | -47.42108 | 2026-09-11 05:27:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| da1b07dc-39b1-36de-9ba1-38a7c0dd155f | -6.08772 | -57.90239 | 2026-09-11 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 80d47ecf-2dfb-31b7-8b11-4185f70122b8 | -3.18376 | -61.11943 | 2026-09-11 05:27:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ed9ea7c-6146-300a-8a0b-d775d74b547a | -3.06941 | -49.52293 | 2026-09-11 05:27:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 38e33240-b4c8-3152-b13e-a910035d8e31 | -4.85974 | -56.0043 | 2026-09-11 05:27:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da306bdb-660e-3a30-be47-584a9fc530a9 | -6.12708 | -45.10852 | 2026-09-11 05:27:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4b9e7006-1d36-32d0-a47a-9d9369252533 | -4.08558 | -56.30152 | 2026-09-11 05:27:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1794f1c1-7352-398c-b4c9-37acf4e67d80 | -3.36777 | -50.75916 | 2026-09-11 05:27:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 98689eb7-c283-33bc-9f7d-94e33039e9ec | -6.81988 | -58.99216 | 2026-09-11 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 436b5b8a-09a1-3718-ab0d-5ddcfb4e87ac | -6.08717 | -57.90593 | 2026-09-11 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e7785ec-c94d-3b17-b172-89e85ad8af4b | 0.11943 | -60.6241 | 2026-09-11 05:27:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 664a4fe9-a080-3fea-80ba-6f564138d69a | -5.97766 | -57.77241 | 2026-09-11 05:27:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80994299-dacc-329f-8052-ed5b645df715 | -7.01248 | -59.77912 | 2026-09-11 05:27:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 992b6615-282c-3bce-8891-167ce1103b6a | -3.66068 | -58.89607 | 2026-09-11 05:27:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 36a94630-6282-353b-96ab-714d8fd94dff | -6.24001 | -51.69242 | 2026-09-11 05:27:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 76aba35e-c5f5-3cf0-891d-08200fdb49b0 | -4.53293 | -54.96806 | 2026-09-11 05:27:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ec101145-9162-3dfd-aad0-49c4010bf29c | -3.39768 | -54.08188 | 2026-09-11 05:27:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26ea51e5-d0aa-35bb-be99-a853dd4f07e2 | -6.63176 | -55.1279 | 2026-09-11 05:27:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad07c88d-b040-33a2-b441-ccdec7aa75ba | -5.00161 | -57.01051 | 2026-09-11 05:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README25.md)
