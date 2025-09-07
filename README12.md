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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 28c9f9ae-1a31-3dac-8183-05cb390ee070 | -22.413099 | -47.436901 | 2025-09-07 00:45:00 | METOP-C | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 03c55413-4416-3f56-aba4-ca1509336fbe | -11.4601 | -55.556999 | 2025-09-07 00:45:00 | METOP-C | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 039e5e8b-744d-3788-88c7-922e9144008d | -7.6604 | -50.304699 | 2025-09-07 00:45:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc349da6-bef9-3972-aed5-b1546bd4bebe | -7.7381 | -48.8312 | 2025-09-07 00:45:00 | METOP-C | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 257d909f-dcf9-3a85-a87e-cb7f54305f98 | -8.3342 | -48.281898 | 2025-09-07 00:45:00 | METOP-C | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f858530a-09ac-3ea4-a6aa-b92fba257774 | -15.7101 | -53.551498 | 2025-09-07 00:45:00 | METOP-C | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1e20c282-e54b-315d-abb7-bc15472b848c | -9.9677 | -51.667198 | 2025-09-07 00:45:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 98b15235-f626-37a5-beff-aaf8d128db12 | -6.1303 | -44.2635 | 2025-09-07 00:45:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6e8631ac-bb8c-37d7-99ef-8d9f12551b95 | -7.6784 | -50.293301 | 2025-09-07 00:45:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47398e38-1907-3da8-93e2-eafba029025a | -12.7717 | -52.962601 | 2025-09-07 00:45:00 | METOP-C | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8ccade7e-1a26-35b3-be6c-d201c7d5fb51 | -11.5784 | -47.179199 | 2025-09-07 00:45:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 03c5b156-7f01-3aaa-884e-7fd18d0cba3f | -6.2206 | -43.311798 | 2025-09-07 00:45:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f110ab35-ea47-324a-8105-3490f8028593 | -21.695601 | -44.516701 | 2025-09-07 00:45:00 | METOP-C | SÃO VICENTE DE MINAS | MINAS GERAIS | Brasil | 3165305 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 996cfce7-e2c5-36f1-8f4d-e35b1993b46f | -17.362801 | -42.657101 | 2025-09-07 00:45:00 | METOP-C | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e28df8f0-9efe-392f-a725-c72828cbc6d2 | -9.9739 | -51.648499 | 2025-09-07 00:45:00 | METOP-C | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8b6d4ba4-0c56-31aa-ac02-2a1858a553c6 | -10.1439 | -48.756199 | 2025-09-07 00:45:00 | METOP-C | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 84a2b0e3-5846-3180-abea-30120c2b1abc | -2.8397 | -49.509399 | 2025-09-07 00:45:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08b062a7-47f7-30e0-944f-b815f39c179f | -6.2342 | -43.2826 | 2025-09-07 00:45:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bed49214-25ea-3db2-b572-dff4acf5f5b9 | -5.7301 | -43.927799 | 2025-09-07 00:45:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e692e22-f7f7-3705-a8c6-fae3bf5eedb0 | -8.4749 | -45.176498 | 2025-09-07 00:45:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8fec255e-e650-304b-a9e5-3febd48e9c14 | -8.1063 | -45.319698 | 2025-09-07 00:45:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 420dcc81-19d9-3238-986d-79e999d54cce | -20.065399 | -41.712101 | 2025-09-07 00:45:00 | METOP-C | CHALÉ | MINAS GERAIS | Brasil | 3116001 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3e6d6bd5-c1dd-369c-a87d-7d7dbecf8ec0 | -10.5751 | -48.476002 | 2025-09-07 00:45:00 | METOP-C | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 95a1b14a-1361-3234-bd0e-f0395f6608d5 | -5.8721 | -45.083 | 2025-09-07 00:45:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 22f6dee0-a1ad-35f7-b4af-071e876832dd | -6.2371 | -43.294899 | 2025-09-07 00:45:00 | METOP-C | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5ee5db8d-1d95-3f10-a463-c6c367125906 | -14.7401 | -47.521999 | 2025-09-07 00:45:00 | METOP-C | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| afafda2b-adcd-36e8-941f-09aaef0b12e9 | -18.014099 | -44.908501 | 2025-09-07 00:45:00 | METOP-C | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 6747d797-7ecd-31ce-8cf6-7ae87a594f48 | -11.859 | -50.735298 | 2025-09-07 00:45:00 | METOP-C | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 77498c7b-57dd-3a7d-817b-113ffa750f8f | -4.2559 | -48.180401 | 2025-09-07 00:45:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d84f2f5-40df-34c4-9d9e-c4fd804a2fc2 | -7.6228 | -46.551601 | 2025-09-07 00:45:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 640c1a48-8d0d-3a2a-b104-87f60b9e302e | -6.8314 | -52.811199 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 184d0fd0-1b9b-3162-8a6d-27a863f7960d | -16.9146 | -45.784599 | 2025-09-07 00:45:00 | METOP-C | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4867c708-e291-385c-b6f3-a22fdbee53ea | -6.1498 | -44.2589 | 2025-09-07 00:45:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d8bb2f0f-52a7-3523-be43-e11794d6bf87 | -8.613 | -54.645599 | 2025-09-07 00:45:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5b7eb31-c3df-37b0-bf60-9f527be6116a | -8.6792 | -54.6689 | 2025-09-07 00:45:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a41f5cd-915d-3695-a94c-491aa285895d | -11.4057 | -43.6152 | 2025-09-07 00:45:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a3c190cb-7137-32d6-88e7-ef8d031d0204 | -5.0211 | -45.322201 | 2025-09-07 00:45:00 | METOP-C | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b24d752d-b54d-399b-8c21-289ebab80de5 | -6.8743 | -45.6101 | 2025-09-07 00:45:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2fac2ab8-ee56-317f-95b5-1a09cd2021b9 | -15.1125 | -48.0835 | 2025-09-07 00:45:00 | METOP-C | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c0eded5b-66f5-30f3-b8c4-b906fa12576a | -13.9086 | -48.0411 | 2025-09-07 00:45:00 | METOP-C | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| fa89bf9e-cb21-368b-b215-76af5c6dd215 | -2.9067 | -48.680901 | 2025-09-07 00:45:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d7e73be-cc97-3e24-91f3-70f1b0954417 | -18.973301 | -44.233299 | 2025-09-07 00:45:00 | METOP-C | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 32f2feb7-e7ba-394a-98b5-7fe628b75940 | -6.7706 | -52.8153 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddf70ea6-835b-3af7-b561-269cccb909ce | -6.8702 | -45.592701 | 2025-09-07 00:45:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| afc13cb6-2f73-3307-80a7-011f592c3bc1 | -16.930799 | -45.765301 | 2025-09-07 00:45:00 | METOP-C | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 51c9952b-8a5c-3a7e-8fc3-55c876457f6b | -15.1735 | -47.987 | 2025-09-07 00:45:00 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d84c7154-bd65-371c-98a7-f88e7d724fb5 | -22.416401 | -47.452599 | 2025-09-07 00:45:00 | METOP-C | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 6eafd328-8f29-38a8-89a7-89fab7f7d2c7 | -5.9356 | -46.1805 | 2025-09-07 00:45:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a162a698-e374-364e-acd6-9163d7ba48d6 | -13.7258 | -46.9137 | 2025-09-07 00:45:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 329a63d1-8126-3fb7-9493-b6a969fb460e | -10.7791 | -47.742401 | 2025-09-07 00:45:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 14a4c61e-8f62-388c-b2a2-80eaca60b127 | -11.1966 | -55.011398 | 2025-09-07 00:45:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 23a2b9ec-ca75-3d64-92ac-c7330f5562a7 | -13.1778 | -44.485298 | 2025-09-07 00:45:00 | METOP-C | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 88f4bf99-7159-3f3f-be73-1bdd3e7db4ee | -11.711 | -45.7089 | 2025-09-07 00:45:00 | METOP-C | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 43b5779e-76fe-3505-bdb9-2a2db0a2e057 | -7.6606 | -50.260101 | 2025-09-07 00:45:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f0a3a29-99e2-39c7-970c-736b19119673 | -13.8271 | -46.277199 | 2025-09-07 00:45:00 | METOP-C | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 921b3012-fab1-395f-a35c-285bab579b90 | -6.8723 | -45.601398 | 2025-09-07 00:45:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a9a51561-3b76-3470-a7d8-29db2dc7f1f5 | -6.8312 | -52.8568 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b23db30-4e2e-36ac-a2dd-4a063fc6cb7b | -13.6439 | -47.9174 | 2025-09-07 00:45:00 | METOP-C | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 38d8f64a-02f6-3abc-a896-7b4ce079ab9b | -15.9791 | -42.383801 | 2025-09-07 00:45:00 | METOP-C | NOVORIZONTE | MINAS GERAIS | Brasil | 3145372 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1f5125ab-ce54-382c-90d5-47468703c175 | -11.5865 | -47.1698 | 2025-09-07 00:45:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b154e061-6176-3dd4-acf9-fd7a5e8d632c | -5.4018 | -44.840302 | 2025-09-07 00:45:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2a3c51f3-568b-3272-bc3b-37a4bc14cfcf | -13.0037 | -45.2309 | 2025-09-07 00:45:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ba21873e-18b2-3c4a-aaa6-33056ec3851e | -11.8341 | -50.526699 | 2025-09-07 00:45:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f82a807b-2085-343a-9770-bfe72fddf486 | -11.391 | -43.639801 | 2025-09-07 00:45:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8e35c4c2-ff2f-391a-a25e-5237347cd211 | -11.1431 | -48.3899 | 2025-09-07 00:45:00 | METOP-C | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 41522ef7-ba39-39a8-ae37-c046fa834fe6 | -13.0119 | -48.085499 | 2025-09-07 00:45:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 51b20d75-51de-385b-be70-67fe81ac0dec | -17.542999 | -44.397499 | 2025-09-07 00:45:00 | METOP-C | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 07143272-cd40-3438-9d31-0d07274b40c3 | -16.272301 | -45.686298 | 2025-09-07 00:45:00 | METOP-C | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7ca954b3-eeee-3b86-ba98-2ba13f40a389 | -11.5718 | -47.735401 | 2025-09-07 00:45:00 | METOP-C | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c313d7f9-ecb0-38f9-92a9-90ad59273f96 | -7.7441 | -50.722698 | 2025-09-07 00:45:00 | METOP-C | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30eaa465-a596-3a02-a93f-d81e465506c9 | -13.8433 | -46.2579 | 2025-09-07 00:45:00 | METOP-C | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e854ce90-aee7-34dc-bcf5-e13d442d4319 | -5.8201 | -44.130901 | 2025-09-07 00:45:00 | METOP-C | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 869e8d38-6adc-3a29-b561-0b0c55c115e8 | -8.6592 | -50.0299 | 2025-09-07 00:45:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8472d844-3b06-334a-977f-3ea41f8be8a4 | -5.6879 | -49.200699 | 2025-09-07 00:45:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 341fb5ec-d861-3b79-b4f1-253b1473b005 | -19.538799 | -41.556801 | 2025-09-07 00:45:00 | METOP-C | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 967dbf68-d222-3dc1-841d-79324e6ccf13 | -14.8152 | -48.181999 | 2025-09-07 00:45:00 | METOP-C | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b469286f-9b7a-3fbe-9e67-65062f55b250 | -10.7987 | -47.7379 | 2025-09-07 00:45:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ab97fcdc-8ba1-32d4-9252-be30094ba88d | -17.004801 | -49.180401 | 2025-09-07 00:45:00 | METOP-C | HIDROLÂNDIA | GOIÁS | Brasil | 5209705 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c24696cc-7666-3832-bc22-382a98c4f351 | -10.7372 | -48.191101 | 2025-09-07 00:45:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 511213dc-50f6-3b6d-bdbd-c50d5d1ecf3f | -16.274 | -45.693699 | 2025-09-07 00:45:00 | METOP-C | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f9aa1d4c-1181-3536-8c5c-8d4135728dfc | -11.4032 | -43.605301 | 2025-09-07 00:45:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 52cb3ab4-c53e-3b53-80c0-5b09abec6a8e | -10.3802 | -44.978001 | 2025-09-07 00:45:00 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 43e72de3-68bf-369f-b8e0-2f96eb8d5375 | -17.358101 | -42.6381 | 2025-09-07 00:45:00 | METOP-C | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9536740c-8fcf-3d8f-855a-6423a3f1b789 | -5.7036 | -43.946098 | 2025-09-07 00:45:00 | METOP-C | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| de75b570-3950-3f60-be64-0e893077c1c2 | -17.681999 | -43.5457 | 2025-09-07 00:45:00 | METOP-C | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 366a707d-b342-3796-b688-e216fd04e7e2 | -13.907 | -48.034 | 2025-09-07 00:45:00 | METOP-C | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 812e29b1-9fb8-3627-8133-d4ef3e01b2b5 | -3.24 | -50.805599 | 2025-09-07 00:45:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74c8aca8-54dc-39f0-9268-5980d1cd2a0b | -13.0154 | -48.055199 | 2025-09-07 00:45:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 59fc4bb7-3c9b-3042-b238-130b9fe2b8f4 | -9.8058 | -46.835602 | 2025-09-07 00:45:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 019842bc-f702-3e3e-b215-f3ca228ce06d | -17.2096 | -46.722301 | 2025-09-07 00:45:00 | METOP-C | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 95acb161-605e-3dd3-8bac-fc3a0865ff15 | -11.4129 | -43.644901 | 2025-09-07 00:45:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8b8b1ade-4556-3386-9a8e-ccba45dcfbfb | -6.5844 | -44.007198 | 2025-09-07 00:45:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d9e5ac51-0353-35fb-b76d-a8bd7614346f | -18.629101 | -43.262699 | 2025-09-07 00:45:00 | METOP-C | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| af0d2c42-69a4-3590-84c2-7398555eccd9 | -5.8581 | -45.633499 | 2025-09-07 00:45:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5cb59d99-3c01-3153-a433-0588f9156541 | -21.685301 | -47.195301 | 2025-09-07 00:45:00 | METOP-C | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8aea26f2-a684-3586-adee-3f932ee807d8 | -15.1704 | -47.972698 | 2025-09-07 00:45:00 | METOP-C | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 1eb4f111-30b8-3086-89d2-08eaec6773da | -4.2483 | -48.5494 | 2025-09-07 00:45:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 273b76c1-ac75-362b-917f-99269988c08a | -7.7174 | -50.329201 | 2025-09-07 00:45:00 | METOP-C | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 359af5e2-7ef6-3cab-8865-9477d469ce61 | -6.2837 | -51.415901 | 2025-09-07 00:45:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b7a7437-45f6-3fca-ae49-e8c5fd3c4050 | -11.4056 | -43.657101 | 2025-09-07 00:45:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README13.md)
