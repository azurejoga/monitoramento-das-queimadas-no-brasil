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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b258139-64a7-3d40-9d4d-e625d8076373 | -18.67261 | -44.04255 | 2025-10-07 03:19:00 | NOAA-20 | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ffa214b8-2d19-3a9e-812b-24a5e6395dfd | -20.11131 | -44.41552 | 2025-10-07 03:19:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 43118395-5b11-33c0-8a86-cfe6e83737e3 | -20.74325 | -43.47465 | 2025-10-07 03:19:00 | NOAA-20 | LAMIM | MINAS GERAIS | Brasil | 3137908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| bcf93229-039c-3495-a917-c2b3c02ab1aa | -21.61689 | -44.0 | 2025-10-07 03:19:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5feac310-9bab-3f49-8251-4a3d4b08dd55 | -21.90323 | -44.89011 | 2025-10-07 03:19:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 2fa373ce-ab5a-3093-9392-3064401a5454 | -21.61982 | -44.00072 | 2025-10-07 03:19:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 189662d8-3bbc-39e6-8481-89cbd73bdebd | -22.88112 | -43.7241 | 2025-10-07 03:19:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 10b5aabb-6bf5-3898-a69f-6c7567773466 | -19.10566 | -43.16847 | 2025-10-07 03:19:00 | NOAA-20 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 33391088-ea1c-3be1-b8a1-afd31ce6da77 | -22.54599 | -44.45351 | 2025-10-07 03:19:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 6f7f11b9-40ea-3827-8382-6b5acfacd486 | -20.25586 | -41.94028 | 2025-10-07 03:19:00 | NOAA-20 | REDUTO | MINAS GERAIS | Brasil | 3154150 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d5354412-5038-3e74-aea3-7e98c082e833 | -22.13055 | -42.91391 | 2025-10-07 03:19:00 | NOAA-20 | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 78ebb109-eb09-31b5-ae9d-913356aa75b9 | -21.07795 | -46.89926 | 2025-10-07 03:19:00 | NOAA-20 | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1f42c7ea-5f2d-3409-a50d-86c8701e52bd | -20.31782 | -45.11874 | 2025-10-07 03:19:00 | NOAA-20 | PEDRA DO INDAIÁ | MINAS GERAIS | Brasil | 3148905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| c603838f-4004-3cdd-bd70-f0757134994f | -20.20323 | -43.91431 | 2025-10-07 03:19:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b9d16b4b-5ce5-3303-acd7-16ef174e1add | -20.19982 | -43.92886 | 2025-10-07 03:19:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7cbc1d28-f7ee-3409-a614-b17f72300d6c | -20.2069 | -43.92242 | 2025-10-07 03:19:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5384afde-d8f5-3f97-9945-023f879f86b6 | -17.96095 | -44.40524 | 2025-10-07 03:19:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a8386f00-b7c8-3b26-916e-d3ccd4c586ab | -20.2069 | -43.92586 | 2025-10-07 03:19:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5d2ae126-1010-3d29-97a2-6e2433289f46 | -23.31541 | -46.94614 | 2025-10-07 03:19:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 36a96615-1eb7-3819-b876-4b85619440ed | -19.78703 | -45.85417 | 2025-10-07 03:19:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8800f90b-ffa6-3776-8790-1d11f42777fb | -21.5466 | -44.27905 | 2025-10-07 03:19:00 | NOAA-20 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| a9bd1c72-5e8e-351e-bb9d-35935733b384 | -19.84805 | -43.25461 | 2025-10-07 03:19:00 | NOAA-20 | SÃO GONÇALO DO RIO ABAIXO | MINAS GERAIS | Brasil | 3161908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f85838f4-f376-38d7-b547-d3811c0d0086 | -20.20795 | -43.91776 | 2025-10-07 03:19:00 | NOAA-20 | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2d1125df-1d8c-3c52-b021-b0909d3d7ae7 | -22.552 | -44.45467 | 2025-10-07 03:19:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 67760445-6051-3e2d-b29d-6137d7f37937 | -21.74357 | -44.42458 | 2025-10-07 03:19:00 | NOAA-20 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 780bfefd-1e5a-3d72-bfba-9b2ed3090690 | -21.54767 | -44.27442 | 2025-10-07 03:19:00 | NOAA-20 | MADRE DE DEUS DE MINAS | MINAS GERAIS | Brasil | 3139102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 361d24fa-3743-33fb-9e00-2d7ba77b360c | -20.82434 | -42.48712 | 2025-10-07 03:19:00 | NOAA-20 | MIRADOURO | MINAS GERAIS | Brasil | 3142106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 5757bfef-8fe9-3f90-b4ac-b7f75465aa08 | -21.90457 | -44.88446 | 2025-10-07 03:19:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| fa2b0f9b-3971-336f-ad2a-5f205d184edd | -21.60999 | -44.00297 | 2025-10-07 03:19:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 1a8d9744-be45-3507-a427-5811fe1716e9 | -21.52269 | -45.59529 | 2025-10-07 03:19:00 | NOAA-20 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 294f2d6e-10eb-3dfb-9172-5e3b2aa470af | -22.54476 | -44.45872 | 2025-10-07 03:19:00 | NOAA-20 | RESENDE | RIO DE JANEIRO | Brasil | 3304201 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| bc5877fa-c1c6-3a7b-a074-bf48dcf1fa82 | -21.89844 | -44.88282 | 2025-10-07 03:19:00 | NOAA-20 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| e4697d25-af15-399d-af7c-680663e03f31 | -21.4903 | -46.03155 | 2025-10-07 03:19:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| dc8504f3-7b40-3b7c-b508-62d3b2bd2af7 | -18.04744 | -43.15232 | 2025-10-07 03:19:00 | NOAA-20 | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 248d8ae6-3564-3959-a336-fec230c95967 | -20.11261 | -44.40999 | 2025-10-07 03:19:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 846f6a60-e787-37c1-8726-8ba84987647c | -4.6875 | -45.828 | 2025-10-07 03:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 9fc7efb3-720d-3a6a-9034-1aff75a500fa | -14.7775 | -46.03 | 2025-10-07 03:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 142.1 |
| 0efd0d3f-6012-39fa-b20d-146da6f33723 | -5.7217 | -44.8366 | 2025-10-07 03:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| f574205b-5d2b-37af-a107-6f5f08c23249 | -5.852 | -42.8608 | 2025-10-07 03:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |
| e58deb91-6a27-3a52-bb66-06024889457c | -4.7061 | -45.8269 | 2025-10-07 03:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 61.1 |
| e223e434-4009-338e-8005-4218c4aac17b | -6.4543 | -44.5749 | 2025-10-07 03:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| f232fb6c-6746-3fe8-b29c-6ac4633e9a04 | -5.8522 | -42.8372 | 2025-10-07 03:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 59.4 |
| 350e29a4-4412-300a-a32a-d1139222d1fb | -10.4291 | -50.3091 | 2025-10-07 03:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 0b0d3d0a-a72c-3b42-8573-18a86fa74348 | -14.922 | -51.4507 | 2025-10-07 03:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 0a2b30f6-88f5-361d-8ed2-ba379eae677a | -14.758 | -46.0335 | 2025-10-07 03:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 123.1 |
| af0e6bd5-b9bd-3e59-b734-e66c7c7a3cac | -14.7575 | -46.0566 | 2025-10-07 03:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 259.6 |
| 3d2056b8-e866-3d69-aef1-2d212d48f40c | -10.748 | -50.4892 | 2025-10-07 03:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 015d218a-58d7-3d72-92f5-ec2c39cee1c4 | -10.4466 | -50.414 | 2025-10-07 03:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| a5f06054-9e76-35cc-8958-b197b9e4a8bc | -22.0071 | -49.7321 | 2025-10-07 03:20:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 89.4 |
| 1187f09b-e955-365d-8f5a-803f42407a5e | -4.6873 | -45.8504 | 2025-10-07 03:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 139.8 |
| 167c5372-fd59-39dc-a34e-f3134cff8eb9 | -13.5072 | -43.6594 | 2025-10-07 03:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 4e0c397d-9926-3ef5-bd70-45994f88312c | -5.703 | -44.838 | 2025-10-07 03:20:00 | GOES-19 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 53.9 |
| a392c301-e135-36d9-b637-15a44b370189 | -10.8731 | -51.0289 | 2025-10-07 03:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 77f56ed4-43e4-38ff-a583-e5d327b00799 | -4.706 | -45.8493 | 2025-10-07 03:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 630a9e60-4278-325e-b26d-f00e31f51fc1 | -10.4099 | -50.3324 | 2025-10-07 03:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 45.6 |
| ce7ee3d7-3ebc-3b82-aa71-658cfd75780e | -10.7291 | -50.4912 | 2025-10-07 03:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 53c989bb-d95a-3119-904d-a0fb50bf2100 | -13.5067 | -43.6832 | 2025-10-07 03:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 0dd45fa0-2157-3165-a6f6-4976cbefa3c7 | -10.4288 | -50.3305 | 2025-10-07 03:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 6b1d6624-bf78-3e19-ba83-0cf8e2e5f30a | -10.4102 | -50.311 | 2025-10-07 03:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| decfe2be-dc79-31de-ac0c-b2e2996e19e3 | -22.0077 | -49.709 | 2025-10-07 03:20:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.2 |
| 8d8096fc-956c-3306-96c0-2ce29e2687e8 | -14.7765 | -46.0763 | 2025-10-07 03:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 0c5278f3-292d-3436-97c3-787a3d35e5d1 | -14.777 | -46.0532 | 2025-10-07 03:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 490.7 |
| 60479d97-0137-3001-a232-d9d46a9c2d06 | -14.7389 | -46.0138 | 2025-10-07 03:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 92.2 |
| 01cd9ca0-9a4a-3d39-83f6-c7140df4277f | -4.6687 | -45.8514 | 2025-10-07 03:20:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 58.6 |
| d1c05c19-0ff9-3e47-b553-8d62f48bb48f | -22.0279 | -49.7274 | 2025-10-07 03:20:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 86.2 |
| ff39c38a-26f0-3020-8377-83e74a794184 | -10.4288 | -50.3305 | 2025-10-07 03:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 28361447-9a2c-3c06-b855-e288fe411e9f | -8.5395 | -46.2406 | 2025-10-07 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 3e93cfa6-1343-33dd-aff6-50c15d5c493c | -10.4099 | -50.3324 | 2025-10-07 03:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 178c29e3-c060-370c-bccf-6c54b89eedee | -5.5125 | -43.0747 | 2025-10-07 03:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 25a28e82-b738-369d-ac19-203b761418c6 | -13.5072 | -43.6594 | 2025-10-07 03:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 80.9 |
| ebd244fe-9a01-3964-90b9-731672098acb | -3.0864 | -50.5835 | 2025-10-07 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.1 |
| ed81e74a-ba90-3896-b03f-4e2ff75c2fc4 | -22.0279 | -49.7274 | 2025-10-07 03:30:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.4 |
| 608c09eb-abf0-343a-b336-b98898b62bc4 | -10.4466 | -50.414 | 2025-10-07 03:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 41.3 |
| a5a8ca30-2d6c-331b-929e-1e37d8aea247 | -6.454 | -44.5978 | 2025-10-07 03:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| b36bb9a3-5b2d-30d2-ad1e-3343222b3ff6 | -6.4543 | -44.5749 | 2025-10-07 03:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 0fe754c7-ae74-3584-a1bc-e673230bca58 | -10.7291 | -50.4912 | 2025-10-07 03:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 9eefe037-24e1-3790-8728-47bdbe09d9fc | -10.4102 | -50.311 | 2025-10-07 03:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 7c560c33-7298-3cf9-a354-601ed2c3437e | -21.5332 | -45.5856 | 2025-10-07 03:30:00 | GOES-19 | ELÓI MENDES | MINAS GERAIS | Brasil | 3123601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.2 |
| 169fcc42-ac9a-3450-ab70-b58cb24d5624 | -4.6875 | -45.828 | 2025-10-07 03:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 9827c26b-0f15-3305-9c14-a3fcdd7d30f2 | -13.5067 | -43.6832 | 2025-10-07 03:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 3668ea1c-7088-3fe2-8451-d8516525eb2b | -8.5393 | -46.2631 | 2025-10-07 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| fab80d4f-1aac-35fc-97b5-a69e9f30fba6 | -22.0071 | -49.7321 | 2025-10-07 03:30:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 105.3 |
| 2cfe594d-2099-3a55-9f55-405decfd54e3 | -14.922 | -51.4507 | 2025-10-07 03:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 711adc7b-bae5-3bc3-982f-ed590dbb1a34 | -10.4291 | -50.3091 | 2025-10-07 03:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| e710e5bc-2288-37c2-b073-7a9a9ba7af1c | -10.748 | -50.4892 | 2025-10-07 03:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 133792f0-f513-3a0d-9af2-8bac3027a6e5 | -4.7061 | -45.8269 | 2025-10-07 03:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 2fdd7ccc-18d8-3200-a590-4011655bcada | -4.6873 | -45.8504 | 2025-10-07 03:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 142.0 |
| 1043a7bc-78cf-35f8-8c78-f193f265ca5f | -4.706 | -45.8493 | 2025-10-07 03:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 3192fa28-f33c-3fcb-af52-7b47333655f1 | -4.6687 | -45.8514 | 2025-10-07 03:30:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 53.1 |
| d895a51e-6865-31f7-a51d-7ba7b5069c25 | -22.0071 | -49.7321 | 2025-10-07 03:40:00 | GOES-19 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.1 |
| 703d55c4-0fe4-3fa8-83fe-9f51dccbee83 | -10.3913 | -50.313 | 2025-10-07 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 50.1 |
| b1a71503-5641-3f75-9565-66e599507edd | -10.748 | -50.4892 | 2025-10-07 03:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 4063e8cb-fac6-32f0-9482-42d4248574d4 | -13.5067 | -43.6832 | 2025-10-07 03:40:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 81083912-8f88-3385-aaf9-6c93864466d7 | -10.7483 | -50.4679 | 2025-10-07 03:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 64.0 |
| f4b10034-b80e-3f5c-b17e-2450697cd62f | -10.4099 | -50.3324 | 2025-10-07 03:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 0b64dca3-5cc0-36d3-b8c8-2cfd3078d195 | -8.5395 | -46.2406 | 2025-10-07 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 260.4 |
| 4b97542c-813d-3399-8fce-59786b2869b0 | -4.6687 | -45.8514 | 2025-10-07 03:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 0352fb8a-1b83-3eaf-a351-d7f7cd47d06e | -6.4543 | -44.5749 | 2025-10-07 03:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| efeff962-aff6-3bbf-b03c-c75386849abe | -14.922 | -51.4507 | 2025-10-07 03:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 95a6e8ee-ab29-365b-93f0-8792d917987e | -4.6873 | -45.8504 | 2025-10-07 03:40:00 | GOES-19 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 108.4 |


[Clique aqui para ver as próximas entradas](README19.md)
