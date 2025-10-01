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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aba32576-8092-3088-83d6-33561dbe2a07 | -9.94014 | -43.59638 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c07db155-a383-3888-8096-be583d9945e8 | -12.76004 | -46.91111 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fe824b3b-cbeb-3783-8280-f084747460c9 | -11.9908 | -46.65199 | 2025-10-01 03:30:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9dec3256-6cda-37bf-8417-dfedd0d7be50 | -9.26943 | -45.6923 | 2025-10-01 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bed6bdae-46fe-3829-ab1e-39e904a7898f | -11.81063 | -45.001 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f10fed04-0615-3d7a-9207-eebf0cee2100 | -11.45705 | -45.08504 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3bd9ff17-de94-33df-886a-e77e103cbc2b | -11.82196 | -44.97712 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9beee5c9-d8fb-3d89-8465-d1038c3dfdb1 | -13.32656 | -47.33688 | 2025-10-01 03:30:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1b5b90ee-f442-30a3-81ce-8d9da0b9994f | -14.18776 | -46.10943 | 2025-10-01 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| ef3ba4a7-7f87-3b28-b52d-71f77182fc3a | -10.82564 | -45.37745 | 2025-10-01 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6f978ad7-7cec-3a40-a771-34d704fd6df4 | -14.06443 | -44.37151 | 2025-10-01 03:30:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c953661c-a9a5-3918-ac37-0ccff26da8c5 | -12.13253 | -42.87719 | 2025-10-01 03:30:00 | NOAA-20 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 461cd8d9-da9b-3446-937c-0982e3dbf4ac | -11.84368 | -44.99751 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a001e5b2-aeb7-33f7-b9de-2b05db5d040a | -11.68413 | -44.30276 | 2025-10-01 03:30:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e371bb16-8e5c-3e37-884d-0cb9f040f388 | -11.53954 | -45.06481 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 33bb3557-6ca4-3dc0-8c99-97210670ea9f | -9.94769 | -43.58894 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0786cb0-0795-3ebf-9de8-3ca5c719a556 | -8.55794 | -44.76349 | 2025-10-01 03:30:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 23e49126-6a2e-34ca-8843-05b35c719453 | -11.83648 | -44.9692 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b7a052e5-57c8-306a-833d-2b9f17ac6c08 | -13.32843 | -47.84649 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6fcd3159-8a5e-3158-9f0f-6abc83fc62cb | -8.58884 | -44.74215 | 2025-10-01 03:30:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 25b3dfb5-e014-3678-aad3-60cf31ef2e92 | -12.78435 | -46.86171 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 41bb01f8-1aa2-3ea0-8daa-2a16fadcac7b | -14.18662 | -46.11479 | 2025-10-01 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.2 |
| de9497ca-5c0a-3597-9d0f-7853d8079c65 | -11.7583 | -46.87372 | 2025-10-01 03:30:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ade7b159-a370-3971-9bd9-bf1215f6b343 | -13.34011 | -47.81208 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5126071d-61b3-3c54-bc02-b7b0fac152c3 | -11.52506 | -43.55157 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04ffb4eb-e71c-3768-8a46-c659d1ab96a8 | -10.80335 | -45.35448 | 2025-10-01 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db26c179-db76-335b-a924-638cd703c7a5 | -11.40038 | -44.89866 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3fb2f324-97d0-31eb-bfcf-591e5cb4de4f | -10.84513 | -45.41382 | 2025-10-01 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 54eb873c-e9fd-3db1-a6b8-044a87f12b05 | -10.82985 | -45.39007 | 2025-10-01 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e3458582-7cf7-3fb7-9f0e-99cddbdab4de | -11.82298 | -44.97213 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 61351717-47e2-357a-8554-dc0ed88537d0 | -13.32933 | -47.86207 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5e4b31f4-224b-3598-97b8-f7faa5cb76c2 | -8.89117 | -45.05613 | 2025-10-01 03:30:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0ee65bfa-fee5-3b4b-b6bc-5d3d52056760 | -9.93008 | -43.6801 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa968380-ae48-3bec-9a34-3f942b869ea0 | -14.20779 | -44.92954 | 2025-10-01 03:30:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2926b70-8c5f-32de-b9bd-93e1549f78af | -11.74388 | -46.88006 | 2025-10-01 03:30:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0aaecf36-311b-3255-93bd-ffa955df0247 | -10.93328 | -46.51009 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7fe494ed-07c2-36e0-a12f-96eaf81e3730 | -11.83723 | -44.99746 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d1c160aa-7c22-399e-9022-d6e2f92b3332 | -11.46029 | -45.0872 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| c8047493-b7af-3203-99ad-703589467f50 | -11.47464 | -45.09507 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3bae2182-29f3-3941-ad60-c86b220cdd13 | -11.4394 | -43.50408 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8beeed2d-7a5a-3ba8-926d-57c65adcc821 | -11.5255 | -43.5544 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d80c05f-9abb-374d-bf52-05b5ff63ceb7 | -10.83061 | -46.66167 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e3c41813-e1f4-3e66-8b81-f1f617ba4ac3 | -11.84791 | -45.00863 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 231ff0a9-d09a-3e89-9d18-089e85595bed | -10.21347 | -43.04216 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5c94bb89-6a27-3499-8531-d818150e9a7d | -13.75604 | -47.94148 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3d58fbc0-f16a-3f09-b0f2-eceea59a50fc | -8.58033 | -44.75168 | 2025-10-01 03:30:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba805f00-fc3c-3502-837b-5ebf549e261c | -13.32493 | -47.86218 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 38de7593-08f8-3c4e-90fa-7c93dbb2562d | -11.44297 | -43.50916 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ba3962b-5121-3663-bb96-f6a4cf8a68a7 | -10.90428 | -46.54544 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 546ff6b4-30d2-350a-acf6-05bb5d2e98d7 | -11.366 | -45.06812 | 2025-10-01 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| feb482e4-5223-31ef-95b2-fefdddc5b773 | -9.26421 | -45.69341 | 2025-10-01 03:30:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c26e0081-0495-33a6-8dcd-60bb657a9607 | -8.55151 | -44.76203 | 2025-10-01 03:30:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3463e8f8-c616-3202-9cc7-2702448e92ee | -13.66391 | -48.08915 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0b8a89b1-f42f-3d16-80a7-b424cbddf45d | -13.32532 | -47.82698 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 88c1d896-3927-3447-a7d5-f13a301f7a75 | -11.18918 | -47.20816 | 2025-10-01 03:30:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9aeed762-ff33-374f-a84d-bb88c729e7a1 | -13.32753 | -47.83591 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 01f546a1-8be3-36bd-9850-5e618206a6f0 | -12.66061 | -46.87121 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d454e28c-610b-398a-a44d-af152bdc7dab | -12.8398 | -46.8716 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 71eee3d0-f323-3113-9101-7c40f8793bdf | -14.18023 | -46.11353 | 2025-10-01 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6650b2de-fb5c-34d9-b541-da1aadf2ce65 | -11.19766 | -47.20311 | 2025-10-01 03:30:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c6bef577-72b5-36d7-a324-d742d1ffab14 | -11.46458 | -45.09865 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| ba13c482-8d99-3a2e-803f-dc86777e5163 | -14.7053 | -42.32227 | 2025-10-01 03:30:00 | NOAA-20 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 84fc99e8-cb8a-3c04-874d-77148838872d | -12.86864 | -46.90319 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51a18cf2-4dce-341c-a488-43d5fd9ba932 | -9.94183 | -43.65106 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d778c88-37fe-33c9-b5c3-e515300b14b9 | -13.36992 | -47.30904 | 2025-10-01 03:30:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 435d939f-ad3e-38bf-98e3-3e810a7f0d0e | -13.32749 | -47.87058 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 50be43ca-5c5a-360d-8015-410a246277ed | -12.84764 | -47.03617 | 2025-10-01 03:30:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f1bf1324-68e7-3459-9541-34ee82c62e55 | -8.55224 | -44.65419 | 2025-10-01 03:30:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 12729fcb-3316-389e-8874-35bd91ca64b7 | -11.76223 | -46.85516 | 2025-10-01 03:30:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 374172dc-4c86-3c93-a056-be1868364b34 | -13.98324 | -44.90925 | 2025-10-01 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 87a620bb-ebc8-3c4f-aa84-e616d163801f | -12.95573 | -46.42441 | 2025-10-01 03:30:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a01bb2ab-b07e-3b69-9c50-6ec5b5d54084 | -11.63271 | -47.5009 | 2025-10-01 03:30:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5b88c3e8-3c68-30ad-b866-290d8a7c57c7 | -11.58603 | -45.04554 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e983424f-1fdd-35cc-bad4-d10631281b1c | -11.46647 | -45.10304 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 2e590408-5d3e-3487-8bfa-f041f9e1bbb0 | -13.97863 | -44.91861 | 2025-10-01 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7054f92e-c08c-3ccf-8447-d369e83669cd | -10.21611 | -43.04063 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 95cd6002-3ed0-3964-ba1c-88ac534d5393 | -11.45836 | -45.09703 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 57462523-39dc-320a-b73b-ce4f2532bf2e | -11.85171 | -45.0219 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 181acd51-630f-3d01-8f47-1c5914f423aa | -10.73782 | -45.3791 | 2025-10-01 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e44f72e1-81fd-3f82-a6a6-459d90939f4b | -9.93935 | -43.66393 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3209b183-3678-31e3-8e7e-4d48a7041e9c | -10.90239 | -46.55853 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bd4dad6d-a732-305e-9c2c-ab88a3bafdf0 | -8.53447 | -44.71143 | 2025-10-01 03:30:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0fe061c9-9532-3666-bec9-116390b1c95d | -10.90368 | -46.55223 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 0b6c045f-ce49-3ee4-8d6b-fbbcaacb1022 | -13.6711 | -48.09064 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e3204a48-8218-3099-86fe-2a13b804be58 | -10.83881 | -45.41273 | 2025-10-01 03:30:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74d08231-0e94-3e3e-a086-3f6f41cd46dd | -8.23548 | -45.51576 | 2025-10-01 03:30:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 717ed265-7d58-394d-850d-441a7209d8d2 | -12.35074 | -43.21625 | 2025-10-01 03:30:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f58b593a-72b5-391e-8ed7-401f9a6c19c3 | -13.67282 | -46.79298 | 2025-10-01 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 02caae58-294c-3503-ba9d-c0a5e254e3c1 | -13.6535 | -47.31911 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f38bdcd-ee12-39b4-a3d3-12afe61f9816 | -10.90705 | -46.56643 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| aa596237-028d-3e8d-ab08-4fdd94bd2cfa | -9.94687 | -43.59321 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7f61f9b-4e37-3a63-84eb-9395503fc339 | -10.93375 | -46.51029 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 29058683-ecf1-3b22-bcd8-ebfe538a35ad | -11.13363 | -43.3803 | 2025-10-01 03:30:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 25d7b8fc-3a39-3d48-a05f-5c4a88fc3eb0 | -13.98229 | -44.91377 | 2025-10-01 03:30:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ee7a6665-7195-35c9-8d4b-e05f7258e176 | -11.73627 | -46.87531 | 2025-10-01 03:30:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1c9ad390-53b3-3d31-8b08-78aedb7a09e0 | -10.33298 | -42.46371 | 2025-10-01 03:30:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d1854954-3adb-3638-89b4-e51d47357e80 | -10.83232 | -46.66037 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ca7d1de4-2963-3cb2-8758-4f07d1de4b8b | -10.91056 | -46.51853 | 2025-10-01 03:30:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d44b6b39-30f3-3a1f-bd93-15d5460d34b6 | -11.81793 | -44.99693 | 2025-10-01 03:30:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a6679fac-ebe5-3c2c-aa79-fb1d7eddd1ae | -13.37174 | -47.32901 | 2025-10-01 03:30:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README19.md)
