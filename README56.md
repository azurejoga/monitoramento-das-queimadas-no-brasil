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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3244b65c-714d-34f3-897c-00a38210c697 | -8.10917 | -43.90779 | 2024-10-15 04:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 460e1d00-840c-3b19-a43f-c3cbbb792902 | -9.72422 | -43.8597 | 2024-10-15 04:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a942edff-93f2-3894-be6e-ec7133810d45 | -9.71876 | -43.85908 | 2024-10-15 04:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 652277d0-e9d9-370e-9293-0302261afac7 | -9.7183 | -43.86255 | 2024-10-15 04:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6d2e3b85-ee61-3659-86ba-77f3a8fe66cb | -9.58058 | -43.50167 | 2024-10-15 04:49:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b755005b-5dcd-3730-a61a-5fe64a042ecd | -9.58009 | -43.50536 | 2024-10-15 04:49:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 059af19c-b398-3ef1-85a1-acc56cf30632 | -9.44665 | -44.17864 | 2024-10-15 04:49:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| f0dff5f5-628a-37d3-bc11-d364c0b701db | -9.44622 | -44.18195 | 2024-10-15 04:49:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 123559c9-398c-37c9-9fdd-c880e33a6818 | -9.44578 | -44.18526 | 2024-10-15 04:49:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 154aa35c-798b-371d-bca9-6c3a936e695e | -9.44137 | -44.17775 | 2024-10-15 04:49:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 725b0f0a-f781-31b9-b7b8-ac07a0ae9923 | -9.43693 | -44.17039 | 2024-10-15 04:49:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6ce13b6c-485f-32af-ac42-4ee13b1b9bce | -9.4365 | -44.17369 | 2024-10-15 04:49:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f031b6a5-865a-3a30-8344-3a9d086d7ce7 | -10.51232 | -44.19606 | 2024-10-15 04:49:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03c3d238-f4c2-3b37-9cfe-b512c6d209fc | -10.25922 | -43.97511 | 2024-10-15 04:49:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f92b5f0e-1e90-33a4-b9ef-4ca26c162074 | -10.09145 | -44.23241 | 2024-10-15 04:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a7ecd803-5152-31be-a15d-77e2e72e376c | -10.09101 | -44.23573 | 2024-10-15 04:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0ca21308-fe1a-3713-892a-1fc4d0b73c43 | -10.08913 | -44.20847 | 2024-10-15 04:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a2c77e39-a719-3cfc-98f1-998c198f2ca4 | -10.0887 | -44.2118 | 2024-10-15 04:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1bda0f75-e18d-3f21-993b-f66f32e58fa1 | -10.08827 | -44.21511 | 2024-10-15 04:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1760256a-9d01-3175-a78b-22a3e10fd704 | -10.08697 | -44.22506 | 2024-10-15 04:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d1ca96c4-496b-3503-8785-5d408417bbff | -10.08654 | -44.22839 | 2024-10-15 04:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb5dceb1-6d55-3601-8489-8726eacac829 | -10.08466 | -44.201 | 2024-10-15 04:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1130c2e5-a105-30a0-aa55-fbac2c03d81b | -10.08422 | -44.20441 | 2024-10-15 04:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49545e18-cfee-3ded-a35e-84fd0a0e8b4f | -10.08379 | -44.20776 | 2024-10-15 04:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44dce8fc-674a-352c-8cc7-0eac0bc4373b | -10.08119 | -44.22769 | 2024-10-15 04:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc66c007-1e8c-3cd8-88a0-bca59baed166 | -10.08076 | -44.23101 | 2024-10-15 04:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ab24263d-416a-3a07-8de3-674f04ef0bf1 | -10.08033 | -44.23433 | 2024-10-15 04:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb1a47e4-89df-3dae-ae68-b906325de6bd | -10.0802 | -44.19341 | 2024-10-15 04:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78f36010-6cd8-3cc0-81b7-c6babb9ec135 | -10.07976 | -44.19686 | 2024-10-15 04:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 947dfb09-b6e2-3ef1-8844-4051f6bcc895 | -10.07931 | -44.20028 | 2024-10-15 04:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5e21dd0-6f45-31d7-9ca9-b6d8505a8497 | -10.07485 | -44.19267 | 2024-10-15 04:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 323b02d8-3cb9-37ba-821d-c859169b8f5e | -10.06296 | -44.2427 | 2024-10-15 04:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c23201ca-f1e3-343d-a0eb-af85a5b06386 | -10.05547 | -44.25876 | 2024-10-15 04:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 94631f83-8288-3810-947b-522278932ceb | -10.05505 | -44.26204 | 2024-10-15 04:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac7b5766-f48f-3a07-90f8-06a29a086fff | -10.04809 | -44.18908 | 2024-10-15 04:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f35655df-7175-3c5e-bf1a-b0f24857c075 | -10.04274 | -44.18835 | 2024-10-15 04:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 6256f3d0-9f70-392d-bd50-97338db47050 | -10.0423 | -44.19179 | 2024-10-15 04:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4a6281f0-d9f8-387e-bbda-ee1c0eb2cd60 | -10.04187 | -44.19523 | 2024-10-15 04:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 475aeb30-27a0-3171-b904-c9e8df97db7b | -10.04143 | -44.19867 | 2024-10-15 04:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 000322c8-91e5-3d43-88e1-dcaf0f393906 | -10.04099 | -44.20212 | 2024-10-15 04:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a673cd4-0f3f-33fb-9ae3-d3fc2311a56c | -10.04015 | -44.20874 | 2024-10-15 04:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f15eca4f-dfd8-3218-b455-bd2cb8bbc03a | -10.03563 | -44.20153 | 2024-10-15 04:49:00 | NOAA-20 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 979c422f-607e-3eee-8d4e-86dfb3a9e8cc | -11.13199 | -44.18302 | 2024-10-15 04:49:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f9d04892-7a5d-35b2-afb5-5ae34ec56f10 | -11.11738 | -44.47277 | 2024-10-15 04:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c54a12ff-9b82-31dd-8a53-8a64da8eb626 | -11.11695 | -44.47612 | 2024-10-15 04:49:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9acffb97-323c-3b9e-98b6-16def35f81be | -6.40151 | -44.74245 | 2024-10-15 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2a62be84-ae2c-35fa-9cf1-02dcd2128287 | -6.39924 | -44.74063 | 2024-10-15 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1df0148a-c0e5-31bf-81a2-4be59ed6aa5b | -6.39847 | -44.74602 | 2024-10-15 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98c3369a-d1ed-3b1f-bf98-c7d937787c15 | -6.31742 | -44.27721 | 2024-10-15 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a8722d12-3667-3d82-86d2-a2bd94124502 | -6.26347 | -44.96848 | 2024-10-15 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ddc8df18-0934-37b3-9c77-6b15b31f51d6 | -6.26297 | -44.97068 | 2024-10-15 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 2e5df4ca-d2d1-3ba7-8e97-8ac7cfdf311c | -6.26271 | -44.97372 | 2024-10-15 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 65da1c81-6acd-3be1-bfa2-adc0df2e13b0 | -5.85608 | -44.87777 | 2024-10-15 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6cb4c729-0acd-302a-8635-a85da624a82b | -5.85588 | -44.88062 | 2024-10-15 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d6bc7678-c2cb-30e1-b205-e1e5149fd040 | -5.85127 | -44.87711 | 2024-10-15 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 05cfb0fc-3a62-32ad-a0d5-c6599b5c2e34 | -5.85107 | -44.87996 | 2024-10-15 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec24d858-3e10-3dfe-a4ed-082595d34882 | -5.83699 | -44.70562 | 2024-10-15 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 26428f19-d883-3bc7-8008-59d9bddf4122 | -5.83623 | -44.71086 | 2024-10-15 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 70650c38-33f5-37a0-9923-ec7bf0d96b81 | -5.83548 | -44.71609 | 2024-10-15 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6267292c-2a17-33c5-ad1e-ccd864340100 | -7.95119 | -44.52934 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f21cfe52-a69f-38bd-ba64-37f544f26477 | -7.95076 | -44.53258 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32566f84-d052-3fae-8538-8d900fb4f892 | -7.95033 | -44.5358 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41619cd9-56d4-3128-a1dc-e95cf895dd70 | -7.94872 | -44.52154 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 743fc466-ae21-3761-a255-308e614474d2 | -7.94829 | -44.52465 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 320826da-3e98-3e93-859f-716458e857f3 | -7.94785 | -44.52777 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cad4026d-b9d9-3461-acf3-b1e388874325 | -7.9474 | -44.53091 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e7c52c3d-163c-399f-ab77-53e4a1257dbb | -7.94697 | -44.5222 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bb45870f-6f38-34c3-a1cb-228113be0896 | -7.94696 | -44.53406 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0014d17-b914-3695-8f82-12cc2e49458c | -7.94656 | -44.52531 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 082efc62-a7ec-32fd-afaa-c9df97ac90a8 | -7.94652 | -44.5372 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be8cb5a5-4f1c-382d-b93e-a1b6bc46e3bf | -7.94614 | -44.52842 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 47686d02-f479-3dc1-a5b3-053f65a8f64c | -7.94573 | -44.53154 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40cd4907-94a2-33b0-9290-a170c5aff7fe | -7.93774 | -44.52605 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 13d28580-9e23-3444-b2a9-05283abcfcbf | -7.93732 | -44.52908 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1f0116b3-6a77-3679-9946-5388e085c241 | -7.93646 | -44.5352 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 00bcd983-0c34-303f-b345-b39bc04315bf | -7.93224 | -44.52839 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d839fb97-b05a-333b-9f1c-36360a2bc338 | -7.9318 | -44.53156 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a0782595-8143-3e3a-8810-c60131dded4b | -7.82375 | -43.99897 | 2024-10-15 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d37e820e-0852-38c6-8041-5983e1865c5e | -7.77142 | -44.54176 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b7952d2-040c-365a-aadc-5c704b58dbd8 | -7.76672 | -44.53846 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d127344-0829-3a29-a863-4a5c4e06f5b2 | -7.76165 | -44.53785 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8f10ef7-20c4-3b55-8e57-b3ec41284de6 | -7.75657 | -44.53729 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90d089aa-a3ea-3a9c-97de-752cd301c11f | -7.75618 | -44.54017 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2a7c6cca-576f-3405-8135-bbe2fee2816b | -7.75579 | -44.54306 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b413cd5-6461-3230-97fe-30b4c0b79247 | -7.75031 | -44.54543 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0436a27b-f3ed-31dc-8b24-aa85b7f9cf1c | -7.74993 | -44.54828 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1abc36e0-9ba1-3c96-a503-5c9401d8bf66 | -7.74954 | -44.55112 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 857fc4df-b20b-3788-ab4f-f600ad7c8b44 | -7.65169 | -44.67176 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62486228-08e2-3590-b9e0-23c3263233c0 | -7.64668 | -44.67107 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 32f29c0d-f6be-303d-abf6-e8785304471e | -7.5964 | -44.66377 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13b958fc-4b1d-3617-9c69-38b633361165 | -7.59597 | -44.66678 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad17f6b2-b55a-3c35-82e3-64b171516eaa | -7.58891 | -44.64449 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2e248267-5c94-339a-aeeb-f17421f4eb69 | -7.5885 | -44.64738 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62e695bc-fdb3-313f-be62-bf60d48daaa8 | -7.5881 | -44.65028 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52e7cf7d-de5c-34e1-9892-9c00ae43b32d | -7.57436 | -44.96017 | 2024-10-15 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 54d8af6a-932a-3cc2-b85a-cb04ba17ef9a | -7.46338 | -44.09661 | 2024-10-15 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e27a2fa9-5f82-370f-86a1-46c0dbedc9a7 | -7.39938 | -45.19149 | 2024-10-15 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f6697a72-55f3-3ceb-adce-c560e32dc1f6 | -7.39383 | -45.19606 | 2024-10-15 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d078d6b5-5ad5-3770-8c3b-f03f26ae3145 | -6.94767 | -45.20759 | 2024-10-15 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbd6aede-b050-3f63-a3cd-6f3d97b3c3ae | -6.9469 | -45.21298 | 2024-10-15 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |


[Clique aqui para ver as próximas entradas](README57.md)
