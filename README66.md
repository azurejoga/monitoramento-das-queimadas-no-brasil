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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 03eac1c3-a50d-37e9-90cc-b2c7e8ebe600 | -11.50321 | -44.06395 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 61d2d48a-f27f-37c4-a3b6-6651664141da | -10.12787 | -44.58448 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 210a87ff-be57-33ad-b3ec-c74d27c7397a | -9.37196 | -46.94869 | 2025-10-16 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 02009ab8-e554-3bf3-9136-bd7c31a5cc15 | -9.15777 | -41.06002 | 2025-10-16 04:40:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 11.5 |
| d01cac0e-4be4-366c-a3ca-4e71cd2d6e76 | -10.12728 | -44.55715 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 99cfcd2d-da22-3dfe-9311-1f87c5f98196 | -8.47396 | -46.23491 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2cb4ce0-df5d-3591-b861-2b24683a31b7 | -15.59285 | -42.40667 | 2025-10-16 04:40:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d18616d-bd16-31cd-93ff-9606d7b3f4ae | -9.69264 | -44.50637 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d91c0fa4-b1ca-3a0c-b525-e72eeb9e786e | -9.81806 | -45.27287 | 2025-10-16 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49684ecc-e6d6-35dd-b60a-a836bdc1fa89 | -10.03523 | -43.83195 | 2025-10-16 04:40:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8f17c925-be06-39bf-b6db-253d2a78942d | -9.68882 | -44.53322 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d5ea6a42-2c55-314c-880a-62d996575b3c | -8.2701 | -45.91492 | 2025-10-16 04:40:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 71ceb763-9e81-3583-855a-9550bb1e33e0 | -10.86315 | -44.41398 | 2025-10-16 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 310d0600-eea9-3042-b699-98ea90281ebc | -10.41977 | -48.88456 | 2025-10-16 04:40:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 91779d9b-ed83-35c4-bc60-6964f3059be6 | -10.13618 | -44.54723 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a55b2183-1f23-3c3d-aa5e-7d4833e395b1 | -10.9172 | -47.58815 | 2025-10-16 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 62e7c6a1-119a-376b-a9cc-685e74925c0e | -15.02975 | -47.31237 | 2025-10-16 04:40:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ba5795ee-06ac-334c-b066-7512306efe3e | -10.81231 | -47.97686 | 2025-10-16 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a18e92a6-9827-31d1-88de-bc90c0a7c048 | -8.45447 | -44.18514 | 2025-10-16 04:40:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 935961ce-8991-3777-89da-bfddf21c47ba | -9.08446 | -47.95055 | 2025-10-16 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5170d812-b954-3f64-900b-ef8fb6bd672f | -10.64828 | -45.24418 | 2025-10-16 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a85d75c0-dcba-3fc5-8335-31d48e3f7e46 | -10.0593 | -43.85296 | 2025-10-16 04:40:00 | NOAA-21 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 46e53440-393c-32e8-8cb2-e028491e44b1 | -11.71379 | -44.27145 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f36369b0-0c17-39d9-8c9b-40ab42a28eba | -9.37136 | -46.95285 | 2025-10-16 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| be0b6469-485e-3c62-8d1f-830cd7e54cf9 | -15.59358 | -42.40022 | 2025-10-16 04:40:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6fc75d37-a817-3699-a683-9914c5c97eae | -9.71251 | -44.52739 | 2025-10-16 04:40:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 47d1ea35-53e2-3d76-96d1-b505f1e01fcb | -12.85321 | -43.81671 | 2025-10-16 04:40:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b46099b-7736-353e-82fb-a8cb469a6a08 | -8.93083 | -45.40324 | 2025-10-16 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ce5379e8-7daa-36cf-8d87-7a82e3882b63 | -8.46136 | -46.19253 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 41bf988f-3706-3afb-b3b4-39aa5eedb90f | -11.76337 | -61.07765 | 2025-10-16 04:40:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c06701fb-a6f4-341c-97f7-e15f627c9153 | -12.17737 | -45.06129 | 2025-10-16 04:40:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be14a893-9826-3225-9150-0da39b8e6178 | -13.45324 | -47.92369 | 2025-10-16 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d175f9cb-9dda-36b5-8e66-53e0ae0f9536 | -8.45218 | -46.17775 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45c8969b-c24e-37f2-bcb2-165ada7c8d2e | -11.43144 | -44.06452 | 2025-10-16 04:40:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f5606a9d-067c-304c-a968-ebfa796e39de | -11.29293 | -49.88674 | 2025-10-16 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1f9372f4-323a-3190-ae01-d3e3f8aee0ed | -10.64475 | -45.23996 | 2025-10-16 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 20d69c24-a12e-3a71-861c-0e950dee42bb | -11.48328 | -44.08092 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8e1e38e1-cfdf-3c5d-b944-3d8db16f0690 | -12.72824 | -48.63665 | 2025-10-16 04:40:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6316fc67-d6b0-312e-9951-a96a29e1f356 | -11.19539 | -48.03492 | 2025-10-16 04:40:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 040afff1-d414-3006-962a-650c2b284b54 | -10.12625 | -44.56482 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f3f953f-3bba-349d-a216-9084a12404f6 | -11.62898 | -48.53611 | 2025-10-16 04:40:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b8677eb1-8ea5-3175-a23a-899bf8ca15d3 | -10.57021 | -48.63102 | 2025-10-16 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 642b9648-a795-3009-8358-78182b051911 | -11.59116 | -44.08088 | 2025-10-16 04:40:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 17e1b6c5-a916-3799-b5a8-6651033d9e3a | -10.13889 | -44.56619 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 54b60aed-e4ab-32a5-a6bb-9cbd1effa39d | -10.12836 | -44.58087 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 3a6665a1-fa79-3374-a3ed-bb29ecd11697 | -11.49351 | -44.10478 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4df6be2a-acc6-3788-9380-393fe161bf67 | -8.40974 | -46.26121 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8304266-9c49-30a7-ad97-326980261a42 | -14.2477 | -44.61507 | 2025-10-16 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa888afa-769f-3cf5-ada9-c4a89fb45c5f | -14.74759 | -42.37871 | 2025-10-16 04:40:00 | NOAA-21 | JACARACI | BAHIA | Brasil | 2917409 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 1b714888-d2df-387f-ac2d-80bf49318262 | -12.23993 | -49.38822 | 2025-10-16 04:40:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ebde76dd-778f-3c9e-85e6-b2f1a0be71c4 | -11.478 | -44.15422 | 2025-10-16 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b6dae81-5756-3f0a-abf3-0ea0df774263 | -10.13144 | -44.55046 | 2025-10-16 04:40:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 97345e06-cd5f-35be-bdd0-c7ac522a48f2 | -12.83424 | -43.81894 | 2025-10-16 04:40:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6edb9e4d-9299-377a-bbe1-b897d8861519 | -10.64879 | -45.24057 | 2025-10-16 04:40:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 85e08c39-6bb2-394f-b956-7758cb75c866 | -8.40546 | -46.2389 | 2025-10-16 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| cf2ab3bc-41ff-3b62-9f3b-f0cd67cd011e | -8.82041 | -47.30414 | 2025-10-16 04:40:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 081f14dd-5dbb-3db6-a8d4-885b19dfdb07 | -9.90531 | -48.1571 | 2025-10-16 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57107b34-0d0c-3cba-8876-f9090022a4db | -13.63673 | -44.4166 | 2025-10-16 04:40:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d5a36d52-3c4e-3c2b-a058-3cffe2f895d7 | -11.76101 | -61.07024 | 2025-10-16 04:40:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ca361da4-d13d-3c50-ad63-207441d21a93 | -19.79912 | -50.97473 | 2025-10-16 04:42:00 | NOAA-21 | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 320bbd6f-391f-3e02-9392-6ddc7b238ebb | -21.22336 | -46.10336 | 2025-10-16 04:42:00 | NOAA-21 | ALTEROSA | MINAS GERAIS | Brasil | 3102001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 54c1143e-9804-3704-bf75-b94f09ff1c72 | -17.76896 | -45.58531 | 2025-10-16 04:42:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d4e9e571-5246-38e9-a8c8-fccb455e4486 | -15.86755 | -53.9608 | 2025-10-16 04:42:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbf168f8-e5b8-3454-bf9a-e3a839d45f83 | -20.39958 | -45.96012 | 2025-10-16 04:42:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 76759c0f-9726-3295-8e85-6bef7a7f7726 | -14.37123 | -56.95619 | 2025-10-16 04:42:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bdbb0f32-0d65-330e-a8e2-759b07499ede | -17.93375 | -46.73436 | 2025-10-16 04:42:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 45eee979-2034-3484-b63f-de6f92da4a0b | -20.05104 | -44.74903 | 2025-10-16 04:42:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 216fcea7-03ca-3258-b824-f31a0ef0101f | -20.35773 | -48.78385 | 2025-10-16 04:42:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 899a8b42-5c04-35bc-a610-21075bda7958 | -18.47648 | -46.83559 | 2025-10-16 04:42:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2f660bb5-a769-3b7d-8206-f49d507f352f | -19.96774 | -49.41555 | 2025-10-16 04:42:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9fd47cee-26b8-3d18-b5fc-522de47f25df | -20.48509 | -45.99234 | 2025-10-16 04:42:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 00ae414d-c403-35c0-abdf-ddf08c359c6f | -19.02921 | -47.51658 | 2025-10-16 04:42:00 | NOAA-21 | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f243a5db-9298-36cb-9910-0bdf21710f97 | -17.60366 | -46.68877 | 2025-10-16 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3edb5d4-9bfe-3262-9979-f5ee43603f90 | -17.61275 | -46.68248 | 2025-10-16 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d0cf928-982f-34f2-b4ec-43a9825135c8 | -17.93423 | -46.7307 | 2025-10-16 04:42:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 953c57ac-2ad6-3bc5-8b08-df02e95e5026 | -18.26234 | -48.24478 | 2025-10-16 04:42:00 | NOAA-21 | CUMARI | GOIÁS | Brasil | 5206602 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02ac4840-7d9a-345d-8dbf-25dda49ab2f3 | -15.8682 | -53.95687 | 2025-10-16 04:42:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d72e35d-9a27-3567-bbdc-ebb1a6a0c98d | -17.21503 | -47.65622 | 2025-10-16 04:42:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2369930d-56dd-38c8-8573-03e6aa975517 | -19.11888 | -46.96522 | 2025-10-16 04:42:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95e3f265-2450-33a1-b788-9836657a8d2b | -15.871 | -53.96143 | 2025-10-16 04:42:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1a40acff-f9d6-3810-bfc2-f4fda029a3fc | -17.94307 | -46.72724 | 2025-10-16 04:42:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93990b92-9a37-3638-8e0c-1c072d87c86c | -19.07464 | -46.82336 | 2025-10-16 04:42:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10aca1d0-acd6-383f-ba5f-61d14cc469fa | -19.79519 | -50.97798 | 2025-10-16 04:42:00 | NOAA-21 | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d1fc4f05-afb8-30f6-9969-0d5f890bd994 | -20.39903 | -45.96166 | 2025-10-16 04:42:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4190ff4-671a-3f51-a1ad-d83ade55ba59 | -19.96415 | -49.41505 | 2025-10-16 04:42:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 59311878-228f-3f21-8969-e18d87b9cfcf | -20.35899 | -48.78709 | 2025-10-16 04:42:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fdc96e05-7189-374a-9b71-c913a6dcb3e1 | -15.8654 | -53.95232 | 2025-10-16 04:42:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b51a962-8e7d-3140-9c3f-ecf73e0cc591 | -19.77307 | -47.97288 | 2025-10-16 04:42:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 765c3576-a1b5-3992-af68-b4a121dfc1c1 | -17.9345 | -46.72966 | 2025-10-16 04:42:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5e818794-b2c2-32ea-bf17-1eee64c26e00 | -17.62743 | -49.34318 | 2025-10-16 04:42:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0cdbc71a-b547-318f-a075-e805e3b074a1 | -20.95302 | -47.40065 | 2025-10-16 04:42:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d790af71-f833-3e95-9a2c-fcbb031299bc | -19.96356 | -49.41937 | 2025-10-16 04:42:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| c9f67622-3759-39bb-96ea-23c5f62f6b9e | -21.63446 | -48.97785 | 2025-10-16 04:42:00 | NOAA-21 | BORBOREMA | SÃO PAULO | Brasil | 3507407 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d0791e9b-359d-35cc-addd-61542b61df04 | -17.92431 | -47.0052 | 2025-10-16 04:42:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6cd3c09f-a0d8-3ce3-aec4-f434ad4d9987 | -18.45123 | -44.48901 | 2025-10-16 04:42:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| ff429a69-881d-3e93-8f67-3fc281d8abd7 | -15.86885 | -53.95295 | 2025-10-16 04:42:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 84ece17e-46e9-3233-b662-3ce9c5ad8d1a | -17.93496 | -46.72591 | 2025-10-16 04:42:00 | NOAA-21 | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66f44543-b1af-35e7-ac19-9279bf101d37 | -15.85735 | -53.97934 | 2025-10-16 04:42:00 | NOAA-21 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 172a17e9-36dc-3bcd-bc1f-0ca3685546ad | -20.94945 | -47.39616 | 2025-10-16 04:42:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 200ea292-1f0e-37d7-8e9e-ab154a4c1467 | -17.65237 | -48.33524 | 2025-10-16 04:42:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README67.md)
