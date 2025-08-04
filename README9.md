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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01ed0c29-cff7-37c0-adce-6dc9600863fd | -7.1996 | -44.49184 | 2025-08-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4440e1d0-afad-320d-9a6c-d521557f17e7 | -7.08965 | -44.36603 | 2025-08-04 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b694c357-921e-37a4-af09-7ab08836a3c0 | -6.83953 | -44.85728 | 2025-08-04 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ea3a119-4d84-3e9b-bdd6-1b89239d5045 | -8.00771 | -43.14909 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a62a3b5e-d260-34fc-a117-40ed06a24dae | -7.99708 | -43.17295 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 39dc10c4-3c0f-35f7-9305-459f7644d63f | -6.67575 | -44.36599 | 2025-08-04 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 69414c50-5277-32f8-b136-88f2f8cb0b45 | -5.8803 | -43.74408 | 2025-08-04 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d849e01-5f65-33e9-a7b0-e2b1f153dd02 | -8.01584 | -43.13587 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 74947cad-f9a6-39f4-baaf-a807babd1f03 | -8.74488 | -46.41553 | 2025-08-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3d718de-d557-359f-8b6d-d798907a1f49 | -8.74026 | -46.41971 | 2025-08-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66b523d2-4a29-3ff3-aca1-077e75815433 | -10.36348 | -45.18632 | 2025-08-04 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1553e53-9787-3c5d-83f0-aa1ba82cfa92 | -8.38157 | -46.94621 | 2025-08-04 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 85356589-f0ac-3e4d-b91d-2965fcd842e0 | -7.40318 | -45.26944 | 2025-08-04 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ed25888d-3e96-328e-ba21-b54a0b698757 | -7.64605 | -45.29778 | 2025-08-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 90cf26af-f999-3ba2-bbdd-cb2f95b4f16d | -9.39187 | -45.50577 | 2025-08-04 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 81d41ce9-9b5d-3413-ac5f-ba98faba6921 | -8.35947 | -46.91408 | 2025-08-04 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b0baa961-d149-34a2-a09d-dbe9010f28a4 | -10.57071 | -45.27278 | 2025-08-04 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0523455-a17a-3a96-82c2-3eb7a10193a6 | -4.12809 | -47.64688 | 2025-08-04 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b327f161-b842-3b50-b4f6-ea61588fc109 | -7.53605 | -44.87564 | 2025-08-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| debd7611-c932-3337-97de-ba6beba942c9 | -7.48277 | -45.05359 | 2025-08-04 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1755341d-fb5d-3530-bbba-83b175105ceb | -7.61918 | -45.30239 | 2025-08-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2463880c-138f-3c6b-baf7-df3a44e940b8 | -8.04041 | -43.11069 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 371841c7-0b1f-39bf-9f11-8abab3e87e2d | -8.05823 | -43.10627 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ba8c664c-bc18-3364-acdc-d34d4a4e0cc4 | -6.67927 | -44.36651 | 2025-08-04 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 109465db-e817-3380-a4b0-90b5012d93ee | -7.78318 | -45.22229 | 2025-08-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8e8df3d0-bbe6-3881-b5c8-2c749b179ba7 | -5.23254 | -40.87148 | 2025-08-04 04:08:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7cc45c16-819a-34e2-a619-d1b2133be557 | -5.28264 | -44.88216 | 2025-08-04 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 69e61c27-9400-3f16-af94-1f407e6f5e27 | -8.35916 | -46.94042 | 2025-08-04 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 68ebb1fd-abe9-3cbf-8f3a-93062f93a143 | -7.52534 | -45.02976 | 2025-08-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22137d84-5b80-304b-bf32-fe7bb5c488fe | -8.55628 | -47.46277 | 2025-08-04 04:08:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a7cc4c38-77a7-3801-8b94-881bffd062a5 | -8.51681 | -44.74146 | 2025-08-04 04:08:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2872e567-e8e7-3d11-a0f2-ef1058262969 | -7.37187 | -44.18823 | 2025-08-04 04:08:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c5019348-7a81-3df5-b9f4-23cad4333597 | -8.03317 | -43.11318 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 666fb1fc-1c6e-3547-b5eb-338587a022b5 | -6.67158 | -44.36951 | 2025-08-04 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69da8cb9-e1af-3e8d-bfaf-744283bec7ae | -5.27898 | -44.88156 | 2025-08-04 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 722f1cf0-03e4-372e-84bd-b242d8008623 | -7.9545 | -43.90567 | 2025-08-04 04:08:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6fd79376-6c20-3f89-aef5-dad4d161e820 | -8.51501 | -44.74606 | 2025-08-04 04:08:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9a2dcea6-e341-368c-8b62-d8b11b7906e2 | -7.99261 | -43.17954 | 2025-08-04 04:08:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| efd13319-2723-3ac2-bcad-c017f74f958a | -7.53407 | -45.04395 | 2025-08-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5106552c-5041-36de-b2fc-fc7436bc9a5b | -7.99934 | -43.1587 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ecd3dc7a-a2c0-308c-97ef-f3271ad71ff4 | -7.4684 | -45.05112 | 2025-08-04 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d44696b-fce8-394e-acf5-52732b43f738 | -8.00093 | -43.2137 | 2025-08-04 04:08:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 470021b4-5fb7-38d7-90ea-d19d85ba7213 | -7.30836 | -44.67178 | 2025-08-04 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 60ff0df8-c3af-3644-aec2-2f46fc9c36ec | -3.39701 | -46.90764 | 2025-08-04 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d820ed1-e202-3e61-90e2-be67b459c1b9 | -8.74039 | -46.39552 | 2025-08-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 29212449-5620-34bb-a7ef-d65fc251ff53 | -4.12733 | -47.65139 | 2025-08-04 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0690cf5c-e665-35e9-a05d-650bb41c85d1 | -4.12884 | -47.64242 | 2025-08-04 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f275ac2e-355c-3e06-a7dc-e2a313ec0150 | -4.12811 | -47.65202 | 2025-08-04 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 1428f07b-6bd1-3325-8e69-46356db981c1 | -6.57208 | -47.03289 | 2025-08-04 04:08:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 54a70e1d-a867-307e-85ff-a53762e17db1 | -8.73961 | -46.40019 | 2025-08-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58d56bec-4d24-3372-9a48-374f54576a76 | -6.20033 | -43.76282 | 2025-08-04 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d80aceb4-1a1b-38e7-91fb-100dd3271408 | -7.55165 | -44.86972 | 2025-08-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 407b1470-8597-39bf-a257-0ffedc0daa2c | -7.99543 | -43.16174 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 89.5 |
| 2db6defe-65b6-3a08-b621-8dd25e0886a2 | -8.01121 | -43.18614 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0085d8e0-dd2a-344d-9e0a-f026bbf9f80b | -10.29692 | -45.17505 | 2025-08-04 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd1125a5-31d0-3c2b-9dff-5cbb776bab42 | -8.27053 | -47.37247 | 2025-08-04 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 95588316-a59a-377d-b0e3-b5ff66e47359 | -7.0814 | -44.37262 | 2025-08-04 04:08:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ebd18a3e-4f91-38af-9c67-9fd4f5df5e3d | -7.99318 | -43.17599 | 2025-08-04 04:08:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 95b9b9ff-0d07-3684-8e81-d28428f0f46c | -6.84728 | -44.28849 | 2025-08-04 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e707598d-830b-346d-a06c-54453bdd1dd4 | -8.73883 | -46.40485 | 2025-08-04 04:08:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aab648d7-5e08-3cfd-89bc-869c37c440f8 | -8.36654 | -46.92045 | 2025-08-04 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b3cf9e1-0574-3938-b124-5274ecaaabad | -10.11776 | -45.65909 | 2025-08-04 04:08:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1d4ac29a-459a-384e-8823-a93b48a19413 | -6.5434 | -42.81037 | 2025-08-04 04:08:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bc08c346-9493-3115-b457-aa428647cbb4 | -10.57552 | -45.26544 | 2025-08-04 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a2f7e92-34ff-3e3c-91bd-79bf0f0a5c9c | -7.69078 | -45.12299 | 2025-08-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 371c7f41-f702-302a-8708-1cf909c59019 | -8.26446 | -47.33398 | 2025-08-04 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 766ba5b4-4837-34f8-934d-338d98c2b54f | -9.64336 | -43.84988 | 2025-08-04 04:08:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8f6fd3f4-1027-317c-a2f9-24e66c07c4e0 | -7.99652 | -43.1765 | 2025-08-04 04:08:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f90c2002-0de1-3b72-a70f-c268c44cacde | -8.25976 | -47.33706 | 2025-08-04 04:08:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e1d45482-4ee1-3c3b-b331-6b47733a1a17 | -7.6185 | -45.30658 | 2025-08-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74c5086f-9953-3a97-9593-015b40635c2e | -10.29603 | -45.17563 | 2025-08-04 04:08:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 81a69c29-9aaa-337a-99f4-ed48cc0e62ad | -4.12371 | -47.65108 | 2025-08-04 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c013d596-8590-3205-9dc6-fab804fc350e | -7.77108 | -45.10622 | 2025-08-04 04:08:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0f9041c0-7ca9-39fb-a329-8c309f9d988c | -5.87845 | -50.14888 | 2025-08-04 04:08:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5b48247-1459-3c66-b1ba-005329f761d1 | -3.74341 | -40.82525 | 2025-08-04 04:08:00 | NOAA-21 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2c76a801-274b-3f74-927d-d787f1861151 | -5.12241 | -37.64425 | 2025-08-04 04:08:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6511d779-2124-3c25-a8a7-76b3d78c8fcc | -7.56256 | -44.89243 | 2025-08-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45d1da32-382f-34f2-9520-fb064f06b3d0 | -6.13037 | -44.44056 | 2025-08-04 04:08:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8e709378-f51c-38a8-b45d-50c45275ed53 | -8.00272 | -43.21767 | 2025-08-04 04:08:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f39eb01f-2cef-3a86-97fe-f38dd84f6443 | -8.13083 | -49.5848 | 2025-08-04 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 529a760d-354a-3078-8e9d-9e6f9e8fa6a9 | -7.44332 | -48.9411 | 2025-08-04 04:08:00 | NOAA-21 | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a158ca0-b722-3c32-bb2a-4a03daecc60d | -5.2863 | -44.88275 | 2025-08-04 04:08:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| ac89e18d-270e-3af8-a7eb-47c3df52ed01 | -8.13465 | -49.5907 | 2025-08-04 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ebd8927b-ec4e-3bda-8703-0a77807f421f | -8.05156 | -43.10521 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 18.6 |
| 46fac328-0fe8-3442-b2fb-924d74bef78c | -8.04431 | -43.10769 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 06428bf7-d9f9-34d5-b1fe-44c9edd78ede | -6.55895 | -43.9158 | 2025-08-04 04:08:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0ebc7706-e551-380c-ad20-ea3c480db980 | -4.74264 | -44.43563 | 2025-08-04 04:08:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d37818a5-a73e-3bfa-abf6-0f8287b92802 | -8.36172 | -46.92497 | 2025-08-04 04:08:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5876eeed-aa5e-3bf9-a21b-f41ba0c84556 | -4.12443 | -47.64659 | 2025-08-04 04:08:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5a96f0c7-c8bb-335d-a66b-fdc2c2389175 | -6.32209 | -45.65493 | 2025-08-04 04:08:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2b41e806-d87e-36c1-8c54-eaf9724978b4 | -7.55454 | -44.87439 | 2025-08-04 04:08:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0cb3493-0b33-3a66-940d-5d8a678ea5ac | -6.145 | -43.78185 | 2025-08-04 04:08:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| faabaee6-4b80-3124-9c7d-bad5a14e1d9d | -10.11847 | -45.65484 | 2025-08-04 04:08:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ddb7592-4a3e-3037-8d23-1424f546605c | -7.996 | -43.15817 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.5 |
| e8cca341-0698-3eef-8441-e73f7b70b5e1 | -7.41131 | -45.28826 | 2025-08-04 04:08:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9675ae4-150a-3f5c-bafb-4ba2f792ea51 | -8.5155 | -44.74936 | 2025-08-04 04:08:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7bc90f52-fb07-3fc7-8436-0c31dce9f2d5 | -8.13416 | -49.5873 | 2025-08-04 04:08:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 13f21149-0fbb-3232-af5b-b82792794230 | -9.39616 | -45.50221 | 2025-08-04 04:08:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c7480441-6772-38dc-b50a-550eeea2d4c2 | -8.00827 | -43.14554 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.2 |
| 000cc1ed-9871-35a3-8375-f97bdbf76854 | -8.02131 | -43.16588 | 2025-08-04 04:08:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |


[Clique aqui para ver as próximas entradas](README10.md)
