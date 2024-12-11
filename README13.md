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
| c3dc46c4-d042-3d9d-81c7-cfaa0aac981c | -6.90631 | -43.50901 | 2024-12-11 03:40:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 329063eb-6813-302a-96dc-66246d854f1a | -6.90528 | -43.51497 | 2024-12-11 03:40:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 17d04366-00e0-348d-9075-0f79c0ee9906 | -6.97283 | -43.00546 | 2024-12-11 03:40:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| a4d75f75-6a46-3abb-a4fe-eb5d381adcab | -8.51227 | -35.13791 | 2024-12-11 03:40:00 | NOAA-20 | SIRINHAÉM | PERNAMBUCO | Brasil | 2614204 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5bc504eb-03a6-3f0a-b442-2e73f7e827d4 | -11.46244 | -44.96084 | 2024-12-11 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b8ab69e9-4e27-339b-9601-aa3376b52765 | -12.15538 | -40.92257 | 2024-12-11 03:42:00 | NOAA-20 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 55bfe10c-2fd2-3421-99ff-abac40f1c27b | -11.46808 | -44.95916 | 2024-12-11 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ff8aa48-6d75-380d-a84d-1da2b3085489 | -14.11744 | -41.67926 | 2024-12-11 03:42:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 859e7bb4-c80b-3c94-b1e5-6e9f94e97e54 | -15.65526 | -39.18975 | 2024-12-11 03:42:00 | NOAA-20 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5150843c-e32d-3f9f-8cf6-e6f084dc5455 | -12.50388 | -43.87835 | 2024-12-11 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef5d6561-904d-3c2c-a1df-482a7e25ec32 | -12.66902 | -45.67706 | 2024-12-11 03:42:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f7399da7-f62c-3e1c-8255-a99d64ff02e7 | -14.96902 | -44.41561 | 2024-12-11 03:42:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1074756a-350f-39e0-beb0-2c346331b8c2 | -18.03887 | -39.9258 | 2024-12-11 03:42:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 083c262d-f219-3026-9df2-7939d78aada7 | -12.41372 | -43.80535 | 2024-12-11 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c47be93f-f4c4-3c76-8a41-98ff3daafcbf | -16.34562 | -43.69717 | 2024-12-11 03:42:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 986764c8-d626-358c-91e9-8a9f8c0e9e54 | -11.463 | -44.95788 | 2024-12-11 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e14cd61c-f8eb-3a5e-abfc-3fb50cbe7155 | -14.83356 | -43.14846 | 2024-12-11 03:42:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 27da8918-01ad-3cc8-9f7b-c687b1647e26 | -17.46734 | -41.84949 | 2024-12-11 03:42:00 | NOAA-20 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3437f3c2-d48b-3433-8339-ede9a3eb34f9 | -12.67427 | -45.67817 | 2024-12-11 03:42:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| bde4b4e3-8185-3995-94e8-559b1196247b | -12.66965 | -45.67376 | 2024-12-11 03:42:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a9b047ad-6543-3066-8250-606de091d418 | -15.35029 | -39.14621 | 2024-12-11 03:42:00 | NOAA-20 | UNA | BAHIA | Brasil | 2932507 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b531d9a6-e694-398f-a36d-162a0e1a2b7c | -16.34993 | -43.69811 | 2024-12-11 03:42:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f53a2ac5-bd3b-3b29-b5fe-1aad5f395b9f | -12.85004 | -43.82129 | 2024-12-11 03:42:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 831846ed-f0e9-3705-b2fe-6fd53869badf | -13.25564 | -41.33731 | 2024-12-11 03:42:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 5be33d7c-92e9-3653-83e3-182fc2b59f51 | -13.25475 | -41.34244 | 2024-12-11 03:42:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| d2ef2ba5-6485-3b92-9f4f-70cfb791ca7b | -16.88887 | -42.8391 | 2024-12-11 03:42:00 | NOAA-20 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e7d19f0-7a3a-3498-b693-06c4a254b396 | -15.06365 | -44.08956 | 2024-12-11 03:42:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 92fa9f70-56c9-3bb9-8df6-aecb50abe13a | -12.1931 | -46.72031 | 2024-12-11 03:42:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c7a0fe3-3873-3cee-97f8-622aa7156b12 | -12.88662 | -43.65136 | 2024-12-11 03:42:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e73fdb91-fe39-3ac7-9841-300a3c6c3f96 | -12.85468 | -43.82218 | 2024-12-11 03:42:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d323f0a3-da3d-30b3-847d-aed8c88bca65 | -15.06281 | -44.09154 | 2024-12-11 03:42:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 09b346b7-fcb4-38c3-b449-f6ef6015065d | -13.86487 | -43.06722 | 2024-12-11 03:42:00 | NOAA-20 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 20f8d0b7-ae29-3e7a-b47a-4c59954f5076 | -18.10874 | -40.1347 | 2024-12-11 03:42:00 | NOAA-20 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 194ceff7-5177-314f-a9fb-3525b9117a6b | -12.41466 | -43.80033 | 2024-12-11 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 246ee95b-29b2-31fb-9376-6ba0a84d57a0 | -14.9746 | -44.41158 | 2024-12-11 03:42:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 73c09d58-4900-3677-9a8f-ea198d95589e | -12.18445 | -41.34979 | 2024-12-11 03:42:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2578ea9e-8a24-31e5-ae49-2dabccc40135 | -11.46865 | -44.95613 | 2024-12-11 03:42:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e940815b-36ba-3e8d-8369-79e4a993e754 | -17.36934 | -41.72271 | 2024-12-11 03:42:00 | NOAA-20 | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 383a739f-ce7d-38fd-8c45-e31c23e35557 | -15.53962 | -43.14692 | 2024-12-11 03:42:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ae9f1300-cd2a-3cb0-a439-932192a2b330 | -16.54906 | -42.6581 | 2024-12-11 03:42:00 | NOAA-20 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7ce0589-1d0a-3113-a419-dca568960644 | -12.41 | -43.79936 | 2024-12-11 03:42:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a148ce6c-162a-35b7-81f5-8a24be5b8e53 | -14.96996 | -44.4106 | 2024-12-11 03:42:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cfae2789-42c6-38a1-8c61-e402065d329f | -18.74957 | -40.12436 | 2024-12-11 03:44:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8754dbff-5caa-3093-a7d7-3c1f4041cf29 | -18.74611 | -40.12371 | 2024-12-11 03:44:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 8efb0e38-6892-3448-bbca-70c941fe612f | -22.8544 | -42.98302 | 2024-12-11 03:44:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c8b08a12-10dd-35e4-916e-88c2975a8a3a | -30.15844 | -55.0117 | 2024-12-11 03:46:00 | NOAA-20 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 3.1 |
| 7fb08bf5-0315-3aec-bb50-1b2cf41ccc31 | -30.15933 | -55.00516 | 2024-12-11 03:46:00 | NOAA-20 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 2.2 |
| 69faddc3-d7f7-308a-b443-eb255a0c9dfb | -30.15771 | -55.01112 | 2024-12-11 03:46:00 | NOAA-20 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 2.2 |
| 17166c79-2ae1-385c-a528-6a0cbdb77706 | -30.16009 | -55.00577 | 2024-12-11 03:46:00 | NOAA-20 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 3.6 |
| a49de46a-dfa1-3d58-b48c-7feae6ca984a | 2.7627 | -60.6378 | 2024-12-11 03:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 07fd19db-6924-36a6-968c-f069633692f9 | -6.9592 | -42.9994 | 2024-12-11 03:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 144.0 |
| e61b6fd1-8a31-36e8-9ded-31fe0dc7e704 | -15.0865 | -59.6487 | 2024-12-11 03:50:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 76f63e3f-f7be-3e37-a7f4-a563d003efe4 | -2.9482 | -53.1206 | 2024-12-11 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 7822d165-2d40-3a83-873b-711ad5cd9c56 | 2.7444 | -60.6381 | 2024-12-11 03:50:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 7dbab4ff-33eb-3208-8600-aade046bba64 | -3.1288 | -54.0853 | 2024-12-11 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 2a4a2c6e-6b97-315d-90a1-08f32b77a97f | -6.9783 | -42.9741 | 2024-12-11 03:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.8 |
| 29a95bd2-4617-3d11-83f1-383a81829c0b | -6.1178 | -42.5559 | 2024-12-11 03:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 98.2 |
| 17d4047c-07f4-3acd-bdde-4127bab10a56 | -6.9161 | -43.4952 | 2024-12-11 03:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 62fdc179-8189-3348-a2b9-feb7dff5118a | -6.1368 | -42.5307 | 2024-12-11 03:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 90.4 |
| e8df461e-1ffb-38d8-a912-c12580e137a7 | -6.8972 | -43.4969 | 2024-12-11 03:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 122.9 |
| 22821ef4-6cba-3edd-898a-0230ae88f2c4 | -6.897 | -43.5202 | 2024-12-11 03:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 156.4 |
| 37404c7d-f09f-3af8-8430-531304df990e | -6.978 | -42.9977 | 2024-12-11 03:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 134.9 |
| d49a007d-32c0-3267-a88f-3969432abef7 | -6.1366 | -42.5544 | 2024-12-11 03:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 71.8 |
| d17a0906-bad7-35b0-b1cc-50e90b7b5c18 | -6.9594 | -42.9759 | 2024-12-11 03:50:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 76.9 |
| 5b610662-e2db-32d5-a216-7b6e78250017 | -2.9666 | -53.1201 | 2024-12-11 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 31540433-bbaa-3e38-8e64-bd093cdb1080 | -6.9158 | -43.5185 | 2024-12-11 03:50:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 045359db-0ac4-3769-853f-6613806fef0d | -6.118 | -42.5323 | 2024-12-11 03:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 148.2 |
| 53dff3d3-2186-35a5-aa32-c1b3b5e917aa | -6.1368 | -42.5307 | 2024-12-11 04:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 117.7 |
| ac8f4b3e-852a-394d-a171-6640e822fc9f | -15.0867 | -59.6288 | 2024-12-11 04:00:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 78511ee6-b978-313e-ac08-96afbb6d8c39 | -6.897 | -43.5202 | 2024-12-11 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 134.7 |
| 4e3bfe6b-60fc-32f0-af59-e4f58e8565ec | -6.8972 | -43.4969 | 2024-12-11 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 120.4 |
| dbb84d91-f239-332c-81bf-4ab461d340b0 | -15.0865 | -59.6487 | 2024-12-11 04:00:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 8f05d9ac-b375-33c4-ae6f-17c13424cf88 | 2.7627 | -60.6378 | 2024-12-11 04:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 9c72d2ac-832f-384c-a560-33eaf2541a8a | 2.7444 | -60.6381 | 2024-12-11 04:00:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 26ef2094-3f5e-32a2-a09e-7d5d5dc6f566 | -6.9158 | -43.5185 | 2024-12-11 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 107.8 |
| b828c8aa-1108-31e9-82a3-df7e80c14857 | -6.118 | -42.5323 | 2024-12-11 04:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 112.9 |
| f8607cd5-4b35-3fe5-97f2-24054f1b067f | -6.9161 | -43.4952 | 2024-12-11 04:00:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 27fec10a-3a85-38bb-8a24-dced0be51d20 | -6.1366 | -42.5544 | 2024-12-11 04:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 82.0 |
| 3b1b22f0-cef4-3824-badb-97867bcd3fec | -6.978 | -42.9977 | 2024-12-11 04:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 133.5 |
| bcb17314-8791-30aa-93f1-95cd6da9ff8b | -6.1178 | -42.5559 | 2024-12-11 04:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 75.6 |
| 0f09f567-b609-3b2e-9405-f9aad94f3ad0 | -6.9592 | -42.9994 | 2024-12-11 04:00:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 149.9 |
| aa1b1495-4f52-38a9-9043-9e1b50288c38 | 2.7444 | -60.6381 | 2024-12-11 04:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 2d6e3b55-6cfb-34dc-908d-db54859652a5 | -6.9594 | -42.9759 | 2024-12-11 04:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 80.1 |
| 297965cd-3a95-3c95-82d5-e54651f6925e | -6.8972 | -43.4969 | 2024-12-11 04:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 123.9 |
| e233bb5d-6af8-3020-a99a-babd9bca385b | -15.0865 | -59.6487 | 2024-12-11 04:10:00 | GOES-16 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 4e850c6f-f4e5-3f2b-be55-3de306bce9ae | -6.897 | -43.5202 | 2024-12-11 04:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 2d460945-d04f-3914-a7ff-6d512aa97c66 | -6.118 | -42.5323 | 2024-12-11 04:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 143.8 |
| 1c55bc08-20dd-3ce9-a284-02fef45ea9f0 | -2.9482 | -53.1206 | 2024-12-11 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 3f44cd88-632a-302a-a48a-c4d11e8f1ce9 | -6.9783 | -42.9741 | 2024-12-11 04:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 81.3 |
| 0f5ecc31-70d9-3c2c-a1e9-dc3ff6c85240 | -6.9592 | -42.9994 | 2024-12-11 04:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 133.5 |
| 593e35b3-6ccb-3072-a0b4-8ab6f1d38845 | -6.1366 | -42.5544 | 2024-12-11 04:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 72.4 |
| 0c06b3da-c940-3a18-a134-2048473ce3a3 | -6.978 | -42.9977 | 2024-12-11 04:10:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 125.5 |
| dce516e2-ff75-32fa-ad3e-8661b26a3186 | -6.1368 | -42.5307 | 2024-12-11 04:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 90.7 |
| ed0a2ceb-3532-35ed-9a0e-59eb422d19a9 | -6.9161 | -43.4952 | 2024-12-11 04:10:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 5cd319cb-6e5a-37c1-8cbb-f33d271294e4 | -6.1178 | -42.5559 | 2024-12-11 04:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 94.1 |
| 31c96cde-30b0-33b3-acc2-ba53fa0d8659 | 2.7627 | -60.6378 | 2024-12-11 04:10:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 87814dd7-5d8e-320b-9a84-3155a73dac64 | -2.9666 | -53.1201 | 2024-12-11 04:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 71d167a9-0c27-3de8-9137-3f668469e633 | -6.9594 | -42.9759 | 2024-12-11 04:20:00 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 78.3 |
| edce15f0-5ae6-3b13-a8f4-912011659180 | -6.9161 | -43.4952 | 2024-12-11 04:20:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 3b4c02b3-6cd1-39ec-87b3-213a67b41d4a | 2.7627 | -60.6378 | 2024-12-11 04:20:00 | GOES-16 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 61.7 |


[Clique aqui para ver as próximas entradas](README14.md)
