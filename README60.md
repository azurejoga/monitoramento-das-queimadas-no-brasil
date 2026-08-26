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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7a07b0e-a15b-3280-9d2f-af6a6ff631f8 | -10.76587 | -53.98254 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 18e91c6d-dad2-30fb-9f9b-343094291877 | -10.42939 | -61.21477 | 2026-08-26 05:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f53d831-fa39-31fb-bf01-0cc66b68336e | -13.22602 | -51.36513 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 28.6 |
| b69300b4-345d-3e59-bdc7-eb1cc664abc6 | -10.77264 | -54.03003 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ff71b422-14e4-3ccc-8b4b-af1d8b5e1ef2 | -13.41922 | -57.07183 | 2026-08-26 05:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 137b6626-59ef-3af3-9b13-83aefd524b7a | -13.35245 | -48.23333 | 2026-08-26 05:29:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63b77a59-362c-330d-a443-57b9d79d0a25 | -11.79083 | -47.64268 | 2026-08-26 05:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f49d8c4f-70da-3fed-9e92-d82f3bb193aa | -10.76137 | -54.01578 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6de64cbf-3274-31f1-9713-ffdefd69ea38 | -13.25573 | -51.38983 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 1827345a-8c74-371f-9caa-868f555a56f7 | -9.66431 | -55.13438 | 2026-08-26 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8513fb37-de7f-3ba7-8973-143c6090eb28 | -11.75091 | -54.53156 | 2026-08-26 05:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 23a58be6-0d9c-36ac-91e5-3bb9cda9adb2 | -13.87033 | -54.08669 | 2026-08-26 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7d674d0b-5629-3426-aba9-624ed6e7d2b4 | -13.24101 | -51.35738 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c1ace790-989f-359d-9e56-c99408568a4c | -13.86126 | -54.03702 | 2026-08-26 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 486b0173-e5a2-3fed-8f87-ee79726d08b3 | -14.39481 | -51.76568 | 2026-08-26 05:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 62f1ec93-712d-36ef-8368-693c318d2bb7 | -12.03325 | -46.04779 | 2026-08-26 05:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 751de59c-7c5d-358f-8bb7-9f522c67432d | -7.79225 | -62.3917 | 2026-08-26 05:29:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fde7722-fe45-3344-89f4-2e4e0ddf1a44 | -12.76051 | -46.46476 | 2026-08-26 05:29:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 40bf496b-8390-3ad7-a1a0-4bb3d33daf3f | -14.31947 | -51.73055 | 2026-08-26 05:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 74851c1c-d752-33b1-a509-22b4c88d6da7 | -12.95124 | -56.61303 | 2026-08-26 05:29:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b19a50a-62ec-3b73-a54e-24ce5940dd8b | -12.03563 | -46.02488 | 2026-08-26 05:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 156.7 |
| c892e434-7fac-3a6a-bf01-a75ae04e95c1 | -13.86575 | -54.03778 | 2026-08-26 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6eaf33c8-47cb-36c5-a848-326e308395dd | -13.6625 | -51.84675 | 2026-08-26 05:29:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fce6dfae-0862-3c34-b875-4812d2153efa | -9.67157 | -55.0838 | 2026-08-26 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d1c5a834-728d-3592-92d4-10609f7125b4 | -10.75146 | -54.01498 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e41f0950-aac0-3ea3-9306-cfcbd9f419d2 | -13.19358 | -51.3443 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 33.5 |
| d65c9ac5-10c7-3cb1-8b48-8f6ac432352b | -9.46841 | -56.89604 | 2026-08-26 05:29:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f7ca92d-f382-348f-b447-9304e887bf80 | -13.30704 | -51.45855 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 25091de8-77ab-3c9a-8f7c-70481a41fa33 | -8.81995 | -62.31598 | 2026-08-26 05:29:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3042ac9-c389-3077-a9de-117392db8bc7 | -12.08862 | -64.24065 | 2026-08-26 05:29:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c3732c0-0f82-328c-b0b1-96259bda7665 | -9.72605 | -49.34515 | 2026-08-26 05:29:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f0ae3245-e1e4-339f-b9f4-c12974c039cd | -9.2008 | -59.57137 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed09df04-a81f-3540-ac2b-28b3ef0f0797 | -13.30171 | -51.45786 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4aaa215c-2cf6-3587-adfa-228ddf778738 | -9.56684 | -49.26051 | 2026-08-26 05:29:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 68f3d4e7-6b17-3b30-9837-23eed979a218 | -12.69581 | -48.40905 | 2026-08-26 05:29:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e337fee8-7e4d-3a6e-b0db-153af5e47a04 | -7.81021 | -63.25983 | 2026-08-26 05:29:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 538b06f1-4a1d-3bfd-95bd-5b35b31f2659 | -12.68833 | -48.41748 | 2026-08-26 05:29:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| d12316db-d1cf-39a4-969c-278c302f323f | -10.43217 | -61.21893 | 2026-08-26 05:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f5fe650-8b9f-39d7-99c0-34ded1391d31 | -14.36378 | -51.75485 | 2026-08-26 05:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aea9c62d-3687-3d4c-8361-fc666bd23c66 | -13.22642 | -51.36171 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 36.4 |
| d993a8d0-88f2-3e9a-906e-1a4f510a9fa5 | -13.17212 | -51.3415 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b0838c3d-a5c0-31c8-989a-6ff178710b67 | -13.65766 | -51.84295 | 2026-08-26 05:29:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f6f68d37-77e2-3f43-9047-772df1de18bf | -7.90122 | -63.68409 | 2026-08-26 05:29:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc3477b2-1e38-332b-b757-c30fc81dcdc5 | -9.9713 | -53.96768 | 2026-08-26 05:29:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f707a4ab-a380-3953-b362-bc08be0393c0 | -9.65647 | -55.07614 | 2026-08-26 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c651eaab-a7a1-3d71-8066-28f7df1410f2 | -12.02079 | -46.01831 | 2026-08-26 05:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a1ca992b-8957-357a-b998-9f81fa39a726 | -14.79857 | -48.80206 | 2026-08-26 05:29:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3c4aebc1-b02f-3d44-b61f-af2e816043aa | -9.1791 | -59.3889 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb7103d0-c3bb-3ff8-9514-fbf75ae72fc1 | -14.79944 | -48.79762 | 2026-08-26 05:29:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c315cc77-c25f-384a-bb49-13e1b47f56e3 | -12.68188 | -48.4169 | 2026-08-26 05:29:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 41b5b9b9-5d47-3ce9-9633-46aab5155daf | -12.76121 | -46.45847 | 2026-08-26 05:29:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 245ff7aa-a741-35e6-aaae-1b3a24f1653a | -12.08574 | -64.23792 | 2026-08-26 05:29:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a141f5f-8038-3807-88ae-1da819a2ca98 | -13.23138 | -51.36583 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 8ff7725b-cf51-389d-bcf4-32fabf6c7898 | -13.24335 | -51.38197 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 21.6 |
| a24824e2-c6dd-3b4d-ab3c-82f48b67c515 | -14.76101 | -48.78796 | 2026-08-26 05:29:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6d6d2336-f5cd-38bf-b306-b893cba84d58 | -11.16508 | -53.99991 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f7d0b51-4b3e-3560-8115-291fe747ec6f | -13.17295 | -51.33465 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |
| a8ccd7c0-7c68-3283-92f8-34f3fbd8ab3f | -10.43495 | -61.22311 | 2026-08-26 05:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ee162303-1a3c-39c5-85d7-8ab3945038b2 | -12.66211 | -48.41891 | 2026-08-26 05:29:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 245f04e8-3a94-3bec-a821-be3a74fae293 | -9.66939 | -55.09897 | 2026-08-26 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d1be475f-22f8-33d1-8319-cbec6dbb4811 | -9.39187 | -60.58016 | 2026-08-26 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69da29c6-36a1-3cb3-a9f4-635ce7030fb7 | -9.19859 | -59.58534 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a220745c-9f0f-3cd9-8d30-803f7104e32c | -10.99288 | -60.79379 | 2026-08-26 05:29:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2011fa5-1372-308a-9089-ed0ee77ed6ee | -13.85576 | -54.07781 | 2026-08-26 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e91109f-e609-3566-b387-a6639c3eef30 | -11.74308 | -54.53196 | 2026-08-26 05:29:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9295cb1-3c38-3627-a87d-7d8490f9952f | -9.45335 | -60.53195 | 2026-08-26 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13a8a8b1-2a00-3829-b03b-be9d5ece9402 | -10.42348 | -61.22137 | 2026-08-26 05:29:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1987c557-a707-3624-8789-f28b81a2fd85 | -9.60794 | -55.11328 | 2026-08-26 05:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 27.1 |
| ad3df387-1374-3d75-8a7a-35b11e437987 | -12.02645 | -46.0344 | 2026-08-26 05:29:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 513504fc-150c-351a-bddb-3375f6128cd8 | -9.1638 | -58.33329 | 2026-08-26 05:29:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ebc03be2-b1ef-3bc4-9d6e-3d738aec9292 | -9.45392 | -60.52842 | 2026-08-26 05:29:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4759b432-3b9f-3376-80e5-40b087575137 | -9.39233 | -55.973 | 2026-08-26 05:29:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a0141033-41c9-3c45-bf44-4a6adcdcd221 | -9.57202 | -49.25895 | 2026-08-26 05:29:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79658ad2-fd20-3791-9624-fe67362c30f3 | -13.18285 | -51.3429 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |
| bf98c86e-94e2-3505-bead-87d26b4da700 | -11.19119 | -54.00352 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eb718d41-9782-35a5-b12f-078afa8dd43b | -12.15756 | -50.59624 | 2026-08-26 05:29:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7579d543-b336-331d-a5e8-143b701bdde9 | -9.17965 | -59.3854 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f3fcf27-5d01-3a47-92d9-027ea60cd588 | -13.22561 | -51.36855 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 8e8acebf-809a-3189-985c-3d0e347f01bf | -11.18685 | -54.00287 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ffe51976-61b9-32fd-97cd-9717fe694a0e | -13.60954 | -49.01042 | 2026-08-26 05:29:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ad8b1805-d85c-350d-bbc0-e4f8e78e4909 | -12.08332 | -64.24912 | 2026-08-26 05:29:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 174ef7c1-da61-3f6a-9097-d7878ba2c97e | -11.79445 | -47.64326 | 2026-08-26 05:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| bb79fbc0-78dd-3216-b9df-1e243a62dea9 | -13.24996 | -51.39254 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f1eb1dd2-dab0-3737-9093-24eaeb644c00 | -13.23578 | -51.5108 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 276ecae5-8536-3977-9eb7-6e4445196f0a | -13.24665 | -51.37477 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 6601658f-82cd-300e-9334-f6e10b9bec20 | -13.24438 | -51.52889 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7915936d-4d3a-36b2-94b4-843ac265dada | -9.17111 | -58.33075 | 2026-08-26 05:29:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb413764-a958-303a-864d-7efbd3eb4ebe | -9.10917 | -60.90351 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f5392b9-8977-31cc-a9aa-7e20dd70968f | -9.04889 | -60.43744 | 2026-08-26 05:29:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e958364-1888-393a-be17-d50a7e80358d | -8.82086 | -62.33259 | 2026-08-26 05:29:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ccc9f362-2809-38bf-a8a5-d266dd42dc0f | -13.18326 | -51.33947 | 2026-08-26 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 5872a90d-9f73-3617-a21b-183d577b6259 | -10.16557 | -55.30463 | 2026-08-26 05:29:00 | NPP-375D | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74e8e789-76e5-32d3-8fdd-cec90ea95b19 | -10.02432 | -46.42123 | 2026-08-26 05:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7829244-b9ac-3978-a349-59e17cb8dd88 | -13.86321 | -54.03473 | 2026-08-26 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 72eb0209-cf9e-30e1-8eb6-fbaf5ee89e11 | -11.68787 | -54.58821 | 2026-08-26 05:29:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf8eda9f-e941-3747-bf59-e711042f317c | -12.64697 | -48.4255 | 2026-08-26 05:29:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7141dd56-289f-3d32-8f15-523bcb270626 | -13.85937 | -54.05101 | 2026-08-26 05:29:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4dcb038-12fe-32bf-a4fb-4a8ed1dbf25a | -7.6218 | -63.36712 | 2026-08-26 05:29:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5bd4b003-bef9-363a-aaea-1f7a39faeadd | -11.88542 | -57.11067 | 2026-08-26 05:29:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 73a53c08-df16-30b4-9ee0-134d0a9d30b7 | -11.16132 | -53.99505 | 2026-08-26 05:29:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README61.md)
