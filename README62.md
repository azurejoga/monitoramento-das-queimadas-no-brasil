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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a53ac73-f1ca-31f3-9402-8d2018d43d25 | -12.9509 | -42.4886 | 2025-10-09 11:40:00 | GOES-19 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 95.5 |
| 7ab0ba7c-e4f1-30ec-beb1-71fe4706168f | -13.4282 | -47.6151 | 2025-10-09 11:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 188.2 |
| 9dd15c13-c756-3332-b8c2-4ce94475f7e8 | -12.6964 | -47.6776 | 2025-10-09 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 1e601b81-57f2-3ea4-a588-f241f33432fc | -17.6415 | -47.2103 | 2025-10-09 11:40:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 174.0 |
| a9e8aab7-4bb8-35a6-9970-c133d69727ca | -18.6504 | -43.9056 | 2025-10-09 11:40:00 | GOES-19 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 4f0d2baa-9b50-3bae-b0c8-3ee751161fbe | -14.3889 | -46.0063 | 2025-10-09 11:50:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 0d70063e-705d-38cf-9298-25c01b01ff60 | -17.6415 | -47.2103 | 2025-10-09 11:50:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 744e718f-5abb-3fca-9dd7-59e63724398a | -12.6964 | -47.6776 | 2025-10-09 11:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 26b108fa-b854-3be4-bb2c-d2c382ee76e5 | -13.4282 | -47.6151 | 2025-10-09 11:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 286.5 |
| 5bf7c2a6-4adc-3169-86e2-b1544d8eb32a | -17.5339 | -46.7472 | 2025-10-09 11:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 104.2 |
| a2a1d2dc-94af-33b8-9356-778856be3621 | -12.9509 | -42.4886 | 2025-10-09 11:50:00 | GOES-19 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 101.2 |
| ba0ade85-4dc5-3627-ab50-58cca075b9b1 | -13.8307 | -45.8024 | 2025-10-09 12:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 2bf77e1e-9a04-331f-8cb6-74385b62040f | -12.425 | -45.7056 | 2025-10-09 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 6d3da388-4313-3f39-ba4d-47e83bf78f4b | -12.9509 | -42.4886 | 2025-10-09 12:00:00 | GOES-19 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 105.9 |
| f5113a2b-4950-3d9c-886b-eb4b6564fd14 | -11.993 | -45.1958 | 2025-10-09 12:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| ceaadd9a-9159-3efb-a0b2-5d997cb07e5a | -12.6964 | -47.6776 | 2025-10-09 12:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 205.7 |
| e5b9dd88-7d8d-3616-9edb-419d997c4d1f | -17.6415 | -47.2103 | 2025-10-09 12:00:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 88b2ba77-24b9-339c-a8ad-d380c5c08d3d | -18.0589 | -44.9632 | 2025-10-09 12:10:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 110.6 |
| a6a049d1-6120-383f-9534-1d2cd4cacff9 | -13.8307 | -45.8024 | 2025-10-09 12:10:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 99.5 |
| dd880a94-6a9c-32e0-a1ba-47b9948b6aa9 | -10.1905 | -44.5471 | 2025-10-09 12:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 7ad1741e-f88e-3862-9afc-582d0707480a | -12.425 | -45.7056 | 2025-10-09 12:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 6c0acad8-8952-3075-abc1-43bbb2c1bbb5 | -12.9509 | -42.4886 | 2025-10-09 12:10:00 | GOES-19 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 135.7 |
| a8e835b7-11ad-3893-b1cd-c181d47c7598 | -12.6964 | -47.6776 | 2025-10-09 12:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 188.6 |
| 2bea14f5-0228-352f-86af-389f7e2d7b47 | -15.5554 | -45.3278 | 2025-10-09 12:10:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 91.3 |
| f59377de-ee31-37ea-a81a-3d541224325c | -11.993 | -45.1958 | 2025-10-09 12:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 113.7 |
| e193fcdf-965b-3cfa-91b9-42e1a4f600a1 | -8.18928 | -43.33893 | 2025-10-09 12:17:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 123.5 |
| c8a512e9-8817-3d26-a30b-28b23c088fcd | -5.50444 | -47.02674 | 2025-10-09 12:17:00 | TERRA_M-T | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| 135c3012-e60a-3147-8cf5-cb58eaa4c8a6 | -7.35321 | -43.86369 | 2025-10-09 12:17:00 | TERRA_M-T | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 8015a4a7-6779-3815-8491-b4a3b9db47cb | -4.63766 | -45.61171 | 2025-10-09 12:17:00 | TERRA_M-T | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 27.2 |
| 8e1aaa0f-ed66-3183-b411-3e959fbdb9f0 | -3.60152 | -43.79897 | 2025-10-09 12:17:00 | TERRA_M-T | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 5f524ff3-a8ad-3d64-aa1d-79623594955a | -7.02136 | -42.8762 | 2025-10-09 12:17:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 28.5 |
| 46f5fc53-1ba1-32bd-83bb-7a7d0c96f599 | -7.50194 | -44.71326 | 2025-10-09 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 406721c7-7988-32a2-84f8-e3c12acc0cd5 | -6.89757 | -47.66452 | 2025-10-09 12:17:00 | TERRA_M-T | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 79bce8bd-8100-37e5-ae9d-b080faea46a3 | -4.50307 | -46.35456 | 2025-10-09 12:17:00 | TERRA_M-T | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| bef82e75-559b-3e36-ba41-c13b50427960 | -3.14572 | -44.42543 | 2025-10-09 12:17:00 | TERRA_M-T | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 14509aaa-aeca-3934-b33c-e92793035bc6 | -7.2559 | -45.80466 | 2025-10-09 12:17:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 4f2f48cf-3674-3145-beef-b2ba41ea679e | -8.16956 | -43.32264 | 2025-10-09 12:17:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 35.4 |
| 870abb44-9933-3875-a81e-2b0f9a57c132 | -3.96767 | -44.16449 | 2025-10-09 12:17:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| a4c121c9-334c-3146-9d53-9fe1a1a0fba2 | -7.01411 | -42.86729 | 2025-10-09 12:17:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 3b2f3e43-6fa4-39f9-8efe-2d84f4ddd65f | -7.99884 | -44.46087 | 2025-10-09 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 2ea54987-44fb-3d71-8186-6db2dd6bbb9d | -4.05067 | -44.16061 | 2025-10-09 12:17:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| a420779a-50f2-3888-b1ce-49b51298d052 | -4.55592 | -46.44026 | 2025-10-09 12:17:00 | TERRA_M-T | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 20edc129-6540-3c69-ac0b-4853ad9f4ee7 | -3.48713 | -45.65816 | 2025-10-09 12:17:00 | TERRA_M-T | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 968121eb-2362-343a-a144-cd2dee6e7c22 | -3.9662 | -44.17484 | 2025-10-09 12:17:00 | TERRA_M-T | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 53aa8d1e-bf63-301f-b698-8e2599558acc | -7.79912 | -44.19548 | 2025-10-09 12:17:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 866aa232-0ce6-3bf1-8d96-3b3fcbab84a4 | -7.2514 | -44.1665 | 2025-10-09 12:17:00 | TERRA_M-T | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 872c6620-a826-3fef-89b3-d30142e69b21 | -8.20003 | -43.3403 | 2025-10-09 12:17:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 210.5 |
| 873cc2a0-49a8-3c91-a7e9-dbf2a2c993d7 | -7.52889 | -44.30339 | 2025-10-09 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 438ddb6e-1923-3ce3-a1f4-758aa992417a | -6.57429 | -45.73496 | 2025-10-09 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1d54b0e4-5f0b-3b77-91b2-2a47240f1a98 | -8.09127 | -44.82554 | 2025-10-09 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 1f6202c9-8282-32e4-995b-d738b1dce70a | -7.49556 | -43.11578 | 2025-10-09 12:17:00 | TERRA_M-T | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 40.8 |
| 5ff33e86-cd14-3552-890b-e75be5d469fa | -7.77475 | -42.39477 | 2025-10-09 12:17:00 | TERRA_M-T | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 18.9 |
| c3881ff9-4fb8-3df3-b920-ff92f68bff36 | -7.7607 | -44.0284 | 2025-10-09 12:17:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 53ac40a4-fb00-3efa-90de-2f25c571fb50 | -5.48181 | -42.90372 | 2025-10-09 12:17:00 | TERRA_M-T | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 1431bfb8-e7f1-3391-b8b9-f446724dc240 | -8.19823 | -43.35384 | 2025-10-09 12:17:00 | TERRA_M-T | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 138.4 |
| 226603eb-c000-3620-8433-e394aa9b1d04 | -4.39986 | -43.05994 | 2025-10-09 12:17:00 | TERRA_M-T | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| b5de411b-9eae-349d-aaad-98d352e32633 | -4.30395 | -45.49377 | 2025-10-09 12:17:00 | TERRA_M-T | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 27.5 |
| b512f358-bacf-30fe-b1cb-b21077826887 | -2.37345 | -47.6297 | 2025-10-09 12:17:00 | TERRA_M-T | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| f693b4b6-b3a8-3857-89a8-8e04ea585f30 | -6.45858 | -44.58119 | 2025-10-09 12:17:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| df70a724-53d5-3682-aede-d8da2ef7b771 | -7.29109 | -44.83396 | 2025-10-09 12:17:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 26.6 |
| de783b1a-e438-3f17-bad9-17fdfb53efe7 | -5.87834 | -44.11749 | 2025-10-09 12:17:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d607e539-b25d-32bc-b079-1204aa56d62c | -4.39124 | -43.04613 | 2025-10-09 12:17:00 | TERRA_M-T | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 34168346-9c6f-395d-819a-acb53c19e4a8 | -7.65542 | -43.89823 | 2025-10-09 12:17:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 17.3 |
| f79342f1-428c-3113-a33c-809b901eade9 | -6.69731 | -46.29859 | 2025-10-09 12:17:00 | TERRA_M-T | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 09bff95a-538e-3127-a50a-27445cd2390d | -1.4622 | -47.17089 | 2025-10-09 12:17:00 | TERRA_M-T | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 60a9be5b-c0fc-3dcb-b931-52a5521834f6 | -4.29494 | -45.49252 | 2025-10-09 12:17:00 | TERRA_M-T | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8e12faef-f2e2-3c9d-a643-f3e9b3b1edd3 | -8.11286 | -43.67401 | 2025-10-09 12:17:00 | TERRA_M-T | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 3310aa13-6b60-3dee-a080-0b9e94dd277f | -7.50141 | -42.72403 | 2025-10-09 12:17:00 | TERRA_M-T | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 36.2 |
| 8ff07e71-d1fe-3446-b8ac-68864e2282bc | -4.88917 | -45.06663 | 2025-10-09 12:17:00 | TERRA_M-T | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0faec9ce-1d98-35a1-b387-ce419db321cb | -3.45363 | -44.40509 | 2025-10-09 12:17:00 | TERRA_M-T | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 6bcd1381-5723-33d1-ad5e-64bfab9e98d2 | -4.48279 | -44.29294 | 2025-10-09 12:17:00 | TERRA_M-T | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 7ab28907-cb6e-3167-8bae-56122fed5d2d | -7.52736 | -44.31455 | 2025-10-09 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 34.7 |
| c925fc7d-9125-3858-8834-e3c5d9da423f | -6.79518 | -50.48315 | 2025-10-09 12:17:00 | TERRA_M-T | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 230.9 |
| b7631010-ccc3-378b-a006-b852ce6ac81e | -7.01671 | -42.74673 | 2025-10-09 12:17:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 25.2 |
| 60213f93-070d-3f16-869b-5e8dc21fc1c5 | -4.34984 | -43.04052 | 2025-10-09 12:17:00 | TERRA_M-T | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 5fcad77e-a6fc-3574-9f3b-8950f4322aa7 | -5.46095 | -43.50554 | 2025-10-09 12:17:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 7135806f-8022-3092-beed-4f27f32b2c74 | -8.37321 | -44.78266 | 2025-10-09 12:17:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 4c27bfff-6edd-3b29-84f8-05f49b9ff85b | -4.6888 | -45.83793 | 2025-10-09 12:17:00 | TERRA_M-T | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 614f2fc0-62c0-3f56-92c7-7371e08adbfa | -4.55466 | -46.44906 | 2025-10-09 12:17:00 | TERRA_M-T | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 51932c56-36e8-3d97-830e-5b89d0c45710 | -4.63896 | -45.60252 | 2025-10-09 12:17:00 | TERRA_M-T | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 44f66ec7-e03c-3a3b-9e25-a47f24b25e45 | -8.28895 | -41.67432 | 2025-10-09 12:17:00 | TERRA_M-T | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 28.6 |
| 4a490820-e18d-3fec-b17d-8ba2e072b777 | -7.66772 | -43.96072 | 2025-10-09 12:17:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| cea14a11-06bc-31ce-89b4-af6e34010bfa | -7.50166 | -42.72984 | 2025-10-09 12:17:00 | TERRA_M-T | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 73.2 |
| 8f48c3fd-bc1b-364e-ae32-4accead8b3f9 | -4.41999 | -45.91079 | 2025-10-09 12:17:00 | TERRA_M-T | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 04dadbfa-f613-397e-934e-29324d07db77 | -4.40161 | -43.04748 | 2025-10-09 12:17:00 | TERRA_M-T | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 03e512de-422e-3c19-9b38-c780eb2d8b94 | -5.98579 | -44.1499 | 2025-10-09 12:17:00 | TERRA_M-T | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 0f7c1dc5-456f-3512-84f3-5edb8a3eeb26 | -7.02504 | -42.8688 | 2025-10-09 12:17:00 | TERRA_M-T | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 39.5 |
| b779f349-5ee5-38f6-b1b4-f4d2f1a62199 | -4.86227 | -42.54079 | 2025-10-09 12:17:00 | TERRA_M-T | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 26.8 |
| 4106ee1a-8d71-3e5b-ae4f-f3b9e5330c6e | -6.69602 | -46.30765 | 2025-10-09 12:17:00 | TERRA_M-T | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 3bf2bf79-9835-3171-aefc-f211ddc6f9c6 | -7.49943 | -42.7385 | 2025-10-09 12:17:00 | TERRA_M-T | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 70.8 |
| 5cb36b80-8127-3a55-9018-f4894b0b0539 | -7.52396 | -42.73273 | 2025-10-09 12:17:00 | TERRA_M-T | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 30.1 |
| dd1c429a-8b62-3374-b5ce-de8df0db7808 | -5.50317 | -47.03555 | 2025-10-09 12:17:00 | TERRA_M-T | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 611ce518-0fb0-347d-83d4-e0b59995a59e | -3.60302 | -43.78814 | 2025-10-09 12:17:00 | TERRA_M-T | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 38.5 |
| 069c9fb9-1e9d-3c52-9cb9-0e0c1b8ddc79 | -3.48584 | -45.66713 | 2025-10-09 12:17:00 | TERRA_M-T | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 0bd168c1-5042-3e2e-b971-8db7ad31326d | -8.28342 | -41.68567 | 2025-10-09 12:17:00 | TERRA_M-T | CAMPO ALEGRE DO FIDALGO | PIAUÍ | Brasil | 2202117 | 22 | 33 | nan | nan | nan | Caatinga | 28.8 |
| 9f99ec3c-686e-30df-b4dc-978f945d592e | -5.45294 | -43.4982 | 2025-10-09 12:17:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 810ed0c5-6243-3913-9e56-a4f364444c2b | -7.51591 | -44.32446 | 2025-10-09 12:17:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 9898ff77-2173-3613-93ae-d7cfa5ec1025 | -6.80343 | -50.49604 | 2025-10-09 12:17:00 | TERRA_M-T | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| f4faa834-a05b-3d0c-a4b1-dc075bcd03d3 | -7.20965 | -46.85223 | 2025-10-09 12:17:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| a02ca719-94b5-31d5-b499-9aad4de59619 | -7.66608 | -43.97272 | 2025-10-09 12:17:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 10.0 |


[Clique aqui para ver as próximas entradas](README63.md)
