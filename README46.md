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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 34367f28-219a-3e81-84cf-44486c5a10bf | -17.98913 | -45.94043 | 2025-08-28 04:10:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ee361756-92ba-3c99-9001-50f8f1a76a81 | -18.17467 | -45.55881 | 2025-08-28 04:10:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c3411daf-e6dc-3ad2-a339-7ec212834d45 | -17.78224 | -44.47118 | 2025-08-28 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0a0397fd-7e17-3275-b47d-30515b6dfc0a | -15.1808 | -52.328 | 2025-08-28 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 095110e0-9308-375b-a9a5-646c85f87e56 | -15.62065 | -52.71367 | 2025-08-28 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 26d3eb97-57b1-377b-b6d0-ffc637d9ebb6 | -17.73682 | -42.67973 | 2025-08-28 04:10:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 9ea9670e-c511-37f1-b746-b911bd15f726 | -18.95453 | -43.83397 | 2025-08-28 04:10:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 395a25bd-11fc-3844-9459-b05ba01c35bb | -18.14653 | -44.44497 | 2025-08-28 04:10:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22b0cf51-ce55-384d-bd75-bcf6f0c8e1e4 | -22.39231 | -43.65513 | 2025-08-28 04:10:00 | NOAA-20 | VASSOURAS | RIO DE JANEIRO | Brasil | 3306206 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| cfaf78f6-2131-3236-9595-39698aed3f65 | -14.29045 | -53.04664 | 2025-08-28 04:10:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a1fd72e-7e93-3821-b077-fea0f88664ec | -13.00136 | -56.90443 | 2025-08-28 04:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 45dea4da-c1ad-32d3-beb8-ca92055a4dca | -20.02448 | -45.55332 | 2025-08-28 04:10:00 | NOAA-20 | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09bd49a9-edcc-3547-ba48-60fc613b1d0c | -20.13858 | -47.37764 | 2025-08-28 04:10:00 | NOAA-20 | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4021ce78-d8db-36af-a2f8-bb2d3e4cbf8a | -14.28903 | -53.05378 | 2025-08-28 04:10:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 14993747-0baf-365b-a6ad-51df3c0ff11f | -17.75891 | -44.48951 | 2025-08-28 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 52736d09-cc15-3b8f-95b2-5db7af01793c | -22.67964 | -44.42443 | 2025-08-28 04:10:00 | NOAA-20 | ARAPEÍ | SÃO PAULO | Brasil | 3503158 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 43bef226-df8a-37d8-88f3-8df58aaf80c8 | -15.68082 | -52.76125 | 2025-08-28 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ae0ddf8-f675-37b0-8d95-8b6f8e158d7e | -14.35999 | -53.21431 | 2025-08-28 04:10:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 566b61f5-16c6-3d29-b430-4b3a957b42b6 | -19.24915 | -42.04568 | 2025-08-28 04:10:00 | NOAA-20 | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| f76f788c-0f1d-31a7-81f4-0fdf3e2d0be3 | -18.18749 | -45.56485 | 2025-08-28 04:10:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7db33890-24c1-37a9-8606-57a14ab9a7ae | -14.3432 | -53.35568 | 2025-08-28 04:10:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a9064797-0209-3c6a-b0f3-8014da54eb25 | -15.67653 | -52.76339 | 2025-08-28 04:10:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 17eabe80-0002-3558-8a01-c07a28374f47 | -17.91843 | -45.90409 | 2025-08-28 04:10:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83628b84-b26e-393b-b79f-ecf1d05e5673 | -16.54155 | -42.34925 | 2025-08-28 04:10:00 | NOAA-20 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ecece6cb-23c3-325b-9e72-e59ef04d0ca4 | -18.88494 | -44.71281 | 2025-08-28 04:10:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 599dbc2c-7162-3020-a703-88813459358b | -15.62376 | -52.7516 | 2025-08-28 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c66502d6-35c6-391d-9793-d7884f5e0217 | -15.2106 | -48.24797 | 2025-08-28 04:10:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 244859f9-4a25-329b-8ca2-587f5a8b91c7 | -19.11196 | -44.02199 | 2025-08-28 04:10:00 | NOAA-20 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bb1bcd1c-7097-3f5b-ac6f-06a36b7158b5 | -17.8135 | -44.51021 | 2025-08-28 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce55f93c-261d-3ab2-b5a6-d90bb3e93757 | -14.33784 | -51.9309 | 2025-08-28 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53dcfc88-2eb1-3632-926b-cb0a3520bb3c | -21.00383 | -47.37204 | 2025-08-28 04:10:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5cd13ca-5caa-3c21-bbd3-4d27ce14a0ae | -15.18014 | -52.33139 | 2025-08-28 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7081923a-e7dd-33dd-b72c-a05ceadaa3f4 | -19.62694 | -43.87438 | 2025-08-28 04:10:00 | NOAA-20 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7f0c4566-e310-3d3d-b93f-f46128ddb2f4 | -21.06413 | -45.61607 | 2025-08-28 04:10:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dac76a25-a35e-34dc-b1e7-bb36df4bfee5 | -19.89786 | -43.61112 | 2025-08-28 04:10:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1465bbfc-2a0d-39eb-879b-76524389ed3c | -19.0671 | -42.13816 | 2025-08-28 04:10:00 | NOAA-20 | FERNANDES TOURINHO | MINAS GERAIS | Brasil | 3125804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5d981c68-8cbd-3e8c-a5c5-cb26de71aaa9 | -22.24297 | -46.58194 | 2025-08-28 04:10:00 | NOAA-20 | JACUTINGA | MINAS GERAIS | Brasil | 3134905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 510d1230-51e3-3631-a2c8-89d289ed07b3 | -21.0073 | -47.37265 | 2025-08-28 04:10:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8263f8b-b98f-385e-971e-97352fced9cd | -20.14562 | -47.37857 | 2025-08-28 04:10:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b0495881-15d7-3866-8552-494143689f85 | -20.30559 | -46.03306 | 2025-08-28 04:10:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 376b8aca-f22a-370d-84e5-2ad8ae5eafd1 | -18.07389 | -44.0644 | 2025-08-28 04:10:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9bfb9bac-209b-3ae7-a791-e33d71dfb3c8 | -19.61865 | -42.7683 | 2025-08-28 04:10:00 | NOAA-20 | JAGUARAÇU | MINAS GERAIS | Brasil | 3135001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8f229f48-81a5-3bdc-894b-d5c02fa59f34 | -15.62309 | -52.75492 | 2025-08-28 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cabc85ed-952a-3499-b8fe-7e5eaaa73061 | -14.32439 | -53.27897 | 2025-08-28 04:10:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b758e04b-f095-3ac1-a1b2-6bcef910cba4 | -15.0965 | -48.54622 | 2025-08-28 04:10:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f310782e-66f9-3db1-96bd-2c1d5604afa4 | -17.76827 | -44.49488 | 2025-08-28 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f3236d62-09c5-3126-8cd7-73cd22d68a26 | -15.66294 | -52.74324 | 2025-08-28 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9cba568e-8837-3798-898f-b57086cc4051 | -19.24859 | -42.04955 | 2025-08-28 04:10:00 | NOAA-20 | ENGENHEIRO CALDAS | MINAS GERAIS | Brasil | 3123700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9e865116-b75a-3ec0-ab59-15f7bb17ace8 | -16.64577 | -46.72454 | 2025-08-28 04:10:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1549c5c-03b0-3d31-bcee-bc151ff04e22 | -15.10645 | -48.55917 | 2025-08-28 04:10:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 915cc23a-6aa0-3696-8939-638f057667a8 | -14.35908 | -52.08923 | 2025-08-28 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1e0a592-ac3d-3bbd-b2d2-63447c8ae2e8 | -20.13929 | -47.3735 | 2025-08-28 04:10:00 | NOAA-20 | RIFAINA | SÃO PAULO | Brasil | 3543600 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98a4a745-f7c0-3e02-bd70-54590a58fe94 | -17.54706 | -46.60995 | 2025-08-28 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49cf0602-4ee6-32ae-a7b2-6f11c297a2b8 | -14.26804 | -53.07479 | 2025-08-28 04:10:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c1592a3f-348f-3251-bef5-ad43fb14cc0c | -20.30621 | -46.02932 | 2025-08-28 04:10:00 | NOAA-20 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 179d5009-b340-391a-8738-bae28a3e3485 | -19.89452 | -43.61054 | 2025-08-28 04:10:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1894a72b-e52c-36be-a53a-68e488079b5e | -20.11517 | -44.33873 | 2025-08-28 04:10:00 | NOAA-20 | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 95669a47-d933-34dc-a8b7-b02da9ca7491 | -14.26733 | -53.07837 | 2025-08-28 04:10:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f7e2e482-264b-3935-aa15-daef75f8a1fc | -15.09611 | -48.61647 | 2025-08-28 04:10:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 034f223e-b01e-34fd-9e03-70bd74d96f0c | -20.67818 | -47.07489 | 2025-08-28 04:10:00 | NOAA-20 | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e16ffb70-0a3a-3771-ab77-3310eeca5501 | -15.66485 | -52.73358 | 2025-08-28 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e016c3f9-76bd-3a01-b983-5f630548e4b2 | -15.08956 | -48.51671 | 2025-08-28 04:10:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5a4d06aa-e298-3b5c-9361-ffe42b36c860 | -19.6744 | -43.33538 | 2025-08-28 04:10:00 | NOAA-20 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8ce2b22f-b747-320b-8f5a-67d3046ceec9 | -20.73002 | -45.8555 | 2025-08-28 04:10:00 | NOAA-20 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b969908-156e-3550-86e1-de5b769bcd91 | -18.20996 | -45.56447 | 2025-08-28 04:10:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 189d108c-a1b8-33f1-b786-e609d6cf3691 | -17.77504 | -44.47365 | 2025-08-28 04:10:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 99b332be-eb29-3fe0-9477-4015a939430b | -12.99878 | -56.91044 | 2025-08-28 04:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b51fb36-d005-37fd-91c2-596d7707c283 | -18.78058 | -47.18813 | 2025-08-28 04:10:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57a5a59d-4f48-368c-b889-51f8e86f6351 | -22.67688 | -44.42004 | 2025-08-28 04:10:00 | NOAA-20 | ARAPEÍ | SÃO PAULO | Brasil | 3503158 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 32054482-49bc-33ef-8125-de68cea2898c | -19.16455 | -41.83258 | 2025-08-28 04:10:00 | NOAA-20 | ITANHOMI | MINAS GERAIS | Brasil | 3133204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| fb32e3fb-a71b-3504-9cd3-6c7e3f4d375b | -19.17757 | -44.51666 | 2025-08-28 04:10:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d48bf70d-475f-394d-b641-762a810640da | -14.35849 | -52.09228 | 2025-08-28 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e245c4a7-c42b-3167-9359-943d045b3f75 | -14.34943 | -53.35303 | 2025-08-28 04:10:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8a2c092c-a356-313f-9861-ab0a93a12035 | -17.54329 | -44.37148 | 2025-08-28 04:10:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d67c2cfa-3d0d-3b9b-892b-bac2a896a842 | -18.56458 | -45.37209 | 2025-08-28 04:10:00 | NOAA-20 | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5300d6aa-1990-3f26-9495-60f50b64a06d | -15.10598 | -48.60737 | 2025-08-28 04:10:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 356b5f50-40fc-34a3-9baf-f6b5a3e917fc | -14.29587 | -53.04753 | 2025-08-28 04:10:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2957ee1-f8eb-3525-afa1-49a0514eae13 | -15.62824 | -52.756 | 2025-08-28 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4f153899-59d1-38af-bd16-1fdf75c41804 | -14.43792 | -53.19677 | 2025-08-28 04:10:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.3 |
| df2c708a-4cab-3be1-88e3-5599b0476f4f | -18.19485 | -45.22372 | 2025-08-28 04:10:00 | NOAA-20 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9863203-ffb8-3c0a-bfbf-71696ba93fdb | -18.15441 | -44.41652 | 2025-08-28 04:10:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e8e5ea31-7f3b-3407-a84b-e63354fd582d | -18.17803 | -45.55937 | 2025-08-28 04:10:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aec8d26f-ad31-3f76-9db6-780c8ad41f8a | -14.36858 | -52.09438 | 2025-08-28 04:10:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 770e7079-cc1a-35a6-a8a6-422ddd0a0e34 | -17.54782 | -46.62665 | 2025-08-28 04:10:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29277451-99bd-3f14-bcfd-200debe3ffb4 | -20.2502 | -42.00791 | 2025-08-28 04:10:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| c4a81c7f-49b3-3744-85b7-a640116add1e | -22.23239 | -42.28758 | 2025-08-28 04:10:00 | NOAA-20 | BOM JARDIM | RIO DE JANEIRO | Brasil | 3300506 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 932708c7-ec05-39ab-975d-99898c1130d7 | -16.54211 | -42.34552 | 2025-08-28 04:10:00 | NOAA-20 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a376590b-6a88-3a7a-abd0-ca0878b6835f | -19.89509 | -43.6068 | 2025-08-28 04:10:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 014630d0-9096-3068-8a67-91ffe4de11d1 | -16.37142 | -43.79365 | 2025-08-28 04:10:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d677dcb7-d4fa-311d-a5b1-d1ecf60f5aef | -15.67612 | -52.73916 | 2025-08-28 04:10:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca14c47d-b168-315e-ad3c-05ab1df14a4a | -14.35383 | -53.21688 | 2025-08-28 04:10:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a63a76c0-32c9-33d7-9b09-1ffff54be929 | -13.00968 | -56.8992 | 2025-08-28 04:10:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d9607066-d8d0-3c0b-bd8a-2465ca967f8a | -20.4349 | -46.01404 | 2025-08-28 04:10:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64c711b0-ef20-3574-b42b-6d6e40b740e4 | -18.87989 | -43.72503 | 2025-08-28 04:10:00 | NOAA-20 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 829ba43a-5894-3408-8f48-d89c0ba8d7bf | -20.55885 | -46.38317 | 2025-08-28 04:10:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 005dead3-30e4-354a-9382-20207680e902 | -18.07664 | -44.06857 | 2025-08-28 04:10:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5585e1b5-651d-365b-963d-2824a3301519 | -22.87245 | -42.78704 | 2025-08-28 04:10:00 | NOAA-20 | MARICÁ | RIO DE JANEIRO | Brasil | 3302700 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b7cdd38b-a476-3ae9-9c84-be629dec3516 | -18.85237 | -43.63713 | 2025-08-28 04:10:00 | NOAA-20 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d13f2043-8967-3208-a6d5-d7cb4688168b | -20.24958 | -42.01218 | 2025-08-28 04:10:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| f04add82-6f88-36b4-b896-8b7fc45a27c8 | -14.27413 | -53.07243 | 2025-08-28 04:10:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README47.md)
