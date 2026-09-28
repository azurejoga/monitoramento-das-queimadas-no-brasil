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

## Dados Diários - Página 93

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8626438-5710-35af-96f4-58a70cbced07 | -18.74263 | -48.23406 | 2026-09-28 16:22:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 474c1b15-a18c-38cb-b187-1a95a43b0a73 | -21.22819 | -45.14188 | 2026-09-28 16:22:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 868a3d33-d306-3d3c-bb59-a729fddcd2a3 | -19.64034 | -42.00536 | 2026-09-28 16:22:00 | NOAA-20 | UBAPORANGA | MINAS GERAIS | Brasil | 3170057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7a2a8a89-de2e-3780-8aa2-94c3b8d0b0dc | -18.09995 | -44.35938 | 2026-09-28 16:22:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 39.8 |
| c403a90a-a74c-3b95-82ae-59755a259c4b | -18.08576 | -44.53735 | 2026-09-28 16:22:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 78c19011-008b-3638-8745-6cb8e4437277 | -23.32166 | -50.91568 | 2026-09-28 16:22:00 | NOAA-20 | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 1dd226e9-5b69-36bd-ad52-84d313fd9b89 | -23.13569 | -50.91632 | 2026-09-28 16:22:00 | NOAA-20 | RANCHO ALEGRE | PARANÁ | Brasil | 4121307 | 41 | 33 | nan | nan | nan | Mata Atlântica | 30.2 |
| 2bd6a4e8-231a-3d8e-8513-1fb6d9c88289 | -19.05792 | -40.30103 | 2026-09-28 16:22:00 | NOAA-20 | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 391a54f9-4f05-3631-b694-16570e3ed19c | -16.73065 | -39.87935 | 2026-09-28 16:22:00 | NOAA-20 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| 06abdc44-9c24-318e-95b3-39de0d3b7273 | -20.46141 | -46.22614 | 2026-09-28 16:22:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5b657411-1dd9-3c7e-8d41-ff72251f9a82 | -22.74644 | -46.2183 | 2026-09-28 16:22:00 | NOAA-20 | ITAPEVA | MINAS GERAIS | Brasil | 3133600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| f3c4d188-8fab-3ca4-bf8a-98429dd2192a | -18.52076 | -44.13182 | 2026-09-28 16:22:00 | NOAA-20 | PRESIDENTE JUSCELINO | MINAS GERAIS | Brasil | 3153202 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a19229b2-fe21-3ed9-b3ed-da779b56f825 | -19.78534 | -44.95979 | 2026-09-28 16:22:00 | NOAA-20 | CONCEIÇÃO DO PARÁ | MINAS GERAIS | Brasil | 3117603 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3b611cfd-9b4e-31e0-809a-aabe1a0ff39f | -23.58914 | -51.57848 | 2026-09-28 16:22:00 | NOAA-20 | CAMBIRA | PARANÁ | Brasil | 4103800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| d8f365c8-8d61-3ff9-a772-2ae64d5823c9 | -21.01707 | -44.99585 | 2026-09-28 16:22:00 | NOAA-20 | SANTO ANTÔNIO DO AMPARO | MINAS GERAIS | Brasil | 3159902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 56b5ab9c-5bb0-38ef-a1cd-11ece04fe241 | -19.59117 | -45.02829 | 2026-09-28 16:22:00 | NOAA-20 | LEANDRO FERREIRA | MINAS GERAIS | Brasil | 3138302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| 978986a1-cd30-302e-bb62-568f8387f938 | -21.73291 | -45.83625 | 2026-09-28 16:22:00 | NOAA-20 | CARVALHÓPOLIS | MINAS GERAIS | Brasil | 3114709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| b560d6ee-6d18-3d88-9391-bf2a2afb7066 | -18.83196 | -43.6204 | 2026-09-28 16:22:00 | NOAA-20 | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 7172aa0e-4b0c-3ff4-8aa0-b492c27bb8fd | -21.3021 | -45.33151 | 2026-09-28 16:22:00 | NOAA-20 | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| e56988fd-d006-32f8-93a4-85cd5983357f | -20.7647 | -51.31828 | 2026-09-28 16:22:00 | NOAA-20 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.6 |
| b0335d9d-e94d-3609-9003-1319b2ebdc9d | -19.13566 | -46.68325 | 2026-09-28 16:22:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 23.5 |
| a95e5470-92b5-31d8-913b-ed9935925398 | -20.65953 | -42.28654 | 2026-09-28 16:22:00 | NOAA-20 | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d67b5128-9d9d-3f27-bb90-379447219543 | -17.79498 | -47.16057 | 2026-09-28 16:22:00 | NOAA-20 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 31.7 |
| 2ffbd839-1fbc-3591-939b-23b91b5921f0 | -20.32298 | -42.01744 | 2026-09-28 16:22:00 | NOAA-20 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| de4f0b6f-93a3-3f0e-b418-75b1548ee17f | -17.95086 | -39.47559 | 2026-09-28 16:22:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| fd7799a4-5919-34fb-9b77-66c8122f100c | -22.85007 | -49.3629 | 2026-09-28 16:22:00 | NOAA-20 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 29370030-848f-33c3-8d14-3b0d404b79c0 | -18.0915 | -44.03134 | 2026-09-28 16:22:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 05eea714-9ae6-37ff-bce3-dc834d8cd8d6 | -20.04748 | -44.12272 | 2026-09-28 16:22:00 | NOAA-20 | SARZEDO | MINAS GERAIS | Brasil | 3165537 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 5598791c-0bd6-37c3-90c3-0c908629f141 | -19.45556 | -41.31936 | 2026-09-28 16:22:00 | NOAA-20 | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 12edd5ba-c0bb-3971-ba9f-a92c61c2e272 | -17.86033 | -39.28521 | 2026-09-28 16:22:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| d4a738b6-2ea0-352b-a023-2bb3687e61dd | -23.13621 | -50.91338 | 2026-09-28 16:22:00 | NOAA-20 | RANCHO ALEGRE | PARANÁ | Brasil | 4121307 | 41 | 33 | nan | nan | nan | Mata Atlântica | 21.3 |
| ae2eb81f-d0cd-31b1-972d-8a0d7c0f50b1 | -21.57939 | -45.8216 | 2026-09-28 16:22:00 | NOAA-20 | PARAGUAÇU | MINAS GERAIS | Brasil | 3147204 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 5b799bbb-c6bb-3900-976b-2089612c6c57 | -18.5586 | -48.39795 | 2026-09-28 16:22:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 92e2be99-c321-330e-9332-8be05fc0cf04 | -19.41428 | -48.43687 | 2026-09-28 16:22:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 6940e177-4c43-36cc-bffc-b810a0390e76 | -18.79773 | -43.83661 | 2026-09-28 16:22:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d9ab02b-521c-3c13-8fde-c43b36360c29 | -21.64138 | -43.66419 | 2026-09-28 16:22:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.0 |
| 95773116-5cff-3ff8-96c7-b4e75de7c033 | -21.05045 | -45.75476 | 2026-09-28 16:22:00 | NOAA-20 | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8d916c5c-12e9-34ee-a5e9-14473c1f1f70 | -21.5205 | -44.48747 | 2026-09-28 16:22:00 | NOAA-20 | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f9ba680b-a6a1-33fb-b389-bbe603269a17 | -18.74348 | -48.22736 | 2026-09-28 16:22:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 161fcdfa-ced2-394c-90cf-2b12b54d9840 | -18.18082 | -43.95004 | 2026-09-28 16:22:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 1f9cb706-7511-3017-8748-44984fbe54d4 | -18.11141 | -44.38776 | 2026-09-28 16:22:00 | NOAA-20 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 048fc438-f69d-3f8d-9703-f67486353393 | -18.74325 | -48.13128 | 2026-09-28 16:22:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| 929559b1-24c7-3884-95fd-6079a54d9b0c | -20.45546 | -50.01036 | 2026-09-28 16:22:00 | NOAA-20 | VOTUPORANGA | SÃO PAULO | Brasil | 3557105 | 35 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 05a5477b-69f5-3717-8a87-e48b40705f74 | -20.45736 | -46.2243 | 2026-09-28 16:22:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6df7b0c4-e22b-3595-a96c-d3dc459ad64c | -20.76605 | -47.11725 | 2026-09-28 16:22:00 | NOAA-20 | SÃO TOMÁS DE AQUINO | MINAS GERAIS | Brasil | 3165107 | 31 | 33 | nan | nan | nan | Cerrado | 17.6 |
| b44d4516-a83f-3063-aeb2-2df935cbb968 | -20.94594 | -46.44803 | 2026-09-28 16:22:00 | NOAA-20 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 3427a3a2-e9b9-3962-824e-14dc8da485cf | -18.88257 | -41.08207 | 2026-09-28 16:22:00 | NOAA-20 | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| e9059196-4049-36a2-8d23-22599e220666 | -19.90355 | -49.32741 | 2026-09-28 16:22:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 227dc081-dbb2-3b60-8823-0eaece52cc7f | -20.06077 | -40.36609 | 2026-09-28 16:22:00 | NOAA-20 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2c19e525-8fd5-3952-b384-cb6ccc9da8dd | -21.3026 | -45.33564 | 2026-09-28 16:22:00 | NOAA-20 | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 08d2794e-5040-3eb9-8532-2b7d7c0dd643 | -18.29541 | -43.01226 | 2026-09-28 16:22:00 | NOAA-20 | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 5b616974-8ceb-307b-9540-3433cd74b26e | -19.43856 | -45.89074 | 2026-09-28 16:22:00 | NOAA-20 | SERRA DA SAUDADE | MINAS GERAIS | Brasil | 3166600 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 58c63ad7-c160-3e1a-9421-a704b4cfe61d | -20.50531 | -41.95261 | 2026-09-28 16:22:00 | NOAA-20 | ALTO CAPARAÓ | MINAS GERAIS | Brasil | 3102050 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| a36c110c-7958-32ec-be62-633e15164831 | -17.783 | -42.34513 | 2026-09-28 16:22:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 0a4f8c9b-96e5-3d8a-8498-49ff566cae97 | -20.80927 | -51.74563 | 2026-09-28 16:22:00 | NOAA-20 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 714ada0a-6300-3383-9a0d-731dfea89c3e | -17.59694 | -45.80458 | 2026-09-28 16:22:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 9ac31df0-c7e9-37a8-bc82-aed1a960115d | -19.10992 | -43.95648 | 2026-09-28 16:22:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a7e65df5-4aad-3341-a7bc-a609ba648f46 | -18.87609 | -46.66649 | 2026-09-28 16:22:00 | NOAA-20 | GUIMARÂNIA | MINAS GERAIS | Brasil | 3128907 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 73c08760-aafe-3d94-a634-b44cb78f6770 | -23.11977 | -52.35008 | 2026-09-28 16:22:00 | NOAA-20 | ALTO PARANÁ | PARANÁ | Brasil | 4100608 | 41 | 33 | nan | nan | nan | Mata Atlântica | 18.6 |
| 346d2ce5-a76c-3850-b274-8f78db74fda6 | -17.94353 | -47.00739 | 2026-09-28 16:22:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 308ae846-3e09-3428-add4-ee7f5ff86210 | -18.68389 | -48.62679 | 2026-09-28 16:22:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 87c9ac58-557f-3284-85eb-ec697bcb0662 | -18.43523 | -43.98238 | 2026-09-28 16:22:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 496b1ae6-bb7f-31c3-b2e8-5d0a0b83f116 | -19.40983 | -48.44338 | 2026-09-28 16:22:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 60.6 |
| a3a19589-aeb1-32ec-afde-be5fd15449c7 | -20.87621 | -44.11638 | 2026-09-28 16:22:00 | NOAA-20 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 839aa755-af57-3cb5-8f8c-0c44810f634f | -20.74027 | -47.18639 | 2026-09-28 16:22:00 | NOAA-20 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 20e65035-1ceb-3618-8cd7-cf7b6ee863be | -20.76994 | -51.30754 | 2026-09-28 16:22:00 | NOAA-20 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.2 |
| 876d6682-c42f-3d63-9128-1016620b62b5 | -19.45014 | -41.94043 | 2026-09-28 16:22:00 | NOAA-20 | INHAPIM | MINAS GERAIS | Brasil | 3130903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 1949dc37-a69c-36d8-809c-4696eea36e10 | -19.4416 | -45.89133 | 2026-09-28 16:22:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| db83e5dc-985d-30d7-b550-89006e049ca2 | -18.08684 | -43.68919 | 2026-09-28 16:22:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 187cfda8-5bd1-36b3-840c-623241e6cc91 | -18.39712 | -42.55012 | 2026-09-28 16:22:00 | NOAA-20 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 665b9807-7f54-3391-939e-d54e4f5567cd | -18.68482 | -48.6216 | 2026-09-28 16:22:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 624c419e-dd38-3204-8e04-dc4f9785c19e | -18.67941 | -48.61912 | 2026-09-28 16:22:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1a45a446-38b2-3dfa-bc4d-ec96d98c7a57 | -18.05972 | -42.97642 | 2026-09-28 16:22:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 93cccb93-07f2-3241-90db-4a2c682524fa | -19.10615 | -43.95706 | 2026-09-28 16:22:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fd5b87f1-e749-3800-a48a-45d9a2c3f32e | -19.44671 | -41.94111 | 2026-09-28 16:22:00 | NOAA-20 | INHAPIM | MINAS GERAIS | Brasil | 3130903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6916238a-d16b-3284-9077-598110a4dcd2 | -18.88592 | -41.08154 | 2026-09-28 16:22:00 | NOAA-20 | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| a8a7ea66-223e-3346-a208-9659486d6c17 | -20.25489 | -41.60917 | 2026-09-28 16:22:00 | NOAA-20 | IBATIBA | ESPÍRITO SANTO | Brasil | 3202454 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 32b56d9b-cfb3-355f-8ddd-a09969150832 | -17.46335 | -44.40662 | 2026-09-28 16:22:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f7e88acd-bede-37ed-9ad8-3dbe2cae0b09 | -18.68516 | -48.62461 | 2026-09-28 16:22:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 40334a33-21cd-3ff0-af22-ff94b25ec98c | -20.08259 | -41.92188 | 2026-09-28 16:22:00 | NOAA-20 | SANTANA DO MANHUAÇU | MINAS GERAIS | Brasil | 3158904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 033d4c52-6261-31b1-95e5-7efcaf634f58 | -22.17427 | -45.71731 | 2026-09-28 16:22:00 | NOAA-20 | SÃO SEBASTIÃO DA BELA VISTA | MINAS GERAIS | Brasil | 3164407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| dc88a27a-2a40-35f2-9c6a-3a95ca832f8e | -20.98412 | -45.80452 | 2026-09-28 16:22:00 | NOAA-20 | ILICÍNEA | MINAS GERAIS | Brasil | 3130507 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6c193276-9b6b-3ffd-9bc1-d3a9b035e3c7 | -17.94802 | -47.00673 | 2026-09-28 16:22:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 57.3 |
| d5e7b57f-2ab4-3cef-a161-35e77169385e | -20.75749 | -51.31013 | 2026-09-28 16:22:00 | NOAA-20 | ANDRADINA | SÃO PAULO | Brasil | 3502101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.0 |
| e3943718-c4a3-3606-a20a-20f61a617ebe | -20.79856 | -45.35342 | 2026-09-28 16:22:00 | NOAA-20 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| f0224cbc-9ae0-3449-b53c-9ebe86bb4b3b | -18.93002 | -47.20042 | 2026-09-28 16:22:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4682d678-59b1-3e62-b72d-4c5593ef93d8 | -18.06282 | -41.42843 | 2026-09-28 16:22:00 | NOAA-20 | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 1e578024-f0d8-3257-82aa-d80928a761bc | -19.00499 | -47.25081 | 2026-09-28 16:22:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| eda128fe-7a05-3beb-b45f-5b83898eafa7 | -23.02849 | -51.8705 | 2026-09-28 16:22:00 | NOAA-20 | SANTA FÉ | PARANÁ | Brasil | 4123402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| c81b3198-d2ea-34e8-9d07-030c786a9f76 | -17.7279 | -44.33802 | 2026-09-28 16:22:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b637f0c5-4886-3e4e-8dd2-e07654a1b14f | -17.07767 | -41.36292 | 2026-09-28 16:22:00 | NOAA-20 | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 11dc95e9-85a8-3ea1-b672-53aabef3bfb9 | -23.05103 | -51.15889 | 2026-09-28 16:22:00 | NOAA-20 | SERTANÓPOLIS | PARANÁ | Brasil | 4126504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 34d89cac-5632-357b-9ae4-9894a492d044 | -19.54417 | -44.95263 | 2026-09-28 16:22:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 185c13ee-95ca-3eca-b6aa-46cefc1a7b64 | -19.46516 | -40.05555 | 2026-09-28 16:22:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 81b9ebb0-93b0-31e9-9492-187f9378c24d | -20.07622 | -41.92699 | 2026-09-28 16:22:00 | NOAA-20 | SANTANA DO MANHUAÇU | MINAS GERAIS | Brasil | 3158904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 22908001-6d01-3f68-92b3-246cfce9c3fd | -19.59595 | -44.86854 | 2026-09-28 16:22:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5e878b16-be9d-3fa2-8533-7e66816cb4f2 | -19.27125 | -47.29588 | 2026-09-28 16:22:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| db8f7435-9d2b-3aae-99d8-8b4a685f9851 | -18.68326 | -48.62073 | 2026-09-28 16:22:00 | NOAA-20 | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 4327099b-8d7b-3828-a470-8ce99b92e4a4 | -17.65837 | -44.30843 | 2026-09-28 16:22:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f65c4823-70a4-36a7-a8be-637c9f6e1810 | -20.20333 | -48.57191 | 2026-09-28 16:22:00 | NOAA-20 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |


[Clique aqui para ver as próximas entradas](README94.md)
