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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb74a90b-ed9f-3571-97d3-1329e77e7046 | -2.30086 | -48.58327 | 2026-09-17 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cc7b187a-64a6-3b56-8757-e8af0c3f2446 | -3.48153 | -54.68402 | 2026-09-17 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57e50614-67a3-313a-ab9d-e48f4d8c5eb5 | -0.91965 | -47.20818 | 2026-09-17 04:38:00 | NOAA-21 | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ba5add11-7e91-3b26-8260-f2e1db65ae1b | -3.48175 | -54.68446 | 2026-09-17 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 129f30e4-100b-380e-8b48-6e87935efca8 | -2.90564 | -50.43157 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cbb8f8a1-3da5-3883-bd83-5cf8abff54f7 | -2.31466 | -55.23415 | 2026-09-17 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04dc9cab-c04e-38cf-9180-4b8d57feafa8 | -3.37299 | -52.79768 | 2026-09-17 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6279ee69-5642-31b2-8105-88e4a0a34cd2 | -2.05168 | -52.08225 | 2026-09-17 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 09c4b3e3-4729-3e1b-9691-f54c02ba1ac1 | -3.81899 | -49.14137 | 2026-09-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ac50f3f9-40c2-36cc-89e6-5a4f33f4238c | -2.82268 | -51.34179 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a24c737d-d2f5-31ec-ab48-cfc46e62fb6c | -2.95582 | -50.3103 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 72b0e56c-2bdd-3e6f-b9a4-f7f96bab54d4 | -1.60585 | -55.56443 | 2026-09-17 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fa36c3b5-e9e1-3e9e-9980-f3dcdf26b190 | -3.88984 | -49.082 | 2026-09-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 513e8733-92c2-31a8-bc0e-4322534a2222 | -3.50505 | -53.20264 | 2026-09-17 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32fdd68b-2ab6-3f3d-aa56-cb123958f2c2 | -2.90196 | -54.18079 | 2026-09-17 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c6003dd7-2711-358f-8cea-e646f2b59ac0 | -2.38018 | -48.22604 | 2026-09-17 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61eb88c2-04c5-344b-b19f-c2aa50120e8f | -2.05564 | -52.08134 | 2026-09-17 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 45b85bb1-a9ac-36c7-bbe9-1a14647b5e96 | -3.71104 | -51.11308 | 2026-09-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38df7544-f0a8-36ef-b4bd-147adfcaa8cc | -2.96987 | -50.33082 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7686a85b-e036-3286-b407-7cfdd957b987 | -2.95751 | -50.32157 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 5918fa9f-bb64-353d-a757-59f04dbec4d5 | -4.55508 | -42.94637 | 2026-09-17 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| c8b130fe-96ed-3c83-ac71-a83c044a54ae | -2.95695 | -50.32516 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 99322687-cb58-3128-a396-88e2a69f1a19 | -2.91194 | -54.17093 | 2026-09-17 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6927869d-6a49-325e-a157-32979578c35f | -2.82414 | -49.23856 | 2026-09-17 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c1fa7d46-28d7-39be-ac51-aed544bba1ed | -4.81444 | -42.89415 | 2026-09-17 04:38:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0daf40e8-8773-325f-a608-878db9c31ea1 | -2.97043 | -50.32724 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6fc3ec9c-1510-3729-aee9-16ed8de483c0 | -2.96594 | -50.33389 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 1715c9d6-1297-3f4b-87be-6074830a018f | -4.54888 | -42.9522 | 2026-09-17 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e4fcfa48-82ba-3471-af13-7f21f1eeb1c3 | -4.35986 | -47.77994 | 2026-09-17 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d2f4e199-74f5-35aa-84d4-997feff8f067 | -3.54707 | -48.18106 | 2026-09-17 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd054cc0-6a83-3ac6-a089-c96886f67be0 | -3.43059 | -51.51313 | 2026-09-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed6dffe7-7080-3806-ac0a-39e0d71db8ee | -2.90954 | -54.17908 | 2026-09-17 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2ce01c92-bb0f-3982-93b2-630e4549664d | -2.80203 | -52.07734 | 2026-09-17 04:38:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| ab8ee189-45e5-33c2-b1a3-0206b85d34fd | -2.49154 | -49.40922 | 2026-09-17 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7aece3e8-24e7-3b7e-aedf-bbcf91a1786e | -2.62615 | -49.11208 | 2026-09-17 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b5ec4338-5116-3090-8256-c55514ed2937 | -3.26882 | -54.25835 | 2026-09-17 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ae7ab0c-ad18-34ff-8672-025910b46eed | -1.78438 | -47.83595 | 2026-09-17 04:38:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a7511023-d4cb-3ead-ae57-7f46174e8353 | -2.89945 | -50.42691 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ee456aac-9a2d-3c1e-a7c7-b700b7eb3b4b | -2.96762 | -50.32314 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8ec50dad-00e1-3067-ac8e-66a8e7cd23ef | -3.7076 | -51.11254 | 2026-09-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d030d500-5a3e-3619-babb-02484628132c | -3.15247 | -49.22675 | 2026-09-17 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6849bc22-ce71-3e87-bf66-34b827658963 | -3.55425 | -48.17861 | 2026-09-17 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c0ea4f2-ea03-3e9d-b5e1-726ccd0a4193 | -2.91639 | -50.40733 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61a63261-315d-3567-b33b-d83c6d6fa461 | -3.37674 | -52.79824 | 2026-09-17 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6dfaa49e-d957-3710-b4a2-a8df58b61282 | -2.89721 | -50.41916 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e800b3fc-94bb-3823-bf1e-fd96fbfdd310 | -2.90849 | -50.41351 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffc4d72d-8475-3d13-8f4a-408f86e0b07e | 0.60472 | -51.95765 | 2026-09-17 04:38:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f6bbb17-3f32-3919-8728-88cf66dd17af | -3.07489 | -51.20192 | 2026-09-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61f71dea-86c8-3216-905b-0c68ff058101 | -3.47626 | -54.69147 | 2026-09-17 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f34514d0-1378-3738-95e0-fb026ec951fd | -3.75928 | -51.13999 | 2026-09-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 72ce96b4-1e9d-309f-b609-9e6b7aa69b57 | -2.8862 | -48.07784 | 2026-09-17 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10177d2a-ba6b-395c-8c45-c3341e66de7b | -2.95302 | -50.30619 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e4c3a3e5-8fcc-3cc7-aba0-c5afcfdfb148 | -2.89268 | -50.42586 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c02a1f18-0d50-3277-ad25-f57369c23525 | -3.48207 | -54.70794 | 2026-09-17 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 47817ce0-01df-30f3-850e-686d62f79c76 | -3.01852 | -51.34303 | 2026-09-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 35ac91c0-8547-3447-b1b9-184e85d863d9 | -1.60969 | -55.5699 | 2026-09-17 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e631acd3-3a4b-3dc2-b821-38bfba784a39 | -3.76332 | -51.13679 | 2026-09-17 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1cc4c1e5-aeb8-3038-9b71-af546706828f | -2.89383 | -50.41864 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7bc74284-e2bf-3b98-a3e5-c541ca448e86 | -1.15226 | -54.16911 | 2026-09-17 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6bb5d81f-a055-3321-8350-29eedd77f143 | -4.18261 | -49.40635 | 2026-09-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e6b89f5-4eb5-326f-9b3a-b7a81b30ebfe | -2.72267 | -47.55466 | 2026-09-17 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35b08a81-7ef4-3b3f-bc04-63a37275c56a | -2.95021 | -50.3021 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 05258dfb-748a-3ed7-953d-d89a5de35414 | -1.03938 | -53.73942 | 2026-09-17 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ea8f8e97-7ea1-385a-a335-04b536ca1667 | -2.32835 | -47.20211 | 2026-09-17 04:38:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| edbd15d6-30dc-3a2d-ae54-dde241d7fdf4 | -2.09834 | -52.04858 | 2026-09-17 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af3b36c2-ae94-3aae-812c-bad3da0599a5 | -3.48595 | -54.68519 | 2026-09-17 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e0645ef-571b-325e-8fef-caac8d71f2c5 | -2.87616 | -51.87561 | 2026-09-17 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b901709-89ef-3f8d-af25-9084c70da2ed | 2.70994 | -60.2942 | 2026-09-17 04:38:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8836ff03-7584-30a7-824f-13e5c2c73b59 | -4.01523 | -49.95465 | 2026-09-17 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71c75439-187c-361f-87ce-2d78a78ce809 | -2.88674 | -48.07437 | 2026-09-17 04:38:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7dbe81ab-0ed7-309c-af14-3d6f91529db5 | -2.95976 | -50.32926 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 86a995ac-e8c5-3bcf-bdca-4a18571c6973 | -3.47368 | -54.70691 | 2026-09-17 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 731aae60-dd4b-3da5-b36d-126e6b535c9d | -2.05534 | -52.08282 | 2026-09-17 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fca1d98e-62bd-3191-b7df-5e50e4f3ae07 | -3.28556 | -50.69496 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fef24dc7-431f-3d39-84d8-2c89a150ca67 | -2.96239 | -52.15651 | 2026-09-17 04:38:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a596b177-7001-337e-8b5b-6bd0f51440d4 | -3.94489 | -49.99024 | 2026-09-17 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 96627a3c-7535-39c7-a14a-acb2f0546375 | -1.61078 | -55.56747 | 2026-09-17 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 51563a8d-bbdb-31e1-82f3-de418f6b6f53 | -1.21773 | -55.64108 | 2026-09-17 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 790ff4f7-b3af-3f9e-b998-575f55b51996 | -4.33987 | -46.61712 | 2026-09-17 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 8fdc9995-0df8-39b3-9c92-916fdd163e3a | -1.03169 | -53.7414 | 2026-09-17 04:38:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a55c9af3-12e1-3f78-9110-04fcad102c94 | -3.04684 | -51.2762 | 2026-09-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5eee2dd1-d05e-3963-b673-622d04ea4bf5 | -2.95919 | -50.33285 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 77b7f5b1-bdc1-3cc9-ab78-35fdeff0b64c | -3.48276 | -54.70442 | 2026-09-17 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a6fd1173-396f-3268-8740-c055d41c5c68 | -3.47562 | -54.69531 | 2026-09-17 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c9491898-c179-3267-9754-ea059a108655 | -2.95638 | -50.32874 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 99fc180a-3bbb-3c80-bc74-f8b10a7f7368 | 1.95403 | -50.94688 | 2026-09-17 04:38:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a979269-143e-35b9-a87e-e31ad9c84c08 | -3.48504 | -54.71684 | 2026-09-17 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 45ad9ebb-2fb4-345b-ae77-bc39a5c4c332 | -2.91297 | -50.429 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f3544af-399c-3470-8b86-a14443f6a24a | -2.87975 | -51.87616 | 2026-09-17 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6ac9e789-4a7f-38b0-ad7c-56be31501872 | -3.84828 | -51.76439 | 2026-09-17 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81bafdab-ca34-31f3-a9fe-88a5d44f91e9 | -1.61154 | -55.56261 | 2026-09-17 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 95306411-b893-3f08-b760-fbe009ae6843 | -4.5832 | -47.16397 | 2026-09-17 04:38:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9544d7bf-4244-3bac-9d81-1cb227f64f1b | -2.91018 | -54.18208 | 2026-09-17 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b7450f98-07b9-3059-95f7-c20e3ca1c996 | -7.19065 | -41.80255 | 2026-09-17 04:40:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 82484faf-b71f-3676-9afa-fec4566c5392 | -7.19479 | -41.80915 | 2026-09-17 04:40:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 3c64e0e0-fcb6-3ff8-89c7-e6efccfe363a | -8.22479 | -61.50468 | 2026-09-17 04:40:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 381cc7c3-2c10-3281-9c4a-d4531692303c | -10.77217 | -46.20364 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 034bb553-8312-30f0-9e89-3754de8c4859 | -7.36959 | -44.48101 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3c100aaf-d9fa-315a-afa8-9b7ac14c897f | -6.62999 | -55.13066 | 2026-09-17 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f66a91a-175a-3c9b-8921-0de13f07ed41 | -10.8345 | -46.15285 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README36.md)
