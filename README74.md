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
| 96aa91be-2894-3ac6-aa25-e5c47824dacd | -3.03337 | -50.42252 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 11d6a8ac-9985-39a9-be07-b6567a913458 | -3.03174 | -50.40719 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 19ec4228-66c3-31e0-b508-4d3830d97342 | -3.03097 | -50.4121 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75cf9bac-61ef-3b14-84c6-528410d4f65e | -3.0302 | -50.41705 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2dc3059e-656b-3ac0-97f4-d892814f88e8 | -3.02944 | -50.42197 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 827a6264-2c3f-3259-9fd7-5fb72908a97a | -3.02781 | -50.4066 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27a37763-87ab-334b-b16c-489ed6423dd2 | -3.02705 | -50.41152 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9fbb4b9-5002-3319-b029-ae31b9f072bc | -3.02628 | -50.41647 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ba5d51f-0303-33aa-be67-c823e001c7a3 | -3.02313 | -50.41095 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 87bcc41d-1abf-3d7d-ab56-47e7c2fd0765 | -3.02236 | -50.41587 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6e2f4a42-c588-32f7-a6b5-801ea06d6a7a | -3.01561 | -50.48523 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b225f5b9-9362-307c-9ad0-914cc457e009 | -3.0117 | -50.48464 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d12bc908-98d4-3a4f-93c3-02609975e299 | -3.01095 | -50.48952 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63ab70c1-1c7f-30ed-b8a7-264cce501ecc | -3.01019 | -50.49439 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4e35e239-cfa2-3eb5-bc39-392f70672d33 | -3.0078 | -50.48404 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad41d3c5-a028-3e7a-825d-c458431cfd28 | -3.00704 | -50.48894 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9351541e-7230-36d2-b374-2ab8aedd222f | -3.00629 | -50.49381 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7883edeb-cea0-329e-a55c-684b5b27f245 | -3.00314 | -50.48835 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a903e7f-a2fd-345e-88c1-b81755f3dab1 | -2.99924 | -50.48775 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a15e2fc-ea62-3bf0-aa93-a518eeef97f7 | -2.98053 | -50.47962 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| faa2d1a1-ca3a-3780-bd6f-44db2fe5cb65 | -2.97738 | -50.47413 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cf92e4fc-b04e-3c60-b856-4e306d66892a | -2.97663 | -50.47901 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 970fbfd9-70f8-3b0c-bc01-556e98989193 | -2.96451 | -50.42725 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2da5162f-b5ab-3d31-bb88-b636a54f755a | -2.9606 | -50.42664 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b62c4cb1-85f6-367e-8149-bd795ca3f69d | -2.95743 | -50.4211 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e88249d3-8af5-3e87-971e-06c35122f052 | -2.91892 | -50.28105 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86f69f06-66b9-36d0-b081-d0b5594cf200 | -2.91421 | -50.28544 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e18f5c7-cd82-387f-a1f4-9404493e624d | -2.81409 | -50.46979 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e690476-fb88-3482-8d55-e56f403c8f6b | -2.81371 | -50.47226 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d7a6e9f-68ff-31ef-97bd-4b339aa1915f | -2.6025 | -50.02427 | 2024-10-29 05:01:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8bd6cfa8-87a1-3340-877c-a14a2247e0a3 | -2.60172 | -50.02938 | 2024-10-29 05:01:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29272c9d-6571-3108-a0d1-f8f83f183782 | -2.47913 | -50.28251 | 2024-10-29 05:01:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 39d2bc0a-e201-30a3-80ff-5a01a7efd96d | -2.47445 | -50.28685 | 2024-10-29 05:01:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 06e71d96-89ac-33b1-a9c3-eccc2818caa4 | -2.45875 | -50.41465 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07dbfb04-34e6-3339-ae97-7b552f73bb8e | -2.40616 | -50.41884 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ff3d1b0-ddfe-3d0b-889c-72d1c0a60890 | -2.97346 | -50.47362 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9831755b-a8e3-380a-b0f4-a3d804228eb6 | -2.97272 | -50.47846 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 77c01374-80d6-3c8d-bd99-d72026ae5c73 | -2.95668 | -50.42603 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 822e0f30-8293-37f6-840f-213ffc002878 | -2.91969 | -50.27607 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffb44a9e-a822-35df-8c4b-47d0e776468e | -2.91497 | -50.28047 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48b83ba6-5b6c-3f29-a255-89d5800f6b1e | -2.91344 | -50.29042 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d3c8000b-4fec-303d-ae85-7183bac3806d | -2.91026 | -50.28486 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9641733-8a0f-361d-baa5-8b28f18b873b | -2.88638 | -49.7662 | 2024-10-29 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdb1338c-2bdf-3c35-b859-a7497885cd70 | -2.88014 | -49.24296 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e56f26e0-e4cd-3886-860d-af6f4eac41b8 | -2.87336 | -49.14598 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a8605477-c9f0-3960-814a-378052e4be37 | -2.87169 | -49.24166 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5bd9a340-f760-3581-80c9-153f7cd3cc65 | -2.86325 | -49.24035 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6fb53929-1c78-3df7-8d53-18da3dda5009 | -2.83369 | -49.23582 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| acd9e4b5-f1d4-30a4-904e-d5ae9a54cacf | -2.83005 | -49.23129 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 6df4aa67-060c-34d2-9267-af486d5f9ab1 | -2.82947 | -49.23517 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 4ae72744-8308-3962-91a9-21c939a65733 | -2.82888 | -49.23906 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 5d49e350-7654-328b-b8fa-09fad1a1ab17 | -2.8283 | -49.24294 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 12aa2c9f-03b7-3f03-abca-fb26a9873a65 | -2.82583 | -49.23066 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| dd821bf3-6cb9-318c-8220-195c0bfad21f | -2.82466 | -49.23841 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 67057159-9ba7-302c-b61e-a27b96974ed4 | -2.82407 | -49.2423 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 28d19677-3401-3e1d-a15e-529b5461650c | -2.82102 | -49.2339 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a8e4e96d-ad46-3915-a0d2-5ffc136403e4 | -2.82044 | -49.23777 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 35adb325-6de5-336c-9e11-8ea2e24cdfa7 | -2.81855 | -49.22153 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b3b48859-e8c4-32d6-826c-183be55a3395 | -2.81797 | -49.22545 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e9274163-c5bb-3722-ae59-b5b5c3fccefa | -2.81433 | -49.22089 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4a640632-ad63-3621-9fb8-b63e87960c1a | -2.81374 | -49.22482 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 50d2ed59-4714-3995-abb1-57e007ded06d | -2.81334 | -50.47461 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 918dc9d3-0b2e-354f-a225-ee535e88875b | -2.81068 | -49.21637 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ce5cc706-504d-3a6b-8094-10df7b13532b | -2.80893 | -49.22808 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 88bff710-96d1-39b8-a3d9-0b6ab02b1aa6 | -2.80587 | -49.21964 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a05cfcb-f7cd-3766-bcfd-5ad43e8fcb0f | -2.80529 | -49.22355 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9c12de5-2b55-3419-b80b-4ed57f769c9b | -2.79672 | -49.22746 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a98cd3b-5ea6-3eaa-ac0e-6c8a8aa0a33e | -2.78111 | -49.32734 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 21c0f295-9b40-32ef-9a3c-3359c448c412 | -2.77519 | -49.36521 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ceac393f-622d-3436-acf3-431e4b72c5ef | -2.77101 | -49.36458 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2af26903-cada-3570-b2d9-192f714123ab | -2.74621 | -50.44447 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f9aaf89-495c-3d26-820f-e6ee5c34316b | -2.71123 | -49.05508 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1fd675ef-96d7-3cf1-8634-8c41f726dbc1 | -2.71023 | -49.05367 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4fbdf65-80c6-31ab-aa7e-4913f58cf572 | -2.70696 | -49.05446 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1366c6ae-85af-3eb4-93c3-260f65c88449 | -2.70563 | -49.31589 | 2024-10-29 05:01:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f57be676-fc9c-3ba7-aa5f-d8e2b5e091f1 | -3.16794 | -50.58711 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6deb3ae7-4507-3dfa-bbe3-a40b689b5144 | -3.60897 | -49.86264 | 2024-10-29 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 762a7c46-0b0a-3063-bfd8-0376be624f90 | -3.60487 | -49.86204 | 2024-10-29 05:01:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2e9cac61-809e-3f84-aacd-30eb9b4bf586 | -3.52646 | -49.24197 | 2024-10-29 05:01:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1e979a1-028a-3da3-b751-e7839d58144e | -3.51229 | -50.47463 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 742d88cb-314f-3535-90cd-5f76cc7b44e8 | -3.49837 | -49.93875 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0173e3cb-b5ff-37f5-a6c4-7277464ed516 | -3.46843 | -50.34864 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3aa09d4c-7d98-3d79-85e1-0f0744bcc279 | -3.46604 | -50.33786 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a4667feb-3be3-33bc-9a88-e948fb32aad0 | -3.46208 | -50.33723 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2fc8e4ae-9cc2-3507-b53e-9a393aff7d57 | -3.44067 | -50.15643 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa0eb871-c9c6-3020-8796-ea26e1cdca4a | -3.43476 | -50.24981 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aa84e284-a553-3885-a670-4301a4b21d00 | -3.43399 | -50.25491 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a2fbfa8b-10ba-39a4-a629-d4f23c8597cd | -3.42976 | -50.20177 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0751fbef-fcbe-3992-9b16-b1f892a162f4 | -3.42489 | -50.34187 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1950abf5-f57a-3a57-8179-3c6daaeeee94 | -3.42093 | -50.34124 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0af50809-1ca7-3c56-bae0-1b0accada849 | -3.36281 | -50.17319 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4c3d3b1a-beda-3494-a93f-a77e0769d309 | -3.36204 | -50.17827 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e554b55-2bdb-3e57-b254-e42f03f83f6a | -3.36106 | -50.15784 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6e8c121f-4df4-314b-a6b0-c64377992dab | -3.35881 | -50.17258 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ebc9001-bbc2-3f36-91b5-8a2b5ada563d | -3.35706 | -50.15722 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0d6a1e91-b227-3593-82e8-cbfdbbd21b09 | -3.35639 | -50.16161 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3052c24e-c9eb-33f8-a484-39f9f68aa6d3 | -3.35306 | -50.1566 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47a5fb9f-791c-3660-b712-b94a57392202 | -3.33127 | -49.92081 | 2024-10-29 05:01:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a66b2a26-e7d7-3870-b3d7-c3483a388cf1 | -3.32776 | -49.91664 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb67ab1b-02b4-3ba6-ba4f-4a93ea36e26e | -3.32721 | -49.92021 | 2024-10-29 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README75.md)
