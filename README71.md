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

## Dados Diários - Página 71

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1cc9f61a-dfcf-3010-b66b-da4f0376555f | -13.51537 | -47.25175 | 2025-10-03 04:12:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1bdf29e-536d-3a6a-9034-a2f01924e676 | -10.93275 | -51.06651 | 2025-10-03 04:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b46642c6-97ed-37fc-89a3-9bc03dd736fc | -13.58246 | -48.19198 | 2025-10-03 04:12:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6471c99c-d27b-3926-8e18-065251349815 | -11.82534 | -51.77359 | 2025-10-03 04:12:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4ed00c96-8d19-393a-949a-aadb257a2b4b | -13.58384 | -47.59139 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 8295c14f-e552-3e22-9ac7-1580c7546748 | -10.88586 | -44.27668 | 2025-10-03 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d2fcf661-2687-3aa0-8ebd-d0309c5e604b | -11.83916 | -45.02361 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2e80e7d-95bc-3ef9-900a-a4973b611acd | -10.87746 | -47.8206 | 2025-10-03 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 7acc63ca-fdfa-3202-9186-3e3a6d2413aa | -13.96861 | -48.16988 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ae9192dc-3eab-3edd-967f-13e3b7b06fa3 | -14.43699 | -46.37323 | 2025-10-03 04:12:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d63ba397-ebd9-3cdc-856e-d34ed863f6d4 | -11.59009 | -47.63191 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9fb477c9-c6e3-35f1-9b10-6055d71f359a | -12.41462 | -45.16623 | 2025-10-03 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e01b838d-50d2-37ad-882a-45b4eca938e7 | -13.28446 | -47.2649 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 26a73edd-8d2f-3735-a623-be955780241c | -12.68334 | -48.54353 | 2025-10-03 04:12:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d2488fe-f2d5-3420-90f8-414fd85f70d2 | -11.99274 | -47.19224 | 2025-10-03 04:12:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3bde08d9-ec40-39a2-a4d9-5e4b1f3b34be | -14.37793 | -45.93402 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95e4e1b1-fafe-3ad3-a605-18f07e6dbfa9 | -12.86318 | -46.99514 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 4cfb0dbc-1374-37e1-9a64-7588fc78da85 | -13.97393 | -48.17372 | 2025-10-03 04:12:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d8c3f45a-a242-3883-9927-7f70a2ed0f40 | -12.93646 | -48.43192 | 2025-10-03 04:12:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c1119d2b-7e0c-32f0-b562-4c11aa9b3d4d | -13.33036 | -47.20362 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 39f57f4e-f6e8-3b95-bcf6-be1605682d4b | -13.19568 | -47.79047 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 842d16f1-7485-3485-933c-d24e22f8b0b2 | -9.07352 | -46.65012 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 19ddde01-064d-344b-9854-f53d91faeec7 | -8.76154 | -49.92236 | 2025-10-03 04:12:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 62d815cf-087b-3a93-950c-01d7ea2f3210 | -10.28103 | -44.32398 | 2025-10-03 04:12:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98be8cf1-b03b-3ed7-bf61-4641317b00df | -11.48732 | -44.99298 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 866dbb06-c25f-3e02-bacb-a82c699df945 | -11.44864 | -44.95985 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 980db4f5-5664-3cd0-b442-4ad2751d0cbf | -9.94726 | -43.75426 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| b6c3198b-0dde-35b8-a109-f4da43a3f020 | -10.45745 | -45.84396 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 81786fe7-59fc-3d18-a960-23ee2aeb963e | -12.41993 | -44.08375 | 2025-10-03 04:12:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e3cf7f7-8aed-30f5-9665-5d218f2236b7 | -10.88646 | -44.27297 | 2025-10-03 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 249e6ae5-07d7-3029-b077-0bf6c8e9e06c | -13.2728 | -47.24212 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 519886ca-f926-3824-aaa1-4a431f2867b3 | -11.05211 | -47.80268 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be1684ba-4d66-3962-bb6d-cc9793fdd960 | -14.22452 | -46.09055 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9931d75e-e753-33e1-85ac-fc8a6a3a01b3 | -14.297 | -46.02816 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65a65fc3-b8ef-3faa-9b4d-707545de62fb | -11.35029 | -44.94403 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ebf23879-33d8-3065-ba0d-c0e63ae07277 | -12.76377 | -44.90864 | 2025-10-03 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b655b78-1484-3cff-8f90-fb6be398dc1b | -13.14432 | -47.83464 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| df876253-e483-35b4-84ce-e67aa625cffc | -13.32428 | -47.58529 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 49826548-f017-38df-9807-12e3d7571cec | -13.35135 | -47.33215 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 53931520-6d71-39d2-8ab8-c45c87c81f21 | -9.95717 | -43.7148 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f7f118a-3c77-3941-aef4-2b2c6cff1866 | -10.22495 | -43.0246 | 2025-10-03 04:12:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 8cdde739-2f36-30a8-a9ea-25a1f6cc6da0 | -13.74245 | -47.99137 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 58ba3e32-f511-362a-b184-4a4d39a0800d | -13.32272 | -47.20263 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 412b6245-25b2-3c79-8fb2-0c83d208a3ef | -13.13856 | -47.8825 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 989ffa1a-7286-310c-b037-677b408e0910 | -14.21202 | -46.08544 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b11f45df-be3e-3f09-b189-42e7151dc959 | -13.23874 | -47.34562 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a6e07cdc-d34c-3609-adb6-820e2bffa239 | -10.86025 | -47.24681 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3bb1d09-cdd5-3c41-8d6d-3784d61542d0 | -12.7535 | -50.5547 | 2025-10-03 04:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45fdf9d4-c7ee-3f22-a5e7-154e7ab9b906 | -11.481 | -44.98804 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5cd5abd-9a74-3b74-befc-1e865f0c00ed | -9.71523 | -48.95282 | 2025-10-03 04:12:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e758dde6-91dd-3daa-b47b-ae44c432295e | -9.90477 | -45.96286 | 2025-10-03 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a8f7364-531f-360b-b0de-a4a3b3aa8596 | -12.22045 | -43.7658 | 2025-10-03 04:12:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 75bbabd3-0436-3a8e-a592-bd92c6fe8dc3 | -11.48866 | -45.11375 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d60925d-b4ed-35d6-901a-f998efdbea4e | -10.9231 | -46.73749 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 45f5a9f7-8364-377e-8248-d6493a04d68c | -14.19359 | -46.06488 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 03eeb1d4-4f11-3411-9e93-85e39ccb09ac | -13.60642 | -43.76027 | 2025-10-03 04:12:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1c910eaa-a48f-3d61-99b0-c44cffddffb3 | -11.09065 | -47.87107 | 2025-10-03 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6fda3814-eb78-3074-97c1-1170b6a3f39f | -10.28651 | -44.32867 | 2025-10-03 04:12:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dee3c445-3d96-3f3e-917a-85042a6cc1a9 | -12.40416 | -44.22324 | 2025-10-03 04:12:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 45fe33a2-1a1a-3a2f-a807-65e375891f4a | -14.29769 | -46.02406 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b32df356-2cc0-3826-b30d-19020b35e84d | -11.45561 | -44.96097 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3adfc81b-c82e-3259-8195-acbf114385c5 | -12.6 | -49.90329 | 2025-10-03 04:12:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0639669d-ce42-3473-bc3b-9cac2334fcee | -14.01283 | -44.9621 | 2025-10-03 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 269a2f20-e3b0-3ec3-9dcf-3a5771b9b138 | -10.27981 | -44.3315 | 2025-10-03 04:12:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e1339073-7ea9-3601-99bb-6d36783003e4 | -11.18718 | -47.25819 | 2025-10-03 04:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab767591-2bce-32ac-8353-d07d3c7f4d4a | -14.21405 | -44.94999 | 2025-10-03 04:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f890ad93-3faa-3c14-b152-123581a2fff1 | -11.23275 | -48.20211 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75a8121b-209e-3a3e-a5aa-e6c538265df4 | -12.28041 | -44.12782 | 2025-10-03 04:12:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b1a42352-8065-3c1f-85b4-0cf6064792cc | -11.60324 | -47.65066 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 498841e6-a66d-369e-94cd-23613c328731 | -9.9268 | -43.72458 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 50c9a60a-b32a-328e-884d-c5e69db97b8e | -9.90533 | -43.72853 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| d9af8c16-d2ff-346d-82e2-ef8d4d616035 | -9.91125 | -50.50214 | 2025-10-03 04:12:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bca944a9-e25f-38da-9431-e49726e56183 | -13.5406 | -47.28651 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| eaebd75a-09c5-3336-973d-a571a47d5b57 | -14.42101 | -46.08723 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2eee311a-b8a0-335e-a204-9a169e8993e2 | -11.82128 | -44.91703 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4baa0599-025a-3768-869f-a943ae6f3bc0 | -11.55565 | -47.66353 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| c5ac5966-9359-3622-a2fb-5ac244d65149 | -9.9186 | -50.90455 | 2025-10-03 04:12:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 299385bf-9d14-33ab-8461-b42f32bb637f | -9.89991 | -45.95531 | 2025-10-03 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1bc48b67-c3f4-33a1-861c-25fa4ef03b78 | -11.81077 | -45.02255 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bafe1b0f-2e3c-30d1-afdc-1d0149285485 | -11.91231 | -46.27477 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ddc18151-78be-3cd7-87de-b36f19212425 | -13.30202 | -47.82397 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79f23904-7f97-3c7c-b663-c940ca64f73e | -11.11275 | -47.73986 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bea5e44e-dc95-39c1-a351-4b6c86d5529b | -13.26431 | -47.24578 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1a678f9c-2094-3428-a224-3324f26800b3 | -9.08245 | -48.02852 | 2025-10-03 04:12:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1b4df86c-bc3e-3326-9178-bc5e93b21a52 | -12.86594 | -47.00256 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6aa3326f-b598-39ac-b056-8209384c642a | -11.90512 | -46.30159 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9db84c2f-1879-3848-abcb-b3e5194bcda3 | -13.20726 | -47.8858 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5c1120a7-45b6-3170-957d-d0f04f0e92e8 | -12.81304 | -46.85987 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 351fe2be-c2fb-396f-b74d-38eb649ffef1 | -11.55963 | -47.66434 | 2025-10-03 04:12:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 64e4bea2-21d4-385e-88d4-9e216f00bdb1 | -11.10352 | -49.8077 | 2025-10-03 04:12:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f4274e63-8842-37f1-bea4-4ee7b4699ea3 | -9.4224 | -47.54488 | 2025-10-03 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6cf3e40e-e3f4-3cf3-b656-e308cd80ae92 | -13.79968 | -47.57391 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 176f21e9-93ca-3c75-bd16-6f195b404c7d | -9.90034 | -43.71648 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6b641b2c-ecb5-3c68-9cca-c756488721a9 | -9.06401 | -46.65878 | 2025-10-03 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 7b59731c-4826-33f8-a33c-d19d7553849e | -11.92237 | -46.28214 | 2025-10-03 04:12:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 9a5596db-6b46-3aa6-bc9f-c761866f9580 | -12.90189 | -46.9292 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50a8e541-92a7-3bc7-a456-a39280e8ddc2 | -13.37763 | -47.28384 | 2025-10-03 04:12:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8a306605-14cb-3ce5-9738-4ddaf216b002 | -10.26374 | -50.3437 | 2025-10-03 04:12:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86c05ab4-a03c-36c5-b66c-da0b875872b9 | -9.91228 | -50.4965 | 2025-10-03 04:12:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8665d5c9-fee1-3c29-a20b-055fa9237fb3 | -11.87643 | -45.01405 | 2025-10-03 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README72.md)
