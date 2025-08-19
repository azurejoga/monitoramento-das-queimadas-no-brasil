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
| 36002fad-86c2-3811-be3e-17282976d7b8 | -5.65805 | -43.3774 | 2025-08-19 03:34:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f458c17c-57d9-34fe-8afa-40ae6e8d24ed | -5.65741 | -43.38111 | 2025-08-19 03:34:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96a916d7-feb8-34e2-bd87-6b83c67f835e | -5.78583 | -43.61251 | 2025-08-19 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 07c061f7-c0c1-326b-a157-e58a240d4c68 | -4.00027 | -43.26921 | 2025-08-19 03:34:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f15f9619-defc-317c-a0f5-4a2c281b2816 | -3.96948 | -42.52004 | 2025-08-19 03:34:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 74651487-614c-33e1-8d83-664c65e1c0f0 | -3.97647 | -42.52207 | 2025-08-19 03:34:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 65599811-ec3c-35d9-b9c9-8b5660da8bf6 | -5.64228 | -43.40202 | 2025-08-19 03:34:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dc662b94-e6fc-31cd-a268-6214e49c8f06 | -3.97829 | -42.51163 | 2025-08-19 03:34:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 745eade0-4c68-3b67-afca-b0429100558f | -5.6538 | -43.39118 | 2025-08-19 03:34:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2ded53a2-dec8-3455-aa23-a93be5f6e30d | -3.98189 | -42.52297 | 2025-08-19 03:34:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9d47bda4-ff82-3412-a094-f882db15a91d | -3.97768 | -42.5151 | 2025-08-19 03:34:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 91f46b4f-b61a-3275-b80b-553e69d230aa | -5.65182 | -43.38019 | 2025-08-19 03:34:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e01515be-52f6-3283-97fd-c7b4e63c7dde | -3.97944 | -43.24264 | 2025-08-19 03:34:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5ffff9b-02f7-3184-9041-964a64bb8124 | -3.25379 | -43.27345 | 2025-08-19 03:34:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cc5d3146-d888-305f-ae7f-9ce6cfead70a | -5.37368 | -42.3335 | 2025-08-19 03:34:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cfe165bc-3a47-3c5d-becb-104e026e5ae1 | -3.81778 | -41.56989 | 2025-08-19 03:34:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0b45a6b1-f850-37f5-afe4-5b0499df51c5 | -5.65054 | -43.3876 | 2025-08-19 03:34:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8d9dd36-0943-3baa-9dce-ca28b901824a | -4.14776 | -46.45483 | 2025-08-19 03:34:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fd327a1e-e980-3150-908b-22716c7210dc | -4.58785 | -43.31656 | 2025-08-19 03:34:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 07224ac3-b80e-31ee-961d-58f4450168b9 | -3.8183 | -41.56688 | 2025-08-19 03:34:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 495558c9-ce33-3792-b2be-71a7b05ebc2d | -5.78085 | -43.60774 | 2025-08-19 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 8f196d02-4e16-3f20-bed7-763e6d488113 | -5.78649 | -43.60879 | 2025-08-19 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 5acc48dd-bf4d-3cd8-ba09-d116d806c951 | -3.97006 | -42.51656 | 2025-08-19 03:34:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 75a5f9db-341c-3126-9f50-adc776849b2c | -3.98731 | -42.52387 | 2025-08-19 03:34:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 953073ee-9f17-35a1-8a0e-7e6769a842d6 | -6.74517 | -41.54856 | 2025-08-19 03:36:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 49fc4059-48e1-38cd-8bbf-0dea5b5feecc | -7.29045 | -43.69234 | 2025-08-19 03:36:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fd51f483-e5f3-395a-8da8-a2ed1231b616 | -7.63114 | -46.2274 | 2025-08-19 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8970f75e-911c-3552-99cf-75f1d532c76f | -12.0384 | -44.01262 | 2025-08-19 03:36:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ca633751-8f14-3adc-94f6-5d1e4ef18ad3 | -6.93172 | -43.60895 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e2b31c7-bdf1-31c8-939c-8c854a75e3c5 | -6.93238 | -43.60518 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3416e323-5bb3-3790-844c-23ba43caa82b | -6.93663 | -43.6072 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18a95984-b364-3fc5-9695-6365f327a2fe | -7.01794 | -44.27544 | 2025-08-19 03:36:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59f2a880-be53-3e86-8732-426652dd767f | -5.96997 | -44.28858 | 2025-08-19 03:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb007d7a-8aec-3893-8cd8-5126296d18a9 | -12.03773 | -44.01605 | 2025-08-19 03:36:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8d08a481-a45e-35d2-a9ae-03e6a4b9a46a | -7.62569 | -46.22096 | 2025-08-19 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 525f780b-f0e8-30c1-bbb5-a0669854f8a9 | -6.93731 | -43.60344 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a422aee2-82a5-3516-b9c1-0525bb744ec2 | -6.94905 | -43.60185 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e2d48c02-667e-3895-a919-de29c119cd86 | -7.62576 | -46.21831 | 2025-08-19 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 66e9284d-fb59-3e7e-8946-a624d12e13dd | -6.94772 | -43.60917 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 239beaca-7d03-3336-a2e9-8583d06318ee | -6.94973 | -43.59808 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a2b37af4-690e-341b-9d92-c595a15a08ff | -8.17892 | -43.27654 | 2025-08-19 03:36:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 353f344e-9e6f-3653-b6b7-d5e57ae84be6 | -11.81214 | -44.26002 | 2025-08-19 03:36:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86939825-9d3e-3e01-8dfb-c11febfb7fbf | -6.92942 | -43.5894 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 6e9caa64-c56e-3414-afe9-569422355be0 | -5.97741 | -44.11764 | 2025-08-19 03:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9b564615-4641-3e1b-8c46-74a931e32a73 | -6.96148 | -43.59632 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 286473b9-eb55-36e3-9026-dc728f35a114 | -6.9462 | -43.58599 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 360fe7a2-50da-331c-bb34-22487a93f395 | -6.96346 | -43.58537 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 23ee04be-cdee-3c83-9037-9bccd07a075a | -6.93106 | -43.61274 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b702e05-7639-32ca-ad4c-6c3adcdd46f7 | -12.03255 | -44.01492 | 2025-08-19 03:36:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b341152c-261c-3d78-8d17-0b6ccd4f1c2c | -8.09238 | -44.84277 | 2025-08-19 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 674f3281-4b8e-3f12-a7c5-021be6b6dcf3 | -6.74295 | -41.54177 | 2025-08-19 03:36:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 2c650cff-af1a-33c3-b488-89f0e0b354dc | -5.97307 | -44.13743 | 2025-08-19 03:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 868731a6-a2c6-30fe-8f8a-5870ab80f46a | -7.58787 | -45.42525 | 2025-08-19 03:36:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 82154d97-b280-34bb-8fd3-85d313da1855 | -6.93868 | -43.59592 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 2fe8e271-4701-39ff-8cab-c9755e7c25e4 | -6.9275 | -43.60038 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 186e236a-b5ef-371c-b2f0-3759f4a359a6 | -6.74203 | -41.54721 | 2025-08-19 03:36:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| aab8988a-0918-3735-9cf6-6e2a6bdde594 | -7.63028 | -46.23001 | 2025-08-19 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 41263cb9-45cb-359d-a35b-b5d5348f69d1 | -6.52986 | -43.44081 | 2025-08-19 03:36:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 789695a8-dc44-3ea6-977e-a32ee5c60cac | -6.74871 | -41.53724 | 2025-08-19 03:36:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b55520eb-4eb5-3aad-85b1-8b5fdbafe959 | -6.7478 | -41.5426 | 2025-08-19 03:36:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 93c6617e-7508-3fc3-84d4-2454214e68eb | -6.93949 | -43.623 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0a9d6ddc-f805-3bb9-bf1f-a0bd6c81a65b | -6.74613 | -41.54315 | 2025-08-19 03:36:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| dc973e99-0770-3227-a281-4e4b0fb3915f | -11.27626 | -40.45834 | 2025-08-19 03:36:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 663f075a-cdc4-3c56-9e45-c847ace03c48 | -5.74795 | -46.68068 | 2025-08-19 03:36:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a3a72c73-e3d2-3e94-b12b-2191418b4337 | -6.41336 | -42.49623 | 2025-08-19 03:36:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 82339872-a261-3f62-93cd-92b749961eb8 | -6.95174 | -43.58699 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79c5a0c2-3de8-3fbf-977e-d3c0efbd4b8d | -7.00551 | -44.27828 | 2025-08-19 03:36:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f66a1b92-504c-39b2-ad90-9d414f52369e | -6.93393 | -43.62207 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 29182f9f-a1e7-3415-bf4b-d6fe6dcc1b32 | -6.51797 | -43.44351 | 2025-08-19 03:36:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 438ec614-e9c1-3854-bae9-601f80af061f | -6.94217 | -43.60822 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 165c9ff3-179d-34d0-94d7-3f215a3d51b9 | -6.96012 | -43.60387 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 429f9343-b075-3e7b-99cc-5f4eca692ad3 | -12.03831 | -44.01234 | 2025-08-19 03:36:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ae85f8e1-35da-373f-9f18-8659acecdd6b | -6.9276 | -43.59394 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 59b263c2-5068-387d-a29a-1dca66324671 | -9.26744 | -44.54057 | 2025-08-19 03:36:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 412ad3ea-7a1d-3261-bdfa-ad0ee34ecab4 | -8.09076 | -44.84147 | 2025-08-19 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f6d45026-f90e-31cc-ab28-fafffff5c943 | -6.92685 | -43.60409 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c37ba377-d3a6-300c-8d53-9e88fd40aacc | -6.9442 | -43.597 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cb567c0d-0b48-3138-a2c2-574791cda8d6 | -5.9766 | -44.28547 | 2025-08-19 03:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3c0f1a6a-5140-37b9-a7dc-c6b484363985 | -6.74991 | -41.55964 | 2025-08-19 03:36:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 87853cc1-af8e-3719-aea6-c70608daca4f | -5.98248 | -44.28652 | 2025-08-19 03:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d342c8a6-bb19-3ce0-bd4d-f176f2a30058 | -9.49184 | -40.3803 | 2025-08-19 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 22308634-0ccb-3785-9188-26ceacc410b7 | -6.06373 | -44.13182 | 2025-08-19 03:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dc7582e6-cf80-3a4f-9a88-3dd658dc2135 | -12.03704 | -44.01917 | 2025-08-19 03:36:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 71c44229-f594-3939-8e4e-ecec266030b8 | -6.94837 | -43.60557 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4dcbd743-7760-360a-8228-3a1fcedf8f9d | -6.74715 | -41.56555 | 2025-08-19 03:36:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b72fbcdf-ca90-39d5-a619-6ce101857ee3 | -9.8489 | -44.68983 | 2025-08-19 03:36:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21d222d6-3266-3c87-a302-debe9d0a5fd8 | -5.97948 | -44.1057 | 2025-08-19 03:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ae090b81-7626-36d6-b43e-94db23f6c690 | -9.49255 | -40.37622 | 2025-08-19 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f838180f-bcb4-3916-ba31-40cfcd544a1f | -6.16305 | -47.27599 | 2025-08-19 03:36:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a495fc9e-32cc-35c7-b7b9-8231486d5c4d | -7.57993 | -45.43366 | 2025-08-19 03:36:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f31ec22b-40f3-3eb7-9678-4c70f3fe6398 | -6.9346 | -43.61839 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e5948d58-0fb5-37fe-a7ff-4d81c58e6e40 | -6.53052 | -43.43716 | 2025-08-19 03:36:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 05f28781-269f-33a8-9764-6660bc215e1f | -6.84809 | -44.42243 | 2025-08-19 03:36:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5daae2a7-f546-35cf-a258-9ab8a6d82355 | -9.48686 | -40.38358 | 2025-08-19 03:36:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fb8a86d7-287d-3582-b9fe-f2930d5ae1cf | -6.06486 | -44.128 | 2025-08-19 03:36:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94991f49-03f4-35c4-bf9a-f0b08ad3dc78 | -6.92878 | -43.59305 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| fdf7db79-07a0-34dc-bf2d-8ac370077337 | -6.1569 | -42.6971 | 2025-08-19 03:36:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d8d6fee9-1a7c-39d5-872c-2088a272d9dd | -6.94283 | -43.60455 | 2025-08-19 03:36:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b61d06b2-f1c2-3e2b-8afa-90c796be94d4 | -6.85396 | -44.42338 | 2025-08-19 03:36:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 491690cc-6608-3c2a-abc7-224388ea703e | -12.04291 | -44.01723 | 2025-08-19 03:36:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README14.md)
