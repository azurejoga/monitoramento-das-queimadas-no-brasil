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
| 3ecbba32-0119-3fa7-b0fd-9c4f53cf651d | -20.53529 | -49.49503 | 2026-04-15 03:42:00 | NPP-375D | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ef410b47-c8c7-3eba-94ba-8fcdf3d35761 | -20.18766 | -46.57796 | 2026-04-15 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b99e8039-0b4c-3d6a-92fb-8838403cb2f0 | -22.08641 | -43.17762 | 2026-04-15 03:42:00 | NPP-375D | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 33b936b2-cd25-32fe-b498-e0d2c288593a | -22.87434 | -48.64742 | 2026-04-15 03:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b1664764-8d57-3c13-963b-8de792502eb3 | -20.15668 | -46.74255 | 2026-04-15 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 325176de-c28e-3248-8a49-083a515a383f | -21.03823 | -48.55035 | 2026-04-15 03:42:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 619a5fae-2e3c-3d74-bd25-bfc852de5aca | -21.03687 | -48.55605 | 2026-04-15 03:42:00 | NPP-375D | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a782e43c-fcaa-32de-9bbd-df854de4d964 | -22.87725 | -48.64951 | 2026-04-15 03:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 86a97ed8-56a8-3fa0-ad97-9670d4704e9c | -20.18665 | -46.58244 | 2026-04-15 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c247ac7-2a9b-359b-8cf7-1b6c8780410c | -22.88169 | -48.64418 | 2026-04-15 03:42:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61e35f2e-1f7c-39d8-987f-c82dbf3f6bbd | -20.22293 | -46.47506 | 2026-04-15 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53fcfa11-3498-312e-a429-31e054c4a7a3 | -20.22388 | -46.47079 | 2026-04-15 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5652cfb0-ccac-3d20-92ed-0fc6467c2be5 | -21.11648 | -42.39074 | 2026-04-15 03:42:00 | NPP-375D | MURIAÉ | MINAS GERAIS | Brasil | 3143906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cd02a82d-8370-3004-8a90-9271948bd238 | -20.16648 | -46.59059 | 2026-04-15 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 32abc024-f584-3b29-a387-5136b0b6d5fa | -20.54008 | -49.505 | 2026-04-15 03:42:00 | NPP-375D | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 320a8be0-3d8a-36e6-b17c-04ff0f020beb | -20.53377 | -49.50132 | 2026-04-15 03:42:00 | NPP-375D | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fba2d8d3-27a3-30ef-8765-623bdf15cd77 | -20.22483 | -46.46655 | 2026-04-15 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f9e51bef-e5b1-3890-bf75-5572c3264dd8 | -20.53487 | -49.497 | 2026-04-15 03:42:00 | NPP-375D | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 07ca68fd-d644-3ff1-9196-ea6d87359cff | -20.17256 | -46.59074 | 2026-04-15 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| adf863b4-5592-3679-849e-2e989d6e8d04 | -20.16746 | -46.58626 | 2026-04-15 03:42:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fb692853-02de-37af-9200-49199277cde0 | -20.54055 | -49.50299 | 2026-04-15 03:42:00 | NPP-375D | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 2702b634-a647-336b-98a9-c2b35df0b758 | -11.79606 | -43.6226 | 2026-04-15 03:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ca9fd286-361b-3b2e-a761-e047f2b041bf | -11.78102 | -43.61996 | 2026-04-15 03:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5b2e3424-5f71-3c35-9c5d-aa4f7fb9d9b1 | -11.70821 | -44.74841 | 2026-04-15 03:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b45b1ee-630b-357d-a60b-327af82702f8 | -11.7907 | -43.63119 | 2026-04-15 03:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1b536115-359d-356f-ae9b-57fe85faa243 | -13.44238 | -43.85277 | 2026-04-15 03:57:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fe0f7fc9-f1b4-3b78-8b07-3d39dac009f5 | -11.78774 | -43.62591 | 2026-04-15 03:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 6a6aacbf-a607-36d9-bdbd-4c4272aa056b | -11.70482 | -44.74408 | 2026-04-15 03:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dda10330-5e3f-3d5e-8987-14b592a4d9be | -11.70885 | -44.74483 | 2026-04-15 03:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fe6a9e5d-765b-376a-93f3-60a5849af861 | -9.00981 | -46.1183 | 2026-04-15 03:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 25e4c63a-195d-3388-b533-7ad9e8cd6c14 | -11.78182 | -43.61532 | 2026-04-15 03:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa30b792-1246-3338-93cf-1e638e7e33d8 | -12.45205 | -43.78408 | 2026-04-15 03:57:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4cc86c92-b341-316a-819a-2b28f752c183 | -11.78558 | -43.616 | 2026-04-15 03:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e9093b2-7d75-3a5b-91e9-5fe5f29ae85d | -11.7931 | -43.61733 | 2026-04-15 03:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2d2349da-3869-33de-998d-d490aca57568 | -11.7923 | -43.62194 | 2026-04-15 03:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| e85b1776-a2c7-3f49-9cd0-89440ae5583f | -11.9558 | -41.29882 | 2026-04-15 03:57:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 60da40ad-0993-3bbc-b896-23d300b713f2 | -11.7915 | -43.62657 | 2026-04-15 03:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d7c32d1c-4c49-3bc4-b81d-18b2be6f8c22 | -11.78478 | -43.62062 | 2026-04-15 03:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3b5d8b56-b0a8-364f-ab49-e7880b410045 | -11.90585 | -43.84306 | 2026-04-15 03:57:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 612027b4-f4b1-330b-9824-12fdf0cdbfb0 | -11.80062 | -43.61866 | 2026-04-15 03:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ba7a5493-cdc0-371a-8d29-4c3729849a30 | -7.83545 | -42.04836 | 2026-04-15 03:57:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9d598701-0ba4-37ac-8680-216201283f92 | -18.73593 | -49.79202 | 2026-04-15 04:00:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0f1f1c4-77bd-3ec2-9372-63116121bef7 | -17.33661 | -43.58957 | 2026-04-15 04:00:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f9ce6098-f475-3ce3-bcb0-fc934a17dbe9 | -15.28437 | -43.06467 | 2026-04-15 04:00:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 7fc496fe-68b0-3a8f-b3ec-67505b0eccc4 | -18.73098 | -49.79108 | 2026-04-15 04:00:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 74de40b0-f645-3f05-8d09-667531e4175b | -19.58766 | -40.07491 | 2026-04-15 04:00:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5b8e68cc-535e-3847-ac72-a64b198d7131 | -19.5972 | -40.0804 | 2026-04-15 04:00:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6c4f8cf1-f284-32da-8552-f8e8535dc19f | -15.54946 | -43.15089 | 2026-04-15 04:00:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e4db2cd1-3c19-359e-bb90-08305a9476d2 | -15.66306 | -43.31337 | 2026-04-15 04:00:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2364931e-dd5e-3255-ab71-45a13788d056 | -17.33731 | -43.58554 | 2026-04-15 04:00:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 54415fce-f541-32fe-8f46-53f113b1bf14 | -19.59103 | -40.07548 | 2026-04-15 04:00:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2447b163-4159-31a3-96a9-1f96c5c729dc | -19.59383 | -40.07983 | 2026-04-15 04:00:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 96d61cb7-18cf-3add-baf8-39fd95531a90 | -18.72976 | -49.79711 | 2026-04-15 04:00:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ee10f578-68d5-3b4a-9c21-f29c43b84759 | -19.5944 | -40.07605 | 2026-04-15 04:00:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 455134f0-b12e-39f2-a94f-3b28f946b51a | -14.73637 | -47.55278 | 2026-04-15 04:00:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8d6a5cf4-b199-3cd1-9490-31b92753192e | -14.73616 | -47.55046 | 2026-04-15 04:00:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e9bf1a3-3382-3d66-aba4-def52f86c06f | -19.60566 | -40.07017 | 2026-04-15 04:00:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c893512d-7dd7-3f76-9249-78694d554568 | -16.66074 | -41.15024 | 2026-04-15 04:00:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e857f472-fe8f-305c-ab89-754730cc84d5 | -19.58823 | -40.07113 | 2026-04-15 04:00:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5a18291e-1e82-3003-9e66-1ffad50db5b9 | -15.65954 | -43.31273 | 2026-04-15 04:00:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e73241f1-7c0c-36eb-b69a-c6404713cec4 | -15.65884 | -43.31682 | 2026-04-15 04:00:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a6523a7a-f158-333d-84bd-e819a259f0a4 | -15.55297 | -43.15153 | 2026-04-15 04:00:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fb52925b-91a8-3c4f-8d5e-5805cb4e0120 | -15.55365 | -43.14753 | 2026-04-15 04:00:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 800b6f0a-760a-3d12-af27-3b9143d14588 | -17.34081 | -43.5862 | 2026-04-15 04:00:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b86513df-8d48-3e71-b9a8-f058edfbb725 | -14.44225 | -44.85359 | 2026-04-15 04:00:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 05d822d0-2b27-3615-a389-98adace9ec5c | -21.69795 | -56.31009 | 2026-04-15 04:02:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| caeece7c-123d-3e86-a44b-f0f33f6c5b97 | -20.31902 | -55.00345 | 2026-04-15 04:02:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79a9790d-ee16-3d97-a421-7c7691636fa4 | -20.18343 | -46.59639 | 2026-04-15 04:02:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e00c25b-aab1-3fdb-b08d-42291745067b | -20.22686 | -46.47266 | 2026-04-15 04:02:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4ef99ab7-87c0-3e8e-bcd0-3fba4f5c3633 | -21.03744 | -48.55041 | 2026-04-15 04:02:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 53d95d5d-113d-3e89-9251-dfb1e471854d | -20.32504 | -55.00182 | 2026-04-15 04:02:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 740c02d6-2d54-3588-a246-cf3a5aff4de6 | -22.87994 | -48.64654 | 2026-04-15 04:02:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c17fdb40-ce99-3d1a-be8d-8a2b48c8d212 | -20.15623 | -46.74076 | 2026-04-15 04:02:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1809b59f-03d9-346d-9798-8bdfdbc4e569 | -23.45564 | -49.25225 | 2026-04-15 04:02:00 | NOAA-20 | TAQUARITUBA | SÃO PAULO | Brasil | 3553807 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a8ae5906-fcbe-34e7-abf8-b9e4a3e1d43f | -22.96003 | -52.70297 | 2026-04-15 04:02:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 38779e49-a808-307e-a298-79a7bbff94d8 | -22.96087 | -52.6993 | 2026-04-15 04:02:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b6db68cc-480b-38c8-af50-5416688c8dca | -21.41173 | -48.6143 | 2026-04-15 04:02:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 92c01f0a-cc5f-3ba9-b2c7-266f30d91bdd | -23.40718 | -46.43419 | 2026-04-15 04:02:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 283a71a5-725b-3744-a847-b0b170e8195d | -20.5401 | -49.49485 | 2026-04-15 04:02:00 | NOAA-20 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1a5a43bd-da64-3a0a-924b-7138b884330b | -20.16857 | -46.58871 | 2026-04-15 04:02:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 0e3fbb00-6688-3c2f-8b23-04dd55799e37 | -20.16764 | -46.57206 | 2026-04-15 04:02:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3df3fffc-7165-3414-a8df-2a283b40a3e5 | -20.15912 | -46.74723 | 2026-04-15 04:02:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 74564930-9122-3ed8-97fb-84266917d7f0 | -23.53897 | -47.63269 | 2026-04-15 04:02:00 | NOAA-20 | ARAÇOIABA DA SERRA | SÃO PAULO | Brasil | 3502903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4b83e575-1350-3171-b380-aa08dc50dfef | -23.45632 | -49.25003 | 2026-04-15 04:02:00 | NOAA-20 | TAQUARITUBA | SÃO PAULO | Brasil | 3553807 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 826b062f-e6e3-3357-9329-248c773cab04 | -20.53543 | -49.49382 | 2026-04-15 04:02:00 | NOAA-20 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 120fc92a-3286-33db-8fc5-330cc7e0554c | -20.32541 | -55.00553 | 2026-04-15 04:02:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 43401114-fa6f-3481-89c3-e20c16c86270 | -22.83847 | -48.63285 | 2026-04-15 04:02:00 | NOAA-20 | PRATÂNIA | SÃO PAULO | Brasil | 3541059 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef5d5d0b-731a-37ba-bc32-d59a34e23f59 | -20.18651 | -46.57999 | 2026-04-15 04:02:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b70b9ed5-b402-3a82-9fc5-04be0a4b7ab7 | -20.32365 | -55.00752 | 2026-04-15 04:02:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 214e0b10-b86a-3e32-84f7-f5d9a68cfccf | -22.96623 | -52.70084 | 2026-04-15 04:02:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7bd0b67d-0dda-322a-8171-7da406697a00 | -22.88078 | -48.64227 | 2026-04-15 04:02:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7964c8ab-55e3-3bc1-98ff-05b070c5ccc7 | -20.53906 | -49.49997 | 2026-04-15 04:02:00 | NOAA-20 | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 54af406f-6e8d-3354-a8b3-9b33ab06df9b | -20.24632 | -46.54251 | 2026-04-15 04:02:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 907aabba-3bcf-3772-aeaa-ecfaeac9c250 | -20.22396 | -46.46651 | 2026-04-15 04:02:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da8eee32-d582-3809-8146-2122cc1c479e | -20.24242 | -46.54168 | 2026-04-15 04:02:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6055b7c7-125b-37dd-aa35-1aca2484fd55 | -21.03654 | -48.55495 | 2026-04-15 04:02:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e3620a90-c1e9-348a-a763-cabc513a2154 | -22.08673 | -43.17464 | 2026-04-15 04:02:00 | NOAA-20 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f2ad22f0-7234-3ad5-9a89-33bf5a761fed | -21.19388 | -48.61057 | 2026-04-15 04:02:00 | NOAA-20 | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| afe36bdb-a302-326d-85f7-9c0ec01c08e6 | -22.65833 | -43.85131 | 2026-04-15 04:02:00 | NOAA-20 | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2aa9f346-1ae0-3487-987d-d92a1af48e80 | -22.91753 | -49.209 | 2026-04-15 04:02:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README3.md)
