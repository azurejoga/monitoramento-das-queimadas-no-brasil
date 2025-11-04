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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf55ab4e-f2bd-3490-a512-79c470f95da1 | -4.47831 | -43.23228 | 2025-11-04 03:40:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93a95947-efd3-3179-a229-9634e302a213 | -4.18757 | -45.78226 | 2025-11-04 03:40:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15d27990-67ea-31bc-a09a-0fe552d539ff | -5.03291 | -43.62218 | 2025-11-04 03:40:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dff92ec2-3b96-3ca6-a4fa-96205e08ee4d | -4.62516 | -46.40768 | 2025-11-04 03:40:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3a2d11d2-f6ea-3428-91c8-3c0b7d87548d | -3.49963 | -45.63572 | 2025-11-04 03:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 410c0f4e-d206-3f37-9c88-5bc963c85ec9 | -5.52408 | -41.12183 | 2025-11-04 03:40:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7a68f7b6-df09-345e-9aa5-61021dc88a37 | -2.87697 | -45.29483 | 2025-11-04 03:40:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3331c3f5-5b08-39b7-ae86-6799bf687eb7 | -2.37772 | -47.71703 | 2025-11-04 03:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1fdc1d11-d2ee-322a-b3c8-d0061ac3b976 | -4.59453 | -45.58444 | 2025-11-04 03:40:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c73880ce-3401-3c15-939c-b59bbe4f53af | -4.02685 | -45.46283 | 2025-11-04 03:40:00 | NOAA-21 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| dcf4f0d2-14fc-3452-b560-382dd2de6b66 | -2.37816 | -47.72772 | 2025-11-04 03:40:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b648512-9734-3e89-8c70-de8d94c0532d | -4.60817 | -45.75586 | 2025-11-04 03:40:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c50155fd-a9e5-3a35-83dc-e66f5e68987e | -3.98487 | -47.08223 | 2025-11-04 03:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8f110eb9-7184-3170-9063-94024ceba273 | -4.58985 | -40.97839 | 2025-11-04 03:40:00 | NOAA-21 | IPUEIRAS | CEARÁ | Brasil | 2305902 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 91e20c83-31cd-3473-b9db-215b57524164 | -4.57821 | -43.34275 | 2025-11-04 03:40:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95a6db24-3174-3f8a-8443-b52885f72bf3 | -3.92364 | -38.4063 | 2025-11-04 03:40:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d66cbffa-9135-3a47-9a0f-bef42ce15dd6 | -3.98894 | -47.08419 | 2025-11-04 03:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d9fdc4b3-1785-3e8a-96ae-d05c69daca30 | -2.49055 | -45.97172 | 2025-11-04 03:40:00 | NOAA-21 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 10d8833b-1364-3ec4-a704-78b4c078357b | -5.53338 | -41.09257 | 2025-11-04 03:40:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dc06d547-a501-32f4-a480-07a97f44e937 | -3.91616 | -47.6921 | 2025-11-04 03:40:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 35f936a2-9a5c-3171-a26e-71995e24fa62 | -4.61339 | -45.76176 | 2025-11-04 03:40:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd43bff5-de51-371f-82a5-c4726a232cab | -6.17315 | -39.94803 | 2025-11-04 03:42:00 | NOAA-21 | ARNEIROZ | CEARÁ | Brasil | 2301505 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8139e27e-6464-3708-bcea-9414dce57548 | -5.37094 | -45.07605 | 2025-11-04 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f608966d-d06c-3a15-b413-10bf3e54d120 | -5.92915 | -41.29676 | 2025-11-04 03:42:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2a96a873-e628-39b2-ba32-39a0d6f470cd | -10.49391 | -42.40866 | 2025-11-04 03:42:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f9ebd113-045d-3a08-a9ff-f2ed2c535f5c | -6.6072 | -43.76198 | 2025-11-04 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ee515047-ff81-35a8-86f0-b262e9d7c300 | -9.00031 | -35.26948 | 2025-11-04 03:42:00 | NOAA-21 | MARAGOGI | ALAGOAS | Brasil | 2704500 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| feb87975-c1ab-3faf-ae8d-94883fd5e2d2 | -5.57668 | -43.78899 | 2025-11-04 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5f33a8e-6c36-3131-a9db-b9b3fd792283 | -6.241 | -42.08541 | 2025-11-04 03:42:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 32304ecf-0598-3669-94ad-682f387ab1d1 | -10.94255 | -44.20121 | 2025-11-04 03:42:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d72fc14c-2ec1-31ca-a5fc-49baecc05e08 | -5.23718 | -44.21305 | 2025-11-04 03:42:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ba64650-41d2-316b-93e2-806bd4eb1c98 | -6.09857 | -41.70402 | 2025-11-04 03:42:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 46cc7e2b-d1f5-330f-b2c0-b1500d2f7193 | -5.92335 | -41.30448 | 2025-11-04 03:42:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 77ce2b3f-f895-3a4d-a3d2-8718d0a28d8b | -11.68542 | -41.12302 | 2025-11-04 03:42:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 88d32f1c-aece-3a91-bd96-3032646927f6 | -5.83392 | -44.66137 | 2025-11-04 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6db29e70-cb33-3480-a138-9d0ce66737dc | -5.57128 | -42.29862 | 2025-11-04 03:42:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1d1e9060-9b1a-35f5-befe-978bf39efd23 | -5.83326 | -44.66507 | 2025-11-04 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 93fc7ad4-c729-3750-a576-0f3a43d9f136 | -4.91453 | -47.32819 | 2025-11-04 03:42:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| abca932b-d386-3262-9ba6-1ac08c6bb83d | -10.01873 | -37.38803 | 2025-11-04 03:42:00 | NOAA-21 | PORTO DA FOLHA | SERGIPE | Brasil | 2805604 | 28 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 73f1fb1e-ae1b-3394-8d3f-24b2861cf651 | -5.36243 | -44.73733 | 2025-11-04 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 144825d4-2517-3383-be57-e64b0750c3ae | -7.85339 | -44.21463 | 2025-11-04 03:42:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0cba11c5-5caa-33d1-bbf5-a39dc97468ff | -5.78384 | -40.80861 | 2025-11-04 03:42:00 | NOAA-21 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| eb310ef9-dd03-3bbf-9954-bd46fd39db42 | -5.89712 | -42.90789 | 2025-11-04 03:42:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| e83f2e33-d434-36af-ad80-383571f0063c | -7.22037 | -39.95586 | 2025-11-04 03:42:00 | NOAA-21 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 815b443b-bf68-3d4a-be0c-5298db650935 | -6.60968 | -43.7587 | 2025-11-04 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d088201-fe12-3dea-bc79-e8242c94d2bf | -5.36468 | -44.74516 | 2025-11-04 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 79ac0537-b385-32df-ada0-77faaf1b9de0 | -5.92853 | -41.32791 | 2025-11-04 03:42:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cd0266b8-d0d2-311f-b60f-7320ea2564eb | -11.11763 | -41.09154 | 2025-11-04 03:42:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 47ee92b8-96ec-34d4-b9b9-3ade270d35f9 | -9.85367 | -44.1402 | 2025-11-04 03:42:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| efdb34d0-4d05-3d67-a414-6caa633da8a7 | -6.413 | -43.0657 | 2025-11-04 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| cfe01b55-2215-3032-bc57-c58ef6208acf | -5.23116 | -44.20647 | 2025-11-04 03:42:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b47576ef-fcf1-32a2-bad8-444f67eb60c0 | -6.42191 | -43.0728 | 2025-11-04 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 388ba090-2ae3-35ba-ac18-cb7f16089688 | -6.13115 | -41.54207 | 2025-11-04 03:42:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 90d9d1f6-2097-3472-94c3-355c751784e5 | -5.65333 | -44.066 | 2025-11-04 03:42:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da23444f-0f3a-3837-be1f-4ab5f137aeee | -6.24561 | -42.08629 | 2025-11-04 03:42:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 4a0f1193-0386-3c06-855c-b3f749855dc0 | -6.31372 | -43.80855 | 2025-11-04 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| abb5623f-79f1-3686-94d2-7218d4875eaa | -5.58141 | -43.79295 | 2025-11-04 03:42:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d3272ed0-06a5-31e8-a024-41bfc0424999 | -5.06166 | -45.91229 | 2025-11-04 03:42:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 8a6151c2-c8fc-319c-8abb-b488fa626284 | -7.85448 | -44.2086 | 2025-11-04 03:42:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 40b495ee-0a2c-37a5-8352-e1033fe3d353 | -5.43164 | -44.65918 | 2025-11-04 03:42:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4f192888-8ff9-3e57-9a90-9fe36467e25d | -6.40806 | -43.06493 | 2025-11-04 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cf2e50dd-28e3-39d1-83e5-9750bec8df53 | -5.36179 | -44.74109 | 2025-11-04 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1106058f-1048-3849-b31c-a54d9ba6dd63 | -6.19213 | -39.33187 | 2025-11-04 03:42:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| eba15b71-b71c-3ac4-b5a7-3eae1c854b0a | -5.89618 | -42.91349 | 2025-11-04 03:42:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 54e0e271-bb4b-36e7-a7fb-4210332eb9a4 | -11.68602 | -41.11954 | 2025-11-04 03:42:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 0cf571f7-1754-3e54-bdd3-ef721478fd1f | -5.29789 | -44.80947 | 2025-11-04 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e02e0c8-db73-340e-928a-84ecbed357de | -6.13928 | -41.54818 | 2025-11-04 03:42:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e9238990-f2f0-3b5f-b7e6-d8276961c986 | -5.28622 | -44.61211 | 2025-11-04 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8c04778-dbcb-306c-9c51-fda7ae00e4dc | -7.77936 | -42.21597 | 2025-11-04 03:42:00 | NOAA-21 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 92c2c7bc-9ab2-3fac-8714-c58c29dd0f6c | -8.66038 | -36.81442 | 2025-11-04 03:42:00 | NOAA-21 | VENTUROSA | PERNAMBUCO | Brasil | 2616001 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 066ed8c8-e162-3386-82f6-8f8e3504e8a5 | -10.86909 | -44.40556 | 2025-11-04 03:42:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 077e4483-4eb1-390c-95b1-12989ad41ea6 | -10.93375 | -44.19368 | 2025-11-04 03:42:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8e214f8c-f868-3c4e-8ebe-9833758b11cb | -6.40993 | -43.07385 | 2025-11-04 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 01b6b5d1-571d-3b11-93be-ef79b21f2a38 | -5.92191 | -41.31317 | 2025-11-04 03:42:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d54fb7b2-3333-38da-899c-6a98ce4b9e5e | -8.11059 | -43.82158 | 2025-11-04 03:42:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e114517d-7bdc-31a4-a3c8-218de6c5b7bc | -4.91738 | -47.32723 | 2025-11-04 03:42:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| abcb8725-d248-3d6f-8c8c-b4d580960b32 | -5.44399 | -47.06528 | 2025-11-04 03:42:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19f8a352-e320-352b-9b06-a799815ee09c | -5.36039 | -44.73675 | 2025-11-04 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 052d0e93-3a1a-3757-a4ba-f8d90242c8bb | -11.32933 | -41.67139 | 2025-11-04 03:42:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e2dbb105-b45d-3903-afa6-982adc25fc7e | -7.78314 | -42.22117 | 2025-11-04 03:42:00 | NOAA-21 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3dfc3ba4-bc6c-36d4-abe1-43a39c80915b | -11.96745 | -41.14666 | 2025-11-04 03:42:00 | NOAA-21 | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 343d2900-43ba-3ed6-a1be-8f565b29273f | -10.86801 | -44.41139 | 2025-11-04 03:42:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| da588cdf-67b4-3e61-91c8-ad894a05af54 | -5.8986 | -42.90989 | 2025-11-04 03:42:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| b7094a87-ecf2-3b19-9ec9-9db37f4c3cfe | -6.43277 | -43.06881 | 2025-11-04 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 901cae7f-c40e-38bf-a088-c11fdd8b9004 | -5.90959 | -39.99369 | 2025-11-04 03:42:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 44a087e3-56a2-3c0e-b403-182b64084e2c | -5.23545 | -44.21422 | 2025-11-04 03:42:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 69e54058-3e23-3539-9d62-12e213ae5747 | -5.89125 | -42.91267 | 2025-11-04 03:42:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| c474de2b-96b4-35b3-8a6c-5f311cc7311d | -6.4844 | -39.41764 | 2025-11-04 03:42:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 44cc6711-4a88-37c5-ba72-0a02d9726d20 | -9.98453 | -36.56026 | 2025-11-04 03:42:00 | NOAA-21 | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9f0542b9-d4be-333f-aca7-ac59a8916e99 | -6.45734 | -37.51456 | 2025-11-04 03:42:00 | NOAA-21 | SÃO BENTO | PARAÍBA | Brasil | 2513901 | 25 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c5016154-e34f-3092-8e3c-41bf99b5cd5b | -6.48358 | -39.42253 | 2025-11-04 03:42:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c0877dd4-1fa0-39c6-b86c-6cf8a35a5519 | -6.60775 | -43.75877 | 2025-11-04 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b9a3477-f190-310f-85ef-df2d2a7b35a8 | -6.61115 | -43.61578 | 2025-11-04 03:42:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 19e6819f-1bc6-30ec-8a28-f3625a570e4f | -7.85394 | -44.21157 | 2025-11-04 03:42:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 126f9841-3efa-3b4a-942f-d333d7769c81 | -6.42782 | -43.06807 | 2025-11-04 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c7b3545f-fa45-3d10-a699-4e40fe28026e | -6.29367 | -37.87825 | 2025-11-04 03:42:00 | NOAA-21 | JOÃO DIAS | RIO GRANDE DO NORTE | Brasil | 2405900 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8ad69b5c-aef1-3589-88b9-1302ea6a1d67 | -7.08694 | -38.82949 | 2025-11-04 03:42:00 | NOAA-21 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ea7be162-8859-3fcd-99f9-5ac4ff8c793b | -11.18036 | -41.79916 | 2025-11-04 03:42:00 | NOAA-21 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 128a46a8-416f-3f0c-b2d0-d7faf061b412 | -5.92263 | -41.30881 | 2025-11-04 03:42:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8181783b-9074-3b24-b338-d4969a29da26 | -6.07317 | -47.28743 | 2025-11-04 03:42:00 | NOAA-21 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README8.md)
