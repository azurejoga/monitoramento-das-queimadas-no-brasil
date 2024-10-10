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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 59eccc6c-5aba-3bee-8dd0-f65f8543b5ea | -3.89619 | -58.8025 | 2024-10-10 05:36:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 86dbc8d8-6cc2-31f8-a6a7-d66591b56406 | -3.89498 | -59.68546 | 2024-10-10 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1b51bdcf-880a-338f-8c21-21b6525bb963 | -3.89234 | -58.80189 | 2024-10-10 05:36:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5815471c-0d03-347e-92f4-41f26ac06423 | -3.84919 | -59.56992 | 2024-10-10 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8f41eb10-96a8-3ac5-ad27-1eb523d4c89d | -3.61922 | -59.79577 | 2024-10-10 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66e64fe6-4d61-3c2e-8b44-6f47f2278be4 | -3.61681 | -59.7937 | 2024-10-10 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 21593e6b-5418-3f18-a3e3-60c4c6d54054 | -3.61559 | -59.79523 | 2024-10-10 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d3311ff-532d-3e34-9bcd-eed313c00284 | -4.52488 | -59.9028 | 2024-10-10 05:36:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5a04b1c-6942-3db7-a3c2-6a5b08b7e825 | -4.4434 | -59.64964 | 2024-10-10 05:36:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 619d5904-e453-3efa-892e-9aa31613d9a1 | -4.38047 | -59.94331 | 2024-10-10 05:36:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b2833e3-2b52-3f98-b457-6d29bf2ee24e | -4.37747 | -59.93855 | 2024-10-10 05:36:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d8a0813-6cc6-366b-9e13-32da3cb9920b | -4.29754 | -60.01773 | 2024-10-10 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95b8e657-fc3c-3209-b119-3d0c1b5cf1da | -4.29457 | -60.01299 | 2024-10-10 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dab92c35-7c71-31d3-9611-3c0547103e45 | -4.29393 | -60.01718 | 2024-10-10 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92c6cf91-1e18-3058-8c9d-3149eb5fc7a7 | -4.29095 | -60.01243 | 2024-10-10 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 04d06eac-e76d-349a-955a-25f92d9c407a | -4.29032 | -60.01661 | 2024-10-10 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 342c5e8e-30a7-3c1c-9069-598e81f224f3 | -4.28734 | -60.01187 | 2024-10-10 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0cd48d4-e466-3e25-8789-38a56e668d5a | -4.28607 | -60.02024 | 2024-10-10 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c14f371-8886-33f4-b3c3-fc8db4d8ce5c | -4.2695 | -59.88432 | 2024-10-10 05:36:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed56540b-b0d0-38bb-b35c-6c40dcf75860 | -4.26887 | -59.88856 | 2024-10-10 05:36:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d384a5e-cffc-3d33-b24a-1027cc82d94a | -4.26823 | -59.89278 | 2024-10-10 05:36:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 349c47a3-941b-3b89-9704-c3c458320f3d | -4.26586 | -59.88376 | 2024-10-10 05:36:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c17046c-0f98-3f0d-ae86-856a7a5700ea | -4.26523 | -59.88799 | 2024-10-10 05:36:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7250aea-c804-39cc-8fcc-f08efe8500b9 | -4.26096 | -59.89165 | 2024-10-10 05:36:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b64dc21b-9a6e-3fe7-b1d5-9c6c54c7deb3 | -4.25969 | -59.99909 | 2024-10-10 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bc3686c-dce7-3c41-b079-b86f0b9e2023 | -4.25671 | -59.99435 | 2024-10-10 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7fc7b2ce-887f-31a2-b760-92d3d9e68b28 | -4.25608 | -59.99855 | 2024-10-10 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e0c12108-94de-311c-9f50-79a8fbd94bb1 | -4.25309 | -59.9938 | 2024-10-10 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6323bbd3-3239-31ca-9c4f-1187f9f2e70f | -4.25247 | -59.99799 | 2024-10-10 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 38212ead-6091-3175-a0ee-dc5f10025130 | -4.22785 | -59.95724 | 2024-10-10 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 08a87960-1c0c-3ca9-ac14-0acf55420b22 | -4.2276 | -59.8623 | 2024-10-10 05:36:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8be425c-ab53-3451-aa08-9ded02123bad | -4.21185 | -59.98908 | 2024-10-10 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a2c3234b-d6ff-3c5c-b1b2-85ee5501d0fa | -4.2112 | -59.99326 | 2024-10-10 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d92a693-f20a-3689-aefd-8b555e95e9fc | -4.20823 | -59.98851 | 2024-10-10 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e9270d7-34f3-39db-9c55-bd8bf27c25d3 | -4.20759 | -59.99271 | 2024-10-10 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9b4dbc77-c7b0-3d2d-828a-4a2e7cf29416 | -4.20398 | -59.99215 | 2024-10-10 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 317479a0-a216-3b55-8561-e5a203b7d88f | -4.20334 | -59.99635 | 2024-10-10 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 047a8b5d-ecc7-3fde-bd8b-fcff7be4572c | -4.18803 | -59.95118 | 2024-10-10 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cccfca05-23d3-34a5-94aa-bc208cf656f1 | -4.18739 | -59.95537 | 2024-10-10 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d03ec1f-70fb-3e16-932c-ae4c5c2fbf1d | -4.1597 | -59.94255 | 2024-10-10 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 50384b79-b0c9-364f-a2e2-f6d23383df2d | -4.15671 | -59.93778 | 2024-10-10 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e8f3990-e5ac-3b7f-96e7-c40306dd48a7 | -4.15608 | -59.94199 | 2024-10-10 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5265e590-50ef-30a5-ba60-db83ffbc1b63 | -6.38383 | -59.99054 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ada7963c-b282-373b-9352-bbf25088ba14 | -5.33379 | -59.80523 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 95f6a1a5-5531-3d44-9d95-ec27ea6c347b | -5.29556 | -60.10448 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 724b312e-dce2-324e-9a16-0d953994af4d | -5.18017 | -60.28007 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d7dbd54f-023a-3a19-adf6-36d851452a8d | -5.08709 | -60.22505 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d84557c2-ff88-3f90-ab20-d31a6109c1b6 | -5.08348 | -60.22449 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 14ecdcfc-4712-3a97-b51a-f135cfc2d171 | -5.29621 | -60.10024 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2ddc133c-6904-3614-98ba-b96c14fd1b21 | -5.20017 | -60.24483 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6dc0ca6f-4249-376d-8a8b-fc3f4a8f0791 | -5.18439 | -60.27646 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 69f3ed83-0602-367b-9722-4f84a4a6bb97 | -5.18377 | -60.28064 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b187d4c-24ef-3c87-bfa6-9274c4844e9a | -6.80286 | -59.14907 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5a5fccea-5dde-3663-aae0-3d8b0aca37df | -6.80165 | -59.34667 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 987682df-c4a3-38b3-8d2c-0e757f99254e | -6.80093 | -59.35153 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b1250f30-1e5b-30e7-83fd-4b70d054e196 | -6.79047 | -59.31497 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7963847d-b8a2-36ca-ae7c-0987349445a1 | -6.78292 | -60.04665 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 5c9374c0-fc7c-34e0-afe5-67cf629f750f | -6.78226 | -60.05105 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e69b7ecc-b29b-300b-8fd9-5fe0fc6a530c | -6.78198 | -59.31876 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 8c2e3633-19b0-3e48-81a4-bedfd6d3ea4c | -6.78161 | -60.05547 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da1adab6-3c45-3cfc-8824-2015e62edfc6 | -6.78125 | -59.32369 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 6b35751f-5353-3e3c-9687-a1c4ba396355 | -6.77788 | -60.05495 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a904f536-9caa-3794-a6be-e6446207a08c | -6.77547 | -60.04559 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 991e56f7-3ed4-3ba3-a527-7a7f6b823755 | -6.77493 | -59.31268 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a7544dd1-a427-3c28-ac87-64a158adb248 | -6.77351 | -60.05883 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b4ec81a9-f3ee-3713-a108-1a608028243b | -6.7711 | -60.04947 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62ef2b4f-719c-3406-940f-6f07d8bb107c | -6.77045 | -60.05389 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e3c6c8a-72d0-392d-a491-5893f124dc62 | -6.7696 | -59.32197 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.6 |
| ca3c695e-3d66-39fe-b019-6a95450becb4 | -6.76889 | -59.32685 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| cad52c61-6bbb-3439-9932-cbd364fb744c | -6.76673 | -60.0533 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a0718e8-61a8-38a2-9374-04a213c0e503 | -6.76644 | -59.31647 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9b1efbd3-cee6-37a1-a2d2-e729e531ecd3 | -6.75337 | -59.32448 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 5daf62b8-30be-3dd5-94c0-2a658f5db113 | -6.75267 | -59.32933 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 50c750fd-f12f-3b95-8301-74528bc614bf | -6.75196 | -59.33423 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 33f06b75-1d67-3a0a-8039-001c1a277688 | -6.74949 | -59.3239 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8420db41-4093-3e46-974e-66a30d0667ba | -6.74193 | -59.66946 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4625d361-aff7-37d5-8e83-632f7e5b6c30 | -6.74133 | -59.29091 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a35750b7-187f-37e4-ba38-6578e5bfcd3e | -6.73912 | -59.30555 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3042bb8a-d53a-3e9d-a13a-5e797c7b49db | -6.73821 | -59.29216 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f996ecf-8a03-3802-9cf9-e333479874fe | -6.73744 | -59.29037 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11fad0ce-be7a-3faa-949b-0da41ea57a3e | -6.7361 | -59.30682 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cb4a95f8-d869-3229-aee2-7827868ccee2 | -6.7301 | -59.32095 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3188ae8d-f7db-35de-a16a-f01583080fb2 | -6.72913 | -59.31912 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8f4e37db-ae9c-3cb4-94f0-6f002f358f6d | -6.72691 | -59.31552 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b8622083-e654-3b52-ab7b-e004aab99cef | -6.72599 | -59.31368 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d85101e3-c8b8-3a25-9b01-00f78371a431 | -6.72373 | -59.31004 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 89aef8d1-83a2-37a8-96b2-0bc13651cad1 | -6.72043 | -59.29783 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fa5b58e4-cdf5-3e04-8014-b6d4050de605 | -6.71969 | -59.30275 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 57f2beaa-a1a9-3ba4-b013-dbd9b28c8485 | -6.71841 | -60.10664 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e6a6c91f-dde2-366b-89ce-a4276af4ef59 | -6.71775 | -60.11098 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| efbba241-46ff-3f33-a7f9-031ed8fe0a47 | -6.71682 | -60.10928 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 89a6d3a6-b981-3487-a46c-7d978b1c5611 | -6.70726 | -59.46416 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4a3d0d9-f781-349f-967a-55c71d5c8cd3 | -6.67583 | -59.46413 | 2024-10-10 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25bbd194-d6f5-32b5-b019-6df0f59b279a | -6.65599 | -59.77765 | 2024-10-10 05:36:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| af605f5b-da44-3609-b32c-b9fd4ab81079 | -6.60319 | -60.00065 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7f3999cd-975d-321a-8a8c-37f5ddce8520 | -6.54981 | -60.00172 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6c02a8b-a60c-3d43-b609-593231d21297 | -6.54915 | -60.00614 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e60a7720-776a-3ad7-a187-0052e3d5bae4 | -6.54718 | -60.0195 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 14317081-efdd-3440-b9e9-9feba63859af | -6.54479 | -60.01001 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| da823910-b535-30a6-889f-b767675b8625 | -6.52953 | -60.06213 | 2024-10-10 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README131.md)
