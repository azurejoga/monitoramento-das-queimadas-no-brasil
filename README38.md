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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44a02cca-0522-35ba-bdca-b1b3a100b221 | -3.21058 | -50.62967 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 38da9e08-b8d5-37ea-ad05-38d63e5aacff | -3.96436 | -48.18022 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 2c729afe-fc5c-3aed-b917-288ed85be618 | -2.29425 | -46.51218 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf65891c-59c1-346a-8495-dcee0b2b095a | -3.61271 | -47.52164 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8973159-460e-3767-bd59-5d3deacad76b | -3.31241 | -51.66471 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 396e2021-49e4-38ad-bc06-bbe389eabe34 | -5.37921 | -42.75822 | 2024-11-10 04:14:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 310e1098-286b-3787-b804-43856a9109e1 | -4.95973 | -42.98145 | 2024-11-10 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e205daba-88b1-3b4a-89a5-d016cca7d9e8 | -3.95696 | -48.12181 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 4b8627ef-bcc4-3fcd-8198-e5c2f8e0190e | -1.34423 | -54.62946 | 2024-11-10 04:14:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 17.4 |
| ad84b83c-050d-3763-8274-2d2a2518070e | -3.69411 | -47.63803 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 385d51cb-b0c7-3fdb-a8a5-428a8e6c9384 | -2.92656 | -48.31527 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7d59d7d-5dfd-3729-b761-af3b9953595e | -1.24151 | -51.75541 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c49bef3d-cb31-33d6-9a20-27460bb97121 | -2.51297 | -46.35741 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46f9269b-cd48-3c56-b850-0b3e9fb894a0 | -3.90668 | -40.38041 | 2024-11-10 04:14:00 | NOAA-21 | GROAÍRAS | CEARÁ | Brasil | 2304905 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4c21d2d6-2961-3305-9ff7-35ab1461bb66 | -2.45361 | -53.68922 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01e104ea-f648-3ae4-8352-bc41df947473 | -5.15326 | -44.24246 | 2024-11-10 04:14:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 326abc33-03bd-3692-837b-629b00226b34 | -2.9428 | -49.35213 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 759d6c70-e313-3cc3-b7c4-e23742161720 | -1.66673 | -53.80627 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5cce6360-5e7c-358c-991b-defcf0afaaec | -2.59408 | -48.3302 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70758c34-52b9-3e52-8388-093dea6e9777 | -2.57281 | -45.55722 | 2024-11-10 04:14:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6535fb44-5efd-3282-8a5a-f9e27a239b5e | -3.09845 | -45.95651 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4544ab73-c7be-3e20-98f7-4b434461f1da | -3.22928 | -50.44264 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eadb3a89-448d-386c-948c-af7d32815f03 | -2.73763 | -49.02359 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c6242b68-5c18-3d8f-8846-a7c9c2b239f7 | -3.77752 | -45.1859 | 2024-11-10 04:14:00 | NOAA-21 | SATUBINHA | MARANHÃO | Brasil | 2111722 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9ca65f3e-be65-346d-82df-522128613b18 | -0.64305 | -52.3665 | 2024-11-10 04:14:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d8d1c165-9512-3371-963e-daf8ce4c38f3 | -2.63574 | -51.71553 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07764395-4db5-3874-a086-371408d2eda2 | -5.31535 | -46.23421 | 2024-11-10 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 753fab80-04a7-3a5e-bd0a-c60d2dd55930 | -4.51698 | -43.98269 | 2024-11-10 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| df761bfc-fcc5-3199-81d8-373c6d9cc110 | -2.82394 | -46.6474 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 886ab00e-9830-31dc-84f0-50985cbc7879 | -4.01651 | -48.29012 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95ad96d4-5f49-3110-99b8-3872ea66d551 | -2.19324 | -49.53057 | 2024-11-10 04:14:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 095b363f-2989-360f-acee-e3c7c92c96fb | -2.20156 | -51.87393 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 43ae268f-a09a-376a-bcc3-87a548441849 | -5.41479 | -46.41251 | 2024-11-10 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 08e3d2d7-d83c-3f67-8b6b-7272ccdc18d1 | -3.19949 | -46.50529 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 38e0fbc5-2c30-340a-9a19-8a71ac8926a2 | -4.69328 | -49.62264 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ac271c9-617d-3101-b111-861241a55aa6 | -3.23443 | -45.38363 | 2024-11-10 04:14:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e48f5fc5-d8ad-3f34-8823-ebc6062e4d55 | -2.68054 | -51.82592 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7050c95-b991-3f29-bc95-216bf8b5371d | -2.73514 | -45.97934 | 2024-11-10 04:14:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 877e273d-3eb2-3042-9fce-9a4abfb4ac0e | -5.53494 | -41.68321 | 2024-11-10 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 18c82af0-909e-3fab-86be-1202ead34e76 | -5.90562 | -46.71427 | 2024-11-10 04:14:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7dedb78f-d93b-3e16-8b26-69516ba48493 | -2.30434 | -46.72353 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 953d3a77-9d37-3240-a821-e13172b64227 | -5.51681 | -43.7919 | 2024-11-10 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a1c1043-4bf9-30ff-b0de-6db576054e79 | -2.23243 | -53.7333 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 75909c10-91fa-354a-afdf-c6506daec84a | -2.59341 | -48.33426 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a304ede3-2342-3f6f-8186-20638646118d | -2.91854 | -49.50303 | 2024-11-10 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 670b7b6d-86c1-33f3-b043-f149dfba0af0 | -2.57298 | -46.53985 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e3a4f2d-71f1-3d13-b657-f12404e36be1 | -1.53748 | -52.20986 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1526d038-f952-3ea6-84e7-782e36a15330 | -2.14846 | -50.45709 | 2024-11-10 04:14:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f22fbdb-c08d-34aa-87ca-5943c759c521 | -5.41408 | -46.41686 | 2024-11-10 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4631cbf2-39f9-3cdf-8335-e6fa6c95c204 | -3.37199 | -49.92464 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73e5cd6d-1c05-31bb-9f89-c457a47db143 | -3.12453 | -50.43706 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| a7bc4163-32d8-3792-b017-afb304e818be | -2.46301 | -47.93748 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec8482ae-a8f2-33f6-8914-62fa45ab03f6 | -3.44769 | -50.74919 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c196baa8-65c3-32c0-a968-2d077fdebf62 | -2.9334 | -51.48058 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 5d448737-9e19-39f5-82be-139cb80dfec8 | -3.25048 | -49.77071 | 2024-11-10 04:14:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abcb5e8f-76c9-30f2-9b39-0d94479acabf | -3.95573 | -48.12931 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| caf7043d-d06e-33cc-b672-c6c72d7f32f6 | -3.12185 | -44.99152 | 2024-11-10 04:14:00 | NOAA-21 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 39766bbf-d3b0-3061-8eab-651f26e68e55 | -2.0854 | -46.79199 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2cf43ecb-2a6f-3f45-be4b-c0c7a4202e85 | -3.70706 | -50.15816 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c0719ae1-4a9c-3f5f-b940-55a92c862533 | -2.67244 | -46.79215 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91082ca6-0b7e-3fc3-b7a5-b83e5556bc37 | -1.98885 | -47.85993 | 2024-11-10 04:14:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90c4d4e8-6e1a-302b-922d-04067f5a3a1d | -2.30314 | -48.50067 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ca02262d-b7a2-3a03-bb63-5fa6ba96b6ea | -2.92121 | -51.67655 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fbef20b0-b29a-3eb8-b33e-0a7ba45d7f24 | -2.17356 | -48.32917 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 06540f57-b32d-3b8d-91fe-4f66303e4373 | -3.45264 | -50.18227 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 63cc07cd-60e0-38eb-9043-7aaf7beb6e13 | -2.30702 | -46.74192 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e46f537-bb75-31f7-b780-b22a955e9e03 | -5.5517 | -44.69538 | 2024-11-10 04:14:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| be3833b0-a306-3f67-a49e-9ab065830a7e | -0.04243 | -50.77009 | 2024-11-10 04:14:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4439a82d-822f-3062-9634-010f70e8e760 | -3.13524 | -50.4332 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d04e754d-109f-3695-845b-cf142131b77a | -2.09602 | -46.34271 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60f11933-3298-30a4-a7d0-c5e8ae7b437d | -2.62674 | -49.47046 | 2024-11-10 04:14:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 837a84b4-5384-382e-abae-32d97b4857b2 | -3.13499 | -45.16487 | 2024-11-10 04:14:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 8cc2cbbd-2753-3940-bd24-d0a2f402a088 | -3.97265 | -48.18159 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bb72f7d2-2108-38e1-a3b9-5085541da328 | -4.21334 | -45.45336 | 2024-11-10 04:14:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c749e7a-886f-3452-8764-ddd5eaeb6524 | -3.95746 | -48.14457 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d07ac694-a40f-36ec-8a21-8b3aa986ee02 | -0.30597 | -51.7014 | 2024-11-10 04:14:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0d5a221-6f39-30f5-a786-99aea6756137 | -4.38121 | -48.57739 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0a1c5757-81cb-34da-9e98-a422f8b3aac1 | -2.8824 | -51.65952 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49b3417a-ba8f-3215-86b3-da48e04fbe2e | -3.14374 | -45.95476 | 2024-11-10 04:14:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3df277f2-de3d-325c-9e7d-248e3e1f7b2f | -4.1155 | -48.50391 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c148f1d-1b55-3764-a2c4-a512885dbae4 | -3.71207 | -40.71258 | 2024-11-10 04:14:00 | NOAA-21 | COREAÚ | CEARÁ | Brasil | 2304004 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 53b2dabc-a63b-3e57-b928-89c04379aa05 | -2.42121 | -46.68353 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c799b6fd-92fc-34d9-b550-91b77ce53002 | -4.40584 | -49.82067 | 2024-11-10 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2656d29f-6b9d-300a-a9a8-87903f43cfb6 | -5.38144 | -42.76562 | 2024-11-10 04:14:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 97464a9e-7b35-3b77-a550-792907cd9fd8 | -3.23053 | -50.45036 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b9a38517-2802-3284-887e-0f980b11a6ac | -3.12851 | -50.44338 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 004cccf1-0ca7-34fc-9dd0-6d17b5bcfa3b | -4.06318 | -49.2809 | 2024-11-10 04:14:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 441699b8-8908-3be0-a748-7f4b2b639e03 | -2.2267 | -48.38365 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3bbc0255-99ff-359d-b944-0673a7a455e9 | -2.58927 | -48.20327 | 2024-11-10 04:14:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84ac8061-38b0-3732-a33b-ced9e2924834 | -4.09171 | -48.51642 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c4d0492f-373f-3979-bcb2-04a0f0b377cc | -3.60414 | -50.45562 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 10720444-506d-3b77-b617-bf0ad8cec2ae | -1.16459 | -51.92323 | 2024-11-10 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83f70e26-6bf9-3789-a100-e835723c1e3d | -1.2984 | -54.67393 | 2024-11-10 04:14:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| be1eb9d6-f5dc-3fa5-8ef4-4a7503fd045e | -3.06317 | -48.03081 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0082fc1d-9ea1-3643-8d22-bcbda57c6a8a | -4.06996 | -48.22501 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f1361427-43c5-307b-a457-6206bfb85caf | -3.95082 | -48.1591 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 39139983-fb49-3e5c-9795-1399f877f132 | -1.23598 | -51.75453 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f039d3f-2701-37a8-ab58-27d8121bce3f | -2.53246 | -47.38284 | 2024-11-10 04:14:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 81f9897f-e86a-35b7-afd4-50c995c55a9a | -4.41754 | -43.64298 | 2024-11-10 04:14:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58e0b01c-9f96-33ed-b709-9a312ea020f4 | -2.04252 | -51.45904 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |


[Clique aqui para ver as próximas entradas](README39.md)
