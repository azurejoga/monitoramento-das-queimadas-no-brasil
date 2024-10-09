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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6adf06f-a582-363b-af5a-93bbcc6b7fd9 | -6.48 | -49.918 | 2024-10-09 00:15:43 | GOES-16 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 3959fdbb-ce24-366e-948a-75ba51ebbb94 | -6.7383 | -39.2307 | 2024-10-09 00:15:44 | GOES-16 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 56.5 |
| 22d298d1-42ab-3dd0-a708-0a2d2ff382a5 | -6.7573 | -39.2287 | 2024-10-09 00:15:44 | GOES-16 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 60.5 |
| 45810959-865e-3185-bc65-373fbe720749 | -6.7614 | -60.0559 | 2024-10-09 00:15:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 044be97a-2732-3bec-81ce-0c49e1dafe9a | -6.7798 | -60.0552 | 2024-10-09 00:15:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 42ece651-26f1-3c44-9021-132d24a78729 | -7.0231 | -59.4303 | 2024-10-09 00:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.1 |
| ccdbb3e8-0090-3953-97ef-2540e85c11ec | -7.0232 | -59.4111 | 2024-10-09 00:15:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 693b1add-dcd1-37da-82dc-2c3b5d4bb83d | -7.0417 | -59.4103 | 2024-10-09 00:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.7 |
| e8f25db5-09d9-3080-86af-39b6d4213e4d | -7.2435 | -59.633 | 2024-10-09 00:15:48 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.4 |
| c931c1b4-09a7-3e61-8a2f-a33ab499f192 | -7.2619 | -59.6323 | 2024-10-09 00:15:48 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 84e62fad-bf90-3bd6-87d8-9b215f43c185 | -7.3473 | -64.6661 | 2024-10-09 00:15:48 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 45.3 |
| d27dd0a7-7719-35ef-934f-fd65855959b7 | -7.7312 | -43.0402 | 2024-10-09 00:15:50 | GOES-16 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 69.9 |
| 3f26edbd-2b38-34e3-b8ae-1eda237a6326 | -8.4919 | -48.6476 | 2024-10-09 00:15:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 177.8 |
| b8d83c11-591a-3b72-b2c5-439c81534682 | -8.4921 | -48.6259 | 2024-10-09 00:15:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 25ff213a-d086-3cc8-a351-f759e1705961 | -8.5107 | -48.6459 | 2024-10-09 00:15:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 6590eb2a-985f-3ebe-a6b6-7f31c09abf0c | -8.5109 | -48.6242 | 2024-10-09 00:15:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 13e7c2d9-b3fb-3522-977b-dcc597609e8f | -9.1044 | -61.1428 | 2024-10-09 00:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.5 |
| cd554c9e-9d43-3d10-b598-e079d2148b6f | -9.0543 | -63.2375 | 2024-10-09 00:15:58 | GOES-16 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 79.9 |
| d7588263-bc7d-31da-bdeb-0292b95831c3 | -9.1573 | -61.5803 | 2024-10-09 00:15:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 76.3 |
| a1ebf460-aa18-3403-ade0-642388b3e001 | -9.1574 | -61.5611 | 2024-10-09 00:15:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 0f6880f6-d4f7-3201-8414-e52dc0c1ec01 | -10.3894 | -61.2502 | 2024-10-09 00:16:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 0b27dbaa-5559-31be-b413-578bff70fcf4 | -10.3895 | -61.231 | 2024-10-09 00:16:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 687b6a76-597c-34c8-9595-aa75efbef493 | -10.59 | -57.5531 | 2024-10-09 00:16:07 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| c873734b-c869-3e80-8b61-d7469581dcfb | -10.5902 | -57.5333 | 2024-10-09 00:16:07 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 95536cd2-c9e3-37e3-bbe1-0a3317aa4f5f | -10.609 | -57.5319 | 2024-10-09 00:16:07 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 7c4d753b-ae9b-34b1-a074-538deb42d3da | -10.5942 | -64.043 | 2024-10-09 00:16:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 75.5 |
| e6f16096-f926-3b9f-a49b-c39dd48d0fe3 | -10.5943 | -64.024 | 2024-10-09 00:16:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 113.3 |
| b63b6605-6bdc-34fb-98d3-f2a0faca4be7 | -10.8567 | -63.9177 | 2024-10-09 00:16:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 87.8 |
| 7b406d74-5700-3e9d-987e-194f82085e25 | -10.8568 | -63.8988 | 2024-10-09 00:16:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 98dde518-7740-3813-9cd1-a452829e7cd9 | -10.8754 | -63.9169 | 2024-10-09 00:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 129.6 |
| b7ae627e-5934-3fd3-84c2-78e2c78cd289 | -10.8755 | -63.8979 | 2024-10-09 00:16:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 101.5 |
| d2cac1b4-9711-3f1e-bb9a-835cef95a749 | -10.8925 | -64.1623 | 2024-10-09 00:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 15096677-5701-388d-8b83-9d154e2dc444 | -10.8941 | -63.916 | 2024-10-09 00:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 88.1 |
| be0d64b7-90c5-338d-a9e5-1302c75839c7 | -10.9112 | -64.1615 | 2024-10-09 00:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 152.9 |
| ae5d435d-f2fe-38e7-9ad3-ae69610afa67 | -10.9113 | -64.1426 | 2024-10-09 00:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 185.9 |
| a485d7d4-1dad-304f-88a2-69ba227772fb | -10.9082 | -68.3988 | 2024-10-09 00:16:09 | GOES-16 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 52.5 |
| ce579a90-fc3b-3006-9e64-6889b55231a6 | -11.5726 | -58.9619 | 2024-10-09 00:16:12 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| f3f87738-88db-3d44-a85b-7642937da22d | -11.5728 | -58.9423 | 2024-10-09 00:16:12 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 7d209310-e0b6-3ea9-aa39-5402116e6028 | -11.6806 | -64.0312 | 2024-10-09 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 92.8 |
| cc2b4cdb-4238-39a1-b39a-cfef1ab7deb2 | -11.6808 | -64.0121 | 2024-10-09 00:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 1e78b5bd-2142-36cd-b717-5d8fb114f351 | -11.9917 | -51.0766 | 2024-10-09 00:16:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 8eb5a822-b4d3-3a84-a6f5-582b4795fa26 | -11.992 | -51.0553 | 2024-10-09 00:16:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 99.3 |
| dbb09493-4cb0-3c90-9304-de0af31a1143 | -12.0107 | -51.0744 | 2024-10-09 00:16:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 158.0 |
| 4c79d562-6fee-3093-a581-204148698ccf | -12.011 | -51.0531 | 2024-10-09 00:16:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 156.3 |
| 015525b0-6d95-33d3-bd9a-2f5091e02c51 | -12.0298 | -51.0722 | 2024-10-09 00:16:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| d19f7572-19a9-38dd-aa2f-852d3cdf3643 | -12.0301 | -51.0509 | 2024-10-09 00:16:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| d8339b6c-bab3-3249-b67f-20045d541555 | -12.7673 | -44.8904 | 2024-10-09 00:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 159.3 |
| cac6b989-2dbf-3d4a-90b8-b25e4b7362a1 | -12.7678 | -44.8671 | 2024-10-09 00:16:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 107.8 |
| f518ca09-698a-34f5-9fbb-46fdcce7ada1 | -12.6676 | -63.0819 | 2024-10-09 00:16:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 143.2 |
| b3559ad5-5a6a-3837-9e25-a44d381dbb66 | -12.6875 | -62.9656 | 2024-10-09 00:16:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.9 |
| d884343a-e36e-36d7-8d5f-8ea0cec4a6c0 | -12.6876 | -62.9464 | 2024-10-09 00:16:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 0b6130c1-d89e-3ac3-b767-96dc4d88314f | -12.7499 | -62.2883 | 2024-10-09 00:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 60.4 |
| a0ac577d-7e94-393c-bed2-6efae189de6f | -12.7501 | -62.269 | 2024-10-09 00:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 133.5 |
| 52eed234-6f7c-3364-a1cc-136878ad31f3 | -12.7502 | -62.2497 | 2024-10-09 00:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 66.6 |
| efeff4c7-0f2b-30a6-813a-f390a0da64aa | -12.769 | -62.2678 | 2024-10-09 00:16:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 15f85a64-772d-3161-ac28-d419738b376c | -12.9166 | -62.7214 | 2024-10-09 00:16:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 66.8 |
| cf0c46e1-68e9-3c59-9033-e8d90efa8e5e | -13.3978 | -61.9376 | 2024-10-09 00:16:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 117.1 |
| dce5c3c8-359e-3b73-8115-3e4427523a11 | -13.398 | -61.9182 | 2024-10-09 00:16:22 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 136.3 |
| 4b0866e2-7d53-36a9-b825-b3286d3cb24a | -13.417 | -61.9169 | 2024-10-09 00:16:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 1bdd2434-47f1-395b-b1d2-788c8c61c60d | -13.8764 | -44.5386 | 2024-10-09 00:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 70.3 |
| b8bf6cfa-fbce-3ddd-af61-de17be2161f4 | -13.8958 | -44.5351 | 2024-10-09 00:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 287041e7-88ab-3678-9233-e87e8fca4fbe | -13.9153 | -44.5317 | 2024-10-09 00:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| d0be7e7a-fdda-33fe-9e1c-510e9249fda0 | -14.0723 | -44.4563 | 2024-10-09 00:16:25 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| 45324c71-546e-3af7-8ff8-9cbdfd5d02e7 | -14.0985 | -44.1447 | 2024-10-09 00:16:25 | GOES-16 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 674dc676-0447-3ba8-9357-007373d5e658 | -14.1862 | -45.4872 | 2024-10-09 00:16:25 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 154ab9a4-adfb-37bd-ba08-8c067c66a9c2 | -15.6795 | -52.4993 | 2024-10-09 00:16:34 | GOES-16 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 293c2ab5-d5d3-3c2c-9bef-7dcbfca5647c | -15.688 | -59.3945 | 2024-10-09 00:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 5252c368-e11c-396b-bcb1-87d7ef467f06 | -15.6882 | -59.3745 | 2024-10-09 00:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 83dd8289-5c8a-3f21-a330-aa76beb7c8ed | -15.7073 | -59.3926 | 2024-10-09 00:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 1d3b7ac7-4b92-3152-b84a-f245f284654b | -15.7076 | -59.3726 | 2024-10-09 00:16:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 127.1 |
| 833142c9-e1b3-3f41-ade4-dd059da9e60c | -16.4383 | -55.9224 | 2024-10-09 00:16:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 66.4 |
| 653800e5-fcd0-35e6-83ad-cb24344f4fb1 | -16.3988 | -55.9479 | 2024-10-09 00:16:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 65.6 |
| 8133d763-ee17-3100-8c5b-0f044f87ee42 | -16.3992 | -55.9272 | 2024-10-09 00:16:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 53.5 |
| db7b432e-1565-3211-b73f-2d698719fc96 | -16.4184 | -55.9455 | 2024-10-09 00:16:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 140.4 |
| 1d9844f5-069f-3875-b2f2-66d593bc091e | -16.4187 | -55.9248 | 2024-10-09 00:16:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 109.9 |
| 914c91d5-39be-3bc4-8b55-f9d874a568ee | -16.4379 | -55.9431 | 2024-10-09 00:16:39 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 65.8 |
| e1a5124f-c2e2-3b09-a26f-34f8739568bd | -16.6338 | -57.1123 | 2024-10-09 00:16:40 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 69.5 |
| f87a0b94-330a-3cc5-bf7c-0c88694f1b5a | -16.7575 | -56.7081 | 2024-10-09 00:16:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 98.4 |
| 81192e25-458b-3705-8fb8-75095222fdd0 | -16.8045 | -57.4402 | 2024-10-09 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.4 |
| c721a3aa-c8b9-3808-8899-47b65434e1c9 | -16.8048 | -57.4197 | 2024-10-09 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 72.1 |
| 4c6dcd5b-cd31-368d-95d1-8baa08a83d6b | -16.8241 | -57.438 | 2024-10-09 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.4 |
| 666c0e7a-8cf1-3391-ba20-886da08f980d | -16.8244 | -57.4175 | 2024-10-09 00:16:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.7 |
| 7c8d29bb-6971-3b55-a44b-bda82fb0951b | -16.8743 | -56.7352 | 2024-10-09 00:16:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.8 |
| bcd3f1e1-ca99-37fb-b45b-8a03e4158c88 | -16.8747 | -56.7146 | 2024-10-09 00:16:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.4 |
| e76e9501-c379-3c29-bacb-e03454250b06 | -16.8898 | -55.8039 | 2024-10-09 00:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 99.4 |
| ef1c035f-4e60-3f8d-82b2-5e6a87c693b5 | -16.8901 | -55.7831 | 2024-10-09 00:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 78.6 |
| d77228bb-2ce4-3bc9-aea7-e7a0306a9446 | -16.9091 | -55.8222 | 2024-10-09 00:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 62.6 |
| 22ac6367-c8d4-39ba-a2cb-d50fbf578f0a | -16.9094 | -55.8014 | 2024-10-09 00:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 142.8 |
| e604a32d-9e4e-3b1e-a93d-f860530af789 | -16.9098 | -55.7806 | 2024-10-09 00:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 96.8 |
| 0fa8cbfd-26cb-331c-b0be-bd0234acc533 | -16.929 | -55.7989 | 2024-10-09 00:16:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 55.3 |
| 8ffa9e9a-2a50-316f-ae24-6bba6b0918e2 | -17.1074 | -56.851 | 2024-10-09 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 105.0 |
| 6a815f46-d3c6-3041-87b2-f29d285b9b71 | -16.9403 | -57.5063 | 2024-10-09 00:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.9 |
| 5e2b9d07-95da-3ea3-b7df-d5a4de02d1c4 | -16.9407 | -57.4859 | 2024-10-09 00:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 131.2 |
| 20580a60-ce85-377e-b0e8-dcb6108883f1 | -16.941 | -57.4654 | 2024-10-09 00:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.1 |
| a02aa61c-4c94-3aa9-afa3-e7cfed5b2053 | -16.9518 | -56.7875 | 2024-10-09 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 112.6 |
| 476b1b5f-74cb-3a98-afcf-ad189c020a99 | -16.9521 | -56.7669 | 2024-10-09 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 95.1 |
| 993949d0-8183-3991-8ef7-3b253147de66 | -16.9599 | -57.5041 | 2024-10-09 00:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.6 |
| 9b395399-8c65-3589-9bdc-bb5347592086 | -16.9603 | -57.4836 | 2024-10-09 00:16:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 62.0 |
| d2d91d59-7b25-35f0-b963-723090fa4688 | -17.0878 | -56.8534 | 2024-10-09 00:16:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 126.7 |
| 565700e9-7eae-38c8-b5c4-f99bc8e3ee43 | -17.1271 | -56.8486 | 2024-10-09 00:16:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 96.1 |


[Clique aqui para ver as próximas entradas](README4.md)
