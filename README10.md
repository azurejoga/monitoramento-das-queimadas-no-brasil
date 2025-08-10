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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d0026f5-9fc5-3dc3-ae6a-c4383affd5f4 | -4.95645 | -47.59875 | 2025-08-10 03:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e7664dcf-3217-3354-b5dc-e5a4e896abb2 | -12.6462 | -44.51055 | 2025-08-10 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da8b4e72-df5b-3a09-bb2e-1f9673861c9a | -8.98711 | -45.68068 | 2025-08-10 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d5ed423e-4a0b-3b6b-b1fb-44211e0cff4a | -8.49742 | -44.75573 | 2025-08-10 03:55:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 38878060-fd27-30f0-bc12-7d042ddb0e12 | -5.47295 | -44.70178 | 2025-08-10 03:55:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| a2223e7d-0aba-39c5-a89c-e5cb7ce10201 | -4.95701 | -47.59546 | 2025-08-10 03:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ee0f47b9-357c-3e14-8aa0-dfa2f6ae53ac | -9.49825 | -46.30037 | 2025-08-10 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11ba4ddc-109c-3e8d-a95c-9a034d488032 | -6.40432 | -38.26874 | 2025-08-10 03:55:00 | NOAA-21 | PARANÁ | RIO GRANDE DO NORTE | Brasil | 2408607 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6cb1b6b7-3138-3a21-8f98-926d5200f0b0 | -10.34191 | -44.90773 | 2025-08-10 03:55:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2cdd3887-19bb-3e74-b036-af1f8df02294 | -9.49449 | -46.29485 | 2025-08-10 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c791f0dd-2996-3460-a007-e4a05812175a | -12.64533 | -44.51555 | 2025-08-10 03:55:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6490c394-234a-3633-902e-20ec6f1119a6 | -7.73013 | -45.53943 | 2025-08-10 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94afb318-160a-3ce8-924c-62c0f83f19ef | -6.57893 | -44.56851 | 2025-08-10 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c6881bcf-c27e-3132-a665-4d2e52c5eb71 | -6.96532 | -44.48707 | 2025-08-10 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| b42a3b40-039c-3c83-9172-0c5d9945ea6e | -12.40431 | -44.21495 | 2025-08-10 03:55:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 291e7c44-9f33-3472-962e-7ef5f244af77 | -12.57665 | -41.28549 | 2025-08-10 03:55:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0ddf8517-2a0c-3cdd-851a-c69bd9c3123e | -6.1889 | -45.44732 | 2025-08-10 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6db66417-d699-345a-bbd7-b77776bf293c | -7.88197 | -45.55592 | 2025-08-10 03:55:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bd749cea-c44e-324a-bbb2-a7bd8ab54f64 | -8.32793 | -44.98451 | 2025-08-10 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4be04172-013c-3362-ab28-9a2ea6cf667b | -6.19506 | -45.43867 | 2025-08-10 03:55:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| bf3a22c2-7859-3d50-96c7-200270798a62 | -9.48782 | -46.27907 | 2025-08-10 03:55:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 29fb2687-2617-3b50-b559-bd607a3cfd53 | -12.57448 | -41.27763 | 2025-08-10 03:55:00 | NOAA-21 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| aecf4a94-4c41-3162-8934-2b401c6289a0 | -9.65972 | -46.7604 | 2025-08-10 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02d0144c-c2ec-3d79-9387-40e11c05b7bf | -10.46342 | -47.94453 | 2025-08-10 03:55:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a137142e-14a1-3be1-b210-d77c8ec78290 | -11.49084 | -50.28151 | 2025-08-10 03:55:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5ce1563-b7c4-340c-9436-234b715d1e48 | -9.52493 | -45.39801 | 2025-08-10 03:55:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90aa58cb-c74c-3bcb-98f8-e2a010386d23 | -13.63409 | -48.99688 | 2025-08-10 03:57:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 97f6185d-d775-37a5-8ce0-54dcb86d57a8 | -18.24476 | -42.58138 | 2025-08-10 03:57:00 | NOAA-21 | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ffe882a7-4bdb-368b-91d5-66bdc8b0e054 | -14.5923 | -47.15652 | 2025-08-10 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed8b6fe5-7576-38f3-82b7-6a5c985727d5 | -16.38083 | -42.53802 | 2025-08-10 03:57:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 25.7 |
| d305c834-c864-3d32-b1f4-208c2333512c | -14.79916 | -40.66526 | 2025-08-10 03:57:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c1435781-6360-3253-91ba-c651442af9ee | -16.38205 | -42.53059 | 2025-08-10 03:57:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 157bd9ff-0739-3e5e-acef-6c5341fc84c9 | -15.09244 | -46.54195 | 2025-08-10 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c65e1343-11cd-3e6b-989c-3dfd2f04edb7 | -20.27364 | -44.25938 | 2025-08-10 03:57:00 | NOAA-21 | BONFIM | MINAS GERAIS | Brasil | 3108107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7056c32b-9a9f-37e9-ba23-c0c50a205b57 | -16.37003 | -42.54009 | 2025-08-10 03:57:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 86c469b6-c417-30eb-b8bb-4ede7fb1ec76 | -18.79216 | -43.80379 | 2025-08-10 03:57:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 965ded9d-e4e8-3962-8b25-5cfd9c58ab60 | -14.29255 | -51.9868 | 2025-08-10 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 602098cb-7660-3d83-ac6a-f5922965d3eb | -14.28433 | -51.96516 | 2025-08-10 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cff153d5-d0aa-3288-b340-3404cba671dc | -12.68994 | -48.20238 | 2025-08-10 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dca20cf0-a78b-3274-af55-f76c40177425 | -16.27092 | -45.03846 | 2025-08-10 03:57:00 | NOAA-21 | ICARAÍ DE MINAS | MINAS GERAIS | Brasil | 3130051 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd33ac00-9f2c-3534-9324-002ae78841e3 | -20.60442 | -42.15312 | 2025-08-10 03:57:00 | NOAA-21 | DIVINO | MINAS GERAIS | Brasil | 3122009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8da578a4-d39e-3f5f-954a-efc7cfb825de | -14.45007 | -47.85867 | 2025-08-10 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aad8a6d0-a51c-3188-b3c6-8abced13dc64 | -18.17134 | -46.99573 | 2025-08-10 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e8959e0a-ff64-3490-a97f-130bb1ef027b | -20.17276 | -43.71499 | 2025-08-10 03:57:00 | NOAA-21 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| f8067233-2404-37be-a962-9c7d9452acc9 | -14.11929 | -45.40895 | 2025-08-10 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 84247ab8-5dbf-3562-b7c9-b0e8eb225fca | -14.28557 | -51.96275 | 2025-08-10 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2549f306-6c51-38cf-bdbb-6984d2f8267f | -18.79365 | -43.80486 | 2025-08-10 03:57:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49022f4c-a788-36e4-a099-9591595023e1 | -13.77602 | -48.87925 | 2025-08-10 03:57:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3ce4838b-a354-3139-9dd8-7036ebe7317c | -16.05484 | -45.02713 | 2025-08-10 03:57:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12059afd-3c23-3541-8ce5-a1cb311d9f4f | -14.10855 | -45.39959 | 2025-08-10 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 08234733-f9e4-3063-b39d-3311c7cc2a61 | -13.59906 | -46.93852 | 2025-08-10 03:57:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d27f4e3a-b6f1-3e64-8189-07a1483b25c0 | -14.29163 | -51.96403 | 2025-08-10 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6007eac6-eedf-3403-9c8e-065ac3703d8b | -16.08024 | -43.62935 | 2025-08-10 03:57:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10778c35-b24b-3f46-af3d-ac9f7f751b17 | -14.59695 | -47.16416 | 2025-08-10 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22962cbc-6a3a-39fd-ba1e-061ae6e5e973 | -14.03512 | -46.34202 | 2025-08-10 03:57:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 80f58ca1-ae77-305d-8109-d48ddc1c1efe | -12.5602 | -47.08129 | 2025-08-10 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f1ca4bb1-8f09-3dbf-8ef7-e74bb34e82c0 | -14.46585 | -47.85177 | 2025-08-10 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b5e7b156-c38f-3759-851d-07c756217a19 | -16.37682 | -42.5412 | 2025-08-10 03:57:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c41ecedc-d97d-372e-8500-27ac92f2c368 | -16.37343 | -42.54065 | 2025-08-10 03:57:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c7a7a6c1-427c-3bf3-a361-46124370c8d2 | -17.19515 | -42.82335 | 2025-08-10 03:57:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e6b78c26-7035-3823-9561-18975b448a17 | -12.71567 | -46.36319 | 2025-08-10 03:57:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6a99884e-0607-3f39-837b-46d39a9e26ea | -19.57271 | -47.2268 | 2025-08-10 03:57:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8f1a60ad-913f-3b74-b2c2-e6f65bc1fc12 | -14.60222 | -47.16049 | 2025-08-10 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4b62c07-188b-3dd3-ac42-c889e92ca776 | -18.17057 | -46.99984 | 2025-08-10 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f536b197-cada-399f-9b2a-a46b039e4e99 | -16.3756 | -42.54869 | 2025-08-10 03:57:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84495998-b7d5-3c04-9497-7aa58fca926c | -18.75964 | -40.5946 | 2025-08-10 03:57:00 | NOAA-21 | NOVA VENÉCIA | ESPÍRITO SANTO | Brasil | 3203908 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ec2a7c42-5b05-3f0a-8842-6c1c06e235c0 | -17.51451 | -41.73225 | 2025-08-10 03:57:00 | NOAA-21 | LADAINHA | MINAS GERAIS | Brasil | 3137007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| daf7dabe-1211-3997-a0ec-f89be9ece05a | -18.17696 | -46.98855 | 2025-08-10 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b8c222a8-82dc-361c-986a-562a29dac96d | -14.10919 | -45.396 | 2025-08-10 03:57:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a70d6b3a-4a60-3f8d-a6fd-62c46097aecc | -18.17625 | -46.99236 | 2025-08-10 03:57:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a8f8de6f-e37c-3986-8602-40de3a5d61b6 | -14.09366 | -46.56921 | 2025-08-10 03:57:00 | NOAA-21 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d74829af-949c-3a72-9a77-7beb9590a14a | -14.28961 | -51.97351 | 2025-08-10 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b90a822f-92bb-38dd-be3f-d57832666e38 | -16.38144 | -42.5343 | 2025-08-10 03:57:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 5707d053-bcc3-3a11-ba5d-24e6adddcf10 | -15.09748 | -46.53833 | 2025-08-10 03:57:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1e9facba-3f22-3af7-86d2-f46a31ad4a67 | -14.29864 | -51.988 | 2025-08-10 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7c65ec0-b5b1-3034-bc0d-c12b4b71d37b | -14.58889 | -47.15794 | 2025-08-10 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76a6d010-1e28-3054-b313-0655afaecfd3 | -14.30063 | -51.97825 | 2025-08-10 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2849011-06ad-3c1e-9787-6c5eeb24ecc9 | -14.08934 | -46.56845 | 2025-08-10 03:57:00 | NOAA-21 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e48dd4f-cdef-3ffe-bc9f-c48710aab532 | -13.63621 | -48.98598 | 2025-08-10 03:57:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 87f133b3-4845-320b-868f-0cb7f80f15c9 | -14.59778 | -47.15963 | 2025-08-10 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09067e49-9922-3f81-909f-485b997f1906 | -18.91068 | -43.14572 | 2025-08-10 03:57:00 | NOAA-21 | SENHORA DO PORTO | MINAS GERAIS | Brasil | 3166105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 044fbde4-605d-3b50-84d7-696a5d47f854 | -16.37621 | -42.54494 | 2025-08-10 03:57:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8b649908-86f4-3998-b681-c38aee4a4631 | -14.58971 | -47.15342 | 2025-08-10 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 45357cc6-4dfb-3dcb-a783-111a2e630127 | -19.36894 | -41.75011 | 2025-08-10 03:57:00 | NOAA-21 | ALVARENGA | MINAS GERAIS | Brasil | 3102209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9535586b-16e5-37a0-bdad-6278a46b7227 | -13.78111 | -48.88 | 2025-08-10 03:57:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b895bf69-8e3e-3ea4-8386-70b5e2618c7f | -14.29963 | -51.98314 | 2025-08-10 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 07380d84-941c-3d16-8451-4a56e139f5bc | -17.51277 | -41.74311 | 2025-08-10 03:57:00 | NOAA-21 | LADAINHA | MINAS GERAIS | Brasil | 3137007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| d4e9c65f-29fe-3cf3-afa6-480c84ecfc23 | -16.37805 | -42.53374 | 2025-08-10 03:57:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 0f0980d2-cbb1-3680-ba57-43f1493a746f | -12.5545 | -47.08642 | 2025-08-10 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d65c609c-44ae-3c1b-8ba2-70dd2b0e3742 | -19.57874 | -47.23994 | 2025-08-10 03:57:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3e8db14-d964-3011-be95-0e76311e5719 | -16.37926 | -42.5263 | 2025-08-10 03:57:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e653a4af-6a2a-3d15-b5b1-575b2de9d8d5 | -12.1695 | -50.21795 | 2025-08-10 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3a1f11b-665a-38b5-891e-3e3df2773239 | -16.37221 | -42.54812 | 2025-08-10 03:57:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a5217df7-f884-3885-be33-b3c1186ad939 | -16.37282 | -42.54438 | 2025-08-10 03:57:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 702d8b02-17f3-3498-812c-f815a6c4d242 | -14.72032 | -47.52456 | 2025-08-10 03:57:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0e24c35-362b-3305-a283-d4f240635b2d | -16.38022 | -42.54177 | 2025-08-10 03:57:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6e94d4f0-54d2-3ee6-8927-df7f6b420731 | -14.60478 | -47.16356 | 2025-08-10 03:57:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e42eb1e1-4628-39f1-ab01-c4268e69ccea | -18.70279 | -47.48899 | 2025-08-10 03:57:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 808150df-d602-32c9-9210-f5b0d3a700d5 | -14.29366 | -51.98428 | 2025-08-10 03:57:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34efadca-6945-3225-8f95-7e6bfacea798 | -13.64217 | -48.9825 | 2025-08-10 03:57:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README11.md)
