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
| f63b9a1b-acbb-3a54-a053-1e7f3fe6bea5 | -11.7917 | -43.6163 | 2026-04-12 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 44.1 |
| b0ebfac0-195d-34e4-a2c8-3188401886df | 2.0138 | -61.1015 | 2026-04-12 01:00:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 60.2 |
| a39502af-775d-300f-abca-b8056aed5cdc | 1.2853 | -60.3126 | 2026-04-12 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 9ee7f4f5-bfb2-3ff1-a637-c1a8e8554a79 | 1.2853 | -60.3126 | 2026-04-12 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.2 |
| d72d0864-ea65-337e-a0bd-818ac67ebc1f | 1.2671 | -60.3127 | 2026-04-12 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 972c0488-f071-3850-be18-8e5f41c9b746 | 2.032 | -61.1013 | 2026-04-12 01:10:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 291233f0-d3c1-34ba-9840-4cffed006353 | 1.2853 | -60.3316 | 2026-04-12 01:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 58.8 |
| ca4fac1b-717c-3f1a-a937-148e2d881c9e | -9.7934 | -37.4809 | 2026-04-12 01:10:00 | GOES-19 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 100.6 |
| 9d57cab3-de8c-329c-be0b-ed89dfa867cf | -20.09616 | -57.22293 | 2026-04-12 01:15:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Cerrado | 7.9 |
| da325d4b-5e7d-3f73-bbf6-0cae9167a571 | 2.032 | -61.1013 | 2026-04-12 01:20:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 60.1 |
| eb17feba-875c-3c2b-86c5-6d06748054a1 | 1.2853 | -60.3126 | 2026-04-12 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 0faccf8e-6c8c-395f-b155-6cf90dcfbf4e | 2.0138 | -61.1015 | 2026-04-12 01:20:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 3c0f5c56-c920-3764-bd6a-e9921422aa60 | 1.2853 | -60.3316 | 2026-04-12 01:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 760dd485-b952-3f6d-93c5-ff2e75765e6e | 1.37327 | -60.65776 | 2026-04-12 01:20:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 13813f5d-e920-34f9-ac7e-00210c1e5e5e | 1.29001 | -60.31705 | 2026-04-12 01:20:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 20.4 |
| c89f346f-3f00-382a-939f-972d92864b05 | 1.34617 | -60.67245 | 2026-04-12 01:20:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 2b566a4c-e098-3331-93f3-555d585cd29b | 1.35599 | -60.6921 | 2026-04-12 01:20:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 25.4 |
| b84f30bb-b0ae-3661-aa57-7fe649daffa2 | 1.27736 | -60.31529 | 2026-04-12 01:20:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 940d4ffc-b255-3425-b883-3dba50fdcc16 | 1.27679 | -60.30949 | 2026-04-12 01:20:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 26823a5a-3b75-3a64-b036-670580cb79f4 | 1.27478 | -60.33448 | 2026-04-12 01:20:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 2024032e-c906-3a4b-8cbb-7c09778b9402 | 1.28742 | -60.3362 | 2026-04-12 01:20:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 98cc0007-531f-399c-a9c4-3b50303796d5 | 1.37076 | -60.67582 | 2026-04-12 01:20:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 0390b1be-8094-3490-9409-83a67b49d8e8 | 1.27406 | -60.32864 | 2026-04-12 01:20:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 42.8 |
| fc5fe014-8fce-3059-9309-cfe2fe01e683 | 2.03355 | -61.10247 | 2026-04-12 01:22:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 82ca3036-ceb4-3138-96c1-41a39b2460b3 | 2.02155 | -61.10078 | 2026-04-12 01:22:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 84.3 |
| b6707f52-14f9-3c28-90b6-2f8425c4fa86 | 2.67731 | -61.18081 | 2026-04-12 01:22:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 13.2 |
| caddf216-0dbf-3b42-8b2f-4aa5ea3ae35a | 2.66523 | -61.17929 | 2026-04-12 01:22:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 7da9096d-4a26-3e3d-a4fa-49f2d5de556d | 2.02389 | -61.08355 | 2026-04-12 01:22:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 23.3 |
| ef26488a-0b58-3cf7-9598-34af4c42375b | 2.37021 | -60.96004 | 2026-04-12 01:22:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 17.3 |
| a45efd82-ccd7-344e-b1e0-8507dc2bc9a1 | -9.7934 | -37.4809 | 2026-04-12 01:30:00 | GOES-19 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 89.9 |
| a481b763-02c7-349d-935c-3b6c846773d8 | 1.2853 | -60.3316 | 2026-04-12 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 08556c7c-7f6e-3725-8924-edc0d1817fcb | 1.2853 | -60.3126 | 2026-04-12 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 5081ed21-9802-3095-a55c-12d95a844870 | 1.2853 | -60.3126 | 2026-04-12 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 75afba47-9046-332b-bd52-2376e5eb6e85 | 1.2853 | -60.3316 | 2026-04-12 01:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.9 |
| a3e1f47c-b09a-3827-972d-c75430bf16b8 | -9.7934 | -37.4809 | 2026-04-12 01:40:00 | GOES-19 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 77.4 |
| 014a6c6c-7af6-3369-a986-fa9bc9639aea | 1.2853 | -60.3126 | 2026-04-12 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 5b7fa915-0f92-3201-9891-4d217c6dae83 | 1.2671 | -60.3127 | 2026-04-12 01:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.3 |
| be6a5cd6-4be9-33f7-8687-9eb341c54ed3 | -9.7934 | -37.4809 | 2026-04-12 01:50:00 | GOES-19 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 83.0 |
| 72ca1350-2b5b-3c00-a276-824297d9c62a | 1.2853 | -60.3126 | 2026-04-12 02:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 66.5 |
| c22e8cdf-b4f7-3ac3-bcc5-d937c76c734e | 1.2853 | -60.3126 | 2026-04-12 02:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 63.7 |
| d72dc391-b370-35e9-a48f-d3bc1ba259f1 | 2.0138 | -61.1015 | 2026-04-12 02:10:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 6d8d1d74-2a1c-325e-8d38-047eb1e26a0a | -9.7934 | -37.4809 | 2026-04-12 02:20:00 | GOES-19 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 90.6 |
| f53d009a-7550-3f6e-a030-2d79f15de0d3 | 2.032 | -61.1013 | 2026-04-12 02:20:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 9ee7deeb-2550-3deb-89b0-58318c231b71 | 1.2853 | -60.3126 | 2026-04-12 02:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.7 |
| fd7f79bc-83bb-31e0-abe2-4c052c6dbc74 | 1.2853 | -60.3126 | 2026-04-12 02:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 8b32566c-b44d-3d53-8a6a-4d7fac689882 | 1.2853 | -60.3126 | 2026-04-12 02:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 22c9b5da-5978-3912-8ecd-888de605b266 | 1.2853 | -60.3126 | 2026-04-12 03:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 2c02b613-059b-382d-9955-7e2c3a411a64 | 2.032 | -61.1013 | 2026-04-12 03:00:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 52.2 |
| b64d6397-31bf-369f-af5b-36752566fc44 | 1.2853 | -60.3126 | 2026-04-12 03:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.2 |
| d588949e-a9fc-3fa8-a327-b501c725a5df | -9.7911 | -37.47858 | 2026-04-12 03:15:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ac2924b0-c75f-3a7b-96d9-cf530a58ff15 | -9.79175 | -37.47511 | 2026-04-12 03:15:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.4 |
| ec235cde-003e-3699-88f7-f54050c66ba8 | -8.57144 | -37.0027 | 2026-04-12 03:15:00 | NOAA-20 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6123f6a4-235c-3263-baa6-0f235b28da57 | -9.79713 | -37.47603 | 2026-04-12 03:15:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 12.5 |
| c502a2e5-073c-3a29-873b-90b3de694546 | -9.79777 | -37.47258 | 2026-04-12 03:15:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 159721db-f833-3039-b9ee-1d56817e172e | -9.80249 | -37.47705 | 2026-04-12 03:15:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 12.5 |
| a150037e-5e52-318c-84af-f137109b2138 | -11.76066 | -37.98866 | 2026-04-12 03:15:00 | NOAA-20 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2e37b83e-3c82-315f-8c00-12d5b2084c99 | -9.79648 | -37.47948 | 2026-04-12 03:15:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 85736fd5-a3c6-3bd6-a40f-ec40e481aadf | -8.57084 | -37.00598 | 2026-04-12 03:15:00 | NOAA-20 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 00a21273-b481-3476-91e4-25e07e476065 | -9.79839 | -37.46922 | 2026-04-12 03:15:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 35a3dc79-dcde-3e1a-880a-2c005bbf768f | -9.80312 | -37.47363 | 2026-04-12 03:15:00 | NOAA-20 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 12.0 |
| 8e404205-aa09-32f0-8961-6887dd3ca363 | -15.28507 | -43.06818 | 2026-04-12 03:17:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 521b84cc-009f-3723-8a45-df82257d711e | 1.2671 | -60.3127 | 2026-04-12 03:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.5 |
| b0733fea-75a6-3be0-804e-2747ed1d65d8 | 1.2853 | -60.3126 | 2026-04-12 03:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 76a1815c-702f-37e6-96b6-c5c1a7a282bd | 1.2853 | -60.3126 | 2026-04-12 03:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.0 |
| e7507a3b-9064-364e-bcda-df3cbb89fa4b | 1.2671 | -60.3127 | 2026-04-12 03:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 50.3 |
| f71f50ae-9d91-3623-838e-b906cf983a21 | 1.2671 | -60.3127 | 2026-04-12 03:40:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 5e930224-2b7e-3c43-8bdd-1402f8b81b21 | 1.2853 | -60.3126 | 2026-04-12 03:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 2f760c2b-deb2-3a11-a206-df8a66002f7c | 1.2853 | -60.3316 | 2026-04-12 03:50:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 8aad2671-fddc-3104-ab66-08dfad0f4070 | -8.57479 | -37.00419 | 2026-04-12 04:02:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 44bed9eb-6df5-3ab8-a0ab-314a0865e174 | -9.79431 | -37.47584 | 2026-04-12 04:02:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3126bec6-2493-3855-8212-e1a801d803c9 | -9.79916 | -37.46803 | 2026-04-12 04:02:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 3.1 |
| b62eded5-8a64-3676-b6f8-2b786677350a | -9.80276 | -37.46858 | 2026-04-12 04:02:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 3.1 |
| bffd8102-b326-3d26-b8bd-5b30ef280e87 | -8.57024 | -37.00523 | 2026-04-12 04:02:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 914c56b0-29ab-3023-ac8f-83a6595cea7f | -9.79922 | -37.47921 | 2026-04-12 04:02:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c40ab19f-4ab1-332c-b21f-a2edf9f05343 | -9.80212 | -37.47278 | 2026-04-12 04:02:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0e0c6f6a-dc6c-35e7-becf-c286a5236169 | -8.57116 | -37.00363 | 2026-04-12 04:02:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 467b8aaa-4606-3504-abe0-dde10efd7077 | -9.79853 | -37.47224 | 2026-04-12 04:02:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b957b677-ba16-39ff-b31e-f511052c7b7d | -10.58816 | -37.4494 | 2026-04-12 04:02:00 | NOAA-21 | RIBEIRÓPOLIS | SERGIPE | Brasil | 2806008 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bb59642b-b5af-3b7c-87e4-1dae38163180 | -9.80464 | -37.46717 | 2026-04-12 04:02:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 05f54dbf-be1d-3558-b169-ce53be9a3978 | -9.72618 | -37.25532 | 2026-04-12 04:02:00 | NOAA-21 | PALESTINA | ALAGOAS | Brasil | 2706208 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 073bc825-b4d8-380c-a6e7-f6c97d86a30f | -9.79562 | -37.47865 | 2026-04-12 04:02:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 09370579-8eea-3262-b532-7773a7ac5969 | -9.80104 | -37.46662 | 2026-04-12 04:02:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3ad435b1-3100-3c05-b6ed-7fc714f5c034 | -9.79744 | -37.46607 | 2026-04-12 04:02:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c30ac20d-8cf6-34a1-a743-49bd7aeb9e14 | -9.80043 | -37.47085 | 2026-04-12 04:02:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 4.0 |
| dbf66d9e-d4c6-39e4-9fa8-a419a7f478b4 | -9.80403 | -37.47139 | 2026-04-12 04:02:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 26d61a3b-6423-3c97-b37f-8809db2ca759 | -8.57088 | -37.00097 | 2026-04-12 04:02:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f0f86280-7125-3540-91ef-7ae0e2dc0028 | -9.80763 | -37.47191 | 2026-04-12 04:02:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3dcee5d5-1d19-3c3b-aceb-2243bb79f36b | -9.79493 | -37.47168 | 2026-04-12 04:02:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a45425ad-cc99-37f1-8ca9-8b19b1f52fe5 | -9.79622 | -37.47448 | 2026-04-12 04:02:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 62089876-f48b-3355-9bcf-eef693116280 | -9.7979 | -37.4764 | 2026-04-12 04:02:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 37a86975-5fe9-3667-940d-97b3a541e6fc | -9.79683 | -37.4703 | 2026-04-12 04:02:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 4.0 |
| d9b7579b-0953-3194-9e89-c37a27815430 | -11.79458 | -43.62867 | 2026-04-12 04:04:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56a4a167-bd39-3d54-a557-83459d1721d7 | -15.37803 | -52.75623 | 2026-04-12 04:04:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a6f6d2a7-9db1-369f-9c30-c486712583b3 | -12.60557 | -43.31936 | 2026-04-12 04:04:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a335bf09-a975-392b-a827-51827a5f17bf | -12.85367 | -39.84317 | 2026-04-12 04:04:00 | NOAA-21 | MILAGRES | BAHIA | Brasil | 2921302 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cfff8a80-925e-30b4-9df9-6ee4258a3db9 | -13.21191 | -43.68979 | 2026-04-12 04:04:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ad52205-6a48-37c2-b1b1-c0c5064dfd1f | -15.37898 | -52.75166 | 2026-04-12 04:04:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b7f17531-4edb-31ae-ae6f-f0c38a299370 | -12.85312 | -39.84684 | 2026-04-12 04:04:00 | NOAA-21 | MILAGRES | BAHIA | Brasil | 2921302 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c74080db-3612-3ff2-8280-ec73e11272cb | -11.79874 | -43.62531 | 2026-04-12 04:04:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e43492b8-5678-39a2-9843-728b577c2d02 | -11.79524 | -43.62472 | 2026-04-12 04:04:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README3.md)
