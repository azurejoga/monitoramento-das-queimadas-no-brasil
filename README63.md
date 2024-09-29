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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c76f4980-5ea3-3eb0-9125-2fececd0d689 | -20.80208 | -53.11108 | 2024-09-29 04:53:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28dc5868-e1db-392f-a140-02c8712cc7d6 | -22.52696 | -54.09523 | 2024-09-29 04:53:00 | NOAA-20 | GLÓRIA DE DOURADOS | MATO GROSSO DO SUL | Brasil | 5004007 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9f42be04-7d19-344e-9dc7-d1369db2ce85 | -22.52637 | -54.0993 | 2024-09-29 04:53:00 | NOAA-20 | GLÓRIA DE DOURADOS | MATO GROSSO DO SUL | Brasil | 5004007 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2b59c270-c6da-3d9c-9821-0785dc2dd7d4 | -19.98248 | -55.49482 | 2024-09-29 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 090178dc-cb3b-3a61-8b8c-39255bd922a1 | -19.98191 | -55.49847 | 2024-09-29 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cc6ae6b6-8a6e-347d-9a93-4f8a8ed6bfc8 | -19.98135 | -55.50212 | 2024-09-29 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 01203c70-6698-3c59-8ca7-bab5785acc12 | -19.98021 | -55.50944 | 2024-09-29 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 90bc7738-e318-359e-8af3-7952c009e615 | -19.97964 | -55.51309 | 2024-09-29 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5a9f9a0a-25c2-370e-9d4b-14e6f0dd592b | -19.97917 | -55.49424 | 2024-09-29 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32d09665-142c-3784-abf4-23216d8b3d91 | -19.9786 | -55.49789 | 2024-09-29 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 11a2e0e5-d0c9-3627-82fa-e200f13e63b4 | -19.97804 | -55.50155 | 2024-09-29 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 977b31c8-36f8-38c7-b461-57247134feaf | -19.97747 | -55.5052 | 2024-09-29 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0458c706-ab6c-316c-a6b7-83932d3adfa0 | -19.9769 | -55.50885 | 2024-09-29 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 99e80ebb-acfd-3bf5-9f3a-be1a8957345d | -22.16924 | -56.03592 | 2024-09-29 04:53:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c15f1953-8f24-358c-8430-72c5c7929bda | -22.16593 | -56.03533 | 2024-09-29 04:53:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 13.8 |
| b6b8b06e-8d9b-33b2-acca-689b6acce470 | -22.16535 | -56.03904 | 2024-09-29 04:53:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 2569879c-f24e-3304-adcc-7458829c43db | -22.16477 | -56.04276 | 2024-09-29 04:53:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 13e48e97-8e62-3288-a4dd-e7bc4c12f55b | -22.16262 | -56.03473 | 2024-09-29 04:53:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 5cf49e9d-4ef7-37f3-b3a4-f0c0c4068d06 | -22.16204 | -56.03844 | 2024-09-29 04:53:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 1b6a1ddd-fb3e-340d-a3f4-7dc6e509d4a1 | -22.15244 | -56.20866 | 2024-09-29 04:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 614997d6-4c8d-32a6-9be3-bfca5aa2ad4d | -22.14913 | -56.20806 | 2024-09-29 04:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 931ad9d2-d889-389c-a1a6-2b82bf1f3a8e | -22.14581 | -56.20746 | 2024-09-29 04:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 917d5c04-eaaf-3f93-85f3-41cdc28ba453 | -21.37038 | -55.71392 | 2024-09-29 04:53:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 53c4cd9f-4343-3fae-b63e-6b6576d84358 | -21.32778 | -56.11669 | 2024-09-29 04:53:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 68b0d52d-620e-3ecc-ae00-69f7f5bf961b | -23.0757 | -55.16665 | 2024-09-29 04:53:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 48c61abf-599e-3538-b43c-898c7edb93c7 | -23.92406 | -55.39886 | 2024-09-29 04:53:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1f594d23-a028-3c61-8a30-d54a8bc4a0cb | -19.99776 | -55.87307 | 2024-09-29 04:53:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 20328fb7-2654-3cc3-b765-c3d888a64da4 | -21.00973 | -57.51073 | 2024-09-29 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 4c9cde04-e1e4-31fe-8933-b822572c74cd | -21.00699 | -57.50629 | 2024-09-29 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| ecbbd328-e909-3b13-86b8-16c52ac3ba23 | -21.00635 | -57.51011 | 2024-09-29 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 153c5819-3bd1-3392-b5f2-a81cee14b2a0 | -28.31531 | -48.71194 | 2024-09-29 04:55:00 | NOAA-20 | IMBITUBA | SANTA CATARINA | Brasil | 4207304 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dec9d924-135b-3cf5-bff6-8b45ff11e2dc | -28.31031 | -48.7114 | 2024-09-29 04:55:00 | NOAA-20 | IMBITUBA | SANTA CATARINA | Brasil | 4207304 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ca461bf0-1002-3fba-8d0a-23031ca94568 | -26.27126 | -50.26901 | 2024-09-29 04:55:00 | NOAA-20 | TRÊS BARRAS | SANTA CATARINA | Brasil | 4218301 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 233c7d81-7b30-3567-b504-30fcd6b81288 | -26.26685 | -50.2684 | 2024-09-29 04:55:00 | NOAA-20 | TRÊS BARRAS | SANTA CATARINA | Brasil | 4218301 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0bd47d70-d15a-3724-8f52-0d84a639cc6e | -26.02473 | -53.75512 | 2024-09-29 04:55:00 | NOAA-20 | PRANCHITA | PARANÁ | Brasil | 4120358 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 72b4c7ed-fdb2-3f71-aeef-7c05549958e5 | -11.06 | -52.5 | 2024-09-29 05:04:21 | MSG-03 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 51825a4b-f28a-3da4-af25-e7f0d624e187 | -1.87679 | -52.09188 | 2024-09-29 05:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2a47ca71-fe3c-37ba-ab68-925d45084f91 | -2.21778 | -53.66896 | 2024-09-29 05:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af496703-78e1-3d75-ad37-75b6ae3f67a7 | -2.21714 | -53.67321 | 2024-09-29 05:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ebbbf314-ebc0-3473-aeff-bea54125f2f2 | -2.15386 | -53.6636 | 2024-09-29 05:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c763ac9e-dc0e-393d-9e3e-911a7ee9fd39 | -2.15257 | -53.67199 | 2024-09-29 05:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 698822b9-9a15-3044-8645-366f06fd759e | -2.15241 | -53.66244 | 2024-09-29 05:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 60aa5ea5-f40d-30d6-bba2-8ad5e246e960 | -2.15178 | -53.66668 | 2024-09-29 05:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 633727b5-bedb-35c9-b737-1eb0ecebd895 | -2.15117 | -53.67087 | 2024-09-29 05:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c4454a5f-2496-3f40-8378-364edd500827 | -2.15055 | -53.67508 | 2024-09-29 05:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 69dfb000-3d8d-3cef-88b9-fd14c1c17b49 | -2.14865 | -53.65827 | 2024-09-29 05:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 7abc98a1-ec8a-35b7-ab84-e9aebcb3165e | -2.148 | -53.6625 | 2024-09-29 05:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| bc6e40ce-8fc0-3222-bb90-a8290726209d | -2.14736 | -53.66668 | 2024-09-29 05:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 2986da71-bfb6-317a-8a5c-554f272a6b12 | -2.14671 | -53.67089 | 2024-09-29 05:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 3a753561-c07b-3c44-ab3c-7324eda5db36 | -2.14654 | -53.66133 | 2024-09-29 05:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 890e02c9-136a-3c35-9186-32bce0b1134c | -2.14607 | -53.67505 | 2024-09-29 05:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| c7cf6928-bfd5-3c09-89e6-37ad18cae3b7 | -2.14592 | -53.66557 | 2024-09-29 05:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| abab9c7c-857a-3165-83b6-5d7aadc9e631 | -2.1453 | -53.6698 | 2024-09-29 05:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| aca3ad85-0581-3883-aa1b-0724709883ff | -2.14469 | -53.67398 | 2024-09-29 05:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 283f9ca0-59bc-35b9-a498-eabeec8e6bda | -1.67202 | -55.13894 | 2024-09-29 05:40:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 664602cb-b567-3de1-94c0-544b402111ce | -1.67151 | -55.14228 | 2024-09-29 05:40:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c17d426-8f8c-3a5e-a2d4-aef538254984 | 4.59876 | -60.32892 | 2024-09-29 05:40:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f66c4ae-0c94-33a9-a789-7af4356b4bc5 | 4.31459 | -60.92472 | 2024-09-29 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 68fc7bf0-e896-3e24-9fd8-67e50c2f52ea | 4.3119 | -60.95138 | 2024-09-29 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49c3aa60-3f7c-3685-89b8-817397ae0bc4 | 4.30775 | -60.92559 | 2024-09-29 05:40:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b1d5d6a6-0b5a-3e12-b8e3-3559d4caa232 | 2.62328 | -61.33715 | 2024-09-29 05:40:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7675ecbb-37aa-3b30-81e6-750ba816236a | 2.62242 | -61.33664 | 2024-09-29 05:40:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f9b2511-8f81-39fa-80e9-e30222fd43ca | 2.305 | -61.32563 | 2024-09-29 05:40:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f9f40eb-ae36-35e1-8bf9-caabf28b9fd1 | 2.30218 | -61.3299 | 2024-09-29 05:40:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6b96df2-e91a-32e9-a8a3-1addc4c1d2dc | -3.50678 | -51.1966 | 2024-09-29 05:42:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| ac25881d-87f4-3438-be04-6db384f7274b | -2.96255 | -51.65046 | 2024-09-29 05:42:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 24d903fd-4e14-3ba3-bdf0-8ed5d4e2e84a | -2.96047 | -51.64598 | 2024-09-29 05:42:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 77272143-7270-3c16-a3b5-055ecc09b3aa | -2.95956 | -51.65214 | 2024-09-29 05:42:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c820ecf5-950a-372a-93ab-e048f1b91f13 | -2.95581 | -51.64934 | 2024-09-29 05:42:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c6a71fee-c236-380f-a6eb-cbd0b710bd8e | -2.88754 | -51.57737 | 2024-09-29 05:42:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 23f0105d-3c2f-3fd4-a257-a907699e1838 | -2.88108 | -51.67031 | 2024-09-29 05:42:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5632d7d8-4e18-31c0-9906-73b6061152a3 | -2.88022 | -51.67631 | 2024-09-29 05:42:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0115273-9717-36fd-88df-198d2a6fc57e | -2.87926 | -51.66462 | 2024-09-29 05:42:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4cc43d3e-89bc-3bdb-ae63-4b506e412432 | -2.87833 | -51.6708 | 2024-09-29 05:42:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9b6e1250-da9d-37b7-81ff-15cd478b7845 | -2.87743 | -51.67677 | 2024-09-29 05:42:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9054eff1-e6e1-3a44-92b2-d32f10c6912e | -2.87349 | -51.67524 | 2024-09-29 05:42:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 810184df-a245-3476-a86c-6b781bbbc6c6 | -2.87071 | -51.6757 | 2024-09-29 05:42:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| feb39e12-ada1-3c1b-a9e5-2cb6a7b28b78 | -2.76183 | -53.23071 | 2024-09-29 05:42:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 223a8f8d-f017-3417-8fdd-16dad51b82da | -2.75574 | -53.22963 | 2024-09-29 05:42:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1dacfff-8687-3e49-befb-f9d8d248b67b | -2.68393 | -52.4359 | 2024-09-29 05:42:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5d6dc254-f00d-3483-a65e-0ef68e6cc8ae | -2.68316 | -52.44117 | 2024-09-29 05:42:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 918515de-72ba-3950-84be-6d9587f7a5fb | -3.89194 | -52.30547 | 2024-09-29 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b29d46c-9c8f-3315-b053-915a92ae0bee | -3.89105 | -52.31171 | 2024-09-29 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c498916a-c913-3986-94c8-d1e2bfbce163 | -5.85428 | -53.56505 | 2024-09-29 05:42:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2d18c085-8c20-320c-b131-f91bf5f053b5 | -3.46316 | -53.79948 | 2024-09-29 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b54d6def-c610-3c48-992c-da0d96868281 | -3.46254 | -53.80369 | 2024-09-29 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2aad1bab-0c2e-327e-bf3f-0d15cf9bb271 | -3.14054 | -53.6896 | 2024-09-29 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5726095d-e15e-3a35-9d9e-0c46769bfa9e | -3.13593 | -53.67934 | 2024-09-29 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5cd87889-1c2c-312b-bafa-803efa2e0ce6 | -3.13526 | -53.68395 | 2024-09-29 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9a6600f7-02b8-32eb-8f4f-bf9168e2b592 | -3.13156 | -53.75127 | 2024-09-29 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1b5635b-1b41-3875-bfff-dd02b59cd47f | -3.13093 | -53.75565 | 2024-09-29 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b7608f58-25ed-37ff-904c-8249bc9eec71 | -3.12626 | -53.74598 | 2024-09-29 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ac479e78-1e4d-3e10-9130-1675f1d37a6d | -3.12562 | -53.75035 | 2024-09-29 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 00005628-c8ee-33fb-b602-6667c2a6d5b0 | -3.12499 | -53.75473 | 2024-09-29 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 872adefd-502a-35eb-8658-65c5619519ba | -3.11968 | -53.74942 | 2024-09-29 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59ed10b2-a2f8-3564-a973-388c3a63c0e3 | -3.11905 | -53.7538 | 2024-09-29 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2949987f-b1da-3fc4-947e-43dc1e0c85f7 | -2.83214 | -54.60768 | 2024-09-29 05:42:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3013487-dea1-3ef2-bfa5-62e887977a39 | -2.55494 | -54.60758 | 2024-09-29 05:42:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7dda7e3f-b65c-3937-9b4b-4ec81c4680ab | -4.06627 | -54.10274 | 2024-09-29 05:42:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4db19ae3-88c7-317f-a902-8603ab58db33 | -4.04828 | -54.01784 | 2024-09-29 05:42:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README64.md)
