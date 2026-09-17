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

## Dados Diários - Página 51

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ba7ed32e-348c-33df-9634-911afa26461b | -12.49431 | -50.76545 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38028da2-e918-3eb2-b8a3-e57b8c737731 | -12.49816 | -50.76246 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a21ed5d5-b097-368e-9491-b2d12898496d | -12.44002 | -48.48385 | 2026-09-17 04:42:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 37118886-2463-3c2a-8b6f-60a3086d4da7 | -12.47743 | -50.84951 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 339ac2c8-d9ea-3220-aaae-ba13a4316fa6 | -12.85312 | -44.39098 | 2026-09-17 04:42:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 92d7c974-f58f-34e5-95cf-fcba3868b0c9 | -12.44488 | -50.81905 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8fb7892f-b10d-3165-9e53-d85efb3c5377 | -12.45319 | -50.85282 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 650e8d33-95a0-3b06-8471-3c753fd7eb77 | -12.44382 | -50.84771 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f18da6fd-a1f0-3389-88d5-b848e7902111 | -13.43754 | -43.81449 | 2026-09-17 04:42:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 6bdaa057-d99a-32b2-8bbc-a7be10362a81 | -12.40215 | -48.47402 | 2026-09-17 04:42:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c44f3c8-1d87-3de8-8d65-2fcb3d416c97 | -12.47733 | -50.76296 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3424a430-2a86-3eee-9c9e-8374eb93a476 | -15.35901 | -52.93411 | 2026-09-17 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 24882f2a-e915-38b5-b84d-77a71781303f | -16.05171 | -52.24202 | 2026-09-17 04:42:00 | NOAA-21 | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4d6338f2-24fa-36fc-9c3b-28978720a4e2 | -12.46027 | -50.78546 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 46d09ada-f681-3062-b366-b2cab1856d4f | -12.51371 | -50.83709 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e548579-0530-383e-854c-de6a09e01d65 | -12.47188 | -50.81979 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4da11408-1271-39d2-b66b-644e9faed7cc | -12.45259 | -50.81308 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c351648-ac30-37d9-9813-e9cb84f60222 | -14.57709 | -46.58712 | 2026-09-17 04:42:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e8e45827-1fde-3cd5-9e28-11ea9184875d | -12.48946 | -50.77212 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7815b59a-ad0e-3500-9c01-6c94f4569fdf | -12.4691 | -50.79409 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 58da06ff-fea2-309a-bc1d-2c038a63969a | -14.84208 | -59.5462 | 2026-09-17 04:42:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7df912f9-3801-3688-8b85-68a0b0ff1c50 | -12.46522 | -50.77544 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| ef7cdc73-0e5b-3254-bcf7-4c0ee76db895 | -12.37334 | -48.46616 | 2026-09-17 04:42:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71ac272c-65eb-3430-82d0-a5c5d6d445c5 | -12.47186 | -50.79814 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ee1ed18-a800-3a13-9a71-52bbad41d3f0 | -12.46587 | -50.85847 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 88bb3328-dbf7-3d44-85bd-934cdab9e007 | -12.45537 | -50.83876 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 16970245-40d7-33d7-b49e-1d8c3a830a6a | -12.47907 | -50.83896 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d8bb6857-13ee-3b10-925b-64e0d12e19ad | -12.42197 | -48.4852 | 2026-09-17 04:42:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a92af01b-9a94-3374-9140-fde1ca9a3a49 | -12.4779 | -50.78108 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 52926729-d134-35bc-ae7d-42258f1c7109 | -12.48889 | -50.82228 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de1ecc43-a7ad-39fe-820c-c61b5cbafffd | -12.45038 | -50.80551 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 842a2b66-25a5-36f3-b7f2-6cff75eac026 | -12.48725 | -50.76455 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 118c834d-adbb-3487-8a58-3f63a0788000 | -12.46855 | -50.79761 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ea860313-f872-314b-b201-fc72abd8a9d9 | -12.75288 | -52.83873 | 2026-09-17 04:42:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 665ae671-416d-310a-8ac9-7c357ef25888 | -12.48616 | -50.77159 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8bfe3bae-1807-3cde-a008-edcc3bb0497b | -12.13818 | -57.18325 | 2026-09-17 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05f29df2-0ba4-349d-bc7a-4fa232622cbb | -12.45532 | -50.79548 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 20a2273a-9369-3870-b2a7-78093bcb118d | -12.44546 | -50.83716 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 44889c6d-ef42-3eba-868d-8db1967386a3 | -12.47574 | -50.8168 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3a244be-7342-3bf6-b504-db2fdbe5c16d | -12.47631 | -50.83492 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a0a5a7e4-ed56-39bf-ab40-a2af3dfeb7e4 | -12.48667 | -50.81472 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| de3fc187-444f-3f40-ae8d-3ae27b4dae62 | -12.49929 | -50.77707 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c9362538-6db4-37ca-a867-a9a68b87b09b | -12.44106 | -50.84366 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a011f4bd-cbdd-364b-b284-742c325cbb52 | -12.46251 | -50.81467 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12143ab1-c2bb-36cf-9f2e-1b284b9e2ce3 | -12.46254 | -50.83631 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0d1b14d-5945-38bd-b5d1-2ab913562946 | -13.60254 | -46.94402 | 2026-09-17 04:42:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| acf53a09-adfa-3868-bcfd-db418eacb476 | -12.47402 | -50.76243 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bb3ffaba-a2b2-3bfd-8372-77422d55859e | -12.40158 | -48.47802 | 2026-09-17 04:42:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c0c706cb-8552-30ab-bf29-f1f0feff5cfa | -12.50688 | -50.7061 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3ab18fb7-bfcc-381d-9fcf-b839795d864f | -12.11274 | -57.2006 | 2026-09-17 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f5feb0d-9524-3f5a-9799-4dda2f3a2f83 | -12.45483 | -50.84227 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4106d5d7-baf1-3ab0-b40f-ce371907c11e | -12.48837 | -50.77916 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8554e7c7-e858-317b-9f8a-63a1b3efc91b | -12.48345 | -50.81082 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d1341acd-c4cc-3092-969f-2ab6c9c8a94c | -13.51793 | -48.94524 | 2026-09-17 04:42:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef2d3f3e-5b83-34ec-a619-5b9175f5dd0c | -16.78051 | -51.64709 | 2026-09-17 04:42:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3083481-44a0-31ac-becd-85d2ce79c188 | -12.46803 | -50.82277 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6a3dc5c3-69ee-384a-95e3-5b8cc923dda5 | -14.12844 | -48.7337 | 2026-09-17 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e60a2f51-d887-337b-b32d-9dcd7059735f | -13.58732 | -45.47487 | 2026-09-17 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5c4563ca-3d32-3d1f-8621-3c11efdbb211 | -14.16182 | -48.75125 | 2026-09-17 04:42:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6c92e0f0-b547-3109-a43d-47eba9887ed5 | -17.74796 | -47.27057 | 2026-09-17 04:42:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3687a08-db62-3924-9360-929b4e08bb45 | -13.75187 | -48.80716 | 2026-09-17 04:42:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cce914c8-ccb2-3697-ad26-f8d9a4762d0c | -12.47355 | -50.83086 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4f4ad884-15d9-3844-b017-8473895f8847 | -12.46576 | -50.77192 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| ee8e0050-5e22-3d62-9357-961452b9c3b0 | -14.14857 | -47.3745 | 2026-09-17 04:42:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d10f459-480b-3eb6-802e-dfa62e90691f | -12.45428 | -50.84579 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2fbf7b78-2c0a-30ee-8457-a4af4b62d8be | -12.02127 | -51.46042 | 2026-09-17 04:42:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ccaba09d-f680-35af-8412-5187daeed282 | -11.98105 | -52.45969 | 2026-09-17 04:42:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9e113058-c0c4-3ec5-b29d-644b986aa1bd | -12.64468 | -54.70237 | 2026-09-17 04:42:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 00cfc8a5-47ab-30c3-8732-62b7b0037d08 | -12.46691 | -50.80817 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 867a36d2-cfbc-3330-b823-fddc5b6abbdf | -12.46746 | -50.80465 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 17591986-3644-3912-9594-c92b8a9d95c4 | -12.47081 | -50.84845 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eacb75f8-ecd0-3091-b441-3f0968f87b56 | -12.78099 | -51.28104 | 2026-09-17 04:42:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01776c41-dac6-3723-bac5-9d5eb3f8f2b3 | -12.47954 | -50.77052 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d7bcf5ea-6c89-3a41-b6a5-0a0f0f72e244 | -12.47899 | -50.77404 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c4292e41-c3e0-301b-833b-7764389d7051 | -16.99338 | -45.46761 | 2026-09-17 04:42:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fc523727-f40c-3463-a0a8-06995591a446 | -11.98384 | -52.46393 | 2026-09-17 04:42:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1ebe0a14-ff75-3c21-99c7-a872d2cc8609 | -11.98443 | -52.46025 | 2026-09-17 04:42:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e3c2119c-acc9-3148-a492-1500659702d4 | -12.46962 | -50.76893 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e63dc2af-f90b-3625-9af2-d467c546c880 | -15.63984 | -52.73476 | 2026-09-17 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db84d0a4-9d6a-3298-8ed4-d42929cae6b3 | -12.47459 | -50.78055 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 776f3fe8-4760-38c6-904a-6c8a8ec9d6a3 | -12.43996 | -50.85069 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46090069-6778-37d7-9fbc-447e9806ab46 | -12.44764 | -50.8231 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| dcdb9d59-051e-3e02-b389-20757bd73da4 | -12.45204 | -50.8166 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2ff1ac3-7fa7-3352-a799-01999ef4e8b7 | -12.48506 | -50.77862 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e238644-a428-34f9-924e-37994694a78f | -12.46751 | -50.84792 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 349a5840-5ec9-30b3-97c6-188e0aef0af0 | -12.45262 | -50.83471 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 25798857-deee-3f4e-9aa5-d199767a148d | -13.60531 | -46.94186 | 2026-09-17 04:42:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e3c2da1-b0d2-34de-85f0-bf5b84c4d83f | -12.49322 | -50.77248 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 20574685-d8ec-33d6-bd93-b17819a24497 | -12.85097 | -44.39247 | 2026-09-17 04:42:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 797fc5bd-0180-37e3-a59b-05883612bbdf | -12.47576 | -50.83843 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d718deea-905e-352a-85bb-ec33543869fd | -14.13075 | -44.01128 | 2026-09-17 04:42:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1c7479ee-c6a6-33d5-95c1-12b8463325bb | -12.11505 | -57.18782 | 2026-09-17 04:42:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 603f4bd9-e5b7-320a-9a49-23a611145845 | -12.47738 | -50.80624 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f249afa1-1928-364e-9403-e8af90a19657 | -15.64043 | -52.73111 | 2026-09-17 04:42:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4785692d-1afe-3910-8b1a-c61c6e749967 | -12.44986 | -50.83067 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5fa1867f-db65-3802-a5ae-1416a3943dd7 | -13.58313 | -45.47418 | 2026-09-17 04:42:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 341e59b0-1a8f-39c3-86c1-5c7479510d7a | -12.46201 | -50.86145 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 3e4e299b-9ddb-38ca-8730-327f9292ce29 | -12.13824 | -61.1665 | 2026-09-17 04:42:00 | NOAA-21 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3c3da984-f04c-3a1b-a18b-7a2524818619 | -12.47464 | -50.82384 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c5c4ed91-260e-3d95-a797-87f4707b78b3 | -12.44267 | -50.81149 | 2026-09-17 04:42:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README52.md)
