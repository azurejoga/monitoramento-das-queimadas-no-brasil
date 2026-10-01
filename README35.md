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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08022da4-0249-394e-9c48-770e8b47790e | -9.07053 | -49.87581 | 2026-10-01 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f07c298a-a764-3bae-938f-9f95e2d070bc | -5.74944 | -45.16241 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 3eb2aa64-ff70-3b50-ade7-d8d9b89a6536 | -4.25207 | -50.78408 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bb36e62a-e5fa-35bb-8578-0e2a70c431e4 | -4.28931 | -50.74259 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a1139ff7-4253-30f2-b7af-ebb961232f0b | -8.36819 | -45.38189 | 2026-10-01 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bcfe5d0-7314-3a29-a512-bc781970ce81 | -4.25885 | -50.80591 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a5fe0c49-8004-369f-bf92-0714646d6ceb | -4.24998 | -50.75935 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| a2322bfe-08ac-374f-ba72-3f78a9c9bfa0 | -4.2823 | -50.74622 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c832b5a4-7924-3afe-859d-3967de862275 | -7.19113 | -46.50197 | 2026-10-01 04:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9e1d3a4c-cc5e-3778-b8d0-809cbd91a4cb | -4.28921 | -50.7906 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 970c54df-1db3-3bbe-9aa6-d9498b007621 | -4.28615 | -50.79607 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| b29e3f80-01c9-327b-b1c8-5ac58259b12e | -4.26305 | -50.78251 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 5598bf61-0497-3425-996f-5d891117a90a | -4.31963 | -50.7871 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d19d7fd5-e457-37f1-b7f4-523776f82a36 | -4.26223 | -50.78706 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 49ea0275-1c07-33a6-8040-c4dd7ec76d34 | -6.0062 | -49.56002 | 2026-10-01 04:14:00 | NPP-375D | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f01e9bce-27f0-3cc9-9536-2e35b8759359 | -8.49644 | -44.75285 | 2026-10-01 04:14:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99435372-c47d-347b-8337-34cc3c59b570 | -7.12111 | -43.16045 | 2026-10-01 04:14:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 5c8f5365-edf9-3400-8f4a-73bdd2e2e7b3 | -11.44749 | -43.45747 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7517188-9aa2-33e0-83ca-40b10369254e | -4.25533 | -50.76527 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 930f045d-cc15-3ee8-95e1-3412e466c926 | -5.74655 | -45.15414 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 25c5de46-c36a-3ff5-acf3-9a6215676121 | -11.3833 | -43.36631 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| de9a52de-8a5b-3262-9cf7-bc90fed0551d | -7.50161 | -45.83728 | 2026-10-01 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| df0515df-2634-3d1d-b46c-ac3126c70d3f | -4.45369 | -47.92308 | 2026-10-01 04:14:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| deb98bcb-82c0-3c06-8a92-1f7494dff891 | -11.38394 | -43.3624 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f1bd750-2435-35f6-9217-95209a0d6c68 | -5.74592 | -45.15789 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 9041913c-a689-38d8-b44d-d8216b96ff17 | -11.43303 | -43.41463 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7589ef06-fca2-372d-979b-94d858291fbc | -4.28708 | -50.76581 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 316.9 |
| f0256389-7c62-38e1-8378-723d42097dba | -7.3238 | -42.08294 | 2026-10-01 04:14:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 502d67a9-eb08-323f-af43-071e7f77dd07 | -4.27992 | -50.79525 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 7eddcacb-357c-398a-aebe-64f05fd47f42 | -4.29203 | -50.76305 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| bd27ae0a-fa14-3137-be0f-abc74e93440e | -4.26654 | -50.76309 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 3abd2b85-94b7-3e22-8ab2-46403d6cbeae | -8.01557 | -42.88151 | 2026-10-01 04:14:00 | NPP-375D | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4bf83066-3a16-3eca-8458-5f7c0c91137c | -4.29679 | -50.80807 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 351dff5e-d2f0-3691-bba6-19cac4d0e8f4 | -4.287 | -50.79132 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 3f3de4e6-9778-367a-84b2-09a46f8a9199 | -10.4089 | -53.7804 | 2026-10-01 04:14:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 072997cc-20ea-31c5-bd34-9e9a87da375c | -10.25085 | -49.67073 | 2026-10-01 04:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0587ee23-4510-3d82-9c68-532be0290c20 | -10.7873 | -50.53038 | 2026-10-01 04:14:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5ede8ca8-7e38-3f86-9b4d-8d45e878a43a | -4.27514 | -50.79831 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b5075950-9660-3b57-8199-32417519d02d | -4.85842 | -45.84242 | 2026-10-01 04:14:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6c4cc680-ee62-3da9-9773-1b052b8fa306 | -5.91184 | -53.49409 | 2026-10-01 04:14:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a1dde383-1fe3-3c3d-96ca-98b280a4d645 | -9.79692 | -44.81414 | 2026-10-01 04:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11190002-3aa5-3c57-a36f-3df152c6209b | -11.25498 | -43.53053 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 77d3602f-6cff-3829-bcd5-508948385956 | -7.85031 | -45.82307 | 2026-10-01 04:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e089d967-9f7a-3060-82c4-a2699037a106 | -7.06802 | -42.32385 | 2026-10-01 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| d7a26310-c24c-37f4-ad02-f3bc67b504be | -11.44068 | -43.41191 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| e5cd6fe4-1b48-35b6-ab46-6cbd08847083 | -4.28188 | -50.82005 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 59dfc321-1de6-32a5-9e2e-ee16dd09a167 | -4.25796 | -50.81083 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6f1a542f-d4e7-38d6-9adf-1bc337c5724d | -4.27273 | -50.7641 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 789ce36b-2f51-3943-a5ac-bdb40dd9c986 | -8.37817 | -50.72861 | 2026-10-01 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 16661983-e8ca-3243-81ab-582b98483657 | -8.24571 | -45.43884 | 2026-10-01 04:14:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ef1c8d7d-d519-32f7-95df-dadb2e476351 | -11.45579 | -43.45084 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6a099462-1860-310c-b1e8-ec4877be129d | -4.28973 | -50.81188 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0043af5c-0064-3495-bc0a-efdd7fd57740 | -6.92185 | -44.56273 | 2026-10-01 04:14:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d675a120-d9b4-3d3a-988b-41be193dab21 | -12.3562 | -46.38287 | 2026-10-01 04:14:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c4c7d8b5-1463-370a-9686-fb8fdd8dd989 | -10.56668 | -50.05284 | 2026-10-01 04:14:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 961145ed-380a-3f3f-9510-6632b7f4e2bf | -10.73471 | -44.4147 | 2026-10-01 04:14:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f4c433b8-ce00-3755-8f1c-297044ff63fa | -4.30808 | -50.78031 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7e7cf451-0c03-3f95-a448-eab922f1a599 | -11.19162 | -45.16269 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e34569b5-b16d-3917-86dd-df5030f77149 | -4.26672 | -50.79765 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a6acf882-16b8-3100-a8e4-0d97c1605504 | -11.61927 | -43.554 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d760d57d-3d1e-3ed0-adef-ba0b2fea6109 | -7.11749 | -43.15985 | 2026-10-01 04:14:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 0f5c35a1-b504-307a-8fd3-e34ffcf9e6d0 | -5.60606 | -46.25252 | 2026-10-01 04:14:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b30703a-d987-311e-adfa-dc5a3b2b1225 | -11.38045 | -43.36181 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dc0effb9-4085-3424-b26f-276b141fdbc9 | -12.17884 | -47.382 | 2026-10-01 04:14:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8011036d-7dcf-3066-9fbe-f0d90de700f2 | -4.28019 | -50.82959 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ec2db8b6-28ec-3e2c-9f75-02604ce7327f | -5.42959 | -43.45269 | 2026-10-01 04:14:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6430f459-2126-3bb9-86be-a30dc4b9b2c1 | -9.08476 | -49.88924 | 2026-10-01 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd49b889-c86b-3e64-a1d3-a6d02fee80b8 | -5.56914 | -45.07596 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fe0ce5df-0c06-3ffe-9a6f-692391605666 | -4.2737 | -50.79433 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| eea5168b-3680-3dbb-9289-880023e5b095 | -12.51262 | -43.0993 | 2026-10-01 04:14:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| eb3f8bcc-513a-353d-a584-545b3eef5151 | -7.11456 | -43.15508 | 2026-10-01 04:14:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| b086e8ec-ec4c-39d0-9405-9cefdedf5629 | -5.10392 | -45.66544 | 2026-10-01 04:14:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 8d827498-3175-314b-a50a-ade0039d45cf | -12.35743 | -46.37587 | 2026-10-01 04:14:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a2f873a3-3870-31a2-a8b2-3b4dc5a69377 | -10.91667 | -43.84542 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd5900aa-9b3e-38ab-8581-07dbf274fc69 | -12.20809 | -43.83354 | 2026-10-01 04:14:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec1e5cb8-ea7c-3cf2-8ed0-78445c076cc5 | -9.81142 | -44.82148 | 2026-10-01 04:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 266e5d27-bc53-3b91-80e4-874d738a1759 | -7.85381 | -45.82779 | 2026-10-01 04:14:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 16c0d933-cc75-32e1-a765-9af8d83c2e1d | -5.44382 | -43.74237 | 2026-10-01 04:14:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5ea50c61-5577-3632-a252-a2f769aee08c | -4.26287 | -50.79544 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ea5bc516-d155-3e83-8627-c8a87caf659c | -11.38615 | -43.37082 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5fcd5511-9116-3ed6-9101-604bb5dd8f6f | -4.30192 | -50.77913 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| ee4152e0-550d-3457-b1ec-b04295c50b42 | -11.39702 | -43.37226 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6139266f-b104-329c-9d7e-64e64b47d8da | -4.25619 | -50.8342 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dc8a5964-4aa9-373d-b18d-ee2200cabe82 | -4.26325 | -50.81697 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4c23dfe5-a369-3f95-836c-d36cccf0ce5f | -12.45417 | -44.19139 | 2026-10-01 04:14:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 08f4d157-3110-383d-b2d0-8981fde27d3b | -9.08541 | -49.8858 | 2026-10-01 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03d8164b-dfda-3a18-a408-9edfa9ca0365 | -11.21107 | -45.1541 | 2026-10-01 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3709bc2f-5a37-36f3-b16f-6a8834592198 | -7.02608 | -45.27965 | 2026-10-01 04:14:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a4890cdd-6185-3ae9-98c5-dbae89c115f0 | -4.27437 | -50.75499 | 2026-10-01 04:14:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| a4d4a759-d6d2-3018-9925-223bb70e9700 | -5.75295 | -45.16696 | 2026-10-01 04:14:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2354abc8-df17-394b-a6e1-25cbfff3586b | -9.12281 | -49.92521 | 2026-10-01 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6bdfc442-0b6d-39c7-befe-d34f7df47b48 | -5.4266 | -43.44755 | 2026-10-01 04:14:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 519ba010-c851-322f-b05e-8083212bad9e | -8.62363 | -45.3721 | 2026-10-01 04:14:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d49b7bcb-1106-35e9-8fec-a79173f431c0 | -12.45059 | -44.19077 | 2026-10-01 04:14:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 9.9 |
| c4f13f45-3679-3b10-8258-a132cc1c09d2 | -6.14042 | -53.25796 | 2026-10-01 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f9e0ad19-fe50-355a-be8e-0fb0f99a3696 | -9.8098 | -44.83103 | 2026-10-01 04:14:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a8a41d7-0292-3449-9b2c-970323d7b0a7 | -4.25687 | -50.78138 | 2026-10-01 04:14:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| e0808feb-4054-3b9c-a71d-6bc75b3a5d63 | -11.41206 | -43.41103 | 2026-10-01 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4548a446-e0b2-39ce-8e0e-3d38171179c3 | -11.68083 | -43.22789 | 2026-10-01 04:14:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1ae68697-c681-3eb9-be72-ca31938c598a | -5.08353 | -45.7868 | 2026-10-01 04:14:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README36.md)
