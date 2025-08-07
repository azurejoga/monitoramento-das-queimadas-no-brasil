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
| 3f4f5f5e-3c2f-3495-a378-d3b6e21be613 | -7.4074 | -60.0108 | 2025-08-07 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 161.3 |
| f015405b-e71f-379b-a7fb-60184a494511 | -8.9041 | -60.5577 | 2025-08-07 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 9f50638c-d858-33c6-84ac-9989ada9ac7a | -10.6445 | -44.7182 | 2025-08-07 00:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 0fbdbcff-0519-3b7c-8d89-083ecd91f71d | -9.0835 | -45.0499 | 2025-08-07 00:50:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 42.5 |
| 70830518-0c66-3aae-89cf-ede6228d3562 | -11.7508 | -48.1825 | 2025-08-07 00:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 124.7 |
| b708a371-55cd-3928-9698-4e5839e9a19e | -8.9042 | -60.5385 | 2025-08-07 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| e2bcfab8-3482-317e-946e-6e2f3d49c735 | -10.6247 | -44.767 | 2025-08-07 00:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 53b7fb81-27d7-389c-8548-9b7f2d29c290 | -8.9215 | -60.7297 | 2025-08-07 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 116.4 |
| 829254c6-1571-39ce-853f-e42c942aab2a | -8.5211 | -43.3063 | 2025-08-07 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 4d3d518d-17b3-3d9a-900f-7fa7a4cf3f0a | -10.625 | -44.7439 | 2025-08-07 00:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 177.2 |
| d6b694b3-9fe5-33ba-b208-fe1f6c889962 | -11.7504 | -48.2046 | 2025-08-07 00:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 56f29190-d275-3811-9742-d5832c085be8 | -8.9212 | -60.7681 | 2025-08-07 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 2081e388-f961-3751-853a-807985ef97d0 | -10.6438 | -44.7645 | 2025-08-07 00:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 118.2 |
| a8ec55d2-dd3b-3742-a649-006593793027 | -10.6254 | -44.7207 | 2025-08-07 00:50:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 7ff99ac4-024a-3b60-9ee7-ba2676480479 | -8.9213 | -60.7489 | 2025-08-07 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 226.8 |
| e30861a8-c264-3da9-bcd8-9e706d27bd82 | -10.6441 | -44.7413 | 2025-08-07 00:50:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 181.6 |
| 6e78cfaf-7320-313c-875e-a5b05c507494 | -7.4076 | -59.9916 | 2025-08-07 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| e589122c-1f3c-3697-b193-09e65f39679e | -11.7699 | -48.18 | 2025-08-07 01:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 51.5 |
| a28eca20-1c9d-3407-935a-beb5f9ff6cff | -10.6438 | -44.7645 | 2025-08-07 01:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 120.4 |
| a9fd8431-b109-3071-b500-f6d3abf02501 | -8.9212 | -60.7681 | 2025-08-07 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 9ecf474d-ac8a-322e-8b71-c9602f73bed5 | -8.5211 | -43.3063 | 2025-08-07 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 4b5e48bf-8e6f-3bac-89ab-3d417d81d6c5 | -8.9042 | -60.5385 | 2025-08-07 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 1af348d6-e954-3ae6-bd62-20e8304c90e1 | -10.625 | -44.7439 | 2025-08-07 01:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 78.4 |
| ca066620-4616-3b27-8d4d-be0b005a03a8 | -8.9399 | -60.7481 | 2025-08-07 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 448a8bc7-c4b2-3e4f-b0fe-ad441a59e0ee | -10.6441 | -44.7413 | 2025-08-07 01:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 168.5 |
| 8875f523-aaba-3a4c-8844-0ef6624ab781 | -8.9041 | -60.5577 | 2025-08-07 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| cce53682-0208-3a00-a5d1-df1ba18705f3 | -11.7508 | -48.1825 | 2025-08-07 01:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 2de1cb5a-fcd7-3180-8eef-1b4823300b17 | -5.822 | -46.2035 | 2025-08-07 01:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 72f97939-6154-3534-bec4-17ed214dce30 | -9.0835 | -45.0499 | 2025-08-07 01:00:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 43.3 |
| b289bc46-3bac-3bd9-9c2a-10f912b4b278 | -7.4074 | -60.0108 | 2025-08-07 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 160.6 |
| 9950b157-34c4-3d14-8c37-c35b64166b8a | -8.9215 | -60.7297 | 2025-08-07 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 107.3 |
| ddb4610f-8334-38b1-a4c3-9a751224c668 | -7.389 | -60.0116 | 2025-08-07 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 61f03928-e6e3-3cf2-afcb-b61800efce4e | -5.8218 | -46.2258 | 2025-08-07 01:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 74.6 |
| 2160916a-db91-3ec6-af48-b8a45b14ff91 | -11.7504 | -48.2046 | 2025-08-07 01:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 0c302e65-b4ab-38f8-9c2d-6cc618cfd58e | -8.9213 | -60.7489 | 2025-08-07 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 217.4 |
| 44eebab5-8fea-3c87-9984-be902b38bc56 | -5.8031 | -46.2271 | 2025-08-07 01:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 1fff492d-1a9b-354d-894b-382ead144baf | -10.6247 | -44.767 | 2025-08-07 01:00:00 | GOES-19 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 42.3 |
| b3e8f6c2-7817-32d9-b4f3-0f63044b4bf6 | -16.71736 | -50.68906 | 2025-08-07 01:05:00 | TERRA_M-M | CACHOEIRA DE GOIÁS | GOIÁS | Brasil | 5204201 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 93bfb8b6-dcc5-3e0f-baf2-08ee4caaaec0 | -22.3463 | -47.21403 | 2025-08-07 01:05:00 | TERRA_M-M | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 2cbfa315-7af0-3cf0-add1-9e6179f0168f | -21.2375 | -49.09461 | 2025-08-07 01:05:00 | TERRA_M-M | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.9 |
| 82705c95-56b2-35fe-ac35-554d25075cdf | -19.84938 | -49.08342 | 2025-08-07 01:05:00 | TERRA_M-M | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 6caaff08-2873-3702-9000-3f31c7da81c7 | -17.20878 | -44.34318 | 2025-08-07 01:05:00 | TERRA_M-M | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 96689208-3e41-39ee-b5f7-a2df5a97e501 | -21.23512 | -49.08044 | 2025-08-07 01:05:00 | TERRA_M-M | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 40.6 |
| 12ee7f92-65d9-32f7-bffc-2b3bc0d7c4e2 | -17.11266 | -49.14854 | 2025-08-07 01:05:00 | TERRA_M-M | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 2474632c-0be3-36c7-91f4-3440ade80e8c | -19.84687 | -49.06856 | 2025-08-07 01:05:00 | TERRA_M-M | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 5a535ad8-2e44-37f6-b2b5-6c9510f4754b | -11.76358 | -48.19564 | 2025-08-07 01:07:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 9e5fc7fc-7798-3e11-8d1b-c4feb0a81984 | -6.91917 | -52.84871 | 2025-08-07 01:07:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 40478e1c-a754-3c84-8a5f-fcaecc5040a6 | -9.93429 | -60.47107 | 2025-08-07 01:07:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 27.3 |
| d77909b6-8f71-360e-89d2-b1c1cfec56b1 | -12.7147 | -47.79087 | 2025-08-07 01:07:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 35.3 |
| d9448c27-059e-3b67-8eaf-fd5f2b1405a3 | -8.91294 | -60.54426 | 2025-08-07 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 5785cabb-b429-3ac5-9de3-23b04a2e29c6 | -11.7536 | -48.17965 | 2025-08-07 01:07:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 7d5e0d71-2802-3392-bb63-291363b8744f | -9.94701 | -60.46358 | 2025-08-07 01:07:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 8e47b8d9-5a6d-3caa-9249-4b2744061f82 | -8.90565 | -60.57327 | 2025-08-07 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 9e9f1a59-b7a1-3bab-b0cd-8090f947352f | -9.93979 | -60.5134 | 2025-08-07 01:07:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| d5ca2c10-f58a-30f9-a68d-5a54280bb137 | -11.74988 | -48.1981 | 2025-08-07 01:07:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 75685eba-979f-35b7-ae2b-65b645fbaa4f | -9.94525 | -60.46969 | 2025-08-07 01:07:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 18.9 |
| bd31b262-e8cc-373d-b1a8-211da272b0b9 | -9.93796 | -60.49928 | 2025-08-07 01:07:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 9ee8cb12-8e77-3a1a-a4fa-e144ae400cb6 | -13.05683 | -56.85169 | 2025-08-07 01:07:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e92fb74d-c00e-34dc-899b-7b4d67540509 | -8.91651 | -60.57181 | 2025-08-07 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 7d476e9c-bdbf-3a71-8673-bfc1f481c5ec | -9.93952 | -60.49324 | 2025-08-07 01:07:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 19.8 |
| 96ba520b-9490-37a6-875a-e6cc3ab660bc | -8.92903 | -60.75526 | 2025-08-07 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 482a0366-81bc-3ade-bba8-1731dabfb537 | -13.73015 | -53.86455 | 2025-08-07 01:07:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 52ef94a7-61ac-375e-a3a6-633b12a7efb9 | -9.46629 | -57.84907 | 2025-08-07 01:07:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| abb8e036-43f8-3da8-815a-1dc125c772d8 | -8.9272 | -60.74099 | 2025-08-07 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 135.1 |
| 7b56c638-1a4c-309b-894f-b58921ce6384 | -11.75749 | -48.20347 | 2025-08-07 01:07:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 100.6 |
| cf15a93e-f6de-3507-a035-c400f4f5bc7a | -9.70684 | -61.29732 | 2025-08-07 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 861afc70-ab2d-3857-ba3c-7376f3ca9d54 | -8.92007 | -60.59929 | 2025-08-07 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| e0498e32-3232-3758-847d-278e08b2b09e | -8.91472 | -60.55801 | 2025-08-07 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 21.7 |
| e2701369-d514-305b-a78a-ff9a60c5c0df | -8.91982 | -60.7709 | 2025-08-07 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 4bc2c50e-b31a-31ac-a6b1-743a73309eba | -9.93606 | -60.465 | 2025-08-07 01:07:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 50c8d15d-5242-37b1-b614-f95e1aa136d6 | -8.90918 | -60.6007 | 2025-08-07 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 018664df-0a4c-38b5-a594-079a93355c50 | -11.78104 | -47.40226 | 2025-08-07 01:07:00 | TERRA_M-M | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 461b8fc5-c0f5-31a3-9ae0-26ddf59408db | -8.92556 | -60.55656 | 2025-08-07 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f3bb949d-7c4f-3f46-a9fa-b6ba4b120cd7 | -11.75956 | -48.17205 | 2025-08-07 01:07:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 76e8ce82-158d-3c4e-b917-8fdf97767512 | -9.94126 | -60.50739 | 2025-08-07 01:07:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 9a48981c-6057-357a-88b8-d67ef39704b2 | -8.90741 | -60.58698 | 2025-08-07 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 064b3c63-3e6f-3aef-8329-e2204348d9b7 | -8.9021 | -60.54572 | 2025-08-07 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 27.6 |
| dfee37ea-0806-3d21-8cef-de1b00fb89c0 | -12.33052 | -46.05326 | 2025-08-07 01:07:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 41.6 |
| c838a065-3e48-3df3-97c9-e9f948a24ead | -8.91829 | -60.58556 | 2025-08-07 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 20.8 |
| a926f3fc-5182-3055-ad25-6d324321a393 | -9.11031 | -48.91028 | 2025-08-07 01:07:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 09444cc1-6f52-3893-8e0e-5fa4689c12f1 | -12.71964 | -47.78455 | 2025-08-07 01:07:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| c2acf235-152e-346c-90dd-b00794d4f2ed | -11.78866 | -47.54639 | 2025-08-07 01:07:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 46.1 |
| d3201c4b-3b74-3fd5-8a6c-a1816330a1be | -13.05809 | -56.86129 | 2025-08-07 01:07:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4aada6dd-3fb1-3fae-a77d-b459f7f9c97a | -9.93247 | -60.45699 | 2025-08-07 01:07:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| d3cc623d-77e6-33b7-a9d8-b1997208e879 | -11.74581 | -48.17437 | 2025-08-07 01:07:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 0d0c9985-8287-3e0e-9e9a-6cdee9079fcc | -8.91801 | -60.75666 | 2025-08-07 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 158.4 |
| c83257dd-10c7-3787-8cb9-f0d6a00a1d0a | -6.44593 | -46.12922 | 2025-08-07 01:07:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 1c254309-a16b-328f-9910-4279f8a969c5 | -9.70883 | -61.31345 | 2025-08-07 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 4e7e4350-fe3d-3f1f-9dfe-1a8ca867b989 | -8.90387 | -60.55947 | 2025-08-07 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 08117709-52dc-3fa5-af66-f9614eebf905 | -8.92538 | -60.72676 | 2025-08-07 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 19c95d0b-051c-3751-9c19-5dd730c65110 | -8.91619 | -60.74244 | 2025-08-07 01:07:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 127.1 |
| 109c984e-48ce-34d1-9c78-68306125b073 | -13.7211 | -53.86595 | 2025-08-07 01:07:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 20ea5889-4e4b-36b8-b73b-c30996012c52 | -6.53538 | -56.21063 | 2025-08-07 01:09:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 562d50cf-f68d-343c-a486-f6fa560c3f73 | -6.41203 | -53.37021 | 2025-08-07 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 5b9bd50d-feea-3217-a16b-eb3dc200505e | -7.4047 | -60.01534 | 2025-08-07 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 167.1 |
| 6a25cf91-8542-37ee-9d0a-349b18acae71 | -7.40316 | -60.00333 | 2025-08-07 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 139.3 |
| d30c0cff-29cc-3e03-bfc8-458ab03750ce | -6.76269 | -59.48513 | 2025-08-07 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4aa90b00-a368-3f27-9d45-9b764c0edc26 | -7.41487 | -60.01384 | 2025-08-07 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 7be7e468-ecc4-36d5-9377-27f5a89b07e5 | -7.41333 | -60.0019 | 2025-08-07 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| fdf06c5f-65f6-3ac0-a73e-e8ee7fa5cdd7 | -5.80781 | -59.22593 | 2025-08-07 01:09:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |


[Clique aqui para ver as próximas entradas](README3.md)
