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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 627b7291-33aa-3576-b856-b8553acdf68f | -2.57591 | -51.83766 | 2025-08-30 04:46:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71ebf32a-7078-35fb-99bb-b97391230691 | -4.37861 | -48.06926 | 2025-08-30 04:46:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e9babe5-dee9-31af-89ce-a3c8d28a9eb4 | -6.55544 | -43.68987 | 2025-08-30 04:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 157f37e8-3402-3547-ab53-e20d4a702a6f | -2.98489 | -48.60273 | 2025-08-30 04:46:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83c843ae-b40f-3b58-a50b-6d68d3dcbea5 | -6.39702 | -45.25616 | 2025-08-30 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61d383ce-b4e6-32b3-92b9-05f6f331e135 | -3.79115 | -49.43028 | 2025-08-30 04:46:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c5e2e27-ca3a-3689-91fe-c8f57de22352 | -2.44241 | -47.32652 | 2025-08-30 04:46:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f68abee-e782-37ad-8813-308132e72a06 | -5.75741 | -45.21634 | 2025-08-30 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b86d8438-0ebc-35c0-93d8-71355d9058be | -6.49834 | -43.53966 | 2025-08-30 04:46:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 548a9aa3-a479-3723-a475-79105056bda9 | -6.32758 | -42.52145 | 2025-08-30 04:46:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a3837430-b3ad-3b53-abb6-aec1573d256f | -6.37949 | -44.33609 | 2025-08-30 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 18115b6c-7eb0-3917-a6bd-e18d1f5cc77c | -5.7506 | -45.37464 | 2025-08-30 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1d3fa85a-dc79-3ae1-8149-c297a38c5ea0 | -6.5902 | -43.64885 | 2025-08-30 04:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c3868120-4adc-32b8-a930-b0f7682e0e89 | -6.32131 | -42.52893 | 2025-08-30 04:46:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f87423e2-40c4-3a7b-a840-32c55e474f74 | -6.41341 | -45.61097 | 2025-08-30 04:46:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a71bb96b-181c-37e7-a400-c7c263bfd073 | -6.41508 | -45.59961 | 2025-08-30 04:46:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 82954e7c-a1eb-30aa-add0-dcbdf81100f8 | -6.59499 | -43.64919 | 2025-08-30 04:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b337c0a4-352c-3ba0-a610-20bd06196a34 | -6.41452 | -45.60338 | 2025-08-30 04:46:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c9104344-c464-3ba7-b932-a92c1246db27 | -6.52749 | -44.85952 | 2025-08-30 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 63fed60f-c1c0-3a51-9cfb-399745bdfe6d | -6.23275 | -43.83236 | 2025-08-30 04:46:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6591ef0e-7c6e-3693-9e1a-0d4419fc3e00 | -3.06931 | -49.46116 | 2025-08-30 04:46:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb13b625-52b9-399d-9b94-3c2e988ac37b | -6.1724 | -43.33483 | 2025-08-30 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2ee88690-0cb5-3e95-a586-ba052e447397 | -4.87749 | -46.85099 | 2025-08-30 04:46:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 12c58b1e-f0cc-3404-a198-e0ce2456788c | -6.17525 | -44.79343 | 2025-08-30 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 04035ad3-2e2c-3587-8271-17a65aa8f2bb | -6.20786 | -42.75321 | 2025-08-30 04:46:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ca1da288-3ccf-3658-8818-5e86e9dae67d | -5.74645 | -45.374 | 2025-08-30 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48bb052f-c900-3991-a15b-967ca007bcc0 | -3.59786 | -49.45744 | 2025-08-30 04:46:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d1180e94-e95c-3c26-a125-9f02be6efd2a | -6.17395 | -43.3283 | 2025-08-30 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6e007227-2c88-3a9b-b25b-4ca8cbe6918e | -5.87853 | -46.50115 | 2025-08-30 04:46:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f531f37f-6004-3a8f-9d95-e9e484b8c158 | -6.17317 | -43.33353 | 2025-08-30 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 14a91413-9765-3605-828f-74e76e3a660f | -6.15595 | -43.58859 | 2025-08-30 04:46:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a1dbe3a7-26ea-3a14-b9a7-7c8b0d79d37d | -1.55585 | -54.545 | 2025-08-30 04:46:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 59346c66-94fb-30e0-a510-3b2224cc5695 | -2.98149 | -48.60221 | 2025-08-30 04:46:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0aacec0e-ce63-3676-b33a-b458abe78860 | -6.36216 | -44.45634 | 2025-08-30 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73ef6ae7-f6b4-35f9-be3c-c583621eb545 | -3.42508 | -49.04812 | 2025-08-30 04:46:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 09caf238-2271-32aa-9a20-2ea03ffe8726 | -6.78012 | -43.78513 | 2025-08-30 04:46:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7c024921-b519-3505-8e88-8b051f04303d | -6.65774 | -44.37315 | 2025-08-30 04:46:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3bfed3b6-2505-3208-b965-15d5744a9c75 | -5.61485 | -45.01349 | 2025-08-30 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63717ff4-0cea-312e-b3ef-ac1c8afed8d6 | -6.1772 | -43.33562 | 2025-08-30 04:46:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 959babbc-169d-3f4b-add1-5c78390d50a4 | -4.15657 | -46.78058 | 2025-08-30 04:46:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46a92746-3e30-3559-a7ae-07554e711ef7 | -6.55997 | -44.21708 | 2025-08-30 04:46:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3eb75c6-11c9-3a6b-81ec-25a117d4f7fa | -6.80754 | -43.7279 | 2025-08-30 04:46:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b30251b-120e-3f39-8b19-4a66d9d1d2f4 | -6.79908 | -43.03423 | 2025-08-30 04:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 15ff0058-c229-3cdb-ae04-c83480198fd9 | -6.21205 | -42.75962 | 2025-08-30 04:46:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2c96e74b-b9de-3de5-a9b7-f4a91feed5dd | -6.18316 | -44.86159 | 2025-08-30 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c4c3fb7-391a-3c26-a20a-a612b0fc1c7b | -3.04845 | -47.01818 | 2025-08-30 04:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 15035391-2fd9-3bb2-92e3-8fe95059d623 | -6.4115 | -45.59523 | 2025-08-30 04:46:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fce488ad-c497-3395-a76c-a1011fc3fe54 | -4.50408 | -47.28916 | 2025-08-30 04:46:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6fb2c0ef-1f2b-3df2-9a38-6ba599957324 | -3.42116 | -49.05116 | 2025-08-30 04:46:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ec7e2b8-fcda-347b-9c31-e20c0482a8a5 | -6.78624 | -43.77589 | 2025-08-30 04:46:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a3857d96-916a-37fa-b576-1e5b9d34d3ab | -3.59452 | -49.45692 | 2025-08-30 04:46:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cefb3cc8-a850-350c-a51b-9b7993a07319 | -3.21859 | -46.83109 | 2025-08-30 04:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2eac8f1d-df8d-38b4-b91c-27b7e8780cba | -5.76007 | -45.36822 | 2025-08-30 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bfaf3e5a-6364-379a-a0f5-d967fa68d44e | -4.87309 | -46.85468 | 2025-08-30 04:46:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 84970f06-4a61-3db2-bf15-74f4d5a7061e | -5.83035 | -44.10554 | 2025-08-30 04:46:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fb9c865-62c8-396c-b8c9-60972fbe5b01 | -7.01528 | -42.02618 | 2025-08-30 04:46:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5360f876-e196-3f50-ba37-cf4ee00b51e3 | -4.15591 | -46.78492 | 2025-08-30 04:46:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50a88404-f8d4-35b6-af89-1ebcb54a1da1 | -6.23534 | -41.81697 | 2025-08-30 04:46:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 2408918c-94a1-3690-bb44-f581b4aefa8a | -5.61542 | -45.00958 | 2025-08-30 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| a7e58769-711a-3fa0-80db-696932e5bcac | -2.88949 | -49.48356 | 2025-08-30 04:46:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 27ecba0a-ed1f-3bef-9cbc-e556e73fb3a9 | -5.7595 | -45.37203 | 2025-08-30 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cb3bc256-4977-3b6c-b09a-f55b5f810391 | -5.96012 | -44.51687 | 2025-08-30 04:46:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78af3a7d-3ffa-3b7a-9176-6f09773f9ab6 | -6.2285 | -44.73304 | 2025-08-30 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dff7ab0e-587f-353a-a37c-c64b5e7e3c4d | -4.98668 | -38.60392 | 2025-08-30 04:46:00 | NPP-375D | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 756099a2-5144-3474-9097-9f40712ca533 | -5.69941 | -45.96169 | 2025-08-30 04:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f33f92e-15c1-3341-8b57-af1c5e468741 | -6.69588 | -43.08144 | 2025-08-30 04:46:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 509eacf6-2347-33ca-9e32-5c460b4a42d2 | -6.48999 | -44.41147 | 2025-08-30 04:46:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79221872-4b2f-389c-a769-a5c7a1941d88 | -6.59975 | -43.64969 | 2025-08-30 04:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4c2a2af6-64be-3fec-b90b-2625b30e8db0 | -6.62129 | -43.73421 | 2025-08-30 04:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f6a94677-c6ba-36ca-9876-d278e1809878 | -5.72651 | -45.53344 | 2025-08-30 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b590b7ff-ab4c-3573-a690-cc97eeb2e6ef | -3.36904 | -51.76984 | 2025-08-30 04:46:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b857dc32-2cb7-39d6-ac34-a73d7a370f24 | -5.72824 | -43.94062 | 2025-08-30 04:46:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 86dd1fe3-dd25-3708-9cc3-98186f527943 | -5.7034 | -45.96231 | 2025-08-30 04:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd9c9e88-4c7a-380e-939d-c4cfe48e3d15 | -5.71122 | -47.42847 | 2025-08-30 04:46:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| be910fb6-f351-3738-bc96-db83a73f91f7 | -5.82806 | -46.3597 | 2025-08-30 04:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 43bca175-aeda-32f8-9d3b-15c1eb25d41a | -6.4881 | -43.54324 | 2025-08-30 04:46:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b8c873c-34d1-3359-82ef-ca25dd6840dd | -6.32719 | -42.52419 | 2025-08-30 04:46:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a0b35bd5-58bd-3ba7-832a-503e90ea5e15 | -4.98745 | -38.5985 | 2025-08-30 04:46:00 | NPP-375D | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| ecc09891-5d6f-3d5b-bcf8-74846a5eea8b | -6.17612 | -43.30837 | 2025-08-30 04:46:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8c12bf62-919f-3b5d-b998-d70bd375796c | -3.64464 | -48.44748 | 2025-08-30 04:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9b480c30-4718-3407-b7fe-70797934c25f | -5.76062 | -45.37216 | 2025-08-30 04:46:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 848a6873-82a4-3793-8312-c4cddc468c5a | -6.29069 | -44.46265 | 2025-08-30 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f426ccb0-fe48-3a07-bf68-ad7cb45cbfaa | -6.52375 | -44.85466 | 2025-08-30 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b71ebd87-b286-3d21-878a-486919b5caa8 | -5.70017 | -45.95653 | 2025-08-30 04:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cba2f8ac-694c-32b2-a86f-1628a7db2635 | -3.73222 | -48.9373 | 2025-08-30 04:46:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0d6087b5-9478-3d6a-b98c-f00e7007c3f6 | -6.28625 | -44.46191 | 2025-08-30 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 077007a7-14fd-3117-969c-700a9973b453 | -5.82027 | -46.35844 | 2025-08-30 04:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 69fb6416-18b2-3620-aa7f-11e05a3a83e2 | -6.4181 | -45.60775 | 2025-08-30 04:46:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95ee4930-4216-3291-86e4-c788800c1530 | -6.52315 | -44.8588 | 2025-08-30 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 300a78f7-5147-3674-9c7e-71584f74d57e | -6.37886 | -44.34049 | 2025-08-30 04:46:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 636d9727-7a98-31eb-adec-69950f913f17 | -3.04483 | -47.0176 | 2025-08-30 04:46:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0431c9cd-3bab-3b5d-80fb-2ebbcd6d332d | -6.55953 | -44.21979 | 2025-08-30 04:46:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66d08878-d830-3b8d-93cd-a313a7e16d2f | -6.41397 | -45.60717 | 2025-08-30 04:46:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 041119b3-11be-3109-bebf-8c337f0df64e | -11.3251 | -43.61439 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ec01e4d-999d-3255-965c-f4072e552a5b | -9.51414 | -54.44328 | 2025-08-30 04:49:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2ba8bc22-af73-35df-a1b0-84917debbf86 | -11.32663 | -43.60267 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9e02d597-4f27-3ec6-b78a-615fdc1201e3 | -10.48197 | -57.95271 | 2025-08-30 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 841d37ad-9bdf-3f5a-9470-8d8cf5bc0dd3 | -7.57959 | -45.13206 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2ea57a42-53fa-3d9f-9abb-81db885d0176 | -8.11783 | -61.21485 | 2025-08-30 04:49:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89b0e681-395b-3672-b1c1-82def2d569bc | -7.75956 | -45.46251 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README42.md)
