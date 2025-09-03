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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 685c3464-8f11-3dad-b772-46ff1a52bc45 | -22.18031 | -48.83078 | 2025-09-03 03:36:00 | NPP-375D | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| 1e85c513-ee0c-30b5-936a-78d72dbc0d34 | -20.59984 | -45.11351 | 2025-09-03 03:36:00 | NPP-375D | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| e3db2412-3452-32cb-8f0f-087839c65a4e | -22.1756 | -48.8236 | 2025-09-03 03:36:00 | NPP-375D | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| a7f7150a-1f2f-3263-9430-7779eb80fc01 | -23.0397 | -45.53718 | 2025-09-03 03:36:00 | NPP-375D | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ec9c2d47-601f-3393-b568-16574010dc38 | -22.39833 | -44.46875 | 2025-09-03 03:36:00 | NPP-375D | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 9afcb482-9e6c-38f8-a4a2-b63279128d84 | -20.40396 | -45.69536 | 2025-09-03 03:36:00 | NPP-375D | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 84672545-8d12-3e16-b198-eb8b457d75f7 | -22.00811 | -45.05547 | 2025-09-03 03:36:00 | NPP-375D | CONCEIÇÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3117702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7601699c-ab09-33d8-8a19-2a1f46852f7f | -22.89758 | -43.58497 | 2025-09-03 03:36:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6a2e4ebe-c86f-3b7b-b59d-0a4d01756585 | -22.00725 | -45.05944 | 2025-09-03 03:36:00 | NPP-375D | CONCEIÇÃO DO RIO VERDE | MINAS GERAIS | Brasil | 3117702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 975834c2-59ee-3e66-bc63-3982f22c1feb | -22.75427 | -47.27363 | 2025-09-03 03:36:00 | NPP-375D | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5680c2c8-7b51-318d-a602-05c1f6f75fd3 | -20.89629 | -50.09809 | 2025-09-03 03:36:00 | NPP-375D | TURIÚBA | SÃO PAULO | Brasil | 3555208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 60129d3c-43df-32a3-9f66-2d2c9c6fa980 | -20.59451 | -45.11231 | 2025-09-03 03:36:00 | NPP-375D | CAMACHO | MINAS GERAIS | Brasil | 3110400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 32029ec9-3ec4-31d4-bc00-0747de0e1c95 | -17.36251 | -49.17531 | 2025-09-03 03:36:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d7ca3887-9168-33fa-941f-744df822a7d0 | -17.92043 | -47.21226 | 2025-09-03 03:36:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 48c4b90b-77bf-3746-ba62-727a2c96fce4 | -18.06679 | -45.99182 | 2025-09-03 03:36:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dac29f50-596d-3bd6-8d26-b0e408cce6c3 | -17.94423 | -47.22519 | 2025-09-03 03:36:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| efd3ed9f-67f7-310a-b8d0-31762fd62c0b | -17.93921 | -47.21783 | 2025-09-03 03:36:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1500f470-2701-3c9b-b3f6-53a5620db6d0 | -18.0678 | -45.98728 | 2025-09-03 03:36:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7902cb79-efb4-3459-aebd-187b1b80f737 | -19.13132 | -47.70251 | 2025-09-03 03:36:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e6eae71-6a00-3753-891c-67c801f559ca | -17.5398 | -47.57997 | 2025-09-03 03:36:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2f42ad5-ed80-3f86-b1c8-7d6e9eeb4c7a | -19.13905 | -47.69817 | 2025-09-03 03:36:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2fcf523c-6a23-35e9-8e61-292d680109f5 | -18.07266 | -45.9933 | 2025-09-03 03:36:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b0de5d6-996e-3b4d-a47e-8cfbadb7dbbd | -17.53846 | -47.58588 | 2025-09-03 03:36:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db8b469a-3049-364a-9957-7c5ca7f40824 | -19.38484 | -49.07049 | 2025-09-03 03:36:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1f15d055-c59d-3e6d-9be7-b36c828e4be8 | -17.94305 | -47.23042 | 2025-09-03 03:36:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dc4c0efb-964c-3c86-9390-175c76e6bbda | -17.53343 | -47.57775 | 2025-09-03 03:36:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a5d37757-09e2-3dc5-8e93-9aa3acc2c60f | -19.74716 | -43.30949 | 2025-09-03 03:36:00 | NPP-375D | SÃO GONÇALO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3161908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 059cadca-e91c-3b5e-a931-d64d00ea7ab5 | -17.94814 | -47.23752 | 2025-09-03 03:36:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4ac91b9f-e798-30cf-9c15-e35b3d81b896 | -19.74947 | -43.29827 | 2025-09-03 03:36:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 7a95b6e7-4e28-3ea5-a311-ab0daf35cbf0 | -19.42317 | -45.56898 | 2025-09-03 03:36:00 | NPP-375D | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 653df75b-a8e8-33bd-9139-7663a7354c0d | -18.06983 | -45.97811 | 2025-09-03 03:36:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 52311bdf-dd78-327a-8429-91568c2f54d3 | -17.91416 | -47.21045 | 2025-09-03 03:36:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b1d4d42-5b80-3c0a-b7ad-cdea8ded54cb | -19.74234 | -43.30832 | 2025-09-03 03:36:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b6fbe559-5b5b-33a0-8812-2e6c23eca452 | -17.92163 | -47.207 | 2025-09-03 03:36:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 21380f10-60aa-389a-a45a-776e4d829ece | -17.933 | -47.21578 | 2025-09-03 03:36:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9d1be6cd-95ce-3a49-92b0-4cda7756ffd8 | -17.947 | -47.24252 | 2025-09-03 03:36:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 35f815ad-e31b-343b-9299-503aa02af999 | -17.95312 | -47.24509 | 2025-09-03 03:36:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95d11b7d-47b6-36be-9cae-bcc82b501070 | -17.53211 | -47.58354 | 2025-09-03 03:36:00 | NPP-375D | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8f09ab96-b4ee-3610-9e2e-89538cdb4849 | -18.06579 | -45.99635 | 2025-09-03 03:36:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 05061253-9a30-3085-86ef-790a1a66ac4b | -19.7435 | -43.30267 | 2025-09-03 03:36:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| aecc8fc6-6733-3b6b-afd0-cccda5649ff6 | -19.75543 | -43.2939 | 2025-09-03 03:36:00 | NPP-375D | SÃO GONÇALO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3161908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 16f87629-f59d-3bb1-a137-da43bc663ec0 | -19.75428 | -43.29948 | 2025-09-03 03:36:00 | NPP-375D | SÃO GONÇALO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3161908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f0202c8c-2643-35f1-aeaa-8970969ef28a | -19.752 | -43.31058 | 2025-09-03 03:36:00 | NPP-375D | SÃO GONÇALO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3161908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5ba1cfbc-dacd-3d7e-977c-1c2fcc623829 | -19.36633 | -49.11517 | 2025-09-03 03:36:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0c63997f-9f9d-32b3-ad59-29f69767e28d | -19.74468 | -43.29696 | 2025-09-03 03:36:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 1d65e487-5a2a-38a5-9f7d-a5beb42fcc42 | -19.68096 | -43.92443 | 2025-09-03 03:36:00 | NPP-375D | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99c49f7b-f54f-36ff-872d-1fcc34418739 | -19.42879 | -45.57023 | 2025-09-03 03:36:00 | NPP-375D | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 09545129-773d-3c37-8eac-3753bf585c05 | -19.74592 | -43.29093 | 2025-09-03 03:36:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 60d25639-d244-32bb-a403-cded58e1f4d5 | -18.06881 | -45.98269 | 2025-09-03 03:36:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| fede9974-e5f9-32d0-8571-300ff6450b72 | -19.1376 | -47.70446 | 2025-09-03 03:36:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1aad7d93-8647-38f6-bf85-9ba720216390 | -19.74832 | -43.30387 | 2025-09-03 03:36:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 84dc68ea-cc2d-33db-98c6-afa0657e821f | -19.42569 | -45.56758 | 2025-09-03 03:36:00 | NPP-375D | DORES DO INDAIÁ | MINAS GERAIS | Brasil | 3123205 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9326753-751c-3e29-9859-5949619ba06e | -19.75064 | -43.29257 | 2025-09-03 03:36:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.3 |
| 68b08b6b-479a-331f-ba9f-9030cd74a705 | -17.93416 | -47.21066 | 2025-09-03 03:36:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b93dfa3b-dbb2-3536-8bfd-955c504c8659 | -23.76466 | -51.63184 | 2025-09-03 03:38:00 | NPP-375D | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 3b93953e-8475-34ad-8b6b-cfdf710a8651 | -25.0444 | -49.2732 | 2025-09-03 03:38:00 | NPP-375D | CERRO AZUL | PARANÁ | Brasil | 4105201 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f271291f-5993-3991-8ea9-aa8400649889 | -23.76664 | -51.62446 | 2025-09-03 03:38:00 | NPP-375D | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| cad3a4ef-25b6-3356-a59f-5a475d40e8ad | -23.92676 | -48.86082 | 2025-09-03 03:38:00 | NPP-375D | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c90f67c7-f463-3c4f-8cda-8388b15f1357 | -23.77142 | -51.63527 | 2025-09-03 03:38:00 | NPP-375D | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| 19731b3a-357f-35d6-a158-dbceabc86209 | -23.77342 | -51.62778 | 2025-09-03 03:38:00 | NPP-375D | MARUMBI | PARANÁ | Brasil | 4115507 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.2 |
| a5033c5e-4a9c-3e66-abfb-398eeabb921e | -12.9382 | -56.9856 | 2025-09-03 03:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 6b5777d6-25fe-39fd-b421-b73b44d68126 | -3.212 | -47.1357 | 2025-09-03 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| b3b5212e-58a3-3e71-9be2-b7cf25447716 | -12.938 | -57.0057 | 2025-09-03 03:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 7d8ee0bf-7921-38df-a21a-345c07e9d81b | -12.9573 | -56.9839 | 2025-09-03 03:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 2c166a9a-acb1-3aa2-b384-a78f577c2376 | -3.2305 | -47.135 | 2025-09-03 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 167.0 |
| ae2c1d89-0517-323c-9c5c-b16499fe81e7 | -19.7408 | -43.3034 | 2025-09-03 03:40:00 | GOES-19 | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 54.9 |
| c308570e-9eff-3e3f-845d-e721dc5f6a99 | -3.2306 | -47.1131 | 2025-09-03 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 3159405a-cee9-3dcd-8c2a-9941998496c4 | -22.1777 | -48.8368 | 2025-09-03 03:40:00 | GOES-19 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 66.8 |
| 976d823f-1d84-3077-be93-0c61f14751e5 | -12.9385 | -56.9655 | 2025-09-03 03:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| fa5e26d2-1fa3-3319-9c3f-497acf30b1d9 | -10.45 | -54.7785 | 2025-09-03 03:40:00 | GOES-19 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 28.7 |
| ee22ca11-b6d6-373f-a8ef-f0ee8737b0dd | -22.1784 | -48.8134 | 2025-09-03 03:50:00 | GOES-19 | BORACÉIA | SÃO PAULO | Brasil | 3507308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 68.3 |
| d775e5a6-33e4-3c9b-bae4-1293e0c24291 | -3.212 | -47.1357 | 2025-09-03 03:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 4a649522-7865-35ee-b71e-4cad54f95534 | -3.2305 | -47.135 | 2025-09-03 03:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 138.4 |
| 4cb8c115-6a26-353d-8901-f8ca08a85072 | -3.2306 | -47.1131 | 2025-09-03 03:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| eb539c77-960d-3b52-96fd-8835d6b45428 | -12.9382 | -56.9856 | 2025-09-03 03:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 713db2c9-5a02-3a64-8560-ed6bdcfb63c5 | -22.1777 | -48.8368 | 2025-09-03 03:50:00 | GOES-19 | PEDERNEIRAS | SÃO PAULO | Brasil | 3536703 | 35 | 33 | nan | nan | nan | Mata Atlântica | 115.0 |
| f602e557-8ff8-36d8-a527-db0bc38d2c7e | -12.9385 | -56.9655 | 2025-09-03 03:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 15110d0e-974a-3c5f-8dcf-d0f53bf295d3 | -2.55665 | -47.71215 | 2025-09-03 03:51:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42a3da0b-7b20-325d-b279-29f77305e307 | -2.13079 | -48.01085 | 2025-09-03 03:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ba01ea5-a875-3aa5-8846-7cfe1a317dc1 | -3.19534 | -40.74175 | 2025-09-03 03:51:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 69f4a26d-e292-3a08-8194-a2401bd98d96 | -3.35398 | -43.37891 | 2025-09-03 03:51:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 162680db-c484-35dd-8326-39cde62758b8 | -2.55453 | -47.71589 | 2025-09-03 03:51:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0b15f64-b924-3def-9875-c2b13c9f6a93 | -3.29326 | -42.65097 | 2025-09-03 03:51:00 | NOAA-20 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9e1e07de-090b-3599-a935-691f0cc23c17 | -2.19841 | -47.99442 | 2025-09-03 03:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0666c7e-9fe2-3960-9fbb-8565e0cbf7f4 | -2.19948 | -47.99646 | 2025-09-03 03:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12a3df54-87ca-3475-b553-aaed0fb95388 | -2.19771 | -47.9986 | 2025-09-03 03:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4aa1e87d-1db2-3bae-a0ab-e9fb4603235c | -2.13736 | -48.00764 | 2025-09-03 03:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b82da7d4-5791-3dbf-842a-cb2eec6fc90e | -2.1988 | -48.00065 | 2025-09-03 03:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e104efcb-5d0e-3e4b-b021-031e88ff9790 | -2.13666 | -48.01186 | 2025-09-03 03:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8b18370e-e0f9-3107-8291-8b17b5a782df | -2.44107 | -47.33254 | 2025-09-03 03:51:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e73bf8bf-66cf-31c7-a737-36130bd93a3d | -2.55596 | -47.71616 | 2025-09-03 03:51:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7867318a-44c0-3bfb-a3fe-f865103bf5a2 | -4.15809 | -38.21085 | 2025-09-03 03:51:00 | NOAA-20 | CASCAVEL | CEARÁ | Brasil | 2303501 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e9c989ce-b95a-3738-8237-6cd37d22ae73 | -2.78639 | -41.87332 | 2025-09-03 03:51:00 | NOAA-20 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 154f354e-15b5-3b69-a2a4-9df922c6dbf6 | -3.1996 | -40.7382 | 2025-09-03 03:51:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 4e33d391-8fd6-32bd-905d-73a4083b00d0 | -2.56025 | -47.71694 | 2025-09-03 03:51:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34aee111-f7c8-3734-bf30-34805e39eaf4 | -3.44923 | -38.97942 | 2025-09-03 03:51:00 | NOAA-20 | PARACURU | CEARÁ | Brasil | 2310209 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d808a2c4-917d-3520-84bc-11626117cc11 | -2.1315 | -48.00661 | 2025-09-03 03:51:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38a439b4-c500-3dee-9c4d-bdb715f0e73a | -2.44171 | -47.32877 | 2025-09-03 03:51:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1b1ca950-799b-3dc5-841c-5747d3238cb8 | -3.19601 | -40.73762 | 2025-09-03 03:51:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 4.8 |
| cc8aacd9-6f57-3f32-8186-9e1201925883 | -3.19466 | -40.7459 | 2025-09-03 03:51:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |


[Clique aqui para ver as próximas entradas](README28.md)
