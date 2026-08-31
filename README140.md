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

## Dados Diários - Página 140

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc69cff1-18b1-33a1-9a41-cbf056c43af1 | -19.48213 | -57.55255 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 20.8 |
| 69b98add-2436-37fa-9ac7-a5b778c031c0 | -15.23976 | -56.39149 | 2026-08-31 16:48:00 | NOAA-20 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 84646e40-1405-326f-916f-bf5242f4396b | -17.77587 | -45.38882 | 2026-08-31 16:48:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2ac2a33e-9657-367f-865c-28ddbd2fb354 | -15.88715 | -56.47549 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 7ef9e869-a6bc-3e03-a348-465ae91a516d | -15.21474 | -56.36041 | 2026-08-31 16:48:00 | NOAA-20 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 6b7c3f32-0f14-3a93-9753-b793f2af604b | -19.21558 | -57.33744 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.6 |
| 5d3ae92b-0cd4-3831-b45e-fdfe0783e714 | -14.39986 | -53.27332 | 2026-08-31 16:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 61b990b3-9f80-39bc-8e32-140b1ac81ec4 | -14.98922 | -48.12983 | 2026-08-31 16:48:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 10c99880-a248-32c7-a14b-950bfd6546f3 | -15.64931 | -40.9577 | 2026-08-31 16:48:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 77dc2b3b-0db8-31da-b35f-7b18db74c11c | -14.23216 | -51.94149 | 2026-08-31 16:48:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 35.8 |
| d1381d8a-1431-3ef3-a293-ffd7f2397280 | -14.79507 | -48.26048 | 2026-08-31 16:48:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 66ecd52d-9e82-3115-b4fd-8cc0da4f4376 | -17.89381 | -52.08885 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 7928035b-7ef3-3d36-ac92-647f7ad3d0a5 | -19.13265 | -57.38862 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 35.9 |
| a72742e0-a7cf-3e0e-8589-67d18e9eb26a | -15.61351 | -56.39357 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e7592386-204b-3165-b513-9cd0c43987b1 | -19.13223 | -57.38407 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 35.9 |
| e4d02ef1-f364-3b5d-bfb4-f9059fe7d2d7 | -17.45362 | -52.41111 | 2026-08-31 16:48:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 5bb916ba-2579-305b-9323-20361db58333 | -14.94372 | -41.02503 | 2026-08-31 16:48:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| c144312d-c56c-3ecc-a13e-1165f6c5a3da | -19.11006 | -57.40474 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 28.4 |
| fd8d919d-a4c2-3308-bcae-3fff5d5ac3a3 | -15.96826 | -55.95931 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 9.2 |
| b0a9020a-ff29-31c1-a240-75c7eff4a7db | -19.21681 | -57.351 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.4 |
| 9a990298-e1a6-335d-9aac-11a6602332a2 | -14.06596 | -42.53403 | 2026-08-31 16:48:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 5bb2cf07-3e4c-3dd4-81bf-49a624f9be80 | -19.22911 | -57.35429 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.0 |
| e9360e9b-70d8-389b-bd18-55646a030ed4 | -19.19467 | -57.34567 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 59.0 |
| df41f934-d25c-3a20-a473-abb152931685 | -15.28228 | -42.25722 | 2026-08-31 16:48:00 | NOAA-20 | VARGEM GRANDE DO RIO PARDO | MINAS GERAIS | Brasil | 3170651 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.8 |
| bbd8c099-4001-36b1-888d-c578544c7924 | -17.87506 | -52.10706 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 187.2 |
| 5d992a9b-f2b9-3259-8821-5df0468cb9dd | -14.97956 | -48.15031 | 2026-08-31 16:48:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 38a7e336-80be-3123-b9fc-213055c6a127 | -17.93761 | -42.80149 | 2026-08-31 16:48:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 4f28863a-d6a8-311a-b643-e8523d77c67e | -16.70765 | -49.34795 | 2026-08-31 16:48:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 09d1f58e-3abf-3963-acdb-299be3b8872c | -14.96283 | -54.56387 | 2026-08-31 16:48:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 97038d7d-2ec8-3a25-bd5c-ad7b25710fd4 | -12.6378 | -39.11849 | 2026-08-31 16:48:00 | NOAA-20 | MURITIBA | BAHIA | Brasil | 2922300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4475b5d9-c4b0-3cf8-889d-a676946906f3 | -16.48366 | -42.30397 | 2026-08-31 16:48:00 | NOAA-20 | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| c7b39d5f-234c-352d-ae74-aa66eee1b82e | -19.11057 | -57.37985 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 140.7 |
| 44ea91d7-8653-383e-9c86-b3fcb21e529a | -17.8695 | -50.49684 | 2026-08-31 16:48:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 83.8 |
| 6ee3aa16-04d7-346b-bd3a-447f59aa2d5d | -19.14966 | -57.37772 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.2 |
| aa197f10-ac61-3d31-9a73-fee93e6e8fe8 | -14.73451 | -47.15623 | 2026-08-31 16:48:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| c45873d9-573b-34d8-bafb-20b989696ebb | -14.95055 | -54.5801 | 2026-08-31 16:48:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 5be0960c-336d-3700-a18a-44f93b636add | -16.56345 | -52.50507 | 2026-08-31 16:48:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9e2d1ff0-6737-33a1-ab08-a6c9df35e67a | -17.71793 | -49.22662 | 2026-08-31 16:48:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 8f74a487-0891-38d0-a2af-31ea899759bb | -18.69302 | -48.22804 | 2026-08-31 16:48:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 09f6b22e-1770-38c4-a1b2-eef07e930e8f | -14.67055 | -53.55492 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| e664f143-50e2-303b-b584-adeeddd15241 | -18.51382 | -48.3429 | 2026-08-31 16:48:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dfe96d27-b85a-3716-8195-3139816e6e08 | -20.26336 | -58.1421 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 17.3 |
| cb85a986-d4fc-3b16-b951-a01dc5a13c2b | -19.15364 | -45.4941 | 2026-08-31 16:48:00 | NOAA-20 | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 661e95ae-cfd5-3cf8-83b7-d4f5343edeb0 | -17.88139 | -52.0905 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 8ab30e36-2f91-312e-9d6e-61856cd4fa30 | -15.61201 | -41.522 | 2026-08-31 16:48:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 0b1b7f49-b88f-3b5e-a4de-286c020706a5 | -19.1777 | -57.35651 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 24.5 |
| 187ac890-ed38-3ae3-ad0c-dc0409d88298 | -19.1174 | -57.38828 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.8 |
| ff889631-f139-37da-95dd-a7af8c82ac8f | -15.98429 | -55.96067 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 33.8 |
| f2d80f8f-3642-3c5c-a2a9-6b07433386e9 | -17.87655 | -52.11891 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| f0da5b6b-e5f2-3649-b1b0-2c5d669702e4 | -14.65802 | -53.56116 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5d9efe75-2463-327a-9f04-b6b1e17a2c50 | -14.9394 | -41.02554 | 2026-08-31 16:48:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 4e25ea6d-e016-317e-9d72-7db3647e8374 | -16.56908 | -52.51633 | 2026-08-31 16:48:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 19.5 |
| d7527264-f0c7-3f26-afaa-5109f16c8549 | -15.40669 | -52.70739 | 2026-08-31 16:48:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6965c2e7-ae4e-3eb4-ba4e-95d113863bc7 | -15.39395 | -52.68625 | 2026-08-31 16:48:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 9.2 |
| dcc65ea5-9060-3b2d-923e-bd5624a328bc | -19.18027 | -57.38371 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 29.6 |
| 20f5f5b5-e185-3326-b803-6d18a28514e5 | -19.22787 | -57.34071 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 120.8 |
| 7f849c11-631e-306f-a46a-455a420da9ae | -15.03941 | -48.09979 | 2026-08-31 16:48:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| abf832bb-f3c2-3c8f-a968-2d25465837f4 | -15.18713 | -48.2256 | 2026-08-31 16:48:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 41.7 |
| d498b9b1-de15-3e34-918b-dbed4f97350a | -17.8557 | -50.50834 | 2026-08-31 16:48:00 | NOAA-20 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 35526d53-24f4-31b2-92a5-755289e07d78 | -16.85737 | -49.59529 | 2026-08-31 16:48:00 | NOAA-20 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 19bc9ff0-aaeb-32b5-a5de-c1dec4fc0b43 | -14.59483 | -53.08846 | 2026-08-31 16:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 34a25459-08c9-3b18-beeb-8e19820247de | -16.39983 | -40.91744 | 2026-08-31 16:48:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 178cb520-ac22-3fbe-86c7-c585679dfd45 | -19.11992 | -57.38078 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.0 |
| a785f14e-1e80-3c32-9338-9b33c4e7f154 | -18.41261 | -47.95397 | 2026-08-31 16:48:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 51.2 |
| ed8f893c-05a1-38aa-8b07-b00f47a94a9c | -15.66801 | -45.91166 | 2026-08-31 16:48:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b136ab04-19a4-32e8-afb9-2904d180730b | -17.86114 | -52.0969 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 9cae0e77-06cd-3966-a4c5-0ed1bdb822dd | -16.29991 | -44.97496 | 2026-08-31 16:48:00 | NOAA-20 | ICARAÍ DE MINAS | MINAS GERAIS | Brasil | 3130051 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 96930e3d-9d21-34d3-b4da-f73515535aa7 | -15.88753 | -56.47896 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 804d1632-4faf-33a6-9a60-3956e9301c0c | -18.11878 | -51.61669 | 2026-08-31 16:48:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| de9bd811-7137-31d3-a8c6-15df44d94493 | -18.26502 | -40.54687 | 2026-08-31 16:48:00 | NOAA-20 | PONTO BELO | ESPÍRITO SANTO | Brasil | 3204252 | 32 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| f5df3906-5956-39db-b13c-29314dd16efc | -15.64223 | -56.37897 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| eeb42b68-4c72-37b4-86b6-80447db7c4aa | -14.21374 | -48.63774 | 2026-08-31 16:48:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9e42e4f4-2dc0-3c62-a5d8-a07a617c7023 | -19.16581 | -57.35777 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 32.1 |
| a3f8ec9e-89db-3846-b7b7-f933821dbe41 | -19.16836 | -57.38494 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.8 |
| c5768184-aea5-3f37-b566-a81f56d232fd | -15.66358 | -56.37615 | 2026-08-31 16:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 563a7fa3-1532-3f15-8f4a-c064bc0f3eb5 | -15.7347 | -56.10607 | 2026-08-31 16:48:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 15.7 |
| 811f15f1-2721-3cea-b633-a00f639a7fc5 | -14.66619 | -53.5555 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f9a2e3aa-da1e-370a-b491-0f036cf26a2a | -16.38146 | -45.10878 | 2026-08-31 16:48:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| f70dfb3f-9855-3d7e-81b7-dba7e95c9917 | -19.18795 | -57.4013 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 38.4 |
| cb7921f2-35ae-3066-a6f8-eb1f41acaa46 | -18.2641 | -52.71648 | 2026-08-31 16:48:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 40.2 |
| 7c968866-bff5-34f6-96d1-fbfa7dd1b71a | -18.27773 | -52.68406 | 2026-08-31 16:48:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 76c88235-0a68-3252-a0f3-801f5dd5f735 | -19.16624 | -57.36229 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 42.0 |
| 173f1586-0878-306a-8204-f41a5d170144 | -14.42223 | -53.15109 | 2026-08-31 16:48:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 8bd6eb37-5b62-3544-8905-b5c5cbbde87e | -19.21931 | -57.3523 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 26.1 |
| afad4bce-80cf-3274-af0e-a2da8706021b | -17.7951 | -39.70477 | 2026-08-31 16:48:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 9ffbbc92-2d19-32d1-afc7-ef29f5e4eea9 | -14.9091 | -46.90107 | 2026-08-31 16:48:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| edca1c2c-d2f3-3343-b661-a8748d3fa53e | -15.19103 | -48.22873 | 2026-08-31 16:48:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 32.9 |
| f56f0e73-a93d-35a6-a8b9-93b5e2ce3e4a | -16.6944 | -49.90156 | 2026-08-31 16:48:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 50.1 |
| cc84aee9-509c-3b23-9d38-051e76816dc6 | -16.97957 | -53.28858 | 2026-08-31 16:48:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| d5094bdd-25d9-3c22-8946-70a17ed3c836 | -15.98914 | -55.95679 | 2026-08-31 16:48:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 26.8 |
| bd4041aa-6b84-3364-b72f-32d9be3587b0 | -17.82997 | -42.06822 | 2026-08-31 16:48:00 | NOAA-20 | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 70.8 |
| 9868bba2-85a6-396a-8148-bf011826afaf | -19.2334 | -57.33556 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 83.2 |
| 67125f4d-694a-31a2-a01e-b2886fa966c2 | -17.86587 | -44.25476 | 2026-08-31 16:48:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 23317568-d988-3e55-824d-ab8974ff2394 | -15.99998 | -43.54547 | 2026-08-31 16:48:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 18d0b1b9-9137-3bd9-83cf-0bd66fcba929 | -19.11868 | -57.36718 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 134.9 |
| 6bd00f37-5751-350e-b327-63451418f68e | -19.10638 | -57.39857 | 2026-08-31 16:48:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 33.0 |
| 6ea656d2-131d-379c-96a9-2ebde26bfb1e | -14.56155 | -52.07869 | 2026-08-31 16:48:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d4377b1f-4197-399e-ad5d-bc53bdafc086 | -17.00113 | -51.84215 | 2026-08-31 16:48:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f77341e3-7b6f-3e85-8d7d-6a2d703f19af | -15.67986 | -45.94327 | 2026-08-31 16:48:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7bddc43c-c791-3a65-ac26-cb7a2a117171 | -14.94993 | -54.57513 | 2026-08-31 16:48:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 8.4 |


[Clique aqui para ver as próximas entradas](README141.md)
