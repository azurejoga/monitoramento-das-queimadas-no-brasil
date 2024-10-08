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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 64edf07a-f1d0-30a2-90b8-e878b646e0ea | -17.1622 | -56.13934 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 7cd26892-5bfe-3d2f-aa00-38c2cfc93fb3 | -17.16159 | -56.12753 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| cce4bcfb-a7f1-35b7-8224-4b41960b152b | -17.161 | -56.13219 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 2285c591-2354-3e49-9991-6988cfe2d0df | -17.16041 | -56.13683 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| e57cf3d6-8bfd-393f-bceb-b9b025505202 | -17.15936 | -56.12478 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 23b3f43e-b757-3d3d-a0a1-80bac25728a2 | -17.15881 | -56.12944 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e7610163-31b8-3c32-86e4-09c412479b70 | -17.15826 | -56.13409 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 316b7b0f-514f-3364-88c6-58ea79dd20d3 | -17.1577 | -56.13875 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| c7676244-eee5-39a2-b6c3-5b4830cc79f2 | -17.15709 | -56.12696 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 4e2dc36a-ced4-3c54-af0d-e27d8858f65f | -17.1565 | -56.1316 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 84755e16-25ac-3e1a-a07d-867d2b4686ba | -17.15592 | -56.13625 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| be35c76a-66f4-3f1c-8487-c2ef4a22a495 | -17.15533 | -56.1409 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 07c1798f-5881-33e0-a18d-06eea3690f6e | -17.15376 | -56.1335 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 9d0cd473-8b85-31a9-9049-352de8d2ae6d | -17.15321 | -56.13816 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| fccffc14-851e-3164-82f0-e3d4ae3bf40b | -17.15266 | -56.14281 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 41f5ade4-9c87-3460-94bb-789a4bb11642 | -17.15211 | -56.14746 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 1aa2c7f6-db44-3104-8020-7b07360dfa6b | -17.15142 | -56.13565 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| e1145869-3bec-387b-9526-d7e05f73091e | -17.15084 | -56.1403 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d2c8b802-5943-3805-bc1a-baadb2a9822f | -17.15025 | -56.14494 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 2110c5d3-793c-32f1-96a8-df014023b91f | -17.14967 | -56.14957 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 7dfc087c-c756-3c99-9e79-265599f60516 | -17.14707 | -56.15149 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 473d56e6-b56f-32c4-8d4d-f1807163e5e8 | -17.14518 | -56.14897 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 5d9836f6-01d9-30b7-89c0-6b7970b529b9 | -17.1446 | -56.15359 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 0bf6a669-04cf-304d-aaa7-cd9c4c37edbe | -17.04536 | -56.05231 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| b7452015-2811-3db5-999e-ed7a42429ddb | -17.04477 | -56.05699 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 9ff04e89-bf75-3332-b8a1-86778f09bba6 | -16.96646 | -56.13642 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 83646267-0e28-3c44-a6e2-dcaaa258d39b | -16.96198 | -56.13582 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c2bdb093-3e3f-3249-a198-a1e6bb7246bb | -16.96142 | -56.14043 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 42d08dd7-93de-3ce8-b748-e26d59749190 | -16.89602 | -55.8717 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 45fee11a-6584-39e6-a72b-155c86db753f | -16.83221 | -55.85697 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4bb86719-4da9-31f5-a468-b494fd8d318e | -16.82824 | -55.85159 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3dee1363-4f9f-36b4-b840-fbca76f3907f | -16.68869 | -55.96593 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| bb347c5d-f0c0-3206-b285-bee62d3a5cbd | -16.68418 | -55.96533 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 58f6440e-46cb-3ada-a737-e64ada382cb1 | -16.66958 | -55.89635 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0f069126-6859-39d7-a6d4-b5bb75053378 | -16.63173 | -55.89338 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 7dde8298-2797-3247-9b1b-dbbd5ca289af | -16.62995 | -55.90755 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c90783f0-68e5-3842-861f-32f5619b0207 | -16.62661 | -55.89749 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| ff5323cc-5f69-3a8a-b5cc-1677c25615a8 | -16.62602 | -55.90223 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 18fb773a-7760-3f1e-a2cf-c0ec1bbdd958 | -17.02699 | -56.66258 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8dfea154-71c4-3d44-a3e3-34556996967f | -17.02646 | -56.66686 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b4b4dba5-6e6d-3801-86dd-caaf14c84f90 | -17.01727 | -56.66996 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 12e3c9b2-b7cc-3ff6-886e-991bd3a57f79 | -17.01241 | -56.67366 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 5715fa06-0016-3afd-b116-ea168f0d1a1b | -17.01188 | -56.67795 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 219088ec-6d25-31de-9709-fad81516b86c | -17.01135 | -56.68222 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| db20a0bc-ec9c-357c-8bee-1e2efdd9cbba | -17.00756 | -56.67735 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| d09a9937-9f5f-36a9-9de3-5be01393fcc2 | -17.00703 | -56.68163 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| bf2e5135-cd1a-35a8-8254-483b80a7303c | -17.00544 | -56.69444 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 6c2d8e5d-6a45-37a3-a0bd-b1cb5204101a | -17.00377 | -56.67247 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 0de03b15-67fa-355e-97a3-0a6bb0509d43 | -17.00324 | -56.67675 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 47668276-c8cb-37b0-9ab0-f057017baf31 | -17.00218 | -56.68532 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 7065d134-5055-34df-b6ff-dbb2bc89df08 | -18.72051 | -57.27577 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 38efcd9a-fc92-3a7d-b8d0-b3fa8cfe9ae9 | -17.00112 | -56.69385 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4ddb822e-5dfa-3676-a351-9b5c941f34a5 | -16.99786 | -56.68472 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 4b6bca30-40b3-3b88-b19e-c25636e8273f | -16.99733 | -56.68899 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 4e111d0c-ffed-39ea-af18-1549ecda386e | -16.99681 | -56.69326 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0955aba7-f99b-363c-9a28-b4174746a75a | -16.99433 | -56.60572 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 88c7f036-59e4-3a07-b433-3ba917d8487b | -16.98999 | -56.60511 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 3b50e5aa-5b55-39bc-b2bd-379d55d4e640 | -16.98894 | -56.61374 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| add88a01-bf74-3974-857b-743ea262b338 | -16.98783 | -56.61038 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 799782dc-4c8e-35f2-90f1-267c443c441e | -16.98727 | -56.61469 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| f7b30f55-0170-30a4-a64a-4bd4af2ac9d4 | -16.93358 | -56.62054 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| f29e3bfc-063e-34d0-861d-b8fd2ef7e599 | -16.93304 | -56.62483 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| be70451e-a24a-3d2a-a1f8-95c2e41a8f4d | -16.82765 | -55.85637 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 464cf12c-4597-32db-931b-2d4daa4037cd | -16.82368 | -55.85099 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 54e7868b-59e4-3405-b26e-8950377ec5f4 | -16.63114 | -55.89811 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c07b122d-50c9-3a6a-8f17-ca8980889d8e | -16.63054 | -55.90283 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c9467056-8260-3610-b2c9-ba14c9ded369 | -17.00809 | -56.67307 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| c92a2b79-e7f7-3a0d-9e66-fe64bb43b95f | -17.0065 | -56.68591 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| a6cdd0d4-f858-3f14-b5c7-be5dbb9cdee6 | -17.00271 | -56.68104 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| c807e65b-c37f-3c74-b880-b3cb1d010c16 | -17.00165 | -56.68959 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| c7036545-9379-3d4c-8aea-3af9f80ee850 | -16.99301 | -56.68839 | 2024-10-08 05:23:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| d5bf167a-f1a6-3398-a1c8-bd027e90a587 | -16.99273 | -56.60667 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4b9a0f72-c95e-3511-bf0e-c273cf959a69 | -16.98672 | -56.61899 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 87114cec-03a5-395c-afb9-0ea459b19250 | -16.9846 | -56.61314 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 421c8e0e-44f5-3d51-baf2-8636669761eb | -16.98408 | -56.61745 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 4d2429df-c184-3e73-a31a-7c5023a6c852 | -16.98293 | -56.6141 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| c85f236a-b423-3c0a-9677-3e17b23a0709 | -16.98238 | -56.6184 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| eea6e32b-f33e-3492-9ec7-9f41dff3d7a6 | -16.97804 | -56.61782 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 71170dac-8afd-3913-a8f8-d45665548744 | -16.97749 | -56.62212 | 2024-10-08 05:23:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 44832cb6-620e-36df-8ee9-d15009938a50 | -6.21857 | -55.65353 | 2024-10-08 05:23:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13a2597b-4ef9-372d-ad7a-bff7126e51ef | -9.81211 | -56.42233 | 2024-10-08 05:23:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1ad96351-482b-3b4c-bae2-4ad792d65667 | -10.82162 | -55.72779 | 2024-10-08 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c462f1e7-31dc-3054-b814-30f2802daeaa | -10.8128 | -56.26761 | 2024-10-08 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96ca20b0-c946-3ebb-aeab-2657d67f8169 | -10.8123 | -56.27123 | 2024-10-08 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f626df9-a485-38ce-9f14-4e8110869daa | -10.6606 | -56.05052 | 2024-10-08 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e71e4fe9-daaf-3bcb-9311-3bfc7cb3933d | -10.66009 | -56.0542 | 2024-10-08 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17c0b2cb-87ee-3aa4-ac01-be97e213f6b0 | -10.63133 | -55.91158 | 2024-10-08 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 3d3e4c81-d979-3a4a-a002-4602777fce84 | -10.63023 | -55.9193 | 2024-10-08 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 77073927-13a6-3b66-b16f-b8c7edbde773 | -10.62968 | -55.92308 | 2024-10-08 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 80828a68-e39d-3d7b-9a85-8186629843b6 | -10.62915 | -55.92683 | 2024-10-08 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4001e9fc-407c-397a-9d90-1cb82c94793d | -10.62913 | -55.91097 | 2024-10-08 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 922a6d6e-b24c-39c7-b6fa-eb2d820b8ed5 | -10.62809 | -55.9187 | 2024-10-08 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0b15a279-a8cb-3964-a339-06295b245fd6 | -10.62757 | -55.92251 | 2024-10-08 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 05e60e00-fc8f-3aa1-b881-4678f192ecde | -10.62718 | -55.91096 | 2024-10-08 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 68f56270-fbe3-3e65-9691-0534527b22ec | -18.71946 | -57.28407 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 78fdb991-b8fb-3c57-8daa-dd2bb2551915 | -10.62706 | -55.9263 | 2024-10-08 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f66c3a41-8666-35bc-9d53-4e9624af6a5b | -10.62608 | -55.91866 | 2024-10-08 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4c8d89e-53ec-31c1-9d1b-f730548d11e3 | -10.62553 | -55.92248 | 2024-10-08 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 260c47bf-e084-36cb-83ff-cb143be34c4a | -10.62499 | -55.92629 | 2024-10-08 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f6f42b39-4c9d-3b8e-a06d-a4e5f4c1c525 | -10.62498 | -55.91034 | 2024-10-08 05:23:00 | NOAA-20 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |


[Clique aqui para ver as próximas entradas](README115.md)
