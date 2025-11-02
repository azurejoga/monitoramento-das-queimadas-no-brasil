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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 014d35be-c79a-3215-a464-d06d43a5db44 | -3.91321 | -50.03164 | 2025-11-02 04:18:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e018d6f2-b198-3166-9f21-dc392bc12507 | -3.08045 | -51.25319 | 2025-11-02 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d9b91903-5943-3e35-accc-ebd4376fd22d | -2.44444 | -49.03129 | 2025-11-02 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aee505d7-fe4f-3ab5-9eee-a6e78809472a | -4.72002 | -45.69208 | 2025-11-02 04:18:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1551bd66-46ad-35dc-ba83-90ac9417f348 | -4.70064 | -45.87882 | 2025-11-02 04:18:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0571a2f-d441-3cf6-9913-e9383ab5d950 | -3.42641 | -50.24221 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 61451729-12b3-3736-9056-44b889f9de58 | -4.66965 | -44.42056 | 2025-11-02 04:18:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 59b04850-c0cd-35b0-b7ff-7fa41691fc0c | -3.13014 | -49.23876 | 2025-11-02 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ad1f1c3-599e-3160-8a66-cdbf69b53641 | -3.50485 | -50.47833 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b12b6098-3188-3694-be32-0ad33992f913 | -3.28883 | -50.20036 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 81edd936-809c-3f57-ba2b-92c8346c989a | -4.64314 | -38.56852 | 2025-11-02 04:18:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 7317476f-0389-36a7-a9d3-b3a85fabca39 | -4.30423 | -45.89537 | 2025-11-02 04:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 95466fd2-fd00-361b-8ffe-df699f40516a | -4.58452 | -44.78556 | 2025-11-02 04:18:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd6c04f3-6c17-3c58-b61a-80767351c847 | -2.72392 | -48.34898 | 2025-11-02 04:18:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f03a74c2-2549-361c-b1a5-64f1bad23832 | -4.32423 | -45.63715 | 2025-11-02 04:18:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fc97aa7c-f4cf-3a48-8451-c7000c88cd78 | -3.55772 | -54.57434 | 2025-11-02 04:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 6ca2bc22-51ad-3a5d-97f7-eb914e48310d | -3.41652 | -44.98376 | 2025-11-02 04:18:00 | NOAA-21 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b59ccc5-3952-31d3-aab4-3284f6edc967 | -3.83749 | -51.31538 | 2025-11-02 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| abd0e608-b41f-373c-985a-b145bfda3f71 | -0.69129 | -52.37177 | 2025-11-02 04:18:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16548a6f-8d17-3250-9995-d2b5716a2aef | -4.13795 | -48.81384 | 2025-11-02 04:18:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 67fc0b0b-c99c-3d55-bea0-1b2ca30a494a | -3.13295 | -49.23619 | 2025-11-02 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2fedca5a-4001-3bd3-a83c-8edd117c585a | -3.41552 | -50.00297 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 220b5bac-730d-36a3-84c5-d33f11d24832 | -3.29324 | -50.20106 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0186bf2d-4c47-3635-a023-83903f454760 | -5.52615 | -41.09067 | 2025-11-02 04:18:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d9b86940-35b1-321d-b63e-e877eed6ff4a | -3.56686 | -51.64457 | 2025-11-02 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4f20f88-b776-3705-b773-da5eb2ab984a | -3.24133 | -50.78826 | 2025-11-02 04:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c7c13e2d-c757-3a3e-bdca-9141342454c4 | -4.14651 | -51.15078 | 2025-11-02 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01eeba61-5002-3681-82d3-db66dc463b74 | -3.60319 | -50.62251 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4f91c5b-c3cb-34aa-aa37-a1cf0bdea191 | -3.75446 | -40.81687 | 2025-11-02 04:18:00 | NOAA-21 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3a9d15c4-cf79-3be0-82d8-5d0c21cc04ea | -4.13432 | -51.13836 | 2025-11-02 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 50a38f13-1009-3d08-bbfe-255a5d9648a0 | -4.66208 | -45.67541 | 2025-11-02 04:18:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 968e45d9-fa35-3101-b6a6-bc7272c6f34a | -14.0155 | -43.4943 | 2025-11-02 04:20:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 76.0 |
| b77ff9fe-f900-30ae-b45f-ebecd0a75e62 | -14.0161 | -43.4703 | 2025-11-02 04:20:00 | GOES-19 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 79.4 |
| d1c07b94-50d0-349e-a6d9-6383744485f0 | -13.3177 | -43.4552 | 2025-11-02 04:20:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| ae4c1e0e-4e07-3d2e-addc-484f88fcdd08 | -7.61625 | -42.29482 | 2025-11-02 04:21:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| de87e99f-5965-31fb-a9ba-046f8ad18bf8 | -7.41252 | -40.07629 | 2025-11-02 04:21:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 79f37370-b6fa-316d-8b90-d36adbbe407d | -6.73318 | -47.43588 | 2025-11-02 04:21:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60b195be-6a3b-3620-8443-d7ca2f15b060 | -10.78145 | -56.81677 | 2025-11-02 04:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fa73e162-d790-35c0-974f-114c72eecda4 | -5.31271 | -44.41661 | 2025-11-02 04:21:00 | NOAA-21 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 48fbc7b6-4e7a-3b42-98be-a5304d5f2197 | -11.87113 | -43.81654 | 2025-11-02 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d699fd4-0979-326f-b8e1-addb3f4a1180 | -7.88773 | -39.10077 | 2025-11-02 04:21:00 | NOAA-21 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 97cc2156-271e-3f83-b96c-dcbdba2701cc | -5.50003 | -44.98058 | 2025-11-02 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1031ca71-4bd5-37a5-934a-ea80f7d45f30 | -11.57186 | -47.07585 | 2025-11-02 04:21:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb13a619-6619-367e-aecc-185f1d49c76f | -5.40479 | -44.9366 | 2025-11-02 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04698b49-924c-38b0-a4f7-e924e3c11ba7 | -9.85034 | -44.15265 | 2025-11-02 04:21:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0f6a866-064e-318e-9eb7-cbae01969874 | -10.73741 | -46.23128 | 2025-11-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12674b08-ce8e-3a0d-8a75-3064d75a4972 | -10.41547 | -44.89996 | 2025-11-02 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| af38bc71-ff2a-3760-9c4d-16c6f12991fc | -10.55367 | -44.90786 | 2025-11-02 04:21:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51f4c05f-4d1f-3cb8-8f29-3f040ed11983 | -6.86609 | -38.71837 | 2025-11-02 04:21:00 | NOAA-21 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 84b43417-bc97-338e-9145-98ee3286cd7b | -9.77952 | -43.85847 | 2025-11-02 04:21:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 20ce5c3e-9521-33c7-8ce3-e5f3642f12e1 | -7.63013 | -43.62329 | 2025-11-02 04:21:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7a00061-f4ec-329e-bdc7-d6b4c8f06d82 | -9.14138 | -51.30573 | 2025-11-02 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5378d7c0-e6a9-301e-ab26-3c6ef327147e | -12.51664 | -45.73363 | 2025-11-02 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7377de40-0335-38dc-b7cc-9941f6ba2a99 | -11.43237 | -44.67711 | 2025-11-02 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4089a27-1156-3033-b067-3f8077342a7e | -5.527 | -48.10663 | 2025-11-02 04:21:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3587f145-1b87-3bb4-97e5-c4d51305f5ec | -7.04154 | -41.46561 | 2025-11-02 04:21:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 66748461-472a-3bb8-917b-cf3d545ed7f7 | -13.05334 | -44.55989 | 2025-11-02 04:21:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 12303233-2215-3cba-807a-ca17e07d050b | -10.74353 | -46.2142 | 2025-11-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0bb865e3-b180-3252-bc86-ab68fd22fa7d | -5.11291 | -46.22251 | 2025-11-02 04:21:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e0191ff6-9d5a-3482-8d28-9b7573a94e4e | -6.0333 | -40.12345 | 2025-11-02 04:21:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 86883ee5-5e4a-3e9e-9430-42384b135d3d | -9.15504 | -51.30378 | 2025-11-02 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79d49eb5-2f59-3bde-ae33-d6acd8532525 | -7.19679 | -44.27328 | 2025-11-02 04:21:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40a704fc-9a56-355c-ab5b-70e01fc76ccf | -10.55654 | -44.5365 | 2025-11-02 04:21:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b69f280-ad34-39e8-882c-e54d520eb0d2 | -5.78901 | -47.55584 | 2025-11-02 04:21:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 84581119-6115-35f9-b573-b4d8a42be691 | -10.73955 | -46.26055 | 2025-11-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b876c267-13f7-3f74-90be-96c8785eb2f4 | -7.32637 | -41.54207 | 2025-11-02 04:21:00 | NOAA-21 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 47871a7c-9f67-3eec-a770-cefbdf745a15 | -8.16036 | -44.48588 | 2025-11-02 04:21:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3c613fb-5c05-357e-a5ca-b536d583ba4d | -5.09532 | -46.11336 | 2025-11-02 04:21:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b1fb90f-871a-3b69-b387-9b96055c1713 | -10.99866 | -54.00754 | 2025-11-02 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5495684-8a01-34d4-b680-e4b6f23aaac1 | -10.50466 | -44.54252 | 2025-11-02 04:21:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f5ce0e73-5792-3586-9e15-2d783e4d05be | -9.78007 | -43.85485 | 2025-11-02 04:21:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0d8032df-dca8-39d6-9bb1-ebb58cac224b | -10.74343 | -46.25756 | 2025-11-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5425596-1d11-3f5c-a545-e801a2a860f7 | -7.50584 | -42.44952 | 2025-11-02 04:21:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5b2bbc53-2002-3942-89aa-f162fdbdd465 | -6.79648 | -42.20428 | 2025-11-02 04:21:00 | NOAA-21 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| c51efd76-d64c-3387-99aa-ca30a0ed3e98 | -11.03119 | -44.03567 | 2025-11-02 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2eb4f4e5-db9a-3a8a-9f1c-77f08b74af74 | -10.97424 | -54.24736 | 2025-11-02 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 934c69cd-3ae5-3e8a-9dc9-37d9033cf876 | -9.11547 | -40.6115 | 2025-11-02 04:21:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0baa58a0-b0bf-3a8a-94cc-18b087724c2b | -10.41492 | -44.90347 | 2025-11-02 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7a825a6a-fde5-383a-a3a6-1fb40bf75cc9 | -11.57522 | -47.07641 | 2025-11-02 04:21:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90ae98fb-6627-303a-bbac-1eeb1902db02 | -7.15818 | -41.82019 | 2025-11-02 04:21:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4277812f-81c3-37a2-ae89-44d19bc2d904 | -11.56792 | -47.07892 | 2025-11-02 04:21:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2077d02c-a0c3-3366-931a-ec7c8fa24ae2 | -7.19786 | -44.26637 | 2025-11-02 04:21:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 31b0933e-b877-3fb1-ad98-f08ccd2a9b0c | -9.06485 | -48.83181 | 2025-11-02 04:21:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9b0b64a6-5509-331d-9f91-bd85f7834f29 | -6.48371 | -39.41085 | 2025-11-02 04:21:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 257ab2af-01ff-3a10-8f96-fc3cc23a9e94 | -11.27579 | -45.49307 | 2025-11-02 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 85f87ef7-3f2b-3719-84a8-fc8849ef2c11 | -11.02952 | -44.04663 | 2025-11-02 04:21:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 77eafe84-2ebe-363b-b90c-cbef880cb554 | -13.12204 | -42.31097 | 2025-11-02 04:21:00 | NOAA-21 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 20c7f27f-1431-395a-a6bd-4cb4248b39d5 | -7.40859 | -40.07571 | 2025-11-02 04:21:00 | NOAA-21 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 402bdea8-4313-36f7-9a6f-c89086098930 | -8.85928 | -49.87812 | 2025-11-02 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2488b7d-3b0a-3ba1-b7ff-136e8e3524c3 | -6.79995 | -42.20486 | 2025-11-02 04:21:00 | NOAA-21 | SANTA ROSA DO PIAUÍ | PIAUÍ | Brasil | 2209377 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| d20bd361-fae5-3954-9577-928e39047f8a | -10.41823 | -44.90398 | 2025-11-02 04:21:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee12f1bc-c9a9-39c3-9162-ced1b1ac170e | -12.58206 | -43.3636 | 2025-11-02 04:21:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f3d2310-3e25-3608-b5fa-876849ae1c10 | -7.03858 | -41.46075 | 2025-11-02 04:21:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 24fabb0b-d2f9-3eea-8719-a143e199e183 | -5.3729 | -45.07407 | 2025-11-02 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2dfdb23-6320-3f84-b15d-464dab6a7e57 | -7.18034 | -41.93841 | 2025-11-02 04:21:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ec564ced-429a-3520-8cf5-fc97496cb626 | -10.73466 | -46.22721 | 2025-11-02 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 89e9f7d9-aede-3e47-8bd8-9a78122d6554 | -5.37014 | -45.07006 | 2025-11-02 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47cb3020-173e-3b28-af64-d3bcb0cd93eb | -5.36911 | -45.20576 | 2025-11-02 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb96ef50-754b-3605-9c74-b21129d95194 | -9.78732 | -43.61395 | 2025-11-02 04:21:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91982e80-38b2-3c62-9ed4-afeba9226370 | -8.95434 | -44.07941 | 2025-11-02 04:21:00 | NOAA-21 | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README11.md)
