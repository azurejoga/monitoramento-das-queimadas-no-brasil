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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bdcaf8d2-20d5-3fdf-a7b8-c0a154ce3856 | -10.14946 | -46.53374 | 2026-07-29 04:32:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b89b613-80e4-3cea-bf1a-897842918488 | -6.87437 | -46.01974 | 2026-07-29 04:32:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d9d574f4-8305-37e0-a04b-4698c637e0ee | -11.17745 | -49.93604 | 2026-07-29 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 004b27fa-66ac-3b81-9489-6feb1821cebc | -10.85933 | -49.44305 | 2026-07-29 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2d9aa091-434e-32c7-b41b-1e2a2da7c532 | -10.96841 | -49.44188 | 2026-07-29 04:32:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5290f198-4a0b-3c4e-bd19-5a24a03214ca | -7.34683 | -45.84394 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bbeaf3f4-a1e6-34f5-af56-7dec5a48a0d8 | -7.33926 | -45.85028 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e313092e-40e1-376c-95d9-fd84d0594795 | -7.34368 | -45.8438 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 41b53ae5-0e0c-319b-9a93-fe890ffdeea6 | -5.23196 | -56.01169 | 2026-07-29 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8184eb7d-1c82-35d8-aa6a-ceccf3346e02 | -11.26539 | -49.55611 | 2026-07-29 04:32:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 15743fbb-a380-3370-b0cc-3c02d6fb690f | -8.96263 | -47.44542 | 2026-07-29 04:32:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6414afe6-af66-3947-99ab-f7be003cfa54 | -9.60876 | -47.76183 | 2026-07-29 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d9e4c0a9-a307-34a2-9615-9568766e7eea | -11.93724 | -43.41668 | 2026-07-29 04:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 25b38b36-82f5-3603-9b2b-84aa5bc83eeb | -7.34479 | -45.83679 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| fe748d9c-181c-341a-856a-b04490651a56 | -6.87656 | -46.00583 | 2026-07-29 04:32:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 335b7335-81d2-3572-8799-ab613bdb30d2 | -5.68764 | -50.09412 | 2026-07-29 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7db0e7ef-d980-36c4-99df-a6c46686ba56 | -6.33539 | -44.60744 | 2026-07-29 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ae889dae-8995-3219-9ab9-4be9b559b681 | -12.1473 | -48.94847 | 2026-07-29 04:32:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5dbfc376-3b1e-32cd-9a17-9a142fa7b6c4 | -11.53335 | -47.5611 | 2026-07-29 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 04e03b6f-7651-3266-bcfa-c86a52a89918 | -6.33596 | -44.60379 | 2026-07-29 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c3f4ad47-f560-39a9-a09a-6a830bae657a | -7.73401 | -44.55579 | 2026-07-29 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| da3c5781-dd8c-389c-b4e9-da7d6df833bb | -10.90286 | -45.215 | 2026-07-29 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 68c63a76-d17c-32b2-a452-ece6d5199e11 | -10.15333 | -46.53075 | 2026-07-29 04:32:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 813c1ef7-c473-3f67-90ea-5704b46274b6 | -10.34865 | -49.74933 | 2026-07-29 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34805d3f-2a79-35c9-b44f-0f82b7bbcd2c | -7.35512 | -45.83446 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 5641ad1f-2065-3d4e-9c1d-74059d7ad926 | -10.47401 | -45.08851 | 2026-07-29 04:32:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 375b436c-a4cc-3d08-acd0-261924bc3fec | -11.51564 | -47.56545 | 2026-07-29 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 997cd09c-edde-39c0-ab8a-afee9746cb17 | -4.94326 | -48.23834 | 2026-07-29 04:32:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef6612f7-2666-3e17-83db-307ef270e531 | -6.87711 | -46.00236 | 2026-07-29 04:32:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2609bf6d-cbe2-3d39-9d4a-382d0786f353 | -11.17811 | -49.93213 | 2026-07-29 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e4b44f25-1b1e-3b55-b66a-b6d93fd2b651 | -7.33483 | -45.85677 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f085daa1-a1ab-3dfe-a193-2ca7d0b82b5a | -11.77537 | -46.57871 | 2026-07-29 04:32:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bd5f33d0-2bab-3241-9f39-50c5b3988818 | -10.13262 | -42.42236 | 2026-07-29 04:32:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e7df13b7-23fc-376e-861a-faf633156648 | -7.89665 | -48.05075 | 2026-07-29 04:32:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc70c485-d9b2-3cdf-b3b0-713f93875b3a | -7.34091 | -45.83977 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 303b547e-a54c-39cc-9a33-1dcc8772bce2 | -6.72607 | -44.36782 | 2026-07-29 04:32:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ec14cbbd-f416-3c33-9eb1-b2ce90d82a13 | -6.84094 | -42.88243 | 2026-07-29 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 016ea909-97c9-3d0c-a285-49ad77849a47 | -12.31476 | -46.75136 | 2026-07-29 04:32:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a2527438-c21e-3833-9a0d-84af09de77ed | -11.60117 | -46.78163 | 2026-07-29 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 915b0c2f-1914-36a5-89bd-46fd58cab84b | -11.53048 | -47.5571 | 2026-07-29 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0efe871a-d95c-36f2-9b57-1eeb7d1ef4ed | -7.34574 | -45.85094 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 29c1e0e1-70c8-343e-a922-729e7d1c79f8 | -7.22618 | -49.59805 | 2026-07-29 04:32:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15ff7c51-1934-378b-9af2-66cb0118588d | -7.34313 | -45.8473 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 956bd3a4-fb76-30ed-b5d5-153623e043e1 | -7.81388 | -46.84728 | 2026-07-29 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 669842ce-6709-344a-8467-c1dd18c8f13e | -6.8738 | -46.00183 | 2026-07-29 04:32:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4594dc66-6e4f-3b50-81bf-a8535247ea8a | -6.99479 | -51.3021 | 2026-07-29 04:32:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 74541818-53fb-3ad7-b6bc-6e6e1513171f | -10.92914 | -43.05998 | 2026-07-29 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| dad347b3-05b4-38bd-bbba-476e3fbfb525 | -6.56806 | -47.86259 | 2026-07-29 04:32:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d403fde0-0c17-3653-9480-7b3cca101797 | -11.52772 | -47.55307 | 2026-07-29 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7ec5d7f-c6df-37c9-9463-71a7ae5f133c | -11.71053 | -47.55774 | 2026-07-29 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de3026e0-aef8-3951-a22f-acfa579b192d | -11.18093 | -49.93663 | 2026-07-29 04:32:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e63e86d1-0dae-38aa-b021-238d3c921162 | -4.94549 | -48.24643 | 2026-07-29 04:32:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 71747cce-5ecd-38ca-9302-de765bde0207 | -7.58946 | -49.55004 | 2026-07-29 04:32:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fce433a-4a40-377f-8a9a-46e6a83601a1 | -5.82311 | -44.74981 | 2026-07-29 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74ce82ad-9521-35f1-a68d-0d3556f23641 | -7.40941 | -43.77167 | 2026-07-29 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6ea00678-4272-360b-8c90-becba1e0c794 | -5.33956 | -45.34721 | 2026-07-29 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ac62279f-a7a1-3353-8d53-70a8989e734e | -6.33879 | -44.60799 | 2026-07-29 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b207e9e0-0b7e-3210-938e-1af553964f02 | -11.55981 | -47.5654 | 2026-07-29 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6bf1f80-cfc9-30c1-ade3-7e1658a31381 | -7.33538 | -45.85327 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f85e8979-ff9a-3d1b-933b-d070fa5eb669 | -6.15719 | -44.65114 | 2026-07-29 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 87447c77-45f8-3efd-9ecc-17c0a30b39b1 | -10.92983 | -43.05508 | 2026-07-29 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1d51d4b4-d80c-33c8-bc76-ad01560e1d4f | -8.96539 | -47.44944 | 2026-07-29 04:32:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6c73fe01-12ca-33a0-8766-e4200d167d82 | -7.33816 | -45.85728 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 592a6671-0e85-3023-a544-4a6ab6bd9295 | -9.33938 | -47.32045 | 2026-07-29 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 79c270f9-2ba4-3b73-a8c8-8ec969b588ff | -7.35954 | -45.82797 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8affebfc-c83c-380b-9872-f100ec3bcb74 | -12.15065 | -48.94903 | 2026-07-29 04:32:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 538629d5-f342-37c3-a5cd-b8b565c04f37 | -10.35213 | -49.74992 | 2026-07-29 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 307474e8-9d87-3c36-bfda-cf12bc223cf1 | -7.35899 | -45.83147 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f8bded4d-288d-3876-a15f-2cf693afec03 | -11.53103 | -47.5536 | 2026-07-29 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8c5c31a3-2eee-38d0-be83-4bc92b61359d | -12.37245 | -43.90249 | 2026-07-29 04:32:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9064f58e-456c-3f68-972c-4d783f5912a8 | -9.20867 | -49.82238 | 2026-07-29 04:32:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9fb26294-6266-33af-81bb-e2bca6281d59 | -10.9453 | -43.05735 | 2026-07-29 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 342d7f5c-a886-3de4-8c60-222cef75c6f9 | -12.45075 | -44.69817 | 2026-07-29 04:32:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 43d94d03-be37-384a-afea-c00d1021e0e5 | -10.93052 | -43.05019 | 2026-07-29 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 69082f89-2d69-3750-b3a6-88b66b329649 | -7.3507 | -45.84095 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 153fe1ab-494a-3fc9-a7c0-79d66910ab9f | -5.83834 | -44.8959 | 2026-07-29 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f021e449-7636-306e-819f-856e82d10ffb | -5.82255 | -44.75346 | 2026-07-29 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6fc19005-e224-3d24-9a03-99b9bd63ef91 | -8.44189 | -51.54731 | 2026-07-29 04:32:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cf2d83e3-9c32-3515-8db7-1b9390f21f99 | -9.3501 | -50.26455 | 2026-07-29 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1565e285-7459-370e-a83d-0e82d8f1d754 | -11.9607 | -43.37707 | 2026-07-29 04:32:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d34863d-26c3-3f4c-9278-f8187820a3df | -10.35342 | -49.74212 | 2026-07-29 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f44e6256-68cd-37b3-a636-199135844209 | -7.34424 | -45.84029 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| cee09c56-502f-3820-9ba7-84215425f5e7 | -11.52667 | -47.56005 | 2026-07-29 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 25a85d5c-1b93-36ea-b8cf-097dc10a701a | -6.07495 | -44.57137 | 2026-07-29 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c1a1aa7-e4a3-31e7-889d-030aeaf4b2b5 | -7.72622 | -47.24952 | 2026-07-29 04:32:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ec1182f7-a86b-3565-be9e-894ef660cafe | -9.08218 | -50.58934 | 2026-07-29 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 569112e2-168a-3644-b241-780fb5af4513 | -11.5423 | -50.29181 | 2026-07-29 04:32:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7b2f4c02-9957-3b2d-a458-42fbaba38084 | -10.93757 | -43.05622 | 2026-07-29 04:32:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 4e07e155-d353-3918-af18-dd560712795b | -7.20058 | -45.49652 | 2026-07-29 04:32:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 653c60f6-b0a7-3c07-ad18-b97a4496388b | -10.348 | -49.75323 | 2026-07-29 04:32:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ac35e567-38ac-36ee-aba9-6c32bcbaccf4 | -12.62471 | -44.62841 | 2026-07-29 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8570ef85-87f2-3622-8106-dad02c488139 | -5.23259 | -56.008 | 2026-07-29 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5c4e1dc-c5b0-3137-8e2e-6616843fd45c | -11.59784 | -46.78111 | 2026-07-29 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 2c1dddd1-1108-3b7a-8a1a-b32a28c71657 | -7.34847 | -45.83342 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| f35b06c8-5218-315b-8f9a-c3a9cd143e38 | -6.15663 | -44.65481 | 2026-07-29 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81c562d2-d3ff-37c6-b421-f79efacc21ea | -11.26601 | -49.55231 | 2026-07-29 04:32:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2045e7fc-c3a7-325c-8dbc-52fcfc4e8624 | -9.08272 | -50.59129 | 2026-07-29 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31eec08c-d303-3bda-b45c-471bca190bf6 | -6.9937 | -51.3029 | 2026-07-29 04:32:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82d42c17-19d7-3594-9cce-bbbc4643fcac | -9.10125 | -50.61054 | 2026-07-29 04:32:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 901d0e20-f696-3cfd-8c9f-6768900dca8a | -7.34629 | -45.84745 | 2026-07-29 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README11.md)
