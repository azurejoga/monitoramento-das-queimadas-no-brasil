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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74585861-5b1e-3986-8f94-1bcffa2f2544 | -18.02977 | -57.32137 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 5cb07db6-68a0-3e86-8057-9fe7ad977f2e | -18.02946 | -57.32159 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 2e177579-08cc-3407-85ae-e5b9f2f13c0d | -18.02876 | -57.37939 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c5fd25d1-7938-38a5-9110-9b37f361e6cf | -18.02793 | -57.32895 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 552acef8-59d4-337b-8fd0-803a795d506b | -18.02741 | -57.33238 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| f0f38829-84dd-3681-80e0-a4a66a085c46 | -18.02716 | -57.33263 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 29ac6d86-f1a3-3f1a-9b0a-e158936d8060 | -18.02662 | -57.33607 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 84d5f290-1d90-3697-9b3c-abfbd1b92b04 | -18.02582 | -57.33977 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 460f0f0d-f7e8-392a-8a23-6ae40f5c458b | -18.02563 | -57.34005 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 68a6e00b-6a26-34e2-b6d0-d3dc0e11f0d0 | -18.02356 | -57.32372 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 08019818-f92e-35c9-9516-459974a2ccd2 | -18.02337 | -57.37852 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| cce171a4-1031-31d4-93a5-2a6378ea821a | -18.02331 | -57.37811 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| e36c7b68-3076-3b24-850b-8e3d439c2f2f | -18.02327 | -57.32394 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9dd15e72-9d2c-38e9-a667-809eb728179e | -18.02276 | -57.3274 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 11c40b24-65b0-3fc3-be61-e894337c1411 | -18.0225 | -57.32764 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| c99309b6-d7a6-3cca-b7d9-0a93a5a9b2f7 | -18.02117 | -57.33482 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 32ea9cb5-e8ed-3e45-abd0-05a1c93d5de5 | -18.02095 | -57.33508 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| e499e3e9-0e35-31f2-b005-374b4fc272f8 | -17.79777 | -57.33833 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 75154f69-14e3-3906-9bf2-d300fd2f660b | -17.79754 | -57.34091 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| ce6f22e4-5cb7-3b3c-82d7-e9664ba5c1ea | -17.79696 | -57.34207 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 07324492-47fe-3088-a433-c14f3732d46b | -17.79676 | -57.34465 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 42316ab5-b432-3708-aecf-3e298fc6ba40 | -17.79616 | -57.3458 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 8598585b-fffa-3638-9a9a-c33c4d56564f | -17.79598 | -57.3484 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7d1cf21b-1327-3e03-a7ef-a58563c34dcd | -17.79535 | -57.34954 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 20e67d7e-609a-3ead-975c-77e768cc67d0 | -17.79374 | -57.35703 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| bd38a260-e0c9-34bd-b9e5-1f0cad648ffd | -17.79364 | -57.35963 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| f7adaaf1-d977-3a60-a04a-901df7085599 | -17.79293 | -57.36076 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b2ddfd44-8884-330d-a7e4-2c21ad9ad47e | -17.79286 | -57.36339 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.3 |
| 9c540713-1b10-3f27-89cf-d4c01940ed21 | -17.79213 | -57.3645 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| e77ee106-9f58-3441-9b5f-5a706a2a0ca4 | -17.79207 | -57.33963 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 6bdd10f3-1c5d-3e00-84d0-a9c0fbac2baa | -17.79149 | -57.34081 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 37ddecab-8af3-34f9-8ea9-66f983e28575 | -17.79132 | -57.36825 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 33b0205f-2745-3f00-815f-e4f2802cb049 | -17.79129 | -57.34337 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 59a03ce9-0a81-3477-b372-4cbf8875fd9d | -17.78895 | -57.3546 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| c567334a-69df-37b2-8749-7668e78d2bba | -17.78827 | -57.35574 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b5540f8d-467b-3efb-9801-a4fb9a3fb8a2 | -17.78739 | -57.3621 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 436fa110-e0ae-3164-9b2d-c95f6dcaed78 | -17.78665 | -57.36323 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| fe8246c5-6e5f-3be1-a6bd-e11de46290de | -17.78661 | -57.36585 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 1f042364-4a72-31ed-bd9e-049a39825e69 | -17.7866 | -57.33836 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 8806d125-f93e-3d62-a8a7-316a1cf79945 | -17.78584 | -57.36697 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 85353f95-687f-394f-b6de-df950bc598b5 | -17.78114 | -57.33706 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| b7cf8828-1416-3948-9914-f7de680cfee5 | -17.78113 | -57.36456 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 743f9ae9-4f52-354b-9b36-ec9f78ac3826 | -17.78036 | -57.34079 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| cc1e2d15-5d40-358c-8095-36f85abc5e97 | -17.77958 | -57.34452 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| da57ec57-7c09-3067-98b4-08885e2e9225 | -17.76707 | -57.34945 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 578733a8-bd48-3c86-bd7f-31b7a2abf3d9 | -17.76628 | -57.35318 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 1fc1a860-8d59-3649-b7da-d4a004d5d27b | -17.76081 | -57.35189 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 19d96927-39a7-35f8-8226-4df5d6dd6768 | -17.76003 | -57.35564 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 2dfd28a2-95de-3cf3-ad00-bad4011edd40 | -17.75924 | -57.35939 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 5ce72316-4f4d-36bc-bc1d-d84b5d04108e | -17.75608 | -57.37441 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 216ecc61-b9ec-3c54-a648-51d5dc80a6a9 | -17.75529 | -57.37817 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 6d45e381-5aa3-3d62-b974-a2551c5cfa05 | -17.69206 | -57.32956 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| a036cab5-a200-3cad-9aaa-8d6809d5dd23 | -17.69127 | -57.32774 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 66193036-54c6-34d8-b31d-8838479e6036 | -17.69047 | -57.33147 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ab654613-e8a6-3487-aecc-2a1ba694654c | -17.68817 | -57.37596 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 8454ac5d-4bf9-3069-835a-20f3acb3227a | -17.68659 | -57.32827 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 6a10ce49-fd3e-38ac-8231-91ba7f442eaa | -17.68269 | -57.37466 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c70f6deb-3656-3d66-9a61-fc64afc80134 | -17.67956 | -57.33446 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 101aada6-20dc-3824-b146-3441e48f3289 | -17.67878 | -57.3382 | 2024-10-26 04:21:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| fea8d8a0-5e3c-379c-84da-3a6c3d1f7e94 | -18.15327 | -57.32994 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| a9acc1d9-bc0f-3c5b-980c-c40fbeef960a | -18.15249 | -57.33361 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 67acfff2-2a51-3c28-af31-5703bf9a1bba | -18.14383 | -57.37411 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 1d075d13-4d03-360c-af28-5ecbb528ac8e | -18.13839 | -57.37283 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| e1f63db8-7e4c-3969-8291-9c5e694bb824 | -18.13759 | -57.37653 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 07603597-d60d-3465-8610-cc1366c34627 | -18.11504 | -57.37508 | 2024-10-26 04:21:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ff6e08b7-1b14-35f3-9745-489aa6675aa9 | -23.98247 | -48.91809 | 2024-10-26 04:23:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1aa6f0e-5a7c-3c65-aa11-f53106170ea4 | -23.40516 | -46.55741 | 2024-10-26 04:23:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2698daea-0dbf-353a-8e94-7c607f25d391 | -23.33887 | -46.77213 | 2024-10-26 04:23:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ed8e1a12-cb46-36b2-a879-ea198a6bdfd2 | -25.18859 | -49.32623 | 2024-10-26 04:23:00 | NPP-375D | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5205bed7-f17d-36bc-b191-f19f64efb3c4 | -24.88703 | -49.55046 | 2024-10-26 04:23:00 | NPP-375D | CASTRO | PARANÁ | Brasil | 4104907 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 88cb8e97-2454-3146-8a3d-6cc96e99f42d | -23.50115 | -55.17331 | 2024-10-26 04:23:00 | NPP-375D | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2c50a6aa-fdc0-37e4-a856-fbc8c8fe3157 | -21.22939 | -57.39182 | 2024-10-26 04:23:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2b25dc6f-b783-32be-be02-7111dc798b95 | -21.22869 | -57.39511 | 2024-10-26 04:23:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6c209bd-720b-3ae1-8dda-3f4b2059ae64 | -3.88926 | -41.02061 | 2024-10-26 04:25:00 | AQUA_M-M | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 46.4 |
| 5b4e557e-a3c6-33df-b5f5-61e36a666c43 | -29.81536 | -51.17603 | 2024-10-26 04:25:00 | NPP-375D | SAPUCAIA DO SUL | RIO GRANDE DO SUL | Brasil | 4320008 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| 3b915139-58ef-3dcf-b5e9-3c3e6eed7874 | -29.18969 | -51.96219 | 2024-10-26 04:25:00 | NPP-375D | ENCANTADO | RIO GRANDE DO SUL | Brasil | 4306809 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| dbe0e5d6-30b8-39f5-8714-0a4f2a6c1084 | -3.013 | -50.481 | 2024-10-26 04:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 02b32311-94ab-367c-b724-e0090c610c1d | -2.8923 | -53.3247 | 2024-10-26 04:25:22 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| d4be1607-b7fa-39e3-b5d0-aad6b543d4c0 | -2.9501 | -52.5708 | 2024-10-26 04:25:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| 525671c1-af5c-3a9d-8e7a-dbbe124f2d51 | -2.9501 | -52.5504 | 2024-10-26 04:25:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 3faf6587-9681-38d4-b903-e5edc7363c24 | -2.9945 | -50.4816 | 2024-10-26 04:25:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| f40ee87a-0f87-3a2d-8dae-153e11f5bac4 | -3.4729 | -43.3377 | 2024-10-26 04:25:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 3fbb5404-4493-39e7-9759-7511354d8fc7 | -3.473 | -43.3144 | 2024-10-26 04:25:25 | GOES-16 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 21454677-db8e-3a77-a610-d20102f7cc13 | -3.6084 | -45.8147 | 2024-10-26 04:25:26 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 9f276c35-9436-3849-bee5-5f2c01efe0d0 | -4.5799 | -48.0349 | 2024-10-26 04:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 184.3 |
| b94e549b-13da-3348-843a-648d3dc092c0 | -4.58 | -48.0132 | 2024-10-26 04:25:31 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 208.0 |
| 32c67772-cbd6-34fe-8d3a-98118cf341ad | -6.8534 | -45.8794 | 2024-10-26 04:25:44 | GOES-16 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 41f19367-5882-3a94-8ac8-d6739d87a636 | -7.6474 | -63.4584 | 2024-10-26 04:25:49 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 059c3030-2eef-3c1f-be91-35810421dd13 | -17.0499 | -53.452 | 2024-10-26 04:26:41 | GOES-16 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 61.9 |
| f495cfe1-f9d6-317d-8bf5-56a907f48d62 | -17.254 | -57.4903 | 2024-10-26 04:26:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.8 |
| 0e84566d-df06-3d26-83f2-b80bbcdeaeec | -17.6667 | -57.4822 | 2024-10-26 04:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.5 |
| e3ad4dd5-5a9d-3c6e-8708-7881f3ec8125 | -17.6861 | -57.5004 | 2024-10-26 04:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 63.4 |
| ca264dca-376d-3c93-8b1d-0761dbc03956 | -17.6865 | -57.4798 | 2024-10-26 04:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.3 |
| b9eb6ea4-4516-3519-a6e0-281a5812db3d | -17.7246 | -57.5574 | 2024-10-26 04:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.2 |
| 8c24eb20-703b-37c5-a6df-d72b9334e5a5 | -17.7443 | -57.555 | 2024-10-26 04:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.2 |
| a1105254-0e60-3cf0-9bdd-10712d30d834 | -17.7446 | -57.5344 | 2024-10-26 04:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.5 |
| 01a6d1ec-421a-3463-b9a4-118df7a2d485 | -17.745 | -57.5138 | 2024-10-26 04:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 110.2 |
| 344586f3-ee0e-318e-a958-79dd159f6368 | -17.7647 | -57.5115 | 2024-10-26 04:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 70.7 |
| 71606bc3-e0a9-3e04-9cec-abc03a7444dd | -17.7674 | -57.3467 | 2024-10-26 04:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 80.2 |
| 35c05209-2b2a-3428-8006-016a285abef3 | -17.7868 | -57.3649 | 2024-10-26 04:26:45 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 99.7 |


[Clique aqui para ver as próximas entradas](README61.md)
