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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3707fb7e-2f4c-3ba4-a49d-d8a406f3a5ba | -6.82446 | -59.95984 | 2026-08-23 04:44:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 775e913f-78a4-3766-bbd8-b2803117c4a7 | -6.86912 | -59.40877 | 2026-08-23 04:44:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8378cf23-f522-3241-afa0-c8370677d084 | -7.39667 | -45.99019 | 2026-08-23 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7fee218-bd84-381c-b94d-00081e368f91 | -7.03698 | -48.02147 | 2026-08-23 04:44:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e6be2e6-0b2a-3b51-8ca9-020b639ad908 | -6.67532 | -58.73791 | 2026-08-23 04:44:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 30.2 |
| ead35982-2f1d-311f-bfe2-0c4c2dcf0f6d | -6.4253 | -56.18576 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63115e57-9c01-36f1-853a-36ad43d6658f | -6.19849 | -53.49172 | 2026-08-23 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 586e0ad4-cc52-386f-b132-9e970c722aa8 | -6.171 | -55.5713 | 2026-08-23 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 63daa4f5-ebf8-369c-8beb-e8701880e1dc | -5.01156 | -47.06844 | 2026-08-23 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e9ac2c1-075f-36eb-844b-b1472dd51651 | -8.16588 | -52.05199 | 2026-08-23 04:44:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e00ff60-55ee-3178-8fac-bd600af8d068 | -8.47301 | -46.99173 | 2026-08-23 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 189e9b3a-4f54-3b2f-94b7-0db8af7f10e2 | -16.07158 | -48.45021 | 2026-08-23 04:46:00 | NPP-375D | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d2851af3-bd8b-3178-ac3d-0c19f5bcbf55 | -13.45007 | -43.84124 | 2026-08-23 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cf145557-8593-385d-985f-fe92c2891868 | -14.15021 | -48.06466 | 2026-08-23 04:46:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa757b2f-3f99-33ba-811e-e00acdadabfd | -10.79756 | -50.96824 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 911e18c5-1386-37f6-9946-3a33800f3c13 | -9.51476 | -51.67564 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ab5df3be-2449-355b-936d-41f0ef960543 | -9.39685 | -60.55976 | 2026-08-23 04:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 822ed5b2-c302-35cc-add3-ee27258c6514 | -12.36395 | -46.45411 | 2026-08-23 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4e3a6231-9384-338d-b1cb-dac94e2bfc89 | -14.9944 | -52.692 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0935d47f-74ac-3a4e-a75a-b839c7cae15b | -16.64696 | -49.30033 | 2026-08-23 04:46:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9bf66bcb-041d-3bc0-a353-75648d66d63b | -12.37108 | -46.45528 | 2026-08-23 04:46:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 122234df-e485-3e41-aa6c-90326e5f0fee | -14.68799 | -48.97116 | 2026-08-23 04:46:00 | NPP-375D | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| db2a80ff-76df-3369-8bcb-a3a0b5da66bf | -7.57248 | -61.20003 | 2026-08-23 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b145289-5d68-3c20-b4a9-8e38ac5da6e1 | -9.49124 | -51.59557 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 282c1d02-0828-357c-b24c-46e0d816c0bb | -10.84067 | -50.97942 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 80ffabcd-faa0-3f68-a4e5-7866b97ac2f4 | -14.37337 | -51.77882 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b9867a09-4c0a-39a7-a536-74700e09b6dc | -12.24265 | -43.11915 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 08511ed9-b65f-3b14-97a6-05ecfb870294 | -14.31312 | -51.84317 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6290f655-e472-30d4-b2e4-f68ae86d6660 | -14.14508 | -48.05233 | 2026-08-23 04:46:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b803b494-23b2-38cf-a1a2-0a836c19904f | -9.63773 | -48.31017 | 2026-08-23 04:46:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a5cffdf-f978-3868-a822-c70702e42368 | -9.04254 | -50.87978 | 2026-08-23 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 873ac8d7-466f-3699-9bd2-5c216979bdff | -9.2354 | -60.38827 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 75f4939c-721d-3872-ba71-b52080cedb9b | -12.83418 | -48.48003 | 2026-08-23 04:46:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b951d95-171e-38ce-a580-ffaa9d2d757d | -9.85979 | -60.12074 | 2026-08-23 04:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f725a65b-a4e5-3f51-b497-51e38e7d620e | -9.45204 | -56.90886 | 2026-08-23 04:46:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 054f4039-ab7f-349a-85db-da357f73e05d | -9.17978 | -59.45471 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 7ac9812e-7a53-3fdd-a5e3-f400b59eed06 | -12.74175 | -48.39938 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4785f58d-eb81-3977-86d9-7154fe2c3769 | -9.03727 | -60.45352 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73c04219-cb76-3537-844d-a02fcb05870e | -14.35277 | -51.77519 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 695d295c-741d-3d9a-b82e-8c5d85adf082 | -11.439 | -44.52845 | 2026-08-23 04:46:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 064a74ed-218d-3e4d-94c3-6392552fa7c9 | -10.51989 | -50.44513 | 2026-08-23 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4832e80c-2d02-3e12-969a-a137ff4ca41b | -9.79965 | -46.61352 | 2026-08-23 04:46:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9fb02723-0a23-3b9b-8727-9225f4152627 | -16.40224 | -51.83756 | 2026-08-23 04:46:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20324aec-39aa-315f-a075-bc6ffa6dcdbd | -9.10519 | -61.58944 | 2026-08-23 04:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0d3227d5-02bb-3b23-93db-913f190e9ec6 | -8.19944 | -54.98004 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d298b584-3657-3d9b-a603-978bebe2bb61 | -13.43488 | -43.85843 | 2026-08-23 04:46:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 8e016218-7edf-3539-b1e1-524b83984262 | -13.24941 | -51.59288 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0092067e-c50b-3a38-85f7-31d1c0e6ee53 | -14.9965 | -52.69509 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 24fb3a80-381d-3abb-9929-46cb46717459 | -14.98092 | -52.66399 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6a38047c-986b-366a-8b2c-a21652d5aab9 | -9.79677 | -46.60908 | 2026-08-23 04:46:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac3fbe95-e261-3f24-91a5-d3fb8f80e1c7 | -9.15959 | -59.46415 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cf95c045-6f37-3725-9089-23109f9970c4 | -8.53934 | -54.84858 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9740957c-1e8a-326d-99a6-dc704828f651 | -10.34624 | -48.23184 | 2026-08-23 04:46:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44daf2d8-aa04-34ee-809c-6893dabdd3b8 | -7.44157 | -59.7774 | 2026-08-23 04:46:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 67415996-ecbf-315d-8523-3f3bc2a06b43 | -13.82545 | -40.11836 | 2026-08-23 04:46:00 | NPP-375D | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| fb97da50-d512-3480-a55c-8473b243d438 | -13.18668 | -51.42632 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| cf9a373b-658c-31f9-b3b7-a4fa06ecb124 | -14.95689 | -52.6555 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3fa29cfa-1ef4-3d98-9f9f-4727feb01575 | -10.05219 | -46.41783 | 2026-08-23 04:46:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c372cf04-0a29-3d6e-aed3-159a78f65a4b | -8.53717 | -54.83485 | 2026-08-23 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d02a32e-cf71-39a1-8907-481fe4b01bd6 | -8.93089 | -60.72275 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b89da2ad-929d-3ddc-b14b-90560f2a94c7 | -13.47622 | -51.74549 | 2026-08-23 04:46:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7743b920-3db2-31a2-9ca0-9e762d59097f | -13.17704 | -51.42075 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 7a4a2a26-a127-3dc3-a69a-b815f177d86a | -12.75132 | -48.38211 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ec70c7f5-4009-3e7b-b3dd-0b9e9a017b53 | -7.60089 | -60.94095 | 2026-08-23 04:46:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a9c77ea6-98dc-344c-9900-6c05fc76159d | -9.11071 | -61.59678 | 2026-08-23 04:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 52b66e7c-9741-3147-80b8-caabca03d124 | -9.41814 | -51.64777 | 2026-08-23 04:46:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db3dd1a3-c5f5-3341-ab48-0cfd2dd8e353 | -12.0029 | -53.42115 | 2026-08-23 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1218686d-af73-3cf9-a54a-11964c3c0d07 | -9.40314 | -60.56105 | 2026-08-23 04:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ecc4b500-97a4-3021-a94d-7b3654218d2a | -14.96396 | -52.65673 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d964b7b9-4d89-35fa-9c18-a4a531f83b05 | -9.1187 | -61.59183 | 2026-08-23 04:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86a2680d-936f-3132-ae4b-91854b98f74b | -14.57615 | -53.02286 | 2026-08-23 04:46:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc23d502-d04d-3c90-81fa-d71772bcc8da | -12.7872 | -48.38379 | 2026-08-23 04:46:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0685fba3-0ac3-3b9d-a6d7-1df7c8cfbeab | -14.49842 | -59.83447 | 2026-08-23 04:46:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a9ec347f-e839-3892-8872-4e9c5e8ca15a | -9.12542 | -61.59315 | 2026-08-23 04:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d20542e4-9b65-3c1b-b199-83cac4651a97 | -15.32378 | -46.0834 | 2026-08-23 04:46:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf3f2705-a776-3b22-a87d-f29f38385ae1 | -11.14722 | -46.1967 | 2026-08-23 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11ce437a-ef7b-3073-b11d-0d88340c21e8 | -11.55578 | -46.94812 | 2026-08-23 04:46:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 504d3b37-4adc-3957-8e77-caddff061440 | -11.27832 | -50.74347 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f795ffc5-17b5-35a2-a38c-9ef8f0879670 | -14.40565 | -51.79159 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 00ee0ffc-c64f-380b-871f-c35be4d28413 | -10.7935 | -50.97144 | 2026-08-23 04:46:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce97473d-b960-3f87-b1c5-a2085bbf1978 | -10.39849 | -50.41704 | 2026-08-23 04:46:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38990dd2-6327-34b6-9acb-388f9df564e7 | -12.58748 | -47.88509 | 2026-08-23 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a1d59bc-11f3-3cb3-a841-c76edaea4ea1 | -15.24352 | -52.85977 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a700bf9b-ad49-38c3-aa73-9947e7dc8d88 | -16.40502 | -51.84181 | 2026-08-23 04:46:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a7cf455e-c158-33c2-8303-b851fdcf7f6c | -12.06759 | -50.59876 | 2026-08-23 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47644688-7131-3177-9e0d-e0ac7f50c265 | -8.98076 | -50.7717 | 2026-08-23 04:46:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69f51611-3dc9-3e45-a8ba-84695088fce7 | -10.8464 | -44.74352 | 2026-08-23 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da09b3ae-18e2-37ab-9ef4-1a11be2c8c13 | -13.20381 | -51.42929 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30c25114-6028-3f6a-bc25-052a45ed31b1 | -9.85927 | -60.12296 | 2026-08-23 04:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e455a55-2179-304b-b609-5a0c123d6639 | -16.11399 | -43.63068 | 2026-08-23 04:46:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6fe5395c-d903-3b1c-8b40-1062f9c819e2 | -14.56675 | -53.03432 | 2026-08-23 04:46:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15b978bb-58fb-371a-98ae-ab59ff6c3ba7 | -16.06029 | -50.43814 | 2026-08-23 04:46:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| abd7d0cf-fcc4-3c21-a9cd-ce73044c3397 | -14.97247 | -52.67091 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90257707-f452-398a-9cda-0fa0e2489306 | -12.23921 | -43.17847 | 2026-08-23 04:46:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| abc906c4-235a-3b96-bbe3-50fcf2bf4074 | -13.17983 | -51.42513 | 2026-08-23 04:46:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e80ed10c-4f98-3f22-a9b1-1059ac41477a | -14.95476 | -52.64667 | 2026-08-23 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89eb6ec2-3ff6-35f7-ab84-599ca31367f9 | -9.21673 | -59.79057 | 2026-08-23 04:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f89e2bd9-ac52-3516-95ac-eb59cae64f7b | -14.35621 | -51.7758 | 2026-08-23 04:46:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5ae191ef-f781-3327-9b2a-c3460445d707 | -10.71553 | -47.74508 | 2026-08-23 04:46:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7389cede-e0a2-32de-97d0-7463d7a23ef9 | -10.99521 | -47.58036 | 2026-08-23 04:46:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README30.md)
