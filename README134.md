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

## Dados Diários - Página 134

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| acd0298b-cb70-3693-b0b4-aa8f1664c881 | -11.3596 | -44.1989 | 2026-09-23 12:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 72.5 |
| e14a9879-6a8c-3bd7-a3ae-d710b6966a16 | -6.5941 | -43.7333 | 2026-09-23 12:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 8da91512-b7dd-34c8-88cc-a45aaa896610 | -6.6775 | -58.5748 | 2026-09-23 12:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 106.9 |
| df5f8b8d-e04e-3e1c-aafe-f508adc19cca | -11.4209 | -47.3603 | 2026-09-23 12:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 178a910b-2acf-3616-99b8-f16e2d3b66c2 | -7.0349 | -44.6625 | 2026-09-23 12:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 553559a2-eb0d-3c3d-9b91-722c848d93b4 | -11.3058 | -43.9963 | 2026-09-23 12:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 195.7 |
| 370c5508-81df-33b3-b69e-0524e512e069 | -9.5918 | -43.9501 | 2026-09-23 12:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 80.9 |
| 90ee8d85-51c3-3cd0-8782-f311cdd08270 | -11.3976 | -44.2167 | 2026-09-23 12:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 39682bb8-c05b-3ef0-bb56-3dca94afcb56 | -7.4153 | -42.6479 | 2026-09-23 12:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 92.4 |
| 66f96a74-5026-3d53-8406-ccfe0d766643 | -11.4782 | -47.3529 | 2026-09-23 12:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 104.9 |
| f56911b5-8add-30d1-a0b3-04ad52e15df5 | -7.1392 | -42.0811 | 2026-09-23 12:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 93.3 |
| 441897d3-7026-3c3c-b35c-c3233a733934 | -9.5731 | -47.9529 | 2026-09-23 12:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 113.4 |
| afd5e1a4-d00e-3c26-83a9-57405c0dc0eb | -6.6129 | -43.7317 | 2026-09-23 12:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 300.0 |
| 6a68386e-1346-38a1-9353-a24078c04e70 | -9.5857 | -48.433 | 2026-09-23 12:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 26f73b4b-9ae8-34b6-a030-940a7a9cf21c | -6.9416 | -42.8834 | 2026-09-23 12:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.8 |
| 44c63973-740d-3b61-a4c1-fce0df295d3c | -6.6631 | -55.0512 | 2026-09-23 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 3d0edaaa-ea38-3494-a477-7f1a051e1cae | -7.4288 | -44.718 | 2026-09-23 12:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 29cd2110-a925-36a9-9a0d-2127af5d35d4 | -9.5921 | -43.9267 | 2026-09-23 12:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 98.3 |
| 810ceac3-2c9d-3308-a2d8-69becf126dff | -9.6108 | -43.9477 | 2026-09-23 12:50:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 92.5 |
| fc60e228-762d-334b-80cf-28083713ff19 | -9.5854 | -48.4549 | 2026-09-23 12:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 49777538-5e3a-38f2-9917-605054819125 | -7.9904 | -44.9608 | 2026-09-23 12:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 70.8 |
| abd0c58c-808d-36f3-ad25-5e72062a4f94 | -6.6127 | -43.7549 | 2026-09-23 12:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| de5d704c-a747-3d1e-b47e-cfa81a4d0d89 | -9.5463 | -45.7708 | 2026-09-23 12:50:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 202.2 |
| fa090bdb-48a6-391e-9f11-d975e3019bca | -9.0242 | -48.1403 | 2026-09-23 12:50:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 050aa352-a85b-34bf-8897-0e191eb68da6 | -6.8985 | -41.6976 | 2026-09-23 12:50:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 72.1 |
| 1dc4f90a-39f8-384e-9890-0173f5d1d8df | -11.3054 | -44.0198 | 2026-09-23 12:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 124.8 |
| b5e29a1a-6ce9-3a8d-b344-aa4000a80687 | -6.8152 | -47.8735 | 2026-09-23 12:50:00 | GOES-19 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 20bc02be-31da-34e8-921c-8613c159246c | -6.663 | -55.0712 | 2026-09-23 12:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 9a2f12b7-59f6-3a35-aed3-bf8b09a7107e | -8.8105 | -44.2757 | 2026-09-23 12:50:00 | GOES-19 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 8670ada7-5ebb-325e-96cd-93e6847053fb | -6.6146 | -59.9272 | 2026-09-23 12:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 113.1 |
| 145ca235-935a-30d4-bed5-762b9ad83ddd | -8.3591 | -45.6056 | 2026-09-23 12:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 353614aa-d17b-3663-bf45-ee60cf81ee8b | -6.2208 | -41.6651 | 2026-09-23 13:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 89.6 |
| c2a7db2a-ff91-3b01-812a-5de6d5e31103 | -11.4168 | -44.2139 | 2026-09-23 13:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 170.9 |
| ce5f155d-1c6a-3e4d-a8be-136df68114f5 | -11.6986 | -43.4654 | 2026-09-23 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 6db8ec2b-37b7-3568-9a57-bd32d6a90b10 | -11.3054 | -44.0198 | 2026-09-23 13:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 187.1 |
| d95bf9eb-eff7-3c27-b78a-962ba1ce4b8b | -11.6798 | -43.4446 | 2026-09-23 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 70ed7618-3ed3-3e60-a1bc-6b50972b92bd | -10.5561 | -46.7095 | 2026-09-23 13:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| ef109cf8-6576-34e0-8921-5bc8dc88c94c | -7.0352 | -44.6396 | 2026-09-23 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 145.7 |
| d64976a3-305c-37db-b5e7-1a4b2a226522 | -10.8002 | -50.8243 | 2026-09-23 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| c353b63d-b0a4-3dfa-a990-2c719130ef8b | -7.4288 | -44.718 | 2026-09-23 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.2 |
| d51a9040-9ccf-3024-b151-f13fcd556107 | -11.4005 | -44.0525 | 2026-09-23 13:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 6b5711c0-a320-3515-962c-2142c621492d | -10.8189 | -50.8436 | 2026-09-23 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 404c114f-639b-3fb2-b6c0-e05238c67794 | -9.5918 | -43.9501 | 2026-09-23 13:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 105.0 |
| 476206b8-f2c3-36c4-aeea-c13e8223250e | -9.6043 | -48.4529 | 2026-09-23 13:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 78.9 |
| d4e6df11-96d5-39b6-8bc6-73c7f9e48798 | -8.5992 | -44.5301 | 2026-09-23 13:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 96.1 |
| d861222d-3edf-36a9-8ccd-816b85135ae5 | -11.699 | -43.4416 | 2026-09-23 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 9352acc7-c20b-3534-aba1-965facfc1d24 | -6.6129 | -43.7317 | 2026-09-23 13:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 317.7 |
| ba69d2ed-7540-31a8-81e8-c56fd8541fd3 | -9.5735 | -46.5337 | 2026-09-23 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 120.0 |
| a63c474d-9f2b-35ae-ad1f-503f721aaff2 | -11.3976 | -44.2167 | 2026-09-23 13:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 175.0 |
| c73221e0-d3a4-3f9a-98a2-25b00781b887 | -8.9202 | -45.9536 | 2026-09-23 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 457.0 |
| ee4bd442-f499-3ced-ae3c-8c4763116c41 | -7.4153 | -42.6479 | 2026-09-23 13:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 124.9 |
| 8fe97c12-3394-399e-a68b-1860044b7d2c | -11.3596 | -44.1989 | 2026-09-23 13:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 87.3 |
| 3fab96ca-073d-3865-aedf-9c79b0aa69e7 | -11.3551 | -43.3764 | 2026-09-23 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 67709268-9f12-3406-974f-1e262c39ee0e | -7.1581 | -42.0792 | 2026-09-23 13:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 84.1 |
| 1ad275c5-3284-3e1e-a93b-790b6aefd2bf | -6.9416 | -42.8834 | 2026-09-23 13:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 92.7 |
| 79b9ec8f-7d63-33dd-9fa9-861bdab00789 | -9.5921 | -43.9267 | 2026-09-23 13:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 120.4 |
| 82ad8bb9-86ee-3235-9371-3610722e4bbe | -6.5941 | -43.7333 | 2026-09-23 13:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 514fa881-f062-3d15-a1c0-5f3fedadf205 | -6.6145 | -59.9464 | 2026-09-23 13:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| d130bb22-ef57-3de3-924b-bc906a0a4a7c | -6.6331 | -59.9265 | 2026-09-23 13:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 136.9 |
| 5fdb528f-85c8-32f2-a40d-353baa509943 | -9.6108 | -43.9477 | 2026-09-23 13:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 125.4 |
| 8b46b0b2-7dac-3b01-be34-500dce98d1d6 | -7.1395 | -42.0572 | 2026-09-23 13:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 87.0 |
| e0124f26-a90e-3a16-a73a-6da59d24b7c9 | -10.8195 | -50.801 | 2026-09-23 13:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 8578fcbc-a059-3dcf-a10e-7e88438cae26 | -6.6127 | -43.7549 | 2026-09-23 13:00:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 9dd98da1-43e0-3bf5-8366-8b79387424b0 | -8.0923 | -44.3307 | 2026-09-23 13:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 6f583af3-df98-3b4d-9005-e78f87ab802a | -11.3058 | -43.9963 | 2026-09-23 13:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 308.5 |
| eae8f62e-26ca-3a41-b196-82af8181d738 | -11.4782 | -47.3529 | 2026-09-23 13:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 08931289-64ed-36b7-b587-db6503e291a8 | -9.5857 | -48.433 | 2026-09-23 13:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 4eb93139-6cee-3c4d-8ba2-27b376f18def | -9.5854 | -48.4549 | 2026-09-23 13:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| c076ebfb-3e0f-3d38-8150-0d4bbf0c12d0 | -7.0164 | -44.6413 | 2026-09-23 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 103.3 |
| ab85a9f1-63a9-37e6-8319-52247fd726cf | -6.1846 | -52.049 | 2026-09-23 13:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 55aae081-5c4a-3342-91a9-93a717de4dc9 | -7.0349 | -44.6625 | 2026-09-23 13:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 115.3 |
| b5bd3870-79cc-30bf-8085-6ffcc9ead8f2 | -11.6793 | -43.4684 | 2026-09-23 13:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 6fe570c7-c90a-350d-a451-0e0748990651 | -6.9174 | -41.6957 | 2026-09-23 13:00:00 | GOES-19 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 75.9 |
| f5c08f21-d7ac-3698-97eb-403536212bc3 | -8.9019 | -45.9104 | 2026-09-23 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 18f511dd-a66e-3eb9-a98b-e75c571cb0a9 | -8.3591 | -45.6056 | 2026-09-23 13:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 1c0c9fc4-384d-3a57-bddf-c4a522fd4c1b | -6.633 | -59.9457 | 2026-09-23 13:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.6 |
| ca1882f0-040d-3cc1-adb7-381e4c98104e | -11.4009 | -44.029 | 2026-09-23 13:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 20286e80-f65c-3516-914f-981afa8d8cdd | -8.9013 | -45.9556 | 2026-09-23 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 245.8 |
| b8f57958-b117-3f3e-ace8-91c61989edc5 | -6.6146 | -59.9272 | 2026-09-23 13:00:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 156.9 |
| e25d182d-54f1-3dca-871a-fec668df9de6 | -7.1392 | -42.0811 | 2026-09-23 13:00:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 104.3 |
| 04368901-b58c-35c2-b7d1-5cdb9cd699da | -8.9016 | -45.933 | 2026-09-23 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 424.7 |
| 9d320889-708b-3a39-b437-539c86bfc5f9 | -9.406 | -47.7507 | 2026-09-23 13:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| e8ebfee8-45a4-3d39-a4b2-291f9881e713 | -9.5518 | -45.3839 | 2026-09-23 13:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 86.9 |
| d73bb83c-5e71-3906-b6a1-8176aabb5639 | -6.6317 | -43.73 | 2026-09-23 13:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 174.7 |
| a844fa43-dc1a-3eb8-951d-57738b66e144 | -11.3551 | -43.3764 | 2026-09-23 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 5364c605-572d-38de-80c6-e74d98ed8980 | -6.2208 | -41.6651 | 2026-09-23 13:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 158.2 |
| 10f8c253-682f-39eb-9cd1-c9090cbecc14 | -11.3972 | -44.2401 | 2026-09-23 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 118.6 |
| f7169ddf-9c4b-37f1-b692-21c700be36df | -6.6331 | -59.9265 | 2026-09-23 13:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 177.0 |
| c9e4ea12-d074-3417-9352-8808b0262daa | -6.9174 | -41.6957 | 2026-09-23 13:10:00 | GOES-19 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 90.9 |
| 87820012-9abc-33c7-be0e-04e9b18ad01a | -11.3976 | -44.2167 | 2026-09-23 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 334.7 |
| b80530f8-391c-3ff0-81d8-bfc0f105db48 | -7.0352 | -44.6396 | 2026-09-23 13:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 89c9b5c4-8ad4-3ed8-a048-8cde7c38ac70 | -9.3797 | -48.3232 | 2026-09-23 13:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 96df9c5d-4c3a-3995-87b0-932ff4d48a53 | -6.2396 | -41.6634 | 2026-09-23 13:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 116.1 |
| b48e3932-9bdc-35c9-a22d-db850040d223 | -9.0242 | -48.1403 | 2026-09-23 13:10:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 32ad6e0d-8abc-3b9a-89c2-93607d51310c | -6.6148 | -59.908 | 2026-09-23 13:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 11cb3c77-df53-39d6-8b41-7cc4c4e22e42 | -9.5857 | -48.433 | 2026-09-23 13:10:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 183.9 |
| 354181b2-000e-3dbf-a7e7-56a83609cc43 | -8.3591 | -45.6056 | 2026-09-23 13:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 77.1 |
| ebded643-f155-30b2-aed4-7caf23060a03 | -11.4168 | -44.2139 | 2026-09-23 13:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 324.5 |
| e073889d-8fae-383b-afa3-902ec282400d | -9.5918 | -43.9501 | 2026-09-23 13:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| c103c8c9-4e2c-30fa-8993-b4c9345c841e | -6.6146 | -59.9272 | 2026-09-23 13:10:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 178.6 |


[Clique aqui para ver as próximas entradas](README135.md)
