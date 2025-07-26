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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf2a9816-a101-3be9-9acb-f0599c132ee0 | -6.88661 | -43.11058 | 2025-07-26 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bc6d495d-82c6-3c1c-8390-54609320e29d | -6.56491 | -41.49522 | 2025-07-26 04:25:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dcf22f11-9250-3e05-9576-8dd80d34147f | -6.63336 | -58.85759 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 4c9ae016-1236-3c80-9543-a0efde4bb964 | -11.11187 | -45.11912 | 2025-07-26 04:25:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2dfde5b8-81d2-3e45-a609-dfcb1b42f905 | -5.65131 | -42.58139 | 2025-07-26 04:25:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3ea47adc-a174-3cc6-ab64-6e0de706ffbd | -7.17458 | -43.48798 | 2025-07-26 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 06005fe3-75ea-332e-945c-de77325c4769 | -6.86844 | -43.67857 | 2025-07-26 04:25:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf397f3e-4e40-39ce-b43c-d4f205a81329 | -7.29234 | -60.17858 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ff809310-7348-3b50-9064-ac9dcff6b1df | -6.62144 | -58.85255 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 30.5 |
| f3b51ad1-894e-3070-b58c-554d9eef3954 | -8.38333 | -44.60589 | 2025-07-26 04:25:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41d7fd7e-3d6c-30da-9cf7-6ecf06be7072 | -7.7865 | -44.54511 | 2025-07-26 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5d03215-5c87-3140-9a9d-612ea8f2cfc7 | -5.77161 | -43.63995 | 2025-07-26 04:25:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ebb805a5-b7d5-32d3-a699-2ea004e04cef | -9.14574 | -45.86934 | 2025-07-26 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ffd1b959-e9ec-38aa-8e58-756d4be44cf5 | -5.87097 | -44.98183 | 2025-07-26 04:25:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b869a5b-1eb1-381b-8fb1-7b79c867d721 | -7.23941 | -43.07314 | 2025-07-26 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| c6f534ea-4fe5-371d-bc45-5c334140c531 | -7.41231 | -43.97676 | 2025-07-26 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d1fac718-3ccd-3e3b-8a24-e7fd46747bb7 | -6.63879 | -58.86452 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e47d1320-eabd-392e-8aea-e0b01177b1d9 | -6.68046 | -58.8239 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 38753d6f-72b0-3214-8667-4ebb1c1a942a | -6.67446 | -58.85715 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 128.3 |
| 05291720-c044-36a3-a41e-735a5772d2d8 | -3.75142 | -49.0524 | 2025-07-26 04:25:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 055b9a78-3ba2-3469-ada3-720089bc7ff1 | -6.65249 | -58.82996 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 0f280de2-60f7-38aa-a843-376fd88b27db | -7.9982 | -45.03944 | 2025-07-26 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b74ed52a-4d78-39cd-9a9f-a77ebe825999 | -7.36837 | -43.43497 | 2025-07-26 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 192ee2aa-1316-3aef-8f53-833863d8b757 | -6.63551 | -58.84929 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 146bf8a7-cbf9-3a2a-b4ee-bca8fcdfb959 | -6.65057 | -58.83785 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 37.3 |
| c7c60c25-61de-3cb4-a61e-af3d4bf11ce9 | -6.67009 | -58.84142 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 39.8 |
| 599d47c2-473e-3068-9465-01769fa0d1dc | -9.36592 | -40.31304 | 2025-07-26 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 37.3 |
| f9f58233-0ea6-30cb-b1ca-dd4af02ca5f3 | -7.1919 | -44.02209 | 2025-07-26 04:25:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9eb2b976-f983-332d-9660-c6074022140c | -6.47177 | -42.78865 | 2025-07-26 04:25:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ef2df46d-b57a-3383-b0d5-22add9516b23 | -6.65393 | -58.85574 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| ba7c7a1c-d704-3ee2-a299-6010938b81a4 | -9.25258 | -50.22623 | 2025-07-26 04:25:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b4af5e4d-640c-3ddc-b000-8e630a9ab21a | -6.65499 | -58.85009 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 181.1 |
| 67e1deeb-defb-3fac-bbbb-70fa8dc12007 | -6.21944 | -43.73791 | 2025-07-26 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de6c8c51-9400-3396-9587-1977983b3d44 | -6.54063 | -45.61311 | 2025-07-26 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f84426f9-17ab-3150-b19b-a92a1a18e4c1 | -6.63888 | -58.86772 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5dbee6ac-bc84-3f10-9f2a-2d739083ca90 | -9.36326 | -40.30908 | 2025-07-26 04:25:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.1 |
| dbb3c3fe-6ffa-324e-af1a-6ee6e4d2c4f0 | -6.66164 | -58.88639 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b0284e7a-d66f-346e-b27c-5eb38de9d8f8 | -6.01313 | -52.17745 | 2025-07-26 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 045df416-285c-3e96-9fc9-e96185d41bad | -10.13699 | -46.72301 | 2025-07-26 04:25:00 | NOAA-20 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5b9c7785-e1bf-3354-ac65-1359404a2ac2 | -4.07824 | -46.90068 | 2025-07-26 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e00d8bcf-3380-3a36-97b5-fe00d78ce0f3 | -10.62309 | -44.76373 | 2025-07-26 04:25:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 1b33aa50-61ea-3a70-886e-919e991bc25a | -8.17479 | -43.2175 | 2025-07-26 04:25:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 1bc921ac-6d09-3a98-b301-b98ee57e578a | -6.65525 | -58.92038 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b146be3b-aa25-338a-8590-4ca9d5d0d914 | -6.10735 | -57.72883 | 2025-07-26 04:25:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4934511-3719-39f3-aadd-3398705251ee | -6.66222 | -58.925 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a7e55eb6-0d58-3305-ad97-9b6cb3915e2d | -6.56387 | -41.5022 | 2025-07-26 04:25:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f4f05de7-d761-34b5-99e7-ae907d2afe74 | -6.62039 | -58.85827 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 30.5 |
| 036cf70b-9b67-3a8c-9b9a-87e5bda9990c | -5.77453 | -43.64443 | 2025-07-26 04:25:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b4c8407-b18a-3854-a88b-aeed1658be4b | -6.88321 | -45.24712 | 2025-07-26 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f28e7f34-6fb1-3b68-87ac-9f4ab086b81b | -9.50066 | -43.17107 | 2025-07-26 04:25:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5905e8e5-2478-3cd6-a9b8-8919639b3ffe | -7.05383 | -43.79122 | 2025-07-26 04:25:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2e97fb7-433e-3e85-9086-6dad6b6880dc | -6.63948 | -58.82755 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 33e85f4b-515b-34e7-82f1-ff068c36cc4c | -6.66492 | -58.87271 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9e3f7bfc-8565-3e89-bea4-38ed712fea93 | -9.73167 | -48.01697 | 2025-07-26 04:25:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8da1a58e-6ae8-3cff-827a-515e31fcb1c2 | -6.63985 | -58.85889 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 99713653-2de2-346e-87ed-b7c05a58bd7d | -6.68414 | -58.83821 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 62a33146-11e6-30b4-a67d-b43c6b0862cc | -6.6399 | -58.86212 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| ecbe1168-366d-3818-b35e-5c8a31573aa3 | -6.66275 | -58.88049 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f227b9de-970f-382e-9e42-a3caa7cb3fe4 | -6.66726 | -58.92847 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0783d964-37cc-3407-8909-cf964cefff0c | -6.68201 | -58.8496 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 89.2 |
| f4f2839c-8b12-384f-a2a0-9065953211e6 | -6.98882 | -47.08342 | 2025-07-26 04:25:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 958550cb-ceb1-371b-ad42-70168d392407 | -6.42382 | -41.15759 | 2025-07-26 04:25:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7f05fc29-f43a-3691-b1c8-44107049ac82 | -6.62556 | -58.83012 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 79788598-518f-37e4-ace5-9ec6db9fd66f | -5.74519 | -43.97661 | 2025-07-26 04:25:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6068063-e508-38e4-a2f6-8375cdb35efd | -7.79074 | -37.59765 | 2025-07-26 04:25:00 | NOAA-20 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 635c5cbe-e9e6-3635-a0c9-dad3285e4bc6 | -4.30262 | -48.10644 | 2025-07-26 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4196d64a-b18a-3b39-9656-83df2cc19d4c | -7.24055 | -43.07062 | 2025-07-26 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 81658b3a-45f4-340d-af4c-d803d4a91efb | -7.28654 | -43.08477 | 2025-07-26 04:25:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f023e01c-04cd-3533-aef0-d85be6bd6b88 | -6.86429 | -43.68203 | 2025-07-26 04:25:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 457bcda8-dea6-319c-b4cf-34ec12567939 | -6.87908 | -43.68028 | 2025-07-26 04:25:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bc15910d-3b37-34de-b96b-a72c74f1c8f5 | -6.63106 | -58.83682 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 1b7d7556-3eb9-3428-b676-b49a0f0c07ca | -7.09561 | -44.87599 | 2025-07-26 04:25:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbc96fca-314f-3a49-b1c9-f5e315e11fcd | -8.82436 | -44.51291 | 2025-07-26 04:25:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99a654a8-1a62-3b29-b733-997d558aa3a0 | -6.67647 | -58.84602 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 2a366a25-1cdf-3596-b828-3b83646c1ed8 | -6.55987 | -41.50159 | 2025-07-26 04:25:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1ec5e604-0063-3987-a6b7-b2313edf9c00 | -6.64742 | -58.8545 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| cecfc676-28e2-3706-9dc5-b603636bfa09 | -9.03045 | -45.34207 | 2025-07-26 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 79662b3c-d864-3edf-933b-fef115483ac7 | -6.65977 | -58.93233 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 090b358b-4efb-31af-96fa-06bcfe975c9d | -10.62018 | -44.75921 | 2025-07-26 04:25:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aef92918-576c-36be-9d68-6f2ea73e637a | -6.65983 | -43.05322 | 2025-07-26 04:25:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 10c6445a-d9d4-32c1-98b4-3d8f48f62be1 | -6.61907 | -58.82887 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 26.9 |
| 20c8e23a-93fa-3343-8277-4c7be4ad95c2 | -7.17629 | -43.48959 | 2025-07-26 04:25:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0920834f-4624-33f4-84f0-cc21f92cb184 | -6.6667 | -58.82367 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 1b9b3c03-f6d8-3720-8f2a-d20213b2570e | -6.66255 | -58.84571 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1757.3 |
| d125f2f8-de34-366f-b2ba-bfdb96ac0a53 | -8.07027 | -49.71847 | 2025-07-26 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 785e3190-2312-3cb8-9c10-13ce05a1a0ac | -6.66125 | -58.93039 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f06dd85-8d18-3c77-9ed1-00bd8c01e156 | -10.63414 | -48.1128 | 2025-07-26 04:25:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ad6d8554-30a8-39a2-a6aa-3ff1047191b2 | -6.8649 | -43.67801 | 2025-07-26 04:25:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| af09d529-b6df-30f2-8f66-0e0d4df011a6 | -6.07007 | -43.65072 | 2025-07-26 04:25:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2e4def6-04dc-33e0-b58c-594089e8a1c8 | -6.76494 | -43.6932 | 2025-07-26 04:25:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3f98461b-6670-3a48-bd72-72ba53745bf1 | -6.66483 | -58.86943 | 2025-07-26 04:25:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 086ff2f8-bc95-3def-997b-8d2889b5a8f2 | -3.66067 | -48.44368 | 2025-07-26 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bd35ba11-9e55-3fb6-b52a-701fbda3cd8a | -8.29097 | -45.0038 | 2025-07-26 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb9570c4-271b-30d9-96dd-b59c25b6948a | -4.10487 | -48.20453 | 2025-07-26 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 785507fc-d426-37a8-80d5-e7adb5f37574 | -11.45455 | -45.19344 | 2025-07-26 04:25:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b916151d-24b2-3c3a-a23d-61182add75f2 | -6.67852 | -58.83466 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 14.4 |
| e9630c39-915d-3035-a86c-568dafc1c80d | -7.36475 | -43.43445 | 2025-07-26 04:25:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ffddd5c0-edbc-301d-b9c6-6f146e3f9bda | -6.64399 | -58.83971 | 2025-07-26 04:25:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 832587f4-6149-3886-8dae-bbabccd5468d | -7.03954 | -40.4089 | 2025-07-26 04:25:00 | NOAA-20 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0375e00e-d0a8-3308-97c1-012a97eaa0cb | -6.52549 | -44.59572 | 2025-07-26 04:25:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README18.md)
