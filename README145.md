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

## Dados Diários - Página 145

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8d933a5b-6929-3ed4-a06d-66a0cac7ff39 | -14.4951 | -48.4106 | 2025-10-02 12:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 85.3 |
| f721595a-1596-3db7-9fa9-602ad5fe9fc2 | -9.9365 | -43.7657 | 2025-10-02 12:10:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 84.2 |
| a1c70a18-fc93-377a-9bbd-a9ea4595605c | -7.7944 | -42.5132 | 2025-10-02 12:10:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 119.7 |
| d853a956-a1de-3a69-beb0-1685976d20f0 | -8.8926 | -46.6296 | 2025-10-02 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 116.4 |
| fc05887d-3c17-3191-9d97-8a7574ddbb9b | -8.8929 | -46.6072 | 2025-10-02 12:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 135.7 |
| 5a60e274-0525-3d4e-93f1-b5434391396a | -9.336 | -45.9305 | 2025-10-02 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 284.2 |
| dfa0fe02-cffe-3cb4-a41d-c6351e90ccd7 | -11.9272 | -47.8941 | 2025-10-02 12:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 8445f7b2-9952-340f-9a52-7d712b7219f5 | -9.9365 | -43.7657 | 2025-10-02 12:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 145.3 |
| fc4bc97c-cc8b-30eb-ae57-5349a070fc62 | -16.0567 | -45.7204 | 2025-10-02 12:20:00 | GOES-19 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 295.7 |
| 57e9da80-e8e1-3e51-a2d0-3da6ee06ea35 | -14.425 | -46.1381 | 2025-10-02 12:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 68e62d9d-53b9-3afc-9737-29d9ddea0c05 | -10.2123 | -48.1909 | 2025-10-02 12:20:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 8657e1a1-5495-3f05-8cf3-744418b927c4 | -9.4272 | -47.5722 | 2025-10-02 12:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 184.9 |
| 7c61003f-0c23-3833-b4c8-c960fba60013 | -16.0221 | -50.8989 | 2025-10-02 12:20:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 50b42a63-ba4f-37c3-9e4b-faaeb442afee | -9.9372 | -43.7187 | 2025-10-02 12:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 172.1 |
| 88edf4aa-3924-3bd0-85a0-b631728dea06 | -13.7962 | -47.5362 | 2025-10-02 12:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 63.0 |
| e0793dd7-1858-32f6-834b-ed0264b41286 | -14.1921 | -46.1321 | 2025-10-02 12:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 170.4 |
| 68ea6828-b9be-38f1-818e-00fc581262fa | -9.3392 | -45.7039 | 2025-10-02 12:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 06e261c8-4084-3973-acea-b675adfebe06 | -14.1917 | -46.1552 | 2025-10-02 12:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 186.8 |
| 4c6d3d4e-a445-3c6a-9445-0172e64722cb | -14.4947 | -48.4329 | 2025-10-02 12:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 82.6 |
| fc163e5d-c8e5-3614-83c9-e28f12ac4f4f | -14.3704 | -45.9634 | 2025-10-02 12:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 1be2779c-c987-32c1-ac6e-6f563252650c | -14.4951 | -48.4106 | 2025-10-02 12:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 3f95cc36-a8aa-3129-8101-636ca3b003ab | -10.212 | -48.2128 | 2025-10-02 12:20:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| fb4fff92-c867-35f0-919a-b7bdd43de1ca | -13.0119 | -45.1988 | 2025-10-02 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 160.5 |
| 518a304b-3b51-3d1a-b802-85c81bd65dcf | -7.8882 | -47.281 | 2025-10-02 12:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 3a243779-1b5f-3fc9-92dc-778d39d86c75 | -9.9178 | -43.7447 | 2025-10-02 12:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 233.4 |
| 7ba81d5d-6824-38ba-97bc-6edd81ccc9a6 | -14.927 | -47.2387 | 2025-10-02 12:20:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 64346ad4-6a43-3988-8cb5-12f37080574c | -11.8234 | -45.0364 | 2025-10-02 12:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 0a5167db-5d2e-38f5-ad0c-f838eeb2081a | -14.2924 | -45.977 | 2025-10-02 12:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 85.0 |
| e524137a-dc9d-3c33-ae9c-79ceaf57dcc5 | -14.4753 | -48.436 | 2025-10-02 12:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 0eb3ee86-f121-3a1b-83b6-5dc483f14388 | -9.3364 | -45.9079 | 2025-10-02 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| 4d786e2b-67c2-337a-b92c-4d6cb40edc94 | -15.2542 | -49.3104 | 2025-10-02 12:20:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 90473672-6493-3d29-9503-0628efc5e98d | -9.9182 | -43.7212 | 2025-10-02 12:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 124.8 |
| 62ac2e72-a52c-331a-b939-905f779491ca | -14.3709 | -45.9403 | 2025-10-02 12:20:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 109.3 |
| bc730741-92ec-3ee2-8cbe-acf34e48cd99 | -9.08 | -46.7215 | 2025-10-02 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.8 |
| fb3c8707-2f36-38f6-8f5d-8ab82ef1e9d2 | -12.9507 | -46.3789 | 2025-10-02 12:20:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 96.5 |
| b4f84cb7-c0d2-381b-93df-950465015908 | -14.8212 | -45.8143 | 2025-10-02 12:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 4e9fa1f5-2c6b-3ab5-b3d4-5fb897e99743 | -11.1746 | -47.2805 | 2025-10-02 12:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| ce6284fb-e93d-3c7e-9a4c-dbaf9c28d4fd | -13.1542 | -47.8568 | 2025-10-02 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 731665e9-3ddb-3ad5-a90a-e6484746c7df | -11.9276 | -47.8719 | 2025-10-02 12:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 518.0 |
| c8396fff-2ebe-37bc-bb78-b0596e9c9554 | -13.1743 | -47.8093 | 2025-10-02 12:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 81055618-c233-335d-823b-5e46250435d6 | -14.4757 | -48.4137 | 2025-10-02 12:20:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 80c4c548-2896-3d3d-802e-f51fa8566062 | -10.3061 | -48.2461 | 2025-10-02 12:20:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 5701a7b2-89c1-3118-96b8-395178d023a7 | -14.2116 | -46.1288 | 2025-10-02 12:20:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 162.5 |
| 0a9981f6-ad46-35e5-ad0a-8d2f8395dbf8 | -13.0114 | -45.222 | 2025-10-02 12:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 224.9 |
| f2b55318-87b5-32ee-8f6b-d5d28eaa28ec | -9.4086 | -47.5521 | 2025-10-02 12:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 168.0 |
| d23407a8-5a57-3a48-a5bb-92ae74e76af2 | -9.9369 | -43.7422 | 2025-10-02 12:20:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 290.6 |
| 0ecd2d80-8a4a-34f1-9750-8a71b3a85ef4 | -7.8879 | -47.3031 | 2025-10-02 12:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| fb0a0aec-dd3f-3c87-8acc-9839dc9ecbbe | -11.9085 | -47.8745 | 2025-10-02 12:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 115.2 |
| 598292aa-c17e-3aea-bca8-b0dbefc3242e | -9.4083 | -47.5742 | 2025-10-02 12:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 197.8 |
| 58d64c0f-0f01-39d8-993e-b0ee761044be | -16.0567 | -45.7204 | 2025-10-02 12:30:00 | GOES-19 | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 464.3 |
| f07c2fbc-7580-37cb-8c4e-7f9d375c2d00 | -11.1746 | -47.2805 | 2025-10-02 12:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 22f62005-df9a-3096-a2e9-7ca0672af176 | -13.3203 | -47.2048 | 2025-10-02 12:30:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 68.4 |
| cd900253-b424-38d5-af15-4c6c6822924b | -13.0119 | -45.1988 | 2025-10-02 12:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 142.2 |
| 0c0dad23-655e-3f33-b2b9-6da81cb7f443 | -11.9085 | -47.8745 | 2025-10-02 12:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 797f3721-c048-3a13-a033-3930370e7179 | -9.336 | -45.9305 | 2025-10-02 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| ddd568d0-691b-347a-a669-9abe653ef691 | -12.9024 | -46.9073 | 2025-10-02 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 853fa848-1c8c-3e21-afe3-f517b858b0b2 | -15.2542 | -49.3104 | 2025-10-02 12:30:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 902f9a2b-e342-3ce7-8406-72f3063df803 | -14.3704 | -45.9634 | 2025-10-02 12:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 180.1 |
| 0d18ba69-6598-3c8d-bef7-3a9f882e3a3f | -9.9365 | -43.7657 | 2025-10-02 12:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 153.3 |
| 5363e3a5-7730-39f7-803e-9a275864ae4f | -10.3061 | -48.2461 | 2025-10-02 12:30:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 70.5 |
| b5820907-65d3-3425-8745-688f1e57c354 | -9.0803 | -46.6992 | 2025-10-02 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| cea57297-1e68-39ab-8d7d-8731bfc2f267 | -14.927 | -47.2387 | 2025-10-02 12:30:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 0b57b57c-fd56-33e7-b54d-406504accf3d | -15.2738 | -49.3073 | 2025-10-02 12:30:00 | GOES-19 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 972b13af-3dce-3476-9950-ced3bbf54e9d | -7.7752 | -42.539 | 2025-10-02 12:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 224.6 |
| ad6e63d3-cc16-32a0-b971-f502735515bc | -14.1921 | -46.1321 | 2025-10-02 12:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 170.1 |
| e3e2ce33-6a32-32ca-ade7-6bae488cd8f3 | -7.7944 | -42.5132 | 2025-10-02 12:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 140.7 |
| 869bb7dd-38f2-3be7-b6f2-72d31b7aed17 | -14.2924 | -45.977 | 2025-10-02 12:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 89.6 |
| e193834f-25bd-3204-8040-834f548db862 | -8.6722 | -47.6924 | 2025-10-02 12:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 83211e6c-344f-38fa-8da5-d4ab8106403b | -11.8234 | -45.0364 | 2025-10-02 12:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 72030e0f-dcfe-3c25-a763-9d2af60aca1e | -9.4083 | -47.5742 | 2025-10-02 12:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 241.8 |
| 87e528f0-9158-3917-b292-5c1a0f1e02ee | -8.2105 | -47.0084 | 2025-10-02 12:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 81.0 |
| ea3ee898-5192-3c6b-9c6d-b4ffdc3642ea | -14.1917 | -46.1552 | 2025-10-02 12:30:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 237.6 |
| 18990880-f305-35db-8a4b-42344d154586 | -9.9182 | -43.7212 | 2025-10-02 12:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 107.7 |
| 73793022-4eb7-3911-ac51-66e4c670497d | -7.8879 | -47.3031 | 2025-10-02 12:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 67575ce1-8b4f-38fe-824e-61a9cf755216 | -14.4753 | -48.436 | 2025-10-02 12:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 60.8 |
| e06f3f4c-75ac-3dce-9b2c-ad6cc038b2a9 | -10.8428 | -46.6064 | 2025-10-02 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| 9eb1fa26-70b7-3fc4-ac7f-1fc8a631100f | -9.4272 | -47.5722 | 2025-10-02 12:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 308.2 |
| 1a51053e-4617-3042-8bde-839ea1a36717 | -7.7755 | -42.5152 | 2025-10-02 12:30:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 124.8 |
| 96f3726b-2770-3f44-9049-246c3c583138 | -10.8237 | -46.6088 | 2025-10-02 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 44d92f8c-22e0-3354-ab0f-af306b93f545 | -9.3389 | -45.7266 | 2025-10-02 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 93.9 |
| b05869a9-f34e-34b6-ba43-73dabc5b8c05 | -7.7941 | -42.5369 | 2025-10-02 12:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 162.0 |
| f9330590-362f-3c6d-91a0-a875bbf8ad79 | -9.9369 | -43.7422 | 2025-10-02 12:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 194.3 |
| 574a6b4f-7a43-31e1-890e-8ac42c17d7bf | -9.4086 | -47.5521 | 2025-10-02 12:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 185.7 |
| edf59112-0a30-3e8a-9307-2d2e777000b7 | -11.9276 | -47.8719 | 2025-10-02 12:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 242.8 |
| 281e17ee-67b8-3f97-ba0b-bc6f0978ab19 | -9.9178 | -43.7447 | 2025-10-02 12:30:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 197.7 |
| 57579a81-c914-359a-aed8-421085e6872e | -14.4947 | -48.4329 | 2025-10-02 12:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 65.1 |
| cdd20104-3b27-3a8e-a014-c923926be937 | -14.5937 | -48.3281 | 2025-10-02 12:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 64.0 |
| 1266a518-d8c0-3e26-8469-05eea9a85e2f | -14.4757 | -48.4137 | 2025-10-02 12:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 94.2 |
| a96a60a6-60e6-38c6-97dd-86f1a050c0db | -14.4951 | -48.4106 | 2025-10-02 12:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 9f0c3916-7347-3ed1-becc-2f2bc337dbd6 | -16.0417 | -50.8959 | 2025-10-02 12:30:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 87f67455-7a1c-3169-a57d-4851aed76812 | -7.8882 | -47.281 | 2025-10-02 12:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 391a03a8-cca2-3ed9-b0ec-7cb235b69236 | -14.3709 | -45.9403 | 2025-10-02 12:30:00 | GOES-19 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 190.6 |
| a5fe0a77-0f4d-3da8-9a2f-80a24ab10ba0 | -8.6911 | -47.6906 | 2025-10-02 12:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 8a22bb08-1843-3ecb-a570-3f66c97607bb | -10.212 | -48.2128 | 2025-10-02 12:30:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 7183281d-5a90-30bb-af99-a865ebdb6c87 | -13.1542 | -47.8568 | 2025-10-02 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 31210d2e-f35f-394b-a990-f5201f7378b8 | -16.0221 | -50.8989 | 2025-10-02 12:30:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 8bc26d1f-25ec-3174-9ce7-ed64e18fd5c0 | -12.9507 | -46.3789 | 2025-10-02 12:30:00 | GOES-19 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 6135d8a0-b1a2-3fda-bc2c-1d299839479b | -13.1743 | -47.8093 | 2025-10-02 12:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 6efbb001-55b8-3411-9333-2488bdc583a4 | -9.08 | -46.7215 | 2025-10-02 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 112.0 |
| bcc00ce6-527f-382c-b125-a01125d2e0f9 | -9.3392 | -45.7039 | 2025-10-02 12:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 84.4 |


[Clique aqui para ver as próximas entradas](README146.md)
