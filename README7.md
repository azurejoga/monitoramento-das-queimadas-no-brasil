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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9aeef55-c438-301f-a771-d9a5f946eca0 | -19.25686 | -49.7523 | 2025-03-26 05:08:00 | NOAA-21 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 6dd9183e-7233-3627-9bdc-1687aa74f356 | -18.99675 | -49.85023 | 2025-03-26 05:08:00 | NOAA-21 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 7a7e32fa-ecf1-3648-8cab-0e669397d74e | -20.76699 | -46.7707 | 2025-03-26 05:08:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 11a7ea6c-ec72-31de-93ad-cb11b41ba2ad | -18.74691 | -55.75291 | 2025-03-26 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 82137ce7-33e7-39dd-8ed4-2411b7d76c8b | -18.91939 | -47.95211 | 2025-03-26 05:08:00 | NOAA-21 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1bc7fa0e-a4a6-3015-a79f-22f47e9591fe | -18.19159 | -53.4437 | 2025-03-26 05:08:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.1 |
| d4f4387a-f860-3bb4-8cd1-9c033b4bd078 | -21.25936 | -46.02739 | 2025-03-26 05:08:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7b48d6aa-121f-3d3f-8810-370392ac38a2 | -15.80696 | -58.28204 | 2025-03-26 05:08:00 | NOAA-21 | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 81ebc097-1eba-3496-ac16-7e542f1bc7ff | -25.57054 | -52.6262 | 2025-03-26 05:10:00 | NOAA-21 | RIO BONITO DO IGUAÇU | PARANÁ | Brasil | 4122156 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| add28462-9bd5-3b76-a649-c7336c6d6c71 | -31.07373 | -53.00424 | 2025-03-26 05:10:00 | NOAA-21 | PIRATINI | RIO GRANDE DO SUL | Brasil | 4314605 | 43 | 33 | nan | nan | nan | Pampa | 0.2 |
| 828b17bd-160c-371d-9b91-fcb1e7e3cadd | -29.43052 | -55.22173 | 2025-03-26 05:10:00 | NOAA-21 | SÃO FRANCISCO DE ASSIS | RIO GRANDE DO SUL | Brasil | 4318101 | 43 | 33 | nan | nan | nan | Pampa | 0.1 |
| cd7366a4-f132-3a3c-ae10-84da1af4afc4 | -30.21571 | -55.53824 | 2025-03-26 05:10:00 | NOAA-21 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 0.0 |
| 20186c24-0c24-3772-8d24-5e2b1868f204 | -31.0503 | -53.31769 | 2025-03-26 05:10:00 | NOAA-21 | PINHEIRO MACHADO | RIO GRANDE DO SUL | Brasil | 4314506 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 22eaa29e-c1fb-322a-8156-6637779e86ba | -28.26715 | -52.65781 | 2025-03-26 05:10:00 | NOAA-21 | PASSO FUNDO | RIO GRANDE DO SUL | Brasil | 4314100 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 52131fc7-c252-3c90-9cc9-78f7e250293f | -25.47076 | -54.19384 | 2025-03-26 05:10:00 | NOAA-21 | SÃO MIGUEL DO IGUAÇU | PARANÁ | Brasil | 4125704 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| a5f88ab3-b5c9-314b-b109-56e26d0a4e27 | -29.52385 | -56.71227 | 2025-03-26 05:10:00 | NOAA-21 | URUGUAIANA | RIO GRANDE DO SUL | Brasil | 4322400 | 43 | 33 | nan | nan | nan | Pampa | 0.1 |
| 1091e352-c771-3c18-8216-dfdff8d6006f | -28.55818 | -53.50122 | 2025-03-26 05:10:00 | NOAA-21 | PEJUÇARA | RIO GRANDE DO SUL | Brasil | 4314308 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 21fe7785-5eef-31aa-8eb2-ce7ab55d8fdc | -30.79769 | -54.97686 | 2025-03-26 05:10:00 | NOAA-21 | DOM PEDRITO | RIO GRANDE DO SUL | Brasil | 4306601 | 43 | 33 | nan | nan | nan | Pampa | 0.1 |
| 3c43f910-4573-3d1d-b2fa-2bc3fd2b08dd | -28.05543 | -53.57125 | 2025-03-26 05:10:00 | NOAA-21 | CONDOR | RIO GRANDE DO SUL | Brasil | 4305702 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5336a22e-7976-36ca-bbc7-94d8e2727fc6 | -30.81667 | -52.23272 | 2025-03-26 05:10:00 | NOAA-21 | AMARAL FERRADOR | RIO GRANDE DO SUL | Brasil | 4300638 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| e92bbd00-52a1-34fe-b1f8-1fbab79d6979 | -31.05063 | -53.31772 | 2025-03-26 05:10:00 | NOAA-21 | PINHEIRO MACHADO | RIO GRANDE DO SUL | Brasil | 4314506 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| 0d167fcf-0a32-3adf-9612-99dc5188b1b9 | -30.4617 | -51.58678 | 2025-03-26 05:10:00 | NOAA-21 | SERTÃO SANTANA | RIO GRANDE DO SUL | Brasil | 4320552 | 43 | 33 | nan | nan | nan | Pampa | 0.3 |
| bf442c3b-ce01-399d-9e46-362fbdd985df | -27.13411 | -53.5399 | 2025-03-26 05:10:00 | NOAA-21 | SÃO JOÃO DO OESTE | SANTA CATARINA | Brasil | 4216255 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b6153ec1-e20e-3a35-b534-42763afae5ad | -30.32825 | -55.1203 | 2025-03-26 05:10:00 | NOAA-21 | ROSÁRIO DO SUL | RIO GRANDE DO SUL | Brasil | 4316402 | 43 | 33 | nan | nan | nan | Pampa | 0.1 |
| ae355f81-9039-35f8-9d0e-593b0b6d0dda | -29.86639 | -51.0949 | 2025-03-26 05:10:00 | NOAA-21 | GRAVATAÍ | RIO GRANDE DO SUL | Brasil | 4309209 | 43 | 33 | nan | nan | nan | Pampa | 0.1 |
| fea0cfc6-0a9f-32d7-85eb-7320b265377a | -25.28348 | -48.67438 | 2025-03-26 05:10:00 | NOAA-21 | ANTONINA | PARANÁ | Brasil | 4101200 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 52d1fc4f-3c6e-33c9-b80c-3905d724c371 | -25.01038 | -53.22967 | 2025-03-26 05:10:00 | NOAA-21 | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 87d81214-d2c3-358b-9650-ad18ce316a0f | -27.83718 | -53.97647 | 2025-03-26 05:10:00 | NOAA-21 | INHACORÁ | RIO GRANDE DO SUL | Brasil | 4310413 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| de33f049-f494-3aec-8f9e-311422eb1b9c | -30.34102 | -51.64391 | 2025-03-26 05:10:00 | NOAA-21 | MARIANA PIMENTEL | RIO GRANDE DO SUL | Brasil | 4311981 | 43 | 33 | nan | nan | nan | Pampa | 0.1 |
| 285eaafa-7914-34cd-a034-f400ae39e9a3 | -28.20201 | -53.63191 | 2025-03-26 05:10:00 | NOAA-21 | AJURICABA | RIO GRANDE DO SUL | Brasil | 4300208 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| 8de6f8f9-01a2-390d-87ad-d99317c9b368 | -26.94235 | -53.04768 | 2025-03-26 05:10:00 | NOAA-21 | SAUDADES | SANTA CATARINA | Brasil | 4217303 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.1 |
| 59efcd88-73a7-3824-81ca-be251517bb50 | -32.57954 | -53.2755 | 2025-03-26 05:12:00 | NOAA-21 | JAGUARÃO | RIO GRANDE DO SUL | Brasil | 4311007 | 43 | 33 | nan | nan | nan | Pampa | 0.2 |
| 53437c79-1812-3490-b322-5055d4822bce | 3.98031 | -61.50754 | 2025-03-26 05:25:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 20f3ee18-85eb-3411-839f-2f551ea5b71b | 4.65321 | -60.91547 | 2025-03-26 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 861d0578-53ce-32f8-ab00-aee3ae815fa3 | 3.99 | -61.50223 | 2025-03-26 05:25:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb3b0cfd-fad4-3d0c-9c0b-0018afc124f5 | 3.99115 | -61.50964 | 2025-03-26 05:25:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a7f5c74-cce1-32aa-ab06-6239e6984f51 | 3.03145 | -61.33414 | 2025-03-26 05:25:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0b42564-0450-3401-aea5-88c1983a100f | 3.98658 | -61.50277 | 2025-03-26 05:25:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f07cb3e-2656-3df3-81f9-266c06686eaa | 2.61419 | -61.50156 | 2025-03-26 05:25:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| db88a6fe-34b5-38cf-8461-ba720708d129 | 4.07893 | -61.58017 | 2025-03-26 05:25:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0730a08d-1ace-3340-9cf1-e91200cbe7db | 3.98715 | -61.50647 | 2025-03-26 05:25:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ff697bf-af99-3c8b-ac94-561783c065bf | 4.67903 | -60.90381 | 2025-03-26 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e421664-168b-3b52-a2e9-bf8dc6c23291 | 2.57216 | -60.70005 | 2025-03-26 05:25:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a871c1f8-b6fc-366b-9928-fb8a1115d209 | 4.67283 | -60.90838 | 2025-03-26 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e56d4193-7dda-3ec1-964c-d37e1473df82 | 3.96548 | -61.50228 | 2025-03-26 05:25:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 81e4db39-195d-38db-a77f-4f446a31b27e | 4.0955 | -61.55095 | 2025-03-26 05:25:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1077de73-8a05-3df1-b03d-5a75c1319d7b | 4.65711 | -60.91833 | 2025-03-26 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 45807c4f-d021-306c-a073-7f7a1a61d518 | 3.98316 | -61.5033 | 2025-03-26 05:25:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6ef44c94-43e5-3787-ba1a-74615d17d5b8 | 3.97175 | -61.49753 | 2025-03-26 05:25:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c637a28-5fbb-30cc-a2c2-908e7db2e518 | 3.97974 | -61.50384 | 2025-03-26 05:25:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3b263fc2-6e13-39ff-b6d3-05c6c2b14312 | 4.65937 | -60.91062 | 2025-03-26 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6b9ae379-aa90-3e5d-a54a-f3d2f8bce270 | 4.65656 | -60.91482 | 2025-03-26 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3b6f7972-012e-3de3-9671-e40643df75a6 | 4.66609 | -60.90944 | 2025-03-26 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e18bb2a-b2a7-3eec-a47a-b330a5fa3284 | 3.96205 | -61.50282 | 2025-03-26 05:25:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d436ec4a-d5a1-31c7-bd8c-88fa1fbde3bd | 3.03483 | -61.33362 | 2025-03-26 05:25:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ff6a935-c871-38c2-8e6b-86ef363105a9 | 3.96149 | -61.49914 | 2025-03-26 05:25:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ab112641-8978-38ef-9b3a-fb3c41f3aa50 | 3.97631 | -61.50437 | 2025-03-26 05:25:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ed250996-18aa-31f9-a0fc-7dc4bdf583f8 | 4.09608 | -61.55468 | 2025-03-26 05:25:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c62e821b-f1e8-3f25-945b-50c51ca36be7 | 3.97232 | -61.50121 | 2025-03-26 05:25:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88fad7ba-7582-356a-aadf-4422506e443a | 4.66272 | -60.90997 | 2025-03-26 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b9535886-81b8-3cf1-8b2a-d88ea95f2cd0 | 4.65376 | -60.91899 | 2025-03-26 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1d2b281e-cf62-3f48-9a33-dde4d058048e | 2.6108 | -61.50208 | 2025-03-26 05:25:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e5f41368-6950-30a6-8035-2d90bd2d7343 | 3.97289 | -61.50491 | 2025-03-26 05:25:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fa734cb1-356d-3bda-bffd-d4c93ab23ace | 3.97574 | -61.50068 | 2025-03-26 05:25:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17f49108-6ce5-35de-9a26-287071e4505d | 3.98373 | -61.50701 | 2025-03-26 05:25:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8db17282-bef3-3800-88a4-b03b0a3202d5 | 4.67848 | -60.90029 | 2025-03-26 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a01395c-e7f8-30f7-869f-99abb3816715 | 2.57162 | -60.69657 | 2025-03-26 05:25:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f47b6e52-7a8c-362d-86d1-a19e152618eb | 4.6762 | -60.90784 | 2025-03-26 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8853e221-62de-3e4f-a927-2ced3a4c6ea7 | 4.67566 | -60.90437 | 2025-03-26 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0195851b-3176-31ec-81bc-b16be517374b | 4.68239 | -60.90325 | 2025-03-26 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b84f8fd2-b170-3907-9c52-329f934b6279 | 4.66946 | -60.9089 | 2025-03-26 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 98419d36-c478-3f75-a6fc-d24d74f04305 | 4.65991 | -60.91413 | 2025-03-26 05:25:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf4cbcc2-2ddd-3789-b9ed-4e7b959c5d0d | 1.83162 | -60.8755 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4469ed50-80f4-397a-8165-2a2afc5d5f36 | 1.82883 | -60.87948 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4cddef59-bbdd-3098-bd2c-e13add74c6b6 | 2.16878 | -61.82281 | 2025-03-26 05:27:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3178fe07-2f10-38ba-b1e6-284ac46a5641 | 2.45917 | -61.31567 | 2025-03-26 05:27:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dcc5673e-46d8-3c9c-8fc2-e2b7cf1fd11e | 1.81938 | -60.88453 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 414ff594-ecff-3224-bc6f-067fc6657854 | 2.17219 | -61.82228 | 2025-03-26 05:27:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a153ce2-fd70-3ad2-acbf-9b972954f1e2 | 1.05607 | -60.55067 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 794eb34d-b442-350c-8848-b23223f23c93 | 1.82659 | -60.88697 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 206fe1aa-39e1-3148-87c5-67402f1e917c | 1.05329 | -60.55463 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b3fd101-cb0f-375f-96d5-269fcd9085e8 | 1.05275 | -60.55119 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93a47b4e-535e-3d94-97ed-09930c360578 | 1.82162 | -60.87704 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3db5cc52-10bb-3029-9b31-abfba2f3e5ec | -1.7271 | -54.33629 | 2025-03-26 05:27:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f8376e39-bb1c-3b91-aa29-438775074f49 | 1.33183 | -60.71195 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf276381-f677-36d5-9017-7c3311950523 | 1.94974 | -61.20167 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00c230d7-ed75-34f8-8656-6b1bd5e5e084 | 1.10894 | -60.54232 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3893dc0-91aa-3031-b0f0-f28258c40ef4 | 2.19438 | -61.80762 | 2025-03-26 05:27:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0e5a3792-97b6-3622-b59a-c4b5f9755936 | 1.10249 | -59.3466 | 2025-03-26 05:27:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 864d0620-8399-3c11-be2c-d491e041202e | 1.50087 | -60.75314 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd5040dc-6757-3bbb-accb-d7b1a22fb5ac | 1.82938 | -60.88297 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3cd87baf-12cb-372e-8114-80bea5036eac | 2.19779 | -61.80711 | 2025-03-26 05:27:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2fad8b2e-4910-3777-9bd1-442134ac9651 | 1.81774 | -60.87408 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c2916b5f-db70-35ed-a06c-3ccd47c09aa2 | 1.82271 | -60.88401 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7487d4ab-6177-3996-b464-3ee6b0f5e1b6 | 1.83216 | -60.87897 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1b46fd77-4b93-3fe2-99d9-237173e23499 | 1.8255 | -60.88001 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7329b687-9a0c-3cb1-a711-dc0d6e22131e | 1.82828 | -60.876 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fca5cf3e-3cf9-352a-9e09-1ff361926722 | 1.05661 | -60.55411 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2d7ba36-4c47-3c10-82ff-c688e409f783 | 1.81829 | -60.87756 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ac03e442-c9dd-3a07-86d6-0a84427583a1 | 1.82993 | -60.88645 | 2025-03-26 05:27:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |


[Clique aqui para ver as próximas entradas](README8.md)
