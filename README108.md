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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31acbfbb-6c34-3735-ba18-aa87e4986892 | -12.97216 | -54.74976 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b07f8212-283e-3c54-8383-7b649e49ca0f | -17.37022 | -52.92743 | 2025-09-12 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 52246ec6-74ce-337c-b705-9deaf8579d90 | -11.90764 | -62.51602 | 2025-09-12 05:21:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 975e5ee0-5b13-3bfd-afd9-ac66799f1568 | -12.35314 | -63.63869 | 2025-09-12 05:21:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce92845a-72bd-3657-9730-fc77a05c4d54 | -12.91882 | -54.76265 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 0dae4ed0-ef86-3c0f-8d13-998cb1a580c4 | -16.66013 | -47.62549 | 2025-09-12 05:21:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f7548310-8b50-3e29-aec9-a8dd87eb4132 | -15.68313 | -52.22519 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 65f52f78-c3cf-3352-9529-c29bf1ec44a2 | -15.79387 | -52.24517 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b637210-c512-3a13-bc76-5091988a1ab1 | -20.00094 | -47.63713 | 2025-09-12 05:21:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 59f23b04-bb28-37d5-88e2-80dc44cb4cb9 | -16.43391 | -49.043 | 2025-09-12 05:21:00 | NOAA-21 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5784aad3-c21b-3dfc-8371-ca25ac505f19 | -15.0823 | -52.43295 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a7e8bd0b-b4cb-3149-a798-a0e399abb5a5 | -12.91564 | -54.75414 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 966e1b05-4ebb-3797-8ce8-0522b0a07663 | -13.90002 | -48.24327 | 2025-09-12 05:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c369b31f-62e9-3b61-9ef6-6290883d2b2b | -14.41826 | -52.9271 | 2025-09-12 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7c046bf2-b973-3750-9d03-5afecf968f1a | -19.24447 | -48.03972 | 2025-09-12 05:21:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 22ccc9ee-aff8-3fcb-bf3e-65f5212169c8 | -17.13083 | -48.49546 | 2025-09-12 05:21:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5806bea8-8617-34e2-88c7-e22501f2f251 | -12.35243 | -63.6429 | 2025-09-12 05:21:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00e6317a-68bc-36ef-b80d-f6918337f89e | -15.15452 | -52.46482 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9807f6f1-8982-35da-b104-d89d617a91fe | -15.52804 | -48.54391 | 2025-09-12 05:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c3c02b52-4c9b-355e-b764-4052ea8dc43a | -15.81776 | -52.22078 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 549dcb88-bf91-3638-af7b-242e87eeaedb | -20.01701 | -47.65265 | 2025-09-12 05:21:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| d79f3b75-296a-3579-920d-83c7e8692a2c | -14.55987 | -54.52305 | 2025-09-12 05:21:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7fc76e02-ab7e-38eb-94f5-cc8a0da38db6 | -15.79532 | -52.23215 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 05b6224f-fda9-376a-b529-4f4813c1a5f8 | -13.27732 | -51.71642 | 2025-09-12 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4eaa4330-bd65-3b37-ba08-e4f69afd6538 | -14.51443 | -53.90828 | 2025-09-12 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd53b42e-9855-32ce-b407-a4e149691f49 | -20.01423 | -47.65314 | 2025-09-12 05:21:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 3d7aab99-0641-3428-a8e9-75ee101211b1 | -14.87774 | -55.85159 | 2025-09-12 05:21:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87fd44dd-caa0-3539-99a1-4f51080c24b5 | -16.25224 | -52.65682 | 2025-09-12 05:21:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a04595a3-8530-3776-a400-f31100085665 | -15.86901 | -48.33328 | 2025-09-12 05:21:00 | NOAA-21 | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8f2689d-9888-3e78-8543-160ffb7fbbd2 | -13.23614 | -51.74163 | 2025-09-12 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 01951520-8388-31c5-a3eb-f83399e22dbb | -14.33304 | -54.12463 | 2025-09-12 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9cdd5906-007f-3c22-a6b1-1369fb5485d1 | -17.83503 | -52.0573 | 2025-09-12 05:21:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a74e87fa-27ad-3234-97d4-f215e9f7aa01 | -17.20929 | -50.15399 | 2025-09-12 05:21:00 | NOAA-21 | JANDAIA | GOIÁS | Brasil | 5211701 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 970fd393-4aa8-3825-8937-f886ec403016 | -14.43391 | -48.42484 | 2025-09-12 05:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 29bfdceb-34ff-3478-8ac6-5623e979a515 | -13.89549 | -48.22385 | 2025-09-12 05:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ddda4f76-6feb-3994-94d0-0c8d6c7b07c2 | -17.37628 | -52.91936 | 2025-09-12 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5dedda2a-389d-37fb-875e-7d64513612fb | -15.78832 | -52.24765 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 3908b6da-befc-32ae-89de-dc69fb62bec5 | -13.89925 | -48.24446 | 2025-09-12 05:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f9626f3c-e439-3348-bc56-e5631d88bee8 | -18.76753 | -48.53056 | 2025-09-12 05:21:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f5d392e0-8645-39e8-9fda-923c976de27e | -18.77164 | -48.53929 | 2025-09-12 05:21:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0e138776-27fa-3d86-83a1-eb0b41da9954 | -15.10588 | -52.45191 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2c69b058-a72c-32e2-babe-3bf6c928e6fd | -16.61967 | -51.81111 | 2025-09-12 05:21:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 137d139c-89df-3c8f-806b-69513e6d13d6 | -13.27658 | -51.714 | 2025-09-12 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6d99d29-3630-3560-bdd0-0deabb42ea99 | -15.54017 | -48.54851 | 2025-09-12 05:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 614e917f-9c3f-3852-b721-b8bfe6c79d9b | -14.88019 | -55.8334 | 2025-09-12 05:21:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b41ace3a-5c9c-3095-b112-6a3ec7998e64 | -12.83407 | -61.94676 | 2025-09-12 05:21:00 | NOAA-21 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c714506d-42f3-39f2-930a-e3d66331a117 | -12.92623 | -54.8041 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| abe239a3-87af-3af1-8ec7-a1246432a993 | -14.42012 | -52.92742 | 2025-09-12 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9b1a8ebb-8e57-3b16-a575-7f8eb1283c83 | -19.19213 | -48.00827 | 2025-09-12 05:21:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0dc7342c-a2a3-3382-a678-5c099a624289 | -12.91616 | -54.75018 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 76c6be15-effb-3ae3-b330-e8650988bd48 | -12.922 | -54.7712 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 54e34ed3-7220-3c09-868a-1a56369da573 | -15.91486 | -51.78944 | 2025-09-12 05:21:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 13bdac72-383a-33a8-b257-b9442fe7b77e | -16.62925 | -49.7955 | 2025-09-12 05:21:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e6e429eb-a368-35f6-99d0-a09bc723470f | -17.13466 | -48.49194 | 2025-09-12 05:21:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ee5a1051-ab63-3eb1-bc74-11c532971c6d | -18.77787 | -48.54625 | 2025-09-12 05:21:00 | NOAA-21 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 25d63fdd-a32f-3e9f-b8bd-d7b862020359 | -19.99377 | -47.63589 | 2025-09-12 05:21:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b028a494-2fd2-3893-86f7-b52eeb825dfa | -12.82617 | -61.95293 | 2025-09-12 05:21:00 | NOAA-21 | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3ce5c423-4c66-3d5e-a984-317a8c4e97aa | -15.58276 | -54.75874 | 2025-09-12 05:21:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8a5ceedf-c5af-33fe-94a6-079770ab3c7d | -12.99056 | -54.77276 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e400852-3914-30d5-9e78-0184027c4337 | -17.38203 | -52.91409 | 2025-09-12 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a23c170c-3eee-30af-b368-f463d2ead4ee | -19.2389 | -48.04158 | 2025-09-12 05:21:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 72025329-fcc3-3e12-bace-cf342c79c6e8 | -16.20046 | -47.98283 | 2025-09-12 05:21:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d7838872-e025-308f-8b8c-d22890cafbe8 | -16.234 | -48.44807 | 2025-09-12 05:21:00 | NOAA-21 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 193dd523-9920-3791-a72b-84ac2b523e6d | -12.12348 | -59.83468 | 2025-09-12 05:21:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6148da3c-9cec-3fe2-8079-eb12e6d35cd5 | -14.49926 | -53.92318 | 2025-09-12 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7746d548-a8d1-35ad-a6eb-fc247bda77fb | -17.14811 | -48.49263 | 2025-09-12 05:21:00 | NOAA-21 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92ae5646-aa3c-338d-9e0c-e4956f603b42 | -18.75433 | -47.62682 | 2025-09-12 05:21:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 096cd96a-5b11-32a4-be52-da47148eb350 | -12.25276 | -59.32271 | 2025-09-12 05:21:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f674106a-fac9-33a2-833e-cef2f084492a | -16.6671 | -47.62645 | 2025-09-12 05:21:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 752821ca-db49-37d4-bc8a-66b6ca109510 | -15.88268 | -48.18513 | 2025-09-12 05:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4947f10-628e-39b2-bfd6-05f30aac8658 | -18.38414 | -50.55645 | 2025-09-12 05:21:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6fed1fcd-56bb-3b5f-83d8-fd862af9657e | -17.37056 | -52.92441 | 2025-09-12 05:21:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 172bb741-a56e-3e49-b63f-4ae1e7595f74 | -15.14794 | -52.47701 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 51ecffc6-d61f-3df3-8e2e-832df2ce3812 | -20.01658 | -47.65863 | 2025-09-12 05:21:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 503bbd9d-f993-3a03-a214-387cb18db86f | -20.01379 | -47.65887 | 2025-09-12 05:21:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 55d8fcb7-36b9-3118-85b5-f0ac549bd659 | -16.62964 | -49.79163 | 2025-09-12 05:21:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 5205d39a-0a72-3b5a-ab4a-31c155224820 | -13.26537 | -51.71895 | 2025-09-12 05:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35b29175-6f36-38b6-9763-e620029118d5 | -16.59621 | -49.81511 | 2025-09-12 05:21:00 | NOAA-21 | NAZÁRIO | GOIÁS | Brasil | 5214408 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 5d2bb115-a2df-3be4-8288-aec9e4809600 | -18.75484 | -47.62007 | 2025-09-12 05:21:00 | NOAA-21 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 4dba3111-12f9-3cbf-bb64-f2815dcdfba4 | -13.13445 | -54.92434 | 2025-09-12 05:21:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9524e8e2-f636-386e-972b-1b4ef1a20848 | -17.83769 | -52.05246 | 2025-09-12 05:21:00 | NOAA-21 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52386d35-d681-3974-9770-3c80f36ca4f0 | -11.77585 | -64.93535 | 2025-09-12 05:21:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ab8c332c-4244-3aa6-914e-f6418171964c | -14.50554 | -53.90972 | 2025-09-12 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 435af1e0-62f5-3a46-a405-98bf9842abfe | -15.52654 | -48.55245 | 2025-09-12 05:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 66550216-48ab-3cca-bd1d-44c4e6b7c18f | -16.20196 | -47.98383 | 2025-09-12 05:21:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 087c2dfa-5ac8-3ade-acbc-a385dbc34594 | -14.50341 | -53.92157 | 2025-09-12 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| eb5cc1be-322f-3f56-a436-41bfc0ab77a1 | -16.65165 | -47.62797 | 2025-09-12 05:21:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e8f6efe3-8e98-3de8-a71b-e1a540833630 | -15.54636 | -49.7457 | 2025-09-12 05:21:00 | NOAA-21 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a07b8b5d-c714-3cc0-a98d-218bffdf8f39 | -14.5153 | -53.9059 | 2025-09-12 05:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2f37e18a-df6c-3444-95be-5db482d01867 | -13.44453 | -56.6698 | 2025-09-12 05:21:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d31bb993-a62a-3498-a326-76c3c06ae928 | -14.21432 | -58.59216 | 2025-09-12 05:21:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 688a09ca-9f31-3ae2-b9eb-050967044ffd | -15.58357 | -54.75626 | 2025-09-12 05:21:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 80d21cf5-3320-38e4-9654-85003ff8bca8 | -14.7214 | -55.62342 | 2025-09-12 05:21:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f1e1f4b-abd8-3240-9289-e8bfc5d90547 | -15.60147 | -52.73618 | 2025-09-12 05:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 143157cf-b2e3-3019-ac8f-a919e9202afd | -20.00304 | -47.64497 | 2025-09-12 05:21:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9c863f77-86e7-3b62-9303-46556401b96e | -15.91446 | -51.79301 | 2025-09-12 05:21:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 57348f63-917f-355b-872a-5d7b0073aeb2 | -13.91696 | -48.26571 | 2025-09-12 05:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 508bb5c8-9659-3334-96bc-2d06ef2fdd24 | -15.1117 | -48.09758 | 2025-09-12 05:21:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b5a15754-d12c-36f1-8765-136c8b65dbd7 | -14.42801 | -52.92856 | 2025-09-12 05:21:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7841ca29-18ef-3abb-811a-ef6152bdcc0b | -20.00976 | -47.65253 | 2025-09-12 05:21:00 | NOAA-21 | CONQUISTA | MINAS GERAIS | Brasil | 3118205 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |


[Clique aqui para ver as próximas entradas](README109.md)
