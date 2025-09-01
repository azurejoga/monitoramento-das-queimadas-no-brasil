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

## Dados Diários - Página 102

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5f2496e-3153-3555-a3f1-005bc7c54a46 | -6.81641 | -43.34376 | 2025-09-01 11:55:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| ea674541-437e-3d50-a695-453ae1d1de3d | -6.15753 | -43.33442 | 2025-09-01 11:55:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 0ef22b48-0a28-37ac-83e4-d7499f981e5f | -7.08403 | -44.34496 | 2025-09-01 11:55:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 51.8 |
| ee56f743-0eab-3191-8eaf-70237742c2f5 | -6.26981 | -43.55682 | 2025-09-01 11:55:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 37bc49c5-56e7-375e-a378-036e3596379d | -6.98126 | -43.11557 | 2025-09-01 11:55:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 17.9 |
| be5701f1-bfc2-37de-855d-da1ae90d56a6 | -6.82898 | -43.32463 | 2025-09-01 11:55:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 53.4 |
| e1f1da3d-0698-3ca9-b195-0ab5b4dbc3a6 | -7.45963 | -44.83943 | 2025-09-01 11:55:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 6e22ba78-7989-3aa4-96eb-632e26a10855 | -6.20057 | -43.33676 | 2025-09-01 11:55:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 6ca8cb98-bf6d-31d6-bf57-bf3aab4c53e3 | -6.30057 | -43.61619 | 2025-09-01 11:55:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| feb2e22c-450d-33dc-bd21-30c0f825c7a5 | -6.83999 | -43.31578 | 2025-09-01 11:55:00 | TERRA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 28.5 |
| 18e4916f-009d-3039-8702-64376f043a57 | -5.69638 | -43.55777 | 2025-09-01 11:55:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b57f21b7-8374-338b-bc74-2ea385225bcb | -6.7472 | -43.78078 | 2025-09-01 11:55:00 | TERRA_M-M | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 102.0 |
| f2b7ac4c-48d7-3e6d-a434-c4536e091d22 | -6.09569 | -43.19288 | 2025-09-01 11:55:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 753f2316-8000-3040-bdf6-3bdf56dc3399 | -7.5824 | -43.83358 | 2025-09-01 11:55:00 | TERRA_M-M | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| fcd668e8-3c4e-30e2-8a5c-4e3b0daf0ebd | -7.24913 | -44.0606 | 2025-09-01 11:55:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| c578bc79-4263-3aad-89f6-570172a224ec | -6.94103 | -42.01298 | 2025-09-01 11:55:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 770a17f8-59fc-3013-97c3-f012329477c9 | -6.15906 | -43.32397 | 2025-09-01 11:55:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 2c6a5bfd-92db-34d9-81f6-f31785fc7150 | -7.07399 | -44.34341 | 2025-09-01 11:55:00 | TERRA_M-M | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 6313ec61-41db-34e4-bb91-f3e5c065baec | -11.9099 | -44.89269 | 2025-09-01 11:57:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 28839d7c-49f9-36bc-96df-389916ebdf0e | -12.59786 | -48.23152 | 2025-09-01 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 96.4 |
| e27723fb-6038-39cb-921a-73d462efafae | -12.57398 | -48.20171 | 2025-09-01 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 3d1f0d15-1299-3d05-a8cd-fd1106460b58 | -14.7473 | -46.74945 | 2025-09-01 11:57:00 | TERRA_M-M | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 397cf3a4-e17d-3cf2-affc-8c0557cb7976 | -14.64239 | -48.03354 | 2025-09-01 11:57:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 8471f45b-5fb5-3658-83af-fe42660fd3fc | -7.96042 | -46.44519 | 2025-09-01 11:57:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 30.5 |
| b4781f9f-28ad-32bd-bc4a-113538a6c078 | -13.29553 | -46.89074 | 2025-09-01 11:57:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| e089d9dc-d4cb-389e-a588-726fef282f3e | -7.93461 | -46.45782 | 2025-09-01 11:57:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 30783c20-abca-3bc3-91b4-0caf1d477026 | -11.45042 | -46.81267 | 2025-09-01 11:57:00 | TERRA_M-M | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 0de3a3d9-9b06-3fa2-a418-a1c5d3f0597d | -8.8583 | -47.51477 | 2025-09-01 11:57:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| ec6b71d9-04f0-3254-864d-c161de52852d | -12.57096 | -48.22005 | 2025-09-01 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 419d1426-45f6-3557-acc3-5587434f39c3 | -8.90278 | -45.11985 | 2025-09-01 11:57:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| eb34eafc-3c03-3453-b843-d379c04302f3 | -11.3733 | -43.61559 | 2025-09-01 11:57:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| bd211220-68b0-33fb-ac7d-bda2aeff143d | -11.96816 | -45.85139 | 2025-09-01 11:57:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| f22e39e7-d67c-31b7-9aa4-95c43c1ef3a6 | -11.38798 | -43.63383 | 2025-09-01 11:57:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| ec85bfb7-b37a-3313-9b9c-30b0135df88a | -11.05403 | -46.98037 | 2025-09-01 11:57:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 12340eac-8665-3a28-bb12-0d40c390736b | -8.47285 | -45.1702 | 2025-09-01 11:57:00 | TERRA_M-M | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 8fd24ff4-c2ac-34e4-acb1-ff0df416bca9 | -14.64218 | -43.96838 | 2025-09-01 11:57:00 | TERRA_M-M | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 6.0 |
| d1b1f304-34d5-32f8-9fb9-8e679caba170 | -14.61137 | -48.94129 | 2025-09-01 11:57:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 53.3 |
| effa2b92-e6ec-3690-9cfd-087536f08bbf | -14.33032 | -48.65137 | 2025-09-01 11:57:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 9e52718d-5bdb-3513-8256-f7ba8de554a1 | -8.85523 | -47.53365 | 2025-09-01 11:57:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 071d16fc-42ab-300f-9bf3-13fa35a85bc0 | -13.31364 | -46.84845 | 2025-09-01 11:57:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 35.1 |
| bb8c1e1a-6f38-3caa-ae95-eede2f959477 | -10.61107 | -44.33161 | 2025-09-01 11:57:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 67.8 |
| d8bb226d-1f75-310e-ab23-e714b53fef2f | -9.49904 | -46.47403 | 2025-09-01 11:57:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 96c07420-27d0-38b1-a91a-ac69cfafc689 | -7.39771 | -47.43661 | 2025-09-01 11:57:00 | TERRA_M-M | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| 750ea499-4aa6-3834-8774-fcfce0195000 | -12.5556 | -48.23651 | 2025-09-01 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 211.1 |
| 5a0b25c3-cb34-3309-9644-5d8e2781490d | -12.98627 | -48.1192 | 2025-09-01 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 42.4 |
| c64dbe05-804a-3aef-808c-95ee00b6e7d6 | -11.9578 | -45.84977 | 2025-09-01 11:57:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 34b21ef4-3c1c-3485-825f-909304838a95 | -7.49057 | -45.98623 | 2025-09-01 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.3 |
| b7405919-64aa-3844-9e26-575824458afe | -8.34458 | -47.43275 | 2025-09-01 11:57:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 195b188a-2c98-30f5-95f2-a61d0372327c | -9.16453 | -45.21746 | 2025-09-01 11:57:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 82fc4247-80e8-3760-9a91-db722dd18060 | -13.3687 | -46.93893 | 2025-09-01 11:57:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.1 |
| e3bf3515-551f-36d9-a4ff-88e3cf292f76 | -13.17525 | -45.2763 | 2025-09-01 11:57:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 5def7e69-6add-36a0-92c1-a4a16619c7fb | -13.37967 | -46.94056 | 2025-09-01 11:57:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| d298b948-0672-3c74-b50c-0753665e5b38 | -14.60794 | -48.961 | 2025-09-01 11:57:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 20.6 |
| a4cf4741-a354-3887-991c-512a4a37f8ad | -10.05366 | -48.08564 | 2025-09-01 11:57:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 08df0d42-d1fe-3f59-8129-e3e6b371bf82 | -11.96416 | -45.85694 | 2025-09-01 11:57:00 | TERRA_M-M | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 32.4 |
| 08f5aaf7-243d-3da6-8fe9-f9d2baec7c55 | -11.35873 | -43.52504 | 2025-09-01 11:57:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| e3301785-e4a1-3901-8a36-2cceab3b17a3 | -7.70176 | -44.99617 | 2025-09-01 11:57:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| cbd8a0c1-61ec-3cd1-9578-f1c42fcb5a92 | -12.78965 | -47.6445 | 2025-09-01 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| b31812d5-f643-35ac-9418-57ccb7fe077d | -15.33141 | -46.10835 | 2025-09-01 11:57:00 | TERRA_M-M | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 18.4 |
| ab55737b-090b-3352-a264-194326536eec | -13.51873 | -46.99995 | 2025-09-01 11:57:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 19.6 |
| e5f93c17-ebd1-3457-a505-3806988eb528 | -9.63818 | -47.81484 | 2025-09-01 11:57:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 29.8 |
| b3d21820-654e-32de-a5fa-7bedf4d27d27 | -12.60102 | -48.21299 | 2025-09-01 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 6f55e7ff-b57d-37ab-bb48-7437042694f0 | -11.05773 | -47.02969 | 2025-09-01 11:57:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 7413c55f-f920-355c-a337-13c393266336 | -12.98244 | -48.11128 | 2025-09-01 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 218.9 |
| 294855cb-c7ad-3986-a6f2-2f8191e03683 | -14.61029 | -48.93521 | 2025-09-01 11:57:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 38b37539-a333-3ccb-9e4b-fa4643941a8a | -14.60704 | -48.95473 | 2025-09-01 11:57:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 069e5754-aee2-3f2c-bf1d-59ec0ce992a0 | -9.28692 | -47.10642 | 2025-09-01 11:57:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 24.5 |
| abd0304c-8452-369d-a1c3-ec5f4cb48a46 | -11.80249 | -46.42101 | 2025-09-01 11:57:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 5cf79d77-b46a-3af6-995a-773f79457402 | -12.87265 | -48.06632 | 2025-09-01 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 35.4 |
| b15cd451-0d4e-325c-9d35-8c898d1332b2 | -11.05501 | -46.91052 | 2025-09-01 11:57:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 26.3 |
| c723ff8c-3cad-39dc-ab03-ed340d0a0f90 | -7.95537 | -46.47755 | 2025-09-01 11:57:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 4498d406-da1d-3c97-bb57-366d482fda64 | -14.09719 | -41.88064 | 2025-09-01 11:57:00 | TERRA_M-M | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 1cb618ac-358e-3cc7-a526-4f304b9dd2fb | -13.31615 | -46.83305 | 2025-09-01 11:57:00 | TERRA_M-M | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 14.4 |
| b71c2a3a-67d6-3b96-8f4e-9085b8bbac3e | -8.85262 | -47.78979 | 2025-09-01 11:57:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| d8af5f19-3261-3294-822e-862d85ecb35c | -12.58037 | -44.79611 | 2025-09-01 11:57:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 27aaf57a-7a1e-34a9-b4fb-f496a18eadd7 | -9.48769 | -46.4724 | 2025-09-01 11:57:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 45eb53c2-7a2b-3629-9969-68e625f50be9 | -9.53128 | -45.82695 | 2025-09-01 11:57:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| afeb77e0-2c84-383b-8fd6-334328d0a677 | -11.91156 | -44.8818 | 2025-09-01 11:57:00 | TERRA_M-M | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 6fc9bc13-3ade-3a15-88f7-4e6e0e50a81f | -11.05172 | -47.00632 | 2025-09-01 11:57:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 003caa70-472c-3b85-b098-fddcf00eb1c8 | -10.04946 | -48.11232 | 2025-09-01 11:57:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| ebb5053a-641a-3678-84c5-3bc7014a71ba | -14.6436 | -43.95887 | 2025-09-01 11:57:00 | TERRA_M-M | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 71.4 |
| c5301211-4a93-3dab-9bae-b1ee79395651 | -8.0109 | -44.0499 | 2025-09-01 11:57:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e706a409-f33d-3f94-9b9b-fde002846a35 | -11.89655 | -46.69034 | 2025-09-01 11:57:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| df9fb394-2118-3317-8bff-3e6a7321dc48 | -13.57635 | -44.30996 | 2025-09-01 11:57:00 | TERRA_M-M | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4150cbe3-ee26-31db-9703-f4ab307d0335 | -12.59854 | -48.20573 | 2025-09-01 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 7f5167a6-3244-3738-b34a-2359fb6e47ee | -11.89892 | -46.67545 | 2025-09-01 11:57:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 1b921020-c28d-3164-8acd-6b343b209b36 | -13.17349 | -45.2875 | 2025-09-01 11:57:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 34b66012-84e0-3814-b88d-e3c20d6ff465 | -14.04576 | -44.55353 | 2025-09-01 11:57:00 | TERRA_M-M | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 40.3 |
| d9bcd8ff-5dd2-3734-a302-b9c6b1a285c6 | -12.57079 | -44.79463 | 2025-09-01 11:57:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 18ac66e9-c0cc-3a82-81d3-88ddfff06538 | -11.06542 | -46.98259 | 2025-09-01 11:57:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 5aeacc99-27b7-3036-b7f6-38a3c6a52574 | -8.85393 | -47.52645 | 2025-09-01 11:57:00 | TERRA_M-M | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 197.0 |
| b80c4db6-22be-32c5-9a26-9431e86d43cf | -12.97039 | -48.10901 | 2025-09-01 11:57:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 41.7 |
| a2fadeb0-408a-3f37-8c67-606ba0c2b57e | -11.04192 | -45.14013 | 2025-09-01 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| c7e396ca-e19b-3fd2-bef9-ef2238e74986 | -11.08982 | -44.63007 | 2025-09-01 11:57:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| f59a506c-99e5-3791-bed3-0972cf215d0f | -11.37901 | -43.5771 | 2025-09-01 11:57:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 9f8e689e-14ab-3a85-8023-e224435a7caa | -7.94373 | -46.47569 | 2025-09-01 11:57:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 33.5 |
| ffcf4509-108c-3af4-a7cb-cd2699ace9db | -9.15415 | -45.21607 | 2025-09-01 11:57:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 6e2209d1-a27b-39c2-987b-c06248fe24cb | -8.1956 | -46.78654 | 2025-09-01 11:57:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 82621b50-6358-3acc-83ba-f5f19985265f | -8.31389 | -46.31657 | 2025-09-01 11:57:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.9 |
| fc60a081-1fcb-3c70-b917-9d5b7ad34592 | -11.81962 | -44.26998 | 2025-09-01 11:57:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |


[Clique aqui para ver as próximas entradas](README103.md)
