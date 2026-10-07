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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 868d7cbf-525f-3447-ad65-6aae6ed7b556 | -3.67199 | -60.54099 | 2026-10-07 00:56:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 00bf2e3c-c00d-3566-a747-47651aa7d314 | -2.15163 | -59.23071 | 2026-10-07 00:56:00 | TERRA_M-M | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 8561a310-9b63-3999-bd04-f149e4ba53e3 | -3.88784 | -59.33142 | 2026-10-07 00:56:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 39.9 |
| db1b2559-d0ba-331a-824a-b402567378c9 | -3.58703 | -54.32547 | 2026-10-07 00:56:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| 6289e5cb-0ce4-3aa1-bb49-fc8767b8a283 | -4.38617 | -59.90321 | 2026-10-07 00:56:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 7273f093-268c-3933-a30e-66100fa43d74 | -3.74323 | -59.44229 | 2026-10-07 00:56:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 069f1d70-aab4-32e4-b34d-2bb759b6c6fb | -3.55553 | -59.49743 | 2026-10-07 00:56:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 0bedd16c-7245-3215-bfa5-f29cb9761ac0 | -1.29034 | -54.55075 | 2026-10-07 00:56:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 0e5b336b-f0cc-3639-acea-d1dbb71da752 | -3.05088 | -59.90619 | 2026-10-07 00:56:00 | TERRA_M-M | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 334387b8-5e0b-3f86-8078-7111307452d9 | -4.92069 | -55.87514 | 2026-10-07 00:56:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 091fa44c-bdca-3aa2-97fe-85782319ebec | -2.1579 | -59.2233 | 2026-10-07 00:56:00 | TERRA_M-M | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 13.4 |
| ddf03a5a-af55-3d72-93c4-2352803ef971 | -3.98191 | -56.22377 | 2026-10-07 00:56:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 059d2af3-91ee-3900-b833-4924f6a2cbda | -3.68239 | -60.53946 | 2026-10-07 00:56:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 908b8712-746c-3695-ab98-8c3318fbfbc4 | -7.88308 | -72.353 | 2026-10-07 00:56:00 | TERRA_M-M | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 28.5 |
| 44c9e4d3-f3c4-38a7-8462-83d50e0d8669 | -3.52293 | -54.65414 | 2026-10-07 00:56:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 166.2 |
| 40bb2499-8a79-35d4-913c-ec37ff413155 | -3.59086 | -61.63047 | 2026-10-07 00:56:00 | TERRA_M-M | ANAMÃ | AMAZONAS | Brasil | 1300086 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 90a28936-1718-3005-adc1-918bc3c77fd7 | -2.9929 | -54.12884 | 2026-10-07 00:56:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 96c43043-bab2-3344-8a7d-9f63aafe165f | -2.59693 | -57.57885 | 2026-10-07 00:56:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 71867027-815b-31cd-91f5-08aba4761ce8 | -2.94061 | -54.13678 | 2026-10-07 00:56:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 9a3ba84f-9425-33a6-af4d-875e179203aa | 0.78769 | -59.19917 | 2026-10-07 00:56:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 0f65573a-760b-3201-93df-d2bed35882ed | -3.27438 | -54.06694 | 2026-10-07 00:56:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 240.2 |
| a27b5377-ddf3-3033-89d6-7a5abd6b08a9 | -4.76301 | -55.64473 | 2026-10-07 00:56:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 21.4 |
| 66954bfc-aa5a-3d4b-a8bc-18b8a2b1cad9 | -3.51745 | -58.76101 | 2026-10-07 00:56:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 1dabf9d8-0977-3b5e-b5d8-e8ab3a2ebd2f | -3.48274 | -59.46844 | 2026-10-07 00:56:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 0d4d54b0-5124-3339-bcd0-9e243ef63896 | 0.44519 | -60.54031 | 2026-10-07 00:56:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 37.0 |
| d46ed836-9e24-34a5-b0b8-c12a7ddbbd61 | -3.29787 | -54.10431 | 2026-10-07 00:56:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 36.7 |
| 3bf94dd5-98f3-3c70-b791-e57a0dfffe68 | -3.38524 | -58.20885 | 2026-10-07 00:56:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 948239b8-0d88-3ac7-a186-274625941757 | -3.48096 | -59.4622 | 2026-10-07 00:56:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 965ecc98-106a-35de-a770-886cd5620b66 | -3.67966 | -55.94175 | 2026-10-07 00:56:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 670eb592-f911-359f-b6d5-c402c374a1de | -3.85223 | -55.96908 | 2026-10-07 00:56:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 45aef826-4f9c-385d-80ee-510523b99907 | -3.28561 | -54.0233 | 2026-10-07 00:56:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 319.8 |
| 55f543b7-2315-3523-b8d4-61b1a33d4637 | -3.36301 | -59.90827 | 2026-10-07 00:56:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 55c172d3-c665-315c-83b0-9fc80cc1e2a4 | -3.39862 | -59.52692 | 2026-10-07 00:56:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| af429021-62e6-3f52-a168-4e92690835c6 | -4.07167 | -54.89282 | 2026-10-07 00:56:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 19bec695-378e-31d2-bd05-6ac4991a0c6f | -1.79743 | -57.12469 | 2026-10-07 00:56:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 18143a5e-61a3-3d35-8aea-71192f480e06 | -4.08784 | -54.89016 | 2026-10-07 00:56:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| cbb0992a-78a8-34c3-ac2f-371e46a5b3dc | -3.34592 | -59.47872 | 2026-10-07 00:56:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c0991073-9c45-3e64-8b24-1b46b38819fb | -3.98589 | -56.25042 | 2026-10-07 00:56:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| b5c38bfd-a260-394a-897e-2ba7d0ca24b5 | -3.29267 | -54.05893 | 2026-10-07 00:56:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 405.4 |
| 40e11cbb-3c83-3aec-819c-b104eed6f4d9 | -3.27349 | -54.07389 | 2026-10-07 00:56:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 191.2 |
| 39d0c979-5c4b-3fa8-9daa-4d6d00146bde | -3.00947 | -54.13094 | 2026-10-07 00:56:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 127.5 |
| 5dbad428-8dcb-3410-9f5e-0a0925af0dc2 | -1.29772 | -54.58533 | 2026-10-07 00:56:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 075fcc4f-fde7-34d5-ab09-cdeedb3a52d4 | -3.58371 | -54.33072 | 2026-10-07 00:56:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 4e76a529-8082-370a-9158-e394abaa353d | -2.70247 | -59.79869 | 2026-10-07 00:56:00 | TERRA_M-M | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| e12f76db-8f76-3c12-b2b4-44f56ba5689e | -3.89924 | -59.32977 | 2026-10-07 00:56:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| e6dc9527-cda1-3fe5-b0bb-96d495c81c4e | -3.299 | -54.09895 | 2026-10-07 00:56:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 9b19086b-123c-3ab7-a5d5-945279fb1000 | -3.35952 | -59.90086 | 2026-10-07 00:56:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| aca05c0e-b0f6-35b9-b000-6d9a36e36624 | -3.48834 | -59.58982 | 2026-10-07 00:56:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 58.0 |
| b563ff2d-95ff-3bc5-9676-b13207f279ea | -3.39639 | -59.51188 | 2026-10-07 00:56:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 20.3 |
| d67e8b74-df95-3a03-bb3a-6e8007881a14 | -3.50624 | -54.65633 | 2026-10-07 00:56:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 137.6 |
| ce0d9779-7d47-3590-8943-b9c00ca07bf3 | -4.15964 | -55.15374 | 2026-10-07 00:56:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| c0272dc9-8c77-3efc-a2a7-07e50ee563da | 2.01336 | -61.08428 | 2026-10-07 00:58:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 29.8 |
| c101e55b-aa50-3a62-b8fd-3ad1dd9d0669 | 1.98444 | -60.61632 | 2026-10-07 00:58:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 5c365f3b-3b27-3dce-b489-985c7ec7ce72 | 2.01148 | -61.09826 | 2026-10-07 00:58:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 8bf131e6-77a7-3fde-a5e9-59d04bd46ae8 | 4.14763 | -61.25468 | 2026-10-07 00:58:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 6ee50053-d0d0-3500-bd59-ee00d81d8c8d | 3.14717 | -60.59626 | 2026-10-07 00:58:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 20.7 |
| 356be6e3-7862-3bbc-b73d-85b8c6ae544c | 3.14379 | -60.60238 | 2026-10-07 00:58:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 14.2 |
| cace0789-2a77-37f8-99bc-5e8c866e0f8b | -3.4763 | -50.0673 | 2026-10-07 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| b2f0a31f-d552-36c3-a1f5-76396083ecc4 | -10.9953 | -45.4068 | 2026-10-07 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.2 |
| e9bd8829-148d-3dde-a286-658ef9b5e893 | -13.5117 | -44.368 | 2026-10-07 01:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 331d1c31-0dee-3a67-8077-91ac44065498 | -5.7376 | -45.1533 | 2026-10-07 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 83880ba1-36c3-3a05-a1f4-c9c2edc49469 | -12.1742 | -44.7284 | 2026-10-07 01:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 220.2 |
| 88100e1d-564f-33e1-8554-c927bd5f925f | -11.1234 | -45.7322 | 2026-10-07 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 255.2 |
| 046347a6-44b7-313a-b1a6-274914b607e4 | -3.8997 | -59.339 | 2026-10-07 01:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 61ad71a4-4520-3cdc-8261-6177255b03c9 | -11.0137 | -45.4501 | 2026-10-07 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 182.9 |
| 5f92bd87-cd39-3a70-9815-2ddf577472f1 | -11.7143 | -43.652 | 2026-10-07 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 3a71765e-e59b-32b6-9d7b-87bc3432a5ca | -3.531 | -54.6757 | 2026-10-07 01:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 08b4231b-b7c0-3794-80e7-b58126fc8ded | -14.2531 | -41.6256 | 2026-10-07 01:00:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 108.6 |
| ec7379be-2a66-35dd-a339-2df3191564df | -1.2922 | -54.5585 | 2026-10-07 01:00:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| a9a1c96b-339c-385a-8629-e90856115c26 | -3.0184 | -54.1282 | 2026-10-07 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| 632bfd41-c3a9-30d8-af34-6c715567422e | -3.4762 | -50.0883 | 2026-10-07 01:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 216.7 |
| 2b243f81-615e-356c-8703-431be5208be4 | -3.1114 | -53.7839 | 2026-10-07 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 122.3 |
| adf98695-256b-369c-a817-70b5a0c89ba6 | -7.8234 | -72.7142 | 2026-10-07 01:00:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 46622ad1-c6a3-3f40-88d3-f20f7e250893 | -11.7528 | -43.646 | 2026-10-07 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 1c69039d-d059-3c23-88ea-3b277f4b1f48 | -2.7612 | -54.1142 | 2026-10-07 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 2c2232ea-891f-36ed-a79e-8e37aa9f06e9 | -3.5126 | -54.6762 | 2026-10-07 01:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 50c45bcd-3fb5-3f2f-b2e2-2760d616be79 | -5.9838 | -40.9123 | 2026-10-07 01:00:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 61.9 |
| e20d618a-e84f-378d-a1b5-4004cf5562a3 | -3.8382 | -55.9972 | 2026-10-07 01:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 594478c0-a26e-3989-a90a-c69363966d8c | -9.4621 | -67.0817 | 2026-10-07 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 4ecd7727-11c3-37fa-bae3-b72f2f620d14 | -2.9448 | -54.1501 | 2026-10-07 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 8a09bbaf-552d-3957-bf19-807442bd2d2f | -6.2759 | -43.6442 | 2026-10-07 01:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 940f3d38-c49c-3155-b799-662be200b88c | -3.5127 | -54.6362 | 2026-10-07 01:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| c90439ca-46ce-395d-94ed-bd5dd1ce5686 | -5.7189 | -45.1547 | 2026-10-07 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 715c9f1d-982c-3076-8973-42049e015aa6 | -3.531 | -54.6557 | 2026-10-07 01:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 148.2 |
| 780db5d5-ecb1-3dc2-8fab-0edbc96272d9 | -11.734 | -43.6254 | 2026-10-07 01:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 2af3cada-17a6-328e-bab7-dc1d6729ab8b | -10.9949 | -45.4298 | 2026-10-07 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 183.9 |
| 5a0d0e37-6cf1-3efd-a1c2-3adb7cc6c25e | -12.1746 | -44.7051 | 2026-10-07 01:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 214.1 |
| bfbfd642-9fd0-3b92-abd2-0f083035d425 | -2.7796 | -54.0937 | 2026-10-07 01:00:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 198.0 |
| 24dcb3ca-604f-30af-bfa7-0230198000c3 | -3.1101 | -54.1661 | 2026-10-07 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 0530fae1-f77b-34fb-b300-20a337700853 | -3.0374 | -53.9268 | 2026-10-07 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.3 |
| ce227d6f-ff02-30a3-9c03-421c00884e52 | -4.7589 | -55.6516 | 2026-10-07 01:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| e5d53eb1-434b-384e-8561-9b4ae9dec974 | -5.7374 | -45.176 | 2026-10-07 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 439f7426-f1ca-3f83-b5ac-296079e0e03c | -11.0646 | -45.8312 | 2026-10-07 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| cd44dcd3-fdbe-3a39-a637-e45b406cb21f | -3.1972 | -50.5592 | 2026-10-07 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 70440b74-e8eb-385f-9894-1a98c6ab7cf2 | -3.0558 | -53.9263 | 2026-10-07 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 28710eed-23a2-35a2-8884-c292c47c607e | -1.801 | -57.1161 | 2026-10-07 01:00:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 3586bf04-58f2-3f2c-8791-de927fff3302 | -3.6206 | -55.2708 | 2026-10-07 01:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| eb9c53af-6d7e-3239-831a-a607ebf8bc70 | -11.014 | -45.4272 | 2026-10-07 01:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.7 |
| 1672f7f0-0fb7-3f1f-b779-52b7cf268e2f | -2.9447 | -54.1702 | 2026-10-07 01:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 08aa22a1-284f-3a45-bbea-d3767f605f67 | -3.1115 | -53.7637 | 2026-10-07 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |


[Clique aqui para ver as próximas entradas](README14.md)
