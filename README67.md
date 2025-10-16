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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7bf054e0-350b-345b-96cb-cc1713628afc | -17.93472 | -46.72698 | 2025-10-16 04:42:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c3b41ce6-13c3-3b6f-8761-9846ef687d7a | -17.61225 | -46.68621 | 2025-10-16 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 44835a64-e9f8-3890-8c7a-1e7c907c1f12 | -18.73244 | -47.46288 | 2025-10-16 04:42:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5335fc96-0193-3c4c-95b9-0f9ed1c27c48 | -15.85801 | -53.97538 | 2025-10-16 04:42:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1516bd4e-9b94-39d9-9f9e-80ba04afb847 | -15.86081 | -53.97994 | 2025-10-16 04:42:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 76bbe888-1544-3e10-8eed-81bd6019d972 | -17.62802 | -49.33904 | 2025-10-16 04:42:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1437a906-65fb-38dc-a742-8f4f5066eda8 | -17.07254 | -43.78949 | 2025-10-16 04:42:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dae9529f-0ec7-3fdd-8b4f-62f3fad78446 | -17.60317 | -46.69245 | 2025-10-16 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00dd1840-566e-3052-98b6-7d4cd5cfe011 | -18.5845 | -47.46478 | 2025-10-16 04:42:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0505e841-513f-3456-b665-b4e30e4b031f | -15.03843 | -52.9939 | 2025-10-16 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fc90deda-ff75-3d81-8ac5-141fa3db42e0 | -18.73177 | -47.46809 | 2025-10-16 04:42:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7741c06-b939-30d5-b82b-090ff4f4a6c3 | -16.46383 | -54.61194 | 2025-10-16 04:42:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 86b1c515-7e2b-3770-9910-417038e1b000 | -17.65605 | -48.33584 | 2025-10-16 04:42:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c9d38d98-08eb-3b0a-91b4-0dbe9076cfca | -20.48067 | -45.99189 | 2025-10-16 04:42:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b981c506-0057-341c-a9f7-6080106d1ed7 | -17.21981 | -46.9291 | 2025-10-16 04:42:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2dec7414-e7ba-34a6-8a4a-fdf62142c93c | -18.39496 | -47.01648 | 2025-10-16 04:42:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6747bd09-ec1a-3027-ac02-60f3ebccbde0 | -17.21123 | -47.65569 | 2025-10-16 04:42:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d23d034-a6f3-30c6-aef0-43ef76886441 | -20.94897 | -47.40002 | 2025-10-16 04:42:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 65b96250-9a46-3ae9-a5fa-d52aec7f64a2 | -14.78841 | -59.24803 | 2025-10-16 04:42:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d519351-e0d9-347a-a725-ff3cfe4cf440 | -17.21568 | -47.65142 | 2025-10-16 04:42:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4e08010-5e72-3f46-ba4e-2327c3c9a8e5 | -19.02855 | -47.5217 | 2025-10-16 04:42:00 | NOAA-21 | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cca083b7-b6b8-3ac8-9af5-79b35faedf66 | -17.59912 | -46.69183 | 2025-10-16 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aa615833-a35c-3597-b787-0466b31410b9 | -17.93404 | -46.73333 | 2025-10-16 04:42:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 80bc3595-4d63-3db9-8d7a-76d948ad56d5 | -18.93652 | -47.21902 | 2025-10-16 04:42:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fb5ee522-663a-3040-baa6-4ab3d75f0678 | -18.21543 | -46.05719 | 2025-10-16 04:42:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0a6fe35-423f-3b4e-aad0-95a3df713c30 | -15.0418 | -52.99451 | 2025-10-16 04:42:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3a5376e-2e4f-347e-bb40-d953af24774a | -17.93902 | -46.72658 | 2025-10-16 04:42:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4973b8b3-11af-38dc-b23d-541c18e11cd3 | -17.59961 | -46.68816 | 2025-10-16 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4b8688ca-4ec1-39f5-a67d-402ee05c0e84 | -29.18056 | -50.13449 | 2025-10-16 04:44:00 | NOAA-21 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 922e121d-3fe7-3745-b5b3-208e71d83055 | -29.17736 | -50.12847 | 2025-10-16 04:44:00 | NOAA-21 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 63169c13-1d04-34cf-9533-fef1c41f62bc | -21.98797 | -56.04231 | 2025-10-16 04:44:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 462723d6-e3f8-3504-b4fa-b432f3701fdf | -29.17928 | -50.11225 | 2025-10-16 04:44:00 | NOAA-21 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b1cf8f5f-3423-391f-af8b-d753cc072344 | -23.00434 | -47.09274 | 2025-10-16 04:44:00 | NOAA-21 | CAMPINAS | SÃO PAULO | Brasil | 3509502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| fe9cc9a0-4e2c-3993-9ee2-744293741cb8 | -22.09784 | -46.54083 | 2025-10-16 04:44:00 | NOAA-21 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 55cc26c4-07c5-37cc-80f0-6930e62b5134 | -22.14143 | -46.94091 | 2025-10-16 04:44:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7751f413-f8c7-3ed4-b1de-1f0ff47f0f7d | -23.0108 | -52.47596 | 2025-10-16 04:44:00 | NOAA-21 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1477393f-d9bb-3f3b-bdb3-bf00046eb39f | -22.78649 | -49.86103 | 2025-10-16 04:44:00 | NOAA-21 | RIBEIRÃO DO SUL | SÃO PAULO | Brasil | 3543204 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 331e5f0c-9eab-35c7-8c41-419fd866ab69 | -29.17414 | -50.12247 | 2025-10-16 04:44:00 | NOAA-21 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 5f41bdff-2e0a-3923-916a-4b6327b57816 | -29.18312 | -50.11289 | 2025-10-16 04:44:00 | NOAA-21 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 160e70ca-7beb-3efe-9129-04b183d14a09 | -29.18248 | -50.11831 | 2025-10-16 04:44:00 | NOAA-21 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4b71fddc-fcf2-3a89-9e50-d1b3bd8de621 | -29.17799 | -50.12308 | 2025-10-16 04:44:00 | NOAA-21 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| afcb67fb-db9d-3f64-83ae-80c563788092 | -29.18632 | -50.11894 | 2025-10-16 04:44:00 | NOAA-21 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c1095a5b-6907-3cb6-b64d-3698db3f7ec8 | -29.18889 | -50.13031 | 2025-10-16 04:44:00 | NOAA-21 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| aba71f72-90b4-3643-88fa-ef7f040bc7b5 | -29.1876 | -50.14113 | 2025-10-16 04:44:00 | NOAA-21 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 53eae8ba-b500-3f7a-b40e-47af4b7bef79 | -29.18953 | -50.12492 | 2025-10-16 04:44:00 | NOAA-21 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 3894bc0a-2ace-36a0-b4ba-3901ef8c70c2 | -29.17864 | -50.11767 | 2025-10-16 04:44:00 | NOAA-21 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a77f95b2-ee3e-302f-b966-b83f8553b732 | -23.69505 | -51.38743 | 2025-10-16 04:44:00 | NOAA-21 | CALIFÓRNIA | PARANÁ | Brasil | 4103503 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1a5f5b7d-58ae-3c74-a83c-d0b04b2a89cc | -29.1895 | -50.15812 | 2025-10-16 04:44:00 | NOAA-21 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f96556e4-d001-31a9-b83f-0f319384e93d | -24.46828 | -50.64574 | 2025-10-16 04:44:00 | NOAA-21 | TIBAGI | PARANÁ | Brasil | 4127502 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 3f3f8ef5-8d69-3355-9b99-ec7555744d08 | -28.29681 | -50.62434 | 2025-10-16 04:44:00 | NOAA-21 | LAGES | SANTA CATARINA | Brasil | 4209300 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1b61292a-751b-3e51-b9fe-5478d66de234 | -29.1844 | -50.13512 | 2025-10-16 04:44:00 | NOAA-21 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 5c8e470f-f3f5-3fd2-b589-8293c742fcf5 | -23.12078 | -55.21695 | 2025-10-16 04:44:00 | NOAA-21 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 9c7dde71-133d-316e-9bab-8718737f3231 | -29.17351 | -50.12788 | 2025-10-16 04:44:00 | NOAA-21 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 5d3d64e9-9229-3684-b1aa-3c98a4c2dbb6 | -29.18376 | -50.14053 | 2025-10-16 04:44:00 | NOAA-21 | CAMBARÁ DO SUL | RIO GRANDE DO SUL | Brasil | 4303608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ab4f3f81-4ecc-3d4e-9859-92df533ad6e4 | -30.39907 | -54.25911 | 2025-10-16 04:46:00 | NOAA-21 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 1.8 |
| ba8f2de6-9962-3ae2-9230-0c6a267d2b8c | -29.9874 | -53.48142 | 2025-10-16 04:46:00 | NOAA-21 | FORMIGUEIRO | RIO GRANDE DO SUL | Brasil | 4308409 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| f9bd7a88-fe00-3f4b-990b-e0af74e1ecf7 | -4.6813 | -44.082 | 2025-10-16 04:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 083456be-ce9f-32af-8a39-ce545ad99ff0 | -4.116 | -48.0352 | 2025-10-16 04:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 7529ec27-dd18-3766-b6b8-e7ad1b0ce316 | -4.3685 | -43.4071 | 2025-10-16 04:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 191.5 |
| b9b08a08-c74f-3d73-84b7-a2b0b4138639 | -4.0974 | -48.0361 | 2025-10-16 04:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 4fc3bd47-bb86-3931-82ae-56e81c086fbf | -4.6811 | -44.105 | 2025-10-16 04:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 112.8 |
| 6d2795ff-c40d-35dc-ac99-9aaecf4ffe25 | -5.6819 | -45.112 | 2025-10-16 04:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 78d5ae30-2f42-3e9e-8602-a8129e3c77af | -4.0976 | -48.0144 | 2025-10-16 04:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 141.1 |
| 573f0129-d84b-3b9d-9009-116be6e9e13e | -3.0157 | -45.3903 | 2025-10-16 04:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 68.6 |
| ea2dba80-c594-3c8f-bcf9-64ccd1a9b027 | -4.3872 | -43.406 | 2025-10-16 04:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 266.0 |
| 820a921a-c7d8-3e46-807f-1a569ef58305 | -5.6821 | -45.0893 | 2025-10-16 04:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 84.6 |
| ecbee6a7-189d-3e1e-aad6-b7ea93d4a7fd | -4.1161 | -48.0136 | 2025-10-16 04:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 154.1 |
| e6eed0cd-c0ed-3d08-abae-b8c7199b93a0 | -4.6626 | -44.0832 | 2025-10-16 04:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 205.0 |
| 62e907d1-e680-3609-bbd0-97d9cfef16e2 | -4.4059 | -43.4049 | 2025-10-16 04:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 08287c94-07dc-382f-8720-9940558b32b0 | -5.4762 | -42.9367 | 2025-10-16 04:50:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 42.9 |
| 8b86d435-aea1-35ce-b30d-cbe5d9d55457 | -4.3874 | -43.3827 | 2025-10-16 04:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 432.2 |
| 30396718-3ca8-3cbe-976f-628279fd5e87 | -4.6624 | -44.1062 | 2025-10-16 04:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 328.2 |
| b7f44b48-934c-3f07-b758-3882008d55ab | -4.3687 | -43.3838 | 2025-10-16 04:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 327.9 |
| 06f7c001-ee44-3e4a-838b-056e4cb15773 | -4.4061 | -43.3816 | 2025-10-16 04:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 167.6 |
| ad12edac-437a-393a-a786-c3252f07be87 | -4.1161 | -48.0136 | 2025-10-16 05:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 131.8 |
| 629db169-3bdb-386c-9575-96565f7fa32f | -3.0158 | -45.3679 | 2025-10-16 05:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 64b832fc-2306-3e53-a808-fe207b9f661e | -4.0976 | -48.0144 | 2025-10-16 05:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 180.6 |
| 9928f2ef-00d4-3572-b4da-de828b406460 | -4.0974 | -48.0361 | 2025-10-16 05:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 10e0549f-2c2e-36f5-9ea7-3e5eb5577fc8 | -3.0157 | -45.3903 | 2025-10-16 05:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 41.6 |
| fbc7b99f-05e4-3599-b72e-a2752acf3565 | -4.116 | -48.0352 | 2025-10-16 05:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 7ea63fdd-6b61-3d91-9f30-e31d24e49a79 | -5.47218 | -42.90759 | 2025-10-16 05:04:00 | AQUA_M-M | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 52.0 |
| e177dc15-2b0a-3372-aec4-45368a86a4ba | -3.84195 | -41.58069 | 2025-10-16 05:04:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 31.0 |
| 222376a8-b3fe-3e2e-8138-9c7710dd1e75 | -7.38839 | -39.70349 | 2025-10-16 05:04:00 | AQUA_M-M | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 24.7 |
| e129ea28-f2de-3ada-9c13-afac4916bd20 | -3.84708 | -41.54868 | 2025-10-16 05:04:00 | AQUA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 33.7 |
| b61a866b-ab04-3db9-8085-e7361cc306e6 | -7.64552 | -35.00055 | 2025-10-16 05:04:00 | AQUA_M-M | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 46f4ee83-1149-3750-a527-d2b943f38455 | -5.4658 | -42.94621 | 2025-10-16 05:04:00 | AQUA_M-M | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 35.9 |
| adaa7ed9-44c7-3bc0-93d4-2e7096530f5f | -6.14963 | -40.92184 | 2025-10-16 05:04:00 | AQUA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 48.9 |
| c361cc9d-518d-3ece-8385-ab37a04a1ac6 | -6.15336 | -40.92786 | 2025-10-16 05:04:00 | AQUA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 26.9 |
| edc13a1a-5173-3ff7-87a7-cc8638de491a | -7.3928 | -39.67686 | 2025-10-16 05:04:00 | AQUA_M-M | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 68.1 |
| 674903a6-d3cb-323a-8158-1e734b6068b7 | -6.15395 | -40.8955 | 2025-10-16 05:04:00 | AQUA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 82.2 |
| f6fde056-4101-34fe-b5fe-e0e1ed232233 | -7.3917 | -39.68391 | 2025-10-16 05:04:00 | AQUA_M-M | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 119.7 |
| 8ffaaf52-fe70-39f2-9ccc-53371907119b | -5.47731 | -42.91363 | 2025-10-16 05:04:00 | AQUA_M-M | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 64.6 |
| c683af7c-c391-333c-8528-16e1f27e5f9c | -6.15794 | -40.90114 | 2025-10-16 05:04:00 | AQUA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 123.0 |
| b01fea1b-99a4-37d6-85e8-5368125d0471 | -5.79814 | -35.5963 | 2025-10-16 05:04:00 | AQUA_M-M | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 5.9 |
| c6bdf9ef-4733-3c56-85e8-7ae7cc8f22b1 | -7.38964 | -39.69646 | 2025-10-16 05:04:00 | AQUA_M-M | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 79.5 |
| 5576b91f-0dda-3282-9e0a-6130b948fe5b | 4.40042 | -60.45002 | 2025-10-16 05:04:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3b01d3d-da85-3f1a-b224-f5136191f985 | -10.12413 | -44.57071 | 2025-10-16 05:06:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 15eb79da-1d5d-391e-b6de-57b236744d73 | -10.12595 | -44.5761 | 2025-10-16 05:06:00 | AQUA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 46.5 |
| 62bf423f-65cd-3530-b8e9-51fd1616c2c2 | -8.18565 | -43.29572 | 2025-10-16 05:06:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 43.6 |
| 584fb50d-7a89-3ba5-acd6-d4c5be199691 | -10.70523 | -44.42452 | 2025-10-16 05:06:00 | AQUA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 42.6 |


[Clique aqui para ver as próximas entradas](README68.md)
