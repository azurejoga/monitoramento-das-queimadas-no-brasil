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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd625600-c44b-3967-a635-8945d1c2f919 | -1.43365 | -47.40966 | 2024-10-16 05:23:00 | NOAA-21 | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 81178590-00e4-3d64-9b17-dac106842628 | -3.21932 | -48.92171 | 2024-10-16 05:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| de4bb8fa-6445-3113-854e-bcc9d701d317 | -3.21869 | -48.92607 | 2024-10-16 05:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 76a7f590-7c36-3c3c-917c-cf6ea0f98454 | -3.21682 | -48.9188 | 2024-10-16 05:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 9fea737d-81a3-311f-be74-1668c5f1b588 | -3.21616 | -48.9232 | 2024-10-16 05:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6c138c9f-3e31-396f-940d-113c8e42dbd0 | -3.21335 | -48.92067 | 2024-10-16 05:23:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4c297252-2578-3b6f-be1d-f370f9468f5f | -2.96907 | -48.00635 | 2024-10-16 05:23:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 992be8e2-83f9-3c42-aea3-128569b08c0b | -2.96276 | -48.00531 | 2024-10-16 05:23:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 60347012-4949-34e3-891f-04a7a6fbff90 | -2.93896 | -47.99119 | 2024-10-16 05:23:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76685a47-ec11-3dad-b971-7899561522cc | -2.46082 | -48.34884 | 2024-10-16 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b6beba45-184d-3ec2-84ea-101d395d257e | -2.46081 | -48.34928 | 2024-10-16 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f6f4324d-f63d-3945-af8a-938b896c8327 | -2.46009 | -48.35355 | 2024-10-16 05:23:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 76acdeb4-1ed0-36a8-9f38-1dfa768c66af | -2.38493 | -47.58996 | 2024-10-16 05:23:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3f3ec9a0-8f82-3042-a81e-8d6d83a01284 | -4.81451 | -49.38979 | 2024-10-16 05:23:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 86b823c0-c5fb-39d8-8bb2-0bcfa3e72e0f | -4.36044 | -48.48846 | 2024-10-16 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a17e930c-b22f-35a5-ae36-4992dd49c103 | -4.3597 | -48.49355 | 2024-10-16 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fdcc3fea-345f-30ab-81db-ad920e51e3fe | -4.35787 | -48.49289 | 2024-10-16 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 953eb672-0bbc-3e32-a808-352357f3a2fc | -4.35344 | -48.4927 | 2024-10-16 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| cd9d5ca3-7bdb-3de8-b31f-5d648bfc7fc4 | -4.32635 | -48.62852 | 2024-10-16 05:23:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9b2ae2e2-a392-3485-a197-053e39400527 | -8.75348 | -49.77716 | 2024-10-16 05:23:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c673e15-8633-33fd-9070-7015d5696df7 | -8.75321 | -49.77644 | 2024-10-16 05:23:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20f30ef9-97b1-32fc-928d-b7ee9d2f5939 | -8.75289 | -49.7819 | 2024-10-16 05:23:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c986966-a903-3f33-b098-ef14f745a249 | -8.75259 | -49.78116 | 2024-10-16 05:23:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3ae94ab1-90b5-3573-b088-a8b7d1da54be | -10.83569 | -49.2451 | 2024-10-16 05:23:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2fefb247-5177-399e-a79e-8546e052b76a | -10.83508 | -49.24631 | 2024-10-16 05:23:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cb7e98d1-09d6-30b8-aec4-313f8fef9f4d | -10.8298 | -49.23898 | 2024-10-16 05:23:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5fa1370a-3ce1-3f55-90f6-131545b2a449 | -10.82923 | -49.24019 | 2024-10-16 05:23:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| fdf1690e-1b74-315c-bf41-0b9ee610ba7c | -10.82917 | -49.24447 | 2024-10-16 05:23:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a56cdc5d-67f9-3c57-955c-ab1b753995fa | -10.82857 | -49.24567 | 2024-10-16 05:23:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d24c0315-3cbd-3af7-81e1-5b80db0a8bfa | -10.82855 | -49.24993 | 2024-10-16 05:23:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 0f611cde-5121-3188-94e9-fa9e5fb36eef | -10.82791 | -49.25109 | 2024-10-16 05:23:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cd36915f-91a1-34bb-8f30-9c40c4929702 | -10.8227 | -49.24345 | 2024-10-16 05:23:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ba579956-ac04-3d52-b70c-ac2959de80ab | -10.8221 | -49.24464 | 2024-10-16 05:23:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 815650fe-2d3f-35f5-8dc1-37139ca1f217 | -10.82209 | -49.24884 | 2024-10-16 05:23:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 30b87bc7-bfd9-300d-9612-bfff5238c1ee | -0.77124 | -48.69603 | 2024-10-16 05:23:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41bc88df-3de9-3907-bf8d-87e3a97c9d2c | -0.77058 | -48.70023 | 2024-10-16 05:23:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fecfc758-f027-34b3-8e9e-8d0da26dd690 | -0.76993 | -48.70443 | 2024-10-16 05:23:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8cda3d5-6bab-31d6-9ed4-ce0bc37f2969 | -0.76927 | -48.70862 | 2024-10-16 05:23:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83370fff-215e-3c02-a259-7182248e619b | -1.14265 | -49.18707 | 2024-10-16 05:23:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 41511bd9-f105-3132-98d3-e19315349282 | -1.14205 | -49.19105 | 2024-10-16 05:23:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4df3c99-2653-3348-af43-f23654a1dd8b | -1.14049 | -49.18917 | 2024-10-16 05:23:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7fd3735b-9ba0-3617-acb2-67f6f98f3f9a | -0.86429 | -48.70833 | 2024-10-16 05:23:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5721395-da12-30af-a161-0ee222756585 | -0.86364 | -48.7125 | 2024-10-16 05:23:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9067f024-fab8-362d-ba34-873dc1aec00e | -2.43744 | -50.23296 | 2024-10-16 05:23:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e88c5893-1a03-3ceb-9ecf-03eabf2a6638 | -0.86298 | -48.71669 | 2024-10-16 05:23:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9911f9ee-5af5-3023-b6f2-f5f43229ce44 | -3.44613 | -49.74004 | 2024-10-16 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd58afa3-33f8-3939-9c50-f97fbe437dd6 | -3.44044 | -49.73916 | 2024-10-16 05:23:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c58f00db-1558-3f73-8e2a-c1f82736157f | -2.97051 | -49.29128 | 2024-10-16 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 23046686-90c8-3c4d-96b7-8f8516ae55a7 | -2.62796 | -49.2761 | 2024-10-16 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64d95209-b55f-36af-9bac-071921f037cb | -2.62157 | -49.27911 | 2024-10-16 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33d05b66-b648-3875-8e21-25122ee8077a | -2.61472 | -49.08659 | 2024-10-16 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 01f9e41c-0248-33db-8465-5dbdaa3d6afc | -2.61408 | -49.09084 | 2024-10-16 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 6b34ead6-df6b-357a-a83a-731f68950c49 | -2.60446 | -49.1151 | 2024-10-16 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f98a077e-818e-35ac-afd0-8418bb3b2889 | -2.59861 | -49.11415 | 2024-10-16 05:23:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 33503bc7-b460-30d2-a278-29faa624d56a | -2.28505 | -49.58722 | 2024-10-16 05:23:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1ed8536f-81a2-3f83-b0e4-db1b4e06cf7e | -2.28448 | -49.59109 | 2024-10-16 05:23:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2c50a0b7-7c74-3db9-8661-ac4173a2b29e | -2.2794 | -49.58626 | 2024-10-16 05:23:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 4220a676-8087-3223-ad85-f2503c9a6d84 | -2.27883 | -49.59013 | 2024-10-16 05:23:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9ab2c13d-e854-3c38-b44d-7fddb58cb107 | -2.276 | -49.58799 | 2024-10-16 05:23:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d7b3cd2a-fdd9-3bc9-8e63-1a580bf80462 | -2.27541 | -49.59185 | 2024-10-16 05:23:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3f36ba19-30e5-32fd-8ecd-1d396f51957d | -2.27317 | -49.58929 | 2024-10-16 05:23:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c2eb1979-0257-3d03-8998-c845171d5ed6 | -3.19298 | -50.31653 | 2024-10-16 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f1dd50f-c08d-38cc-a68e-e8feb10c602c | -3.17056 | -50.46703 | 2024-10-16 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e83bfc0-bfd3-307d-a48d-089b814825a9 | -2.43638 | -50.24002 | 2024-10-16 05:23:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 637dff53-5c0a-3e5b-a08e-f2c7a8c183f3 | -3.23585 | -50.18007 | 2024-10-16 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6580356-a8ea-3e33-93f1-34e7aa190f1d | -3.2353 | -50.18368 | 2024-10-16 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f467496b-fde4-3d63-90b6-8ac5cb53c44a | -3.17107 | -50.46355 | 2024-10-16 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af2c6e9f-417b-377e-a667-ef7b7623dc45 | -3.07315 | -50.36381 | 2024-10-16 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| d2bd0c33-c96f-3df1-8101-4b211d3f881c | -3.07263 | -50.36732 | 2024-10-16 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| fc39f9f9-181a-3e6f-9534-eb553ee47d51 | -3.07211 | -50.37083 | 2024-10-16 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 5bd2f796-a224-3cee-af4f-c280f18a4a6e | -3.06773 | -50.3629 | 2024-10-16 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 12360d4b-b010-3cab-b667-772b1d2951f1 | -3.0672 | -50.36643 | 2024-10-16 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c52d8a03-0e2c-377f-a312-59848938ba1c | -2.42847 | -50.18119 | 2024-10-16 05:23:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a7b3bdd-58ac-3046-a5b2-f3162044aa09 | -2.40436 | -50.30611 | 2024-10-16 05:23:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| da6dba8c-b102-3dc7-9b27-82daa8f4b183 | -2.39896 | -50.30526 | 2024-10-16 05:23:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e25b26e-f449-39f9-b83c-b37be2abffe8 | -4.39422 | -49.67486 | 2024-10-16 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 32f2c09a-4545-3448-aaa8-9c87ede2088a | -4.39378 | -49.67577 | 2024-10-16 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b51eb4da-29bd-380a-906d-523f2712428b | -4.39365 | -49.67892 | 2024-10-16 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 73c17469-5c81-3a7e-b05f-702a9fcf5ab2 | -4.39319 | -49.67982 | 2024-10-16 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e2dfbaac-fc7f-3f4c-acc3-a3d054e53361 | -3.93567 | -49.95556 | 2024-10-16 05:23:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e85b3c4-e29a-3b40-87c0-15673ed8af59 | -3.93509 | -49.95941 | 2024-10-16 05:23:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc12d463-5b40-3ec7-aceb-b1ebb8236c1f | -3.98764 | -50.71139 | 2024-10-16 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1ffc7c4-18e8-3860-b7d0-f2b887f3f281 | -3.98226 | -50.71054 | 2024-10-16 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a890db37-825a-3336-9a9f-e50f0017c59f | -3.98176 | -50.71394 | 2024-10-16 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32634ec2-ae27-3543-9d1f-a05c3dcf6e1a | -3.57434 | -50.5652 | 2024-10-16 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4bfc06e6-ddd6-3dc6-a0ec-250f6a4327f9 | -3.98127 | -50.71733 | 2024-10-16 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49e8b6ba-2dc2-3400-b2df-91d411ca94fe | -3.97688 | -50.70971 | 2024-10-16 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d991f1e5-f3e8-35c7-85ab-1fa8db99d26d | -3.97638 | -50.7131 | 2024-10-16 05:23:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 72a917db-0b72-3051-b4d1-ca4783bf16bb | -3.58413 | -50.5737 | 2024-10-16 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c3b9a7a9-a17f-3135-adab-4591fc4b4f18 | -3.58361 | -50.57721 | 2024-10-16 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1e1a5dcf-f6d7-3d1b-af3f-d1bd04135175 | -3.57975 | -50.56595 | 2024-10-16 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 938f2eeb-4e54-3536-ae3b-bbff744cfce6 | -3.57924 | -50.56942 | 2024-10-16 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 86c64ba7-08a3-362b-a52f-6917db42462d | -3.57873 | -50.57291 | 2024-10-16 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 745c7660-24c0-3773-b092-c7c3ad14d3f8 | -3.57821 | -50.57641 | 2024-10-16 05:23:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 27a6da87-09ba-3fe1-871f-bb039a570ee7 | 2.28382 | -50.85437 | 2024-10-16 05:23:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aef028bc-7b03-3440-b168-78721e9e6a6e | -2.15432 | -50.89656 | 2024-10-16 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f7c1842-6baf-3709-a210-5ba8925756ff | -2.2443 | -50.45201 | 2024-10-16 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0918afe9-f0f9-3004-a88b-a8b5e5f3db3a | -2.24259 | -50.45073 | 2024-10-16 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eecc4fe0-18e1-3d6e-aabb-86a08a6a5886 | -2.2421 | -50.4541 | 2024-10-16 05:23:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f7f3d564-2a02-30b8-b643-b0e59d15f9cf | -3.61643 | -51.38248 | 2024-10-16 05:23:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README57.md)
