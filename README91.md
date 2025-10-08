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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77b71dc3-a2e2-3e7e-a44d-ea66fde483a7 | -11.74958 | -50.92257 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 66bab2f3-ea95-35f7-87c3-d17480aed8fb | -11.16754 | -54.87383 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4e2ff7bb-c75e-3f9c-af76-e9be5187c30c | -11.00691 | -50.89254 | 2025-10-08 05:29:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae4d19df-8d5a-35bd-bf17-60a0a325333a | -10.38651 | -50.23203 | 2025-10-08 05:29:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4818570b-d0db-3ad9-adba-5c7f175cd88b | -9.86855 | -60.3177 | 2025-10-08 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4b31e31d-3f55-3557-ae77-1075f4caefd3 | -11.74164 | -50.93118 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a4e901e3-214f-3295-b8ef-f1c99007706d | -11.17797 | -54.87233 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 078b91ed-3705-3ced-aaee-96d8dd03db74 | -12.32318 | -50.26958 | 2025-10-08 05:29:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| af05c131-47cd-3822-8055-02fbb4028763 | -11.15867 | -54.8633 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70304b52-2361-318f-a0c8-f3f99328ec18 | -11.7351 | -50.9303 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ef034345-45f5-3f9f-8147-8ca2f7584395 | -12.32248 | -50.27594 | 2025-10-08 05:29:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ede639d2-930d-3f05-95d0-37954e416592 | -10.89884 | -51.02058 | 2025-10-08 05:29:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7740eb4c-c8e1-30e4-ae12-31f56bd0bb71 | -11.14516 | -54.88852 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 27a43f84-0700-3988-a477-f06b9bba7881 | -7.87998 | -61.19258 | 2025-10-08 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e505897e-1771-3676-a859-807a0f54d411 | -11.17055 | -54.88776 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| d1866c6b-3bc9-3d13-99d7-575ba0b7b63e | -6.94995 | -63.09649 | 2025-10-08 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0c7e480b-c669-3e39-99b4-4adead330317 | -11.1633 | -54.86708 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 92dc5f96-fb6c-3b04-b44b-3693498571c9 | -11.11888 | -54.04762 | 2025-10-08 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 148f6ac6-e9bf-350d-8ea7-f01b6fdc37a9 | -10.91171 | -51.02226 | 2025-10-08 05:29:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dc2f4249-9e6e-3677-89d8-b25b35afd991 | -11.74045 | -50.94424 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.3 |
| ad1bbe7a-eac3-364b-a50f-d8c0c61b1fe4 | -10.39767 | -50.22531 | 2025-10-08 05:29:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c98b8991-d11d-3dd0-980e-c19d56e28d4c | -10.88261 | -56.06499 | 2025-10-08 05:29:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 089af005-63c3-35ea-a65c-b8e2a5e02b84 | -11.16951 | -54.89777 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4d605ba-fa3a-3f37-a9ca-41d29a5b181c | -10.23741 | -52.69731 | 2025-10-08 05:29:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 159e3377-7b44-3b32-97c3-6bb28cdca884 | -7.82351 | -61.15816 | 2025-10-08 05:29:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ff676030-6a85-3268-aca8-3aede90a9b10 | -10.89382 | -51.01893 | 2025-10-08 05:29:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd875080-0091-3c39-b734-8993fd914c10 | -10.23167 | -52.69656 | 2025-10-08 05:29:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a85ba253-919e-3b02-8554-937710b2eac4 | -11.34078 | -56.20668 | 2025-10-08 05:29:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 979679e3-9464-312f-a2e1-3276780bac9e | -11.74434 | -50.91043 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 33.7 |
| e0503413-4018-3ec1-92b2-ec6caa5f906f | -11.18301 | -54.87294 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 695c3a55-aefa-3c04-901a-5ec420ecdee9 | -11.16913 | -54.89921 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 43488ee0-1afc-3407-9013-9c56f70a0bae | -11.1579 | -54.86926 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 17fbc345-eedd-393a-8d43-e6a920ef1223 | -10.34735 | -50.24899 | 2025-10-08 05:29:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 09ee04be-fcb7-353c-9eb6-e3faa48a932b | -11.17373 | -54.86563 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b1ad5c0-4b54-39d8-9c66-b015fa17963a | -11.74408 | -50.90858 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 30.4 |
| aaee8c04-3e05-3239-b206-1401d10817bb | -11.17415 | -54.9013 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 402cb1f8-fc95-3037-8c7e-01413d0e4f8b | -11.18637 | -54.88383 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 22c0ff83-1a33-390c-b87f-816c816d2264 | -11.74369 | -50.91609 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 3d7ae1a6-8ba1-3f57-8a93-457b53b06177 | -11.15596 | -54.88411 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59f210f9-bcb8-3069-9199-11924507ce6e | -11.13202 | -59.08023 | 2025-10-08 05:29:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cdc7930f-55a2-34a9-9f92-cfcae8387a5e | -10.24367 | -52.69402 | 2025-10-08 05:29:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3ce9159a-dae7-301b-a249-01c27a486361 | -9.33179 | -60.59652 | 2025-10-08 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a38919d8-7ff6-3d21-9e4e-e5886e23e966 | -11.70654 | -50.95126 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 22.6 |
| ebcb8af0-8fe2-36fb-ae32-b53e2fa393c0 | -11.18492 | -54.89545 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 034cac7c-c601-3712-8c53-5882fc96054b | -11.46063 | -50.20565 | 2025-10-08 05:29:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bcd6c719-54d8-3f5b-8aad-2dbe89b15b20 | -11.18223 | -54.87885 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1d2f2b64-ce6d-3893-a31a-041db90c472d | -10.39698 | -50.23132 | 2025-10-08 05:29:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 75566183-8827-372d-9bbb-68906e49346f | -9.38928 | -59.41687 | 2025-10-08 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6ed39bb5-f983-30bf-809d-ef3d65be9f1f | -10.8694 | -53.74337 | 2025-10-08 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ab011244-0023-318c-a1ab-11c69c483da0 | -11.11357 | -54.04684 | 2025-10-08 05:29:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1cd9a88d-345e-3eef-aff8-b505c6587e8b | -11.36336 | -55.18286 | 2025-10-08 05:29:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d10950cf-422f-30f7-974a-514b57a7896b | -6.9389 | -63.12341 | 2025-10-08 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 59ed5b79-0561-3718-ab51-e7646e8153f1 | -11.76495 | -50.89989 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 838f4aae-a33e-3d53-bfcc-6dfba091914d | -11.76594 | -50.89603 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 29.1 |
| bd467130-110b-3b7d-a4a5-e64d8226a498 | -11.16715 | -54.8768 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0f2f0ba2-8545-37a4-9215-5354fc23701b | -11.00715 | -50.88987 | 2025-10-08 05:29:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 193b0e1a-06cb-35bf-a7be-f0959f22a213 | -11.36177 | -55.18229 | 2025-10-08 05:29:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| db81d892-fc2e-3147-90b2-6a74dcb03418 | -11.18674 | -54.88089 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1a0e3adc-cb23-3705-9df9-7c57afa29f93 | -10.23691 | -52.70129 | 2025-10-08 05:29:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6700a907-33ac-3519-81cc-7a366bd3e8d7 | -10.99919 | -50.90276 | 2025-10-08 05:29:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| fef36cee-1485-3da6-9db7-5d2651cec937 | -11.71575 | -50.9865 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 200f6566-772d-38db-94e9-0a19c2514d45 | -12.3765 | -50.30021 | 2025-10-08 05:29:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c3d60fe7-7225-392c-b4c9-900ab1d59a8e | -7.58722 | -64.50753 | 2025-10-08 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ad6fa39a-2db3-31d7-9114-483ba5ea1bb5 | -6.94277 | -63.12043 | 2025-10-08 05:29:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2183b0e0-8097-342e-a968-2a8515cd9c1c | -6.68697 | -58.81283 | 2025-10-08 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb572973-0380-309a-b21d-23b71da17288 | -7.59871 | -64.50167 | 2025-10-08 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7bee8c1c-3cd4-341c-9686-318de521eba8 | -11.16948 | -54.89634 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1fa330b7-fcf8-3a22-af1c-0bccbafecf8e | -11.76397 | -50.91296 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 408c48e7-bf4b-3aff-9a56-085e65bc60fa | -10.40368 | -50.23221 | 2025-10-08 05:29:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 39e69308-2253-3461-8a5d-822a4fa0ca91 | -6.7022 | -58.81076 | 2025-10-08 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4102e6da-9cf0-3909-b6ec-a6cc40ffbf33 | -11.14826 | -54.8646 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 296e950b-808a-3a5f-89e1-b2b8f277a2af | -11.17163 | -54.87899 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d208d284-2f70-3fa3-bfec-fee6e2cdda99 | -9.64185 | -55.08003 | 2025-10-08 05:29:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d4807ed-a9fe-3b05-9cd0-b8973550882c | -11.18032 | -54.89331 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 8cabeadd-90a8-3f07-9521-40aaf095e7d4 | -11.73146 | -50.96402 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9642d863-6ced-3f1a-9b3e-8ed86d53fbc2 | -10.35472 | -50.2439 | 2025-10-08 05:29:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6f14cf4c-4c64-3fef-a302-70562d55ec3d | -11.745 | -50.90477 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 96ede575-db55-3a4a-99c5-6775c27d6809 | -7.4673 | -63.56915 | 2025-10-08 05:29:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f78ee0ce-ab9a-3407-87fa-525aa0f8b263 | -11.18146 | -54.88468 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 6e05a150-bbbf-3e7a-b8e9-391119e3071e | -9.90527 | -54.7257 | 2025-10-08 05:29:00 | NOAA-21 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e44009d-408c-3107-b896-08da0d6bd504 | -10.38288 | -50.23553 | 2025-10-08 05:29:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fb685fb1-7334-3e0f-abd6-058a6bb56f81 | -9.16933 | -59.56514 | 2025-10-08 05:29:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 693f6d5b-f6cc-3793-a920-fc109715f69c | -11.172 | -54.87603 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 01cdf59a-b320-3956-8f7d-2b787de7b97a | -11.13475 | -54.89005 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 091e4034-7bca-35ea-936b-8679c415c3b6 | -10.90528 | -51.02142 | 2025-10-08 05:29:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 67ba4ae9-8874-3e34-a556-91151b15f7f4 | -11.17415 | -54.8999 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 21d9888c-7cd7-3580-9056-28d10227719a | -11.17334 | -54.86863 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 25b4157d-8e23-36a5-9263-9a9fdbd0e9fd | -9.32891 | -60.59217 | 2025-10-08 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21ac69eb-56f1-3bec-bfe2-a13728088ce0 | -11.15288 | -54.86845 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf5131c8-716f-3e0e-8fc5-77c0e59f518a | -11.18243 | -54.8744 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7616a240-f7c3-3560-9130-22b5bd7b73b5 | -11.3414 | -56.20193 | 2025-10-08 05:29:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b2308981-fd98-3ec5-88d4-e09125d2ab8d | -11.15056 | -54.88633 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 10fa1ac7-d221-30f8-89e3-6ea8ebcfba26 | -9.99353 | -60.01387 | 2025-10-08 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55868df0-0e27-3180-b2dc-c2bfde0e1f82 | -9.98997 | -60.01334 | 2025-10-08 05:29:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad2c2f52-2cdc-3cc0-b3b0-ddac891600c1 | -11.14748 | -54.87061 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fea98d2f-3749-3385-b024-9dc31aa4c8f4 | -6.69126 | -58.8091 | 2025-10-08 05:29:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4c37287f-40b2-3974-aaa8-ea8136a74bee | -11.74756 | -50.93767 | 2025-10-08 05:29:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 66484db4-a7c8-306b-9ceb-8f8d4314bd6a | -6.36959 | -58.20881 | 2025-10-08 05:29:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2faca570-c714-34bf-a31d-3618652b0169 | -11.15712 | -54.87521 | 2025-10-08 05:29:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d5dc0d38-94ed-38aa-a5c5-603c63dc2d3f | -7.59468 | -64.50488 | 2025-10-08 05:29:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README92.md)
