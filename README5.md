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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 37c16c44-f50e-3147-9b99-4a597b306ada | -4.2891 | -59.961899 | 2026-09-07 01:29:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2de66a2c-73ab-397d-bd75-8f5e6a3371d0 | -5.9984 | -57.699902 | 2026-09-07 01:29:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ecc76e69-4872-3ed7-b5cf-3851927ea221 | -2.9773 | -60.936401 | 2026-09-07 01:29:00 | METOP-C | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 069bfa41-55d9-31ec-a22b-d94b7f97a874 | -5.2642 | -60.118 | 2026-09-07 01:29:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9abb6443-f238-3a4e-8913-05fd023aabe4 | -6.655 | -59.929901 | 2026-09-07 01:29:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b3de0300-c5f4-3be2-ae7a-385f866ccde4 | -3.0843 | -61.5359 | 2026-09-07 01:29:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 97800264-4c73-36c5-b8a5-2eb6826d366c | -6.1328 | -57.744701 | 2026-09-07 01:29:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 395d3a27-5fc8-3ecf-90b5-0c714ad620eb | -13.2565 | -61.731499 | 2026-09-07 01:29:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3c1720ad-645a-3047-87ec-e502b68e9863 | -6.5086 | -58.2869 | 2026-09-07 01:29:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3256194-571e-3940-81e0-2fcb4ecf127d | -5.2645 | -60.163601 | 2026-09-07 01:29:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 99770204-4e4b-314d-938a-ab37e6767540 | -5.1633 | -55.9687 | 2026-09-07 01:29:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 299a8d5d-7586-3476-9519-8b0f218d5292 | -6.6861 | -59.930302 | 2026-09-07 01:29:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 607cf254-0fe8-33cd-b9e4-47162eac1e4e | -5.8304 | -60.246101 | 2026-09-07 01:29:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 15df2d86-c5de-3116-9e1c-ef57b2c90012 | -7.7028 | -55.385601 | 2026-09-07 01:29:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ba5dbbb-b1aa-30aa-9d2c-edf89487d23d | -5.297 | -60.125801 | 2026-09-07 01:29:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 95262ec9-72af-3dc7-ba7e-e0dbf7b9934d | -6.6567 | -59.937 | 2026-09-07 01:29:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0a3fac10-d45f-3d5d-b53c-cc437645df2c | -5.3767 | -56.042599 | 2026-09-07 01:29:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20c1d404-8735-37bc-8de5-dd1855d07cae | -6.0631 | -57.798901 | 2026-09-07 01:29:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d177d3a-65ce-30ac-b7f2-172945acb1bc | -6.0006 | -57.7089 | 2026-09-07 01:29:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74ab9add-493b-34c3-9be7-ab9e96cc4019 | -3.3845 | -61.315899 | 2026-09-07 01:29:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 69b49655-1d74-3960-b30b-ce4bbfdd80c6 | -3.1502 | -60.657398 | 2026-09-07 01:29:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f015651f-9046-38a3-b0da-021e830567e7 | -2.8798 | -50.453098 | 2026-09-07 01:29:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9253110-f9ce-3cd2-8e80-94501355932f | -6.1191 | -57.642899 | 2026-09-07 01:29:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4efb5777-3f36-35dc-87d6-4bf4a207f23c | -3.8337 | -60.7584 | 2026-09-07 01:29:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2daf27a6-29a3-30d4-b4c2-49c579d3a034 | -3.3885 | -59.415699 | 2026-09-07 01:29:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ad919f70-3f16-3cc4-8417-4ab999948a45 | -5.1605 | -55.956799 | 2026-09-07 01:29:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e34035c7-bc93-3eef-9a83-823f2e1b714d | -6.0589 | -57.780899 | 2026-09-07 01:29:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 51b00526-2a6d-3b94-b9a4-92b5697bb704 | 3.9725 | -60.555901 | 2026-09-07 01:29:00 | METOP-C | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9c0d37cf-f750-32a7-b5e1-16dda1751e68 | -5.2628 | -60.156399 | 2026-09-07 01:29:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b724bd34-35e6-38d0-ad1d-23e233dc5dc7 | -8.5294 | -63.8853 | 2026-09-07 01:29:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 9396baa8-fae9-3dc1-8a5f-c5c330562d16 | -6.0082 | -57.697601 | 2026-09-07 01:29:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd2bb28d-d458-387d-a19a-1ed1abbac849 | -13.2549 | -61.724098 | 2026-09-07 01:29:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f6ea0bd5-66f8-3a73-9d09-4389864c3702 | -3.3943 | -61.313702 | 2026-09-07 01:29:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c2984dfc-1691-308c-bf3f-edb8b1f1355a | -13.2353 | -61.7285 | 2026-09-07 01:29:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6e4d7328-61c6-3507-87e4-0e1496cecb1c | -3.6159 | -60.575001 | 2026-09-07 01:29:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 23e2da52-0740-30d5-b064-d3ed2236308c | -3.3787 | -59.4179 | 2026-09-07 01:29:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b221478f-04d6-3eaa-9c09-fb7edbfd0554 | -3.1468 | -60.643002 | 2026-09-07 01:29:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8436bd45-c7d1-356b-9353-54ed7654a8eb | -8.7612 | -62.428699 | 2026-09-07 01:29:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e61ed20f-2f5b-374d-9a06-9c23bc272120 | -6.6681 | -59.941898 | 2026-09-07 01:29:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b82a22cc-0772-307a-8f07-eae6db3521a4 | -3.6143 | -60.567799 | 2026-09-07 01:29:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 94d489ab-f384-3f9d-a4a3-3d79fb527ab4 | -3.3877 | -61.3298 | 2026-09-07 01:29:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8ab7392d-f48a-3246-9a6e-a49cada253b9 | -2.8874 | -50.484001 | 2026-09-07 01:29:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e61cb20c-9276-387d-a436-4c7482979cdf | -7.0566 | -56.468399 | 2026-09-07 01:29:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8e2b7b9-d256-3c39-8b1a-a5398e44fe5e | -13.2712 | -61.751499 | 2026-09-07 01:29:00 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3aa94424-1981-3a07-af8f-2b1373694772 | -6.0061 | -57.688499 | 2026-09-07 01:29:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 148cc9a9-11ca-33a4-a5d7-5348ce0220a2 | -5.9865 | -57.6931 | 2026-09-07 01:29:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5585e1b-fa6c-3298-a286-8f185c2cf34f | -3.1435 | -60.628601 | 2026-09-07 01:29:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 51bb2978-4f58-3755-a339-b102822b89c8 | -5.3614 | -56.021599 | 2026-09-07 01:29:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e76e859-f363-3778-b022-0749924c6928 | -5.5934 | -60.247501 | 2026-09-07 01:29:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e2e1b2e4-4595-3c8f-9cbb-a3eee2db742d | -5.8321 | -60.2533 | 2026-09-07 01:29:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| beaf42e6-02e3-3621-a3ab-05d6fc318025 | -3.1518 | -60.6646 | 2026-09-07 01:29:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7356ffaa-03dc-3051-b808-556da5021880 | -13.2728 | -61.758999 | 2026-09-07 01:29:00 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| c3e4f096-910f-3261-9786-dd7017b54614 | -3.3769 | -59.41 | 2026-09-07 01:29:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9813118e-3855-3410-8e6c-318e87c2a4d1 | -2.8895 | -50.450802 | 2026-09-07 01:29:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3f9743b-013d-373c-a4ba-8cc5dfefd10e | -3.1485 | -60.6502 | 2026-09-07 01:29:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5cc0843e-3dc6-36bf-b7ea-288c49d4b4a8 | -6.6535 | -59.967999 | 2026-09-07 01:29:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e46a81ab-cba1-3d81-ad30-5a2a757a1536 | -6.6583 | -59.944199 | 2026-09-07 01:29:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ca2c8815-619a-3944-a716-6e3c1cccafa7 | -13.2843 | -61.717499 | 2026-09-07 01:29:00 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 3cba3d26-beb1-3466-823d-d6456269126d | -3.1452 | -60.635799 | 2026-09-07 01:29:00 | METOP-C | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1c19f087-78e1-30ad-ae5e-8a740be272dd | -3.3806 | -59.4259 | 2026-09-07 01:29:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1b004e85-f757-3308-93e8-f0f4944f73b0 | -13.2352 | -61.7752 | 2026-09-07 01:29:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5c91d47f-d999-3dd8-a469-91e252f3bf1f | -3.6176 | -60.582199 | 2026-09-07 01:29:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cd8c160c-536c-3a9c-bfd1-3a703eb16a35 | -3.1354 | -60.6381 | 2026-09-07 01:29:00 | METOP-C | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bb62b078-5280-3d59-a240-8232890efa87 | -5.9887 | -57.702202 | 2026-09-07 01:29:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 540acd46-f633-39d5-8acf-3b002fc8e2f8 | -13.2451 | -61.726299 | 2026-09-07 01:29:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a044aa09-74fc-3448-838b-0b493cbf58aa | -6.135 | -57.7537 | 2026-09-07 01:29:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5abdbdf-44bd-3808-a12a-bda2224cdd99 | -3.7745 | -61.7561 | 2026-09-07 01:29:00 | METOP-C | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8594a0d5-36ce-35a9-bcc6-e83efebb7bf8 | -7.1178 | -56.508499 | 2026-09-07 01:29:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 703bf0e3-6af4-3810-881f-f356d2bc9cfa | -3.9037 | -60.927898 | 2026-09-07 01:29:00 | METOP-C | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 604fc989-0d0e-3de0-9614-a4592fd78c0a | -7.1154 | -56.4981 | 2026-09-07 01:29:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d219917-93b4-3920-bd0a-988b02a5819b | -6.1114 | -57.654301 | 2026-09-07 01:29:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b11352e-1b59-3689-9aea-4e0a5b72c774 | -13.2859 | -61.724899 | 2026-09-07 01:29:00 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f7aca54c-4a2e-38a8-aeb3-f90a59774a24 | -13.2647 | -61.721901 | 2026-09-07 01:29:00 | METOP-C | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 954acc23-b9b6-3fa2-909a-104cf08d4b34 | -3.7631 | -61.751499 | 2026-09-07 01:29:00 | METOP-C | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d5afa4d4-b3f9-3f9d-bda4-0c9b312a292f | -8.5259 | -63.869301 | 2026-09-07 01:29:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d9c09f77-1aad-3992-a0e9-455aa174831c | -20.5994 | -58.008202 | 2026-09-07 01:29:00 | METOP-C | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f4f9cf0f-01f9-3ffa-843b-31928f4ecb38 | -3.3927 | -61.306801 | 2026-09-07 01:29:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 96f42182-e9eb-3782-bba1-1ea5878b0cb8 | -6.6485 | -59.9464 | 2026-09-07 01:29:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c1899699-13cf-3287-aba1-f02906351a48 | -6.061 | -57.789902 | 2026-09-07 01:29:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| deb7293d-2929-32cc-9368-ec0adf665ee5 | -2.8971 | -50.481701 | 2026-09-07 01:29:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4cca3f4-8ee9-3dc7-abc4-6a3ed905fbff | -3.3909 | -61.343601 | 2026-09-07 01:29:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4b42ccc8-05aa-3020-acfa-12592a90f5e0 | -14.5271 | -59.8004 | 2026-09-07 01:29:00 | METOP-C | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 11a83fef-89c5-3978-8d96-e1bf467a8eca | -3.3861 | -61.322899 | 2026-09-07 01:29:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8c0cb390-8a90-3618-8cae-dca8ba1a9e3a | -5.2743 | -60.1614 | 2026-09-07 01:29:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4a1bc000-9030-3098-86bc-ad1d96b30d5b | -6.6519 | -59.9608 | 2026-09-07 01:29:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 06cb57c9-d1e5-381c-b620-5f3d541d1d49 | -5.4903 | -60.203098 | 2026-09-07 01:29:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7abc694d-cf9d-3587-ba68-996822cbd958 | -6.6779 | -59.939701 | 2026-09-07 01:29:00 | METOP-C | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 6abc4b01-7df1-3d11-9f7f-68ee47f948ab | -5.3683 | -56.0075 | 2026-09-07 01:29:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f85406e-bcfe-3805-8232-eded9a607f7d | -5.4887 | -60.195999 | 2026-09-07 01:29:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c037b59d-91a2-3eeb-ba31-314f0bb34608 | -6.4475 | -58.159199 | 2026-09-07 01:29:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef4f6a3d-f34a-36f9-b4da-204f4360075e | -2.8819 | -50.419701 | 2026-09-07 01:29:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb1d4aa4-2ca3-3c53-90ad-e85b2ccad072 | -5.2889 | -60.1353 | 2026-09-07 01:29:00 | METOP-C | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 27b8d905-c7f4-3d51-8a59-7559b0937c5b | -6.1307 | -57.735699 | 2026-09-07 01:29:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9833d7a-e197-3176-ad05-2406f40420f7 | -3.137 | -60.645302 | 2026-09-07 01:29:00 | METOP-C | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7ae4258c-70cb-3346-8345-e554b017c02e | -8.5179 | -63.879398 | 2026-09-07 01:29:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 17dae4ed-44b4-3c09-91ae-f334b77ded09 | -6.1169 | -57.633801 | 2026-09-07 01:29:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 523d3888-0530-3d1d-97c9-ff06dd539b9f | -13.2745 | -61.7197 | 2026-09-07 01:29:00 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7f8a0df9-d7ca-3dee-bd67-916ad0859212 | -3.4155 | -61.316299 | 2026-09-07 01:29:00 | METOP-C | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8d5a29c5-f932-322f-87a8-f1a6d26d9b33 | -3.7836 | -58.853699 | 2026-09-07 01:29:00 | METOP-C | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b6a9cc12-533c-35b2-8869-f1150abef62c | -6.5105 | -58.2952 | 2026-09-07 01:29:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README6.md)
