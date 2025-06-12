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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 47dcd0ca-5b49-3643-8fd4-72a7384175be | -20.55929 | -50.10456 | 2025-06-12 04:53:00 | NOAA-20 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| afee2329-9d8a-33c5-b0a4-e1c1d4c13ffb | -20.60673 | -48.87583 | 2025-06-12 04:53:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f10e29f8-753b-37fa-9d2c-aed6f3013420 | -20.60429 | -48.87198 | 2025-06-12 04:53:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d58581c8-41c6-373c-8835-1f0df9aa42f9 | -23.23755 | -51.28337 | 2025-06-12 04:53:00 | NOAA-20 | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 77a1f737-9f89-32da-88e6-1936eb269aa4 | -20.37925 | -55.0389 | 2025-06-12 04:53:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 224533fe-a570-3960-ade4-b89e3b72083b | -21.82488 | -56.26487 | 2025-06-12 04:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c3434c31-bb8d-3484-8cdd-17268fc36ddd | -18.65066 | -55.71886 | 2025-06-12 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| a64d7975-9ec8-315e-b885-5a8ca546bd7a | -20.4391 | -46.40908 | 2025-06-12 04:53:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a217a21d-c9cd-3070-be5a-5baf7a6992f6 | -20.43377 | -46.40882 | 2025-06-12 04:53:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 65581c98-e20b-3dd2-9221-f9e5ec5aeb67 | -18.66318 | -55.74722 | 2025-06-12 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 2e5703dc-10f1-3d28-b96e-403abf09c040 | -21.89173 | -56.29175 | 2025-06-12 04:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aa0bbc00-a680-37b4-98d6-290abbc1a7ef | -20.45024 | -46.40525 | 2025-06-12 04:53:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cacc355f-6505-38f6-abcd-f0571613f1a0 | -20.44612 | -53.31633 | 2025-06-12 04:53:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.1 |
| ff094b95-e7f1-3435-a1ee-84602a981f14 | -18.66376 | -55.74358 | 2025-06-12 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| ab59bb95-b96d-304e-9bd9-297001df8b10 | -20.4493 | -46.40588 | 2025-06-12 04:53:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| acab5eaf-8a01-3d53-b99e-f62f41488f15 | -20.44397 | -46.40561 | 2025-06-12 04:53:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0731220a-f01c-39a6-8db8-06563ced4317 | -19.08213 | -53.46832 | 2025-06-12 04:53:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82fb946c-d98a-3d7c-ad7a-c32aa72f7c95 | -22.77016 | -49.32071 | 2025-06-12 04:53:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d5956846-c621-3bc9-8460-5767a03058a9 | -21.75095 | -53.27081 | 2025-06-12 04:53:00 | NOAA-20 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e0273ad8-a295-3626-a49d-c818f5f51ded | -19.05122 | -53.46324 | 2025-06-12 04:53:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7598438-c2e0-321c-a9ec-3851534191f2 | -21.8282 | -56.26547 | 2025-06-12 04:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3ee0eb1b-cf7f-3c8d-bfae-7a1e5549a23b | -21.81789 | -57.54756 | 2025-06-12 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dc17b7cd-178c-33b9-987d-3570bdec3181 | -20.73235 | -56.65675 | 2025-06-12 04:53:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 17fa1738-bee5-3ad3-9cfd-b4894ac14604 | -19.57805 | -49.10815 | 2025-06-12 04:53:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 34ea0b32-84b1-30a9-8c44-1c2a85f039ce | -20.44449 | -46.40887 | 2025-06-12 04:53:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa03235a-6d58-3638-ae9b-37e171171ec8 | -18.40814 | -55.57672 | 2025-06-12 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 15f25df8-a856-3e85-8a35-efe39c26566c | -20.99421 | -51.79332 | 2025-06-12 04:53:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 387c6867-0332-3db1-9576-398e0e3f8e12 | -18.65944 | -55.72787 | 2025-06-12 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 9dd52031-d6ce-3ed7-a8c1-b05b164c9b97 | -20.43421 | -46.40465 | 2025-06-12 04:53:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f7b319b-ed77-38d8-bd3e-33c21ed89fcd | -22.77468 | -49.32125 | 2025-06-12 04:53:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a67d9ce-104f-3d71-a008-a52ad05435a5 | -20.43861 | -46.40554 | 2025-06-12 04:53:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f17e1705-21fc-352f-b81f-3c83a7cc583f | -20.43956 | -46.40477 | 2025-06-12 04:53:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11ee0a2c-2f20-3d23-8cbe-8c5d01f82dfa | -21.82761 | -56.26918 | 2025-06-12 04:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0142463a-778b-3832-aeaf-ad27b9a6e685 | -20.55785 | -50.10559 | 2025-06-12 04:53:00 | NOAA-20 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 636fcfab-8128-3e21-8df1-60f26941b4e5 | -20.72903 | -56.65617 | 2025-06-12 04:53:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b2e4401e-139e-38ee-a306-666727a1a85a | -20.9226 | -49.09435 | 2025-06-12 04:53:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 2adbf16b-d77f-3989-ba14-77012b88827a | -19.0827 | -53.46442 | 2025-06-12 04:53:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6bfb96e1-dcba-308d-bd30-6b141764f4c1 | -18.65339 | -55.72307 | 2025-06-12 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| c336da07-08d0-3e24-8c87-703b8803e494 | -19.05179 | -53.45933 | 2025-06-12 04:53:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 240b365e-2240-3372-a707-386ce17bd75f | -23.23708 | -51.28717 | 2025-06-12 04:53:00 | NOAA-20 | CAMBÉ | PARANÁ | Brasil | 4103701 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 914fb364-a482-3d84-92eb-4f96468a9037 | -20.56201 | -50.10619 | 2025-06-12 04:53:00 | NOAA-20 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2f3c8708-9758-35b5-8373-22c0ad75e2ff | -20.7257 | -56.65558 | 2025-06-12 04:53:00 | NOAA-20 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e1d43c43-939b-3d5a-8b42-b28ec1c67282 | -18.66276 | -55.72845 | 2025-06-12 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| b6acc331-2b80-3a6d-9fbc-d1bb5357270c | -19.8932 | -54.66827 | 2025-06-12 04:53:00 | NOAA-20 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac7fa6d6-e0cf-3398-8275-941d2caa7ef0 | -20.44357 | -46.40961 | 2025-06-12 04:53:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ab468c4c-274e-3369-bd65-bf174d7502aa | -19.08327 | -53.4605 | 2025-06-12 04:53:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8ff6df41-12ca-3170-8183-297d647efd15 | -21.04135 | -55.63058 | 2025-06-12 04:53:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a4a824b6-6dc6-31b4-9583-18fc80907089 | -20.37592 | -55.03832 | 2025-06-12 04:53:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2abf1f1-571a-3e0c-8ab3-4ba8ec2a1237 | -18.66218 | -55.73209 | 2025-06-12 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 36151636-9772-33cd-ba42-f09b6f02bd6c | -20.55735 | -50.10953 | 2025-06-12 04:53:00 | NOAA-20 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| f3bba792-3cc3-3ec4-9a21-3e1fd2a33b71 | -22.26965 | -54.15759 | 2025-06-12 04:53:00 | NOAA-20 | DEODÁPOLIS | MATO GROSSO DO SUL | Brasil | 5003454 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2199c691-bc88-32ae-8b31-0b3c091a96b2 | -20.44491 | -46.40487 | 2025-06-12 04:53:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 973e00f3-8654-30b0-a6e3-54b540dd2832 | -20.60221 | -48.87524 | 2025-06-12 04:53:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 5dc8ff30-f093-3f08-be3b-12b98304b057 | -21.6127 | -57.57665 | 2025-06-12 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1b85d14f-cea0-3dcd-b1ef-eabea160c3ea | -20.55881 | -50.10852 | 2025-06-12 04:53:00 | NOAA-20 | NHANDEARA | SÃO PAULO | Brasil | 3532603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 486b5e90-51ce-3d07-b004-d42d67bc311b | -20.72368 | -55.02824 | 2025-06-12 04:53:00 | NOAA-20 | TERENOS | MATO GROSSO DO SUL | Brasil | 5008008 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c88e584e-8984-34cf-9c77-d1334ee43f58 | -21.61334 | -57.57281 | 2025-06-12 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be4fdf08-e498-3375-b6d7-e1a9711f6ec5 | -18.66102 | -55.73936 | 2025-06-12 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 8718eb4e-8619-3977-a457-33676c4e5285 | -20.54741 | -55.83665 | 2025-06-12 04:53:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9e65d916-0de6-36f6-a3ad-d71efe825045 | -20.44984 | -46.40892 | 2025-06-12 04:53:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7658d0f1-4e44-3451-9d0f-84406523e71d | -20.44961 | -53.31691 | 2025-06-12 04:53:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 70b44f17-b484-3ed0-8fbc-5c38b159c92a | -18.41088 | -55.58092 | 2025-06-12 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 1d6f6701-a162-387c-8f6e-faef4bcdd27c | -20.43819 | -46.40983 | 2025-06-12 04:53:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60fb07c2-fca2-3090-a192-b7af0cd3fca3 | -20.60376 | -48.87671 | 2025-06-12 04:53:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 4086ad70-d5ad-365b-be7c-08e9e45e21d1 | -18.66707 | -55.74416 | 2025-06-12 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| c8d936ba-4b69-34ba-9818-972e6225f8ee | -30.80274 | -55.37773 | 2025-06-12 04:55:00 | NOAA-20 | SANT'ANA DO LIVRAMENTO | RIO GRANDE DO SUL | Brasil | 4317103 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 6979b2e7-f94b-3543-9f58-c1fbd8a74244 | -25.19297 | -49.32671 | 2025-06-12 04:55:00 | NOAA-20 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 53227300-dddc-3a86-a16b-d7173b8774bc | -24.2414 | -50.74012 | 2025-06-12 04:55:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7a812093-96d9-3e7a-a045-5d3eb06947b0 | -26.7282 | -50.12537 | 2025-06-12 04:55:00 | NOAA-20 | PAPANDUVA | SANTA CATARINA | Brasil | 4212205 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 385e136c-38b6-3db9-82ae-72e709ef3197 | -13.8864 | -54.6519 | 2025-06-12 05:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 892d539a-941f-31f5-b96d-e8efcc5be3f7 | -13.8864 | -54.6519 | 2025-06-12 05:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 0c2c3f6b-270e-3197-9d24-682530a39e96 | -13.9056 | -54.6498 | 2025-06-12 05:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 1fdb21c9-fec6-3f4e-a742-4868b46803aa | -6.94051 | -42.80286 | 2025-06-12 05:33:00 | AQUA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 4d35b5f2-c9f1-3b4d-95a3-7d754f1f2bfb | -5.77447 | -43.61675 | 2025-06-12 05:33:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c1e8cc7d-1638-3c39-bae6-e4be8ee052db | -6.9459 | -44.56667 | 2025-06-12 05:33:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 007f2864-bd98-3ad5-a689-acb150c0c2f3 | -6.95847 | -42.80543 | 2025-06-12 05:33:00 | AQUA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| bb031ebd-537e-3e49-834b-e00f4efdd661 | -6.94724 | -44.55782 | 2025-06-12 05:33:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ded84af1-509c-3a0a-b2d0-a674b48cca30 | -7.2246 | -44.79116 | 2025-06-12 05:36:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| fa23b88a-8d14-3bdd-92fa-3567132cbbbe | -17.28224 | -42.66184 | 2025-06-12 05:38:00 | AQUA_M-M | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 3df97fc2-e17e-3a3b-b3c6-cb50fda2ba08 | -10.64391 | -49.42234 | 2025-06-12 05:38:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 404433bd-ee24-3173-a82c-118ce6f4f4b1 | -13.89131 | -54.64127 | 2025-06-12 05:38:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 84.8 |
| fd4a0fbf-d9d0-358b-b84e-7be2bc1199f9 | -12.82456 | -47.37829 | 2025-06-12 05:38:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 78e8affb-195d-311d-9c9a-c7a4c97d794c | -10.65485 | -49.42411 | 2025-06-12 05:38:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| e22c8961-d970-32e1-996c-974409de5af1 | -15.37245 | -47.87856 | 2025-06-12 05:38:00 | AQUA_M-M | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 15.6 |
| af8d8bf1-ba52-3a09-8c9e-e64dd123c8c2 | -11.5751 | -47.42868 | 2025-06-12 05:38:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 613697f0-5c43-351e-8579-69eb5f04d6ae | -10.69802 | -49.51185 | 2025-06-12 05:38:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 98b94bd5-1fb0-3e71-b79e-66dbc23a0f2d | -11.57345 | -47.43894 | 2025-06-12 05:38:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| c0f037d9-8c3e-3c48-8169-08559d94b95d | -11.56976 | -47.4317 | 2025-06-12 05:38:00 | AQUA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| f9fe5c71-26f7-38c7-9e1e-90b1e9dce608 | -11.84289 | -43.79642 | 2025-06-12 05:38:00 | AQUA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f519bdd7-4e98-364f-876b-a18c900d09cf | -14.17684 | -45.48923 | 2025-06-12 05:38:00 | AQUA_M-M | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 7b4773ee-0fa6-3807-9cbc-0818302e64d7 | -10.65557 | -49.35174 | 2025-06-12 05:38:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 74e33cdd-99d3-30e6-aea5-c2f0ebe0d2ed | -10.65716 | -49.41006 | 2025-06-12 05:38:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 20daf6df-adef-3ffe-a03a-df9592d7ce09 | -7.8259 | -63.86435 | 2025-06-12 05:42:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a997bdd9-a1eb-36e6-a6dc-279965ec6ea0 | -7.89422 | -61.47272 | 2025-06-12 05:42:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6bdde844-7b13-38d5-9439-fbb5ba62cdbf | -7.8293 | -63.86488 | 2025-06-12 05:42:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ed9c5c2-b392-3723-b7e0-55233159bb08 | -7.77738 | -61.36974 | 2025-06-12 05:42:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9e52cd53-ebdd-335d-a130-2dbdac84d44c | -9.18368 | -61.86612 | 2025-06-12 05:44:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b14da9d2-51c6-38f0-859c-710efe6968dc | -10.87633 | -54.74626 | 2025-06-12 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d516287e-241c-30ca-9ab2-3535ed12311c | -12.43268 | -54.87591 | 2025-06-12 05:44:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91eeb8ba-2aa3-395c-9eb9-898395299d69 | -9.25246 | -57.53708 | 2025-06-12 05:44:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |


[Clique aqui para ver as próximas entradas](README21.md)
