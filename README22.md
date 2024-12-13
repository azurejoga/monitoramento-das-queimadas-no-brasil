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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bfd8338a-429e-30c9-93e9-44412e345576 | -13.37064 | -54.25096 | 2024-12-13 04:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e8ba6f69-6ac5-3c78-8758-0b6e6570e892 | -13.7034 | -43.98267 | 2024-12-13 04:23:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 94d4e37a-58f3-3bfe-a217-8948b01aa9c6 | -14.78572 | -52.6403 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 35c52b91-e2f0-353b-963d-96fa07dbfe7a | -11.20955 | -53.8218 | 2024-12-13 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| d6e004db-0016-3b7c-941d-0f6086208e9e | -11.19815 | -53.81826 | 2024-12-13 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c9b9266a-c804-3ed0-a2c7-ee48147c4812 | -13.37549 | -54.25184 | 2024-12-13 04:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2910f25f-f170-3834-a20a-45c2e22fe93f | -14.77932 | -52.6417 | 2024-12-13 04:23:00 | NPP-375D | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 26f15055-29f8-3adf-9b3b-9b189418fbda | -12.30176 | -50.0904 | 2024-12-13 04:23:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 646c50df-279a-312a-84a7-907e035eaacf | -13.07061 | -52.03459 | 2024-12-13 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 28a02147-8670-379e-9209-29283620d309 | -13.06219 | -52.03306 | 2024-12-13 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8c8f5504-f03a-3cab-8856-62d4f6cb1e7f | -11.20748 | -53.83275 | 2024-12-13 04:23:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 3d70643b-1bc4-30d4-8377-2b4032c809ed | -12.05735 | -46.88807 | 2024-12-13 04:23:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d91fcc92-21dc-3a86-a5c9-bbd47552538e | -13.06 | -52.04501 | 2024-12-13 04:23:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3e247f8c-3b63-34ab-8613-d03f3e065bbf | -12.2814 | -50.09874 | 2024-12-13 04:23:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70daaabb-eed3-31e9-9ee8-9a439720b15a | -11.6885 | -48.07804 | 2024-12-13 04:23:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99f1e41c-9d06-36ff-96e6-c38554f93d7e | -29.62541 | -51.97369 | 2024-12-13 04:25:00 | NPP-375D | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f63dca78-9ba1-3d73-a839-c9da572ac038 | -29.62272 | -51.96881 | 2024-12-13 04:25:00 | NPP-375D | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| f451d6cf-ca7c-38d6-afcb-b68e55646ec3 | -29.14459 | -52.86764 | 2024-12-13 04:25:00 | NPP-375D | TUNAS | RIO GRANDE DO SUL | Brasil | 4322152 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| d5eeed16-91ea-36b6-beab-cfeb4fa14b80 | -28.58367 | -49.44025 | 2024-12-13 04:25:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5dee4430-493f-37e5-bf16-cb7aec3321dc | -30.74886 | -52.16192 | 2024-12-13 04:25:00 | NPP-375D | DOM FELICIANO | RIO GRANDE DO SUL | Brasil | 4306502 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| d4a51279-a440-3fb4-84e0-903dd9d8f298 | -29.00971 | -50.77306 | 2024-12-13 04:25:00 | NPP-375D | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 14cd4c6c-771e-3074-9627-9536cea02012 | -28.58702 | -49.4409 | 2024-12-13 04:25:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| c8865eb9-998c-3a42-9833-10e789fd7a48 | -29.62202 | -51.97294 | 2024-12-13 04:25:00 | NPP-375D | CRUZEIRO DO SUL | RIO GRANDE DO SUL | Brasil | 4306205 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 495fd9ae-34e6-3618-97d6-ea0467de897a | -25.57013 | -49.35425 | 2024-12-13 04:25:00 | NPP-375D | ARAUCÁRIA | PARANÁ | Brasil | 4101804 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 6e7df840-e529-3d2d-aa81-9e9b81e42c47 | -6.9158 | -43.5185 | 2024-12-13 04:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 126.0 |
| ace46d68-e074-398a-8bac-a9fd37739340 | -11.2151 | -53.8125 | 2024-12-13 04:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 0194664b-1d76-3ad3-a2ac-c43e5702f5f2 | -6.9156 | -43.5418 | 2024-12-13 04:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 7507a3a7-64c7-3e46-a652-c3c988886ab0 | -6.9346 | -43.5168 | 2024-12-13 04:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 8c38442b-7a4a-3237-80c1-4c999e80bf54 | -14.7848 | -52.642 | 2024-12-13 04:30:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 57.8 |
| a8f80729-9e31-375e-b813-e1fd70f3f9a7 | -12.5499 | -57.6996 | 2024-12-13 04:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| cd548423-0803-36dd-a366-4fce1441f01c | -12.5497 | -57.7196 | 2024-12-13 04:30:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 195b3ad0-6555-3e8f-8121-9f0542705096 | -11.2148 | -53.833 | 2024-12-13 04:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| b0bf0202-b156-34b7-8f59-8852a344769b | -14.7655 | -52.6446 | 2024-12-13 04:30:00 | GOES-16 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 57.1 |
| a229f291-73dc-30b1-951e-de2e7a8ed517 | -2.4923 | -51.8027 | 2024-12-13 04:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| f89dc482-52fb-366a-a592-df2dc58f48fe | -6.9161 | -43.4952 | 2024-12-13 04:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 6d2d3dd4-5439-36f7-9125-cc41966a12ec | -11.1959 | -53.8348 | 2024-12-13 04:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| b1def2d7-9f1c-371a-950a-83adec227e17 | -11.1962 | -53.8142 | 2024-12-13 04:30:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 60.5 |
| fe9f85f4-c6e3-3e57-8aff-f187b12908a3 | -13.0644 | -52.0326 | 2024-12-13 04:30:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 54d1ad87-471d-3c18-8b74-3e4af15c722e | -6.9349 | -43.4934 | 2024-12-13 04:30:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 49.1 |
| 1dca04cb-6a4f-36d8-8881-94ef08e6a7f9 | -11.1962 | -53.8142 | 2024-12-13 04:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 6c795667-56c1-3b61-9456-ab714d01bfd6 | -6.9156 | -43.5418 | 2024-12-13 04:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 77bd42a0-889d-3b77-81b2-db47396f46c4 | -5.2108 | -43.3067 | 2024-12-13 04:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 179fcb6c-4a8d-3b4b-bc14-5c032e0b9a87 | -11.1959 | -53.8348 | 2024-12-13 04:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 201617c5-2014-373d-b7f4-3cb180ecf45d | -12.5497 | -57.7196 | 2024-12-13 04:40:00 | GOES-16 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| c0f13680-96fd-37be-8feb-8f23e26801e6 | -6.9158 | -43.5185 | 2024-12-13 04:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 167.3 |
| f5811d44-4378-3d23-9eca-29baa925f8f1 | -6.9349 | -43.4934 | 2024-12-13 04:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 82.8 |
| d65ac6b4-6ddc-3c8a-ba4b-23bcb65e79ad | -5.211 | -43.2833 | 2024-12-13 04:40:00 | GOES-16 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| eca35682-2281-39cf-8ffb-0c767030c14b | -6.9346 | -43.5168 | 2024-12-13 04:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 176.6 |
| 5e03d18c-de3c-330c-8a03-1c5e98a9379f | -6.9344 | -43.5401 | 2024-12-13 04:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 40cae0f0-1d6d-3db4-92d7-2d916a3d8c5e | -11.2151 | -53.8125 | 2024-12-13 04:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 74463629-88ba-34bf-8361-8265dcab9d60 | -13.0644 | -52.0326 | 2024-12-13 04:40:00 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 66.7 |
| daa1952c-8afe-3969-8aa7-5306a9201db4 | -6.9161 | -43.4952 | 2024-12-13 04:40:00 | GOES-16 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 6e21b8c7-dc73-3e68-8c7a-37ea873d66a8 | -11.2148 | -53.833 | 2024-12-13 04:40:00 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 700af05a-c5f8-389d-b284-f0d7f6d99724 | -0.3603 | -48.44274 | 2024-12-13 04:40:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6eff4a67-0e7a-396c-9471-3e3551ba3379 | -0.75393 | -47.75845 | 2024-12-13 04:40:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| a3c7d45f-cc0f-34ed-add0-6bb8f6387304 | 2.54568 | -60.73649 | 2024-12-13 04:40:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7b758a8d-7bb5-388f-943f-2a270c148b34 | -0.36084 | -48.43922 | 2024-12-13 04:40:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 077e5253-36d5-3005-a9c1-af7381219653 | 2.54492 | -60.73134 | 2024-12-13 04:40:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 50bbaa83-1de4-319a-8378-ba9ee7dddf02 | -0.36309 | -48.44677 | 2024-12-13 04:40:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aa49f038-fafd-3699-b757-ff3f2e9db71b | 2.53854 | -60.7323 | 2024-12-13 04:40:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85b2de47-8b83-35aa-9da9-e505f893851f | -0.75052 | -47.75793 | 2024-12-13 04:40:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 055b2420-c0d1-33b0-b096-20f9496b104e | -0.94018 | -46.92145 | 2024-12-13 04:40:00 | NOAA-20 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6225bba-21eb-36f5-9827-50ddc6724586 | -0.36364 | -48.44325 | 2024-12-13 04:40:00 | NOAA-20 | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2540e9d3-02f0-3edd-b825-3f9d47126730 | -0.93956 | -46.92542 | 2024-12-13 04:40:00 | NOAA-20 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42a0ff33-00fd-3201-b745-5434a7116f9c | -2.74029 | -52.9677 | 2024-12-13 04:42:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3a077d7f-992c-33d4-a204-6d6e6c50338b | -3.14301 | -45.58673 | 2024-12-13 04:42:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dd7dc577-3c92-3705-a71e-2b59595afcd3 | -4.50958 | -42.06502 | 2024-12-13 04:42:00 | NOAA-20 | BOQUEIRÃO DO PIAUÍ | PIAUÍ | Brasil | 2201945 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7085161b-2133-3c1f-912d-3d6b77d160f3 | -4.37952 | -47.62927 | 2024-12-13 04:42:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08d703ed-00a3-3432-9431-e0b4bc03ddd2 | -3.00656 | -48.03196 | 2024-12-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cbdbe677-7a23-3f1d-bedf-db163ada0fa1 | -2.47504 | -53.64003 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3bb931cd-db1e-3c15-b7d8-00403a20e143 | -2.47905 | -48.5802 | 2024-12-13 04:42:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d564a8be-c90b-3e87-9551-64aa4d3bd5a2 | -3.26517 | -46.92872 | 2024-12-13 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae572a9a-a823-34bf-9e62-643c08bdfc1b | -2.50725 | -46.84814 | 2024-12-13 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3926aecc-5697-3f82-8da4-653e46509d2c | -3.26945 | -46.92507 | 2024-12-13 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 736b9d27-621c-3859-a1db-b5b99c7482b3 | -2.44204 | -53.96178 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef0c6bf7-a66d-3869-add6-ea036b54118a | -1.68329 | -52.55618 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 43f4b50b-cbe1-33d0-9bb7-0c7c3f093f08 | -4.64022 | -42.8805 | 2024-12-13 04:42:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b8d748fe-565b-3e2c-9d78-cd20579c5497 | -6.91561 | -43.50118 | 2024-12-13 04:42:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c70693e3-50cb-3ee9-a96e-63747e300156 | -4.87168 | -48.14828 | 2024-12-13 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5790cddc-825f-3b84-9b16-aa70f4864f1c | -5.21996 | -43.29385 | 2024-12-13 04:42:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8bd5b6ee-0d48-3b3a-b6ba-9cf88bb7a54f | -2.41381 | -53.70052 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cd721fe0-fb13-3ffb-84db-4014302a07b5 | -6.30457 | -43.46568 | 2024-12-13 04:42:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a48e61b5-b299-3837-acdc-db6b8aa0a132 | -6.28101 | -49.64411 | 2024-12-13 04:42:00 | NOAA-20 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| addec8a0-8da8-31e9-8da6-7affcf31b609 | -4.91717 | -37.48915 | 2024-12-13 04:42:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8dbd9ac9-5f41-3009-8ed7-083f04e15c51 | -6.12728 | -42.54059 | 2024-12-13 04:42:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6afcc321-1c61-3eee-8cd0-0dc3c376f074 | -1.91494 | -52.64807 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d2e8e3f-bd25-3610-8edb-d51abb66a917 | -2.91589 | -48.00671 | 2024-12-13 04:42:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64a99e97-acc2-355d-b2d9-353f6aa4fda9 | -2.44896 | -53.64706 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f381cc99-2c24-379a-a9ea-7687e089ee40 | -4.77867 | -48.50638 | 2024-12-13 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d8c1543-6fa9-38bd-9c72-4a6aae4ef1c8 | -4.54857 | -48.00688 | 2024-12-13 04:42:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 76054658-e067-344c-9809-b7ce148c024a | -2.29653 | -54.00067 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5e7d7bbe-0797-37d3-97a5-b1e55faf4c83 | -6.92113 | -43.49657 | 2024-12-13 04:42:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 10.7 |
| abccdc3a-be94-35e0-9af6-f7843fb551bd | -6.21421 | -43.9523 | 2024-12-13 04:42:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e92c2af-0229-3031-bff7-3fbf1ea0c4e7 | -2.41079 | -53.69548 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff7ca041-fcf8-3c79-934c-aa1cad81baed | -4.7325 | -46.50055 | 2024-12-13 04:42:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 55ee57e5-cc4a-3170-8765-519807786829 | -5.21055 | -43.29234 | 2024-12-13 04:42:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 40.5 |
| dac281b7-cf1d-3d2e-9050-726b945ec794 | -1.70035 | -52.56293 | 2024-12-13 04:42:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c72b3d77-2a87-3644-97c2-5bb8d5fac127 | -3.26712 | -46.91613 | 2024-12-13 04:42:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| acf2c284-102d-35d0-a0d0-35a481aba4d2 | -2.18878 | -53.65467 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b12f93f2-83e1-335e-8e93-ba945a44db46 | -2.30412 | -54.00188 | 2024-12-13 04:42:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README23.md)
