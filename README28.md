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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c28c388-c501-3394-b476-5368afb0185c | -13.63322 | -47.90157 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bbae2875-cc9b-3ebd-b002-5c637d4cd533 | -11.26506 | -54.12856 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8e101d89-9591-3e9c-9f9d-0b5d35025e7a | -9.68404 | -54.84371 | 2026-09-14 04:34:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a39a3a3c-2df3-3de6-9e94-f8e0331f659f | -15.00946 | -48.5203 | 2026-09-14 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4363e8a-88c4-3b38-a3c7-7e36e81ec24a | -11.22535 | -43.43333 | 2026-09-14 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e085ea57-9adb-3aa4-89d6-eb787771133f | -11.36475 | -43.96512 | 2026-09-14 04:34:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f78c9b96-453e-3c2b-9309-0eeb15ca95d0 | -14.81819 | -48.15427 | 2026-09-14 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0bd73700-bc16-3da8-bb0d-2359800fdf83 | -15.05527 | -48.55865 | 2026-09-14 04:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e41603e3-89b7-3726-9af0-1f613c29ff6b | -10.6841 | -54.15257 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 847f62ad-0912-3c1a-aca3-a4ffa4fb652d | -10.67793 | -54.15753 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 6a264636-7d1f-309c-944c-ab9934bb7910 | -13.0009 | -49.81232 | 2026-09-14 04:34:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 200091c7-c4a7-3604-a536-54046f2b9954 | -10.67682 | -54.13591 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9395895-ee80-3fcf-88db-287612ef47c2 | -10.57292 | -51.33588 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d050781-0d71-3a9c-833a-3bd5c97f0a80 | -13.63046 | -47.89721 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f50afa16-ddae-3ba2-a0ee-7cd4d585dc3e | -10.67559 | -54.15368 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 1dbe44d1-de24-34e4-9e0c-4523539986b3 | -10.1022 | -48.86562 | 2026-09-14 04:34:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72e84f85-d266-3a22-9991-371254bd0c82 | -12.39796 | -44.41374 | 2026-09-14 04:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ffed24a1-0014-359a-aab3-bc68076bafb5 | -14.83577 | -48.15335 | 2026-09-14 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bab42e44-f180-303c-ae3a-4e8c06112434 | -10.11097 | -48.85822 | 2026-09-14 04:34:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4d2350b2-c3dd-3194-b733-3239f860afa4 | -13.29846 | -51.31022 | 2026-09-14 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 293e6421-30a1-3fa1-9373-dd13efb77540 | -10.68016 | -54.17332 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8a993f45-8a77-3ee1-8c1c-7083ad65d340 | -10.54893 | -51.30058 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c8552a5b-5179-3e0e-abf2-aac29f79a039 | -12.3981 | -46.49047 | 2026-09-14 04:34:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a1bf8e9b-cf33-365a-a495-c2041f970ea0 | -13.29366 | -51.3139 | 2026-09-14 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| baa2525c-6280-3b90-a34b-5026d8f4b95e | -11.51444 | -50.25463 | 2026-09-14 04:34:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3b38a108-454f-3ffc-ab1f-8ef6653ddc70 | -10.58131 | -51.33734 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4524c71d-d76d-3515-8409-0455bc61f916 | -14.82681 | -48.1443 | 2026-09-14 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2859134c-2e9a-33f3-b64f-d735f78ffe3d | -10.43046 | -48.64649 | 2026-09-14 04:34:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| b78685ad-b561-346b-9e78-898940a37921 | -13.35823 | -51.72062 | 2026-09-14 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d00d2b12-7e71-3a37-a517-1dee527a52e7 | -13.28966 | -51.31315 | 2026-09-14 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5630bc01-64bb-3d2e-bbf4-3c488fb9e166 | -10.57713 | -51.3365 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d6a85f3d-c652-3992-9fb5-d8e7c265d06b | -13.62242 | -47.90357 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a46d274d-9c59-3c23-8040-fdd207c19cdb | -10.23697 | -50.90752 | 2026-09-14 04:34:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 033ed0df-cd86-3944-96a4-7b29298a9876 | -13.56332 | -51.46001 | 2026-09-14 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ce854c7-407c-39b7-8d70-a63ab5da79e8 | -10.98 | -51.43285 | 2026-09-14 04:34:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dfe2349c-2dc9-311c-8447-41ef3ca53595 | -14.18428 | -47.3962 | 2026-09-14 04:34:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 3dde31cc-57f6-313e-9ed7-47827bf4c8b2 | -13.30167 | -51.31538 | 2026-09-14 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c19316a2-0f5d-3345-9c73-54e84a6d75cf | -10.94728 | -48.36336 | 2026-09-14 04:34:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3fb9e713-db1a-39e3-80da-3818e32ec3f8 | -11.37334 | -43.95486 | 2026-09-14 04:34:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6dba10a0-8d21-3f39-97f4-71ea05ffcfc0 | -9.69379 | -54.34047 | 2026-09-14 04:34:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae9d84ef-629d-387c-be5e-693f63a9354e | -10.7682 | -48.97186 | 2026-09-14 04:34:00 | NPP-375D | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9cf5692b-f544-3c69-8e11-50db860cef9b | -10.68186 | -54.16437 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9d9943d3-6ab2-3e30-94eb-b1f23e66f7dc | -15.81688 | -42.37465 | 2026-09-14 04:34:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78caabf7-14d3-3005-a600-6baa5f15aa48 | -11.19522 | -46.30709 | 2026-09-14 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a918bf21-c592-38b3-9dba-c73ff1edd1be | -11.23409 | -43.44671 | 2026-09-14 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a9bf14c6-a642-3987-8eb4-b7e36eb38822 | -14.18822 | -47.39312 | 2026-09-14 04:34:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c858070f-8ceb-3f93-955c-dd0459f99c29 | -13.59216 | -47.89448 | 2026-09-14 04:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1dfa144b-7b4b-3db7-ae83-a11b7b62bcdf | -10.67623 | -54.16642 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| cf8582ca-f509-3f68-94ee-29130a9be63a | -14.16896 | -47.42693 | 2026-09-14 04:34:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 398d0a50-0ac0-3dfb-9a69-4f5e21749b61 | -13.77875 | -48.79643 | 2026-09-14 04:34:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1200f2d5-cb76-3cf6-9cf2-403d8e2410b0 | -13.51509 | -44.16895 | 2026-09-14 04:34:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 144bca67-ee91-34b0-aafc-55d80aae91ac | -10.0722 | -48.7798 | 2026-09-14 04:34:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 243887c6-c61e-33cb-9b3a-ea4c83803646 | -14.82002 | -48.14317 | 2026-09-14 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e721aba0-f243-3099-a203-b92d8378db95 | -14.83298 | -48.14911 | 2026-09-14 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76a85346-068d-3587-854e-5837c9f8e653 | -10.67956 | -54.16055 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d05872d7-5f39-3e3b-aca5-367f0c1135eb | -14.8114 | -48.15316 | 2026-09-14 04:34:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13f6e530-615a-38cd-a1ec-bdd2b3f60875 | -10.56451 | -51.33449 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dfab7d14-fd58-3417-b06b-e12991515bf9 | -11.17861 | -42.80032 | 2026-09-14 04:34:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ee41f28f-a58a-31a0-a939-8644ff376d61 | -10.54697 | -51.31192 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3912e31d-24d5-325b-ba4a-de7be059f2c3 | -10.54764 | -51.30806 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0aa1e72f-67eb-36fa-9197-330a197565dd | -9.9856 | -50.27605 | 2026-09-14 04:34:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f37e129c-7345-3383-a011-5fe0cd92079c | -14.87021 | -49.94581 | 2026-09-14 04:34:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9b1c9a7-2d0c-3e3a-a6f4-ef1f4014f2b9 | -12.39512 | -44.40947 | 2026-09-14 04:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 62bdfc51-5366-33b4-a5e0-45b2d49ecaac | -10.66606 | -54.14865 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 2210fdce-6e99-3ccc-9805-e4c58a101e60 | -15.55064 | -48.7925 | 2026-09-14 04:34:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3be33791-1042-3df0-8f33-f819e2c9b0c0 | -11.2335 | -43.45063 | 2026-09-14 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab04638e-1f6c-3bf7-9647-296c0dfbd770 | -11.59378 | -46.77726 | 2026-09-14 04:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 73e5b5ff-c5eb-3959-ae2a-6ac420030a97 | -11.21487 | -46.4191 | 2026-09-14 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e980b7d8-9f20-39aa-8329-fde3753ad1e1 | -10.6819 | -54.17641 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c3e51a52-7bcd-3388-8b5a-f475a174a829 | -10.95065 | -48.36349 | 2026-09-14 04:34:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8741e13-d311-3682-a6af-624a0bcade44 | -11.05597 | -49.57345 | 2026-09-14 04:34:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cd29ce6c-7606-3519-b5d4-ae09295196c6 | -10.48609 | -51.24111 | 2026-09-14 04:34:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b716c0cd-ef75-3c87-92ae-1602f8d44c73 | -10.41186 | -57.22893 | 2026-09-14 04:34:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5acfb8f6-9eb8-30dc-947b-53e6b631231d | -11.193 | -42.80254 | 2026-09-14 04:34:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3f342278-517b-3e5d-af72-3efbf3e82fd2 | -15.55409 | -48.79299 | 2026-09-14 04:34:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 93febaba-6273-3d5e-812e-03460f9b43cb | -9.71442 | -50.85061 | 2026-09-14 04:34:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74cc435b-63bf-352a-b661-91621b54ec7e | -11.34631 | -46.77694 | 2026-09-14 04:34:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63dac4c1-e5fa-3803-99bd-a5e1f7db0c1a | -10.80639 | -58.5829 | 2026-09-14 04:34:00 | NPP-375D | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a8ba95e-ef44-3f6b-a6f2-383a1e6630de | -14.18763 | -47.39676 | 2026-09-14 04:34:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8b589134-a2d6-3856-aabc-79d92a96de84 | -10.54787 | -51.30682 | 2026-09-14 04:34:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf7fdbd6-1828-3795-b925-bb93d599f013 | -13.32477 | -51.71801 | 2026-09-14 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9f21ce5-68a2-389b-b25d-45122516041e | -16.23273 | -52.64968 | 2026-09-14 04:34:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 022e020f-029b-33f0-b637-eed7c1a690f1 | -11.23759 | -43.44726 | 2026-09-14 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 46fbb682-397e-3cfe-983c-618c6c14b891 | -10.67849 | -54.15458 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 6d58488e-ab6d-3c48-badf-285acb7ed798 | -11.23118 | -43.44225 | 2026-09-14 04:34:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5e56cd5d-2b43-37d3-b18c-6167e0bec806 | -10.42974 | -48.65082 | 2026-09-14 04:34:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 8a7dcf05-9040-3837-8055-b5683dbb6480 | -10.65654 | -54.1436 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6f3bff4c-4407-324e-a889-024343820a7b | -10.68408 | -54.16443 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 64ef558c-51bc-3304-975a-a39e2f7c0604 | -11.2143 | -46.42263 | 2026-09-14 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 37001108-f9d9-3c81-8064-244466d9c206 | -10.6857 | -54.15552 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 7a2b3f78-51f1-3215-affe-ff713613af84 | -10.67451 | -54.15958 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 0d643d2b-639c-3007-ac6e-076dd435b504 | -10.9793 | -51.43673 | 2026-09-14 04:34:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 74d4abe7-1dcd-3ce5-a604-81aef736df74 | -17.98253 | -44.33979 | 2026-09-14 04:34:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e013e8c8-5fa3-361d-a13e-32f2ed550e94 | -10.67829 | -54.13892 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 358b3e37-fb60-3b07-b38d-7d5216595a6a | -10.68355 | -54.15548 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8faacf7e-151f-38ed-ab54-dcff9335a97e | -13.5593 | -51.45926 | 2026-09-14 04:34:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b3d3506c-2b49-3564-8b12-353ecf6ce71b | -9.68469 | -54.84032 | 2026-09-14 04:34:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 304eea30-f347-3b26-9027-ca70ca5edcd4 | -10.68861 | -54.15639 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e9c32991-6587-360a-aca3-cd375a9f810e | -10.68072 | -54.14286 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e68849b1-cbc5-3394-8991-5df84e490cb9 | -11.17828 | -46.39127 | 2026-09-14 04:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README29.md)
