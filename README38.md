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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3a5e7a0-f1d0-32c4-9936-6fa25488c3ab | -7.22908 | -39.96441 | 2024-11-11 04:21:00 | NPP-375D | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c300c4b7-0247-39ab-b57b-786022fd4ba8 | -7.436 | -39.76965 | 2024-11-11 04:21:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| aa9dbd22-f801-3191-82b1-74fc26d17529 | -7.12383 | -47.68349 | 2024-11-11 04:21:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f2bd701a-d2e9-36ca-a3f0-d11bb716f69d | -7.12317 | -47.68758 | 2024-11-11 04:21:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59ef513f-a85f-3a66-bcc9-e7ca98b6aabf | -17.66524 | -57.46986 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2a0665bb-caa6-34bd-8a03-daf3ace989af | -17.61805 | -57.53627 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| f705557a-81c0-34f9-b756-44018e46b05e | -17.29828 | -57.48782 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 8dc28db1-bf2d-35f9-995f-a70416d978d3 | -17.63715 | -57.52859 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.0 |
| 45f2d664-7a3e-300a-8f74-ef16bbb61d25 | -16.93777 | -57.65596 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d8042ce8-d9dd-3681-b91d-9fb60688b07f | -17.63079 | -57.53115 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 8d9a189d-8c9c-39a3-a5ac-0cb7725c3235 | -17.28358 | -57.31075 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| bc96c100-84aa-31c2-bdde-5838c7054f47 | -17.58871 | -57.42839 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ee604ffc-16c6-3886-811e-344d04531fd0 | -17.30303 | -57.49304 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 4cfa9827-52c7-3b36-bc2c-36909172e5a1 | -17.25677 | -57.49042 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 733974d8-998c-328b-a558-18583a615c9f | -19.53655 | -44.07974 | 2024-11-11 04:23:00 | NPP-375D | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dee09f50-3cff-3692-ab1b-88e4632cba27 | -17.59665 | -57.52715 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| d33d0da0-d868-33d1-9004-8396d52f9a12 | -17.58891 | -57.43791 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3131510d-4863-3c19-922b-fa562905f08c | -17.28552 | -57.30792 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6b78b70c-3558-35f4-8aae-78ac31520012 | -17.24242 | -57.48801 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 1f0d3936-fd13-3938-b735-f80962e96ca6 | -17.28465 | -57.49694 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| ade13ee6-9941-3d13-879d-b54f6cda2915 | -17.59975 | -57.43097 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 7755266f-ec02-375d-acde-ecb3ca458008 | -19.98253 | -44.10202 | 2024-11-11 04:23:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 3ec0a616-cb80-3c51-b8b4-145dab675665 | -17.63797 | -57.52472 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 49010a6b-e390-3ea1-833f-286d4e0162b5 | -17.61887 | -57.5324 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| e49b2e75-3006-3cf6-bec2-5bac591eb770 | -17.68001 | -57.51847 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5916afe2-7d46-3425-9a31-b1f4b2d69dcf | -17.27824 | -57.49955 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 463e60e0-88b9-34d2-b6e0-7f8772bfec2f | -15.56975 | -47.85625 | 2024-11-11 04:23:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 85fd6884-4115-31f1-90ec-dc019c822641 | -17.25035 | -57.49303 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0b05e745-406b-3d40-9b41-8ff2ab761d0d | -18.63637 | -52.1431 | 2024-11-11 04:23:00 | NPP-375D | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0712b198-15cb-39de-8f08-0bf1dc9ab1c3 | -17.63878 | -57.52084 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| b8efd7ec-2f0b-3b85-b7a0-c4a64bb937a1 | -17.29271 | -57.48652 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 1e71cbed-165d-3503-9393-87fb435c2151 | -19.97883 | -44.10148 | 2024-11-11 04:23:00 | NPP-375D | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| d017fa6f-51d0-3c6d-8c22-d42239c501b6 | -17.59893 | -57.43479 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 19fcbf4a-347e-33be-b782-b8e9942f5cec | -17.60078 | -57.50782 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| f08541bd-87d7-39fa-944d-9109a153305c | -17.248 | -57.48933 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7f8cc9bf-46d6-3495-9855-4d519978fdf9 | -17.59441 | -57.51037 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| cd4828dc-2b76-3cb1-9358-c65b67a0723a | -17.59048 | -57.43029 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 88afacae-6929-302e-aa6e-495f0a05aaa5 | -17.59418 | -57.53877 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 0e27bb72-644d-391d-810e-824adb1943ca | -17.60056 | -57.53622 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 10daa847-b361-3f08-9443-2552e19b6e16 | -17.58969 | -57.4341 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8258a20c-799f-3e59-a7d7-a74e1142576f | -17.61387 | -57.44632 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5171dc66-f1c9-32de-9b15-47ab3b65a621 | -17.24405 | -57.48019 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| d3652024-58de-3d6d-a3eb-20205b7e214b | -17.30942 | -57.49044 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 228cdddb-8ac4-3faf-90ce-f1ae12768226 | -23.92545 | -54.03914 | 2024-11-11 04:23:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 9a643896-ceb5-35f7-96e3-236650ae091f | -17.54836 | -43.88692 | 2024-11-11 04:23:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 327fa8ae-be2c-3b7d-9f6c-2975dbf1ab10 | -17.25203 | -57.48521 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 0fae10b1-97c5-32a1-b7ec-e09422862ab5 | -23.91619 | -54.04091 | 2024-11-11 04:23:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| d0f2778e-04c8-3fc7-a440-1fd8e4f29604 | -17.61723 | -57.54014 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.4 |
| 3e238c13-d03e-3e95-829f-228594798cea | -17.24323 | -57.4841 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 972c95d4-e277-32e2-8505-8cdba5886e5e | -17.59583 | -57.53102 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 19f53064-2376-3024-a4ed-71b246c3204a | -17.24881 | -57.48542 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 8f51d179-43dc-3314-89c7-5f2e89fc3de1 | -17.68081 | -57.51462 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5c822a0e-f6a6-315d-a958-d280ab8d981e | -18.32352 | -55.574 | 2024-11-11 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3d564d89-6c52-3252-8c06-938e2b7305ad | -17.30778 | -57.49826 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 31f197d0-2425-39a1-8dcd-5997e54e42df | -16.94344 | -57.6573 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 54ff6e70-1647-3637-8102-2a94099cf936 | -17.62184 | -57.43613 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7e23f1dd-29e3-3785-9147-a60e99bc8bea | -23.92435 | -54.04474 | 2024-11-11 04:23:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| ca17112e-1bad-3431-b93b-f5f31d62d4f1 | -17.60917 | -57.44119 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7f877845-daec-323a-bc34-4d95b0736572 | -17.24477 | -57.49173 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 1ed90699-e111-3de9-8ad2-ef019a9f831e | -17.3022 | -57.49695 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 505394a8-468b-3679-ad5b-c10b307c5cba | -23.02208 | -53.60181 | 2024-11-11 04:23:00 | NPP-375D | QUERÊNCIA DO NORTE | PARANÁ | Brasil | 4121000 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a00d65d6-a955-3b35-b0d6-8460d6d9466d | -17.29353 | -57.48262 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| d0a457d8-b4cb-35a8-b928-07db100f6f5e | -16.94429 | -57.65323 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 9c5dc114-653c-3255-aecd-059549a13c69 | -17.23835 | -57.49435 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 0936bd2b-91a4-3120-9318-130490c2dbc5 | -17.2344 | -57.49844 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| e657a16f-22d6-3cab-8c27-ebff2d79b881 | -17.24161 | -57.49192 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 781f0fd3-8c88-3eb6-94ec-5af3d4495f02 | -23.92833 | -54.04566 | 2024-11-11 04:23:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 11.1 |
| d3a1a610-a898-3db2-b9fa-c703bb948974 | -17.27516 | -57.48651 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 4108fd15-8f8a-345c-82d6-9603d21d9031 | -23.92415 | -54.04275 | 2024-11-11 04:23:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 14.5 |
| c5cf6248-416b-301a-b63d-09434bfa80bb | -17.7691 | -57.51685 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 661fc5c8-a4ac-353f-a2d6-3f10cc7f8755 | -23.9175 | -54.03732 | 2024-11-11 04:23:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 664a0d83-1610-3728-873c-0c40cf3adaeb | -17.68379 | -57.51863 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a8b3480d-aa97-349b-8c59-869d3d593d66 | -17.59748 | -57.52328 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 3c467a78-ffc9-30fe-a888-a9c707f68fde | -17.59996 | -57.51167 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 4c44e4c2-1c5e-31f4-b1a2-d23406512d51 | -17.71478 | -57.50974 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| cfbfa831-2aa6-3d87-a202-164b327f5a60 | -23.92038 | -54.04383 | 2024-11-11 04:23:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 8a7bc6f7-1133-3aed-b65b-1d43e2a040d0 | -17.59812 | -57.43861 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 57099a1c-3165-3093-95b8-004edfd34d7c | -17.35911 | -57.43527 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 03116a5d-70da-304a-8d37-fe936698df77 | -17.60138 | -57.53234 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.6 |
| 844d8a78-2be5-3136-99a2-af8f0918842d | -17.30385 | -57.48914 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9b18102e-44f2-3078-9f4e-5d05a55c6b51 | -17.6116 | -57.42975 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| d287efce-a7d9-3bbf-b90d-8efd822da2ac | -17.27907 | -57.49563 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 47c87f79-0b62-36fa-9651-09d767943445 | -17.60611 | -57.53753 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 41e4a814-5a66-3841-81d5-e572849f30a4 | -17.58496 | -57.42898 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 526c1aef-0945-3e81-be7f-45cb314e9755 | -17.60138 | -57.42334 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| efef166d-2e3c-3773-b992-1ab79a371623 | -19.43768 | -44.33994 | 2024-11-11 04:23:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a77194b-831b-36b7-8e17-a1eb072d9c8d | -17.2375 | -57.49825 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| b86719ae-d754-33fd-be1e-75c8c86e9fdb | -16.93863 | -57.65191 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| c9d4e259-14c7-3740-ad64-742438c12e6a | -17.6016 | -57.50395 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 2a6d4d65-a4fb-309a-986f-074911db30e1 | -23.92943 | -54.04005 | 2024-11-11 04:23:00 | NPP-375D | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| b36bb1df-5038-3539-9650-f2b824e67edb | -17.6155 | -57.43866 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 9276a132-d66a-3d57-9056-b8d05cccad77 | -17.5911 | -57.52585 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.3 |
| 3ef00c9b-de24-318d-8cbd-70ed86f0867a | -18.14575 | -47.80148 | 2024-11-11 04:23:00 | NPP-375D | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 150902b2-da9e-3d8c-b44b-c7976a49976c | -17.6316 | -57.52728 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| ef68ab3c-7149-318f-ba83-efe2fbe9bb09 | -17.59974 | -57.54009 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 7f52c36c-54f8-3b6b-88dc-888ef79c476f | -17.25277 | -57.49456 | 2024-11-11 04:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| eed8c0d0-8f2c-364f-bfb8-a9ca45a5b2db | -17.6667 | -57.47085 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| bb3d89bc-ee2a-3665-81e0-661b3fe7cfee | -17.60715 | -57.50525 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| e35c15f9-2841-35e3-a962-589f140ac85c | -18.32237 | -55.57964 | 2024-11-11 04:23:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| a86dcc40-43df-3d24-91c4-bcbd0ee9bfed | -17.62264 | -57.43233 | 2024-11-11 04:23:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |


[Clique aqui para ver as próximas entradas](README39.md)
