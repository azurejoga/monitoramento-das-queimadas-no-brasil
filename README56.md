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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1026af41-c83e-3b58-943e-29b2e10551a4 | -17.2483 | -46.91788 | 2025-10-06 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 38d30d99-5511-36ee-96c0-a7a11b7c67f8 | -18.69404 | -49.24373 | 2025-10-06 04:29:00 | NOAA-21 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2676aee0-04b0-39a9-94b6-05dd78d18eeb | -18.25823 | -53.32932 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d268e6cf-c326-3986-bed5-79e76885534f | -18.00463 | -57.59676 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 2cc5dab9-fd35-3577-8733-dcd8b7dae35f | -18.17681 | -53.36912 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f6b97eab-3c2b-3f0c-a241-e6f5ef2599d1 | -22.82114 | -45.54029 | 2025-10-06 04:29:00 | NOAA-21 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| fb2d7b24-606a-3d02-b841-24d6fdb117a9 | -21.72542 | -50.06877 | 2025-10-06 04:29:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8c5c03b1-45d9-36a3-8928-db65d253421a | -18.27048 | -53.32621 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3ba73f6a-6719-3d39-a9f7-767e3e7ac67d | -22.70801 | -44.87229 | 2025-10-06 04:29:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e127ecfd-5ba1-3727-8067-312c1762d7a0 | -18.27096 | -53.32368 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 12.9 |
| e229670f-cea8-3bb0-8005-477bf794fa24 | -16.14934 | -57.57339 | 2025-10-06 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 75611519-b8cd-30e5-89c9-0825f261b712 | -20.11756 | -46.35355 | 2025-10-06 04:29:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83c04584-2c1c-3c97-a92f-9c9d4c94b7b9 | -18.17968 | -53.37494 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 93044738-e65a-355d-b9b5-7c0e42316682 | -18.12362 | -53.40708 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 615dea5d-dd8f-30f7-a581-26ca053a7bbf | -20.5013 | -46.99388 | 2025-10-06 04:29:00 | NOAA-21 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 234991d4-5828-3820-b033-b53bd7c6639f | -18.27305 | -45.41386 | 2025-10-06 04:29:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fcfe51c8-91bc-3b5f-85a8-425d06868425 | -18.28523 | -45.43425 | 2025-10-06 04:29:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6098cc12-a9fc-3242-b45f-7c70315d95cc | -16.96138 | -52.67915 | 2025-10-06 04:29:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe24d52e-9908-3a1d-8191-33ff173a3474 | -19.94564 | -44.63155 | 2025-10-06 04:29:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c23b46a3-16f9-3a74-8240-ec45497fddb0 | -18.59341 | -49.98447 | 2025-10-06 04:29:00 | NOAA-21 | INACIOLÂNDIA | GOIÁS | Brasil | 5209937 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2d43f775-ff16-3211-bc3e-148b32f0db95 | -17.99066 | -57.53391 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.5 |
| e1a1c56e-f1d7-3492-aab6-f9d93c42055b | -22.37598 | -50.02046 | 2025-10-06 04:29:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 859bfd25-96ea-309e-8101-26f8d09d6772 | -21.34392 | -49.78947 | 2025-10-06 04:29:00 | NOAA-21 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 070a8eb8-a691-39ee-87f4-2471f292adf3 | -21.39135 | -45.04228 | 2025-10-06 04:29:00 | NOAA-21 | INGAÍ | MINAS GERAIS | Brasil | 3130804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 4bd54bc4-7807-39da-adfa-7432add3b47b | -18.10274 | -51.83364 | 2025-10-06 04:29:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a46046b-1dda-312a-a028-8f1f0cd83c2f | -19.66262 | -45.92268 | 2025-10-06 04:29:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 69e2cd2f-281d-3b7b-972d-a43bf7c376f1 | -18.28225 | -53.32599 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e7464b9-91a2-3712-bbba-a3872d4ca483 | -16.14417 | -57.57261 | 2025-10-06 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| afcf4bee-cb3b-3a6f-a944-0cd5cc82add4 | -17.99808 | -57.59991 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1fc0b8d2-7810-3d75-8d95-00e5cbf62d03 | -19.94514 | -44.63544 | 2025-10-06 04:29:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| d40d558c-005a-3017-a6f3-37fbbed45f01 | -18.14317 | -53.403 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d7334912-198e-3cb7-978a-03d88c7a6e05 | -18.39684 | -45.21527 | 2025-10-06 04:29:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 76330930-a1cc-3db5-bf70-75491a9bffed | -17.95809 | -48.55213 | 2025-10-06 04:29:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c137e6a5-beff-37b9-bf4b-23c5a036ffb3 | -18.12655 | -53.41269 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b7cca8bf-14ca-38ef-9cc5-3096988592a2 | -18.14511 | -53.39249 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 120d85ef-5eb4-32fd-9511-29db43189c01 | -18.27939 | -53.32029 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8667c755-02f4-3a1b-9c25-14bf23952968 | -19.95354 | -44.63221 | 2025-10-06 04:29:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 884d948c-39d0-3e5e-b45b-72cc74bc2541 | -18.9895 | -50.56413 | 2025-10-06 04:29:00 | NOAA-21 | SÃO SIMÃO | GOIÁS | Brasil | 5220405 | 52 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 9ac7ecd5-e2b4-38b7-92ab-7ecc71658eaa | -15.87951 | -59.38002 | 2025-10-06 04:29:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 14efe293-bdaf-3bf4-a70f-5a121b81e13d | -18.41143 | -46.76656 | 2025-10-06 04:29:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe512af5-2b42-3ccb-a790-7af7cc77a890 | -22.90439 | -44.71487 | 2025-10-06 04:29:00 | NOAA-21 | CUNHA | SÃO PAULO | Brasil | 3513603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| fe6de3cd-0f29-34e2-8d08-f8b07f95c808 | -22.61997 | -43.56371 | 2025-10-06 04:29:00 | NOAA-21 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6861e1b9-8487-3a6e-8aed-527b77f9a25e | -21.44354 | -44.02982 | 2025-10-06 04:29:00 | NOAA-21 | IBERTIOGA | MINAS GERAIS | Brasil | 3129400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ebab33bb-a312-34b8-9d37-240947817cdd | -22.36879 | -50.02298 | 2025-10-06 04:29:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| ddfb4f86-15d4-33ef-a0e7-460d51204abe | -17.95865 | -48.54851 | 2025-10-06 04:29:00 | NOAA-21 | CALDAS NOVAS | GOIÁS | Brasil | 5204508 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b21b2a43-b980-3180-9588-1867bf75ad8c | -18.27179 | -45.42305 | 2025-10-06 04:29:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ecaf634f-d4b9-3267-934b-83b2784ebe19 | -20.26875 | -43.63488 | 2025-10-06 04:29:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ea777f2e-6cce-3664-a486-9d7e65689642 | -23.40426 | -45.38282 | 2025-10-06 04:29:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d6fa79d8-6547-3257-9eeb-ce548c33813e | -17.26305 | -46.9123 | 2025-10-06 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f909bf5-76c5-36e6-a612-b61e3694006b | -21.94768 | -46.45339 | 2025-10-06 04:29:00 | NOAA-21 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| f0222df0-1a92-3877-9dac-1114ea41786f | -17.98672 | -57.60513 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8cd68660-c8a4-3f0b-b2eb-f8ace1da8cd2 | -17.98313 | -51.13559 | 2025-10-06 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af700b35-311f-346f-b4bc-33d5cff70dc0 | -21.21657 | -44.23207 | 2025-10-06 04:29:00 | NOAA-21 | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c9050be8-415e-3059-9dcf-e436bf361b20 | -22.71827 | -44.85462 | 2025-10-06 04:29:00 | NOAA-21 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cae71aaf-1d2c-34c7-b820-076322b930bb | -17.85034 | -57.63797 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b87315a1-9c2b-39be-b4b8-5b1601033857 | -17.96888 | -57.54002 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 06fdd939-66fd-3a3b-8605-be2b805f759e | -18.25314 | -53.35813 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 32f8f3ff-95fd-3b51-8b6e-cac8809b4be8 | -18.13035 | -53.41341 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 9f99d7b4-45e9-3d18-8786-c5dd8647437f | -23.39188 | -45.38623 | 2025-10-06 04:29:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 0cca82c9-a41a-340f-94e7-2a0f440a0fde | -17.60669 | -44.45497 | 2025-10-06 04:29:00 | NOAA-21 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e4f34742-36c9-39ce-8741-29638b3c1a94 | -17.84209 | -57.62745 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| ddc9ac57-78c7-359e-8c9c-bfda1011141c | -22.52918 | -43.57204 | 2025-10-06 04:29:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c4258519-fc82-3afc-a4bd-5c402ffcd9e6 | -23.43676 | -45.47512 | 2025-10-06 04:29:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| e7e86846-8512-31a8-82b1-223853ce0d79 | -17.8847 | -57.64763 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 68c3fda4-1452-3329-bea3-fbc7dd1d4b9a | -17.95772 | -57.59532 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| ae78bf77-4db6-3077-a29d-8dbcb4c009f9 | -18.26752 | -53.32087 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 58e1e45e-f655-37ab-a5de-00e619cafb17 | -18.19094 | -53.37767 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dfac7f6a-d468-3405-8e6d-8389d12b854f | -18.11127 | -53.41022 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a27e5041-db24-3afd-8ed8-5379c24825c0 | -22.291 | -49.91052 | 2025-10-06 04:29:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 652a7b83-ce1f-30a3-8705-5a11523a0b21 | -22.38317 | -50.01794 | 2025-10-06 04:29:00 | NOAA-21 | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 3d174ddf-8cc0-3697-88e5-787b059dc3bc | -22.97202 | -47.60603 | 2025-10-06 04:29:00 | NOAA-21 | MOMBUCA | SÃO PAULO | Brasil | 3530904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 7f2aa1c7-470e-38d1-9801-94229c57a767 | -16.14782 | -57.56886 | 2025-10-06 04:29:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d6e92eaa-a34b-33a2-8bcb-2c02702b1322 | -17.38336 | -53.59402 | 2025-10-06 04:29:00 | NOAA-21 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 49ba5852-3c02-3c58-bb8e-4616c65baf0c | -17.96205 | -57.59944 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 0ac71d89-3a99-3214-ad91-ac9962bf3c23 | -17.06832 | -46.6371 | 2025-10-06 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f86aedbc-ce94-373b-9adb-4cb2363779f5 | -17.98327 | -57.59657 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| a36596a1-1704-32b6-be29-b72d9838100e | -17.97068 | -44.999 | 2025-10-06 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2969e009-dacb-36e0-80f1-39922dd6aed2 | -17.99477 | -57.59452 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 2362ceb2-0d09-31bf-b8f4-2a3129a424d4 | -20.09399 | -44.19644 | 2025-10-06 04:29:00 | NOAA-21 | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 16223bb2-cb80-37f4-88f6-e9f3ede6b67b | -18.09923 | -51.83299 | 2025-10-06 04:29:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0046ab55-7935-36b2-9b5b-6f62c7508abd | -17.885 | -57.6473 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 239053ce-69d1-3c63-ac69-d6486c34500f | -18.26668 | -53.32566 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 73182c06-2d2a-3f22-a121-361f5e72b022 | -17.24774 | -46.92174 | 2025-10-06 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7e7ca2d-30e6-3a04-a149-28de9631edcd | -17.9528 | -57.59414 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c45d419d-e44a-3edf-b02f-613303660717 | -17.88173 | -57.58458 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| abfc32e8-4d39-333d-87ad-bfc683d445b8 | -21.74251 | -50.06804 | 2025-10-06 04:29:00 | NOAA-21 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e9e16dbd-7fe1-3855-a26e-69b127dcd2e2 | -21.56896 | -48.33179 | 2025-10-06 04:29:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1aa31e8c-ca8a-3c2b-816b-e58ff7a9216b | -17.25402 | -46.92641 | 2025-10-06 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ddc41449-bbe1-3f19-b820-7aced71a53ad | -17.86565 | -57.58755 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| a86a5ec5-568b-3d33-bfeb-df9d39fe7433 | -17.88006 | -57.64608 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c630df36-85c8-30b7-9249-20558aaf18a6 | -22.27689 | -46.75479 | 2025-10-06 04:29:00 | NOAA-21 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 66c8505c-d969-31e4-9b79-f924082d5f95 | -19.95288 | -44.63739 | 2025-10-06 04:29:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6d18a018-59da-33b8-84c3-2bea9c88cff5 | -17.66762 | -44.43881 | 2025-10-06 04:29:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dc34ef22-2417-3f64-9291-71cf65e80a8a | -17.9952 | -51.62976 | 2025-10-06 04:29:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d44563aa-4981-3c68-8bfc-334897964e25 | -17.83803 | -57.62191 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 25e85b05-1d0f-3693-b81c-41aa92271c14 | -18.46646 | -52.97433 | 2025-10-06 04:29:00 | NOAA-21 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb0534e6-58ed-3923-8ea1-6ae45c829aad | -21.78598 | -52.12807 | 2025-10-06 04:29:00 | NOAA-21 | PRESIDENTE EPITÁCIO | SÃO PAULO | Brasil | 3541307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2d3a2e48-5763-39d8-882f-d6410bc3924b | -18.00156 | -57.53688 | 2025-10-06 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 7ff683cc-4708-38be-a2e7-41368b859312 | -23.17771 | -46.26361 | 2025-10-06 04:29:00 | NOAA-21 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 4cde4043-53b6-3626-b58e-3f5cf3fdc5f0 | -18.25104 | -53.34789 | 2025-10-06 04:29:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README57.md)
