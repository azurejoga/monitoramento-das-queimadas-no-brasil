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

## Dados Diários - Página 242

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 173bdd6b-2337-3e63-ac56-0c2db77e44a8 | -9.7313 | -65.0757 | 2026-10-07 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 3f6f5252-cc0f-3d55-94bf-19fea669b97e | 1.8038 | -55.5261 | 2026-10-07 17:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 22bd2ef3-ff5c-313b-8190-c83ce4b762da | -11.6382 | -43.6166 | 2026-10-07 17:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 274.2 |
| 12a947c6-beaf-32c1-a275-1c869012bef8 | -7.8789 | -72.3674 | 2026-10-07 17:20:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 3b2bd9fa-92e6-30af-bf0d-e7f90c2a8274 | -9.7126 | -65.0951 | 2026-10-07 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.8 |
| aa15ce79-58d5-38a3-b6aa-eeba8139bf8f | -2.8899 | -54.0912 | 2026-10-07 17:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 32637fd8-ae58-328f-b609-c9050679254e | 1.6385 | -55.785 | 2026-10-07 17:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 7a5f4636-cfb9-3a99-8580-887b43f50661 | 1.8768 | -55.7227 | 2026-10-07 17:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 8b03956e-672c-3f0d-aada-98df8a434a78 | 1.712 | -55.6459 | 2026-10-07 17:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 217.3 |
| 5ab6e2d1-8f3f-3215-8b6e-f83e6b180c78 | -0.3768 | -52.0153 | 2026-10-07 17:20:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 08ad94ed-eed5-3138-9003-39725df02b7b | 1.9864 | -55.8789 | 2026-10-07 17:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| fa48c7c2-f076-399b-8acb-40a8b3c00edb | -11.3745 | -46.6948 | 2026-10-07 17:20:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| e8f74d7f-4d96-3f08-a259-20847aed90f6 | 1.7671 | -55.5661 | 2026-10-07 17:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| f4201752-29e3-3520-9441-87f490de6359 | -8.028 | -71.0695 | 2026-10-07 17:20:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 157e2b98-73cf-3b5e-aa37-00199740ac84 | -11.7362 | -43.5068 | 2026-10-07 17:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.8 |
| 81b960af-75ad-3043-b243-77a4160ddce9 | -11.1051 | -45.689 | 2026-10-07 17:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 258.8 |
| 2aff457f-d0a3-365c-87c9-fbaa9932495d | 1.8038 | -55.5261 | 2026-10-07 17:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| c59f4498-5276-347e-be23-97dc4b420c45 | -3.951 | -41.5426 | 2026-10-07 17:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 147.1 |
| 9b687c1c-a83d-3720-bc36-2781693862b8 | 1.8767 | -55.7424 | 2026-10-07 17:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| ee3d349b-c5f6-3520-8012-e6c156f3f44b | -9.4621 | -67.0817 | 2026-10-07 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| aedf36ae-7967-326d-bcf9-19d62ba21e39 | -9.806 | -65.0167 | 2026-10-07 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.4 |
| d5595bd4-f409-3a99-9e9e-859721419767 | -9.8246 | -65.016 | 2026-10-07 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 65.0 |
| f681cccf-b562-322c-b74e-986747fda10d | 2.1267 | -50.8371 | 2026-10-07 17:30:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 79.6 |
| c403a80d-7ebb-3334-aa17-c6f6991bb1b2 | -11.3745 | -46.6948 | 2026-10-07 17:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 98a83db9-a216-30ac-981f-f57d8e9c1b8b | -11.8508 | -43.5361 | 2026-10-07 17:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 156.5 |
| cf15597d-b426-3eaa-8c27-afc34a541f03 | 1.8951 | -55.7224 | 2026-10-07 17:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 51151319-22ae-3329-912e-2f902775377d | -10.9762 | -45.4094 | 2026-10-07 17:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 41c5c3ba-3780-3b86-8f2a-e17b749acd00 | -12.1742 | -44.7284 | 2026-10-07 17:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 400274a8-1ae6-3555-8bbc-20a6ac310ad3 | -9.0988 | -65.3596 | 2026-10-07 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| b09b5763-639f-3d2b-b7dc-6cd6594aa729 | -9.4509 | -45.8271 | 2026-10-07 17:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 388.3 |
| 48d526fa-3a02-3dda-a4dc-88e1dab14297 | 1.8951 | -55.7027 | 2026-10-07 17:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 4748c23b-a4c7-36e2-b3ab-c118d3ca3f28 | 1.6385 | -55.785 | 2026-10-07 17:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| e27f4d3d-d966-3feb-9856-6fcda3bc665d | -11.619 | -43.6196 | 2026-10-07 17:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 0fcfef29-fcac-3dc9-ba12-7724565553a6 | -8.4707 | -70.8444 | 2026-10-07 17:30:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 4127b59e-89de-3951-a359-9d2f6a144264 | -9.6572 | -65.022 | 2026-10-07 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 0c3e96ce-c526-3b61-a482-66e87c8d5992 | -11.0867 | -45.6459 | 2026-10-07 17:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 151.4 |
| c8b2849b-2a85-3d31-b261-52aef52352b5 | -12.2136 | -44.6758 | 2026-10-07 17:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 118.7 |
| 2d27b4e9-5c3b-328f-bc09-02b3379bda30 | -9.6757 | -65.0401 | 2026-10-07 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 63ec20ff-3535-34ae-b973-d5e6620c9cab | -9.7499 | -65.075 | 2026-10-07 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 41efcf6b-b405-3bba-9e71-537f3617ccd9 | -11.6186 | -43.6433 | 2026-10-07 17:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| e25ab290-7d0a-309d-9166-12a6b90d7da6 | -11.6181 | -43.6669 | 2026-10-07 17:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 74819ed7-b368-3ca0-bf72-6ce1843b9f96 | -9.8245 | -65.0348 | 2026-10-07 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 68.9 |
| f1a1a5ed-d07f-3ee1-9cba-9c175b9e331f | -9.5468 | -64.8196 | 2026-10-07 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 37727ec9-5f06-3365-8104-5776ada40928 | 1.9134 | -55.7024 | 2026-10-07 17:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 8d2c9d40-1686-3feb-a159-77f25de5fa3d | -9.4435 | -67.1008 | 2026-10-07 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 1c5f0325-956b-35ac-8fd1-fdd597ed99a3 | -11.0676 | -45.6485 | 2026-10-07 17:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 131.0 |
| f5386c88-f78f-3fe4-8dc1-b4d64344e310 | -9.8244 | -65.0535 | 2026-10-07 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 9b145d9b-b411-3dfd-b24c-df4f6780c3c0 | -12.2132 | -44.6991 | 2026-10-07 17:30:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 05d965d6-c09e-3734-b14d-7b5c3c7622f3 | -7.8443 | -70.8705 | 2026-10-07 17:30:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 9cdd7402-498d-358d-b796-3332547bfe4d | 0.7266 | -51.3749 | 2026-10-07 17:30:00 | GOES-19 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 53a08eaf-8869-30f8-a391-eff80821b740 | -9.4513 | -45.8044 | 2026-10-07 17:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 162.0 |
| ff02c7c8-b2e5-364a-a612-efe1055ae26d | -9.4682 | -65.6839 | 2026-10-07 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| ca584269-3881-3537-b041-7e31c7cadeac | -9.5425 | -65.6815 | 2026-10-07 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 82153230-d263-3d78-9f2a-3491f50e552a | 1.7487 | -55.6059 | 2026-10-07 17:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 314e9f95-fd8b-311e-9d8b-a2f7252bfe13 | -7.8789 | -72.3492 | 2026-10-07 17:30:00 | GOES-19 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 141.8 |
| 0e9f432c-d82a-372c-a5e6-0fe91d4655a8 | -9.7312 | -65.0944 | 2026-10-07 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 5f83c9be-8d2c-3051-b0e1-a06d5918c51a | -9.7126 | -65.0951 | 2026-10-07 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 199f9dc8-8e58-324f-bf50-8cb27c03ec33 | -3.6612 | -54.2715 | 2026-10-07 17:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| 5dda5971-563a-3ca6-996f-e4d2a98716b1 | 1.8768 | -55.7227 | 2026-10-07 17:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 0feab4f9-8384-3738-b003-269599735b32 | -2.8899 | -54.0912 | 2026-10-07 17:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 344d2995-e6e4-3a5f-a027-452de1dc8ed2 | 1.7671 | -55.5859 | 2026-10-07 17:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| d1f7364f-e94d-39a2-a29e-7e2ff038d2e9 | -8.0852 | -70.0619 | 2026-10-07 17:30:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 166.0 |
| 193825c7-e94b-350c-820c-e994a8c59cb6 | -9.8685 | -45.7556 | 2026-10-07 17:30:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 243.6 |
| 45113dc0-05ab-3e40-b650-1be5c963c65a | -9.5176 | -67.1173 | 2026-10-07 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 88.9 |
| b315098f-7a8a-3857-a2c6-0679edc48b17 | -2.8714 | -54.1318 | 2026-10-07 17:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 106.6 |
| e6ff6b54-3f69-3b2f-b47e-ba529a66cf5e | -5.9649 | -40.914 | 2026-10-07 17:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 322.0 |
| 7f0289e8-976f-3ccf-a067-c13e0e641a46 | 1.9681 | -55.8792 | 2026-10-07 17:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 924e04ab-093c-395c-9be2-2503d6af973d | -9.8061 | -64.9979 | 2026-10-07 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 5e3c1273-679d-38fa-9979-226f46631eb7 | -11.8503 | -43.5598 | 2026-10-07 17:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 161.1 |
| b2af14a2-6951-3698-9e2c-b7651453dcaf | -9.432 | -45.8293 | 2026-10-07 17:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 8493bd1a-d05e-3255-a671-cf6f558ec793 | -11.8315 | -43.5391 | 2026-10-07 17:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 6641788f-0625-335b-8a0d-f8bcaa0b1845 | -11.1051 | -45.689 | 2026-10-07 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 584e0bbf-a31f-32fb-8208-afdfa4b9c7ad | -11.7738 | -43.5482 | 2026-10-07 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 9c88fbd4-c1d5-385c-a967-e0bf1e096c3f | 1.7671 | -55.5859 | 2026-10-07 17:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| d6855467-f109-3258-88ac-80085f7d4533 | -2.7613 | -54.0941 | 2026-10-07 17:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 675.8 |
| f4f73e10-2c9a-3857-a441-045ddd036aee | -9.4621 | -67.0817 | 2026-10-07 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| d3f09cf0-3c7a-3735-b887-055bc6f832b9 | -9.0987 | -65.3783 | 2026-10-07 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 937360cf-712e-329c-b7c6-ae491718c412 | -9.806 | -65.0167 | 2026-10-07 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 54bea44f-396d-3dde-ada5-1292e7126478 | -9.432 | -45.8293 | 2026-10-07 17:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| b67c29ca-4f08-353f-97b1-6c66d13d983f | -11.7362 | -43.5068 | 2026-10-07 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.2 |
| f73f7951-d0ca-3cb1-b518-7416a5085151 | -0.3952 | -52.0357 | 2026-10-07 17:40:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 54.2 |
| c4f3923d-e170-3852-b45d-dc05537b5233 | -9.8685 | -45.7556 | 2026-10-07 17:40:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 139.2 |
| 59210382-ea84-37ac-8eff-31f4759504d5 | 1.7671 | -55.5661 | 2026-10-07 17:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 23946e9c-6dce-36a9-8f04-12d4e332ea0d | -9.5468 | -64.8196 | 2026-10-07 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.9 |
| caeb769c-6701-33b7-8ad0-b2d45af59ea3 | -2.8713 | -54.1518 | 2026-10-07 17:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 763edfcd-18d4-3722-b336-02c512932e03 | -11.7143 | -43.652 | 2026-10-07 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 238.1 |
| d476f770-2931-37f0-9462-63234b8a34e5 | -11.8503 | -43.5598 | 2026-10-07 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 166.9 |
| f3bac293-411e-32f7-bd32-995ecc893652 | -2.8164 | -54.0929 | 2026-10-07 17:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 112.9 |
| 7cf0eae5-8494-3fb4-8b8d-b62bf76c3fd6 | 1.8951 | -55.7224 | 2026-10-07 17:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 50692676-167b-333a-88f8-a1295d263a0f | 1.7487 | -55.6059 | 2026-10-07 17:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 37546734-054c-3e8a-b296-f3cc5662f6ef | -9.5313 | -46.8513 | 2026-10-07 17:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 121.2 |
| d6d8b18f-6158-328f-a6e1-18f05a59d74c | -0.4319 | -52.0561 | 2026-10-07 17:40:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 72c9bb75-d35f-3753-b9c1-696dc06f5977 | -11.1047 | -45.7119 | 2026-10-07 17:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 5ba055fd-b4a4-3f99-9f42-bab53b5f2394 | -5.9649 | -40.914 | 2026-10-07 17:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 222.6 |
| e940be6d-c340-3d72-8bff-428740bda734 | -2.8714 | -54.1318 | 2026-10-07 17:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 116.2 |
| 8ca92289-a1cc-3a0c-ad02-954f93b717ee | -9.6572 | -65.022 | 2026-10-07 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 56.0 |
| b1149e79-9dd9-3b35-99ed-141053fd7358 | -5.9838 | -40.9123 | 2026-10-07 17:40:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 154.7 |
| 79ba92e5-9c6b-3f6e-8726-0a359f8f2202 | -11.2337 | -44.8446 | 2026-10-07 17:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 326aac50-7bb8-3310-956c-3cba181755cf | -2.8899 | -54.0912 | 2026-10-07 17:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 8dbb7513-7db0-346f-9bde-702e24d5b386 | -11.6387 | -43.5929 | 2026-10-07 17:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 120.8 |


[Clique aqui para ver as próximas entradas](README243.md)
