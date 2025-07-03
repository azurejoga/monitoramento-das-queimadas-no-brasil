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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf161c2e-5a4f-312f-96b4-d77c8a47ef0b | -5.39783 | -43.24375 | 2025-07-03 04:55:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7a788679-c12c-3790-9268-b7ffd54cc8a9 | -2.91117 | -48.23886 | 2025-07-03 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| fa7aa91c-618d-3972-8f2c-305a2f7ea1c2 | -6.02024 | -49.22506 | 2025-07-03 04:55:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 34fbbed2-f43a-3cc7-89ab-d8584e877a92 | -5.91432 | -43.44619 | 2025-07-03 04:55:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c3e30161-49cc-3a33-a463-9d8c64ec5cfd | -6.96574 | -42.88968 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 43.5 |
| b9b02783-ac95-3747-b277-582e8c1fcd30 | -6.72231 | -43.17626 | 2025-07-03 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d68b9bd2-4d57-3fba-9b4e-97176de714c3 | -3.7196 | -53.75312 | 2025-07-03 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e51edce2-ab6b-33d0-9576-f421659b2f21 | -6.96702 | -42.87985 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| efdd5ea0-53c0-3ef9-a560-9221d84dd254 | -6.96288 | -42.87637 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.1 |
| 792c6851-81b5-3e8d-b7d9-40a21b41b55a | -7.44163 | -44.44173 | 2025-07-03 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b23e0cb3-87bb-315c-be92-a7b634dfd563 | -6.96913 | -42.87714 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 0189e95a-61c0-3ae5-b7df-476c36dcfb40 | -3.08176 | -52.43024 | 2025-07-03 04:55:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f26a161-162e-3331-8384-b2f815237ee7 | -2.53191 | -53.95708 | 2025-07-03 04:55:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 89926823-9c50-3e11-9221-80df3b4987ab | -6.60932 | -43.89553 | 2025-07-03 04:55:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 7c6aaaab-8009-38ba-ae0c-85f07d46d5e7 | -6.2955 | -43.68262 | 2025-07-03 04:55:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 3a1cea4a-10d7-3924-bb8f-4861dd059903 | -4.53412 | -48.02647 | 2025-07-03 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4f3bd3e0-c51d-3340-b726-4ef8dda5a0f6 | -7.44107 | -44.44596 | 2025-07-03 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4c577c13-214d-37ac-89d3-388bb0fed739 | -7.09101 | -44.39285 | 2025-07-03 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f37ecb10-0dca-3d74-a828-dc5ddff27961 | -6.17968 | -42.60929 | 2025-07-03 04:55:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d85a05fc-e223-3576-a24c-c75788b33d4d | -6.96142 | -42.87403 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| a8c61e22-5104-3072-be09-dd0cf0e4f851 | -6.19451 | -42.64161 | 2025-07-03 04:55:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1bbbaca3-39fa-3d4b-8fdc-cbea2bad3e04 | -6.93063 | -43.88583 | 2025-07-03 04:55:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 23515b72-ab85-3070-8fe6-198adf90ab04 | -6.96076 | -42.87907 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| ec421755-84e8-3540-a176-577e45864ef2 | -2.89326 | -48.03586 | 2025-07-03 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39efd23b-f4d8-38ae-b278-9dd67c30fe77 | -5.42596 | -49.0796 | 2025-07-03 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5eb33a2c-cc40-3c2a-bcd3-5f4051627023 | -6.96012 | -42.88401 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 43.5 |
| d2309aa7-5d34-36b4-a30b-d5e740a3259e | -6.96767 | -42.87485 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| ac153be0-5261-3489-98e5-c7afb578328b | -4.40188 | -47.63097 | 2025-07-03 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 789a4398-fc00-3932-8064-02a87441048b | -3.49858 | -51.18238 | 2025-07-03 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 438c0c41-b999-3ed1-90fe-1c2e701a6190 | -6.68668 | -43.15881 | 2025-07-03 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 44472f68-53cf-39a4-8b82-b2d4dbd01367 | -7.22444 | -43.06512 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| b5f1a941-5bd6-3774-a60d-a8512fb6f0d3 | -6.29607 | -43.67854 | 2025-07-03 04:55:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 5ac4e975-2339-345f-a18b-f7601aade4b1 | -3.50974 | -47.21946 | 2025-07-03 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4030ef44-5ca4-3b2f-8c95-01073e3c547e | -6.9622 | -42.88134 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.1 |
| 99ec5a20-d399-35e0-8170-8b515600a3b4 | -7.22997 | -43.07092 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 130362a0-31c6-3bf7-b78a-4d27b278a502 | -3.70905 | -53.71275 | 2025-07-03 04:55:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cb97b59c-f107-33c7-98c8-635671d8e75a | -4.53411 | -48.02176 | 2025-07-03 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| efc816e0-7c5c-3d6d-8083-414a715405bf | -7.67698 | -44.66167 | 2025-07-03 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1fbac550-52de-3869-b5a8-0ed719107d35 | -6.17784 | -48.05599 | 2025-07-03 04:55:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8abeae34-1973-3126-b8e9-af2bacf607a8 | -6.96085 | -42.8912 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 45.8 |
| 2e7f2f4d-ce11-302f-8e05-be9cd234947f | -5.90779 | -43.44955 | 2025-07-03 04:55:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9308d4f-324c-38f2-bf08-2e4ca3fc1596 | -6.68732 | -43.15411 | 2025-07-03 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 8.1 |
| a545d280-eceb-37ca-b6a1-fe6e0ed14f77 | -7.21956 | -43.05446 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| c6f75c4f-3625-3472-8a3e-15440620fe0f | -7.26003 | -44.33616 | 2025-07-03 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc6bc287-b13f-3596-8aac-64272ebd2b86 | -6.68603 | -43.16353 | 2025-07-03 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 1e902cf8-3d02-3032-a1b0-c1cfae61912f | -4.53893 | -48.01855 | 2025-07-03 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dad1e718-058e-3b13-91b9-acaabe72d5e9 | -5.87175 | -50.14656 | 2025-07-03 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 02605b8a-48e3-34ff-b4f0-2f4e1b1298e2 | -6.96845 | -42.88206 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| a1b12e8a-2050-3a87-8412-1b44b6265bbd | -4.41928 | -47.66409 | 2025-07-03 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 61692126-d22f-36db-a02b-634fd73ec8b3 | -4.53835 | -48.02254 | 2025-07-03 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d5ec4c83-1389-38f3-b743-7c94894c3392 | -6.33308 | -43.75568 | 2025-07-03 04:55:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f80170b0-a307-3715-8364-1556d2101425 | -3.29223 | -49.19258 | 2025-07-03 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 70e0dd30-2ea0-3678-aec0-91cb5ef28ee9 | -6.20699 | -51.4522 | 2025-07-03 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3441d26b-581e-3684-b359-9604a83bc2b7 | -4.27975 | -48.19078 | 2025-07-03 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a9085d55-2132-38f4-ba95-115b8ad4420f | -5.72605 | -49.10567 | 2025-07-03 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8691e38-1445-3e69-ae29-b3262afa7174 | -4.53535 | -48.01846 | 2025-07-03 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6f0b14b4-053f-335a-a724-54bdd5493e18 | -6.17903 | -42.61412 | 2025-07-03 04:55:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4aee1833-59d5-3934-8f8a-1a914043e437 | -6.96638 | -42.88474 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 43.5 |
| 6951e212-134e-3701-aab3-53ca6059c5a9 | -6.17347 | -48.05544 | 2025-07-03 04:55:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6ad9a7f0-a5f0-32ba-9827-4e742881ceff | -7.23062 | -43.06606 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 3e3e076d-8057-394e-a4c9-78d6669ad60c | -4.53473 | -48.02245 | 2025-07-03 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4527cc7a-02e5-3980-b23e-ea0e4b56abdf | -6.2896 | -43.68196 | 2025-07-03 04:55:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| f2d500f0-3e8b-3cf9-9fe4-e6b09437c3ed | -6.94972 | -42.87959 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| be6f273f-e397-34b4-878d-d2c8237f6fcd | -6.6928 | -43.15958 | 2025-07-03 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 7fcf678c-cad6-3328-91ce-d7ef88b2f9a7 | -6.72077 | -43.18233 | 2025-07-03 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 14a6b7e5-86f8-3653-8d00-e0086b8d88ec | -6.33233 | -43.75409 | 2025-07-03 04:55:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b4673535-d37e-3bb2-b4d8-a675c9355368 | -6.94905 | -42.88458 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 26285689-2fe3-3b29-8234-0b067f7821e5 | -6.19386 | -42.64635 | 2025-07-03 04:55:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 509feeb9-175b-374f-8251-a49f47f91562 | -6.1741 | -48.05105 | 2025-07-03 04:55:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c028344b-5d47-35f0-b76d-4e1aaeb230d7 | -7.21826 | -43.06416 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 284bb1c5-cfcc-394a-8bef-965a559e857e | -2.89385 | -48.0321 | 2025-07-03 04:55:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ed448b6-fbe1-38e6-9b86-76956c48b1e8 | -4.28454 | -48.18753 | 2025-07-03 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fd9101cb-ddd9-37bd-b8fa-a43463739a25 | -6.9504 | -42.8746 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 2d3688c1-3935-3e3a-be80-afc8af2ea228 | -6.28433 | -43.67679 | 2025-07-03 04:55:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 820eb841-06f4-3b0d-9530-b04c4f81ad50 | -7.1946 | -43.10015 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 97a7de6c-deee-3032-a500-d9b70eaf3e74 | -2.91936 | -48.24011 | 2025-07-03 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e02f81e3-f2d3-37b5-90ab-102c9ff46b34 | -6.95595 | -42.88057 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.1 |
| 24180745-c7ef-3f27-8063-799bae4239e2 | -6.28902 | -43.68615 | 2025-07-03 04:55:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 27d8fadb-6b3d-36ac-8fc1-851aa1b1bbef | -2.91031 | -54.48673 | 2025-07-03 04:55:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3230f417-04b1-38c7-af2a-94c1ae2600a3 | -5.72202 | -49.10505 | 2025-07-03 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7b52ce06-b566-3285-bb7e-4c04f0a82339 | -6.69311 | -44.06047 | 2025-07-03 04:55:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ef88737-c3ae-3a2a-9f5a-c7b0766ae018 | -7.09155 | -44.38903 | 2025-07-03 04:55:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 28b70ca3-6c46-3362-b086-2773a3b84643 | -7.40553 | -45.4189 | 2025-07-03 04:55:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e05670e-1d8d-3285-aa92-0df2d3f0c722 | -4.53897 | -48.02319 | 2025-07-03 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0f3169eb-13fe-3bef-b644-6c500bb6717b | -6.20759 | -51.44817 | 2025-07-03 04:55:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12a81e5f-09b5-3f4d-8012-dd852c38b62d | -6.95527 | -42.88555 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 45.8 |
| b1dfdf13-81e9-30b7-b376-73bd3b3224c2 | -3.88478 | -54.21325 | 2025-07-03 04:55:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 09a77a07-fe7a-3c55-9cb3-0367f47be994 | -4.28395 | -48.19139 | 2025-07-03 04:55:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 23b8578c-7d7c-32eb-a964-75a1fc297a55 | -5.87552 | -50.14718 | 2025-07-03 04:55:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 4402dad6-6ad3-3517-ad97-c15dc412943a | -6.60989 | -43.89146 | 2025-07-03 04:55:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b6b6d7ee-752d-3998-a6c8-26494ddae8b5 | -6.69256 | -44.06438 | 2025-07-03 04:55:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34b8c136-d8b3-3566-b880-ba606cd4ffca | -6.95663 | -42.87556 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 34.1 |
| a5bb3b4f-2e71-3074-804e-f622990f5083 | -6.72142 | -43.17768 | 2025-07-03 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3b404719-3694-3561-b938-5f7994759ca8 | -7.21891 | -43.05933 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| ffc6738e-7e22-3168-910d-5b3b85d8cf11 | -7.22509 | -43.06025 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| ce6452fa-aad3-3a17-b147-572cedcaf6d4 | -6.02373 | -49.22921 | 2025-07-03 04:55:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1a4c1fe-6727-36d2-8c75-90e074c78931 | -6.33364 | -43.75171 | 2025-07-03 04:55:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c65b49cb-ce6c-3d96-969a-0891fca80ae9 | -4.03125 | -48.06353 | 2025-07-03 04:55:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 89a00465-08ab-33fa-b174-5d29e1592d5e | -6.9546 | -42.89047 | 2025-07-03 04:55:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 45.8 |
| 412de6a1-5c0f-3b22-a9b3-450388f035a8 | -6.72532 | -43.14961 | 2025-07-03 04:55:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README20.md)
