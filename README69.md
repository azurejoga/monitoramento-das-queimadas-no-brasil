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
| 313ffc57-eb90-35b1-bdb6-f924f6c898a7 | -17.06231 | -56.73801 | 2024-09-30 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 18733e55-35e7-3d7e-94fe-9b81c57a5b52 | -17.06178 | -56.74225 | 2024-09-30 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ffe02588-5f2e-39ae-8d23-0d444f3d649e | -17.06126 | -56.74649 | 2024-09-30 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| b910209f-f5c5-3669-a9fb-3733ce0d3c4a | -17.06074 | -56.75074 | 2024-09-30 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| c4bd7bb9-7257-3c5a-bfdf-d46413b6f032 | -17.05905 | -56.72887 | 2024-09-30 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| e16176b8-c655-3701-b51d-c9178d2f8836 | -17.05853 | -56.73314 | 2024-09-30 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| cd388448-f283-3076-afd1-a877becdc40c | -17.058 | -56.7374 | 2024-09-30 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 187e1177-f9e8-3478-8951-f4581789d0f5 | -17.05748 | -56.74164 | 2024-09-30 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a2d0a3c0-8781-3f78-bb8a-5283386a1f73 | -17.05696 | -56.74587 | 2024-09-30 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 529b56d9-b188-3b6b-b64c-bc814e03745e | -17.05643 | -56.75013 | 2024-09-30 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| a163de91-e046-309d-8de8-b550bd632756 | -17.0559 | -56.75438 | 2024-09-30 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 26a1c8fb-155a-34b9-96a3-36ed1310a1f9 | -17.05474 | -56.72826 | 2024-09-30 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 107dff43-7c6f-3726-8560-98ab2d854b55 | -17.05369 | -56.73679 | 2024-09-30 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| d154bfe8-5fc4-3749-b978-f314ea0debdf | -17.05317 | -56.74103 | 2024-09-30 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 3c7d2938-16df-33e7-87a8-cac17ba30800 | -17.05264 | -56.74527 | 2024-09-30 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 87daa563-3e0a-362d-a18f-04f7e6aa0d1f | -17.05212 | -56.74952 | 2024-09-30 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| fd13600e-86dc-30dd-b75f-c3563b3b653a | -17.0516 | -56.75376 | 2024-09-30 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.7 |
| 3c6aaa02-d603-30f5-931d-815fda145340 | -17.05043 | -56.72766 | 2024-09-30 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 195c6390-980c-3e29-8031-8bf57e994b98 | -17.04938 | -56.73619 | 2024-09-30 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 85c782ea-0dd9-38eb-b5ed-a80f143de4bf | -17.04886 | -56.74043 | 2024-09-30 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| f0e802de-01fb-3745-a999-87995aac01c0 | -17.04834 | -56.74467 | 2024-09-30 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 34753137-040e-3fd2-bc55-73eb36c6c9c5 | -17.04611 | -56.72705 | 2024-09-30 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 98ce9eab-73c0-385c-b1d2-924dfb50815d | -17.04559 | -56.73132 | 2024-09-30 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 9f0f3274-0c50-3d38-a266-66a2938e8cd2 | -17.04507 | -56.73558 | 2024-09-30 05:25:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 32d468f3-09ec-3d49-bc75-01ef4bbe7b1c | -16.82207 | -57.55782 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2852eba8-4bfb-34cb-bf6d-9c15a3835927 | -16.81942 | -57.54597 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| e841d344-c9b8-3aeb-9006-8eef738c6ef1 | -16.80533 | -57.56025 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 802317d2-f22a-3689-8b6b-1186fa5ebdf9 | -16.78978 | -57.48903 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 37729f11-3115-33f7-a693-3ae32554562d | -16.78569 | -57.48844 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 1a044b9f-e420-33dc-bb7b-1716fc578f3c | -16.74841 | -57.48692 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| d0769155-52c8-3644-b466-4394d8c2c00c | -16.74432 | -57.48633 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| c300a51e-87a7-39da-ad60-51af6c2f69b3 | -16.73302 | -57.47699 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| dbd06663-9d16-3835-becb-c95e9a03bb70 | -16.71789 | -57.46836 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 2707dbfb-db6b-34e1-afc8-39ffb4f96988 | -16.71739 | -57.47214 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 60ae1be1-c341-3d45-a4d6-d3c7cb230288 | -16.71714 | -57.47084 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 12491a9f-580b-312b-ad63-b4f024a82d34 | -16.71343 | -57.53291 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| 68fdc8b0-03ed-384b-8a9a-927468f180e6 | -16.7133 | -57.47155 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 8fa0c63e-62c7-3877-b0cd-d3ebb9a79b61 | -16.71313 | -57.53548 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |
| 6a8de874-fb31-34b6-93ed-cbe357a2e540 | -16.71293 | -57.53665 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| e390dfa2-26a7-37bd-8cb6-341c17248d64 | -16.71114 | -57.4249 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.2 |
| 303c0d10-0b54-38c5-bbd8-8eb852492879 | -16.71063 | -57.42871 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.1 |
| 332a9c50-930c-3553-b4d6-3486f52e89f5 | -16.70986 | -57.52858 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| a0f0d092-5b94-3d3e-8361-34a54aab1836 | -16.70953 | -57.53115 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.9 |
| ad05907b-c22d-3b65-8729-1012191da5d4 | -16.70936 | -57.53233 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.9 |
| 172d8ea0-674e-3081-bb0e-16aaabe70dab | -16.70921 | -57.47097 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 5cc99462-74e2-3ab8-902e-0e78f7ca63a5 | -16.70654 | -57.42812 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.1 |
| 4a3e533b-816d-3a84-870a-fee82f326cde | -16.70579 | -57.528 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| b6bd170b-f759-3b93-b094-0c7e0cfbf1ae | -16.69784 | -57.43074 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2743e79f-fbfc-3aa5-9346-32edd9e81340 | -16.69374 | -57.43015 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e2441c7d-f16e-3bbc-b40a-cfdc3e6510ed | -16.67847 | -57.45113 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| b6f5a173-3a28-344d-96ba-f54ae73bd6e1 | -16.67798 | -57.45492 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| ffca9ff5-a7a6-3e6e-a474-2cac3f8640ee | -16.67389 | -57.45432 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| ef9938a8-8f47-3dab-a77a-85cf52991f7f | -16.6734 | -57.45811 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 4665145a-78fb-37c5-ab83-b585f0bbac59 | -16.8235 | -57.48617 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 814d9358-bd49-33f7-bab8-ad0da6e7321d | -16.7448 | -57.48254 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 81e924be-66fd-36e1-b91c-20ffbcaed823 | -16.72845 | -57.48018 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8d26eff7-65ec-3a9e-827e-5735b7e35a19 | -16.71761 | -57.46705 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 5036eb6e-da13-3b13-a22a-afc4e9023069 | -16.70704 | -57.42432 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.2 |
| f3ccdcbd-9779-3ee4-9ee7-8433b66747b2 | -16.68815 | -57.44096 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 77d79a51-c7c1-311c-bf6f-e4ec967f1622 | -16.68765 | -57.44474 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| d74ac27b-6a3e-3b74-8cb6-72643588354c | -16.68306 | -57.44793 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| dabf6eca-6f70-337f-b0d0-8377a2c89ad2 | -16.68257 | -57.45172 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 93d03666-1850-3273-9192-bf55334b674b | -16.67897 | -57.44734 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 79f0efa5-f5dd-3133-ac24-991230ba38ab | -16.67438 | -57.45054 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| d9b71b13-63e9-3039-86de-abc9f4240f45 | -16.6698 | -57.45374 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 61e29516-5a95-3923-9e5c-3ec85e8cf868 | -16.66931 | -57.45752 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 4e7bebdd-464e-39fe-a389-004aacad6a58 | -16.6508 | -57.43941 | 2024-09-30 05:25:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 643757f8-1133-3f9f-b9ec-e2c24100edb5 | -12.41083 | -57.79014 | 2024-09-30 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9c96a4f-ff03-3113-9f7a-b7e2a53d4381 | -12.40705 | -57.78954 | 2024-09-30 05:25:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d38331ea-a62f-33cc-9f7b-11ca730a8dc4 | -13.79292 | -58.94313 | 2024-09-30 05:25:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b87b449a-d756-3398-bf9c-043e0c871c7d | -13.7893 | -58.94264 | 2024-09-30 05:25:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 77b14d9e-35ba-3b97-be45-da41cdc44aa5 | -14.90634 | -57.96244 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 80ec3142-866d-3d79-8a32-bac638679020 | -14.90495 | -57.97247 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c07937e9-064a-36ab-af31-228d831d05ae | -14.89126 | -57.98593 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d728325e-f771-39b6-a762-5c76a126d08c | -14.88981 | -57.99648 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b54680cd-5c05-32ee-9d40-8b142e1f290b | -14.88741 | -57.98528 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8ce71a1b-2c59-31d9-9ee7-0b6ae550097d | -14.8867 | -57.99046 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7074e570-d328-34db-87be-a5c31c920986 | -14.88597 | -57.99572 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c941cd75-05c3-366f-8ffd-6174c8800315 | -14.77752 | -58.22266 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8bdd5fea-c85f-37fd-8a97-e69809b5bf37 | -14.77439 | -58.21731 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1f9bb9a4-c2a3-3560-9eb0-acafd480f793 | -14.77372 | -58.22208 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41b793f4-de5c-3b75-aa6d-51d6b257786e | -14.77059 | -58.21674 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8444c0ff-b6f5-3a53-ac79-8fb0b9b48713 | -14.76992 | -58.22151 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 038d3784-9304-3a3a-8452-22b3482fed82 | -14.76924 | -58.22631 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4492436e-0ded-306c-b201-f0635e3b826f | -14.93737 | -57.94894 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4450391f-ae62-3ed6-83fe-0d6845467176 | -14.93552 | -57.95153 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a7c8015-adcb-30e4-ac1d-e01e3837d16e | -14.93283 | -57.95332 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07d4a27c-a5f3-3242-ba90-ffd18a588904 | -14.93165 | -57.95099 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26aa2632-56e4-3ec4-bd86-5a9fbfbc6b12 | -14.93096 | -57.95592 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e2869992-cd03-36bd-a88f-72d4a81a1a5c | -14.92896 | -57.95277 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 490e150c-5e0e-3ab8-85d9-34a069e9dd88 | -14.9283 | -57.95771 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ba83d81-132c-38ce-b834-bc13c14c40cf | -14.92708 | -57.95535 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c9060f2f-0fa6-3b5a-a371-364cf7ee0133 | -14.90565 | -57.96746 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| c3089251-89da-31ef-8202-364d498a587e | -14.90178 | -57.9669 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 669ec9b6-adb1-35ee-9faf-1dd6e6078aa4 | -14.89054 | -57.99116 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b450c947-743a-34b4-892b-e68c91bc101b | -14.88908 | -58.00178 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 03f17744-ee12-3a1b-81a5-834f5c704be5 | -14.88836 | -58.00702 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 498b0c29-e932-35c4-b363-b904de43a67e | -14.88525 | -58.00099 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8a1483cf-c1dc-3beb-909b-46e279cbe60d | -14.88454 | -58.00615 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 77212fba-abd6-386c-90a7-2dd39e27794f | -14.77736 | -58.21944 | 2024-09-30 05:25:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README70.md)
