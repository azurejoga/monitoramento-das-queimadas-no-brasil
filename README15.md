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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8a98e360-5f04-3194-afe1-fb3373738edf | -18.3671 | -50.67416 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 08487a3f-1209-3b2c-9d60-f81dcf31efae | -17.31365 | -42.67119 | 2026-07-28 04:34:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8bbcf75-ee93-38ee-a286-c606c5b6f314 | -18.36453 | -50.67998 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 952eec7c-fc25-366e-8a72-4dd1ddd1f28e | -15.8019 | -56.70248 | 2026-07-28 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 732670c4-8427-30b5-9dcb-cb7fc5ccd05c | -20.63634 | -42.70065 | 2026-07-28 04:34:00 | NPP-375D | PEDRA DO ANTA | MINAS GERAIS | Brasil | 3148806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 82d1ab14-6b1b-3b06-ba9c-de4db45b4fbc | -14.29694 | -45.64293 | 2026-07-28 04:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5821ed1-8fc7-35e6-bf5a-2705b12cefcc | -18.37926 | -50.66785 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 596a386a-522f-31c5-b91b-c6d56fec067a | -19.72235 | -47.41334 | 2026-07-28 04:34:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54d0657d-74aa-397e-b14b-b628677a8609 | -19.17104 | -42.99289 | 2026-07-28 04:34:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 80c666dc-c143-3ad7-bab9-5478e4272897 | -18.37289 | -50.66223 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 38.0 |
| befec034-4799-3259-8699-aefeae0d8cf5 | -16.86572 | -49.58524 | 2026-07-28 04:34:00 | NPP-375D | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fdf16b89-4b4b-3ed5-af5f-b332e4012cad | -15.44669 | -41.37356 | 2026-07-28 04:34:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 4ecf92e7-d0eb-37c5-8595-f4052aa18cc4 | -15.58688 | -47.71602 | 2026-07-28 04:34:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 16cfed48-3c59-3ca1-a794-704211e40296 | -15.23982 | -48.57943 | 2026-07-28 04:34:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 56e965cc-a1ed-34bf-8da2-8a11eb2d62f5 | -15.81728 | -41.89585 | 2026-07-28 04:34:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f300b85-ae09-392b-b00c-5ec93528b7f2 | -18.36578 | -50.66078 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| db565a91-1881-3362-ba25-74e3030380ac | -14.30029 | -45.64347 | 2026-07-28 04:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6f4d04a-b486-3ed7-90b0-bc0612dc3326 | -15.442 | -41.37688 | 2026-07-28 04:34:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 3a65984c-e861-34df-aec4-aac2e8221d07 | -17.33389 | -43.63401 | 2026-07-28 04:34:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 3cdfd5c1-9ddc-3f3c-bb22-6b95c7fb1982 | -15.44252 | -41.37305 | 2026-07-28 04:34:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| 5854f83f-8c11-3f4f-a132-76971ece3d32 | -15.32799 | -43.02476 | 2026-07-28 04:34:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 67c30fe2-ab99-30fd-bf90-4485bf9022b2 | -16.86707 | -49.57732 | 2026-07-28 04:34:00 | NPP-375D | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b4539721-218d-34d8-ad21-0f5a79ca429a | -15.40396 | -55.92357 | 2026-07-28 04:34:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b19512af-f6c1-3e6d-8dfa-390a08615b52 | -18.3617 | -50.67501 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 5e1737ec-9cce-3495-8db4-41980f1bba64 | -14.3035 | -58.97108 | 2026-07-28 04:34:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b44754ef-1bb6-3c5a-ba27-e0dfdc205a8a | -17.35135 | -50.3783 | 2026-07-28 04:34:00 | NPP-375D | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e3b42dc-4a77-3a5d-bcf3-3b9ea37e3c5b | -16.56662 | -51.62353 | 2026-07-28 04:34:00 | NPP-375D | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aaf27b73-9fdc-37e2-a68d-137a0a130df1 | -13.34966 | -54.28775 | 2026-07-28 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d332ca0-9f12-37c8-b9fa-cfa6658cd699 | -19.22962 | -46.96699 | 2026-07-28 04:34:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9af73b93-1fe2-3f69-a31e-96db84a3d091 | -15.24383 | -48.57629 | 2026-07-28 04:34:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eee1842e-1de4-3dcc-929f-11899e51cbb6 | -17.39889 | -47.32792 | 2026-07-28 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4d1de39-6a6b-374b-a9ee-ccfa06196b08 | -18.37645 | -50.66296 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f8367214-5d08-35e0-8497-945b323593e4 | -14.41177 | -52.11752 | 2026-07-28 04:34:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ee4f7c72-9b5f-3f32-9beb-89253cb1ceed | -13.35544 | -54.28343 | 2026-07-28 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d562bc55-d5d9-32f9-8659-b721e771cd91 | -18.37271 | -50.68411 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 185cddfa-0f26-35e0-b28e-365895e61da1 | -18.36504 | -50.66499 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7a4c93d2-085d-34b9-a491-ec1b406c884c | -15.44617 | -41.3774 | 2026-07-28 04:34:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.9 |
| c0c31d40-2239-35c8-83dd-e2343dd4a646 | -16.52735 | -47.73873 | 2026-07-28 04:34:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2d674b58-c77c-3e5e-bbca-f8862221384a | -15.81324 | -41.89521 | 2026-07-28 04:34:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a58a3bab-4c21-37ba-89a3-c3faca38bd31 | -16.37626 | -46.88303 | 2026-07-28 04:34:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c48b0113-ae30-3c64-b064-a7e7a1bf681b | -15.7645 | -48.38792 | 2026-07-28 04:34:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f39662b8-46cd-31a8-ae3d-53af14cb961c | -18.37571 | -50.66714 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d96fd3c9-2097-3f34-b786-1cd4f992d33e | -15.81721 | -41.89511 | 2026-07-28 04:34:00 | NPP-375D | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 650409ca-c56b-3c3d-b2a3-416cb2075d19 | -13.34786 | -54.28853 | 2026-07-28 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 288d4648-ae1c-35ce-bfb7-cbdf75fd4590 | -14.8405 | -46.68671 | 2026-07-28 04:34:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1375fc6d-c6c9-3350-97f2-0da435d259a4 | -18.37141 | -50.6706 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 29.8 |
| a4a8c8b7-44c0-3e42-aaa4-f0588e4c7e75 | -17.31295 | -42.67631 | 2026-07-28 04:34:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3be6de61-e04f-32df-9712-9f41954438fd | -18.3639 | -50.66224 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 4dcfde6f-3a2d-3261-9c64-8090253a8aee | -18.36673 | -50.66719 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 6ab6d905-5afe-3ab9-b5b4-91783b7bf0b2 | -18.36635 | -50.67843 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 3ff299b0-0730-3dd5-b33b-faaba8f98fcf | -15.40904 | -55.92498 | 2026-07-28 04:34:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3609f84-f7aa-3a54-9f78-701f42d3e485 | -18.38 | -50.66368 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b1ccb32b-b971-3ad8-874b-55856a78bf66 | -18.36354 | -50.67349 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ba76a988-55ec-3d04-9728-2804db645ce6 | -15.44901 | -43.81424 | 2026-07-28 04:34:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 013a812e-fc6d-3880-bb3a-98bcc1e69d0b | -18.37348 | -50.6798 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 7594a88f-672e-32d6-a513-847a2388bf31 | -18.36785 | -50.66991 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 7c53baa2-e456-3d3b-a9b1-c605a6d11c49 | -20.30115 | -46.3563 | 2026-07-28 04:34:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51a33d1e-a6ab-3113-8607-66cb4ed52524 | -19.1671 | -42.99215 | 2026-07-28 04:34:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b801dfec-19e0-3613-983f-7630d7219408 | -18.37704 | -50.6805 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 25.9 |
| f645b9fa-273f-373b-957b-4a9bb7b512fa | -15.7754 | -48.2796 | 2026-07-28 04:34:00 | NPP-375D | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 925be986-5400-3dc1-8481-955cfb3031e8 | -15.44149 | -41.38067 | 2026-07-28 04:34:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 6f33129e-bf8c-30d8-9443-45a6ed9fb15e | -18.91531 | -50.64661 | 2026-07-28 04:34:00 | NPP-375D | PARANAIGUARA | GOIÁS | Brasil | 5216304 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b37489ca-eca7-30b7-b4cf-52b8692a323a | -17.08727 | -51.73795 | 2026-07-28 04:34:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5812bb6-db75-30e1-a788-47851b79d0be | -18.37628 | -50.68481 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 2a3d9332-a9f2-35de-9654-48c1945b8d8c | -13.34484 | -54.28686 | 2026-07-28 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fd73ceca-ec6e-3b76-90d3-e40a308906d1 | -13.35267 | -54.28941 | 2026-07-28 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 672d9a00-6eca-3658-bfa5-1389fd964d89 | -20.98647 | -46.45736 | 2026-07-28 04:34:00 | NPP-375D | NOVA RESENDE | MINAS GERAIS | Brasil | 3145109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7de13c63-78ef-3a00-bd03-3d6df48420ef | -18.366 | -50.67143 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 3aa5d8be-cf6c-36ee-90ee-8b2907da2b7c | -20.20724 | -44.41244 | 2026-07-28 04:34:00 | NPP-375D | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 78217a9d-db57-36af-8709-e630d9915a92 | -13.35369 | -54.28419 | 2026-07-28 04:34:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9bbe1b6-e0a8-3262-b033-6a18d51d7dff | -15.32423 | -43.02421 | 2026-07-28 04:34:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 453ee4ee-f48d-37bb-86c1-3ef6a9a70ff8 | -17.39832 | -47.33154 | 2026-07-28 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c0350560-4b26-3e16-ba85-6214aa8f1c89 | -15.40834 | -55.9285 | 2026-07-28 04:34:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d674daa4-666c-39ef-85bc-0874249f047e | -18.85934 | -43.45464 | 2026-07-28 04:34:00 | NPP-375D | ALVORADA DE MINAS | MINAS GERAIS | Brasil | 3102407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| e1c23db0-2eee-353a-aca3-083e7df6ad5e | -17.08923 | -51.73504 | 2026-07-28 04:34:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2f539b4c-ddbe-38a9-93a4-eecfc8227aad | -17.08812 | -51.7331 | 2026-07-28 04:34:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fa43fc48-a413-3718-9b21-bb62ad6721fd | -17.30902 | -42.67573 | 2026-07-28 04:34:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 55dbc58c-3ec9-3a26-b442-2ff2b863e8ac | -18.3686 | -50.6657 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 32ddd169-c09c-386f-81f6-45cab89c69c6 | -14.41586 | -52.11832 | 2026-07-28 04:34:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 406518cd-9875-3870-9b8a-3efc18b7ab27 | -14.30977 | -58.97273 | 2026-07-28 04:34:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1086abf8-afc3-37e3-b4c5-f77b38506a62 | -13.70515 | -51.89998 | 2026-07-28 04:34:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05e3d7dc-ab22-3ad9-869a-853cce05d993 | -17.35892 | -47.08353 | 2026-07-28 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8eef47a4-745c-3dec-b6f5-02049666ccd5 | -18.37066 | -50.67485 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 29.8 |
| a38c636c-2d75-32c1-a36d-0d7b57c03f3f | -18.37778 | -50.67625 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| eec7792e-11cc-3c13-89e7-7aec46238c63 | -18.37423 | -50.67555 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 488671fa-38d0-37ca-b6d3-76d03ff7a19d | -15.79998 | -56.70218 | 2026-07-28 04:34:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8751a6b9-79ed-38c4-b64f-ed1b5b0e23ab | -18.36745 | -50.66296 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 54025763-0edc-3aaa-adfc-b66ef11a479e | -18.36526 | -50.6757 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 560f5fd9-25c6-3176-bc28-3864d4890182 | -17.30973 | -42.67057 | 2026-07-28 04:34:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6b57ff81-b6dc-3e78-b24e-b9abd212a0df | -20.30457 | -46.35686 | 2026-07-28 04:34:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2fcc1498-8114-38d9-9d51-8e327e2694a1 | -17.4013 | -47.32781 | 2026-07-28 04:34:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86a32916-3d9b-3993-886c-c2e0349265cc | -15.44566 | -41.3812 | 2026-07-28 04:34:00 | NPP-375D | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| e53e8f13-80b0-3465-a07a-d4fd99349283 | -18.36915 | -50.68341 | 2026-07-28 04:34:00 | NPP-375D | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 3bb6278c-de9f-3f1a-a672-1709b679a5f2 | -16.52344 | -47.74177 | 2026-07-28 04:34:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 642dc0d4-b828-3e7b-80d1-2d3d141bc77d | -22.06746 | -56.5313 | 2026-07-28 04:36:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0df693b8-7c67-3287-90dc-064093c07748 | -23.77957 | -49.03976 | 2026-07-28 04:36:00 | NPP-375D | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b8b433c4-3c50-302c-b675-7f8279430df8 | -23.18937 | -49.77543 | 2026-07-28 04:36:00 | NPP-375D | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4cd66f9c-19e7-3552-a84c-5597af5e01fa | -22.05921 | -56.52367 | 2026-07-28 04:36:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c1be84c2-a201-331b-934f-e87b88f4d91d | -23.97819 | -48.52718 | 2026-07-28 04:36:00 | NPP-375D | CAPÃO BONITO | SÃO PAULO | Brasil | 3510203 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d6c14cee-f71b-3e36-baf7-8d0694e33919 | -22.05808 | -56.52904 | 2026-07-28 04:36:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README16.md)
