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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3dd1fdbd-1f35-3884-a1e3-0adb8647ba5a | -17.61925 | -46.95643 | 2024-10-07 03:38:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 084ce13b-a273-3682-b2f6-dab754551b97 | -17.61435 | -46.95121 | 2024-10-07 03:38:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b8b2dfd2-0175-3280-a3fc-e5e9868a59ce | -17.60948 | -46.94585 | 2024-10-07 03:38:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f2ed423a-28ab-3800-88a3-2c1fe985d9ff | -17.60863 | -46.94975 | 2024-10-07 03:38:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8776406c-dc35-3d90-a492-29bdb0740fc5 | -16.91048 | -47.1496 | 2024-10-07 03:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a41c4ce5-e957-3c8c-a7af-83a93435db69 | -16.9095 | -47.15413 | 2024-10-07 03:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dad15d26-ff2b-3990-a445-59772afc1501 | -16.90356 | -47.15302 | 2024-10-07 03:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 31b2bf64-504b-354e-bd67-3a29cff6c517 | -16.90257 | -47.15759 | 2024-10-07 03:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bb5ec1d7-e5cb-3b2d-8352-185e57913ebf | -16.89668 | -47.15621 | 2024-10-07 03:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69a87f3f-d155-375f-9048-a1b36330d655 | -16.89412 | -47.15317 | 2024-10-07 03:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90b44e94-ab31-3896-a250-fdf17599a042 | -16.89322 | -47.15744 | 2024-10-07 03:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1d3ed0c8-fda0-3a58-8c1d-11c167d54a13 | -16.89085 | -47.15457 | 2024-10-07 03:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d104b990-6039-343f-bfcc-1bb4dc4cdbd6 | -16.88993 | -47.15882 | 2024-10-07 03:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 94e54c1b-d98c-37aa-923f-616b3d9c095f | -16.88899 | -47.16309 | 2024-10-07 03:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b6687870-1a00-3a86-ad82-36cb3c2b4e61 | -16.88769 | -47.18365 | 2024-10-07 03:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92ec1d07-9841-3221-b376-9d22fed27540 | -16.8874 | -47.15572 | 2024-10-07 03:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3b9332fc-9ebe-3969-99d8-4fa0c43ffb87 | -16.88649 | -47.16001 | 2024-10-07 03:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4c0835e3-9639-3d4f-b817-f799eee7e5cd | -16.88519 | -47.18053 | 2024-10-07 03:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a1b3c335-7f8e-378d-b929-924214a04923 | -16.88467 | -47.16864 | 2024-10-07 03:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3d4b4b50-c362-324d-8aad-97e72d92c122 | -16.88408 | -47.15725 | 2024-10-07 03:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8cc7793b-8d29-37c2-b84b-0d41f3d05b17 | -16.88222 | -47.16577 | 2024-10-07 03:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bb0fa368-ac13-3439-8999-c63e102c5442 | -16.88187 | -47.18191 | 2024-10-07 03:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0fb25761-f866-3db0-be7c-d9c638c92f0d | -16.88127 | -47.17014 | 2024-10-07 03:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d205c83c-8587-3272-8846-2b953c12060a | -16.87974 | -47.16269 | 2024-10-07 03:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53ca8276-4b9d-34b3-8fb5-ad650ca973ff | -16.87882 | -47.16705 | 2024-10-07 03:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 987d0924-7a83-31ff-bf88-adba7abe71b3 | -18.59451 | -47.31027 | 2024-10-07 03:38:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8e50b107-edcb-35bb-8be3-be85cec78198 | -18.59355 | -47.31459 | 2024-10-07 03:38:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7915133e-f309-395d-999e-01c637b5338f | -18.58933 | -47.30873 | 2024-10-07 03:38:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08c9cd39-a65f-31f9-bd22-eeabb304a151 | -18.58868 | -47.30925 | 2024-10-07 03:38:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f88a689-3acb-3768-b7fd-a98ba6ae3884 | -18.58842 | -47.31299 | 2024-10-07 03:38:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e46aa91-6d3f-3ece-b25d-8526517a9c89 | -18.58774 | -47.31349 | 2024-10-07 03:38:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e1c1a32b-1160-3968-b06b-675edd50731e | -18.30778 | -47.1356 | 2024-10-07 03:38:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 12e663ed-6a78-3a2a-a1d5-8e1e09c291dc | -18.30698 | -47.13926 | 2024-10-07 03:38:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d86f9690-9596-3b75-9f24-4058bc41fed3 | -18.30613 | -47.1431 | 2024-10-07 03:38:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f2dd38b7-974d-38be-aa95-b240d9685ba4 | -18.30278 | -47.13274 | 2024-10-07 03:38:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c7f96d5a-26e2-33f5-97d5-3c0643b949b8 | -18.30207 | -47.13417 | 2024-10-07 03:38:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 78d147e7-310a-35ed-bbfa-fd275ab4cc44 | -18.30205 | -47.13617 | 2024-10-07 03:38:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 42ebe31e-7364-3f72-a435-f4cfcd65f3d3 | -18.30129 | -47.1377 | 2024-10-07 03:38:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 73d7fdaf-df1b-3a0f-b9cd-fa26507bfe01 | -18.30124 | -47.13996 | 2024-10-07 03:38:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9d330aac-4929-32dd-a0c5-57e78a47ceea | -18.30042 | -47.14167 | 2024-10-07 03:38:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ad5f0da0-aa88-337b-b9d0-598dc7371679 | -18.30035 | -47.14412 | 2024-10-07 03:38:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e1259cd2-dfbc-37af-8b20-8cdc5b853df1 | -18.29948 | -47.14593 | 2024-10-07 03:38:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cb143ce2-c0ea-3fdd-8371-60dd34ce9b20 | -18.29941 | -47.14855 | 2024-10-07 03:38:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f41b51a6-1804-32fa-96fc-34f87c49d941 | -18.29628 | -47.13499 | 2024-10-07 03:38:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| dea575c8-0a93-3287-9247-db98c96742fd | -18.29554 | -47.13647 | 2024-10-07 03:38:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ee1e54de-de4c-3fe8-91af-9119db62f60c | -18.2955 | -47.13863 | 2024-10-07 03:38:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8762fae2-25bd-3acc-bada-32e631dbcd4f | -18.29468 | -47.14035 | 2024-10-07 03:38:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b828212b-f2fe-38a2-a714-b305bb68b52b | -18.29461 | -47.1428 | 2024-10-07 03:38:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 75f2ea1d-d195-3cfa-937a-6dd24659f908 | -18.24049 | -46.40072 | 2024-10-07 03:38:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e9b2fd9e-ca2f-3094-b446-f6baef2c5e8f | -18.23971 | -46.40443 | 2024-10-07 03:38:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9ca3fbe7-b9c1-3dca-8343-3d462433ee29 | -18.23924 | -46.40063 | 2024-10-07 03:38:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f8f2cedb-1ae6-3304-b1b0-675bf39e42b5 | -18.23844 | -46.40433 | 2024-10-07 03:38:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c7b05fc3-7385-3237-ab4b-3eea54680011 | -19.19444 | -46.5781 | 2024-10-07 03:38:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 610c6403-02fe-33f7-82cf-a15d22f42722 | -19.96617 | -46.83707 | 2024-10-07 03:38:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 117223b5-3e7e-356a-a82c-779821929c48 | -19.94946 | -47.52834 | 2024-10-07 03:38:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 92a1bec8-33df-3a6d-abbb-09508b5e0ac0 | -19.94912 | -47.52835 | 2024-10-07 03:38:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 76259b2b-3b6d-3c63-938f-562a9066ea82 | -19.94852 | -47.53254 | 2024-10-07 03:38:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 41d9c0b2-1268-39ca-aab7-9d176c291d12 | -19.9482 | -47.53257 | 2024-10-07 03:38:00 | NPP-375D | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 13ab643f-69be-3c45-a4cd-298c8a331918 | -19.82724 | -46.82022 | 2024-10-07 03:38:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| acc5f6a3-a832-3e17-a951-29ada2c10954 | -19.82636 | -46.82428 | 2024-10-07 03:38:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90d3b36b-73dc-3b0e-b84a-bcf82a13dc28 | -20.46068 | -47.66384 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87906bc7-1934-3775-b1bf-c06fdfd2d695 | -20.45975 | -47.66812 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 218f701a-951f-3952-982a-a4337f03b9b8 | -20.45881 | -47.67241 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f1777b99-73a5-3869-a8ad-5fbf5c5d7f30 | -20.45786 | -47.67677 | 2024-10-07 03:38:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 177793c5-d785-3b78-8a4e-9ff898580b0e | -20.45692 | -47.68104 | 2024-10-07 03:38:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3ae2de1a-b638-388c-a102-9e1981be5f74 | -20.45601 | -47.68519 | 2024-10-07 03:38:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 85375315-cf97-369d-b516-828db5166a04 | -20.45511 | -47.68934 | 2024-10-07 03:38:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 30103bf4-3472-3561-9d0b-1a08bbae55d1 | -20.45419 | -47.69352 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 382985a2-3b1c-3c67-93e2-a987f54caf89 | -20.45327 | -47.69772 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 43.7 |
| fc4f455c-c984-3e84-a062-465b4b6a9073 | -20.45236 | -47.70189 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 431dca18-5ade-3584-b033-7d2a60324c9d | -20.45218 | -47.67538 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 75fd6ca7-c9bc-35c0-9909-de7437191883 | -20.45144 | -47.70609 | 2024-10-07 03:38:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 997dd7a4-882e-31a2-9b82-ffd7df548f07 | -20.45124 | -47.67968 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 0076c905-6e07-310f-ae3f-fbbb45ba83fd | -20.45052 | -47.71032 | 2024-10-07 03:38:00 | NPP-375D | GUARÁ | SÃO PAULO | Brasil | 3517703 | 35 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 42d0eafd-f596-3f1b-8900-e91d31946afd | -20.45032 | -47.68387 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 8b586694-a7f6-3ac5-bc94-fe69236e0e6d | -20.44941 | -47.68805 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 77fc1eb4-73b8-32a2-a600-43e91c6ed799 | -20.44847 | -47.69233 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 805ae9a6-763b-34e6-9107-775a41f0d190 | -20.44784 | -47.67293 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29c768a1-cf0e-337b-8e48-9b4de7c067af | -20.44754 | -47.69655 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 6d24a435-b697-3401-849f-628695e3bb6a | -20.44687 | -47.67722 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c7355908-b206-3c63-8322-3356669647e7 | -20.44664 | -47.70065 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 80ee00d6-0268-3923-8057-42d2c0c37ca9 | -20.44646 | -47.67423 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6de98986-4b20-3c7a-9841-facbea792acb | -20.44591 | -47.68144 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c802a397-10cb-333f-8751-f57061ba9d72 | -20.44575 | -47.70473 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 2657923f-b9af-33b7-a1ad-e6b3e9db53db | -20.44552 | -47.67851 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1403b3e9-ec62-39d2-85b1-f320b835cce2 | -20.44497 | -47.68558 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 11.2 |
| e8e2275f-84d3-3f32-9cda-b7678d8d094d | -20.44483 | -47.70892 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 1191855d-3234-3f09-a8c8-e520cdbbe639 | -20.4446 | -47.68271 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37722d64-b540-34f0-813e-5c56e670814c | -20.44402 | -47.6898 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 11.2 |
| f1517969-86a6-330b-808e-c77f1236edd9 | -20.44391 | -47.71312 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 44f008f8-cef7-3604-8864-050e5cb7ab78 | -20.44368 | -47.68686 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 18.0 |
| deca3434-19fc-359f-be88-134608f297d4 | -20.44304 | -47.69411 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 1629b2ec-134e-3415-9a8d-a410d63c0b25 | -20.44275 | -47.69114 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 85fe96c3-fc80-3736-b314-05423b6120cd | -20.4421 | -47.69826 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 09f0725f-6959-31c0-9be1-af4773bc4d26 | -20.4418 | -47.69544 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 32.0 |
| cef1b33e-c901-3d01-8bb6-09b649f620bd | -20.44119 | -47.70227 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 30.8 |
| fe970049-9dec-313a-9d1a-3b223d2cbec7 | -20.4409 | -47.69953 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 32.0 |
| 09eb9799-87ac-3897-8b1e-80cde7d55aed | -20.44025 | -47.70639 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 816c18f2-475e-36a4-9d66-ca55c965db65 | -20.44002 | -47.70354 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 31.3 |
| b0d006a0-1339-3d26-962f-064ccabd3ea6 | -20.43929 | -47.71064 | 2024-10-07 03:38:00 | NPP-375D | ITUVERAVA | SÃO PAULO | Brasil | 3524105 | 35 | 33 | nan | nan | nan | Cerrado | 23.4 |


[Clique aqui para ver as próximas entradas](README48.md)
