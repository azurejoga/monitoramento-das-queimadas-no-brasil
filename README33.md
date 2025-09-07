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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bdcc0494-0b02-3061-b28e-f8e176b067b4 | -10.74601 | -48.18269 | 2025-09-07 03:57:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 802360eb-8b3c-3e43-b805-b096e77ee41b | -8.4413 | -47.3067 | 2025-09-07 03:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c83e8234-df29-3036-878c-5320195f9356 | -7.01837 | -44.97371 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 75500f31-57f5-3d30-bb40-ccf04afa6d62 | -13.18849 | -44.48491 | 2025-09-07 03:57:00 | NPP-375D | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54d6a5bc-f94d-377a-a425-69eda9cb06d6 | -13.01198 | -45.22405 | 2025-09-07 03:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 47841b92-efbb-3559-aaed-9d1304443a6c | -5.69234 | -48.13808 | 2025-09-07 03:57:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 310ad869-aebf-3659-92fe-9cfde8c7de10 | -7.74641 | -48.83182 | 2025-09-07 03:57:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c6fd6006-ec9f-349c-915c-ac8198a3b613 | -6.22872 | -43.57029 | 2025-09-07 03:57:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c80a547-2852-392e-b278-66ff853f2e02 | -7.86523 | -47.87238 | 2025-09-07 03:57:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 50c5c675-09fd-3775-aba9-ba7a00f13db4 | -11.59712 | -47.16886 | 2025-09-07 03:57:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| c4fda885-cbc8-3cee-b49e-cc9bc3156a8a | -11.41101 | -43.60899 | 2025-09-07 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1af41631-17be-3f4b-8637-f65bee95ba5e | -6.79823 | -47.07207 | 2025-09-07 03:57:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8afc1457-abdf-30af-8c04-a050bb8a5a5a | -13.39876 | -42.41372 | 2025-09-07 03:57:00 | NPP-375D | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 14a02c01-6b98-3016-8d5a-0fcc7378ee53 | -11.14388 | -48.3923 | 2025-09-07 03:57:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7185392-46c4-3d3a-a2ca-bd55fe175dbb | -8.91904 | -45.81305 | 2025-09-07 03:57:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f01e6d91-7c15-36f5-81e0-e20ec08bd54f | -11.40308 | -43.63217 | 2025-09-07 03:57:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8c150865-ead2-37e0-8a6b-fe51bf281957 | -7.25436 | -41.88879 | 2025-09-07 03:57:00 | NPP-375D | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7abe40f2-b9c9-39ef-b6f4-ea3631eca1db | -9.98555 | -51.6639 | 2025-09-07 03:57:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4c5db40f-ee89-3f22-97d4-a003e121bed8 | -5.69048 | -48.13489 | 2025-09-07 03:57:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 616a8870-221b-3dce-b811-89de6a581c78 | -6.1967 | -43.36749 | 2025-09-07 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0467f29d-8203-3c1d-8db1-99ac7414fea8 | -9.8405 | -46.54882 | 2025-09-07 03:57:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1473219b-1c21-3037-a2f2-dfd40fe158cd | -7.81815 | -45.42893 | 2025-09-07 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| af531d18-df75-3f06-984d-737ab738874d | -7.01178 | -44.94271 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e03d5608-1a01-3f6d-95b0-5b016943cb1c | -5.86696 | -46.10074 | 2025-09-07 03:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 16f80811-2d4a-35b4-93f3-c2cf2f4ed519 | -6.80064 | -50.84329 | 2025-09-07 03:57:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7674004e-412f-3581-9adc-2bd45e2a47d5 | -5.94144 | -46.17326 | 2025-09-07 03:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84f71067-91e1-3679-a1b8-0b0486fd7341 | -8.30174 | -44.98285 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50be73e8-a473-3220-8489-f7630785b9e7 | -6.19809 | -43.37814 | 2025-09-07 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f6224858-94e2-3924-98ed-dceaba5213e6 | -8.15063 | -44.86879 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 811d815c-822d-3773-92b2-e204a866c4b7 | -7.60923 | -44.66507 | 2025-09-07 03:57:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c588cc20-da16-3637-a983-ffad758bd765 | -11.57817 | -47.76033 | 2025-09-07 03:57:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7be61ce7-b18b-3fba-8e48-fcedd9185e5e | -8.11844 | -45.31839 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d06dcf7d-bee3-392a-b9bb-98433e6f7b95 | -6.20337 | -43.37177 | 2025-09-07 03:57:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 07d0a852-2505-3d84-aac3-fc84afe9f5f3 | -7.75356 | -48.82513 | 2025-09-07 03:57:00 | NPP-375D | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f6e8a692-b313-305c-90cf-05dfda32c651 | -6.52755 | -42.93048 | 2025-09-07 03:57:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e28f401-e0aa-3af9-92ac-88da032a0aed | -7.01915 | -44.95309 | 2025-09-07 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed44145e-1039-323b-a4b1-aa99b3840fdf | -5.68981 | -48.13875 | 2025-09-07 03:57:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 2ed36171-62cd-37cb-acdb-f8675b1c90f8 | -8.43824 | -45.02797 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6514f527-6343-3bb3-b650-a02e012f1a22 | -8.01761 | -45.49559 | 2025-09-07 03:57:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| aa6aa58a-b7d6-3ccf-bd86-98079f083420 | -12.81443 | -48.02048 | 2025-09-07 03:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 704a55c1-05fd-354a-8849-0bcaebe1964b | -8.48426 | -45.18135 | 2025-09-07 03:57:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7b2608fa-4c85-3602-97dc-bbd2cb1e9c85 | -12.9289 | -54.7744 | 2025-09-07 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 208.2 |
| a6e8e871-0288-3bec-b3bc-72b22570f771 | -19.8853 | -57.9031 | 2025-09-07 04:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.9 |
| 84aa1705-5a4e-3c34-ab4f-da684a16fdd1 | -19.8857 | -57.8823 | 2025-09-07 04:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.4 |
| 629e76ff-ed72-3fab-810b-4614127a1c65 | -12.948 | -54.7724 | 2025-09-07 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 394.0 |
| bcba1fba-51fd-3fa3-bf32-97701f48fff0 | -3.5995 | -47.5142 | 2025-09-07 04:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| b422447f-8a12-309c-beaa-ee37af74e0f0 | -12.9482 | -54.7519 | 2025-09-07 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 120.1 |
| 03eeae44-3729-3542-99a2-4cee9a5bd371 | -12.9286 | -54.7949 | 2025-09-07 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 50a263ec-e4af-3c33-87be-d2a107ff33b1 | -12.9477 | -54.793 | 2025-09-07 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 111.6 |
| 680a6a60-d5e0-3f42-9df2-c9d475013ee7 | -19.8656 | -57.885 | 2025-09-07 04:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.2 |
| 388a2c2d-8718-3c73-a2f8-01fccd06c1d9 | -19.8652 | -57.9058 | 2025-09-07 04:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 68.4 |
| b6e42c6e-1009-3e9b-b4ec-770a247ff952 | -12.9292 | -54.7538 | 2025-09-07 04:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 95786024-c00f-3872-aecb-e4604e19eb20 | -17.68147 | -43.53848 | 2025-09-07 04:00:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 679fe351-8c05-3b58-b002-a82805cdeb26 | -18.5477 | -43.82202 | 2025-09-07 04:00:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7bd595b0-f6f5-3cd5-99ef-e5db02f8bd0d | -18.39002 | -41.01606 | 2025-09-07 04:00:00 | NPP-375D | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| dbe36da0-bd9d-34c5-b1a1-a2b6fe779b53 | -19.46975 | -47.75978 | 2025-09-07 04:00:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| db7b0328-e570-3fb0-9f87-b93feb3b2142 | -13.90233 | -53.99627 | 2025-09-07 04:00:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7c7c4e5b-1337-31c8-87ff-c24f54222ff7 | -13.7262 | -46.90611 | 2025-09-07 04:00:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1efaff88-5b66-3fdc-836b-3acf750f08c5 | -15.83546 | -52.27672 | 2025-09-07 04:00:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c36b8b36-395b-3c5d-95e0-d9ffe3a7f8ff | -17.22737 | -46.71557 | 2025-09-07 04:00:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7cfd932-25c1-3e15-8694-cb3b41bab6b0 | -17.69205 | -43.51918 | 2025-09-07 04:00:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a73eacbd-abb9-3873-a1ad-ae9f49972a2c | -18.69343 | -44.45009 | 2025-09-07 04:00:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa701b54-d326-3c5e-9e8e-28607c709e78 | -19.89263 | -41.434 | 2025-09-07 04:00:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1697aefe-5a92-363a-a0cc-2944c00227e1 | -19.48432 | -47.75399 | 2025-09-07 04:00:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 63c37c1c-7b48-38f5-ab7a-1cf1f9c43fd3 | -18.2359 | -42.66351 | 2025-09-07 04:00:00 | NPP-375D | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d0c2797d-ffbd-3b99-83d9-003cfa8f6a91 | -19.47235 | -47.76965 | 2025-09-07 04:00:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| be057290-366b-39af-9b25-6a9b369afa35 | -18.35665 | -43.92044 | 2025-09-07 04:00:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7dcb2062-8890-32a5-8f4c-0def1c66a080 | -13.9108 | -53.99107 | 2025-09-07 04:00:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 94df6b19-2cb0-326d-96fe-681593060df7 | -15.33798 | -52.74439 | 2025-09-07 04:00:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a452df90-9429-3531-9883-6929ae059400 | -13.93722 | -54.02581 | 2025-09-07 04:00:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f8d45453-423d-370e-8dfc-f6cd39b6bf88 | -15.53677 | -42.65456 | 2025-09-07 04:00:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| aff3c665-bea8-3ee9-909f-0c262915d6a6 | -15.53034 | -42.62935 | 2025-09-07 04:00:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d4ec8145-2be8-3548-9892-ccf84b56347b | -12.81815 | -52.94946 | 2025-09-07 04:00:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 72b1c6c8-d1fe-3a98-89e5-86c7c99f420a | -14.77852 | -48.12019 | 2025-09-07 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cc2a11b3-c3ec-3bbd-b22b-ef4b6d53f8b5 | -18.3609 | -43.91703 | 2025-09-07 04:00:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f54a2dfb-1c4c-3cf7-a07c-aeec53c91582 | -16.08605 | -41.81454 | 2025-09-07 04:00:00 | NPP-375D | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 82b6d827-af0b-35fa-92e4-c82e9a37f1c6 | -17.10367 | -49.89361 | 2025-09-07 04:00:00 | NPP-375D | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3de2b9b-f685-3666-8766-cd4264cc0140 | -13.90092 | -54.00263 | 2025-09-07 04:00:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f836724-9214-389b-8347-79361eeaa457 | -13.71519 | -46.88982 | 2025-09-07 04:00:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 35a4f71b-ad55-31d4-ac09-1937c0d1bae1 | -15.88345 | -52.20119 | 2025-09-07 04:00:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c59dd79f-ce59-340e-9a8d-f1cedfd7f524 | -19.48265 | -47.76274 | 2025-09-07 04:00:00 | NPP-375D | NOVA PONTE | MINAS GERAIS | Brasil | 3145000 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6994ee74-bbc1-312b-aeff-6506de663d94 | -14.56547 | -43.72811 | 2025-09-07 04:00:00 | NPP-375D | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d5694a7-664c-3ab1-b360-fb258c25124b | -16.33255 | -52.94846 | 2025-09-07 04:00:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8df7c8b4-53ee-3c6f-93e3-41d40acce078 | -17.10435 | -49.89036 | 2025-09-07 04:00:00 | NPP-375D | INDIARA | GOIÁS | Brasil | 5209952 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1c42bd52-0c8f-33fa-81e3-38cb32e19432 | -15.88369 | -52.19843 | 2025-09-07 04:00:00 | NPP-375D | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7589568f-e05f-32d5-8973-fd8e36b8d7b8 | -17.37918 | -49.23731 | 2025-09-07 04:00:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d7241b5a-1f6f-301c-b386-58d7e2d94d6d | -16.82125 | -49.18643 | 2025-09-07 04:00:00 | NPP-375D | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff22cc91-3a48-3a88-93b9-e63d5c91f5b4 | -17.70267 | -44.48355 | 2025-09-07 04:00:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5910387e-94e1-3cc4-af15-cdbff3545741 | -17.67021 | -43.54066 | 2025-09-07 04:00:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6436b127-9011-3937-a850-33913a829bca | -19.11075 | -46.69553 | 2025-09-07 04:00:00 | NPP-375D | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 617499b9-7ce3-386f-b461-ab24dd02b817 | -18.02946 | -47.08797 | 2025-09-07 04:00:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 04af04cf-e4cf-3f24-8fce-5f1968e5fb24 | -15.73025 | -47.02637 | 2025-09-07 04:00:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 85c6d94a-fa6b-3ac0-9af7-ecb536e45675 | -14.84871 | -46.69547 | 2025-09-07 04:00:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6ebec1c8-4aeb-31f6-80ed-c7b7b83a42f1 | -14.96975 | -47.59364 | 2025-09-07 04:00:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f62b9eb6-4a11-39fa-9ee7-be39abcc6d84 | -15.33175 | -52.74244 | 2025-09-07 04:00:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ca80c7d3-97e7-3dc9-850c-b85aa9ad2bc2 | -17.52937 | -42.58215 | 2025-09-07 04:00:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 46ac916a-b4a5-3fe0-bac6-30b54112ab06 | -13.91174 | -54.02003 | 2025-09-07 04:00:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f60b79f3-0231-340e-a67f-574838ab0064 | -12.78071 | -52.96067 | 2025-09-07 04:00:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8326e5a9-c328-357c-900d-e65bea4d0060 | -15.01288 | -48.00541 | 2025-09-07 04:00:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c7d3c4c5-dec3-3605-acce-c1e500e175da | -14.79611 | -48.26244 | 2025-09-07 04:00:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README34.md)
