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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87a3a52f-f4ed-314d-b267-a37d2e8e84ef | -6.42437 | -43.71936 | 2026-07-21 04:25:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 77438779-7e4f-3ac2-ada9-8522e69ad574 | -4.66065 | -42.42091 | 2026-07-21 04:25:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f671226d-ade1-3a00-bf20-793b43479297 | -3.67089 | -48.97097 | 2026-07-21 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f515f45d-cdcb-3337-a6cf-07c3d559d912 | -6.93274 | -43.6588 | 2026-07-21 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59ebf8ac-5493-3210-8a3d-87c8d0e4bdf2 | -5.12174 | -43.23098 | 2026-07-21 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc984d60-b009-3760-a604-c8d5df288793 | -5.74644 | -43.26657 | 2026-07-21 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 807ecb93-7ea7-3cb6-a74c-a407a3a43fe9 | -3.14452 | -48.1518 | 2026-07-21 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 280847a6-4adc-3ea0-8a4f-08719f57cefc | -4.44899 | -46.13348 | 2026-07-21 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 80bff4ea-6df4-3c65-950e-86950ab3fc1a | -2.43335 | -47.0303 | 2026-07-21 04:25:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2bb7311-b69d-39a6-afe5-1d9c6050983b | -5.9187 | -46.71978 | 2026-07-21 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d487b5e8-0b6b-36fd-88f7-ec2359f0404a | -4.77385 | -41.79089 | 2026-07-21 04:25:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 5184c1f2-c7f6-33e5-a28d-349f5b509ac1 | -5.74584 | -43.27058 | 2026-07-21 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad165cd5-5cf7-3c0e-8a3d-701fec44931a | -3.97868 | -48.42696 | 2026-07-21 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0aa3958d-6876-3493-a11e-d9bfe2e00aab | -3.14877 | -48.57929 | 2026-07-21 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bcbdcb6d-de3c-37b7-a09f-998f5c054e05 | -4.16402 | -43.09779 | 2026-07-21 04:25:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a9d5dab8-5184-3412-94f0-6f7023591a65 | -4.68491 | -43.22123 | 2026-07-21 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02fdcd42-7183-3aae-97df-347286e8ffe3 | -3.95829 | -48.00283 | 2026-07-21 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83f5c766-a64e-37f2-b67f-a3f26232e52d | -5.12466 | -43.23549 | 2026-07-21 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5dc82eb6-dd1a-3853-9b44-edfc32a9db00 | -2.79847 | -48.57844 | 2026-07-21 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 177c436d-57da-352d-a915-03206b0358af | -5.60697 | -44.02561 | 2026-07-21 04:25:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c16e5233-7fed-3c0f-a34c-69f3331dac60 | -6.84211 | -46.3842 | 2026-07-21 04:25:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 01167da1-180f-32ce-b730-112490181a6a | -6.92569 | -43.65771 | 2026-07-21 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee84538d-ae10-31f5-a097-b27167f0ea8a | -0.85687 | -52.7175 | 2026-07-21 04:25:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c1aa853c-0129-3723-9dba-27a570c15782 | -3.14804 | -48.15235 | 2026-07-21 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bbca58aa-aa61-39c2-8bd6-b18be041fa09 | -3.72818 | -49.26971 | 2026-07-21 04:25:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 15c2bec1-6635-3500-a43d-75955d462b54 | -3.15235 | -48.57986 | 2026-07-21 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 208ee475-75a6-3668-a3af-c370801f885f | -7.08476 | -46.53234 | 2026-07-21 04:25:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1150e0ad-db3b-3802-a757-4181df3fb0a5 | -4.1611 | -43.09334 | 2026-07-21 04:25:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 568284d9-4e60-3f38-97f4-6496de297e98 | -2.69513 | -49.02333 | 2026-07-21 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a36ea308-c51c-3b80-9acc-d9d4aea1cdf6 | -2.47214 | -49.35639 | 2026-07-21 04:25:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ef4083d-1e57-33a9-8ce3-1bf79f00a37d | -5.67192 | -43.57076 | 2026-07-21 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 04bef1f5-1a25-391a-80d4-a57a315471ba | -5.74229 | -43.27005 | 2026-07-21 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf814237-bae8-3397-8e08-4fd8a3768f63 | -2.4714 | -49.36097 | 2026-07-21 04:25:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69b98e40-7045-3820-abd2-94a1e3ea3950 | -2.80213 | -49.52496 | 2026-07-21 04:25:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76ea28d9-2db5-3277-85b8-fce8436058a0 | -3.2628 | -49.53287 | 2026-07-21 04:25:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14a8864c-670c-3b84-80fc-a47e4b9b08d0 | -3.45884 | -48.81984 | 2026-07-21 04:25:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a314bf79-b632-3ccc-b489-0d2a14cd6a05 | -5.12185 | -43.96488 | 2026-07-21 04:25:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f2b1dae7-93ce-3f1a-8e55-ba68f1121510 | -4.48081 | -47.51556 | 2026-07-21 04:25:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2db5a90f-e2f6-381e-877b-4cfbd6e5aa67 | -2.8004 | -48.57831 | 2026-07-21 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8898a14d-b6ab-3c26-997b-afbfefcfbfdd | -6.43815 | -44.55432 | 2026-07-21 04:25:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f06db68-47c5-3b86-83cd-070d1e5c60bc | -3.15594 | -48.58043 | 2026-07-21 04:25:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd59a76c-489b-3641-9675-38b341c27fc5 | -5.11761 | -43.23438 | 2026-07-21 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 77db70c3-37b1-3ac3-998f-64beadb5ae9c | -5.91539 | -46.71926 | 2026-07-21 04:25:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2cb282e9-962b-3059-a88b-55b4e3a65852 | -4.30076 | -42.32511 | 2026-07-21 04:25:00 | NOAA-21 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bba364c3-8c91-30f8-b429-0bb1f360cad7 | -2.31887 | -48.58052 | 2026-07-21 04:25:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b45c8c9f-fa45-3c86-812e-cb321afb0eed | -4.77315 | -41.79553 | 2026-07-21 04:25:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| b5133b6c-eaed-3012-9509-eb727deb6c77 | -5.93911 | -46.35133 | 2026-07-21 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6af4783-0683-386a-ade4-e4895f7e2bcf | -5.04142 | -44.46522 | 2026-07-21 04:25:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5306bfb2-311a-31ed-ae27-cf527f2f4fa0 | -5.12759 | -43.23999 | 2026-07-21 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2a47e82b-4b52-37af-8e3e-1ddd06187517 | -2.79834 | -49.52436 | 2026-07-21 04:25:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0fcf741-5e38-31d5-b733-00b644ae52c6 | -5.3437 | -43.17645 | 2026-07-21 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9229784d-3e6d-34b9-a9ef-57acd1495887 | -3.67157 | -50.94804 | 2026-07-21 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07237767-8cdf-3817-a4e0-9f9bf207bc5d | -2.69882 | -49.0239 | 2026-07-21 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a0b27a0-8eeb-3cc2-adcc-130ae3254f73 | -4.1605 | -43.09727 | 2026-07-21 04:25:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b01e1129-7276-338c-bc5c-6429f4a043c5 | -4.65699 | -42.42036 | 2026-07-21 04:25:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f88b5da8-edfd-300c-9d0e-8fb5f88553c2 | -5.12114 | -43.23494 | 2026-07-21 04:25:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 43c4f210-caf3-3961-9c0f-f61f8f6714e1 | -6.60097 | -51.70517 | 2026-07-21 04:25:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ae1c0169-836d-3839-bc97-378325229e9e | -3.16449 | -48.07097 | 2026-07-21 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed7bf9ff-66e8-314f-8990-6f78209e4508 | -2.46763 | -49.36038 | 2026-07-21 04:25:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8c54195-7b73-38a2-a3a1-df40e6af0e1e | -3.24292 | -47.92484 | 2026-07-21 04:25:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d34dfed2-351b-3d2c-8a53-c01ab7f29a54 | -5.34015 | -43.1759 | 2026-07-21 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7d3bc23f-b49d-3a81-aece-22d3adacccf5 | -6.01398 | -47.10987 | 2026-07-21 04:25:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3f52917b-277b-3147-8a37-bb2826734b72 | -5.67833 | -43.57574 | 2026-07-21 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35f90971-4e7c-34cd-a436-5867d5c91bf9 | -3.26355 | -49.52818 | 2026-07-21 04:25:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 71418031-338c-3bcb-aa2d-b48b994b4060 | -3.97293 | -47.19545 | 2026-07-21 04:25:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a3d6ee0c-c818-3a6c-84f9-51d023e715b4 | -5.75 | -43.26707 | 2026-07-21 04:25:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c96b7bdb-4722-3a65-a214-096aefcacda4 | -4.44952 | -46.13003 | 2026-07-21 04:25:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2b49bd23-1e71-39bf-9b0f-6e0e58f90f1a | -12.13742 | -48.25934 | 2026-07-21 04:27:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24ce64a6-6cd3-3003-a073-fbbb4e026a52 | -11.83434 | -44.76551 | 2026-07-21 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0e35b16f-b4ad-388d-b248-6ca3700eb626 | -11.34601 | -47.99252 | 2026-07-21 04:27:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 855b544f-1d00-37c9-8ee9-9165fcdfe188 | -12.52675 | -48.25057 | 2026-07-21 04:27:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3524551e-bde3-3ecf-a1a6-40c8c6ed281b | -9.40977 | -46.69226 | 2026-07-21 04:27:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 156f2374-f309-3fd8-9b11-3c6001f372e0 | -9.08693 | -50.58132 | 2026-07-21 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d333758a-9851-375e-8d79-2a381623d422 | -6.13119 | -55.80844 | 2026-07-21 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00bd5dc5-e592-30c0-a71d-163c7adca369 | -11.41056 | -47.51717 | 2026-07-21 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7630e03e-41c2-3845-82d0-5b6d1267c483 | -10.86643 | -50.42109 | 2026-07-21 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8c14ab2b-82f6-3500-a460-6817b463c122 | -6.54108 | -55.15644 | 2026-07-21 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f69eb163-7e23-3115-a4de-d41fedeeb571 | -8.75848 | -49.08041 | 2026-07-21 04:27:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fcf422bb-73ca-3fd9-86db-a6d8439eab7b | -12.46204 | -46.51942 | 2026-07-21 04:27:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 372d8eb7-e919-3cba-bcba-bce639df4e42 | -7.84168 | -47.10768 | 2026-07-21 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7dfc2947-4561-3761-bc23-44692ab3c084 | -13.30764 | -45.12621 | 2026-07-21 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 7aab9877-0420-34f1-8486-1ec16027bbf8 | -14.73822 | -44.6645 | 2026-07-21 04:27:00 | NOAA-21 | CÔNEGO MARINHO | MINAS GERAIS | Brasil | 3117836 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ab8f0fc5-c747-3318-836a-249a8f915b59 | -10.82482 | -50.42699 | 2026-07-21 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| ead2b1a2-17a0-3d2a-8691-bbbca8336f05 | -11.98195 | -47.10208 | 2026-07-21 04:27:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d06537b-b347-3069-83ac-13fa89f32bd6 | -11.3449 | -47.99956 | 2026-07-21 04:27:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7a723ee5-c929-397e-90ff-33a7d4045a38 | -11.98471 | -47.10613 | 2026-07-21 04:27:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfa27294-63f3-3039-aae5-44435fe88445 | -11.91121 | -43.84357 | 2026-07-21 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 305b6c8e-f084-32b8-ba73-683ebffb525b | -12.70024 | -45.32684 | 2026-07-21 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37a1dbaf-35eb-31e3-9b27-0445c7973820 | -7.73103 | -47.24747 | 2026-07-21 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d92c456f-c628-3b35-88f5-6a23d7302cf0 | -12.86607 | -46.87676 | 2026-07-21 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7aee5360-1d35-3e0e-bf32-45a0859ec8db | -12.66064 | -48.22208 | 2026-07-21 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7d0ce404-a436-38bc-ab15-be6e3ea30a88 | -9.17213 | -49.63961 | 2026-07-21 04:27:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf99c18b-3340-3bf0-83db-1f5b0a1c738a | -11.34214 | -47.9955 | 2026-07-21 04:27:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a241b595-c67e-3601-8b0d-081c6cfed289 | -12.37282 | -45.67122 | 2026-07-21 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02f5985d-58a7-325f-b5c6-51883cc62182 | -13.31233 | -45.14342 | 2026-07-21 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 681af819-bb75-3e0c-8e95-ce942f86afbe | -10.52942 | -50.28169 | 2026-07-21 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c72fb615-185a-3a70-abd6-cc21c4ed8a1b | -9.08843 | -50.59535 | 2026-07-21 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cfd30a24-179c-3cb9-bf79-e2cabd27bbfe | -9.54788 | -49.30033 | 2026-07-21 04:27:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57296ded-ccfe-3ccc-a084-49dbdf1751d2 | -12.14129 | -48.25635 | 2026-07-21 04:27:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c8e3676f-690c-3e5f-aac9-e0d18cb38370 | -10.57089 | -50.44296 | 2026-07-21 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README7.md)
