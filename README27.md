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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 672a4124-fe78-358b-9e1c-83046ca34738 | -8.3664 | -46.19849 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e103ba55-9e28-3f4a-b95b-54ba9825fd15 | -13.71042 | -47.7146 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 005cf492-f155-3052-bfea-32149413ec7a | -11.48491 | -44.02471 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97f75cc5-06dc-3e85-8ed1-cb78700e59ea | -7.12028 | -44.72919 | 2025-10-18 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b9274d2e-255a-36a3-aeee-3fd17acd3c2e | -10.90641 | -47.91183 | 2025-10-18 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90483021-c94c-3968-81f3-6e5b6703252b | -13.04204 | -48.19042 | 2025-10-18 04:02:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d7e4b556-71bd-3119-8191-3c0c10b201b8 | -10.62473 | -45.23301 | 2025-10-18 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97ff32ce-9b4e-3b79-8211-d218cfbab57a | -10.95508 | -49.76925 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 34410120-f412-33cc-b2bb-78bebbe8ee7f | -10.23819 | -44.05659 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 34884521-6957-32f3-814b-97d723f39cb3 | -10.25108 | -44.0534 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1470c86-dcfc-3953-8496-6ff3e06c0e79 | -10.63623 | -45.23505 | 2025-10-18 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c5b9a6c5-c267-3b8e-916f-e2f4fb3c8422 | -12.9879 | -48.45584 | 2025-10-18 04:02:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2be7a8d5-5f9f-3d77-9558-3a407c167040 | -11.67983 | -43.90181 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 517575b1-95b4-389e-a7f4-55b94ff46ee7 | -13.92702 | -46.52853 | 2025-10-18 04:02:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce6c8c44-8954-3e8f-9038-a42b1296e8f3 | -11.34583 | -44.24634 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4f39ae9-f346-3db2-bff1-26a3a794dc98 | -8.22788 | -39.03606 | 2025-10-18 04:02:00 | NOAA-21 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f7e7c860-7af0-3c3e-bd4f-b1971c0e290c | -13.48026 | -47.95501 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 470d29ea-fd93-366b-baf1-6d20d6f158fd | -8.33846 | -49.96807 | 2025-10-18 04:02:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41d91b36-88be-3f50-bea5-0b0c591b52f9 | -6.95245 | -44.86878 | 2025-10-18 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1a59f2c5-31fd-3915-ba62-3f97303d19d8 | -10.43087 | -44.91201 | 2025-10-18 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 733e827e-1526-3969-8929-87531320b04c | -13.03423 | -49.23239 | 2025-10-18 04:02:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fc1c2e8b-5260-31ba-93c4-13ec253f7be9 | -6.96055 | -47.1221 | 2025-10-18 04:02:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 45b46b6b-28b0-3d5a-9d04-1a1785d97fe5 | -8.29844 | -43.39229 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 71ec3a54-bfcb-3fc0-af8a-ba67b8f78abb | -10.57731 | -47.40385 | 2025-10-18 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 692235da-4632-3e0a-ba0e-9a54d3dc1e49 | -7.16248 | -42.37313 | 2025-10-18 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 29ba83ef-9936-3c2c-a55a-efae9ac54771 | -8.86019 | -46.01071 | 2025-10-18 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1954f6a1-0c32-3caf-a10a-b8f3d03899cd | -11.94297 | -44.24357 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e7e29222-9903-3904-9781-f7bc3df0c3a4 | -13.42481 | -48.08582 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8eb31e6-e0a7-3722-8f0c-4dde5a4c39e8 | -13.46417 | -43.76233 | 2025-10-18 04:02:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8e7eb560-4f74-3915-9c62-bba31dbb3201 | -8.29658 | -43.38895 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 288822ae-74a0-3409-be05-859980ac9cae | -10.48984 | -43.4124 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 03e9a6fc-7fd5-3d85-9a9b-c5aff2e0ca01 | -12.72946 | -43.01276 | 2025-10-18 04:02:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f30daa4a-d8cd-3408-8380-309b10784ca1 | -10.25252 | -44.06675 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b34402d-0cfb-3de6-889a-045fb7251696 | -8.75227 | -48.59673 | 2025-10-18 04:02:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8d2f704d-c098-34e2-86d5-1ba9c1147620 | -7.36304 | -44.23456 | 2025-10-18 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 03067a70-2282-3996-9d56-e1077437b826 | -10.24825 | -44.04054 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9d517559-db7a-3be2-88fe-67ea89f74474 | -10.23669 | -44.04313 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ea10a158-8938-379c-ad2e-d2bd63859add | -6.942 | -43.69001 | 2025-10-18 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 532306ba-9e77-3075-9533-a34bcce74a77 | -11.09632 | -44.70151 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1691e4f5-7e8b-36c6-881a-f463bc2b2eac | -8.92068 | -47.96274 | 2025-10-18 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd7c8622-2096-364f-bcff-630206e97e6d | -13.76262 | -43.11776 | 2025-10-18 04:02:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6e14f2d2-045a-32bc-94eb-5d364a579c6a | -13.41654 | -47.98278 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc0f4727-ce25-3a1a-9c61-0ce132aab687 | -6.93831 | -43.68941 | 2025-10-18 04:02:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 037bcd0f-4c65-3bff-9faf-14b090fc6760 | -7.20474 | -45.06881 | 2025-10-18 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c363bde6-6279-311a-80cf-22d788008008 | -11.20779 | -47.83564 | 2025-10-18 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 64f80a77-bd0e-3f52-a89a-7e2772940ad9 | -7.21243 | -44.99834 | 2025-10-18 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 556c5a0b-c830-3b82-912b-3b279cc78b3b | -10.29792 | -44.03975 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1657138d-d1a1-35fa-bb37-1dcb0a879f62 | -13.89789 | -42.50988 | 2025-10-18 04:02:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f6fcabbe-d9f7-37e9-8ab8-9ccbcd7a7893 | -14.09172 | -42.9134 | 2025-10-18 04:02:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 05483ede-3781-344f-bfd6-3a4ec595f5b1 | -10.23096 | -44.05536 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6a5fc557-ea8f-3f10-9299-70e7d54e1283 | -8.30779 | -43.40233 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 40ae2f39-e9dc-3dcb-9329-3e6595f36f6c | -6.58732 | -47.07337 | 2025-10-18 04:02:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 63da80ff-2d81-3d21-86be-aef8a035440d | -13.77898 | -48.23499 | 2025-10-18 04:02:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 108f5625-643d-3173-a54c-5272d4d407f4 | -10.92625 | -47.55873 | 2025-10-18 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 13141577-05a4-3d74-8d93-477566283660 | -9.09235 | -47.82851 | 2025-10-18 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e4af94f-ddf5-3cfa-8f1e-c225af305a12 | -9.22319 | -48.58777 | 2025-10-18 04:02:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6f15cf30-9850-34d0-977d-127b83852898 | -8.11581 | -41.21634 | 2025-10-18 04:02:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0d2e6da1-3edc-3bda-a3cf-7eb57094b34a | -11.37329 | -44.28146 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66575b3e-9d04-334c-aba0-a7499555dc30 | -7.98978 | -44.16063 | 2025-10-18 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 48610f41-8d8c-3ad4-928c-96ccde1a377c | -7.67357 | -44.62997 | 2025-10-18 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c104ab10-3da1-31b6-82eb-acf148a5326e | -10.51694 | -43.40052 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db207a63-914e-33ac-9b8f-277467a07fa8 | -12.7997 | -48.65504 | 2025-10-18 04:02:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73eb4d25-5b1b-3c85-8be9-5146306667ea | -10.98268 | -44.32775 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6bee0076-7156-3184-9636-ee63b439e65d | -8.20936 | -43.96806 | 2025-10-18 04:02:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d40caf7-7852-3e77-bf9d-8ca7d6994a51 | -13.11889 | -48.09713 | 2025-10-18 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a273a5ef-1186-3bdd-bc19-9be863403895 | -12.78593 | -48.626 | 2025-10-18 04:02:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbf12f2c-0748-39b6-aa04-63fad2c3f846 | -8.53734 | -49.60146 | 2025-10-18 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3cb2083-9cb0-30fc-ae15-d4fd63c68f10 | -7.76372 | -42.48428 | 2025-10-18 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e5905ec5-2785-37ef-873e-eb834601fcc5 | -11.64884 | -47.8529 | 2025-10-18 04:02:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5c760c17-f7f9-3e66-8149-8ac424301846 | -8.35946 | -46.21391 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e04b89a7-5d60-3cbd-bdac-ff5f27875a51 | -8.39117 | -46.23044 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 4ef79c8a-c2df-3ff6-8936-54c47a740c1f | -7.24897 | -46.25377 | 2025-10-18 04:02:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3630305-f3d1-34a2-8c3b-03aca1693c25 | -13.03473 | -46.94678 | 2025-10-18 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 43ba0b9e-b2c7-3bed-b3bf-6656a58a15d6 | -13.45376 | -47.92738 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 45543638-72cf-33c7-93e8-10c7dd80f44e | -11.36334 | -45.26057 | 2025-10-18 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 82835932-d13b-36e1-b67c-93081ff6afe3 | -10.8282 | -43.93074 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b54fd377-0440-3d65-b1f2-1a3857376460 | -10.8389 | -44.39871 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a1b83eb3-bd74-38f6-b859-707157eb48c5 | -11.20943 | -47.82644 | 2025-10-18 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8cd270fc-d559-3988-9885-dbc557eb439b | -13.3576 | -43.21342 | 2025-10-18 04:02:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 0e4a6ea5-7c46-38ea-8f8a-f2bc7a459fdb | -10.236 | -44.04733 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6c3fd64e-697e-325c-a456-a0b282b3187f | -7.45619 | -42.16761 | 2025-10-18 04:02:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 50585f79-9a8f-32e9-9fad-f317d6685474 | -11.64355 | -47.85666 | 2025-10-18 04:02:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6e903528-f5a2-3acd-8492-2bed3915b829 | -12.17762 | -45.07932 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 62b77113-b819-3675-bea2-cc11286bd278 | -10.12385 | -44.54033 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4d38e82c-32da-3c41-a447-3abdb9971b52 | -8.36308 | -46.2443 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea9a82e2-c14c-3e79-88c2-08b987ba3c03 | -8.45064 | -44.1696 | 2025-10-18 04:02:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 38d47336-f0c0-3941-8c86-5ba1ff1465af | -10.51562 | -43.40853 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 380e0822-e078-38f7-aaa5-c997ad9e0797 | -14.09719 | -43.63231 | 2025-10-18 04:02:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| fe18c29c-fd6b-3603-b1e7-84a53730c9a5 | -8.30202 | -43.39286 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 394ac9bd-93e7-3cb6-a63e-33239916cd1c | -10.51979 | -43.40504 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 58a92580-8d36-3d13-91e1-096435036398 | -10.25895 | -44.02887 | 2025-10-18 04:02:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8fb7fc3f-dcef-353f-b69a-36e6e2b16030 | -10.62178 | -48.02227 | 2025-10-18 04:02:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b21babd-ef28-39bf-ac06-6b8f4bf52710 | -8.35881 | -46.21775 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e925a592-ddf6-378c-8404-0c49b56bd612 | -12.63197 | -44.22752 | 2025-10-18 04:02:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5cef8fb2-2da4-3a56-a622-79dacd3d86f0 | -12.91619 | -48.58731 | 2025-10-18 04:02:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9015f119-c6bc-3ca5-9b05-445e2d198bea | -10.24599 | -44.03176 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bf7e4a8c-6f50-3b17-a725-097f4234221c | -10.53612 | -43.37122 | 2025-10-18 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 75c1638f-413f-3c90-9d90-33133aaabdba | -10.92706 | -47.55418 | 2025-10-18 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e53f7c09-ceb7-3f5f-aeae-150cfff4e9ce | -13.46291 | -43.7653 | 2025-10-18 04:02:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fccaaea4-37a9-3479-a8c5-6e84b931be06 | -13.62068 | -43.96338 | 2025-10-18 04:02:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README28.md)
