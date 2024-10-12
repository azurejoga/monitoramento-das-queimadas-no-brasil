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

## Dados Diários - Página 131

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bd4016a4-b708-39e3-becc-9b318559fc95 | -11.23406 | -60.56634 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e655ebb5-9b25-3f26-9ebb-d988b84c5e7f | -11.23279 | -60.48543 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 94f09625-0a97-3022-b591-65b8ab29630f | -11.23168 | -60.49261 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 77d1d16a-286c-3879-9708-d5824671ad28 | -11.22943 | -60.48489 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8511fd19-6475-38d4-9731-6ee6084a586e | -11.22833 | -60.49205 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7073c702-9586-3604-842a-1849c1fc00a6 | -11.22778 | -60.49564 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| af9d248f-f68f-3362-8490-a2aee243cb3e | -11.22662 | -60.4808 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4c289dcd-32d2-3be5-8484-5d3e5a8f2d54 | -11.22607 | -60.48439 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 659cf065-358e-3b7e-9414-867ae969c8d0 | -11.22442 | -60.49511 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fddb8858-e272-348f-a036-0d950ccbc791 | -11.22405 | -60.58672 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4db4ff0-9f21-3b0a-b0e9-3132ddaa871c | -11.22387 | -60.49869 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 967d805c-b42c-3b49-92b3-951a817f188b | -11.22176 | -60.55705 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d27b4fc9-cc6d-3020-ab2a-a8493783a7d2 | -11.22065 | -60.56424 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bbe999ec-4e91-3b43-9fce-3b14a6983a62 | -11.22052 | -60.49815 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e827c2c-2f67-3b09-beb5-23204fd8893e | -11.21785 | -60.56012 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 04d54f5b-15f5-3565-bdde-edfc5872cf1f | -11.2173 | -60.5637 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92d15fc2-c39c-35ca-b31a-16abf3db3ebc | -11.2157 | -60.59636 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b489cd86-d2ea-38ce-aef4-c313b42058bd | -11.2118 | -60.59941 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce6afe57-f661-39ae-897f-b51510701ee4 | -11.21125 | -60.60299 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15e7de0c-0d6a-3ea7-82a0-dcb93c6827d5 | -11.20735 | -60.60604 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4a49ef00-57c9-39dd-8ebc-d4729c37e9eb | -11.20125 | -60.62337 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5e078ca-f622-3ad1-94cb-266d85d489b6 | -11.19868 | -60.48369 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47c803d8-3f76-3f8b-b807-36f647993909 | -11.19801 | -60.44313 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0873d826-80cc-3a09-9f40-e0e4d27aec21 | -11.1979 | -60.62285 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 70b3430a-519d-35df-ab12-5a5bf86dc12e | -11.19746 | -60.44673 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b589ffb-9579-327f-b847-7cac9d95c0d2 | -11.19455 | -60.62232 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 03287104-226a-3ec8-966b-92fad041e41a | -11.1941 | -60.44621 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 841f27a6-4cbe-3f8f-ac85-9af01c6f6b3d | -11.19239 | -60.4349 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1ff3de87-5474-3ccf-bcdb-166ba5e7c7c0 | -11.19112 | -60.43451 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6fb6177b-ed1b-32ba-b650-800b66511fcc | -11.19056 | -60.4381 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aac69039-56f6-3cbd-a09e-d121d2c8e952 | -11.18977 | -60.49696 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4a7955b-7428-3ab4-9ab2-b3859a265630 | -11.18922 | -60.50053 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4bc89870-ea04-325f-a4d9-e98e98369351 | -11.1872 | -60.43757 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e128cf5c-05fa-3768-9666-dd1b417af1d7 | -11.18061 | -60.62377 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae1b660b-d7f4-3460-92b8-4943a5c20662 | -11.17951 | -60.63092 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 85baeb96-b283-3615-8dda-079c7fc860cf | -11.17827 | -60.45086 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d8f11a1d-ca49-3958-b0d6-8eaa9134225f | -11.17726 | -60.62325 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2d2487b-0bf9-3b6f-976a-6dfff73298a4 | -11.17671 | -60.62682 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab611ae1-926a-3b79-9dae-a251edc7b4c3 | -11.17617 | -60.63039 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 14159f69-fc74-32ec-a30d-b055334a5e59 | -11.17605 | -60.46521 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 20c5ddf5-cce4-38bb-9319-054ddb1f2e19 | -11.17547 | -60.44674 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05246567-8050-33ed-8c9e-aa4df6911202 | -11.17446 | -60.61915 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eb75dec8-9dac-3708-9230-880e38522040 | -11.17391 | -60.62273 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d21d4f9-cd58-3910-a7bf-223640d1e3e4 | -11.1738 | -60.4575 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0276f99-a090-3184-bad7-b076a960e983 | -11.17337 | -60.6263 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dd6ccc07-a667-3837-b0c9-11788fa6a173 | -11.17325 | -60.46109 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2148f627-d180-331a-8780-8ae059f495fb | -11.17282 | -60.62986 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f03be24e-c8e4-366f-8696-cbbce3c16c78 | -11.17002 | -60.62577 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e4fb761-a174-326c-9ecd-53e1dd7b7506 | -11.16887 | -60.61092 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 815bf3cd-f70b-3a04-91ab-2c9d5d7e760c | -11.16832 | -60.61451 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c11aff2-6754-3765-aa5f-f042e3d0196c | -11.16667 | -60.62523 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9385cc4f-0668-31a0-8dc5-eccbc6059fe5 | -11.16607 | -60.60683 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8d8a0027-726e-3e4c-b51e-5d07400ba0ca | -11.16502 | -60.60278 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb6524c1-d307-3ffd-a44f-4fb0c60a6e1f | -11.16447 | -60.60635 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96bee0ac-6639-3396-a806-e261fafa05b7 | -11.16168 | -60.60226 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cb87172d-57a6-355f-8a6f-5249c6e140ad | -11.16112 | -60.60583 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4d99b235-3eba-34f6-9449-1c2a42f64270 | -11.15889 | -60.59814 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 132b7057-088b-366e-8b17-e637278f3cff | -11.15833 | -60.60173 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b359b54-e2b8-3ba7-8e4c-0ff7a220e17b | -11.1578 | -60.62722 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99c4a67d-3c60-3137-ac42-41df7bb9bced | -11.15725 | -60.63079 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cd85ae4-66c8-37d3-86da-b338190f006c | -11.15553 | -60.59762 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7af4d9fc-12c2-3ce3-812c-a5f9d81cc7e4 | -11.14773 | -60.60369 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 781ea281-fda8-3f14-aa8b-1636e304ee1d | -11.14159 | -60.59907 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c2825e7-59f1-3d61-a375-ad47b2a85d7a | -11.13824 | -60.59854 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24e356d8-a340-35de-a1ae-e554d3f1b4ad | -11.13489 | -60.59801 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7f075a2c-d038-38f6-89c1-c57268f0d788 | -11.12124 | -60.46392 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0d864c7a-cbf2-30e4-baca-22a2ee6a882c | -11.11789 | -60.46339 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c42b9af9-b176-3672-9bde-807cb2a84361 | -11.11734 | -60.46698 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcdbe49b-fbd4-3441-a132-2f3ef58117f7 | -11.11343 | -60.47004 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 865784f0-cbbc-376c-91f8-1d4ae1756870 | -11.11288 | -60.47361 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c1c5898-bbab-3a04-b25e-48f67c7fc487 | -11.06179 | -60.43644 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40e0d129-825b-3643-b388-172150e63cdc | -11.06123 | -60.44004 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1f677d96-7522-3def-9b0b-3ceba32eea2e | -11.06068 | -60.44362 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 223b0808-c463-3079-8621-c32252e14873 | -11.05788 | -60.4395 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c18590df-7ac6-325d-9e3e-45079b4ee600 | -11.05732 | -60.44308 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8bdc650e-c7d5-3af6-a25e-f3d229b5ae37 | -11.01056 | -60.54573 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66388425-20bb-34fa-b03a-410a357cfe5d | -11.2641 | -60.5052 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d2cd0e61-e803-3a62-9831-64e541df1c70 | -11.00776 | -60.54166 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58fceed1-5a6c-3442-a76a-44d8ada15612 | -11.42648 | -60.43064 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 330a14ca-fd55-3480-8c0f-067114109cbe | -11.42593 | -60.43422 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af1ce3d7-e674-3bb1-b3f3-e935ff3d5132 | -11.42312 | -60.4301 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7cada9e-80fb-3e90-92a6-b773897fc7c3 | -11.42257 | -60.43368 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f518988b-55e7-306f-801d-48d3c023c17f | -11.42207 | -60.45948 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f636f2e9-d38c-3a7d-b941-a9b35c3c93ee | -11.41976 | -60.42955 | 2024-10-12 05:25:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36bc8df7-1daa-3491-9194-76970176de7f | -11.41871 | -60.45895 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c334f75-9613-306c-b2de-c4c38110d801 | -11.4159 | -60.45483 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 12db34dc-70ce-38db-bbf4-7256e02117a2 | -11.41535 | -60.45842 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e1092328-ee90-3c79-b9a9-d35d3f67f789 | -11.4131 | -60.45066 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6d4154b-fff9-3109-872a-16b59da3c2ab | -11.41254 | -60.45429 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d52e016c-bdd5-3552-9c31-4fc40c8c44de | -11.38235 | -60.59697 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c1a0b4a-d6e4-3877-8466-dc6a1680477e | -11.35157 | -60.5517 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc59bed6-2fb7-3915-a1a3-55c2cee8e0e8 | -11.35102 | -60.55529 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 01dbc194-e84f-3376-9bf0-dc5f9c861aaa | -11.34265 | -60.56502 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20a0decc-71b4-34dd-b50b-1b19c6b4e0c3 | -11.34092 | -60.53168 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed3facd2-0e06-3d6a-b0ad-47dafe9716bd | -11.34036 | -60.53526 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30769aea-8f35-33eb-8b6d-ef769cb1d8f5 | -11.33756 | -60.53117 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3986709-774f-3c1e-aa71-8388065898a2 | -11.33701 | -60.53474 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c22c7637-89b4-3527-9758-bd7b3f0c5d33 | -11.33646 | -60.53831 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ce7ec81-b185-3afd-a7c5-5282da9787c5 | -11.3342 | -60.53065 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 01866c24-6d7f-392e-9d6d-3c1bb98befa3 | -11.3314 | -60.52654 | 2024-10-12 05:25:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README132.md)
