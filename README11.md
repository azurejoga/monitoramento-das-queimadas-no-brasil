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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b885f94-5c76-3905-aaa1-7bcedae931be | -7.26365 | -44.1908 | 2026-08-24 03:49:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee4fba04-4442-3353-9904-696fb1b95338 | -7.36649 | -45.79684 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9ef4da7d-d3f2-3b28-85e4-3837d96e39ba | -9.43073 | -36.80941 | 2026-08-24 03:49:00 | NOAA-21 | ESTRELA DE ALAGOAS | ALAGOAS | Brasil | 2702553 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b421c47e-7ce1-3c11-8348-d17ffaf061a0 | -7.19016 | -42.74892 | 2026-08-24 03:49:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4be43fd3-a8f5-37cd-a55b-a602ff0ce629 | -10.46136 | -46.22422 | 2026-08-24 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ea162bf6-6f91-3ade-9cb1-354fd35e60d1 | -12.27404 | -43.19921 | 2026-08-24 03:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebe7c6bb-421f-3e9a-b0e5-38e3c95e33f3 | -8.09912 | -47.48632 | 2026-08-24 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fbd8ef46-0dc3-3942-9719-3716565d26c3 | -7.30425 | -42.97305 | 2026-08-24 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 05fcb595-2219-3c97-b675-0ac234fab411 | -5.57229 | -45.29108 | 2026-08-24 03:49:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e13233cf-0944-38ae-a7b9-91cb9ca892d9 | -7.97652 | -45.25874 | 2026-08-24 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a288b261-d798-3491-927e-d47cf3c5525f | -12.14415 | -43.38891 | 2026-08-24 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e62a07a6-ebec-357c-bb3f-8b163a02c2f6 | -7.29942 | -43.00114 | 2026-08-24 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d72857fd-1f32-3818-bb22-f2d789943ddc | -11.36347 | -40.06017 | 2026-08-24 03:49:00 | NOAA-21 | CAPIM GROSSO | BAHIA | Brasil | 2906873 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 29c44b98-d526-3681-9175-a2af485506d1 | -7.35969 | -45.80516 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 58cff2a2-8a0a-3670-8068-f98c27f2b4d0 | -12.7456 | -46.46859 | 2026-08-24 03:49:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e1a53028-539f-3626-ab09-423ade022548 | -12.41175 | -42.89653 | 2026-08-24 03:49:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3f18017e-1f62-30a1-9604-cfa4d254a3a6 | -7.97557 | -45.26427 | 2026-08-24 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6bccadcb-ea74-3470-8c48-d931b265b1fc | -10.29684 | -48.20203 | 2026-08-24 03:49:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f76c85a3-3cbc-35f0-adf6-16253690ef8e | -12.41081 | -42.90404 | 2026-08-24 03:49:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| de11f4c4-38b6-3264-b7fa-04c20f3f14b3 | -12.74067 | -46.46782 | 2026-08-24 03:49:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5d77a620-e0fe-37df-86c2-fa9e33665228 | -7.27235 | -45.36988 | 2026-08-24 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8b61010b-271a-3070-8d1e-a8ed49baf8fc | -12.74981 | -46.44565 | 2026-08-24 03:49:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 240e515d-92c3-308a-91d8-058571353d4a | -7.19372 | -42.7535 | 2026-08-24 03:49:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 33a944a1-7829-3a47-9b9a-18b9c5e17a7b | -6.40158 | -43.82889 | 2026-08-24 03:49:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 835d0e57-dfc8-34d6-8cb0-f17fad7f8ebc | -11.23715 | -38.46186 | 2026-08-24 03:49:00 | NOAA-21 | NOVA SOURE | BAHIA | Brasil | 2922904 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f3d5003a-bbc5-3d6d-9a3a-15772eb53827 | -7.36594 | -45.7999 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 129a385c-3a36-3364-9395-09d03ec575bd | -5.63419 | -48.41849 | 2026-08-24 03:49:00 | NOAA-21 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3b83fd44-fb12-32cd-9903-f52c79816e0e | -7.25038 | -49.87946 | 2026-08-24 03:49:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 156e9943-1c6b-34b5-bb65-14ac45f56096 | -7.3711 | -45.80074 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 786140bf-ba06-3d8f-b856-089f961ca347 | -10.04477 | -46.43488 | 2026-08-24 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ba1127e2-e8d8-30bc-8562-0b2d78d6de55 | -12.74317 | -46.46556 | 2026-08-24 03:49:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| af62fd88-89b5-3d3a-b810-bbf2bac4992b | -10.73297 | -47.98103 | 2026-08-24 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 677c705b-b8d8-30bd-8e89-729c52afbc04 | -7.48957 | -45.13251 | 2026-08-24 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa7ea24e-6751-3385-a5f5-9c649bb8b5fd | -12.74547 | -46.4536 | 2026-08-24 03:49:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec830004-dbec-3c0e-b5e1-4c8eb8e126ce | -10.04309 | -46.43058 | 2026-08-24 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76f8e43b-21ca-3959-a13c-55ab5bf1cde5 | -11.57904 | -46.95327 | 2026-08-24 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e8788e36-2eac-3d0e-aee2-c0af2c4f1ba5 | -13.08978 | -43.35282 | 2026-08-24 03:49:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 43acb7d7-04ce-37a2-8cfc-ef32938d8a30 | -10.72735 | -47.9801 | 2026-08-24 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9646f4a8-e8fd-3dcb-93ba-f6d4ed1f4d42 | -12.74653 | -46.44809 | 2026-08-24 03:49:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9f94deca-ff15-3c89-96c2-f27e28251277 | -13.08581 | -43.35211 | 2026-08-24 03:49:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ce92fb58-15ed-3689-8ab8-b9246f2701de | -11.5835 | -46.95786 | 2026-08-24 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7621594-9c0f-3c11-88ab-9c294fe38a1e | -7.36539 | -45.80296 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 760a2650-95d0-3859-bc9c-b49486c2a7b3 | -8.96104 | -50.76131 | 2026-08-24 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2e11ab8b-eb5c-3d95-ac50-f96b5b22c23c | -7.1824 | -42.74369 | 2026-08-24 03:49:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a17c78b8-3d5f-3dc3-8986-2c660d1e044c | -10.45689 | -46.22033 | 2026-08-24 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0a3aebdc-cf9f-390c-a2d2-10ac816c58f6 | -7.65298 | -42.74141 | 2026-08-24 03:49:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8d9dc6b7-a3cf-3a15-b6b9-e32f6e858c66 | -7.36724 | -45.82237 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3081d053-01fa-3e21-9c61-eafdf9cbbe8b | -7.35915 | -45.80822 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d1a6ea76-21ae-3cb2-be11-f2ae00a8b07c | -7.24554 | -49.8683 | 2026-08-24 03:49:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 60e4d4fd-b1d6-37cb-86f9-2321b23e26e6 | -7.19242 | -42.76129 | 2026-08-24 03:49:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fb7aa8e6-46e5-384d-a465-3089b330ec1f | -8.59266 | -49.99231 | 2026-08-24 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0cc0f8c4-5c5c-3cd8-b7da-123b1a2e9340 | -7.89785 | -46.33072 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 89dc440f-f995-3a90-a1e9-d0e47634a1f4 | -7.14914 | -43.08948 | 2026-08-24 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d8ec6767-0b10-395f-8e5f-5a4bf52069ba | -11.59332 | -46.93438 | 2026-08-24 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36bc0d89-7e5e-3ef0-8012-31b7bab972d1 | -12.27467 | -43.19566 | 2026-08-24 03:49:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b6509e7-8903-368a-9744-b2876caffcce | -10.04421 | -46.43784 | 2026-08-24 03:49:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 52b099a9-6b1c-3192-904f-737e9eed70f5 | -7.96884 | -43.925 | 2026-08-24 03:49:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ee84f72-9a44-3393-a196-401109fce5c4 | -7.37182 | -45.82651 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0fd5ff3d-9973-3d2d-abae-e14662183e4d | -12.74806 | -46.4665 | 2026-08-24 03:49:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e759b4b3-ac37-324f-83cc-c656e4cd031d | -7.30783 | -42.97768 | 2026-08-24 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 62e547db-1e39-3b00-8eaa-ad1a5cef8862 | -7.25056 | -49.86264 | 2026-08-24 03:49:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 06ab3581-7afe-36b5-ab40-31d3f6c86be8 | -12.74882 | -46.45108 | 2026-08-24 03:49:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 56ea166e-0cbc-3bfa-8d3b-763412187fb3 | -7.65133 | -42.74151 | 2026-08-24 03:49:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0802c505-e294-3f49-b3dd-bca97127ee97 | -7.16558 | -42.74103 | 2026-08-24 03:49:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 5ca339bc-17ad-37d8-88eb-da89e979c91c | -7.39655 | -45.98945 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b76876a8-e91f-35fa-a0bb-dbfa2b704530 | -7.36154 | -45.82455 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| df1063fa-1784-3acc-8cc8-b9d4dbe65b2f | -7.44928 | -46.91838 | 2026-08-24 03:49:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 928c0d5b-7484-31d4-a923-03785c23b05b | -7.97325 | -45.25983 | 2026-08-24 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 624d6935-12af-3f6e-a7c3-368318ce735b | -9.61867 | -39.31604 | 2026-08-24 03:49:00 | NOAA-21 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| cb2f6be8-3d58-39b0-a641-ffa892de040d | -7.14843 | -43.09356 | 2026-08-24 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 703899e6-f4b0-3783-b160-be8b5c2e007f | -8.37537 | -46.47385 | 2026-08-24 03:49:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52a65701-4f12-3b2e-889d-36d671985edb | -8.09989 | -47.48223 | 2026-08-24 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 93317fd5-efb3-3eb1-85f6-c1e3a49f1242 | -7.96923 | -45.28207 | 2026-08-24 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ec670033-a6ef-30d4-87f8-697b17d04815 | -10.01517 | -46.82451 | 2026-08-24 03:49:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 794c944c-e6e1-3dc8-9546-d13d09a90219 | -7.36612 | -45.82869 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7b8fea6f-8c92-39fc-ba69-4c9d9d54dd32 | -7.89839 | -46.33213 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e830afe-065e-38bb-87ae-4910a93f127e | -11.62295 | -51.09275 | 2026-08-24 03:49:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| caef7056-2caa-30cf-807d-23e7379acf96 | -12.403 | -42.90071 | 2026-08-24 03:49:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| afbf24f3-59b9-33af-b85b-7731c4e6e3c5 | -7.24795 | -49.87632 | 2026-08-24 03:49:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| fa0922f0-df2c-3e9a-a1b0-ea34cfa98e48 | -8.58704 | -49.99496 | 2026-08-24 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9a484ac8-3155-3757-87bb-bc843f934709 | -7.65196 | -42.7377 | 2026-08-24 03:49:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dc756ae9-9718-3b77-9e69-802558fbda65 | -7.97161 | -45.2579 | 2026-08-24 03:49:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| b97769e4-b492-3fbe-996d-111416150c4e | -8.9553 | -50.75448 | 2026-08-24 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb54cbb1-1bd4-301f-9410-e584ba47f17c | -7.25129 | -49.87449 | 2026-08-24 03:49:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| 9fb3ecf6-68f7-34a5-b58f-6efd37a47596 | -8.37597 | -46.47053 | 2026-08-24 03:49:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bfe20e8d-fc83-3718-8148-b29ec58d1ff1 | -7.3643 | -45.8091 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1a504cc4-e636-343c-a685-a995b61e74c0 | -7.25314 | -49.86444 | 2026-08-24 03:49:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 515da9f7-645e-3cde-90f9-7f1ba3b9a56d | -8.10561 | -47.483 | 2026-08-24 03:49:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f9967dca-6b00-36df-a64f-74fa07710615 | -11.09987 | -38.59827 | 2026-08-24 03:49:00 | NOAA-21 | TUCANO | BAHIA | Brasil | 2931905 | 29 | 33 | nan | nan | nan | Caatinga | 4.2 |
| eb1fb832-42a8-387d-bf94-d6df8324ed53 | -6.94786 | -42.69291 | 2026-08-24 03:49:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c2bfe4f5-fc00-34d5-a2c2-8f9c499228b9 | -12.13881 | -43.39554 | 2026-08-24 03:49:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9490b95d-950a-3333-a113-3e557d87ac97 | -5.07229 | -49.37769 | 2026-08-24 03:49:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca8c937b-518f-3de7-9708-68fc76771f11 | -7.89891 | -46.32491 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 953e8ab9-8545-31c6-973c-372e83b0675e | -7.48462 | -45.13187 | 2026-08-24 03:49:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 77064759-71bd-3b22-a283-01738fb47ca3 | -7.37811 | -45.82104 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f539f359-a29c-3ce0-97c2-790778695a91 | -13.07234 | -39.9005 | 2026-08-24 03:49:00 | NOAA-21 | BREJÕES | BAHIA | Brasil | 2904308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 73729105-bd3f-3eb6-806f-eb740125cffd | -7.19307 | -42.75739 | 2026-08-24 03:49:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 9aa79a99-b305-3ae5-a239-7e7385290ce2 | -11.54877 | -46.96448 | 2026-08-24 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 777f0d28-f029-3c64-bee3-3e2e148c48ed | -7.15344 | -43.09019 | 2026-08-24 03:49:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a28e1184-bafd-3226-b057-5a5b4becb5ab | -7.37755 | -45.8242 | 2026-08-24 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README12.md)
