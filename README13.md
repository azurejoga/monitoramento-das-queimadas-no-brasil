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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ce8ab3b-8f17-3d81-84ab-012d2fe72dbe | -13.26855 | -54.34158 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 0c55ccd7-aa69-3c1d-854b-83954e0479ac | -11.48638 | -52.91877 | 2026-07-07 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a2dbd27-96c2-362d-9123-6f09310e14cd | -11.68429 | -44.55312 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ba83cb0c-df49-30ba-afbd-a648e79eedec | -11.44459 | -52.92839 | 2026-07-07 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 92e122d3-b1d1-382d-8c4e-9e4ec8ca0595 | -13.27637 | -54.34303 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5eeec1fe-461e-3410-ae0b-0dca20cd7c45 | -13.32034 | -54.37362 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46400a57-d2b6-3827-801e-e5f8f71a28cc | -11.66932 | -44.56151 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1fd95283-520b-3787-ad1d-2b9c4cc27c71 | -11.65379 | -44.57343 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fcabcfa8-0626-30df-8812-91c88a692cd3 | -11.68761 | -44.55367 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ee5e60f5-2970-367a-84ee-0a41bb5adb20 | -13.27323 | -54.34613 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c674f5a0-ed2a-3852-8fe9-ae09a91cc0be | -10.93291 | -43.06433 | 2026-07-07 04:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 592e380b-011d-36bd-a45c-60f003f3b8e7 | -11.04959 | -49.60088 | 2026-07-07 04:25:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2a6f1b65-2910-3da5-9a61-938add446a09 | -13.29644 | -54.35386 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa475f78-d833-3c5d-8a66-27b8f1600fb6 | -13.29039 | -54.35632 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff43f727-d35d-3077-9121-3d0fd2a92d6f | -13.53828 | -52.91331 | 2026-07-07 04:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f856be7d-9bc0-34aa-8910-3778eeb6b988 | -13.26247 | -54.23028 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c47d47a-6106-3d6e-8262-718102f16d9d | -11.48865 | -52.9158 | 2026-07-07 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 306c6cac-a17d-37d8-8c4f-8b8fbdb4f3c2 | -13.53343 | -52.91244 | 2026-07-07 04:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a836a64a-c520-328d-8823-f53e7cb13f4e | -10.82688 | -49.37566 | 2026-07-07 04:25:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f45d279-5ff4-3ff4-9bcb-24986b0dcb76 | -10.86423 | -46.35979 | 2026-07-07 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc8942d2-03a1-3696-a390-50e378d0412c | -13.60085 | -56.62023 | 2026-07-07 04:25:00 | NPP-375D | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e5162eb-3e21-32a2-bed4-b42f2fd03777 | -13.28036 | -54.35087 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bab9e111-5f7c-392c-8de7-1c315c81bcb6 | -13.3094 | -53.34753 | 2026-07-07 04:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3fc4481a-2c2c-3f47-aeb7-0d8df696c265 | -15.50786 | -42.20563 | 2026-07-07 04:25:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c12cd42f-af84-3f24-bc1b-95cbf0db7096 | -11.65935 | -44.55988 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a20883a-09f9-3929-ae16-b0f6c709fb1b | -13.07506 | -48.17135 | 2026-07-07 04:25:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| daab9c54-7a8b-337a-8cfb-a4745c5d7081 | -13.25724 | -54.34261 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18619fd7-d665-3b0e-9632-eb2bfd6562bd | -12.793 | -44.49483 | 2026-07-07 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9482efc-0960-37d0-9362-f23bc6ad623f | -12.79468 | -44.48421 | 2026-07-07 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d68d3b28-c483-3673-bbf2-3ec131ba4a55 | -13.28777 | -54.34158 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f84e5cc6-dff2-3d9e-88aa-5b29d330393d | -15.50912 | -42.19684 | 2026-07-07 04:25:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0edf8e42-19e8-301b-92bf-6a08b9de185c | -13.26791 | -54.34492 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 0594e3a5-f748-3482-8d09-caa99753d121 | -11.68705 | -44.55719 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9f0a158-78a7-3cff-9572-782a51eed8c9 | -11.68096 | -44.55258 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff94a924-a1b1-3331-9813-9c05c5cdf18f | -13.26726 | -54.34828 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e567aeff-acc7-3bbf-a4c2-b8a44eaf9732 | -12.79633 | -44.49538 | 2026-07-07 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9d68511e-8482-3dff-b5e2-989e791713ce | -10.8309 | -49.37639 | 2026-07-07 04:25:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d90d75f-f139-36ac-b206-30591eb57225 | -9.40493 | -48.02425 | 2026-07-07 04:25:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1e2b65a-f146-3767-ba0d-99ad8267f39a | -9.28523 | -49.5852 | 2026-07-07 04:25:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 848bcdba-9a19-3cb9-a5f7-a6b62e5603dc | -13.31709 | -54.36189 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 51a06bf9-413c-3c7f-a277-4f86bcb81f77 | -12.51163 | -48.25409 | 2026-07-07 04:25:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 42bd7e9f-6600-3dd2-8615-96a946942976 | -13.31975 | -43.62256 | 2026-07-07 04:25:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1874b02-d217-333a-8ebf-d7728ff05387 | -13.2618 | -54.23371 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ef56c19f-2e52-3d2c-9916-131748f9493b | -11.68576 | -50.38211 | 2026-07-07 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| edbe8714-db13-3afd-83d3-e02aed71eae4 | -13.27767 | -54.3643 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb54ac88-49f0-3205-8928-1be18c7404cd | -11.66876 | -44.56503 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 21acdb9c-f9a2-33c5-aab7-45f4f0f826d9 | -13.27064 | -54.35954 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5dc6af7-8067-3cf1-8cdb-7632b9dfce28 | -13.27791 | -54.35068 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e4e4e45-b582-34e8-b191-23c334b0cb19 | -11.84264 | -48.25187 | 2026-07-07 04:25:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0a51c8a1-01ff-3504-904e-76278938e0a1 | -11.72323 | -49.84695 | 2026-07-07 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7fa9b3ad-6932-3d6a-9366-49d83309d89b | -11.69426 | -44.55475 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bc1f24e9-c5ea-3d03-8860-355953e47c5e | -11.67041 | -44.57614 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 544a85f8-0c00-3fa8-b473-5e0372aa5c37 | -13.2697 | -54.34855 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b1dd5d7-bc92-3149-bbec-94a3e1a7c6bd | -11.68041 | -44.5561 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e3006fe6-1272-3eee-859a-b59ce768e20f | -11.66544 | -44.56449 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f371b8a2-5899-3e2f-ad94-dc8df7fd474c | -13.54069 | -52.91252 | 2026-07-07 04:25:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4fa480d3-afa9-31bd-aa8d-6930b3d73e2e | -10.84887 | -46.38845 | 2026-07-07 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db6f0d91-338b-3ded-b00b-d5a31a9e37e8 | -11.64416 | -50.37025 | 2026-07-07 04:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| bc6d30c8-b3ff-34d2-b05b-a6698a9fc1d5 | -9.52525 | -48.16323 | 2026-07-07 04:25:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a2819d47-ce31-35b1-b8c7-0452ec34648b | -13.27569 | -54.34638 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7c2d7ea2-d2a7-3dd4-8398-95bc7cc797fb | -11.66985 | -44.57966 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 357019cc-d289-3848-8dc7-82e7fc759cb5 | -11.56168 | -52.79591 | 2026-07-07 04:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60691bd1-bfce-3fff-84cd-5bb0f3b9e6dd | -11.69038 | -44.55773 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7813ea9-5589-31c2-9ee9-21e0ba3870cf | -13.27302 | -54.35975 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4d2a44e-7d3d-3f90-8273-1d13cb4bd026 | -11.92028 | -43.374 | 2026-07-07 04:25:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27a5047a-5cfb-3cac-b82d-0b49bd579c8a | -11.66988 | -44.55799 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 1cfddac0-b556-3258-a361-57f98aaa9197 | -12.75307 | -44.55363 | 2026-07-07 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 43f434a6-2f3e-391d-9815-f0197a065b6a | -13.25904 | -54.34624 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8b284f27-ef8a-3b7b-9d7f-bf3590a939f6 | -12.79412 | -44.48775 | 2026-07-07 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 523c859a-deff-3cc6-85ad-0028689e1499 | -13.93161 | -46.64598 | 2026-07-07 04:25:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca24c103-b850-3e9b-a050-b30e6c8ca29d | -11.6293 | -46.3609 | 2026-07-07 04:25:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44b50dce-1898-3d68-a6c4-79b55e1fb389 | -12.3625 | -47.42818 | 2026-07-07 04:25:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3d226f67-f63c-3a40-b9cf-407dc632ba5f | -13.28053 | -54.33709 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a14d8d1-f897-3ebc-8419-398e15274c96 | -11.66323 | -44.55691 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e806aa27-e8fa-323a-974e-1ee8d1ba8406 | -11.66652 | -44.57912 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f6b40ba-3e80-38bd-a659-6db71565dcdd | -11.66708 | -44.5756 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7cb1d9dd-41db-3dab-85cf-5ccf4389ec35 | -10.93573 | -43.0685 | 2026-07-07 04:25:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| 6fb6e67c-489c-36bb-bc28-7c3b8fefa8c4 | -13.25252 | -54.22472 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31b13940-e7ff-3eb8-9ca0-444be750da9f | -12.7858 | -44.49729 | 2026-07-07 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 0ab0b378-0d35-34ca-979a-3f790a9c4d8c | -11.63024 | -46.37657 | 2026-07-07 04:25:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57ea645e-6f52-3710-88f4-c4c55f00db4b | -12.35896 | -47.42755 | 2026-07-07 04:25:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 49d23e91-e9b1-321c-b752-707c8d8f33d7 | -12.75363 | -44.5501 | 2026-07-07 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 601fd91d-531d-3d41-9c4f-de16d3feb892 | -9.1993 | -45.31705 | 2026-07-07 04:25:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e673695-0d8c-3d69-9d32-f9b9f11c97b6 | -9.31308 | -51.9138 | 2026-07-07 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dda2ee7f-109d-341d-9706-2448336d6a55 | -13.28436 | -54.35867 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45573d5f-7eb1-36e2-b411-a324d55ba382 | -11.65879 | -44.5634 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e7115c7-b5d6-3118-9f1f-de0b72e8ca01 | -13.27453 | -54.3394 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d67d6751-d340-3496-a721-c794112aa3c8 | -13.27234 | -54.36311 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ad83a344-0830-3351-9752-338ce93a3371 | -10.41265 | -46.83734 | 2026-07-07 04:25:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1aad8c42-9e38-309e-ac05-9641fe4126da | -13.26573 | -54.34065 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 36da5e14-75b1-3ada-971b-7258179fef53 | -13.31054 | -53.3416 | 2026-07-07 04:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d997072f-99c3-3d17-8706-c55dc7c805dc | -12.78801 | -44.50491 | 2026-07-07 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a2c3cef-ca2a-32b9-a95f-f8e2005d7b67 | -13.28674 | -54.40266 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24eecc47-9f4b-364c-b3ff-61340c1e1ead | -13.27597 | -54.36072 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6f921f00-f33f-3f9d-9f08-601e6f6d3d83 | -13.26999 | -54.36292 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c74ff5c3-9763-3152-b478-66ae2ca6268b | -9.31445 | -51.91489 | 2026-07-07 04:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5b7fd1b-3302-3201-acf9-b2f744f24ca4 | -11.92365 | -43.37452 | 2026-07-07 04:25:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| aa45e3ce-fd08-3974-8f78-4f62a630726c | -12.75583 | -44.55772 | 2026-07-07 04:25:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9f6dab99-7089-3846-82ed-99c74a8ff42b | -11.66432 | -44.57153 | 2026-07-07 04:25:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b8a9f8f1-3884-3afd-9156-03368ac285ca | -13.27662 | -54.35737 | 2026-07-07 04:25:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README14.md)
