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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ef8ae03-97f4-305b-bf7b-24dc9d4dee03 | -10.21105 | -48.21125 | 2025-02-18 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0496a1e3-d8b8-3692-88c7-789b16db87db | -7.54894 | -45.87206 | 2025-02-18 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 266a850a-f713-3aeb-bf1d-6d167b19be27 | -7.54827 | -45.87653 | 2025-02-18 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f49af9c8-e875-3392-ba83-bbf80322759b | -14.15781 | -47.30337 | 2025-02-18 04:40:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6164d37d-e4b1-3616-95a3-5952df6d80c6 | -10.60878 | -45.11168 | 2025-02-18 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01d7de92-bdc3-3900-b148-17c1caf3563a | -12.32654 | -52.48564 | 2025-02-18 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a1ca7dd-26e2-34ca-b75d-c633fb85b86f | -13.28388 | -39.7999 | 2025-02-18 04:40:00 | NOAA-21 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 02de549e-4ea2-35bb-bae5-57b28f02dc78 | -13.28341 | -39.80431 | 2025-02-18 04:40:00 | NOAA-21 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 8821423f-ed10-3f83-98bd-1aa3fab8d96d | -13.28801 | -39.80189 | 2025-02-18 04:40:00 | NOAA-21 | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6a222620-b53f-335b-84be-3cbb2b239605 | -12.70613 | -44.67513 | 2025-02-18 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0a5e28cc-ca23-3969-80f1-40e16ee2adf4 | -12.84593 | -43.82612 | 2025-02-18 04:40:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 784bab2d-175f-399f-9455-5871ce898316 | -12.32376 | -52.48137 | 2025-02-18 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4baf394c-28b2-3d97-abd8-3c4be1b15ada | -8.12664 | -43.14126 | 2025-02-18 04:40:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 7cac1c31-27bd-3070-9531-23340496bc9f | -11.59695 | -44.85097 | 2025-02-18 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a9d658e-5bd7-3bf9-94f6-c9db265f731c | -12.33053 | -52.48249 | 2025-02-18 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7a63809-dbec-3318-a0a3-47c455c9ec73 | -10.61336 | -45.10852 | 2025-02-18 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8209af62-d22e-36ee-837c-22e196972c40 | -14.28074 | -47.41529 | 2025-02-18 04:40:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 404f1a19-0a47-3869-aef1-e6d0af62162a | -14.47324 | -45.82561 | 2025-02-18 04:40:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 214b9103-6f62-30f6-a031-b0610e22ae80 | -12.32993 | -52.4862 | 2025-02-18 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 484ca293-569c-3408-b165-66685a4ea410 | -10.61286 | -45.11223 | 2025-02-18 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8ea1f094-50bc-3e28-ab06-bbaa351c7f54 | -10.6057 | -45.10368 | 2025-02-18 04:40:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 25792d21-b0da-3f9a-b425-c2ada7b2cb98 | -11.59275 | -44.85035 | 2025-02-18 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 125eef25-9654-30db-88d8-de806d190a24 | -12.32316 | -52.48508 | 2025-02-18 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a3d7f02-9e5e-3202-b259-05a549baa8a0 | -14.27912 | -47.41329 | 2025-02-18 04:40:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 608cd366-d165-334e-b609-cad684f47386 | -12.33392 | -52.48306 | 2025-02-18 04:40:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ba2700b-60e7-3f75-a049-ead371e4754d | -7.54961 | -45.86753 | 2025-02-18 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be347e61-fe13-3f52-ac2b-211229d15038 | -12.85052 | -43.82677 | 2025-02-18 04:40:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e9e526bf-a280-3890-bf88-f827d4c00413 | -18.4443 | -44.48884 | 2025-02-18 04:42:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6b381bd-053d-3b83-9434-a4df554168b8 | -20.37498 | -43.59142 | 2025-02-18 04:42:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 010a3f06-f2f1-3154-ab54-f7c6a1f74b29 | -16.89873 | -43.65785 | 2025-02-18 04:42:00 | NOAA-21 | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ea070d3-b864-33fe-8ecd-10bf76568d08 | -20.28466 | -49.92115 | 2025-02-18 04:42:00 | NOAA-21 | ÁLVARES FLORENCE | SÃO PAULO | Brasil | 3501202 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4ee4ab4a-6705-32fe-a7b3-1edcc784a5a9 | -18.41129 | -55.59454 | 2025-02-18 04:42:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9eb3cb23-7323-3137-82bd-51065ed34f08 | -18.54632 | -56.18081 | 2025-02-18 04:42:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| e8658f40-6565-3512-84af-a1cfcfca94f4 | -14.98398 | -50.77293 | 2025-02-18 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 14d410e7-9e9c-3b07-93d7-567c89e49bb8 | -18.53313 | -56.16864 | 2025-02-18 04:42:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 99ff04ba-b3d4-3d68-a480-cba431eaebd3 | -14.98729 | -50.77346 | 2025-02-18 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8159d9ae-7927-377c-af09-27a91f0b1de5 | -19.0743 | -56.06516 | 2025-02-18 04:42:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| e0a2c8aa-bd01-367d-947e-4df3fd47cbb7 | -16.09881 | -60.07984 | 2025-02-18 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 841eda73-01d0-3155-a0cd-c4c9127e7176 | -16.90364 | -43.65855 | 2025-02-18 04:42:00 | NOAA-21 | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5203b7e2-254e-38f6-8d25-868cdf59449d | -18.54343 | -56.17544 | 2025-02-18 04:42:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| d39ee037-47db-3dd3-93ff-0d5b9174d9de | -15.07966 | -48.94356 | 2025-02-18 04:42:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5fe66ef1-5f6c-3330-a1eb-5b8dbe43d680 | -19.07144 | -56.05991 | 2025-02-18 04:42:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 9075849d-82c6-3dfb-aaf3-abeaaa0ed03c | -14.99061 | -50.77399 | 2025-02-18 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2daa4c53-0443-3516-a09d-59b574cb864e | -19.33964 | -44.83701 | 2025-02-18 04:42:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e833580-c123-32e9-8040-7493b0693cc8 | -19.06698 | -56.06374 | 2025-02-18 04:42:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 589f394b-e249-33f7-b634-67755d02d715 | -19.98646 | -51.27791 | 2025-02-18 04:42:00 | NOAA-21 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 28b372a6-ee21-3745-ae1f-2b3a1abc96a0 | -17.58187 | -50.39094 | 2025-02-18 04:42:00 | NOAA-21 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 068a8a60-a591-3a49-a492-de2472fde110 | -16.61833 | -43.33777 | 2025-02-18 04:42:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4778f257-2ea9-3662-9e46-7d5c2fe025e0 | -20.76367 | -46.76971 | 2025-02-18 04:42:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 0f13b483-0223-32a9-8d03-8b8f665991c4 | -14.98343 | -50.7765 | 2025-02-18 04:42:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8eecf68-2bfb-3615-8347-23838a1e272b | -19.07064 | -56.06444 | 2025-02-18 04:42:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 7eb4cdd0-69fc-320c-a408-bf6ec58e2c02 | -19.4987 | -55.34285 | 2025-02-18 04:42:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| c6d1c535-702b-3b37-bd0e-bc253d73c50e | -20.70416 | -41.70134 | 2025-02-18 04:42:00 | NOAA-21 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 802b7c6e-323a-3163-964e-580a70d4efbb | -19.49943 | -55.33867 | 2025-02-18 04:42:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| cfdd4370-208c-3ff4-808c-3157ac779595 | -18.40693 | -55.59824 | 2025-02-18 04:42:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| db630cd2-8a37-3546-9c3d-6bd5453f4539 | -20.37467 | -43.59446 | 2025-02-18 04:42:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| b45a0b91-31e4-3add-b5e6-88732a9c4313 | -18.39597 | -45.97548 | 2025-02-18 04:42:00 | NOAA-21 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e8901ed2-14e7-3109-b1f2-837684dac580 | -19.14931 | -46.35813 | 2025-02-18 04:42:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c67e71ab-4726-3475-9446-497a33760b8b | -19.1175 | -56.22281 | 2025-02-18 04:42:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| f8f8d88e-9ee5-39d1-96df-b56edd6d079a | -20.41541 | -43.55467 | 2025-02-18 04:42:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dded1521-4aba-30c3-a37d-eed45a004d27 | -16.90158 | -43.658 | 2025-02-18 04:42:00 | NOAA-21 | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 51576ddd-bf29-334b-813c-998a59dc232d | -19.12036 | -56.22813 | 2025-02-18 04:42:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 027ca914-429a-3663-97fa-d59dbe5671f2 | -20.70373 | -41.70604 | 2025-02-18 04:42:00 | NOAA-21 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5229910a-e239-3895-ba07-fc96c5ed98a9 | -16.09789 | -60.07814 | 2025-02-18 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ec7ef998-da15-3bc7-a9a2-a6f17f4b80be | -18.40769 | -55.59385 | 2025-02-18 04:42:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| c0e98dbb-795d-3783-9285-74154fdc4721 | -17.75366 | -42.89468 | 2025-02-18 04:42:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4eb99c63-4a6d-37d3-b8a0-2ee5dbfccf52 | -19.96461 | -45.16367 | 2025-02-18 04:42:00 | NOAA-21 | ARAÚJOS | MINAS GERAIS | Brasil | 3103900 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8af8a439-614c-324a-8f3e-ae1d52594872 | -16.1954 | -60.00414 | 2025-02-18 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 98a70b3e-1845-3633-b1fc-6e60b9fb0a9e | -19.50166 | -55.45191 | 2025-02-18 04:42:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| e497c94a-9eab-3826-82d1-f8dceeb17239 | -19.12119 | -56.22351 | 2025-02-18 04:42:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 0788319c-d5ee-3a2d-b90e-108d4f8b61b2 | -15.56964 | -47.85531 | 2025-02-18 04:42:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd0f30f6-0c17-3d23-af59-13c120448984 | -16.19697 | -60.00749 | 2025-02-18 04:42:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8c9bf38b-c902-32ea-abcd-16be4fe23d0b | -18.54054 | -56.17007 | 2025-02-18 04:42:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.2 |
| ce63edfa-b051-32c7-91c4-89cfc25c9fc0 | -15.47761 | -42.16702 | 2025-02-18 04:42:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8bb6c85-28b6-3212-8b43-fef04be5d636 | -19.07796 | -56.06586 | 2025-02-18 04:42:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 716ad822-e2bc-3fcc-9b6b-93749899e4bf | -19.06779 | -56.0592 | 2025-02-18 04:42:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| 3066bf02-c07a-3918-98d7-e30d31e70ab3 | -19.06413 | -56.0585 | 2025-02-18 04:42:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 61c41303-5afd-3be1-a8a0-e54f82affb40 | -19.02354 | -57.62202 | 2025-02-18 04:42:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9c5e8d18-59fb-372e-ab08-f6caa78f0c17 | -22.20218 | -56.96692 | 2025-02-18 04:44:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a9cca32c-b6ed-355e-905a-77c8d9e4552e | -22.42717 | -55.64269 | 2025-02-18 04:44:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7467dcf2-f443-34b5-b256-d60d7b0c8cc7 | -21.38321 | -48.57054 | 2025-02-18 04:44:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e24be964-b1da-3bea-b3ff-50d77a24956e | -21.2767 | -54.02047 | 2025-02-18 04:44:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20d0615f-698a-36b6-8001-79167ce4dc44 | -21.42073 | -48.55059 | 2025-02-18 04:44:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 72ad23c0-8ef8-3085-8048-55f67f68c19c | -22.67536 | -42.85407 | 2025-02-18 04:44:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| ab70edbb-d460-3da6-9a2d-63fe1542fa95 | -21.41691 | -48.55004 | 2025-02-18 04:44:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 2a9914bb-245d-38cb-813f-c4512ab4d59d | -21.36795 | -48.53769 | 2025-02-18 04:44:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf2b06fc-0820-3127-8e7d-0d1e0b951cf4 | -20.92086 | -56.54595 | 2025-02-18 04:44:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7a86697b-4b73-36aa-adc3-17f028514a88 | -20.91721 | -56.54523 | 2025-02-18 04:44:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f5a9e518-495d-3700-92f8-1604077ca2e5 | -20.50742 | -55.92507 | 2025-02-18 04:44:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e465984-87cc-3134-9652-43e9b5df8d23 | -22.19852 | -56.96613 | 2025-02-18 04:44:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cdb133ea-fa35-3c95-b896-237f49d091c8 | -21.07361 | -56.38795 | 2025-02-18 04:44:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2addf8f1-875f-3d87-92c4-0987350d69b4 | -20.9057 | -56.56698 | 2025-02-18 04:44:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d853082-abca-3a68-a86e-ebf0fc33251f | -21.07644 | -56.39308 | 2025-02-18 04:44:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b34e4c4c-79c6-3a28-ac0b-d836cbf1fb07 | -23.33897 | -46.77227 | 2025-02-18 04:44:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 216c7a82-fc6a-3840-ba33-7b310ddf7b79 | -21.96486 | -57.58585 | 2025-02-18 04:44:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a3a642d0-3b15-3ead-a2bd-fcc56255a266 | -21.07724 | -56.38862 | 2025-02-18 04:44:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 43783339-df63-3a3a-9321-92f9f3af9de4 | -23.40765 | -46.55704 | 2025-02-18 04:44:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bff29b80-bb8c-3532-899c-0c5f8ad13856 | -22.20667 | -56.96307 | 2025-02-18 04:44:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09419938-cf57-3e55-801f-5d9220fe5ccc | -21.42008 | -48.55562 | 2025-02-18 04:44:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 3db29471-58f6-328d-a4d5-881034e00af9 | -20.90854 | -56.57223 | 2025-02-18 04:44:00 | NOAA-21 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README6.md)
