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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3d15a421-bdf9-3894-bfb8-10a8bdeb0dfd | -22.41198 | -46.79954 | 2025-09-22 04:19:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c7ae5c6-1e7d-333b-9b6a-2268cf8cb746 | -10.38898 | -46.08431 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ae9da9a-82e9-3fc9-aa66-be59940cd45d | -20.67173 | -54.57343 | 2025-09-22 04:19:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e1772d8c-85ab-3b0a-af37-e9f698cba900 | -15.03301 | -55.2898 | 2025-09-22 04:19:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 836ef15f-79b2-319c-b498-e855bba9cdcd | -9.99011 | -46.24543 | 2025-09-22 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8d725d61-8649-3a00-aad8-6cc6d3429929 | -14.6884 | -48.78325 | 2025-09-22 04:19:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8d9feada-5deb-300f-8d73-637e1564157c | -15.99501 | -59.48148 | 2025-09-22 04:19:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a59f33b0-bc45-36b7-ae75-7a264f19e5f5 | -19.85659 | -57.30524 | 2025-09-22 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2f7add00-39e8-3dd6-a85d-5f370c5d71c1 | -21.13841 | -46.3362 | 2025-09-22 04:19:00 | NPP-375D | NOVA RESENDE | MINAS GERAIS | Brasil | 3145109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| e4aed018-3bf7-3409-8acf-400f9e109bb5 | -17.40814 | -45.0171 | 2025-09-22 04:19:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 549651f1-bc9b-3a05-bd40-d6fdc3e773d2 | -17.67196 | -44.08486 | 2025-09-22 04:19:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4361c13f-ea38-3ed7-9d82-fe6d34b365ae | -10.04328 | -49.19966 | 2025-09-22 04:19:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f205979c-1888-3b03-8261-1605016f8869 | -14.62132 | -49.7499 | 2025-09-22 04:19:00 | NPP-375D | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f93b5394-4823-3c1a-ae49-7a193b17e63f | -20.66858 | -54.49212 | 2025-09-22 04:19:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80029e3c-f06d-3fea-8709-a9adb90fd7d9 | -15.03655 | -55.28997 | 2025-09-22 04:19:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa1df7b5-6192-3294-9290-a613d860c228 | -18.38285 | -46.46742 | 2025-09-22 04:19:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| bcc33e8d-de5a-3293-ab15-8a02d61e8d75 | -22.00559 | -43.30968 | 2025-09-22 04:19:00 | NPP-375D | SIMÃO PEREIRA | MINAS GERAIS | Brasil | 3167509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3f99b80a-5132-352f-b023-191ca5c2ce20 | -15.76712 | -59.41063 | 2025-09-22 04:19:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f661853d-c00a-3279-979d-478ce1f825fc | -18.37892 | -46.4705 | 2025-09-22 04:19:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 38a58f08-cc38-3088-8187-a1e3b7135564 | -10.65699 | -44.23607 | 2025-09-22 04:19:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 807fb1e2-e4ae-3202-852c-1c6b15d4659c | -19.31059 | -43.75734 | 2025-09-22 04:19:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 298fc51e-ddd5-3c94-a828-810bf0ccc8ef | -10.65422 | -44.23202 | 2025-09-22 04:19:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97931665-593e-3bef-a39f-6b5b8a87785a | -15.90723 | -45.33634 | 2025-09-22 04:19:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a5a15cc1-1e3b-374e-8c37-c3b424519dc5 | -19.85371 | -57.29112 | 2025-09-22 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1fb74d62-113c-38ab-a59a-a0cc284ed184 | -19.84728 | -42.20115 | 2025-09-22 04:19:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 48135fd6-c6d5-3c56-9007-124eae9f3bb6 | -10.34765 | -46.06655 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0f33a5a7-530e-3eb4-97d8-40733b9018f5 | -10.39243 | -46.08487 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 43dc406c-74bd-3979-b7ac-91bbe6762f30 | -20.86915 | -42.81235 | 2025-09-22 04:19:00 | NPP-375D | COIMBRA | MINAS GERAIS | Brasil | 3116704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 99e13d1b-a834-3061-aa4c-21c9dd56e449 | -11.45032 | -43.53489 | 2025-09-22 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82ab7044-578e-3e80-bfbf-ddfabecd9604 | -15.15998 | -49.58866 | 2025-09-22 04:19:00 | NPP-375D | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 6e1ab311-7607-3abd-978c-1cfd3ce7461d | -20.38651 | -58.05622 | 2025-09-22 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 9a421c9d-7558-304c-a9be-1197353c3125 | -10.36796 | -46.06124 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f8bf5968-95a5-3e1b-baa7-d79b423c415a | -11.47931 | -43.5468 | 2025-09-22 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f190e0ac-ce00-3dd9-83c1-bf66b68cb84b | -17.68277 | -44.0827 | 2025-09-22 04:19:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a6269c90-7d33-3f12-bfbe-3632eda2486e | -17.44256 | -44.81633 | 2025-09-22 04:19:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d141b48-9ea9-34f8-94fc-9edbad15ca68 | -20.66967 | -54.48683 | 2025-09-22 04:19:00 | NPP-375D | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d989c20e-2651-38f7-9555-3d0a11047cec | -19.85753 | -57.30102 | 2025-09-22 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 43b2b464-0d70-3d4c-b32b-e124b230c641 | -11.43804 | -43.52564 | 2025-09-22 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a65af138-4ab2-33d2-9ed2-b315ca5e4cdd | -21.55147 | -43.82928 | 2025-09-22 04:19:00 | NPP-375D | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 5b400f95-2868-3da6-bce5-3df7a1a0b283 | -10.04393 | -49.19598 | 2025-09-22 04:19:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5da9ca16-4330-3a55-9b70-c6eca4c8988d | -15.94698 | -59.40224 | 2025-09-22 04:19:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 29a0f937-ce06-3e6b-9a4f-6092277dcd43 | -15.76189 | -59.41983 | 2025-09-22 04:19:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c8e4fe2-6fc6-3254-9c70-10ad50bc1f46 | -18.50107 | -42.6874 | 2025-09-22 04:19:00 | NPP-375D | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dcf261e5-adeb-343e-9377-36460de999b8 | -20.75628 | -43.35875 | 2025-09-22 04:19:00 | NPP-375D | SENHORA DE OLIVEIRA | MINAS GERAIS | Brasil | 3166006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ece8c45a-74d8-3a7e-aaf2-9b1cf9949005 | -10.36192 | -46.11912 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 39a86279-89e0-3043-a2d1-3dabf2cbe90d | -22.40591 | -46.79459 | 2025-09-22 04:19:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 18d820e6-3933-3a81-9f7c-f5d07675971a | -11.46091 | -43.53291 | 2025-09-22 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| afb316f6-e19d-3a47-8530-d093dd04ba6d | -17.43534 | -44.79622 | 2025-09-22 04:19:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0088732-42ef-328f-92d0-a824de562e81 | -16.07352 | -43.47779 | 2025-09-22 04:19:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa2069fb-7319-33dc-901d-98e95e766fdc | -17.34291 | -46.82888 | 2025-09-22 04:19:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8ccf450-ffc0-3683-a035-fc9664473cc1 | -21.62765 | -43.65114 | 2025-09-22 04:19:00 | NPP-375D | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| bf6da025-4a71-305d-9a05-e151f36f7b00 | -17.56089 | -44.92638 | 2025-09-22 04:19:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a7e9f5e-1655-3fb7-90d4-b8f6b24949c4 | -17.25924 | -43.43441 | 2025-09-22 04:19:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 618766b3-e309-313e-b67b-4a3710bd6c14 | -20.6723 | -42.28329 | 2025-09-22 04:19:00 | NPP-375D | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 58bcfc39-342e-370a-9a31-2ccb0c84f454 | -17.6072 | -44.1679 | 2025-09-22 04:19:00 | NPP-375D | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a77e222-bcad-3207-b586-7fb835008726 | -11.49993 | -43.56836 | 2025-09-22 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e95adbf-d11d-3ba2-8b92-de67917fe6be | -11.46425 | -43.53344 | 2025-09-22 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d56750e7-0fa2-3f65-86e1-2b36577f84d5 | -10.3827 | -46.07933 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 518af03b-cb10-3571-8ea4-46dee1174e0a | -9.99073 | -46.24162 | 2025-09-22 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8d38e6f-3018-3e67-b796-284b7f152cd5 | -10.46704 | -48.03794 | 2025-09-22 04:19:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9c1ed55c-c5bb-3d8e-b017-19d57735dcd3 | -20.26625 | -55.50056 | 2025-09-22 04:19:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 5.7 |
| be718231-582c-3d2b-9dbf-d65cd1801ba0 | -22.40806 | -46.80268 | 2025-09-22 04:19:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c2a156df-e17d-30f8-850d-0cb3bfaefccb | -18.94032 | -45.76785 | 2025-09-22 04:19:00 | NPP-375D | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 04ca3068-6811-3cda-bf50-1daa01888ae2 | -17.25175 | -43.43714 | 2025-09-22 04:19:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b1b591aa-ca1c-36b8-9a12-e64ee1a0433a | -19.11456 | -43.17537 | 2025-09-22 04:19:00 | NPP-375D | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 926faa3f-8285-34ed-aeb9-3d58f9c086bb | -11.45756 | -43.53238 | 2025-09-22 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b1f3f0a8-8047-304f-ba95-9fe557939f8d | -9.26805 | -45.85056 | 2025-09-22 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bfe4052d-3431-3323-81dc-0044b8bc6f64 | -18.98712 | -44.2298 | 2025-09-22 04:19:00 | NPP-375D | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d7051f96-883d-3c4e-8de7-b664f5692e17 | -10.34818 | -46.07355 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03561c9c-9ba5-323c-bda8-0e3fbc3ccd85 | -10.25413 | -46.07418 | 2025-09-22 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 99ac22e1-09b9-3d6d-9135-35120c63ecdb | -19.63733 | -57.74193 | 2025-09-22 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 9ad3dadc-1ebb-3652-9ac7-073068217f7b | -17.06051 | -44.90055 | 2025-09-22 04:19:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| af96634a-6631-39d4-a421-224490939aa4 | -17.67537 | -44.08543 | 2025-09-22 04:19:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 64fe6778-65f3-369d-9261-cb428079fa97 | -8.85343 | -46.1567 | 2025-09-22 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e3024c9-f5fd-3097-a64f-c6172f9f6db8 | -17.25066 | -43.43744 | 2025-09-22 04:19:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 205a0134-450f-3362-9f68-1e5d14ea6a4e | -15.7644 | -59.42264 | 2025-09-22 04:19:00 | NPP-375D | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d94210df-2034-3d71-a21d-2e750bc24c41 | -17.66799 | -44.08812 | 2025-09-22 04:19:00 | NPP-375D | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 90e58a95-4241-3a7e-9859-ef99012db33c | -20.8661 | -42.80704 | 2025-09-22 04:19:00 | NPP-375D | COIMBRA | MINAS GERAIS | Brasil | 3116704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8a6f39bd-b8a9-3ef7-a286-dfdfae538bec | -18.26759 | -42.91798 | 2025-09-22 04:19:00 | NPP-375D | COLUNA | MINAS GERAIS | Brasil | 3116803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f8dd8d93-926e-3385-b6f9-478f92b5eee1 | -16.99938 | -48.04807 | 2025-09-22 04:19:00 | NPP-375D | ORIZONA | GOIÁS | Brasil | 5215306 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a0db92a9-a2ce-3662-b0e2-fb55ee4511ec | -11.41798 | -43.52242 | 2025-09-22 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6fb4bd6a-a737-37ef-8f2e-bfc0e803e0bc | -17.43478 | -44.79989 | 2025-09-22 04:19:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22b32a1e-ffb4-3c94-8fb2-2e561f36bc57 | -21.60664 | -44.73049 | 2025-09-22 04:19:00 | NPP-375D | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 788ff885-9524-38d5-a220-7ded54e7aadb | -17.34352 | -46.82515 | 2025-09-22 04:19:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37dc2bbc-ae4c-3f4b-83a7-7fdc189d6b20 | -10.06784 | -45.63623 | 2025-09-22 04:19:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ebe16f31-d602-32d1-8e51-604901a58694 | -20.5878 | -45.74604 | 2025-09-22 04:19:00 | NPP-375D | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc435b66-96cf-32e3-81be-2e5b1e592a45 | -11.52437 | -43.62354 | 2025-09-22 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 321d1372-8b2d-3853-b90f-fde4d075960f | -10.85026 | -42.26381 | 2025-09-22 04:19:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 84f8a764-de4e-3ce8-a5ca-3a50802b90fc | -7.71183 | -55.44984 | 2025-09-22 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32530734-672c-3c08-999a-fe8a3192300c | -20.37037 | -41.10518 | 2025-09-22 04:19:00 | NPP-375D | VENDA NOVA DO IMIGRANTE | ESPÍRITO SANTO | Brasil | 3205069 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 18def21a-6a57-303e-9b8d-68ebbb00be76 | -10.46078 | -44.19397 | 2025-09-22 04:19:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b87ad47-8368-3450-925f-d841c6320bbf | -20.18855 | -44.62863 | 2025-09-22 04:19:00 | NPP-375D | CARMO DO CAJURU | MINAS GERAIS | Brasil | 3114204 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d17abfa7-1a1b-3393-a8d9-1f70f9ac0b7c | -22.41375 | -46.78832 | 2025-09-22 04:19:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 807fa42c-7338-3b64-9fe8-55cac8821792 | -11.48599 | -43.54788 | 2025-09-22 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da5e11d5-9bc1-3c06-a149-aa7b147b96c2 | -18.10121 | -44.26405 | 2025-09-22 04:19:00 | NPP-375D | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f4bd46a5-da10-316b-a25f-abe22a2c673f | -18.84343 | -42.19339 | 2025-09-22 04:19:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 436b0f3b-5e26-3959-91ad-9f2748dada1e | -22.4159 | -46.79641 | 2025-09-22 04:19:00 | NPP-375D | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 3db799fb-14dd-3979-9beb-6bd6686ccf87 | -20.26823 | -55.49116 | 2025-09-22 04:19:00 | NPP-375D | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1c5511d-2e41-385c-9e46-7186c94aab79 | -18.05288 | -43.84501 | 2025-09-22 04:19:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0e68dfe9-f329-3e51-a33d-0307e440dec7 | -20.67165 | -42.28823 | 2025-09-22 04:19:00 | NPP-375D | FERVEDOURO | MINAS GERAIS | Brasil | 3125952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |


[Clique aqui para ver as próximas entradas](README24.md)
