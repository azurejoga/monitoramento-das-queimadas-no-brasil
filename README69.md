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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f9730c59-9517-3afe-bedc-16efaba38f6a | -8.89284 | -71.3434 | 2026-09-29 05:55:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c653d614-a56b-3907-a6f4-cbbcc2b47db0 | -9.13435 | -67.93452 | 2026-09-29 05:55:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e352d7a4-8c76-355d-8309-761a608b9ba2 | -9.92838 | -60.7169 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| acfd6888-f888-355e-aefc-863a739b01ab | -10.38919 | -61.2711 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 89540814-655f-34b7-97eb-20729b6edae9 | -7.26655 | -72.69355 | 2026-09-29 05:55:00 | NOAA-21 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87480710-0138-3b4c-b124-41c2316f9952 | -8.82994 | -71.80003 | 2026-09-29 05:55:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0878aa8d-2217-39bc-b8cd-b429103718e4 | -10.39455 | -61.26836 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d6d6a601-ea30-3cfe-aa9b-659b8f9a392b | -10.38322 | -61.23824 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 244231d6-f3d3-3de0-972c-1fc836b9fbe3 | -10.40316 | -61.24104 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7c2fdae-0319-3e25-a104-1b4c0473d38e | -10.40007 | -61.2657 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b91957eb-7d91-3e73-8007-3abc927843fd | -10.38084 | -61.25624 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 983f0762-5a1b-390e-b99d-ff569711783f | -10.38454 | -61.26691 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b480fdc-90d7-3a34-bbd2-50d6a27cf16a | -9.35026 | -68.28287 | 2026-09-29 05:55:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fa20e939-01c3-3fc0-a327-797eb2e6e897 | -10.39329 | -61.23943 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| cc0a1cdd-2fee-3070-8429-840dd54eb5df | -8.91142 | -64.15026 | 2026-09-29 05:55:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 701aab94-abce-3675-9f67-f6d15230ae1f | -7.85953 | -70.88651 | 2026-09-29 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bacf6e1e-d891-316c-b4c8-64fac2b7d4e7 | -10.39792 | -61.24311 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f2903dc3-e4a7-3ce2-bb17-0fa07db810fa | -6.95553 | -71.49794 | 2026-09-29 05:55:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bac03151-3f55-3587-9a26-543c137c9aa6 | -7.18174 | -69.8866 | 2026-09-29 05:55:00 | NOAA-21 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efdf30bd-f837-354a-b9d8-4e512c5b23e7 | -8.02381 | -70.82912 | 2026-09-29 05:55:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d364e6ce-0657-3ad5-ab57-caca2dd6b63a | -10.3924 | -61.2453 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 940ee920-9245-31f0-a15c-79756516676b | -10.38908 | -61.27111 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71992dc0-35b9-3b9a-8684-c6d0995c0b8e | -10.39369 | -61.23643 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 008b9367-dbd2-31b3-9292-9d1555480234 | -9.93064 | -60.72717 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| ac9007cc-440f-3de3-bece-d1cebacaab48 | -10.3925 | -61.24537 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 82.3 |
| a705b4a0-7a39-3604-926e-985524a707ee | -9.16443 | -61.40984 | 2026-09-29 05:55:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| aaf7f58e-b71c-3686-a073-6d2f6a2baa3a | -7.18118 | -69.89013 | 2026-09-29 05:55:00 | NOAA-21 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a069e7c-445d-32c5-a0f8-dd2bcc4d62be | -10.39084 | -61.25781 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 5054bbd3-137a-3b46-8ef1-e2fe9d7517db | -9.93236 | -60.72709 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 08b6a318-a987-3c60-b7fd-6ff1306889e1 | -10.39409 | -61.2334 | 2026-09-29 05:55:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 191b1575-748a-318d-901a-2e85fa13d7c2 | -12.84919 | -62.16994 | 2026-09-29 05:57:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41dee9de-4b45-33ea-aadf-0e7b3d87ec69 | -20.70243 | -57.96162 | 2026-09-29 05:59:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 53d4e22f-5a91-3fbc-9277-de39ad84662d | -20.69546 | -57.96098 | 2026-09-29 05:59:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 2f18c9f5-9974-3095-bf33-003119b27711 | -10.3895 | -61.231 | 2026-09-29 06:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 374b4c8a-ffe5-349b-bda9-65f781d5a067 | -10.3894 | -61.2502 | 2026-09-29 06:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 224.7 |
| 9cd7e7e0-c42a-3e00-9451-f75d87794bfd | -10.3892 | -61.2695 | 2026-09-29 06:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| ba4f8d42-2b44-3154-8e80-5d0abf1d59f9 | -10.4081 | -61.2492 | 2026-09-29 06:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 60128367-dff4-3fdd-94ea-b7e78f1d7b09 | -10.3894 | -61.2502 | 2026-09-29 06:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 186.6 |
| 333c2d19-770c-32be-b0a5-b62fc6fc7979 | -10.4081 | -61.2492 | 2026-09-29 06:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| ad1ed281-2236-324d-a863-ec6dc5a5efaf | -10.3892 | -61.2695 | 2026-09-29 06:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 1068769d-388a-3d17-83fd-162d0e6b5f8d | -10.3895 | -61.231 | 2026-09-29 06:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 58.2 |
| fca46862-167e-38ea-b811-de50fe66d534 | -10.3707 | -61.2513 | 2026-09-29 06:30:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 387d23aa-1f1c-3f08-877e-376b54977629 | -8.90223 | -64.13812 | 2026-09-29 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48268264-469b-3a59-8ec0-ab9e7bbde66d | -6.93201 | -71.77954 | 2026-09-29 06:31:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 306793eb-c355-39a7-9913-e1592d7998ce | -7.79044 | -71.98334 | 2026-09-29 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0710246-5d8c-36b0-a20e-c34ae74f85cf | -7.38119 | -72.47585 | 2026-09-29 06:31:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94790a5d-4900-3252-8bd6-57cbf9634d75 | -8.90714 | -64.14828 | 2026-09-29 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 74058686-2af8-3366-b434-8e8abf9a8cbe | -6.9757 | -71.7605 | 2026-09-29 06:31:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0192560-d8bb-3ad5-8820-7e9501361154 | -7.79593 | -73.00661 | 2026-09-29 06:31:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9049973e-9859-328d-ac0d-665433a5361c | -9.16475 | -61.40449 | 2026-09-29 06:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 68c42c20-608b-3914-8a68-3880271e85e4 | -7.18274 | -69.89063 | 2026-09-29 06:31:00 | NPP-375D | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| de00394e-5d88-358c-9932-580c73483a5a | -7.89144 | -70.90527 | 2026-09-29 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b10a70f6-02d9-3faa-801c-d016073a9916 | -8.91328 | -64.14908 | 2026-09-29 06:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bdd90c28-a53a-36c4-abbb-c5114b0254fd | -7.7975 | -73.00601 | 2026-09-29 06:31:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2f7e917c-7ad1-3dab-9451-fe4a5af39fc4 | -8.03455 | -71.25641 | 2026-09-29 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98a83f8d-125d-336f-9e10-ee07b388fe7e | -6.97994 | -71.68379 | 2026-09-29 06:31:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92a09a4c-eaca-3d7d-9858-a2fe08c108bd | -7.89235 | -70.90725 | 2026-09-29 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19ea308a-0575-3005-851f-7e1f5b515679 | -7.18614 | -69.89144 | 2026-09-29 06:31:00 | NPP-375D | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99b0d384-eb35-3343-89fb-756c58b86948 | -9.17317 | -61.40298 | 2026-09-29 06:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a45fe809-312b-3e18-9550-a49232c05486 | -9.16591 | -61.40221 | 2026-09-29 06:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0ad0c360-3c8d-3b68-ae33-f007d81e8a5d | -9.16502 | -61.40983 | 2026-09-29 06:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 340b2c75-0b6f-3568-b83e-d210d717689e | -7.37827 | -72.47136 | 2026-09-29 06:31:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eef87575-36c4-36c1-92ff-34bf0c100968 | -7.26465 | -72.69368 | 2026-09-29 06:31:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 625f6346-978d-3d48-90d5-efe0b485a361 | -7.18328 | -69.88705 | 2026-09-29 06:31:00 | NPP-375D | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8d21736-e528-3126-ae58-a14d72209449 | -8.90162 | -64.1428 | 2026-09-29 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee5a7983-3810-3cc9-bb5c-418c65a48044 | -7.78981 | -71.98751 | 2026-09-29 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 592f494f-7d3d-3e60-95d4-f5d4202d6c70 | -7.38179 | -72.4719 | 2026-09-29 06:31:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9394a68b-fcf7-3c48-83fe-859b17fcd1c9 | -8.03386 | -71.26098 | 2026-09-29 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88be3546-6a2b-34a4-9a4d-2d158825bedf | -9.17202 | -61.40515 | 2026-09-29 06:31:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 18cdf80e-562e-36f5-b7bb-72b18b6347d8 | -8.91267 | -64.15376 | 2026-09-29 06:31:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5db9d144-2203-348b-a5a1-d08e52af0912 | -7.85893 | -70.88582 | 2026-09-29 06:31:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47464778-c0a7-3ab0-a5de-41a97c4b89be | -6.97634 | -71.75632 | 2026-09-29 06:31:00 | NPP-375D | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1755837-62ec-31d6-bdbf-31e682b02281 | -8.90775 | -64.14361 | 2026-09-29 06:31:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b40e5528-a168-3bee-859f-8951f9afc431 | -7.7994 | -73.00715 | 2026-09-29 06:31:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9f85192a-ed59-3bc5-ac37-1de6e1e656c0 | -7.24296 | -72.4596 | 2026-09-29 06:31:00 | NPP-375D | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aee6b9ad-819a-3afc-b64b-a0db9eb36e9c | -8.76449 | -69.34657 | 2026-09-29 06:33:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 561fb2e2-7789-3490-8ed2-6b0a43c005bd | -8.76617 | -69.34502 | 2026-09-29 06:33:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f0398e4-9317-32ae-a978-198eb4694b42 | -9.19693 | -67.74342 | 2026-09-29 06:33:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aef64854-f967-3a4e-bf56-b990ddea68f6 | -8.75781 | -70.8232 | 2026-09-29 06:33:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ebaa7b1-f7d4-33fb-91bd-564228bc7785 | -9.12599 | -67.84505 | 2026-09-29 06:33:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6e705cdd-e3b1-38d9-ae11-c4c448c74e01 | -8.76879 | -69.34721 | 2026-09-29 06:33:00 | NPP-375D | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 711db69d-f1d2-354e-ac93-c5143f20bbb7 | -9.12118 | -67.84437 | 2026-09-29 06:33:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d4812bf1-912f-3830-9f08-d4d9ed9541ae | -8.84568 | -70.62734 | 2026-09-29 06:33:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d49655f3-12fb-316a-ac72-051c3779062b | -9.13855 | -67.9313 | 2026-09-29 06:33:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 677e63fb-8b6e-3126-83d4-cd9758120bb5 | -9.13784 | -67.93644 | 2026-09-29 06:33:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b96ea0eb-45db-393d-b9c0-dcbbcaee19d2 | -10.3894 | -61.2502 | 2026-09-29 06:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 129.1 |
| 40b1b1c6-8fb7-3ccb-96a6-6aa6b615caf4 | -9.177 | -61.4073 | 2026-09-29 06:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| dbb4c7de-c6c8-348b-a650-200ae853c34b | -10.4081 | -61.2492 | 2026-09-29 06:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 7a8d64c7-b26d-39a0-b8bc-38a91ba2d029 | -10.3894 | -61.2502 | 2026-09-29 06:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 326d0444-e587-32a0-930c-57fab2f6c7ac | -7.18445 | -69.89388 | 2026-09-29 06:52:00 | NOAA-20 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f5c4dc2-f43e-3c73-8d23-3ac30f624123 | -8.03061 | -71.25998 | 2026-09-29 06:52:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3b21d2e7-69d2-38a0-86e8-2ad285a02ad5 | -7.79076 | -71.98923 | 2026-09-29 06:52:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4ee5699b-3434-3799-8f6a-c6cd92de8531 | -7.18214 | -69.89022 | 2026-09-29 06:52:00 | NOAA-20 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83ff728b-0b6e-3953-aa91-a1460424ef5f | -7.18514 | -69.88885 | 2026-09-29 06:52:00 | NOAA-20 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b591fd29-dc28-35d1-aa78-ff31336399f0 | -7.79125 | -71.98559 | 2026-09-29 06:52:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1b290647-0cef-3730-b681-28316e6228c9 | -9.177 | -61.4073 | 2026-09-29 07:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| f35b01bb-e915-378b-b0f1-1862d5721ae1 | -3.70658 | -54.22122 | 2026-09-29 07:09:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 56226bb3-3c42-30b3-bb24-82851aff1dbf | -6.28664 | -43.66319 | 2026-09-29 07:09:00 | AQUA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 1d835914-f521-32f6-bd59-5b835065a6b3 | -3.21997 | -54.31347 | 2026-09-29 07:09:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d93a52ca-00a7-3cd6-9411-26f7f8c95dc9 | -4.0508 | -54.92535 | 2026-09-29 07:09:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |


[Clique aqui para ver as próximas entradas](README70.md)
