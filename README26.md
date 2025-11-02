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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47e763aa-01ef-3c48-93fa-a858599be0b0 | -3.89297 | -52.20775 | 2025-11-02 05:10:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3a947ca1-8e81-39b7-a779-dbbf7ce2feaf | -4.13506 | -51.14115 | 2025-11-02 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4963a19-193c-3dc8-ba27-a354bfdce519 | -3.5932 | -54.04402 | 2025-11-02 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b496e8cd-c721-3850-9c98-f2718cbea0b5 | -3.5557 | -54.57446 | 2025-11-02 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 1a529ef7-bb66-325d-a81f-c1da176a9a29 | -3.50571 | -54.37805 | 2025-11-02 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7e6bc4c0-b1b3-3bea-8a0a-9ce1c03d2bb0 | -3.55971 | -54.57124 | 2025-11-02 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8b282159-7308-3ab4-8852-ad79783ff409 | -11.34883 | -51.44994 | 2025-11-02 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3dcec527-4eb5-3432-8827-55c8cf677743 | -10.30482 | -53.77735 | 2025-11-02 05:10:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 06faec35-8650-3541-b672-e213dbc2d5b5 | -9.63286 | -62.06419 | 2025-11-02 05:10:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c349981e-2b45-3f20-8a78-554e70cfd803 | -4.10287 | -54.11785 | 2025-11-02 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9387996f-63e5-3cab-9ddd-5907c06a2f9c | -10.99765 | -54.00237 | 2025-11-02 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77a4ab47-af69-36f2-b370-c6f682061a44 | -10.62983 | -52.18085 | 2025-11-02 05:10:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e34bac73-37f8-3b3f-a51d-f2df6a2ff3e9 | -10.62927 | -52.18498 | 2025-11-02 05:10:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6270601f-e220-3619-a30e-75a356e6e50d | -10.73261 | -46.25715 | 2025-11-02 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7eee39a3-b280-3d58-831e-9e60f0c35a5a | -10.97497 | -54.24762 | 2025-11-02 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8e6d016f-8a0d-3ebe-a381-ebd7bb543576 | -10.97505 | -54.25011 | 2025-11-02 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 289cc1d6-9603-30b4-8469-50ef78241751 | -4.1345 | -51.14486 | 2025-11-02 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d6b466cb-404a-3dd6-9dcb-eac4ebde30e5 | -3.59182 | -54.56848 | 2025-11-02 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7787faa1-e20b-3232-855f-75eb738f7374 | -3.54478 | -54.69108 | 2025-11-02 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5768a8b7-2745-341d-a6a4-4ea58a6c3bb3 | -4.13334 | -51.15256 | 2025-11-02 05:10:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 122ecf2a-a3be-379b-98ab-e619634db304 | -8.8604 | -49.88112 | 2025-11-02 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 515c3f5c-a78b-3d3b-a7da-2182731e32a8 | -4.10667 | -51.10101 | 2025-11-02 05:10:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b3119d16-8c3d-3b54-9488-cbc054b9f6f3 | -9.06236 | -48.83378 | 2025-11-02 05:10:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f950fdf-1d47-3240-9bb9-82443f840051 | -10.73196 | -46.26245 | 2025-11-02 05:10:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02fd594c-2f01-3d63-ac65-c51f9934c1c5 | -3.57172 | -54.58465 | 2025-11-02 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea3f444d-22dd-3322-b90d-eae8063e6bbf | -11.34792 | -51.45684 | 2025-11-02 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d962eed-2d22-3063-8400-90b46278063c | -3.23616 | -58.88797 | 2025-11-02 05:10:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 119860c7-c2b4-37d7-a720-f29aae2041de | -3.50225 | -54.37753 | 2025-11-02 05:10:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7bdda01-e067-303b-96a8-c9cd44c39454 | -6.54029 | -55.04681 | 2025-11-02 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 558af0b2-7850-33c5-9f23-959f24903536 | -2.69021 | -59.81204 | 2025-11-02 05:10:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aae170f6-14e1-37dd-9378-887e06fa4361 | -3.5963 | -53.53823 | 2025-11-02 05:10:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8aa8570d-5492-3583-a9ea-e297a1fd8857 | -4.50682 | -54.92705 | 2025-11-02 05:10:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c3f66f5-e485-399e-8efe-865f24dccef1 | -9.78051 | -57.41555 | 2025-11-02 05:10:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c7ecfa87-d7bf-3589-955c-43223d0b730a | -10.58777 | -57.8132 | 2025-11-02 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 94871a29-413b-384f-a57d-ade798af4cdd | -11.86469 | -63.36529 | 2025-11-02 05:12:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7829f221-3936-37a5-b6a0-18fb98eef1a7 | -13.51307 | -57.24009 | 2025-11-02 05:12:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f67e084e-931f-347f-85b4-b556b9b5c76a | -15.87891 | -54.39663 | 2025-11-02 05:12:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9dc1ee54-b1a9-361f-8acc-2c5dc7c30477 | -10.7835 | -56.81475 | 2025-11-02 05:12:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 53cadc8c-0828-3802-8ba0-b07abff283d7 | -15.62528 | -58.22556 | 2025-11-02 05:12:00 | NOAA-20 | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 64525764-973b-38f7-beda-d3e7f234db3e | -13.49136 | -61.44681 | 2025-11-02 05:12:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad8a499a-27cc-3d25-b621-fb9abe3e9f74 | -13.72416 | -51.4585 | 2025-11-02 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ea7bf4aa-6414-3ed6-9a60-87db41d7c95a | -12.36857 | -63.88121 | 2025-11-02 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38d4a08d-9619-3f0f-b26e-a3346092e9b8 | -12.23464 | -60.32397 | 2025-11-02 05:12:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 80b17d78-5ca5-3421-80a3-015937164f14 | -12.42253 | -54.49585 | 2025-11-02 05:12:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fbb5eee6-bcc5-399d-a49b-7a41f3608b39 | -13.49069 | -61.45078 | 2025-11-02 05:12:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9576281c-7ea0-331b-b3e4-05ef7ec12916 | -13.11297 | -59.18383 | 2025-11-02 05:12:00 | NOAA-20 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b77d9bb7-49fc-303c-8aca-6dfa44865e9e | -12.37664 | -63.88271 | 2025-11-02 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7d152bf9-cd7e-383a-98f4-71054f488006 | -12.32248 | -57.72626 | 2025-11-02 05:12:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 568683bc-510b-3407-891b-bf327b1dbce5 | -15.62807 | -58.22977 | 2025-11-02 05:12:00 | NOAA-20 | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |
| f2a416f4-ef85-3b06-b611-9efdf65c511e | -16.28028 | -56.599 | 2025-11-02 05:12:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 484c311a-bc8e-3197-a29c-13cfd90bed5b | -11.97823 | -58.06369 | 2025-11-02 05:12:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e08988e4-ade7-33d0-b6da-15e22f52e1f0 | -12.4644 | -54.32637 | 2025-11-02 05:12:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b269c0c-3707-3c5f-8806-f6cb754f80fb | -14.66059 | -46.61431 | 2025-11-02 05:12:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0c309b39-3230-35ff-ab85-88a99adfa4c2 | -12.87615 | -50.89584 | 2025-11-02 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1d3a1a31-07f9-3d6c-bb70-d4a5e49ffec2 | -12.01725 | -64.01777 | 2025-11-02 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33858e98-eaec-30e5-a87c-53e6b8d4eaa6 | -9.4094 | -65.61069 | 2025-11-02 05:12:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a95d6f0b-82ad-3219-afc0-b488469f6735 | -12.36922 | -63.87758 | 2025-11-02 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b940446-3b5f-3516-96f5-ab841c2cbdb9 | -15.24087 | -51.75349 | 2025-11-02 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7b6ab26b-f0ad-3a4c-9ae8-b85ddd8dbefd | -11.979 | -63.67179 | 2025-11-02 05:12:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da854ed3-c010-3d99-add7-b21d8750a258 | -15.24152 | -51.74828 | 2025-11-02 05:12:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6253eb2f-2f37-33f2-bc01-0d29cd02631b | -12.17354 | -53.62404 | 2025-11-02 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9284d73d-271f-3548-833a-d06d22fc2c49 | -13.49838 | -56.56583 | 2025-11-02 05:12:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b7893a1-25ad-367d-919a-72f3d07ef32d | -15.06441 | -52.79289 | 2025-11-02 05:12:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 708411f2-54eb-3044-a69a-a539764907ea | -12.3726 | -63.88195 | 2025-11-02 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| abad1c07-1a78-3c82-a006-daffaed9ac8d | -12.311 | -64.04071 | 2025-11-02 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 096088e0-6e3c-3fe4-a980-57058a7ddbed | -11.88489 | -63.45092 | 2025-11-02 05:12:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e95e0c35-f040-39b5-bd0e-66c2af4544c1 | -12.23255 | -54.39481 | 2025-11-02 05:12:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b12dd462-93a9-32be-a963-bad5f6b6accb | -13.98214 | -51.50247 | 2025-11-02 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2d2e23a5-9ea1-3aee-a169-2c4a0b580c38 | -13.77442 | -48.87432 | 2025-11-02 05:12:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6603112-16d2-3f4d-abf4-0296f20a83db | -12.4354 | -63.14233 | 2025-11-02 05:12:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8325a219-6558-3328-bd66-2aaa378db421 | -12.32303 | -57.7227 | 2025-11-02 05:12:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fed44d5f-a46c-3892-b51a-7c47a4f20695 | -14.65457 | -46.60838 | 2025-11-02 05:12:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9cd3fd4-8fdc-39ad-87ff-bdbbf50ba019 | -12.24377 | -54.38883 | 2025-11-02 05:12:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de88193b-3f9c-392c-b76f-d3c75360a520 | -10.78631 | -56.81893 | 2025-11-02 05:12:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90cec8ba-3cb0-35e6-9a71-297621d1f3c0 | -13.98688 | -51.50309 | 2025-11-02 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d8f22e6d-86a3-3bd7-8d3a-08156c69df3e | -15.61016 | -56.03643 | 2025-11-02 05:12:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3bda7958-ea33-38ce-9386-e1d336db4085 | -12.86712 | -50.88908 | 2025-11-02 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 2652fb61-3921-3433-8df7-46dad2342f5c | -13.49418 | -61.45138 | 2025-11-02 05:12:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b26edc9d-c2b9-3a80-9513-59f64be08156 | -13.49351 | -61.45536 | 2025-11-02 05:12:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 406bd961-f8ea-39dd-99a6-f237eac212ff | -16.17101 | -59.39545 | 2025-11-02 05:12:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dcd5b935-5d22-3463-80c3-17fe2d8d1efd | -12.37599 | -63.88633 | 2025-11-02 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a968a31d-a4bc-3c04-97b7-bd31ed57d212 | -12.23525 | -60.32028 | 2025-11-02 05:12:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4f704952-c6fb-31b9-9525-c452bafdebfa | -13.49202 | -61.44283 | 2025-11-02 05:12:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 048ca091-4f31-35ad-9053-8924a0125ef9 | -15.62193 | -58.22502 | 2025-11-02 05:12:00 | NOAA-20 | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 373f5875-0155-3a34-a9f1-088faa95b5f5 | -15.30314 | -59.23327 | 2025-11-02 05:12:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 80763f47-3200-36a3-8a59-1eef54aa885a | -12.15072 | -61.43526 | 2025-11-02 05:12:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 832c02b1-528a-3fb9-9831-673ad128aadc | -11.88193 | -63.45404 | 2025-11-02 05:12:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6a04e0af-f30b-3206-9761-841ca626ca4b | -12.08252 | -55.36974 | 2025-11-02 05:12:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e7a976b-fb36-3cb1-ae34-7c37da5fd57d | -13.9719 | -52.45298 | 2025-11-02 05:12:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7b2255e-34e6-3c0d-b0cc-2a34108d2f2d | -13.98623 | -51.50827 | 2025-11-02 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d456e8a2-801a-33e6-9435-dd1413b7be2b | -12.37729 | -63.87908 | 2025-11-02 05:12:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7f1f61f9-9c7f-3fb2-bde8-d5e142e17aaf | -11.36759 | -54.31297 | 2025-11-02 05:12:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55f34104-1c6b-3f49-aee7-c5f3f8e68540 | -12.24088 | -54.39118 | 2025-11-02 05:12:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3318152-174c-30cd-9f50-19d415541ae3 | -12.17305 | -53.62757 | 2025-11-02 05:12:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6e7b75d-f9d5-3d51-b295-77924deed942 | -13.49617 | -61.43948 | 2025-11-02 05:12:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c73bb02-9b2f-3bdd-a47a-d298434e57dc | -13.72501 | -51.46031 | 2025-11-02 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e792a0b4-700f-34e3-b620-d228f2468b84 | -12.87198 | -50.88972 | 2025-11-02 05:12:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6884e248-b18b-3bc7-9071-1ad3b740f1a3 | -14.59251 | -56.00103 | 2025-11-02 05:12:00 | NOAA-20 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 38f3c0f7-a1ff-346d-9c74-236fdeffd799 | -12.24471 | -54.39172 | 2025-11-02 05:12:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77fa9ea3-8564-3013-9e6e-422352ed5ac3 | -15.62472 | -58.22923 | 2025-11-02 05:12:00 | NOAA-20 | SÃO JOSÉ DOS QUATRO MARCOS | MATO GROSSO | Brasil | 5107107 | 51 | 33 | nan | nan | nan | Amazônia | 18.3 |


[Clique aqui para ver as próximas entradas](README27.md)
