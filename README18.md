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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 57ec5f91-353b-3d89-aa72-f074f8b8687d | -15.14458 | -44.02851 | 2025-09-10 03:25:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 399b3662-3d0c-3cbf-ae8a-f876cddb7310 | -17.12906 | -39.53826 | 2025-09-10 03:25:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5a3fb7a3-0e97-33cb-90e6-fbaf9090683f | -17.50461 | -43.72712 | 2025-09-10 03:25:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5fd94ca-947f-37c6-aa03-f96b78ce3d90 | -18.03566 | -47.15014 | 2025-09-10 03:25:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 545293eb-5975-3ac3-a368-92841dae7e1f | -17.77536 | -46.14244 | 2025-09-10 03:25:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d4cc2dc0-0972-37a3-a57f-b4ed2ea22358 | -16.29031 | -45.68921 | 2025-09-10 03:25:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34ddc755-49bc-375b-bc97-ba456cccb207 | -19.89303 | -42.28617 | 2025-09-10 03:25:00 | NOAA-20 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a613ab1c-c833-3b38-9cf1-1dbae07b17e4 | -21.30834 | -43.88767 | 2025-09-10 03:25:00 | NOAA-20 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 1616917c-87d1-3e33-a534-24217ceb01d8 | -19.99745 | -47.61497 | 2025-09-10 03:25:00 | NOAA-20 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b347de83-bd86-33fc-b42c-9f3caf47ad5e | -17.3067 | -46.75069 | 2025-09-10 03:25:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8e08cf12-7e84-3d73-b111-99c0b7f69ee4 | -17.24068 | -46.08099 | 2025-09-10 03:25:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8f941216-30e5-31d2-a3c3-a90a1f00f804 | -18.52682 | -43.28347 | 2025-09-10 03:25:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4c268d8a-2e93-3655-ada9-b2a9f774463d | -17.71218 | -44.44366 | 2025-09-10 03:25:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef2e6b02-a4dd-301e-be56-87e2296e7609 | -20.46716 | -43.95852 | 2025-09-10 03:25:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 60a13ac8-2415-3e85-9e25-c11ab6c848f2 | -19.74837 | -45.71687 | 2025-09-10 03:25:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b972e768-ab2b-3677-bc0e-6f64af945b9c | -19.73159 | -47.90691 | 2025-09-10 03:25:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fb8b8996-614f-39fe-b256-d549162cc001 | -14.59884 | -43.93201 | 2025-09-10 03:25:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 680beb6c-88b4-3f84-810e-c0087521c52d | -19.20813 | -43.06195 | 2025-09-10 03:25:00 | NOAA-20 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| f632b3aa-4030-3ad4-93d7-c106cc11a6d5 | -20.28831 | -46.25232 | 2025-09-10 03:25:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dca9badb-b5d0-3b64-9d04-2f5413c0a9eb | -15.79861 | -41.42009 | 2025-09-10 03:25:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 026b4b83-96f8-3bbb-9ffd-81eb13831633 | -16.28246 | -45.68751 | 2025-09-10 03:25:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cebe9e2f-30e1-3320-b9c8-42dd8bda22a6 | -17.33056 | -46.71396 | 2025-09-10 03:25:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea797e58-b66a-3e72-b345-83a3843489de | -18.45984 | -46.46907 | 2025-09-10 03:25:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3256e800-3594-312a-9eac-712e181a45aa | -15.79353 | -41.41906 | 2025-09-10 03:25:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 666bc855-44b9-3eeb-9ed0-72c6c9b9c239 | -20.20373 | -41.54738 | 2025-09-10 03:25:00 | NOAA-20 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 6fd03eef-10e5-3320-86fb-930c493e3ead | -20.05892 | -47.53712 | 2025-09-10 03:25:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2a009966-d604-384f-aef7-f0ccf13f3635 | -15.22378 | -44.04188 | 2025-09-10 03:25:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 23610610-4a04-391d-8421-70e8776bf976 | -23.3866 | -45.9688 | 2025-09-10 03:28:00 | NOAA-20 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 81f22b33-5b98-34d2-b47e-38ec1b7e008d | -23.35695 | -47.20573 | 2025-09-10 03:28:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 7f2811d6-d285-3e49-a91c-7eccde6fd5d0 | -23.35941 | -47.19566 | 2025-09-10 03:28:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a7f55182-7bbf-3aad-be5d-9d6181597470 | -23.35819 | -47.20063 | 2025-09-10 03:28:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c9743aaa-6b67-3bde-a7cb-43dbc650cc81 | -22.6792 | -47.46902 | 2025-09-10 03:28:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 77c99cce-5048-3eea-8931-c8316dc4cf3f | -22.56816 | -48.56414 | 2025-09-10 03:28:00 | NOAA-20 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1311b939-39fd-37b1-9731-96d1176015e8 | -23.1991 | -47.35073 | 2025-09-10 03:28:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ffd2babe-d3cb-3048-93d4-da79aeb6b3e9 | -23.39219 | -45.96819 | 2025-09-10 03:28:00 | NOAA-20 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a34346c3-593f-33d9-9e08-c5909be6da14 | -23.32114 | -46.87727 | 2025-09-10 03:28:00 | NOAA-20 | CAJAMAR | SÃO PAULO | Brasil | 3509205 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4a5eb7ba-e03a-3196-8632-a37da8e05909 | -23.38652 | -45.96635 | 2025-09-10 03:28:00 | NOAA-20 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ca20cca6-9768-3dbb-8840-61416811e8eb | -23.39228 | -45.97062 | 2025-09-10 03:28:00 | NOAA-20 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ba8cbfd8-4624-3d14-a8e3-d817a161dafd | -22.62574 | -44.63533 | 2025-09-10 03:28:00 | NOAA-20 | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| e604dbc5-63c9-32c0-b36f-2b116e9f1bd2 | -23.29531 | -45.47662 | 2025-09-10 03:28:00 | NOAA-20 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 3fed4862-77e2-33e2-bf68-9cf088ddb328 | -23.29425 | -45.48113 | 2025-09-10 03:28:00 | NOAA-20 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 126c682c-236c-30ee-9970-189318ee6c06 | -23.2986 | -46.16182 | 2025-09-10 03:28:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 511fb40a-5aad-39b6-b2a6-33daf0a8b77d | -23.39326 | -45.96639 | 2025-09-10 03:28:00 | NOAA-20 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a3ba1c8b-1943-3b56-ad40-5be803cae52f | -23.3044 | -46.16345 | 2025-09-10 03:28:00 | NOAA-20 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c350198e-ef34-3ee2-ac82-6c0d42138bfa | -22.67862 | -47.4664 | 2025-09-10 03:28:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 483579e5-765d-3c34-8cb3-57b5cccf1fc9 | -23.38759 | -45.96452 | 2025-09-10 03:28:00 | NOAA-20 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 98443151-a7cf-3e3c-8d35-847dd5163d29 | -22.77621 | -45.35818 | 2025-09-10 03:28:00 | NOAA-20 | GUARATINGUETÁ | SÃO PAULO | Brasil | 3518404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4d6a38f0-f121-3b4e-a915-a49b333ca1c1 | -8.0602 | -48.6856 | 2025-09-10 03:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 154.8 |
| 01b46c51-5009-372a-b23a-45a5094ae218 | -18.0218 | -47.1319 | 2025-09-10 03:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 60.7 |
| e28e6d99-672b-374e-be65-bb328f24cfd1 | -8.0604 | -48.664 | 2025-09-10 03:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 79.4 |
| fb347a3a-b8f3-329a-b17f-676654aa1a0e | -18.0212 | -47.1551 | 2025-09-10 03:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 53.5 |
| e2d48263-12ab-3a86-812a-1a29f6a3a66d | -18.0412 | -47.1509 | 2025-09-10 03:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 52.5 |
| e411b08c-df52-3cf3-8677-55ad5fd7b6ad | -20.4756 | -43.9435 | 2025-09-10 03:30:00 | GOES-19 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 92.1 |
| 523f7573-17b4-38e0-9ed3-9bec09551ab2 | -12.9292 | -54.7538 | 2025-09-10 03:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 6d8d4109-674b-39a0-bf6c-d65e2bdd7b3b | -8.0414 | -48.6873 | 2025-09-10 03:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 208.3 |
| 112106a9-e52c-3d6e-8b6d-f3dd119537f8 | -8.0416 | -48.6656 | 2025-09-10 03:30:00 | GOES-19 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 1f3a9114-856c-3bab-9b25-e1115c8cb0e7 | -12.9292 | -54.7538 | 2025-09-10 03:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 28e7d083-a79b-3d3b-b46f-aebfd606e52e | -18.0218 | -47.1319 | 2025-09-10 03:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 5df07299-8634-3b89-b6bc-98b6c5c9a1a8 | -18.0212 | -47.1551 | 2025-09-10 03:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 10661d9d-b9fd-3e64-90b9-d55b06493ef5 | -20.4756 | -43.9435 | 2025-09-10 03:40:00 | GOES-19 | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 67.3 |
| 6fd6777b-b31c-38f2-94a3-f26264a4c1b6 | -12.012 | -50.9891 | 2025-09-10 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 100.8 |
| dadcf28b-2548-38ea-b370-ae67e6e95003 | -12.0117 | -51.0104 | 2025-09-10 03:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 61bb16cc-a4ba-389d-95df-60a5173ba5a3 | -12.9292 | -54.7538 | 2025-09-10 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| ea8ae462-8d65-3c6c-bafa-d562a726283b | -1.19864 | -46.15234 | 2025-09-10 04:12:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cedea079-a297-3b54-bf41-f7fdf5d75f4e | -6.17263 | -41.04646 | 2025-09-10 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 13f08229-3b83-344c-b59c-dff922774fd6 | -8.06783 | -48.67092 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3fd5bc2-02af-3a15-b8c2-91bdb3639dc3 | -6.45549 | -43.04071 | 2025-09-10 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff873e7c-ae33-3dee-bd1a-03993c50d8fb | -5.71631 | -45.41471 | 2025-09-10 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ebc03231-075a-3d2d-b246-f9c3cd4385dc | -5.42259 | -45.88002 | 2025-09-10 04:14:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 697b8ed1-c272-3684-aff8-a07fa3462e74 | -6.29836 | -44.21258 | 2025-09-10 04:14:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e57d5ea0-f7fb-33ad-a0b1-4de36dc8fbec | -7.70626 | -44.77543 | 2025-09-10 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48f2fde1-1fef-3128-af19-28f535966806 | -5.54416 | -45.57397 | 2025-09-10 04:14:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69e28531-31a3-35ea-9707-f1113e6f3d9a | -5.58959 | -42.90028 | 2025-09-10 04:14:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9b569550-9054-39f2-a552-e9ab3ce1865f | -6.62541 | -43.99586 | 2025-09-10 04:14:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf827b2a-ab6d-3857-a2e9-43989f3a768f | -5.50902 | -42.6759 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 9ea12f35-11fa-3d9e-863d-c8d54855fac8 | -8.0553 | -48.67178 | 2025-09-10 04:14:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d1b6535a-6d9d-359b-9bf8-cd442408701d | -5.94186 | -42.77926 | 2025-09-10 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 538dbf90-ba40-3343-8158-37549f7311ae | -7.89075 | -46.2607 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 93bcb68e-1432-3c84-9823-d15b44c8cc79 | -6.20492 | -43.294 | 2025-09-10 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 458e3b46-bacb-3abf-bc4c-72fc266ad335 | -7.86259 | -46.2529 | 2025-09-10 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 970f8f40-9e9e-36ce-aba1-0c07c06261ab | -6.20614 | -43.545 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70e4ee01-4730-3bba-8edc-a3ad313f111e | -6.31477 | -43.41766 | 2025-09-10 04:14:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f228e11f-04e7-363f-b044-f63835c09efa | -6.19762 | -41.04178 | 2025-09-10 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 1db666d0-4c05-3346-bbad-8c17cdba632c | -5.96026 | -45.8072 | 2025-09-10 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d127cb20-4e4d-31ec-a8e8-a9b5a2cacdf7 | -6.24813 | -43.40664 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 744b083e-1572-349b-93f8-75aeffacedfe | -9.69154 | -46.81488 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 92bdc490-e3ef-31df-96eb-56ca97cc629b | -3.49218 | -51.25119 | 2025-09-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb1ace1a-8424-34cf-8841-b3d1344d4944 | -6.39731 | -44.38383 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12f4df43-d33d-385e-82a8-69eab4101cd9 | -5.72567 | -43.89553 | 2025-09-10 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e1181a55-0d18-364e-bebf-a17951a11c68 | -6.48498 | -42.41286 | 2025-09-10 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bb1cb1f2-b554-34e0-a3dc-675943ec4334 | -6.20945 | -43.54552 | 2025-09-10 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86291e14-dbad-3076-b244-d2d803c6a3b7 | -6.56432 | -43.14957 | 2025-09-10 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc2f856b-ef80-3f49-a88d-d7a75e5ae749 | -6.40186 | -47.33554 | 2025-09-10 04:14:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 674e5e96-e907-3b9b-b580-4e0067a8088d | -9.45023 | -46.71494 | 2025-09-10 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 54fbcb72-f2d4-3d94-a8c7-4aa44feb77de | -9.06382 | -45.75038 | 2025-09-10 04:14:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e8d34883-95cc-33f3-aae1-abfa86b8412f | -9.83106 | -46.04665 | 2025-09-10 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6850f3e7-a8b0-30bb-a103-076ce0117c19 | -9.05989 | -49.81403 | 2025-09-10 04:14:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ecfca31f-b67d-3d52-bdd5-974a6aefe4ee | -6.42536 | -44.43958 | 2025-09-10 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41322d82-4858-33d1-8a74-ac9f4a90eb9c | -8.85318 | -47.27488 | 2025-09-10 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8f6f50fe-4178-390a-8d4f-c4a809f65e2b | -8.83794 | -48.09204 | 2025-09-10 04:14:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |


[Clique aqui para ver as próximas entradas](README19.md)
