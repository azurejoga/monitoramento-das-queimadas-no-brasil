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
| ea760ac7-278d-37df-b6c6-108381782f47 | -13.39303 | -48.0872 | 2024-10-05 04:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 550a3d4d-07e2-3c03-a886-f82aea597fe9 | -13.33851 | -49.3301 | 2024-10-05 04:14:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b4e3dfb7-e357-3f18-ab42-01cc6a7bf4e3 | -13.33461 | -49.32914 | 2024-10-05 04:14:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3053e45e-3f34-3eff-a758-b90a2efda13c | -13.33241 | -49.31869 | 2024-10-05 04:14:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 27b6c3f3-da96-31b8-9be7-0db35f85197d | -13.30168 | -49.31504 | 2024-10-05 04:14:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 62fffdd3-2abf-3379-905b-7ca196107d94 | -13.29303 | -47.92578 | 2024-10-05 04:14:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85fb1537-fd4a-3595-8dc7-e1c136216012 | -13.21856 | -48.54077 | 2024-10-05 04:14:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3377e3e5-f13f-3046-8e7b-87a1d836fec5 | -13.21344 | -48.66219 | 2024-10-05 04:14:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e1811fb2-db8f-3601-9934-4b70b7f73da2 | -7.40689 | -44.65626 | 2024-10-05 04:14:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 76ea895b-fd73-3eeb-b4e5-6b0aec169246 | -10.15359 | -36.22099 | 2024-10-05 04:14:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| 0022ea0b-a449-3a94-b361-a60ab8c08a78 | -10.15252 | -36.22223 | 2024-10-05 04:14:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| d381c0cc-7206-367c-9fbf-30a690707970 | -10.14877 | -36.22036 | 2024-10-05 04:14:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 537ceaaa-cad4-3bda-8334-b179cfe6c4b7 | -15.27295 | -40.32588 | 2024-10-05 04:14:00 | NPP-375D | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ee24e55d-fdfc-3a37-b79c-b82915b0a9bd | -15.27201 | -40.32175 | 2024-10-05 04:14:00 | NPP-375D | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| afb0f543-959d-3b76-b37a-bdcd12b832e1 | -12.25388 | -45.59975 | 2024-10-05 04:14:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 624743ea-6fd9-306e-ba5c-59f4b05fc55a | -12.11127 | -45.20556 | 2024-10-05 04:14:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f90a9351-91b0-3c1d-83fb-f8ca7c82c238 | -11.42583 | -47.19392 | 2024-10-05 04:14:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6e4601a4-287b-3184-9814-2bbd23f7fe40 | -13.10319 | -46.34415 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b093a67f-43a8-3457-916e-e1939743f6ae | -13.10128 | -46.35569 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f34d8e83-1d52-3c43-b056-10b48dd20972 | -13.10066 | -46.35947 | 2024-10-05 04:14:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fe5f2804-e8a5-3fe9-9acd-7d8a930d44c4 | -9.25333 | -43.51534 | 2024-10-05 04:14:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 00055a99-518a-3758-a666-85e9adc55357 | -9.25056 | -43.51131 | 2024-10-05 04:14:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ea543a2e-a0f8-36da-81f5-051ec400cbe2 | -9.25001 | -43.51481 | 2024-10-05 04:14:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| abe2397b-e628-331b-bd2b-be6e0a4125ae | -9.24501 | -43.50327 | 2024-10-05 04:14:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 94d27c71-4da1-3b47-a3aa-00935c02320a | -9.24446 | -43.50676 | 2024-10-05 04:14:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 52611f87-2e42-356e-90df-32f1b74c4b1a | -9.24114 | -43.50623 | 2024-10-05 04:14:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0bfce9fa-7b6d-3437-a009-f15893f91aaf | -9.23724 | -43.48772 | 2024-10-05 04:14:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 275612db-3432-3e90-b68f-11699e7351e3 | -8.18682 | -43.73532 | 2024-10-05 04:14:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0d46b1c3-caab-32cd-a4b7-15c95c8d5aea | -8.1835 | -43.73479 | 2024-10-05 04:14:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d6be00e0-0874-3a96-9214-12d982718920 | -8.17861 | -43.7264 | 2024-10-05 04:14:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b4a08737-635c-32e0-942a-b44b27c09104 | -8.17584 | -43.72238 | 2024-10-05 04:14:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e6c7bb71-9f36-3f6d-bfab-7a3756c10d8c | -8.17528 | -43.72587 | 2024-10-05 04:14:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3e363071-7903-321e-8f37-4b8420035eda | -7.62822 | -43.69981 | 2024-10-05 04:14:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7d4e68ad-d59f-33eb-afd8-5ec085b8b770 | -9.54665 | -36.93412 | 2024-10-05 04:14:00 | NPP-375D | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c0e4f54c-f007-36e3-975c-9a4e46638601 | -9.49866 | -40.36862 | 2024-10-05 04:14:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 042cb270-e554-3a9b-96d9-7f9938c169c2 | -8.97811 | -40.84735 | 2024-10-05 04:14:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.4 |
| af8d8a0d-6483-30db-9d14-2071a9513c00 | -8.96228 | -40.57506 | 2024-10-05 04:14:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9393bf76-4cac-3191-8693-19117f6f6ddb | -8.9329 | -42.59637 | 2024-10-05 04:14:00 | NPP-375D | SÃO RAIMUNDO NONATO | PIAUÍ | Brasil | 2210607 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| f0b06c9c-6a4a-30b9-bf29-7667b29a47a0 | -8.72223 | -41.58379 | 2024-10-05 04:14:00 | NPP-375D | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 718ce862-e77e-3016-9608-ddf1b5439096 | -8.71879 | -41.58326 | 2024-10-05 04:14:00 | NPP-375D | LAGOA DO BARRO DO PIAUÍ | PIAUÍ | Brasil | 2205565 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 206b8cb7-72b3-39ca-8bb7-864aee6ea441 | -8.3333 | -41.16178 | 2024-10-05 04:14:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 47b992e1-b2b0-3ca4-9d68-4dd5ef7d076a | -8.32983 | -41.16118 | 2024-10-05 04:14:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 67468231-972f-3c59-9018-6ceb5f838b5d | -8.29897 | -42.83004 | 2024-10-05 04:14:00 | NPP-375D | BREJO DO PIAUÍ | PIAUÍ | Brasil | 2201988 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 125ac0c0-832f-3f9c-9c99-cd601a7733a0 | -8.15435 | -41.34961 | 2024-10-05 04:14:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 91135dc3-3243-3553-ba79-5b4dcd9efdcd | -8.09415 | -41.21994 | 2024-10-05 04:14:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d026567e-eb8c-318c-b012-4bb6ca2cbea9 | -8.0594 | -40.95163 | 2024-10-05 04:14:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6e7aef45-66db-30a1-b065-a17d45ed9ddc | -7.94439 | -42.46091 | 2024-10-05 04:14:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7617fc03-52b6-3c5a-ba53-d5e88592bbd2 | -7.94104 | -42.46039 | 2024-10-05 04:14:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e228c734-8184-3094-9fb9-92e19be4a078 | -7.9377 | -42.45987 | 2024-10-05 04:14:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5cf1a757-1833-32e5-95c4-f563ceabc842 | -7.93435 | -42.45935 | 2024-10-05 04:14:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5e045805-3b34-3eea-b174-dd919ce6a27a | -7.90356 | -41.14555 | 2024-10-05 04:14:00 | NPP-375D | JACOBINA DO PIAUÍ | PIAUÍ | Brasil | 2205151 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 24c3629f-0c25-300d-991b-17d7ea7d1b11 | -7.66214 | -42.83789 | 2024-10-05 04:14:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2ce6058c-8a28-3e3a-b2a2-f6b826ca3339 | -7.66167 | -42.42438 | 2024-10-05 04:14:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c566ffb8-ba40-35f2-9ff3-706eef33cbf3 | -7.66063 | -42.45318 | 2024-10-05 04:14:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d5a8506c-dc70-3c03-987c-219a128d3fb1 | -7.65729 | -42.45265 | 2024-10-05 04:14:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3aa30f8e-bc1e-358f-bcfb-4ef7381ab5fe | -7.65497 | -42.42333 | 2024-10-05 04:14:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| bbf94493-09ed-33d2-bb27-82dd7e6324e5 | -7.65163 | -42.42281 | 2024-10-05 04:14:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3889ec36-0bd4-3343-a7d2-5e37043ecfb3 | -7.64828 | -42.4223 | 2024-10-05 04:14:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8cd59290-5e78-3c13-aad2-0a800f1d3f61 | -7.64548 | -42.41823 | 2024-10-05 04:14:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8d28de71-9d5d-39d6-a8c8-07b843fe5c2b | -7.64159 | -42.42126 | 2024-10-05 04:14:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| da0b0d5f-fdb1-3637-bc40-5c0dbdec1fb9 | -7.63824 | -42.42075 | 2024-10-05 04:14:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 30515288-2df6-3b67-a25a-a9f27f7c24a1 | -7.63565 | -42.48176 | 2024-10-05 04:14:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 835ec8b0-3bd7-337d-b199-cf72b1b5258f | -7.63176 | -42.48476 | 2024-10-05 04:14:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5d41f34a-c365-3a77-8254-6bdb10678cec | -7.63046 | -42.42675 | 2024-10-05 04:14:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2ee60733-683c-35bf-b967-c671a2ea9804 | -7.6287 | -42.42678 | 2024-10-05 04:14:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 0b1b867a-95cf-3132-b7dc-dcd315e1135a | -7.62842 | -42.48423 | 2024-10-05 04:14:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5e72cb6e-8aee-397f-b3d6-7635ac3c5557 | -15.09071 | -43.13313 | 2024-10-05 04:14:00 | NPP-375D | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 21479139-3e62-346d-b315-82a06f5bfe7c | -14.32404 | -42.34867 | 2024-10-05 04:14:00 | NPP-375D | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ca9bec87-6d60-368c-94ea-341f33b51f07 | -14.1347 | -41.69366 | 2024-10-05 04:14:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 59fd84b5-63cc-3901-87c9-ca8783276900 | -14.11857 | -41.6775 | 2024-10-05 04:14:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f5717ef4-0aa8-3a17-abef-8ce25b64da99 | -14.0361 | -41.70518 | 2024-10-05 04:14:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d930966a-6735-39f8-9140-756aca38a399 | -13.97738 | -42.50014 | 2024-10-05 04:14:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 071cfd98-4529-38df-bc4e-1f10889c8530 | -13.53615 | -42.03143 | 2024-10-05 04:14:00 | NPP-375D | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f69e0fd7-a07e-3c52-a596-f8a83945bd67 | -13.5332 | -42.02695 | 2024-10-05 04:14:00 | NPP-375D | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9b7ff703-c29d-3974-b541-41577edcc66c | -13.53262 | -42.03093 | 2024-10-05 04:14:00 | NPP-375D | ÉRICO CARDOSO | BAHIA | Brasil | 2900504 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 37fac0df-f7f2-3d30-adcf-cc4d8fffe3d9 | -12.67835 | -43.12028 | 2024-10-05 04:14:00 | NPP-375D | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 0c761fc2-57aa-3425-af6f-0646e614ee45 | -11.83241 | -42.7469 | 2024-10-05 04:14:00 | NPP-375D | IPUPIARA | BAHIA | Brasil | 2914109 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 705355c8-70eb-3213-8f41-9e043b0ec98a | -11.7585 | -42.93003 | 2024-10-05 04:14:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 66a43a15-1fa7-3d05-a5b6-fdf2829455c3 | -11.75512 | -42.9295 | 2024-10-05 04:14:00 | NPP-375D | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 17472398-207b-3c8b-a12c-b2561f4147dd | -11.56483 | -42.18232 | 2024-10-05 04:14:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6e56e2d3-f267-3bdd-90de-4d7492182d3e | -11.24156 | -41.64193 | 2024-10-05 04:14:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 62b329a6-a9a8-3e26-9527-f065a68b5131 | -11.21691 | -43.32426 | 2024-10-05 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 7ef2c585-e3e1-31da-8abb-9b500a9fe3d4 | -11.21357 | -43.32372 | 2024-10-05 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 25a53c77-ea59-33d1-9676-cb23b07003d2 | -11.11046 | -43.33675 | 2024-10-05 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5e2bc6ad-287c-33b4-9122-d1ad386d4cfe | -11.10991 | -43.34031 | 2024-10-05 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5c60f4f8-8985-3c87-ac8f-60576a64a7a2 | -7.79915 | -43.10579 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 89cd2f5c-7878-3663-9ab0-1a67c542f7f4 | -7.79861 | -43.10926 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 41fbf3bb-c8e5-3d81-9026-fe86e8bf4e7b | -7.79806 | -43.11275 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 4f3b0696-f041-3fe8-8566-4002f486266d | -7.79751 | -43.11623 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0eb18693-267d-31f2-9ca0-0c0b7ed66ba4 | -7.79583 | -43.10526 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| f1fbaf5e-0702-36c0-bb9d-792cfc69786f | -7.79528 | -43.10874 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 519cc6f8-45e8-3db5-8954-fc0b6747630c | -7.79474 | -43.11222 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| b48305c3-823a-3cfb-a941-838a47a28a1a | -7.79419 | -43.11571 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 283ec3bb-7249-3ce9-adde-6d6a910fb16e | -7.79251 | -43.10474 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1605853d-c1f1-3645-8b75-9367940fe026 | -7.79196 | -43.10822 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b6612441-748a-37b6-8f7a-017ee45e733b | -7.79141 | -43.1117 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| fc589585-868f-369f-9847-0e6e7dc3c0a1 | -7.76805 | -43.06522 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b2d20b2e-0d7a-3d6e-8901-859808ea0ff1 | -7.76418 | -43.06818 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 5ba18209-8732-3380-8aaa-9e91b461f334 | -7.76363 | -43.07166 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d4eead1c-17c8-3b14-96e9-4de2e08d20ff | -7.75589 | -43.07756 | 2024-10-05 04:14:00 | NPP-375D | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |


[Clique aqui para ver as próximas entradas](README63.md)
