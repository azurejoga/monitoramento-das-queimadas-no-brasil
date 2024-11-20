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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ccc6f91f-46ca-3463-aa4a-c971f78d6417 | -3.0859 | -54.66855 | 2024-11-20 04:27:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35479b41-2e39-330f-b528-a113d3cd310a | -4.88851 | -42.61934 | 2024-11-20 04:27:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6b9c5b0-92f7-34b5-940c-b22f8ca2df66 | -6.54082 | -44.18492 | 2024-11-20 04:27:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ecf65d7-5233-36d4-8b03-a141620f8d20 | -5.0709 | -45.16099 | 2024-11-20 04:27:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c60511b1-5aaf-30ac-a3da-c5efb8bc1e1a | -3.05317 | -48.50221 | 2024-11-20 04:27:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6aa9a373-cfa4-353a-9e75-66b092f07615 | -2.34436 | -54.78375 | 2024-11-20 04:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6c3e6830-8a5e-3fe1-bd49-c8d78dd3c50e | -6.54025 | -44.18874 | 2024-11-20 04:27:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 48f590ff-7de3-3ee1-969a-d0dec9062d00 | -8.00119 | -44.38494 | 2024-11-20 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3d42d6d8-e7e6-3575-9268-21b5caa80da0 | -7.99861 | -44.38751 | 2024-11-20 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ee87657-c40e-34c0-93ac-78be0dc4d5e2 | -4.51623 | -50.57692 | 2024-11-20 04:27:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e00f4cc5-3998-3190-8a11-3390ace2f6fc | -2.9084 | -53.05991 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cfcd7589-00d7-3391-9a82-c75ebfe80972 | -3.13381 | -48.58806 | 2024-11-20 04:27:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 06d932e6-77da-3438-9dac-578d5150fde3 | -2.28247 | -53.63693 | 2024-11-20 04:27:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8a1b207-8e11-3591-a512-c1b0110fbeda | -5.60072 | -46.17544 | 2024-11-20 04:27:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32182888-39a4-358e-bca7-d9d2bfc69c13 | -8.0006 | -44.38884 | 2024-11-20 04:27:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 54751214-3df9-3853-97b9-bcb96ba21891 | -5.06398 | -45.3609 | 2024-11-20 04:27:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ed901c8a-ffdb-3dfd-88f2-32f783ac8731 | -3.6118 | -54.74735 | 2024-11-20 04:27:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 904379bf-c838-344b-8a2d-f897bba82ac0 | -4.11028 | -51.04912 | 2024-11-20 04:27:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2019f74b-ee07-3414-b873-e558f41b1c51 | -4.38096 | -50.41545 | 2024-11-20 04:27:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7102c1e5-9496-3776-aeef-a6071f738312 | -5.2303 | -49.5224 | 2024-11-20 04:27:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 712846ed-763c-3b02-bb94-e05575b260d0 | -5.00006 | -45.53279 | 2024-11-20 04:27:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 278e0af4-3eb3-35e8-b7ac-9b6f0c90b908 | -4.99359 | -46.9251 | 2024-11-20 04:27:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a3c85715-c2e5-3622-b784-c71dd2a959b7 | -2.62881 | -54.27346 | 2024-11-20 04:27:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d38fc051-e024-33de-98a0-6c1d4c0008bc | -4.94316 | -50.6428 | 2024-11-20 04:27:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dd2ef1c7-5639-337a-8a0c-9c564ed7f568 | -2.9178 | -53.0616 | 2024-11-20 04:27:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 52860c2d-af1e-3c05-a648-06666e9506c4 | -3.94438 | -46.71707 | 2024-11-20 04:27:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 43cee489-272f-3b11-aa6d-5da2edca4ebf | -3.71406 | -51.84261 | 2024-11-20 04:27:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 67b53ee5-ad28-3ef5-b9cf-dce014a7d2b2 | -5.96611 | -48.06911 | 2024-11-20 04:27:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4154b409-f1bc-30dd-b286-343878080326 | -11.10016 | -54.62259 | 2024-11-20 04:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8046382b-4fcf-30a7-9a7c-8104a43ae672 | -15.87282 | -53.27847 | 2024-11-20 04:29:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5b6af7df-f4b4-34e6-9fe3-b2f7e965a5dd | -15.87764 | -53.27386 | 2024-11-20 04:29:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7da769aa-a82e-3beb-af75-2fd530c8b27c | -12.89057 | -48.51236 | 2024-11-20 04:29:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 657b0f4a-fc09-3663-8590-fcdc383aa2b1 | -11.1024 | -54.63661 | 2024-11-20 04:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a9a8754-098d-3c75-82cd-58435acf0295 | -15.87468 | -53.26806 | 2024-11-20 04:29:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 903cb323-d1be-3c93-871d-ba7d648cdcf1 | -13.95066 | -42.59152 | 2024-11-20 04:29:00 | NOAA-21 | IGAPORÃ | BAHIA | Brasil | 2913408 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 934f692f-52a9-3407-b502-910d2b959b5f | -12.5303 | -44.53383 | 2024-11-20 04:29:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ce32267-9fa8-3c5c-9dc8-29eaabcf557f | -11.50065 | -54.2783 | 2024-11-20 04:29:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| abca7e33-0232-3e05-9edb-ab9c6994c210 | -16.74359 | -45.76695 | 2024-11-20 04:29:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 91a4e6b7-c6a2-32c9-afa0-ad51f3577902 | -11.59096 | -42.97688 | 2024-11-20 04:29:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 813e7da3-307f-31b9-98c4-e12224b0c53e | -11.11328 | -54.62881 | 2024-11-20 04:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 52e26af6-be12-3587-91b9-5ab9d9fb53ef | -11.49978 | -54.27757 | 2024-11-20 04:29:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| afedeb00-dfad-30bb-a727-8503adbd8dac | -11.49545 | -54.28184 | 2024-11-20 04:29:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0fc5b629-4d06-38a5-8ddd-d37df0910121 | -11.36216 | -44.57738 | 2024-11-20 04:29:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3a79acfe-b6f8-3219-ab07-4a7a25fc9758 | -14.87151 | -43.15179 | 2024-11-20 04:29:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 31b56a23-f359-3fc0-a868-bcc26ff5bd07 | -16.74 | -45.76641 | 2024-11-20 04:29:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 04297ceb-1166-348c-bd3b-91b8c83b9317 | -15.86988 | -53.27255 | 2024-11-20 04:29:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e5750b3d-2881-3818-8600-3593745ec05f | -15.87376 | -53.2732 | 2024-11-20 04:29:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5f5c47b5-8328-3515-96e9-25f3b458db1c | -11.10697 | -54.63743 | 2024-11-20 04:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07332943-28fa-3da6-9445-632e8731dd66 | -12.4599 | -38.47809 | 2024-11-20 04:29:00 | NOAA-21 | SÃO SEBASTIÃO DO PASSÉ | BAHIA | Brasil | 2929503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 83758011-fa30-3f96-b720-b31b73cb5347 | -12.03975 | -54.65324 | 2024-11-20 04:29:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f0d1750f-0fb8-38af-897f-1e9454c92d6b | -12.12788 | -54.29009 | 2024-11-20 04:29:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9676e41a-7d9b-3ea5-8703-2bdb3b266fce | -12.85755 | -43.81749 | 2024-11-20 04:29:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 39175e38-3dcf-348e-9e8d-3a8c4e0a6f6b | -12.05116 | -44.48679 | 2024-11-20 04:29:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be9e35e2-777e-31d6-bfc4-6ef2708147ba | -11.1039 | -54.62809 | 2024-11-20 04:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6c48a10-5a97-3481-ab33-6df99fb7c660 | -11.10784 | -54.63269 | 2024-11-20 04:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1c102742-05c6-3e0e-8a37-b6dfc8d1f1c7 | -12.5259 | -44.53516 | 2024-11-20 04:29:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a350abf-0209-3f83-be10-a31a8b117bdf | -11.57161 | -44.82958 | 2024-11-20 04:29:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63973add-ec8c-30af-bc30-2b7109394837 | -11.11219 | -54.63454 | 2024-11-20 04:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 448f8b24-0611-3468-97cb-0b59bfb5c148 | -10.63001 | -54.60996 | 2024-11-20 04:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1be3fc40-3734-366b-ae46-c67ccf5fc865 | -9.99193 | -55.65236 | 2024-11-20 04:29:00 | NOAA-21 | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7c474d2c-c898-3356-a7be-910aece87fb8 | -9.99691 | -55.65329 | 2024-11-20 04:29:00 | NOAA-21 | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 360ad6e8-800b-392a-bd81-e21dbadff554 | -11.31473 | -54.02167 | 2024-11-20 04:29:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d36a6c1b-b299-3c2c-a036-aaa363df1bca | -12.58298 | -52.4937 | 2024-11-20 04:29:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bb4b0256-0b6a-3b15-9ba6-725ab3513d20 | -12.03609 | -54.64779 | 2024-11-20 04:29:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d4052c9-f090-3ac0-9913-71c5faaaae2b | -18.16819 | -39.63888 | 2024-11-20 04:29:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 9a2110d5-907a-3982-b8e8-fb03084405b6 | -12.85669 | -43.82011 | 2024-11-20 04:29:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d00472e0-6d39-3c22-9484-13c513d0de6d | -11.0939 | -54.63127 | 2024-11-20 04:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4845c697-38b4-3a05-856d-445762e26644 | -17.09592 | -43.80529 | 2024-11-20 04:29:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6885122d-ccd8-3509-9fc5-8f954085c383 | -15.30405 | -56.53144 | 2024-11-20 04:29:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 723a4cde-5a39-3e5d-a8e0-8bc711a01435 | -12.12348 | -54.28935 | 2024-11-20 04:29:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 21236431-a59c-3ccc-8973-44050ca55508 | -11.49897 | -54.28196 | 2024-11-20 04:29:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ccc18e9-900b-3275-afbe-75a735cb5d8a | -12.12866 | -54.28573 | 2024-11-20 04:29:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e94b486f-6e36-3f9d-a8f2-026d775e58a9 | -15.29923 | -56.53053 | 2024-11-20 04:29:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 60ca7778-253c-3a31-960f-ceba85d222c7 | -11.10306 | -54.63284 | 2024-11-20 04:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ffec11c3-dde9-3afd-a761-714b87a69fc4 | -13.29017 | -39.80902 | 2024-11-20 04:29:00 | NOAA-21 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| b8371303-ec2b-3e7c-91b6-41596a843ebc | -13.59366 | -48.77773 | 2024-11-20 04:29:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5a8fd721-e93e-348b-aa95-66f9fbed6914 | -12.79168 | -38.22295 | 2024-11-20 04:29:00 | NOAA-21 | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 0d91a9f1-2428-34b1-9053-de3a919f22c2 | -11.09848 | -54.63205 | 2024-11-20 04:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5ad86e4-2b8a-35fd-a4b9-1577927f5e99 | -12.27162 | -44.98589 | 2024-11-20 04:29:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 812540f3-fe4a-3f14-9622-a9013f67e171 | -11.09932 | -54.62731 | 2024-11-20 04:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8d37d11-db07-3182-a87f-6ce2a827051f | -11.09764 | -54.63683 | 2024-11-20 04:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd909061-f309-338d-9a5a-b20b8b5170e5 | -12.12426 | -54.28499 | 2024-11-20 04:29:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b0aadc4e-a224-3768-a2c2-efc7be2b8e26 | -11.10847 | -54.62893 | 2024-11-20 04:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 613df111-966e-3c42-8f43-327bf9e82d27 | -15.87672 | -53.27903 | 2024-11-20 04:29:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0c1ddf2-3352-34f9-b03b-e280409c5238 | -17.67653 | -42.74179 | 2024-11-20 04:29:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c76eaf8f-c226-366e-b4ca-162927a3552c | -16.73941 | -45.77066 | 2024-11-20 04:29:00 | NOAA-21 | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1631423a-eb1d-3806-bf3f-eabab4951b2a | -11.11303 | -54.62978 | 2024-11-20 04:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 41fa19fd-b6b5-3c65-a3af-8edee97fb1fe | -13.29084 | -39.80347 | 2024-11-20 04:29:00 | NOAA-21 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 0cdb755a-5d83-3a45-a1a9-465f9b2320eb | -15.29819 | -56.53597 | 2024-11-20 04:29:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6f148a7c-3b89-3d8c-8c33-829167f25a22 | -11.38112 | -54.92769 | 2024-11-20 04:29:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7fca50f4-645f-38be-86f1-2555cea443b5 | -11.10415 | -54.62714 | 2024-11-20 04:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d9e64ea-d9d7-3518-8125-50ae207f4884 | -12.04059 | -54.64864 | 2024-11-20 04:29:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 223bcec0-d271-34c0-9262-79643f1f345f | -11.1124 | -54.63355 | 2024-11-20 04:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 1c1900e3-01cc-357c-bba6-b80264fd08d1 | -11.09558 | -54.62181 | 2024-11-20 04:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d601a852-66e8-3310-9760-2ce57c54a580 | -11.49455 | -54.28109 | 2024-11-20 04:29:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bda4e15e-a7be-3116-9b7c-5abfc512cf36 | -11.10474 | -54.62337 | 2024-11-20 04:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86d70ae1-85cb-36ea-a9c4-6fa2e5c31d84 | -12.03692 | -54.64319 | 2024-11-20 04:29:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 35731923-ecef-3316-b3fc-ae8575b1cf12 | -11.37992 | -54.92609 | 2024-11-20 04:29:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f97b9dac-8746-3559-83dd-dcd2e4c1ce87 | -11.10763 | -54.63367 | 2024-11-20 04:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 754dce8b-cab5-3fa1-a9b6-9b2463d04334 | -11.10328 | -54.63186 | 2024-11-20 04:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README40.md)
