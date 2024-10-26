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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40ce0124-e484-3aaf-8238-dd94e04681f8 | -3.61238 | -54.03902 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fcaa8f05-5a2b-3dcc-8d6a-7b137b988646 | -3.5777 | -54.63209 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b30717f7-651b-380d-8c83-7fc45ff868b2 | -3.57698 | -54.6364 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b9ac7711-ae75-3fa9-89e9-8cd89649a19d | -3.57472 | -54.63125 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 19632aca-0175-3b93-a93d-23317c538dca | -3.57397 | -54.63555 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ba5c3a9-9f9f-353a-8c2b-ef3b9c1f64af | -3.55419 | -53.99114 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d41a939f-81b9-3429-8b1a-ff6b1183ab92 | -3.55353 | -53.99504 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73e7b1f5-f058-3918-93a6-b11ba37bd4a0 | -3.51347 | -54.02415 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc8e2770-73d4-3548-b5ee-bc90b0fea917 | -3.50776 | -54.02321 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c5f7743f-95bb-30fe-b463-4fbd10442f58 | -3.49635 | -54.44222 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 40eea0a7-80c0-398f-a0c3-f00469223c99 | -3.49054 | -54.44096 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cdac42dc-89b3-3d42-aaa7-18c627cc6a5b | -3.48697 | -54.46222 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 64596efa-2aee-3757-9486-90a62ce69369 | -3.4847 | -54.43985 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e05c357f-0d23-3256-97d6-c5ff17a043ac | -3.48109 | -54.46129 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20af2ac1-7ac4-39c1-a857-8dd59234c995 | -3.44167 | -54.13161 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3109930a-9937-34a0-825e-517a5249c2f9 | -3.4312 | -54.57704 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 404cd49e-182c-312e-b0b3-0f3a273ab109 | -3.42532 | -54.57578 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9bbf3b28-60ad-38a6-80d4-38c08cb17db1 | -3.42462 | -54.57992 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| daaa3c9f-1be6-3fb6-a833-2e9840645448 | -3.41872 | -54.5788 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 86336e69-b88a-3dfb-9a54-d8fbecfc8281 | -3.41799 | -54.58307 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bccc816d-a5dc-39ea-9c3e-336c5ee46171 | -3.41552 | -53.87002 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 337deb71-3297-3a52-b17d-28ea3cc70343 | -3.41281 | -53.87068 | 2024-10-26 04:17:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e54cd2c7-91a4-3a05-ba3e-4481bd08e060 | -2.68152 | -54.02623 | 2024-10-26 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14f74486-fb6e-3946-a705-b0b16d76e510 | -2.68084 | -54.03032 | 2024-10-26 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ab428c2-3a03-3150-8a51-a3cd26379a4d | -2.47666 | -54.04498 | 2024-10-26 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ca6d4f5d-64c4-337c-a845-3102831925f3 | -2.47087 | -54.0439 | 2024-10-26 04:17:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 206b1880-378b-3826-91b7-01a630c201ee | -4.07322 | -54.43339 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| da7ffad3-619f-381f-a66c-4d67b20d81c6 | -4.07251 | -54.43743 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 77e2a586-8547-32de-acd8-54052fd78078 | -4.0368 | -54.54964 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 962309c3-193e-37ac-8821-a577b471f8de | -4.03612 | -54.5537 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5dfdb4e-0db0-3177-bcac-debfb7814e0c | -4.03506 | -54.54906 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40fc193f-f455-3b03-976c-98114dd4607e | -4.03435 | -54.55314 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 383aa576-8640-3c5a-ac12-e729315f64ac | -4.03159 | -54.61684 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 959ca805-568d-3f97-a74d-420835aad401 | -4.03095 | -54.54863 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2eeafb80-6af8-3ee0-a98b-841248ebbe05 | -4.03092 | -54.62086 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b520d6a6-d491-3629-a9ec-3c2587d4200b | -4.02938 | -54.61611 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e044e72-df61-3988-a825-8a3af7c64818 | -4.02868 | -54.62013 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b1e9ad57-fd9b-3391-a06d-54a0711bcceb | -3.93121 | -54.54104 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d54c9893-b806-3b9a-984b-ec746641afba | -3.93014 | -54.53931 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 43266502-a7fa-31f2-8016-895edfbfa1d0 | -3.92539 | -54.53983 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4b37378-d7c0-3afc-b6f6-ccd00a055d5c | -3.88493 | -54.14378 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0fb45051-e88a-3b4b-ad42-4d8daaf1f37a | -3.73898 | -54.48494 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28cf0b6b-3039-3672-a766-228975290b59 | -3.73831 | -54.48895 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2894e327-30f4-37dd-afd0-42e1b713d1f5 | -3.73798 | -54.48338 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c194ba7f-d44d-3603-b288-84b37e33b9ea | -3.73731 | -54.48726 | 2024-10-26 04:17:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33dc4e58-49ca-3433-b9d8-6f09d8bb1eab | -1.38438 | -55.84268 | 2024-10-26 04:17:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 77071a64-dcab-3ab2-b051-6eb98964da68 | -1.38301 | -55.83789 | 2024-10-26 04:17:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ccd8983c-884a-30c9-87e8-acae14a3ff1c | -1.38208 | -55.84347 | 2024-10-26 04:17:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c0314cc9-6a0c-36af-ba81-b7d05ee12582 | -1.37866 | -55.83608 | 2024-10-26 04:17:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2958760d-4c4e-37d9-8918-16c95d32882e | -1.28991 | -55.71772 | 2024-10-26 04:17:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2287474e-0bf7-3be3-9afe-f36098f41985 | -3.63639 | -55.51295 | 2024-10-26 04:17:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f27a6a50-50ca-371b-b8bd-0def057b9c2a | -3.63411 | -55.50826 | 2024-10-26 04:17:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 81c44bcb-b33f-389c-a8e2-8fed898e9115 | -3.63325 | -55.51315 | 2024-10-26 04:17:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0ddef32e-7dbf-3d86-978f-c2369b92e66f | -3.63103 | -55.50665 | 2024-10-26 04:17:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 790eb633-3cf0-3260-bb30-bc1da0421857 | -3.63019 | -55.5116 | 2024-10-26 04:17:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 079a101b-c718-31d2-a630-c237d19bc04f | -3.62936 | -55.51649 | 2024-10-26 04:17:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7d28c573-dfd4-3bf4-8ca3-796865684546 | -3.62392 | -55.51057 | 2024-10-26 04:17:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1c296b28-5290-3535-8317-80646062810b | -3.5591 | -55.45249 | 2024-10-26 04:17:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 635cdbf3-d420-3ecc-a85b-81693bcf571c | -3.55831 | -55.45721 | 2024-10-26 04:17:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f0da5e9-f3b9-3c40-b6ca-b5def134e086 | -3.55652 | -55.45401 | 2024-10-26 04:17:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 79cd3ca7-72e8-3c8f-b012-2be80c4ce716 | -4.04347 | -56.28241 | 2024-10-26 04:17:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8fc6ea13-b14e-3505-b756-3cf0b58b0536 | -4.03696 | -56.28121 | 2024-10-26 04:17:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 37945812-ff21-3d4a-ba79-056fad70eff2 | -3.99865 | -55.73406 | 2024-10-26 04:17:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| af5e0085-b7cb-3ba2-9b28-43af1bc7b662 | -3.91988 | -55.92356 | 2024-10-26 04:17:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b296f61-2c79-3b05-a40b-be2af5a2e93b | -3.91894 | -55.92896 | 2024-10-26 04:17:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7d4f0be4-8145-306a-9f91-24e267959ff2 | -3.70024 | -55.96207 | 2024-10-26 04:17:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 286d37d1-fc2d-3d69-a460-41f89f1cc496 | -3.69881 | -55.96565 | 2024-10-26 04:17:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| abc07838-b56f-346f-b483-0295913f23d6 | -3.69377 | -55.96127 | 2024-10-26 04:17:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2461eb85-f4ec-38be-bfc1-718dd47c9235 | -3.69235 | -55.96472 | 2024-10-26 04:17:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 13cea087-dc9b-3526-9734-d4dcf9b9560c | -9.96474 | -44.15564 | 2024-10-26 04:19:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7692ea41-7244-3104-88e6-7a1275f785a5 | -8.79346 | -44.71776 | 2024-10-26 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 298199a3-7ea2-33bf-87fa-a62c5aefd706 | -8.79236 | -44.72475 | 2024-10-26 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 31526f8e-584d-36f9-a2b9-2d188c1102ba | -8.79013 | -44.71724 | 2024-10-26 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a73b7a36-491a-3cae-aad2-3820ccf1ce6c | -8.78958 | -44.72073 | 2024-10-26 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3049a989-f0a5-3d6a-b81e-e739370214cd | -8.78904 | -44.72422 | 2024-10-26 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4bdbfd3-3bc7-3de9-8766-383233c9a5e1 | -8.78849 | -44.72772 | 2024-10-26 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07ac3290-e25a-3146-811c-084ad828f457 | -8.78794 | -44.73122 | 2024-10-26 04:19:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1ca43470-0940-3c30-963f-76d1c1cd95e5 | -9.00838 | -44.31126 | 2024-10-26 04:19:00 | NPP-375D | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac5e4751-56de-31c0-bbc4-8da1e1854429 | -9.00503 | -44.31074 | 2024-10-26 04:19:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 8e96e571-b524-392c-ad26-86cb3cccb4d4 | -7.76531 | -45.16496 | 2024-10-26 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf77eb6a-0e26-3be3-92f8-0aac8752b7a3 | -7.76476 | -45.16845 | 2024-10-26 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2eca7a88-f382-3f90-ba92-80c6339762c5 | -7.87902 | -45.45487 | 2024-10-26 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05319bec-b4bc-3bfc-bb8d-2ccf20e5afe6 | -6.70013 | -43.95574 | 2024-10-26 04:19:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 51cf065c-e97e-3026-859f-69e779ead2b9 | -11.9996 | -44.3672 | 2024-10-26 04:19:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5b36e3c7-f3b1-3cdd-9c9f-791ca40aa823 | -11.99621 | -44.36666 | 2024-10-26 04:19:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2f2b25cc-3f15-324e-a450-1b50cf630283 | -11.53385 | -45.83698 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18249eba-1c9a-3fe6-89cb-425fd5cafcd8 | -11.53053 | -45.83645 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d02b1bde-2b66-324d-a541-d03155701efa | -11.51836 | -45.82727 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a426d31f-f5ba-33c4-8132-95ac655a89a7 | -11.5178 | -45.83078 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a7c90ae6-2646-3be8-87ed-9b661039bbca | -11.51171 | -45.84782 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 564a235e-d467-3ce5-b2db-95bdcdd88c74 | -11.50397 | -45.83215 | 2024-10-26 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab1e1d5b-56d3-34d5-9f74-a032d6a83480 | -11.21229 | -46.13523 | 2024-10-26 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7a1086c-632b-331a-8030-c916d6c8190b | -10.99706 | -45.26429 | 2024-10-26 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 99680cf8-0e93-38f2-8168-efcc5b3975bb | -7.33607 | -39.30729 | 2024-10-26 04:19:00 | NPP-375D | BARBALHA | CEARÁ | Brasil | 2301901 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b27321df-8209-395a-8826-03bbf7e85020 | -13.66631 | -44.29345 | 2024-10-26 04:19:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 516452e6-a992-3309-9dc5-e2904bd4a454 | -8.52079 | -45.63327 | 2024-10-26 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba5ce0d1-0b71-339c-bca6-c66df8254b16 | -8.52024 | -45.63676 | 2024-10-26 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a0cf7e35-5838-3010-bba7-2c13647e5752 | -8.51746 | -45.65428 | 2024-10-26 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d0d65f9-b576-39c6-bca3-450297ddda85 | -8.51691 | -45.63623 | 2024-10-26 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6c84bd77-f49d-3681-820e-b7173c5c34e7 | -8.51357 | -45.65726 | 2024-10-26 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README48.md)
