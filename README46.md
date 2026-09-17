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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9fcb747c-7808-38da-ad01-3d07c71aee1c | -8.3968 | -42.21075 | 2026-09-17 04:40:00 | NOAA-21 | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 8863231f-0e09-36e7-b446-15c3b130e8e6 | -7.38589 | -44.51387 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 40290adc-ddf4-3913-ae4e-91a6a4302992 | -7.83296 | -50.23197 | 2026-09-17 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4cbff532-909f-30ff-820e-1ddc251ac7af | -9.78301 | -46.48059 | 2026-09-17 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78dd80ae-ade6-30d2-883b-c4b57d98bfbb | -9.18647 | -46.76086 | 2026-09-17 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f97a7bd-9dfb-37c5-90c3-cff78abb944e | -7.1131 | -43.09622 | 2026-09-17 04:40:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a9540ae4-f3b1-3dde-8133-9060b5ddbc89 | -9.10833 | -45.7182 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 13066417-a870-3cb2-bfe8-2afa76b9cf19 | -7.07041 | -41.82455 | 2026-09-17 04:40:00 | NOAA-21 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 96a05e4e-e12f-326b-aa73-6dbeab8a8c3e | -7.27361 | -44.21327 | 2026-09-17 04:40:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bbb37958-5470-3b51-9f52-48d34416b3ca | -7.44771 | -44.57406 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c15870d7-4be5-3b92-b87d-942523b1b3e2 | -8.78899 | -46.89659 | 2026-09-17 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 950c2d89-011e-3af7-87cc-479db583b39e | -11.58529 | -46.88604 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70b9bb76-ba14-3142-a3fa-e66df2d829e4 | -7.14204 | -42.09005 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fce179a8-298a-34b1-941d-6d92f0055a7f | -10.54321 | -44.85827 | 2026-09-17 04:40:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 6f9f29fa-2504-34b0-8b09-aab2a1edd2f8 | -9.11942 | -45.73151 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 08a75e0d-3ec9-3766-8057-799ba65e8a50 | -9.90619 | -46.51072 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0b8245db-ce18-3ae9-a414-f0a1511aa552 | -8.56569 | -44.54459 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9d25e9c9-560b-3967-8104-3e9127d19d6b | -10.5042 | -46.33027 | 2026-09-17 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ccbe1f5-9858-364a-838e-9c4a7a14791b | -5.18162 | -49.36972 | 2026-09-17 04:40:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33308c47-746e-3b4d-aef6-58d83fc0ab2b | -10.01374 | -45.50142 | 2026-09-17 04:40:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a68f2388-95d4-3543-8cb6-9447f84f0ce8 | -5.15271 | -55.9378 | 2026-09-17 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7d8ebe44-d21a-306b-a4f3-e5d0a8591cc4 | -7.64387 | -44.33911 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8e1b176c-c44a-3bfd-80f1-9aed0ece0dd8 | -9.91121 | -57.06427 | 2026-09-17 04:40:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7af6b83a-157e-3227-8469-68c04f4b95e5 | -8.85831 | -46.98655 | 2026-09-17 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 175dbe6e-e939-395f-93e8-b53030a19354 | -9.83499 | -48.36388 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b87b7783-3246-3b32-ba54-6881d62fa046 | -7.97181 | -44.83787 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9d7c6082-2090-33d4-ba56-df08d3823b52 | -9.60562 | -45.34286 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34199a36-d630-3a32-b18a-cc9ea8a204f3 | -9.61127 | -45.3612 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9fffe852-965b-34f5-9d3d-9c3ba2c7ca00 | -4.56965 | -54.90596 | 2026-09-17 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c782494c-2d47-3eaa-bc28-40812e5991ff | -9.8298 | -46.50145 | 2026-09-17 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f11ebdba-f827-3458-b111-0e133cfcdd25 | -11.53319 | -46.86721 | 2026-09-17 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 60358ca7-8191-39ba-bcca-fd49299a5f7b | -7.58512 | -46.33647 | 2026-09-17 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2991463b-e609-38a6-9c60-cfca4e9b373f | -8.86192 | -46.98714 | 2026-09-17 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| de8ab9f3-6fae-34b7-b0bc-ed9cd0d1cddd | -5.84419 | -49.9834 | 2026-09-17 04:40:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e95122d6-ea3b-310a-8280-b4c180a4fcd3 | -5.8621 | -52.05907 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4e61f18-2565-3bb9-9e97-89d83b6762b3 | -7.94727 | -44.8311 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 63c5d307-78e4-3aad-9be2-309e30275a2d | -5.80117 | -47.24749 | 2026-09-17 04:40:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| c5f64b0f-c1d9-3ddb-ad0a-da97300966f0 | -7.65077 | -45.84059 | 2026-09-17 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7b9d2957-405c-3947-9af0-cea68dadbac2 | -12.31389 | -47.958 | 2026-09-17 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| e2b80cd0-507a-3cc2-be82-3181e29e5ddb | -8.26157 | -42.15844 | 2026-09-17 04:40:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 9208a238-421c-3515-809b-08702782a375 | -7.12729 | -42.16318 | 2026-09-17 04:40:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 94d6f463-0741-3af6-a237-fa0e276247c7 | -7.53835 | -48.59856 | 2026-09-17 04:40:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 018307f3-de94-3376-b45f-a902a9b832ac | -11.01585 | -45.20986 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 377f4d73-99b5-3463-9778-623fbbcdb32e | -8.22525 | -55.46322 | 2026-09-17 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90191f34-e30f-3a0c-85d2-01b8dddfc680 | -6.78748 | -48.66475 | 2026-09-17 04:40:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b72abdbc-eaf7-33bb-a4cd-66a4ef922afd | -5.84012 | -44.89304 | 2026-09-17 04:40:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6a1794d0-ab6f-32b4-a908-9de4baa332b0 | -7.09332 | -42.09293 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| f33f4bb4-9952-345a-88e7-4d575d089367 | -4.38629 | -56.35318 | 2026-09-17 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39d8557c-01aa-3913-906f-d6b2aa1e1da1 | -6.11696 | -51.70548 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f4901c4-eb2b-3e72-ac1f-f26c3a437a5c | -7.58745 | -44.93082 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8b269e6e-4678-3f4a-b4e5-3da49a8cb967 | -5.90611 | -52.09801 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ed0220fa-1eca-3e4c-8e6d-c03b387a98c3 | -9.39401 | -60.30283 | 2026-09-17 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 858609bb-f4d3-3b59-b600-e6e01125c20e | -5.46582 | -44.95691 | 2026-09-17 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9030e186-6035-3a15-a74a-d7130aeb4eea | -10.78963 | -46.19135 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b558091c-2999-3d2f-9b8d-d0360b4c7c22 | -7.04462 | -42.05304 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 776d4ca6-9224-3be2-af43-654d2ff1fd12 | -5.75197 | -57.59627 | 2026-09-17 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 65c17955-972c-3236-949a-2e4cde13355c | -11.89363 | -43.83276 | 2026-09-17 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e6859f20-bba1-37a2-bec2-e85aa50fdecc | -4.53512 | -54.93166 | 2026-09-17 04:40:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a63b124-8a29-387d-b43a-fb75178be351 | -9.60394 | -45.34246 | 2026-09-17 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5161e5b0-e582-3ef5-942c-e5b766f541a4 | -10.96002 | -48.3136 | 2026-09-17 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 96f15a59-dd5d-30df-8e3e-769703678eba | -8.86011 | -46.97432 | 2026-09-17 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4df9217f-496e-3d40-bac2-b312bdc62c14 | -5.67735 | -44.8266 | 2026-09-17 04:40:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f43c609d-73d0-3437-8693-08706ef0a61e | -9.10444 | -45.7176 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 21.2 |
| f4ad3511-e4e6-3670-a1c0-47861ae25979 | -7.44569 | -45.29412 | 2026-09-17 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 02045660-ae42-3712-a717-1a2abb705980 | -5.65259 | -44.80491 | 2026-09-17 04:40:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c0fc49d7-9f19-385f-9625-f468c5bb6d64 | -7.04389 | -42.05844 | 2026-09-17 04:40:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 601f1196-0dc3-3b5f-8f75-9c4fc3b0da45 | -7.27272 | -44.21046 | 2026-09-17 04:40:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87357ae6-02f2-35f3-b8d7-661224529788 | -6.93833 | -41.69732 | 2026-09-17 04:40:00 | NOAA-21 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e03673a4-896a-3b86-b571-a5152621e19d | -8.47522 | -46.89201 | 2026-09-17 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f7aab47e-93c4-3122-aafa-7339af8f9b2b | -10.51103 | -46.28247 | 2026-09-17 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 171cbcb1-bf61-3aa8-a353-8dd30e15f5c8 | -5.63614 | -44.80753 | 2026-09-17 04:40:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 893f65ef-219a-3b42-ae8a-57e036abb459 | -7.36549 | -44.48031 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e479510-39b4-3048-97ad-52fe1b1a6f01 | -5.85979 | -52.06694 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 482ecc7d-dcc7-357d-aa01-2506d50ea375 | -9.34653 | -50.18916 | 2026-09-17 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65b5b14d-55db-3556-bccb-bb92cf8cba9c | -10.55364 | -43.67525 | 2026-09-17 04:40:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 091aaa9d-847d-3610-93bd-e255f433e027 | -10.78224 | -46.2029 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e8ade900-da65-3c2f-b0b6-0d5dcf0c9091 | -5.83717 | -52.05104 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 04ff008f-53aa-323f-b535-390c5f77b752 | -9.18391 | -46.75377 | 2026-09-17 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 349ed754-19e1-3764-9f76-233fa391015f | -9.03842 | -47.75728 | 2026-09-17 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66126f84-e629-3324-bb6d-8e9470ab9401 | -7.64602 | -44.32409 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 97703ca3-aee6-3b44-96ef-e39b68895556 | -7.07562 | -47.48903 | 2026-09-17 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f0002270-a8c2-3983-a0a9-e8e08bb46e4b | -7.46219 | -42.1068 | 2026-09-17 04:40:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b317b78e-be50-3b79-8b8d-906c9cc73be2 | -11.61046 | -50.6303 | 2026-09-17 04:40:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3de2eb57-d52f-3864-a59f-2717debad264 | -12.32103 | -47.95908 | 2026-09-17 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c86df643-76f3-3a1b-8213-72e0f92d1efb | -8.52821 | -44.50801 | 2026-09-17 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4213616b-1055-3655-8cfd-f7e325d1ac0a | -8.86111 | -44.8984 | 2026-09-17 04:40:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a5fac9b7-b906-30f3-b897-37415f1016cd | -4.88103 | -56.06082 | 2026-09-17 04:40:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eda1e1a9-cc75-3a4b-a383-c2909afb15f5 | -7.36087 | -44.48331 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f647dfbf-1814-3d32-9a95-05487d717b4e | -7.43852 | -44.58006 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b500b200-f6fe-3e8b-a313-1e099feb5df4 | -5.42808 | -44.80337 | 2026-09-17 04:40:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 80b3f1b5-43b3-31b8-ad78-1d45cf4a37ec | -10.51034 | -46.28732 | 2026-09-17 04:40:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 637257ad-ad60-31fc-9e07-0e9465f9249a | -9.03551 | -47.75284 | 2026-09-17 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 98d3edaf-1e29-38da-9309-81324e102374 | -9.11076 | -45.72873 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 36b7ac9f-0384-38ff-9063-6228b2dc7a0c | -10.01195 | -45.50056 | 2026-09-17 04:40:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5aebceb-b677-3707-a0be-39059ddf2ff2 | -7.96479 | -44.82894 | 2026-09-17 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ab4b46ba-ad28-3140-8505-bc4586a47bd3 | -9.85221 | -48.38953 | 2026-09-17 04:40:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d3bda8c6-2c1b-3116-bedb-ea0c72569ce5 | -3.82459 | -55.784 | 2026-09-17 04:40:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 13753f69-e2f3-3946-b0cc-c32ab7a42254 | -5.82802 | -52.08589 | 2026-09-17 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1a3fe10-0fd5-3aa5-adfa-4c5ba781a19d | -9.11538 | -45.72432 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 26.9 |
| e9cd3c85-ddb5-3b71-af7b-6c3a03113952 | -8.87366 | -45.88514 | 2026-09-17 04:40:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |


[Clique aqui para ver as próximas entradas](README47.md)
