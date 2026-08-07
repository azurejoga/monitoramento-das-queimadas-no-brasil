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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce7301d1-76d2-3bcd-bbc3-bea04f4108d5 | -16.68575 | -51.36549 | 2026-08-07 05:06:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d9a5e25-7d78-31e0-8af1-e76615a52a70 | -14.27717 | -49.71449 | 2026-08-07 05:06:00 | NOAA-20 | CAMPOS VERDES | GOIÁS | Brasil | 5204953 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf779b60-a41c-31d4-b223-b803cf85b390 | -15.0768 | -53.59155 | 2026-08-07 05:06:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 398875d7-bd64-39a1-8d14-8c5b56cc69a5 | -15.10864 | -53.59641 | 2026-08-07 05:06:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 36f4957a-a2e7-3363-be52-aefbe6b265ba | -13.83087 | -53.71463 | 2026-08-07 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c759911-46f0-34dc-bf7e-1ff1db3be6ce | -17.53879 | -45.35551 | 2026-08-07 05:06:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 85d1abc0-c8c5-3d48-92c4-28196295a4cc | -15.07738 | -53.58744 | 2026-08-07 05:06:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5a694143-c9fe-3572-887c-4f34939a3ff9 | -14.37569 | -53.3493 | 2026-08-07 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e13c0390-1abc-36e9-9701-8198145748df | -13.82622 | -53.72196 | 2026-08-07 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b0ef8aff-3fb4-3963-9e77-768c29e9faa1 | -17.53268 | -45.3547 | 2026-08-07 05:06:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ecd516dc-0487-3cb5-af6c-1cdb83944209 | -14.44266 | -53.33839 | 2026-08-07 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ca79810a-a4e9-3df3-bcfa-f9857e83ebdc | -18.1461 | -47.98845 | 2026-08-07 05:06:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04b847b5-dcb8-34d7-9588-d796920c920e | -15.08995 | -52.76587 | 2026-08-07 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bd9f2ec0-17cb-3ebd-8854-61f8876029c3 | -14.30695 | -54.73537 | 2026-08-07 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 07a3148b-228c-32cd-abf4-01e2e1d09de0 | -14.35123 | -54.90789 | 2026-08-07 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0e3f963d-a160-3ad9-8c20-f7f3826b8076 | -16.68983 | -51.36617 | 2026-08-07 05:06:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7a0ffd6-7a26-3373-8e23-1eaeccbf8680 | -14.32535 | -54.97538 | 2026-08-07 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4fc1e5b2-53b5-3161-81ac-a71b91c18d4d | -15.12399 | -53.5904 | 2026-08-07 05:06:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f015d09-8e81-3680-b3eb-6c6ce6907382 | -14.35011 | -54.91525 | 2026-08-07 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 22ed142d-fee3-362e-a7ee-eac24679a3b7 | -15.08092 | -53.58798 | 2026-08-07 05:06:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| d8133ebe-5d06-306f-bc50-ce6bbe5b9c47 | -14.15855 | -53.99821 | 2026-08-07 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59981e67-ba4d-3cc0-b3e1-a49cfe51c506 | -18.14681 | -47.98216 | 2026-08-07 05:06:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e4c7921-02c8-3423-9c30-088aa9a9663a | -19.9972 | -43.97113 | 2026-08-07 05:06:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 519c1228-a822-37ab-a093-1a59da0ab0d6 | -14.44205 | -53.34256 | 2026-08-07 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd3d248e-096c-30d3-ac20-1870a60dfc8a | -15.06688 | -53.56158 | 2026-08-07 05:06:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8f558969-dd02-3c7f-8797-11f0b61d090f | -15.87055 | -43.6032 | 2026-08-07 05:06:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0aa9298e-2bee-31cf-92da-d6736d02a981 | -17.48193 | -53.32364 | 2026-08-07 05:06:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4bf1939d-cfef-3023-98b4-50a2175455f9 | -15.07855 | -53.55401 | 2026-08-07 05:06:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 65cb720b-67e6-3243-8f95-8504d215b06d | -13.83028 | -53.71856 | 2026-08-07 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76005054-9acf-3d13-abee-c425580657f7 | -14.31032 | -54.7359 | 2026-08-07 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec112c7b-11eb-3673-8bad-0d268be614c8 | -14.30413 | -54.73115 | 2026-08-07 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7564058d-a929-3871-a050-1a4cc0959798 | -14.31088 | -54.7322 | 2026-08-07 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9465b48c-3ce0-3fe1-9809-3bc09027f582 | -14.34956 | -54.91891 | 2026-08-07 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 87276901-175e-3554-bb35-a79ae0624a84 | -14.34117 | -54.92883 | 2026-08-07 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 207ff55e-8f3b-3f35-843c-72aeeb11dbfb | -14.162 | -53.99873 | 2026-08-07 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec16534c-9392-34a9-92e8-9844c84bf52a | -13.42425 | -57.02386 | 2026-08-07 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b34ceb46-a9ec-3f6d-b430-6811fff183be | -13.69424 | -51.97353 | 2026-08-07 05:06:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 07230e61-37bc-3c56-a194-617090c0b89b | -14.33227 | -54.96487 | 2026-08-07 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 80246958-b3b3-362d-bcd7-956339c7250c | -13.69033 | -51.97561 | 2026-08-07 05:06:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8164c8d2-bcc9-3461-b80f-629efea9cbf6 | -17.99605 | -45.87925 | 2026-08-07 05:06:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59142b10-1087-3a10-9fa1-6debc508d5ff | -17.85586 | -49.61021 | 2026-08-07 05:06:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 51d723eb-ec03-360a-af2d-33ea71d4ace1 | -14.35067 | -54.91157 | 2026-08-07 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3e57b27b-2f66-3bd8-ba91-feb500f7ef91 | -19.71041 | -48.13089 | 2026-08-07 05:06:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 44bad956-daf1-31bf-8254-bba1e43ccd7a | -16.53011 | -49.42135 | 2026-08-07 05:06:00 | NOAA-20 | GOIANIRA | GOIÁS | Brasil | 5208806 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 60da78d0-9044-303b-b76b-6f6173038ca6 | -13.68965 | -51.98035 | 2026-08-07 05:06:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a36293c8-538a-36a2-8422-6adb0003129b | -17.46201 | -47.15662 | 2026-08-07 05:06:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c22495a1-7f21-36ef-b20e-b525ef0d6417 | -13.42033 | -57.02689 | 2026-08-07 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26eb19e4-fa59-37a7-83e7-99a0c2f389b4 | -15.08034 | -53.59209 | 2026-08-07 05:06:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| bc1de240-4f35-37a0-bdfa-7479a0542060 | -15.07679 | -53.59248 | 2026-08-07 05:06:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6e73b181-50f8-36ca-81cc-e91ee144cadd | -15.58404 | -54.29047 | 2026-08-07 05:06:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b7074ba-2e12-39b8-a29b-389aa16a7d0c | -20.00247 | -43.97155 | 2026-08-07 05:06:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 34194a13-6aff-3707-85d5-44b3a4ed65e5 | -16.4913 | -52.71947 | 2026-08-07 05:06:00 | NOAA-20 | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0e5fdce9-6c9e-304b-9c52-586e3ec0d562 | -15.09278 | -52.76426 | 2026-08-07 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5168eaf-721c-320c-aec8-1c91675ddd3a | -15.08786 | -52.77256 | 2026-08-07 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| daf7a072-9548-3d81-baa9-090d14bcb48d | -14.30357 | -54.73484 | 2026-08-07 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| fb9a7ecd-06ec-3237-adf2-5a11bf7f636a | -13.89791 | -53.9198 | 2026-08-07 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c223212-78b3-3cbe-adf9-6b998bae99b7 | -13.4286 | -57.03938 | 2026-08-07 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7a4362e-97a1-3183-9961-0b9549b2e6ef | -15.87114 | -43.59708 | 2026-08-07 05:06:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 239a5bc6-4428-3cb8-8105-3c078b04a359 | -20.00197 | -43.9775 | 2026-08-07 05:06:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| deee315c-10a1-37b6-ab9a-80812195c522 | -15.1057 | -53.59176 | 2026-08-07 05:06:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3db324a-6c17-3d84-8382-f84bdd8e7481 | -15.14687 | -52.7545 | 2026-08-07 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c15d06a-cc8c-38a1-b558-549f8bc3e918 | -13.43035 | -57.02859 | 2026-08-07 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 67482ffc-37ff-3995-8620-27d67f81de83 | -13.82274 | -53.72142 | 2026-08-07 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 05ba26bf-0784-3805-910a-29794c5a12a2 | -14.43849 | -53.34202 | 2026-08-07 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5596f669-f6a7-3986-bfc8-b0dc3af98a0b | -14.32591 | -54.97173 | 2026-08-07 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e29d391-16c4-3448-9064-58fd13725c4f | -14.4178 | -53.05616 | 2026-08-07 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ab42f32e-1e78-3522-ae73-9cfe9a709898 | -16.49066 | -52.72421 | 2026-08-07 05:06:00 | NOAA-20 | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3f32922d-9d58-3e22-8571-02d97bf6484e | -16.88959 | -51.07592 | 2026-08-07 05:06:00 | NOAA-20 | IVOLÂNDIA | GOIÁS | Brasil | 5211602 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5d4f0764-cfee-3bca-92e3-26a6a5ae01e6 | -14.34006 | -54.93615 | 2026-08-07 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a77a2c2d-10a0-3eda-83ae-c43c547bffe4 | -13.8268 | -53.71803 | 2026-08-07 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 280a47b3-0792-316c-94ce-575f6fd2ce08 | -15.08848 | -52.76813 | 2026-08-07 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a580865-b2d1-3a59-b6c3-cc7b7fb77821 | -13.42467 | -57.04242 | 2026-08-07 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36d71572-aa95-37da-86d8-8d002995d899 | -17.45652 | -47.15618 | 2026-08-07 05:06:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7630fa80-69d1-3869-a720-f95d92073989 | -13.68979 | -51.97775 | 2026-08-07 05:06:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 946e1d23-6645-3f7d-be78-68ac00f18bfd | -15.08498 | -52.77414 | 2026-08-07 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d52cc56-b792-3e17-af56-2013ea6cbd94 | -13.82333 | -53.71748 | 2026-08-07 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3f736ec7-8ebf-31b8-b0d0-5a3e17408886 | -16.75479 | -47.58523 | 2026-08-07 05:06:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ac31c7b5-934b-3d20-af93-d4df1da16cae | -15.07872 | -53.55499 | 2026-08-07 05:06:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 3510650a-6a9a-3024-a6c6-7b03617f06b5 | -18.14646 | -47.98529 | 2026-08-07 05:06:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81e78e15-378f-38e0-8d56-19e4a39382f5 | -19.7153 | -48.13505 | 2026-08-07 05:06:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3ac2c079-d236-3eba-a3a0-d1b79e2e3bc7 | -19.99528 | -43.97536 | 2026-08-07 05:06:00 | NOAA-20 | BELO HORIZONTE | MINAS GERAIS | Brasil | 3106200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5ae1af6b-5391-3649-ab5d-922bd6fc3d20 | -22.52481 | -43.55871 | 2026-08-07 05:08:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d40cdddf-409d-36ef-a3c8-9888ad57d571 | -22.52791 | -43.56583 | 2026-08-07 05:08:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d6be6f6b-9ae3-3703-8537-7e0a3557aaf0 | -20.3885 | -49.30859 | 2026-08-07 05:08:00 | NOAA-20 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6ef2cc48-0503-3dee-a4e3-0b737302041a | -20.54989 | -50.52117 | 2026-08-07 05:08:00 | NOAA-20 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c3a51e8d-4784-3691-a280-892e72631c42 | -20.6119 | -46.29591 | 2026-08-07 05:08:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d0126c52-e861-3bf1-8ed0-3bb85c461ef9 | -20.60592 | -46.29524 | 2026-08-07 05:08:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ad2877c-6748-33cb-b398-b2a924c645c8 | -22.52842 | -43.55849 | 2026-08-07 05:08:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 7abb2143-10bd-32eb-99d9-b6ae8a0d5ecc | -22.53229 | -43.55414 | 2026-08-07 05:08:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e04ae695-2996-3450-9dec-12bbfe2abccf | -22.5358 | -43.55556 | 2026-08-07 05:08:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 6e0f75eb-a468-30ee-9167-0e7d38a15db7 | -22.53189 | -43.56027 | 2026-08-07 05:08:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 4ebfe037-e793-3f67-ad73-e5d2a8b6a085 | -22.53539 | -43.56142 | 2026-08-07 05:08:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 9009438e-aa9f-3df7-9997-b2ce55bdeef0 | -22.53148 | -43.5669 | 2026-08-07 05:08:00 | NOAA-20 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 3c4ab2c3-d77e-3b01-b5a4-2eb991d93c0f | 2.51802 | -60.64285 | 2026-08-07 05:46:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 55aafdc9-e1aa-389f-b45a-258dc4bbb0b5 | 2.70332 | -60.09058 | 2026-08-07 05:46:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd59835c-7feb-3c9f-84f1-80766f249589 | 1.93831 | -60.85037 | 2026-08-07 05:46:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9894126e-ceed-33b3-989b-a3c36d71e097 | 2.51879 | -60.64762 | 2026-08-07 05:46:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9daaf060-7e04-3742-b3d0-abc36bf0348e | 1.02612 | -60.38957 | 2026-08-07 05:46:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 43502575-344e-3511-8104-78c493699aec | 1.9414 | -60.84505 | 2026-08-07 05:46:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3af294f6-65b4-386c-b3be-ecd14bfa26ff | 1.93757 | -60.84564 | 2026-08-07 05:46:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README25.md)
