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
| 46369c6a-45be-3c70-bd4e-2b1de94114e1 | -6.6975 | -55.429 | 2026-09-01 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| ef63ff93-68d9-39da-b145-8fdef9babfb5 | -6.6976 | -55.4091 | 2026-09-01 00:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 281.5 |
| 54724c90-333b-37a1-b6c8-b0593b1dc621 | -17.3713 | -42.3794 | 2026-09-01 00:50:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 37b7326e-142e-30fb-9579-31a73488ca8b | -15.7841 | -51.0874 | 2026-09-01 00:50:00 | GOES-19 | SANTA FÉ DE GOIÁS | GOIÁS | Brasil | 5219258 | 52 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 4d4b9c33-0525-3902-bf6a-e6739658123f | -7.3488 | -60.5691 | 2026-09-01 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| a92e2527-4e39-370d-a08b-b86d69b09a50 | -7.2005 | -60.6897 | 2026-09-01 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| ebe705b9-86fb-3249-9897-a130c126bec4 | -3.0425 | -39.9355 | 2026-09-01 00:50:00 | GOES-19 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 47.3 |
| 700c6084-686c-336c-bc0f-600b51185720 | -14.1266 | -52.7895 | 2026-09-01 00:50:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 55.8 |
| bb32b1fe-f13b-3d63-a454-a0c40a80212e | -7.2005 | -60.6897 | 2026-09-01 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 320096ea-7b26-3ae4-95d7-e9c18371b88c | -18.5089 | -50.8974 | 2026-09-01 01:00:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 133.6 |
| 257fb5ae-6643-354d-bb2b-9534cc52a6c5 | -6.9551 | -55.655 | 2026-09-01 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| d4037ec8-1bec-3f8b-9003-f190d3b2b2a1 | -17.3713 | -42.3794 | 2026-09-01 01:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 23848dc9-c713-3a19-9f37-523c4a25812d | -19.2147 | -57.3483 | 2026-09-01 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 69.5 |
| a5377889-f159-3da2-8a3e-4af38965b7e9 | -6.1844 | -57.7395 | 2026-09-01 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 09343dbb-0b50-3721-8ddd-281fb12431b5 | -7.5894 | -60.4827 | 2026-09-01 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.9 |
| a2072742-0706-308c-86f6-f9b66d48e37a | -17.3921 | -42.3495 | 2026-09-01 01:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 303.5 |
| dc1faed3-605d-3b23-9adf-d9ad94a3ebd8 | -14.4587 | -52.5151 | 2026-09-01 01:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 02c64b01-df80-3809-8e84-60e703bd6001 | -19.1951 | -57.3301 | 2026-09-01 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.5 |
| ff5f355a-403e-36fc-a733-c1ed62e9e08d | -6.6035 | -58.6166 | 2026-09-01 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 9879e3b6-6d72-3dfc-8413-5dd00f84e266 | -10.036 | -44.7056 | 2026-09-01 01:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 109.2 |
| ca5f2b7e-262e-3df4-ab32-51851ae62cf4 | -6.7162 | -55.4082 | 2026-09-01 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 0b540aa1-1930-3002-b489-1b7e1a4e86a7 | -19.8853 | -48.0932 | 2026-09-01 01:00:00 | GOES-19 | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 19a1d7d4-b5e1-3922-985f-1365807b4f5a | -10.017 | -44.708 | 2026-09-01 01:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 1f82c690-c4d4-325f-9b44-02d9b517a9c2 | -6.6975 | -55.429 | 2026-09-01 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 55bcd63d-6b5c-3a75-a1b8-1af743b53f9a | -7.5524 | -60.4843 | 2026-09-01 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.0 |
| d72dc0b0-ce58-36a8-978b-a8fe63f6dac6 | -16.4773 | -47.9381 | 2026-09-01 01:00:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 84.9 |
| eff9f65b-80cc-33c8-b0b7-985149a4ab4e | -7.5526 | -60.4651 | 2026-09-01 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 602c26cb-fe98-3e31-b904-16cd0b185bdd | -7.571 | -60.4643 | 2026-09-01 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 121.4 |
| 03db2a3b-780e-34cb-8436-5fd61ccf68c3 | -7.5895 | -60.4636 | 2026-09-01 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.9 |
| edde9f0b-013d-3e40-9c4d-52897dca2ec3 | -17.4122 | -42.3445 | 2026-09-01 01:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 04c26837-40d5-38af-ab62-b1f170a0dce8 | -7.3487 | -60.5883 | 2026-09-01 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| b713f810-2ec1-35df-b6ff-1387b7088af2 | -16.4768 | -47.9608 | 2026-09-01 01:00:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 6ab12663-7951-3af0-ab89-17234ee2fd0d | -6.9367 | -55.636 | 2026-09-01 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 9bce55b4-b9bf-3e97-a106-5fa85ea4f4f5 | -10.0173 | -44.6849 | 2026-09-01 01:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 8367eebd-7882-3199-9f1e-33a4798d2146 | -6.6036 | -58.5972 | 2026-09-01 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| b8b19653-ba4c-3d4f-9cd5-fb937cbadb72 | -19.1947 | -57.3509 | 2026-09-01 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.1 |
| ecf535a9-3aa0-3abb-858b-06940cdedd46 | -10.8627 | -45.356 | 2026-09-01 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 9a3e5c69-fdb8-305f-9347-b4261f1fa4a8 | -3.0425 | -39.9355 | 2026-09-01 01:00:00 | GOES-19 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 40.0 |
| 22cddfce-2ad3-3c5b-959a-0b142dfc57a4 | -7.5709 | -60.4835 | 2026-09-01 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 40c25e50-358a-31d2-812d-7fa3ed7ca9d4 | -19.2151 | -57.3275 | 2026-09-01 01:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 115.6 |
| b46a1ea2-7aef-3531-88d3-1e231cd3e125 | -17.372 | -42.3544 | 2026-09-01 01:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 120.8 |
| 3bca1d8a-5a66-3d59-a5c5-ed9892a13e3a | -17.3914 | -42.3744 | 2026-09-01 01:00:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 142.9 |
| d178f1a7-b767-3abc-8afa-7e64fce4c069 | -16.4971 | -47.9344 | 2026-09-01 01:00:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 58.4 |
| c9334938-e091-34af-a47d-348ddfff07f3 | -7.3488 | -60.5691 | 2026-09-01 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 507ad5c1-0667-39ce-995f-569c8f18cb76 | -10.3574 | -50.0171 | 2026-09-01 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 000be4a4-45bd-3d06-b7a7-7e96fa4561f9 | -10.0364 | -44.6825 | 2026-09-01 01:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 162.1 |
| 260ef467-5f24-3861-b540-0ca3eef056a3 | -11.3232 | -45.2009 | 2026-09-01 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 046012f4-74a0-3451-a312-faee0e6d3ee6 | -10.8818 | -45.3534 | 2026-09-01 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 45.9 |
| b136cd5c-11ca-3b70-b7cb-3ce0568437fc | -6.9552 | -55.635 | 2026-09-01 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 93b30e23-a3ff-316e-9adc-3ef225953555 | -6.6976 | -55.4091 | 2026-09-01 01:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 196.4 |
| 619581f8-650f-3123-add3-0a8d30740b33 | -16.0547 | -54.3908 | 2026-09-01 01:00:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 7be32af6-6ffe-3a1d-81c9-bad71b929140 | -7.182 | -60.6904 | 2026-09-01 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| e64b5fd5-9bd9-3445-8402-657fdc1b661e | -3.8604 | -44.0585 | 2026-09-01 01:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 17507229-ec85-3058-b33f-9021a65e556b | -6.6975 | -55.429 | 2026-09-01 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 2cb9dbd9-b6c9-3d2c-bc4b-998dc83880c9 | -10.0364 | -44.6825 | 2026-09-01 01:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 208.0 |
| f9edfa4c-8a29-3657-9ee9-27e552c1ebff | -10.0173 | -44.6849 | 2026-09-01 01:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| d7c72881-067d-3b0b-90f2-f29fdb34e04d | -10.036 | -44.7056 | 2026-09-01 01:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 225.5 |
| f260b7b8-9268-359a-8d2f-e58a9a32fb9c | -19.1951 | -57.3301 | 2026-09-01 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 97.4 |
| cf5627ff-e425-305a-8e0e-16efba7a1a72 | -18.5089 | -50.8974 | 2026-09-01 01:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 200.4 |
| afd2fb27-8881-38e9-92f5-a70a049e04a8 | -7.905 | -44.2346 | 2026-09-01 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 264ec102-234d-34bf-8ec6-38dede4f88ee | -18.5083 | -50.9195 | 2026-09-01 01:10:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 2190a8dd-3709-3135-a60f-c3ec585a7704 | -14.4587 | -52.5151 | 2026-09-01 01:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 772d1fe2-b83a-3929-923a-9adbee3c7dc2 | -19.2147 | -57.3483 | 2026-09-01 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 65.8 |
| c676f64f-3189-3093-922c-5fe0c42ecd55 | -19.2151 | -57.3275 | 2026-09-01 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 110.9 |
| cffb1cf4-57c8-3f50-afe8-c73559af1a70 | -7.5895 | -60.4636 | 2026-09-01 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 3bbc34f7-2981-3b11-bec1-6ce501a684b0 | -6.6976 | -55.4091 | 2026-09-01 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 128.1 |
| 44db1368-e62e-3ad5-bb37-5b2125ae19a2 | -4.7734 | -41.8026 | 2026-09-01 01:10:00 | GOES-19 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 52.2 |
| 349bddb5-d1fb-3237-a749-3681f7b9b661 | -7.9048 | -44.2577 | 2026-09-01 01:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 9f366e72-30eb-3caf-8169-e7c0ccb054d8 | -19.8853 | -48.0932 | 2026-09-01 01:10:00 | GOES-19 | ÁGUA COMPRIDA | MINAS GERAIS | Brasil | 3100708 | 31 | 33 | nan | nan | nan | Cerrado | 103.6 |
| f912e504-c272-39a5-b9f3-8e09677c0707 | -3.8605 | -44.0355 | 2026-09-01 01:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| c908e87d-7f16-3394-a25b-7568e7a8d7be | -7.3487 | -60.5883 | 2026-09-01 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 0118156a-8f8a-3ba9-bb26-a0a45dcda87f | -3.8603 | -44.0815 | 2026-09-01 01:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 7cef6aff-99d1-3f85-9d7f-9d7c65fa2d7e | -10.017 | -44.708 | 2026-09-01 01:10:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| f40d2a07-4cd7-33f0-b533-52c6fe4cf445 | -7.3488 | -60.5691 | 2026-09-01 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.9 |
| d06058d2-5bce-3c38-9912-627a850ff1d8 | -17.3921 | -42.3495 | 2026-09-01 01:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 278.5 |
| b9494ba6-c5b3-3d18-b6d8-1b1a98a6e0c0 | -7.5711 | -60.4452 | 2026-09-01 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 59561438-a96f-33bd-8ffe-ae5916bf967b | -7.5526 | -60.4651 | 2026-09-01 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 3dcff39c-54ab-3573-95e2-93d91c6b96cf | -3.879 | -44.0576 | 2026-09-01 01:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 4f04ac0e-b7ee-3d54-a46a-85ff420e1d97 | -17.3914 | -42.3744 | 2026-09-01 01:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 129.3 |
| 6ca0602c-bfe1-3721-90bf-73b3aa5d7ea4 | -17.372 | -42.3544 | 2026-09-01 01:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 6956b2a3-409c-36cc-a4ee-ad864a8eca74 | -11.277 | -50.5815 | 2026-09-01 01:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 0e392efa-4199-3a5b-a7dd-c0dc684928f4 | -3.8604 | -44.0585 | 2026-09-01 01:10:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 1c53a75b-9049-3388-8118-93cdd3fe7b87 | -11.2767 | -50.6029 | 2026-09-01 01:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 17baf9b8-2195-3011-b82a-65174810fb8e | -6.9552 | -55.635 | 2026-09-01 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| b736a40a-58ff-3eda-8289-e6fdd52440d7 | -7.571 | -60.4643 | 2026-09-01 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 240.5 |
| dfdd18f2-732b-3395-ab16-c5ef96da089e | -7.5894 | -60.4827 | 2026-09-01 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.0 |
| ecb25db8-337b-3e88-9dcd-665ce8f30223 | -3.0612 | -39.9346 | 2026-09-01 01:10:00 | GOES-19 | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 35.6 |
| e426fb63-e61c-34b6-9777-b435d2e6c4b5 | -16.0547 | -54.3908 | 2026-09-01 01:10:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| e8473a5a-945b-3fbe-b0f5-9ed292aec2a3 | -7.5709 | -60.4835 | 2026-09-01 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 145.9 |
| e93aa535-f9fa-3955-821e-52f3197c2abb | -7.2005 | -60.6897 | 2026-09-01 01:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 39.6 |
| f9a60929-14a9-346a-b90d-4fbd43d52f32 | -17.3713 | -42.3794 | 2026-09-01 01:10:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 2e8dc445-3735-35db-89b9-073379825599 | -6.7162 | -55.4082 | 2026-09-01 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 2a53baf5-be35-35df-b65a-acc9a466cd10 | -11.258 | -50.5836 | 2026-09-01 01:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 9d5c522d-4977-3bd0-9808-4803bb264136 | -6.9367 | -55.636 | 2026-09-01 01:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| fd728b43-1e37-3269-984c-ff91c212f771 | -6.6036 | -58.5972 | 2026-09-01 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 1cac3969-457b-360f-a399-e640f66b8295 | -19.1947 | -57.3509 | 2026-09-01 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.1 |
| 213c7e4a-e52e-37e0-bb0d-8f56826d1c8d | -17.39 | -42.36 | 2026-09-01 01:15:00 | MSG-03 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e5ebc41c-8f98-38c7-9cc6-edfd91fc2cf3 | -11.28 | -50.56 | 2026-09-01 01:15:00 | MSG-03 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 08d2d2af-da2a-30cf-a212-52db0acb6b88 | -10.2 | -50.3 | 2026-09-01 01:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fb87dde5-e3b1-3854-b4dd-67d19302069b | -10.17 | -50.29 | 2026-09-01 01:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README13.md)
