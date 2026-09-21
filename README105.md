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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8cf853a6-13a5-3497-87c2-8ca1caccbc9e | -5.76475 | -57.58859 | 2026-09-21 05:59:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1320af32-a38a-3af1-892f-67090b523939 | -3.08245 | -61.17521 | 2026-09-21 05:59:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4815b7ee-0f18-3cef-8f3a-b8c7b2e37ced | -3.39184 | -59.58386 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5640ea9f-e320-3e3b-bd00-082f80255d53 | -3.48336 | -59.56389 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9accc1f1-661d-3b4b-9594-b5fd441e637b | -3.82064 | -58.88065 | 2026-09-21 05:59:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c27aa0a-dd23-37ee-bd7a-18dcd130dc7e | -5.01188 | -56.09545 | 2026-09-21 05:59:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 14530840-410b-3387-aa21-b995046e8847 | -3.44163 | -58.23679 | 2026-09-21 05:59:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 76309737-9beb-345c-90f3-a45adc986efd | -3.75272 | -59.42325 | 2026-09-21 05:59:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88ad2a75-9850-3bd7-909f-17317a3673c2 | -3.4909 | -59.61681 | 2026-09-21 05:59:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e57982b0-a33b-3aab-b188-19d28f2fb5a1 | -6.7281 | -63.1303 | 2026-09-21 06:00:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 5df1ca7c-f54e-3540-95a8-e689905a0c6d | -8.78444 | -68.84459 | 2026-09-21 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 29a16d24-265c-3d43-8cb8-19d3f3edf580 | -6.35971 | -58.28957 | 2026-09-21 06:01:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd5342ab-0c01-3e03-8262-827928de34f9 | -8.79956 | -69.52115 | 2026-09-21 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3c4077b-be39-3e7e-a272-7b6cf26e4434 | -7.3318 | -55.60808 | 2026-09-21 06:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d7a12870-8ba2-39c0-ad46-1a3287b4f67b | -11.98415 | -58.07306 | 2026-09-21 06:01:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 657cf670-3ce0-3608-9f7e-96490a95f670 | -10.77503 | -68.66483 | 2026-09-21 06:01:00 | NOAA-20 | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09b217fc-502d-3532-af03-81714ace8583 | -9.61241 | -65.36342 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f839fdd5-bcdf-32ff-b8f2-4b2f3054b5af | -7.3322 | -55.22197 | 2026-09-21 06:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2b9de0cb-151e-3149-866a-1d01d3720819 | -7.33102 | -55.61402 | 2026-09-21 06:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b80dbf62-ad7a-384b-a15e-2ac6b29ffbf0 | -7.32413 | -55.61285 | 2026-09-21 06:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7e071831-56c9-3f12-8d1b-f5a13b9fd718 | -6.29549 | -59.96431 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f43d3a93-4def-3240-8bec-b783917c2e51 | -9.10701 | -60.94888 | 2026-09-21 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a5cc5d9f-2011-3529-b895-7629da175e5f | -6.79845 | -58.79403 | 2026-09-21 06:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b766c8d6-d9b0-3867-8df8-a24d3f90391f | -6.20026 | -57.78099 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 07b889e8-bb71-3f2a-ba3b-5bdfff543501 | -8.98264 | -68.81501 | 2026-09-21 06:01:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 90ef2068-e0bb-3017-aae4-a671605acb7a | -5.93319 | -59.9559 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7099d7da-699c-3982-8e4d-848df5fa5e1c | -9.2188 | -67.93002 | 2026-09-21 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| eedd2fda-2c54-3904-9428-e4af356d04bd | -9.03715 | -61.65619 | 2026-09-21 06:01:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4a70533c-73d2-30f5-bc65-a2abc3613727 | -9.18151 | -71.83327 | 2026-09-21 06:01:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ffda285d-a5a8-3514-ba9f-5106f8250803 | -9.55991 | -66.02175 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d63f7778-da6a-30f0-8add-b86f635e2c38 | -6.73971 | -59.42113 | 2026-09-21 06:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cd3d6817-2378-3eae-95e3-274e83b506a1 | -9.55326 | -66.01639 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b3e0507d-117f-3f85-9a70-e17097ba4324 | -8.04773 | -61.33383 | 2026-09-21 06:01:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0420ca65-8114-3d07-b9f6-6f1e935f8ccf | -9.56387 | -66.04724 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3e4362fe-a89c-3ed4-b897-1a9bbe58a853 | -8.79216 | -60.79596 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03c599d2-9f0a-33f6-946c-b0f2f17ed571 | -6.29518 | -59.92932 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39ceeee8-bcaa-36e9-a8a7-389c40f59533 | -6.7316 | -55.09829 | 2026-09-21 06:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f38dc8c1-055b-3088-adc1-b7da531e8233 | -6.30909 | -60.01674 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fbd8f885-057f-328d-b021-147398c2f638 | -6.36026 | -58.28549 | 2026-09-21 06:01:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6444d0c-39d0-3b22-80ab-276fd73f3f70 | -7.58445 | -57.68069 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1f6c4fef-27de-3043-97cb-b5d5b7915462 | -7.57032 | -57.69302 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a2ae6921-e3b7-38d2-88b3-cfcac67d5649 | -8.7953 | -60.80103 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5dcaa2b1-da59-3f7e-b551-c82d84191737 | -6.46328 | -59.99403 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| afb8c1f6-b87b-3529-9a9c-d882d853c5f2 | -6.37962 | -60.01603 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f775cd0e-ff76-305a-ae6b-26db12a504d8 | -8.22615 | -71.04372 | 2026-09-21 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 626404e2-a3be-3b77-87d0-db79a5a014d4 | -6.44414 | -59.97134 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ccce378d-8723-390b-9b5d-5f86e448e984 | -5.93276 | -59.95895 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9b4837d-0384-3da1-ab8d-93cab2596586 | -6.72711 | -55.07764 | 2026-09-21 06:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e96985b8-ac3a-338e-a3b7-0b2ff43e25f5 | -9.11206 | -60.94956 | 2026-09-21 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c58311e-295c-3095-885e-83210b2d5ec8 | -6.99118 | -61.34989 | 2026-09-21 06:01:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8c394c87-b3e8-3bdf-8919-35c2a6ab413c | -7.28225 | -61.11722 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f02c7e2a-9721-3d42-9a2a-607ad00b7ebf | -6.19965 | -57.78533 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 42a90b12-22be-33e2-b891-deaf74b0ef8d | -6.72185 | -55.08657 | 2026-09-21 06:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 79be6799-d046-376e-8c73-27b5b64a8247 | -10.62673 | -69.11282 | 2026-09-21 06:01:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89c0e1ed-4ec4-3de6-945b-1de7028848dc | -8.77742 | -69.01832 | 2026-09-21 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b5c0755-7c07-3695-8fd5-917e840c2d11 | -7.81099 | -61.80976 | 2026-09-21 06:01:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e899716-2881-3de6-9e92-53386db251a4 | -6.30069 | -59.96496 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61286344-685a-389d-ae6f-698010f4e5aa | -6.44932 | -59.97209 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 16a8c940-9545-3849-b6e7-0d4df30ac75b | -9.55521 | -66.00343 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 62dd55bd-89b7-36c6-9c9a-bb32318d0106 | -6.12164 | -59.9518 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1bbf150-25be-326d-b53f-089f91af0706 | -9.55626 | -66.02122 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6e319ee-ad80-3098-95bf-0f23a96dbb20 | -6.13414 | -59.93777 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30a580a7-2449-3a0c-a253-62de688db553 | -8.78058 | -68.84755 | 2026-09-21 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac45189c-50de-34c7-aa06-d07343c272fe | -10.09828 | -64.33293 | 2026-09-21 06:01:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97289786-a0d8-36a5-8ef8-b3a6ae0baf6c | -8.83729 | -69.45554 | 2026-09-21 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| caf29b4e-1e7b-39ad-a391-f8778b0be89b | -8.95887 | -64.40684 | 2026-09-21 06:01:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa61a5e7-f8fe-35e3-9fb4-7e4d103a3ca8 | -9.74975 | -65.05624 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09432a06-a9de-39c2-8d02-c4f9d7444359 | -6.12912 | -59.96057 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64f6826d-4acb-3398-8b55-3d99d86c7387 | -9.02 | -67.74377 | 2026-09-21 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a604654a-9574-3e1a-99a8-5d056b5f936f | -9.02888 | -60.36371 | 2026-09-21 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dd9bc3f5-eec7-3027-a0f5-f5d35a203bac | -9.55091 | -66.00722 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60e200ef-7b61-3c98-be7a-5f7fa87553c1 | -8.86221 | -68.4983 | 2026-09-21 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b7254aa-c19c-32e3-a3db-389bf21d303b | -8.86057 | -68.50884 | 2026-09-21 06:01:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e61cade0-b562-32b3-bb9a-43a66b67147c | -6.45076 | -59.96982 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| daafabc5-225e-3faa-8da2-e1b4bb2940e0 | -7.32297 | -55.2064 | 2026-09-21 06:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b0a75579-4777-3edd-8131-dc255ee96a68 | -7.98752 | -71.33991 | 2026-09-21 06:01:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6ec4258-9ce9-3c81-94c9-b0190ccee030 | -6.76427 | -59.11753 | 2026-09-21 06:01:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c0e17e75-5df3-329d-95a1-d9b674bcfcee | -8.98788 | -69.51193 | 2026-09-21 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3dbacee-3b23-3eb2-b82a-41162b1a844a | -8.74219 | -69.45481 | 2026-09-21 06:01:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc110c4e-5fe9-35fe-bcd2-60f53683c694 | -9.10662 | -60.95179 | 2026-09-21 06:01:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00f6595f-3494-3b88-8687-bae57c70eae8 | -9.55498 | -66.02972 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e011dfba-1e66-3cf5-8641-d2b819869e80 | -9.03307 | -61.6502 | 2026-09-21 06:01:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 899909c2-2c92-3b53-bd55-fef8e9176fd5 | -10.46027 | -61.31758 | 2026-09-21 06:01:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d876325a-0c77-31d0-8cd1-b71b0c59a0a7 | -9.56022 | -66.04668 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b05f3fb-08ab-35b9-b4e9-6e04fdd61523 | -9.55604 | -66.04739 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 551119fb-4b0f-3c1e-9920-0419b6194795 | -6.13697 | -59.94302 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0802efea-2ccc-3003-ae78-461c01559036 | -6.12122 | -59.95488 | 2026-09-21 06:01:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78fd9fce-f219-398a-9af6-09efd9ef783f | -9.54989 | -65.68491 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d23e3158-7a97-3d41-9d03-3102b3026df3 | -6.18893 | -57.7749 | 2026-09-21 06:01:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c61ac833-0df2-34d9-a708-af833600aa51 | -6.35927 | -58.29005 | 2026-09-21 06:01:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01d434fd-7b7a-3047-b229-0cefbe05fa30 | -6.90279 | -71.51899 | 2026-09-21 06:01:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d18f62a-a6ce-313b-9583-8bc0ec49f645 | -7.58215 | -63.04724 | 2026-09-21 06:01:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f4156f6-0dad-3ef8-a02a-b6f568c520bc | -10.47059 | -69.19985 | 2026-09-21 06:01:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b7d9225-ce78-37b6-a3d0-698155335434 | -9.55862 | -66.03027 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc240e02-00dc-3dfb-acb4-d46f20d17ab3 | -9.57115 | -66.04836 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1689c711-987e-325a-8add-d13a3564b4eb | -7.24894 | -55.59492 | 2026-09-21 06:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b03f256d-d35e-3942-b1c0-6486ee24e350 | -9.57053 | -66.05262 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09d6f115-37b2-3c05-a9d8-1ebc599259b6 | -6.96106 | -71.75931 | 2026-09-21 06:01:00 | NOAA-20 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d4075361-bee1-3dd8-9bc0-bad312413443 | -9.55968 | -66.04791 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c1a08699-356f-3db3-8d26-0b13dd2b1830 | -9.55239 | -66.04686 | 2026-09-21 06:01:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README106.md)
