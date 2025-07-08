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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c5dffa8-ed64-3ca2-aa45-9a62f98098d8 | -8.06527 | -43.12114 | 2025-07-08 03:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 083749ba-03e1-31ae-971a-60ca68a44212 | -6.67223 | -43.77273 | 2025-07-08 03:21:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6609d51-bb06-3bc5-8aa2-658ac48fb6a9 | -7.21485 | -43.12001 | 2025-07-08 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ec8684e0-0c9e-3468-acaa-c73971f4fb00 | -7.18676 | -43.12624 | 2025-07-08 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| b8044569-06fe-3dd7-b514-0e2dd904e215 | -7.19114 | -43.13874 | 2025-07-08 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| a8133538-df81-354a-81e6-376964af0f59 | -6.52975 | -43.53995 | 2025-07-08 03:21:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e185d34f-1c62-39d5-b64c-b5c3202f5888 | -7.24351 | -43.07429 | 2025-07-08 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 61147db1-6175-3d38-8272-c7a3076b6008 | -7.24945 | -43.07821 | 2025-07-08 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| f621f1c7-9c10-31a4-9b2f-d240d9db6624 | -7.10158 | -44.1764 | 2025-07-08 03:21:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba827253-5607-33ff-b146-57afe8612f29 | -7.19328 | -43.12738 | 2025-07-08 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 364a36dc-e9cf-3632-a1b5-e27c9516cf75 | -6.53168 | -43.54289 | 2025-07-08 03:21:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f56dbddf-5abe-300a-bf55-752490004d23 | -7.19979 | -43.12857 | 2025-07-08 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 1b0530af-3f6d-3a8a-bf65-167f00182509 | -7.25546 | -43.08215 | 2025-07-08 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| e4b9dd68-95b1-38cc-a214-013590679a2e | -7.25647 | -43.07669 | 2025-07-08 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| fc45b16f-1e12-396a-9b02-981541845924 | -7.19872 | -43.13425 | 2025-07-08 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 43fca987-0f3d-3f6e-a8d2-8a5c8be42254 | -6.52857 | -43.54637 | 2025-07-08 03:21:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9b292b8e-e6d0-3e60-a129-d8ed13447529 | -6.68016 | -43.76795 | 2025-07-08 03:21:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dba61adc-0185-3f88-b225-91b156f3e6a0 | -8.06629 | -43.11581 | 2025-07-08 03:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.9 |
| 2c65a8d9-b0b7-35dc-8d98-812810ddb4a8 | -7.10292 | -44.16937 | 2025-07-08 03:21:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f4145e5a-01ed-3285-9aed-9fce139b31b2 | -6.67339 | -43.76647 | 2025-07-08 03:21:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b1e501ce-c121-3968-b912-c8ea73e7a2f5 | -7.19221 | -43.13307 | 2025-07-08 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 75ad14d1-c9ab-3220-a6f6-882c2f305e75 | -7.27204 | -44.64922 | 2025-07-08 03:21:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 88df42b2-fee4-3794-9a12-e17e3bc06613 | -7.27607 | -44.64755 | 2025-07-08 03:21:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 060fd953-415f-3cee-a24e-136a0b007cde | -7.20082 | -43.12305 | 2025-07-08 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| cae3b80c-5031-36bb-8b3a-509df365c019 | -6.7294 | -44.33461 | 2025-07-08 03:21:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| aee10d00-7e86-3826-bb45-9cbbd0acaca0 | -7.25443 | -43.08772 | 2025-07-08 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 40045b4e-fb86-3e23-8513-01e58cec3cbc | -7.25488 | -43.08487 | 2025-07-08 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 02242ac9-aa4b-37b8-9e55-2c3e4a611759 | -7.25594 | -43.07934 | 2025-07-08 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 60daf8e1-c15c-375b-a06b-14b4aa6f3848 | -7.24248 | -43.07983 | 2025-07-08 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| ec464595-81cb-311f-b6c6-85865e1ccbc2 | -7.24897 | -43.081 | 2025-07-08 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| d621aadf-95b5-3587-a392-8beff23353ea | -7.22135 | -43.1212 | 2025-07-08 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a986da36-fd43-3d3f-8139-4bf7ee877cb9 | -7.24838 | -43.08376 | 2025-07-08 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 252f6d7e-68fa-30ea-9add-e3af16e7cdd7 | -9.19694 | -45.34153 | 2025-07-08 03:23:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 116ee4ef-41ed-3e3b-843d-a3b8b163b81b | -11.4249 | -45.1135 | 2025-07-08 03:23:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| eb14f2a5-d571-36f7-ae30-d3c5fa218ffe | -11.14269 | -42.3245 | 2025-07-08 03:23:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 34b6d62d-d07f-3bf5-a792-0989649b2482 | -11.8409 | -43.79949 | 2025-07-08 03:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6f2f3a92-2ef9-3f46-ac7f-227454811d56 | -12.98339 | -44.89083 | 2025-07-08 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85ff99f3-633a-30c2-ac24-876098d6625c | -11.41944 | -45.10558 | 2025-07-08 03:23:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| d9a63e73-fb97-35de-919f-99af9ae9272e | -10.97321 | -45.11885 | 2025-07-08 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 625b7558-ddb4-3916-9bf9-a5c390fc4cbf | -11.29251 | -45.26845 | 2025-07-08 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eb0cf182-083b-35d3-bb5b-80b341c09b42 | -11.433 | -45.10861 | 2025-07-08 03:23:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a06066de-6584-322f-a76c-624c3813654d | -11.88608 | -44.92768 | 2025-07-08 03:23:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 639af7f3-f088-33f7-8737-ce022a8f4eb1 | -12.99113 | -44.88651 | 2025-07-08 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3517ccae-ad87-329c-aa58-af6293da05eb | -10.97347 | -45.11695 | 2025-07-08 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e42b5180-3504-337b-b857-a700183b23f2 | -11.44786 | -45.10531 | 2025-07-08 03:23:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bac98606-acd3-3f80-9402-d35f32baca3b | -11.84465 | -43.79815 | 2025-07-08 03:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f3accdd4-44f0-3ad1-bd99-9f23c7af30ce | -9.20406 | -45.3431 | 2025-07-08 03:23:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61aad8cf-776d-324e-9a59-df464b9f205b | -11.43036 | -45.12138 | 2025-07-08 03:23:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3c8b0b56-073c-3420-9a7a-f1a5aea9a598 | -11.43168 | -45.11499 | 2025-07-08 03:23:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 18d1f410-5187-376f-9ca4-4182aafb0347 | -11.88494 | -44.93316 | 2025-07-08 03:23:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d4c821b4-a2d3-3c02-ada3-85323ed46bed | -10.97456 | -45.11237 | 2025-07-08 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 6e30f7d4-3e22-3500-b34d-802b2729b1b7 | -10.97478 | -45.11039 | 2025-07-08 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 4fd7f1a7-d9cf-3daf-b181-055397b22227 | -11.29109 | -45.27531 | 2025-07-08 03:23:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a60bfeb4-2321-3b4d-a088-acf586450724 | -12.98578 | -44.87944 | 2025-07-08 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a008edd2-a4d2-3363-929d-caf221440442 | -11.42622 | -45.10709 | 2025-07-08 03:23:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| f1972217-93eb-36b5-b64f-10389d1340d7 | -14.15359 | -42.573 | 2025-07-08 03:23:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 75c421e6-1bb7-382b-ba9b-c3fd6b1005a5 | -11.83838 | -43.79689 | 2025-07-08 03:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b406451b-a9f4-376e-a8f5-c859dfb63438 | -11.44655 | -45.11167 | 2025-07-08 03:23:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c9886957-c733-3d86-86c8-73f3473ad50b | -12.9846 | -44.88509 | 2025-07-08 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd0e1913-2e46-3404-8740-fcc02f0468a7 | -11.1435 | -42.3203 | 2025-07-08 03:23:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1c51ee05-1646-347a-90b0-a571ae016340 | -11.42754 | -45.10073 | 2025-07-08 03:23:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 340dd603-2bf3-3487-93a1-ce36ea5f847e | -11.43846 | -45.11651 | 2025-07-08 03:23:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| edc6e38c-b0fc-3d9c-808b-b597b12f5906 | -11.43432 | -45.10225 | 2025-07-08 03:23:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| a0fbdcf3-7f57-3cc5-9033-376953d03a2e | -11.83567 | -43.79305 | 2025-07-08 03:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c0cdadc-9550-3cae-96ac-c6213fa72128 | -14.15546 | -42.57456 | 2025-07-08 03:23:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3fd40125-ac48-3046-bd59-d17d40b14fb7 | -11.84192 | -43.79437 | 2025-07-08 03:23:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae08da3e-716e-341e-b489-7472dbd3c3e5 | -11.4181 | -45.11206 | 2025-07-08 03:23:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.6 |
| d687bba4-5d8b-39d2-b910-e54de8b3f826 | -18.2296 | -44.19974 | 2025-07-08 03:25:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5adbe92f-63cf-3b2d-921a-171bdd5b781e | -18.22395 | -44.19818 | 2025-07-08 03:25:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 10.0 |
| bdd937e1-e0a7-3437-8c45-e1602e5536be | -21.62411 | -43.4677 | 2025-07-08 03:25:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3f0d92b6-1980-329c-8bb8-c8df86f4a7f1 | -17.88467 | -39.78725 | 2025-07-08 03:25:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 15b8f5ee-3414-39d9-b24d-9e2f534c238b | -19.59441 | -47.61607 | 2025-07-08 03:25:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 484e9fda-f897-3e9a-a76a-d1de851e99e2 | -16.58565 | -43.64939 | 2025-07-08 03:25:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3883208f-4c8c-3971-b9f5-fa6517bf000d | -19.59291 | -47.62225 | 2025-07-08 03:25:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9c56119f-3f03-32b3-b9ef-7db1becf1eaa | -20.81865 | -43.15116 | 2025-07-08 03:25:00 | NOAA-20 | PRESIDENTE BERNARDES | MINAS GERAIS | Brasil | 3153103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| fb47c3e5-3577-381b-bfff-e08b88b82b70 | -21.07873 | -45.44633 | 2025-07-08 03:25:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 37170415-310b-3983-b73e-f56d22ddb435 | -16.04692 | -43.80389 | 2025-07-08 03:25:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b949a1b5-cc8c-36ca-a203-102c00b446cb | -22.34171 | -41.78452 | 2025-07-08 03:25:00 | NOAA-20 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 87a01c9e-3c6e-3f9f-b599-f37ac756385a | -18.22305 | -44.20231 | 2025-07-08 03:25:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| eecc9ccc-7270-3fe5-9910-73180297a5d9 | -20.91834 | -43.92967 | 2025-07-08 03:25:00 | NOAA-20 | CASA GRANDE | MINAS GERAIS | Brasil | 3114907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 87dc32a2-cc0d-30f0-b0cb-549d5edf0453 | -21.07972 | -45.44201 | 2025-07-08 03:25:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f9b5abe-8e6c-3351-be22-a6db39f44b91 | -16.68027 | -43.88559 | 2025-07-08 03:25:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c33ccd3-15fa-38a1-bb0c-e53031ca0d7e | -21.62482 | -43.46444 | 2025-07-08 03:25:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 581b4220-9b07-3a26-b033-c6aeb500fff6 | -16.57995 | -43.64814 | 2025-07-08 03:25:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 89dcc716-415f-3742-b967-959ad54047ee | -17.88902 | -39.78817 | 2025-07-08 03:25:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 29d22d33-b94c-3991-8a6e-fd53b98cfeb9 | -21.30164 | -48.5648 | 2025-07-08 03:28:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 592fc7f2-1ad8-3f30-8da6-e859e3e99087 | -23.71203 | -47.44244 | 2025-07-08 03:28:00 | NOAA-20 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ce308230-43d2-3e77-9072-a64c88e97d07 | -10.6489 | -49.4483 | 2025-07-08 03:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 58f7a56b-8fa1-3135-b09d-ade107b04ddc | -10.6486 | -49.47 | 2025-07-08 03:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 0bcc11d5-7de2-39d6-877e-47cb2ec53699 | -11.4201 | -45.1181 | 2025-07-08 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| f5b311ca-2f09-3e0b-96c5-04b44752c3b8 | -11.4205 | -45.095 | 2025-07-08 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 1b8ee9af-4456-3a72-b026-3161fc0079bf | -11.4393 | -45.1154 | 2025-07-08 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 75.7 |
| 6c464b29-163a-3ff0-80b8-78e2935f7c2b | -11.4397 | -45.0923 | 2025-07-08 03:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 97.2 |
| c3242263-d639-351f-85fc-13a93e2a5e04 | -10.6299 | -49.4504 | 2025-07-08 03:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| a9f768b2-7dda-317b-beb2-91378ec5fb00 | -11.4397 | -45.0923 | 2025-07-08 03:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 449c7dee-62f7-3ea0-9632-3dfd94ac8011 | -10.6299 | -49.4504 | 2025-07-08 03:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 978f9f8c-d11a-3c8b-a5fe-dd1a2ead342f | -11.4201 | -45.1181 | 2025-07-08 03:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 4d1a42b0-3aa5-3105-912a-8dbb57c952b2 | -11.4393 | -45.1154 | 2025-07-08 03:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 0dc9387c-763d-3fe9-99ba-d922fb89d7e4 | -11.4205 | -45.095 | 2025-07-08 03:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 2ae4342d-2e0f-39e1-bf38-991ea972d245 | -10.6486 | -49.47 | 2025-07-08 03:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 61.1 |


[Clique aqui para ver as próximas entradas](README5.md)
