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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8baff1de-b9fe-323a-a67f-c52d4aa78290 | -2.94864 | -54.22701 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 42ae5a15-e44a-321a-89f5-a066712caa8c | -2.94815 | -54.43596 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 59bea882-1894-3531-b9b0-dee67499b132 | -2.94805 | -54.23082 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6767f0e7-174f-3b6a-a435-4fbc7bc7fe3b | -2.9475 | -54.21135 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b6cd0aa-e745-3481-9352-983ce1bac255 | -2.94691 | -54.21514 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea0c0ade-ec32-3e93-8b50-d04cda38e43a | -2.94683 | -54.26176 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9df9ff5-8437-3cf1-aebb-b7b41a7ab0db | -2.94633 | -54.21892 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 894c75b8-960d-3ffe-b6d9-0bb39bf1f197 | -2.94574 | -54.22272 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0d9a6a3e-0cf9-3c4f-905e-1b42cce1c0b6 | -2.94515 | -54.22652 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 903b636c-36f0-35b8-a8ff-fd2bd9ce7df9 | -2.94457 | -54.23033 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3cd3a2ed-2495-3489-9680-38e660996a9a | -2.94394 | -54.25742 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c0ace04-089a-311c-be4b-4a9a5e70acb4 | -2.94284 | -54.21843 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c9be0f4f-7e0e-3f5c-87d4-3fed68fff270 | -2.94226 | -54.22223 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e41d8aeb-3f48-31df-b81b-1ea66f459378 | -2.94105 | -54.25308 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1cd0e523-00ce-3c72-9bec-53a729cf246a | -2.94047 | -54.25687 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3cc5e13b-f9bc-369e-bf2a-5416f7021220 | -2.93779 | -54.43435 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cae8c46d-52fc-3346-92fe-26e079c860fa | -2.93758 | -54.25255 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2fe52efa-e9cf-30b2-9677-9bc5c84e01af | -2.93722 | -54.43806 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 87bc6bc2-8c9f-3cac-a677-5745df914fc5 | -2.937 | -54.25633 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0d3ea3c-7d3f-3acb-9e31-90b9481b8f4a | -2.93526 | -54.24448 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8346d560-e70a-34ab-be3c-10444333f0fd | -2.93468 | -54.24825 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7eadc5a-903b-3bd1-910c-9c94a426585e | -2.93434 | -54.43384 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85f9a75b-77c9-39ef-8836-7060162fac89 | -2.9341 | -54.252 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 437492e9-634f-304d-98f7-0740af8e110a | -2.93376 | -54.43754 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5888e90-a411-3791-9e9c-3a3009fc676c | -2.93121 | -54.2477 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d066d874-7867-342b-928c-c8e282766e07 | -2.93063 | -54.25145 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c361ad93-2a4b-3724-9023-039e531e863e | -2.87283 | -54.15764 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 618950ba-3a55-3f49-b04e-c1406afc03a2 | -2.87223 | -54.1615 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f56cb751-939b-35f9-ac34-683251d6318a | -2.87162 | -54.16536 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 39aefeb2-905a-3fa7-b792-df95b8524109 | -2.86874 | -54.16096 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e4332cfd-370b-3389-b5b1-928d8a71090d | -2.86814 | -54.16483 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9fbadb75-6377-3c6b-8945-5f9f9b1e5587 | -2.86525 | -54.16042 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4878d66e-0d40-398d-b428-816416407fa2 | -2.86466 | -54.16428 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fef61303-0093-35c0-97ed-3e1fe7294e28 | -2.86177 | -54.15988 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57f3464b-f594-3929-86d8-0ce74c305486 | -2.85855 | -54.45368 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27ae88f0-ed8e-32dc-8ebf-fe4a5584b39a | -2.85828 | -54.15933 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76c47bbf-5ca4-38b7-ae63-c47941e3a7f7 | -2.85769 | -54.16317 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f19623c-ab8c-3a48-9750-9f082cc873b5 | -2.8551 | -54.45317 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7bb50ec7-cd9e-3205-ab1d-4ddfe4131d75 | -2.8548 | -54.15879 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0aa518f-2d29-3bc8-bb49-59db450759c1 | -2.85451 | -54.45694 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90dc9b1d-3a39-3b9a-b0df-709124824497 | -2.85421 | -54.16262 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99fd3d10-ca96-304a-a6a6-9e712098756e | -2.80963 | -54.51869 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 779fcdbf-e2ff-34b4-a878-6570a26445bd | -2.77582 | -54.41809 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ba5d745-48c2-3013-8abb-08e7bedbbd4f | -2.77524 | -54.42184 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6ebaed4-3a5d-3be9-832e-6bc73fd83fe8 | -2.77328 | -54.41838 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aeed2a33-3b34-3b15-8042-c3304f89cbe3 | -2.77269 | -54.42212 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 304e989e-739a-3f08-970c-a224c1bf6811 | -3.11696 | -54.49191 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b25adddd-1c21-3710-80b8-9ce74be87928 | -3.11409 | -54.48763 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99d73e57-5221-3918-beaf-485de7bd6922 | -3.11352 | -54.49138 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 834197c5-99e5-35b7-9765-4f8f9a3543e3 | -3.11267 | -54.12178 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9250704-5f84-3faa-a2c3-f496f55be662 | -3.10948 | -54.49464 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e199ccb2-7280-31c5-a360-99c9f611447c | -3.1089 | -54.49841 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b1de504-35a0-30f0-b006-f83012e5c7fb | -3.10648 | -54.74097 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a469e25-7a62-31a0-95de-4474a1966e14 | -3.10603 | -54.49414 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 379b8af6-01b6-38e6-8eab-dd2c0ba6e61f | -3.10591 | -54.74466 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 51c2d6e0-bf91-3d13-b466-040b2defa0e6 | -3.10545 | -54.49791 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ec00ff6e-24f7-3f8e-95d5-38e664683af2 | -3.102 | -54.49738 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2db6af3e-ac93-3f88-8226-adffd5ebde1d | -3.09978 | -54.13558 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef1b9451-152a-37b2-a724-de8dc5f7fc54 | -3.09918 | -54.13942 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bec4dce9-3d77-38c4-bd63-c22036f426ce | -3.09799 | -54.14711 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a58e9743-925f-3b6b-beab-9a823568c1e1 | -3.09628 | -54.13507 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2170982b-971a-360c-a2cd-a014a212d44e | -3.09568 | -54.13892 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1c38d720-bd4c-3a17-b84c-e76cb360b329 | -3.09411 | -53.70895 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 054687d6-bb6c-32fd-accb-414bc0140cc9 | -3.09347 | -53.71301 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 05595860-6d7b-317e-992b-7b539c505fd1 | -3.09284 | -53.71702 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec131835-af6f-3954-9572-b5fa2ecdc7a9 | -3.09055 | -53.70836 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ef3c35e3-8363-307c-b16c-0d68584134e2 | -3.08991 | -53.71245 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5639d2a6-7b9b-3bf1-9abc-52576c3030af | -3.08928 | -53.71647 | 2024-11-03 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9422fdb-1e22-367e-bc39-490eab4ae7b3 | -3.0423 | -54.90706 | 2024-11-03 05:08:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b29b8a2-3e99-3414-9bf7-9af1913b8c26 | -3.03947 | -54.9029 | 2024-11-03 05:08:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df30cb16-dd0d-3f90-8677-1a8ecb4a2d40 | -3.0389 | -54.90654 | 2024-11-03 05:08:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87f5979f-0bb3-3beb-b55e-13a22ed1d52a | -3.03269 | -54.54404 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29b13738-c97d-3454-bfcc-632ce98d6c5c | -3.03211 | -54.54778 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e78fa49f-5855-3839-8cb2-a1c4eeda0e27 | -2.99014 | -54.88407 | 2024-11-03 05:08:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e275c63b-2c2c-361c-ac8c-ca882bc65939 | -2.98441 | -54.43016 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f179835f-00fc-3759-ba1c-18063132fbaa | -2.98382 | -54.43387 | 2024-11-03 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3045d466-8482-34ff-ac41-62c96ff837a3 | -2.94761 | -53.67546 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0046b3f-9faf-36be-b32f-5aeb81cdd7c5 | -2.94342 | -53.67894 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9447cde-f997-3f24-8fae-a6068fd128fc | -2.93985 | -53.67839 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d35b9e45-ce42-3970-954f-aedecb592260 | -2.93923 | -53.68241 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56eefc37-d7d5-3669-951c-de9a2b820047 | -2.92916 | -53.67676 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5001653d-f7ac-3dfd-b8f8-5ce279918e01 | -2.92622 | -53.6722 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| beb09cf7-afb2-3152-8e69-f4ea4b0f5a36 | -2.9256 | -53.67621 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81600184-00e9-34df-9fa0-d230dc03b11d | -2.92204 | -53.67566 | 2024-11-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eeeaadae-4dc4-3c48-bf62-b1fd7b6bf4ee | -2.88631 | -53.86102 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f0e6f69-c041-3673-9ade-4f347de724dc | -2.84337 | -53.83556 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b1e06db-07e6-3eaf-913a-d4cbb8a89829 | -2.83983 | -53.83501 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a132ee08-3495-3b48-848d-09b3c273113b | -2.83922 | -53.83894 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f407e37-59f2-3028-9fdb-92a2199865c8 | -2.80986 | -53.70066 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fd2f676a-2a4d-3f26-9112-9c85a0d3d5f8 | -2.79366 | -53.87631 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2c8df8d4-9063-395a-916c-5cf6500c2930 | -2.79305 | -53.88023 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85da0aca-fe6a-3676-937b-ddb29c959ab4 | -2.79031 | -53.8277 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36126bbd-1e7a-3237-b327-8d4b92093dbc | -2.78971 | -53.83165 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0b2f6fd3-b27a-387d-917a-8382711dd3f7 | -2.77954 | -53.87423 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7682ac47-9f1b-366e-a324-f7dfd1ccefd1 | -2.77541 | -53.87759 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54bed189-ec3d-3d66-874f-17d8069d1220 | -2.94067 | -54.13969 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2f4bdc48-3857-3f6b-b1e5-fd964f346e77 | -2.9155 | -54.11324 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bd44c5b4-8dd8-3f9e-a454-99e53e799b1b | -2.91489 | -54.11709 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3ccee422-ad2a-3bf5-8227-45df8bcaf7a9 | -2.91429 | -54.12095 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 99983395-774b-39ca-915b-9e0df557594c | -2.912 | -54.1127 | 2024-11-03 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |


[Clique aqui para ver as próximas entradas](README70.md)
