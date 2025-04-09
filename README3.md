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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b4f823c-7ddb-3158-a374-87adf7ff5255 | -13.93308 | -43.28165 | 2025-04-09 04:27:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 421f7536-ce4a-32dd-a3f1-661fbe949ae5 | -20.41604 | -43.55333 | 2025-04-09 04:29:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| cf53463d-76c8-351a-a1b9-768d4166a60a | -19.89616 | -48.35713 | 2025-04-09 04:29:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7effb27a-ba4a-38bb-b2e0-94d4ee529008 | -21.98551 | -46.8228 | 2025-04-09 04:29:00 | NPP-375D | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d4b531b0-8f84-3d60-a64d-4df09e2211df | -22.67309 | -42.85456 | 2025-04-09 04:29:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 37d778b6-fcd5-309e-961e-8a9b6ece1de9 | -17.60308 | -46.70256 | 2025-04-09 04:29:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25175631-c15c-3931-8d92-6ea4aeb1caae | -17.4826 | -48.98221 | 2025-04-09 04:29:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b901406-ceec-3ff4-b416-cc13815240bf | -20.32697 | -47.54942 | 2025-04-09 04:29:00 | NPP-375D | JERIQUARA | SÃO PAULO | Brasil | 3525409 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d8469c7f-27bd-319f-847a-56a950d8ac55 | -17.45453 | -48.17163 | 2025-04-09 04:29:00 | NPP-375D | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2738eb85-d393-3e53-bf5a-5b2c8bc7788d | -18.39224 | -50.52398 | 2025-04-09 04:29:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b3bf31ff-72aa-3dfc-818a-294a521a5d64 | -22.67765 | -42.85513 | 2025-04-09 04:29:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 81491b1c-cffa-33a3-aef8-b3bcc756125e | -17.86355 | -44.56734 | 2025-04-09 04:29:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 476625d4-fd78-3980-9d44-c47e14e4f759 | -17.25565 | -48.6 | 2025-04-09 04:29:00 | NPP-375D | SANTA CRUZ DE GOIÁS | GOIÁS | Brasil | 5219209 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d76a6120-adff-3285-af24-7c6114637fd0 | -21.98413 | -46.82018 | 2025-04-09 04:29:00 | NPP-375D | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba5c32f8-ae9c-38d3-bb4f-f538c4b68fe2 | -22.67821 | -42.8502 | 2025-04-09 04:29:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| e7b33d6a-f81b-3e26-8dc4-1507c5e8d95e | -18.38886 | -50.52335 | 2025-04-09 04:29:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 092c1feb-45f1-3f76-af2e-c5574477df3d | -19.89281 | -48.35655 | 2025-04-09 04:29:00 | NPP-375D | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 79b94eab-094c-3129-80fe-c8d959ab23ce | -17.60653 | -46.70312 | 2025-04-09 04:29:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4830e8ab-7f52-39e6-8cea-9ca3ef59375e | -23.8173 | -51.65834 | 2025-04-09 04:32:00 | NPP-375D | KALORÉ | PARANÁ | Brasil | 4113106 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c4844966-53f7-3a51-b73b-b200bcd8b5a6 | -21.68371 | -52.98238 | 2025-04-09 04:32:00 | NPP-375D | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 176f7c3d-056a-30f8-8f7d-3ed3f2954ef6 | -23.81665 | -51.66223 | 2025-04-09 04:32:00 | NPP-375D | KALORÉ | PARANÁ | Brasil | 4113106 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a6d805ca-4a6c-3e86-aa73-086c4d9120ce | -23.40477 | -46.55719 | 2025-04-09 04:32:00 | NPP-375D | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 7bef0e6c-6c34-3fb8-befd-5d62b60e0ba4 | -23.43127 | -52.02335 | 2025-04-09 04:32:00 | NPP-375D | MARINGÁ | PARANÁ | Brasil | 4115200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 60730cdf-b319-310c-9092-fdc179147659 | -22.90159 | -43.7551 | 2025-04-09 04:32:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a9df522e-8630-30d7-b8d1-709c0a16737a | -21.39184 | -56.15055 | 2025-04-09 04:32:00 | NPP-375D | GUIA LOPES DA LAGUNA | MATO GROSSO DO SUL | Brasil | 5004106 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4cefbc2b-925e-3cb3-9861-7d6f6ddc3f35 | -22.95979 | -49.87235 | 2025-04-09 04:32:00 | NPP-375D | OURINHOS | SÃO PAULO | Brasil | 3534708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| baac66ff-d810-3484-b173-1738574ac660 | -6.01343 | -43.84882 | 2025-04-09 04:46:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ce29aa8-cc23-3a68-a60f-40726e40ffe9 | -2.53221 | -53.95699 | 2025-04-09 04:46:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a6bd2746-2d7a-3e3a-bdac-cbcb2bf7a38e | -6.01301 | -43.85182 | 2025-04-09 04:46:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ce56f8fe-f937-3c80-a97c-fb897962a9c6 | -7.07397 | -44.37421 | 2025-04-09 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4655eb27-b1f5-3a00-8498-95302859ab15 | -7.0744 | -44.37121 | 2025-04-09 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20d611da-516d-3610-8192-8d1eec81c662 | -11.2106 | -48.84779 | 2025-04-09 04:49:00 | NOAA-20 | CRIXÁS DO TOCANTINS | TOCANTINS | Brasil | 1706258 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f99406a6-64e3-363f-b4d5-adf8e0569964 | -7.07312 | -44.38023 | 2025-04-09 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf6a2c45-2a78-35c6-baa8-b28cae6fd500 | -10.72566 | -42.32017 | 2025-04-09 04:49:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| dbdd2ad8-15fe-3771-a564-2cb6c24503df | -6.71682 | -47.60725 | 2025-04-09 04:49:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 359e947a-26a3-33ae-8004-ebaa62938b04 | -7.06811 | -44.37953 | 2025-04-09 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b668fa4-18f0-3cfd-ab8d-2da0d67b5691 | -7.06854 | -44.37651 | 2025-04-09 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e39e3e9-7dd3-3c3d-a151-6228658f6e6b | -13.01841 | -45.06816 | 2025-04-09 04:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 69ba91b3-a0d3-37e3-8b30-49b7d01e5633 | -13.01803 | -45.07138 | 2025-04-09 04:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d19e7aad-c282-3625-ba61-c475b662e1c2 | -10.71961 | -42.31943 | 2025-04-09 04:49:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 0734335d-8b86-3c40-88d5-19ab14dd219c | -10.72621 | -42.3156 | 2025-04-09 04:49:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a9493267-ec5c-3e90-b240-12aa1176a532 | -9.81517 | -48.04405 | 2025-04-09 04:49:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f7e0090-c30b-3191-9ed8-61ea9aad148b | -8.85895 | -49.88739 | 2025-04-09 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9a801a63-7f69-338a-abba-4903e9b74e87 | -7.06939 | -44.37047 | 2025-04-09 04:49:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 607c5cff-6908-3901-95b6-9395653e2cac | -13.02323 | -45.07204 | 2025-04-09 04:49:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63ba9e0a-85cd-39a5-9e17-6c497fa5e71d | -10.54246 | -44.66914 | 2025-04-09 04:49:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9db320df-549e-3d5f-9af6-ddfe530b37b4 | -6.59023 | -44.78872 | 2025-04-09 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| abadb54d-e6cc-3e8a-855d-ce5a2966c5e5 | -10.54206 | -44.67229 | 2025-04-09 04:49:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 84d1e6d1-e93d-3f43-9722-4cbfae6621da | -8.10956 | -43.12311 | 2025-04-09 04:49:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 190537a7-4f5e-394b-bc62-1f1ac5e47047 | -15.07996 | -48.94508 | 2025-04-09 04:51:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5dd31c74-a011-3155-95a3-f529b13dc9f9 | -14.72806 | -59.86517 | 2025-04-09 04:51:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f5beae7-2977-35e1-8633-fa7813d64ec9 | -17.60645 | -46.70474 | 2025-04-09 04:51:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd2f75ec-1f28-3f7d-989b-98b3a1d5eba8 | -17.45263 | -48.16942 | 2025-04-09 04:51:00 | NOAA-20 | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d16916d6-3d6f-30f4-9318-7f434623c394 | -15.07724 | -48.94496 | 2025-04-09 04:51:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8dec5c46-560a-3482-9621-481c6a2a2e85 | -18.39178 | -50.52425 | 2025-04-09 04:51:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18a33304-b509-306b-9941-17d6f9395595 | -19.4046 | -56.57378 | 2025-04-09 04:51:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 3a4f0f4d-9229-3a32-814c-bb6fe25c28ed | -19.76813 | -49.38357 | 2025-04-09 04:51:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 04e91990-9c20-30e3-90f2-12faef7d023e | -24.2442 | -50.73853 | 2025-04-09 04:53:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d6109e89-7ab2-3cbd-bdf3-6db90e92076b | -23.81509 | -51.66051 | 2025-04-09 04:53:00 | NOAA-20 | KALORÉ | PARANÁ | Brasil | 4113106 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 432d0f24-361e-30d8-90eb-16f0df35a0b0 | -25.59097 | -50.42779 | 2025-04-09 04:53:00 | NOAA-20 | FERNANDES PINHEIRO | PARANÁ | Brasil | 4107736 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0b7edd18-8dff-3269-90f9-29eb20c7b8b9 | -21.68284 | -52.98152 | 2025-04-09 04:53:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 215b7336-53c6-3131-a29c-72d13ebc1317 | -22.19714 | -55.72197 | 2025-04-09 04:53:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f2257a83-7dc5-3b2f-8a02-45e6ccd039b2 | -10.72266 | -42.30846 | 2025-04-09 04:59:00 | AQUA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 7293337a-d6f3-388b-a414-d2acfc3279af | -9.78037 | -36.85087 | 2025-04-09 11:34:00 | TERRA_M-M | GIRAU DO PONCIANO | ALAGOAS | Brasil | 2702900 | 27 | 33 | nan | nan | nan | Caatinga | 21.0 |


