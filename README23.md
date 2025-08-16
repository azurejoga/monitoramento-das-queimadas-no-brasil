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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd7d9152-b31a-391d-80f3-ef90f17977f2 | -12.60257 | -46.9438 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| cbeb2ebb-0b52-31ed-8d7e-8cf5f1380b7c | -10.9585 | -45.18703 | 2025-08-16 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7e99342c-25c5-3028-b651-fbad9c1c89bb | -12.57326 | -46.94535 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3669bcf1-51e3-32c5-9c0f-90062c624fdd | -11.31011 | -42.13074 | 2025-08-16 03:45:00 | NOAA-21 | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cf8fd0ae-bc23-34b9-828e-5b6ec84be9ac | -13.57144 | -46.97389 | 2025-08-16 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 42f7ea30-a664-3b76-bab7-52bfbeeca8c2 | -12.59502 | -46.92302 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| f770f15e-7998-3cb0-8bd5-5e3da383a419 | -12.29753 | -50.01514 | 2025-08-16 03:45:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fc3acfd9-52fa-3cc8-836e-9efb5146c524 | -12.58665 | -46.93621 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7beea492-cde6-3ae5-ab1b-d589da2e8382 | -7.36628 | -43.82831 | 2025-08-16 03:45:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11fecf79-437d-30fc-b024-0bf947f1cb6d | -12.59366 | -46.93 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 9421bd70-02a1-308f-b7d3-8d4c9846369b | -8.18504 | -45.02182 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0fddb220-6eab-36e8-a577-0978855cc954 | -8.34465 | -44.94829 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| df5741ea-a569-32bd-8911-d5439c768dd7 | -8.19037 | -45.02275 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d0d147c-0edf-330e-9ea8-a74eb903368b | -12.61213 | -46.95435 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e5b3c460-f9e9-3646-aaab-df3851a0792a | -12.59946 | -46.95984 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 96f865ab-cad8-35af-af52-81a3205b57f6 | -11.25707 | -50.47985 | 2025-08-16 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| afa21751-f6af-326e-b1fd-6467faf81317 | -12.60822 | -46.96458 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c0888253-e7a9-38b9-ab85-8188f5d6cec7 | -13.41917 | -43.67632 | 2025-08-16 03:45:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 692ef050-4093-3dfd-974c-cd9072e9f8c5 | -12.80119 | -45.96564 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5fd779af-641e-3110-a289-ef82f8b434d0 | -13.57104 | -46.97703 | 2025-08-16 03:45:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 54b7b947-256a-3fcd-963d-29ea67b7e9d6 | -12.82174 | -46.00014 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0d7a9369-e552-3eb3-ac9c-16789c5212ba | -12.54769 | -46.95725 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| aa8dfddb-55de-300b-a450-3b8fe1a3601b | -12.56998 | -46.96212 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1a118339-9b23-3e82-8d8e-6643bd95fcbb | -8.18853 | -45.03305 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b41cd486-92be-3df6-abb1-09e9f1e51abb | -12.82754 | -45.99826 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fba00b03-9d29-3654-b250-2f0bcaaa69d0 | -12.46322 | -46.98465 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37acf163-4617-3606-bb18-a677d63f48ae | -11.25849 | -50.47293 | 2025-08-16 03:45:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8c5ba9b3-e3ba-3682-955b-ec81ce232a32 | -12.61856 | -47.87248 | 2025-08-16 03:45:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 73500ed6-3952-3331-a946-df28ac537c97 | -12.84028 | -46.04467 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8380cfcc-bab1-3d9b-ac71-cf47d58d7bec | -8.29797 | -44.9649 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2cf466e3-791e-3388-b506-259d46c0a7ce | -12.60215 | -46.9161 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 08e40dae-2507-3000-878a-323fe1d1c784 | -9.18385 | -45.32505 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a51a5808-d6af-3086-ac1f-0d9239842938 | -7.39569 | -44.89855 | 2025-08-16 03:45:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc3f4eb0-0d02-39ca-b1e3-8a72d324d885 | -9.81234 | -48.54132 | 2025-08-16 03:45:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ce6bd427-8c3e-381a-a8bb-d382e9508bb7 | -12.59232 | -46.93687 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e57d2ad2-9f29-3785-bc93-3c104bac956f | -8.16841 | -45.02251 | 2025-08-16 03:45:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f9b767b1-794b-3a0e-8c75-11fae71c4180 | -9.26356 | -44.55584 | 2025-08-16 03:45:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 99afd859-d9c6-3f8d-8ff2-e81325cfed83 | -11.99522 | -44.53956 | 2025-08-16 03:45:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a69397d6-8ef0-3382-bc17-8909f30cca21 | -12.57076 | -46.95814 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 82c6018f-1dc2-3bae-b947-7a8917ca5c00 | -12.84426 | -46.05223 | 2025-08-16 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| daebb7a3-c8cd-3665-add7-b4c0df60bdea | -12.56148 | -46.94625 | 2025-08-16 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a52cffe8-dabc-31a7-a1e8-b76464f53e7c | -7.14664 | -44.3905 | 2025-08-16 03:45:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7292ff40-b3b3-32f1-a6c2-2c06c37ae3ee | -20.66738 | -49.3919 | 2025-08-16 03:47:00 | NOAA-21 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e4a66aa-99de-38d1-b2a8-f9f0ba996696 | -18.12317 | -44.99686 | 2025-08-16 03:47:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bdf4a9fb-b4a2-30d2-bb7e-8bfeb938dbfe | -20.05164 | -44.63535 | 2025-08-16 03:47:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 770060f0-ea7a-3cb4-81d6-42ec3907758a | -17.21304 | -49.58584 | 2025-08-16 03:47:00 | NOAA-21 | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 94f8bdbd-6054-31e1-8054-ededc225ac85 | -17.60739 | -46.68405 | 2025-08-16 03:47:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e8a638af-5276-34a5-a6ae-d9e90b7d3881 | -18.95101 | -41.00795 | 2025-08-16 03:47:00 | NOAA-21 | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 79f1405a-2f95-3ac7-b3b8-3edb7332f510 | -20.07856 | -49.42717 | 2025-08-16 03:47:00 | NOAA-21 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 5627ed52-1ff7-3f8c-9488-bff2d16980c0 | -20.40656 | -42.40139 | 2025-08-16 03:47:00 | NOAA-21 | PEDRA BONITA | MINAS GERAIS | Brasil | 3148756 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 19e435dd-eaf2-3266-9afe-38445115ca07 | -19.53337 | -43.6253 | 2025-08-16 03:47:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b36d9e7e-0df3-341e-9266-a585bd2d4412 | -20.08516 | -49.4242 | 2025-08-16 03:47:00 | NOAA-21 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 14.9 |
| 84f8ecee-e37e-39fb-8a07-448d30faf75c | -14.61736 | -47.92411 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 04b0a331-095d-371e-bbe2-29e26fab07db | -21.0624 | -50.30633 | 2025-08-16 03:47:00 | NOAA-21 | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 223ceae1-8a36-33eb-b503-ac44a6758ff8 | -19.29903 | -46.21097 | 2025-08-16 03:47:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20d5c003-12aa-3c39-b139-0b183e86e564 | -14.58537 | -47.93443 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 91f89ee8-de37-3b67-a0d6-423a74f9c1e2 | -21.06343 | -50.30189 | 2025-08-16 03:47:00 | NOAA-21 | BURITAMA | SÃO PAULO | Brasil | 3508108 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| e54e7eb0-5521-3e06-a99f-e5d233e76b5c | -20.40988 | -46.49003 | 2025-08-16 03:47:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa0ad9e4-aba1-3d1a-9f76-bd53ab3b5084 | -14.5879 | -47.92234 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c7f0bb3e-3156-3d75-8511-939c959ea141 | -18.72709 | -39.81982 | 2025-08-16 03:47:00 | NOAA-21 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 66ea68b4-6256-3888-b12a-ec2d8c2fbc2b | -24.91708 | -52.36242 | 2025-08-16 03:47:00 | NOAA-21 | PALMITAL | PARANÁ | Brasil | 4117800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e68ea484-4670-39c6-88f6-11edfe90857f | -20.4209 | -46.53268 | 2025-08-16 03:47:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1d62178c-3ff0-3b8d-a8b4-89c1c2670ac5 | -21.55301 | -46.85273 | 2025-08-16 03:47:00 | NOAA-21 | SÃO JOSÉ DO RIO PARDO | SÃO PAULO | Brasil | 3549706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c65a90e4-b4c8-3e46-b209-51d3e164baf4 | -18.04633 | -47.72666 | 2025-08-16 03:47:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 71b20cf1-5e28-3b93-825f-2972e2861805 | -18.22553 | -45.2222 | 2025-08-16 03:47:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 23e9799c-0593-3991-a1b2-e123efc85751 | -20.05246 | -44.63111 | 2025-08-16 03:47:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5659b2a0-bed8-3220-a2d6-ef9aaa422647 | -20.01265 | -41.88468 | 2025-08-16 03:47:00 | NOAA-21 | SANTANA DO MANHUAÇU | MINAS GERAIS | Brasil | 3158904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8573a653-3efb-375b-a84b-86006bf15db3 | -17.88848 | -39.76553 | 2025-08-16 03:47:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9b169339-0def-3f72-bab3-1c7b1f989ced | -20.41251 | -46.50124 | 2025-08-16 03:47:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0d1fc749-90e3-3978-abbd-4d92e630b408 | -16.22715 | -51.12538 | 2025-08-16 03:47:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4a1fdfc2-080c-3092-a21b-32bbb3441ad6 | -14.58456 | -47.93333 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9af69c3b-199b-3fd0-a43d-c77fee5de32e | -14.59064 | -47.90919 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 134f0ad0-172c-3f2a-867b-7f8bb1bc2d14 | -19.5326 | -43.62942 | 2025-08-16 03:47:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e25aaed-2a5d-3eed-be9a-f76ce80d2c72 | -20.00912 | -46.4327 | 2025-08-16 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 423f68f6-d070-3055-9487-8b3270288730 | -19.36942 | -41.7541 | 2025-08-16 03:47:00 | NOAA-21 | TARUMIRIM | MINAS GERAIS | Brasil | 3168408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8ab580bf-78ac-349f-8043-0be253e55d23 | -16.68212 | -41.34986 | 2025-08-16 03:47:00 | NOAA-21 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e9ca2bb3-e6b7-339d-a812-84970847f257 | -21.52709 | -49.14364 | 2025-08-16 03:47:00 | NOAA-21 | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a6fe1a8b-12f0-3558-b611-309371d79e27 | -19.6649 | -49.37899 | 2025-08-16 03:47:00 | NOAA-21 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6615e490-d250-365a-8631-c5d54bf0de40 | -19.95346 | -44.14273 | 2025-08-16 03:47:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| b97cf6e1-8b3f-3022-921d-80b68d3f882a | -20.42887 | -46.51729 | 2025-08-16 03:47:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2bb7301e-500d-39b8-b227-96a5affc95e6 | -17.60801 | -46.68104 | 2025-08-16 03:47:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2e01fab2-fe2a-3f6c-b62e-2152ba988802 | -14.6183 | -47.91959 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 78629417-f177-3882-9ef5-63d5676bdda0 | -24.91674 | -52.36285 | 2025-08-16 03:47:00 | NOAA-21 | PALMITAL | PARANÁ | Brasil | 4117800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| b6706ce1-8332-357e-93ff-1a1958693557 | -17.33621 | -46.56326 | 2025-08-16 03:47:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 95fb920a-9f86-366d-991d-d52151c65510 | -18.87289 | -40.14595 | 2025-08-16 03:47:00 | NOAA-21 | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 8f820233-a82e-3f93-a350-bb8032fc0086 | -18.48153 | -50.42996 | 2025-08-16 03:47:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1843e5ac-b755-3587-ae2f-5370c42e96b8 | -20.00504 | -46.43424 | 2025-08-16 03:47:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5e813375-25f6-3f3f-b3f1-d2e5d53fbe25 | -18.50896 | -43.64752 | 2025-08-16 03:47:00 | NOAA-21 | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2337f0e-c9b2-36cc-90fa-667939a4a808 | -20.4153 | -46.53615 | 2025-08-16 03:47:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ded653a9-6004-3637-b029-d5240019a8cc | -21.51661 | -45.45196 | 2025-08-16 03:47:00 | NOAA-21 | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 874b6ac7-c22f-326a-a93e-7bcc4fb0f104 | -20.66827 | -49.38786 | 2025-08-16 03:47:00 | NOAA-21 | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 341b8d96-1ce0-37cf-a397-63be7612384b | -21.52627 | -49.14734 | 2025-08-16 03:47:00 | NOAA-21 | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 48aae0cc-6a83-383a-9c08-6f25c54b6a48 | -17.37591 | -48.16229 | 2025-08-16 03:47:00 | NOAA-21 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2f51c615-9d70-35b9-a045-ef5c15a5fa2a | -17.60862 | -46.67802 | 2025-08-16 03:47:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 048328ec-7ae7-39c0-a500-fdbd6a96c120 | -21.04889 | -44.10874 | 2025-08-16 03:47:00 | NOAA-21 | PRADOS | MINAS GERAIS | Brasil | 3152709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8e65c5c9-e3ce-3e8e-9f51-748cb05498bf | -20.39488 | -46.49166 | 2025-08-16 03:47:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1836d9b6-2cfb-34f8-a165-1e1931a4f8f7 | -14.59688 | -47.9314 | 2025-08-16 03:47:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 651c5b7f-32ea-389c-b9ca-5129bf77d925 | -21.38283 | -45.74104 | 2025-08-16 03:47:00 | NOAA-21 | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2df1dd0e-d39b-3e1f-bea7-a2732a462bb7 | -20.41484 | -46.54479 | 2025-08-16 03:47:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f50434ef-bdd3-3f8d-9f0d-ef5e6ce1b5f3 | -18.12222 | -45.00166 | 2025-08-16 03:47:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README24.md)
