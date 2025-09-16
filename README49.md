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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b81af40d-b162-3e04-a2f7-1ba7b9fe6614 | -8.1172 | -48.26228 | 2025-09-16 04:29:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0629dc4c-027a-30bf-a22f-e95e20d08305 | -8.906 | -48.61121 | 2025-09-16 04:29:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c85d5388-687a-311e-be70-8887962074e5 | -11.70654 | -46.88715 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 859e2e07-9f05-3c28-b07f-206bfc2a0827 | -8.91471 | -46.23578 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e36f0cf8-dded-3ba6-906b-f80d41786d77 | -7.48274 | -46.12107 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4eff0a8c-3d4b-3d53-b19c-a94fa155d269 | -7.67244 | -46.29077 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0985fabc-82f5-33a1-bf03-35eb9aa330a8 | -11.71153 | -46.87713 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ff963d58-1f2c-320b-a47a-25c5393ab617 | -10.7468 | -48.18192 | 2025-09-16 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e29670b-f7ba-3797-95bf-cf94c2468d7b | -12.11657 | -47.53333 | 2025-09-16 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1cd9ec30-df9f-3aeb-a7b3-32a165ada264 | -8.59013 | -46.34633 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eae30fc9-ad17-359d-a32a-2576d1816d8b | -9.45572 | -48.60112 | 2025-09-16 04:29:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7b52abcf-8da6-3b3a-9c81-78ad81b93d63 | -9.09732 | -44.84225 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6a36c32b-390b-32e6-876c-ef679801a560 | -7.67302 | -46.30872 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4453abef-0dce-3cf4-bd8d-29e3ae620962 | -9.05583 | -44.84786 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 770aa873-fca0-3216-9573-a37ec1099f02 | -12.77579 | -47.95938 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ed61b44a-386d-3331-90e0-5fd38edaff96 | -13.21026 | -47.28432 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 61ed28d0-77c7-32d8-a2ed-2b2efd32a931 | -11.11622 | -45.32006 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f88ca0af-5b7f-38a1-8b50-a7d1f58f6f47 | -12.61668 | -45.74638 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8d4a64dc-11fd-35e6-9f7c-8c35b4c5d825 | -9.06686 | -47.03447 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| a9f9facd-65b4-3468-9d81-d3438012264c | -12.68706 | -47.98878 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba67760f-7953-33fc-aa47-83b30c0acaa5 | -12.66144 | -47.71933 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c67c3f1c-2eea-3c57-bd75-88699d3a99fb | -11.07369 | -49.06993 | 2025-09-16 04:29:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a12ed209-f1da-3966-9765-36de1b41dc41 | -9.4689 | -48.58444 | 2025-09-16 04:29:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fb03b863-9d83-3867-807b-ca9f66093d55 | -9.18313 | -47.04278 | 2025-09-16 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9c5fb6e-1733-3b59-a82d-63a6fae538d6 | -10.71468 | -46.48615 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b1306094-cac7-3a26-b678-6c0dde42c685 | -12.60995 | -47.95791 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f23f1f28-d6bf-32e6-af38-7e7e5f9e6e74 | -13.20638 | -47.2873 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 84628719-58fe-3ccb-ac11-255a68f03efa | -12.73263 | -47.2 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| df6a36fe-0908-321d-a5ec-4caed27f43af | -8.41876 | -47.21436 | 2025-09-16 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e59b120e-f8d6-386d-a812-eea7bf434ba1 | -11.59868 | -46.97178 | 2025-09-16 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3f61e900-a764-3ba8-9ee8-31d030432bb0 | -12.68152 | -47.9806 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4a712bef-50e1-3627-9b2e-466cee82031a | -10.79055 | -50.6584 | 2025-09-16 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 302cea8c-b4ab-3c15-82e9-dc4dd1ab0c93 | -12.97908 | -47.9565 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a95ef4b0-0e57-36e7-9885-138fb7e1dd0b | -7.67576 | -46.2913 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3f94d0c-41c3-370c-b8a8-d6ac9f7dcb7d | -7.59792 | -49.3327 | 2025-09-16 04:29:00 | NPP-375D | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6eec6c2e-f387-33fb-ae6e-7913ee12f99d | -6.55411 | -54.98513 | 2025-09-16 04:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 92c09b1b-accd-3de0-b8ac-63a76b5c7274 | -12.97074 | -47.96604 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6db4a8d0-a2ac-368f-a32b-93e32101904a | -8.66557 | -46.3796 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f318bd55-560f-36c9-b0c1-7634b773a90c | -12.85344 | -47.13889 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0af4b71c-176b-3d20-a343-818da175b3d3 | -10.8825 | -47.7849 | 2025-09-16 04:29:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b08e0c2-00c0-3d77-972d-e7d632f30d20 | -7.97442 | -45.63617 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d6ff0583-4df8-3c2a-9c6e-416bb2554572 | -8.12381 | -48.26267 | 2025-09-16 04:29:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b9a9535-a113-3072-b5e4-3c826d3a44ea | -13.21582 | -47.29253 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0179f1bf-b6e6-3a49-a3c8-63dab8298f16 | -11.99702 | -46.67346 | 2025-09-16 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ad0d164-b1e9-3d9f-ab0c-8fc84942b3e2 | -8.37312 | -47.52102 | 2025-09-16 04:29:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e89aa02d-15b8-372b-8e93-c1d2af9a491a | -8.66722 | -46.36911 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 96877217-5543-36f1-aeff-47a3453ae55f | -6.55358 | -54.98515 | 2025-09-16 04:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 68ace564-990e-36ad-a4d7-d04aef44a510 | -8.41895 | -45.74918 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 32a8d568-3e7f-3899-944e-7cfb4a64fd24 | -12.80324 | -47.18589 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 112af0a6-4be2-3de5-a539-e5c49c9c56c5 | -8.92882 | -45.51568 | 2025-09-16 04:29:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06c249d6-69f9-3027-8a67-9e9e4a1d69ca | -10.78313 | -45.97527 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8360e9d4-9f64-3bb2-a3a8-2be814434e2d | -11.24165 | -49.95571 | 2025-09-16 04:29:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dbab1c3c-6536-3df3-8737-1445172f9da7 | -10.72027 | -46.49429 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 7f42d08c-4cd4-31e5-bdad-21cbb39aa2bc | -8.92521 | -54.44635 | 2025-09-16 04:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 028c9bdd-849a-3f01-9a94-7c9fa7588e59 | -12.54456 | -45.8745 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 4987e12b-c8e0-3ec7-ba1f-8d3cb9a429f5 | -8.58127 | -46.35926 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a46ab64-d49e-3e16-8419-20c01c8ad3ac | -13.03559 | -47.98768 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cea18aed-ba94-3fdf-8d24-dd19bb1b4f10 | -7.40813 | -49.996 | 2025-09-16 04:29:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d2729a2-55e1-32fc-8e7f-c2a272578868 | -9.7457 | -55.37829 | 2025-09-16 04:29:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9fc831ba-9a43-39b6-841b-2c70192ecb00 | -7.8339 | -46.11916 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dc3e7c7b-31c9-3e0d-8b8e-c462b21b9d48 | -7.98451 | -45.65957 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d7297756-09fc-3ea3-9017-b1d0c3f1cca0 | -8.08917 | -50.15928 | 2025-09-16 04:29:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9d9da89d-7702-32de-a0a9-9cf2839840a2 | -7.71114 | -49.55818 | 2025-09-16 04:29:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fbb240f9-6d1a-3cd4-94fa-d34bfc628477 | -9.1471 | -46.95414 | 2025-09-16 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25d9fde2-16e4-3cbc-9a52-341a4f41cb1f | -7.99413 | -45.65413 | 2025-09-16 04:29:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2a9300a4-0d58-3afd-8c10-33f5317c7b1e | -12.62967 | -47.51466 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c7f9cc7-5481-3fa0-9b08-0c4fd1f21ee2 | -10.78249 | -50.66146 | 2025-09-16 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 146e239a-68fc-361a-873f-4d9ec0f742c4 | -12.05727 | -46.55075 | 2025-09-16 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6467bfd6-bc7f-3b6a-ac95-298acb8a33b8 | -9.17708 | -47.06647 | 2025-09-16 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56470101-7234-3c61-a1f0-c03ae4a456b5 | -9.45972 | -48.598 | 2025-09-16 04:29:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6b739ae-bc28-3df9-9544-713e50a8345c | -7.46171 | -46.14635 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a060743-f095-3672-a554-653cae4d4bd3 | -11.50151 | -43.72312 | 2025-09-16 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 21817a75-e8d4-32ee-a66e-80ac486d5b47 | -7.68438 | -44.67393 | 2025-09-16 04:29:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1d07328-9ed7-3ce6-b654-2cc68ab676a0 | -12.61726 | -45.74259 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 976efdde-6f0a-3e6b-99e4-5a2c9bb9b0fb | -8.11943 | -48.27015 | 2025-09-16 04:29:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6148407a-f70a-3f9f-a266-eb34021672d7 | -6.55874 | -54.98618 | 2025-09-16 04:29:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69d24985-d9d4-3e6d-a7fd-577b11d4c70f | -10.71583 | -46.50084 | 2025-09-16 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| a9763a3d-90a7-3ed3-af62-307885c6b3bf | -10.73629 | -44.7578 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 990c02e8-02c5-36a0-af66-2150b253cf7a | -12.81323 | -47.2314 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 89c546c7-23c4-3c5c-a748-422dda4a227d | -10.71492 | -44.75509 | 2025-09-16 04:29:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e1c6ad99-90d2-361f-ae00-109574410bb7 | -11.12475 | -45.12137 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb93e224-32fc-3307-9d49-03d761c43232 | -8.67168 | -46.38417 | 2025-09-16 04:29:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 3d688a88-fa4a-3542-ba27-45fa1e1fa973 | -7.69305 | -45.1382 | 2025-09-16 04:29:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50d4b6dd-1930-30e9-9645-981f84ab6482 | -11.29901 | -50.85447 | 2025-09-16 04:29:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2273c423-fe1c-33d7-83c0-6f038fd515d3 | -11.08014 | -49.75457 | 2025-09-16 04:29:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 744ea4a4-4a4c-3ee5-a16b-5c3e3ec4acd0 | -8.87942 | -46.18661 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 731a9dd9-0bee-3eb8-be96-603cd11b70d7 | -12.80378 | -47.24809 | 2025-09-16 04:29:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a98a8e34-4937-3bbe-8f44-2e10ee482f64 | -11.50217 | -43.71864 | 2025-09-16 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f2b310f6-91a7-3c32-be7a-d4488551f138 | -9.15432 | -46.97322 | 2025-09-16 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd67a53a-d46b-3204-bbce-866dfd871e0d | -11.12024 | -45.31681 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b4cb0d2-25fb-3216-9b44-fa811875504f | -11.58162 | -45.02461 | 2025-09-16 04:29:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50ff7ee5-2fe2-3ccc-b9bb-45dc33bb669f | -11.1237 | -45.34066 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59714864-656d-330c-b99a-63463ea63ae0 | -8.97643 | -46.2347 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2abe9512-3181-3399-a0b9-b5b18281a0b8 | -8.12597 | -50.1662 | 2025-09-16 04:29:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| de05ce0e-208f-3eaa-bdcb-a6b7afc3bb16 | -13.22842 | -43.41886 | 2025-09-16 04:29:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e440a05c-c957-3a93-8077-98a3d8ae3ff9 | -11.13405 | -45.34227 | 2025-09-16 04:29:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 36f31750-5eb3-3fa3-98f7-b1b5a6bba4b3 | -12.66866 | -48.01851 | 2025-09-16 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d1591138-4fcc-37a6-9624-4df668c0b923 | -10.17403 | -46.14283 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 657435e1-d963-3402-9cfc-4e3d96a7dd76 | -8.97588 | -46.23824 | 2025-09-16 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2fc92c1f-aaf8-35d5-9d36-161002ea983d | -12.5483 | -45.63815 | 2025-09-16 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README50.md)
