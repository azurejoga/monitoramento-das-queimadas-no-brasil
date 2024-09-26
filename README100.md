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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f45d90f3-8032-3c4a-81a9-a279064c809c | -7.61181 | -55.29361 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d14e5f4d-4f7c-3712-a682-4e6d7d1a28ad | -7.61168 | -55.35836 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 358ae274-7491-3e1a-a814-5fefb9b59215 | -7.61017 | -55.28255 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1943e575-0ca2-3ae8-927c-8d764a4f61d6 | -7.60961 | -55.28606 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 916a9188-cb1f-39dc-9c52-9b292ebf2e2c | -7.60905 | -55.28957 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a35656f1-7cc4-3aa6-a902-7b63475706b1 | -7.60892 | -55.35431 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45cba014-3087-3de9-9763-0989589ee6c1 | -7.60836 | -55.35782 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c03e2919-3b71-3290-b3b5-8e9e3632ad74 | -7.6078 | -55.36134 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 66e014e1-0c3a-3bd6-8381-2722616bbf5e | -7.60648 | -55.28483 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e2de4f1f-66af-356c-ba7c-e66a6cbd784b | -7.60616 | -55.35027 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 08c5a12a-c2dc-3ce2-be59-9ca13d7ec9d8 | -7.6056 | -55.35378 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 827b39b5-c9ca-3197-b980-ec721f1dda37 | -7.60504 | -55.3573 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a082dd71-4b6a-3abd-b838-a3589596b34c | -7.60447 | -55.36081 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1247bbf-84d3-3079-9996-dbf76e127ed2 | -7.5983 | -55.91446 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63604aaf-50a2-3a4f-86de-9b56fe85ddde | -7.57997 | -55.57777 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d50f1c3d-99c2-3fd8-83df-2ac6a335a365 | -7.56881 | -55.58327 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| edfe3a48-0fe3-319c-8b2d-090ccb0bbf43 | -7.56241 | -55.56336 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07f04a37-216e-3839-80df-5aef1a8aa59c | -7.55457 | -55.59122 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5734c71-ba1a-3298-a274-48e652e034cf | -7.46005 | -55.50001 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d6d84490-427d-3f89-998d-8e6e297d4e27 | -7.37941 | -55.49085 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 410cdd10-db48-3aaf-9db4-723cb1d54047 | -7.37884 | -55.49439 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53926ca1-2a2c-306f-8037-b758a39c3f29 | -7.37827 | -55.49793 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 045637da-45a2-3211-adbf-52cdf49b2f7a | -7.37771 | -55.50148 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7855067d-76e3-3bab-88a3-7528e303d349 | -7.37607 | -55.49032 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2aab39d-2d21-3739-98af-1adf7f5f0019 | -7.376 | -55.5121 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 7baadd20-1f87-30f3-8026-d3fffd0c8a41 | -7.3755 | -55.49386 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 3067565b-088a-3b3a-b692-2329bf2d0179 | -7.37493 | -55.49741 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| cc735ee2-a97f-305f-be32-0143faddcf32 | -7.37437 | -55.50096 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 81530c32-3b00-37d1-9a1a-133dcb1c4e4b | -7.3743 | -55.52274 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 47ae8771-26d8-3d92-8304-67de9decc307 | -7.37323 | -55.50804 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| d2335078-a387-3e3d-8901-80a49ebeaf51 | -7.37266 | -55.51158 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 058e6da5-c989-37b2-8375-845d1d8bf06e | -7.37216 | -55.49334 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| bbdaeb13-518e-3518-b42d-8e1359cac00b | -7.3721 | -55.51512 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 53a2b871-b332-375d-9244-a49988a18f3a | -7.3716 | -55.49689 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 703a2870-0256-33d3-b8bf-10102eeed335 | -7.37153 | -55.51866 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| f0e61522-1586-3b75-b30a-65663a4efc83 | -7.37103 | -55.50043 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| b914ac70-6192-3779-834f-73c7ff502208 | -7.37096 | -55.52221 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| b510804b-ee2d-36d8-9ad7-6d22cb5b228b | -7.37046 | -55.50397 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 065ec30f-4ede-30e4-b969-c4103c6909f2 | -7.36989 | -55.50751 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 1c786c83-ab3e-3bf4-9e52-cb1f3881ca16 | -7.36933 | -55.51104 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 36.4 |
| e244fbc8-0ef1-3beb-b921-36e3d7980e46 | -7.36883 | -55.49281 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ab6b366d-abf4-3833-a1ff-59c18db02aff | -7.36876 | -55.51458 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 7e3dafa7-33d5-383f-a79c-58eea77dbe84 | -7.36826 | -55.49636 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 60266079-df16-333f-bf5d-7ab7c401baec | -7.36819 | -55.51811 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| a33b48ed-57cf-39d8-b431-73f692457533 | -7.36769 | -55.4999 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d43f69ee-e0b9-377e-b6b8-008b7c3f07e9 | -7.36712 | -55.50344 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bbb5b926-98a1-3b87-85c0-9e99b4155bcd | -7.36656 | -55.50696 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| cc333e48-f7ef-38ee-9079-9c0ef4e8ae8d | -7.36599 | -55.51049 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 29eb18ae-0b6a-3da5-abd1-4be63324adbf | -7.36543 | -55.51402 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d314fcdb-2610-3c55-aba1-e62cc7c06958 | -7.36492 | -55.49583 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b9598115-f0a2-3443-bffa-8e33005d3592 | -7.36435 | -55.49936 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 325c08fe-f4c1-3eeb-882f-f2ef99431719 | -7.36379 | -55.50289 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1618394b-8b48-382d-923e-fba5d7311766 | -7.30973 | -55.30977 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3789c301-8ff6-3f15-81bc-680816722d57 | -7.1968 | -55.76484 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34fd7f1a-c05d-3c22-9fdc-4b6080698249 | -6.47859 | -55.56551 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f50a173-9bac-32df-a4f4-c65995081113 | -6.47523 | -55.56499 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3290c592-9817-344c-8ece-f9b34ebaf4fc | -7.82031 | -54.73092 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 37425040-9840-3535-b0a3-93d041c9c7e8 | -7.81976 | -54.73439 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| a4fffa85-53b3-30ae-ac2e-c9b129bc8e82 | -7.81701 | -54.7304 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 84245959-b1a7-38af-97c2-a6d1906bcaac | -7.81646 | -54.73387 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 40c18fcc-6b58-3f1a-a38f-27fce0c34ca6 | -7.81371 | -54.72987 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8a999f59-cfd3-3f39-8f36-654ee3d5b5ce | -7.81316 | -54.73335 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| f1127aa0-6a52-37d3-84ea-69532050a161 | -7.81096 | -54.72588 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c1b07649-fc0b-39b5-a60a-3dbd51a17572 | -7.81041 | -54.72935 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 11f82d24-2911-360c-bf75-842d773369be | -7.80986 | -54.73282 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e99edca5-bf69-316a-aa13-8503782a6d8c | -7.80931 | -54.7363 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c48fa532-c8f4-3714-bf27-7887ee21be4f | -7.80876 | -54.73977 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2f9148e0-5760-38a3-93d6-8f7e17d9b305 | -7.80766 | -54.72536 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 962705ac-5d38-3498-9d99-6680324304e8 | -7.80711 | -54.72883 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9b037f8e-6466-32b9-83cf-2eade3774b17 | -7.80656 | -54.7323 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 35ca706b-5215-3f66-93e3-956bad9bda62 | -7.80601 | -54.73577 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8d4a764c-bed0-3e35-8e57-e47d3789599f | -7.80546 | -54.73924 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 57b967bf-5cab-37f7-915f-70a05af62e85 | -7.80526 | -54.71436 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| fe034aea-573f-3ba2-82cd-0aff782ac390 | -7.80491 | -54.74271 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 60c4172f-7f20-36a5-ae2a-7f90bdd188ef | -7.80471 | -54.71781 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f51f9488-c7d9-3e6f-8123-884126d2c971 | -7.80417 | -54.72126 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8552bcba-7999-3556-846d-49e8571cbb84 | -7.80363 | -54.72472 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| dcd4eb00-f2bf-3b9c-91b8-4cd00fab1f3e | -7.80308 | -54.7282 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f569bcf0-3206-32c9-81e8-3df7f7cd3d62 | -7.80254 | -54.73167 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de1d43d0-35d4-30cb-8784-2512efe56720 | -7.80196 | -54.71385 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 760cc611-88ac-37a2-a6d5-5f4d729fb92e | -7.80145 | -54.73861 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 047d43be-0f0f-3b8c-81e9-a5e8749a4c02 | -7.80141 | -54.7173 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 33756aae-6df8-36ae-93a8-3c0f3e55372a | -7.8009 | -54.74208 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 42b20eec-6e7a-313d-ae97-a6a5612c45c4 | -7.80087 | -54.72075 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 611409df-da02-3cb6-b917-36908c9627a6 | -7.80033 | -54.72422 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| da3b2e5e-ea49-3669-aea3-b0a9ff5eb029 | -7.79978 | -54.72769 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 98ff5774-b2ff-3b5f-a0f1-a0ccd7dd4522 | -7.79869 | -54.73463 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 94646d81-26b1-31a6-964d-fdf251dee7c5 | -7.79866 | -54.71334 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5dfb030f-4107-34a7-b8f9-71e61f47afad | -7.79815 | -54.73809 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bb68d77a-3143-3dd8-a0f3-4ebccc52b35b | -7.79811 | -54.71679 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8f50078d-ac85-34fb-abcf-1273b7da3970 | -7.79757 | -54.72024 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 62c29db7-f23a-36f5-b5a7-6d699011dd56 | -7.79703 | -54.72371 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d4a258ec-20be-39b9-b5c9-7a81ca228d8d | -7.79536 | -54.71283 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7bc45c33-35a1-31de-b49a-eb43af91d743 | -7.79481 | -54.71628 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ac4f02fb-6ec1-3f2a-9481-74c178c3be30 | -7.79206 | -54.71231 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8165682b-2983-3edd-9b7b-74f20d163287 | -7.79151 | -54.71577 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c73f5538-b77e-3d80-aa06-4e45b7c64793 | -7.78767 | -54.71872 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ff3baa5-7bbe-35f3-a1a3-e3ded76701de | -7.75331 | -54.97976 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b5709fa-b05c-382e-ae3e-8d9ee1544c79 | -7.75306 | -54.74518 | 2024-09-26 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90c73657-3ece-3714-bf1c-c3fb0fbeb2d6 | -7.57611 | -55.1544 | 2024-09-26 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README101.md)
