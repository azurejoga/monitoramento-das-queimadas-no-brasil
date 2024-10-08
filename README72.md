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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb28d666-317b-3086-ad27-eb486f72d1a3 | -20.65623 | -42.09595 | 2024-10-08 04:38:00 | NOAA-21 | CARANGOLA | MINAS GERAIS | Brasil | 3113305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 8609b091-fd7f-3098-8c78-8a02fce26198 | -21.98136 | -42.41903 | 2024-10-08 04:38:00 | NOAA-21 | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 40c4122e-18ab-3ffb-915d-f7f01c5ee22f | -21.97908 | -42.41791 | 2024-10-08 04:38:00 | NOAA-21 | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2cf62519-a9f9-3c06-af00-a8ff62760624 | -21.97804 | -42.42796 | 2024-10-08 04:38:00 | NOAA-21 | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| b57cd154-a564-388c-877b-dccf9dac8794 | -21.9762 | -42.41865 | 2024-10-08 04:38:00 | NOAA-21 | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f3508d9e-8e91-33cd-a997-c64e08c3cf25 | -21.97557 | -42.42516 | 2024-10-08 04:38:00 | NOAA-21 | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 212baa31-4524-3625-86aa-24803c2eb150 | -21.97526 | -42.42845 | 2024-10-08 04:38:00 | NOAA-21 | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| de3bdbbe-834f-30cf-9614-7488f003236d | -21.97391 | -42.4177 | 2024-10-08 04:38:00 | NOAA-21 | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f7da562a-19b0-31b1-81fb-2fd836f8f0df | -21.97132 | -42.41547 | 2024-10-08 04:38:00 | NOAA-21 | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e243e101-556f-335a-a72d-6aa1f3f2030f | -21.97104 | -42.4184 | 2024-10-08 04:38:00 | NOAA-21 | CANTAGALO | RIO DE JANEIRO | Brasil | 3301108 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6e943a7f-133f-3e8d-bc48-a9850f5adfdf | -21.86157 | -43.3786 | 2024-10-08 04:38:00 | NOAA-21 | MATIAS BARBOSA | MINAS GERAIS | Brasil | 3140803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 05711122-3f18-3e32-b344-a22f872530bb | -21.55676 | -42.33215 | 2024-10-08 04:38:00 | NOAA-21 | PALMA | MINAS GERAIS | Brasil | 3146701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| a6a114bb-4abb-301a-adbc-5bc788eda494 | -21.55397 | -42.33105 | 2024-10-08 04:38:00 | NOAA-21 | PALMA | MINAS GERAIS | Brasil | 3146701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 83e959ad-9115-384e-8e86-95bbdc102e87 | -21.55362 | -42.33474 | 2024-10-08 04:38:00 | NOAA-21 | PALMA | MINAS GERAIS | Brasil | 3146701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9f601d62-f968-34b3-8a0c-e3bd41c0beb1 | -21.00731 | -43.05944 | 2024-10-08 04:38:00 | NOAA-21 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8d8c66e4-7a05-3b17-aa61-ec3263895e7f | -21.00244 | -43.05889 | 2024-10-08 04:38:00 | NOAA-21 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| f0873fed-2678-3951-9185-de6b0701ed4a | -20.80424 | -44.50984 | 2024-10-08 04:38:00 | NOAA-21 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| dd7e778b-5aae-33b0-a0d5-55d40f6293a6 | -20.51427 | -44.97856 | 2024-10-08 04:38:00 | NOAA-21 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 21f179d4-885e-38e8-9611-5c8fbb1d9720 | -20.51336 | -44.98021 | 2024-10-08 04:38:00 | NOAA-21 | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 92265fdd-7be0-376b-af92-001bcd693c60 | -20.9177 | -43.74657 | 2024-10-08 04:38:00 | NOAA-21 | CARANAÍBA | MINAS GERAIS | Brasil | 3113107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d1ec6320-bd8f-3a7c-867c-9308ff5b11f8 | -20.91307 | -43.74581 | 2024-10-08 04:38:00 | NOAA-21 | CARANAÍBA | MINAS GERAIS | Brasil | 3113107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 99402aa7-4829-3aaa-aa48-545e24c8f32d | -20.45062 | -43.80305 | 2024-10-08 04:38:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| bbc0ab5d-4f3a-39b2-ab3b-f28065dfc655 | -20.45043 | -43.80391 | 2024-10-08 04:38:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 4de140c1-c042-32a2-8248-83349dd0bbfc | -22.04202 | -45.17038 | 2024-10-08 04:38:00 | NOAA-21 | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 3f168f99-1b2c-3ecf-8290-f9a463ab012c | -21.71301 | -44.65239 | 2024-10-08 04:38:00 | NOAA-21 | MINDURI | MINAS GERAIS | Brasil | 3141900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e5c20ce6-09f5-351e-8867-0d8f866d5deb | -21.68774 | -43.9792 | 2024-10-08 04:38:00 | NOAA-21 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 35dd78dd-b3dc-3352-99c1-96d38f971214 | -21.68313 | -43.97858 | 2024-10-08 04:38:00 | NOAA-21 | LIMA DUARTE | MINAS GERAIS | Brasil | 3138609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 28896de8-88eb-3aef-a617-1f09749b88dd | -21.14443 | -43.75903 | 2024-10-08 04:38:00 | NOAA-21 | ALFREDO VASCONCELOS | MINAS GERAIS | Brasil | 3101631 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2ead7ea8-eb52-3229-9580-e64316ff4892 | -20.76439 | -46.36852 | 2024-10-08 04:38:00 | NOAA-21 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| faea05ac-a42a-313b-95c5-dbc50f6cb80d | -20.76048 | -46.36791 | 2024-10-08 04:38:00 | NOAA-21 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fe119571-b328-3258-81d8-20f75be64cb4 | -20.65338 | -45.91868 | 2024-10-08 04:38:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b300e6c0-eb9e-3b24-9427-a4afc2a8a32e | -20.65294 | -45.92224 | 2024-10-08 04:38:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fdfa9809-4960-3c6c-abe2-88020ba26608 | -20.65247 | -45.92596 | 2024-10-08 04:38:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28ebeb8e-b081-324a-965a-3cfdd951b011 | -20.6489 | -45.92177 | 2024-10-08 04:38:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f033e13c-f5ae-30f6-a854-b38beb22396e | -20.64846 | -45.92535 | 2024-10-08 04:38:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e93de668-79ad-3092-8169-c2ef94217d0c | -20.64801 | -45.92894 | 2024-10-08 04:38:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80fb6f03-dfe1-3ce4-b49f-4206e1249cb0 | -20.64445 | -45.9247 | 2024-10-08 04:38:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23b33b2c-6245-39c4-b77a-195bfd1af184 | -20.64401 | -45.92822 | 2024-10-08 04:38:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| df31359b-9be1-38db-9e98-739035a27c47 | -20.32228 | -46.26567 | 2024-10-08 04:38:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba147632-8120-383e-a8de-c00daf253581 | -20.3216 | -46.27095 | 2024-10-08 04:38:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 95a712cc-9ae3-36ed-8910-996880c4102d | -20.31768 | -46.27042 | 2024-10-08 04:38:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c11f62f5-8406-3d9e-b117-e6d0ec0eb28e | -20.36401 | -45.2195 | 2024-10-08 04:38:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 25bdc7a3-c8d7-3bd2-b5cd-a59dc844bdad | -20.99041 | -45.83759 | 2024-10-08 04:38:00 | NOAA-21 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 14fbcbc8-e24b-332f-8cbd-3e8b2bcce460 | -22.12441 | -46.0417 | 2024-10-08 04:38:00 | NOAA-21 | CONGONHAL | MINAS GERAIS | Brasil | 3117900 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fe640ea1-cd6d-30e0-bc70-bbb815e27e84 | -21.96755 | -46.5451 | 2024-10-08 04:38:00 | NOAA-21 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a9669bf6-9d1e-3069-a570-265abe31a65d | -21.96688 | -46.5505 | 2024-10-08 04:38:00 | NOAA-21 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e4aa0e76-f305-30c5-89ed-9c4f48f47222 | -21.89088 | -46.70996 | 2024-10-08 04:38:00 | NOAA-21 | ÁGUAS DA PRATA | SÃO PAULO | Brasil | 3500402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a0647697-ab62-3562-b648-0afdcee2e321 | -21.89015 | -46.71569 | 2024-10-08 04:38:00 | NOAA-21 | ÁGUAS DA PRATA | SÃO PAULO | Brasil | 3500402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8424e48d-f5c9-3c61-93eb-348a371adf82 | -21.81738 | -45.68082 | 2024-10-08 04:38:00 | NOAA-21 | CORDISLÂNDIA | MINAS GERAIS | Brasil | 3119005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| be1aacd7-58dd-38e0-a48c-de2d0713e6b6 | -21.28365 | -46.65331 | 2024-10-08 04:38:00 | NOAA-21 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3078dc5a-06aa-3062-9eeb-1a8a348a4a41 | -21.20261 | -45.79435 | 2024-10-08 04:38:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| e1901ea1-7a3b-3e9a-a7fa-389475f79c1f | -21.20214 | -45.79814 | 2024-10-08 04:38:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| cdd53155-4ea7-33d2-96d6-7ed3266250a2 | -21.15311 | -45.82822 | 2024-10-08 04:38:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 305cb0ce-dac1-3441-af01-7d1c35440dbe | -21.14907 | -45.82745 | 2024-10-08 04:38:00 | NOAA-21 | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0c1e57e7-6799-3462-b4a5-6d57e879de1d | -21.14322 | -46.77145 | 2024-10-08 04:38:00 | NOAA-21 | JACUÍ | MINAS GERAIS | Brasil | 3134806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 73739764-3e79-3155-9850-0d06b0f0a6c3 | -20.99613 | -46.08696 | 2024-10-08 04:38:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 24a274fc-0138-3eaf-a412-1d6658bd655b | -20.98026 | -46.08362 | 2024-10-08 04:38:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 228f357c-8eee-355e-ad3b-e92c6b15f817 | -20.9763 | -46.08278 | 2024-10-08 04:38:00 | NOAA-21 | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 7c72387a-3cbf-3378-affc-f14d1ef16de1 | -23.33969 | -46.77173 | 2024-10-08 04:38:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| e223c10f-8144-3b65-8d24-08225d739a80 | -22.5831 | -46.66338 | 2024-10-08 04:38:00 | NOAA-21 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e6994b5b-fa11-3b47-b94e-1967211a9ebf | -22.57908 | -46.69629 | 2024-10-08 04:38:00 | NOAA-21 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 2519e8a2-4e3f-38ee-89eb-ceb3089f3023 | -22.57614 | -46.6609 | 2024-10-08 04:38:00 | NOAA-21 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 412a4152-4c9b-3438-a01c-5f9eede2d771 | -22.57586 | -46.68988 | 2024-10-08 04:38:00 | NOAA-21 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 53d78380-1cb4-30cf-b431-89e82efccaa5 | -22.57584 | -46.69442 | 2024-10-08 04:38:00 | NOAA-21 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| be4d1019-c8aa-316b-b418-61d5de2ca277 | -22.57526 | -46.66185 | 2024-10-08 04:38:00 | NOAA-21 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| a13ff9e7-7633-3753-9b63-6e5922a94705 | -22.57518 | -46.69951 | 2024-10-08 04:38:00 | NOAA-21 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| 9c601b15-33f9-32d4-aae7-e0ce30ca08cc | -22.57518 | -46.6954 | 2024-10-08 04:38:00 | NOAA-21 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 603be122-a779-3181-aaec-8607afc12da2 | -22.57456 | -46.70041 | 2024-10-08 04:38:00 | NOAA-21 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| db7e0662-cfb9-3469-9a94-c75319729fa7 | -22.5726 | -46.68842 | 2024-10-08 04:38:00 | NOAA-21 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 8d0ab52f-347a-304f-98b6-4d5ab427d36d | -22.57193 | -46.69363 | 2024-10-08 04:38:00 | NOAA-21 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 9ca70df1-0c1d-3490-bb0e-4ee29871187b | -22.5719 | -46.68944 | 2024-10-08 04:38:00 | NOAA-21 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 36e0250f-5c71-36dc-885b-5cdc4b5a18ac | -22.57128 | -46.69456 | 2024-10-08 04:38:00 | NOAA-21 | SERRA NEGRA | SÃO PAULO | Brasil | 3551603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 36e58f3f-cd4f-3a37-ad06-dc7d45eedb00 | -22.49897 | -46.12573 | 2024-10-08 04:38:00 | NOAA-21 | CAMBUÍ | MINAS GERAIS | Brasil | 3110608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 346e9432-9ed1-3919-9a63-308d46a91ae1 | -22.40952 | -46.61727 | 2024-10-08 04:38:00 | NOAA-21 | MONTE SIÃO | MINAS GERAIS | Brasil | 3143401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4e7b9617-9e76-3fe3-9879-1ce02fe5c055 | -23.45204 | -47.27334 | 2024-10-08 04:38:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 39fb98b7-821b-3870-bd6e-4f89c9582e8c | -23.39846 | -47.00791 | 2024-10-08 04:38:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 354dd71a-28fc-3e93-8d01-a0a9780cc968 | -23.39843 | -47.00587 | 2024-10-08 04:38:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5c75d73d-7778-3a95-a539-3db01ad50849 | -20.69631 | -47.60027 | 2024-10-08 04:38:00 | NOAA-21 | BATATAIS | SÃO PAULO | Brasil | 3505906 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ad64e6a8-1a1e-355c-a007-66b2d6bb2998 | -20.69265 | -47.59976 | 2024-10-08 04:38:00 | NOAA-21 | SÃO JOSÉ DA BELA VISTA | SÃO PAULO | Brasil | 3549508 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e4581255-e8ad-32a1-96f2-691fcbbcfb64 | -20.68508 | -47.17674 | 2024-10-08 04:38:00 | NOAA-21 | ITIRAPUÃ | SÃO PAULO | Brasil | 3523701 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| adb465fc-9fe4-36d9-81ee-2c8878ecc1ce | -20.68446 | -47.18142 | 2024-10-08 04:38:00 | NOAA-21 | ITIRAPUÃ | SÃO PAULO | Brasil | 3523701 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba3b0329-67db-3cf3-ae9a-7781f5139a89 | -20.68134 | -47.17617 | 2024-10-08 04:38:00 | NOAA-21 | ITIRAPUÃ | SÃO PAULO | Brasil | 3523701 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef2e05c4-bf0b-31e6-879d-3ba8829f030a | -20.68073 | -47.18082 | 2024-10-08 04:38:00 | NOAA-21 | ITIRAPUÃ | SÃO PAULO | Brasil | 3523701 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb0a8709-7aec-326d-8326-a21409fd9c25 | -20.47489 | -47.69101 | 2024-10-08 04:38:00 | NOAA-21 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99aa3580-b63d-3972-9a34-a7f3458b77dc | -20.47427 | -47.6955 | 2024-10-08 04:38:00 | NOAA-21 | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8adcf949-5a69-380a-9027-56fa805b143d | -20.458 | -47.62479 | 2024-10-08 04:38:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bbc56456-9891-3eb7-9fb7-27550b34c61b | -20.45436 | -47.62421 | 2024-10-08 04:38:00 | NOAA-21 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e9df9183-7d27-325a-9a2c-ffbdbda31dff | -20.43559 | -47.68019 | 2024-10-08 04:38:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b68a348-994b-34f8-9589-061161079d21 | -20.43375 | -47.6664 | 2024-10-08 04:38:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ef4c8ad-904b-36e5-91b4-4b419541b890 | -20.3675 | -48.84114 | 2024-10-08 04:38:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 209.7 |
| 94ddd4fa-6f6f-36ad-a6cd-c76cb6dd035a | -20.43133 | -47.65693 | 2024-10-08 04:38:00 | NOAA-21 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d28408a4-b17e-3756-b772-bd9f62fe8d6c | -20.43073 | -47.66132 | 2024-10-08 04:38:00 | NOAA-21 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8e8f5bf1-371f-34cd-a9a6-8de5760c8c21 | -20.43013 | -47.66575 | 2024-10-08 04:38:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4e95576-47f8-3023-b27d-6d59eb924b86 | -20.42833 | -47.67902 | 2024-10-08 04:38:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d8a0d827-6e0d-3b34-abd7-6964c47ebe8b | -20.42772 | -47.68346 | 2024-10-08 04:38:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2794d93f-8513-3aee-8700-591db29310cd | -20.4277 | -47.6563 | 2024-10-08 04:38:00 | NOAA-21 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ae03be42-b9fd-38ac-9e0e-a743d6ac4052 | -20.42711 | -47.66067 | 2024-10-08 04:38:00 | NOAA-21 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ae10d497-6e95-384c-bdeb-c2cdb733fd0d | -20.42651 | -47.6651 | 2024-10-08 04:38:00 | NOAA-21 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 92a57b3a-9e3e-3014-8851-4e1d4f8a8f4d | -20.4259 | -47.66959 | 2024-10-08 04:38:00 | NOAA-21 | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8c422152-e9d4-36aa-b584-3e68225f1094 | -20.42587 | -47.64245 | 2024-10-08 04:38:00 | NOAA-21 | RIBEIRÃO CORRENTE | SÃO PAULO | Brasil | 3543105 | 35 | 33 | nan | nan | nan | Cerrado | 9.8 |


[Clique aqui para ver as próximas entradas](README73.md)
