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
| 7830518d-1758-34ad-97c9-e25488a2f03b | -17.80608 | -44.48701 | 2025-08-25 04:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d3bca71-a3f6-305a-a075-eed1a7ea311b | -18.33144 | -46.00991 | 2025-08-25 04:19:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5f4bef6b-2120-3079-803c-7bb205ff5f4c | -19.36852 | -44.21584 | 2025-08-25 04:19:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 91b83520-cbfb-38b5-ba7b-f2a3ec6db112 | -18.74721 | -43.84004 | 2025-08-25 04:19:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7cd21b97-e858-3219-85cc-ba9f54eb2cf6 | -20.04842 | -44.47426 | 2025-08-25 04:19:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 4ea77291-e2d9-33b1-a272-b016b2f6bb9b | -17.91905 | -46.08099 | 2025-08-25 04:19:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66f47a8c-3bcf-31ad-a0d4-7002b6fcd276 | -19.35335 | -46.15061 | 2025-08-25 04:19:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 117554ed-a369-3ebd-b639-ffa8602f81cc | -20.0484 | -44.47385 | 2025-08-25 04:19:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 08d6cca3-96fc-3892-8996-ec333c651e88 | -17.58214 | -48.48264 | 2025-08-25 04:19:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b20dcb8b-f5a9-31e7-bd53-033f4fee170c | -17.79652 | -44.4818 | 2025-08-25 04:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68353bbb-88ed-367e-b04c-554c3bece628 | -19.47457 | -44.35305 | 2025-08-25 04:19:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e239a18-e2db-3c19-98b6-4ad82a1308d0 | -19.91783 | -44.62832 | 2025-08-25 04:19:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 53ade231-3a0d-3166-a649-ddda0179bae1 | -18.60844 | -43.28627 | 2025-08-25 04:19:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bace684c-0ba6-3b44-aa02-6ae2d6bf6596 | -18.86132 | -46.89626 | 2025-08-25 04:19:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3a68bf24-36c7-356b-b801-0a80028d8fb5 | -19.51015 | -40.56401 | 2025-08-25 04:19:00 | NOAA-21 | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f6ab2044-6095-37bd-a915-64f72e76282c | -19.91363 | -44.62866 | 2025-08-25 04:19:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| ee04c383-b2b8-30cb-be79-eaa64056a584 | -17.57866 | -48.48194 | 2025-08-25 04:19:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4fcdac3a-a735-3927-be4e-528ee4129ea2 | -19.64294 | -46.10282 | 2025-08-25 04:19:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ed2e49fd-0bf1-3058-94a9-f67ee48d6707 | -18.71934 | -43.8204 | 2025-08-25 04:19:00 | NOAA-21 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b14f9776-a63b-35c9-bcc8-0a6b14d02793 | -17.8413 | -44.4126 | 2025-08-25 04:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 61391a74-edd8-3357-a542-292f9abaf12a | -17.59856 | -46.10788 | 2025-08-25 04:19:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16b764b4-196f-38ae-83f8-7cab0d8293f6 | -19.63254 | -43.1888 | 2025-08-25 04:19:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d1b43893-326f-302b-b2d3-38e25e9cd0ec | -19.7286 | -46.46932 | 2025-08-25 04:19:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d18b2634-43e2-3686-889c-69018b5d1738 | -19.48782 | -46.1176 | 2025-08-25 04:19:00 | NOAA-21 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 11f1200d-7ddc-3634-8bb1-420ce07819ba | -17.57863 | -48.7356 | 2025-08-25 04:19:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b5a8ba9-bbcb-347b-9f4c-cb06c00f03ba | -20.04387 | -44.48145 | 2025-08-25 04:19:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 10657548-372f-3cb2-890a-d010f02de4af | -19.36795 | -44.21978 | 2025-08-25 04:19:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8009ef88-d68b-31be-b7d4-c0edd0c55ade | -15.14358 | -59.59095 | 2025-08-25 04:19:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e635710-a281-3d47-a2b2-87bbc2cceedf | -20.16433 | -41.50164 | 2025-08-25 04:19:00 | NOAA-21 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b3f36e8b-7418-30d7-bf1e-0b1f2d094936 | -19.7319 | -46.46989 | 2025-08-25 04:19:00 | NOAA-21 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68513c5f-85d2-3950-b1ea-e54a30dd6a80 | -23.7921 | -47.51198 | 2025-08-25 04:19:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 737fec07-075e-3af4-94ce-5ad01236ec19 | -18.76773 | -48.02796 | 2025-08-25 04:19:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a4cddcab-b7ff-3ac3-b01b-4a44b961cbe5 | -20.01497 | -42.84808 | 2025-08-25 04:19:00 | NOAA-21 | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 7e8f59b0-df69-3ea2-86c9-8150049e7f66 | -19.06612 | -44.32149 | 2025-08-25 04:19:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 480e0d20-4f30-3e0a-aac6-d70b1f6a8215 | -18.38745 | -46.83645 | 2025-08-25 04:19:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cc4acd90-2957-3b18-aa4a-698d7c1d6aa9 | -19.47799 | -44.35361 | 2025-08-25 04:19:00 | NOAA-21 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 40056cc1-ea68-3c7c-b060-8bcd95f66e77 | -19.91702 | -44.62925 | 2025-08-25 04:19:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 7ebfed57-0d69-3138-9aab-d07dcc4d515c | -19.17868 | -44.51239 | 2025-08-25 04:19:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 2adacad5-ecc9-35c9-9f23-8e747b8cee0a | -18.45143 | -47.55685 | 2025-08-25 04:19:00 | NOAA-21 | DOURADOQUARA | MINAS GERAIS | Brasil | 3123502 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 79e62d6f-c394-351c-a538-a9cede29826f | -19.96247 | -42.84954 | 2025-08-25 04:19:00 | NOAA-21 | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6ffb719c-803b-3ffa-8f32-b8bdbcc4ad08 | -18.41225 | -49.26313 | 2025-08-25 04:19:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ffa97ecd-9004-3843-b753-0351d6fc6533 | -17.57934 | -48.73148 | 2025-08-25 04:19:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d755b1cb-a63b-3bc1-aa00-692bac6a3b6d | -17.60358 | -46.09761 | 2025-08-25 04:19:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2aa7dddb-498d-355d-b182-05ca187fcf42 | -15.14615 | -59.5918 | 2025-08-25 04:19:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f9d995c4-a3f9-3df2-8b24-fbc4bf465bef | -19.0701 | -44.31815 | 2025-08-25 04:19:00 | NOAA-21 | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ed7a92a8-de74-3ca6-a152-7340e5c51075 | -18.68159 | -48.18502 | 2025-08-25 04:19:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 1cf2b433-8aed-3565-abba-bd902b503f1c | -17.34443 | -47.85305 | 2025-08-25 04:19:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a90d92b-2ffc-3dc1-89f6-046b704f7788 | -17.59525 | -46.10731 | 2025-08-25 04:19:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34c0a4b6-623b-3af8-b0d4-1fcc15d2d0e0 | -18.85539 | -46.99701 | 2025-08-25 04:19:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f32c43b-c172-3616-9e5e-7840768010c3 | -20.43991 | -41.68821 | 2025-08-25 04:19:00 | NOAA-21 | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5af947d0-26eb-3343-9cfc-cd960c2d033d | -17.92736 | -46.07129 | 2025-08-25 04:19:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 881c0dae-75ae-376b-a30f-4ff3f6f65b8e | -18.23384 | -49.25686 | 2025-08-25 04:19:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f45c4b3f-9f92-3091-8167-4a3d0d4e04af | -17.84075 | -44.41633 | 2025-08-25 04:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| e6d4a6ae-6a41-39b4-97ce-de3b93652087 | -18.39078 | -46.83701 | 2025-08-25 04:19:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b53af56-027e-327e-b70e-0e79009cbb37 | -20.42545 | -42.31813 | 2025-08-25 04:19:00 | NOAA-21 | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 482b6e6e-5a77-368d-ad78-8634cffddfcd | -23.7954 | -47.51259 | 2025-08-25 04:19:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b80343ee-00cd-33d1-a7a0-dfc6155dacc1 | -17.59252 | -46.10314 | 2025-08-25 04:19:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7e73b76-d812-3d33-a272-7241d427f8c2 | -19.57201 | -41.60788 | 2025-08-25 04:19:00 | NOAA-21 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 3e95bf60-3e8b-3c06-9c71-3b6421b754d5 | -19.17812 | -44.5162 | 2025-08-25 04:19:00 | NOAA-21 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 22.2 |
| d00b73f4-b606-333f-8d07-ab2942e76c86 | -20.04784 | -44.47778 | 2025-08-25 04:19:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6721a230-cf7d-3ab5-9462-f3520aa7b23e | -19.91727 | -44.63218 | 2025-08-25 04:19:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| a471156d-cbdb-3295-aa89-a69b41233605 | -18.86465 | -46.89684 | 2025-08-25 04:19:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 64b39029-16e7-3487-a317-ae9b3d027546 | -20.04785 | -44.47818 | 2025-08-25 04:19:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3955ff65-81ab-3627-988f-39152fd04a71 | -19.9588 | -42.84903 | 2025-08-25 04:19:00 | NOAA-21 | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d1d4f2bc-23d1-3a68-836b-763e5d43dcd3 | -19.57179 | -41.60655 | 2025-08-25 04:19:00 | NOAA-21 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bb0323b3-8779-345b-9d10-09006fc82732 | -19.91645 | -44.6331 | 2025-08-25 04:19:00 | NOAA-21 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| cf21d0f9-0fc0-30d6-afb0-7d2df639a1f4 | -17.92292 | -46.07794 | 2025-08-25 04:19:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5453cf07-3713-34b2-aedb-48d1e8047011 | -19.76517 | -43.14544 | 2025-08-25 04:19:00 | NOAA-21 | BELA VISTA DE MINAS | MINAS GERAIS | Brasil | 3106002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6e72a6bd-8843-3a4a-ae94-20bc9dd00ddc | -19.63314 | -43.18443 | 2025-08-25 04:19:00 | NOAA-21 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 09e5dce5-ae5d-32f8-bfaf-e39e654dee49 | -17.59913 | -46.10427 | 2025-08-25 04:19:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7ae22b17-dc68-3131-afbb-849a413457fa | -17.34771 | -47.85303 | 2025-08-25 04:19:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd7d40a2-46c3-3249-b1af-9fd052870bba | -19.64351 | -46.09917 | 2025-08-25 04:19:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9bdefec3-d6c2-38c7-ba47-b26f349babe1 | -15.14197 | -59.598 | 2025-08-25 04:19:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f081b96e-1a89-3555-9b2a-08f64c948bf6 | -18.39019 | -46.84067 | 2025-08-25 04:19:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be544d47-8cbe-3573-b6ea-61ff00bf33d0 | -18.38686 | -46.8401 | 2025-08-25 04:19:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89066697-5242-372d-93e7-67c9c0dde9f2 | -20.04728 | -44.48204 | 2025-08-25 04:19:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 58f22d02-1531-318f-bc36-26db0d542885 | -19.69624 | -42.11774 | 2025-08-25 04:19:00 | NOAA-21 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 505f2db9-a2bf-3002-83f4-1b08b9cf643c | -20.05182 | -44.4744 | 2025-08-25 04:19:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 74c2abba-f787-3063-bf06-68f1636dffcd | -17.60027 | -46.09704 | 2025-08-25 04:19:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4df3632b-8573-3cd8-9798-2437774b10d8 | -15.14458 | -59.59887 | 2025-08-25 04:19:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42c842ef-ca1c-3d55-9f3e-a16eee746642 | -17.58288 | -48.73207 | 2025-08-25 04:19:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7fe1bc7-9689-3eda-ad7d-04a5e45c498a | -19.5757 | -41.6071 | 2025-08-25 04:19:00 | NOAA-21 | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 41965af2-2c5d-3643-97d3-983f2d85ecc1 | -20.04729 | -44.48164 | 2025-08-25 04:19:00 | NOAA-21 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 984b53fd-5b04-3ae2-8e53-6349f8b97516 | -17.58217 | -48.73622 | 2025-08-25 04:19:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0391f1f6-f842-3885-ac16-3dec3a96e677 | -17.80553 | -44.49065 | 2025-08-25 04:19:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8a4c6135-8ce0-3302-9131-1e0a75d0bb32 | -18.4107 | -49.26138 | 2025-08-25 04:19:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6c0c5845-d879-3f8f-8f11-d04d59d6c976 | -19.81207 | -42.20289 | 2025-08-25 04:19:00 | NOAA-21 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| a03c3fe3-f462-3106-8c7a-518b17d702b7 | -8.2129 | -61.3739 | 2025-08-25 04:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.4 |
| bb3852c6-5f99-3886-a6f8-5b2b48162041 | -8.9689 | -65.4198 | 2025-08-25 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 0b1e5f33-391b-3b8c-8cae-9d56c5fbef45 | -8.9874 | -65.4192 | 2025-08-25 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 78.3 |
| 020a7e03-5049-3616-8eb0-728a72fd8c09 | -9.0416 | -65.7163 | 2025-08-25 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 5aee38f3-c17e-3222-b984-681b73615d2d | -8.9875 | -65.4006 | 2025-08-25 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 15cb3b91-f18a-3a79-bae5-e0a30353e427 | -8.969 | -65.4012 | 2025-08-25 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 920519cd-6066-3f04-9723-643d2bdb2f11 | -8.0681 | -49.6951 | 2025-08-25 04:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 8069bd23-9390-37cd-bce7-11e66505c4d5 | -8.8733 | -62.4685 | 2025-08-25 04:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 7e31c79a-4ae4-30c1-91f2-e7ebbe0c1033 | -7.9077 | -63.073 | 2025-08-25 04:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 38.1 |
| aa34e110-d847-3f2e-8a6f-3cfd6f2f45e1 | -9.06 | -65.7344 | 2025-08-25 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.3 |
| d2f84a82-d123-341b-875e-7b5810711c0c | -8.0683 | -49.6738 | 2025-08-25 04:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 002f00be-fd76-3c57-9c0d-aecc96e2c22a | -9.006 | -65.4 | 2025-08-25 04:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 250913f3-46e3-30a3-8f07-58455a89b3d5 | -8.2128 | -61.393 | 2025-08-25 04:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |


[Clique aqui para ver as próximas entradas](README36.md)
