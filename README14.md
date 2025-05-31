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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f0d71592-ff17-3a5d-ae8d-0e45c7ef54d7 | -11.78798 | -44.28581 | 2025-05-31 04:53:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51daca5c-26f8-3f15-af26-9eec45b15448 | -12.50096 | -55.18866 | 2025-05-31 04:53:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e3b98cd5-060b-319b-a1fd-e7e66e3ad00b | -10.45912 | -47.94094 | 2025-05-31 04:53:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8c2e2bb7-1a76-3292-9a20-1732ec343167 | -9.99054 | -48.16053 | 2025-05-31 04:53:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc1915a2-12d7-3639-8895-2eddad109267 | -11.91082 | -54.42294 | 2025-05-31 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41edc7bb-f2b9-30d3-8c7c-d16735786182 | -11.91805 | -54.42049 | 2025-05-31 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9e53aa71-d7a2-3eaf-b7f8-b2adc069452f | -11.50835 | -48.23536 | 2025-05-31 04:53:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ddc649f-cf04-321d-bf2f-bb5d8169e0c4 | -12.37452 | -54.16462 | 2025-05-31 04:53:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0d358b6-7fac-3270-b3d7-a7615e7bc7e5 | -13.63054 | -47.44805 | 2025-05-31 04:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c39e6f37-c2ff-3b5a-8752-a7bd52545c87 | -9.96556 | -49.812 | 2025-05-31 04:53:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b10ebbc-e73c-367d-924f-e9078ded00a5 | -8.79101 | -47.9427 | 2025-05-31 04:53:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80298fc1-25f2-3259-8fa4-ae4957d0a6d4 | -12.02437 | -49.51708 | 2025-05-31 04:53:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 733a1051-faa0-3907-9ac8-53e072feea44 | -12.18091 | -54.24908 | 2025-05-31 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 082f7258-db7d-3032-928f-1b4d0b1de635 | -11.13704 | -53.94223 | 2025-05-31 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c7c68da5-8e93-32f4-ba22-5b4524087fee | -12.45764 | -54.91536 | 2025-05-31 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 37f1d0f0-c71d-3860-b239-54b85b28df69 | -12.0191 | -49.52647 | 2025-05-31 04:53:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 0229b22a-f5e6-3168-a558-5d00c35dd2e4 | -12.10221 | -54.66614 | 2025-05-31 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c05beead-f14e-34bc-9302-6ef1dd93e8e6 | -12.10338 | -54.66961 | 2025-05-31 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2d9954ef-333f-3981-9e23-7667767b744f | -10.45803 | -47.94879 | 2025-05-31 04:53:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 58345081-a02f-33b0-817c-e449f6609b8d | -9.80735 | -54.8895 | 2025-05-31 04:53:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c04cd93-01f7-3541-aeff-0b5b2fb93259 | -10.83829 | -54.01655 | 2025-05-31 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 828f3b7a-96b9-3645-927c-1866c72449e9 | -13.10441 | -45.27784 | 2025-05-31 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cbaec0bc-9902-3543-8140-6a02262de458 | -12.19531 | -54.26596 | 2025-05-31 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba0ebf7a-140c-3e76-a322-43b7efc8bb03 | -9.3164 | -49.48564 | 2025-05-31 04:53:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68b8a022-fbd7-3c17-b94a-5589673123d3 | -12.45429 | -54.91479 | 2025-05-31 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4a4785b4-6e3a-3e25-8951-e950672b1e05 | -12.03216 | -49.51821 | 2025-05-31 04:53:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3cc11ab9-b3ae-363d-adc8-44a063ec6128 | -9.26896 | -47.91395 | 2025-05-31 04:53:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58220ec3-9474-3f5e-bce8-048db4f48be9 | -8.66035 | -47.80971 | 2025-05-31 04:53:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9ccd394d-d176-392b-b0a8-f72a37d120c4 | -8.79076 | -48.80708 | 2025-05-31 04:53:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5db30dea-cb48-3507-8f7b-3fe48714ae71 | -9.52613 | -54.7693 | 2025-05-31 04:53:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9830923-065a-3aae-9a67-23330760f2db | -12.1073 | -54.66659 | 2025-05-31 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7066a81a-19b3-3ecd-929e-d6d2e3f9a2b7 | -10.29785 | -57.14006 | 2025-05-31 04:53:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4887066a-ca03-304d-8549-d5e7f1c54b48 | -11.91749 | -54.42403 | 2025-05-31 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 80aba001-946a-3839-9e73-a458e058f9b0 | -11.10676 | -50.8768 | 2025-05-31 04:53:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fe4805bf-3764-39de-8c39-9b971823eaa4 | -9.39921 | -48.42437 | 2025-05-31 04:53:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cea79ccc-8de6-34aa-8308-633f1d289e41 | -11.84023 | -51.26617 | 2025-05-31 04:53:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9d8c9e9f-6c0e-3db5-b75f-225d749d7b33 | -13.10157 | -52.2849 | 2025-05-31 04:53:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5bdefb5-0832-3930-a000-48c9b6a689cf | -11.91359 | -54.42703 | 2025-05-31 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ab3ad44-20de-3371-8b4d-93fc50132746 | -13.101 | -52.2887 | 2025-05-31 04:53:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee63516c-f601-38ae-a588-6547b36b7d7e | -11.89675 | -47.44799 | 2025-05-31 04:53:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad3d45ee-2227-3529-9e1a-1061b4df6e35 | -10.65053 | -49.43219 | 2025-05-31 04:53:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0953673e-6c2c-39c2-8e66-6344969e2b5a | -12.10164 | -54.66972 | 2025-05-31 04:53:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1bb02adc-98e0-3dd3-98b3-dc65682279a3 | -11.14314 | -53.94683 | 2025-05-31 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff1dcbea-c5dc-30a4-8cf7-1011675be626 | -9.60441 | -49.02315 | 2025-05-31 04:53:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b89d71fb-a8cd-3ff2-9e10-3edb0e6415e4 | -13.09257 | -45.28656 | 2025-05-31 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b384f4a3-ba70-3350-a557-2e348162622f | -10.33029 | -57.49337 | 2025-05-31 04:53:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71db6299-8900-36b3-9812-84a9a812a7c8 | -10.64217 | -49.43579 | 2025-05-31 04:53:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 85cf9e37-0e0b-374e-a9df-b49d86994d3b | -11.20822 | -47.82386 | 2025-05-31 04:53:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d9af3da0-8b10-3146-a94c-18e2fc9015b7 | -10.45858 | -47.94488 | 2025-05-31 04:53:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 174b104f-51fd-3a8e-afa8-7f8d810b2905 | -8.205 | -49.80174 | 2025-05-31 04:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d8a32912-cbd4-3890-a4d3-f48dbbd7c1a3 | -11.83316 | -51.26508 | 2025-05-31 04:53:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 21.2 |
| d45722f8-23ce-33de-bc2e-53f0e3b69dc6 | -10.99814 | -50.75576 | 2025-05-31 04:53:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a6773381-8905-306a-bf69-374d2c34d12c | -11.82489 | -51.272 | 2025-05-31 04:53:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| cac485c9-0f8c-3ad3-b2df-a4e094abacb7 | -11.1426 | -53.92869 | 2025-05-31 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2978a409-f41e-336e-9614-1b69543ba802 | -6.63504 | -55.00931 | 2025-05-31 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4e48fad-24ed-3a0f-9cf9-dbcaf725ca23 | -8.476 | -49.60348 | 2025-05-31 04:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f7fa2748-dfbd-3bae-9b2c-6540953c2e0e | -11.91054 | -54.82113 | 2025-05-31 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc8beeb2-8402-3b68-8d13-982543c10d0d | -12.03147 | -49.52318 | 2025-05-31 04:53:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3e2d582-914c-3b55-9d8a-574f69ed47ba | -13.63566 | -47.4443 | 2025-05-31 04:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05dd4ae1-ec70-3bc8-81d0-07fb8a27a3cb | -11.70555 | -54.55698 | 2025-05-31 04:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fce20072-9840-392f-82d9-2d674ba10818 | -9.52672 | -54.76568 | 2025-05-31 04:53:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88ab0fcd-385b-36a5-afcc-a266191bfa43 | -11.07667 | -55.05516 | 2025-05-31 04:53:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a57a109d-b0fb-3594-9b77-4676683a8737 | -11.13981 | -53.9463 | 2025-05-31 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 674fdb7b-bdd1-3e48-b0d5-5dde514f8785 | -11.83903 | -51.27423 | 2025-05-31 04:53:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| d85a9f97-4037-313e-8a30-3a4dbb1a07e9 | -10.46333 | -47.94158 | 2025-05-31 04:53:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b85dd137-8931-374e-b02c-af3caeb4f6ba | -12.37119 | -54.16407 | 2025-05-31 04:53:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 01b8b421-0d4e-38cc-a75e-9809350e1687 | -11.91112 | -54.81755 | 2025-05-31 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad7e2879-4524-3dcc-bad8-3c5c123aaf05 | -9.56088 | -55.0077 | 2025-05-31 04:53:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 50099b5f-8548-3571-8605-0eeb1d0a69aa | -12.27524 | -44.58917 | 2025-05-31 04:53:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe8285bc-0637-3588-90c5-069b9ceef889 | -8.47536 | -49.60785 | 2025-05-31 04:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7f18898-d47a-313f-a8c6-a338f6f376eb | -12.02299 | -49.52705 | 2025-05-31 04:53:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| b23a2007-2470-3045-8282-46d11a3f7119 | -12.6058 | -56.02365 | 2025-05-31 04:53:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c8ff15a6-b1a3-3ffd-b5d9-f1c8eaf659e6 | -9.676 | -48.60476 | 2025-05-31 04:53:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d88252e-2901-3415-9b25-fe4cc793e0ae | -13.10388 | -45.28135 | 2025-05-31 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b030264d-570d-3113-b021-71b33e38efe4 | -12.26979 | -44.58861 | 2025-05-31 04:53:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| da4a1453-4477-3583-a765-36b9dac2c447 | -13.10305 | -45.28789 | 2025-05-31 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 03c517cd-4412-3a3d-92a6-1e48f66015ba | -8.11626 | -45.90045 | 2025-05-31 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c2831f8-1140-3b1d-8cb9-db627c9d2303 | -10.2986 | -57.13567 | 2025-05-31 04:53:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d146ffb6-8ec7-3d94-96d7-848a16c462a1 | -11.91472 | -54.41994 | 2025-05-31 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c0bba02-2a3e-3c00-9883-14690fe772d9 | -10.64669 | -49.43159 | 2025-05-31 04:53:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| db3d4652-d322-372c-8aec-6123b9550dbd | -12.50491 | -55.1856 | 2025-05-31 04:53:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 53a78653-7c7f-3a82-b6b5-1cf9d655a5c7 | -11.64683 | -54.39821 | 2025-05-31 04:53:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 883b448d-207f-343b-90e2-cbfc227a8c89 | -13.09903 | -45.2775 | 2025-05-31 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38ef0867-d8b8-30bb-9fb2-592dd3994491 | -11.83609 | -51.26967 | 2025-05-31 04:53:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 21.2 |
| cc46cac0-c5b3-3435-8b72-fcce777f6721 | -10.61215 | -44.76619 | 2025-05-31 04:53:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 949ce301-8d47-33a5-8faf-2de5137428b4 | -12.30062 | -52.48521 | 2025-05-31 04:53:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2640af63-58f4-35e1-b7fa-de5fa8cb7508 | -9.40322 | -48.42499 | 2025-05-31 04:53:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 21ae186d-1285-3e5f-aa21-ca84d02507db | -9.27259 | -47.91824 | 2025-05-31 04:53:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6643a720-fb58-39a9-b50d-96c5692865dd | -11.91447 | -54.8181 | 2025-05-31 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 072db4db-095f-3f4a-9b88-7adf1a2d5768 | -12.01979 | -49.52148 | 2025-05-31 04:53:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| d3d012e4-e98f-3387-a772-51ef968a451b | -12.63375 | -51.68535 | 2025-05-31 04:53:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d92ee5a8-5d11-3985-bd0d-e46b7211815e | -11.04001 | -54.00204 | 2025-05-31 04:53:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24c50ed2-8857-347b-b1a3-b96ee563b3cd | -13.10429 | -45.2781 | 2025-05-31 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e4f8f850-3b70-303a-a2e5-5aac3d74e409 | -13.10444 | -52.28925 | 2025-05-31 04:53:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ea56f03-518b-3160-b464-34d7ead9d3bb | -9.31572 | -49.4902 | 2025-05-31 04:53:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e8b868f8-0f13-35f5-8f0e-e7962496309f | -10.45383 | -47.94815 | 2025-05-31 04:53:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a95c6126-8d1c-39f2-9ffa-47dcd5144642 | -13.09297 | -45.28333 | 2025-05-31 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24d8a51a-695f-3bb1-bd37-5b620e6d4b75 | -8.67476 | -48.28691 | 2025-05-31 04:53:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a2ca0f25-de9f-3c97-9900-152cda553fa8 | -9.60488 | -49.02517 | 2025-05-31 04:53:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 622d9844-c2ed-39d3-b635-d7ae8fdd0a2c | -11.91195 | -54.41585 | 2025-05-31 04:53:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README15.md)
