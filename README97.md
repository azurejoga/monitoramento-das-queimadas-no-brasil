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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4e36b7f3-fb42-3a84-a2aa-881cdd24abce | -16.01636 | -50.95015 | 2025-10-04 04:17:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| ddb3c063-0776-3bde-81c4-699edfeb871a | -18.63303 | -50.67331 | 2025-10-04 04:17:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 894b92b3-2693-3f78-b9bb-812943332d24 | -17.58322 | -44.4628 | 2025-10-04 04:17:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2bcb3139-36db-346d-b310-69d7dd31d508 | -16.01215 | -50.94185 | 2025-10-04 04:17:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c34b0c58-a771-325e-b9d0-84797f97e415 | -21.59886 | -45.28157 | 2025-10-04 04:17:00 | NOAA-20 | TRÊS CORAÇÕES | MINAS GERAIS | Brasil | 3169307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 292e2559-2f29-3c20-ad96-b8597e32920c | -16.04645 | -51.04342 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bd691916-97aa-38a7-9db8-aecb04bf6fe6 | -16.35776 | -47.06931 | 2025-10-04 04:17:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 013a2ead-7d6d-3a64-93a1-37ba3b61eb0e | -17.33641 | -46.65041 | 2025-10-04 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d49695b-4009-3205-90e8-6f4e48955992 | -20.59077 | -42.08923 | 2025-10-04 04:17:00 | NOAA-20 | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a9b76ff6-e2f3-373c-9873-66dfe86d61f0 | -15.22222 | -56.82178 | 2025-10-04 04:17:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c7ca95d-e653-3f99-a581-773b1a6c445d | -16.75644 | -43.96282 | 2025-10-04 04:17:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e0d31e52-cf5d-3751-9bf6-14f898ce9bd5 | -21.69069 | -50.06731 | 2025-10-04 04:17:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 74ef7dfd-531d-3d9a-a706-d6f98105e80c | -15.60885 | -46.9282 | 2025-10-04 04:17:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 635a1dda-ea95-3089-9021-95dadc974a7e | -20.14035 | -46.4197 | 2025-10-04 04:17:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 13bbdbd0-4cb4-38d1-9e47-7bd440cf46ec | -15.72261 | -46.27425 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d72bf011-b187-3b5b-b569-74c2a5a749a6 | -14.58087 | -52.49797 | 2025-10-04 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7900ba2-e27c-3c07-9972-3d044c73485c | -16.27535 | -47.10168 | 2025-10-04 04:17:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6effb44c-1afb-309d-a699-4d7e626482b9 | -19.59482 | -44.62848 | 2025-10-04 04:17:00 | NOAA-20 | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d3d8e664-4dc5-3412-b318-9f394f411404 | -17.0578 | -46.63255 | 2025-10-04 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1395b39-34a4-3756-9d14-e3a337711d3f | -20.06884 | -43.75189 | 2025-10-04 04:17:00 | NOAA-20 | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 68936fe5-7f40-3b3e-84ed-b4012f5ead3f | -21.69714 | -50.0732 | 2025-10-04 04:17:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 356d5a82-8049-32a8-a025-25568896387a | -20.9675 | -43.91995 | 2025-10-04 04:17:00 | NOAA-20 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2b1b9836-d696-3123-903c-506e9e798998 | -21.07603 | -49.3482 | 2025-10-04 04:17:00 | NOAA-20 | POTIRENDABA | SÃO PAULO | Brasil | 3540804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9f36e5de-03a3-3671-8f1f-2fc7e6a32396 | -15.53281 | -46.81738 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52ed13a5-8d01-3429-8f40-e1c36245ca26 | -19.89117 | -42.62418 | 2025-10-04 04:17:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3640946f-5362-35d5-a0f4-5392e3bea83f | -15.95807 | -43.33344 | 2025-10-04 04:17:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a6ab868-97e6-3952-97b1-cc660be19492 | -21.21771 | -45.82631 | 2025-10-04 04:17:00 | NOAA-20 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 77f66ac4-516b-3349-94df-ff698256d1e4 | -21.20662 | -46.0718 | 2025-10-04 04:17:00 | NOAA-20 | ALTEROSA | MINAS GERAIS | Brasil | 3102001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| ec70d25b-8ccb-319e-9763-531983ebe022 | -16.01223 | -50.91766 | 2025-10-04 04:17:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 774c0477-7045-3e4e-b95d-abe2cd48132f | -15.56877 | -48.18318 | 2025-10-04 04:17:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81d85313-7ee6-3ff6-a7c7-86d54dcbdd38 | -20.02791 | -45.28696 | 2025-10-04 04:17:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 726fc997-eb20-3cca-8bdf-419ea498440c | -14.99275 | -49.96041 | 2025-10-04 04:17:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| be349bcf-2fa5-3620-ba35-04e62e016614 | -16.40015 | -52.15648 | 2025-10-04 04:17:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bb931d0f-adf3-3b1d-a1e1-988f328bdcd7 | -19.68502 | -44.61203 | 2025-10-04 04:17:00 | NOAA-20 | SÃO JOSÉ DA VARGINHA | MINAS GERAIS | Brasil | 3163102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d6916f04-3fe5-33d2-8409-4693147ff092 | -14.95991 | -49.99531 | 2025-10-04 04:17:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 47c19a99-e7f0-3619-aff5-2f48b3551821 | -21.69271 | -50.07703 | 2025-10-04 04:17:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| b991f86b-85b4-30cf-9f31-a9f7a4abc4fb | -22.27743 | -46.75838 | 2025-10-04 04:17:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| d771c913-aa8e-3bbd-ae16-84d31fa60fcf | -20.72236 | -49.61584 | 2025-10-04 04:17:00 | NOAA-20 | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| eeabcb68-9319-3994-b867-224ec066f2b9 | -17.16705 | -53.03793 | 2025-10-04 04:17:00 | NOAA-20 | SANTA RITA DO ARAGUAIA | GOIÁS | Brasil | 5219407 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04a8a04e-3e28-31bd-8127-ba570791e91a | -18.59245 | -46.49545 | 2025-10-04 04:17:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 02bc5581-4e22-3845-849f-c90559792acc | -15.60377 | -52.49218 | 2025-10-04 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4be1e1eb-0f7e-3190-88ad-3382a6424f44 | -18.31463 | -44.04087 | 2025-10-04 04:17:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bfd81d95-5c74-34d3-a5f5-4ccfd72442ec | -16.3472 | -47.09089 | 2025-10-04 04:17:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba3248b6-71b7-3247-8d27-cd1c3afef5a4 | -15.70862 | -46.27568 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 089acc65-a685-3c82-b631-bd5be215faab | -15.73083 | -46.27959 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2d74620d-f7f7-3524-8d35-ab38283ee956 | -18.17396 | -53.34529 | 2025-10-04 04:17:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 593d9947-d253-3ac3-8e81-eac2fb8bec6d | -21.67903 | -50.06957 | 2025-10-04 04:17:00 | NOAA-20 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 473e861b-a3de-38e4-ae01-028ed0fe714c | -17.96024 | -44.39427 | 2025-10-04 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1aad84f2-e9f7-35a4-be36-642150a5effd | -21.49127 | -44.63952 | 2025-10-04 04:17:00 | NOAA-20 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 74cb5e20-5bbf-3d57-b13b-4bb7f07d9b06 | -19.47404 | -46.5289 | 2025-10-04 04:17:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b365121b-af8d-3552-b45f-ae5d01f28e86 | -19.45587 | -44.29054 | 2025-10-04 04:17:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b2ad307-7172-3346-a057-4351c2f93d60 | -22.36594 | -47.03363 | 2025-10-04 04:17:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 173a9fd6-4966-3446-8b9d-cee4c18131c6 | -15.5786 | -52.4731 | 2025-10-04 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 565539be-8304-35a2-affa-54602dee1c34 | -15.57959 | -52.46789 | 2025-10-04 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 70d12ad1-c772-3c71-9f82-325802dce693 | -22.12606 | -42.91358 | 2025-10-04 04:17:00 | NOAA-20 | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d353a41e-845f-394e-9075-1f2a54d99413 | -15.32103 | -47.33076 | 2025-10-04 04:17:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fc2ae650-406e-3ee9-9baf-0d104eebf186 | -15.8183 | -46.24935 | 2025-10-04 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ec2af0a5-1245-3f2e-a04b-5da8dfe79c26 | -18.17376 | -53.35778 | 2025-10-04 04:17:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 594d8cef-ca6c-397b-89e3-47fe60fd0656 | -21.18753 | -45.13192 | 2025-10-04 04:17:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 077399fe-f502-3428-806d-c3625490fef4 | -17.98497 | -45.00879 | 2025-10-04 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66cd6160-a2ac-3324-9735-c0541cab1773 | -14.99106 | -49.95859 | 2025-10-04 04:17:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae7c55cf-4585-37b3-a3a8-b55837954666 | -15.60751 | -52.47231 | 2025-10-04 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8ef9f91c-708f-3083-95fb-ee060b41fb73 | -15.71829 | -46.25848 | 2025-10-04 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91f0ec62-6bce-38e6-8e30-037f2e9390a1 | -16.01291 | -50.94563 | 2025-10-04 04:17:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 61c2e5d8-a59c-3cf2-af01-4a19725728ed | -17.08358 | -46.24145 | 2025-10-04 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9044a142-f1ed-3d99-9a04-b55b7b58537f | -20.83965 | -46.42044 | 2025-10-04 04:17:00 | NOAA-20 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc9c0a79-7cc0-34a5-8f98-57ae8fce5407 | -17.02598 | -43.44188 | 2025-10-04 04:17:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d4103001-2de7-361b-804f-aab54fcae078 | -16.00619 | -50.85653 | 2025-10-04 04:17:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6aebeb1a-b32c-3992-9651-fad37b230fe8 | -15.53008 | -46.80989 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00c495b9-cf54-30ca-b09d-2e9daf56651e | -17.14818 | -47.02708 | 2025-10-04 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a5b64f7f-2dd2-3234-a21b-b631fb2816cf | -16.73411 | -46.215 | 2025-10-04 04:17:00 | NOAA-20 | DOM BOSCO | MINAS GERAIS | Brasil | 3122470 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13c0f635-f908-39e8-b179-9d5d6afa756f | -21.68546 | -50.07558 | 2025-10-04 04:17:00 | NOAA-20 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ad28ffb7-2b5d-35ce-a693-05865f6f24e3 | -20.13489 | -43.99544 | 2025-10-04 04:17:00 | NOAA-20 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 15cf9de0-6b2e-3016-9aa4-782771d48bb7 | -18.34245 | -52.01812 | 2025-10-04 04:17:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f14d9f65-9825-3a78-9aa3-cc40be60ac69 | -16.35847 | -49.40709 | 2025-10-04 04:17:00 | NOAA-20 | BRAZABRANTES | GOIÁS | Brasil | 5203609 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8bb90ae7-b6cc-390e-b32e-70bb103deb56 | -16.01242 | -50.92538 | 2025-10-04 04:17:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| fb7ff98b-8716-3320-9881-8f829814fae4 | -16.02542 | -50.94777 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| df026bf2-8ba0-372a-94ee-f5f8feb66713 | -16.03172 | -50.93705 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2e924cb4-f973-38ac-a38b-96353678ab9f | -21.69352 | -50.07249 | 2025-10-04 04:17:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 85b9ab2f-9a96-3352-9b4a-7dc4cb876bcc | -21.06974 | -44.67672 | 2025-10-04 04:17:00 | NOAA-20 | BOM SUCESSO | MINAS GERAIS | Brasil | 3108008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b70f22c3-5fce-3524-9514-b3c99faf28d8 | -17.99715 | -48.33163 | 2025-10-04 04:17:00 | NOAA-20 | CORUMBAÍBA | GOIÁS | Brasil | 5205901 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c01d143-5177-344c-9ba0-5a16ec1e6140 | -16.35713 | -47.07308 | 2025-10-04 04:17:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 726eb252-ab62-35ea-bca3-57f9328f5237 | -17.63622 | -44.45265 | 2025-10-04 04:17:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 64de9c79-ffcf-35e3-84a4-95d36af79e20 | -17.586 | -44.46708 | 2025-10-04 04:17:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b02d9f40-9eaf-33b8-b4b5-555d9a62b54a | -15.72991 | -46.27167 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 530a5b6c-58fb-3f4f-891f-6447baa9d032 | -15.53344 | -46.81366 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e49b2b47-6e23-311b-b0a1-bbc7ec9ce649 | -19.76721 | -43.78775 | 2025-10-04 04:17:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97ae662b-f8d9-312d-bd5c-336e3e529f25 | -19.71455 | -44.12424 | 2025-10-04 04:17:00 | NOAA-20 | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86d528c7-f14b-39da-a8ae-ca2c1c65488d | -22.28405 | -46.75958 | 2025-10-04 04:17:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c5148534-fe86-3e51-ac0e-2446321a1871 | -19.88752 | -42.62361 | 2025-10-04 04:17:00 | NOAA-20 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 6824009a-24a4-30ac-b9bc-adaf1695136f | -21.12625 | -42.87904 | 2025-10-04 04:17:00 | NOAA-20 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b6c2e944-bd11-3aef-a541-d6f1f8ca99b9 | -17.08084 | -46.23723 | 2025-10-04 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 79352fd8-833b-379a-83c2-e76490301728 | -15.3245 | -47.33134 | 2025-10-04 04:17:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 619c3159-3ef2-35e8-ab1e-818509c17170 | -16.69355 | -48.88801 | 2025-10-04 04:17:00 | NOAA-20 | SILVÂNIA | GOIÁS | Brasil | 5220603 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0514126b-f0d5-3525-b580-4646460b5350 | -20.41202 | -44.13127 | 2025-10-04 04:17:00 | NOAA-20 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ac63ff47-240f-3a05-9931-f9129bc50748 | -19.51602 | -43.83151 | 2025-10-04 04:17:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a32e7c0b-2010-3a4e-93c7-10051279dc27 | -18.14088 | -51.04704 | 2025-10-04 04:17:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a25c046f-5179-3e09-93f7-70813b0976cf | -17.0875 | -46.2384 | 2025-10-04 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| daab36bb-3e77-321c-9237-c2e28525ab83 | -16.02326 | -44.28618 | 2025-10-04 04:17:00 | NOAA-20 | JAPONVAR | MINAS GERAIS | Brasil | 3135357 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 89b45518-db1d-3476-b6df-ae4679c11ad3 | -17.08181 | -46.25238 | 2025-10-04 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README98.md)
