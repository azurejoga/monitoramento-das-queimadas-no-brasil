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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3e5ee73-cde4-3a3d-9944-8c5bc3ac9230 | -10.08143 | -55.49252 | 2024-10-25 04:40:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b241b45-047a-369a-ab26-c533cecbab51 | -10.08078 | -55.49623 | 2024-10-25 04:40:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb5a2bc0-c8e4-39be-a838-9c23fcf07936 | -10.07799 | -55.48806 | 2024-10-25 04:40:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6abf359d-2900-3e39-b9fd-0d22417c836a | -10.07734 | -55.49177 | 2024-10-25 04:40:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c42edc5-6999-31f5-8d4e-40d6bc07dfec | -10.07669 | -55.49548 | 2024-10-25 04:40:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 538b19a4-1872-34b7-8844-f026942ad017 | -9.9187 | -56.26099 | 2024-10-25 04:40:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78820ddc-2513-3898-9040-523ff32ada50 | -12.02452 | -57.08603 | 2024-10-25 04:40:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 3fef04b1-7f15-362b-99d7-445ebac7d9e5 | -12.02373 | -57.09044 | 2024-10-25 04:40:00 | NPP-375D | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4da3f86f-845e-3fa8-beca-6bfb23ba5ad8 | -11.90244 | -56.40744 | 2024-10-25 04:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a18bb784-0ee2-3093-be92-fb6b3d7b6fbb | -11.90174 | -56.41138 | 2024-10-25 04:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bd511ceb-63d4-39d0-8481-1abac4c5acc8 | -11.89822 | -56.40664 | 2024-10-25 04:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ca6b471d-2e89-3828-9a15-bf1e29e15e72 | -11.89752 | -56.41058 | 2024-10-25 04:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c0a26e8f-f6d4-3ecf-a5de-c0bd541acfd6 | -11.89682 | -56.41451 | 2024-10-25 04:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8a517947-a080-3219-ba21-c0f14584b66e | -11.8933 | -56.4098 | 2024-10-25 04:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c6860cf4-e2ac-373b-b054-b01300a1acdb | -11.8926 | -56.41374 | 2024-10-25 04:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ed56ed6a-3e8a-32b1-8742-8c098059c2fd | -11.88908 | -56.40903 | 2024-10-25 04:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a915fc77-1e89-3047-871b-7adc4d954c1c | -11.88514 | -56.21157 | 2024-10-25 04:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e638c14a-df5a-30cd-adf9-754f4e0fe941 | -11.88511 | -56.21438 | 2024-10-25 04:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1aaaa26d-266e-3434-9f3b-a590b58def2c | -11.88447 | -56.2154 | 2024-10-25 04:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 09ecfcfb-ff1c-3278-be67-27961946623f | -11.88442 | -56.21822 | 2024-10-25 04:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5285a713-a011-3ca9-b647-5163e41573d2 | -11.88164 | -56.20977 | 2024-10-25 04:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a82b890b-0d5d-3098-a503-799a18cdf2a1 | -11.88164 | -56.20694 | 2024-10-25 04:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9758c259-cef1-33a3-a5d5-2e7945d27156 | -11.88097 | -56.21078 | 2024-10-25 04:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1fc7cf11-0440-3609-a28e-3e60ea4947d6 | -11.88095 | -56.2136 | 2024-10-25 04:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aad2a43b-cab0-3e1b-9cf5-ff868453053b | -11.88031 | -56.21461 | 2024-10-25 04:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| db337a4a-7ccc-3c2f-b123-5aca40a3ad14 | -11.87748 | -56.209 | 2024-10-25 04:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ae80a49-2ba3-36ed-a5da-d3aaca897e5e | -11.87681 | -56.21 | 2024-10-25 04:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67af9d22-358e-35b9-a2b7-62587f351657 | -11.87678 | -56.21283 | 2024-10-25 04:40:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e15dc0f9-591a-33ba-8331-28e02bf1a360 | -11.41187 | -56.73156 | 2024-10-25 04:40:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11e4d1a6-b98b-3ce7-a555-c428ae3d8b13 | -11.13527 | -56.78941 | 2024-10-25 04:40:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 992761f8-f218-3959-b950-23116584e578 | -9.75783 | -57.23701 | 2024-10-25 04:40:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be56625b-16ec-36b2-baf0-1f5051eb0465 | -11.06224 | -57.82061 | 2024-10-25 04:40:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e339ac3-b400-3b42-a172-0318ab56eb90 | -11.05844 | -57.82185 | 2024-10-25 04:40:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63c82c5c-d379-3a94-8af3-8f693f5d6d29 | -16.04659 | -58.25775 | 2024-10-25 04:40:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 7807099d-e278-3945-9b57-94154bea1dff | -10.39137 | -58.41739 | 2024-10-25 04:40:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79360ec6-55c5-3e71-b1e7-8ce74a64653f | -15.69361 | -59.74334 | 2024-10-25 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ba0ba604-f2d6-3c3a-994f-4bfaf6d399a7 | -15.6887 | -59.74229 | 2024-10-25 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b481485-6806-3c22-8041-8b909a39e51d | -15.6838 | -59.74123 | 2024-10-25 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c964ca6e-32f0-3baa-943c-af80d3e66497 | -15.68267 | -59.74693 | 2024-10-25 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 266f2d4b-a69e-33ab-8db1-d03cb6f0d612 | -15.6789 | -59.74019 | 2024-10-25 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 558cdf50-29fb-352f-b386-585a34d98fd0 | -15.67824 | -59.73721 | 2024-10-25 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3b83446c-d026-3cc1-a2bc-c6afe1f9a404 | -15.67776 | -59.74588 | 2024-10-25 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| dc0b57fe-a52b-3e77-b494-49aa18b8922c | -15.67715 | -59.74292 | 2024-10-25 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e6d914c3-a93b-3978-88bc-04e591a64d9b | -15.67399 | -59.73915 | 2024-10-25 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 49caddb5-a72b-3889-b873-ea09cb530ca4 | -15.67286 | -59.74483 | 2024-10-25 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 013b99a5-ff1a-31f6-b4a0-ffa7f6dc0086 | -15.67224 | -59.74187 | 2024-10-25 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ce31783-98c4-38b1-b5b4-b87f2e03fdfc | -15.67172 | -59.75053 | 2024-10-25 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b7b88b9-4579-3328-abcb-2846980ec334 | -15.67114 | -59.74759 | 2024-10-25 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 48d131cc-44c5-3015-9d1f-5f845a8436a0 | -15.66944 | -59.76196 | 2024-10-25 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d14fa21f-b338-3eeb-afa9-5268023b605e | -15.66895 | -59.75904 | 2024-10-25 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5845ad48-33ef-37e1-9757-70a92fe22e33 | -15.66795 | -59.7438 | 2024-10-25 04:40:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f495b835-6957-3ff9-ba00-e90f89eacce8 | -15.2915 | -60.39951 | 2024-10-25 04:40:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4989d9c0-d2b7-3fb1-a63b-f0b7d08f3ae5 | -12.05595 | -63.14772 | 2024-10-25 04:40:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 27badffb-894d-3283-ad17-136f43c5aaab | -12.05538 | -63.14465 | 2024-10-25 04:40:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 61437fc0-75f6-3f9e-9228-f595facf9a92 | -12.04949 | -63.14629 | 2024-10-25 04:40:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8f17dd08-fcef-3085-8c3f-9cb04f8e0edf | -12.04892 | -63.14326 | 2024-10-25 04:40:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f61b52c9-3b29-3c4c-9288-5537a1d16c0b | -12.04776 | -63.14877 | 2024-10-25 04:40:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 51f33fdc-ac41-36bb-8443-26008b24064d | -12.4676 | -63.16457 | 2024-10-25 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5174be77-8e48-32d4-8692-a05b7f7bc2d7 | -12.46706 | -63.16473 | 2024-10-25 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 68245496-5d0a-3028-b807-38f7d51a1d9f | -12.46648 | -63.17004 | 2024-10-25 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ad14d95-95d5-3d3a-ae3a-06fdb8069f1d | -12.46591 | -63.17017 | 2024-10-25 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 121755b7-3449-3815-a538-f6543fd6f75c | -12.46478 | -63.24422 | 2024-10-25 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 179f341f-5371-3881-bf52-994f40975f38 | -12.46375 | -63.24409 | 2024-10-25 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb37d110-d26b-336a-9624-c40e12fd011b | -12.46365 | -63.24974 | 2024-10-25 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd51485c-c2fe-38ad-8db4-05cb9e6834e6 | -12.45782 | -63.17953 | 2024-10-25 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8da9ccd8-2b47-3c15-979e-50d452b09fcf | -12.45669 | -63.185 | 2024-10-25 04:40:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71b9da6b-e1ee-317b-8bb4-42f19aec5b87 | -7.86525 | -63.73952 | 2024-10-25 04:40:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7d546aa5-f1a9-3736-8d66-6cb8168ef40a | -18.30456 | -56.167 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| ca574119-492c-332f-bde9-6015a9d1bd1b | -18.3037 | -56.17174 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| c54ac631-d4cf-3c7a-b0a7-dc277796dfe3 | -18.30205 | -56.24555 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 754725a6-f0b5-3c8e-bae7-a3e332065491 | -18.2997 | -56.21535 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| e4cd3d43-b38b-3add-9ca4-0e76dee2d968 | -18.34454 | -56.20446 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| c65ac0b9-0f54-3b64-b58f-b4a4eea752ad | -17.22695 | -56.6789 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 610de24c-0efc-39cc-80d1-dac194e30592 | -17.2259 | -56.67556 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| bd98a7ba-87f9-388c-a5ea-8f68000ef6d0 | -17.22494 | -56.68076 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| eee7fd34-b89f-3995-9345-f52053e74e80 | -17.22301 | -56.67812 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 38a132ea-9b16-3a07-8d48-a539e2502a96 | -17.21608 | -56.67133 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 897eaa61-efa0-36e8-ab2b-c130032cb70c | -17.21215 | -56.67055 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| b5758c22-5e64-3558-9f73-1934702258c2 | -17.21018 | -56.67245 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 8f6d48bd-4eaf-3508-996c-df418bf4df9b | -17.03247 | -55.99462 | 2024-10-25 04:42:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| db61d6b9-8a29-3742-be24-98d53eaa2bb9 | -17.02868 | -55.99389 | 2024-10-25 04:42:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| c660cf66-2ffd-367f-911d-f6aa5cb43c9a | -17.02576 | -55.98836 | 2024-10-25 04:42:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6e2ea0ad-f730-35e1-9f58-91fbffefee7b | -17.02228 | -56.00758 | 2024-10-25 04:42:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 90c8675e-a04f-32f6-99cc-2d533567e41c | -17.01999 | -56.00502 | 2024-10-25 04:42:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 0fd84ee1-62c9-3f42-a751-3468454701f1 | -17.01703 | -55.99947 | 2024-10-25 04:42:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| a8d5c7e7-5680-31a4-91f0-36b84d2f3440 | -17.01619 | -56.00429 | 2024-10-25 04:42:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| bbb8bc76-f4ea-37e3-b47c-8869cb0a141b | -17.01469 | -56.0061 | 2024-10-25 04:42:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 264c767e-abae-3d14-a4eb-78783728ed7e | -17.0124 | -56.00354 | 2024-10-25 04:42:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 801e5fe9-0458-31a7-89e7-10db3f2e8375 | -17.0109 | -56.00537 | 2024-10-25 04:42:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| bcfa8034-5b71-3c81-9062-e54372e1fafb | -17.02955 | -55.98909 | 2024-10-25 04:42:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 23b47092-e386-33ad-bf7c-9db2b824a82a | -17.02695 | -56.0035 | 2024-10-25 04:42:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| dcde13a3-c6ab-37c7-a9ca-ba9af643d606 | -17.02489 | -55.99316 | 2024-10-25 04:42:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 190fd878-d5c4-3594-9fc1-d9f7d55b15a8 | -17.02251 | -55.99059 | 2024-10-25 04:42:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| ff5ef695-fa91-3c9b-a927-e2193e2fc8b4 | -17.01936 | -56.00202 | 2024-10-25 04:42:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| ad9e45b7-8b04-35c2-99ed-c3fc45f7b543 | -17.01849 | -56.00684 | 2024-10-25 04:42:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 9348f3d3-d5c5-3417-af2e-be3302b233da | -17.01557 | -56.00129 | 2024-10-25 04:42:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| b88d391d-d8b7-31c1-85fb-962df240ba7a | -17.01155 | -56.00837 | 2024-10-25 04:42:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 4bfccbd6-7350-38a1-b247-9d98d3e2c077 | -17.92165 | -56.20613 | 2024-10-25 04:42:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| e68739e1-199b-3234-b191-1e8d9f683386 | -17.22599 | -56.6972 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1963eb18-d46e-3ba3-8219-a0c8eaeeeb8c | -17.21411 | -56.67322 | 2024-10-25 04:42:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |


[Clique aqui para ver as próximas entradas](README75.md)
