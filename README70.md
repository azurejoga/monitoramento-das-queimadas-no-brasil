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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 33608ec4-4205-3521-acb6-e30ceea7e6b7 | -8.1879 | -44.2283 | 2025-10-09 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 82786323-2d60-36e4-9b43-9e3bb854ed79 | -14.6327 | -48.3219 | 2025-10-09 14:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 26088368-4696-3036-815d-cc55d73163e9 | -10.1905 | -44.5471 | 2025-10-09 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 318.2 |
| 8e889553-7d84-355e-a754-292a296d01bc | -17.3781 | -45.0687 | 2025-10-09 14:10:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 69e047f1-c87e-33ed-b1a9-412c49b17135 | -12.6964 | -47.6776 | 2025-10-09 14:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 152.4 |
| aee30249-8e9d-3c65-8a49-8314544bfbbd | -7.5277 | -44.2952 | 2025-10-09 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 94.7 |
| fe21fc4c-a481-3af9-9255-575c0f7887cd | -8.2263 | -44.178 | 2025-10-09 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 3d0caca2-0f5c-320a-96f8-3adf279499c9 | -17.3033 | -58.0974 | 2025-10-09 14:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 75.9 |
| 08426c89-5c2a-39a5-bb30-cb2298a30140 | -11.7501 | -64.8814 | 2025-10-09 14:20:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 9ccbf97e-ed28-3d39-bedd-9f17f1756c49 | -13.429 | -47.5701 | 2025-10-09 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 167.2 |
| d294aec0-52a2-3424-b718-f7acbaa013c1 | -14.9367 | -46.782 | 2025-10-09 14:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 4f8123b0-7eb4-343e-b7ef-570ba45fd195 | -15.8288 | -43.7555 | 2025-10-09 14:20:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 150.2 |
| 6c8803bd-b926-3d7e-9eda-aa5d8368a6c6 | -14.2559 | -45.8681 | 2025-10-09 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 211.8 |
| 2aa01526-c2ea-3bc3-a63b-66939b6bc1d2 | -14.2754 | -45.8647 | 2025-10-09 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 187.2 |
| 367a1230-570d-3ab3-b419-c668dc263180 | -15.0771 | -46.5972 | 2025-10-09 14:20:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 8a3ff1d1-a4ac-329d-9989-153c01891d66 | -13.0771 | -47.8681 | 2025-10-09 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 2ca35f09-d18c-3f33-b3a3-0f4583223f11 | -17.6538 | -44.4339 | 2025-10-09 14:20:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 05e224e9-c48e-3aaf-98aa-d532de79af0a | -8.6295 | -45.1 | 2025-10-09 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 149.6 |
| aa1df604-d727-3ddb-80f5-53adbd3414ee | -13.7553 | -45.6999 | 2025-10-09 14:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 186.6 |
| 109ec48e-3caf-3f15-b75f-b5629afa0cbc | -17.2846 | -58.0384 | 2025-10-09 14:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 102.1 |
| 415a3a51-70b5-370e-a6ff-9f2b359d7894 | -7.0369 | -42.78 | 2025-10-09 14:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 77.1 |
| 3a1cefe1-103c-34b2-a1b0-0783abae6325 | -13.0783 | -47.801 | 2025-10-09 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 471f3c74-5154-3518-a5f4-4c001a7b4a46 | -13.2967 | -48.4801 | 2025-10-09 14:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 4b2c5ae4-76a8-3da4-9c59-e85338a60665 | -13.2779 | -48.4607 | 2025-10-09 14:20:00 | GOES-19 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 125.0 |
| c2215b7c-8cc3-3ddb-a14a-f2d381dfcbf4 | -12.6964 | -47.6776 | 2025-10-09 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 156.8 |
| e3296d79-1a50-3a1b-9c3e-1ff7a2ef1f34 | -17.2843 | -58.0588 | 2025-10-09 14:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.0 |
| e1c178ba-f440-3b34-80bb-5b57ea0a3e13 | -8.5602 | -44.6264 | 2025-10-09 14:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 9ee21861-054b-3620-87e2-2f62c5be49c1 | -13.0779 | -47.8234 | 2025-10-09 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 972fa277-067c-3efb-b7ca-64fd49391892 | -10.1393 | -45.4039 | 2025-10-09 14:20:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 121.1 |
| aa76eee7-3ac5-3398-a1c1-67150c4e99c2 | -7.5463 | -44.3164 | 2025-10-09 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 151.7 |
| 2d9e2ffa-ee8f-3b74-abb7-df48f56a8553 | -5.3999 | -40.9856 | 2025-10-09 14:20:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 231.7 |
| 8af6771d-3974-35f2-94e9-5b5fd9662f47 | -14.4452 | -47.9943 | 2025-10-09 14:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 6c192041-ec39-38e8-9464-4d840a001620 | -12.2754 | -47.6473 | 2025-10-09 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 150.8 |
| cd7145c3-5000-3a93-8dfd-af02858f6a8f | -17.285 | -58.018 | 2025-10-09 14:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 94.4 |
| 525a955f-494b-33f9-b076-37023d8817bc | -15.8085 | -43.7838 | 2025-10-09 14:20:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 359.5 |
| 3b40c1a4-cf26-3592-ab60-50a41e2fb81d | -10.1905 | -44.5471 | 2025-10-09 14:20:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 165.4 |
| 1c4d9a59-1243-35e0-a247-ea387f8f3218 | -7.546 | -44.3395 | 2025-10-09 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 0a68bc50-102f-38d4-94e0-53db2203d65c | -13.0976 | -47.7982 | 2025-10-09 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 125.6 |
| 6add514c-5eb1-30cc-9341-76083649c5f2 | -7.7922 | -44.2229 | 2025-10-09 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 74f74821-7463-39a6-827f-1685833d98e1 | -11.993 | -45.1958 | 2025-10-09 14:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 214.0 |
| 08208b9d-a2da-3177-af47-2415f4268b1e | -7.7736 | -44.2017 | 2025-10-09 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 76b8eee0-51d2-3955-97a2-42492b3a9a1c | -16.2788 | -47.1556 | 2025-10-09 14:20:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 85.4 |
| aa42db24-927c-3a49-96d4-923af5073594 | -12.2525 | -47.8728 | 2025-10-09 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 152.0 |
| a2fb687a-b0df-3446-b44e-ab6c93c1d90e | -13.4101 | -47.5506 | 2025-10-09 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 1ce1cad2-2760-3322-a89e-c9f267b7f7ac | -11.785 | -45.0421 | 2025-10-09 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 131.7 |
| b81bbec5-50af-36bd-b73a-07735ae87f2c | -11.7833 | -45.1347 | 2025-10-09 14:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 151.1 |
| 11375280-ea27-3879-a42b-e596dd38f207 | -13.8725 | -51.8693 | 2025-10-09 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 738bba33-f2ad-371c-80c8-21c12ab7f1b6 | -14.3543 | -50.7551 | 2025-10-09 14:20:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 115.4 |
| e9ad33dd-0861-3072-a8d2-dac6a91c5e8d | -13.0387 | -46.819 | 2025-10-09 14:20:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 040e20f3-4802-3e47-b58d-376646237483 | -11.4682 | -43.4774 | 2025-10-09 14:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 174762cd-baa2-3844-9fd0-eda8a9f03f69 | -10.214 | -45.4859 | 2025-10-09 14:20:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 111.7 |
| e2e2c11b-25b9-3921-a88f-1d75007d84cf | -16.0946 | -45.7829 | 2025-10-09 14:20:00 | GOES-19 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 89.6 |
| acecaf4f-86e5-3724-8597-232b852ab76f | -10.1199 | -45.4292 | 2025-10-09 14:20:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 136.3 |
| f0602af5-baad-3c22-a3bc-c02e8b8558ae | -17.9002 | -57.6594 | 2025-10-09 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 73.8 |
| 0a095fca-8cd5-3b76-9d2f-8222e36a5170 | -10.1389 | -45.4268 | 2025-10-09 14:20:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 41d480af-dcb3-3fdc-978f-af4b35596f1f | -7.5275 | -44.3182 | 2025-10-09 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 35826612-6fb4-38ca-bdf4-cfdca5878e1d | -17.8805 | -57.6617 | 2025-10-09 14:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.4 |
| ed115b51-bc4e-3f44-adff-8a687ba26091 | -4.9011 | -42.2464 | 2025-10-09 14:20:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 98.4 |
| 866aa7e8-76cc-3758-a951-69cdea9e5196 | -13.0775 | -47.8457 | 2025-10-09 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 138.4 |
| 3d326a38-59e5-3d55-9c92-3caf8b91e236 | -14.3349 | -50.7578 | 2025-10-09 14:20:00 | GOES-19 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 147.2 |
| d2cac16b-b8b1-3093-b9c4-b8bd1793595b | -8.6106 | -45.102 | 2025-10-09 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 731c350d-d898-3672-b9ab-d8292e302474 | -7.5041 | -44.7109 | 2025-10-09 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 0a5c2ec6-6ef4-3122-9cf8-acecc4305794 | -8.6292 | -45.1228 | 2025-10-09 14:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 155.8 |
| 928398f2-be07-3aa6-ac3b-7070253e4c3d | -12.2521 | -47.895 | 2025-10-09 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 130.9 |
| d5123d1f-bbbf-3845-a604-d3be31b7a1b7 | -9.3209 | -45.6607 | 2025-10-09 14:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 110.6 |
| 65aa9e00-7309-301a-80d5-b92fd3832aa8 | -8.0678 | -44.7929 | 2025-10-09 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 79.8 |
| b36c5423-6da1-3d62-8393-e2903b402703 | -17.3781 | -45.0687 | 2025-10-09 14:20:00 | GOES-19 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 117.3 |
| ec81e15c-9ef9-31ae-a92e-83dd9f9a5b8e | -13.7548 | -45.723 | 2025-10-09 14:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 191.2 |
| f2752782-c099-3a16-a757-aad56019e762 | -8.1879 | -44.2283 | 2025-10-09 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 114.6 |
| affc3867-a885-3368-8361-b42246b11125 | -12.6496 | -45.0021 | 2025-10-09 14:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 237.3 |
| 9c617dd2-9299-3e1e-9380-86e705694dfd | -17.3037 | -58.077 | 2025-10-09 14:20:00 | GOES-19 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.2 |
| aab08830-a84e-3e05-99b4-f66d6fd7e5de | -13.3052 | -48.0129 | 2025-10-09 14:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 120.6 |
| a4561ab5-8e85-34e8-9eff-161e9a2cc075 | -7.9963 | -44.4788 | 2025-10-09 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 24cb1c3b-2c0b-30f4-a8d8-f40dd1e528cf | -15.1543 | -45.7533 | 2025-10-09 14:20:00 | GOES-19 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 98.1 |
| aea95fbe-f1f0-3322-9852-74aaa0dbce96 | -10.158 | -45.4244 | 2025-10-09 14:20:00 | GOES-19 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 127.9 |
| dd867290-a500-3d0c-96b9-1694b3e40d65 | -8.1055 | -44.7891 | 2025-10-09 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 43aaa6dd-79c3-3945-aa13-f1d3a0ce5c5c | -13.0582 | -47.8485 | 2025-10-09 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 6095b2be-a51b-3ec1-a4a8-cd5bdd50a247 | -4.8823 | -42.2477 | 2025-10-09 14:20:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 96.2 |
| 204f1b25-6029-37d4-8931-5c432bf1ad4d | -13.0586 | -47.8262 | 2025-10-09 14:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 5287d98c-0065-326d-8a2a-c043a1c77b49 | -8.1615 | -43.3465 | 2025-10-09 14:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 76.9 |
| 8547437b-468f-32fd-a1bc-2ced528c4635 | -13.7553 | -45.6999 | 2025-10-09 14:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 158.2 |
| 2ef39b05-744c-3af2-821f-0d969f3fbf4f | -11.7501 | -64.8814 | 2025-10-09 14:30:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 39ad2e71-e23d-3c3a-9ed3-1cb9b807a8c4 | -12.6964 | -47.6776 | 2025-10-09 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 152.0 |
| caa79c2c-2258-3417-b618-31d03593ce32 | -8.6106 | -45.102 | 2025-10-09 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 171.5 |
| 74417f11-4611-33ea-ad10-9567937257f7 | -7.7933 | -44.1304 | 2025-10-09 14:30:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 67.5 |
| f3984abd-499a-39c1-a49b-4ed143763981 | -10.1905 | -44.5471 | 2025-10-09 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 165.1 |
| 164c823a-bc68-357a-9c10-e99cde894aa1 | -17.9029 | -57.4947 | 2025-10-09 14:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 70.9 |
| 841b3c99-cc58-39ea-bd09-378af296c4b2 | -13.0582 | -47.8485 | 2025-10-09 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 122.3 |
| c6494e93-64b3-3132-aa42-1d24353f1c10 | -11.4682 | -43.4774 | 2025-10-09 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 94fda663-0247-3d58-847e-657b7d2316a9 | -5.4187 | -40.9841 | 2025-10-09 14:30:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 130.7 |
| 15cebc85-bce3-3b77-8924-885ddc58cb10 | -8.2083 | -44.1105 | 2025-10-09 14:30:00 | GOES-19 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 3988e8a0-e617-3c13-ac86-9cbbb62cbe0a | -4.8823 | -42.2477 | 2025-10-09 14:30:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 113.5 |
| 4b4b2d24-e412-3668-8e7c-6a1002aa2664 | -4.9011 | -42.2464 | 2025-10-09 14:30:00 | GOES-19 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 99.1 |
| c2c100e5-e7d8-3b15-95b9-7b9ed6c9d7b2 | -16.2788 | -47.1556 | 2025-10-09 14:30:00 | GOES-19 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 9b4ca385-4137-3b02-944d-7ec9ef6a90d0 | -9.3019 | -45.6628 | 2025-10-09 14:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 132.9 |
| 74f853d6-7c25-3ffb-afbe-402d4756a671 | -13.4097 | -47.5731 | 2025-10-09 14:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 120.9 |
| a91d6f4b-83f3-383b-9f5b-ed7d115c2274 | -13.0381 | -47.896 | 2025-10-09 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 24592bb4-e1e1-3f73-b5ae-de4e5fab3003 | -8.6103 | -45.1249 | 2025-10-09 14:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 22356ed0-fdf8-3dbf-ada6-519457ca8637 | -13.0586 | -47.8262 | 2025-10-09 14:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 147.4 |
| c51b9e33-5b4a-36b6-bca6-11c7be2a8ab6 | -15.8091 | -43.7597 | 2025-10-09 14:30:00 | GOES-19 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 143.0 |


[Clique aqui para ver as próximas entradas](README71.md)
