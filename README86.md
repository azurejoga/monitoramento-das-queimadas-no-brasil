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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 460b8eb4-ebcd-3e1c-a882-11a9a413ba33 | -15.26603 | -48.77238 | 2025-09-29 12:19:00 | TERRA_M-T | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 5d2fb8e8-86b8-3155-bb29-6361bc6c3e4d | -19.87895 | -48.31301 | 2025-09-29 12:19:00 | TERRA_M-T | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 13.5 |
| f5b70919-d5d4-3761-aaa7-c189ff262130 | -19.30246 | -46.24806 | 2025-09-29 12:19:00 | TERRA_M-T | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 28.9 |
| e0873c7c-686f-3259-a08e-705645b743c2 | -13.62409 | -47.35191 | 2025-09-29 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 38689a55-a269-3f72-83ed-39f4e1a7e332 | -11.9436 | -47.89172 | 2025-09-29 12:19:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 109c756c-4107-3a57-86e0-c3e72ae7d910 | -11.35752 | -45.07381 | 2025-09-29 12:19:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 61689f85-5011-33e5-b02a-4db536c70378 | -15.04848 | -46.96368 | 2025-09-29 12:19:00 | TERRA_M-T | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 629fe992-0dbb-361a-b186-1cd6562c5bf5 | -9.79572 | -46.9323 | 2025-09-29 12:19:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 7e5b8090-4a31-375f-acdd-987bac34bd3b | -13.61561 | -48.06781 | 2025-09-29 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 2ee2cfa5-029a-3274-ba95-8a59bd7500bb | -10.4085 | -48.11853 | 2025-09-29 12:19:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ca28d3b0-bbc1-3cc0-9c60-a655d55ebec2 | -14.52702 | -48.39309 | 2025-09-29 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 378f7eb5-8aa9-3567-80f7-865c04b7f145 | -13.73164 | -48.66987 | 2025-09-29 12:19:00 | TERRA_M-T | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 278bf068-058c-356d-aabc-7fef7a168a32 | -10.33143 | -48.20167 | 2025-09-29 12:19:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 054537dc-6ae6-3c9c-bf7d-e8e7b4a8a1af | -12.80459 | -47.74663 | 2025-09-29 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 56454dd9-c2bc-36e3-bb69-cba10a3fde71 | -19.87761 | -48.32285 | 2025-09-29 12:19:00 | TERRA_M-T | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 47.0 |
| e84189f5-9d34-380f-ba3e-ba257b2d2925 | -13.7973 | -47.95864 | 2025-09-29 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3eaf28a9-ddf8-39a3-86bb-fae21bba06c7 | -11.84597 | -51.78342 | 2025-09-29 12:19:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 34.3 |
| a6707ca8-cab5-3104-b2f2-bf5cdba5d0c6 | -9.78163 | -46.17811 | 2025-09-29 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 81b03d7e-b0cc-3f81-aaaa-6c3eaf83eb87 | -20.05587 | -41.3454 | 2025-09-29 12:19:00 | TERRA_M-T | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.5 |
| c54914e3-4f8c-3776-a48e-6810b294a7b1 | -10.80875 | -47.96393 | 2025-09-29 12:19:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 11159835-db3d-34e8-9ab8-a008e2c7507d | -20.35939 | -44.86952 | 2025-09-29 12:19:00 | TERRA_M-T | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 215.9 |
| b90258e6-c7d2-3378-9a4c-5c0a6d1c8617 | -13.73033 | -48.67891 | 2025-09-29 12:19:00 | TERRA_M-T | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 971be1da-9235-3bf0-8957-97735977e983 | -15.29618 | -49.51181 | 2025-09-29 12:19:00 | TERRA_M-T | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 1385530a-fb43-3620-a283-69ac0a8472cf | -9.51209 | -47.69042 | 2025-09-29 12:19:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 24.2 |
| 81bf18fd-a8b7-34b7-91ff-a07f73649ea9 | -10.14096 | -45.30582 | 2025-09-29 12:19:00 | TERRA_M-T | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 69a821c8-56f6-3d10-b569-6faed8b9175c | -11.69362 | -44.31018 | 2025-09-29 12:19:00 | TERRA_M-T | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 53c407ed-0fe7-3545-b7f2-5e0dedb95e6f | -9.77899 | -46.1969 | 2025-09-29 12:19:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 31.8 |
| b5b4d7ae-5f01-36cb-9124-9aaef5815139 | -13.1864 | -50.73376 | 2025-09-29 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 331b1b79-903b-33d5-8c57-3584aba101ae | -17.43123 | -53.05162 | 2025-09-29 12:19:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 196fbba1-5e31-3e0b-b4bd-1de1ca0eae5a | -11.26842 | -48.36109 | 2025-09-29 12:19:00 | TERRA_M-T | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 602cca94-3834-37e1-beb3-2b9cd8da2c32 | -10.82651 | -46.67381 | 2025-09-29 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 5fa34dc4-f9b8-3dca-90aa-4fa4f251a2b2 | -9.75646 | -47.78942 | 2025-09-29 12:19:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c1f53828-5abe-309d-b146-c32a1ebd3a6b | -14.61234 | -41.27726 | 2025-09-29 12:19:00 | TERRA_M-T | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 45.2 |
| 5fc8effe-f026-35e4-86fa-4907844d79ab | -11.55875 | -46.8418 | 2025-09-29 12:19:00 | TERRA_M-T | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 50.4 |
| c91ac4d4-d809-382f-ba99-647fd5c9ea15 | -11.26923 | -49.60411 | 2025-09-29 12:19:00 | TERRA_M-T | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8f5ba299-a42c-3b59-afc9-c462578b2e75 | -12.69964 | -46.91422 | 2025-09-29 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.0 |
| e3dde9d7-6126-3535-937c-ee4c899e3a62 | -12.85921 | -46.95857 | 2025-09-29 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 55.6 |
| a9e9936a-ca5c-3f90-93d4-bbad82d060e1 | -10.42161 | -46.1463 | 2025-09-29 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| cd286361-d576-36de-8526-3725000c759b | -14.70597 | -45.20923 | 2025-09-29 12:19:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 03c12e27-e214-31ca-a8dd-fde9c6a61fda | -15.97035 | -42.53864 | 2025-09-29 12:19:00 | TERRA_M-T | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 9bc0a4eb-0816-358f-9d22-a17d2c854ad8 | -12.94098 | -46.7639 | 2025-09-29 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 824cb926-31d9-3145-9497-5fd7c45b1e37 | -17.99995 | -46.69848 | 2025-09-29 12:19:00 | TERRA_M-T | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| db372d54-a274-3bf7-9a2a-ac69c2e43b5d | -13.63817 | -47.31647 | 2025-09-29 12:19:00 | TERRA_M-T | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 966b79b4-05f5-3081-b2f8-4994c02de46d | -20.11304 | -44.23329 | 2025-09-29 12:19:00 | TERRA_M-T | SÃO JOAQUIM DE BICAS | MINAS GERAIS | Brasil | 3162922 | 31 | 33 | nan | nan | nan | Mata Atlântica | 44.4 |
| bb11b009-1198-3615-a1af-f84e720c5b5b | -13.81006 | -47.9323 | 2025-09-29 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a4174b08-96bd-3175-97e4-5284ce39e822 | -15.51459 | -47.92521 | 2025-09-29 12:19:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 27e50259-cf78-34e3-a8c5-c5f8d08c6a0d | -15.29503 | -46.42059 | 2025-09-29 12:19:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b719cbc9-dfa7-3626-bfc0-3137f62acd07 | -19.86851 | -48.32156 | 2025-09-29 12:19:00 | TERRA_M-T | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| bbe43ffa-0581-341b-a6d2-3177fd355dad | -15.51328 | -47.93451 | 2025-09-29 12:19:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 15f128b1-f9f6-3771-8e7d-266e0f35f023 | -13.80503 | -47.90377 | 2025-09-29 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 0275fa1d-8d0e-3f4a-8c87-9fa1570a9437 | -13.17692 | -50.73227 | 2025-09-29 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 350.9 |
| 5e97e453-c328-3e77-81eb-7995fa4842b3 | -12.97618 | -46.24335 | 2025-09-29 12:19:00 | TERRA_M-T | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 18.8 |
| ffbcf0e7-3010-3492-bcb0-eb974591bc48 | -12.00798 | -47.44084 | 2025-09-29 12:19:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 333d2c4b-5415-3cd1-90be-9380c830a062 | -16.10039 | -46.026 | 2025-09-29 12:19:00 | TERRA_M-T | RIACHINHO | MINAS GERAIS | Brasil | 3154457 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| eb195364-026b-3c7f-b4ce-1feaad4f390f | -14.89199 | -51.04787 | 2025-09-29 12:19:00 | TERRA_M-T | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 2684812a-c946-398f-b6ea-a42821aff5d5 | -16.5317 | -46.9425 | 2025-09-29 12:19:00 | TERRA_M-T | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1e7da504-8ca7-3ee9-8714-48b54109536f | -11.662 | -45.32725 | 2025-09-29 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| ec2fb9ba-71fb-3ecb-9701-cc7006049508 | -12.89565 | -47.0946 | 2025-09-29 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6fcf145d-b3f7-32f6-9079-cc4ed1ee4562 | -15.04714 | -46.9736 | 2025-09-29 12:19:00 | TERRA_M-T | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 52.8 |
| cd2e9cdd-c255-3ae5-a494-c9473a548534 | -12.43315 | -44.10742 | 2025-09-29 12:19:00 | TERRA_M-T | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 0a78d8fa-561a-38bc-9fb3-efeb8cfd88a1 | -9.80676 | -47.8786 | 2025-09-29 12:19:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 43decd8c-7d5b-3d87-a76c-58a6c1820e57 | -13.74214 | -47.88873 | 2025-09-29 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 877b5156-457e-346d-b799-ac0a6a8cb026 | -11.41078 | -44.89888 | 2025-09-29 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 63ab40f1-cdd0-3feb-920c-73d143478662 | -11.42062 | -44.90039 | 2025-09-29 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 3fc936ae-1f33-3634-879a-e6d1a3635be3 | -10.81622 | -46.6818 | 2025-09-29 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 5c7435e6-2ce7-3253-ac5e-9972e26c9822 | -18.47232 | -44.01165 | 2025-09-29 12:19:00 | TERRA_M-T | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 46.5 |
| b0fd3457-6f15-3f3f-addf-8917434a7d1f | -17.71638 | -46.68559 | 2025-09-29 12:19:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| f21ffcb2-e3f8-3f8d-8b9f-0d753295be5d | -18.00292 | -46.70491 | 2025-09-29 12:19:00 | TERRA_M-T | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 66daf17e-12f9-3962-ab42-8c6a1d12adda | -9.99558 | -45.41612 | 2025-09-29 12:19:00 | TERRA_M-T | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 02341d6d-a9e8-32d9-af5c-21d13ddb11ca | -14.86906 | -47.20355 | 2025-09-29 12:19:00 | TERRA_M-T | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 68438170-7c6d-3c2e-9a54-778f1e6f0f87 | -13.57667 | -48.0746 | 2025-09-29 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 65ad05d4-aa22-3d4d-b961-776139aa0d98 | -12.96435 | -45.18824 | 2025-09-29 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| e6b58295-13ad-3dd8-aa69-e3f75c8d51e9 | -13.37971 | -48.1628 | 2025-09-29 12:19:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| df476f89-0a5d-3c0b-bb70-4337eee7496d | -12.3677 | -47.18115 | 2025-09-29 12:19:00 | TERRA_M-T | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c84883c2-0f4d-325a-a0ed-2714c9be9782 | -15.39217 | -41.1183 | 2025-09-29 12:19:00 | TERRA_M-T | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 60.7 |
| 4894b83d-1f37-31c1-bccf-e8771cdec54a | -15.46732 | -47.93731 | 2025-09-29 12:19:00 | TERRA_M-T | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 81396c36-82b0-3e5f-9888-e6fe554b4852 | -15.21954 | -50.09401 | 2025-09-29 12:19:00 | TERRA_M-T | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 4834d7a0-a373-38a3-b74a-59cd93f00de4 | -16.48631 | -46.03492 | 2025-09-29 12:19:00 | TERRA_M-T | BONFINÓPOLIS DE MINAS | MINAS GERAIS | Brasil | 3108206 | 31 | 33 | nan | nan | nan | Cerrado | 14.8 |
| e7250f08-1f09-334c-8efa-733b12479097 | -9.41406 | -54.67911 | 2025-09-29 12:19:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 40d4f78f-559e-3a2c-95a8-5c5ab55c0e86 | -10.62578 | -48.52765 | 2025-09-29 12:19:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 40.8 |
| 435b52b6-e311-3e17-9e7b-989039c41195 | -12.77238 | -46.85384 | 2025-09-29 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 7a58ad0f-5f35-3e57-bfb2-ac9530c5a05f | -9.7288 | -47.77944 | 2025-09-29 12:19:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 0ad5f378-3db4-348d-8f29-16c6038820a3 | -15.4335 | -48.24365 | 2025-09-29 12:19:00 | TERRA_M-T | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| d3771cb0-b016-3395-bb79-174eb425facc | -12.01268 | -46.62355 | 2025-09-29 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5f17056a-8bc3-3a71-af5e-bc2ccb8105e3 | -15.54153 | -41.47099 | 2025-09-29 12:19:00 | TERRA_M-T | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.7 |
| c5eeced9-d77f-36b7-a66e-3514ade5dba4 | -12.92389 | -47.15542 | 2025-09-29 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 77c52d78-0006-3f17-8024-c72a57458bd4 | -16.99646 | -47.25697 | 2025-09-29 12:19:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 21afda77-ace9-3463-9a94-444f1f596e6d | -10.91534 | -47.73893 | 2025-09-29 12:19:00 | TERRA_M-T | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| af6c025f-aec0-35e8-b8ec-91c018135d98 | -12.96632 | -45.18346 | 2025-09-29 12:19:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 494b3f34-2cfe-3ab4-bff3-5a3caad1e20e | -11.99067 | -46.58187 | 2025-09-29 12:19:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 83c9b503-c897-387f-abd1-f5c260e5a706 | -9.94085 | -48.79499 | 2025-09-29 12:19:00 | TERRA_M-T | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| b53d4a6f-1012-3c3a-89ef-22ecdb1a4959 | -13.35646 | -47.81783 | 2025-09-29 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 526ea528-0a1c-3079-907d-280db7fe91e9 | -15.8264 | -46.9298 | 2025-09-29 12:19:00 | TERRA_M-T | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f29f4522-df5f-3130-8d2b-832f1f6628bb | -11.80794 | -47.62709 | 2025-09-29 12:19:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 94e07aab-24a2-3c9a-8a3a-52c3315a92ee | -12.70094 | -46.9049 | 2025-09-29 12:19:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 0af6382e-8c8f-3987-93dc-b5636312f78b | -11.93036 | -48.0607 | 2025-09-29 12:19:00 | TERRA_M-T | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d6a3473a-4d3f-330f-9152-b50650d92cf3 | -13.56685 | -47.29937 | 2025-09-29 12:19:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| cbe03619-abdf-3ad0-ae5d-8bf7cda57aa3 | -12.2677 | -47.7613 | 2025-09-29 12:19:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| d0196fa0-9e6e-3eb4-8919-180286647870 | -13.36473 | -47.29672 | 2025-09-29 12:19:00 | TERRA_M-T | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 90170748-6db0-3ac4-ab2e-e756522ae461 | -14.86773 | -47.21319 | 2025-09-29 12:19:00 | TERRA_M-T | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |


[Clique aqui para ver as próximas entradas](README87.md)
