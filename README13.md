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
| 3f2fe35a-b797-31fb-99cf-619903fcc2a9 | -10.30347 | -57.12346 | 2025-06-27 04:21:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 367a7460-ee3e-3cf2-bdb3-2be4a44d263e | -12.75598 | -44.41074 | 2025-06-27 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| fab4bba3-9e5c-3820-9da5-dc2e90aecb75 | -11.56862 | -52.11325 | 2025-06-27 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 35.6 |
| a48ef966-cd59-38ed-b1b8-84ff4124ec5d | -9.37668 | -48.54016 | 2025-06-27 04:21:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 741fe19f-13d0-3af7-8796-5f6512b7f556 | -11.89254 | -48.25725 | 2025-06-27 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05e0d2f4-38d1-3eb4-ade1-2636b53921bb | -8.84367 | -49.85442 | 2025-06-27 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72446860-d5d1-3b8b-9cde-1dbec82d5215 | -10.62635 | -46.71086 | 2025-06-27 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a9ec2ad-62d9-35b4-acd9-4d78eca47768 | -12.75543 | -44.41449 | 2025-06-27 04:21:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ff9424c9-6eb4-3436-849b-ba9c03e8f3fe | -11.05624 | -55.37372 | 2025-06-27 04:21:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 15745c11-7d26-3912-a3b5-ac1189a0604b | -10.41831 | -47.51236 | 2025-06-27 04:21:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd994dc7-eeb7-30d2-8eab-e38eb24fa30d | -13.10366 | -52.29274 | 2025-06-27 04:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e76c52a7-a2c5-3cc8-bdd7-1c00419bbe76 | -14.38157 | -50.32742 | 2025-06-27 04:21:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 55c25b47-772b-3710-b4d1-2214c4f92118 | -11.36162 | -48.70638 | 2025-06-27 04:21:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d981a3c6-d7c4-353b-b3d7-e9bb7287fe05 | -11.77445 | -55.04119 | 2025-06-27 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1404a60c-e5d7-350d-b783-af15afaff680 | -9.23293 | -50.03214 | 2025-06-27 04:21:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1cde060-cfda-3612-a1eb-0ad6b6315e13 | -11.43668 | -54.46909 | 2025-06-27 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5c833ce-c372-39ce-bb66-43873ed01e5f | -10.4223 | -47.50923 | 2025-06-27 04:21:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 82405bd6-e73e-3d7e-ade0-84c263198e4b | -10.71336 | -59.13105 | 2025-06-27 04:21:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8d0b7569-6c39-34f1-adf0-ae55a03d1fad | -11.06227 | -55.37121 | 2025-06-27 04:21:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 244df7cb-bd56-383c-a8da-597884891411 | -8.84283 | -49.85936 | 2025-06-27 04:21:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f217e762-d946-3e3c-9816-90caac24e218 | -10.83055 | -53.74232 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 18997913-daa2-3411-b3a0-4b91bd7f32b0 | -14.21124 | -45.50893 | 2025-06-27 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e848b1bb-5e7e-3764-ab39-fc57643122fe | -12.02462 | -57.0909 | 2025-06-27 04:21:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 56a7095c-2293-3dce-89ad-4f46d9948fdc | -14.40964 | -47.89091 | 2025-06-27 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 927c2f6f-ae28-34fa-8acd-f4548b867c5e | -12.41666 | -46.66757 | 2025-06-27 04:21:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d1520e6-0a08-36b5-8090-055e0826cfcc | -10.86785 | -54.30306 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5ec389a9-fc01-3c12-8a45-559295612f17 | -10.82185 | -53.73514 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51d86294-7dcc-3d8c-b6ab-6ad7192008d1 | -9.36967 | -47.62782 | 2025-06-27 04:21:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5cc250d6-80f0-3ff6-ad3d-d74cd1393e17 | -10.30081 | -57.13734 | 2025-06-27 04:21:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4ae5764d-9235-37c5-b81f-d66d5e2a4257 | -9.34541 | -58.85415 | 2025-06-27 04:21:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4267093-790c-39c8-9834-ef92a850146b | -14.43837 | -48.87085 | 2025-06-27 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6b4ca8d3-4e9b-35ef-b87d-1c1ee1b9aa36 | -10.85986 | -54.03848 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 26653965-2711-3104-a95b-f056936c0fed | -11.59067 | -44.64701 | 2025-06-27 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ee349a7b-fc66-32b1-a2ef-143d58e679e7 | -11.78024 | -55.03896 | 2025-06-27 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 669022b3-0fa4-368e-96a9-3cd5264540eb | -12.1336 | -54.667 | 2025-06-27 04:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0740db0-cdee-3b54-8caa-4458c95ffc4e | -13.29338 | -57.08968 | 2025-06-27 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| be82e384-96d9-3098-a421-a41ae626c279 | -10.85879 | -54.04432 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 68812de4-8028-32e4-ba2c-0176a2184a63 | -10.85493 | -54.03751 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a15a9777-57fc-3ea6-ba44-0ee75703d489 | -9.11983 | -49.44164 | 2025-06-27 04:21:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 28112628-2a0d-339c-94fb-541ce193e1a8 | -11.58067 | -52.1102 | 2025-06-27 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| e54ec308-a7ea-3e24-b217-cd0a25ba52d6 | -9.75913 | -48.04528 | 2025-06-27 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fff594fb-cc0f-3329-8a51-1e826124f766 | -11.8184 | -47.5301 | 2025-06-27 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57a23d3b-9ab9-320b-98a8-e08d4e71f1e1 | -10.63249 | -46.69367 | 2025-06-27 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 13360e60-2180-3832-88fa-3f0aeb65f091 | -11.58003 | -52.12385 | 2025-06-27 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 4265036f-e3fb-35e0-9f1e-95b7a4f4ed36 | -14.01416 | -54.49636 | 2025-06-27 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4cff8352-63d8-3603-949a-048b0ccd5fe8 | -11.80253 | -57.35386 | 2025-06-27 04:21:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a3ad52c-69aa-3ad4-b3fd-9721a08782b8 | -11.77625 | -55.03156 | 2025-06-27 04:21:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1902160-8b5c-3d88-ad57-772918a909a2 | -11.60763 | -55.54224 | 2025-06-27 04:21:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5fa6e1c7-6af1-33e2-8973-9229844c4f2e | -10.54348 | -46.35374 | 2025-06-27 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b42c802-5b04-3f6a-a8de-abab5c9ad983 | -13.10293 | -52.29677 | 2025-06-27 04:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f6bf446c-0fd4-3872-a742-a4e912dd6480 | -14.29443 | -41.60054 | 2025-06-27 04:21:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7fdc19a0-df41-339a-91f2-1bfd102d83ea | -9.50317 | -56.09606 | 2025-06-27 04:21:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0fd381a-370a-32e7-8d2d-816d9b7ba3c7 | -9.08925 | -47.97033 | 2025-06-27 04:21:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1329f989-cedf-3d9a-b1a3-e9fc752cbb73 | -11.37056 | -47.55091 | 2025-06-27 04:21:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 938ce42a-ed44-3202-96db-cd707b9153a0 | -10.03177 | -54.32833 | 2025-06-27 04:21:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| bff359be-a6f6-3bd3-9406-dec5b6fa6fa8 | -11.06698 | -55.37574 | 2025-06-27 04:21:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4539d135-e31c-3119-b523-a96e9a4b7a8e | -10.37399 | -48.30561 | 2025-06-27 04:21:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| db329ba8-9bea-35d8-94a3-b00a95ecca18 | -9.07224 | -49.42173 | 2025-06-27 04:21:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5ae4ad42-1125-3724-8388-81634688dcf8 | -10.82378 | -53.75213 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d6be8755-62ec-3a53-8b9c-b50c290a5597 | -10.82957 | -53.74773 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e4904804-8de8-3971-8a88-6493397edb46 | -11.60407 | -55.54826 | 2025-06-27 04:21:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fe0e867a-6a70-34b8-9edd-92bd9275a9b9 | -10.80791 | -57.75629 | 2025-06-27 04:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e7193d33-e723-358b-b113-d8d719d65076 | -11.75557 | -54.23158 | 2025-06-27 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1cf92619-8d2c-3311-817f-018f7919b031 | -14.44181 | -48.87146 | 2025-06-27 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2cf5d01f-4d5c-3138-8299-be9623bcdd5d | -12.03624 | -48.75481 | 2025-06-27 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b0106d7c-c58f-3599-a68d-d2b85b6d082c | -9.79055 | -48.56279 | 2025-06-27 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 977e917b-23d2-36db-b909-9f710c4a9ab1 | -12.60422 | -57.88389 | 2025-06-27 04:21:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f052b278-7c6f-354f-bef0-592669c712eb | -10.82475 | -53.74675 | 2025-06-27 04:21:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 91edccb2-1d40-314d-9f7d-811def45b260 | -11.60473 | -55.54472 | 2025-06-27 04:21:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d44394b7-4745-3fef-a0cd-f516c24d0ee2 | -11.80695 | -47.52488 | 2025-06-27 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b9e9ca9f-7eef-3eb2-acdc-cfe24079702a | -14.02002 | -54.49176 | 2025-06-27 04:21:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 692eb8f9-4373-364c-a08f-0aa972d7c76a | -11.11429 | -47.00285 | 2025-06-27 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ae32babd-affc-3775-b30a-b223f3ce6d05 | -11.95442 | -47.02726 | 2025-06-27 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b3297d0d-2321-38e5-846c-e73b86cf01c8 | -8.61272 | -51.58297 | 2025-06-27 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 4f9579d8-9b20-3cf6-8e12-3e60a4972cb7 | -9.07072 | -49.4309 | 2025-06-27 04:21:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 891f6e7e-44e5-3a81-8959-beba91865c62 | -9.12281 | -49.44688 | 2025-06-27 04:21:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b363691e-3f53-3d1f-94d8-eaabddf1dc87 | -11.67053 | -46.73633 | 2025-06-27 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3124dfe-be43-34d2-9840-cf91d7f29e2e | -12.10788 | -54.66527 | 2025-06-27 04:21:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebf2d13e-27be-33e3-9e00-2399c1690de1 | -9.82092 | -48.38125 | 2025-06-27 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 918570d2-c237-345e-9d05-e232dde3b1b9 | -16.68181 | -43.88551 | 2025-06-27 04:21:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b78143d3-bfcd-3293-9eb9-8f3a1096684b | -14.2107 | -45.51255 | 2025-06-27 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1cb28bcb-a835-30d8-8a08-1b4b2599d4bb | -11.57144 | -52.12238 | 2025-06-27 04:21:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 1feb38e3-c07f-31cd-aa05-5b2c57cdf033 | -10.27294 | -47.60387 | 2025-06-27 04:21:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9d7f9542-70ca-356d-84c5-0091ac23d8f3 | -14.20827 | -42.78133 | 2025-06-27 04:21:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 8683a039-c8ba-3bb3-91bf-c08600ac3671 | -12.01371 | -47.16595 | 2025-06-27 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bcf40e14-66b1-3b20-b6e2-2b57e79c8db4 | -11.368 | -48.71164 | 2025-06-27 04:21:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fed8bb13-0237-3cd3-b3c2-793750977970 | -9.79061 | -48.56805 | 2025-06-27 04:21:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9cfd85d2-fb9e-368a-90df-0efbaa1bfe2b | -11.60696 | -55.5457 | 2025-06-27 04:21:00 | NOAA-21 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 32bc1654-1467-3647-91d7-4f2910623a29 | -11.43559 | -54.47497 | 2025-06-27 04:21:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ee227d4-22a2-3b92-a3f8-89f3e028b13f | -13.58989 | -45.25898 | 2025-06-27 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6b3f04d3-11c8-3ab3-8022-2119667263fb | -15.56951 | -47.85682 | 2025-06-27 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 493b1e19-47f2-33ad-aa8c-4c32b062087d | -12.04801 | -48.07938 | 2025-06-27 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 450d29d0-6e34-3f4d-8d4c-b2eb87c142c7 | -10.27691 | -47.60406 | 2025-06-27 04:21:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 27662119-1139-3530-832a-c553b41a72d7 | -12.00037 | -47.16377 | 2025-06-27 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbe0843a-a8fd-3e13-81c8-84890f59c20a | -10.54567 | -46.3613 | 2025-06-27 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a042c792-2bd1-3a2a-a90f-54f553c4ef0d | -10.81418 | -57.75741 | 2025-06-27 04:21:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56804e04-425a-33e1-9361-6d5c1eb793a0 | -10.42133 | -48.6174 | 2025-06-27 04:21:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e6235812-6572-38dc-824d-14122c3484cc | -11.5868 | -44.67237 | 2025-06-27 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c171fb6d-1179-3af9-b8ac-0119d66a3c5d | -8.61989 | -51.56712 | 2025-06-27 04:21:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8e4f0489-f1b5-3206-9a95-7c16372112a6 | -12.00428 | -47.16074 | 2025-06-27 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README14.md)
