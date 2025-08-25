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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 13393340-8a4a-3984-b547-4599a78e962d | -3.4439 | -49.051 | 2025-08-25 01:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 7bcaf723-c9ed-300c-a417-795c8389a2fe | -8.5942 | -62.6505 | 2025-08-25 01:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.7 |
| d3eedf8c-0a3a-3258-bd6d-bcb08b6de903 | -14.28788 | -60.37317 | 2025-08-25 01:26:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| ba9a21bc-06ec-32bb-84b0-d006b149f489 | -13.15125 | -53.75135 | 2025-08-25 01:26:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 193.8 |
| 8654877f-dfcd-3b01-8771-9742348cea83 | -12.99737 | -56.88908 | 2025-08-25 01:26:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| da1eae20-c1e6-3477-a108-b9d09b2ede4c | -14.21998 | -58.63245 | 2025-08-25 01:26:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 4f79eac1-b89a-3a2c-b228-cdcee7a23fda | -14.43881 | -56.46285 | 2025-08-25 01:26:00 | TERRA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 5277fe29-0118-349e-a5b3-24ef2127c818 | -18.06157 | -51.37286 | 2025-08-25 01:26:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 0a549467-b76d-3843-8829-2b0e050ca2e5 | -14.441 | -56.47659 | 2025-08-25 01:26:00 | TERRA_M-M | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 28.8 |
| d5d0c8c8-54ad-39a8-8bd4-2d816abc2f18 | -13.15811 | -53.74458 | 2025-08-25 01:26:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 398.4 |
| b62ad882-118b-3d95-8116-43515b2b5c18 | -14.21061 | -58.63391 | 2025-08-25 01:26:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 3803c8c3-10b4-3c3f-8693-47a236548fba | -18.08094 | -51.39298 | 2025-08-25 01:26:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 37.0 |
| 09382618-de0b-3bbd-a9d5-6c13bef07252 | -14.71171 | -55.93559 | 2025-08-25 01:26:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| df860291-ad70-39aa-b72f-4754acc5d000 | -13.15419 | -53.72177 | 2025-08-25 01:26:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 183.7 |
| 6c82ae10-b808-3948-95d1-1aec4df900df | -14.11167 | -53.99762 | 2025-08-25 01:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 55.0 |
| c908c937-34ec-33fa-a35a-e03a585ff6eb | -15.14452 | -59.59497 | 2025-08-25 01:26:00 | TERRA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a6de4df9-9649-3a8c-adfb-05e2cd290003 | -13.14749 | -53.72851 | 2025-08-25 01:26:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 270.1 |
| 9a4d53a1-556f-38ca-b1d6-86ff0cf1dba8 | -15.63729 | -52.72667 | 2025-08-25 01:26:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 5ac44f19-64c8-35f2-87d6-6a3bd2636dce | -18.08142 | -51.39812 | 2025-08-25 01:26:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 1e543e41-29da-3419-89a1-90d7921f3b83 | -13.00433 | -56.89447 | 2025-08-25 01:26:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 86007cb2-f4c7-3cbc-8426-075c1d0825c5 | -15.6286 | -52.70877 | 2025-08-25 01:26:00 | TERRA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 3fbaa23f-c9d3-358e-9602-40de216dee1f | -18.06627 | -51.39602 | 2025-08-25 01:26:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 0f941a2e-56dd-3a3c-8e0d-0f627d426b55 | -13.00804 | -56.88736 | 2025-08-25 01:26:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| aa72ac05-c099-3167-8932-0eda9693523a | -18.06678 | -51.40136 | 2025-08-25 01:26:00 | TERRA_M-M | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 6ed20a0a-6e6b-3e82-bd91-66ce82df26fc | -14.1123 | -54.01394 | 2025-08-25 01:26:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 9b1cc371-fce8-3391-ad2b-8f4d9f90d21c | -8.99124 | -63.64949 | 2025-08-25 01:28:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 21.3 |
| a73e675d-2b0f-3bb6-abae-9c992c56a1c2 | -9.23302 | -60.92981 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 31a92ac8-c9d9-3b37-a39d-46a450df416f | -7.63075 | -62.72244 | 2025-08-25 01:28:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 9be5f802-7b39-3a4a-bfb5-80fd70d0d7c2 | -8.63277 | -62.64116 | 2025-08-25 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.1 |
| cf9b5e43-5658-38d9-9df6-f3b8d924660e | -7.04764 | -59.82249 | 2025-08-25 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3785ef50-f6da-333b-bcb9-e2a94a64e9c6 | -8.22309 | -61.41895 | 2025-08-25 01:28:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 39b1e21b-588a-3857-97db-50dbeaf5e3f2 | -10.25202 | -59.10649 | 2025-08-25 01:28:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 2a194dcb-11f0-3247-a669-4427d89be393 | -9.00896 | -65.69452 | 2025-08-25 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 834eb811-a342-3ce1-aa2e-39e928db9a7f | -8.97003 | -67.48153 | 2025-08-25 01:28:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 944cd7fe-6267-3560-b458-7d6a1d15f6a4 | -9.0999 | -61.42283 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6affb976-211f-3830-aa5b-4a6171f4038c | -9.96475 | -60.1757 | 2025-08-25 01:28:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b08979aa-34c4-3ed2-8ba6-1505eebecf60 | -8.57503 | -63.91843 | 2025-08-25 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 40bb7d11-1d2e-31ea-9ae8-17decd3addd8 | -9.81387 | -64.25285 | 2025-08-25 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 441270fe-0bff-370a-b1ae-7f2c37e5ddf9 | -9.194 | -59.5025 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 44d5a911-d59e-3ace-9776-0bce12bf2a2f | -8.88443 | -62.39555 | 2025-08-25 01:28:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e5fa1eb1-dba3-37b9-8423-2f1d7e1dce8a | -12.85663 | -60.15765 | 2025-08-25 01:28:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6dc54629-ad08-3ab7-b3a4-440520e1ac9f | -9.17263 | -60.82636 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 6206d37b-ef65-325a-b1a9-74b01a64839a | -9.01218 | -65.39796 | 2025-08-25 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 6ea5e5f5-f4f0-3976-9c84-d0a5b58f63a6 | -6.91384 | -62.99958 | 2025-08-25 01:28:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a6c557ed-2ffd-320d-8cdd-230dd5b09f4f | -9.14066 | -60.73374 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0262b3a8-a5ff-3d36-a8f9-6e0350f781bd | -7.54687 | -63.85985 | 2025-08-25 01:28:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 9252210b-ed10-3d5a-98a2-431f670f8b58 | -9.96611 | -60.18525 | 2025-08-25 01:28:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 28.0 |
| a4e3e9e8-a2ba-3f6e-9ec7-e0aa76f0bf01 | -9.57641 | -55.37779 | 2025-08-25 01:28:00 | TERRA_M-M | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| f13885b6-4f0c-36ed-9bcc-806ca6ff7f35 | -9.31299 | -63.44451 | 2025-08-25 01:28:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 483e47fe-699a-39dc-8afb-2723d21c3596 | -10.26162 | -59.10518 | 2025-08-25 01:28:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 95885004-a1d5-36b5-aec6-ceadf40d45cb | -9.20046 | -59.48024 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 395ad015-626a-367b-865b-0698418dfb38 | -9.0063 | -63.63145 | 2025-08-25 01:28:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7c91c5e5-2197-366b-88c6-7a0a53eb8e3d | -8.11158 | -62.87037 | 2025-08-25 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.1 |
| b7b8b231-5aa1-311a-8efa-db72d148b0c1 | -9.06039 | -60.62219 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2b621769-3f6c-3b46-bf15-f3c2f1ff6016 | -9.3117 | -63.43501 | 2025-08-25 01:28:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 962f582e-1609-31e5-be2a-c644e41a8afb | -12.60069 | -60.36505 | 2025-08-25 01:28:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2b1c32d5-e152-3ea9-b64c-542c3022747e | -9.13688 | -60.77212 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| a75a298a-d249-382d-a10a-8c1fef4255c4 | -7.91904 | -63.07504 | 2025-08-25 01:28:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 644ac8b2-f9f3-32d6-8675-1e609d00c0a6 | -8.68263 | -62.87264 | 2025-08-25 01:28:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 62db2bf0-944f-36cc-b237-cc71366af17d | -9.13167 | -60.73515 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 612c9ab4-82dc-324b-926c-4c119820e5d4 | -9.26874 | -63.46035 | 2025-08-25 01:28:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3d43c5a0-3e6d-32ea-8a40-ad8b284163f7 | -8.8918 | -62.4491 | 2025-08-25 01:28:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 19fd8dcd-84ac-331b-a1ff-07bac302c868 | -8.88663 | -64.19003 | 2025-08-25 01:28:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 645588fe-a977-3cf7-a913-f8b559aed66f | -6.92271 | -62.99833 | 2025-08-25 01:28:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 22.0 |
| ddb731b6-a4ca-3dca-beee-b8d9303d328b | -9.0223 | -65.39663 | 2025-08-25 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 32b8dae1-76f1-3392-96c2-7ff562f1ba41 | -9.20197 | -59.49063 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 82e56388-aa4b-3cab-98eb-8691af3814f6 | -9.25266 | -59.64084 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| f4bf3e18-0a9f-31e5-ac87-d2287ed4f8e8 | -10.45899 | -59.12788 | 2025-08-25 01:28:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 924ea918-f750-3e17-aa18-5c49d20e1976 | -9.04483 | -65.72779 | 2025-08-25 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| d7875d26-f976-35d3-9502-f8e867afae6d | -8.94958 | -62.13525 | 2025-08-25 01:28:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a58c606a-b1ab-3f59-8e1a-9a2d5f12bcf6 | -9.19595 | -60.92592 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 02b124d8-462c-30c6-9bda-9a6db58af2fb | -8.68387 | -62.88169 | 2025-08-25 01:28:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 21b4f4dd-5dd9-3d4d-89c0-249e232ade58 | -9.20459 | -60.79343 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 85625624-b0db-340d-90ea-65ccdeab006e | -9.81792 | -64.28418 | 2025-08-25 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a5711d39-f145-3b4e-b79c-809b79b082d2 | -8.6089 | -62.59891 | 2025-08-25 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 3813f405-0be4-3ecd-bf21-f1a6810339e6 | -9.23173 | -60.92065 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| d0c44649-8870-36f3-9d14-3d61886a9f00 | -9.20328 | -60.7842 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 424e8347-150c-3959-9d4e-f2747104cd53 | -9.2036 | -60.91545 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 3f81a3d9-4bd7-3ec3-b613-7a67bc9b113b | -7.57124 | -63.43254 | 2025-08-25 01:28:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2f52878d-66f5-32c4-b59f-2be4865dcd74 | -9.19561 | -60.79476 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 58cb71d2-a147-359c-8e93-734b63f2411e | -8.90311 | -62.46571 | 2025-08-25 01:28:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 16.2 |
| c534243d-703e-3683-ac0d-87c7e00a005a | -9.51385 | -60.50501 | 2025-08-25 01:28:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 5559df39-18a5-3544-bf35-3217a43cd548 | -9.21384 | -60.92327 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 44e75b6c-f88b-3293-acaa-81909bb091e2 | -9.79796 | -61.20804 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9151462f-de8c-3864-8937-adf693069ec5 | -9.09279 | -65.71512 | 2025-08-25 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 23.5 |
| cf84deb5-c91f-3e3b-966a-2442be486d65 | -9.52423 | -60.51303 | 2025-08-25 01:28:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 4f35b2a4-c569-3ad6-9b60-01c01f209930 | -7.4385 | -60.62404 | 2025-08-25 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1a3d705b-f44f-3e1b-8fb4-d629e667df39 | -12.59017 | -60.36352 | 2025-08-25 01:28:00 | TERRA_M-M | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 70b71cca-f926-365d-b9ae-3525798b35ab | -7.53259 | -63.8233 | 2025-08-25 01:28:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e1c89a59-4344-3889-a585-aa43a43832c4 | -7.0723 | -60.06178 | 2025-08-25 01:28:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 9cca427f-de53-3ffe-8860-33cc00a7d937 | -7.6579 | -63.52726 | 2025-08-25 01:28:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 7bd12a05-2221-3c1d-9761-16ff6cde4aea | -8.89057 | -62.44017 | 2025-08-25 01:28:00 | TERRA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 19.1 |
| c5ae13eb-d2c6-3e3b-b75d-18fbdc07c5b4 | -8.59118 | -62.60143 | 2025-08-25 01:28:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 7b5ffd85-eae1-309f-8853-3200d56445cd | -9.205 | -59.51141 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.8 |
| ea410c2a-5cbf-336c-a07e-b3987322f907 | -8.97323 | -65.41531 | 2025-08-25 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| e11d0d1a-415f-352e-adc4-202dc28497e7 | -9.16366 | -60.82769 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.4 |
| f3751832-1e4f-399a-889a-4adc554ef058 | -9.01063 | -65.38612 | 2025-08-25 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 85cb1607-cae8-3b44-ae7e-53d8b75fc237 | -9.1943 | -60.78552 | 2025-08-25 01:28:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 0449a606-4e1c-369e-b178-ccc785a21512 | -9.06556 | -65.72499 | 2025-08-25 01:28:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 32.2 |
| e57e43b1-cdd0-3a80-a189-7d0498a2a172 | -9.51519 | -60.51436 | 2025-08-25 01:28:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 18.4 |


[Clique aqui para ver as próximas entradas](README11.md)
