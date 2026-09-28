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

## Dados Diários - Página 107

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b90fe5f-d1ce-3c3a-9525-6d6d962c176e | -11.84281 | -47.77862 | 2026-09-28 16:24:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 1a4feb49-446d-364e-8bc9-8d3f5ed5e197 | -12.61371 | -47.31517 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4c3c3570-83f5-388b-a746-7a4d2b315a8e | -12.07417 | -48.53805 | 2026-09-28 16:24:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 529.2 |
| 51ac39b1-5c1b-3950-af1c-b60839a8fb56 | -12.31311 | -50.25743 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 941f5d36-1fce-3426-90af-a1953683c1ae | -14.08489 | -46.32925 | 2026-09-28 16:24:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 69638331-c2a0-3128-9090-00b1b93a5254 | -12.68817 | -47.26063 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 640b4b1e-6fcb-3dfc-8ad4-68594f808528 | -16.81006 | -40.79662 | 2026-09-28 16:24:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| b3d55273-da8d-3613-939b-47675fad576b | -13.70764 | -48.82947 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 742a5f70-1f23-39d8-ae4d-22a88b8c1bcb | -15.07043 | -54.60216 | 2026-09-28 16:24:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 218.2 |
| 7c29541e-9b05-3b10-b21b-a77f41baf5b8 | -13.29872 | -40.40499 | 2026-09-28 16:24:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 757c065a-94eb-3628-b517-39949506d4fc | -11.5261 | -47.39222 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3b68a80c-2c9d-3e90-bbc5-58f271ffc4b4 | -12.64386 | -47.32046 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7e7a03fb-6453-3a2b-b6dd-b636ae9e9833 | -15.1871 | -46.17492 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| deb46a8c-e79a-33c9-9704-12042d0e1cd4 | -11.98605 | -41.97863 | 2026-09-28 16:24:00 | NOAA-20 | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 7.6 |
| fae93d13-89c5-3f8b-ac7b-69c444370912 | -12.74186 | -50.68282 | 2026-09-28 16:24:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 92961757-2b19-319e-83a0-65713568b692 | -11.86527 | -47.1013 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b8962bbd-0618-3887-8975-c18305a2a413 | -15.40448 | -47.91938 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 33b98834-a5e6-35b2-8311-eaef31f5eef6 | -11.84628 | -47.78086 | 2026-09-28 16:24:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 4851fec1-4b58-35ce-895c-eec61931d10a | -13.3303 | -38.99821 | 2026-09-28 16:24:00 | NOAA-20 | VALENÇA | BAHIA | Brasil | 2932903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 5530db2a-9c1a-34e3-a427-c01caa9f424d | -15.55365 | -47.92516 | 2026-09-28 16:24:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9c83feac-a888-3e48-a15d-33e661bf41d9 | -16.15382 | -42.85194 | 2026-09-28 16:24:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 97f80917-221b-32e7-a9e5-cf2ead8fcccc | -12.67853 | -47.3531 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 753e1788-22cc-3496-8cf9-25e8ed81188f | -12.30195 | -50.25241 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 393141e1-b7b4-384a-bea7-0f17b2b1db9a | -15.20525 | -50.24685 | 2026-09-28 16:24:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 30da3049-90ed-3496-a446-eb0bdd18010e | -12.65337 | -47.35122 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 36.9 |
| 81454417-9c1f-3468-8490-7f25e82afa88 | -12.43553 | -44.15878 | 2026-09-28 16:24:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5d53e91f-fc96-3427-aeab-9d930af49fa3 | -11.20929 | -44.76215 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 75b134ce-69b0-354f-a3e8-01fd9c9ec2e7 | -13.4746 | -48.63442 | 2026-09-28 16:24:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 809b480d-c3fb-357d-8674-43c5646368a2 | -15.17757 | -46.14094 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 2ecbd843-8cf3-3e76-92a4-897a3e0ac026 | -12.16082 | -50.40969 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a16295b7-ae0e-39c7-be81-961db29f7426 | -12.38121 | -50.24215 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| f5893d68-342e-3941-a485-fae40d37aee1 | -12.61906 | -47.32269 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 428e12e1-692a-311e-820b-bd0fe4ed95eb | -13.08619 | -47.45422 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 5dc2a3c2-77eb-3d84-9efd-308d9e6ed7d3 | -13.31813 | -43.94711 | 2026-09-28 16:24:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 5cb583e0-93be-3e8e-8260-21802303d3c4 | -11.36999 | -43.42534 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 00faf68f-16e3-3138-82d6-1ca36b9b2888 | -13.08402 | -47.43694 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 594ff3a3-6417-3014-a77b-d968e238ffa5 | -15.39929 | -47.91547 | 2026-09-28 16:24:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ba7d31d7-d3ce-3f91-9271-30ed6ba86cfe | -12.71074 | -46.9807 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8558d453-a6c2-3474-b68c-8e8dcadd4d54 | -11.39615 | -45.41164 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1ba3bf8f-6fea-37e4-a76b-b12a7e429473 | -16.34625 | -47.70007 | 2026-09-28 16:24:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 16c085da-6ad4-3378-96ec-6e1f7dd78f31 | -12.28676 | -50.25756 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a3d72c18-b9e0-3cc8-bab6-46355448862f | -15.34463 | -48.12555 | 2026-09-28 16:24:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 0262ce99-5792-3b05-bc15-7462e1dc03ce | -11.21651 | -44.78656 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e4c91872-6374-36d5-85aa-1a00809aefd2 | -14.32565 | -44.80444 | 2026-09-28 16:24:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 8dc8f1fc-64b7-3f7a-9386-0981a567ebb7 | -12.71143 | -46.97689 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| be9f931f-d7ca-30d0-932a-dfcf2e6cfb36 | -15.07271 | -54.60254 | 2026-09-28 16:24:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 146.6 |
| ca262a0f-7c5f-32ee-8643-3bd42f20b801 | -11.6747 | -43.5253 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 9390f409-3be3-313e-867a-64955b2d0e24 | -12.74411 | -47.2897 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 5547ccf4-01f4-3ff7-8204-4f5830640985 | -16.25978 | -41.81485 | 2026-09-28 16:24:00 | NOAA-20 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| 66ca25ec-7a08-300a-8861-83e2bec03b66 | -12.4474 | -48.21727 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 801adb50-089b-39f1-aa44-b7214c48d91a | -11.21949 | -44.78188 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 912c8563-5c94-3c9a-804d-0c9e119aa6cb | -15.02211 | -49.5832 | 2026-09-28 16:24:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 11f976d8-87dd-3081-bcd9-0760f7f1b9de | -16.34544 | -47.6982 | 2026-09-28 16:24:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 375b9e47-d414-3b50-bdf8-195b690eedfb | -11.45699 | -44.92627 | 2026-09-28 16:24:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 859e6e60-688f-381b-9a40-ef8363601c9a | -12.64743 | -47.33957 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| e58a5f14-a513-3f01-b27a-7336bd049975 | -11.53252 | -47.15683 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 9872c909-b9c7-3ba0-a290-8c8d9c98a87e | -13.08998 | -47.44933 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 4c2e9749-b74f-331a-91c2-190193ac08ca | -14.61443 | -49.09849 | 2026-09-28 16:24:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 1d4db2ad-3d57-3778-bb5d-526f46d3822b | -11.20392 | -44.80107 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 689bb27f-9a97-3b3e-bb52-1b57ec6d14ad | -14.66667 | -48.76343 | 2026-09-28 16:24:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 7b477d6b-f892-38fd-a797-f3bb5339d332 | -15.09078 | -54.7128 | 2026-09-28 16:24:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 2254089e-6e1a-33f7-850a-d2f3409be0dc | -13.16668 | -48.55083 | 2026-09-28 16:24:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 46781066-6e31-3c94-b043-cf56742b0a72 | -12.74763 | -50.6856 | 2026-09-28 16:24:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 69c903e0-c46c-3359-bc73-b09b73e73e77 | -15.46373 | -41.06664 | 2026-09-28 16:24:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 92b52fcd-eaf9-3dc5-a854-c7d1d711458b | -15.15312 | -43.6105 | 2026-09-28 16:24:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 22.4 |
| 26057ae4-69e7-37b8-a302-3d954b27e154 | -11.18952 | -44.80312 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| fc6fb929-f146-3b2d-9a11-8c8a37f6660f | -12.78432 | -54.01711 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 37c7ab3e-e910-365b-81de-aae307c4a87c | -11.38021 | -43.42382 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 673c654e-8857-373b-884b-c24f818d62d6 | -12.70261 | -47.33735 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| d2862ec1-4b40-36c6-b256-b02a99ee360b | -11.22152 | -44.78282 | 2026-09-28 16:24:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 005f0ad6-98b9-3355-b89c-e0ef22982ea0 | -12.74146 | -50.67936 | 2026-09-28 16:24:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ead022eb-c336-3aea-8e98-f0a634124f32 | -12.43678 | -44.14201 | 2026-09-28 16:24:00 | NOAA-20 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 55.6 |
| ab128cf8-e96a-316f-a488-cf2a29b765d3 | -12.75318 | -47.30178 | 2026-09-28 16:24:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 3cfac8f7-cde7-3e8e-a4a9-f88adf9419f0 | -15.20898 | -46.19125 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 9da15224-3cef-3a5d-815a-076cc2a2a031 | -13.69226 | -48.82472 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| db839ccf-28d0-35b9-b9cf-8486d77f0d3d | -16.61863 | -41.51615 | 2026-09-28 16:24:00 | NOAA-20 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 4a331272-51e8-3f2d-accf-7016c6910af9 | -13.32635 | -43.95417 | 2026-09-28 16:24:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 4fe8bc4f-870e-3f17-94bd-3306491facb9 | -14.26795 | -40.52449 | 2026-09-28 16:24:00 | NOAA-20 | MIRANTE | BAHIA | Brasil | 2921450 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| adccc182-640c-378d-8dfd-5a0ac278956e | -15.21718 | -46.18998 | 2026-09-28 16:24:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 12.9 |
| c1a117e8-7024-3ff1-b28b-3bc91d711b1f | -16.341 | -47.69554 | 2026-09-28 16:24:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 07a25425-b699-39c5-bb8e-25f27eb76135 | -12.44442 | -48.21943 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| a90addff-4d81-365c-9690-89f33964d64a | -16.43798 | -47.49644 | 2026-09-28 16:24:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 8da79d77-32d0-36f0-a291-9ecb74e4c57f | -11.53349 | -47.38321 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 918530db-1f88-36de-9593-7cb96d152e03 | -11.39492 | -43.42921 | 2026-09-28 16:24:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f787f441-64f5-365c-8a83-29aea088929c | -11.84192 | -47.78143 | 2026-09-28 16:24:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9a536cb8-40ad-3f74-ba75-7285d2b98541 | -12.79905 | -54.00974 | 2026-09-28 16:24:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 43d26551-fc6a-39cd-90b7-3e40cfda33d6 | -11.53305 | -47.1607 | 2026-09-28 16:24:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 28866c6f-c87a-3ee1-8f73-a47d136ca504 | -14.20429 | -41.32812 | 2026-09-28 16:24:00 | NOAA-20 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 6f07f684-11ec-34ea-bcce-16a06c9ac979 | -11.90746 | -47.02461 | 2026-09-28 16:24:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 643b56de-99ab-3c31-8f8f-5331505b73f6 | -16.79197 | -43.01097 | 2026-09-28 16:24:00 | NOAA-20 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 368bd287-8cb5-3f8b-81ff-191a1fddc07d | -15.15371 | -43.61462 | 2026-09-28 16:24:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 73.8 |
| bea4e3d8-2832-335d-9a0e-eaaf85c462d3 | -15.06769 | -54.62363 | 2026-09-28 16:24:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 7a155101-606f-3328-86e0-4c1591c9a990 | -13.45531 | -48.59409 | 2026-09-28 16:24:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 16d365ba-a85d-32b6-a817-5d2a6543ce19 | -15.0698 | -54.59531 | 2026-09-28 16:24:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 218.2 |
| e9dfb709-b950-3fac-bfd1-baa53d14e7f6 | -17.30295 | -44.53152 | 2026-09-28 16:24:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 77c500ff-9403-353b-abad-cc22722c4b3c | -12.74458 | -50.68301 | 2026-09-28 16:24:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 18e41a8a-f547-312d-931c-2acf620c8c34 | -12.86183 | -44.81261 | 2026-09-28 16:24:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9a5b1ce7-db70-3119-96b2-a605c463705a | -12.44287 | -48.21781 | 2026-09-28 16:24:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| aff0efe7-cb9a-378b-99b0-08166f455f0d | -6.47578 | -39.89771 | 2026-09-28 16:26:00 | NOAA-20 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 01e30e30-5ad0-3008-88a3-63cb423da43c | -7.51348 | -44.57103 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 21.6 |


[Clique aqui para ver as próximas entradas](README108.md)
