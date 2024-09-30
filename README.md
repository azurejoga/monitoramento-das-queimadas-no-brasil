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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa608188-b8b9-3c79-b112-63b43f8caf1d | -21.81285 | -41.43919 | 2024-09-30 00:03:00 | TERRA_M-M | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 33.7 |
| 2201194a-1398-3428-8699-b205dad1d8dd | -21.81277 | -41.44574 | 2024-09-30 00:03:00 | TERRA_M-M | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 29.1 |
| 0d7b51f5-aadd-36cb-a780-04baf0ad0ff5 | -21.79777 | -41.13319 | 2024-09-30 00:03:00 | TERRA_M-M | SÃO JOÃO DA BARRA | RIO DE JANEIRO | Brasil | 3305000 | 33 | 33 | nan | nan | nan | Mata Atlântica | 25.9 |
| 0312b8c0-d622-330d-b3d1-7e7a854de99a | -11.12 | -45.74 | 2024-09-30 00:04:21 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b44b68b1-1f5d-3ea9-a170-b2a63445f63f | -11.15 | -45.79 | 2024-09-30 00:04:21 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aed4a595-c377-320b-b274-589f8d46e49d | -11.15 | -45.74 | 2024-09-30 00:04:21 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6dbb9f0b-bff8-3118-b2b5-67b53ec72eee | -11.18 | -45.75 | 2024-09-30 00:04:21 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 75645a8e-5cfe-3571-95c7-742cf03be571 | -11.18 | -45.7 | 2024-09-30 00:04:21 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 12f89a8e-b2fc-32ed-8693-33cd6512e655 | -10.66 | -46.2 | 2024-09-30 00:04:23 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 922c3546-4abf-3710-a3b2-8d26e0560332 | -10.66 | -46.15 | 2024-09-30 00:04:23 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a5cf4a08-8c6e-3498-ab2d-8a41755a4b8e | -10.69 | -46.16 | 2024-09-30 00:04:23 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8ec12f5e-32fa-3aae-9ca3-809a010d3975 | -11.06 | -52.5 | 2024-09-30 00:04:23 | MSG-03 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9f7dba38-a788-392d-84ed-d84f410153aa | -19.90043 | -43.20442 | 2024-09-30 00:05:00 | TERRA_M-M | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 34.3 |
| 3df9525c-410e-31c6-b028-58022e05cef2 | -19.89724 | -43.1693 | 2024-09-30 00:05:00 | TERRA_M-M | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 73.2 |
| 25713a58-2db2-3268-ada8-e717e2299b0a | -19.89052 | -43.19978 | 2024-09-30 00:05:00 | TERRA_M-M | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 69.3 |
| f5278e4a-7b1d-3173-bf29-b4d9670ca277 | -19.88759 | -43.16478 | 2024-09-30 00:05:00 | TERRA_M-M | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.9 |
| 69051b66-64e1-3628-8ada-a276e574bc02 | -10.6921 | -45.87375 | 2024-09-30 00:07:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 0dc2caff-e34a-36b9-be66-e3c962b8b6ae | -13.75233 | -42.60443 | 2024-09-30 00:07:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 51.1 |
| 02df7562-e6f0-33f5-9401-ff472cb5b708 | -13.75019 | -42.61127 | 2024-09-30 00:07:00 | TERRA_M-M | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 45.4 |
| 981372b1-0e8f-3440-81de-b4797d5009ad | -12.72844 | -43.48857 | 2024-09-30 00:07:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 4b398e41-462a-3855-b53b-59f5b668febd | -11.2006 | -45.73835 | 2024-09-30 00:07:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| d51f3cd1-19f1-3e7d-82fe-cc18541a8c08 | -11.19628 | -45.69654 | 2024-09-30 00:07:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.3 |
| f2897e49-e8c3-367e-92ba-ca1d3084beb7 | -11.19582 | -45.70307 | 2024-09-30 00:07:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 9a7d52d3-71ad-321e-9ae0-200b1def50d9 | -11.1829 | -45.73977 | 2024-09-30 00:07:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 277.1 |
| 2897300f-7a6b-3170-88c9-4b95675ba62f | -11.18273 | -45.74649 | 2024-09-30 00:07:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 223.2 |
| 8ce92083-1506-3e72-99b4-955429e77391 | -11.1786 | -45.69762 | 2024-09-30 00:07:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 222.2 |
| 00109b15-dd43-33dc-b4a5-e0b6579678b3 | -11.17814 | -45.70434 | 2024-09-30 00:07:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 248.0 |
| 8d9b8469-e85f-3222-b97a-bf081625ee5b | -11.16507 | -45.74841 | 2024-09-30 00:07:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 230.1 |
| 21cdba56-f1ca-3b7b-990f-71a545cb41ae | -11.16488 | -45.7534 | 2024-09-30 00:07:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 209.0 |
| cf6520c0-7930-3388-bb6b-1840958c81b7 | -11.16055 | -45.70632 | 2024-09-30 00:07:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 4064f7a5-58ce-3305-83ed-9136912a44b0 | -11.15158 | -45.62303 | 2024-09-30 00:07:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 48.6 |
| a1eddee0-beee-3587-a4fb-0ad7aea07edd | -11.14743 | -45.7504 | 2024-09-30 00:07:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 523.5 |
| 5daebe4c-2046-34d0-8204-53f4b17070cd | -11.14723 | -45.75533 | 2024-09-30 00:07:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 445.6 |
| c8ae3aec-2bdd-3f01-a186-1d62593d0708 | -11.14295 | -45.70824 | 2024-09-30 00:07:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 450ad732-079b-3b41-99ac-db4d903bcdc8 | -11.14248 | -45.71321 | 2024-09-30 00:07:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 161.9 |
| d84f09ae-97f2-3498-be3f-6015343cc3a8 | -10.69242 | -45.88063 | 2024-09-30 00:07:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 832536cc-5928-345e-b342-00321a69a680 | -8.33006 | -41.17604 | 2024-09-30 00:09:00 | TERRA_M-M | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 9f272d5a-7753-3bdf-a1a1-f1277ad95111 | -8.31387 | -38.6691 | 2024-09-30 00:09:00 | TERRA_M-M | CARNAUBEIRA DA PENHA | PERNAMBUCO | Brasil | 2603926 | 26 | 33 | nan | nan | nan | Caatinga | 7.8 |
| e646b07a-62aa-39b8-80b0-5ed5c89d609d | -7.929 | -42.7751 | 2024-09-30 00:09:00 | TERRA_M-M | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 5346b8a5-fbb9-3e76-b6ad-685dc3ddca36 | -7.91558 | -42.77665 | 2024-09-30 00:09:00 | TERRA_M-M | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 53.1 |
| 1bc715e5-b0ba-33c9-a22c-da3a2dad74e9 | -7.91292 | -42.75526 | 2024-09-30 00:09:00 | TERRA_M-M | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 40.1 |
| d3964c42-6833-3f76-b50c-b2e49daad79d | -7.89248 | -39.33492 | 2024-09-30 00:09:00 | TERRA_M-M | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 46.4 |
| 7c0a3e99-698c-33f5-ac20-9faf3d168a57 | -7.89186 | -39.3408 | 2024-09-30 00:09:00 | TERRA_M-M | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 5ce283db-0cbe-3a8a-a42a-50d4f26324aa | -7.89086 | -39.32294 | 2024-09-30 00:09:00 | TERRA_M-M | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 52.6 |
| bcaaa4a9-8388-3e3d-a341-fecd557c407d | -7.89032 | -39.3288 | 2024-09-30 00:09:00 | TERRA_M-M | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 112.8 |
| eec97dcf-3a6b-3e38-9a46-d36af6f6d8d7 | -7.68924 | -35.25506 | 2024-09-30 00:09:00 | TERRA_M-M | NAZARÉ DA MATA | PERNAMBUCO | Brasil | 2609501 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 46b367d2-e2af-379f-8e02-585fbdeffac7 | -7.06219 | -35.24519 | 2024-09-30 00:09:00 | TERRA_M-M | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 04d412ff-bff3-397d-8acc-648f552e1251 | -6.79716 | -40.14601 | 2024-09-30 00:09:00 | TERRA_M-M | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 6.8 |
| eb65c3ff-4985-3d45-8b22-beee6ff73372 | -6.78652 | -40.14731 | 2024-09-30 00:09:00 | TERRA_M-M | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 89c623f4-b243-32f5-a818-3cc76b3add1d | -6.74886 | -35.2507 | 2024-09-30 00:09:00 | TERRA_M-M | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 6.2 |
| ba539f17-88ca-3728-9e53-936e194f4f6b | -6.74759 | -35.24169 | 2024-09-30 00:09:00 | TERRA_M-M | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 29.0 |
| 1b0e4dc8-56e7-39eb-9f75-12e12b4a8ba8 | -6.71296 | -34.9963 | 2024-09-30 00:09:00 | TERRA_M-M | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| caf0bb2c-66e9-30dc-8de4-caed07c0c050 | -6.53163 | -35.21139 | 2024-09-30 00:09:00 | TERRA_M-M | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| dfde6c4f-2589-369e-b6a6-f1a00e278473 | -6.53034 | -35.20228 | 2024-09-30 00:09:00 | TERRA_M-M | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 38.8 |
| 1a511f54-634b-3399-b39e-e57ccd7c6a9f | -5.99349 | -35.44551 | 2024-09-30 00:09:00 | TERRA_M-M | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 78.5 |
| 5bc2f813-e3f5-3d8a-b7d1-17e33a4e2a48 | -5.99222 | -35.43652 | 2024-09-30 00:09:00 | TERRA_M-M | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 8f4f4ad0-091c-3199-a849-4d6d2fdeeaa3 | -5.79024 | -35.37656 | 2024-09-30 00:09:00 | TERRA_M-M | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 650bfdae-c54e-3f7c-921a-0122c29d56c1 | -5.78896 | -35.36752 | 2024-09-30 00:09:00 | TERRA_M-M | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 910257ad-d68a-3f41-b6be-e7407a2a7b81 | -5.52779 | -35.54917 | 2024-09-30 00:09:00 | TERRA_M-M | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 74e3753a-8b20-3365-be34-f3b0806044fe | -5.52653 | -35.54019 | 2024-09-30 00:09:00 | TERRA_M-M | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 9152c78c-0c72-374c-9322-e5456c7980a3 | -4.41714 | -43.85986 | 2024-09-30 00:09:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 0db614dc-4696-3e2a-a8c6-119938c2c2d7 | -3.96222 | -41.4954 | 2024-09-30 00:09:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 71a40fb5-64d4-3074-ab1a-14d05f4287dd | -3.96127 | -41.48908 | 2024-09-30 00:09:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 12.6 |
| e6f4c3e2-c00a-359d-80f2-c13a0056e623 | -5.98203 | -45.38425 | 2024-09-30 00:09:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| e4dc630e-8ddb-38a6-bdbf-80b4497728e1 | -3.59635 | -44.55137 | 2024-09-30 00:09:00 | TERRA_M-M | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| bb60d63a-3ac8-327d-8769-1541d6eecca4 | -3.62517 | -44.5477 | 2024-09-30 00:09:00 | TERRA_M-M | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| acde9001-1f00-33e5-b2b9-bfc8956eae3b | -3.5929 | -44.52571 | 2024-09-30 00:09:00 | TERRA_M-M | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| a60fe06a-0e9b-317f-a482-0a931398279e | -3.58195 | -44.55327 | 2024-09-30 00:09:00 | TERRA_M-M | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 0207eccd-8bf7-3503-82b2-3062984a0ac4 | -3.57856 | -44.52777 | 2024-09-30 00:09:00 | TERRA_M-M | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 7e15016c-d143-3dd8-8298-c3069d0af4be | -1.72921 | -47.13699 | 2024-09-30 00:09:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 579efaef-9741-3b74-b0f2-eb53c47bef9f | -22.382601 | -43.372299 | 2024-09-30 00:23:18 | METOP-C | PATY DO ALFERES | RIO DE JANEIRO | Brasil | 3303856 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f3efea2e-71fd-3c49-b6c5-b03a80453024 | -22.384399 | -43.381802 | 2024-09-30 00:23:18 | METOP-C | PATY DO ALFERES | RIO DE JANEIRO | Brasil | 3303856 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a19d822f-82f7-3ed7-8b66-3f4024c7f1d2 | -22.077499 | -42.451401 | 2024-09-30 00:23:20 | METOP-C | DUAS BARRAS | RIO DE JANEIRO | Brasil | 3301603 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 04f5cc2d-eee0-3a0e-95cc-138b0c4081bf | -22.067699 | -42.453602 | 2024-09-30 00:23:20 | METOP-C | DUAS BARRAS | RIO DE JANEIRO | Brasil | 3301603 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 037b240b-ab08-33e4-9037-1e354a3c2c54 | -22.069401 | -42.462101 | 2024-09-30 00:23:20 | METOP-C | DUAS BARRAS | RIO DE JANEIRO | Brasil | 3301603 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b90e80c8-d668-3ff1-a4d4-cb99143a39b3 | -22.767099 | -46.786201 | 2024-09-30 00:23:22 | METOP-C | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f6ee0310-6811-382d-b510-583e8e1d14c4 | -22.769699 | -46.8013 | 2024-09-30 00:23:22 | METOP-C | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2661f426-d554-38d7-9cd7-ff14a5d254b8 | -22.391199 | -47.7047 | 2024-09-30 00:23:31 | METOP-C | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0a3eabfc-692f-3e7b-8b36-7d80210ba6a3 | -22.3941 | -47.721901 | 2024-09-30 00:23:31 | METOP-C | IPEÚNA | SÃO PAULO | Brasil | 3521101 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 01e5da24-07e5-3705-9f77-d15406805e26 | -21.6112 | -45.5732 | 2024-09-30 00:23:38 | METOP-C | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0683ef0f-10ab-31d4-b759-14dd131b50f8 | -22.237 | -49.636101 | 2024-09-30 00:23:39 | METOP-C | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fd1a591b-771b-3125-99f1-dcb4007a64fc | -21.522499 | -45.861599 | 2024-09-30 00:23:40 | METOP-C | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e32583e3-8138-38bf-8789-daa46e0f6815 | -21.520201 | -45.848999 | 2024-09-30 00:23:40 | METOP-C | FAMA | MINAS GERAIS | Brasil | 3125200 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cc0088dc-9476-3c37-af39-51447eb4cf68 | -21.524799 | -45.874298 | 2024-09-30 00:23:40 | METOP-C | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 88cdf044-ffaa-388e-b9e5-194b03c6eb85 | -21.858601 | -48.3545 | 2024-09-30 00:23:42 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5cf9ea34-056c-30f6-b4a9-fbe5872af6b5 | -20.6598 | -42.2728 | 2024-09-30 00:23:43 | METOP-C | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0a72c234-e285-35e5-bda8-c2cfdb93e5c3 | -20.661501 | -42.2808 | 2024-09-30 00:23:43 | METOP-C | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4e376ec4-0bca-3bff-ab65-c724496f0cdc | -21.2299 | -45.921101 | 2024-09-30 00:23:45 | METOP-C | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 14163108-3569-3522-b5ea-d851bde2e7d5 | -20.4349 | -42.324299 | 2024-09-30 00:23:46 | METOP-C | SANTA MARGARIDA | MINAS GERAIS | Brasil | 3157906 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3bb69a79-8c88-3a7d-8cf0-8c26832f3b6f | -20.285999 | -43.499298 | 2024-09-30 00:23:53 | METOP-C | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c0f679f3-5fe3-3b50-a0b6-2a1d0d5153ef | -20.2878 | -43.508202 | 2024-09-30 00:23:53 | METOP-C | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| afb8f349-c18f-3a79-a9c3-f4efda09e27e | -20.2896 | -43.5172 | 2024-09-30 00:23:53 | METOP-C | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5b691657-7ac1-3457-a72a-be3f4f4f70f9 | -20.6695 | -46.451099 | 2024-09-30 00:23:56 | METOP-C | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4d075972-e1bd-3a24-a6a9-505ba8845bf5 | -20.6597 | -46.452999 | 2024-09-30 00:23:56 | METOP-C | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a21faea8-8a93-3a06-8a31-29fb7e1f2120 | -19.8899 | -43.157902 | 2024-09-30 00:23:58 | METOP-C | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a4e6f312-66b4-3425-b67b-3dafd8ec9c11 | -19.891701 | -43.166401 | 2024-09-30 00:23:58 | METOP-C | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c21bea79-b900-309a-bf1a-aa09b5085e40 | -19.8934 | -43.174999 | 2024-09-30 00:23:58 | METOP-C | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c6b44a7f-fff6-3d52-9900-714fb715d9ef | -19.8801 | -43.160099 | 2024-09-30 00:23:58 | METOP-C | JOÃO MONLEVADE | MINAS GERAIS | Brasil | 3136207 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ef310b6f-f974-3a99-8a6e-f077fb3e0a49 | -19.881901 | -43.168598 | 2024-09-30 00:23:58 | METOP-C | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fd022f22-ec00-385b-b31c-842da66e82df | -19.0737 | -43.366501 | 2024-09-30 00:24:12 | METOP-C | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README2.md)
