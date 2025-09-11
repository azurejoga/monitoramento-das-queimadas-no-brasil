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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad48321f-25d4-32b9-a4da-4b2c76c40612 | -11.4137 | -43.54214 | 2025-09-11 05:29:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.3 |
| c789378c-60c7-3bdf-ba21-1da4a664310a | -6.56251 | -44.2078 | 2025-09-11 05:29:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| e409446f-c523-3e94-a46d-49056befb5a2 | -10.17173 | -46.18999 | 2025-09-11 05:29:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 80fd3e80-a32c-39b6-83f2-54bfa418dbf5 | -6.34243 | -43.77864 | 2025-09-11 05:29:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 7c42d78e-79f9-3065-a7bb-0aeabedfacf7 | -6.66773 | -44.12244 | 2025-09-11 05:29:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 473b28b4-de73-31da-bde6-80b4776350fd | -6.1936 | -43.48762 | 2025-09-11 05:29:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| c0383417-b083-304a-bea6-519a2d0b6439 | -6.37339 | -45.17226 | 2025-09-11 05:29:00 | AQUA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 44db05db-f4a8-348a-b608-ff269ba8dcde | -13.58253 | -47.67373 | 2025-09-11 05:29:00 | AQUA_M-M | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 04563492-5b31-3ac5-9bba-d43f0696b692 | -6.39638 | -43.50693 | 2025-09-11 05:29:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 8725ee1b-fbbc-30c9-9f9a-3d8db62f2f71 | -11.01739 | -45.05955 | 2025-09-11 05:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 4341e2b8-b510-343f-b8d9-331a98de3a4b | -6.30881 | -43.81932 | 2025-09-11 05:29:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 653d8d12-a32e-3b06-bb8a-ec17762c0f53 | -11.98877 | -47.57767 | 2025-09-11 05:29:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 9ebdcef5-9adc-3c35-a5b7-53873361d672 | -6.40248 | -42.60959 | 2025-09-11 05:29:00 | AQUA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| f500b775-2b8c-3f7c-a5be-b6d4c182b001 | -14.39932 | -47.30238 | 2025-09-11 05:29:00 | AQUA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 8ff11427-f55c-329f-bc61-7361ac0fcd88 | -5.55523 | -43.04663 | 2025-09-11 05:29:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b41cfe74-f052-398f-86b2-34107078a83d | -6.31373 | -43.45021 | 2025-09-11 05:29:00 | AQUA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| bbd77e08-d08e-377a-a69a-4940d465f287 | -11.46248 | -43.69793 | 2025-09-11 05:29:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 78028a1d-8b81-3da2-8b01-1256b39d364f | -5.65158 | -42.62158 | 2025-09-11 05:29:00 | AQUA_M-M | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 43dc0575-b2f9-3ecd-a3e3-989f44684e9f | -11.36234 | -46.54384 | 2025-09-11 05:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 1a582008-b9de-3b58-8bc4-dd782ab02ce0 | -11.33997 | -46.48297 | 2025-09-11 05:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 76ef1357-0b18-38dc-a701-b6c15fecb6b9 | -8.8777 | -49.54769 | 2025-09-11 05:29:00 | AQUA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 82e27da8-4e28-3845-9a24-51274bc72d7a | -11.02468 | -45.05267 | 2025-09-11 05:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 0f4800b8-3f2f-3c64-b724-c8a56bfdf236 | -5.54521 | -43.04498 | 2025-09-11 05:29:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 02f15f5e-2557-3168-b0cd-daa757be79e4 | -11.99998 | -47.58691 | 2025-09-11 05:29:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 3f22e51e-2b62-3b74-bd8b-f205b8df06c5 | -11.15555 | -45.30962 | 2025-09-11 05:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 1f006fb8-f253-3762-928f-9758baef3b6e | -6.24789 | -43.40938 | 2025-09-11 05:29:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| e6337051-5862-3ab3-b572-a6b6e3560928 | -6.24601 | -43.42137 | 2025-09-11 05:29:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 41ed5c03-c562-36bc-97ba-fb0855d1f31e | -9.04918 | -46.96214 | 2025-09-11 05:29:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 41.6 |
| a0f59771-1ac3-38f3-a1c9-592dd0e3b7a0 | -6.31528 | -43.81398 | 2025-09-11 05:29:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 9a945473-4b0f-3253-9ae2-88aab45aeb8d | -11.45711 | -43.60907 | 2025-09-11 05:29:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 7bf60f02-3d68-351a-9b0e-c44f2bc70427 | -11.98727 | -47.58473 | 2025-09-11 05:29:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 8755961f-e1cb-39d6-b4df-600e2a454564 | -9.04566 | -46.97685 | 2025-09-11 05:29:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 0b8b01db-5e06-3b40-bc37-d38bd46fb7c9 | -6.19166 | -43.49973 | 2025-09-11 05:29:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| dddbbd7d-c355-3ea8-b072-03d32bbfbb45 | -15.21974 | -44.03782 | 2025-09-11 05:29:00 | AQUA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 2dca481d-d3a6-37f9-991f-3e763366d6b0 | -14.13532 | -45.39489 | 2025-09-11 05:29:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 53806318-4360-38d0-b0ea-e2efed4e110f | -11.35626 | -46.50825 | 2025-09-11 05:29:00 | AQUA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 9b8ea7d2-75eb-31c3-8880-aa2afef8d1cf | -9.01621 | -49.76236 | 2025-09-11 05:29:00 | AQUA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| d8d85ddc-6c04-3421-834c-69b389d4c6aa | -11.47379 | -43.68874 | 2025-09-11 05:29:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.4 |
| bc1174c7-684d-3abc-b728-961a2461b24c | -6.34774 | -44.08706 | 2025-09-11 05:29:00 | AQUA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 30c90441-f375-3a76-8719-29254e2c7014 | -19.22836 | -47.99889 | 2025-09-11 05:31:00 | AQUA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 286.2 |
| df46ab63-0509-32ca-a717-7263b73ed23b | -17.39091 | -44.92355 | 2025-09-11 05:31:00 | AQUA_M-M | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9dc59184-1b40-3d0b-a489-e7d58ee90502 | -17.82932 | -46.73193 | 2025-09-11 05:31:00 | AQUA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 15.5 |
| c440c1a6-580e-34fe-ae69-fae316e2fdb3 | -15.1186 | -52.40351 | 2025-09-11 05:31:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 63.2 |
| c4531883-28cf-3d6a-99e2-7d147143887a | -15.10266 | -50.14919 | 2025-09-11 05:31:00 | AQUA_M-M | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 37.8 |
| 6447774c-0de9-33e8-8523-25279b37caf0 | -22.8001 | -46.4277 | 2025-09-11 05:31:00 | AQUA_M-M | PEDRA BELA | SÃO PAULO | Brasil | 3536802 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| cc289fbd-eafd-36d6-a744-5cb7f4b1b277 | -19.97796 | -47.62576 | 2025-09-11 05:31:00 | AQUA_M-M | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 108e14a2-7e39-3150-b870-1f22ef6100c4 | -15.11832 | -52.39604 | 2025-09-11 05:31:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 9de97c1a-fe19-354c-87f8-f0f2cab56df0 | -17.72862 | -44.42976 | 2025-09-11 05:31:00 | AQUA_M-M | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 938cc6c1-3c44-3493-a096-fcb0e3984cf4 | -17.37321 | -52.92195 | 2025-09-11 05:31:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 58.9 |
| ce7adc9f-c6e8-3329-a040-38c9f2769456 | -15.67367 | -47.01834 | 2025-09-11 05:31:00 | AQUA_M-M | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 25.4 |
| e21594d9-46f9-3798-bb3c-73dcc692464c | -22.8385 | -47.4693 | 2025-09-11 05:31:00 | AQUA_M-M | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 4e54f12a-e2fd-3595-8d7b-0dd6de4ae62a | -16.27934 | -45.6755 | 2025-09-11 05:31:00 | AQUA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| e0f61c1e-0c6a-3978-986e-48846748d104 | -17.55349 | -44.54559 | 2025-09-11 05:31:00 | AQUA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e5180c60-e89f-3301-9968-86f4bcdd46b7 | -18.00362 | -47.99194 | 2025-09-11 05:31:00 | AQUA_M-M | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 36a418cc-ee10-369f-983d-68a2977cb1d7 | -15.9795 | -42.9798 | 2025-09-11 05:31:00 | AQUA_M-M | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 25b69f47-fee4-3ce6-99f8-2ac11a8845ec | -20.70015 | -46.07049 | 2025-09-11 05:31:00 | AQUA_M-M | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 20.0 |
| c59ab1f5-ebb4-31ee-b77c-7d76fcda24f6 | -19.22546 | -48.01483 | 2025-09-11 05:31:00 | AQUA_M-M | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 154.0 |
| 82068d75-08ba-3f9f-8c4e-cdba5fb1368e | -18.55711 | -46.55949 | 2025-09-11 05:31:00 | AQUA_M-M | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 278fe719-f374-3afc-8b2a-71cd551f390e | -15.11007 | -50.12689 | 2025-09-11 05:31:00 | AQUA_M-M | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 1eea8170-f833-3431-a816-e5e3613a889e | -15.12228 | -50.12442 | 2025-09-11 05:31:00 | AQUA_M-M | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 17.7 |
| c96aa57f-afc0-3685-b332-4753fe5e0d14 | -19.99977 | -47.6293 | 2025-09-11 05:31:00 | AQUA_M-M | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 775ef917-c2d7-3d9f-8f9e-cb0037dd9b53 | -20.03515 | -42.73634 | 2025-09-11 05:31:00 | AQUA_M-M | RIO CASCA | MINAS GERAIS | Brasil | 3154903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| cfb02665-741e-3b2f-86b9-e3b0dfcda2e3 | -20.16073 | -41.03614 | 2025-09-11 05:31:00 | AQUA_M-M | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 559203af-369d-3771-8a24-0a162baec7ef | -17.36892 | -52.91638 | 2025-09-11 05:31:00 | AQUA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 47.3 |
| f4203f56-ee28-3e3e-ab2d-8b5d5b72f9b5 | -15.61604 | -47.54204 | 2025-09-11 05:31:00 | AQUA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 15.0 |
| ede4c31a-b960-3763-abb7-63be50f95c70 | -21.4283 | -45.47113 | 2025-09-11 05:31:00 | AQUA_M-M | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 184df52c-90be-3b77-82fe-5366021b3ce7 | -20.03654 | -42.72704 | 2025-09-11 05:31:00 | AQUA_M-M | RIO CASCA | MINAS GERAIS | Brasil | 3154903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.8 |
| 705ac78c-6663-346f-8808-883ae38ab88a | -15.61911 | -47.52481 | 2025-09-11 05:31:00 | AQUA_M-M | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 29.0 |
| 100be88b-0ee9-3c26-b8da-b8758f2162b6 | -19.98884 | -47.6277 | 2025-09-11 05:31:00 | AQUA_M-M | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 48.2 |
| c7a310f1-db55-316d-9ce9-01b02c6ed9ae | -15.12462 | -50.12952 | 2025-09-11 05:31:00 | AQUA_M-M | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 3f1f2f34-d864-3453-b366-04bffdde164d | -15.67419 | -47.01307 | 2025-09-11 05:31:00 | AQUA_M-M | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 2803aba0-7227-3ac1-b6d6-c96b98736f12 | -16.27801 | -45.68087 | 2025-09-11 05:31:00 | AQUA_M-M | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3812f583-f08f-3a9c-a800-03ba8fa3d8d2 | -15.10773 | -50.12185 | 2025-09-11 05:31:00 | AQUA_M-M | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 18393aa5-b8eb-3caa-b9e4-6fb6f333637f | -19.98046 | -47.61169 | 2025-09-11 05:31:00 | AQUA_M-M | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 15.5 |
| a252e911-e515-382e-bddc-1e44f6a83481 | -15.10478 | -50.15435 | 2025-09-11 05:31:00 | AQUA_M-M | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 29.1 |
| e6631b27-0a11-3d7f-b674-81d4a0afa07f | -15.67102 | -47.03317 | 2025-09-11 05:31:00 | AQUA_M-M | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 74506ab9-b1bb-3b3f-b89b-94c1e1fa43d5 | -16.29311 | -50.05156 | 2025-09-11 05:31:00 | AQUA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 23.2 |
| a8ee8eb2-2f49-3489-b583-beaeab0cee12 | -17.2595 | -46.08036 | 2025-09-11 05:31:00 | AQUA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3e2201c1-f0dc-315f-a055-9f9f06e6effd | -15.13598 | -52.40554 | 2025-09-11 05:31:00 | AQUA_M-M | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 46.8 |
| fe10131a-e634-3ecb-b645-6d9e84a6c83b | -15.67163 | -47.02805 | 2025-09-11 05:31:00 | AQUA_M-M | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 7036123d-eb0d-34ed-ab47-17deea975727 | -20.14498 | -43.66323 | 2025-09-11 05:31:00 | AQUA_M-M | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 22c45c4f-211d-3937-a960-fa2db629f57d | -20.15162 | -41.03405 | 2025-09-11 05:31:00 | AQUA_M-M | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 550dac1c-8555-3692-b9d1-fa0ed4f01bd6 | -17.56279 | -44.54712 | 2025-09-11 05:31:00 | AQUA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 882c682d-62c2-380e-93e3-638402a115a2 | -22.92555 | -48.38737 | 2025-09-11 05:33:00 | AQUA_M-M | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 14e86fbb-dab0-3e06-9677-aba011ff2eb7 | -22.59037 | -51.87664 | 2025-09-11 05:33:00 | AQUA_M-M | SANDOVALINA | SÃO PAULO | Brasil | 3545506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 35.4 |
| 6fbac6a9-6fc4-3c89-accc-1cf2f14d9c29 | 0.42833 | -50.75437 | 2025-09-11 05:33:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d813358e-8bea-370f-bfec-050244f43620 | -3.79657 | -51.15843 | 2025-09-11 05:33:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 07026a76-68ae-3f56-a583-65448fe1e6b7 | -3.31959 | -54.91436 | 2025-09-11 05:33:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cbb2e333-8ff6-3470-ba85-6a6c99d85acf | 3.87846 | -59.63899 | 2025-09-11 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af639a4d-2c63-3447-8887-28b0099312f6 | -3.32002 | -54.91137 | 2025-09-11 05:33:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74e0baf5-aa45-3901-98ca-4003b3aecdde | 4.12855 | -59.97403 | 2025-09-11 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6285253-efa9-3c3e-bb9c-4ee05d87183e | -3.24341 | -50.80346 | 2025-09-11 05:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 08512b25-38e8-3c22-a5e6-2c2a9271d592 | 4.12799 | -59.9705 | 2025-09-11 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf5e99fa-68ee-3b6c-bcb1-cdd3280d7ce0 | -3.32008 | -54.91146 | 2025-09-11 05:33:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b3b660cd-2e4e-3016-bf73-323f772b47cf | -22.92814 | -48.37289 | 2025-09-11 05:33:00 | AQUA_M-M | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 16daeedd-c2e9-391c-92eb-a47914572124 | 4.12519 | -59.97453 | 2025-09-11 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c6a2b53-d4ea-359a-938d-a797df022afb | -3.31963 | -54.91443 | 2025-09-11 05:33:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1bb5d94f-5575-3efe-833d-67ccd431528e | 0.43011 | -50.75256 | 2025-09-11 05:33:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 28fb3b38-d26e-3e7e-bfcd-fe49f740da42 | -23.14652 | -48.25067 | 2025-09-11 05:33:00 | AQUA_M-M | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 5538d0ec-b51d-3bdb-95ce-e656d1aafd90 | -3.24421 | -50.79796 | 2025-09-11 05:33:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |


[Clique aqui para ver as próximas entradas](README125.md)
