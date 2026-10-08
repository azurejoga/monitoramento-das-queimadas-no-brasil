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

## Dados Diários - Página 272

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3e7294e-d842-3b21-9117-251167004461 | -11.65027 | -43.68494 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 44.4 |
| b4842a9e-0919-3bed-9198-92b490b43713 | -11.07525 | -44.03412 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 204.9 |
| 984c0433-3dcf-3ad6-a576-5c0378f0fd81 | -10.43658 | -47.28148 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 61c7dd1a-074a-3385-bee4-0b1358a646fc | -8.78741 | -47.37651 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 2e5bf817-ce36-3f74-9e0d-86493f325f1a | -11.41069 | -47.57071 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a49c50b9-beff-3bb1-8c8a-8df73cd53a29 | -11.61222 | -43.62464 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 0caa6702-e937-335c-9900-04127e599856 | -8.95969 | -47.54704 | 2026-10-08 16:18:00 | NPP-375 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0f53e686-5a8e-3046-8827-410ebc96f21d | -12.23414 | -44.71032 | 2026-10-08 16:18:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 33cb86a2-e376-3478-b368-62d28b3915cc | -12.61614 | -44.5442 | 2026-10-08 16:18:00 | NPP-375 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 27.2 |
| e62b1ced-da39-3432-aee2-3d4413d6ea02 | -11.63257 | -43.71107 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| e3c0c192-5569-3339-b947-94556c574f9f | -12.6173 | -44.54059 | 2026-10-08 16:18:00 | NPP-375 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 2dadc4de-1a32-34e6-a1f0-8adc162ed94f | -9.7648 | -44.78936 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 91dab33c-a70e-3b17-afa1-2f83fb79ae01 | -11.76469 | -44.68484 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 9a54e3bc-8378-386f-b52e-d2fb73a1840a | -8.96665 | -47.56251 | 2026-10-08 16:18:00 | NPP-375 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0e5bb99e-e844-34a5-bccf-e0a802848042 | -8.78701 | -47.37352 | 2026-10-08 16:18:00 | NPP-375 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| dafe6545-02b1-3439-885d-09f9aa2d8500 | -6.92671 | -34.96916 | 2026-10-08 16:18:00 | NPP-375 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 81360311-c9a4-38cf-b7b3-9a6a666051aa | -11.1049 | -43.99775 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| beeb23f6-2435-3723-afae-534b6197765b | -10.17533 | -48.05307 | 2026-10-08 16:18:00 | NPP-375 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 167d7479-9c06-308a-995c-9a82d2b2e6d5 | -9.45122 | -38.09065 | 2026-10-08 16:18:00 | NPP-375 | PAULO AFONSO | BAHIA | Brasil | 2924009 | 29 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 45d6f930-3d1f-367a-a326-f1f26b398e5d | -10.61702 | -46.27777 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| cbbee432-d61e-350a-a1b7-dc45d1dd41f2 | -11.84047 | -43.52774 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.1 |
| c0b4d189-6709-3ee6-a554-608fb79bb6c4 | -11.23647 | -44.84245 | 2026-10-08 16:18:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fc4c5a61-0c40-3fe4-abed-911de5dc0224 | -6.66215 | -35.11818 | 2026-10-08 16:18:00 | NPP-375 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 15a4da88-8a4b-3a82-8a31-c8a69232dfae | -10.37932 | -46.30501 | 2026-10-08 16:18:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 29.9 |
| d376191b-f844-31e6-8d33-bc93a7b735b3 | -9.82821 | -45.75986 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 0bdd4dc3-49e1-3a5b-a891-6bbc2d1f44ba | -12.62477 | -47.89338 | 2026-10-08 16:18:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| aaf2a876-8f06-3696-8051-71a08331d289 | -9.84653 | -47.84743 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| dca67384-185f-34f5-9388-484f3413ce7c | -9.52531 | -45.6105 | 2026-10-08 16:18:00 | NPP-375 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 86db0c81-b50e-3270-aa2b-4ad457249c63 | -13.11755 | -46.3432 | 2026-10-08 16:18:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ee106116-6a7f-3589-974d-607c79474636 | -9.32732 | -38.09343 | 2026-10-08 16:18:00 | NPP-375 | DELMIRO GOUVEIA | ALAGOAS | Brasil | 2702405 | 27 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 36713e51-8332-3e83-9d46-5892857fc9c1 | -9.50565 | -46.07537 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e360614a-4452-31db-a27c-3422137a4110 | -11.10917 | -45.6751 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.9 |
| b593ba49-ff7d-387d-90b4-9ceb2e6ade3e | -13.35752 | -43.8769 | 2026-10-08 16:18:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 37a38220-0a4a-35e3-ae46-618609761abd | -8.96178 | -45.15678 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 185.0 |
| 8d54abf5-9838-3c03-98b0-1d1b076d2ca9 | -11.24584 | -46.25553 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 3bed5006-44ef-3a3c-aef6-e9224d14bd5e | -12.41119 | -46.44299 | 2026-10-08 16:18:00 | NPP-375 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 410049cb-bb24-32d6-ba62-12a7b3a3d22b | -8.9435 | -45.18054 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 33.7 |
| d5474273-a2c4-369e-a138-7151faa77dd2 | -11.08692 | -44.02443 | 2026-10-08 16:18:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 166.9 |
| 7ef7cada-fcf3-395b-be47-d2e081466036 | -11.92257 | -46.79197 | 2026-10-08 16:18:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7d1a3bff-d6cf-3849-a490-23dd12f9e2d8 | -12.62063 | -44.54361 | 2026-10-08 16:18:00 | NPP-375 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 27.2 |
| df4f65f9-8fdf-309d-aff1-a3c004bad4eb | -11.95579 | -47.76849 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| e86ed92a-dfc8-345b-a0ef-28a6f9a06320 | -9.85367 | -47.84875 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 38.2 |
| 2cb76e6b-4d8e-3db6-b5e4-4cca6ced5d7d | -11.74896 | -43.64558 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| ee8ccfde-e895-3d53-a7cc-6159e0bbf9b7 | -13.68115 | -48.6412 | 2026-10-08 16:18:00 | NPP-375 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 2c0afc0a-d5c2-3629-8b8f-f6c281e1a66e | -10.84983 | -47.94884 | 2026-10-08 16:18:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 716ca4bb-b5a0-390e-ac13-07aa48ff95ff | -13.12113 | -46.33 | 2026-10-08 16:18:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d7b7bb75-78c5-36eb-b2f4-676bac41f2d8 | -11.7099 | -49.04621 | 2026-10-08 16:18:00 | NPP-375 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7681f64a-8122-3c99-92c2-7d924971045e | -11.20803 | -49.42252 | 2026-10-08 16:18:00 | NPP-375 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| b9ecc8d7-555d-3a0d-9c1d-6616ec5d207e | -8.64957 | -37.10023 | 2026-10-08 16:18:00 | NPP-375 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 12e85423-b54a-3bca-b027-613204111e53 | -9.84377 | -47.85757 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 21.1 |
| e8cd5335-7bab-34bd-923e-073c2d173690 | -10.30507 | -42.38029 | 2026-10-08 16:18:00 | NPP-375 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 36.7 |
| 7817ffea-041b-3ece-b334-2aba46591992 | -11.85424 | -43.56815 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 573e44ed-62c2-3da6-95e1-922530d83a11 | -9.35779 | -46.57921 | 2026-10-08 16:18:00 | NPP-375 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 8fea45f9-37a4-352c-8dd4-28c33b7b886a | -9.80792 | -44.77517 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 49d45d05-2470-32ee-9241-015a6b4a3812 | -11.7727 | -47.73831 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e36ae000-69ae-3ac2-9629-6c2be9f30a08 | -10.81738 | -47.34163 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 101ef012-ea4f-3820-a4e0-e84e145b3503 | -9.14073 | -45.82471 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 27.3 |
| 1baf4e6f-2096-313c-befb-e1cb8ef63836 | -11.11185 | -45.69566 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 50619f71-5a53-388d-9f9e-edac0c0464a4 | -9.22824 | -45.65658 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 903e2654-fc4a-351e-ac47-3ea0ec7857d8 | -13.58746 | -39.78174 | 2026-10-08 16:18:00 | NPP-375 | WENCESLAU GUIMARÃES | BAHIA | Brasil | 2933505 | 29 | 33 | nan | nan | nan | Mata Atlântica | 38.4 |
| 5e6fd99e-9c41-3580-854a-af34d7bb8613 | -11.75827 | -44.9493 | 2026-10-08 16:18:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| dbd18384-fa38-37e3-a33b-8fad5efb996f | -9.84796 | -47.85822 | 2026-10-08 16:18:00 | NPP-375 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| d04c4327-f873-33ca-af3e-0ffaf92650b6 | -10.41934 | -47.26733 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| bec1269c-2576-3216-9afb-47a052675bef | -10.92478 | -45.39444 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| f4e39edb-7390-33f7-aad1-94d8204e641b | -11.27487 | -45.20049 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 7d5a87d8-c366-3231-ab07-ba081a7558ff | -11.62256 | -43.70023 | 2026-10-08 16:18:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| dec55eba-e127-33eb-859b-fccf23cb131e | -12.02591 | -43.44771 | 2026-10-08 16:18:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 152.8 |
| b3dd4ec7-c148-3dda-97c9-ffcba9c970eb | -10.16505 | -44.67836 | 2026-10-08 16:18:00 | NPP-375 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 16764043-4c37-3ff3-8f06-a390bbb46a56 | -9.43026 | -41.73912 | 2026-10-08 16:18:00 | NPP-375 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 9d0e3d46-dfc2-373f-a354-c6184954541d | -13.69771 | -49.12761 | 2026-10-08 16:18:00 | NPP-375 | ESTRELA DO NORTE | GOIÁS | Brasil | 5207501 | 52 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 3c7750e1-06cf-3746-8b57-6fa939ca820b | -8.93921 | -45.14992 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 28.9 |
| 8861d635-b05f-350e-a1a9-651f8a37cc96 | -8.95617 | -45.14862 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 32.1 |
| f4b8f774-3e60-3adf-96c4-98cc31ac81de | -10.99063 | -45.40273 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f484bcd5-d6ae-3213-b8f9-536349cdc214 | -12.42143 | -46.442 | 2026-10-08 16:18:00 | NPP-375 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| b5433e54-370a-37f4-beb4-7063730be744 | -12.61787 | -44.54513 | 2026-10-08 16:18:00 | NPP-375 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 41.8 |
| e00bb035-d400-3eb7-9b8c-6037a68e0e70 | -11.30171 | -44.83549 | 2026-10-08 16:18:00 | NPP-375 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 50.1 |
| ac41c4ea-2901-32ef-9dc1-b39f322b4890 | -9.38905 | -47.09045 | 2026-10-08 16:18:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e79c7f90-4bd5-31ec-b5ef-39d6dce01f5d | -12.19215 | -44.8178 | 2026-10-08 16:18:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 40.6 |
| 540e5419-d5e0-3298-8e39-61d940c349b0 | -9.13741 | -45.83509 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 2cb79145-e7bd-3d3c-8dca-dcd8c57cd430 | -10.48209 | -47.2207 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 192201b6-d079-3fba-ad74-f7539fb2ed7c | -10.50742 | -47.29244 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 5f48d42a-0ef1-3939-b91f-2db18fd2010e | -8.76175 | -36.66046 | 2026-10-08 16:18:00 | NPP-375 | CAETÉS | PERNAMBUCO | Brasil | 2603207 | 26 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 6f56722c-76f1-3e06-8ac5-698fb6d527c1 | -13.80904 | -48.41478 | 2026-10-08 16:18:00 | NPP-375 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7f287319-a041-3bd5-a374-d73219804af7 | -13.11869 | -46.35251 | 2026-10-08 16:18:00 | NPP-375 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| a1440f21-9ae8-34a5-bf2f-9de20c750e04 | -8.93538 | -45.15488 | 2026-10-08 16:18:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 4f0907ff-a41f-3340-b1a3-700a2ce0f171 | -9.78662 | -44.78262 | 2026-10-08 16:18:00 | NPP-375 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| c265788c-2556-3495-ae40-0ea730f25373 | -10.94108 | -45.38547 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 27.3 |
| eafa1ea9-7931-355f-8e56-c2ca04e5a49b | -11.39233 | -47.55636 | 2026-10-08 16:18:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2c3da1a9-b879-3746-9126-9355a4307803 | -14.05122 | -43.82533 | 2026-10-08 16:18:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 98.0 |
| 3666483d-370c-3b7b-86c6-3c9629443d05 | -13.95647 | -44.8556 | 2026-10-08 16:18:00 | NPP-375 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| b047dbe9-3afb-3b53-8505-28d38e92b9b6 | -12.83244 | -44.63028 | 2026-10-08 16:18:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 27acf406-0b08-3dc9-9f92-7d445b184dd2 | -8.99359 | -42.33704 | 2026-10-08 16:18:00 | NPP-375 | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 26.2 |
| 7bf78289-3b35-3bee-8b03-dcb5d654adda | -13.69944 | -49.08786 | 2026-10-08 16:18:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| d6c41bab-0af1-3e9a-94d5-3e01ce6424f3 | -11.26838 | -45.18682 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 730b21d6-ed14-3a1c-85d8-2f3305d3a9d2 | -10.90092 | -45.53455 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 5d932c4a-1f46-3b40-b2e2-6140a0f92313 | -10.51594 | -47.31929 | 2026-10-08 16:18:00 | NPP-375 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 57b4aae0-c91e-3ec2-aeb9-5c9701f2d9da | -10.74552 | -48.54205 | 2026-10-08 16:18:00 | NPP-375 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 42163af9-f716-300f-9a24-0ce9857becfc | -7.64999 | -37.66921 | 2026-10-08 16:18:00 | NPP-375 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 1408d04c-c751-35c8-a7b0-0c8c03e38dcd | -11.24642 | -46.26926 | 2026-10-08 16:18:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 18b7d799-d57c-364b-b080-800eb5e215ae | -8.5912 | -45.69292 | 2026-10-08 16:18:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |


[Clique aqui para ver as próximas entradas](README273.md)
