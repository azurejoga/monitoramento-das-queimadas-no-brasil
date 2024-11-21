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

## Dados Diários - Página 79

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f94a3d3a-0ce8-35fe-ab9e-181c53fa7118 | -1.52608 | -60.33028 | 2024-11-21 05:48:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8caa9833-19c9-3ae5-a0c9-e424f02986da | -2.71761 | -53.16844 | 2024-11-21 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e6618a0a-9f44-36a1-8a63-3ae29dd26efd | -1.19193 | -53.67675 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91eed675-345d-3931-b6c9-3bd121529482 | -2.3721 | -53.83157 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05c3eb55-ff68-3397-977b-3935212e1b55 | -1.18516 | -53.72141 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 43661e4b-baed-3449-a712-4ac6b8aa8c9e | -1.91156 | -55.3998 | 2024-11-21 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 206431ae-c1ec-3315-a035-c21c6457f9fc | -1.19771 | -53.68269 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c5bb3365-5886-35ab-8c8e-491fcf098c0c | 4.31492 | -61.25382 | 2024-11-21 05:48:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4282878-0d39-31f5-965b-f9639c871cc6 | -2.06817 | -53.43424 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b1dcea06-5d33-3791-9a84-25e8203c2edb | -1.12164 | -53.39436 | 2024-11-21 05:48:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 451ed5c3-67e1-3bed-baea-91645ad6118c | -1.18589 | -53.71663 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 36998587-892a-3743-aa87-300c6d309000 | -2.14065 | -53.77745 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 54a4902b-faef-34d0-abf8-c53882387990 | -1.46427 | -52.66989 | 2024-11-21 05:48:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 2267657b-3ace-309c-89f3-bdc2ef4f0823 | -2.14362 | -53.57327 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7230c3e4-2e16-30d0-9c9f-15468d04c77e | -1.36654 | -55.6988 | 2024-11-21 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9672482e-45ae-35b8-b318-f064f01a2838 | -2.41368 | -54.63778 | 2024-11-21 05:48:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 694772b6-ceca-3280-b894-9a6413827140 | -3.10526 | -53.17564 | 2024-11-21 05:48:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 114bd461-f9c8-3f4c-b860-5c11d83df0aa | -1.72688 | -52.70396 | 2024-11-21 05:48:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| be81a410-6542-30a4-8285-56a5cf9713e2 | -2.41993 | -54.63879 | 2024-11-21 05:48:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d16db073-90cc-3f6f-905f-93b66fb1441f | -2.1463 | -53.57229 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 828df973-dcbb-3043-93fe-b86edf806d3f | -2.023 | -54.5274 | 2024-11-21 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 70bef0f3-d37c-3617-86ec-3ca006fabff4 | -2.01671 | -54.52661 | 2024-11-21 05:48:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 70648dd7-4231-37a7-b0e0-6f52b96cf027 | -2.33769 | -53.92803 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| afa0e1f1-5dbc-38cb-9c34-7ceaf65a56e1 | -1.47408 | -53.48562 | 2024-11-21 05:48:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f094b19e-773b-3c16-bdb6-d5c27af7464b | -1.36798 | -55.69606 | 2024-11-21 05:48:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ab20787-d786-3644-891c-906c042ee84f | -2.61203 | -54.53757 | 2024-11-21 05:48:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 28365d59-c814-3cf7-ac00-8ebc2e9930b3 | -4.58 | -48.0132 | 2024-11-21 05:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 61c2c636-2700-3a04-8f5f-8c9937618519 | -3.2951 | -53.8395 | 2024-11-21 05:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| d6bc791d-6319-3480-86e5-87e8fce2e81e | -3.295 | -53.8597 | 2024-11-21 05:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| d2e14101-703d-3f22-bc96-54262e959693 | -2.0259 | -54.5289 | 2024-11-21 05:50:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 114.4 |
| 8f7e99cc-5ed4-3199-a325-751149cb562e | -4.2388 | -46.1197 | 2024-11-21 05:50:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 06a5ef04-7c5e-3cc8-af3b-00a9845a4480 | -3.2767 | -53.84 | 2024-11-21 05:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| edfef1c5-7f5a-3969-abd5-1fb3c77b137f | -3.28175 | -53.83973 | 2024-11-21 05:50:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 68474450-34aa-3532-b57f-5cfaca425749 | -3.28669 | -53.83403 | 2024-11-21 05:50:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 035f23c5-c847-3174-aff9-df09a9ab77d5 | -3.27262 | -53.83739 | 2024-11-21 05:50:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b74389f4-507d-316a-bdf8-81d6628ca2ca | -3.27923 | -53.83866 | 2024-11-21 05:50:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| d0e89a35-fdcd-3e2a-a26c-204ed407d461 | -3.56842 | -54.68475 | 2024-11-21 05:50:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6a780334-d570-32de-b903-ac88b2568b93 | -3.29748 | -53.85358 | 2024-11-21 05:50:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8906cac-ea3f-329c-a001-6089f0aa06ba | -3.2925 | -53.84092 | 2024-11-21 05:50:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c16c51c4-7dbc-384f-83de-4bb7aabd7c97 | -3.50973 | -53.80433 | 2024-11-21 05:50:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 983b9668-fdbf-3be5-b226-fae1fee0d183 | -3.29084 | -53.85247 | 2024-11-21 05:50:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 6033ba39-6021-36b4-a458-6eb207d7d716 | -3.28094 | -53.82664 | 2024-11-21 05:50:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3a9e8144-9e05-3c54-bf6a-a806e26e06c4 | -3.10724 | -53.74802 | 2024-11-21 05:50:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a16956f9-d178-3bac-aa6f-66271a2ae668 | -3.18955 | -54.32407 | 2024-11-21 05:50:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d79fbe2-9962-32c5-88cf-63103121f05a | -2.94183 | -54.79964 | 2024-11-21 05:50:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9ad736b-137c-3fd8-8fea-7ff58e71105b | -3.57058 | -54.68783 | 2024-11-21 05:50:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cd7f9cfb-83ca-310c-b0f0-76a56f1dabfe | -3.42081 | -53.28981 | 2024-11-21 05:50:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f1c5d3a3-9ca8-3739-b763-cc46529aaa69 | -3.10639 | -53.75388 | 2024-11-21 05:50:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a3135813-b7ca-3f59-be9f-b3881b2084ca | -3.51053 | -53.79871 | 2024-11-21 05:50:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 44ac0871-7aa0-37c7-b05a-2211a3ef7123 | -3.2809 | -53.84543 | 2024-11-21 05:50:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ef24ac88-c4da-37c0-9777-2dbb5d2cfd49 | -3.28438 | -53.82211 | 2024-11-21 05:50:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 06b99016-2b9d-304f-b5bf-ad3394a0ed0e | -3.18313 | -54.32293 | 2024-11-21 05:50:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0015f07c-a20e-3539-b843-ea403d6df836 | -3.26941 | -53.83126 | 2024-11-21 05:50:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6b0c9c49-0a89-37e5-937b-0104ee7b55a4 | -3.18389 | -54.32293 | 2024-11-21 05:50:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b202778c-ca94-3453-a292-41aa79473fb0 | -3.46897 | -54.56294 | 2024-11-21 05:50:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8af44a2-4b5f-3842-8002-f4b927aff51d | -3.27348 | -53.83132 | 2024-11-21 05:50:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 11e19ba8-b918-3a7c-b058-77d91b667e31 | -3.19597 | -54.32523 | 2024-11-21 05:50:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 691b1e4e-112c-3726-8149-8b9c06470e85 | -3.27513 | -53.83852 | 2024-11-21 05:50:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1c253383-5283-3b0b-89a4-b14bda710826 | -3.10808 | -53.74216 | 2024-11-21 05:50:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dda1e118-4f4b-30ab-998e-2a299f762ddb | -3.57477 | -54.68568 | 2024-11-21 05:50:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94fc2c4d-53be-36b8-aae9-237d4d8614fd | -3.28834 | -53.82239 | 2024-11-21 05:50:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8d465046-f347-3cce-a89f-ea84171196d6 | -3.28262 | -53.83385 | 2024-11-21 05:50:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 782d62fa-7323-3ece-a525-687070cc2962 | -3.57132 | -54.68255 | 2024-11-21 05:50:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 21859f4b-2b7f-381c-9a81-51a50b368b08 | -3.19673 | -54.32528 | 2024-11-21 05:50:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2e6102eb-06ff-3994-afde-b7dfdd79927f | -3.42044 | -53.28883 | 2024-11-21 05:50:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 07e9242d-b748-3d95-911f-155255d16298 | -3.10142 | -53.7411 | 2024-11-21 05:50:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9c832abc-df14-367c-a66d-648d9565772c | -3.28009 | -53.83264 | 2024-11-21 05:50:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 903833ab-cc92-3280-a6b5-46909423348a | -3.19518 | -54.33055 | 2024-11-21 05:50:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 968c8a83-1e8e-3f5d-a40e-59920636bbba | -3.28422 | -53.85135 | 2024-11-21 05:50:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 26d71955-5375-38e9-b93e-948fde94924b | -3.66856 | -54.65527 | 2024-11-21 05:50:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 15b4c1da-a7d1-3095-b127-363aa12ff579 | -3.42171 | -53.28331 | 2024-11-21 05:50:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0c9a3fd9-4714-3b58-9475-463841696a51 | -6.44733 | -62.85965 | 2024-11-21 05:50:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd14c0e2-0f00-3e08-838b-76a2d7470580 | -5.14166 | -60.384 | 2024-11-21 05:50:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 9.5 |
| a8cab0d0-23d1-3a68-8a59-28b87c04dab6 | -3.29665 | -53.85936 | 2024-11-21 05:50:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 43021371-d9fc-3181-9b08-536e6002801b | -3.28586 | -53.83982 | 2024-11-21 05:50:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b888e0d7-6c7c-384c-9b31-544a80b64cae | -3.28178 | -53.82073 | 2024-11-21 05:50:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 77469beb-89c8-3758-8222-7f9f0dcb0a7a | -3.29167 | -53.84668 | 2024-11-21 05:50:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 7459fc9a-5434-3403-a7c8-e60f86a6f3c1 | -3.18392 | -54.31755 | 2024-11-21 05:50:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4ef7e0f8-1622-32bc-a9db-44076e83a3da | -3.27602 | -53.83252 | 2024-11-21 05:50:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 45b62826-1a15-3ddb-8c58-1195fe00faa6 | -3.6748 | -54.27707 | 2024-11-21 05:50:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3a51c2b1-8a7b-3b32-a142-7a54052a00d7 | -3.18465 | -54.31754 | 2024-11-21 05:50:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 33b70397-511a-3c1c-bc26-09b7c7575b9f | -3.28351 | -53.82793 | 2024-11-21 05:50:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a32aa582-5422-3f34-9140-16af8ec80d5b | -3.11685 | -59.92913 | 2024-11-21 05:50:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a56643b-71e3-38ef-9e83-99dd8a4828ed | -3.28751 | -53.82822 | 2024-11-21 05:50:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f4ee5e4c-446a-3e2c-a7c7-bd2144d76167 | -3.19031 | -54.32409 | 2024-11-21 05:50:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a0c09f42-c176-3e5e-b68b-647912281e62 | -3.28504 | -53.84555 | 2024-11-21 05:50:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| fad85851-fbd1-3117-93cf-b29c8e588863 | -10.11973 | -65.02818 | 2024-11-21 05:52:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6de514c2-da02-3651-8630-4e79cc8d2036 | -10.19373 | -59.53756 | 2024-11-21 05:52:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 527e59aa-ef62-31fb-a2fe-5aabb9953359 | -10.12033 | -65.02407 | 2024-11-21 05:52:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2aeeab68-bb8a-35fa-abee-3a749bd648d4 | -10.19411 | -59.53463 | 2024-11-21 05:52:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26070f2f-cb02-3757-ba61-b5696fa6c788 | -10.12329 | -65.02872 | 2024-11-21 05:52:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12e34f7f-0fd8-3e0a-ac59-66afe66fd20b | -10.1239 | -65.02462 | 2024-11-21 05:52:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 345d5c99-99be-3641-96d1-92079b4f9ed9 | -4.58 | -48.0132 | 2024-11-21 06:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 001ced38-1820-3bf2-87bf-fc0a5a8996ab | -4.5799 | -48.0349 | 2024-11-21 06:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| f3f91f41-b3d9-3577-8046-377332b761e6 | -2.0259 | -54.5289 | 2024-11-21 06:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 43dfab15-38d2-38ef-9229-d3ddd564a53c | -4.2575 | -46.1188 | 2024-11-21 06:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 71.3 |
| d731c479-310b-3e62-a70b-52e83085c9b7 | -3.2951 | -53.8395 | 2024-11-21 06:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 09a9f1e5-6b84-3330-ae3c-6271493c1865 | -3.295 | -53.8597 | 2024-11-21 06:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 50b96410-a4fc-34d1-820b-3ddca0a7c39f | -2.0075 | -54.5292 | 2024-11-21 06:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 640003e4-5beb-368d-8660-10edd84898ed | -3.2767 | -53.84 | 2024-11-21 06:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |


[Clique aqui para ver as próximas entradas](README80.md)
