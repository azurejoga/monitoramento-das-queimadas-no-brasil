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
| 49c0f251-20e7-3fe2-9994-4afe43832cc9 | -17.90234 | -44.19914 | 2024-09-26 04:08:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c6bcd1d9-d0f2-3491-b5b9-0ec593225cb7 | -17.89067 | -43.99403 | 2024-09-26 04:08:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 30b388de-0151-323f-91e1-941e3d19e605 | -17.84791 | -44.45816 | 2024-09-26 04:08:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b13c8fe1-9581-3198-b729-6d5453383848 | -17.69975 | -44.21323 | 2024-09-26 04:08:00 | NOAA-20 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b711c477-a22b-3cd5-bdcf-1dbb2ccfaf31 | -17.09521 | -43.80421 | 2024-09-26 04:08:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2963df99-297f-32bf-a660-4db3a8ef12ec | -16.68165 | -43.88622 | 2024-09-26 04:08:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a37a6fff-0360-324a-b689-d5f4f8dfb5a2 | -17.79636 | -43.24572 | 2024-09-26 04:08:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 150580f5-e892-38e6-9bb9-10de440719dc | -17.7958 | -43.2494 | 2024-09-26 04:08:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 339a31f4-c6ba-38e2-8141-a533f915bed7 | -17.79247 | -43.24887 | 2024-09-26 04:08:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8beee73a-660f-303c-ab4d-7c00bc092d49 | -17.79026 | -43.24104 | 2024-09-26 04:08:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a9a6ab32-cabf-3832-8c93-488cc6f0e76c | -17.7897 | -43.24468 | 2024-09-26 04:08:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76dde0d2-c5c0-30da-9232-2cd20a3cc1e4 | -17.59678 | -43.19807 | 2024-09-26 04:08:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb959d13-2c51-3fb9-ad55-6286698a023d | -17.26512 | -43.16986 | 2024-09-26 04:08:00 | NOAA-20 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 52086969-cb06-3859-963e-4e9cf8e1a097 | -19.57731 | -43.53108 | 2024-09-26 04:08:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Cerrado | 15.9 |
| cb642ff3-2302-3f75-9014-e2a465bd941f | -19.57674 | -43.53482 | 2024-09-26 04:08:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 9ef901eb-3a2e-36ac-9b08-e762c58c2408 | -19.57617 | -43.53854 | 2024-09-26 04:08:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| c8110e36-b3c7-386e-b16f-0345b64cb267 | -19.57561 | -43.54224 | 2024-09-26 04:08:00 | NOAA-20 | NOVA UNIÃO | MINAS GERAIS | Brasil | 3136603 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 286243e7-6d35-3e06-ae6e-d23c87b32068 | -19.57397 | -43.53056 | 2024-09-26 04:08:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8652bb39-c574-307f-b8ce-085e4157d949 | -19.56285 | -43.53628 | 2024-09-26 04:08:00 | NOAA-20 | NOVA UNIÃO | MINAS GERAIS | Brasil | 3136603 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 385ada20-b914-3678-a451-03faeb5470a9 | -19.37217 | -44.15892 | 2024-09-26 04:08:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc07fbbc-e94f-3b0b-9b28-ccc4188760de | -19.24262 | -44.35736 | 2024-09-26 04:08:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ab2fb852-f23d-3c6e-b19f-fffa5484f042 | -19.24204 | -44.361 | 2024-09-26 04:08:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91e1a90f-1bfa-3ad6-b5d7-f129878c216e | -19.20277 | -43.74011 | 2024-09-26 04:08:00 | NOAA-20 | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9495e81c-4093-388b-9a05-348edd4a880c | -19.11149 | -44.5218 | 2024-09-26 04:08:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8af0b27a-8cec-3823-a661-3a643719b574 | -18.84066 | -43.75501 | 2024-09-26 04:08:00 | NOAA-20 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3e8eb215-6e1a-3b82-b008-989c3611785c | -18.67114 | -43.86464 | 2024-09-26 04:08:00 | NOAA-20 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1e4d225-3f48-3507-b6ac-bcaa27838c06 | -18.28707 | -44.04223 | 2024-09-26 04:08:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02e81101-10e1-3f9d-9b41-0ac475da5e54 | -18.2865 | -44.04585 | 2024-09-26 04:08:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d52f135a-a69d-3ea5-831f-7387582adf35 | -18.28319 | -44.04528 | 2024-09-26 04:08:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ee6843e9-c76c-35cf-810c-647c2d4b8902 | -18.28263 | -44.0489 | 2024-09-26 04:08:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f92ea35c-a043-353e-9243-aaf0e2ca41fc | -18.28045 | -44.0411 | 2024-09-26 04:08:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f5bad5af-aa0e-320a-a020-5e80f4c0cdfc | -18.27988 | -44.04471 | 2024-09-26 04:08:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 28c5cd2f-5c07-338d-9607-3919f6c281b9 | -18.21737 | -43.94481 | 2024-09-26 04:08:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35ce2be1-42ed-34b0-9258-372d5d442a29 | -18.04833 | -44.35067 | 2024-09-26 04:08:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aacda71b-1002-3395-bcfe-dcd367c6027f | -18.04776 | -44.35428 | 2024-09-26 04:08:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57bbc454-af72-30c5-b259-b08f7d47a767 | -18.04502 | -44.3501 | 2024-09-26 04:08:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52a40833-0543-3e10-9b3b-e72cc4abdb44 | -18.02936 | -44.38451 | 2024-09-26 04:08:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 338dd8e2-8dd5-3a7e-9275-32e483f6eb28 | -18.02922 | -44.40676 | 2024-09-26 04:08:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b98153a8-94cc-3362-8bc6-a8620889cd5f | -18.02878 | -44.38813 | 2024-09-26 04:08:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64f7a12e-9554-3483-80a5-19ff0a308829 | -18.0249 | -44.39117 | 2024-09-26 04:08:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d45b97e0-2c2e-3bf3-a0d7-9f03f5cfa4ef | -18.01524 | -44.34489 | 2024-09-26 04:08:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f8f709d1-a89b-37a3-82b9-bb943fca950f | -18.01466 | -44.34852 | 2024-09-26 04:08:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2030d0bb-aeb2-3cd8-ac89-b858692655f9 | -18.01193 | -44.34432 | 2024-09-26 04:08:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3523032d-0758-3bf9-bf88-5399327dd3bc | -18.00862 | -44.34375 | 2024-09-26 04:08:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95b540e3-6a81-31f6-9ca8-d5271acca960 | -17.99177 | -44.47105 | 2024-09-26 04:08:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| afd1668b-b586-3c95-8c99-f5f39a5f3c79 | -17.98962 | -44.46321 | 2024-09-26 04:08:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e3338ad-27ab-314e-92c9-7174d5786ae7 | -17.98904 | -44.46684 | 2024-09-26 04:08:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ea46210-beb7-310b-9c40-75a71c96ca2a | -17.98846 | -44.47047 | 2024-09-26 04:08:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c93dfa8-2798-3cb8-8ff0-a701d23d3dd9 | -17.98788 | -44.4741 | 2024-09-26 04:08:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de788b53-4b6e-3c67-8ac4-a698aa9300fd | -17.98631 | -44.46263 | 2024-09-26 04:08:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 90086205-9e03-3820-a0ba-79d0ef379508 | -18.86243 | -43.4394 | 2024-09-26 04:08:00 | NOAA-20 | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f91c6021-9b90-3bd1-bf49-5cdaffc27c71 | -18.86024 | -43.43141 | 2024-09-26 04:08:00 | NOAA-20 | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| ff2ccd74-a0c1-3d97-8bbc-4882ec98c50b | -18.85967 | -43.43513 | 2024-09-26 04:08:00 | NOAA-20 | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| a6849ab5-cf96-31e9-9fae-9423743d4a37 | -18.8591 | -43.43882 | 2024-09-26 04:08:00 | NOAA-20 | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7e81073c-7ff5-3729-a7f7-0d8be5a44300 | -18.8065 | -43.62591 | 2024-09-26 04:08:00 | NOAA-20 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 606080a3-019c-3724-8d12-e630e3e91efa | -18.61849 | -43.41398 | 2024-09-26 04:08:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 222900e6-847c-381e-b02c-4ea88be29b34 | -18.61794 | -43.41762 | 2024-09-26 04:08:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 72278136-d119-3e9e-a279-1acfee4e9253 | -18.61461 | -43.41706 | 2024-09-26 04:08:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b360e634-8d76-3904-90b6-37780d36c812 | -18.61128 | -43.4165 | 2024-09-26 04:08:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8935626b-5394-3854-838b-13914507a66f | -18.33093 | -43.209 | 2024-09-26 04:08:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 6375e27c-f9cd-37c7-9bb7-f9f939e27d5a | -18.90512 | -43.2496 | 2024-09-26 04:08:00 | NOAA-20 | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e94d0010-001c-323a-8b00-4bda4dc8f95a | -20.18897 | -43.74543 | 2024-09-26 04:08:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| dfdd36d5-8bbc-3b5d-8dcb-c76c56564832 | -20.18564 | -43.74487 | 2024-09-26 04:08:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 21ce6fbe-b751-3a04-be09-414b30f99597 | -20.18537 | -43.54342 | 2024-09-26 04:08:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 06f6f2c9-db8b-391a-8a58-ac143f91ad4b | -20.1826 | -43.53904 | 2024-09-26 04:08:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| bbe13a9f-9382-3b01-ae5e-6ddbeb60d07d | -20.18034 | -43.55405 | 2024-09-26 04:08:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c0be3005-1fff-3684-a14f-ff9293bef8b3 | -20.1798 | -43.55766 | 2024-09-26 04:08:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 89c9929f-1727-3754-a0b5-bc9041b98e28 | -20.17645 | -43.55716 | 2024-09-26 04:08:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9eaa8b85-65d2-30df-a96f-0f012da30dd3 | -20.17366 | -43.55299 | 2024-09-26 04:08:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 65655c26-7313-3548-91c8-bf65a57a75a6 | -20.17311 | -43.55664 | 2024-09-26 04:08:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 7593cd42-d316-3204-a2cf-f9a980685908 | -20.17256 | -43.56023 | 2024-09-26 04:08:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 1af73c9a-8309-33e1-b2dc-3f4b97bdc16b | -20.16923 | -43.55968 | 2024-09-26 04:08:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 47fb6927-e67a-37d3-acca-ba55a0168319 | -20.16868 | -43.5633 | 2024-09-26 04:08:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e1654de7-0569-31ca-b023-5aae5b3315eb | -20.16699 | -43.55181 | 2024-09-26 04:08:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9fe3c29a-b6ea-3815-8d08-5a85737b6030 | -20.16589 | -43.55912 | 2024-09-26 04:08:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 539460ea-eea3-3a19-a555-ecaeaec8eea3 | -20.16534 | -43.56274 | 2024-09-26 04:08:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0784cc7c-5ef4-39bb-a605-50fbe081ca29 | -20.16255 | -43.55853 | 2024-09-26 04:08:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 13c93c3d-3974-3aaa-8b7e-1ed434613f20 | -20.16254 | -43.52103 | 2024-09-26 04:08:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| f0f4de4b-f8d6-3b2c-a1e4-ddeb83b878b4 | -20.16195 | -43.52485 | 2024-09-26 04:08:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| a1a417db-c2de-33ac-8a12-6ff9c876655c | -20.16068 | -43.5556 | 2024-09-26 04:08:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| b2f2f579-e09c-33d8-bd40-558a761acc64 | -20.1592 | -43.52045 | 2024-09-26 04:08:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 33f073c2-fb9a-339d-9cab-c3e5e4970891 | -20.15803 | -43.52812 | 2024-09-26 04:08:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e23ab6bd-2b52-3063-bd00-c840854ccf7e | -20.15744 | -43.53193 | 2024-09-26 04:08:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 968ea776-c507-335c-8658-38c996b6bdfd | -20.15587 | -43.51986 | 2024-09-26 04:08:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 72c30aaf-d6b3-3299-8581-d85c189780c3 | -20.14975 | -43.515 | 2024-09-26 04:08:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1955d679-0a1a-36c2-a777-565b837e01b0 | -20.14699 | -43.51065 | 2024-09-26 04:08:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4045453b-7f92-3be1-a9c9-1d6f831558dd | -20.14676 | -44.35065 | 2024-09-26 04:08:00 | NOAA-20 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 1c66bb65-78ea-324c-a465-b934020e4123 | -20.14573 | -44.33543 | 2024-09-26 04:08:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f7067bf8-74e4-374e-96d9-e893aac4f8c3 | -20.14515 | -44.3391 | 2024-09-26 04:08:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 1c1db9fa-7f5c-3823-9d20-cbcf499a5d27 | -20.14344 | -44.35008 | 2024-09-26 04:08:00 | NOAA-20 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 6551fa14-1042-3118-89ff-e7862544e62a | -20.14013 | -44.3495 | 2024-09-26 04:08:00 | NOAA-20 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 36b6d995-edb4-30d4-9c54-07eeaf083ce2 | -20.13789 | -43.59317 | 2024-09-26 04:08:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c24c18ed-febc-336d-b6be-8df6f2639542 | -20.13401 | -43.59621 | 2024-09-26 04:08:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 44f41eda-a70a-388a-bee4-8f7870935e0d | -20.13351 | -43.5317 | 2024-09-26 04:08:00 | NOAA-20 | SANTA BÁRBARA | MINAS GERAIS | Brasil | 3157203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 2f0179dc-74a0-3018-9325-6e2b3a4126dd | -20.12836 | -44.27215 | 2024-09-26 04:08:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5b68c9e2-7d5e-3ea8-b224-758b88fd4403 | -20.12779 | -44.27583 | 2024-09-26 04:08:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d660fb93-1840-3842-9292-8713e607eb01 | -20.12619 | -44.26425 | 2024-09-26 04:08:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4cb9e86b-697b-32c2-a049-ae552ad781e9 | -20.12562 | -44.26793 | 2024-09-26 04:08:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| f78c3d15-1b01-3759-a0cb-4e15c02ba732 | -20.12447 | -44.27527 | 2024-09-26 04:08:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a1bafb21-d199-396f-9353-06032f0abdbf | -20.12391 | -44.27894 | 2024-09-26 04:08:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |


[Clique aqui para ver as próximas entradas](README70.md)
