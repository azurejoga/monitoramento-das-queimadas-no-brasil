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
| ebb70116-f8ff-37fd-8ce8-59657593c6ef | 3.90118 | -60.96265 | 2026-02-03 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc442271-7923-3f46-93d4-f22ec3994348 | 3.89712 | -60.95944 | 2026-02-03 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afe6a64e-aa0c-3af9-b417-adcb920fe229 | 3.2912 | -61.076 | 2026-02-03 05:46:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 239fabff-cdd2-39f1-bfbe-6756ddca3a24 | 3.43512 | -60.6879 | 2026-02-03 05:46:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da6d5f03-5bd9-3b98-9911-2ef01566e47a | -1.58433 | -53.99348 | 2026-02-03 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bc09f9b-b662-38f1-9c68-6e4468d46f04 | 3.29406 | -61.07168 | 2026-02-03 05:46:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40e848a4-ade6-31cd-8d13-3a8d6918786a | 1.83408 | -60.84662 | 2026-02-03 05:46:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e019996-434e-3eb4-a781-9d6ed1ffe1f8 | -1.58372 | -53.99752 | 2026-02-03 05:46:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9578ce7-2752-3a39-b8b9-b1f9cbc055bf | 3.88122 | -60.993 | 2026-02-03 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3074e184-bd95-36c4-ac7e-048aadc765bc | 3.89816 | -60.94376 | 2026-02-03 05:46:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 484a7dc5-4e9b-35b4-999a-52b190376dc5 | 2.89059 | -60.26528 | 2026-02-03 05:46:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a543cd3e-1950-34bd-94b4-fc17640041c1 | 3.88307 | -60.99576 | 2026-02-03 06:05:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4ca40d30-7d8e-373a-b416-6282972f18b4 | 3.51686 | -61.02363 | 2026-02-03 06:05:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2ef3a3a-e4ee-3a78-ab05-6909924386bf | 3.51737 | -61.02664 | 2026-02-03 06:05:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31d3f527-8694-3aa1-a602-c24e54075fdf | 3.87849 | -60.99961 | 2026-02-03 06:05:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d23381ad-12b5-378a-80cf-a6d2fdfafd5b | 3.878 | -60.99672 | 2026-02-03 06:05:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| de52a7dc-76b6-39cf-a40c-5a22b0c2f4b6 | -3.07322 | -40.10692 | 2026-02-03 11:51:00 | TERRA_M-M | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| a81e7622-89e1-3aa3-8790-d88ca22e1891 | -3.37925 | -41.20766 | 2026-02-03 11:51:00 | TERRA_M-M | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 1095e6e6-f86b-3c54-86de-f209b0b26102 | -3.3806 | -41.19813 | 2026-02-03 11:51:00 | TERRA_M-M | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 96b7e472-95b9-329d-b389-33a6520f1227 | -7.55568 | -36.27164 | 2026-02-03 11:53:00 | TERRA_M-M | CABACEIRAS | PARAÍBA | Brasil | 2503100 | 25 | 33 | nan | nan | nan | Caatinga | 63.4 |
| 965f1237-aa4c-3843-a512-04fc780ba367 | -7.55942 | -36.27891 | 2026-02-03 11:53:00 | TERRA_M-M | CABACEIRAS | PARAÍBA | Brasil | 2503100 | 25 | 33 | nan | nan | nan | Caatinga | 44.3 |
| 790d11a3-5970-3865-8eaa-02385241b744 | -10.30591 | -36.99062 | 2026-02-03 11:53:00 | TERRA_M-M | MALHADA DOS BOIS | SERGIPE | Brasil | 2803807 | 28 | 33 | nan | nan | nan | Mata Atlântica | 27.5 |
| e3a129f5-9bac-32c8-89a4-e9c83a3db928 | -9.51832 | -35.98624 | 2026-02-03 11:53:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 49.1 |
| 6f9accae-ad84-3939-98ba-7e015603823d | -10.31121 | -36.99706 | 2026-02-03 11:53:00 | TERRA_M-M | MALHADA DOS BOIS | SERGIPE | Brasil | 2803807 | 28 | 33 | nan | nan | nan | Mata Atlântica | 32.5 |
| 989d6998-8e09-35e1-8be7-48ff5713e97b | -9.51768 | -35.99173 | 2026-02-03 11:53:00 | TERRA_M-M | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 44.7 |
| 8e69c9de-a2a2-34ee-bfff-9382dbb88700 | -28.25372 | -49.64551 | 2026-02-03 11:59:00 | TERRA_M-M | BOM JARDIM DA SERRA | SANTA CATARINA | Brasil | 4202503 | 42 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 35535c1b-a96c-34f6-9506-764662f150ad | -8.6596 | -35.3599 | 2026-02-03 14:00:00 | GOES-19 | GAMELEIRA | PERNAMBUCO | Brasil | 2605905 | 26 | 33 | nan | nan | nan | Mata Atlântica | 130.7 |
| 600fab0f-3655-3b2a-bc1e-f2a4594b7098 | 3.8763 | -60.9971 | 2026-02-03 14:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 64.1 |


