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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a09d6a4-9f70-38a9-9454-a42d32f04633 | -23.03247 | -52.6714 | 2026-03-28 04:19:00 | NPP-375D | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 706cb5c9-227d-32b0-b282-dcb44ecc3be7 | -17.81342 | -42.73759 | 2026-03-28 04:19:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 95c5558b-e2ec-34c5-8ce7-970a61f2a897 | -23.02802 | -52.67026 | 2026-03-28 04:19:00 | NPP-375D | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 29bcd0c2-e306-35b1-81fc-756671276491 | -17.81229 | -42.74511 | 2026-03-28 04:19:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| dfae4cbb-193c-3b56-8ebf-322ff0cc5ba2 | -24.54216 | -50.73185 | 2026-03-28 04:19:00 | NPP-375D | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| e884368e-35b7-3d5f-b4a1-1826a50a9b5a | -26.0617 | -49.3903 | 2026-03-28 04:19:00 | NPP-375D | PIÊN | PARANÁ | Brasil | 4119103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 78378a93-11dc-3dbe-8efd-8c2859181f6a | -17.81285 | -42.74135 | 2026-03-28 04:19:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 4c9ea898-e590-31d1-8850-d28af2081f77 | -31.43341 | -53.70176 | 2026-03-28 04:21:00 | NPP-375D | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 1f669bdf-ccf9-3ada-869a-e60d276af4db | -3.26866 | -52.81468 | 2026-03-28 04:34:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a43cbc79-8e51-3215-8fc0-da2a5bb97512 | -3.2752 | -51.93403 | 2026-03-28 04:34:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c599d349-4f63-3451-8acf-3d8d04ec2105 | -10.37246 | -48.30927 | 2026-03-28 04:36:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb3e0791-dcdc-3ec9-a78e-37f820e6341c | -20.89436 | -43.27 | 2026-03-28 04:38:00 | NOAA-20 | BRÁS PIRES | MINAS GERAIS | Brasil | 3108701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2f905c42-cadc-3a34-a887-55ab0db7253a | -20.8047 | -49.81209 | 2026-03-28 04:38:00 | NOAA-20 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 153d7de9-9ea5-3906-afdd-c7be6cc625b1 | -20.80527 | -49.80824 | 2026-03-28 04:38:00 | NOAA-20 | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 0bcd879b-dedb-31df-afa1-ca72a54164c1 | -21.71112 | -48.43108 | 2026-03-28 04:38:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbd6ec24-bda8-3b2b-a960-e81ba5bad969 | -18.89313 | -45.47954 | 2026-03-28 04:38:00 | NOAA-20 | PAINEIRAS | MINAS GERAIS | Brasil | 3146404 | 31 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 36cddc96-1e19-3492-a9c9-be0a7ccbb137 | -18.88859 | -45.48272 | 2026-03-28 04:38:00 | NOAA-20 | PAINEIRAS | MINAS GERAIS | Brasil | 3146404 | 31 | 33 | nan | nan | nan | Cerrado | 0.0 |
| a4f6bb5e-dd30-3911-be74-970dfe7804bc | -17.81452 | -42.74298 | 2026-03-28 04:38:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 87ff1206-bd99-30f4-8396-99fa82f268e5 | -17.81467 | -42.73947 | 2026-03-28 04:38:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 6a0a86ec-0389-330a-8c19-c6e9857e7c1a | -21.35966 | -47.06203 | 2026-03-28 04:38:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 704d14a2-2760-3fcd-8efc-cb07d96e1287 | -18.48274 | -44.80934 | 2026-03-28 04:38:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a3f2c57-2ffe-39b4-b2fd-16651ff2108e | -21.49709 | -48.76979 | 2026-03-28 04:38:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 39835c4b-0897-3877-bccd-cfb2db5d7f8a | -21.35436 | -47.0628 | 2026-03-28 04:38:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ba59329-d79c-3da3-be87-e51465f776f4 | -21.23075 | -48.5377 | 2026-03-28 04:38:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a25aaeac-b30d-335d-bbe5-48ef82fee1e3 | -21.35583 | -47.06151 | 2026-03-28 04:38:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97411c1e-717d-32d0-814b-5a2dfb621370 | -21.5436 | -48.72122 | 2026-03-28 04:38:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f1bef0d-6c95-3e21-ab46-05c44ca498b1 | -18.48327 | -44.80511 | 2026-03-28 04:38:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd2d48c9-50dc-3e6c-a88f-10de20c817a3 | -17.80976 | -42.74203 | 2026-03-28 04:38:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 8529a644-e821-3285-8842-faf9c746da2c | -17.80928 | -42.74393 | 2026-03-28 04:38:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 67a9f6a2-1bfd-3437-bf97-6e9e15e21b97 | -21.35818 | -47.06333 | 2026-03-28 04:38:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02b73724-cab0-3653-8285-c06156d999f3 | -15.60602 | -48.45684 | 2026-03-28 04:38:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 87c717a7-96b6-34bd-9f3a-26bf3db510ef | -17.20951 | -45.4061 | 2026-03-28 04:38:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9f02bdd6-f068-3fdf-b039-a06c9694bc14 | -21.7146 | -47.25574 | 2026-03-28 04:38:00 | NOAA-20 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c15e1c2d-b880-37e8-bab8-16e5959d273f | -17.81406 | -42.7448 | 2026-03-28 04:38:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| aebb8bd7-3f36-395c-8680-33940795f3b7 | -21.90456 | -48.51509 | 2026-03-28 04:40:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2da154c1-9765-3e8c-9cc7-c2c214d3fe7c | -23.03013 | -52.6726 | 2026-03-28 04:40:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 080670bf-91fb-3d1c-b076-dd0548256062 | -22.52875 | -46.02498 | 2026-03-28 04:40:00 | NOAA-20 | CAMBUÍ | MINAS GERAIS | Brasil | 3110608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3a904c25-0b76-329f-858e-f6510055fee7 | -24.54329 | -50.7312 | 2026-03-28 04:40:00 | NOAA-20 | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 0e7dba66-2c06-3187-a86e-4a7540eca827 | -24.54386 | -50.72725 | 2026-03-28 04:40:00 | NOAA-20 | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| cf9de975-4f3d-34da-8e8e-c913a2db66da | -23.40541 | -46.42042 | 2026-03-28 04:40:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bf800427-8fec-3648-969e-97297709a2a2 | -23.03075 | -52.66882 | 2026-03-28 04:40:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6f06d6e2-efbd-3ff2-802d-1e29af08e061 | -31.43379 | -53.70156 | 2026-03-28 04:42:00 | NOAA-20 | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 3.3 |
| 8b1bafd6-d44b-32ea-80fd-3a0384011378 | 0.98081 | -59.38126 | 2026-03-28 05:23:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42dde5fb-f26b-3c75-a781-475dd63aa4cb | -3.2754 | -51.93413 | 2026-03-28 05:25:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f221db8-cccd-3830-b74a-cebb7da6be27 | -15.66567 | -59.3217 | 2026-03-28 05:25:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c43b7a3f-dffc-3197-9df9-56ac67b8666c | -24.54562 | -50.73111 | 2026-03-28 05:29:00 | NOAA-21 | IMBAÚ | PARANÁ | Brasil | 4110078 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 41e0e1ca-e7a6-342a-9bc7-a88054f217d4 | -9.52491 | -47.54742 | 2026-03-28 12:06:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cb1f6d43-cafa-3c75-b45c-63b9c9063154 | -9.52619 | -47.53815 | 2026-03-28 12:06:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 97cee029-bf3c-3b0a-bac6-994ad395a761 | -9.45081 | -47.28365 | 2026-03-28 12:06:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f25ea1af-7b2f-3280-b38f-50b24a4903ad | -20.80842 | -49.80883 | 2026-03-28 12:08:00 | TERRA_M-T | POLONI | SÃO PAULO | Brasil | 3539905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.1 |
| 333a7af5-7909-326f-a0e9-5411b12abef8 | -18.9334 | -46.98274 | 2026-03-28 12:08:00 | TERRA_M-T | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 13.2 |
| b39dfd08-64ed-38e9-abfc-9123f62eae23 | -23.02967 | -52.66955 | 2026-03-28 12:10:00 | TERRA_M-T | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 29.5 |
| 6794d11f-4287-3cf0-a7f6-ebfd9e4d48af | -25.11408 | -50.68903 | 2026-03-28 12:12:00 | TERRA_M-T | IMBITUVA | PARANÁ | Brasil | 4110102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| aa64714e-fc8f-3e35-807b-5e2ed5b91cc1 | -27.01497 | -50.97963 | 2026-03-28 12:12:00 | TERRA_M-T | FRAIBURGO | SANTA CATARINA | Brasil | 4205506 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 14659ba8-2016-3cff-9c59-d359af72ac81 | -27.01634 | -50.96912 | 2026-03-28 12:12:00 | TERRA_M-T | FRAIBURGO | SANTA CATARINA | Brasil | 4205506 | 42 | 33 | nan | nan | nan | Mata Atlântica | 18.3 |
| e461c1cf-e295-3872-bb23-f67206605574 | -26.64764 | -49.5137 | 2026-03-28 12:12:00 | TERRA_M-T | DOUTOR PEDRINHO | SANTA CATARINA | Brasil | 4205159 | 42 | 33 | nan | nan | nan | Mata Atlântica | 14.0 |
| 6f7a1d43-8574-3b47-8197-efa85d5ac547 | -29.71789 | -51.74379 | 2026-03-28 12:12:00 | TERRA_M-T | TAQUARI | RIO GRANDE DO SUL | Brasil | 4321303 | 43 | 33 | nan | nan | nan | Pampa | 4.0 |


