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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0e8d52a5-b19d-3563-8f6a-c3e5dc02ba06 | -1.6811 | -52.5558 | 2024-12-06 00:10:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| b13a45cf-b9ca-308d-a1f4-ca87a9e0f353 | -1.6811 | -52.5558 | 2024-12-06 00:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 81e7159f-74c8-3f99-9ee1-43e93714a20c | -19.59125 | -40.4538 | 2024-12-06 00:32:00 | TERRA_M-M | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 13654a2d-ad88-3d12-96ab-203c98b3be9d | -15.44898 | -43.65735 | 2024-12-06 00:32:00 | TERRA_M-M | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 4206ebd4-566a-32ba-8d8a-2d744d425cf0 | -9.83701 | -37.08049 | 2024-12-06 00:34:00 | TERRA_M-M | TRAIPU | ALAGOAS | Brasil | 2709202 | 27 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 1ecf07eb-60a7-330e-8749-d9c78f7e97e3 | -11.05869 | -45.38684 | 2024-12-06 00:34:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| fda4805c-238f-3035-84ac-383a53d12228 | -13.22238 | -43.97738 | 2024-12-06 00:34:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2e32d3b2-8f0d-3888-9fea-c46208ebf23a | -6.78529 | -40.21881 | 2024-12-06 00:34:00 | TERRA_M-M | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 7d93433c-2801-3452-89ee-6ba5f61a2ce8 | -7.48243 | -47.48837 | 2024-12-06 00:34:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7fde5cf2-1b0d-3ea8-9af7-3867e694eb58 | -8.02801 | -47.69425 | 2024-12-06 00:34:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 744fa63f-c48d-3819-9d24-31bbc6aed66d | -12.85242 | -51.92385 | 2024-12-06 00:34:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 19.7 |
| c0167f4c-d4a4-3c39-b50e-fffafeeffce3 | -9.10294 | -43.19428 | 2024-12-06 00:34:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 8230e353-8f61-3deb-a905-98acf0dece1f | -9.10418 | -43.20321 | 2024-12-06 00:34:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| e3a30545-db3c-37e9-b5b2-8224d001067a | -9.11517 | -43.14098 | 2024-12-06 00:34:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| dba16905-1a14-3662-b671-9104f4515649 | -13.61497 | -44.09508 | 2024-12-06 00:34:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 749d4a7f-e6cf-355e-9953-529463144042 | -8.99462 | -35.44138 | 2024-12-06 00:34:00 | TERRA_M-M | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 84.4 |
| 4961ec53-de1d-382b-aecd-a0d4279fad5e | -7.22808 | -39.9586 | 2024-12-06 00:34:00 | TERRA_M-M | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 9.9 |
| f23adefa-d988-3a8f-a784-89673513cd09 | -6.12027 | -46.92923 | 2024-12-06 00:34:00 | TERRA_M-M | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 04c9e462-941e-35a5-9843-488ed4e618ea | -11.88932 | -40.95842 | 2024-12-06 00:34:00 | TERRA_M-M | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 14.6 |
| ecb1950c-860e-3f20-8778-49ffef2c0c98 | -13.4141 | -41.1161 | 2024-12-06 00:34:00 | TERRA_M-M | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| f63d460b-a37b-3740-83ac-481553de9a81 | -13.23152 | -43.97608 | 2024-12-06 00:34:00 | TERRA_M-M | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| c1a3eb7e-f177-376f-8fc2-3d77be110f08 | -5.26901 | -44.03379 | 2024-12-06 00:34:00 | TERRA_M-M | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 6f7af871-1c29-3965-ad48-da0af208645c | -6.07073 | -44.63176 | 2024-12-06 00:34:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1d70dcbe-e314-3195-85af-71220de19384 | -11.05728 | -45.37628 | 2024-12-06 00:34:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| a89d3284-4a98-37af-97e3-85823b7d2115 | -12.02261 | -43.00448 | 2024-12-06 00:34:00 | TERRA_M-M | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 3a93ec52-667a-35a3-a867-827626e8a3dc | -10.22366 | -42.18966 | 2024-12-06 00:34:00 | TERRA_M-M | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| fb097e72-cfc0-3f1c-b66e-6352cfd6545e | -12.86401 | -51.9501 | 2024-12-06 00:34:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 36.2 |
| 218fbc4d-0848-3d98-aa9a-da1c7281cfc0 | -9.19994 | -43.16512 | 2024-12-06 00:34:00 | TERRA_M-M | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 6a282e46-2ad0-32d1-b410-76a9384fd1dc | -13.62418 | -44.09377 | 2024-12-06 00:34:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cd192983-6ffe-37f2-a0e1-75a2a4d5d3d1 | -12.85618 | -51.95802 | 2024-12-06 00:34:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 836df697-502a-3ba6-8164-aae19f58935c | -6.78707 | -40.23084 | 2024-12-06 00:34:00 | TERRA_M-M | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 21.9 |
| 264b1d27-ac74-35c6-bd4b-e5ee9fef0cf8 | -9.96921 | -36.11976 | 2024-12-06 00:34:00 | TERRA_M-M | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| 023ec501-9791-3a2c-95f6-56bbab28c8ab | -1.6561 | -52.7328 | 2024-12-06 00:35:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f6a43f8-53f1-3f22-8c11-fc1c3f4eef46 | -3.2146 | -46.783699 | 2024-12-06 00:35:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d625d6f-d31a-32ef-ba35-2a421c185e31 | -3.8087 | -54.742298 | 2024-12-06 00:35:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf8e5fc3-9fc5-36a6-8eb2-b15294e559a3 | -12.8486 | -51.921398 | 2024-12-06 00:35:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 527846a8-fea5-398b-a824-7bfc093fcd37 | -13.6156 | -44.087002 | 2024-12-06 00:35:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8da1a7ea-fb0d-358a-bf99-e6dbd7f5ce41 | -19.587 | -40.446701 | 2024-12-06 00:35:00 | METOP-C | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1c0a2754-1410-3f37-8a53-7643ca516890 | -11.0519 | -45.374699 | 2024-12-06 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 605e25c6-6865-3afb-9602-ef4ed95debaf | -13.614 | -44.079899 | 2024-12-06 00:35:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c13c000e-253d-35e9-ba8e-17c664067f91 | -12.2337 | -52.450401 | 2024-12-06 00:35:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f997e428-8dcb-38fc-bd2d-634b0e6b2877 | -4.7469 | -44.753399 | 2024-12-06 00:35:00 | METOP-C | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| caae14d5-6df3-3316-8e54-65138fc53037 | -15.4361 | -43.652401 | 2024-12-06 00:35:00 | METOP-C | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 3f1ccb6b-b6bb-3cf3-9eda-c99aca924df4 | -11.8786 | -40.946499 | 2024-12-06 00:35:00 | METOP-C | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 5f050919-f2f4-3dd0-b8db-b4858579a0c6 | -3.79 | -50.0755 | 2024-12-06 00:35:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4ea963b-7b29-3151-99cb-ea7a0024989c | -13.2169 | -43.969799 | 2024-12-06 00:35:00 | METOP-C | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c9172313-6111-335e-adcc-2f61471004fb | -5.2595 | -44.031799 | 2024-12-06 00:35:00 | METOP-C | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7ff9ec3-ca5c-3e10-935d-1654ddd739e0 | -13.2186 | -43.977001 | 2024-12-06 00:35:00 | METOP-C | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 83b46351-3373-324a-bab4-a4b72d86031e | -12.8513 | -51.934898 | 2024-12-06 00:35:00 | METOP-C | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 41564041-2468-3c3c-a5e3-4f9bf6fac4d5 | -6.8665 | -47.237499 | 2024-12-06 00:35:00 | METOP-C | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0f3751b1-bd82-38d7-ae1a-9b8143f44318 | -9.962 | -36.108101 | 2024-12-06 00:35:00 | METOP-C | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 095798d8-9be6-34c7-aefa-0ba722a8d86d | -11.0535 | -45.381599 | 2024-12-06 00:35:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 30e8d25e-04f4-3422-bb45-958997fc0f29 | -3.2162 | -46.7906 | 2024-12-06 00:35:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9357dd7-6ee2-3b42-8c92-b55e3bc8582c | -8.0186 | -47.684399 | 2024-12-06 00:35:00 | METOP-C | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b8d2a6c4-b0cc-39a5-99f6-f41fe78f3ca0 | -4.7487 | -44.761002 | 2024-12-06 00:35:00 | METOP-C | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 853f08a8-abf5-3cea-8883-76f9b3e6b575 | -1.67061 | -52.73835 | 2024-12-06 00:37:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 9e53c7d7-6a8e-3037-aa80-d0f32e47b3ee | 3.2366 | -61.028 | 2024-12-06 00:40:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 57.1 |
| a77975e8-297c-3ee9-b39f-21fce9b638df | 3.2366 | -61.028 | 2024-12-06 00:50:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 57.7 |
| ad6e6b9b-8cb0-342b-9ce3-2c8124a2a6db | -21.197599 | -56.9109 | 2024-12-06 01:14:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 0687bf3b-da71-38eb-9aed-180f96c6d828 | 2.4323 | -60.647099 | 2024-12-06 01:14:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 06232aef-d71d-3fe6-9087-b3b820fbf4dc | -0.6375 | -63.025002 | 2024-12-06 01:14:00 | METOP-B | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b6a6b945-8700-3768-9896-1062b5b03f76 | -2.0022 | -52.336201 | 2024-12-06 01:14:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b8fbf27-8b53-3005-b90e-d73957fec684 | -11.8178 | -57.816799 | 2024-12-06 01:14:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 21cd4bc1-926f-3017-ba86-ec761a3d07c6 | 3.2437 | -61.023399 | 2024-12-06 01:14:00 | METOP-B | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0b9daa35-4e9d-369a-941b-788e51097556 | 2.4843 | -60.690399 | 2024-12-06 01:14:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 22f494c7-f37d-30da-a4f5-52c0764f5ec3 | -12.2324 | -52.452801 | 2024-12-06 01:14:00 | METOP-B | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c9de106f-a994-3ea9-a5e6-c53ca6bc4584 | -11.8161 | -57.809299 | 2024-12-06 01:14:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 297a2ee2-543f-3b04-bb31-4b6af9998c43 | -12.8422 | -51.921902 | 2024-12-06 01:14:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5585fc5f-d0ad-3960-a966-16017b0d132d | -21.195999 | -56.9035 | 2024-12-06 01:14:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| af7ef84b-2763-3296-87a7-4243bdfa4c5d | -0.1779 | -60.668701 | 2024-12-06 01:14:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 873cdb20-dc54-315c-9096-664db8745868 | 3.242 | -61.030899 | 2024-12-06 01:14:00 | METOP-B | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c633aa8a-6504-3c94-aef7-c5bd0100da91 | -1.0682 | -62.649601 | 2024-12-06 01:14:00 | METOP-B | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7e16de0c-f0e9-353d-ac2c-be238ec8f42f | -1.0666 | -62.642799 | 2024-12-06 01:14:00 | METOP-B | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c1612ff9-ee0d-3236-9499-7daca8a6c9dc | 2.434 | -60.6395 | 2024-12-06 01:14:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 32ded915-ee42-3f5b-9543-d2c60bea85fa | -16.093399 | -60.0853 | 2024-12-06 01:14:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be211018-1060-3af5-8867-62ddd86e31d1 | 3.2403 | -61.0383 | 2024-12-06 01:14:00 | METOP-B | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ddc6458b-5f50-3527-a322-360efdeb0110 | -2.4776 | -54.101398 | 2024-12-06 01:14:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d4aa414-fecf-359b-97c3-6c604669d91f | -19.1528 | -57.546398 | 2024-12-06 01:14:00 | METOP-B | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| a650c090-a631-3953-9d1e-0a6930ce3186 | -2.4813 | -54.117599 | 2024-12-06 01:14:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44599df1-50f5-3c56-9066-3a9d0194b89b | 2.486 | -60.6828 | 2024-12-06 01:14:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6e40be7e-0166-3687-a389-fd68289389f2 | -0.636 | -63.018101 | 2024-12-06 01:14:00 | METOP-B | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bb6c6fc7-53d3-37da-a47b-e109ab0434f8 | -2.0119 | -52.334 | 2024-12-06 01:14:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f083ae6-c490-30ed-a4d1-b4a43552a062 | -2.785 | -53.2304 | 2024-12-06 01:14:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 295eb432-c907-375c-9fbe-47289aae75c1 | -12.8462 | -51.937401 | 2024-12-06 01:14:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 620ea034-5319-3e3d-ab78-ed4149e31cc5 | -9.3389 | -36.038 | 2024-12-06 01:20:00 | GOES-16 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 85.6 |
| dda00e90-f244-3d3b-9218-0f6fa87811ad | -9.3394 | -36.0108 | 2024-12-06 01:20:00 | GOES-16 | CAPELA | ALAGOAS | Brasil | 2701704 | 27 | 33 | nan | nan | nan | Mata Atlântica | 132.5 |
| d17808c8-6740-3401-a796-0e6841dbd7c2 | 3.2366 | -61.028 | 2024-12-06 01:30:00 | GOES-16 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 0e2c7f44-31f4-3f97-90b5-df49b411787c | -7.6528 | -73.098198 | 2024-12-06 02:14:00 | METOP-C | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| e57ecc0b-1d70-3077-9e90-d55cf0c29115 | 3.23758 | -61.05874 | 2024-12-06 02:17:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 23.1 |
| e1d06bf0-5fdb-3914-bf83-8cf401f27ebc | 3.24248 | -61.02279 | 2024-12-06 02:17:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 8760185b-b2ef-3ab5-bec5-b7d7810b6762 | -2.0309 | -52.3458 | 2024-12-06 02:20:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| dbdd9535-481f-3fc7-9d99-77817753d2d9 | -17.8765 | -40.1729 | 2024-12-06 02:30:00 | GOES-16 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 105.2 |
| 80fd072e-e2ea-307d-8be3-99e9a14859fc | -9.4777 | -35.7975 | 2024-12-06 02:40:00 | GOES-16 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 74.7 |
| 3bf8de1f-352a-392b-9f26-8552c8c9f2f7 | -9.47861 | -35.79549 | 2024-12-06 02:47:00 | NOAA-21 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 34.8 |
| 4912af6e-2d4d-3a6b-962b-6ea9fe1c4593 | -9.48325 | -35.7931 | 2024-12-06 02:47:00 | NOAA-21 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 28.0 |
| 2a53b1fd-a12e-3a9f-ae2e-75afcdd34d36 | -9.47626 | -35.79141 | 2024-12-06 02:47:00 | NOAA-21 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 28.0 |
| d1f8b6af-54d5-3dbb-b580-4f1241477b12 | -9.48466 | -35.78613 | 2024-12-06 02:47:00 | NOAA-21 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 28.0 |
| 8ba14f3a-2e26-333c-86c1-89b88e9fb81a | -9.47483 | -35.79847 | 2024-12-06 02:47:00 | NOAA-21 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 3efa0507-3f91-38d0-828d-6f828862b2bc | -9.48 | -35.78837 | 2024-12-06 02:47:00 | NOAA-21 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 34.8 |
| 89a873f1-ecf3-3ada-ba22-d1a1f70a649f | -9.48136 | -35.78143 | 2024-12-06 02:47:00 | NOAA-21 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 42.0 |


[Clique aqui para ver as próximas entradas](README2.md)
