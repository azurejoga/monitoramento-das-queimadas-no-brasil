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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93ddf879-b4f2-3cba-97c9-76f2ca95106c | -9.5971 | -42.92922 | 2024-10-26 04:19:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 45cbeb6f-2057-33fd-bb3f-c5e8a33eae03 | -9.59652 | -42.93306 | 2024-10-26 04:19:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 01e11ec1-fefa-3935-be71-5aae3f839b60 | -9.47644 | -42.98712 | 2024-10-26 04:19:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c9970b66-4901-3205-96bd-8dadcd223169 | -13.64741 | -44.30224 | 2024-10-26 04:19:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3615bec-bec7-3a3c-8cca-999b9cf54481 | -13.6143 | -43.98691 | 2024-10-26 04:19:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d05a50e8-d854-331d-bf82-20d30f7fa93e | -13.61372 | -43.99082 | 2024-10-26 04:19:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad1f6fe4-a753-396d-a8db-b7d10dfa6980 | -13.61083 | -43.98637 | 2024-10-26 04:19:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b391a48e-2d12-3e87-be4e-2d0bb3e946f3 | -13.61025 | -43.99027 | 2024-10-26 04:19:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6acbe6ac-90c8-3c66-8bf9-c79b898b363b | -13.57077 | -43.74696 | 2024-10-26 04:19:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3d48902c-8dfe-3341-938d-04194502cfa6 | -13.53792 | -44.65961 | 2024-10-26 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4e81327-11d5-356f-9d81-be2b7831cc9d | -13.47595 | -44.02588 | 2024-10-26 04:19:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7f81ee20-8639-3ea4-93d7-52e03fe789c2 | -13.45528 | -44.09394 | 2024-10-26 04:19:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e1a0189b-79fa-3b49-a370-405ade0b8a82 | -13.43109 | -44.35159 | 2024-10-26 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a893f42-07da-341b-b8ed-b600b6229a45 | -13.43053 | -44.35536 | 2024-10-26 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0d42ab7-b33c-33b0-8fc0-0f42653ad293 | -13.35783 | -44.25869 | 2024-10-26 04:19:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b24bdd5-938d-30c7-9d12-3053941c3091 | -13.35737 | -43.92781 | 2024-10-26 04:19:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0bc567d9-5b31-372e-9057-8e4252cc54cc | -13.35726 | -44.26249 | 2024-10-26 04:19:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2278dd25-3869-3084-b88b-930518b4d75a | -13.35669 | -44.26629 | 2024-10-26 04:19:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4dd4bcf6-5ca0-337e-9724-d6d8fc15d8f0 | -13.35383 | -44.26196 | 2024-10-26 04:19:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36a3ca8f-dd2a-33b1-b952-11402ae2013a | -13.35326 | -44.26576 | 2024-10-26 04:19:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 250d4473-d890-38b6-82db-85fbdc82e468 | -13.2948 | -43.95901 | 2024-10-26 04:19:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d53bafb-198c-31d2-9ed8-529ec6ad814c | -13.29133 | -43.9585 | 2024-10-26 04:19:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e183ce7-89e0-34dd-8733-ceb47664d052 | -13.29076 | -43.96234 | 2024-10-26 04:19:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ebd4bb5-332c-3b25-a9f4-c99a4c63ab0d | -13.28729 | -43.96182 | 2024-10-26 04:19:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d32f2913-4f36-309c-b469-b637441d5407 | -13.28438 | -43.95745 | 2024-10-26 04:19:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1516a549-b718-38c6-b0eb-05fd6ec1fe08 | -13.28381 | -43.9613 | 2024-10-26 04:19:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36da5c9d-5b1b-370c-aa49-7f09895391d9 | -13.23933 | -44.46915 | 2024-10-26 04:19:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a12cced3-9efa-3415-a306-9ce1ebeb9526 | -13.23148 | -44.63534 | 2024-10-26 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b48c5c62-041a-3dcc-b2e8-a314cdcf34ff | -13.23091 | -44.63905 | 2024-10-26 04:19:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11de3afa-88f9-3132-aedf-b0fb26a84f9b | -13.21675 | -44.57217 | 2024-10-26 04:19:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a40a9dfa-114a-3d4c-bb93-143f5ef55980 | -13.17941 | -44.58912 | 2024-10-26 04:19:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| becdee86-f65c-3674-b0cc-209e9987e4c1 | -13.02223 | -43.75628 | 2024-10-26 04:19:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aa73c3f6-9958-30e1-a3c1-91e372aa4044 | -13.01874 | -43.75576 | 2024-10-26 04:19:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8679c914-57d5-31b2-84e8-097557351d95 | -12.86465 | -44.61726 | 2024-10-26 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 661d4584-548d-3d6f-9322-14c047b09cc0 | -12.86409 | -44.62094 | 2024-10-26 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79bb29e1-6fa7-34a2-af75-d6205e8269ef | -12.86126 | -44.61673 | 2024-10-26 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cc60dadd-f80d-309f-8211-97c44437845e | -12.71321 | -44.39723 | 2024-10-26 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c3549de-3d5b-3795-a3a5-5a9812303643 | -12.71037 | -44.39297 | 2024-10-26 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5971011d-36f3-3290-a51d-914fe6809596 | -12.70981 | -44.39669 | 2024-10-26 04:19:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c79087fb-a666-3fdc-9741-0b2171131053 | -12.66858 | -44.2064 | 2024-10-26 04:19:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4326f00d-6bf7-3b2e-8ff2-8fc530c58d83 | -12.46971 | -43.79441 | 2024-10-26 04:19:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5b05d3ba-0f8a-301f-b73e-d4428428fa54 | -13.83848 | -43.7351 | 2024-10-26 04:19:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d40ed521-19a6-3842-9fb5-0ee6c6576b88 | -6.45477 | -44.67987 | 2024-10-26 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66f1f780-97c3-36ab-9e05-af262eaed6d7 | -6.45144 | -44.67934 | 2024-10-26 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 43f6f8e5-4166-38ca-b32e-008ce2aa02a1 | -6.40894 | -44.51988 | 2024-10-26 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a50c693-6630-39b6-b1e4-0f30dec12b61 | -6.40562 | -44.51936 | 2024-10-26 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e8b73aa-ea4f-3c87-ba4f-ed86d11caa04 | -6.34764 | -44.56353 | 2024-10-26 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5a3cdf1c-4016-3d9a-aced-8b53e49c2670 | -6.32853 | -44.68483 | 2024-10-26 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3791009c-860f-3c42-bf9f-f9ade50608f2 | -6.25234 | -44.63396 | 2024-10-26 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8694d749-ff94-3352-a65b-76406a7c775a | -6.25179 | -44.63742 | 2024-10-26 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e4779d2-803d-3c21-beba-fa47c358781c | -6.24847 | -44.6369 | 2024-10-26 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8a9c2548-b7f4-3380-826d-a0d6f4445b19 | -6.22632 | -44.62632 | 2024-10-26 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83ba56a0-0c55-3a98-99fa-578541d098d9 | -6.22355 | -44.62233 | 2024-10-26 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 91c338b5-1e17-351d-ae74-d37250d04d96 | -6.223 | -44.62579 | 2024-10-26 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5bb67c96-b517-30af-af8f-a62872a7f538 | -6.22023 | -44.6218 | 2024-10-26 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6d76cc11-1136-34a7-8110-8de9d8c41722 | -6.21968 | -44.62527 | 2024-10-26 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd0d7cfe-1acb-315f-ad31-18eaa61cd3ce | -6.18657 | -44.73002 | 2024-10-26 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb32147a-f1db-3017-9af9-fa4678ab99c3 | -6.08308 | -44.33355 | 2024-10-26 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d358272-e3b9-31c7-8a79-b92f22c85b47 | -6.08175 | -44.70958 | 2024-10-26 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3c91ea44-e7ce-3a27-8796-41c25c0ff768 | -6.0812 | -44.71304 | 2024-10-26 04:19:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3fc18f5a-5caa-344a-8994-e09b53375b9c | -7.30801 | -44.97846 | 2024-10-26 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 89b79591-c9ca-3152-8955-baf13cc36c80 | -7.30634 | -44.96752 | 2024-10-26 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6dd24c94-8c4f-3fa5-b8f7-aebcf9b5e23b | -7.30579 | -44.97099 | 2024-10-26 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 85ee696e-b612-3e2a-a75f-c9d9f2a60fbd | -7.30469 | -44.97793 | 2024-10-26 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e6a46503-fb56-3505-8ec7-88c9c4740b3a | -7.30415 | -44.98141 | 2024-10-26 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1c8dc45-bdaf-3bc7-940c-06d8934e140a | -7.30302 | -44.96699 | 2024-10-26 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b410ae51-79f2-3156-9abc-f10951b51fd9 | -7.30247 | -44.97046 | 2024-10-26 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c54e8c1c-4eb3-3e6d-a9ab-8b807acc0de2 | -7.30137 | -44.9774 | 2024-10-26 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2dc6f61d-5736-3d36-9892-cd145a6f3f17 | -7.30083 | -44.98088 | 2024-10-26 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c676770c-3591-3bfe-8663-20e4c141e0c7 | -7.28864 | -44.97183 | 2024-10-26 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4152a77f-dba4-3cc8-aa2e-2c5df699b73f | -8.76795 | -44.70658 | 2024-10-26 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c82c99d-6341-3be7-af12-2833f0c38e65 | -7.28809 | -44.97531 | 2024-10-26 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7c9679d2-46a6-3064-8a21-e7218a92290d | -7.28477 | -44.97478 | 2024-10-26 04:19:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0699230c-2ce1-357d-8d72-bc537b69969f | -7.02605 | -45.19792 | 2024-10-26 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 70ec6d55-fc61-3eff-b462-6be29939dd9c | -7.02328 | -45.19391 | 2024-10-26 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b84d93e3-43b5-32df-8265-c00cc09525d1 | -8.76353 | -44.71304 | 2024-10-26 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea91a2e8-84ff-3960-9403-8db9c33072ed | -7.02273 | -45.1974 | 2024-10-26 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6a06e4bf-e8b3-3594-aec4-708555a73781 | -6.81958 | -44.4674 | 2024-10-26 04:19:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3fe24fab-4959-38b3-868b-00a526fa42fb | -6.81626 | -44.46688 | 2024-10-26 04:19:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 26667c62-c9d9-338f-9970-8e74d55dd7ce | -6.81572 | -44.47035 | 2024-10-26 04:19:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7ae82554-ac20-3c84-8105-b785837027ff | -6.8124 | -44.46983 | 2024-10-26 04:19:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5cc97ce5-0674-3ff0-b9ac-9c95d05aaa7c | -6.71243 | -44.69953 | 2024-10-26 04:19:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e30cd33d-e183-3324-9505-2481270520ca | -6.71188 | -44.703 | 2024-10-26 04:19:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4559948e-7995-3cac-bac8-2d2d25fae8de | -6.7091 | -44.69901 | 2024-10-26 04:19:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 985aab58-644b-3600-9c61-9726f48b2994 | -6.69067 | -44.16897 | 2024-10-26 04:19:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 60b0839a-4fe4-36df-a37e-299ab560810a | -6.59968 | -44.19069 | 2024-10-26 04:19:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8846220e-e70b-3760-8fe8-8b64448dd228 | -6.5969 | -44.18669 | 2024-10-26 04:19:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f0c8b651-80ca-3539-ba8e-4d871a6c0baa | -6.5575 | -44.37268 | 2024-10-26 04:19:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6630afe9-8e2a-3001-a7f3-073159d0e057 | -8.78739 | -44.73471 | 2024-10-26 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05bd5c1d-30b6-3171-9997-5a002478ce50 | -8.78685 | -44.7382 | 2024-10-26 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50457626-8663-32b8-9259-80f3d3025341 | -8.78407 | -44.73418 | 2024-10-26 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b240ba0-c94a-30ba-972e-dff7c6c56617 | -8.78352 | -44.73768 | 2024-10-26 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6b564f56-4724-3e59-be22-961137cf7ad5 | -8.7807 | -44.71217 | 2024-10-26 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47256a23-2768-3843-869d-d33a9e14be54 | -8.78016 | -44.71566 | 2024-10-26 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c21361d-a7eb-38d6-8a1a-f3850768ff82 | -8.77961 | -44.71916 | 2024-10-26 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 07697a36-e9aa-335c-8aa9-496719111600 | -8.77906 | -44.72265 | 2024-10-26 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b018c53d-9d4e-3f73-8df0-49998eb6d7d5 | -8.77851 | -44.72615 | 2024-10-26 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 804abd3c-a2d2-33c6-bdb7-e274d1793d69 | -8.77628 | -44.71864 | 2024-10-26 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 087e840f-3e94-3841-961f-20d12feba93f | -8.77574 | -44.72213 | 2024-10-26 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0299e4a-2e61-3a7b-858e-6287442cb71d | -8.77519 | -44.72562 | 2024-10-26 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README50.md)
