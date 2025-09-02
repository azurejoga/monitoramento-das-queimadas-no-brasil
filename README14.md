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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2bc8c59-969c-306a-8639-98de9e12d2bb | -22.9545 | -49.74121 | 2025-09-02 03:28:00 | NOAA-21 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| e49e3b81-ebf9-3bf2-8c63-140e9d4dd89c | -18.04729 | -47.74644 | 2025-09-02 03:28:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f8bc92c3-a27e-3d6b-b01e-82a17072d065 | -17.61339 | -46.64426 | 2025-09-02 03:28:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c3080fe7-ab25-3346-aac3-a14e51da3970 | -18.36863 | -46.02548 | 2025-09-02 03:28:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 277a1b8c-492f-3bf3-b1a2-13cbdacbc00b | -18.36631 | -46.02591 | 2025-09-02 03:28:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 98a33bb9-0f89-3078-8237-44783d5cb9c6 | -17.88815 | -47.16922 | 2025-09-02 03:28:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b8a8dd85-97ef-38a6-b566-30caa9867eb5 | -17.88765 | -47.16766 | 2025-09-02 03:28:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| acb964b5-738e-38d7-a2ed-f8a853795ec9 | -19.41939 | -43.79097 | 2025-09-02 03:28:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 42c92117-6faf-3cdd-87d9-64f33124eda4 | -20.11566 | -46.0136 | 2025-09-02 03:28:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d9ed200-3d50-36d5-a454-ae9e190dec5d | -22.5274 | -46.81643 | 2025-09-02 03:28:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 9961eaea-83b4-3d97-be59-6dd581985893 | -23.93389 | -48.85243 | 2025-09-02 03:28:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d614d591-fefd-3861-9cc7-b23c58e8be4d | -17.70536 | -46.89668 | 2025-09-02 03:28:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 25.9 |
| c3f42bbb-eaee-3d04-b275-0d63f626d644 | -18.54874 | -47.46085 | 2025-09-02 03:28:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9cb4a37-4f3f-3714-a635-12ece9a8055d | -18.06909 | -45.95842 | 2025-09-02 03:28:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 346232d9-2c82-31af-98c2-f3d13f7a0f35 | -22.52129 | -46.81496 | 2025-09-02 03:28:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d5d44fd7-13ba-36a7-8ff0-5a8e9d2b25cf | -18.59243 | -44.5153 | 2025-09-02 03:28:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f15dee22-3113-38ea-9ad5-36f512005a03 | -19.41855 | -43.79488 | 2025-09-02 03:28:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6390dc35-fef8-39dc-bcfe-712a1f14eb84 | -22.39908 | -47.18659 | 2025-09-02 03:28:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| e4eadfd6-dd58-39ef-acf9-fcb2777f8d71 | -18.04892 | -47.7396 | 2025-09-02 03:28:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bbd6575d-a828-355f-8067-157cc2ce9ea3 | -18.07259 | -45.95257 | 2025-09-02 03:28:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f0b0a63d-262e-3226-b0e7-3c3a08ff5002 | -20.11533 | -46.01263 | 2025-09-02 03:28:00 | NOAA-21 | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 625f5b04-e952-3606-b898-98a955255a8b | -22.40033 | -47.18144 | 2025-09-02 03:28:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 762f1f0f-d70c-344a-af7e-ad0cbe32fed3 | -22.52973 | -46.80663 | 2025-09-02 03:28:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 9a268293-3520-3dfc-b416-030d8a9b56cc | -17.89339 | -47.17725 | 2025-09-02 03:28:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 30d19595-dabf-3ef4-8f25-2295ee4635c6 | -19.82175 | -45.00414 | 2025-09-02 03:28:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e7200923-810c-341c-a20f-05cee9c80831 | -22.10475 | -46.96594 | 2025-09-02 03:28:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 105a662d-9497-3f7d-a46a-4f4655dabcf8 | -19.81629 | -45.00453 | 2025-09-02 03:28:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 73ade26f-639b-3c1c-a661-047c50905cf6 | -18.5472 | -47.46732 | 2025-09-02 03:28:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 131905e6-f9d1-341a-a257-8b9e726b0b4e | -22.3929 | -47.18483 | 2025-09-02 03:28:00 | NOAA-21 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e1e9f6e7-95f6-3f8d-afc6-fd478c64e3dd | -23.34829 | -47.14742 | 2025-09-02 03:28:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 6f4a1aad-b2ac-3094-9a0d-791208da5e6c | -17.88981 | -47.16228 | 2025-09-02 03:28:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4fe7a971-f465-39b8-8a0c-2e98b8346833 | -18.07024 | -45.95328 | 2025-09-02 03:28:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 55a964ec-21e8-3f5d-8f1d-90b57b544aa7 | -17.8929 | -47.17586 | 2025-09-02 03:28:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 17.7 |
| eafc2b4e-8a68-3312-bdf5-f38211920272 | -22.52248 | -46.81 | 2025-09-02 03:28:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 9997a99f-a0c4-3f47-af76-d29fe782bbf4 | -23.93894 | -48.84783 | 2025-09-02 03:28:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f6423ee4-6b5e-3b88-9385-54ae4605fc45 | -23.9355 | -48.84605 | 2025-09-02 03:28:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7bdea404-dbbf-3efd-a162-1dc7bd3054a1 | -22.67634 | -47.29919 | 2025-09-02 03:28:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 04ba353c-3a38-3828-8255-239934263b65 | -22.53087 | -46.80183 | 2025-09-02 03:28:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 6e9792e3-0f9f-3d28-bc92-49e617882379 | -17.61626 | -46.64658 | 2025-09-02 03:28:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9ed89bef-6fd0-3656-b3d9-abcd7e94a738 | -17.60966 | -46.64492 | 2025-09-02 03:28:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b0ec602-1bf5-3d3b-adba-1eadc7867bdb | -23.9324 | -48.84586 | 2025-09-02 03:28:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 48d17efd-e1ef-3522-8945-e8a8d0a8cdcb | -17.89441 | -47.16932 | 2025-09-02 03:28:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 6ff94e90-7f43-3208-99c3-21450fc3425c | -18.07141 | -45.95768 | 2025-09-02 03:28:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b470047a-5877-323c-813b-e0b572731f1a | -19.82076 | -45.00853 | 2025-09-02 03:28:00 | NOAA-21 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| aec62989-b766-3d80-9672-6ddb804449db | -18.37266 | -46.02725 | 2025-09-02 03:28:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7bc2db1b-5ca4-3241-a4f7-807350aacb37 | -19.41312 | -43.79368 | 2025-09-02 03:28:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6fa303eb-3a25-3426-a3c1-2f77735b6e9a | -18.07653 | -45.9549 | 2025-09-02 03:28:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f530817-5368-3a69-945d-1196fd076eb6 | -18.59338 | -44.51095 | 2025-09-02 03:28:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3cc9a012-09f7-3e17-9b08-ff6bdd9ed40b | -22.52368 | -46.80497 | 2025-09-02 03:28:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| d28ae241-e1c6-3cd2-93cd-f6589928a3ed | -17.89493 | -47.17083 | 2025-09-02 03:28:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| b6db3e4c-1087-3f32-97a8-acee47814ff7 | -18.07022 | -45.96286 | 2025-09-02 03:28:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 59af01d2-4633-3606-a06e-b60408da3852 | -22.11086 | -46.96783 | 2025-09-02 03:28:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1d5b56ae-acb2-35f5-9a49-d7d4b14f569f | -22.52857 | -46.8115 | 2025-09-02 03:28:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| be43baf5-fa1b-3999-bee5-d1d1d1962422 | -22.52484 | -46.80012 | 2025-09-02 03:28:00 | NOAA-21 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 18347cf4-fc06-374b-8d17-e41c0795592f | -19.41394 | -43.7898 | 2025-09-02 03:28:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e0a7b3c7-f52c-323c-8345-be4d4f657513 | -17.70688 | -46.89012 | 2025-09-02 03:28:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 9120efeb-18ad-311e-ad55-302acc58628b | -13.6918 | -46.9439 | 2025-09-02 03:30:00 | GOES-19 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 74.4 |
| d8697dbb-aa1e-342c-8843-495d42c62e05 | -12.611 | -48.1784 | 2025-09-02 03:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 41043c40-612e-3ed3-a692-30799efd363e | -6.7909 | -52.8165 | 2025-09-02 03:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 5c1e57a7-34b9-3934-8765-a7ebd403c792 | -6.8095 | -52.8154 | 2025-09-02 03:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| b45728f2-9142-3a94-b2bc-e22d9b722931 | -15.5671 | -48.3244 | 2025-09-02 03:30:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 1de08c46-4fae-32ca-9a9b-9f8028dcd021 | -12.6302 | -48.1757 | 2025-09-02 03:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 7f306ca2-38be-3449-86a5-11c1b988c0a8 | -11.6647 | -57.3533 | 2025-09-02 03:30:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 67.7 |
| cbb7907d-2f43-385f-b5e9-b478a1b8bb6d | -7.5476 | -61.3437 | 2025-09-02 03:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 47e3ecd1-6d98-33d3-ac38-adf0ab9e502b | -9.1207 | -61.4864 | 2025-09-02 03:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 9c624582-210f-3eaa-ac22-1b99efa9a980 | -17.9016 | -47.1569 | 2025-09-02 03:30:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 55.5 |
| 8ecd50f7-63bf-3dc2-bf2b-1e26336be2c7 | -3.2305 | -47.135 | 2025-09-02 03:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 084d3700-8816-31e2-a1df-5fb18f1a3691 | -7.5477 | -61.3247 | 2025-09-02 03:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| a3647cfa-7842-3d67-9b97-8e899b586c1c | -17.9016 | -47.1569 | 2025-09-02 03:40:00 | GOES-19 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 03a7b379-ffd3-3c83-8be0-e14987b754ea | -15.5661 | -48.3694 | 2025-09-02 03:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 87eec723-6b61-31cf-b65c-0ebf5beefa10 | -7.5476 | -61.3437 | 2025-09-02 03:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| efd46108-d8b1-3a16-9a1e-0a33d0445cd5 | -3.2305 | -47.135 | 2025-09-02 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 71b0c6a2-7e31-3450-b412-42ca4b761bd1 | -6.8095 | -52.8154 | 2025-09-02 03:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 460be1eb-b850-376e-a0d6-b9e485c1a935 | -6.7909 | -52.8165 | 2025-09-02 03:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| bdb52bc8-a0f5-3e0f-8053-f42ccfbad0b8 | -6.8914 | -45.8313 | 2025-09-02 03:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 1b30becd-a139-3afb-a91e-807e867217b7 | -7.5477 | -61.3247 | 2025-09-02 03:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| cd2d3a70-bbd3-3cef-8dc1-1e8ac8259394 | -14.2034 | -51.6558 | 2025-09-02 03:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 67.3 |
| c830ad01-302f-37e2-828a-2c128e521523 | -9.1207 | -61.4864 | 2025-09-02 03:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 5ceb553f-06c8-32c8-b56b-0ab90a7a6949 | -15.5671 | -48.3244 | 2025-09-02 03:40:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 4b87a581-acc7-3f53-aff5-2ac5694da0b0 | -6.8911 | -45.8538 | 2025-09-02 03:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| afc0d160-03d0-3e79-bb73-a16de0f7b673 | -11.6647 | -57.3533 | 2025-09-02 03:40:00 | GOES-19 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 8357c6dc-d7b7-3474-8d5d-d36196dfebb9 | -6.3383 | -43.52143 | 2025-09-02 03:49:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1844ba47-026a-35a2-aa27-9051c306c39d | -6.97889 | -44.30661 | 2025-09-02 03:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| abfd644c-c9f8-3c06-9106-92987e48a197 | -4.21972 | -47.21118 | 2025-09-02 03:49:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7f0e8998-c2fa-3581-a57e-2d0eb569dde0 | -7.30677 | -44.28056 | 2025-09-02 03:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d9fab9ba-fac0-36a5-b7e2-f1d04f7efea1 | -5.50955 | -42.64253 | 2025-09-02 03:49:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 5.8 |
| 1602ed20-a5cf-313f-9567-1e644fdf1fdc | -6.7234 | -42.25163 | 2025-09-02 03:49:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6fb100c3-7aa4-37a6-b7ad-4758ae0447a0 | -7.67497 | -43.87304 | 2025-09-02 03:49:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c88def2d-4c40-3f91-b41a-1fdc27bcf650 | -7.59832 | -37.80309 | 2025-09-02 03:49:00 | NPP-375D | JURU | PARAÍBA | Brasil | 2508000 | 25 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ccba443b-ddfd-35cd-a377-1564f792425e | -5.68833 | -45.95333 | 2025-09-02 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ac5fd68e-86a2-31b8-ae8d-83056437ec88 | -5.36969 | -42.62114 | 2025-09-02 03:49:00 | NPP-375D | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f6d8eed4-40f8-38f7-8919-3b9145d900ca | -6.27341 | -43.29144 | 2025-09-02 03:49:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 061e769e-fc22-3d54-a6f5-443a6b81091b | -6.22443 | -43.36152 | 2025-09-02 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 62bd742c-3fab-387b-a42d-6333a2c7eead | -7.61876 | -44.03405 | 2025-09-02 03:49:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb512e28-6a9c-30e6-96f1-1ec61682590d | -5.69921 | -45.95531 | 2025-09-02 03:49:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4be4ed41-9a65-3ad7-8ed2-348d680d39a9 | -4.31143 | -48.08655 | 2025-09-02 03:49:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5874a058-a526-3e20-a37b-b43743124cfb | -6.24143 | -41.80299 | 2025-09-02 03:49:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| cfc8a910-db65-3e34-a4d8-af0f051d75e3 | -6.81692 | -43.3322 | 2025-09-02 03:49:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| e766f38c-b551-3abb-a7a1-88d4cb7a7f18 | -5.50081 | -42.64113 | 2025-09-02 03:49:00 | NPP-375D | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| fadfba0a-02f4-32e1-8853-1e4ff72a4e6b | -5.26063 | -37.90086 | 2025-09-02 03:49:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |


[Clique aqui para ver as próximas entradas](README15.md)
