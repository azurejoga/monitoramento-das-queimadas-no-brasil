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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc4f217f-f01b-3958-9302-f42edec98cbd | -17.84695 | -56.85521 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 670319f0-0733-34b0-a679-12433faa014d | -17.84203 | -56.85394 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| a20fa1c1-4b21-3ab0-8230-53c6dfb0982b | -17.64104 | -56.2373 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 62b9e6d3-4061-30b6-ac66-ff043d14a7d4 | -17.6402 | -56.24129 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| d8f5f03f-92e4-3bd8-b274-ed400f1c64eb | -17.63936 | -56.24528 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5edee979-c1e0-3bf2-89d9-f0692760f712 | -17.63545 | -56.23597 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ea46845a-2bcf-3480-8a59-5980e63961a0 | -17.63293 | -56.24791 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 0acc7ad0-3a52-3cc2-a9c4-370923659c56 | -17.63209 | -56.25191 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 17f6c6ce-77b6-3020-8ca5-a8dfb1119c1c | -17.62986 | -56.23465 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c0aefae0-14e8-36c3-8ca7-398783c5b964 | -17.62427 | -56.23335 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| ebe2f0a6-6304-3ac6-97e9-a884be9e8b85 | -17.20887 | -56.68454 | 2024-10-17 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a18d2dce-5aec-31d9-a18a-eeda9d70b6e7 | -17.20794 | -56.68888 | 2024-10-17 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 5a377947-f6ea-3088-a65f-ab62f741747c | -17.20308 | -56.68315 | 2024-10-17 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 21599ce6-5e17-32fc-a8ae-d71566a9a84f | -17.19822 | -56.67741 | 2024-10-17 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 273c5fe0-c2a4-3d1a-a3e9-75fbe05e5364 | -17.98083 | -57.42841 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| fad8a4d3-62f6-3ace-bfdb-7d39dee982af | -17.97591 | -57.42226 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 624ab420-c1b4-339d-ab7a-9607c12e8076 | -17.97487 | -57.42693 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 1f4bb1be-bd24-3749-87e4-fba290ea8a7f | -17.93882 | -57.44759 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 40e3b8c6-4bca-3d48-b39b-3ff69e9e0cf6 | -17.93777 | -57.45226 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 3193decf-a153-3dc7-889b-8d667a871a71 | -17.93681 | -57.45012 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 11974315-9782-3199-b95a-e207280b0b58 | -17.93579 | -57.45481 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 3111e5e3-7926-3e6d-9692-04345d7fa209 | -17.92794 | -57.43997 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| fbc75f5c-0a99-3d1f-8b87-0ea595a2a379 | -17.92689 | -57.44464 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c8ab0e20-429d-3d83-b5f4-fe095324a045 | -17.9259 | -57.44244 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| fd3fd5ea-847f-36b9-9338-df6776ded8e7 | -17.92488 | -57.44713 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4e21176b-f961-3cc4-be3e-92b025e53f29 | -17.92303 | -57.43383 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 942521cb-f222-326e-82fc-9bd5bec77308 | -17.92197 | -57.4385 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7e516e09-3556-3be9-addc-99b252c1cec1 | -17.92092 | -57.44318 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| e8a1e83c-e902-3538-ab82-ebf2aa3fc2aa | -17.91993 | -57.44095 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 54c8e789-a0e9-35e4-ac05-8989603938fe | -17.8844 | -57.24798 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 2125b41e-095c-3594-85b0-a9ea577e122a | -17.8815 | -57.24608 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| b65338da-e0f7-339b-85af-b0194e05830b | -17.8785 | -57.24649 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| e4c6ec7a-4145-3fb7-b400-f70bbc80d5be | -17.87559 | -57.24462 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8bf4e73c-15b9-3785-8f0c-fa2ce53e0511 | -17.8726 | -57.24502 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 74e81495-c872-3836-a3f3-e89bfa9b858e | -17.87161 | -57.24962 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2cf095a2-ea31-3d22-9b60-00b45375adaa | -17.86867 | -57.24775 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 7b39c1b9-40b5-3ae1-a232-233d6f7afae4 | -17.86765 | -57.25232 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 13ffac6a-472d-341f-b494-6c7eaeccfc89 | -17.8657 | -57.24816 | 2024-10-17 04:17:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| cb81a70d-b64d-3857-b7c2-357bcaba6a31 | -17.22792 | -57.31134 | 2024-10-17 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 6ca22a85-8a77-39ea-a562-7a1e7454134d | -17.22703 | -57.31029 | 2024-10-17 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| e7f7a5fa-1638-33d4-90f7-71e1f35ade96 | -17.22687 | -57.31608 | 2024-10-17 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| e18655d0-f4b7-3257-a605-41e040845609 | -17.22601 | -57.31503 | 2024-10-17 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f3d6f377-c4f0-336d-b49c-0aa9ecbc06d3 | -17.22582 | -57.32082 | 2024-10-17 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| f98be0a4-9e9c-37be-bd20-4602cb497d11 | -17.225 | -57.31979 | 2024-10-17 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 4bb73041-d8d0-3f9e-b492-886bba8bab53 | -17.22192 | -57.30988 | 2024-10-17 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| d0e5b922-126e-362b-b857-23261ef9e3d9 | -17.22103 | -57.3088 | 2024-10-17 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 35b83ebb-392e-3861-9809-cfc6d969f135 | -17.22087 | -57.31462 | 2024-10-17 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 0f1613a8-3c86-396c-a8e7-2a0b32b5caeb | -17.22001 | -57.31355 | 2024-10-17 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| c2ec7432-ab6b-3d09-a796-6ceff01b538b | -17.21982 | -57.31937 | 2024-10-17 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| cf060dec-e54c-3fa5-909c-47ea5850c748 | -17.21899 | -57.31832 | 2024-10-17 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 81cb6eb5-32d7-360a-919a-54bdb56a213b | -17.21876 | -57.32412 | 2024-10-17 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 06db0b48-396d-30eb-9e2f-72396243f345 | -17.21797 | -57.32308 | 2024-10-17 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 11072aeb-a1e4-315d-bca3-f67f96909dfc | -17.16922 | -56.81286 | 2024-10-17 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| ec25703a-189c-3c53-8dc2-700c5291d2ac | -17.16844 | -56.84513 | 2024-10-17 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 6989a407-61f4-3b9b-be04-6f7a3ba30533 | -17.16827 | -56.81727 | 2024-10-17 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 5d7c2fec-e781-3fed-bb61-a08aef0f4bff | -17.16354 | -56.83931 | 2024-10-17 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 13be237b-7354-3df2-9735-e20cdeb4a6f4 | -17.16164 | -56.84814 | 2024-10-17 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e04cb907-fbe3-323c-a323-0e9c7a3366b8 | -17.15959 | -56.82907 | 2024-10-17 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| d5e35dc0-a895-3b4e-80b5-fee427526bf8 | -17.15865 | -56.83346 | 2024-10-17 04:17:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8dff3f65-28c8-3c4e-8a3a-81e57b24064f | -22.30489 | -41.88057 | 2024-10-17 04:17:00 | NOAA-20 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9626fdaa-fdc9-3466-a44b-019a63357cd4 | -17.1867 | -49.85377 | 2024-10-17 04:17:00 | NOAA-20 | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa4f1231-e983-3c44-99d6-94e073a8078d | -18.59167 | -41.11496 | 2024-10-17 04:17:00 | NOAA-20 | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2c8f76ad-8a91-34d4-8dbd-186367fede79 | -22.59801 | -42.21372 | 2024-10-17 04:17:00 | NOAA-20 | ARARUAMA | RIO DE JANEIRO | Brasil | 3300209 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a6e50d98-56aa-34f5-a970-0ecbf89df839 | -18.59955 | -41.11583 | 2024-10-17 04:17:00 | NOAA-20 | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| 2fac4348-cc1a-39e9-92ac-63e52681e570 | -18.59891 | -41.1207 | 2024-10-17 04:17:00 | NOAA-20 | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 542728f0-7607-3542-8a7e-0ddaf9fcfe53 | -18.59629 | -41.11024 | 2024-10-17 04:17:00 | NOAA-20 | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c30b7bb8-27a5-3942-b6a2-304971624bc5 | -18.59561 | -41.11539 | 2024-10-17 04:17:00 | NOAA-20 | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| dbe40056-b421-33f4-a2ae-60bdef9059f1 | -18.59495 | -41.12042 | 2024-10-17 04:17:00 | NOAA-20 | MANTENA | MINAS GERAIS | Brasil | 3139607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| e3a9bd81-ea99-3b4c-80fd-40522b4e9bfc | -18.39908 | -40.87996 | 2024-10-17 04:17:00 | NOAA-20 | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 812f99f4-c8cb-34d0-9451-6bc961402359 | -18.39511 | -40.87943 | 2024-10-17 04:17:00 | NOAA-20 | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| b72af42b-3220-3cc5-b990-939aa9ca652f | -18.39441 | -40.88475 | 2024-10-17 04:17:00 | NOAA-20 | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 66bc0770-08d2-3775-9f9c-ad8fffb1013b | -18.39114 | -40.87883 | 2024-10-17 04:17:00 | NOAA-20 | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 16.2 |
| 49298f33-93c8-3568-b938-3b05cc4822f2 | -18.39044 | -40.88416 | 2024-10-17 04:17:00 | NOAA-20 | ECOPORANGA | ESPÍRITO SANTO | Brasil | 3202108 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 11c1a1a5-6805-3954-bf40-c5fc5761d84e | -18.09119 | -41.42818 | 2024-10-17 04:17:00 | NOAA-20 | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 52a622e2-27f1-396f-873e-202fa67aa04b | -18.09052 | -41.43318 | 2024-10-17 04:17:00 | NOAA-20 | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 36c96517-208d-33dd-9775-ff63757df75f | -22.30501 | -41.88411 | 2024-10-17 04:17:00 | NOAA-20 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| bd424d4e-d98b-3e12-90c8-14d56a9401a6 | -19.13907 | -42.29222 | 2024-10-17 04:17:00 | NOAA-20 | PERIQUITO | MINAS GERAIS | Brasil | 3149952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| ef8913db-7b74-3d59-90d1-b334712b83fa | -18.55215 | -42.95175 | 2024-10-17 04:17:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1cc84a5e-546c-3079-a17e-99cd643dcc13 | -18.40015 | -42.19706 | 2024-10-17 04:17:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 973f1df9-2af4-3d2b-b3c8-0b8310d89d16 | -18.39644 | -42.19669 | 2024-10-17 04:17:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 1649975b-ede7-31f7-a163-288802d71f20 | -18.39586 | -42.20097 | 2024-10-17 04:17:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5bd7fc05-e485-3005-8a49-06c345ce1774 | -18.39218 | -42.2004 | 2024-10-17 04:17:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6b632b7e-602c-3a85-ae55-62fdf57183a8 | -18.38849 | -42.19981 | 2024-10-17 04:17:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0c6a0785-c542-3b26-926b-fbdd02229350 | -18.33154 | -42.34483 | 2024-10-17 04:17:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 075c3ce2-06e4-3d6d-8169-25686d4bf186 | -18.28587 | -42.79731 | 2024-10-17 04:17:00 | NOAA-20 | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 41bf94b1-2257-3eb9-85f3-7a7c429554b4 | -18.28231 | -42.79668 | 2024-10-17 04:17:00 | NOAA-20 | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 43b0f823-75f3-3f2b-9314-c6a434e90488 | -18.25862 | -43.03724 | 2024-10-17 04:17:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| abd7eb93-0b84-3a2c-8f64-ddad8d101295 | -18.25842 | -43.03823 | 2024-10-17 04:17:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b2286017-4962-38d8-b351-6c8d6e44c424 | -18.0988 | -42.91805 | 2024-10-17 04:17:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 12ccdc0b-53c3-37bc-abb0-96e98fabdd59 | -18.09821 | -42.92225 | 2024-10-17 04:17:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d03f4dc6-0882-30f7-aa98-53a63cbe0acd | -18.08796 | -42.7191 | 2024-10-17 04:17:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1793984a-8e40-3874-b7d5-afba056f29db | -18.08624 | -42.7219 | 2024-10-17 04:17:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9e52c527-cb99-382e-bbc1-4f4abffed677 | -18.08442 | -42.70861 | 2024-10-17 04:17:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fc6a1564-7a19-336e-a9ca-b8b2d0eca72d | -18.08203 | -42.70948 | 2024-10-17 04:17:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 8f250678-42f8-3591-b5dd-5083c5409913 | -20.93287 | -42.59634 | 2024-10-17 04:17:00 | NOAA-20 | ERVÁLIA | MINAS GERAIS | Brasil | 3124005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e1efde15-ed01-3899-b08e-e7d9c1ec0271 | -21.20938 | -42.83768 | 2024-10-17 04:17:00 | NOAA-20 | RODEIRO | MINAS GERAIS | Brasil | 3156304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 924e8eaf-f470-3339-915a-e9e53e0eb0bc | -21.04721 | -43.37901 | 2024-10-17 04:17:00 | NOAA-20 | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7a27003e-3b8f-3c86-b2bb-db43a4dbd3c5 | -22.90218 | -43.7527 | 2024-10-17 04:17:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a3e39c32-8b18-306c-90cc-78b14f36d217 | -22.90156 | -43.75711 | 2024-10-17 04:17:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1133248a-3493-38ee-b6bf-5166eea4d9fa | -22.78601 | -43.75893 | 2024-10-17 04:17:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README35.md)
