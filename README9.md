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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31428163-da47-3317-b604-9a7ecf965339 | -23.33846 | -46.77243 | 2025-06-04 04:04:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2e058e05-38ce-3de8-a9e0-4da1a1a425e5 | -19.16068 | -47.82005 | 2025-06-04 04:04:00 | NOAA-20 | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93541987-6ec9-37c8-8955-642a2f4b2a44 | -23.40571 | -46.55613 | 2025-06-04 04:04:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f910c441-7e27-3686-9218-1d7425ef1507 | -20.34973 | -40.35992 | 2025-06-04 04:04:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7790f0e0-f272-3ca1-a363-7770810cec40 | -19.93315 | -47.26721 | 2025-06-04 04:04:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 201aa5d3-8803-30f6-bf1f-b79be36df1c9 | -23.59358 | -47.43818 | 2025-06-04 04:04:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c3840cf4-feeb-3619-8c3f-61d60d547431 | -22.90057 | -43.75075 | 2025-06-04 04:04:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8a11c9a7-d3dc-3339-8872-8bf0442a194a | -20.54674 | -54.12296 | 2025-06-04 04:04:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2330bf7d-2a18-30ce-b9de-65654a5317a8 | -23.97337 | -46.25166 | 2025-06-04 04:04:00 | NOAA-20 | GUARUJÁ | SÃO PAULO | Brasil | 3518701 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 190881aa-4700-3525-a3a8-7626329488e6 | -19.93226 | -47.27209 | 2025-06-04 04:04:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd98c581-6c6f-3c0c-ad2c-b9dadf0576ed | -20.41579 | -43.55105 | 2025-06-04 04:04:00 | NOAA-20 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7514551c-3990-384c-b569-42c58b228995 | -20.54202 | -54.11746 | 2025-06-04 04:04:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ba8db29-70ba-3ced-b147-ee0231daaf83 | -19.84823 | -43.84497 | 2025-06-04 04:04:00 | NOAA-20 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 32fef0ff-0d23-309a-9b96-7327eb3331fe | -23.37086 | -46.03417 | 2025-06-04 04:04:00 | NOAA-20 | JACAREÍ | SÃO PAULO | Brasil | 3524402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e70efcdf-382b-39c5-868d-36604bdf4427 | -25.09035 | -50.24277 | 2025-06-04 04:04:00 | NOAA-20 | PONTA GROSSA | PARANÁ | Brasil | 4119905 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2ce93de4-6116-3b58-8320-226ee1e74e61 | -22.74372 | -47.13803 | 2025-06-04 04:04:00 | NOAA-20 | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca4ee734-306b-32e7-8b53-f5840c2758a2 | -22.54108 | -48.81041 | 2025-06-04 04:04:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e839f3e6-3412-360d-aea3-2d702becdea2 | -23.98491 | -48.91865 | 2025-06-04 04:04:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f0a6939-f3c4-3ce7-b8c2-a5c95e6b1528 | -25.18982 | -49.32823 | 2025-06-04 04:04:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0b7ab125-ebef-3efb-8cb8-35f9a92f0999 | -22.85723 | -42.98035 | 2025-06-04 04:04:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f45c3d16-addc-3634-9c55-7edf9d2f1393 | -21.65045 | -44.38659 | 2025-06-04 04:04:00 | NOAA-20 | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| eed0d90b-d32f-3dde-825e-b745f614830b | -22.92038 | -45.41317 | 2025-06-04 04:04:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0697aee0-ae21-31d5-9da1-3259ef0eeb14 | -25.1909 | -49.32509 | 2025-06-04 04:04:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d6d63b13-3d6f-3e8e-a408-757e1eb1daa7 | -19.43682 | -44.3404 | 2025-06-04 04:04:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71df6568-5f41-3c70-abfd-33b42d1c547c | -21.91224 | -42.2609 | 2025-06-04 04:04:00 | NOAA-20 | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6aefac9d-e47e-30cf-b2b6-b2b4924e93f6 | -6.9602 | -42.9052 | 2025-06-04 04:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 114.8 |
| d33aac33-1e91-38da-a680-efa37406fe1d | -6.9602 | -42.9052 | 2025-06-04 04:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.8 |
| 851620ab-1d53-3d58-ad2e-a03cdd588f4c | -6.9791 | -42.9034 | 2025-06-04 04:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.2 |
| 27ddfeb1-fd5b-3c62-8675-4d3ee930a6c3 | -7.0169 | -44.5954 | 2025-06-04 04:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 3b5e6743-60c4-3f5d-97fa-ef9fe58e194f | -6.9791 | -42.9034 | 2025-06-04 04:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.1 |
| f7d39668-4516-3db5-b78b-9880f78be368 | -6.9602 | -42.9052 | 2025-06-04 04:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 91.7 |
| 657defcc-a9ea-3f8c-84b1-b3b8e0bfc998 | -7.0169 | -44.5954 | 2025-06-04 04:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 46e8c141-eb35-3053-b32e-39e85e898411 | -6.9791 | -42.9034 | 2025-06-04 04:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 71.4 |
| c683ad8c-5f6b-3159-9f2f-3303a49a6baa | -6.9602 | -42.9052 | 2025-06-04 04:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.5 |
| 7371b901-7b97-384a-8150-c06177b9f5d1 | -4.81546 | -45.25992 | 2025-06-04 04:49:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c72d377e-b82d-3ea8-a716-5752258b695f | -2.58782 | -51.92038 | 2025-06-04 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ca9dd88-8700-34c7-8974-cb51f11aea60 | -3.13287 | -41.7898 | 2025-06-04 04:49:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f20fd3fb-9a0f-3921-af7c-a23052145ceb | -3.70828 | -53.70967 | 2025-06-04 04:49:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dee78337-70b7-33e6-bcec-7dc4eaafb15a | -3.13858 | -41.79066 | 2025-06-04 04:49:00 | NOAA-21 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 0e49a76f-5812-398d-afd0-71874c9a7d2b | -4.642 | -47.96844 | 2025-06-04 04:49:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f87dc7f-0b58-3afa-b358-2b37b1787481 | -4.00647 | -43.24289 | 2025-06-04 04:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d456975-dee8-307e-b00d-5dce61ba4c7f | -2.58729 | -51.9238 | 2025-06-04 04:49:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0dc1396-bdf9-3749-8618-23e4fb012bd9 | -4.81015 | -45.26393 | 2025-06-04 04:49:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 7188fa4b-0427-3eef-84c6-e57af8950fd8 | -4.80555 | -45.26309 | 2025-06-04 04:49:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d57bb2f3-fb86-33af-8508-d3857e675454 | -4.006 | -43.24614 | 2025-06-04 04:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 59ff645b-c7aa-375d-a957-e1ac3cdb1bd6 | -2.53387 | -53.95864 | 2025-06-04 04:49:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9937eb48-746f-301d-a319-de9edc08e94c | -4.81085 | -45.25916 | 2025-06-04 04:49:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e994a67f-f661-3318-8ec1-db6b6e3a173c | -4.81892 | -44.35703 | 2025-06-04 04:49:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa34b007-4825-3bf2-b879-8562205d2cef | -4.82383 | -44.35781 | 2025-06-04 04:49:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac535516-c551-3179-8336-15cd1cf8380e | -4.81476 | -45.26472 | 2025-06-04 04:49:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1edc690d-50da-3ba0-b6b9-87a8a33d0ea7 | -4.00076 | -43.24532 | 2025-06-04 04:49:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5016d99-6f98-3d63-ac50-c9cbb1dcff67 | -6.9791 | -42.9034 | 2025-06-04 04:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.4 |
| ae7cdc1f-c6b6-33bf-a4fe-f12280cf8c0e | -7.0169 | -44.5954 | 2025-06-04 04:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 7c5ae3e4-a20f-33b2-bfcc-2b0367a341ed | -6.9602 | -42.9052 | 2025-06-04 04:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.4 |
| 263cbb94-b827-3704-83fb-92f0fe6808d0 | -6.37514 | -43.6824 | 2025-06-04 04:51:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e393259f-8202-37f8-ad2b-7a066bc97696 | -11.9071 | -47.45116 | 2025-06-04 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 614a96b8-02f2-3985-89c8-9eb71ddb3a8d | -7.58317 | -45.86501 | 2025-06-04 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8a09abe2-d084-3172-a73c-c917324ec9f2 | -10.49721 | -53.65685 | 2025-06-04 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c4970d52-648e-3274-8f7d-908b1f7a83eb | -6.3694 | -43.68493 | 2025-06-04 04:51:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f70894a-5f87-3f90-b04f-3f0aac57256d | -11.57851 | -47.46063 | 2025-06-04 04:51:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba746d1c-2c68-3613-83c8-467603ac0873 | -8.95613 | -47.27865 | 2025-06-04 04:51:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 410a6b76-5be5-31b6-8917-6496c8187e43 | -7.29435 | -43.45636 | 2025-06-04 04:51:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 07b025e2-b22b-309d-9f7d-a63e32bd400c | -10.3562 | -48.73289 | 2025-06-04 04:51:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f57ae135-0026-39cb-8948-f3e0f7c9febf | -8.27735 | -55.10835 | 2025-06-04 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b8be003-c791-36e2-983a-e6409d2719cf | -7.90112 | -50.36262 | 2025-06-04 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 172501c1-54d0-36b3-9daf-e02c929f332e | -6.68559 | -43.68624 | 2025-06-04 04:51:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 45d08e7a-606f-3942-94bf-aa48917b6f84 | -6.21048 | -43.33231 | 2025-06-04 04:51:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 26e771fa-a67b-3acc-abb0-ea6001d1be27 | -7.01743 | -44.59861 | 2025-06-04 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e954257d-d72f-3ba3-8e02-f678ad5f567c | -11.83532 | -51.28886 | 2025-06-04 04:51:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 08da1c93-0d28-3b63-ae2d-22dece27749c | -6.96817 | -42.91006 | 2025-06-04 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 36.4 |
| 762e51d2-5449-3325-9bf1-e384830f6610 | -6.86652 | -47.84967 | 2025-06-04 04:51:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 536a2c10-9569-3840-afe6-3eefc893a496 | -6.96204 | -42.91314 | 2025-06-04 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 7a997a2a-0534-3171-a0c7-46f95d7f197d | -8.61007 | -51.57861 | 2025-06-04 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 873ac3ce-c2ea-398a-aa8f-78286acb94bd | -7.90005 | -50.36378 | 2025-06-04 04:51:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2bbf17be-4dfe-340c-bdf5-164db87bc06c | -8.75361 | -49.77383 | 2025-06-04 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8728c1ae-f858-3634-a480-84ff5ac07730 | -6.37405 | -43.68658 | 2025-06-04 04:51:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ffe7400-d121-3d27-aa15-b2b64bbe54ee | -10.3005 | -57.14374 | 2025-06-04 04:51:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7d722da-7473-3190-a0f6-f88194c53388 | -7.01448 | -44.58274 | 2025-06-04 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9283a42b-22cc-3697-92a5-0bfe0fc2e25d | -6.68606 | -43.68292 | 2025-06-04 04:51:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8b8090b-006c-3aa9-84f5-76582136c1c2 | -7.01048 | -44.61224 | 2025-06-04 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| b4df39e1-c4c9-3784-aa6c-7eb8cf440a65 | -11.40694 | -52.94403 | 2025-06-04 04:51:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a069e46-f930-3401-b3a6-c9b74531bddf | -10.68786 | -57.64954 | 2025-06-04 04:51:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7910e6f5-0b7b-31f0-ad36-9879a82e44f3 | -8.07597 | -43.11776 | 2025-06-04 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 26a11dac-8fce-3a0f-86df-14d32dcb69ae | -8.75486 | -49.76518 | 2025-06-04 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| e3162723-0584-388e-b0d1-4f66a1cd95a1 | -6.29285 | -47.01067 | 2025-06-04 04:51:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c45ebffc-22be-37db-9ee2-825621ba6a14 | -9.39619 | -48.43457 | 2025-06-04 04:51:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80d75767-8b9c-3cdc-a8f9-934e74917f0b | -10.8342 | -56.96286 | 2025-06-04 04:51:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 531cf4f0-3a1d-3681-83e2-e7d5a0b19205 | -8.91103 | -50.0475 | 2025-06-04 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bfe0087f-7bf1-3f3d-ae8c-6db7d6aba6c7 | -10.05546 | -44.6438 | 2025-06-04 04:51:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 27000c81-26d3-31ba-83b9-8de5d23124cb | -7.58844 | -45.86096 | 2025-06-04 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 094e76ed-8d17-3a93-aaa8-03d30b18b495 | -11.562 | -47.62003 | 2025-06-04 04:51:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 99d1e49c-7e3b-3739-8329-ecb92572f9e7 | -7.99235 | -50.69575 | 2025-06-04 04:51:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d2e4acc-eae3-3e14-93e3-8ec38db1d399 | -8.07036 | -43.11698 | 2025-06-04 04:51:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| ac9acc2f-bb31-3b72-b22f-b0a90aa1731b | -11.53448 | -47.3185 | 2025-06-04 04:51:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35a062d1-499d-373e-b729-daf9b911b55c | -7.88505 | -46.19129 | 2025-06-04 04:51:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b79a7037-da90-3d2d-8a52-5e695b50e8aa | -7.01901 | -44.58698 | 2025-06-04 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0309c27e-49be-3c82-80c4-026bfc61a1d8 | -7.01164 | -44.60368 | 2025-06-04 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cef8cd8f-b26b-356d-af54-0c9fcc6b2d08 | -10.13905 | -52.13862 | 2025-06-04 04:51:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a99576e0-0e9b-3b78-a1c6-28a28a3f2fc2 | -7.01204 | -44.60076 | 2025-06-04 04:51:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ed2c3cce-8abc-3c22-8e74-ffda35ae565e | -10.5016 | -53.65041 | 2025-06-04 04:51:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |


[Clique aqui para ver as próximas entradas](README10.md)
