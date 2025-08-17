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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b0fa4716-ee55-3036-9f69-363110b18b98 | -5.81024 | -59.21431 | 2025-08-17 05:31:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4c44c21-edc9-30b9-b763-7599a9eb1da8 | -7.42459 | -60.59728 | 2025-08-17 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b98e85a-a02a-3f7e-93bd-2be6c4655793 | -9.50278 | -60.53226 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80b50605-6a54-3391-9f92-67ccf02d8069 | -7.10125 | -59.22519 | 2025-08-17 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 733f275e-fa21-3cc5-9bb8-237c3661b8e1 | -9.19887 | -59.63465 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16d03ecd-540e-3906-b1ea-ab2d5018cc93 | -11.36126 | -55.39034 | 2025-08-17 05:31:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| edcbf26c-f9f9-3656-b66c-a51c5411c0f8 | -11.35767 | -55.40186 | 2025-08-17 05:31:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c598b5e6-f33b-39a7-bc19-dd10f103bc2f | -5.45571 | -60.13184 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 811dee1f-a8b9-3cdc-9d5f-f7b4bfff4312 | -8.98895 | -60.49572 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4b4463c3-dac5-37ff-9f64-83f71224c495 | -9.00038 | -60.53633 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de2317b0-1cd3-36ae-aa13-6bc560708313 | -10.43252 | -60.28848 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7323ce09-f734-3900-9c53-eeabf05ca82b | -9.51147 | -60.52182 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a338cc40-33c8-3704-a907-c985d00d0317 | -8.52104 | -70.82117 | 2025-08-17 05:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a721a4b4-a4aa-32c6-8129-f5b80a54127d | -8.91947 | -60.76548 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31b9f6da-d637-3852-82ad-443ecb074489 | -9.99916 | -65.28452 | 2025-08-17 05:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66323a2d-9bfe-36cc-aed4-9516c82c7675 | -12.99881 | -56.86916 | 2025-08-17 05:31:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41d328e2-3f8b-37df-8571-8f4a61bb78e9 | -8.99178 | -60.52338 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ebe3936-99f1-36e1-8f6a-e767db5dcc96 | -8.99985 | -60.51687 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 742abe61-648b-3d43-8d7a-8dedc14dcbe6 | -8.97512 | -60.4936 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a6d92d8-5620-3972-95d9-d9fb236b817e | -8.8736 | -68.50793 | 2025-08-17 05:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f035212-4d24-32c7-b0b6-12f3a177c901 | -11.36555 | -61.84792 | 2025-08-17 05:31:00 | NPP-375D | PRESIDENTE MÉDICI | RONDÔNIA | Brasil | 1100254 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| a2046836-e192-37ea-80eb-62b6ed19140f | -6.07508 | -59.95967 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bfe3feb3-c9ee-3973-ad69-5969a23f8c2e | -8.79875 | -52.0705 | 2025-08-17 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c214589-944a-357e-b0ed-8dd7ccc787d6 | -9.18143 | -59.65303 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c698df9-a81c-3840-9c74-43034c0a93bf | -8.23599 | -61.46912 | 2025-08-17 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b8448bda-76d6-3cbc-a17c-516493fc93f2 | -9.13534 | -60.74481 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b5184851-fc7b-3e03-94e7-2dffae732c55 | -5.80136 | -59.22504 | 2025-08-17 05:31:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d3cf974b-0937-37fe-8fea-6de51b003821 | -5.45855 | -60.13601 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58552186-4921-3198-9272-bed75cffad38 | -9.14132 | -58.29724 | 2025-08-17 05:31:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 37385597-d2e1-3565-a145-70799625f13d | -9.22217 | -59.65073 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 96ca5835-0c55-3db6-9857-41e7b4c5a59b | -5.0079 | -62.39997 | 2025-08-17 05:31:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 758a1a1a-f61b-3a6f-91ab-abaaed32f845 | -9.18501 | -59.65366 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| adf529a2-3ba4-32f2-bb31-64fa499f28f8 | -11.35566 | -55.39522 | 2025-08-17 05:31:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2fd4e2f0-149b-3f8d-a82c-7a8250791fb1 | -6.07394 | -59.96713 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fb9fee33-494a-392e-80d0-6f41475e6059 | -9.18247 | -59.69523 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f6fba68-1a44-3149-b020-38f70d85e1cd | -8.98204 | -60.49466 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| c0fb3efc-e2ac-30c4-a90e-cf3bb8525d0e | -9.76405 | -67.53379 | 2025-08-17 05:31:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 408bc69c-9674-3984-92a0-745928e02b13 | -11.35906 | -55.39109 | 2025-08-17 05:31:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b4fde1b9-d2f4-352d-a95e-5ea82e523db7 | -9.19025 | -59.69221 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab28369a-184a-317a-b865-f267b9c25e6c | -9.50858 | -60.51748 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f27f379-7833-3d88-bf1c-86300a5c6cea | -10.12587 | -57.77161 | 2025-08-17 05:31:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7879a022-f297-3dd3-953a-60554118f7a4 | -8.9981 | -60.52824 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a5ebe47-7c3b-3380-af96-3d587acf3ef2 | -11.36218 | -61.84738 | 2025-08-17 05:31:00 | NPP-375D | PRESIDENTE MÉDICI | RONDÔNIA | Brasil | 1100254 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c9d10f7-991f-3a8e-b766-cb310f9c69aa | -7.49068 | -63.80964 | 2025-08-17 05:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c1854f7-6ffe-32b1-8cb4-50d9a689c307 | -6.07852 | -59.96017 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09131684-e034-3406-a76c-ca47b80fab5c | -6.66801 | -58.81419 | 2025-08-17 05:31:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6591770-ab98-3617-9842-9472fbb8e52d | -9.13745 | -58.29665 | 2025-08-17 05:31:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed2690d1-d646-3838-8590-af0d1c3e9c67 | -9.50625 | -60.53278 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6d85102-83e0-3bd3-a90f-a8fd5744594c | -9.55424 | -63.66512 | 2025-08-17 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5ce55212-19fb-3ee9-97b6-bfc05a0910e7 | -8.9998 | -60.5401 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 049ed4e5-18a0-3a6b-9635-76025c7ef755 | -10.36229 | -64.50539 | 2025-08-17 05:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c69e238-841f-3bb6-a098-f9f2e45e845c | -10.31161 | -54.16144 | 2025-08-17 05:31:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fc6f460-dfa9-3ea9-8971-3c47a875f271 | -10.00232 | -59.96356 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d6c7f83e-6be9-3b82-8e26-bb002918d7d7 | -8.98542 | -60.54174 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70b3aa81-fbed-30d8-99c1-415254361797 | -5.45798 | -60.13967 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7897d5d5-319b-3c51-aaa0-4ce9970578d6 | -6.08653 | -59.93079 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c5d9608-a1e9-3b2d-a50c-547b4e9c4e09 | -13.01288 | -56.86633 | 2025-08-17 05:31:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 01bb350c-9646-3a88-a5c8-c7a2afd79a7f | -11.35493 | -55.40056 | 2025-08-17 05:31:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 161bc4f6-d59c-3124-ae89-96222cf49f95 | -9.55367 | -63.66867 | 2025-08-17 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0df05b52-07a8-3958-935b-f2ee619c6de7 | -9.55816 | -63.6621 | 2025-08-17 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c15e662e-a7f5-3e9f-adca-4ca224d52314 | -8.89834 | -60.74322 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4be2856-397b-3258-a27c-ea47f2df410e | -6.67209 | -58.81316 | 2025-08-17 05:31:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f010ba1-f609-3d03-b965-3fbd23583490 | -10.35889 | -64.50483 | 2025-08-17 05:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 69d82be4-7dbe-3e37-b5cd-b2af3c4c2dcf | -9.50394 | -60.52462 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3429dd84-9d63-3423-b84b-94cbb948eacb | -6.46462 | -55.89529 | 2025-08-17 05:31:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ef039022-3a68-3417-81b9-4a99ae172bfd | -5.00456 | -62.39945 | 2025-08-17 05:31:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c99ca914-ab7a-3515-b8fa-a5ab8faedc6e | -9.92738 | -60.46429 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ca8654d-3401-31d1-8379-5ec0f7aaf61d | -8.98662 | -60.51091 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0532ca65-e8fb-35ca-83c2-3a0ead98628f | -10.35193 | -64.46203 | 2025-08-17 05:31:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c452929-daa3-3810-8e9a-31c8f8334a53 | -8.88075 | -68.51768 | 2025-08-17 05:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 215aa90f-a223-3488-b409-7b2b3cff73af | -9.54114 | -63.5755 | 2025-08-17 05:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 02a89e8c-e917-3fce-9f36-9ab7bfd995ce | -9.26414 | -60.77167 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c57543e-aa71-39c5-a599-0d5ada278d01 | -8.80573 | -52.02935 | 2025-08-17 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b04c1925-4d2e-39ae-9924-176b2623c6c7 | -8.98194 | -60.5644 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7a51981-ce11-384a-aee9-74dc8e3200f9 | -9.50683 | -60.52896 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8630676-5327-3f36-a801-c4265acf37be | -9.51432 | -60.54963 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 663ecc0d-59e0-3c05-a0d3-1528c1753c30 | -9.21858 | -59.65019 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 30fc90e1-cbf4-37bc-a90c-363780828848 | -8.9831 | -60.55684 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f4e2f638-d093-3088-8135-4c302bd4e853 | -9.14518 | -58.29784 | 2025-08-17 05:31:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0fb85d82-f9c2-38f3-b26e-6fff7389d503 | -8.79825 | -52.07443 | 2025-08-17 05:31:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07d3e8c5-bd46-3985-ad13-5fad22649336 | -9.18563 | -59.64952 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c5a0ccf-49e9-3e28-805c-102ff377f9a1 | -11.35639 | -55.3898 | 2025-08-17 05:31:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b38a7d85-cc79-3102-9b41-022c3090b931 | -8.23709 | -61.46206 | 2025-08-17 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b00d6ce5-57ae-3480-97df-1fa888921730 | -9.19948 | -59.63052 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 86622d8a-0b00-30a4-aa69-e0556cf874a9 | -9.18921 | -59.65012 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4cb25f9-2cfb-3968-83b4-60433e17f8a9 | -8.99465 | -60.52769 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 279fc46b-8863-35d4-8a79-909d8c549b9e | -8.23989 | -61.46611 | 2025-08-17 05:31:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 905d45fb-9102-3298-9bf1-e5fd0a4db147 | -7.42516 | -60.59361 | 2025-08-17 05:31:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 81af76b3-dff9-38a9-82d9-ff47226dbbda | -11.35836 | -55.39651 | 2025-08-17 05:31:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 271f1c3b-7b8b-3d12-b2ef-7653ebabddfb | -9.51319 | -60.53383 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 70024f88-fa5f-3124-ad7c-cbc85904980b | -8.98655 | -60.55738 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d0565fc3-d574-3676-9a2d-e61d02659c45 | -9.88261 | -64.27248 | 2025-08-17 05:31:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0258f22a-6d9e-3bdc-b312-4f597773391f | -6.90172 | -63.04269 | 2025-08-17 05:31:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6cd32886-1617-32e5-8f6a-79684bd707c9 | -5.80076 | -59.22895 | 2025-08-17 05:31:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac7e5d32-e335-365e-9263-97c1094c1130 | -8.88574 | -68.51434 | 2025-08-17 05:31:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c4cb76a5-a0b8-397d-a17b-72ed431f8c88 | -5.45231 | -60.13132 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4b548fbd-fd34-315d-80b3-d0ea74f927d1 | -9.00155 | -60.52878 | 2025-08-17 05:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35caa370-1abe-3017-ab58-60e9cb34801a | -9.508 | -60.5213 | 2025-08-17 05:31:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9b700fbb-47b4-3cfe-94bd-f109e112fb16 | -10.11879 | -57.76325 | 2025-08-17 05:31:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c5233fe-efc6-3218-af6d-6676b288596d | -6.06819 | -59.95865 | 2025-08-17 05:31:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README34.md)
