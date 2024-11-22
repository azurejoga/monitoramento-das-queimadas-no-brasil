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
| 8fca014b-eee0-3e7a-8791-5c0f852b9245 | -4.91741 | -44.38073 | 2024-11-22 04:12:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e50e2059-865b-3253-9770-14f6b574c433 | -3.8034 | -51.2649 | 2024-11-22 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3cc29251-4b76-3569-8e49-1187b0a65a76 | -3.29527 | -54.72659 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| af7387ff-c632-35d9-a383-3facdf25eb58 | -3.51459 | -50.80867 | 2024-11-22 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d46825e8-d488-36a3-9ca7-4e581967152c | -3.31416 | -47.01944 | 2024-11-22 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b6db91f-55d3-3199-9e0c-e5aef5e3ad80 | -5.81664 | -44.74528 | 2024-11-22 04:12:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d7cf5808-c611-36a4-8f8a-1b0922b768cf | -3.95952 | -45.32759 | 2024-11-22 04:12:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cacbddcc-8876-3467-8ae7-6de7fa517fc5 | -2.30695 | -53.6033 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8d7de45f-8e89-3d62-b488-d97d109c655c | -3.1824 | -46.55229 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d3c30645-e600-3ca4-84e2-ebbe018df7a6 | -1.2009 | -51.95115 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dd3e4041-710b-3232-90e8-53f0b03a5d95 | -1.7755 | -53.60346 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d47e7d2b-9174-3413-b7c4-becb2ce6139e | -3.00641 | -45.12753 | 2024-11-22 04:12:00 | NPP-375D | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a2d97c3-39e9-391e-9010-b1d46bc20234 | -3.22478 | -54.23793 | 2024-11-22 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2c6f12e8-c700-3aed-81f5-50e4bc978c0c | -1.62193 | -52.42702 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e5908e04-0230-3437-a9ce-d45221a39eb9 | -4.46469 | -48.02984 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be2ce851-80bf-3d5d-8086-d8554f83212e | -1.64039 | -52.61444 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 13ec6788-e888-3bda-ab80-893ed1400ea0 | -5.96064 | -48.05613 | 2024-11-22 04:12:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ee3057cf-1046-388a-a6b6-810d73092567 | -3.23482 | -54.2567 | 2024-11-22 04:12:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| bdaa1a47-d376-36e5-a90b-38d36261a4dd | -5.8189 | -44.75323 | 2024-11-22 04:12:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bcd79bb-5eb0-344e-96b4-75a7e281abf8 | -4.25387 | -48.70394 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b349aed2-a1fc-3512-9412-5b679a4f9271 | -3.10248 | -53.74409 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09d66e87-0a3e-3232-9a6e-a5932ce79a2d | -3.75816 | -46.12234 | 2024-11-22 04:12:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f4497594-ef8b-366f-9af9-e463a5c17d63 | -3.88918 | -46.66621 | 2024-11-22 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20dcc518-7e82-3df1-9be6-8a09e070ff5b | -3.91386 | -42.44092 | 2024-11-22 04:12:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f4359a80-ad13-3282-99b8-3e9c68630eac | -3.88614 | -43.99151 | 2024-11-22 04:12:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2fda6b21-2370-3cae-b0cf-0591c2bba556 | -4.81838 | -43.69292 | 2024-11-22 04:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8b51f81-3b02-356b-b8d0-24940322d4ab | -2.68516 | -46.87508 | 2024-11-22 04:12:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 890cab55-4e41-3216-b948-3179608f4704 | -6.9232 | -46.11232 | 2024-11-22 04:12:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55640547-6928-344d-8154-e700679b5c9b | -2.12245 | -47.67194 | 2024-11-22 04:12:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| af9ec304-3e9c-3630-a72c-f73baf5b1e3a | -1.18942 | -51.94922 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 01bcdeb4-c04a-3af5-9b0f-129becc0ba6d | -1.19413 | -51.95827 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 1a790fee-659b-3286-98c3-a43917d01b71 | -1.64143 | -52.6263 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3366f3c0-385c-348d-9857-039ec1265a12 | -2.7378 | -54.13181 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a905960-c56f-3b63-af1a-4bea8e356954 | -0.266 | -51.56609 | 2024-11-22 04:12:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae26e9b9-116a-3573-9a41-1dcbf5e0fc29 | -2.30437 | -45.50545 | 2024-11-22 04:12:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 60e04cca-a413-3317-b599-12be367d870a | -3.85405 | -51.40393 | 2024-11-22 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a40e0f2e-fda9-3860-baa0-8e20e59569b2 | -2.93834 | -48.01501 | 2024-11-22 04:12:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fb0e9dfb-e64d-30d6-b1de-44539ac96521 | -2.7383 | -54.12979 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ae3c928-5c72-3bbc-89fc-137f61bd4983 | -3.47107 | -45.91345 | 2024-11-22 04:12:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a85c495e-0819-3116-ab32-d18006aa15a9 | -1.21665 | -51.74157 | 2024-11-22 04:12:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1ed0247-82c8-385b-8183-7f2822d5a786 | -4.39624 | -44.12307 | 2024-11-22 04:12:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c410b7c7-98bb-3834-be10-d87ad142f11c | -2.78944 | -48.10398 | 2024-11-22 04:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c98d0d69-c9d4-31af-83a0-17dd838e2e3c | -3.05206 | -51.32979 | 2024-11-22 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bafc4917-5411-3984-9f66-ca14dcb6161d | -2.2019 | -53.65174 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27c726f7-1370-339b-9990-b5f1fc713cfa | -3.19007 | -51.61384 | 2024-11-22 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0e5772a9-e281-361e-8264-39d1f3e893f5 | -3.85394 | -52.35754 | 2024-11-22 04:12:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39fe4a63-b5e6-39ce-943a-15af64c66c75 | -5.96124 | -48.05253 | 2024-11-22 04:12:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eeede481-33da-31c8-b7ed-7b732e58ce62 | -3.65272 | -51.14266 | 2024-11-22 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 60b0e1f6-788e-35e8-8740-f8adca9f2e6c | -2.63813 | -46.19854 | 2024-11-22 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61954891-bf59-3374-888a-616337118633 | -3.10611 | -53.99261 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 782b448e-7983-356a-a21b-af4f7c959341 | -1.09521 | -53.16588 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 30da1407-d0ce-3922-964d-27d66fd87926 | -4.53914 | -42.98177 | 2024-11-22 04:12:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b2f37e9c-7fbf-37ad-9ab3-eafd4efdb8df | -2.6938 | -46.25811 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2497fece-67bc-39f8-841d-e0467cbd6199 | -1.21006 | -51.96904 | 2024-11-22 04:12:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d7403c22-a80e-39e9-8043-af1d7f0a59b8 | -3.64131 | -51.45605 | 2024-11-22 04:12:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7221413-6f92-3204-960b-9c04eb1ae519 | -2.43412 | -46.52619 | 2024-11-22 04:12:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fcbb6d10-ceec-37d9-bd58-054e7a6b81e7 | -3.58074 | -54.68016 | 2024-11-22 04:12:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ed2780fc-2726-3986-b0be-520ac51628ad | -4.28725 | -48.23926 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 007cd6f5-401f-31c9-a0b1-a7089be34c04 | -5.40555 | -45.12862 | 2024-11-22 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ecb68e97-9de5-31df-8783-ec0649b009c9 | -6.38002 | -42.2262 | 2024-11-22 04:12:00 | NPP-375D | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 11fdfa67-e217-3027-8bcf-cc56bc957e7f | -6.11743 | -42.5211 | 2024-11-22 04:12:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| f24a7544-e7ef-33bc-9642-7546b9b583f8 | -3.2174 | -54.24237 | 2024-11-22 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| de92c9da-e7fd-30ac-8ed5-d113761aeeb5 | -2.00858 | -54.52494 | 2024-11-22 04:12:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ae85b564-f318-3cab-8b30-be93ca8fe029 | -2.22079 | -53.73186 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ea0a2ee7-b749-311e-ac15-60aad1d89017 | -4.11309 | -51.05127 | 2024-11-22 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2f47fb07-04cb-3e39-a9b8-655214710fce | -2.40632 | -48.32877 | 2024-11-22 04:12:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de145cf6-deb5-3cf6-bdea-e2cb1ba9e8bd | -4.00792 | -49.91652 | 2024-11-22 04:12:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c98a46e3-033b-32ab-9032-88a4b26d7730 | -5.71109 | -43.83011 | 2024-11-22 04:12:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2cd8936-3ee5-3bcc-b7f7-7855bde7d61b | -4.34126 | -45.53072 | 2024-11-22 04:12:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b997bb11-5299-32f3-adb8-caccc6a94f81 | -4.40079 | -44.11631 | 2024-11-22 04:12:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 73f41910-3d0f-3010-9ea1-8b6d2cb29eb0 | -0.92019 | -51.736 | 2024-11-22 04:12:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a6760a0-4c6d-34f0-906c-235884aff15e | -2.35229 | -48.55155 | 2024-11-22 04:12:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e9d72adc-fbff-3687-878a-4690d7a94a66 | -4.23882 | -48.63255 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6ed93a78-0642-3de0-9f0b-3282673e0526 | -1.22408 | -51.74318 | 2024-11-22 04:12:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e906d82c-8e50-37dd-a358-4ca0490e05bc | -1.58842 | -53.81603 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| e0d7b3c3-1f1e-39c5-b375-5161c00dc2fb | -4.07358 | -46.83491 | 2024-11-22 04:12:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c20aa7bf-22c2-38f5-847b-9c52e594b11e | -6.27836 | -44.73723 | 2024-11-22 04:12:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c411ea59-2125-36eb-a5ff-0cc150bd6ddd | -3.84042 | -51.14207 | 2024-11-22 04:12:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75cd70b8-021a-3a28-87e1-e7edeaf11bda | -1.9207 | -52.08404 | 2024-11-22 04:12:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a676e8a4-d32f-3852-a2e1-2aef1f4bc72c | -2.66382 | -46.15983 | 2024-11-22 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd32fa5c-79c2-3cbe-9e95-400bd0f87b75 | -4.24684 | -46.11364 | 2024-11-22 04:12:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 833a6a6d-3c20-31b6-b19f-03c19c631491 | -2.69684 | -46.23935 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bdb9e0af-2315-3b9a-b6d9-5fac70c0ec07 | -5.73911 | -46.20729 | 2024-11-22 04:12:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a928b12a-93b5-337f-b10e-c4c761eb55ef | -2.74473 | -54.13091 | 2024-11-22 04:12:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4c555043-e939-36c6-ba8c-dbd2efd95f87 | -2.706 | -46.23119 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d5608a44-2a6e-33d7-80fc-0578aafabed0 | -3.28421 | -53.85187 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9640bd51-bb36-3919-b353-fae9e28e982d | -3.40718 | -46.24386 | 2024-11-22 04:12:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 012a0897-0464-3e1d-a3c7-6ca2012cf3a9 | -5.53709 | -42.94025 | 2024-11-22 04:12:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a1fa99e2-dc7b-3086-a45d-6bbb26c9c11e | -1.77824 | -53.59938 | 2024-11-22 04:12:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a32ba656-8bee-3464-ac42-d2ed465c2019 | -3.78792 | -44.01704 | 2024-11-22 04:12:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 756895c9-5d93-3f62-863e-eb731e9a6b2e | -2.78526 | -51.41074 | 2024-11-22 04:12:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ee784ad7-f975-3594-9725-75ef62d052a1 | -5.51007 | -45.48578 | 2024-11-22 04:12:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ced3eaaa-c762-3d7b-8d99-47b3d24c01b0 | -2.65631 | -46.2472 | 2024-11-22 04:12:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eff3f205-a09e-3ad6-88c7-ee45716477a3 | -3.90347 | -40.97588 | 2024-11-22 04:12:00 | NPP-375D | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 427e5dcf-b2cc-3486-a32e-3e98619c2827 | -2.63441 | -46.22192 | 2024-11-22 04:12:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b78224af-7192-3ecb-838a-b02dcfb984d7 | -4.21663 | -48.65629 | 2024-11-22 04:12:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c8fe2704-d7a2-3f6b-a194-4d2b4943e419 | -4.40702 | -44.12103 | 2024-11-22 04:12:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb5addae-d1d6-3c51-97d8-35f973398b84 | -3.57417 | -54.67899 | 2024-11-22 04:12:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fd1ee695-c1bc-31f7-8efe-82c3fd455717 | -1.22797 | -51.74344 | 2024-11-22 04:12:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1da8be03-05f5-382d-b837-9da68ee8fe22 | -3.28047 | -53.83598 | 2024-11-22 04:12:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README25.md)
