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

## Dados Diários - Página 146

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b610718a-31ab-3e24-a774-f3bab1d1d3b7 | -11.78993 | -47.38385 | 2024-10-09 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d839a19b-52e0-3b05-b5e0-64cceeb04212 | -11.78931 | -47.38807 | 2024-10-09 04:40:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a583927f-ec40-3b33-ba63-e131bb51df06 | -11.78223 | -62.88374 | 2024-10-09 04:40:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e2a736a-8f70-3c07-a8b7-52684418cb50 | -11.77584 | -62.88222 | 2024-10-09 04:40:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 228d7806-a47e-3bf2-98c1-4886d54fed87 | -11.7683 | -62.88632 | 2024-10-09 04:40:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a1ad7bd-b549-3e51-9973-7a3ca1cb5798 | -11.76186 | -62.88503 | 2024-10-09 04:40:00 | NPP-375D | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50263fce-00f8-3e89-8fba-9775329c0bab | -11.73797 | -48.41177 | 2024-10-09 04:40:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2afc776b-ee84-3625-8917-14d67defcc30 | -11.7374 | -48.4156 | 2024-10-09 04:40:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0cb42c9-7635-3dbf-87ec-f5264f96950c | -11.71479 | -65.00653 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8a1a7bb6-abcf-318b-89da-3a08feb776a8 | -11.70862 | -65.00422 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 92251cd7-90f1-3f44-a6d2-3cb46ec3128e | -11.70853 | -59.12448 | 2024-10-09 04:40:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce9c3fb1-63c1-36ea-89be-6d1e34dcf4ed | -11.70797 | -59.12753 | 2024-10-09 04:40:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6193bc89-254e-3d1c-8d09-ab55e11680a2 | -11.70755 | -65.00494 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 51ef55ff-a8e4-3caa-affd-90507599781e | -11.70705 | -65.01149 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 00854c85-ffd8-33ee-84b4-1ec53e1a258c | -11.70603 | -65.01223 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 6205e07a-c747-3146-862e-af5ad92e53bb | -11.70544 | -65.01896 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 1a7e67d4-7041-3964-bc36-3ab8ee4b256f | -11.70473 | -46.4892 | 2024-10-09 04:40:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d33d6317-bcc0-33aa-b989-f83c555b3fec | -11.70445 | -65.01973 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 99acecf6-faa3-3816-8251-47222badfcba | -11.70405 | -46.49389 | 2024-10-09 04:40:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1eeac865-31e5-3c79-83ad-dfd7c6a273f3 | -11.70139 | -65.00262 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| cad4f8d1-ac4c-3240-bf42-c97b9cd1ee8b | -11.70032 | -65.00333 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d09614fb-e9ad-3cf0-bffb-96be1a8a07ee | -11.6998 | -65.00999 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 33dbb8a9-f766-32dd-a42e-e65be9548852 | -11.69877 | -65.01071 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d33b9461-28d9-37af-a508-439f6d285fd6 | -11.69819 | -65.01743 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 81381f72-df23-39be-8620-78faabdaa09f | -11.6972 | -65.01818 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 002991e4-3ba9-3fa8-aa51-6ed448a3acdc | -11.69701 | -49.95869 | 2024-10-09 04:40:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e4a0ad1-bfe1-326c-b8c9-0f6fca5642ea | -11.69646 | -49.96223 | 2024-10-09 04:40:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cfe73bcf-1810-3a2b-bed2-0aef7765a959 | -11.68556 | -64.01292 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2a068418-7690-31f3-96fc-52cacbb82661 | -11.67877 | -64.01109 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cce3c3d6-b868-3a6e-ac5c-c259c69ea345 | -11.67647 | -64.0204 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd37e676-a837-38e0-8741-8be21508cee6 | -11.6763 | -64.02303 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4f1246b4-2c10-3415-9b8b-f465d6e50549 | -11.67538 | -64.02552 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e71bd10c-87d2-3bae-abcd-5134ec49c184 | -11.67525 | -64.02811 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f5f34994-0454-3206-826a-be244475ca38 | -11.67411 | -64.03146 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 05fa3f5c-c1ce-33f0-9116-ec48bb70292f | -11.6673 | -64.02972 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 97bdc180-122b-3df6-8f40-60a8c567189f | -11.66703 | -64.0332 | 2024-10-09 04:40:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c94c61f-c5ae-33ab-aed9-1ed7e24b045b | -11.61398 | -55.02006 | 2024-10-09 04:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 493df443-b890-3f94-9939-15283ab10ca7 | -11.60178 | -54.6944 | 2024-10-09 04:40:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b44e7dd-887f-3dfc-b3f5-19d7178b7056 | -11.59796 | -54.69368 | 2024-10-09 04:40:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 539c9570-f513-3632-98e3-633cbe66eac5 | -11.57447 | -58.95338 | 2024-10-09 04:40:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 866c7ff3-72fb-3d31-a3bf-2326a40a18a5 | -11.57391 | -58.95635 | 2024-10-09 04:40:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 07348004-9ceb-3576-a97f-bd9b25dd6718 | -11.56943 | -58.95237 | 2024-10-09 04:40:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8d47b5a2-fdc0-3e7f-a663-f95203d8a29b | -11.56888 | -58.95533 | 2024-10-09 04:40:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5d1341ff-34c0-3705-beb5-4bfec90daf3b | -11.56832 | -58.95833 | 2024-10-09 04:40:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 191c5061-7d73-32df-af33-ca68e66b8937 | -11.56381 | -46.9402 | 2024-10-09 04:40:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03fab3c6-a486-3084-9893-d586bb8da972 | -11.5595 | -49.90419 | 2024-10-09 04:40:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 32e4fb08-e29b-3858-8365-23f949b60b03 | -11.55895 | -49.90773 | 2024-10-09 04:40:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 066dd2d8-98a0-3223-944f-f5f7bdc202a0 | -11.55562 | -49.9072 | 2024-10-09 04:40:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0b2ad36-b050-388b-ba7c-ec79b98e7e48 | -11.55228 | -49.90667 | 2024-10-09 04:40:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6433a9cc-e4e9-3ca2-8678-a159d391e620 | -11.55173 | -49.91021 | 2024-10-09 04:40:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ad8cfcf-93ae-3352-abbb-9d57766c8b7a | -11.48906 | -59.09881 | 2024-10-09 04:40:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 874aeac0-36c9-3159-b7cc-7382234039ea | -11.48478 | -61.97595 | 2024-10-09 04:40:00 | NPP-375D | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3cdaede6-0e1f-39ba-94c1-2d113a5fccfd | -11.48477 | -61.97886 | 2024-10-09 04:40:00 | NPP-375D | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4aa1ee21-ad51-3b3c-bf7b-0b02af70d4db | -11.48383 | -61.98066 | 2024-10-09 04:40:00 | NPP-375D | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 28196481-5da7-3a0a-9ec0-c03d7ff854d7 | -11.47866 | -51.85957 | 2024-10-09 04:40:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbe490d2-49a1-3f29-b36e-e6c21e19e133 | -11.47863 | -61.97771 | 2024-10-09 04:40:00 | NPP-375D | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 74cce050-9197-3e31-abb4-f1b1815c8e76 | -11.47239 | -49.48949 | 2024-10-09 04:40:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ac17cfbc-f09d-3a79-be20-61f0888478c3 | -11.46958 | -49.48537 | 2024-10-09 04:40:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be0302c2-738a-370c-bedf-55a90008c821 | -11.46903 | -49.48896 | 2024-10-09 04:40:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dc61987d-9f8a-3b7f-ba94-93fd1d4081d8 | -11.44967 | -47.90752 | 2024-10-09 04:40:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23a19f70-8238-364c-b684-228496644936 | -11.44186 | -54.4757 | 2024-10-09 04:40:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5faffc8-5c12-3147-8788-c5cece269934 | -11.44107 | -54.48035 | 2024-10-09 04:40:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 682e8873-1a6c-334f-977e-96ef5fddbb58 | -11.42619 | -60.45428 | 2024-10-09 04:40:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 950cefb7-3f4c-3866-b62e-95676e9bab09 | -11.4203 | -55.21556 | 2024-10-09 04:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83e0cb69-17b1-33c4-b2b4-a76030298d21 | -11.40336 | -51.24076 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 17ec39b3-ba63-3d0b-bbfa-c201ac91be63 | -11.39378 | -60.41227 | 2024-10-09 04:40:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 272c2cb6-4037-38c0-800b-ffb6dd83cb99 | -11.3882 | -60.41128 | 2024-10-09 04:40:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ae5878c6-6983-3eeb-b7b3-95865cdd6d43 | -11.37546 | -51.09383 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59f285af-4a7b-3ed1-8eee-ce9a88252bda | -11.37213 | -51.09328 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4687e1f8-79e1-3719-8ac8-4f4eba805e58 | -11.36936 | -51.08919 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87624444-97c4-3ae7-abf2-232a516e7349 | -11.3565 | -51.00737 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e08048b2-56c2-3fa9-b6f0-1e0a2d6bfe2f | -11.35317 | -51.00682 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| a2888e58-24c8-3a6c-8137-b704353646b7 | -11.3526 | -51.01036 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 5a7086be-5c02-3137-9b33-efe4c0a48c7c | -11.35204 | -51.0139 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ab8d49ef-9c5f-3df2-88fc-8b6694eb32eb | -11.34927 | -51.00982 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76975a62-4059-3b7e-9905-c28045902964 | -11.34871 | -51.01336 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a150b21e-81c1-3229-8523-e68769bff18c | -11.34814 | -51.0169 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e3074328-4944-3213-87f0-324a3817ba47 | -11.34746 | -58.9865 | 2024-10-09 04:40:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd58a33d-52a3-38aa-a8ec-00ec5144a34d | -11.3469 | -58.98948 | 2024-10-09 04:40:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8dec3223-1678-3eb2-9cae-f5e81c7e2232 | -11.34184 | -58.98845 | 2024-10-09 04:40:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 077f6b34-06c6-357b-ac4f-0a9ec2401d74 | -11.34126 | -58.99152 | 2024-10-09 04:40:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46cae8bb-9474-3051-ae70-2e8e22217a54 | -11.3397 | -55.23286 | 2024-10-09 04:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67a8ed0e-35a9-3c13-9e7a-fc1bdef2661c | -11.33435 | -58.91681 | 2024-10-09 04:40:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e37fc48f-fe9f-35e9-a3e7-6a6a2e3de127 | -11.33378 | -58.91979 | 2024-10-09 04:40:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 792c9bd7-84a9-3a54-8b8c-87213e7ab5e4 | -11.32581 | -55.20764 | 2024-10-09 04:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d83555aa-f2d7-3204-aa66-e1aaf85d8cdd | -11.32547 | -50.96596 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a277750a-6653-37e3-b0ab-538fcb36c862 | -11.32353 | -55.20873 | 2024-10-09 04:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 306fa5b1-864b-369e-bda2-dbeff607a22d | -11.32213 | -50.96541 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bb32b54f-5464-32f3-8c75-e0ee5aa1570d | -11.32186 | -55.20689 | 2024-10-09 04:40:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96bb2e31-66bc-38b6-80ab-d553fc65a185 | -11.3172 | -51.31851 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40323246-228c-3bdf-b3ed-4a0b12746cc1 | -11.315 | -51.31081 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dfbe6670-4c4f-390f-8d14-f684df6d7a08 | -11.31443 | -51.31438 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e355d137-4374-308f-96a5-518b3405d855 | -11.31165 | -51.31026 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| baf00f1f-d3bb-37e5-89d2-a988d583805b | -11.31108 | -51.31384 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9f398c6c-8af0-38a3-8357-70a68d760519 | -11.30788 | -51.41993 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 524db973-dad9-3ac2-85f0-847a1bcb943b | -11.29623 | -51.08482 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 51c2b9bc-0190-3380-8882-0e3036b50627 | -11.29346 | -51.08072 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 60d5e610-d9c5-38a5-a201-5e72b97d479a | -11.29289 | -51.08427 | 2024-10-09 04:40:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 358084ff-4bef-3504-94fd-7eda9c4fdaaa | -11.28875 | -54.57729 | 2024-10-09 04:40:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb2f0307-91d9-3385-9761-d76b25a6ccc7 | -11.28493 | -54.57662 | 2024-10-09 04:40:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README147.md)
