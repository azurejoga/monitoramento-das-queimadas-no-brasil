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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7790ef8-0a5d-37ea-af11-836ac1bd07c6 | -11.65164 | -64.01001 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f78f113f-7f4b-3c17-a2fd-338cc1372bb0 | -11.65073 | -63.99065 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5cd6f865-2878-3e2c-b1db-6dfb30f0781e | -11.62324 | -64.00137 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7db0fb40-1c22-3bba-b74c-01cf8b5874bc | -11.59947 | -63.91843 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| daf61d8f-864f-3dc7-aa37-6165afc58654 | -11.5988 | -63.92221 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 15fbda58-58af-3586-812e-d4ed8e6fc857 | -11.59604 | -63.9138 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a6e880a-e9ab-3e9e-bb4a-68a559dbc9da | -11.58964 | -63.71452 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 549d8c4a-f3ba-3ee4-8c64-285a5c299be5 | -11.5862 | -63.71012 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 679a9110-5328-3ae9-857d-cf5ecb90f141 | -11.58559 | -63.71366 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 707c57e8-0831-3ac9-8fd1-6da17786d077 | -11.58364 | -63.72497 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7d6dd2d-5106-3ab6-9d9b-57d5c3b8e216 | -11.58028 | -63.72013 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b199eebe-7585-3356-abc3-025817481364 | -11.57961 | -63.72403 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8f9cb8f0-9f2e-3b00-a279-3e56b75cc6df | -11.5749 | -63.72697 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ac864f0d-5958-30c8-8cba-0cee04e8135d | -11.57423 | -63.73082 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b43670ef-e2aa-3305-b459-fda74c7fdbd4 | -11.57357 | -63.73465 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cc80d5ef-751c-3c8c-b215-4a3f42d80525 | -11.57291 | -63.7385 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f98ea7a6-9b33-3f8b-b8ab-d6c8e0e3d1cb | -11.56878 | -63.73809 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49f46cd0-912a-3454-885d-79a89895222d | -11.56651 | -63.91248 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79473bca-0cbf-3799-ab7e-ad956264a1c5 | -11.56583 | -63.91628 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de28bf06-62bc-3b6e-9144-859699b968d4 | -11.56515 | -63.92007 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 170c94fa-ea8b-37fb-afd5-b62aff4410f9 | -11.56307 | -63.90791 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44d6a098-e0d8-3b4a-aa9a-81251844dd22 | -11.56063 | -63.90763 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f227d167-1c3d-3334-9ba5-2c244a4560b9 | -11.55896 | -63.90715 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e941f63-f35b-35a0-8e62-905da173f116 | -11.55651 | -63.90686 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c741b5a-5654-32f7-adf4-50b48a36730e | -11.55239 | -63.90611 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2de37fef-a7dd-3f17-a257-a80f8137e1ea | -10.8883 | -64.17731 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 412111db-9554-3d3d-9cd1-9a9f29ead61e | -10.88754 | -64.18156 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c00a8bfa-a9b4-3774-a9ea-07ed2fea19c0 | -10.88624 | -63.89103 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 889c1524-595d-3de4-942f-af6190c02dce | -10.8785 | -63.8862 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7a4d6f25-18ec-3b63-9b50-929d839748bf | -10.87429 | -63.88578 | 2024-09-28 05:10:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bbb5751d-d837-3961-971f-283e9ad61813 | -9.96151 | -64.73274 | 2024-09-28 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6e29b09-1ad8-3bd6-b0b8-9ab88036759b | -9.95705 | -64.73188 | 2024-09-28 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea10ab6d-3d33-3db5-9aeb-076e4530ad05 | -9.93117 | -64.77354 | 2024-09-28 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b6cbe977-37e1-3072-b4f2-efda08fbbbc4 | -17.85285 | -45.90047 | 2024-09-28 05:12:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 92de3d26-ded2-3399-97e9-0254658ffbfc | -17.85225 | -45.90733 | 2024-09-28 05:12:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 1f1a0fa0-6148-319d-a55a-e29ab3ddad67 | -17.85118 | -45.8981 | 2024-09-28 05:12:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 335a54b3-30cf-3680-8428-ba0571b26ddc | -17.85064 | -45.90475 | 2024-09-28 05:12:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 5336fd51-441e-3f1e-96b0-5d7db028ffe7 | -17.84641 | -45.89301 | 2024-09-28 05:12:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 22.7 |
| e786e829-5b55-3efc-b761-84c69a9f4e6d | -17.84584 | -45.89953 | 2024-09-28 05:12:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 815ba7c3-07fd-332d-a353-692b89f539f9 | -17.84525 | -45.9062 | 2024-09-28 05:12:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 63e4a1b5-0406-30e1-b97b-f1218492db1a | -17.8447 | -45.89064 | 2024-09-28 05:12:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 61668cf6-9d19-3e68-bef5-a64ffacdf589 | -17.84416 | -45.89719 | 2024-09-28 05:12:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 24.5 |
| e0c0ca10-5358-3345-89cf-8fd17b7dc839 | -17.84363 | -45.9037 | 2024-09-28 05:12:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 24.5 |
| b4d2d1e5-787e-34ce-bfdf-cd7b2a32ff85 | -17.83882 | -45.89872 | 2024-09-28 05:12:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 294c65b5-0c13-322d-8f0c-8ced2ae01bd6 | -20.57683 | -46.26175 | 2024-09-28 05:12:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c7ebef90-c6fa-3cde-b1ca-053123a5f64c | -20.57438 | -46.26234 | 2024-09-28 05:12:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 57920127-e9d3-3d47-b744-1e13908dfc06 | -20.57398 | -46.29756 | 2024-09-28 05:12:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ca78e84b-4271-367d-9b8f-ef73d589cc4b | -20.57348 | -46.30374 | 2024-09-28 05:12:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a888083d-fdfc-3d3d-9366-003432c73219 | -20.56919 | -46.26828 | 2024-09-28 05:12:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cc7d7245-3c0b-3595-9578-f968e32d0dc0 | -20.56748 | -46.25943 | 2024-09-28 05:12:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 65df5efe-0455-32b7-8619-f389bd76f607 | -20.56298 | -46.25687 | 2024-09-28 05:12:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1954c131-4433-38fd-9c0d-a15ccdd0677f | -20.56232 | -46.26528 | 2024-09-28 05:12:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 899a0ccb-57ce-35ae-a5fb-6b19b9905737 | -20.56051 | -46.25733 | 2024-09-28 05:12:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c676ff9e-7336-3902-94b0-fb02d5ed4de6 | -20.55992 | -46.2655 | 2024-09-28 05:12:00 | NOAA-20 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5da855e6-48eb-3ae1-9738-ea4cc9a6d648 | -20.5506 | -46.29612 | 2024-09-28 05:12:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2cb3680-4bdc-3a1f-ba2d-977c037386d7 | -20.55003 | -46.30402 | 2024-09-28 05:12:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3f648ebf-eefa-38d2-89b2-adcf3314b8be | -17.00661 | -45.93079 | 2024-09-28 05:12:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b27b8d0-8aee-346a-8d93-3544e40fd5fb | -17.00717 | -45.92421 | 2024-09-28 05:12:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d360858-ceb1-3203-9ffb-8f3d0ef41461 | -20.5929 | -47.46788 | 2024-09-28 05:12:00 | NOAA-20 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9a3774eb-6da4-3927-ae8f-249e0f8836bb | -20.59243 | -47.47372 | 2024-09-28 05:12:00 | NOAA-20 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a1c11c7e-d8d8-3b1e-9c40-df35236d23b5 | -20.58783 | -47.47276 | 2024-09-28 05:12:00 | NOAA-20 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ffb1dc99-a57f-3277-b21e-617ea1f8fe56 | -21.88498 | -48.50142 | 2024-09-28 05:12:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 885cdd06-e517-3b7b-9b5d-5270eb57e536 | -21.88456 | -48.50653 | 2024-09-28 05:12:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 827ca781-745e-315d-80d0-783555f0d332 | -21.84998 | -48.21437 | 2024-09-28 05:12:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38d691ff-dc83-3fce-ae02-bbef705371bf | -21.84822 | -48.21489 | 2024-09-28 05:12:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42b951a3-b007-3276-b4e0-16cfa1292489 | -21.84777 | -48.22022 | 2024-09-28 05:12:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3ed4044-1301-3b6e-9f35-5c4aab6c44f5 | -21.84353 | -48.21428 | 2024-09-28 05:12:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5dbcc269-f548-3afa-89f0-91531db05b3d | -21.84314 | -48.21941 | 2024-09-28 05:12:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b42fae10-2fd6-35e7-9752-6a58c256e4de | -21.84178 | -48.21468 | 2024-09-28 05:12:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bab9e30a-b055-358f-b3d0-87c05278eb25 | -21.84136 | -48.21972 | 2024-09-28 05:12:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01d35791-45f5-3f60-8379-3258322eb9fb | -21.83536 | -48.21421 | 2024-09-28 05:12:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bbc7f547-149e-3800-aeef-f3a6d782d7e9 | -21.623 | -47.75894 | 2024-09-28 05:12:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7cf184da-8844-3a08-a673-bda9fa9af3b7 | -21.62255 | -47.76465 | 2024-09-28 05:12:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1db848b9-6679-3ae7-b63d-790f98528d06 | -21.62211 | -47.77035 | 2024-09-28 05:12:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2bbc9ccf-5a76-3f4a-a241-783a4e7fc9d4 | -21.6164 | -47.75872 | 2024-09-28 05:12:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 42bdac51-bb07-34e3-b884-349f8c426e37 | -21.4126 | -47.77283 | 2024-09-28 05:12:00 | NOAA-20 | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| aee97704-8cdb-3237-ad0f-04b373c44dd8 | -21.40602 | -47.77267 | 2024-09-28 05:12:00 | NOAA-20 | CRAVINHOS | SÃO PAULO | Brasil | 3513108 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b4f2ddca-ce37-39bb-8561-d415a5974c77 | -19.46776 | -49.11486 | 2024-09-28 05:12:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3da3795a-ec6f-39ed-baf1-0a2963a76c86 | -19.46408 | -49.111 | 2024-09-28 05:12:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 06ad2497-1d15-39fe-b852-f80f4fbf06c7 | -19.46362 | -49.11567 | 2024-09-28 05:12:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9d2cbb68-4792-3c2f-a466-47ec960221be | -19.46228 | -49.10942 | 2024-09-28 05:12:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 06f4a802-d4e2-3ae6-be47-aaed95993b6e | -19.46185 | -49.11406 | 2024-09-28 05:12:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9475bc9b-6b40-3474-935f-50608060786c | -22.35427 | -49.32354 | 2024-09-28 05:12:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| dbe9b0b6-1b56-3fc0-945e-9bf0e4e6cb97 | -22.34827 | -49.32264 | 2024-09-28 05:12:00 | NOAA-20 | DUARTINA | SÃO PAULO | Brasil | 3514502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| dabf4aad-58ff-37c7-828d-ff2d99a96815 | -21.09492 | -49.1363 | 2024-09-28 05:12:00 | NOAA-20 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3dd4d015-7580-3b10-ad33-ea08952e44b7 | -21.09452 | -49.14081 | 2024-09-28 05:12:00 | NOAA-20 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5a61b092-e1c4-3e5c-88d1-b30713f76f2b | -21.08847 | -49.14056 | 2024-09-28 05:12:00 | NOAA-20 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 732fa935-be87-3f0d-b450-fb9cb8f3d9d7 | -21.08809 | -49.14491 | 2024-09-28 05:12:00 | NOAA-20 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7323dce8-359b-3937-8058-fa5801fa0aa5 | -22.5991 | -49.20631 | 2024-09-28 05:12:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5f39c3ce-b2c6-394d-bb97-fd3d51e7bfd4 | -17.0983 | -52.15187 | 2024-09-28 05:12:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3cdee980-22e2-3a69-9e1d-6ac80c2ee874 | -16.66774 | -50.59889 | 2024-09-28 05:12:00 | NOAA-20 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22fa314d-fadb-371c-b59b-f4802026cfce | -16.66737 | -50.60202 | 2024-09-28 05:12:00 | NOAA-20 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80a62bd0-cc2c-305d-acaa-dd37d5c84c5b | -16.66306 | -50.60164 | 2024-09-28 05:12:00 | NOAA-20 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1eeac5bf-acea-393c-a81c-8724d8489fe2 | -16.66218 | -50.60133 | 2024-09-28 05:12:00 | NOAA-20 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f1400e21-4d39-3ded-89e2-781cf3573703 | -16.66341 | -50.59851 | 2024-09-28 05:12:00 | NOAA-20 | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9b39933-93e1-37a6-b5dc-bc0f3456c37c | -20.9961 | -51.79768 | 2024-09-28 05:12:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c6cb2982-d2a8-3c99-8568-916972c660e0 | -20.80773 | -53.10622 | 2024-09-28 05:12:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 915252be-9c16-3e1e-89d7-64e01576b979 | -17.09414 | -52.14661 | 2024-09-28 05:12:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 486d98b0-b9da-3b60-b5fc-6f253ab82a7d | -17.09357 | -52.15131 | 2024-09-28 05:12:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb8b7ecc-be52-3351-94e9-6f7a4202217a | -20.80715 | -53.11135 | 2024-09-28 05:12:00 | NOAA-20 | SANTA RITA DO PARDO | MATO GROSSO DO SUL | Brasil | 5007554 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README93.md)
