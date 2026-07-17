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
| 75a42f15-f84d-323f-b63c-c5a3f73d874a | -19.81862 | -57.97352 | 2026-07-17 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 187deff4-d486-3b49-b0dd-e9842556b568 | -22.46942 | -43.09328 | 2026-07-17 04:06:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 080a5951-2a4c-3353-a335-2c23833fa514 | -20.32983 | -46.64088 | 2026-07-17 04:06:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 132ccff9-3a9d-3367-a5ae-50e77d9dd3d9 | -19.86334 | -57.98894 | 2026-07-17 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.9 |
| ac33d73c-c691-35f1-a5e1-e0f74f5b75d1 | -22.24907 | -52.87137 | 2026-07-17 04:06:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| be8ce2da-2ff3-3029-b415-0dc5943b4a8f | -22.24336 | -52.8732 | 2026-07-17 04:06:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 55b1c084-52b6-3abb-b2a3-093a8a0a4781 | -21.77002 | -56.29976 | 2026-07-17 04:06:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 70e337f4-4a26-384c-a88c-514f2abd7bda | -19.83294 | -57.94594 | 2026-07-17 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| ef19a2be-2dd7-31f9-8a83-432f4a78137c | -19.83973 | -57.97929 | 2026-07-17 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 7e133ece-4543-3173-85d8-3bcbdb338230 | -20.33863 | -46.63348 | 2026-07-17 04:06:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1d1182c8-9cd3-3f29-afa9-034ee516c873 | -20.70784 | -47.29149 | 2026-07-17 04:06:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e34a8d2a-b1df-3743-8fa9-85dd5938635a | -19.82566 | -57.97543 | 2026-07-17 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 3bcb9a44-1d39-34cf-951b-8d91178173e6 | -23.10115 | -48.75073 | 2026-07-17 04:06:00 | NOAA-21 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 99879a70-7740-32ba-81ee-e0a4899d133c | -22.24594 | -52.87512 | 2026-07-17 04:06:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 58f9dc3f-5ab1-3673-9ca0-469ca0c81e9d | -19.8327 | -57.97735 | 2026-07-17 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 84cd8adb-a63a-31b0-8b31-c7fb3862eedd | -22.91696 | -49.20529 | 2026-07-17 04:06:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68902947-9f20-337c-9b3a-2ceda24f1110 | -20.33423 | -46.63723 | 2026-07-17 04:06:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c8032ae4-ca0b-3095-8c97-1552c3082de9 | -22.46886 | -43.09697 | 2026-07-17 04:06:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 4ee41ddb-afee-39ae-ac9c-60e77980f378 | -23.50741 | -48.57049 | 2026-07-17 04:06:00 | NOAA-21 | ANGATUBA | SÃO PAULO | Brasil | 3502200 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f919449b-b872-3197-9818-65f5f2bec562 | -19.84677 | -57.98121 | 2026-07-17 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 6088ca54-80cd-32ff-b2a9-caaee30682aa | -20.65655 | -48.68008 | 2026-07-17 04:06:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bb797527-fbf7-3a5c-9af4-d8e3ef821a05 | -22.46555 | -43.09631 | 2026-07-17 04:06:00 | NOAA-21 | PETRÓPOLIS | RIO DE JANEIRO | Brasil | 3303906 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| a9dcbc1b-9abe-3b62-9624-3f081bd7a6b9 | -20.4377 | -43.69439 | 2026-07-17 04:06:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| eb208af5-72b6-3cd2-a1b3-ba8af16ca0b5 | -20.54979 | -41.27584 | 2026-07-17 04:06:00 | NOAA-21 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5530218d-3dc0-3402-85aa-260bb28a4c63 | -23.10503 | -48.75155 | 2026-07-17 04:06:00 | NOAA-21 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b5410d48-2c3d-3484-9971-0354be95e9c2 | -20.343 | -46.6299 | 2026-07-17 04:06:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e3fce91-5a81-339b-a2fc-9db66707e3a2 | -19.83477 | -57.93856 | 2026-07-17 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| a0e8b0cd-85aa-385c-80bf-bd4f85a9dae4 | -21.2766 | -44.51054 | 2026-07-17 04:06:00 | NOAA-21 | NAZARENO | MINAS GERAIS | Brasil | 3144508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f06dcaca-d5c1-3a68-ac14-d8ea9f533114 | -21.72399 | -41.20618 | 2026-07-17 04:06:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a78503ff-069e-3a85-b7bb-f4017c7165b7 | -19.85629 | -57.98705 | 2026-07-17 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 8f0a2d79-3b2e-318c-af5e-48286c4d0dd7 | -21.66699 | -56.33037 | 2026-07-17 04:06:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 069f2a83-72b9-382f-a54f-84e0012ddfdb | -20.92047 | -47.02475 | 2026-07-17 04:06:00 | NOAA-21 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 508730f1-eea4-3f91-8100-0ee16f48bd13 | -22.24663 | -52.87197 | 2026-07-17 04:06:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 2a70b457-5297-3543-b7ee-177776316e89 | -23.78655 | -48.4569 | 2026-07-17 04:06:00 | NOAA-21 | BURI | SÃO PAULO | Brasil | 3508009 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| ef6496c5-8be6-3443-8d99-7e2cd3f39de7 | -22.4908 | -44.04939 | 2026-07-17 04:06:00 | NOAA-21 | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 11a8af1f-a445-332b-9dbd-56ca62977595 | -20.33337 | -46.64206 | 2026-07-17 04:06:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39fef7b3-d843-312f-8ee1-b9bacb0e3167 | -22.2484 | -52.87452 | 2026-07-17 04:06:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 10a58218-b27f-38dd-936d-7247a8b7bac3 | -20.61716 | -46.29201 | 2026-07-17 04:06:00 | NOAA-21 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7f34fcd-9012-3bc5-a403-a3238f0c6fc4 | -19.86084 | -57.98505 | 2026-07-17 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 4245ec03-56cd-3940-9928-4ea901d8aa32 | -21.35099 | -51.04474 | 2026-07-17 04:06:00 | NOAA-21 | VALPARAÍSO | SÃO PAULO | Brasil | 3556305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 2ffc5f58-b7d7-3c51-999e-17b7bc81d0f1 | -20.65071 | -50.11087 | 2026-07-17 04:06:00 | NOAA-21 | FLOREAL | SÃO PAULO | Brasil | 3515905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 52475900-8e4a-3c42-b7c2-2d66d73f6f1d | -21.66087 | -56.32821 | 2026-07-17 04:06:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| de0684a5-9293-3d7b-bcc0-bc4cb8632ae7 | -19.81524 | -57.95684 | 2026-07-17 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| eccc41d4-07fd-3461-88c7-0b8643d045c2 | -21.05998 | -43.32817 | 2026-07-17 04:06:00 | NOAA-21 | ALTO RIO DOCE | MINAS GERAIS | Brasil | 3102100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 5c7dc53c-1b91-32a4-ab2f-4d5d61020c00 | -22.24469 | -52.86695 | 2026-07-17 04:06:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| a0a5d067-b9aa-3f8c-ad96-d7e888eaaa88 | -22.24732 | -52.86886 | 2026-07-17 04:06:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| a3508559-bc7b-39f8-ad4f-d92e94e29612 | -21.66633 | -56.3178 | 2026-07-17 04:06:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1af108c-ad3d-39ba-bf2d-315e31d9b345 | -21.02777 | -44.17658 | 2026-07-17 04:06:00 | NOAA-21 | CORONEL XAVIER CHAVES | MINAS GERAIS | Brasil | 3119708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3599771e-f7ba-3249-8778-805f3ffb24ce | -19.82592 | -57.94403 | 2026-07-17 04:06:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 54a383d3-159d-3e83-9478-146cd6213d82 | -19.88179 | -44.76365 | 2026-07-17 04:06:00 | NOAA-21 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a4470609-81f7-3401-8f5c-bc515384605e | -20.64504 | -41.4152 | 2026-07-17 04:06:00 | NOAA-21 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d5eacc41-74b1-3824-8b54-cb4518bc73b9 | -22.49139 | -44.04566 | 2026-07-17 04:06:00 | NOAA-21 | VOLTA REDONDA | RIO DE JANEIRO | Brasil | 3306305 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 372d5467-bd27-34fa-bd17-5920e65161c1 | -29.10037 | -50.6228 | 2026-07-17 04:08:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 618354a3-10a6-30c2-b084-bafe5d0a9ae7 | -29.89898 | -53.9603 | 2026-07-17 04:08:00 | NOAA-21 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 2.8 |
| 43a0e3dc-25e5-3106-939b-7813d47146be | -28.84273 | -50.69482 | 2026-07-17 04:08:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a9ec901b-54a7-35a2-b9c6-1f722b1708b4 | -28.53211 | -50.57518 | 2026-07-17 04:08:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d7647dc1-6c01-3495-90b9-dfd82babb44d | -29.10148 | -50.6172 | 2026-07-17 04:08:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6a7f5bb2-1105-305a-8bf3-080e35c1c479 | -29.87203 | -54.63656 | 2026-07-17 04:08:00 | NOAA-21 | CACEQUI | RIO GRANDE DO SUL | Brasil | 4302907 | 43 | 33 | nan | nan | nan | Pampa | 2.5 |
| 55a64759-7b58-36c1-93f8-44448913456c | -30.74265 | -54.36314 | 2026-07-17 04:08:00 | NOAA-21 | LAVRAS DO SUL | RIO GRANDE DO SUL | Brasil | 4311502 | 43 | 33 | nan | nan | nan | Pampa | 2.8 |
| edb19355-be95-3783-bb0c-43beff72207b | -28.89381 | -52.62187 | 2026-07-17 04:08:00 | NOAA-21 | SOLEDADE | RIO GRANDE DO SUL | Brasil | 4320800 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b19f3d86-97d5-3801-b5da-855192242452 | -29.09759 | -50.61632 | 2026-07-17 04:08:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 6d066348-21d9-32a4-b5b3-30cada070cb0 | -25.42829 | -52.89804 | 2026-07-17 04:08:00 | NOAA-21 | QUEDAS DO IGUAÇU | PARANÁ | Brasil | 4120903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| b24ac679-4b61-32bf-b41b-3488077dfd92 | -28.53301 | -50.5739 | 2026-07-17 04:08:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 66784a6e-c281-342c-a4c3-9285c521ed85 | -32.34945 | -52.39482 | 2026-07-17 04:08:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 1.7 |
| a2121dac-5753-3f37-8648-b26cd70922ae | -29.89563 | -53.9534 | 2026-07-17 04:08:00 | NOAA-21 | SANTA MARIA | RIO GRANDE DO SUL | Brasil | 4316907 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| 824be674-df47-3d59-945c-073adeb32201 | -27.3477 | -50.72822 | 2026-07-17 04:08:00 | NOAA-21 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b7381d2e-7ea7-30b8-8a19-d3a8a14f6d8a | -28.88514 | -52.61945 | 2026-07-17 04:08:00 | NOAA-21 | SOLEDADE | RIO GRANDE DO SUL | Brasil | 4320800 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 202b00b3-fc74-3ef0-9e35-466199cc9dda | -25.42786 | -52.90104 | 2026-07-17 04:08:00 | NOAA-21 | QUEDAS DO IGUAÇU | PARANÁ | Brasil | 4120903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 99828325-14ef-3f75-b0fd-eeaae8877e3a | -28.53713 | -50.57057 | 2026-07-17 04:08:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 88a000cf-6286-3e83-9316-70d3c9834553 | -32.3498 | -52.39368 | 2026-07-17 04:08:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 2.3 |
| e2c8cd9a-23f0-3c56-989f-11a37cb0293f | -28.9868 | -50.43272 | 2026-07-17 04:08:00 | NOAA-21 | JAQUIRANA | RIO GRANDE DO SUL | Brasil | 4311122 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| e5798399-b241-3259-96d8-a2cce09419da | -30.69574 | -52.56236 | 2026-07-17 04:08:00 | NOAA-21 | ENCRUZILHADA DO SUL | RIO GRANDE DO SUL | Brasil | 4306908 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 0e285859-5f48-3224-bf4e-b1649c2e764f | -28.84538 | -50.69723 | 2026-07-17 04:08:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1cba4eb1-2494-3476-a839-089638735b7d | -31.32105 | -54.16043 | 2026-07-17 04:08:00 | NOAA-21 | BAGÉ | RIO GRANDE DO SUL | Brasil | 4301602 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 3dc0a941-e111-3aa1-812d-9e48ac8ec3fa | -28.84554 | -50.70144 | 2026-07-17 04:08:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 9c666f12-417d-3ecd-ac05-18e9e2d06825 | -28.53691 | -50.5749 | 2026-07-17 04:08:00 | NOAA-21 | BOM JESUS | RIO GRANDE DO SUL | Brasil | 4302303 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a3665b1d-6431-3e41-b539-2a98077e813c | -29.22962 | -55.76176 | 2026-07-17 04:08:00 | NOAA-21 | ITAQUI | RIO GRANDE DO SUL | Brasil | 4310603 | 43 | 33 | nan | nan | nan | Pampa | 1.9 |
| 0292d920-74ff-392e-a51e-bb4d24148c2d | -28.88512 | -52.6207 | 2026-07-17 04:08:00 | NOAA-21 | SOLEDADE | RIO GRANDE DO SUL | Brasil | 4320800 | 43 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| af1c980a-ce1f-36d5-8d05-66edeff8b5a7 | -28.84425 | -50.70288 | 2026-07-17 04:08:00 | NOAA-21 | SÃO FRANCISCO DE PAULA | RIO GRANDE DO SUL | Brasil | 4318200 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| be8cf1a2-fc6d-3e28-95dc-a40fe8595b22 | -28.89378 | -52.62312 | 2026-07-17 04:08:00 | NOAA-21 | SOLEDADE | RIO GRANDE DO SUL | Brasil | 4320800 | 43 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a3ab4c29-5d97-396d-be9e-71a70708de79 | -9.4581 | -64.0519 | 2026-07-17 04:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 131.7 |
| 6d45ab2a-c596-32bd-9591-0f2f70473832 | -9.4582 | -64.033 | 2026-07-17 04:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 178.1 |
| 4da0edf0-d8b5-32d3-a6a8-7bcd2063880d | -13.2451 | -45.1142 | 2026-07-17 04:10:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 4e58f65e-ad08-3202-b3d8-ee10d99908dd | -13.2649 | -45.0877 | 2026-07-17 04:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 9c577c44-13bb-38a4-bbf6-44b58da3c969 | -9.4582 | -64.033 | 2026-07-17 04:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 126.4 |
| dbbe978f-a883-3a7b-aeb3-e62238195940 | -13.2645 | -45.111 | 2026-07-17 04:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 4733d3ea-4ed7-3a4d-b72e-43c8f24713f4 | -9.4581 | -64.0519 | 2026-07-17 04:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 86.6 |
| d116f786-15bc-3863-bd07-6065b8bfdb11 | -13.2456 | -45.0909 | 2026-07-17 04:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 85a0902b-9001-32d2-841a-22e781e1c298 | -13.2451 | -45.1142 | 2026-07-17 04:20:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 134.9 |
| 16c9ae7f-6ba6-3ecf-8f49-22bbbf5d615a | -13.2456 | -45.0909 | 2026-07-17 04:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 2a7165c9-c29a-373a-ac91-d7919c20609e | -13.2645 | -45.111 | 2026-07-17 04:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 155.9 |
| a4a52072-a3d8-3c55-a43e-c0b1d8b79274 | -13.2649 | -45.0877 | 2026-07-17 04:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| cc2b094d-cd32-3964-b31b-e47ef79064dd | -13.2451 | -45.1142 | 2026-07-17 04:30:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 146.0 |
| bac62127-1b89-3fab-b2c0-e05892749349 | -0.08864 | -51.2807 | 2026-07-17 04:36:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ce6c1933-6aaf-31d4-8a44-6e35f87e669d | -5.79668 | -43.63811 | 2026-07-17 04:36:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3289a361-c9f9-39e0-9891-b2393126f7cb | -3.50411 | -48.03565 | 2026-07-17 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4c64894-6c03-3bc5-8764-8dcd45f69652 | -5.60321 | -43.34645 | 2026-07-17 04:36:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c5cddcf-394c-3e09-bd62-10b66bac226d | -5.60543 | -36.8704 | 2026-07-17 04:36:00 | NPP-375D | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8ef00511-2aa2-3d39-b210-f33cae1584c7 | -4.65568 | -42.42317 | 2026-07-17 04:36:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8415ef11-d97f-3ff2-901b-240b420624f0 | -5.80083 | -43.63467 | 2026-07-17 04:36:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README8.md)
