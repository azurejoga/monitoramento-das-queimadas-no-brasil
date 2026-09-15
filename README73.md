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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7109c734-8918-31d4-92f2-ac9c44d034dc | -7.01884 | -44.60709 | 2026-09-15 12:06:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| b0a00f64-1b28-3276-b513-cda9aca84efc | -6.69357 | -58.69377 | 2026-09-15 12:06:00 | TERRA_M-T | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 9a329fc9-9a7e-32c9-82ab-bbec646140d0 | -7.10181 | -47.48511 | 2026-09-15 12:06:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| f6e561bb-5a79-32d8-bcd8-09f835ab29aa | -8.84951 | -45.87663 | 2026-09-15 12:06:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 0348fe5d-366d-3ede-a7c9-8727e86f9624 | -6.38227 | -51.66653 | 2026-09-15 12:06:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7ec2751a-e951-3cbd-a2bc-59132dd58a5d | -11.51951 | -45.78184 | 2026-09-15 12:06:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 091cf633-8a10-3c98-9711-2a947678029c | -5.71995 | -51.85141 | 2026-09-15 12:06:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f3c71f70-3888-3fa7-83c7-c9494c6abbba | -10.87687 | -46.33326 | 2026-09-15 12:06:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 732419aa-c762-34ff-95a6-55b403c60496 | -9.3533 | -50.11797 | 2026-09-15 12:06:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 166.6 |
| 05642f56-0434-31a7-9271-cefc8bf76137 | -4.51577 | -54.9665 | 2026-09-15 12:06:00 | TERRA_M-T | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| e795ebc6-6635-3f52-9bd1-8065faffdba5 | -5.98644 | -52.11447 | 2026-09-15 12:06:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b27250d7-51f7-39b0-a0d2-c0dbe88c3218 | -9.3513 | -50.12327 | 2026-09-15 12:06:00 | TERRA_M-T | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 424bb31c-0b67-324a-86d3-a7ca5f3ef47a | -7.17054 | -44.22612 | 2026-09-15 12:06:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 081fd634-7ccc-3536-bbc8-d4470f88402a | -6.16453 | -52.74202 | 2026-09-15 12:06:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 39a23ac2-6e93-333a-be00-77fff87246bf | -9.75953 | -46.11787 | 2026-09-15 12:06:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 44.8 |
| ff9658a9-5831-3d9a-8cf3-246d1b36d067 | -12.32372 | -47.97516 | 2026-09-15 12:06:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 48.8 |
| bd7a2ef0-6bf8-3d41-a5b8-75df3100f0cb | -11.49943 | -45.80018 | 2026-09-15 12:06:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 64.6 |
| ef82f3a4-c604-32c6-a1d1-527bd3aaf89e | -9.42377 | -47.85718 | 2026-09-15 12:06:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 32.9 |
| e2d81847-25f2-36ce-b6ba-7f745ab57a9e | -15.5738 | -48.81095 | 2026-09-15 12:08:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 5dbb1e3a-8954-335d-8f02-2a40d8257fd2 | -13.5565 | -51.45218 | 2026-09-15 12:08:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ec855267-bec5-3a63-9825-bd0752ec4bce | -14.36863 | -52.46477 | 2026-09-15 12:08:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 22.6 |
| f62f3c2e-3e34-30c6-a094-78e639da5719 | -12.12713 | -57.18951 | 2026-09-15 12:08:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9fe437b1-74b1-39de-95f2-ff6bea7ebe6f | -13.7026 | -51.80802 | 2026-09-15 12:08:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 8c4990ae-8588-322d-b345-5ff35ce45ca6 | -13.21744 | -51.63697 | 2026-09-15 12:08:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| ea02d971-3773-3a21-af94-af9f2ad3b29d | -14.40285 | -45.26069 | 2026-09-15 12:08:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 827d4871-f621-3fd0-9f32-581ed799ca5d | -15.57904 | -48.81705 | 2026-09-15 12:08:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 51.8 |
| d6924194-7a5d-3f50-8b85-dcb251514577 | -15.57713 | -48.83387 | 2026-09-15 12:08:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 9fd86c19-443a-3c72-82af-e795fba20a68 | -16.06658 | -49.92586 | 2026-09-15 12:08:00 | TERRA_M-T | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 6d8ee56c-123e-3598-89ae-f70bfad8c022 | -13.21605 | -51.64753 | 2026-09-15 12:08:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1745cd38-e65b-30f6-bdab-f11af143e1ec | -13.59852 | -47.89643 | 2026-09-15 12:08:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 77328a1e-4967-3e4a-ba04-a057bb0b1fd2 | -14.45037 | -49.02524 | 2026-09-15 12:08:00 | TERRA_M-T | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 2fc9d3ee-d5d2-30fd-949b-66deafc06af0 | -13.7012 | -51.81841 | 2026-09-15 12:08:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 2d45ea5f-f8bf-3d81-bc96-28fe38ff52ac | -16.06722 | -49.93242 | 2026-09-15 12:08:00 | TERRA_M-T | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| db3e4fb8-533d-3e66-8feb-6e56bd4d6ff2 | -14.14552 | -54.06323 | 2026-09-15 12:08:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 393c3f7b-acf0-3d79-a5c1-af7f2228d2c4 | -13.29131 | -51.29818 | 2026-09-15 12:08:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 202dd1d3-d16f-3d62-8bee-7bafdb06b399 | -13.7764 | -48.81805 | 2026-09-15 12:08:00 | TERRA_M-T | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| bfc5e1a8-06d7-3e7b-8ca4-95f822e20746 | -14.36728 | -52.47465 | 2026-09-15 12:08:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 6c7da85c-a0c2-3b06-9f7a-6b40c355cebc | -15.57181 | -48.82752 | 2026-09-15 12:08:00 | TERRA_M-T | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 5604316e-50ed-3875-a455-5b5a18e9104e | -13.69315 | -51.80673 | 2026-09-15 12:08:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 9007d434-bb47-3d51-ba7b-c84bef6681ff | -13.69176 | -51.81713 | 2026-09-15 12:08:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| f711d8c1-e1fe-3ef9-91fd-fdf580f689b3 | -13.99805 | -54.0722 | 2026-09-15 12:08:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0a75d50e-1b3e-33bb-b8d1-9c06b2c19766 | -14.37532 | -52.47176 | 2026-09-15 12:08:00 | TERRA_M-T | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d9ab4655-1589-3ceb-aa22-14d0cece021c | -13.76651 | -48.80166 | 2026-09-15 12:08:00 | TERRA_M-T | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 787f5d3c-12f3-3409-82f2-7ca309bb9cbc | -18.00299 | -45.0544 | 2026-09-15 12:08:00 | TERRA_M-T | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 71839895-b61d-3dd5-8fb5-8a5a799bcdb4 | -8.638 | -44.4567 | 2026-09-15 12:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 130.7 |
| d3285a3e-946e-3eeb-bf01-6d0773e40bf1 | -9.7687 | -46.1067 | 2026-09-15 12:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 215.2 |
| 4dad9a5a-b8fe-3b88-9035-bb910164f8e1 | -14.1666 | -47.3876 | 2026-09-15 12:10:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 4233654d-f326-387e-9b13-57be5fa7295a | -9.3575 | -50.1156 | 2026-09-15 12:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 134.3 |
| d7fb3ca9-efda-30d3-aec6-d49e246a82cb | -9.3572 | -50.137 | 2026-09-15 12:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 00c8ee95-217d-3965-a900-616eed09c714 | -11.5045 | -45.771 | 2026-09-15 12:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| bfa52214-7efc-369b-9715-ee430bdfc2f6 | -10.8665 | -46.3105 | 2026-09-15 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 336.5 |
| 43690160-8ace-3e7a-a0d5-42b1949f9949 | -7.0164 | -44.6413 | 2026-09-15 12:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 172.2 |
| e7da8ae7-08d2-3006-b292-721871c50779 | -10.9875 | -48.3209 | 2026-09-15 12:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 02c70313-2756-3b54-835f-b9303ff41e06 | -7.0166 | -44.6184 | 2026-09-15 12:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 6a1f1669-515b-3963-8977-3757c998a274 | -8.4852 | -44.5885 | 2026-09-15 12:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 4baf7d28-3c81-3e70-be3e-fdc3af4b5695 | -11.5041 | -45.7939 | 2026-09-15 12:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 0382b48c-589e-352d-bd67-d394141e9cde | -10.8661 | -46.3331 | 2026-09-15 12:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 131.2 |
| e8567fe9-a6d3-3011-a92d-7c47fd357090 | -20.69628 | -49.01524 | 2026-09-15 12:10:00 | TERRA_M-T | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 41702602-8b7b-3930-a6dc-9809037f59b3 | -11.5041 | -45.7939 | 2026-09-15 12:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| d0f35997-ead2-344c-a259-a30c69e0496f | -11.5049 | -45.7481 | 2026-09-15 12:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 72.0 |
| fd17000d-0b37-3d74-b704-16c40813d17d | -13.7006 | -51.8061 | 2026-09-15 12:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 31f9c636-bee5-39ea-b589-dff3ef817e49 | -8.638 | -44.4567 | 2026-09-15 12:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 69.2 |
| b6b67cb7-fe3d-3d3e-83ad-d3890690c035 | -13.7002 | -51.8274 | 2026-09-15 12:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 71.4 |
| ce21ca6c-5b34-325c-a226-c08c3608a601 | -10.792 | -46.2071 | 2026-09-15 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 1ed61623-5631-3cf3-aed4-e6fc3b9a2dc5 | -7.0164 | -44.6413 | 2026-09-15 12:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 183.5 |
| cbf9e291-10f6-335b-8e21-aee3a91f279e | -10.7916 | -46.2298 | 2026-09-15 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 4b83007c-8e3f-3fc3-8839-d8248fd07599 | -9.7687 | -46.1067 | 2026-09-15 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 372.0 |
| 7b0b5d8f-a5eb-3889-9f85-f7b24a2ff0a1 | -14.4048 | -45.2626 | 2026-09-15 12:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 0efe11d3-7381-345f-a063-082f63bb1b22 | -10.8474 | -46.313 | 2026-09-15 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 135.9 |
| 7f8c76c6-50ab-335f-969b-8a64d007998e | -8.6191 | -44.4588 | 2026-09-15 12:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |
| d9331dc9-14fe-32d5-9a7b-81fe12e81e23 | -10.8665 | -46.3105 | 2026-09-15 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 502.0 |
| dbf0819f-d52f-3b50-9d81-58b23f0b3a5c | -9.3575 | -50.1156 | 2026-09-15 12:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 130.0 |
| f569a97d-d0d5-3bd0-9297-6ba2ed960551 | -11.5045 | -45.771 | 2026-09-15 12:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 134.1 |
| a0158948-c658-3495-b21f-9f8c51163070 | -8.8459 | -45.8713 | 2026-09-15 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 70.2 |
| f1aa07aa-af35-304b-81ea-c671cf1b7f28 | -9.4234 | -47.8588 | 2026-09-15 12:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 73358720-c3c5-31a6-97c0-08193d2fa470 | -10.8661 | -46.3331 | 2026-09-15 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 660589e4-c516-3f0e-98df-2d9c5b371b8a | -7.0166 | -44.6184 | 2026-09-15 12:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 90733716-0319-3450-8b8a-21520210b636 | -8.638 | -44.4567 | 2026-09-15 12:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 173.1 |
| 7148b154-7e64-3782-9aee-1c61d47ba387 | -13.287 | -51.2832 | 2026-09-15 12:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| b6948412-e70c-396e-b3b8-70a6d44ea46e | -11.5045 | -45.771 | 2026-09-15 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 216.1 |
| 34384170-e631-3600-b2c0-1e81d0654255 | -10.792 | -46.2071 | 2026-09-15 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| d197802b-6351-3a05-8c91-41255b965f51 | -18.1714 | -51.7466 | 2026-09-15 12:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 31a1e287-1d6f-340a-9c21-1794b28c62eb | -8.6191 | -44.4588 | 2026-09-15 12:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 233.0 |
| 38be7291-b42d-34f4-be58-aeadc2785259 | -9.3575 | -50.1156 | 2026-09-15 12:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 2a992791-610b-3cb6-b48f-165a32c9d51d | -11.5041 | -45.7939 | 2026-09-15 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 431.3 |
| 0eacfb9f-4425-378e-975f-1771530987ee | -9.7687 | -46.1067 | 2026-09-15 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 349.6 |
| 3a657371-0a5e-3e9c-a6d6-032287ea0a7c | -10.9875 | -48.3209 | 2026-09-15 12:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 2c9a7285-5eca-380a-a084-f52b71e7224b | -10.8661 | -46.3331 | 2026-09-15 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 139.8 |
| f0cea0a3-8f8d-393e-a068-6045bc8d31b2 | -10.8665 | -46.3105 | 2026-09-15 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 405.3 |
| f54466e3-067d-3c5f-b370-e802ae295069 | -7.0164 | -44.6413 | 2026-09-15 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 132.7 |
| f5ba2742-3a0d-3b56-8a9f-cd80594ba1e1 | -8.6383 | -44.4336 | 2026-09-15 12:30:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 6ba90a18-3f5f-3e18-bbe9-e04a87d2aa76 | -7.0352 | -44.6396 | 2026-09-15 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| ec84b145-10c4-30d7-8225-11700677216a | -7.0166 | -44.6184 | 2026-09-15 12:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 792e4fa7-0b17-305e-afb3-20f4adf1e68a | -10.8419 | -60.8202 | 2026-09-15 12:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 3a6108a3-ef7e-3115-9d4f-8b6a551543c7 | -10.792 | -46.2071 | 2026-09-15 12:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 648795cd-7f1a-3bc6-b0b2-7b02ac6ecfe9 | -18.1709 | -51.7685 | 2026-09-15 12:40:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 3750346e-845b-3fdb-8336-9f022646d4a1 | -11.884 | -43.8142 | 2026-09-15 12:40:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 583dfafa-89b6-3397-b25f-e80f56d8d33c | -8.6191 | -44.4588 | 2026-09-15 12:40:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 0b0d12b3-c3e9-3dd0-8f1a-c6d21d6df0a6 | -9.3575 | -50.1156 | 2026-09-15 12:40:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 8889ba2a-fedd-3ff9-be7b-453ec79c2dcf | -13.5963 | -47.9027 | 2026-09-15 12:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 58.7 |


[Clique aqui para ver as próximas entradas](README74.md)
