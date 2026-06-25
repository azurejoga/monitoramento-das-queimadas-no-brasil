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
| 72745e34-84fd-3637-9489-a2ddf2bd54c7 | -11.91697 | -44.1697 | 2026-06-25 03:28:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c1d7535-b956-3c6a-b274-f2ea14791496 | -7.7324 | -44.17868 | 2026-06-25 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ba2bcb3b-8575-370c-a001-7ee1de1732c6 | -11.91465 | -43.40407 | 2026-06-25 03:28:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 95f03bab-6ebf-3cfa-9b0b-2af56c38a5df | -5.75331 | -43.19395 | 2026-06-25 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| da43f50b-0e82-3198-940f-174567f3b791 | -11.23084 | -43.33508 | 2026-06-25 03:28:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 15d177c6-15a8-33a4-90d0-9a3f8255c23e | -11.2517 | -43.327 | 2026-06-25 03:28:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6eef1739-ab9b-3211-a2fe-094d0179ab29 | -11.90854 | -43.40272 | 2026-06-25 03:28:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d733f681-5dab-3f8b-9c5e-052cb7b3fa84 | -6.97317 | -42.89099 | 2026-06-25 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 3f9f9611-7e91-365c-9a4c-e295c0675658 | -7.75375 | -44.62025 | 2026-06-25 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 21e962d0-0db8-3dd4-a162-3f3ad1865c34 | -6.9934 | -42.89038 | 2026-06-25 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 008b53bb-0b3b-37e3-8e79-d2c64a271c1a | -7.76207 | -44.61502 | 2026-06-25 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e8d0e228-3dce-3966-a9a3-ede199808719 | -11.91399 | -43.40461 | 2026-06-25 03:28:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 675036d1-f402-34b6-acf6-8c77210fae4b | -7.76079 | -44.62159 | 2026-06-25 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3f18a7c4-3230-3d4a-8508-c6e8984636e9 | -11.2236 | -43.33916 | 2026-06-25 03:28:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ff1ac854-9c93-35c2-8877-fe9fd720747d | -6.97307 | -42.89192 | 2026-06-25 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 4d3eb19c-f336-379c-b747-91d0861a0d02 | -5.81528 | -43.58785 | 2026-06-25 03:28:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a049eb57-e03f-3f02-83fd-cd954a7d7576 | -11.91301 | -43.40938 | 2026-06-25 03:28:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7d208d1-103a-30ac-9c05-42ac918f69b3 | -7.74796 | -44.61241 | 2026-06-25 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9c3c1154-6a60-3491-8f07-26a315aca3c1 | -6.98597 | -42.89436 | 2026-06-25 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| aeef8acc-0ea1-3235-a4ec-e5366229861c | -7.74536 | -44.62582 | 2026-06-25 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 5bc418c6-775e-3cf9-b62b-a7db569355e6 | -9.19094 | -45.32395 | 2026-06-25 03:28:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ae0a165-ec10-3ee2-baee-3359007395c5 | -7.75496 | -44.614 | 2026-06-25 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 109fc469-f1ae-35a0-8246-7bf546080c6d | -7.7498 | -44.6184 | 2026-06-25 03:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 035c0be3-dcd0-3a33-9943-a4ad68c1338a | -12.7373 | -44.4521 | 2026-06-25 03:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 8f725a5a-39cf-336b-8a35-33dd7daeae09 | -17.12046 | -41.34454 | 2026-06-25 03:30:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b4c46671-9848-30bc-9d22-f1fc465278cf | -12.7441 | -44.46796 | 2026-06-25 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9080eca4-59fa-3454-be20-4ad68bd58b20 | -14.85464 | -42.7922 | 2026-06-25 03:30:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7eb7dd4f-a819-302b-936d-cf523373da8f | -12.74528 | -44.46247 | 2026-06-25 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| fba08364-7b40-3f1f-91e1-d2a1779501e3 | -15.75647 | -43.23291 | 2026-06-25 03:30:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9c5ce7d3-9246-31cd-9bdc-e5cbd0d70b4f | -12.74644 | -44.45701 | 2026-06-25 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| d8772c7b-0c03-3952-a95e-e88a4a6ed2a4 | -12.74593 | -44.45683 | 2026-06-25 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 1b19dd8d-0aa4-3102-9fec-f9b1ade668b0 | -12.75169 | -44.46388 | 2026-06-25 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 4bfb15f9-4f07-3c08-9721-1ca77e4eb8e4 | -12.74706 | -44.45136 | 2026-06-25 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3b9f9ebf-05cc-3e28-ac2f-0986061eebbf | -12.84077 | -44.35865 | 2026-06-25 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6e397a21-147e-39f2-afc1-4e0339ebabfd | -12.75121 | -44.46374 | 2026-06-25 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| b573e686-5dd0-3567-a63e-76fc0cc3180a | -12.83439 | -44.35732 | 2026-06-25 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 41846b05-63e8-3a30-bd4f-187b695d97d0 | -12.73725 | -44.46636 | 2026-06-25 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 43dbb8a1-7ef7-3fab-8ffc-4daf08c2de62 | -17.34139 | -42.6258 | 2026-06-25 03:30:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 434e3630-5267-32a7-a73c-1e7865f29898 | -17.34737 | -42.6236 | 2026-06-25 03:30:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 14.6 |
| dda6c9db-8a98-3f78-b912-982104a25398 | -12.75052 | -44.46937 | 2026-06-25 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 17c53808-bd10-3060-802e-6fd8983b8c8a | -12.73952 | -44.45542 | 2026-06-25 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.3 |
| f2f9b906-f21f-30ad-a186-02f7d1b2b4da | -12.74761 | -44.45157 | 2026-06-25 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 57f060cc-8525-338c-87b3-ef5be8f39c6a | -17.8213 | -40.13423 | 2026-06-25 03:30:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| ffff526b-1927-3dd6-a5ba-9688caa4c4f5 | -12.73838 | -44.46089 | 2026-06-25 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 7981f77c-6948-3bb4-8ffb-023036c26a28 | -12.75008 | -44.46924 | 2026-06-25 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 8b6bd6b6-d801-3de9-86b7-a55051c09fbf | -17.3407 | -42.62917 | 2026-06-25 03:30:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3e8a06ca-c990-32e1-888d-ddb460003492 | -17.34668 | -42.62696 | 2026-06-25 03:30:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 991754ad-21fa-3a79-8c84-21115e46cfc0 | -14.85147 | -42.79148 | 2026-06-25 03:30:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 00b127c5-17a5-383a-aa2c-4c4fc8966a25 | -12.73197 | -44.45947 | 2026-06-25 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 60be3185-8e0d-3d33-92cc-61e48d97e952 | -17.34208 | -42.62245 | 2026-06-25 03:30:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 96283071-2038-3d16-9e9f-9d1daa0b09e9 | -12.74366 | -44.4678 | 2026-06-25 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f3610a36-b372-317b-9ee8-54d7ec548e57 | -12.7448 | -44.4623 | 2026-06-25 03:30:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 0ff3cc4a-52ad-3180-b803-8af935c789af | -18.5213 | -47.2457 | 2026-06-25 03:32:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9821313a-9767-3590-b38d-682853184634 | -7.7498 | -44.6184 | 2026-06-25 03:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 62.5 |
| fd9e9f52-256d-3e1b-a707-50b5bfcbde75 | -12.7373 | -44.4521 | 2026-06-25 03:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 623595f3-f733-3cb4-bb9e-b4151aa84592 | -7.7498 | -44.6184 | 2026-06-25 03:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 61.6 |
| bd2622ac-ff34-3170-8d6d-6c6afc2dbffc | -12.7373 | -44.4521 | 2026-06-25 03:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.3 |
| 534530ed-3797-31b4-a2a8-1cb1ebb4d9c5 | -12.7373 | -44.4521 | 2026-06-25 04:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 43.7 |
| fb491836-f7ea-35fd-8198-c916b1bb14cf | -7.7498 | -44.6184 | 2026-06-25 04:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 62.5 |
| 682512c2-dc0f-3f3e-b9e7-12742ed98c49 | -11.8678 | -51.7473 | 2026-06-25 04:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 53d65d89-54c4-37fc-ad18-a01d79c1307b | -11.8868 | -51.7452 | 2026-06-25 04:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 421.4 |
| 98c8c099-c2dd-3711-b9e5-f58f9e993673 | -11.8865 | -51.7663 | 2026-06-25 04:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 202.5 |
| 8bb6d7e7-4e79-35a3-83cc-ee16981aad06 | -7.7498 | -44.6184 | 2026-06-25 04:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 66.5 |
| f9e5645c-a83e-3696-bbce-1b3c2cb50fba | -11.8675 | -51.7684 | 2026-06-25 04:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 3a50c452-cd8f-327f-9183-e9cb431d5482 | -12.7373 | -44.4521 | 2026-06-25 04:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.1 |
| b1ef52ec-7a7a-3f2e-82c6-91fb3cb6942b | -11.9059 | -51.7431 | 2026-06-25 04:10:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |
| b4bf120d-370a-3f5c-9724-776bc37dc9f5 | -3.04158 | -40.12337 | 2026-06-25 04:12:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 24c3f34b-8445-3f89-9e91-a0d67a5f90d2 | -9.74195 | -47.877 | 2026-06-25 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac32f033-f4fd-35f3-847a-6a68af8ea09e | -7.76457 | -44.61849 | 2026-06-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d2503cb3-9557-3039-a22c-06920d58856d | -8.68755 | -47.8581 | 2026-06-25 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b84f57d2-47f0-3e65-bef5-d2c4c1f8f888 | -5.75709 | -43.18997 | 2026-06-25 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 37786726-2119-3ed0-9dea-8a941f5279f6 | -9.16052 | -45.40187 | 2026-06-25 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff0bf214-9100-3deb-bbea-f66639d866f3 | -10.827 | -42.69706 | 2026-06-25 04:14:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fe2127e0-e7d4-373a-bbc0-210dd2e80e64 | -10.29265 | -44.69147 | 2026-06-25 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| f7f34327-6743-3325-9848-5c1607a9382b | -5.81308 | -45.06094 | 2026-06-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d79a323-714b-3a95-83ac-5bfd731c2fb1 | -5.81086 | -45.05283 | 2026-06-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 497388f3-0ef4-3ef9-976e-bfc7b6c07310 | -5.81185 | -45.06852 | 2026-06-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40e77bb2-c436-366f-ab19-198168012637 | -8.79931 | -44.81053 | 2026-06-25 04:14:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a61086a1-3901-3326-b167-33038d2e662e | -6.99109 | -42.89408 | 2026-06-25 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 9818b23a-3abe-3b58-ae7f-5e44c77dee87 | -9.46226 | -49.8333 | 2026-06-25 04:14:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48a4a2be-880b-3b6e-aff8-3a58818bb3cc | -9.67846 | -47.02476 | 2026-06-25 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eff35ef8-2382-3188-8417-50729a229c19 | -5.80863 | -45.04912 | 2026-06-25 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d60ca8df-dcf8-345f-a08e-59af8f5a166f | -6.76073 | -46.3121 | 2026-06-25 04:14:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ecd3af20-2c18-3f54-821d-cfdaecda0d68 | -7.76064 | -44.62153 | 2026-06-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 301111a7-5d6a-3899-9740-1323744c9d44 | -7.74037 | -44.17146 | 2026-06-25 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b3498f3f-bcdc-3076-8685-2505ac20fc19 | -10.03238 | -46.62072 | 2026-06-25 04:14:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68800713-dff8-38ee-8b79-c4bbd4f87bc8 | -6.59601 | -43.89592 | 2026-06-25 04:14:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 53e20927-28f7-37e9-8de9-741f4b0090c2 | -7.7293 | -44.17687 | 2026-06-25 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 52c70c7c-dab9-3285-9c62-1180ffc20cc8 | -9.20811 | -45.32261 | 2026-06-25 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c4fd75f-e3dd-3977-85b3-f6f70c24298d | -7.75451 | -44.61692 | 2026-06-25 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ce9328e5-089c-3866-9647-4d9fafa1215b | -6.31177 | -44.65088 | 2026-06-25 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d9fb872-e6e5-3c86-9f6d-ef6bbd01c762 | -7.64546 | -45.2937 | 2026-06-25 04:14:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1cc97f31-6dcf-37f8-ba94-1b365eb7b5cf | -6.98449 | -42.89306 | 2026-06-25 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| fdd279d6-578c-3a90-9d9c-9bbffb8d8bbf | -7.9588 | -47.44781 | 2026-06-25 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 45fafe0b-84bd-313e-8be1-34f25cbb21d7 | -5.82422 | -43.58706 | 2026-06-25 04:14:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6e44f943-0d5f-3072-a430-4c57ccbb293e | -8.6829 | -47.86228 | 2026-06-25 04:14:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| f4ed5726-7a20-3196-8bb1-8e6e9c8e9ea1 | -6.97514 | -42.88807 | 2026-06-25 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| e94041e9-e307-3829-a214-719bd2875faf | -7.79385 | -47.59378 | 2026-06-25 04:14:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa986321-32ab-3276-9898-4bfbd7bace5a | -4.66685 | -43.2189 | 2026-06-25 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e5b2e6a-9e83-3e3f-a35b-3c7bebfaac3b | -6.98503 | -42.88961 | 2026-06-25 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |


[Clique aqui para ver as próximas entradas](README7.md)
