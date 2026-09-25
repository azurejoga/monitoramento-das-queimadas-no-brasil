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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 71fbd66d-f2b5-3fae-9551-a7c86035ea09 | -12.24167 | -50.74434 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 79.6 |
| f2b87bdd-bfed-35df-a7fe-7d274f11d2ec | -10.42408 | -53.78059 | 2026-09-25 05:31:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 972bb4a5-b5b0-316e-8150-02de06634880 | -9.58233 | -65.90231 | 2026-09-25 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c03de63e-0c6e-32a2-b825-cf825609eb7d | -11.28223 | -51.28992 | 2026-09-25 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5ef6f93f-8b90-3534-9e90-b204c16ca9b9 | -9.62579 | -62.30158 | 2026-09-25 05:31:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 21c6c0e4-0bba-366a-8f54-0248f5c0234f | -10.62592 | -54.00065 | 2026-09-25 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1c0863d-7380-3c36-aed3-4129505db1b9 | -11.2896 | -51.29577 | 2026-09-25 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 4a1fb642-827a-3c39-b83b-c45ada7f5357 | -9.10883 | -61.4367 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 153813c2-849f-34a5-bc66-8352e5006d7e | -9.67256 | -66.82804 | 2026-09-25 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d881c1d0-2890-38d6-9242-663757b75ec1 | -11.2902 | -51.29043 | 2026-09-25 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 15.2 |
| f63d37cf-870f-36dd-9df2-f9b12da80431 | -9.36018 | -60.36598 | 2026-09-25 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 21d91677-92ab-3994-b918-2288f1373d79 | -12.19333 | -50.77966 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 597f82e5-e094-3881-aa27-48426141f8f0 | -12.19949 | -50.72553 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 183c1b61-8ade-3206-beaf-3c141c2f4556 | -9.31857 | -59.67517 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| abc6d685-bd90-3a69-b72b-6b5eb9395d83 | -11.808 | -58.16171 | 2026-09-25 05:31:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb9882bc-2bbd-3b85-8079-ed73732e51f3 | -8.8498 | -71.08801 | 2026-09-25 05:31:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c837f8ea-9593-35b0-9da0-b5f814a12f07 | -12.20768 | -50.80694 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 704aeb19-f4c7-3050-8a49-9e0eb422fd6f | -12.21696 | -50.78388 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 828f9a17-d15c-386d-af2a-6668a9339791 | -9.35946 | -61.171 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2a027ee3-e97b-30ba-b55b-1910d3e0201c | -15.18253 | -56.05744 | 2026-09-25 05:31:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 898dfd83-fc19-3ba7-a632-10f78bc0caf0 | -10.66595 | -61.83029 | 2026-09-25 05:31:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f1c9222-8588-3cc9-a09a-6f0f95db438f | -9.35265 | -61.16994 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fac496c9-6245-31a7-9ac8-fd5275b2a562 | -12.201 | -50.80608 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 47.4 |
| ec3b3979-c988-3e28-94c8-bf7016aea5b4 | -12.23088 | -50.71843 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 0f1c0da9-eae7-3523-9b54-f481dad6900a | -10.56457 | -59.48627 | 2026-09-25 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08ba02df-9455-33c5-9ec7-5fc38e6e6ebc | -12.20164 | -50.80011 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 8c4c3001-bd16-34c5-8b6a-e62d281f32d6 | -12.20002 | -50.78049 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f7298144-272e-31ed-b318-e1f4b1af31af | -9.01929 | -60.51715 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d52ec74d-a0fe-363a-baa5-9a132c380e8d | -12.2069 | -50.72033 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 996088de-3467-36cf-9bd0-9935b8927237 | -12.25243 | -50.7701 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 25.6 |
| f0728b3d-e9c2-3650-a39c-1d57266f93df | -9.21041 | -60.4763 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7844ae0-04e7-3425-85be-b6caf1296a49 | -9.06799 | -65.69651 | 2026-09-25 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 271863e6-260f-393c-b136-8e2bcead9be4 | -10.90341 | -53.95242 | 2026-09-25 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7e283d6-6dfc-33f3-81e1-568f14ed9dfe | -9.38708 | -66.51241 | 2026-09-25 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5fe07e0d-8fd3-386e-b8f8-b805b9bf03dc | -9.956 | -64.7579 | 2026-09-25 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8e108833-7d80-345e-8535-31c797441aad | -12.19689 | -50.7813 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4c0375f3-0bb3-3fe8-8e18-6b73f7f524c5 | -12.20966 | -50.69617 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5276ec60-ca78-3003-8114-5b5fe1ad7a8b | -9.26888 | -57.18081 | 2026-09-25 05:31:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b542dff4-e32a-3768-aff0-6eff3d4a6a79 | -12.20897 | -50.795 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 64108b99-c168-3235-8f28-7fc85e77613f | -9.04204 | -65.40896 | 2026-09-25 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52d72d1d-1398-3728-a1ac-45d19a70657a | -8.38768 | -71.07686 | 2026-09-25 05:31:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abe0e9fc-1135-3a7b-9d58-786e782ad711 | -12.23836 | -50.77443 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5a5892f1-7d84-332b-bdd3-5e8af6384662 | -15.07553 | -52.80235 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c1501cbc-09da-3e58-8194-91fbfac161dc | -11.89833 | -62.90974 | 2026-09-25 05:31:00 | NOAA-21 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57208045-9be5-30e6-b90a-7f0cab7a5456 | -12.20206 | -50.73315 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 466f37bd-d407-347a-8c9f-38e78739017f | -9.06734 | -65.70047 | 2026-09-25 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbfca5af-9a40-3b20-86a4-27b966b9a7f8 | -11.56412 | -61.2394 | 2026-09-25 05:31:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bcf42dc9-86c1-3012-ba41-16f7c29eecaa | -9.32285 | -59.67814 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1beb9cf-a919-389e-a878-abb64e022fbf | -12.70201 | -63.07716 | 2026-09-25 05:31:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7774636c-c300-3962-a4fb-f73cef1f2f43 | -12.20431 | -50.68317 | 2026-09-25 05:31:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b699d4e3-91c0-3c76-bd2e-b60a37fd9485 | -7.86127 | -72.86328 | 2026-09-25 05:31:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 96a0163e-bccf-3c28-9eee-0bb79bd9d43e | -16.00695 | -56.3207 | 2026-09-25 05:31:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 3251fa33-f889-3880-9b91-00402a1f890a | -9.59032 | -60.51963 | 2026-09-25 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f5b0828d-ce57-3c98-91c0-33d88e148b94 | -12.23101 | -50.77959 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 0fd45055-e096-3791-857e-1e4c58985cc8 | -12.1956 | -50.79327 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e2d5bd01-26b4-36d3-a62b-f4ddf8083d3f | -10.4182 | -53.78349 | 2026-09-25 05:31:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 66f7a257-00c0-3749-94cd-80247137260a | -12.2289 | -50.73659 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 20958951-bdae-3f6f-9d90-c32626034430 | -12.24506 | -50.77528 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 25.6 |
| ddab15c1-ae0e-3308-86c0-f16adf7aaf53 | -9.93482 | -60.71674 | 2026-09-25 05:31:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5329c679-831d-3647-859a-d49b6b3f9ec1 | -11.94053 | -62.3902 | 2026-09-25 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14216702-30dc-3163-8ab2-1ff72296b277 | -9.18196 | -58.06926 | 2026-09-25 05:31:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3538d46-7577-3502-9b21-496c8e9e60aa | -8.96071 | -72.84843 | 2026-09-25 05:31:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b86ed2e5-6abc-3056-b369-8e24516e698e | -7.75849 | -70.72982 | 2026-09-25 05:31:00 | NOAA-21 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb32fec0-d298-30aa-a0eb-f2eaf9427872 | -9.1488 | -59.48476 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a89fe83c-653b-3ed6-a1dd-281fe7bad252 | -8.96003 | -72.85217 | 2026-09-25 05:31:00 | NOAA-21 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 54b34693-e459-32e1-a30f-3461dc20d716 | -9.58741 | -60.51517 | 2026-09-25 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4ae73a5-81ed-3d31-a5ff-28e5c26dec6e | -10.61854 | -53.99879 | 2026-09-25 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce394bbb-ee70-3d55-b99b-fcdfb0f1de9b | -9.73401 | -54.80477 | 2026-09-25 05:31:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9c96f6d9-2eb8-30ce-b3e6-fcce1b59c0a7 | -12.22351 | -50.72362 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 36.0 |
| b62ee340-6dd3-31b3-8866-4e8b3e5fa231 | -9.73907 | -54.80504 | 2026-09-25 05:31:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5d2928c6-62e7-3361-b9bc-17ddf6f7b83f | -9.08468 | -61.4367 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| af937c16-6b86-330b-a742-01b6d8eec05e | -8.79421 | -66.597 | 2026-09-25 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b321d62b-ebe4-36e9-82ad-67bad3aa09b5 | -11.18048 | -51.36579 | 2026-09-25 05:31:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 833788ea-656c-3d2b-b78a-80471e3c83a8 | -13.22069 | -51.55527 | 2026-09-25 05:31:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| bb90bb19-bcb3-3dc5-b2fe-4f07b0d969ac | -9.60733 | -61.8232 | 2026-09-25 05:31:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83b77eb9-1f56-38c9-839d-34128f39bb8e | -9.06445 | -65.69599 | 2026-09-25 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d1d53d8-811a-319d-a0d7-345d597c058a | -12.19624 | -50.78729 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 2aa4c8ba-17ea-37e7-857c-b5597739e64e | -12.18095 | -50.80352 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 70844f35-bd02-393e-8c69-b7a7cb6cf44c | -15.07605 | -52.79739 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 95cd8ee0-95f7-3a32-89f7-36b0d9dc0c84 | -12.23635 | -62.63469 | 2026-09-25 05:31:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bab031ef-9e99-34ef-9800-39df92e64ca9 | -8.79051 | -66.59637 | 2026-09-25 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f6f17b26-ad0e-3463-bf17-fa9ae0448f50 | -11.28318 | -51.29493 | 2026-09-25 05:31:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2ae8ec0b-64fe-3606-8c9b-d3ab0ffbbfec | -12.20229 | -50.79415 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 584fbfd0-18e2-3113-b55e-b56f40881def | -15.18363 | -56.05882 | 2026-09-25 05:31:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| db7eaa59-4783-3032-bfd8-e3f8a5b13b11 | -9.81849 | -65.06229 | 2026-09-25 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 47875b3c-c1a5-3680-ab6f-753aa50073d5 | -9.15798 | -59.47294 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d65406be-ac27-3a2d-a875-f4691955c80d | -11.56758 | -61.23991 | 2026-09-25 05:31:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9efdce4f-6d79-3880-85dc-128586b0eddc | -12.17467 | -50.70408 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.4 |
| df2dcff8-bc61-35fc-81ae-057c6add879e | -12.22693 | -50.7547 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 95827ffb-d516-325c-9a21-bc0fd398b9a7 | -9.21271 | -60.46062 | 2026-09-25 05:31:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc378ccc-1654-3a61-9062-c7149fa9a31d | -9.49932 | -64.75175 | 2026-09-25 05:31:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2973fc38-7582-3c1f-a7bd-0f707e3564f1 | -10.61895 | -53.99537 | 2026-09-25 05:31:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9f9afd5e-1639-323b-98b1-fa79a7cd13ee | -9.22655 | -71.86089 | 2026-09-25 05:31:00 | NOAA-21 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cef06143-11fb-3141-9c44-58a1515de592 | -9.38047 | -66.5069 | 2026-09-25 05:31:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ba9f9886-8166-33e2-ae9c-2b36d3f51b88 | -8.46449 | -64.15237 | 2026-09-25 05:31:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f4cc30b-55b1-3439-a975-9006f265b7b4 | -9.58333 | -60.51859 | 2026-09-25 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 65e1ca4a-3eba-3296-bfa7-fbd6796ebf12 | -8.00547 | -71.30956 | 2026-09-25 05:31:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96372bd2-3542-371a-8f88-25215aa1633f | -9.42579 | -60.46344 | 2026-09-25 05:31:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5394ea53-e285-3d6a-83a9-1de994c44abf | -12.24572 | -50.76928 | 2026-09-25 05:31:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 25.6 |
| dbf75f33-24d7-3f15-9958-d3ac2adab216 | -9.23892 | -68.06221 | 2026-09-25 05:31:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README35.md)
