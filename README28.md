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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2d4a2ddb-9f95-35bf-b8f8-ec9ceab6fcb4 | -11.4336 | -56.0711 | 2026-07-02 14:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 161.9 |
| cc0e9df9-4335-3e1b-be9d-dc0ab6dd4946 | -6.9135 | -43.7281 | 2026-07-02 14:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 115.4 |
| e5424e3a-9204-3e5b-89c9-2c7fe9f832cb | -11.4338 | -56.0509 | 2026-07-02 14:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 212.5 |
| 0a436aa0-1da5-36dc-83f0-ef681cc16002 | -5.3787 | -43.388 | 2026-07-02 14:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 6e4709eb-2f7a-322c-b6c1-27b6d7f5d862 | -11.4147 | -56.0726 | 2026-07-02 14:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 217.2 |
| f723c41b-9f40-3b82-9a4d-e350e77467b2 | -11.4149 | -56.0525 | 2026-07-02 14:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 275.6 |
| 943575cd-a219-3f2f-aab9-0bac57647a07 | -10.7843 | -53.5434 | 2026-07-02 14:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 444a9675-3913-3ac5-8341-aa04002ad978 | -6.9326 | -43.7032 | 2026-07-02 14:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 541d3c8b-6fc9-345a-bf97-a258821b1343 | -17.732 | -46.7756 | 2026-07-02 14:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 7e3baf91-a45b-3546-9b36-8c8d7fa1074d | -6.9135 | -43.7281 | 2026-07-02 14:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 95.6 |
| c22d708c-03c0-3b25-ba54-fc6c6bd8c3cd | -6.9323 | -43.7264 | 2026-07-02 14:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 1583eadc-ee3e-315c-bf16-dcb4b6c8c7d4 | -6.4251 | -45.644 | 2026-07-02 14:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 8b2275d5-5eba-345e-b587-3833b5703178 | -12.5138 | -48.2581 | 2026-07-02 14:50:00 | GOES-19 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 560ba0f8-1215-3205-9eba-ff05496fca47 | -11.4338 | -56.0509 | 2026-07-02 14:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 113.0 |
| 3256b0d6-4640-3c10-b9bb-7e33b6ac5d53 | -17.712 | -46.7798 | 2026-07-02 14:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 104.2 |
| d49a90de-093d-359a-9dc7-88a6208a348f | -6.4253 | -45.6214 | 2026-07-02 14:50:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 0255847e-2754-3a2a-92c4-b052b1ba8a66 | -11.4149 | -56.0525 | 2026-07-02 14:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 380.6 |
| ab50acfc-4994-37f3-bd03-82cdc16f913e | -6.8767 | -43.6618 | 2026-07-02 14:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 7c422eb5-dda7-33f9-88ea-e5859499a20f | -6.9138 | -43.7049 | 2026-07-02 14:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 82.3 |
| df4c0e2e-816e-3cf6-a71f-06c6094d4013 | -11.4147 | -56.0726 | 2026-07-02 14:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 373.3 |
| 9171ff01-7ef8-30e5-989d-febce0984703 | -11.4336 | -56.0711 | 2026-07-02 14:50:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 4e2ba022-a58d-3b6a-bc61-89d4993c6f99 | -3.8671 | -42.9685 | 2026-07-02 14:50:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 2b322645-7700-373f-8402-00403d7e8718 | -11.3655 | -55.431 | 2026-07-02 14:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 573605e7-023e-39bd-9072-4621c9696410 | -10.7843 | -53.5434 | 2026-07-02 14:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.6 |
| ebcebb71-9b16-341a-95c8-0591ecfa939a | -5.4738 | -45.4201 | 2026-07-02 14:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 14358601-e13f-3ad7-9db4-ad9a497de44e | -11.4338 | -56.0509 | 2026-07-02 15:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 137.1 |
| 0a5c4a9b-5283-3c6c-a3ed-a9a7eced9446 | -3.8671 | -42.9685 | 2026-07-02 15:00:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 2fbcc352-f8de-31a2-818c-ecdaa56a5f07 | -6.9135 | -43.7281 | 2026-07-02 15:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| c4c963f2-1fb0-3468-aa46-a255d607696f | -9.3113 | -46.361 | 2026-07-02 15:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 713177c4-15b0-3bff-b2c1-b2a5cf95ced6 | -10.7843 | -53.5434 | 2026-07-02 15:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 2e9c1952-4b9c-3d8b-8fb8-2b4ffe6c182a | -6.9326 | -43.7032 | 2026-07-02 15:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 5b44d263-3e81-30a8-889c-80bd519dd44b | -5.4738 | -45.4201 | 2026-07-02 15:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| f847c506-5db5-31a9-a830-73e186b8af23 | -11.4147 | -56.0726 | 2026-07-02 15:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 451.0 |
| 75969f20-be5d-33f5-9fba-6fec12989e1d | -6.9138 | -43.7049 | 2026-07-02 15:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 4110f8ae-e74b-3119-8b68-808605754d9d | -6.9323 | -43.7264 | 2026-07-02 15:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 2d1596d2-b6e9-3bcb-99a7-1eecd748957d | -11.4149 | -56.0525 | 2026-07-02 15:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 472.2 |
| f32228c4-fa2c-357c-8e1f-2a65ae1ac833 | -5.3787 | -43.388 | 2026-07-02 15:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| cdb06999-89d3-3c8a-9a25-0490e55413dd | -11.4336 | -56.0711 | 2026-07-02 15:00:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 124.6 |
| e6598650-3521-3afc-b4fc-7af673995a6a | -11.4338 | -56.0509 | 2026-07-02 15:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 158.4 |
| 0c755aa7-ce0d-319b-bd9c-749240caa081 | -6.9323 | -43.7264 | 2026-07-02 15:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 1e28a4a1-117e-39ee-adb2-baf3239828f1 | -10.3857 | -46.6855 | 2026-07-02 15:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 149.8 |
| fbdee692-7297-3343-85de-131a0d741cde | -11.4147 | -56.0726 | 2026-07-02 15:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 440.3 |
| af089930-3bee-315e-97e8-ffcb7ad9d6da | -3.8671 | -42.9685 | 2026-07-02 15:10:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| eff671d1-dcba-302c-adff-8e8dee161fca | -6.9326 | -43.7032 | 2026-07-02 15:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| cfa847d4-8a28-3351-bd59-5ce609651a92 | -9.3113 | -46.361 | 2026-07-02 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 0c5e64f9-9468-34d6-8e71-10bf0f45d0ba | -5.4738 | -45.4201 | 2026-07-02 15:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 9f45c6fe-f9d1-3575-9ff6-7e855310c003 | -6.9135 | -43.7281 | 2026-07-02 15:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 119.3 |
| e9b3dac5-c531-3e4c-a4ed-b677dd0bd0e6 | -11.4336 | -56.0711 | 2026-07-02 15:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 129.1 |
| c2a5cbcc-2a2c-3411-a520-c307f1ce89f4 | -11.4149 | -56.0525 | 2026-07-02 15:10:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 534.9 |
| 7175f5b0-959e-3758-b095-7598f71eea78 | -6.9138 | -43.7049 | 2026-07-02 15:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 91.6 |
| d9b91ad2-08cb-3d0a-aeab-dcc70a905782 | -5.3787 | -43.388 | 2026-07-02 15:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 603287e8-322f-3bc5-b2ae-83f2f7dae63e | -6.9323 | -43.7264 | 2026-07-02 15:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 747f95b7-055e-378c-915f-fb8f68bf8fae | -3.8671 | -42.9685 | 2026-07-02 15:20:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 3a010b6e-c937-3ec0-83bd-1c21168d50b3 | -6.9135 | -43.7281 | 2026-07-02 15:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 4a95e472-e961-3aa2-aac9-69009f6c8174 | -11.4149 | -56.0525 | 2026-07-02 15:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 470.5 |
| e81827a5-efb9-3918-9f7b-f561aff987e1 | -9.3113 | -46.361 | 2026-07-02 15:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 120.9 |
| df588d98-8622-3734-ac54-76021faf7a39 | -11.3466 | -55.4326 | 2026-07-02 15:20:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 99.6 |
| 55957123-1cf8-3a87-8855-0888d081f963 | -6.9326 | -43.7032 | 2026-07-02 15:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 87.2 |
| a489e4db-ec33-3680-9f5b-d552e18e14ad | -6.4253 | -45.6214 | 2026-07-02 15:20:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 106.6 |
| 1f81323b-5123-34e9-9219-04fa483671e7 | -6.9138 | -43.7049 | 2026-07-02 15:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 110.1 |
| 350b03ec-25a1-38fb-8202-ccab5be81bec | -11.4336 | -56.0711 | 2026-07-02 15:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 297.8 |
| e7235793-bf17-3fd7-8da1-af57641280ff | -11.4338 | -56.0509 | 2026-07-02 15:20:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 273.8 |
| 2a9f28fe-d58b-3ff5-be6f-08e6bbda737d | -5.4738 | -45.4201 | 2026-07-02 15:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 542cb18c-29b6-390a-b5de-73433b777e92 | -11.3466 | -55.4326 | 2026-07-02 15:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 148.2 |
| 7ca34569-e22d-3743-98fb-0c64f19b2080 | -6.9326 | -43.7032 | 2026-07-02 15:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 100.8 |
| a82ef6bb-96eb-3238-aadc-9511825319b0 | -6.9138 | -43.7049 | 2026-07-02 15:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 1ef4e06a-8948-3d27-b9b3-62f6c4f946f5 | -3.8671 | -42.9685 | 2026-07-02 15:30:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 91b3d4fb-19ba-3f1c-b764-81e01c2b9215 | -6.9323 | -43.7264 | 2026-07-02 15:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 9f01dd36-1717-3e89-90a2-edbcee38fc39 | -20.2335 | -55.4991 | 2026-07-02 15:30:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 02f86460-5d22-3ab8-9fff-ed0e3b051e62 | -11.4149 | -56.0525 | 2026-07-02 15:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 587.8 |
| eb46d71a-13cb-315a-846f-3921e837b6f9 | -11.4338 | -56.0509 | 2026-07-02 15:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 229.8 |
| 6ccd773d-6973-3fd8-bc5b-0f3e7123809a | -6.9135 | -43.7281 | 2026-07-02 15:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 108.7 |
| edc38471-19d9-3c8c-92d2-dc71ec06395b | -11.4336 | -56.0711 | 2026-07-02 15:30:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 254.1 |
| df8be1c8-8bf0-38d6-b9c3-fa436b19de1d | -11.3657 | -55.4107 | 2026-07-02 15:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 7955fe64-7f0f-34b9-a890-3e57a079087a | -11.3655 | -55.431 | 2026-07-02 15:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 09f1456d-111e-3c06-8d83-7be052ffa3e0 | -3.8671 | -42.9685 | 2026-07-02 15:40:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| dac39326-5e79-3724-9ff7-fe8578c4c4d9 | -11.4149 | -56.0525 | 2026-07-02 15:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 560.1 |
| 5ea4cfc7-1b2f-30f2-8307-e3f1283bb71f | -10.7843 | -53.5434 | 2026-07-02 15:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 4de6b3b9-ff94-3490-8156-adabbdac795a | -5.3787 | -43.388 | 2026-07-02 15:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 826a3ccd-d619-3000-93a2-fffe06111720 | -11.4336 | -56.0711 | 2026-07-02 15:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 446.5 |
| abf0dea2-7cb0-3fad-8049-00b13a32ae0b | -20.2335 | -55.4991 | 2026-07-02 15:40:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 150.5 |
| b2feb42a-d72c-3580-8909-35d5adc14538 | -20.2339 | -55.4777 | 2026-07-02 15:40:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 66.0 |
| e2b41b7c-c337-32ef-8da8-8e340c899100 | -11.4338 | -56.0509 | 2026-07-02 15:40:00 | GOES-19 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 366.9 |
| 5b4c606b-248f-3389-ae23-a586d69355a8 | -6.9135 | -43.7281 | 2026-07-02 15:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 26635082-25fc-3e1a-9ff6-bc5174ae0a7a | -6.9326 | -43.7032 | 2026-07-02 15:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 048040fc-2430-3b64-9d0a-b9ecc028f0ba | -6.9323 | -43.7264 | 2026-07-02 15:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 101.2 |
| c5cb9dcd-f6b5-3bb5-be9e-07b7b8555fd9 | -11.3657 | -55.4107 | 2026-07-02 15:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 3f54f584-2d60-3c0f-b666-0ad60a08652f | -11.3466 | -55.4326 | 2026-07-02 15:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 120.8 |
| 13ee98ad-c833-32e7-bb64-fabecec5e286 | -6.9138 | -43.7049 | 2026-07-02 15:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 115.2 |


