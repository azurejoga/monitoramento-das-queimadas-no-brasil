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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9ecbf0b4-1127-3323-89c7-5c45a4ddcc9e | 2.7357 | -60.4036 | 2025-03-23 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 3d9363ec-e38c-342d-b730-9e520ed39fc1 | 1.2945 | -60.00867 | 2025-03-23 04:44:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 350be459-3b7b-3b43-bcde-0fa25082ec30 | 2.73495 | -60.39862 | 2025-03-23 04:44:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 13.2 |
| f1c6f113-8b5d-317f-b906-03dc1a3430a9 | -8.10793 | -43.13441 | 2025-03-23 04:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 34a18fcb-5205-33b1-81ff-0b27eb56ced3 | -8.10214 | -43.13944 | 2025-03-23 04:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| dbc931fa-cf28-3046-a589-7525ba80e15b | -11.35543 | -55.12953 | 2025-03-23 04:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ed3cad3-17b3-3e88-b7a2-da32a3eefc01 | -12.77269 | -45.39998 | 2025-03-23 04:46:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4bb5a070-b224-3175-9f67-eadd9f6e3d81 | -9.66686 | -65.75359 | 2025-03-23 04:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9a101eba-2cd8-350b-b567-18b2ec27ac9c | -8.1313 | -49.47647 | 2025-03-23 04:46:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1ba59383-02fc-3103-b939-b8a75a7d7ba2 | -8.10715 | -43.14016 | 2025-03-23 04:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 59494c77-a475-3871-a808-3ed3fa699e80 | -11.35472 | -55.13371 | 2025-03-23 04:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e15e1c7c-9808-3880-adb6-ba71731eed7a | -12.77686 | -45.39751 | 2025-03-23 04:46:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a009c6aa-0f28-3073-894e-dfe09328aa2f | -8.05206 | -49.97287 | 2025-03-23 04:46:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57f3a614-1125-3741-9a37-617e48955b7e | -12.77791 | -45.39585 | 2025-03-23 04:46:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7dbcb8bb-50f1-354d-8063-2a2286d1748d | -8.10293 | -43.13367 | 2025-03-23 04:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| ae797762-a906-3285-871d-8bd06a05f6a8 | -18.54203 | -55.13771 | 2025-03-23 04:49:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 06bb8a82-f634-3d12-88c5-91652bd2f298 | -18.63706 | -54.59859 | 2025-03-23 04:49:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cca792d7-3a28-37ae-90a0-758703d47fc4 | -20.18293 | -46.7144 | 2025-03-23 04:49:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0362b21-eeed-3a4c-8237-c03c1f622ca8 | -18.6404 | -54.59918 | 2025-03-23 04:49:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a52b82cd-ead1-346a-b15e-a83369f9efec | -15.29134 | -60.20033 | 2025-03-23 04:49:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 525f1034-51c3-3c87-9af6-5cd769d910e7 | -15.56888 | -55.65027 | 2025-03-23 04:49:00 | NPP-375D | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a23c8c05-2f11-39a1-8b60-63258aa983d4 | -18.63981 | -54.60286 | 2025-03-23 04:49:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1664b19c-9d19-3550-baed-c286ebfaa7aa | -18.49538 | -55.12535 | 2025-03-23 04:49:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| af28b581-799e-3321-af7b-60d456453e64 | -18.49875 | -55.12596 | 2025-03-23 04:49:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ece5a874-c74e-3260-94c0-5f05a5e417d3 | -18.49813 | -55.12973 | 2025-03-23 04:49:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| db971356-abe5-324b-aeb9-c13540672294 | -23.26862 | -51.20673 | 2025-03-23 04:51:00 | NPP-375D | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7a73bce2-de01-3933-8da3-4f6a962cee4b | -19.4388 | -54.78814 | 2025-03-23 04:51:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e521eba-ed95-33fb-be86-4657e43b90bc | -23.2723 | -51.20731 | 2025-03-23 04:51:00 | NPP-375D | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5592ba59-0f2e-3c31-8164-5c935d869bf6 | -23.44374 | -51.85724 | 2025-03-23 04:51:00 | NPP-375D | SARANDI | PARANÁ | Brasil | 4126256 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e140da4d-6da3-3a57-99a8-e3e9ddbbc019 | -23.33819 | -46.77003 | 2025-03-23 04:51:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c5afdbb2-e8a3-316b-a893-219ce7987d74 | -23.46933 | -46.28769 | 2025-03-23 04:51:00 | NPP-375D | ITAQUAQUECETUBA | SÃO PAULO | Brasil | 3523107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 7567b900-4c59-33fb-8f58-c5775e44cee2 | -22.76473 | -47.29366 | 2025-03-23 04:51:00 | NPP-375D | NOVA ODESSA | SÃO PAULO | Brasil | 3533403 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 321b9cf9-35bb-3922-bdb4-b9ff5a3361d4 | -24.9236 | -52.2648 | 2025-03-23 04:51:00 | NPP-375D | PALMITAL | PARANÁ | Brasil | 4117800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 13c32a79-3543-3865-9aa6-12d30ca7b393 | -28.98211 | -49.44024 | 2025-03-23 04:53:00 | NPP-375D | BALNEÁRIO ARROIO DO SILVA | SANTA CATARINA | Brasil | 4201950 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| a546f035-6574-3300-b96b-11f722080aac | -30.01882 | -51.31256 | 2025-03-23 04:53:00 | NPP-375D | ELDORADO DO SUL | RIO GRANDE DO SUL | Brasil | 4306767 | 43 | 33 | nan | nan | nan | Pampa | 3.0 |
| aa827093-0434-38ac-b324-ba1eb74ef3d8 | -30.01996 | -51.31331 | 2025-03-23 04:53:00 | NPP-375D | ELDORADO DO SUL | RIO GRANDE DO SUL | Brasil | 4306767 | 43 | 33 | nan | nan | nan | Pampa | 2.7 |
| 50fecdf7-5b5d-307f-a0da-64a55e3d2778 | 1.29939 | -59.99948 | 2025-03-23 05:06:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ef21e7a-94ac-3f19-a9c7-d2ee5a50e407 | 2.73606 | -60.41092 | 2025-03-23 05:06:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.4 |
| f619c3cc-3e4b-3b3b-99e5-fc81054186b9 | 1.29861 | -59.99458 | 2025-03-23 05:06:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bb6b0292-bad5-37d1-a394-198c81fa3c2c | 2.7355 | -60.4073 | 2025-03-23 05:06:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 17.8 |
| c94be06d-ac3c-370c-9489-7161012145d1 | 1.30094 | -60.00923 | 2025-03-23 05:06:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0aa39baa-5301-3da2-8077-7172cff63ebf | 1.29736 | -60.00775 | 2025-03-23 05:06:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 932a227c-7b6c-3c2f-9585-f4aa34d94d6d | 1.30127 | -60.00721 | 2025-03-23 05:06:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9057dc7-f08c-375e-a516-cdb710da52a6 | 2.7379 | -60.39581 | 2025-03-23 05:06:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 09cd3331-78b7-3695-8894-6c02acc9c243 | 2.7438 | -60.3801 | 2025-03-23 05:06:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e2e87447-886e-3e5b-9763-7d6bcf1ddcaa | 2.73198 | -60.41156 | 2025-03-23 05:06:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 94787e8e-db04-387a-b4a5-91c0ae1ead16 | 3.24582 | -60.25996 | 2025-03-23 05:06:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 917d887a-f65a-3939-b678-ee289ceab7c3 | 2.74493 | -60.38734 | 2025-03-23 05:06:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e02f9644-a14a-3cdb-8b1b-a89f94047027 | 2.20137 | -61.35021 | 2025-03-23 05:06:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7084c69-7998-3f2a-9d57-99eae8c3d8a0 | 4.21688 | -60.13153 | 2025-03-23 05:06:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eb9de148-0cca-3a81-a4f0-f4a9a0bace51 | 3.89529 | -59.65707 | 2025-03-23 05:06:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a4ca941-286c-3ddf-b94a-650c12f15d41 | 1.90785 | -61.09946 | 2025-03-23 05:06:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f7896719-85cd-30ff-960a-42695da10f97 | 2.39808 | -60.40582 | 2025-03-23 05:06:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5de8a31a-408f-31ea-a6cc-31d8c1922bd3 | 1.30017 | -60.00438 | 2025-03-23 05:06:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ebd48e4-6cda-3ae9-9067-f794c9972a2e | 1.30052 | -60.00232 | 2025-03-23 05:06:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ff107d4b-1b31-3ecb-8c44-7c1c9cd6d055 | 2.78854 | -60.64079 | 2025-03-23 05:06:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 712c854d-8ceb-3a6a-89ad-2f2ac6592bab | 2.74844 | -60.38309 | 2025-03-23 05:06:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e7d5c25-6fb3-3d25-8d09-1ffe1cd52ee0 | 2.8276 | -60.43772 | 2025-03-23 05:06:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ff07ac8-af3a-375f-ad57-08a25c486939 | 2.58162 | -60.27219 | 2025-03-23 05:06:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 040418f2-99b0-3d2a-bcf7-2418f12e5387 | 2.73846 | -60.39943 | 2025-03-23 05:06:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7b3274fa-c731-3759-8969-26c9865e9c87 | 4.21521 | -60.12062 | 2025-03-23 05:06:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c52033ee-6de1-36c2-b2ca-92bd7bff3e22 | 1.29703 | -60.00972 | 2025-03-23 05:06:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa99d6cf-b341-3f86-964a-46bfd686334e | 2.20631 | -61.3536 | 2025-03-23 05:06:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 810a64bc-6a16-3a86-ae4d-a4319dde490a | 1.29627 | -60.00495 | 2025-03-23 05:06:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5452f0c9-2de5-3c2d-9a24-96ed2a321350 | 2.73142 | -60.40794 | 2025-03-23 05:06:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.4 |
| cebb23a1-9f43-3b44-85e2-0c8503febefd | 3.24989 | -60.25934 | 2025-03-23 05:06:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 247181fa-1fb2-3e03-ab12-55356170721f | 2.73494 | -60.40369 | 2025-03-23 05:06:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 17.8 |
| eb3312df-894f-341c-9445-8722a618c08d | 2.7351 | -60.37777 | 2025-03-23 05:06:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81ee5d76-e168-3680-8df4-8edd190ee14d | 2.73662 | -60.41454 | 2025-03-23 05:06:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 11.4 |
| b0d0e0dc-eb46-3a8d-a8c6-8052f41640cf | 2.24896 | -60.30193 | 2025-03-23 05:06:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82169d7b-d8dd-3d26-90bf-4785d2dec238 | 2.73902 | -60.40305 | 2025-03-23 05:06:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 8cd682a7-32b2-362e-acd7-2b99c5304046 | 1.29238 | -60.00551 | 2025-03-23 05:06:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17e6a484-f78c-38c8-be60-ad204f96352d | 1.90844 | -61.10339 | 2025-03-23 05:06:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1194cee-d0af-31aa-95e5-60399c917a13 | 2.73958 | -60.40667 | 2025-03-23 05:06:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 17.8 |
| 088967a2-55a8-3e41-bf33-4664a16379e2 | 2.89787 | -60.46499 | 2025-03-23 05:06:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffe30dbb-3ed8-35cb-b078-1304041779b4 | 2.73917 | -60.37712 | 2025-03-23 05:06:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.0 |
| dc79652f-f599-36f7-b20f-86895048ec1c | 2.73973 | -60.38073 | 2025-03-23 05:06:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1cb9fe18-530e-3c28-a7c8-bcc995ad6e38 | 2.38068 | -59.93156 | 2025-03-23 05:06:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99631703-18b5-3955-b7c8-3d4dab13288d | 4.21577 | -60.12428 | 2025-03-23 05:06:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 699dd065-5c6b-39bf-b73e-bbbdd8593bad | 2.39402 | -60.40642 | 2025-03-23 05:06:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c51d9cde-d6b2-3a61-a27f-3c7fdd5e8171 | -12.55996 | -57.75434 | 2025-03-23 05:10:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31448440-65d9-3044-a5e5-593c1ba7a401 | -12.55608 | -57.75739 | 2025-03-23 05:10:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2195dbc4-b244-3770-a0a8-e066145a00c7 | -9.92533 | -59.93906 | 2025-03-23 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15a8ec22-ef75-3af2-88cd-afd16775d155 | -12.55375 | -57.70567 | 2025-03-23 05:10:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6eecfc5c-dc74-395d-b416-1d75373a4422 | -11.35371 | -55.13074 | 2025-03-23 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a062eb2-4317-334a-b7c7-1d797bc23abd | -11.35733 | -55.13131 | 2025-03-23 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fdd266b6-c703-38ac-98e6-3984e90dae15 | -9.66324 | -65.75391 | 2025-03-23 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6746b387-a30e-32d0-80db-c6b1d01d9455 | -12.55941 | -57.75792 | 2025-03-23 05:10:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55105a27-6558-3769-977f-441faf29cae6 | -9.85857 | -65.26008 | 2025-03-23 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c5fd954b-1e1c-3011-9818-b47db04d4991 | -12.55662 | -57.75381 | 2025-03-23 05:10:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 151fc379-7c86-312d-aa7c-2117c7934ba3 | -9.92096 | -59.923 | 2025-03-23 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 914571c3-cc3c-327c-b13d-a63b4ad12f31 | -12.56329 | -57.75487 | 2025-03-23 05:10:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c45874b6-4cb3-383c-b45d-167cd2c7d281 | -9.92158 | -59.91928 | 2025-03-23 05:10:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78938415-da47-32fd-a917-3e4bd4d16164 | -12.93876 | -55.94286 | 2025-03-23 05:10:00 | NOAA-20 | LUCAS DO RIO VERDE | MATO GROSSO | Brasil | 5105259 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f206b012-e131-34e1-b546-ec82ec59f330 | -9.85689 | -65.26122 | 2025-03-23 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eafee6c7-90f8-3d76-8f26-05646a669a2f | -9.66204 | -65.75521 | 2025-03-23 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e299133b-7ada-3086-afe9-05806c9c0602 | -15.56825 | -55.65033 | 2025-03-23 05:10:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e23d27b4-ff45-3eaa-b5c0-c8e186f287e2 | -12.56274 | -57.75845 | 2025-03-23 05:10:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 64608e5f-0f6c-33ed-9dd9-91f4f3f0be9a | -18.49843 | -55.12373 | 2025-03-23 05:12:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 54602d28-f76e-3f5e-b103-a247b0ed0c05 | -23.26869 | -51.20894 | 2025-03-23 05:12:00 | NOAA-20 | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |


[Clique aqui para ver as próximas entradas](README4.md)
