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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9de398b-ab37-3f13-892b-85504ac11f5c | -17.59627 | -43.19896 | 2024-11-26 04:18:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9719fa2d-a6fe-3468-8d63-dd3658811a30 | -16.53937 | -46.03123 | 2024-11-26 04:18:00 | NOAA-21 | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9c9d5d72-3c07-3225-874a-5dfe62078d1c | -18.39705 | -50.99781 | 2024-11-26 04:18:00 | NOAA-21 | CACHOEIRA ALTA | GOIÁS | Brasil | 5204102 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6b4b61af-5df3-3319-b034-eb5837070285 | -19.56494 | -44.85275 | 2024-11-26 04:18:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d73e2603-bf4a-32b8-9e21-ebfebd97edc8 | -18.11555 | -51.16474 | 2024-11-26 04:18:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d271c7f-c6bc-3839-9fb1-a65306be402f | -17.74497 | -44.53067 | 2024-11-26 04:18:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2fb5496d-f8d0-35c7-9745-a95c2604d099 | -17.78165 | -42.80965 | 2024-11-26 04:18:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0bef78d4-2b91-36af-96a2-4ca138f4780e | -16.68233 | -43.88228 | 2024-11-26 04:18:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3619a8cf-fc9f-3b2c-8c2a-8ac41b76ed44 | -19.20913 | -45.37972 | 2024-11-26 04:18:00 | NOAA-21 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d5b21c90-4ac4-3f12-8d4e-bf7b57022a72 | -17.70491 | -54.94361 | 2024-11-26 04:18:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e48e46dd-9bda-30fe-8828-fd06fcf0a1f9 | -19.56438 | -44.85658 | 2024-11-26 04:18:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 325d83e2-9cc1-3f4b-9229-fb507182b6e1 | -17.3795 | -42.48477 | 2024-11-26 04:18:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 892a7393-0539-3515-b10e-475a2deccf94 | -16.34913 | -43.69448 | 2024-11-26 04:18:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b133e2c7-bd80-3f1d-a2b2-d0b006983419 | -17.416 | -47.08107 | 2024-11-26 04:18:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 60f80034-01bd-3ee6-b641-06124e2b4477 | -18.45015 | -51.73588 | 2024-11-26 04:18:00 | NOAA-21 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6d434a08-1a37-3759-b9f5-31492a22551c | -18.25853 | -51.27194 | 2024-11-26 04:18:00 | NOAA-21 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58627f80-b86b-3f89-92dc-a245a78139fc | -19.53686 | -44.07872 | 2024-11-26 04:18:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7151dd62-0a3d-3849-81d1-e16de55fad4b | -19.5635 | -44.85346 | 2024-11-26 04:18:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d146a6ac-1058-374f-9d3e-a132769f1276 | -18.81273 | -47.22211 | 2024-11-26 04:18:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5cd94f9c-a6d8-3188-a58d-1b03e7f8e520 | -15.18246 | -53.06144 | 2024-11-26 04:18:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 884f0654-130f-364d-8573-b5e3fc780fbd | -18.21991 | -45.05254 | 2024-11-26 04:18:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d4052a61-1fac-33fd-a93c-a304d1bbe947 | -16.68176 | -43.88617 | 2024-11-26 04:18:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8e8dc4bf-043d-311c-8810-6575a540998b | -17.09611 | -43.80439 | 2024-11-26 04:18:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 454cb5f9-e632-3c0c-b1be-55380ed8f46e | -19.20968 | -45.37602 | 2024-11-26 04:18:00 | NOAA-21 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33e6b586-e99e-3df1-a8e4-203be6153094 | -3.1876 | -48.4387 | 2024-11-26 04:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 102.2 |
| 43edb415-c091-31d5-bef7-492d246e28b9 | -17.6453 | -57.5874 | 2024-11-26 04:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 59.5 |
| af4c59bb-c6d1-3e25-8aff-6c67ddd9f2af | -3.1877 | -48.4172 | 2024-11-26 04:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 72e75561-fb78-3b35-b4bb-f30ddeefee88 | -4.5376 | -43.2807 | 2024-11-26 04:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 3da1b264-2e7b-3f87-9c91-f745d43d5c9f | -2.8014 | -53.0227 | 2024-11-26 04:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 0b5bbc2b-930b-38ed-a37c-639b6fe600cc | -4.5375 | -43.304 | 2024-11-26 04:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 007e608c-92e9-3462-bb79-8e38af200a46 | -6.0862 | -48.0339 | 2024-11-26 04:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 654c7b66-866e-382f-a081-81f4f27d09b6 | -3.6042 | -50.3781 | 2024-11-26 04:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 4fac16d0-895e-3ddf-9de9-95287944ca06 | -3.1691 | -48.4394 | 2024-11-26 04:20:00 | GOES-16 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| e47a8008-40da-3fc8-9936-3ee0cf4c4e28 | -20.96003 | -45.74506 | 2024-11-26 04:21:00 | NOAA-21 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 04cb2844-36a4-3e02-9355-b93c6c0bee06 | -24.96223 | -49.22819 | 2024-11-26 04:21:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 70a1b396-164a-3ca7-9399-91532414bfcb | -21.65292 | -55.80856 | 2024-11-26 04:21:00 | NOAA-21 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a1b42b0-a9da-300a-a171-8cea21bb5b43 | -20.40655 | -48.76908 | 2024-11-26 04:21:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91e494ea-ff52-3048-8acf-1490cc3ec682 | -20.86862 | -47.06851 | 2024-11-26 04:21:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c44fa2cd-9202-32c5-8f3f-8c0d3e457651 | -23.74532 | -49.01958 | 2024-11-26 04:21:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2823b73-b6c0-360a-92b7-1be88b5f4731 | -20.99697 | -51.79488 | 2024-11-26 04:21:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| f8fec084-7168-3623-99f5-26b403767c66 | -17.63809 | -57.58969 | 2024-11-26 04:21:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| ddc6bf85-4195-3151-ba0f-f55a887c8405 | -21.20879 | -42.83655 | 2024-11-26 04:21:00 | NOAA-21 | RODEIRO | MINAS GERAIS | Brasil | 3156304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 27e6b771-c27d-3c8f-b490-2d014e49e32e | -20.37755 | -45.6026 | 2024-11-26 04:21:00 | NOAA-21 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb613d62-c29f-309c-9184-fb46e6fc772b | -20.32647 | -48.82887 | 2024-11-26 04:21:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4dcd22de-96c7-3b98-abe2-53ced365922f | -17.64507 | -57.58644 | 2024-11-26 04:21:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 68f89ea7-45a4-38f2-b320-4a1a9f844686 | -21.32177 | -47.40748 | 2024-11-26 04:21:00 | NOAA-21 | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 48f9477e-4494-327e-8a5f-0381ee43a2c6 | -21.56158 | -54.20327 | 2024-11-26 04:21:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96ccb229-7cfd-3905-82fa-3d3e87858b69 | -20.42305 | -48.77626 | 2024-11-26 04:21:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce512107-3eab-321e-a5ca-8a353606ad79 | -20.80472 | -49.03623 | 2024-11-26 04:21:00 | NOAA-21 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b6c118a6-030d-3e78-8592-59708d77c116 | -19.67749 | -49.89723 | 2024-11-26 04:21:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| affa8713-6457-37f2-aa73-6187b6eaa5a8 | -20.5808 | -44.57478 | 2024-11-26 04:21:00 | NOAA-21 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6bf4e5b9-0cb5-3a10-9673-904666dd7079 | -24.24257 | -50.74047 | 2024-11-26 04:21:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a671c363-166f-30f7-a836-1c0e31907081 | -21.38325 | -48.63146 | 2024-11-26 04:21:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e4fb2e5f-b40d-3260-809a-422b58d8dbb5 | -17.63313 | -57.58364 | 2024-11-26 04:21:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.0 |
| 249a5a2e-fe16-37f0-be0b-b869df187aad | -19.03941 | -53.14827 | 2024-11-26 04:21:00 | NOAA-21 | PARAÍSO DAS ÁGUAS | MATO GROSSO DO SUL | Brasil | 5006275 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6cfd0af3-b3f1-3efe-b599-d66151f486d2 | -21.92225 | -44.75739 | 2024-11-26 04:21:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d3f15bec-7da4-3487-96c5-21039a4a9ee4 | -24.72861 | -52.19661 | 2024-11-26 04:21:00 | NOAA-21 | MATO RICO | PARANÁ | Brasil | 4115739 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f69bf659-8122-38dc-b3f1-1e35ba2077d9 | -17.65003 | -57.5925 | 2024-11-26 04:21:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.4 |
| 146b6bbe-3dd3-318b-bee0-afcb077b1a03 | -21.19708 | -44.93677 | 2024-11-26 04:21:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 916e0bde-b6bb-38ba-9fc5-91a32719272a | -22.08659 | -48.21813 | 2024-11-26 04:21:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 44bbe339-e2a3-3830-a9d7-c105979e8fb2 | -20.32924 | -48.83355 | 2024-11-26 04:21:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 667748cd-e0ac-3f38-9b75-898efff0988f | -21.32236 | -47.40379 | 2024-11-26 04:21:00 | NOAA-21 | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4f7e8176-bb10-3acd-8ab3-dd3fc87a154f | -17.65104 | -57.58784 | 2024-11-26 04:21:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 17.7 |
| 7c4add48-5d2a-384e-8db9-2950c9700252 | -17.6391 | -57.58503 | 2024-11-26 04:21:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| b3be169b-8619-3496-b3af-d258649f11ec | -22.1029 | -49.61312 | 2024-11-26 04:21:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 074d908d-10e2-3965-bdc0-aa189ebe63e5 | -20.90816 | -47.39875 | 2024-11-26 04:21:00 | NOAA-21 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9461b290-9d72-3027-8831-09be8d9cdbb1 | -20.0969 | -44.82345 | 2024-11-26 04:21:00 | NOAA-21 | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b908a089-1f86-319a-9a4c-433890a7156f | -20.32991 | -48.82954 | 2024-11-26 04:21:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ef5e05a3-6844-3f77-8caa-da8727182491 | -20.4518 | -44.17873 | 2024-11-26 04:21:00 | NOAA-21 | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 46eff8ad-28a8-3c16-8a29-bebd160a1138 | -22.64048 | -46.21978 | 2024-11-26 04:21:00 | NOAA-21 | MUNHOZ | MINAS GERAIS | Brasil | 3143807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0d377889-6b1b-3f43-9d06-842b9b48d2ee | -20.79967 | -53.55082 | 2024-11-26 04:21:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c001950-ac2a-39b4-a4cb-3527e8c583e5 | -23.63137 | -46.42661 | 2024-11-26 04:21:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 38933911-f275-3fe2-989d-156628f37ca3 | -22.54176 | -48.81374 | 2024-11-26 04:21:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71acf442-1363-3a66-abaa-ed4df692ce2e | -20.90211 | -43.82035 | 2024-11-26 04:21:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0236fa2b-c90b-3c6c-8b4c-b315fdc76427 | -17.63212 | -57.58832 | 2024-11-26 04:21:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| fafd7f17-70cc-3163-93db-20a1b758743e | -23.48468 | -46.92564 | 2024-11-26 04:21:00 | NOAA-21 | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 29913861-2808-3579-ad71-bf012a18e5d5 | -21.56608 | -54.2043 | 2024-11-26 04:21:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 879194c4-fbd9-3057-b1da-3d8dff495b16 | -20.45123 | -44.18276 | 2024-11-26 04:21:00 | NOAA-21 | PIEDADE DOS GERAIS | MINAS GERAIS | Brasil | 3150406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 9503949a-9009-35e3-97c0-7b3eaef3c2a0 | -21.31905 | -47.40316 | 2024-11-26 04:21:00 | NOAA-21 | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 691c6f11-daad-34c4-810c-c9a4b01b44a0 | -22.67656 | -50.43621 | 2024-11-26 04:21:00 | NOAA-21 | ASSIS | SÃO PAULO | Brasil | 3504008 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eedc3eb3-36a1-3960-88c3-eba51c3954fd | -19.62302 | -47.17852 | 2024-11-26 04:21:00 | NOAA-21 | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e2a91551-fc0d-32b3-92bc-d71cda7c2317 | -19.69078 | -51.28704 | 2024-11-26 04:21:00 | NOAA-21 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3b87b78-d299-30fb-b0c8-e474a3034b0b | -20.57768 | -44.57544 | 2024-11-26 04:21:00 | NOAA-21 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a1a84b29-18d4-336e-9a91-64022fddb09a | -21.56257 | -54.19841 | 2024-11-26 04:21:00 | NOAA-21 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bfb4ce99-52f0-3489-80fc-2823e28750b3 | -17.64012 | -57.58035 | 2024-11-26 04:21:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.3 |
| fa0830ed-a0fa-3212-a390-747715ca5cd7 | -17.65342 | -57.58617 | 2024-11-26 04:21:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 32632ce2-f561-359a-96d2-7c9c22bf2a83 | -20.76488 | -54.30768 | 2024-11-26 04:21:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9cc65c26-f3f1-3869-a071-dc3ab7aa93e1 | -23.75 | -49.01238 | 2024-11-26 04:21:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2b74f1b-ea5c-3cdd-9435-efab7a290c82 | -23.40502 | -46.55534 | 2024-11-26 04:21:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2756e30e-3e4f-3a11-9de6-c9654e0a22e3 | -20.32303 | -48.8282 | 2024-11-26 04:21:00 | NOAA-21 | COLÔMBIA | SÃO PAULO | Brasil | 3512100 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a550f54-068e-385c-a8dd-42b9826670d2 | -20.41596 | -43.55202 | 2024-11-26 04:21:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b21b90a8-839e-353b-9921-bad54f4b246a | -20.79981 | -53.55272 | 2024-11-26 04:21:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 36de6b0d-0bf7-3695-99af-bd1bfbfb673a | -23.74869 | -49.02024 | 2024-11-26 04:21:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d5f8b4f-7049-3fff-8d1e-d432ea6e8adb | -23.33799 | -46.77234 | 2024-11-26 04:21:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 27c0930e-3c34-3854-ac4b-0f47e4a0acbb | -19.19153 | -52.32085 | 2024-11-26 04:21:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef639cbf-2878-3f7c-bd15-1950d02857c0 | -21.17947 | -43.98124 | 2024-11-26 04:21:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 023cacd0-77de-31e3-ad9e-fc36347fda49 | -19.67387 | -49.89653 | 2024-11-26 04:21:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9cc636df-1cde-30de-b3a2-c91aa369234e | -24.9656 | -49.22882 | 2024-11-26 04:21:00 | NOAA-21 | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 5e79ab17-fd01-347f-8247-d4f7233c9ebf | -17.64641 | -57.58944 | 2024-11-26 04:21:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.1 |
| 29621630-1a41-39e1-b13c-08126af8087d | -22.09941 | -49.61248 | 2024-11-26 04:21:00 | NOAA-21 | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |


[Clique aqui para ver as próximas entradas](README20.md)
