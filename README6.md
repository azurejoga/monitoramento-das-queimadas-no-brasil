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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e016b9b2-30ef-34f5-93c7-a276fe92e8fa | 3.9356 | -60.59996 | 2026-03-02 05:10:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a23b276-ba62-357c-a42b-acad6e98008e | 3.04688 | -60.67094 | 2026-03-02 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a8ca9c70-eda0-3164-9c75-db0dbc4e6d38 | -24.33448 | -49.72777 | 2026-03-02 05:16:00 | NOAA-21 | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1833e670-b04c-37ec-87df-cd045c4aaa83 | -18.79785 | -57.6181 | 2026-03-02 05:16:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| f7a2369b-fba4-35ad-9bb7-ece1945bcd3d | -21.09554 | -48.74469 | 2026-03-02 05:16:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 9b68496f-e4b6-3030-a178-7c50cc455a7a | -18.80137 | -57.61866 | 2026-03-02 05:16:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 23a4ce7b-cede-3975-86cc-db92ca943ade | -24.33327 | -49.7281 | 2026-03-02 05:16:00 | NOAA-21 | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8b8efc22-f59e-3052-a7ef-04fc0ba23954 | -18.79375 | -57.62167 | 2026-03-02 05:16:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.8 |
| f5e1c5da-2f53-3193-9b65-359e355fea48 | -18.80195 | -57.61452 | 2026-03-02 05:16:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.5 |
| 710eb884-07fd-392c-bd69-dd7ca8e17cbf | -18.79726 | -57.62223 | 2026-03-02 05:16:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.3 |
| a40285f8-ed05-360d-92df-424c32786ec5 | -18.80548 | -57.61508 | 2026-03-02 05:16:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 98b1388a-22ef-3e14-b6e0-60be272c4548 | -18.80488 | -57.61922 | 2026-03-02 05:16:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| a3482852-0dc7-3f51-81c2-da4ae9c0964a | -30.10757 | -52.67645 | 2026-03-02 05:18:00 | NOAA-21 | RIO PARDO | RIO GRANDE DO SUL | Brasil | 4315701 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| b63e2b95-e37d-347d-872d-27f8414efc8e | 1.5046 | -59.9306 | 2026-03-02 05:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 0487e1b1-2a7a-31fc-9a1e-e3bde5e2625a | 1.5047 | -59.9116 | 2026-03-02 05:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 300c75ca-0278-383f-b1e2-5cb7a82f743d | 1.5047 | -59.8925 | 2026-03-02 05:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 1093cab8-9262-399b-8ce4-6bec296d2f6d | 1.4864 | -59.9117 | 2026-03-02 05:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.3 |
| e8ed867b-73dd-3af9-b127-27f9f13cf281 | 1.5047 | -59.9116 | 2026-03-02 05:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 1cea2ce0-2aea-31d2-8cb3-eb61d3b99a46 | 1.5047 | -59.9116 | 2026-03-02 05:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 90.9 |
| d9bd6109-fb49-37df-ad4c-46199048aa75 | 1.4864 | -59.9117 | 2026-03-02 05:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.4 |
| da2a9266-c177-3b05-8692-f435d257125b | 1.5046 | -59.9306 | 2026-03-02 05:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 1e3bbf5e-1548-3fb0-8519-88bd5060161a | 3.64554 | -61.04627 | 2026-03-02 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e8a6313-ad7e-3003-beea-47c6c1899103 | 1.47319 | -59.92298 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7aed4676-1578-33b2-bcc9-623ee33aa706 | 1.51406 | -59.93568 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a0f0435d-2b84-3063-841e-dd251e1db298 | 1.16717 | -60.83361 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9fe9cee-6e10-3259-9b14-64a2e947cde1 | 1.47724 | -59.92623 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 808baeaf-ae24-356f-acd3-90d7e5d30590 | 1.08857 | -59.2484 | 2026-03-02 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 468349ab-35c2-3b05-9005-6d7e1f54af23 | 1.00278 | -59.55258 | 2026-03-02 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1440fadd-652b-39cc-8726-b1e297b3c23b | 3.64831 | -61.04229 | 2026-03-02 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6c2f86e-d93f-3a56-aec0-de3b523f6ee6 | 1.09396 | -60.17484 | 2026-03-02 05:40:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4fc42ca1-e0ac-3e04-ae66-ff9871a877c5 | 1.50826 | -59.92134 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.8 |
| aa2972df-9b80-3d11-bba2-5f29cc6f7f6f | 4.25626 | -59.91321 | 2026-03-02 05:40:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76daba4b-f864-3542-a9cb-31642619af0a | 3.18707 | -60.67966 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61e7e392-7b82-381c-85fe-2a320d6499a2 | 0.74206 | -60.15996 | 2026-03-02 05:40:00 | NPP-375D | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e5fb4fe-64ac-3437-a111-b20d629f0953 | 4.36992 | -60.62245 | 2026-03-02 05:40:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 299f83e3-eeaf-3024-8a34-5e61f00d0092 | 2.18706 | -61.92626 | 2026-03-02 05:40:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ae791dc-d03b-388d-8c83-5b3870fd48f7 | 1.82958 | -60.84562 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5acedeec-37f4-3b75-bc15-f2604e380945 | 0.49607 | -60.49869 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 270d8f15-8618-39b8-8d20-db42486c27c3 | 2.86206 | -60.82742 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef9054f4-f4da-39d1-91b6-a761773f6617 | 0.30572 | -60.44556 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8243d70b-7a0d-3ed8-979f-718586e8d8a1 | 1.45453 | -60.07093 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 764cd6eb-9d5a-3954-a2ba-b8df20978c5c | 1.15485 | -59.87497 | 2026-03-02 05:40:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9dc2c9ae-0754-3d58-a17b-c74e1c809ec1 | 1.72923 | -60.54916 | 2026-03-02 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d44ca4e3-cdac-3558-ade2-dee4db0c4f6d | 2.86096 | -60.84192 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76404541-e898-30b0-b334-149c94845c40 | 3.16837 | -59.90746 | 2026-03-02 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34bc3e6c-9f50-31eb-afc4-cb20f0398992 | 0.80018 | -59.86656 | 2026-03-02 05:40:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.2 |
| f4feaf72-1616-32e0-8682-94ed17776240 | 4.37714 | -60.6249 | 2026-03-02 05:40:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a63cac6-f0ae-3a65-a83a-83a8d4e422a1 | 3.60766 | -61.66394 | 2026-03-02 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 954d66ff-23e2-3339-8b4e-27fa7f7a239c | 3.41182 | -60.83764 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff09d871-036e-34f9-a3c3-4c9dc9854a6a | 4.06829 | -59.89773 | 2026-03-02 05:40:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 812e294c-4a9c-3f33-ab3a-f4f3f47f9870 | 1.51003 | -59.93252 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b54bc51d-cca6-3032-9df8-7bcd0d04e923 | 4.35211 | -60.57513 | 2026-03-02 05:40:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e578e9e7-c0b7-3615-98a6-d916f8cbc3e8 | 0.89251 | -59.79044 | 2026-03-02 05:40:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c49a3e06-f4b3-3b5f-8974-921dcd42eac6 | 0.45196 | -60.39688 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba6f0bec-6dc1-38c0-ab12-811bf52053dc | 1.45796 | -60.07038 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48669bbc-c605-3351-8736-d83e47498974 | 3.17207 | -60.69291 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0a66aa0b-27b4-33e4-8dd8-87d59a0dbfdb | 3.41738 | -60.82962 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| efe9ae5f-8915-3a2a-b79f-a1d5cedb4c21 | 1.036 | -60.51684 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c9e5d56-64e0-34d1-aaa9-4e3314a52152 | 1.16437 | -60.83768 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64b6d4c2-45e7-3bcc-a6be-5e1439e0b008 | 3.45792 | -60.78395 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 66f57ec9-b2e5-30f7-98a0-2284e681b076 | 1.45393 | -60.06721 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b74252a-b89b-3d50-84c7-8431ba6ccd1c | 0.92255 | -60.52676 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad52aedf-3713-3ed4-9df5-345a88e36990 | 3.17236 | -59.91057 | 2026-03-02 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ee9c8140-f1bd-3738-b4dd-da35a7d4ca01 | 1.51633 | -59.9277 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6805af79-2e1d-344e-ae79-daa3fe35a783 | 3.08332 | -60.01012 | 2026-03-02 05:40:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5b936ae2-566c-3331-8944-396b2ee4386f | 1.48877 | -59.93209 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62b453be-792c-3530-9ace-a9a2c1e8ba16 | 3.19097 | -60.68261 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf53a729-26d5-33f1-afbf-15f450cd9172 | 1.49792 | -59.92294 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e644507-80d4-3082-b22c-e96d8ec743a9 | 3.42681 | -60.82456 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02639e23-723a-3268-909e-4d4511ae2772 | 3.42404 | -60.82857 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c12a6fb-c378-3aee-b9be-9c08599c12d2 | 1.50246 | -59.90695 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| cd8dd4dc-7739-325a-aa5d-72d78eb63ec3 | 1.48414 | -59.92514 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 433b9779-cee3-39df-a05f-808af68c6be0 | 2.85817 | -60.82445 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 00657dc9-6081-311d-8380-0dc92d11a741 | 1.50423 | -59.91814 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 55da5036-4d3e-3cb2-a3f2-8fda75000de5 | 0.45821 | -60.39214 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 58752df4-31d2-31e7-95fb-af2ee319be85 | 1.48129 | -59.92945 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c47c873-09ae-37dc-961e-ddb64270b8cb | 1.1197 | -59.1987 | 2026-03-02 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0ba443cc-a1e0-390c-8d88-97464e5e2c2e | 0.87082 | -60.4643 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 42913e35-0f0e-3c4b-957b-6ee8ca3142be | 1.07139 | -59.25519 | 2026-03-02 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 509cc4e3-74ed-3568-b7a2-48b1f1b3d4d7 | 1.11613 | -59.19927 | 2026-03-02 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79494500-bba6-39b6-ba10-69728630e04a | 1.48924 | -59.91277 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4b6ae798-9dd3-3def-8ed4-1361c3da7a73 | 2.85018 | -60.83285 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 81ffe049-f04b-3d19-994c-bc59952741b6 | 0.45312 | -60.40422 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 420a262e-e866-3819-8cec-877776fe8094 | 1.51347 | -59.93196 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57dc90bb-02b8-326f-8ce7-75462fdaf407 | 4.08351 | -59.88439 | 2026-03-02 05:40:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a538d78f-ea63-3d69-a7ad-fb4b923f6c67 | 3.64499 | -61.04281 | 2026-03-02 05:40:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d9fbaa0-ad35-3302-bd30-710ed5219cc3 | 3.83546 | -59.94891 | 2026-03-02 05:40:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3b5d528-ea68-36a5-95aa-107edae75b40 | 3.57872 | -60.33333 | 2026-03-02 05:40:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aed57a42-39d0-3546-9de8-e28c8eb314d5 | 3.01765 | -60.69564 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d2c7fa1-6264-3f02-b992-946fe07e63f3 | 3.04776 | -60.66932 | 2026-03-02 05:40:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2f4164d0-874e-3194-9e37-b0b8c80e535f | 1.47438 | -59.93048 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ffb7b8f-220a-3922-b3a5-412dbda42300 | 0.85471 | -60.40716 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0511f42-1c4a-3959-9ca5-805a77c72064 | 1.16157 | -60.84175 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ea6c624d-ea6b-3245-a949-d5afa9f890d0 | 1.5123 | -59.92453 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 57357585-b67c-397c-bb75-432bb53186a5 | 1.47784 | -59.92998 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d212508-2e50-32c8-8dee-e8c63ae163b8 | 4.50322 | -60.54495 | 2026-03-02 05:40:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7670f70a-f8ce-37d1-8639-9df324766d61 | 1.4801 | -59.92194 | 2026-03-02 05:40:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68bb26fb-fbb8-3287-afca-6caaa239d683 | 2.22741 | -60.75114 | 2026-03-02 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8035ea0b-7859-3935-8fb1-5b94eabfc7e1 | 0.80079 | -59.87037 | 2026-03-02 05:40:00 | NPP-375D | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 569463f4-d35d-3360-ac9c-d1a9e9824974 | 0.0554 | -60.98354 | 2026-03-02 05:40:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README7.md)
