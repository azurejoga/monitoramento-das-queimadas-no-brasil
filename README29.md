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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf3c15d5-9cd0-39e3-aa29-5fdb5862fc84 | -5.62987 | -44.83972 | 2024-12-04 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 393ee485-5be5-35d1-9ac9-b83de79eb5a4 | -6.40422 | -44.05453 | 2024-12-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ff3ebaa-ca4e-35a9-9ba6-31d24745d03c | -10.21798 | -42.18749 | 2024-12-04 04:12:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 71938f65-0a5c-3cff-ab8f-3157ae473ff6 | -5.5828 | -45.15508 | 2024-12-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93937695-9a30-340f-8339-b8ee409c196b | -9.19499 | -43.15889 | 2024-12-04 04:12:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8b94ea14-3693-3849-8df9-69f74cdc719c | -7.54314 | -45.87042 | 2024-12-04 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4d93a15-1ab3-3726-9b94-7ad94aca9dd6 | -6.25668 | -43.16226 | 2024-12-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.5 |
| f58c0b57-083c-3ae8-b36a-97049402a543 | -6.25513 | -43.55998 | 2024-12-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 967263cc-dd14-39b6-b2ab-70ec1b2606de | -10.04857 | -36.56063 | 2024-12-04 04:12:00 | NOAA-20 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2f26cf8b-79ef-3919-a7e9-42a2b9562518 | -9.01673 | -35.64619 | 2024-12-04 04:12:00 | NOAA-20 | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7f93efa8-851d-33c4-b62a-0573c30f8e24 | -5.57585 | -45.15394 | 2024-12-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5c48c013-8f51-33bf-ab1d-228563464cc5 | -5.57337 | -45.16934 | 2024-12-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6a38ce1-509b-3aff-af5b-aa3b77da36b2 | -6.26054 | -43.15933 | 2024-12-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 978c5059-3cc8-3a47-8221-437e6db45837 | -6.25236 | -43.55598 | 2024-12-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b1155ba-6a1b-3c31-a7ab-8fed226b6cbf | -6.11646 | -41.93503 | 2024-12-04 04:12:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 47b643c6-e926-31f9-aa47-2bf9a98a7be5 | -6.0183 | -42.36711 | 2024-12-04 04:12:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7f8384bc-e38b-37ce-907a-3ec95466433c | -6.25181 | -43.55946 | 2024-12-04 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bd708594-28fb-382d-877b-3ccf38882535 | -10.04682 | -36.55787 | 2024-12-04 04:12:00 | NOAA-20 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7d6694ff-9669-306c-895c-5c7527e1aeca | -10.03989 | -36.55449 | 2024-12-04 04:12:00 | NOAA-20 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 182d58bd-655d-3163-b408-c05ae73a57d3 | -9.02163 | -35.64689 | 2024-12-04 04:12:00 | NOAA-20 | NOVO LINO | ALAGOAS | Brasil | 2705606 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4220df19-7d7c-3b54-b11e-02d415a2c566 | -5.57399 | -45.16548 | 2024-12-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 32709fdb-961a-35a7-949b-978f778458d4 | -6.27724 | -44.73957 | 2024-12-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19fc4aaa-51a6-3c33-b1b6-e48f695bd2d8 | -10.04618 | -36.56276 | 2024-12-04 04:12:00 | NOAA-20 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 611b9256-9f34-376a-834f-6e9b8415bc49 | -5.58095 | -45.1666 | 2024-12-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc91e9cc-e7d9-3e23-88de-dd88a9417ec9 | -7.5566 | -47.58587 | 2024-12-04 04:12:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 32ff271b-2af3-3d50-b376-79e4f827771e | -10.04389 | -36.56 | 2024-12-04 04:12:00 | NOAA-20 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3b21018c-2c05-3eab-ad85-605cb67a3d55 | -11.18629 | -40.31785 | 2024-12-04 04:12:00 | NOAA-20 | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 470959fd-bb7b-3532-9605-c3e0fe796c47 | -10.22213 | -42.18771 | 2024-12-04 04:12:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2ef3f2ca-54bc-3cc0-a84a-24cce6de5882 | -7.5643 | -47.58719 | 2024-12-04 04:12:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1bdca0f0-eb37-3726-a1e7-4083f327e7b9 | -6.08018 | -48.07302 | 2024-12-04 04:12:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 96e509b0-781e-33dc-b686-373469a129cf | -6.09503 | -43.9689 | 2024-12-04 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9d46cf62-6eba-3f5a-8189-d6edad568667 | -5.81718 | -44.11073 | 2024-12-04 04:12:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 37f4556f-5072-3c0a-8cc8-aa3c94934965 | -7.56045 | -47.58654 | 2024-12-04 04:12:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 72f82680-dba8-3d93-9c9c-c5246c956f22 | -6.07611 | -48.07241 | 2024-12-04 04:12:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ea959b3f-0314-3b78-9a9c-a83150b7c625 | -11.5287 | -38.01244 | 2024-12-04 04:12:00 | NOAA-20 | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a4932f61-052d-32ff-9c5d-194ea4a45992 | -5.58033 | -45.17045 | 2024-12-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79ada988-b7e2-3e4a-849a-ce7b746fad4d | -5.57809 | -45.16219 | 2024-12-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f190644e-ff1e-35f7-8357-099942d0f552 | -6.40478 | -44.051 | 2024-12-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b45469e2-94d1-316a-b561-e33405fe556c | -6.08136 | -48.06593 | 2024-12-04 04:12:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 61f7da74-bb99-3d26-a993-ae8c1b48c56e | -6.08077 | -48.06947 | 2024-12-04 04:12:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3cc876ab-ec92-37a6-97a4-943e67757a99 | -5.63331 | -44.84026 | 2024-12-04 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca09e9cf-aefd-36f9-8eed-bf1041903b02 | -6.07671 | -48.06882 | 2024-12-04 04:12:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bdcdc099-6ff4-3eb6-9e79-fbc8511a27d1 | -6.39697 | -44.05701 | 2024-12-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f69e947f-11b7-3778-a406-38f93563cb09 | -6.40699 | -44.05864 | 2024-12-04 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5588e9fe-d377-31c5-9eb1-e4ec7b36be97 | -6.09559 | -43.96535 | 2024-12-04 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15d1eace-ab4a-3090-870b-ae253925f072 | -5.57932 | -45.1545 | 2024-12-04 04:12:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 146f01da-8b52-39d3-875d-3d3f60d4cb41 | -6.27665 | -44.74323 | 2024-12-04 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13f7d167-f9f2-3747-b5eb-9b810afcd69f | -6.25999 | -43.16278 | 2024-12-04 04:12:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 1def8fc8-d07a-3a2a-9d1b-2f2d98c206c2 | -5.63271 | -44.84398 | 2024-12-04 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c5d2ee54-8b07-3b27-9d30-35964a7a4728 | -5.62584 | -44.84292 | 2024-12-04 04:12:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7b78a57f-0bd8-3e72-bb01-da2b934d4d44 | -12.48119 | -46.34756 | 2024-12-04 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9c4cac2f-dcef-3da2-8773-e91722848eaa | -17.84902 | -40.12725 | 2024-12-04 04:14:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 88b76176-5dd6-3102-be0f-7fc5573f5ae4 | -13.24256 | -39.97915 | 2024-12-04 04:14:00 | NOAA-20 | IRAJUBA | BAHIA | Brasil | 2914208 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7c743ffe-c355-3d14-8de3-d566735a0700 | -17.85363 | -40.12402 | 2024-12-04 04:14:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b9475508-cbd5-3818-b6a8-93bd51f28ba2 | -12.78233 | -45.55555 | 2024-12-04 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 963f0838-6fe9-386e-9068-19e581699581 | -13.80964 | -41.58309 | 2024-12-04 04:14:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c3114057-09b5-3b97-b8b1-105b14e73be7 | -13.80669 | -41.57807 | 2024-12-04 04:14:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 83e2af15-a5d4-3d52-b3e6-d1ccff1a651c | -12.92901 | -41.11642 | 2024-12-04 04:14:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 47ff4274-4652-3eaa-8c5b-89abf33b790f | -18.73078 | -39.89433 | 2024-12-04 04:14:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 98f48b7b-6f71-3ed3-807e-0a11b64e6921 | -13.41848 | -41.11164 | 2024-12-04 04:14:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 35313047-ff9e-38ba-8719-6a4cca05b464 | -12.48181 | -46.34376 | 2024-12-04 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9f1d16d7-7af9-356e-99eb-7dbf87f99ae8 | -12.93266 | -41.11692 | 2024-12-04 04:14:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 81029258-dd29-35da-a1df-45c7952b5c71 | -13.81028 | -41.57864 | 2024-12-04 04:14:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| eda5ab79-e7c0-3961-8fad-ab86d86078c0 | -17.85264 | -40.13155 | 2024-12-04 04:14:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| a2cc2eff-82ac-3782-b53a-3d119400a41f | -13.41768 | -41.11417 | 2024-12-04 04:14:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bf276ce5-da2e-3c2a-8d5b-7b8d34b62faf | -12.47496 | -46.34258 | 2024-12-04 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bd8807bb-bb36-34f0-935f-3152353bf060 | -12.78292 | -45.55195 | 2024-12-04 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11aeaddd-161d-344c-9934-9780492024d8 | -17.85314 | -40.12778 | 2024-12-04 04:14:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 8bf80967-07a0-3fea-8a1c-2946247809a2 | -12.47776 | -46.34698 | 2024-12-04 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cc21fc4b-5cb2-3663-85fc-a0eb19db2aa5 | -12.86657 | -46.69399 | 2024-12-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 36900fa7-1ba4-3c98-a2e7-83f1df058cd1 | -16.67992 | -43.88476 | 2024-12-04 04:14:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc93e9c5-a756-315f-b231-35d1bde6dc94 | -13.41402 | -41.11359 | 2024-12-04 04:14:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| eab510ac-1b57-3d75-8743-d5714912a548 | -13.81089 | -41.57434 | 2024-12-04 04:14:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a4d8ac7e-84e7-314d-9ff6-40ddbb850161 | -12.47434 | -46.34639 | 2024-12-04 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f95c365d-4557-30bf-9a9e-8092ab2fb4c4 | -12.02293 | -49.54454 | 2024-12-04 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d74cad54-8b6d-331b-ae0e-84cd3079ce14 | -12.45656 | -47.30642 | 2024-12-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be02982b-00a5-37e3-a88d-14b99a09aef7 | -13.41482 | -41.11107 | 2024-12-04 04:14:00 | NOAA-20 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3459fee5-1f87-3c06-9623-71d88f552c50 | -12.47838 | -46.34318 | 2024-12-04 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b793a719-3ed2-3c8b-9a52-6ed3eab84352 | -12.44181 | -44.96798 | 2024-12-04 04:14:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2755638d-b01d-3469-a4be-e5c080fa48bd | -12.92964 | -41.11209 | 2024-12-04 04:14:00 | NOAA-20 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| a36f1c21-f018-3859-9e6f-a23f9a73fb3c | -12.38145 | -47.32418 | 2024-12-04 04:14:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be120240-bd74-3c82-b6b6-db41ea6d3fbe | -13.24157 | -39.98181 | 2024-12-04 04:14:00 | NOAA-20 | IRAJUBA | BAHIA | Brasil | 2914208 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 42868cbf-3c82-3133-8006-06aa21de5458 | -12.17511 | -47.98738 | 2024-12-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3468a997-f46a-3ded-864f-b5eba3f481e7 | -18.60776 | -44.25936 | 2024-12-04 04:14:00 | NOAA-20 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4a6c92eb-61b3-3b1e-943e-b23c103e1026 | -6.0858 | -48.0774 | 2024-12-04 04:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 208b80ee-0df6-3007-937c-f5a2c639229f | -1.7729 | -52.6156 | 2024-12-04 04:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 4a8fac2b-740b-344f-b682-1dc500cce813 | -1.7728 | -52.636 | 2024-12-04 04:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 08ee8864-64f2-3bdc-aa53-d06e20e2d2e2 | -6.0674 | -48.0569 | 2024-12-04 04:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 83f10e9a-9114-332c-b486-47b2960a52f2 | -3.259 | -53.659 | 2024-12-04 04:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| e3594a44-cd6d-3262-90d9-2a1fc4dcf4ad | -6.086 | -48.0557 | 2024-12-04 04:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 7959e737-708c-358e-b09f-3846e76c0933 | -2.8196 | -53.0629 | 2024-12-04 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| bc2debbf-ea06-3d36-8f39-f648d0e5bc94 | -1.6241 | -53.5308 | 2024-12-04 04:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 9b98dabd-d721-3d38-8875-df9172c8da2b | -3.259 | -53.6388 | 2024-12-04 04:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 328e904e-6bee-3436-a72f-25143d29a893 | -1.7361 | -52.6162 | 2024-12-04 04:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 8dadf957-1552-37ac-9cd7-1bf5ff059ea9 | -4.1223 | -43.9299 | 2024-12-04 04:20:00 | GOES-16 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| a6f5fc1d-2b18-3816-901f-7c9e0f37598c | -1.7544 | -52.6363 | 2024-12-04 04:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 19891102-24e2-3284-a3ce-16a748f8df59 | -1.7545 | -52.6159 | 2024-12-04 04:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 545a2bdc-e639-3504-9086-325fb8249aee | -2.8012 | -53.0633 | 2024-12-04 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| f579750c-6a11-3b45-9fda-49fd922d4480 | -3.2775 | -53.6181 | 2024-12-04 04:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 47cb829c-70b4-3779-b9fa-36f9926b9f2c | -2.8197 | -53.0425 | 2024-12-04 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |


[Clique aqui para ver as próximas entradas](README30.md)
