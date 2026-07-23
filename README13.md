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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed37495b-f204-36fd-a9cc-de38ade937bf | -20.16686 | -43.91853 | 2026-07-23 04:27:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 21326f53-81ec-3112-973f-9d5aef865a40 | -21.15861 | -48.64185 | 2026-07-23 04:27:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b0c609c6-18bb-3ffd-9864-f0093bfd8e25 | -20.16336 | -43.91793 | 2026-07-23 04:27:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| a3d18f27-fe1f-38f5-bbdf-6713019711a8 | -14.30844 | -52.09224 | 2026-07-23 04:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7d868a01-38a7-3618-a03a-78b96e18a809 | -15.9138 | -41.94328 | 2026-07-23 04:27:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 89b31ec8-846f-3ff7-85ce-5ed16b111d92 | -17.7354 | -52.74272 | 2026-07-23 04:27:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7cbceab1-b794-3501-b93a-2d4d40d37350 | -18.95312 | -48.80963 | 2026-07-23 04:27:00 | NPP-375D | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 121bae64-e1eb-3580-a5a5-fdc2ce930c31 | -19.70601 | -48.08024 | 2026-07-23 04:27:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cf08285f-596c-3020-adb6-0a79e902ac37 | -14.37602 | -58.3404 | 2026-07-23 04:27:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ddc5bbba-a5fe-3065-8b3e-dfc463471845 | -17.57734 | -47.50417 | 2026-07-23 04:27:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 31c424fd-7a21-3fd1-85d2-93e0db17c651 | -17.57332 | -47.50735 | 2026-07-23 04:27:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d237243b-bf15-343f-81d0-046738d80844 | -21.36852 | -43.75962 | 2026-07-23 04:27:00 | NPP-375D | ANTÔNIO CARLOS | MINAS GERAIS | Brasil | 3102902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a0005507-33ab-3652-a25d-643752755959 | -14.30933 | -52.08753 | 2026-07-23 04:27:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 27c696e7-7230-393d-850d-732da86977a2 | -19.70876 | -48.08474 | 2026-07-23 04:27:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e2e62a37-a823-3eb1-8140-d3b1110cdec2 | -17.26033 | -48.28261 | 2026-07-23 04:27:00 | NPP-375D | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fa22f0d8-6842-3b68-b2a1-cb0aeaad6822 | -17.57671 | -47.50796 | 2026-07-23 04:27:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f4ff5126-fc2f-332d-93fd-9ac04fb93fe5 | -17.57056 | -47.50294 | 2026-07-23 04:27:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db94003d-8331-3153-adac-c97e906bce5a | -20.16275 | -43.92208 | 2026-07-23 04:27:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| c1f48dd4-b31f-3d37-a07a-8fae66a87e3d | -20.17037 | -43.91912 | 2026-07-23 04:27:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 90ecdd3f-2061-3224-ad9f-bb774631f69b | -15.66921 | -50.28209 | 2026-07-23 04:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f7715ca3-b8b6-32a2-9446-bba8fa4b9171 | -17.57882 | -47.51619 | 2026-07-23 04:27:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7081ec03-ccd6-34cc-bd2e-c490f34cb603 | -17.58073 | -47.50479 | 2026-07-23 04:27:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a06814a5-5753-375c-8573-d490fa845359 | -21.40381 | -45.65086 | 2026-07-23 04:27:00 | NPP-375D | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f0418a86-3026-38f1-9371-0e5180d9170f | -12.87696 | -58.28974 | 2026-07-23 04:27:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8ab5621-9425-3b36-915e-6328fd61cc26 | -20.23177 | -42.82543 | 2026-07-23 04:27:00 | NPP-375D | SANTA CRUZ DO ESCALVADO | MINAS GERAIS | Brasil | 3157401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| cee16365-e8c7-30e6-8da7-e2fe94b1d917 | -21.21164 | -48.99255 | 2026-07-23 04:27:00 | NPP-375D | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e5d7e44c-e9e8-3fc3-85bb-412b5195084d | -15.6699 | -50.2859 | 2026-07-23 04:27:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d330873d-3781-3d55-8d61-bf858f931310 | -17.61466 | -41.99068 | 2026-07-23 04:27:00 | NPP-375D | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| eb0a1777-a5e9-3d8e-9ea4-91a0bf573a96 | -11.7875 | -47.1108 | 2026-07-23 04:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 0f052c99-e670-3bcf-94db-c3e51b6835da | -11.9641 | -50.3747 | 2026-07-23 04:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 46.8 |
| c83adc7b-38f5-330f-bdf8-ef9e6b22fa73 | -11.7879 | -47.0884 | 2026-07-23 04:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 927b20d3-486f-3187-88c4-709f1d7837c7 | -11.9645 | -50.3532 | 2026-07-23 04:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| c8991036-11a7-342e-89d2-cd9e8293c8e6 | -11.698 | -50.3629 | 2026-07-23 04:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| b90e9b7c-26bc-3c17-960a-a296d799dc5d | -11.9641 | -50.3747 | 2026-07-23 04:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 8ad70dfe-0553-3d5d-bdea-7cd996ca023e | -11.7875 | -47.1108 | 2026-07-23 04:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| cf06c8e3-ba13-3251-a3cd-16d0a08374f9 | -11.6792 | -50.3437 | 2026-07-23 04:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 8f93c63e-cb99-313d-9a00-a486866350b1 | -11.698 | -50.3629 | 2026-07-23 04:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 224da558-e332-3ca4-8ca7-43d88d95ec7d | -11.6789 | -50.3651 | 2026-07-23 04:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 312e4e57-9ffa-380f-930f-9a39bd9b52e4 | -11.7879 | -47.0884 | 2026-07-23 04:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 235eed26-d993-388a-81eb-e6deb5b31292 | -3.52317 | -42.69589 | 2026-07-23 04:42:00 | NOAA-20 | MILAGRES DO MARANHÃO | MARANHÃO | Brasil | 2106672 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f4a6fe6-f7be-3aa8-acbb-6400310bbbca | -0.51872 | -50.55735 | 2026-07-23 04:42:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e84ec453-275a-3d53-b018-27c65bb2dfd7 | -1.78333 | -55.52607 | 2026-07-23 04:42:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbb31a43-6c24-3e39-a729-b7b6ec3b8881 | -0.85485 | -52.71581 | 2026-07-23 04:42:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3a90f2b3-7abc-3505-a405-82e9c134abc3 | -0.08949 | -51.27918 | 2026-07-23 04:42:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9ba38221-77a4-39c7-99e2-3b18e82e60a4 | -2.76694 | -48.57489 | 2026-07-23 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 87b7341b-b086-3289-91d4-e68fbc9af540 | -3.14696 | -48.14739 | 2026-07-23 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba9dddce-9844-3c59-a3ae-5dc5b94a6077 | -2.72393 | -49.78933 | 2026-07-23 04:42:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abb8f435-2495-3ada-ba27-c1fab1846441 | -2.77024 | -48.57541 | 2026-07-23 04:42:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c56c683d-d6de-3e11-b20b-e198a18945d9 | -3.14255 | -48.15381 | 2026-07-23 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a011284a-e364-34fe-9a4d-63d0417bf832 | -3.14587 | -48.15433 | 2026-07-23 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d34acd0c-9ab7-3cfb-967f-6ebc746538ad | -3.42078 | -43.1636 | 2026-07-23 04:42:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e67251a3-dc50-316e-9b49-1620e676edc5 | -2.48526 | -50.76092 | 2026-07-23 04:42:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 78474a50-a22d-3cf5-8a68-9221775191a9 | -7.03787 | -45.54353 | 2026-07-23 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6bf57481-3ccd-3068-81d4-baa914dca27a | -4.8387 | -44.07088 | 2026-07-23 04:44:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5c4f393-c993-3a7b-9692-ff072fec77ff | -8.80387 | -49.37322 | 2026-07-23 04:44:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bd4ee3ed-e577-3ee8-9f4f-9ccf16b093c3 | -5.319 | -43.5593 | 2026-07-23 04:44:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f635ecee-b630-3745-a47d-46f04ea829e3 | -6.14659 | -49.87289 | 2026-07-23 04:44:00 | NOAA-20 | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0818c809-9e3b-3389-8983-7d29c5871ae0 | -4.83463 | -44.07028 | 2026-07-23 04:44:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1bca3c0e-8a53-310c-826b-4f949548e3c9 | -7.90051 | -48.27426 | 2026-07-23 04:44:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9aab6eda-ec61-3251-8f63-35fe985df832 | -5.80871 | -43.63511 | 2026-07-23 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 61348b17-d7b9-30a1-9337-1040ef784d79 | -7.88801 | -46.89973 | 2026-07-23 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 82d04a1f-77b0-3680-a36e-bbdd8245dde3 | -5.54942 | -45.38742 | 2026-07-23 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b29d39a1-0331-3220-8617-a9f5f49a08fc | -6.88056 | -56.50348 | 2026-07-23 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b28d1fbf-3bf6-3fb6-b852-98b8941aa00d | -9.23199 | -50.1497 | 2026-07-23 04:44:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d117c56-62ed-33cc-9038-4d0447c6bdea | -3.27365 | -48.83096 | 2026-07-23 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b011558-b3cf-3225-b263-cf563f50621e | -6.84805 | -47.93872 | 2026-07-23 04:44:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e184b12c-57b7-359b-9d06-444f55b48f98 | -7.01137 | -45.41552 | 2026-07-23 04:44:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd498693-6750-36d8-a82f-378c700d2095 | -2.84268 | -54.67937 | 2026-07-23 04:44:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c613c879-df1b-3eed-80fb-b8f02b3607ef | -8.8374 | -47.07496 | 2026-07-23 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b4371946-16d6-3e9d-bd92-2f5048ed8913 | -7.88971 | -46.90324 | 2026-07-23 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0cfa1ecc-c695-3d02-b17e-274b364a54a6 | -9.16663 | -58.31225 | 2026-07-23 04:44:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9dc4ce4f-c4a0-3d5f-bb03-78d7e18494ee | -5.63581 | -47.10285 | 2026-07-23 04:44:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ca5360ef-4d27-3cad-8f1f-55fc4e7edaa0 | -6.54112 | -55.15488 | 2026-07-23 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddd34e0b-b31e-3980-9d43-f02edcd5dd46 | -9.46171 | -45.64683 | 2026-07-23 04:44:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2fc44b30-6439-36f4-95fc-9bb1497dd32b | -5.82668 | -43.48185 | 2026-07-23 04:44:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| d0db0a0f-6b71-317f-8c1d-9643ba1fb447 | -3.09592 | -54.51374 | 2026-07-23 04:44:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab22a6f5-c476-34ac-aa0d-925a59c8241a | -9.10561 | -49.65778 | 2026-07-23 04:44:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 222c52f2-c701-3cff-b881-c33f32cf7c75 | -6.05035 | -43.86981 | 2026-07-23 04:44:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f8b2cb28-ebfa-3d98-adbb-97713f2cfde3 | -6.20945 | -49.43353 | 2026-07-23 04:44:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 205e0238-155f-34c8-a4d8-88fafab16320 | -7.73009 | -47.24692 | 2026-07-23 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 269a1101-0c19-3ce3-91bf-35ac00c09605 | -8.83677 | -47.07911 | 2026-07-23 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b65d51d5-4584-3e33-97fb-bdac8b6320ea | -8.80719 | -49.37374 | 2026-07-23 04:44:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37d3e7fb-612c-318e-b28d-fd560881eedd | -7.72952 | -47.2485 | 2026-07-23 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aabd4218-80c3-3ae9-b5b6-2e6ffa6b808e | -3.19262 | -48.76215 | 2026-07-23 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19504f95-aa60-377b-b311-568ffd3be7d6 | -7.01139 | -45.85231 | 2026-07-23 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe81f77b-c501-3c05-bfac-a05f370f98ba | -7.01065 | -45.42032 | 2026-07-23 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d3e640b1-4e5f-3bce-ac67-27de97d07ff3 | -8.79777 | -49.36866 | 2026-07-23 04:44:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc37112d-554f-3f26-a3cb-1aaa8765596c | -3.27035 | -48.83044 | 2026-07-23 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea541f42-5fcf-309f-b793-9017c69d42df | -8.68274 | -47.8287 | 2026-07-23 04:44:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e4b21ff-1688-3554-9a08-ee80a7ec481c | -5.8221 | -44.13674 | 2026-07-23 04:44:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9fae27eb-a3c2-315e-aad4-3c9e85789582 | -7.88613 | -46.90268 | 2026-07-23 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0918ff24-3476-3d3e-bed1-041114dd7afd | -6.04615 | -43.86922 | 2026-07-23 04:44:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1488879f-6fe9-3c88-9093-7080f46495f5 | -7.83011 | -47.11114 | 2026-07-23 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b2524dd-38f3-3a0e-bf22-ba9e32589b47 | -6.30697 | -43.65728 | 2026-07-23 04:44:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dd7c480c-1b58-3402-96d4-2071d1448d1e | -7.0417 | -45.54406 | 2026-07-23 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| fca9b73a-ee17-31d9-b7c4-5b4aa320fe6f | -5.4887 | -45.12153 | 2026-07-23 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e2f19790-9ac3-333f-8862-20d7d86c3d43 | -5.80445 | -43.63454 | 2026-07-23 04:44:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55787235-128f-33f9-b51d-154939277c34 | -5.67538 | -43.57636 | 2026-07-23 04:44:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca52a35b-a691-3191-9f40-a20acf429c73 | -8.6787 | -47.832 | 2026-07-23 04:44:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b5ca7d2-4daf-3e5e-b323-ec627298c55e | -5.85021 | -49.06112 | 2026-07-23 04:44:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README14.md)
