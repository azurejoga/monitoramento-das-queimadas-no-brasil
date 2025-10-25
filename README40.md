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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52bbc3a2-03ae-3d11-b9ad-f85bff805b5b | -8.31173 | -47.8627 | 2025-10-25 04:19:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04658c11-5554-3423-9902-0c3df2d09e47 | -9.9992 | -47.59045 | 2025-10-25 04:19:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3602415-437c-32a2-afe7-e000e8875f3e | -12.77762 | -47.38031 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4eb3441e-1e27-3513-8653-d6ab06eaecb2 | -10.46963 | -50.20932 | 2025-10-25 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b4e6831b-0e8e-3bb2-aba7-00615d93d5a7 | -12.69785 | -46.33208 | 2025-10-25 04:19:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3330a62f-0f7e-3882-bfe9-26e4a5c9edc0 | -13.33375 | -47.95119 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1be4b09-9b7d-3f54-80d9-f997fb84de23 | -13.33407 | -47.92793 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ed0e38a-9d29-3706-b8ea-63ebf58572a1 | -8.33825 | -46.17623 | 2025-10-25 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 946de4e2-5cf2-3b44-ba17-6ddc9284eb4d | -7.58602 | -43.58302 | 2025-10-25 04:19:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c9a0a5b-1170-371a-b9fa-a4d3a70cac55 | -10.67807 | -48.09125 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5b0efc18-369b-32f7-9e33-0492a3033811 | -10.63646 | -47.92325 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 136fc2ff-71ef-3930-b032-b631326b623f | -9.99613 | -47.09259 | 2025-10-25 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 312bd499-6e5a-31c2-a82c-7fb4e28633d1 | -12.77688 | -47.85954 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b6a3a332-084d-3b82-8c52-447f2f15ec0b | -10.96351 | -50.28608 | 2025-10-25 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8d439d1-dc20-3c13-9960-0283718de501 | -6.82639 | -44.01299 | 2025-10-25 04:19:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dfba4b03-8103-3e84-998e-9b50a1ab58bc | -7.62948 | -44.56708 | 2025-10-25 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55637ff8-8983-3809-bd70-81b89daa8c32 | -5.81847 | -52.10101 | 2025-10-25 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d0a3016a-10d4-3b5f-91d0-34b43d884706 | -7.86552 | -46.73027 | 2025-10-25 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 94d359e5-0f80-3e65-9d72-504af636594c | -7.96633 | -38.28152 | 2025-10-25 04:19:00 | NOAA-20 | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 2.1 |
| aeb42c27-eb85-3e80-af65-23b4548f69c0 | -13.2885 | -47.49915 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a06bef40-a40a-3948-a7c2-4be9ca7aead7 | -13.40966 | -47.96056 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 967e6e4a-6fee-3d28-89be-502a6d7326d3 | -6.97378 | -46.42886 | 2025-10-25 04:19:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e99ad634-f2f6-3401-808f-d1c42e51b535 | -10.65067 | -48.06139 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f658589-de12-3c81-b961-3a90632a4808 | -8.7778 | -45.76913 | 2025-10-25 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c4095f2-6024-3861-84f3-a06812587648 | -12.82993 | -47.262 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 86aab132-6dc8-3fe1-8fc1-a192d92719ab | -12.83117 | -48.66784 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2e81e4a7-c56a-32e1-be6d-7c26fb438054 | -13.03809 | -47.38295 | 2025-10-25 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 68ec4d74-93af-38c2-beda-09e59f37d624 | -7.43966 | -46.60859 | 2025-10-25 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 23353a56-0bfe-388a-86fc-fa96260d2fe6 | -10.79454 | -44.9151 | 2025-10-25 04:19:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c1cd312f-6a50-3739-92bf-040551370faf | -10.44738 | -44.9641 | 2025-10-25 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 7ad21023-a11a-3df0-a376-309bdc7d6696 | -12.04671 | -46.40924 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 563506f3-74f8-36e0-adff-424776375eb0 | -13.34939 | -47.41194 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 943898bf-2f9c-33e7-9ca1-cd72e0b49b91 | -12.29859 | -47.4585 | 2025-10-25 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 947173ab-3aef-3c99-b050-db0c29edc148 | -12.22633 | -47.21391 | 2025-10-25 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 765e2c9e-65ff-3659-a7b2-ddba4f7ca1cc | -5.81876 | -52.10495 | 2025-10-25 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a5bb927-bcda-3e10-a3be-85ab64e99dc1 | -13.03749 | -47.38659 | 2025-10-25 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 53a86043-dafd-3ecc-b38f-e190a836eef8 | -9.99731 | -47.60196 | 2025-10-25 04:19:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec479ef9-2e71-3cec-980c-f6713bd06c96 | -12.09749 | -46.4108 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51c50c58-a9c6-326a-aa86-cb0789d96312 | -12.9466 | -48.50137 | 2025-10-25 04:19:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc0e0939-e42e-3e5c-af51-bf2f46485d60 | -6.89183 | -43.6137 | 2025-10-25 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37b35926-3872-3111-a447-8ceaa9969a7a | -9.61005 | -46.89706 | 2025-10-25 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 22e45748-bebf-3071-a35b-985db7671ded | -10.96263 | -50.29115 | 2025-10-25 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 736fdcd4-1db8-35a5-813e-c8c0c7dc3b0f | -12.85421 | -48.55278 | 2025-10-25 04:19:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e98193e4-158a-365c-8a92-8a0aec393969 | -12.21534 | -46.50216 | 2025-10-25 04:19:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c97c1694-12bc-3647-af02-ebf576722772 | 1.65014 | -55.72762 | 2025-10-25 04:19:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2fefa50b-49a3-394d-a2d5-5c2696d9f548 | -11.55457 | -54.51862 | 2025-10-25 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1c11271-17a4-33d5-aca8-7799907b961e | -7.58432 | -43.5718 | 2025-10-25 04:19:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 714aea74-1110-3ca5-9e97-a241075a604f | -6.81771 | -45.4437 | 2025-10-25 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 683569d4-9b4c-3185-933c-f0f3ff3de036 | -1.49145 | -47.81133 | 2025-10-25 04:19:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 638f4a5f-94a1-328d-89dd-87166d386730 | -12.08533 | -46.42306 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 07d8177f-fcbc-38dd-86a1-f1b37b01ca5f | -7.00363 | -43.46755 | 2025-10-25 04:19:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 950f4882-5e65-39c3-b091-224c623c5e80 | -9.99186 | -49.31374 | 2025-10-25 04:19:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5b97d683-6c30-3ea8-b2d4-d4d8f25f9566 | -12.25253 | -47.44317 | 2025-10-25 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4fde9ad2-816e-378f-bf10-90a999a3cb28 | -9.30252 | -45.1818 | 2025-10-25 04:19:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b3406b2-9c2a-3df3-a388-33cd439d8999 | -10.92871 | -50.41683 | 2025-10-25 04:19:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b9a289e8-4ca7-3508-a0ce-168e069f9430 | -6.95732 | -43.50053 | 2025-10-25 04:19:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 850935bb-5dca-3534-9480-ddb8ac981922 | -6.88849 | -43.61317 | 2025-10-25 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93dd9986-8e0f-3d5c-b56b-4ce5e4bfb3f0 | -10.59832 | -47.98122 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d09786b7-11dd-3d0a-bddf-a222deb8e3e9 | -8.05001 | -48.28754 | 2025-10-25 04:19:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6562ded0-ae3a-323f-ab73-8bd974289a3b | -9.57964 | -48.5631 | 2025-10-25 04:19:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 02d8a4a2-a355-36bf-9688-13de16da55b7 | -13.32508 | -43.0973 | 2025-10-25 04:19:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a569f608-fb7e-341d-8454-835d0d0bb90d | -13.04924 | -47.20957 | 2025-10-25 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e2a21525-c59a-30ba-94ae-48228d0a5fd6 | -6.91187 | -45.173 | 2025-10-25 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 84c2bc71-a1c9-3c52-9565-6a9ca6f26541 | -13.64582 | -44.23117 | 2025-10-25 04:19:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b33e51f4-8e9e-335e-af46-63a338715e3f | -12.23738 | -47.48679 | 2025-10-25 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49b975cd-9c32-33dd-bef8-a8f35da4e24f | -11.96707 | -48.19235 | 2025-10-25 04:19:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe127e5a-6a8a-3a5f-886c-e41e4dc0f62b | -12.46607 | -44.53253 | 2025-10-25 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73525170-2d53-3e8e-a7e8-248dc7fd079b | -10.25462 | -47.99864 | 2025-10-25 04:19:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e80f41a5-0a36-3194-a59f-b5155476ec68 | -10.65904 | -44.71651 | 2025-10-25 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 00d0c9e2-56da-338e-948a-de26f9941511 | -13.26901 | -47.98308 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a4a5116d-73b8-3f3b-b8a6-765dea41ccbf | -10.65631 | -48.07067 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f600f211-1960-3c19-bf0e-95a74b0efd57 | -8.10529 | -44.5 | 2025-10-25 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 62117f04-85f0-3e14-8d4f-6c3e20167e03 | -12.12387 | -46.71371 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 14932b78-98c4-3125-b70c-417f2fce0e1b | -13.05593 | -47.21066 | 2025-10-25 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2e8dd3e1-588d-35a7-86e8-3f99a07e094b | -6.73666 | -44.15174 | 2025-10-25 04:19:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 64f68f4a-4d3a-3e9e-9e3b-be785ef6955e | -12.0434 | -46.40867 | 2025-10-25 04:19:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a1d60dd-08c2-3d43-9c8d-b1777736c4c4 | -13.34997 | -47.40836 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e40f681-74d8-3f57-afac-ffa52e875619 | -12.15108 | -48.01678 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 411e9147-0daa-3640-92e2-25aaaf53ed6a | -10.98262 | -44.73076 | 2025-10-25 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 749189bb-aa40-3f21-af2b-470f7af4bf9e | -13.40751 | -47.9524 | 2025-10-25 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ba767a71-65ba-3a0c-99f9-0bd5689c7026 | -10.41391 | -44.74256 | 2025-10-25 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f1b57d6-14a2-3412-ad1c-baa33049719e | -6.80606 | -42.39298 | 2025-10-25 04:19:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 4e198645-2f3f-3934-8e45-51f28db2b61a | -13.08738 | -47.56815 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e652207-1935-395d-ad71-12c38414ee24 | -7.99092 | -49.25263 | 2025-10-25 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| da16d9e4-8d31-3c35-9397-44c5c3f8ac78 | -6.91242 | -45.16952 | 2025-10-25 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b60f26bd-56bf-3893-9fea-ce6845bb83ca | -6.96512 | -43.49448 | 2025-10-25 04:19:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 21bdb92d-d048-3ec7-a7f5-eab5abebe1f7 | -9.25407 | -45.59496 | 2025-10-25 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6af4d449-3bd3-3dc5-8b7e-8b8d33efd064 | -7.14795 | -44.12795 | 2025-10-25 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a31c9fbc-ceeb-343f-93e2-51140909e7ab | -11.359 | -54.32521 | 2025-10-25 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 325587b3-1a1c-3849-ace5-abd4e6b28737 | -12.77347 | -47.85894 | 2025-10-25 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7a91f863-bba6-396f-9ca3-5ec43dbfe730 | -10.65355 | -48.08724 | 2025-10-25 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 680e331c-b8f2-3e01-b5bc-800501864b03 | -11.89971 | -43.06456 | 2025-10-25 04:19:00 | NOAA-20 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 74ac06bb-8fe9-3f37-99ff-c96808beb105 | -12.06742 | -47.12846 | 2025-10-25 04:19:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1783695d-17cf-3e80-b3e9-33e7b77ddfdd | -9.08877 | -47.81264 | 2025-10-25 04:19:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d8e58f6-e8ee-3bed-8abb-a84bc607cd1f | -10.26553 | -43.96928 | 2025-10-25 04:19:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b6c239f-ba46-3664-909a-d9fe928cd717 | -6.89796 | -43.61826 | 2025-10-25 04:19:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 73aacfa5-b820-3926-9088-6bd4db57877c | -6.79414 | -45.42175 | 2025-10-25 04:19:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 736d5a01-55a7-3e09-9ba3-a61d8ae6d905 | -9.31266 | -46.98143 | 2025-10-25 04:19:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7b9d2b3-e7b6-34d8-a1e7-4e30dea82ac5 | -9.99795 | -47.59811 | 2025-10-25 04:19:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8b4786b-9420-3f8c-9e47-7ebcc67d7fdd | -10.83964 | -48.81245 | 2025-10-25 04:19:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README41.md)
