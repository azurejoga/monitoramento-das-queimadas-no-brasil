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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f23835da-a1db-370c-89f4-604372c9c195 | -14.16997 | -45.45973 | 2025-08-03 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ce040099-762d-3f69-a279-c80b9809b5da | -15.55026 | -54.27605 | 2025-08-03 04:55:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 20f3f538-ef19-334f-801d-d7766d19207c | -14.17036 | -45.45652 | 2025-08-03 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d41e110-177d-31d5-a50f-a8c9c2462547 | -13.07685 | -47.39489 | 2025-08-03 04:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f4187190-92c6-37a5-b402-ede22f0ad79e | -18.83774 | -46.45274 | 2025-08-03 04:55:00 | NPP-375D | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 141983b2-410c-39d6-b815-da94d02709ef | -13.07638 | -47.4329 | 2025-08-03 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 11f4e8ae-83ed-3bad-91b2-7b663c2bd8d5 | -17.21202 | -44.85262 | 2025-08-03 04:55:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70e696d9-656c-32dc-af9a-71929ff656bd | -19.61916 | -43.17383 | 2025-08-03 04:55:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1887a1eb-1e50-3688-beaa-82175e4ff091 | -19.73724 | -45.26178 | 2025-08-03 04:55:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f745142c-ef07-3637-b81c-09922cd4a557 | -14.37611 | -50.32352 | 2025-08-03 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f56d2f9-f324-3fa4-8d75-35965797311a | -13.07303 | -47.42373 | 2025-08-03 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d1380d6-bb35-3d75-bb23-681b1e89d813 | -14.16267 | -45.43255 | 2025-08-03 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21c3fb46-56d5-353b-bb03-9130251ad0ba | -12.75133 | -56.57634 | 2025-08-03 04:55:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8f4fe494-4656-39fc-b9ae-49ffc3ebc873 | -13.69235 | -41.37208 | 2025-08-03 04:55:00 | NPP-375D | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1552f600-671a-3349-a288-55cb190e7157 | -14.00214 | -53.92796 | 2025-08-03 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e161be7c-30c2-3935-aae4-0953df5be2f5 | -20.07825 | -43.99702 | 2025-08-03 04:55:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8b574b18-575a-3152-8a2d-8efec8666c7e | -14.14218 | -45.42678 | 2025-08-03 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53bfe1af-6892-3a17-801f-8ff4480f91ec | -14.15745 | -45.43192 | 2025-08-03 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9c7a3ff-20e4-320d-abeb-b6ae5cea36a3 | -18.54297 | -48.90384 | 2025-08-03 04:55:00 | NPP-375D | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5e0be33-ddec-3206-ba89-7a31ec1f7f78 | -13.06688 | -47.43578 | 2025-08-03 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1bf655e6-3539-30df-a4c2-f0ff53ac1d4c | -13.08084 | -47.43371 | 2025-08-03 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 475925f5-72a1-36f9-97b7-d72c42a5b2d2 | -18.61829 | -49.19246 | 2025-08-03 04:55:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 873b9b6f-e4c1-3eed-a3be-b31fb3dd88f0 | -14.10453 | -54.0071 | 2025-08-03 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 78c51064-3524-3796-8bb6-5914df0ead43 | -15.54694 | -54.2755 | 2025-08-03 04:55:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 455db9b2-b01c-3b3f-8cdd-8da6229f03c0 | -14.17153 | -45.4468 | 2025-08-03 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| efb0d1e8-bbaf-3cfd-a069-fda95382922b | -14.17075 | -45.45329 | 2025-08-03 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2155f97-797b-3e01-8b0a-541bedc983b1 | -14.16228 | -45.43578 | 2025-08-03 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b63d8bc-1b8b-37dd-ad6f-d6d9f423fff2 | -14.17596 | -45.45391 | 2025-08-03 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b2dba7be-1ccd-3d68-871f-3dea69700c51 | -13.06747 | -47.4313 | 2025-08-03 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a88c3229-07f7-3cce-a327-e9f4d3558026 | -14.16189 | -45.43902 | 2025-08-03 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3914034-d345-398f-87ad-77977564eeeb | -15.16359 | -47.03189 | 2025-08-03 04:55:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 537a9830-857e-374b-9537-6b436e30b318 | -20.02121 | -46.43275 | 2025-08-03 04:55:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f17f1b15-2479-3a12-a921-4feec488380e | -11.74588 | -54.72423 | 2025-08-03 04:55:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58a55636-a266-33b8-993b-a5a753dacf40 | -14.83418 | -48.38522 | 2025-08-03 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9a0f6809-68cc-37ac-898c-b42155c04f78 | -18.23114 | -44.69866 | 2025-08-03 04:55:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b1dbd9e-3fce-3fa8-9fd7-99bb9afd26b4 | -14.09242 | -52.19602 | 2025-08-03 04:55:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2c3b67d1-44fe-376f-9929-0788f148dde0 | -13.0624 | -47.43516 | 2025-08-03 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4822060-1462-3233-a9d1-8ca0ef050a65 | -19.15263 | -49.12545 | 2025-08-03 04:55:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 88ebdd67-5cd6-3692-815b-5bf9314df55c | -18.57679 | -51.16442 | 2025-08-03 04:55:00 | NPP-375D | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 0a7bb7e3-d4f9-343c-88a3-6cbf7b093415 | -12.68861 | -48.09068 | 2025-08-03 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 41ab2249-6614-33e5-8328-3b8e3ba7b908 | -13.06629 | -47.44027 | 2025-08-03 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 56ac543a-a409-3c40-a0ea-e0fee0036980 | -12.76255 | -56.57419 | 2025-08-03 04:55:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e558d6e-435f-3352-abee-1765a4aa21e1 | -18.5806 | -51.16499 | 2025-08-03 04:55:00 | NPP-375D | CAÇU | GOIÁS | Brasil | 5204300 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c0383557-2756-368c-baba-450fd4988292 | -13.07135 | -47.43642 | 2025-08-03 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8004595f-3866-35ff-b182-6616532adad6 | -17.8745 | -51.68892 | 2025-08-03 04:55:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b282af33-de0c-3df8-94e9-5fa0311ce56c | -14.17114 | -45.45005 | 2025-08-03 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1b24e014-7145-3e3f-b745-5a85f4c3b314 | -14.16749 | -45.43645 | 2025-08-03 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31b3f7be-990e-36a2-9fdb-7d832f3466d7 | -19.7402 | -45.2602 | 2025-08-03 04:55:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 359be5c9-9bbd-3d8f-af1e-f3d93834f1c1 | -12.50301 | -49.0125 | 2025-08-03 04:55:00 | NPP-375D | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 74558a0c-34af-3345-ae76-b620aa09ecc0 | -14.14142 | -45.43321 | 2025-08-03 04:55:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c99ed5fc-9387-38d4-8d77-71474d253d19 | -13.08139 | -47.39514 | 2025-08-03 04:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5f7b510d-40ae-3534-8c27-b3523189a8d1 | -18.98295 | -48.41416 | 2025-08-03 04:55:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1c5b710-93b6-3617-8028-e989361a2a45 | -12.68333 | -48.0975 | 2025-08-03 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4953e96b-5212-3e2f-aee0-cacb71329d67 | -16.72335 | -49.42064 | 2025-08-03 04:55:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a9f500f8-7841-3090-9d31-157efdd1703e | -15.54417 | -54.27135 | 2025-08-03 04:55:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a50251f3-49ac-3d08-a7aa-e3b92d19c104 | -22.72195 | -44.73755 | 2025-08-03 04:57:00 | NPP-375D | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 37685d68-f9e2-3b4f-b493-be43cc5d4d76 | -23.19199 | -46.31138 | 2025-08-03 04:57:00 | NPP-375D | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 14ad3c68-4bdb-3bdd-ba35-684bbf453217 | -22.2206 | -55.15984 | 2025-08-03 04:57:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0afc7463-7c35-3c5c-9729-f98bb23c6e11 | -26.73175 | -51.58196 | 2025-08-03 04:57:00 | NPP-375D | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 188e9df8-79e8-3f9f-a60e-97604b38f90c | -26.19484 | -53.01007 | 2025-08-03 04:57:00 | NPP-375D | RENASCENÇA | PARANÁ | Brasil | 4121604 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 293f43d3-2d34-3680-a634-9ab670415dfb | -23.25013 | -53.87364 | 2025-08-03 04:57:00 | NPP-375D | ITAQUIRAÍ | MATO GROSSO DO SUL | Brasil | 5004601 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 004ad61a-555f-3696-936e-093cf743e811 | -20.9465 | -45.93632 | 2025-08-03 04:57:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aa140c1b-f3c9-36cb-9663-8ad938eee121 | -22.66592 | -53.37637 | 2025-08-03 04:57:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0b717567-4071-33f1-8acb-564e59a31dfb | -20.86381 | -54.95351 | 2025-08-03 04:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b07fd085-c324-3a44-9480-6f0efee48a0f | -24.31343 | -51.97446 | 2025-08-03 04:57:00 | NPP-375D | NOVA TEBAS | PARANÁ | Brasil | 4117271 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 33168377-e006-3092-bc5e-1e585fba7818 | -26.73726 | -51.57036 | 2025-08-03 04:57:00 | NPP-375D | ÁGUA DOCE | SANTA CATARINA | Brasil | 4200408 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8408552a-ae1b-3dcc-9c93-ad3c2bd29e64 | -21.4515 | -55.1049 | 2025-08-03 04:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 07583ca2-b679-3719-8452-1940a7d99c4f | -21.31013 | -48.56672 | 2025-08-03 04:57:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a27a0d7-15ff-36c0-baf9-b71423def2d2 | -24.31734 | -51.97506 | 2025-08-03 04:57:00 | NPP-375D | NOVA TEBAS | PARANÁ | Brasil | 4117271 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 221280d5-784e-31b1-bc40-079125d01b75 | -27.16182 | -51.21041 | 2025-08-03 04:57:00 | NPP-375D | IBIAM | SANTA CATARINA | Brasil | 4206751 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 2776133b-bde4-3531-a41d-1572083dc96b | -24.23443 | -48.46701 | 2025-08-03 04:57:00 | NPP-375D | GUAPIARA | SÃO PAULO | Brasil | 3517604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 61e723f2-6ec4-3fa4-ba2b-4160c1fdb8c0 | -20.85988 | -54.95667 | 2025-08-03 04:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2b8be342-402d-353d-a74e-d08e73c53e8f | -22.72736 | -44.74607 | 2025-08-03 04:57:00 | NPP-375D | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 1eb3a4be-e130-3008-a471-6cecd3889880 | -23.19164 | -46.31509 | 2025-08-03 04:57:00 | NPP-375D | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2f5966cb-0200-3a7e-9021-ac11d01cb43f | -24.08655 | -52.35838 | 2025-08-03 04:57:00 | NPP-375D | CAMPO MOURÃO | PARANÁ | Brasil | 4104303 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5a8cf8b4-21a8-3b96-a093-730dab6fd2f9 | -22.22233 | -55.14839 | 2025-08-03 04:57:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 951aae55-a18f-349b-b6ec-d6732d948544 | -20.94615 | -45.93735 | 2025-08-03 04:57:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ac5b981-c42b-318e-a138-bd96b9407344 | -21.44815 | -55.10432 | 2025-08-03 04:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 214e6548-2f7f-3600-adf0-499db6ce9414 | -20.9516 | -45.9385 | 2025-08-03 04:57:00 | NPP-375D | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 495ef3af-24bf-333f-9a74-2e781fe77b40 | -24.31686 | -51.97721 | 2025-08-03 04:57:00 | NPP-375D | NOVA TEBAS | PARANÁ | Brasil | 4117271 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ce509b01-4fdf-3421-b05f-16012692a90d | -23.98566 | -51.31062 | 2025-08-03 04:57:00 | NPP-375D | FAXINAL | PARANÁ | Brasil | 4107603 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a1b90f0c-9dd3-362a-b318-df8eb983f6dc | -22.66652 | -53.37202 | 2025-08-03 04:57:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cac43983-854e-3055-ae70-dd79c24256d7 | -24.31295 | -51.97661 | 2025-08-03 04:57:00 | NPP-375D | NOVA TEBAS | PARANÁ | Brasil | 4117271 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| de8b62c2-5803-3bfa-9a62-0ca591882f50 | -20.86046 | -54.95289 | 2025-08-03 04:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9abe498f-c752-33a1-8987-a69535d069d6 | -20.85654 | -54.95604 | 2025-08-03 04:57:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3f9c4dc9-1f98-38e9-8f34-7c15c23292f2 | -22.66949 | -53.37695 | 2025-08-03 04:57:00 | NPP-375D | TAQUARUSSU | MATO GROSSO DO SUL | Brasil | 5007976 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9956aa25-83ea-3c8f-961f-56e96b000d8d | -24.21962 | -51.8617 | 2025-08-03 04:57:00 | NPP-375D | JARDIM ALEGRE | PARANÁ | Brasil | 4112504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 877af755-ae6b-321c-9589-eb2b7121e070 | -22.22118 | -55.15602 | 2025-08-03 04:57:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| afb5f80c-008d-391c-8a69-7f035f80aa12 | -24.22112 | -51.86077 | 2025-08-03 04:57:00 | NPP-375D | JARDIM ALEGRE | PARANÁ | Brasil | 4112504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| b7a5b3db-8757-3428-9d9c-1994ded61936 | -22.7277 | -44.74189 | 2025-08-03 04:57:00 | NPP-375D | AREIAS | SÃO PAULO | Brasil | 3503505 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 898bdc07-616c-3960-805e-551461cf61eb | -22.22175 | -55.15221 | 2025-08-03 04:57:00 | NPP-375D | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 20ad4ada-8f3d-3f8c-8dc2-a73d29eae896 | -8.0132 | -43.1278 | 2025-08-03 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| 8df409f2-234f-3933-948c-3b8851264fde | -7.9937 | -43.1769 | 2025-08-03 05:00:00 | GOES-19 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 124.0 |
| 7352df11-3eff-3d5a-aa8b-a4997f43c047 | -7.994 | -43.1534 | 2025-08-03 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 106.4 |
| bedadd10-684e-3051-8dd2-65352c8b2790 | -6.6329 | -59.9649 | 2025-08-03 05:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 947227c1-ae31-3294-9a70-e6825a83e1a3 | -8.0129 | -43.1513 | 2025-08-03 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 329.1 |
| bb5646e3-ae5a-3ab0-8861-7c591f0bb8c6 | -4.5497 | -44.2047 | 2025-08-03 05:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| aee35786-d9fa-3daf-9d81-bb6cb1f4b5f8 | -8.0126 | -43.1749 | 2025-08-03 05:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 210.7 |
| a9f5d0c4-8994-3ea9-8e9e-95ea1e6cb0b0 | -6.6329 | -59.9649 | 2025-08-03 05:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 3fb0e8b1-65a7-346b-8eed-e7ea7b9adcb3 | -8.0132 | -43.1278 | 2025-08-03 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.3 |


[Clique aqui para ver as próximas entradas](README28.md)
