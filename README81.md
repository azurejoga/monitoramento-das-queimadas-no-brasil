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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 370b95ea-74be-3767-955f-0713db03cade | -13.51088 | -51.5253 | 2026-09-22 05:23:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 8ce46d4b-fcf3-3833-97a3-f66ab4bd9fa0 | -3.50852 | -55.48356 | 2026-09-22 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c6276634-4cc1-3535-9041-ef262f08d24e | -5.21193 | -56.09916 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5027be4d-84ed-37e9-84e4-ece987acac49 | -8.12398 | -47.12281 | 2026-09-22 05:23:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 560cadc6-a3ac-348f-84cd-114a266f8a59 | -6.79181 | -59.94921 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 63bf120a-2fee-3454-9a69-22536949b42e | -6.4676 | -59.96802 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb6fc344-9d79-30d1-bf25-76ec9622321f | -4.86006 | -56.07381 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f797b75-0350-3f3f-b2f0-bc0535d1f3ca | -5.99109 | -44.72569 | 2026-09-22 05:23:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f19d2eed-0f15-3cfa-9da6-423348d4c01f | -6.78365 | -58.60945 | 2026-09-22 05:23:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93776cd9-1394-3315-8072-0a63ca353d09 | -7.57203 | -57.65936 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99d5b527-22e6-3af4-9a58-482889256909 | -6.10776 | -57.74356 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8827a38b-11b1-30e6-b385-cbef8eee004c | -3.06865 | -54.39482 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 27c6394c-4faa-328e-89da-66182945cc59 | -11.01649 | -54.14848 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 028104b0-36c5-3299-94ca-b0e73513d74e | -6.03997 | -57.82572 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3e1f4187-8fa5-38a0-8145-4c2632d57885 | -6.45794 | -59.9826 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 23efe246-6498-3295-8fcc-cec7778ca171 | -6.7997 | -58.78854 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 842eb204-0433-3f3c-a117-02fbff1a3c31 | -4.308 | -55.58813 | 2026-09-22 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f0e2db4-15bd-3bdb-97a6-720ab4d59321 | -7.58313 | -57.69683 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29e994f5-a44a-32e3-9972-76e327dd1f54 | -3.38703 | -59.42654 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 78418611-8ef1-316d-8e02-2ad5a4e85be7 | -6.73956 | -55.07307 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2503951a-831f-306a-a609-8caeb1b7ef1d | -4.94257 | -55.82148 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27807f4a-b816-3b6b-b4d6-2c722f9e0694 | -7.39966 | -55.22921 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| beb46622-2cea-3212-8e6d-121eab90d654 | -12.14393 | -61.16319 | 2026-09-22 05:23:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fab2e8e9-f192-3b55-99b0-e6adff099537 | -6.38309 | -55.28278 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4a6605a8-54e5-3fbe-94fc-5f376a95d0cd | -13.7211 | -48.78397 | 2026-09-22 05:23:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2aa990b-aaed-38f4-8c5e-483f99c34e6b | -3.4838 | -59.56463 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 31b17286-84f0-31e8-b3a8-bd238f87a984 | -1.7494 | -47.1362 | 2026-09-22 05:23:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 702b7351-ce30-3342-992b-6f9cfd4a7182 | -2.9555 | -57.71513 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df33cda0-dbd2-3fe0-a21d-b4c5be85e840 | -5.81738 | -57.74359 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3aa47f7f-0ae7-358a-b4f9-b5131b2adf46 | -7.86141 | -54.70343 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9587eb01-b93e-3171-af97-a5af6b4a4752 | -6.73318 | -55.06799 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2b515413-9686-37d9-ae47-6e07825c56b5 | -3.06624 | -54.41013 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94774959-b9aa-30c3-8110-3b73accc5a04 | -3.4854 | -59.57732 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3286e2f-c38d-3682-b624-bf18dc21e936 | -5.84884 | -49.78337 | 2026-09-22 05:23:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2fe626fa-c4f1-3aa5-a425-42e6d66fe19b | -6.13647 | -59.96104 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00ae498f-1e32-392c-a3fd-1e02242fedd4 | -6.38427 | -55.27521 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3ffda602-fba1-32af-afab-27e712b47179 | -3.46266 | -58.3212 | 2026-09-22 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f7ceeca-8f38-3c06-a65a-e9d42576a222 | -5.83827 | -53.48084 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef0e9217-2831-3a43-94f7-10cf9d18846f | -5.37386 | -56.05199 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f9be0a7-a255-33e3-b74e-78b444713a2f | -6.92205 | -59.63397 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c8eb046-4e9f-39a9-aabe-29b464da7ba9 | -5.93773 | -57.70897 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf9aa0c8-df62-39b0-8cd6-6360a90c22c9 | -3.05295 | -54.40414 | 2026-09-22 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 59fdfcdb-b953-39fa-b4ea-2bf2dbfd133b | -6.83926 | -55.53097 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ea240dd-34c2-3d42-86cd-bbe3439cf3eb | -6.11442 | -57.74462 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd5e9a79-c501-3df2-8d08-aa6ba023f375 | -3.22651 | -61.05178 | 2026-09-22 05:23:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 119e6c4a-3784-30c6-b41f-770ad06ed520 | -13.92844 | -48.56757 | 2026-09-22 05:23:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f7ca275d-d8ff-3699-a8d6-ba589338931a | -6.80657 | -59.39518 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a0bef91e-1ca4-3d5e-9d13-d381d4a47105 | -12.83636 | -50.97628 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 55a926c4-edc5-3746-b39c-b460ddacfa43 | -4.18756 | -51.24419 | 2026-09-22 05:23:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8ccb209d-c11c-3d25-83af-4d0a3c97e44b | -3.17469 | -58.59352 | 2026-09-22 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae5fed7b-aba1-31f1-af43-8435eebb9704 | -6.70565 | -59.00463 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 602d8e20-cf9c-3ae5-98b2-e87b79c5a34b | -2.86525 | -57.79575 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ddc06c81-5d12-3351-997f-85cb8f896a75 | -6.40779 | -60.04826 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 22e9a4f2-b7f4-3512-bee1-88df4eb18739 | -3.78816 | -55.87775 | 2026-09-22 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d755ae0-9d0a-380c-943d-de9f6f70345c | -5.91774 | -57.68437 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7f4be173-6c33-3073-be99-884ab566e0cb | -3.44068 | -50.61221 | 2026-09-22 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0784ccf8-8049-319e-b916-65a0c888846e | -3.82457 | -59.33603 | 2026-09-22 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c6dcba07-7654-302b-bbcf-9986e9730abf | -4.96843 | -55.83276 | 2026-09-22 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d9c8f562-4fbd-30fe-b23e-c9a411f48cff | -6.12529 | -55.81872 | 2026-09-22 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f574ea0-5db7-3ec5-ab33-b868371a8888 | -7.42596 | -49.84917 | 2026-09-22 05:23:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fde5e9aa-c247-327f-bd8e-9b23229c84de | -8.76766 | -71.10808 | 2026-09-22 05:23:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e505ee6c-1c34-3ade-a08f-72f20c80ef72 | -3.38348 | -61.29173 | 2026-09-22 05:23:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0bfbc904-f059-30a0-994f-50f717eb5c2d | -7.60791 | -55.35728 | 2026-09-22 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b496ad3-0226-3c6b-bf8d-92622f03ef3e | -6.52466 | -58.30969 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aea2782e-a92f-3fc2-aa78-6bfecded93d1 | -6.2802 | -57.74225 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d32a0c9-1a72-3321-947a-d473a0fb638f | -1.68201 | -54.93164 | 2026-09-22 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13dcb786-9a7e-39ff-89af-4cd40e57d048 | -7.13926 | -48.44239 | 2026-09-22 05:23:00 | NPP-375D | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5f466d55-12bf-3ddb-9ee2-d4149ebe8c12 | -6.70682 | -58.99733 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5ae68c0-0aeb-3b23-ab89-add1680b8dec | -6.45153 | -59.97752 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b6c8935-0436-365f-b731-85b3b16c88f0 | -11.70285 | -50.994 | 2026-09-22 05:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 30.0 |
| 9ae5cd26-139d-3953-90c9-ddcbfe5a0233 | -3.22884 | -53.94569 | 2026-09-22 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b9e8995-193e-3d55-9f9a-82cb7026d3f2 | -7.8805 | -54.7232 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b675f117-8cee-3207-a05a-83c3d4f6e3a0 | -5.61122 | -44.84152 | 2026-09-22 05:23:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0284092a-3564-30c3-b427-410e8ebe5f7c | -7.57758 | -57.6888 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 36179142-de13-3fe8-a563-50a0e5100075 | -6.69581 | -60.0076 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d2fd865-727b-317b-80d5-0e90b79e1b11 | -12.14327 | -61.16715 | 2026-09-22 05:23:00 | NPP-375D | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 22bd9013-8a0e-3391-a635-be1894ce1480 | -6.1201 | -59.95012 | 2026-09-22 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1e06a2a-708a-35d4-a350-ffcf8628b227 | -13.33826 | -51.28208 | 2026-09-22 05:23:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d1c93181-874b-3035-9f52-f0e658a706d4 | -3.23594 | -53.94681 | 2026-09-22 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8e59ddbd-e6b2-3dee-92c6-8c29c4567d81 | -2.02272 | -48.77851 | 2026-09-22 05:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e3e21129-9216-3dfb-8065-3d72380136df | -7.58036 | -57.69282 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db4924e6-6be3-36af-a86a-1b3d2a050d09 | -6.0689 | -57.73024 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 460ef06d-493b-3911-a814-581ffc89c266 | -10.90467 | -54.07079 | 2026-09-22 05:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c580865e-5192-3158-ab4c-b567b988cd9f | -3.44758 | -58.45763 | 2026-09-22 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 798434cc-46cc-3be8-8c86-5162e3796f8d | -6.73601 | -59.4226 | 2026-09-22 05:23:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fefc9add-76c7-38aa-a615-0dfcf1dedc8c | -6.10665 | -57.70768 | 2026-09-22 05:23:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| be31218f-0dba-31ab-a780-58a6364d031f | -5.84216 | -53.53187 | 2026-09-22 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2deb4ef9-6533-330b-9681-adbcc5eae5a4 | -2.16502 | -47.88407 | 2026-09-22 05:23:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 134322f2-c3b6-3ea8-b46a-976f88b6a582 | -6.62114 | -59.91109 | 2026-09-22 05:23:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 20544a38-60a2-375d-bbf1-52412f6ce6cd | -13.92752 | -48.5756 | 2026-09-22 05:23:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f32e00f0-63b7-3c56-8f8d-7deb8a5f1ca1 | -2.02755 | -48.77925 | 2026-09-22 05:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 935b091a-23dd-31e8-b549-9e92b78f3fb6 | -8.31445 | -44.75598 | 2026-09-22 05:23:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4b551d82-1bef-3fe5-8580-f8795c9c3b1c | -1.29715 | -54.20417 | 2026-09-22 05:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4af2e577-f86d-3f07-913e-b82eab9fccd2 | -3.41769 | -60.19786 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be7e2909-2ff8-33ef-925c-3e729eb1d0c4 | -14.5866 | -52.17923 | 2026-09-22 05:23:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2765d49-5fab-31a8-af89-c239a2388258 | -2.28682 | -58.09696 | 2026-09-22 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2af230e0-ff46-3f96-a2da-377bce488b0e | -3.01212 | -54.17903 | 2026-09-22 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d3ec8406-d223-35d1-87fa-a8eab5d66c13 | -2.93457 | -57.80285 | 2026-09-22 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60a13cf3-e91a-3499-9682-3b3186682f49 | -2.41485 | -57.90491 | 2026-09-22 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 161e46bd-3b24-38d1-8a8c-4ce31641b671 | -3.40199 | -59.58171 | 2026-09-22 05:23:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README82.md)
