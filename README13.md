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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 084f9b24-9766-345c-a321-32310e2baf55 | -13.02879 | -43.90041 | 2025-10-09 03:32:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f159dd1a-a961-35d8-8f4f-2a5f81f6d69a | -16.7514 | -43.97549 | 2025-10-09 03:32:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 5f0e21e7-59b8-369c-8db2-24a6277aa0cf | -17.3865 | -45.05389 | 2025-10-09 03:32:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 24df2087-6e52-359c-b37d-ce086f4e3f99 | -16.20067 | -43.6561 | 2025-10-09 03:32:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| edf39d25-bf00-347d-b22a-b9908b996b53 | -13.80053 | -45.82865 | 2025-10-09 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 03ac935f-9522-350c-8601-0785ba866fbc | -17.96013 | -45.00341 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 98776c82-7e22-352b-a22e-ced5af531bec | -16.28643 | -47.1293 | 2025-10-09 03:32:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3d1549f0-3bb0-354a-803b-58fcc982f677 | -13.8287 | -45.81857 | 2025-10-09 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7dda3e05-072c-3bb9-84fc-5c7cbb5bd733 | -18.41591 | -45.23442 | 2025-10-09 03:32:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 8dbeef8c-876c-34f0-95c6-5252fad24603 | -11.78742 | -45.0465 | 2025-10-09 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b6d34b3-51e5-3c33-989d-4a456ef3cc69 | -18.04031 | -44.97808 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3d71d23-7724-32ff-8cbc-588b2a3bac09 | -18.06457 | -44.42033 | 2025-10-09 03:32:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0998b2a9-8dfa-3601-bcb3-168283bb9427 | -15.64562 | -40.84163 | 2025-10-09 03:32:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ddad499f-8354-3445-8032-5a131d161804 | -17.64058 | -47.19756 | 2025-10-09 03:32:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 25364138-4d79-3012-a758-532e6f42ce0e | -11.98766 | -45.21906 | 2025-10-09 03:32:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 172f64c5-f22c-36c7-82b1-87d830df047f | -15.46981 | -47.9567 | 2025-10-09 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b13ab36e-3326-3c54-8975-f61045f30dd3 | -13.13078 | -43.9026 | 2025-10-09 03:32:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d22a52f9-556d-3372-808c-6470bedab575 | -14.98171 | -46.28922 | 2025-10-09 03:32:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 14c596b8-929d-35bd-b4c4-3d038254f5b9 | -13.78992 | -45.87891 | 2025-10-09 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bdf7b925-3364-399f-ba9e-3cf0cb70fbdd | -11.66914 | -43.90098 | 2025-10-09 03:32:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b7d1296-f58b-306d-b945-20959eecaf0f | -17.6393 | -47.20326 | 2025-10-09 03:32:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 5030d772-840c-336f-9a37-534cced793d6 | -11.76594 | -45.15201 | 2025-10-09 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ae36dbdb-96d1-3cf6-8a17-e024c83270f7 | -15.13147 | -43.67101 | 2025-10-09 03:32:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 88191913-a06b-393f-869f-ad23ac10fd34 | -18.29077 | -45.43475 | 2025-10-09 03:32:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a3e19ddd-6103-3eb4-b05c-1f8daffd01fb | -17.89561 | -44.26294 | 2025-10-09 03:32:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f4fc8669-d93a-352d-9fd0-498b69c384bc | -17.98828 | -45.62135 | 2025-10-09 03:32:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d5cc4e8b-c469-3b84-902c-eb7581a8eb24 | -11.78561 | -45.15072 | 2025-10-09 03:32:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e4bd92a3-32f6-33ce-a840-623f6b56841d | -17.58316 | -46.06962 | 2025-10-09 03:32:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6c4514a7-8151-3ce9-9bff-109730668301 | -17.33461 | -42.13605 | 2025-10-09 03:32:00 | NOAA-21 | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0049c94a-d349-3a8c-afe4-c1abb622a46d | -13.80247 | -45.85039 | 2025-10-09 03:32:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6f866b09-1642-3386-850d-1a6abdd5fb69 | -15.31855 | -43.84959 | 2025-10-09 03:32:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6fb3b005-dce6-310a-9f85-bbf0e46830b6 | -16.70439 | -47.5931 | 2025-10-09 03:32:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2389189b-c012-3b65-af71-0baf39868767 | -13.48758 | -42.02201 | 2025-10-09 03:32:00 | NOAA-21 | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cb18ebaf-7b67-3720-903b-25bf8f24db96 | -13.80439 | -43.93251 | 2025-10-09 03:32:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9ca9dae7-a2ad-3e0d-bfa9-e06434ec4c8a | -17.63811 | -47.20856 | 2025-10-09 03:32:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 19.9 |
| e17dcee2-c5c0-37ef-9a46-a06e9db57121 | -17.21235 | -47.65229 | 2025-10-09 03:32:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| e930d9af-7491-34f8-8b04-2c10198ac518 | -17.95258 | -44.98635 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| af051ec4-65a5-38fd-a8a9-ed301ead08e2 | -15.21873 | -46.37756 | 2025-10-09 03:32:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 039aa5ff-1f0e-375f-bcd0-ff6ec973d57b | -17.45996 | -43.38587 | 2025-10-09 03:32:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1656827-41f7-3ba2-b383-a61e42c3667d | -15.38787 | -47.30067 | 2025-10-09 03:32:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 24a6995c-be4b-3889-b181-879e57d7238c | -17.37754 | -45.07896 | 2025-10-09 03:32:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bd96795e-ba9c-3710-ba90-2ff5367065c0 | -14.78422 | -46.11033 | 2025-10-09 03:32:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fdfe1c5f-10ec-3ba6-950a-e146c6677438 | -13.61345 | -44.43847 | 2025-10-09 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d5e44550-feb9-34fe-8a47-74b8e91c4c8e | -18.03867 | -44.98585 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 473e26df-9b6b-35a5-b4a3-dc2330ae2167 | -18.03226 | -44.98901 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| cc928955-02bc-3b7d-a548-a7c1c12e10b6 | -17.97458 | -44.9635 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6dc5c00f-5268-3745-9222-1c603e796d6b | -15.8095 | -43.78276 | 2025-10-09 03:32:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 216f53e1-d3b4-3bd6-87ba-d5707e00e1a0 | -13.03363 | -43.90555 | 2025-10-09 03:32:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b7822219-2b09-3af2-9c1f-4884a4a952e3 | -18.41765 | -45.22625 | 2025-10-09 03:32:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5b5f44c2-8622-3385-aad7-e5cd812bee28 | -14.41596 | -43.98616 | 2025-10-09 03:32:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 090560c7-a525-3e36-bf2c-19e673b55d7d | -17.38805 | -45.05669 | 2025-10-09 03:32:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cae2beb0-ef81-3adb-a489-4887eaa9b33c | -18.08992 | -44.44988 | 2025-10-09 03:32:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63e3a2ec-05f2-33a0-aff0-fef179caa013 | -11.9948 | -45.18397 | 2025-10-09 03:32:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e119c115-4a14-3ff7-9dbc-7c7bf4ed9c05 | -14.97931 | -46.28614 | 2025-10-09 03:32:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 80ae0ca7-a12e-3572-a0e2-9e4ed55f3a3f | -15.47045 | -47.95287 | 2025-10-09 03:32:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| af82299c-ec22-30e4-bef6-37a123784467 | -12.42762 | -45.70778 | 2025-10-09 03:32:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f34d8546-5264-31a5-843f-dab4aa794b42 | -17.95538 | -44.99873 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d173a30f-0df5-34d7-883a-9434d7ee5c6b | -12.04682 | -43.50146 | 2025-10-09 03:32:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3a2f646-e944-3ce5-9b49-547341855d9a | -10.86625 | -44.63648 | 2025-10-09 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 05344208-bd39-34a1-bf58-390212ddffec | -15.32285 | -41.73925 | 2025-10-09 03:32:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 203b09ae-e9a5-37fe-9f77-fd5e429982e8 | -10.88055 | -45.08296 | 2025-10-09 03:32:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 987fb95f-6128-3fdb-8d5a-8e3060f26422 | -17.60789 | -47.18477 | 2025-10-09 03:32:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 250d8305-9bd4-33b1-8fa5-e5af1994a98f | -14.42224 | -43.98352 | 2025-10-09 03:32:00 | NOAA-21 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| aa674c47-c714-3e52-a4ea-21c9c88db0da | -17.93112 | -44.60403 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a8520aac-b245-3b2b-9c8c-f19e9423a308 | -15.63682 | -40.83989 | 2025-10-09 03:32:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2ab396f9-d154-3017-8ad2-7abab27ed20a | -18.06085 | -44.43835 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cf7dfc98-3c56-36a1-98a9-9fc0583dc6eb | -17.63182 | -47.20703 | 2025-10-09 03:32:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 31.5 |
| e29bf267-15f2-3a64-b5f3-5ed58b1f0ad6 | -18.30558 | -45.43346 | 2025-10-09 03:32:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4cecc893-85b7-34fe-a754-0f28ff3d1c4b | -15.21733 | -46.38406 | 2025-10-09 03:32:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d07045d8-5974-3bdc-8cf6-7a4488279902 | -14.97812 | -46.29181 | 2025-10-09 03:32:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f5b6adda-3575-308e-87e7-80e23b538335 | -15.64036 | -40.84523 | 2025-10-09 03:32:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f6586513-50bf-3793-b347-4efefee25849 | -17.53563 | -46.75334 | 2025-10-09 03:32:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43da03e1-628b-3f91-aeea-23dd6eb17c40 | -13.94096 | -42.3556 | 2025-10-09 03:32:00 | NOAA-21 | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9afe483d-148d-38e1-8c60-d1447e977412 | -17.9003 | -44.26245 | 2025-10-09 03:32:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 95a8142a-b2ae-31bf-a202-6a2c154736f7 | -15.13217 | -43.66751 | 2025-10-09 03:32:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9b6ea4ab-3e90-3ff3-84a8-308f3a380f67 | -16.27098 | -47.13816 | 2025-10-09 03:32:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4227008e-616a-3001-a377-9a237b804e1c | -17.39009 | -46.89071 | 2025-10-09 03:32:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b072089c-7e58-3272-9f3b-0ced715900af | -16.08521 | -45.79021 | 2025-10-09 03:32:00 | NOAA-21 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4cbd5c73-610d-3c05-86c4-115468bf15e1 | -13.39488 | -47.25413 | 2025-10-09 03:32:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 2454c3f6-baaa-3f28-90fe-69bf6e70ea61 | -18.09418 | -44.45596 | 2025-10-09 03:32:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2006d966-fddc-3165-acd3-c3118105b30f | -17.37784 | -46.88705 | 2025-10-09 03:32:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5be17b48-cfee-3b06-8e7c-538f81e4a72d | -15.07357 | -46.61092 | 2025-10-09 03:32:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ccb665ea-c6cb-3071-938c-e8cbb6428f91 | -15.78852 | -46.24819 | 2025-10-09 03:32:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b5a382ee-2d3b-303e-aad2-8e71d05b5989 | -17.37749 | -46.66093 | 2025-10-09 03:32:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 54d50e41-8b45-3884-9beb-5fc5ad2374a0 | -14.7883 | -46.10344 | 2025-10-09 03:32:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d3a5f98d-0f2c-3fe3-8da1-f65e3b0c9470 | -10.85505 | -44.62891 | 2025-10-09 03:32:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| f04b3507-75b8-397d-bc16-3762055a8b4b | -15.2371 | -46.35325 | 2025-10-09 03:32:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ee9bc8d-e42a-3a5c-86e7-edbce6775bf0 | -13.8235 | -45.81232 | 2025-10-09 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 230fe867-4914-30ad-a52b-abaada7bc968 | -18.03949 | -44.98195 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0239b8a6-5a72-324c-8197-92d2dfecd606 | -14.93473 | -46.78365 | 2025-10-09 03:32:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c9bc11d7-86d1-3cab-a78e-cf076d8fa202 | -18.41506 | -45.23841 | 2025-10-09 03:32:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 1e1d0472-1a5a-3431-8804-64e48027d4c8 | -17.95069 | -44.99378 | 2025-10-09 03:32:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| db3904ff-964c-3ec1-8878-e235f4fcc039 | -13.38632 | -47.26067 | 2025-10-09 03:32:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a0ebad84-7296-3ca7-9e85-891eca7d7d7a | -17.4945 | -45.30438 | 2025-10-09 03:32:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e3c47446-393c-35ae-b9bc-73b58567f73c | -17.37678 | -46.66006 | 2025-10-09 03:32:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 848a94a0-9784-3ecd-b4c0-a5b9ae9387c8 | -17.4611 | -43.38028 | 2025-10-09 03:32:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 28f0fa07-a394-3997-90e3-97165ea4a569 | -17.33355 | -42.14137 | 2025-10-09 03:32:00 | NOAA-21 | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6ca5cac8-a8fc-323c-a0fa-b64bf547260e | -17.52338 | -46.75031 | 2025-10-09 03:32:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2031bb1a-e956-374d-ad25-8cca8a6edc29 | -16.37686 | -46.38712 | 2025-10-09 03:32:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 45d0fa39-ab75-35ac-8c45-f971e89e03f2 | -15.05889 | -42.33759 | 2025-10-09 03:32:00 | NOAA-21 | MORTUGABA | BAHIA | Brasil | 2921807 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |


[Clique aqui para ver as próximas entradas](README14.md)
