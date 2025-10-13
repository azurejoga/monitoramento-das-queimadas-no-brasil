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
| d5949ca5-45c5-3039-a6f9-fd836ebfa351 | -3.0726 | -49.404 | 2025-10-13 02:40:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| bb947dd3-4359-3b00-a2ca-e1d8b6919ae5 | -15.185 | -43.5767 | 2025-10-13 02:40:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 74.2 |
| 123f2b1d-409e-3f21-b8e9-f52eea664649 | -9.8228 | -62.1979 | 2025-10-13 02:40:00 | GOES-19 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 62.0 |
| d028aff5-24b0-3a56-9adf-36a5fa057e27 | -4.47 | -44.9392 | 2025-10-13 02:40:00 | GOES-19 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 62.7 |
| c349b4f9-e23c-30eb-a82b-086cb76aecff | -16.1203 | -53.9836 | 2025-10-13 02:40:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| f0e1b80b-d416-3bb6-8198-32dc83c15156 | -2.5423 | -47.811 | 2025-10-13 02:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 43bdcef2-cd2a-3241-a943-30dc26014c38 | -4.4886 | -44.9382 | 2025-10-13 02:50:00 | GOES-19 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 2199cea5-645d-3886-99be-0d28c838c21c | -17.3384 | -53.7922 | 2025-10-13 02:50:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 79.9 |
| dd8c61bb-70ee-3b13-aef6-a38055bf9756 | -7.5449 | -46.089 | 2025-10-13 02:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 1e409afc-10b2-3f9a-b05e-681c4cc20f1d | -16.1203 | -53.9836 | 2025-10-13 02:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| cc71600e-9688-3083-977b-091efda85a61 | -4.47 | -44.9392 | 2025-10-13 02:50:00 | GOES-19 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 10422371-8014-387e-98ba-5376e88a5d9e | -16.1577 | -50.0023 | 2025-10-13 02:50:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 75.3 |
| f81ef5a1-3387-3760-91bd-727535d99051 | -16.1581 | -49.9802 | 2025-10-13 02:50:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 145.7 |
| 17fdfa8b-cb1c-3a68-81b8-e8af1d0a929f | -17.338 | -53.8135 | 2025-10-13 02:50:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 108.4 |
| f7eff732-4c28-3e53-ace2-f5d43db5d740 | -7.7547 | -44.2036 | 2025-10-13 02:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 108.1 |
| 724697a5-8132-3dff-866f-dc9a25492770 | -15.185 | -43.5767 | 2025-10-13 02:50:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 69.2 |
| 0a15d7ba-504c-380f-9454-6a14bc6bc692 | -16.1385 | -49.9834 | 2025-10-13 02:50:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 89.7 |
| d6ebbe6f-012d-3bd9-8ca3-ed97138bc286 | -2.5238 | -47.8115 | 2025-10-13 02:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 8f36a6a4-e413-3b11-b6f5-dac17b6b8fbe | -3.0726 | -49.404 | 2025-10-13 02:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| cde75720-986c-31d9-8f94-84ebc4ee1368 | -16.1207 | -53.9625 | 2025-10-13 02:50:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 765acbb4-8466-34a2-bf8c-6edd6f03ef3c | -2.5423 | -47.811 | 2025-10-13 02:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 51cb332d-77d1-3055-897e-66d902e6a9f5 | -17.338 | -53.8135 | 2025-10-13 03:00:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 96.5 |
| b124a6db-52f1-3941-a431-001fb439d050 | -16.1581 | -49.9802 | 2025-10-13 03:00:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 189.8 |
| 12a124dc-38b0-3fe3-ab75-69b3b2cfd90a | -2.5423 | -47.811 | 2025-10-13 03:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 111f6831-34a7-367f-b15f-30fff82dbc3f | -16.1207 | -53.9625 | 2025-10-13 03:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 44af4977-942d-3376-affd-eaf55cc434e6 | -8.4655 | -46.1359 | 2025-10-13 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 28fbf809-e6c8-3e19-8aa6-fbddb1d04fe7 | -17.3384 | -53.7922 | 2025-10-13 03:00:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 7f5a0df2-ad19-3f1f-82e0-30d0c07d1dcc | -4.4886 | -44.9382 | 2025-10-13 03:00:00 | GOES-19 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 125.7 |
| d7e31824-83c7-36d6-8015-3600d5132714 | -16.1586 | -49.9581 | 2025-10-13 03:00:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 3861fc8c-8de0-3e26-a12c-35867d5f543e | -7.5449 | -46.089 | 2025-10-13 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| c3836cf8-b715-39e1-b6bd-6f77051177fc | -4.47 | -44.9392 | 2025-10-13 03:00:00 | GOES-19 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 111.1 |
| 6d826ff2-38cb-380d-8a53-6f00654d93d0 | -2.5239 | -47.7899 | 2025-10-13 03:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 848a224c-c139-3812-b583-28e9bd2c2137 | -2.5424 | -47.7893 | 2025-10-13 03:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 2646e2d4-47fb-311b-bfe9-ee52ce59068e | -3.0726 | -49.404 | 2025-10-13 03:00:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 303ad1c2-c01e-3965-bcce-8bfce3653694 | -8.4658 | -46.1134 | 2025-10-13 03:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 9b2eff67-c7d7-3454-929c-70f85e7badaa | -16.1385 | -49.9834 | 2025-10-13 03:00:00 | GOES-19 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 275ce873-b23b-341e-9b4a-2d7cc6dcae45 | -2.5238 | -47.8115 | 2025-10-13 03:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 29edff9d-6e8a-3b34-a0b9-618e2cd2dccc | -7.7547 | -44.2036 | 2025-10-13 03:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 82.2 |
| d818bc84-fbfb-301a-a9a3-016092a74df4 | -4.88502 | -37.50477 | 2025-10-13 03:02:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 2175291a-6af6-3233-a78d-24a5d230cb76 | -4.88598 | -37.49923 | 2025-10-13 03:02:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 4.9 |
| db015abf-d4f4-3165-8caa-5e88e37694c7 | -4.88368 | -37.50555 | 2025-10-13 03:02:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 7346f7e7-75af-3424-9347-622ddb43358e | -4.88468 | -37.5 | 2025-10-13 03:02:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 0f932f3e-4656-3e10-91ad-1b32ff364cbe | -15.5341 | -41.83052 | 2025-10-13 03:06:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 427d8958-eef5-392c-95cd-d99e0a275cfa | -17.34857 | -42.4746 | 2025-10-13 03:06:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4f483094-4eed-342b-ae89-92013548fb8b | -17.34489 | -42.47673 | 2025-10-13 03:06:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2326d4f5-0bca-3780-a79d-56d21144c5ab | -17.34158 | -42.47281 | 2025-10-13 03:06:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9fbe7a26-19d9-3523-8557-7ca395f0e8cf | -19.26652 | -41.272 | 2025-10-13 03:06:00 | NOAA-20 | RESPLENDOR | MINAS GERAIS | Brasil | 3154309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| fc5d399b-148f-399d-bd02-acfe6b22cc96 | -15.54605 | -41.81023 | 2025-10-13 03:06:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f83cef7d-96ba-305b-ad2c-cf8b2a9df5cc | -15.53579 | -41.82309 | 2025-10-13 03:06:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2421ccc2-4da7-3617-a582-98e53ce0de0a | -15.54443 | -41.81739 | 2025-10-13 03:06:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| b0ec0516-5eaa-3390-ac02-e2c272d9beaa | -15.52883 | -41.82133 | 2025-10-13 03:06:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| dd57a9b8-544b-3471-9cb4-00fed7d7c9c1 | -19.26518 | -41.27767 | 2025-10-13 03:06:00 | NOAA-20 | RESPLENDOR | MINAS GERAIS | Brasil | 3154309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 28c42bec-8385-3324-a176-569ade25b4dc | -17.3466 | -42.4696 | 2025-10-13 03:06:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5e3e30ac-8ddc-382c-9528-7add219929d2 | -21.08723 | -42.93808 | 2025-10-13 03:08:00 | NOAA-20 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0b828679-6840-3832-a6e6-7267868118df | -20.84378 | -42.8128 | 2025-10-13 03:08:00 | NOAA-20 | COIMBRA | MINAS GERAIS | Brasil | 3116704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e8c182ad-c3b4-34d5-99a7-4ca6386c52e3 | -20.83708 | -42.81116 | 2025-10-13 03:08:00 | NOAA-20 | COIMBRA | MINAS GERAIS | Brasil | 3116704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 25bb7e11-1440-387b-9070-cdc10785335a | -16.1203 | -53.9836 | 2025-10-13 03:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 89fa19c9-262a-3392-95d6-aab3a2944eaf | -2.5238 | -47.8115 | 2025-10-13 03:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 4a088321-f837-3dc2-84b5-73f84e810dde | -4.4886 | -44.9382 | 2025-10-13 03:10:00 | GOES-19 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 8e4f6947-6caa-3436-a4f0-4e09da90e6c9 | -9.8228 | -62.1979 | 2025-10-13 03:10:00 | GOES-19 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 391c446c-3e48-3aec-8254-c362f641be90 | -17.3384 | -53.7922 | 2025-10-13 03:10:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 21c20da4-9284-379c-85a8-2610ca50aaf4 | -4.47 | -44.9392 | 2025-10-13 03:10:00 | GOES-19 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 143.6 |
| d385e87a-f281-32fe-a692-2f87b42e6366 | -3.0726 | -49.404 | 2025-10-13 03:10:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 57df32ed-37e2-3ad6-a078-e5b8856a29d9 | -2.5423 | -47.811 | 2025-10-13 03:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 066880ee-19ea-333c-bfb2-a2f513aa2e66 | -4.4701 | -44.9165 | 2025-10-13 03:10:00 | GOES-19 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 55e458c3-6251-3963-b9ce-2886536bb6ec | -17.338 | -53.8135 | 2025-10-13 03:10:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 100.6 |
| a3222420-d556-349e-9458-0c6a5b9c9827 | -4.4888 | -44.9155 | 2025-10-13 03:10:00 | GOES-19 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 35.5 |
| b6dcafdd-1afa-34fa-b88f-3ecb40265d4b | -7.5449 | -46.089 | 2025-10-13 03:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 7e653217-da9f-385c-9b44-00a2f3cffd28 | -2.5239 | -47.7899 | 2025-10-13 03:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 00f829cb-c831-3d57-b28f-75dab5e88f94 | -16.1207 | -53.9625 | 2025-10-13 03:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 095bd505-10c0-3ff5-8a4b-d7be1b81c404 | -7.5049 | -44.6421 | 2025-10-13 03:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.5 |
| daf544b1-71b9-3fce-ba3d-4423f3078021 | -8.4469 | -46.1153 | 2025-10-13 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| a7507a9e-5c1e-394f-b11d-67c75261f3fd | -2.5238 | -47.8115 | 2025-10-13 03:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 59790d87-9a65-3818-99e0-779480ba9d8e | -8.4655 | -46.1359 | 2025-10-13 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 406e4f91-816e-3bb3-8c64-a6bec9dd2a07 | -9.8228 | -62.1979 | 2025-10-13 03:20:00 | GOES-19 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 0948a457-8ff6-35c9-8c72-ada28489359b | -7.5052 | -44.6192 | 2025-10-13 03:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 6b8a6b78-435e-3712-8946-fc9643f266e2 | -4.47 | -44.9392 | 2025-10-13 03:20:00 | GOES-19 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 58.9 |
| e9257516-7aec-3fc7-9e9b-3d9226ebaf7f | -17.338 | -53.8135 | 2025-10-13 03:20:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 104.4 |
| bb6e9ccd-9b60-3e0d-9aaa-d682b5d40ef0 | -7.4863 | -44.621 | 2025-10-13 03:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 7120ae76-740c-370b-8bfd-9f34348fc175 | -17.3384 | -53.7922 | 2025-10-13 03:20:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 5bc1e122-1d6f-3771-8695-73610e6c5348 | -2.5423 | -47.811 | 2025-10-13 03:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 90100fdf-4a33-37b1-badf-59cdfcc64c39 | -15.0375 | -46.6271 | 2025-10-13 03:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 75.1 |
| f22d5144-07e1-391f-9ce4-fe1b56cdd34b | -8.4658 | -46.1134 | 2025-10-13 03:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 201.1 |
| d7afd326-1fec-3285-bf33-cdbdf53540af | -4.4886 | -44.9382 | 2025-10-13 03:20:00 | GOES-19 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 40.2 |
| c829a915-b2ae-3511-9175-497aedc10799 | -16.1203 | -53.9836 | 2025-10-13 03:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 5689fe5e-8b70-303c-8f3a-a6f22f0c96ab | -7.5052 | -44.6192 | 2025-10-13 03:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 154.3 |
| c5b63d8a-1af6-357e-ba08-6604502297fe | -8.4469 | -46.1153 | 2025-10-13 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| b5761829-5a39-3f7a-9c11-917f36a7fae1 | -8.4467 | -46.1378 | 2025-10-13 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 7852779a-f4a2-3e9c-aa85-9ed1367ee735 | -9.8228 | -62.1979 | 2025-10-13 03:30:00 | GOES-19 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 7700b7f7-31d9-3db8-b703-b6c1f4fe63ee | -3.0726 | -49.404 | 2025-10-13 03:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 34ac999a-1df8-33ee-bd1b-baa1db1d2d3a | -8.4658 | -46.1134 | 2025-10-13 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 148.3 |
| d6932b09-82b1-3e15-8b85-77eede3b2837 | -7.5049 | -44.6421 | 2025-10-13 03:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 106.0 |
| f4e44b5d-b09c-38cb-af6e-091893402d67 | -15.0375 | -46.6271 | 2025-10-13 03:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 1ccbe8c0-4ece-39b9-81d9-3ea8661031f4 | -16.1207 | -53.9625 | 2025-10-13 03:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 3eee97b1-b54b-3b9c-b191-89ab8f48cfe5 | -7.5054 | -44.5962 | 2025-10-13 03:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 4f995fc1-2f9c-3738-88a0-74a2b29f8277 | -7.4861 | -44.6439 | 2025-10-13 03:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 116158ff-9ea6-3d80-aab3-114380da7ad9 | -7.4863 | -44.621 | 2025-10-13 03:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 2284635d-85f5-316c-863b-90c2940aa9f5 | -7.5449 | -46.089 | 2025-10-13 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 1b0d080e-ad22-33c1-865c-f0a04ab10a3c | -17.338 | -53.8135 | 2025-10-13 03:30:00 | GOES-19 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 88.7 |
| b3b6f5b6-abfe-30d8-9d60-d7c7a9acbdeb | -16.1203 | -53.9836 | 2025-10-13 03:30:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 70.7 |


[Clique aqui para ver as próximas entradas](README7.md)
