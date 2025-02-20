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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 75f89f37-ca06-38fc-8a25-47f9236666ed | -10.75545 | -44.93435 | 2025-02-20 04:50:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fd7430e2-4ca3-3a06-9877-c9d80278865c | -20.73161 | -54.60241 | 2025-02-20 04:53:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d33ddaa-4df8-33f7-866c-2a082172ab4b | -23.13295 | -53.57573 | 2025-02-20 04:53:00 | NOAA-20 | QUERÊNCIA DO NORTE | PARANÁ | Brasil | 4121000 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1a3e8fef-02d9-3041-a19b-a1c505dcf343 | -20.72374 | -54.41343 | 2025-02-20 04:53:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4d803dbe-c6e7-3993-9fff-ab7d634b97e5 | -22.26749 | -48.50233 | 2025-02-20 04:53:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d77355e-b2c8-3b18-a249-8ce791a7ed95 | -22.26872 | -48.49834 | 2025-02-20 04:53:00 | NOAA-20 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cbece284-f707-364b-9144-ead34f59a00b | -23.02616 | -48.43708 | 2025-02-20 04:53:00 | NOAA-20 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ee695f0-ba28-30b8-ba45-9855d8eff541 | -22.67414 | -42.85236 | 2025-02-20 04:53:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a4ace789-04fd-3991-990c-6d9450e7c3bd | -20.73555 | -54.59915 | 2025-02-20 04:53:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 33b8adb4-e0bb-3d65-8b8b-458820777881 | -20.8598 | -54.08486 | 2025-02-20 04:53:00 | NOAA-20 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ce5bf0d-c480-3d85-9b6a-88f9fd1a6db3 | -14.42561 | -45.64898 | 2025-02-20 04:53:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05401304-f1ae-3806-afce-3bfa22b76b51 | -14.4212 | -45.64195 | 2025-02-20 04:53:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1014ae90-4472-3765-8c67-e7debb6d69c8 | -14.45507 | -45.66565 | 2025-02-20 04:53:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 18f9cbbe-fd08-378f-9792-032fdf0d479d | -14.47036 | -45.81783 | 2025-02-20 04:53:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5205d9e8-9ac8-3257-a43f-bd54fced0d1d | -12.80114 | -45.01375 | 2025-02-20 04:53:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9006ced8-6367-3cec-93c1-0c06bb23bc03 | -14.43078 | -45.64962 | 2025-02-20 04:53:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b1bb6bb-9aac-36ba-bb3f-099948a1c23d | -14.45468 | -45.66881 | 2025-02-20 04:53:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 190bd000-2ad9-37c1-bd60-5f9cd2fe50ea | -14.41124 | -45.63748 | 2025-02-20 04:53:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4daf30b2-81fe-3b41-93b6-0d8296a61311 | -12.79667 | -45.00653 | 2025-02-20 04:53:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c11125c-f4cb-3f00-9a97-9e785d723c71 | -15.07846 | -48.94369 | 2025-02-20 04:53:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a41d893-bf40-3720-848c-2cba676a7ca8 | -14.42925 | -45.66237 | 2025-02-20 04:53:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f987fd36-b101-3424-adfa-0ec5c6573352 | -18.44902 | -51.9391 | 2025-02-20 04:53:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ce05b85c-0852-3f9a-9f80-d2ce50cbf9bb | -14.4499 | -45.66497 | 2025-02-20 04:53:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd9d94e8-a5ae-3c9e-8724-f8d7d4e4f465 | -14.47584 | -45.81536 | 2025-02-20 04:53:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9a6adba8-a4d2-31a4-9ac3-0bcebdc9c1e7 | -11.69235 | -47.80148 | 2025-02-20 04:53:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad582b36-9a2c-3cef-b5eb-0ae4d785b274 | -11.57228 | -47.63444 | 2025-02-20 04:53:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4fb5ab6c-e583-3e55-9700-b85986feebd7 | -14.43403 | -45.66619 | 2025-02-20 04:53:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19e1419b-9d7f-332f-8259-f262d65e5265 | -12.80074 | -45.01704 | 2025-02-20 04:53:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 61e12399-46f1-388e-8491-c6b04e36689e | -14.43595 | -45.65028 | 2025-02-20 04:53:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c634563d-f28f-3008-af3b-5461f4fd5c31 | -14.42082 | -45.64514 | 2025-02-20 04:53:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a247caf-6d77-323b-a443-dd0c97f74c03 | -14.41679 | -45.63491 | 2025-02-20 04:53:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dbc6e75a-6e12-32c9-b0f5-1809e20392e9 | -16.68113 | -43.88559 | 2025-02-20 04:53:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ad02ecc2-bdca-346a-9902-f79138c89ed7 | -14.42485 | -45.65535 | 2025-02-20 04:53:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4007cd9c-af94-395c-8947-9e9c51084a5d | -14.4304 | -45.6528 | 2025-02-20 04:53:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa90956f-10bb-3c23-be04-d596bc9a11d3 | -14.42599 | -45.64579 | 2025-02-20 04:53:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 58326398-d959-3103-9648-f8bd512f76d8 | -11.57606 | -47.63919 | 2025-02-20 04:53:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7f2ef281-f621-3d5b-b31e-ac7f134572d2 | -17.4618 | -47.01348 | 2025-02-20 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 85b6e95f-dc7f-3485-8ded-9f3001179c4b | -14.44359 | -45.67382 | 2025-02-20 04:53:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 19c16778-1840-347b-960b-49433c7d8723 | -17.46245 | -47.00783 | 2025-02-20 04:53:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9725d0fc-5811-3e3b-a09f-79163d740620 | -14.44952 | -45.66814 | 2025-02-20 04:53:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 94ea328f-6fe8-3d7a-ba57-86791c99fd22 | -12.79586 | -45.01314 | 2025-02-20 04:53:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35aff4dd-1c7b-3fd9-956d-76f9ba0a123a | -14.47072 | -45.81472 | 2025-02-20 04:53:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 479842ca-b1fa-3037-bab8-42d1afb2fba2 | -14.42044 | -45.64834 | 2025-02-20 04:53:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 853167b3-9074-3740-a20d-b6620aa807d9 | -12.79708 | -45.00322 | 2025-02-20 04:53:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 978ce605-05b9-307d-b0b6-6613ec81a7b3 | -14.42006 | -45.65153 | 2025-02-20 04:53:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 887d7275-6f88-34bb-a954-9b53f1c6d6c5 | -12.79139 | -45.00586 | 2025-02-20 04:53:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0634181c-c20a-30c7-8da9-caafbde2641a | -14.41641 | -45.63811 | 2025-02-20 04:53:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c9d62b11-1677-397e-b542-ad289492414a | -14.42523 | -45.65216 | 2025-02-20 04:53:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1541e044-f95c-38ea-a42b-da58bffdb107 | -12.79627 | -45.00984 | 2025-02-20 04:53:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdb2e5d8-d3c0-380b-aef6-7ff9a701e78a | -14.43881 | -45.67 | 2025-02-20 04:53:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a45eccb2-e6d7-313d-9f94-a8d7ed88a679 | -14.41162 | -45.63427 | 2025-02-20 04:53:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a47ec3ae-73f1-33b5-a00f-e45fd472431c | -29.24669 | -51.95444 | 2025-02-20 04:55:00 | NOAA-20 | ENCANTADO | RIO GRANDE DO SUL | Brasil | 4306809 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 71085b45-0255-34e0-84d2-5385db10cd73 | -30.23124 | -54.48977 | 2025-02-20 04:55:00 | NOAA-20 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| dfbfcd65-a652-3f02-929d-738b68b9acae | -25.19684 | -49.32422 | 2025-02-20 04:55:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 58d0bf59-e7fe-30f8-9ab9-f68e2c5160a7 | -25.1916 | -49.32918 | 2025-02-20 04:55:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2b5a8125-e744-3564-83a3-ae01e9248606 | -25.93063 | -52.39516 | 2025-02-20 04:55:00 | NOAA-20 | CHOPINZINHO | PARANÁ | Brasil | 4105409 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fb3c6d79-b870-385d-a688-2ee21562a518 | -20.20723 | -46.50169 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45fd7598-427b-3724-acce-e0585c491a35 | -20.20795 | -46.49485 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b7883c09-5106-3632-a551-e5db64c0ead0 | -20.20268 | -46.49424 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a916bc5b-912e-305b-8ded-910a959cec61 | -20.2083 | -46.49148 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 058b9084-bbc3-37c4-a77a-995dadb5052e | -20.30788 | -46.50598 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 06efd537-db47-393e-a541-bbdec7f25fa1 | -20.24218 | -46.47398 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5a68377-bc5d-38de-93d7-dcb75cd2cc76 | -20.21677 | -46.5122 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0900d71e-7e68-3bf0-80d0-0bdad9f431dc | -20.20934 | -46.48165 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b99f32db-cea7-395b-b3e7-653deea87c74 | -20.21078 | -46.51848 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ff05e3fd-238d-3d8e-926f-f553f9f91930 | -20.02277 | -47.18125 | 2025-02-20 04:55:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d6859c4d-898a-3d44-b2bb-f08300625637 | -20.29692 | -46.50879 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 366099c0-4252-33e4-86ba-a399d0fd1647 | -20.0231 | -47.17822 | 2025-02-20 04:55:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5936bb52-2d62-3bbd-8097-d506c1600cce | -20.209 | -46.48489 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0b09bf11-5370-3bdf-afcb-77a7c495e0cd | -20.22062 | -46.52603 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8a554520-3aab-3754-b874-ac1b9f1ae779 | -20.22134 | -46.51931 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1dc3a510-4822-3d17-8276-1c403039a356 | -20.25109 | -54.13674 | 2025-02-20 04:55:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01b454b9-5a13-35d6-8522-59f41f6615ab | -20.2419 | -46.47293 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d54c941-674c-37c0-a28e-25492c1f9fb5 | -20.21149 | -46.51179 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7c4aa604-4cd9-356d-9dbd-6bf1e37061b9 | -20.23231 | -46.46198 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fcc873aa-54a3-33b9-82c7-a1172e32ca39 | -20.22098 | -46.52263 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19a6e302-3a60-315b-9b61-1db63405ccfa | -20.30663 | -46.51795 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2a98371-6baf-37c1-8493-d8373b89eeb8 | -20.23302 | -46.45969 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 16f5fbe3-0781-30eb-983f-bc2727d6f682 | -20.24156 | -46.47636 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e52795c7-6bdc-3fa6-ac8a-d20658e23b3a | -20.21043 | -46.52175 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8620ae1-8ed1-3014-b18a-74c6394cb1c3 | -20.30722 | -46.51227 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0788688c-f986-3412-b87e-14dc032db419 | -20.21712 | -46.50888 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e9e8c59-a1e9-3856-973e-4eb101075280 | -20.22274 | -46.4558 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 35bdbda5-872f-39a8-b864-7d4f23996bf2 | -20.22025 | -46.52948 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6232ad07-dc7b-3496-a7f5-4ffb30e60b2a | -20.30755 | -46.50917 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30eed9b0-dab6-30c7-98c3-6fdea40e40d9 | -20.23763 | -46.46219 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57c6ed00-52f9-3e68-b299-23f8a4b9e169 | -20.24181 | -46.47742 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d565f82-3296-3d2f-a404-dac22ed5883e | -20.20687 | -46.5051 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4bba2f6f-8465-3f6e-8e9a-46885eafdc0a | -20.22168 | -46.51605 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86d1a0eb-0640-3ea1-8b66-0e4090180bd4 | -18.94426 | -52.39575 | 2025-02-20 04:55:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 413b7e22-e116-3399-835e-cb60f4f977e9 | -20.29162 | -46.5085 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a950f33f-d6e7-39f8-ad48-6a7b8bef9517 | -20.22804 | -46.45622 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be0839a2-e3c9-3e82-aee9-1bc0790142b5 | -20.22769 | -46.45951 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 81688aad-1f7c-32d7-9afc-916ca0a124d1 | -20.21494 | -46.47906 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c384f2d-efe4-34e0-aa83-74d00ab91730 | -20.29727 | -46.50546 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd17f48e-db6e-3770-8689-2a95c28b1a74 | -20.21536 | -46.52546 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0e0cf55-5761-3a57-a2cc-2d76cdbcce9a | -20.23266 | -46.46306 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 82831852-16a3-3a1b-9697-7e9236584e4a | -20.23798 | -46.4633 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eeba45dd-7cc6-3483-9754-481a636ceb00 | -20.23265 | -46.45863 | 2025-02-20 04:55:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3310cfed-23e0-3a19-9331-18aeea09ee4c | -20.25449 | -54.13729 | 2025-02-20 04:55:00 | NOAA-20 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README7.md)
