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

## Dados Diários - Página 84

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90312da6-c68e-3a41-9f7f-633e2ef5544b | -14.90537 | -47.231 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48378855-911a-3a39-bbd3-a89ea5d4d1c6 | -13.94539 | -48.09503 | 2025-10-02 04:32:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c89e060b-b500-33f6-8cb6-64835a733a4e | -15.26437 | -48.00751 | 2025-10-02 04:32:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f77628f9-23a7-39a5-b603-0a3d8afdd2f2 | -13.17276 | -47.852 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ac82d004-6656-33f3-94ff-f9bebb16f12c | -13.30738 | -47.85622 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 431dd94f-8ac4-3010-a16a-b5465e2ee2bb | -14.31356 | -45.88938 | 2025-10-02 04:32:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cda844b2-0349-345b-bfe5-86b7ed08c190 | -15.25559 | -49.30119 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b03d53fb-2aaf-3009-b21a-7713963f04b2 | -13.69625 | -48.6213 | 2025-10-02 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0e15d5f1-1aee-3591-b40b-76cb27daaa09 | -12.70334 | -48.58576 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3fda7e7a-e573-3e70-adf9-1bab891dc5af | -13.3118 | -47.82787 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74419501-c682-360a-b858-276a842bf988 | -15.31646 | -46.28461 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e57f07e9-886c-35d9-b96f-1ca37dfb0172 | -19.69686 | -43.98939 | 2025-10-02 04:32:00 | NPP-375D | SÃO JOSÉ DA LAPA | MINAS GERAIS | Brasil | 3162955 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e35b9959-5c06-3067-b03e-a44f1f707f9f | -16.36419 | -47.08146 | 2025-10-02 04:32:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 525193f4-c12a-3ee3-8ef9-131317b4ffea | -12.86932 | -47.00402 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 043c9618-72ec-393b-a1b4-86751c04e62b | -14.17955 | -46.66899 | 2025-10-02 04:32:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4543ec83-56e5-38c0-9735-e5dd209c5187 | -15.94574 | -43.33667 | 2025-10-02 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1cdb557d-9ee9-34b0-8694-cd9700534960 | -15.4095 | -47.06234 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9f1bcd8f-acf4-3e6c-b791-074d88578312 | -12.41428 | -54.35672 | 2025-10-02 04:32:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c63cb230-bff9-3a5b-8ae1-c662df47c947 | -13.61608 | -47.28856 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b624a96-66e4-393b-94c0-1769cef084fa | -13.17833 | -47.83836 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c6d03c86-03dc-36b6-9f49-37598951b56b | -13.70349 | -48.61888 | 2025-10-02 04:32:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 099dd794-b3dc-3b27-ba53-976d2a4cc54e | -15.25636 | -49.27499 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 70272c67-2645-3a2f-871c-314c0c21d04d | -14.40058 | -46.07664 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 81ea37e4-56ba-3457-8801-976d4d3c3748 | -13.31766 | -47.33255 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9b95370f-237e-39ac-85e9-fd76a090cf71 | -12.68384 | -48.57885 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 9b30ebd7-e3c0-3fbb-ab34-22578b019a81 | -13.75965 | -51.21564 | 2025-10-02 04:32:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b5c7cd2e-f5bc-3e32-9a74-f4e83279d456 | -18.50872 | -44.03819 | 2025-10-02 04:32:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c75ab873-4810-3b75-93b4-f0955005da0a | -12.85709 | -47.03865 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 598ed4a7-3f18-3bf4-83fd-ff20aabe4765 | -13.36629 | -46.62959 | 2025-10-02 04:32:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1f1a2bcd-642c-3c7f-a5f3-cd02fcbe8968 | -13.37605 | -47.28728 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 669951cd-34b1-300a-ae6f-d7694a9af093 | -15.86132 | -48.12766 | 2025-10-02 04:32:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6dbbcace-ee24-3256-b858-f57ae708e455 | -13.30044 | -50.67724 | 2025-10-02 04:32:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5b2b1619-60fa-3416-9b84-c5ab821ac8df | -17.17636 | -47.03184 | 2025-10-02 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 962f0f9e-e848-3e48-834c-f8bdfa5e4506 | -14.47179 | -48.42316 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7aa766fe-e95e-3178-b2ab-7d694711dbfe | -12.41662 | -45.17019 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63e89236-86f9-3574-bebb-a51fee7ced68 | -15.33434 | -46.25936 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 28fc9139-2ae4-3911-b754-7a9202ecadea | -15.28195 | -49.29802 | 2025-10-02 04:32:00 | NPP-375D | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53531c06-7ed0-3340-bf2d-da92dd6bf5fc | -13.21422 | -48.44257 | 2025-10-02 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 46fa55dc-e5d3-3867-821a-56b6bd5fd0f5 | -11.87127 | -49.912 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87c195cb-d4d5-35e5-a12d-2f1bb2cc49bb | -13.37829 | -47.2949 | 2025-10-02 04:32:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 91b90d65-9605-36b2-8980-e5bfe85f00df | -13.68417 | -48.05925 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2295eccb-2ae9-3a9f-b117-4f6ee37f22e0 | -12.40481 | -51.07544 | 2025-10-02 04:32:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3c2a723b-11fe-3c98-89af-b09990a22973 | -14.98692 | -46.90208 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d77fbef-4c1f-3200-b4de-e746c6b55a9a | -13.86305 | -51.24584 | 2025-10-02 04:32:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc67e42a-9097-3476-8329-ce72d1c92e3b | -15.01156 | -55.27515 | 2025-10-02 04:32:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 48e7eb09-02c9-3c4d-9ee0-bb8f7ede332a | -15.94527 | -43.34032 | 2025-10-02 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 8b84552e-66d1-3209-976e-41d9d4b7efbb | -15.86075 | -48.13125 | 2025-10-02 04:32:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a9144205-9970-32b9-a571-32b45e058629 | -15.93396 | -46.21237 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00587eeb-8340-338d-8b14-e384841d3606 | -13.56704 | -47.27341 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab22f978-4302-3bf6-bb2a-6a9cbdc9a1ea | -13.05919 | -47.06397 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33d7a0f3-8292-3d4e-809a-89bb0cdb08bd | -15.31475 | -46.29627 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa56e7a2-ee25-3702-b79c-c0b334ccdd11 | -12.02119 | -52.51514 | 2025-10-02 04:32:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aab858ad-ce53-32fa-8a74-c684a312eaef | -13.19386 | -47.84819 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 999a79b7-4f10-3ab7-8e3c-091f3943dd89 | -13.13235 | -47.41949 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ee67015b-ef2d-3b5e-8160-44641d165170 | -13.23009 | -48.50724 | 2025-10-02 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eced3a1e-7303-3da7-b400-b5ab907d24ea | -13.84317 | -47.51971 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91369e71-66ae-394d-996d-94ca38ba2af5 | -17.1735 | -47.02749 | 2025-10-02 04:32:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa8934aa-5979-368d-93af-9e63458fce8b | -15.93681 | -46.24113 | 2025-10-02 04:32:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0788941-a1b1-3a83-a812-535f9a81165f | -19.28839 | -43.74807 | 2025-10-02 04:32:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0a6cbb3c-a6ad-36d3-a8ff-731d8937d1f9 | -19.46513 | -43.87598 | 2025-10-02 04:32:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e13e454-d6ce-301b-863d-cbd5b3efef2b | -14.42463 | -46.35828 | 2025-10-02 04:32:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c2edc76-7393-35e3-9d75-2d67889f667c | -14.90593 | -47.22736 | 2025-10-02 04:32:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a7a40d3-8347-3d39-8faa-592ee9cd8a1b | -13.75219 | -48.01258 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f0946bfd-fbfc-3ac0-bad5-b4649a2ef129 | -13.46509 | -47.23519 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ec67ab2-cf98-3032-a839-8ea719975e51 | -12.93655 | -46.43175 | 2025-10-02 04:32:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e7b51dff-c56a-3fbf-8f41-1b1c6dc350a2 | -15.22852 | -50.11263 | 2025-10-02 04:32:00 | NPP-375D | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e1b086d0-9c4e-3277-9652-0162c70a7651 | -12.68719 | -48.57939 | 2025-10-02 04:32:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| a3df6580-6c31-3066-a6dd-8d7ac17b098b | -18.24422 | -53.31189 | 2025-10-02 04:32:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1b8b6666-2e5d-332f-9206-bceae54b8ab8 | -15.94073 | -43.34335 | 2025-10-02 04:32:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9866a5cb-19e8-376d-a2f8-e64c5b37ddff | -14.4288 | -46.10086 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24028fe3-0444-3cdf-9470-167acae1fdb6 | -13.33289 | -47.80225 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9ec78dec-4777-3029-af45-4bd86ded14ef | -14.48398 | -48.4325 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6191a084-002a-35a6-abe2-5ff3215c70de | -13.00812 | -45.23006 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9d0106d0-7d79-36cc-a983-83e8cf522056 | -14.6974 | -49.62162 | 2025-10-02 04:32:00 | NPP-375D | PILAR DE GOIÁS | GOIÁS | Brasil | 5216908 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f8e66c2b-5426-353e-9be1-5a7d50443091 | -12.49601 | -50.23851 | 2025-10-02 04:32:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 72d74e7e-f3fd-3027-a9de-31c13ce62782 | -13.21747 | -47.34904 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fd597588-6b82-3911-833b-ba4056e12db7 | -14.81898 | -51.40459 | 2025-10-02 04:32:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9b487144-69f1-350c-bbaa-1b2f1f35dab8 | -13.16893 | -47.81133 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 85e57b7d-d380-3c97-b7f4-99e4bd9cec83 | -13.22536 | -48.43718 | 2025-10-02 04:32:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ad7dfa94-0f23-3141-b8de-a211773d7ce8 | -14.86522 | -48.39304 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7bcbc33a-5d5d-3b67-b04e-3aebf20c859c | -12.67203 | -46.85899 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d4b84416-688d-37df-b8d2-8f7a78a013ca | -14.36622 | -45.96534 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 056a952c-86a9-382b-990f-34a0e1b16fb0 | -14.48512 | -48.42535 | 2025-10-02 04:32:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c347ad8d-5727-37e5-8a0e-58d722c8b7d7 | -10.881 | -53.76261 | 2025-10-02 04:32:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 24e2fd08-ca8d-31d6-8eba-53f630046602 | -13.80309 | -47.54205 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| f626cd2b-7a17-39ab-9b31-c21b7b0bd2ca | -13.01166 | -45.20593 | 2025-10-02 04:32:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8e6be148-2a97-3a0d-bb70-dcaac26f5a4c | -13.75174 | -47.95045 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f55da08-1beb-3164-858d-ac241211a614 | -18.88004 | -48.02573 | 2025-10-02 04:32:00 | NPP-375D | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d50bf471-13b7-397f-8012-a666012e6177 | -12.68683 | -47.56578 | 2025-10-02 04:32:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 880cef87-9fae-3ae5-ac50-c140d8c38151 | -14.9779 | -46.87028 | 2025-10-02 04:32:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6da073f5-df0d-3955-a0d3-e2ea863ba61c | -13.65326 | -47.30559 | 2025-10-02 04:32:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d05bd27d-9e58-320a-a17f-d2fd5348e1f9 | -13.75941 | -48.01013 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00605ef6-fe0f-3671-a9e2-e4c794908d77 | -15.15548 | -48.40128 | 2025-10-02 04:32:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8fcb7ad8-e048-37d7-acbe-af71b8b31553 | -12.76335 | -48.25497 | 2025-10-02 04:32:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 316ff345-0d98-377a-8ad0-49cdafade799 | -15.32166 | -46.27335 | 2025-10-02 04:32:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22bbb9fb-b95f-3c6d-a936-20d61bd84105 | -16.00469 | -50.8997 | 2025-10-02 04:32:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f0513ce1-ec7b-3b72-b5dd-987ac0f86f54 | -13.20728 | -48.50743 | 2025-10-02 04:32:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b52a7332-3c93-37ba-88c0-b266518c8aa5 | -13.80365 | -47.53848 | 2025-10-02 04:32:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 5767df29-794d-32e5-b727-d0d909c949bc | -14.42474 | -46.12793 | 2025-10-02 04:32:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e65b8a7f-c039-3b9b-b997-609826975be6 | -12.67538 | -46.85953 | 2025-10-02 04:32:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README85.md)
