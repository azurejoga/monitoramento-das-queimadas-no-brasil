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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4a3910a8-7d97-33ef-9c0d-4d49fcc68a4a | -8.74895 | -49.75438 | 2025-05-17 03:49:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e09d737b-7d71-3ae6-8796-e90ae203eda5 | -11.57932 | -47.60968 | 2025-05-17 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 26bc4d0d-dbc0-3844-b9a6-f8c62c6353bb | -13.31218 | -45.37168 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ff9e4a00-bf21-33f7-bd21-9cdf876babb5 | -11.78158 | -47.35347 | 2025-05-17 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78e3388c-0233-3104-9f0c-36d86eabd117 | -15.36844 | -45.66959 | 2025-05-17 03:49:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| da66179d-150c-38a2-9182-91260252d6dc | -13.30953 | -45.38585 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6459742-b1fa-38ce-8365-2bad30dafbf5 | -11.97246 | -48.11015 | 2025-05-17 03:49:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7c96a42a-af61-3b0b-909b-913828d2604c | -11.79373 | -47.40554 | 2025-05-17 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d459a7c8-20df-3f67-85ea-1b3061f3ea50 | -11.15877 | -48.67754 | 2025-05-17 03:49:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 69b84164-9828-3960-969d-44394407d48d | -11.41623 | -44.71317 | 2025-05-17 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6a146e09-0891-3b43-b672-40bdf695565c | -11.43704 | -44.72643 | 2025-05-17 03:49:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 48150fc2-80c1-348b-b15d-23e38a5275d3 | -11.64577 | -48.03 | 2025-05-17 03:49:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5782af09-b3b9-386b-9a7f-1e51c84995bd | -11.78817 | -47.34781 | 2025-05-17 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b955df70-d596-33fb-81c8-51a84974f991 | -11.57792 | -47.61689 | 2025-05-17 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 65e73bbc-e88e-3a2b-a738-017ef5411502 | -13.31318 | -45.3914 | 2025-05-17 03:49:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 20375f8f-d4da-3d68-acfc-dfae61fb7535 | -11.79708 | -44.28373 | 2025-05-17 03:49:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30224614-2ec5-3f94-a5c2-f8788a9aa90a | -11.78223 | -47.35009 | 2025-05-17 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| fac92350-9604-3eaf-a0ab-7e2322acc654 | -22.6954 | -47.5311 | 2025-05-17 03:50:00 | GOES-19 | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 89.1 |
| ff0e4d23-eb38-3a97-b48f-a7f1c02a78ed | -13.1498 | -56.8054 | 2025-05-17 03:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| d0f3194a-bd0d-3f10-a777-7b80c0eadebc | -18.95645 | -52.2461 | 2025-05-17 03:51:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 88001298-5379-328e-b3d8-5017e74f3671 | -17.26434 | -49.00864 | 2025-05-17 03:51:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4fe6064e-69f5-3398-8de9-5359d9c725d3 | -15.26842 | -51.47601 | 2025-05-17 03:51:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5c53e422-ac7f-35af-be83-5ac6a4770d6a | -21.60467 | -51.6 | 2025-05-17 03:51:00 | NOAA-21 | DRACENA | SÃO PAULO | Brasil | 3514403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 58338b53-1d8f-33be-a4a6-0597953bfdad | -19.06712 | -53.45745 | 2025-05-17 03:51:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 321c6ab1-4315-3112-9192-e734064ade0b | -22.69968 | -47.52602 | 2025-05-17 03:51:00 | NOAA-21 | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 52068a96-cf09-3583-854e-0c39ed642528 | -19.83961 | -40.08157 | 2025-05-17 03:51:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 71a38c9d-6d31-3307-833b-f3c7e84efeb4 | -18.95025 | -52.24439 | 2025-05-17 03:51:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce0fbe95-8caf-3e40-8cfb-86d265f792b4 | -22.69875 | -47.53054 | 2025-05-17 03:51:00 | NOAA-21 | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 91118182-1ec1-38c2-bfa8-effdbe010ecc | -17.58035 | -47.48707 | 2025-05-17 03:51:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eff69e62-a849-3d29-8cb2-dde137e91ca8 | -17.26967 | -49.00978 | 2025-05-17 03:51:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7751d473-e7f1-3075-86a2-e2d100714ded | -19.97654 | -47.19203 | 2025-05-17 03:51:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 43ebf37b-52c1-3795-95ac-29632bd7c51d | -21.17972 | -43.9817 | 2025-05-17 03:51:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0f159af3-d29e-3157-af30-585eb3b94e6e | -22.6775 | -42.85578 | 2025-05-17 03:51:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| a17e0940-957b-311f-82b6-b4c2f44b79e9 | -17.27041 | -49.00627 | 2025-05-17 03:51:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2d7ed442-b7bc-31a4-9e69-b98cde6fc149 | -17.26682 | -49.00881 | 2025-05-17 03:51:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 05c60b84-a2ef-34d0-9189-8349794d0c54 | -17.2651 | -49.00505 | 2025-05-17 03:51:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cf629775-e760-35f7-b164-5adcaf036368 | -19.71835 | -40.35358 | 2025-05-17 03:51:00 | NOAA-21 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c1d012ad-b05d-3e5f-b5cb-dfe3ecbf4f4f | -22.74063 | -42.95945 | 2025-05-17 03:51:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 46ea8e4a-12ff-3056-9d1a-6e84e007a88c | -18.95331 | -52.24591 | 2025-05-17 03:51:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8f798ebb-2544-3066-af95-df0ba0aef6ec | -22.69936 | -47.52813 | 2025-05-17 03:51:00 | NOAA-21 | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.7 |
| 85987a4b-9059-3a84-ad03-2972c66c2198 | -15.2672 | -51.4816 | 2025-05-17 03:51:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 721cfc21-56a9-3cb3-8171-c5f441a0b595 | -22.70308 | -47.53172 | 2025-05-17 03:51:00 | NOAA-21 | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.2 |
| c006d53b-b6ac-31e7-ad22-26cee626d1b5 | -20.96996 | -44.33047 | 2025-05-17 03:51:00 | NOAA-21 | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 89996ebe-cc4c-393f-af4d-179b83e8ba0d | -18.38968 | -44.18941 | 2025-05-17 03:51:00 | NOAA-21 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 485b81e7-a1c6-3f1a-8856-da6daa9101d5 | -19.59749 | -45.01374 | 2025-05-17 03:51:00 | NOAA-21 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cfdc4c56-99bc-32cc-9c8d-70a83a3050ac | -19.0605 | -53.45563 | 2025-05-17 03:51:00 | NOAA-21 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 518093ec-b64b-3c9c-bcd6-b7e75d306f7f | -20.76584 | -46.76909 | 2025-05-17 03:51:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b9b0584f-139c-365b-b3bd-5f1f5c5d0a5e | -22.53928 | -48.81479 | 2025-05-17 03:51:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6babf4d1-2eca-3355-810c-df0228d11cf5 | -18.38876 | -44.19452 | 2025-05-17 03:51:00 | NOAA-21 | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 43b901a6-3eba-3404-9d5c-77242368de96 | -18.95452 | -52.24051 | 2025-05-17 03:51:00 | NOAA-21 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ccf7a6d5-9328-3e02-aeec-f68d8334b9c6 | -17.57884 | -47.48851 | 2025-05-17 03:51:00 | NOAA-21 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 365ca200-aead-3db2-bd90-9ace138f4e0b | -17.14764 | -44.81031 | 2025-05-17 03:51:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dd5ca526-a589-3651-8d9f-f21a1ba96f9b | -17.77892 | -42.80702 | 2025-05-17 03:51:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3859c680-13dd-3854-bd0c-88b7c1d3fd84 | -22.70401 | -47.52717 | 2025-05-17 03:51:00 | NOAA-21 | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.2 |
| 11655355-98eb-3c04-9236-2346b82ddc15 | -21.60557 | -51.59873 | 2025-05-17 03:51:00 | NOAA-21 | DRACENA | SÃO PAULO | Brasil | 3514403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| a2e4af93-aaa3-3591-94bf-ecf69ec7d93d | -17.26754 | -49.00525 | 2025-05-17 03:51:00 | NOAA-21 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| dfb2560b-e78c-328f-90eb-4ca7be37fdfa | -23.40581 | -46.55643 | 2025-05-17 03:51:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7b7098fa-339d-374f-a272-c3114830422a | -15.26078 | -51.48022 | 2025-05-17 03:51:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0a02f6d1-cd33-3fe5-9ec7-b67e4126a6b1 | -21.62599 | -43.46541 | 2025-05-17 03:51:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 600228fb-5b0f-3275-b36c-d5dc1157216f | -15.26962 | -51.4705 | 2025-05-17 03:51:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2b292fe5-7328-3118-a68e-5ba541e4c05e | -21.60458 | -51.60301 | 2025-05-17 03:51:00 | NOAA-21 | DRACENA | SÃO PAULO | Brasil | 3514403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| d1dbf1ac-afc8-3025-892e-66fa193fa60b | -22.78725 | -43.75908 | 2025-05-17 03:51:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b8901762-fe8f-302d-957b-ccb12b7b9658 | -23.33835 | -46.7711 | 2025-05-17 03:51:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 00f7113e-cb9a-3b6f-b37a-21aef6e8f179 | -22.90111 | -43.7538 | 2025-05-17 03:51:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e687b0d4-7fa3-36ed-928f-e11f5ddc951a | -22.70369 | -47.52934 | 2025-05-17 03:51:00 | NOAA-21 | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 38.0 |
| 67491259-93c8-3c17-ad8b-604bb6e5fcd2 | -21.72698 | -48.43691 | 2025-05-17 03:51:00 | NOAA-21 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 84d4fcc8-d618-34ca-b617-e341fd4c5bd4 | -18.90408 | -48.3271 | 2025-05-17 03:51:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e829ac61-f1c7-3eb1-ab59-766cb03e4805 | -21.6037 | -51.60431 | 2025-05-17 03:51:00 | NOAA-21 | DRACENA | SÃO PAULO | Brasil | 3514403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 2306646e-893c-3b22-a6d7-fa5753f99b06 | -20.16907 | -47.84106 | 2025-05-17 03:51:00 | NOAA-21 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ce0fd3f-f07f-3ff1-9dee-243ecfb6e89d | -17.74915 | -42.89291 | 2025-05-17 03:51:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ebb0091-efbe-37ca-8d41-e6688227ade7 | -25.19852 | -49.3216 | 2025-05-17 03:53:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2626ee5a-ea54-3868-b9e6-c3ffc7191595 | -23.59818 | -49.01482 | 2025-05-17 03:53:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3c85a658-c3e4-3c3c-9559-88c55a2269ee | -23.59668 | -49.01823 | 2025-05-17 03:53:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a18c777-367b-3fc7-93f9-9f7cfc108622 | -23.98714 | -48.91858 | 2025-05-17 03:53:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd6e17e6-93be-31eb-961e-5277bc293dad | -25.19275 | -49.32565 | 2025-05-17 03:53:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| dd00c6c1-b6ad-3af6-9b47-ceea8299c12a | -23.59785 | -49.01262 | 2025-05-17 03:53:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2491e47e-8add-33a6-b99f-64517c2e1108 | -22.7165 | -47.5256 | 2025-05-17 04:00:00 | GOES-19 | PIRACICABA | SÃO PAULO | Brasil | 3538709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 108.5 |
| d7fd454b-ba6a-3c8f-a009-7f01c8f1845e | -22.6954 | -47.5311 | 2025-05-17 04:00:00 | GOES-19 | IRACEMÁPOLIS | SÃO PAULO | Brasil | 3521408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 123.3 |
| bea9ae33-929a-33f5-a725-10ce522ab68d | -6.71193 | -42.139 | 2025-05-17 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| acfc10b3-6332-3504-8033-85bf8afdb7cf | -7.31039 | -43.23835 | 2025-05-17 04:14:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d07075c5-c419-39ea-bdd0-6af980c94c99 | -6.84344 | -42.79016 | 2025-05-17 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 14332ad1-1c81-3edc-949e-519580de206b | -6.71023 | -42.12782 | 2025-05-17 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 0be8ab41-fff7-35a1-af49-41c4d5adedcc | -5.10408 | -44.79849 | 2025-05-17 04:14:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| e5e54dc5-f441-35df-bdb5-eae28c76f68f | -6.70912 | -42.13493 | 2025-05-17 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2b5a93c2-11a0-3697-b9a2-0f5d8f7d7e1e | -7.31371 | -43.23888 | 2025-05-17 04:14:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0381bd1a-6dc7-3d6e-afda-78615a03e94c | -6.71248 | -42.13545 | 2025-05-17 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 148713e1-b973-3ee0-a063-68e7174c87a9 | -6.84234 | -42.79714 | 2025-05-17 04:14:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 098972c9-43a9-304e-92bd-b0700a0718f5 | -6.72313 | -42.13346 | 2025-05-17 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bc19e7ae-0cef-3178-8f62-80c250f620e7 | -5.10004 | -44.80169 | 2025-05-17 04:14:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6592794d-4d05-3b1b-9d58-4a431f199468 | -6.70857 | -42.13848 | 2025-05-17 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 01ea17b8-6a6b-3806-9351-6394318afe2e | -5.10349 | -44.80223 | 2025-05-17 04:14:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 8957438d-6366-301e-b6fd-541c685e423d | -7.31426 | -43.2354 | 2025-05-17 04:14:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0d059c69-1b1f-3362-a79d-d115a76af7bb | -6.70631 | -42.13086 | 2025-05-17 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f6c00ee6-8a56-3295-be2b-61cea41e0bb3 | -6.72704 | -42.13044 | 2025-05-17 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 594e8b68-7e3d-34a5-9d93-d45cafe15b35 | -6.84622 | -42.79417 | 2025-05-17 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d763c124-399e-34c4-ab3a-74f5022db461 | -6.75238 | -44.536 | 2025-05-17 04:14:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ca97f76-2d55-3ad6-bffc-9fd2bdfe2bd3 | -6.72143 | -42.12227 | 2025-05-17 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 6ee113e2-8acb-3699-a100-78ed723256ba | -6.75295 | -44.53242 | 2025-05-17 04:14:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e6287ca-2869-3cbd-86cd-f23dab46ba3c | -6.70968 | -42.13138 | 2025-05-17 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7b5b26ae-dc95-3a5b-a6d5-9820382bf4b8 | -6.72424 | -42.12636 | 2025-05-17 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |


[Clique aqui para ver as próximas entradas](README5.md)
