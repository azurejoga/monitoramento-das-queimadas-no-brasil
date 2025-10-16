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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4b35b45b-f2dc-307b-8cb7-4e1a66f09b62 | -8.4717 | -44.1746 | 2025-10-16 01:40:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 5e9afa6d-6e5a-3d3b-bf44-2dc73910a5a2 | -4.3685 | -43.4071 | 2025-10-16 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 318.6 |
| 646fa62e-65d1-3e6c-9f58-4db48715538e | -4.9293 | -45.8811 | 2025-10-16 01:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 7448354d-e2ca-3be6-aa2c-89bb7734bfdf | 1.8032 | -55.8815 | 2025-10-16 01:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| e862dce2-575c-3656-b9b4-662a58331168 | -4.1161 | -48.0136 | 2025-10-16 01:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 165.5 |
| c47042e0-c7a3-3c6b-8968-9be2ccfe1a35 | -7.2565 | -41.7335 | 2025-10-16 01:40:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 77.4 |
| aafa71aa-fa8e-3686-bf27-ccf734042fef | -12.6612 | -43.4268 | 2025-10-16 01:40:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| b97cff01-da4c-38e9-bba0-bbfc163f8b12 | -4.0976 | -48.0144 | 2025-10-16 01:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 114.3 |
| b559c9f8-d09f-320e-9bec-bf35d4795352 | -4.5041 | -45.4118 | 2025-10-16 01:40:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 71.2 |
| a6d17cae-00ad-3bb7-b2ea-2756aab7b0fd | 1.8217 | -55.7629 | 2025-10-16 01:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 7a9d3586-2d53-32eb-bb5e-a269f3c19f86 | -8.4714 | -44.1978 | 2025-10-16 01:40:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 04ffc00e-4d83-3f39-8940-12baa7613ebd | -5.5147 | -47.3069 | 2025-10-16 01:40:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 132.7 |
| 7c81e673-aec7-37e9-bdf9-5cab28dcec9c | -4.35 | -43.3849 | 2025-10-16 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 92c61314-d81f-37be-8c0e-09befd1614b0 | -5.496 | -47.308 | 2025-10-16 01:40:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| df2e56f7-56e2-312a-aa20-a23bb56c15e0 | -4.6624 | -44.1062 | 2025-10-16 01:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 4c7e70a1-28a3-3460-915e-f19ce266fa3c | -7.9439 | -44.1381 | 2025-10-16 01:40:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 98a70695-b769-36ec-867a-df96c49e5f0d | -7.4894 | -42.7586 | 2025-10-16 01:40:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 85.4 |
| d226d048-bdf2-3f06-806a-28abebf2f284 | -7.4706 | -42.7605 | 2025-10-16 01:40:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 118.9 |
| 7c8bb87a-c765-3e3e-bd16-dbc4d0ab0b4c | -4.8644 | -44.5748 | 2025-10-16 01:40:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 1d0ade58-9b91-30ce-88d2-0c204ab77199 | 1.8401 | -55.7232 | 2025-10-16 01:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 7a0cf5c5-4e9d-3b03-a052-e244f6b3946a | -4.4061 | -43.3816 | 2025-10-16 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 59.2 |
| fe4285da-95ff-32ef-a821-e95bbed8e410 | -8.4528 | -44.1767 | 2025-10-16 01:40:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 53ff80f6-0b17-3880-9c80-5781536892e0 | -4.3872 | -43.406 | 2025-10-16 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 411.3 |
| 774b5330-a6c2-388a-89eb-67e59560465d | -4.3498 | -43.4082 | 2025-10-16 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 56ada8ba-9277-3fdb-ba28-3f92f7015231 | -5.4276 | -44.2402 | 2025-10-16 01:40:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 51.1 |
| cf9006d8-b0d4-3976-8cf9-f6c303c9cead | 1.8218 | -55.7431 | 2025-10-16 01:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| f25b5992-fbc5-39e3-a28e-e3a8bfa0c7f1 | -12.6805 | -43.4235 | 2025-10-16 01:40:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 130.5 |
| 6bd12ceb-5acf-349b-8624-3f903cd68aeb | -4.4059 | -43.4049 | 2025-10-16 01:40:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 551acbb3-4a4f-3e52-b367-e2e47b9ce134 | -4.116 | -48.0352 | 2025-10-16 01:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 122.2 |
| 8a525007-d12c-3a89-a0f3-3d2f5d8bbeb6 | -4.3874 | -43.3827 | 2025-10-16 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 354.6 |
| df534078-3669-38ed-a3fd-eb837d3bd77e | -9.7162 | -44.5149 | 2025-10-16 01:50:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 89.9 |
| e7485dec-7079-3127-8982-0ef7f2b6ba1d | -7.4894 | -42.7586 | 2025-10-16 01:50:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 83.2 |
| e1a1e3e5-569f-355c-8b29-dffd87477f6b | -8.4714 | -44.1978 | 2025-10-16 01:50:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 070f2d12-cff7-39b0-b132-bb0ae6ac6bb7 | -7.9628 | -44.1362 | 2025-10-16 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 841639db-9914-38c6-84fb-fc70afaa22d6 | -4.1161 | -48.0136 | 2025-10-16 01:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 143.8 |
| 8efc15a1-65c9-3ba1-b851-2e5c34eb37c2 | -4.8644 | -44.5748 | 2025-10-16 01:50:00 | GOES-19 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 28c22360-3e9a-36d0-9af7-5cc6261bfa45 | -4.9293 | -45.8811 | 2025-10-16 01:50:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 52.9 |
| ea440334-20ab-3d9e-958a-bc97d2a77056 | -7.4706 | -42.7605 | 2025-10-16 01:50:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 95.7 |
| 45ba46cb-2d88-3e36-81ff-76079c9803d3 | 1.8218 | -55.7431 | 2025-10-16 01:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 1efd518a-3276-3594-a57b-fc5f4c435cc2 | -8.4528 | -44.1767 | 2025-10-16 01:50:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 364d38eb-121c-3506-b08b-f0a32591d3d3 | -4.5041 | -45.4118 | 2025-10-16 01:50:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 64.8 |
| dee4eef9-af21-377c-8cc2-314d8340ede1 | -4.6626 | -44.0832 | 2025-10-16 01:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 35.9 |
| d29e3782-63d7-33f5-9c06-f046008ebc2f | -5.5147 | -47.3069 | 2025-10-16 01:50:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 131.7 |
| ab61603a-27cb-3848-b166-3cb7ee116e89 | -5.8989 | -43.8598 | 2025-10-16 01:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 60ea960d-767a-38f4-8e3d-f650c57f9325 | -8.4717 | -44.1746 | 2025-10-16 01:50:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 121.3 |
| a02d3669-c6b4-304f-b6bf-54e2651277ea | -12.6805 | -43.4235 | 2025-10-16 01:50:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 128.2 |
| b8fcb24a-aa21-3783-890e-6f3d2646eb79 | -4.4061 | -43.3816 | 2025-10-16 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 80cf5156-de31-3ddc-b372-f1b23cff982e | -7.9439 | -44.1381 | 2025-10-16 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 7ce3ebf1-826e-35da-9b69-e8ecda3546eb | -5.8612 | -43.8858 | 2025-10-16 01:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 35.3 |
| c7765f2b-b237-3268-aec7-b16b1d899bba | 1.84 | -55.7626 | 2025-10-16 01:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 98e798cd-e559-3498-9996-04602d21911f | -4.35 | -43.3849 | 2025-10-16 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 6fbb54fd-2aa9-3219-9fe9-8e4a42bf1e31 | -29.187 | -50.1287 | 2025-10-16 01:50:00 | GOES-19 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 63.1 |
| 267442bb-6e1e-3d3d-b3ad-c6896a9f4019 | -4.6624 | -44.1062 | 2025-10-16 01:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 42.0 |
| f8f4ba80-09d5-3cc6-96b0-91cedbca4111 | -12.6801 | -43.4474 | 2025-10-16 01:50:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| cff7911c-4819-3e44-a131-6885fa48a4e6 | 1.8217 | -55.7629 | 2025-10-16 01:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 86bcee9f-cde6-37cc-b9ef-fb6de56c0294 | -4.3687 | -43.3838 | 2025-10-16 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 378.4 |
| d0c760a8-db07-3377-9603-f5c8a561e058 | 1.8401 | -55.7232 | 2025-10-16 01:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| fd153ca2-0238-370a-9b77-b9e949854028 | -4.3872 | -43.406 | 2025-10-16 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 393.1 |
| 2b48798a-6a66-3573-bee2-37f2b660d073 | -4.0974 | -48.0361 | 2025-10-16 01:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 8e75137d-d649-30ef-b9c6-5d57d96a5086 | -4.5042 | -45.3893 | 2025-10-16 01:50:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 142e507f-3489-342f-8978-91feb0219308 | -5.8799 | -43.8844 | 2025-10-16 01:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 83a6f48b-99c1-38fc-bb20-1f361c3141eb | -5.8802 | -43.8613 | 2025-10-16 01:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 0294f76c-ee56-3322-af41-819299431dd9 | -7.9442 | -44.115 | 2025-10-16 01:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 63.6 |
| bfdef76d-5e9c-3c18-92d4-afd0c2477070 | -4.3685 | -43.4071 | 2025-10-16 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 301.1 |
| 40d04fed-4156-3c39-b79d-bb200aa5094a | -7.2565 | -41.7335 | 2025-10-16 01:50:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 81.1 |
| 2579e817-725b-3383-966d-c3e2b37fa4dd | -4.116 | -48.0352 | 2025-10-16 01:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 2c98ab93-99be-327b-afd0-9fa4ec4fd966 | -4.0976 | -48.0144 | 2025-10-16 01:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 125.1 |
| bb11019d-f2ed-3159-a461-ac1175f65514 | -4.3498 | -43.4082 | 2025-10-16 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| d23e1819-84ee-3d66-afb3-71a338fd5b94 | 1.8401 | -55.7429 | 2025-10-16 01:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| fb6074d6-3058-3a16-87f8-64b35b8d2a49 | -7.2754 | -41.7316 | 2025-10-16 01:50:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 54.0 |
| 9923743b-a48b-3554-a911-372e56340f8f | -4.4059 | -43.4049 | 2025-10-16 01:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| bb7f27e9-7b0a-32fa-9b10-4c0993795b81 | -8.4528 | -44.1767 | 2025-10-16 02:00:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 4c5f3606-c43b-323c-8a14-323e46f9d3ea | -4.3687 | -43.3838 | 2025-10-16 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 421.2 |
| 702b26f6-b500-3a85-ab53-c188e994161f | -4.4061 | -43.3816 | 2025-10-16 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 170.5 |
| 4e9f367a-05d4-38b9-b93c-a044dbf1e488 | -9.5339 | -40.3531 | 2025-10-16 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 66.8 |
| 3d033091-0a59-3be4-bd00-bca86a093a8a | -12.6805 | -43.4235 | 2025-10-16 02:00:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 0185c598-05de-3f2f-bbd5-88d606feb81f | 1.8217 | -55.7826 | 2025-10-16 02:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| f3c84c22-99a2-3963-b2ab-8d1a93ed9fbd | -4.116 | -48.0352 | 2025-10-16 02:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 123.2 |
| 256576ed-f2ee-30f9-88f5-3281da927788 | -4.4059 | -43.4049 | 2025-10-16 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 217.6 |
| c9414fd6-cc64-3f6a-8c7a-2cdeb6ca72c6 | -4.6624 | -44.1062 | 2025-10-16 02:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 0ab5eea9-6688-30aa-bae1-564c19c9acf6 | 1.8401 | -55.7429 | 2025-10-16 02:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 82aa9e81-22c6-32e1-b26c-f86456fc5b4c | -5.5147 | -47.3069 | 2025-10-16 02:00:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 32e442ed-ba6c-3ed3-8f2c-1e54304ebc6e | -4.0976 | -48.0144 | 2025-10-16 02:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 109.4 |
| e80e4b3b-3afd-31c3-8ec8-8809bc7e5fcf | 1.84 | -55.7626 | 2025-10-16 02:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 99aa79ac-ee51-3236-8f83-c6b839824f07 | -4.0974 | -48.0361 | 2025-10-16 02:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 9241e083-1273-3f9b-a65f-3957d6bd4ffe | -4.3874 | -43.3827 | 2025-10-16 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 614.6 |
| 82c59882-2f61-36be-9acd-f7cbc15128b4 | 1.8401 | -55.7232 | 2025-10-16 02:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 6fa11f8f-1324-3fec-888c-f961a59cc6af | -4.3685 | -43.4071 | 2025-10-16 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 348.5 |
| 97b8c0c1-1333-32e7-8ace-f224147c0d85 | -8.4717 | -44.1746 | 2025-10-16 02:00:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 8c1c5c98-5d58-38cf-9576-b12cdc6f8113 | -4.3498 | -43.4082 | 2025-10-16 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 33f66d75-b839-38cf-9c2e-1aa663d2da36 | -5.4762 | -42.9367 | 2025-10-16 02:00:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 106.0 |
| 1b463132-2815-3f5e-8161-07afed1b7882 | -5.8799 | -43.8844 | 2025-10-16 02:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 04b74975-7a36-33df-92e4-e7bf4500372b | -7.2565 | -41.7335 | 2025-10-16 02:00:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 70.3 |
| 7f8e07fd-f885-3f41-9729-b5e2c8041de6 | -4.5042 | -45.3893 | 2025-10-16 02:00:00 | GOES-19 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 101.4 |
| 9d6178be-3515-325f-870b-a1a9fa096fbc | -4.6626 | -44.0832 | 2025-10-16 02:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| e9d4fff3-ad2e-397d-b28c-ccabe605fbb9 | -12.6612 | -43.4268 | 2025-10-16 02:00:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 00e77684-e68a-32c8-a188-1a7b76a90d46 | -9.7162 | -44.5149 | 2025-10-16 02:00:00 | GOES-19 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 93.0 |
| ba38a491-830f-33bf-8373-f4c5911e121b | -9.5343 | -40.3282 | 2025-10-16 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 62.3 |
| 187de406-f83f-3595-9978-ef06fa32692e | -4.35 | -43.3849 | 2025-10-16 02:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 57179c4f-e162-3d09-b193-53681d30a060 | -7.9442 | -44.115 | 2025-10-16 02:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 62.6 |


[Clique aqui para ver as próximas entradas](README8.md)
