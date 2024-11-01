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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29e9c6ca-0291-3c87-b335-660ef5a07069 | -1.12443 | -48.37329 | 2024-11-01 04:29:00 | NOAA-20 | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 78edb663-867b-3a2a-ba88-a28d8d9fe191 | -1.1012 | -47.44938 | 2024-11-01 04:29:00 | NOAA-20 | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| eee33899-c4c8-3d17-a8db-e700edfc603e | -1.05474 | -48.00632 | 2024-11-01 04:29:00 | NOAA-20 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 44ed1298-71e7-33c6-9721-953ac6e415a8 | -1.04064 | -47.79044 | 2024-11-01 04:29:00 | NOAA-20 | TERRA ALTA | PARÁ | Brasil | 1507961 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 186c681f-426e-32b5-a766-b7ba64acead6 | -1.03639 | -47.34346 | 2024-11-01 04:29:00 | NOAA-20 | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 06ff8c85-0b21-3e62-ba48-cb430b8ca721 | -0.85444 | -47.63546 | 2024-11-01 04:29:00 | NOAA-20 | MAGALHÃES BARATA | PARÁ | Brasil | 1504109 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0ae60b1-40d2-324b-8444-24a1ca07a67f | -2.35778 | -48.68661 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5c157e26-8dd4-3ef0-9483-b16ab56b8ebf | -2.35554 | -48.67879 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6a84deb-06c2-3a76-9f3b-7386a1079455 | -2.35496 | -48.68243 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29fae619-8a1f-3516-8500-27fde09efca5 | -2.35214 | -48.67826 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4dff6bc1-7fa5-35e4-9fdc-ce894b1c102b | -2.35157 | -48.6819 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30bf336e-3fe5-3e1b-9665-2f229af32f3a | -2.34875 | -48.67772 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 65acc963-dc37-3ec3-8fbf-f6980cb8a192 | -2.34818 | -48.68136 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b83c5ba9-de78-308b-b92e-8c4c6c06eb33 | -2.34196 | -48.67666 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 107868cd-1a5b-3e6d-80c5-8669827d475b | -2.33367 | -48.59722 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 102dadb3-0f23-30aa-936b-4b2dcd47f23f | -2.32396 | -48.83514 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| a06e89d3-8880-3cb6-aad7-ddd2c7a1aafd | -2.23834 | -48.534 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6247b1ba-a1f7-364a-83f1-8dc8cec1cde5 | -2.22768 | -48.51383 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80cdc387-afee-3928-b928-5a1979fba6db | -3.50714 | -48.22588 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dd43050a-86a0-335b-a375-239956ce62a8 | -3.5038 | -48.22536 | 2024-11-01 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9882e0b6-7d81-3ed1-8430-21237e4d7c8d | -3.1711 | -48.80142 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec8515ae-d216-33cc-aeb5-8a833c0a57f7 | -3.1475 | -48.5687 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6afe896a-503f-39df-96da-819ade00e98b | -3.11913 | -48.80071 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cba5bd3d-cfaa-31ce-b679-8f6b69d1e7ff | -3.11315 | -48.65527 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4068b5d-6e64-3593-9ec8-f81ea58f4dde | -3.11034 | -48.65113 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| efc10b79-f1c0-3efb-af47-411f9a43baea | -3.10977 | -48.65473 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb3e6c46-f2f2-392f-810c-f36b6be39a8d | -2.88855 | -48.28757 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 619d7701-e7c5-3f85-9a46-ac68e2bd5fb3 | -2.88521 | -48.28705 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82508345-63a7-31d8-a021-aa4c5f57b017 | -2.88465 | -48.29057 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 544e0b2e-2cee-3ad2-a7bc-0ba530380b4a | -2.8813 | -48.29005 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c230624-e07f-357c-9b6a-80585cae0ae8 | -2.87049 | -48.6616 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cc307ae6-5609-3ce0-9727-9334b2306f29 | -2.86711 | -48.66106 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 12a0863c-157e-3123-a67d-690bda835b9e | -2.86373 | -48.66053 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ce99ee4f-21a8-3cc5-b525-674d83e139e5 | -2.86035 | -48.66001 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c57fa81b-4f5c-31af-ad15-71371a0f4a8f | -2.85978 | -48.66362 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 25c6f9b7-d5d5-37ef-831e-d533fec7920a | -2.85697 | -48.65948 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aaf4ee78-3c6f-31e9-9b49-69481ac3a96d | -2.83212 | -48.43527 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59feb3c2-3d09-33a0-a360-4655a3348108 | -2.83156 | -48.43883 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 986c1076-9448-3577-bd42-696daa2bf440 | -2.83102 | -48.35493 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 346e19dc-515c-3470-b94f-f20121ec0c41 | -2.83046 | -48.35848 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d0c16554-a2cb-326f-b9ac-cdd5afabe0c9 | -2.82876 | -48.43473 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 396fbfdf-4c2b-3c27-abfb-9f8bd43cada0 | -2.8282 | -48.4383 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 316ee123-ce13-378b-be90-9dba0db031d4 | -2.82764 | -48.44188 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee7864a6-b964-3870-8300-65a4e0979d61 | -2.8181 | -48.45866 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bc4bee8-6ee3-3d53-b17f-03398a28e4ad | -2.77458 | -48.64684 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3c048e5a-b8e8-3b29-996c-d66debe84346 | -2.77401 | -48.65045 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 247a480a-3c35-31d4-b039-b2b18ae47081 | -2.7712 | -48.6463 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1797bbbc-7fe1-3577-bbfe-5f74c5f8fd06 | -2.77063 | -48.64991 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 54d4f38f-3187-39c8-8cd1-8cb343d4de91 | -2.76991 | -48.7203 | 2024-11-01 04:29:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 312e1b0f-8198-34df-b3f8-0e112090b481 | -2.52661 | -47.37558 | 2024-11-01 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f8c71bf-69e0-3286-a907-25868f6a7b7e | -2.5246 | -47.45284 | 2024-11-01 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0aa991b7-e08d-3319-b5dd-6d6959be0284 | -2.51745 | -47.45525 | 2024-11-01 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e00702e1-d2bb-3aef-9dc9-93918ca00afb | -2.5169 | -47.45869 | 2024-11-01 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 80ea57d2-3544-32c6-b710-b9b8a676bda2 | -2.51414 | -47.45473 | 2024-11-01 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1441cc0a-8bc0-341a-8b45-5a17778f06a2 | -2.5136 | -47.45818 | 2024-11-01 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 000072e4-5b2b-3200-8a10-4d5883567e3e | -2.51083 | -47.45422 | 2024-11-01 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4d48c3bf-06b5-3524-9de0-531a1d9f8c9b | -2.47919 | -47.93581 | 2024-11-01 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1cfb91d-4fc4-393b-af05-6ead42216b50 | -2.47587 | -47.93528 | 2024-11-01 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c3b15ff-c0fb-34b4-ab05-351d25619ac1 | -2.41422 | -47.80778 | 2024-11-01 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 18037f28-3ac1-3abd-bf83-e458255cab5c | -2.39982 | -47.72684 | 2024-11-01 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b021374-b014-3bee-8b57-179c0731ec59 | -2.39704 | -47.72285 | 2024-11-01 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3d74dcab-3593-3941-9e75-55160c2af724 | -2.3965 | -47.72632 | 2024-11-01 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5aca5ed3-56f5-3560-bea7-24b6eb10811b | -2.39372 | -47.72233 | 2024-11-01 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 93037420-fbc5-31ec-8cb4-a7a3585c57ee | -2.39318 | -47.7258 | 2024-11-01 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 10cb6322-7036-39d1-903d-9aad46576e21 | -2.3802 | -47.5925 | 2024-11-01 04:29:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9faae2ae-5ac1-3c58-a82c-5612f6284488 | -2.20763 | -48.1929 | 2024-11-01 04:29:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c9930f48-1b41-37ce-82de-901c203e2773 | -2.20446 | -48.7261 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcdc679f-64ac-3ccb-8968-959259d27d29 | -2.19982 | -48.35212 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3645c3a3-bfdc-30f0-bf9e-70255d289e29 | -2.19926 | -48.3557 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 277245ad-1d0b-35e5-be27-40d1e649599f | -2.18534 | -48.82472 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eed1c3de-635b-3753-aa24-3c2e7cd819a4 | -2.17326 | -48.72495 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 60f94e35-c7a8-3bbd-9195-2f33ff5fea05 | -2.16928 | -48.72808 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c3c7ee99-05ca-33fa-ae4c-ce9169c29b26 | -2.16518 | -48.75374 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2aa1667-9430-380a-a827-7ea1a5ba92b6 | -2.16178 | -48.7532 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8bae32e-f70c-3744-8a8a-ccc3007375c6 | -2.14509 | -48.79198 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1ec7c38b-6ccb-300e-93fc-82fbd8449e28 | -2.44248 | -48.86094 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb2fec4c-b98b-3e55-863d-fd9c9eae3878 | -2.4356 | -48.8825 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fcff2a18-76db-33d5-a2a6-24ab58a570cb | -2.43218 | -48.88196 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d96d2c81-a6c6-3bbb-8bd0-2c6b125fff4b | -2.4316 | -48.88565 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b31fadd7-4dc1-314a-a0c6-3c29bf340929 | -2.41759 | -48.81934 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6bddd05e-76fd-34b0-9480-faa1d60bc72b | -2.41701 | -48.82301 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81382b46-6ecc-391f-821b-e3554b001c45 | -2.40496 | -48.85503 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90392e5f-77d1-3b28-a81e-5b2789a3c789 | -2.40154 | -48.8545 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0d9b1e2a-b5a1-3cfb-934c-9dca74ffb9df | -2.36514 | -48.68404 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 48eb4bc6-bf51-3442-976b-42b3278ceec9 | -2.36457 | -48.68768 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8aaa56b-45b0-38fe-8deb-fe894eb36fa0 | -2.36175 | -48.6835 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5429f0b-e505-326a-92ac-f1c6334714e3 | -2.35836 | -48.68296 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9142b086-d071-3d4f-b164-566c2c1bcaf1 | -2.35439 | -48.68607 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb94e189-05c2-38a8-8374-92737e4b1683 | -2.34932 | -48.67408 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e03ec26-ad56-37b5-ab2c-d90f44c3cc25 | -2.3476 | -48.68501 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9bfda8d4-b6d1-3f3d-8477-bc943c2efcb5 | -2.34726 | -48.84259 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5208ab2f-f8a0-34e4-8889-97292ef505aa | -2.34593 | -48.67355 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2360f9b4-a751-37b0-aed0-47c1e0baa1c2 | -2.34536 | -48.67719 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab199cb7-ef1b-32e6-83a6-05471e8e84e8 | -2.34478 | -48.68083 | 2024-11-01 04:29:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3b33779-3839-37e7-912a-b2762e7958d1 | -2.32737 | -48.83569 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 102bdad5-3e58-31dd-8961-a68fafbc0b82 | -2.32338 | -48.83883 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 0fdf58e6-13db-38af-9c08-6623a660a90a | -2.20164 | -48.72192 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1aab47e4-4a3e-38b1-92b5-a0f69f8389bf | -2.18876 | -48.82526 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb8bf3d2-c610-39af-91b3-d4ce5709f71e | -2.17608 | -48.72915 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| a1af129b-0937-396b-91a4-3e1d4cb26e8d | -2.1755 | -48.7328 | 2024-11-01 04:29:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |


[Clique aqui para ver as próximas entradas](README33.md)
