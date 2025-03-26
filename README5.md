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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5a728e2f-a339-39b3-85e0-2dfeb71ad712 | 1.8135 | -60.8767 | 2025-03-26 04:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 49.9 |
| d207f63b-da0a-30db-802b-bcb93ab7f155 | 1.8317 | -60.8765 | 2025-03-26 04:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 1ba1e4a2-1e18-34f5-9e6c-81986a614546 | 1.8317 | -60.8954 | 2025-03-26 04:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 47.6 |
| b92c5333-38ac-3c99-b938-95d0d05c57a7 | 1.8317 | -60.8765 | 2025-03-26 04:10:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 07e87717-d360-3246-b4b2-60c89f21699b | -6.07217 | -44.23773 | 2025-03-26 04:10:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f97a842-0ad1-3c7f-9b27-adb3091f44e1 | -3.94306 | -47.99154 | 2025-03-26 04:10:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f1a6132-7cdf-3c8b-992a-3f8bbac0958c | -5.52007 | -37.62129 | 2025-03-26 04:10:00 | NOAA-20 | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e412a28b-e505-3bc4-bef6-bbbe7f3a4d6a | -6.89731 | -34.94467 | 2025-03-26 04:10:00 | NOAA-20 | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 77edeb53-674a-3338-b2a7-82077a321147 | -6.90278 | -34.94765 | 2025-03-26 04:10:00 | NOAA-20 | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 5ac17192-abd2-3e6b-9295-6fed3915e590 | -3.00812 | -48.0387 | 2025-03-26 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63cd2941-c033-306d-a085-54c27626cfc2 | -3.00748 | -48.04269 | 2025-03-26 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c53498d-d9ff-32a9-8cec-30183e404af1 | -4.81708 | -42.98624 | 2025-03-26 04:10:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2b53be2e-f433-3332-b386-4c522de6bc64 | -5.6311 | -44.31871 | 2025-03-26 04:10:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9fa66385-54a6-3743-b4ae-58787ddea0af | -6.89784 | -34.94669 | 2025-03-26 04:10:00 | NOAA-20 | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 7463f11b-d031-33c8-8be3-d6252b44e16d | -6.90224 | -34.94567 | 2025-03-26 04:10:00 | NOAA-20 | LUCENA | PARAÍBA | Brasil | 2508604 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 88606fc1-eb54-3710-a594-fa62becdb400 | -5.3956 | -46.96102 | 2025-03-26 04:10:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6f27ad1-101b-3804-b6f1-7b03377d9c43 | -3.31863 | -40.00577 | 2025-03-26 04:10:00 | NOAA-20 | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ceaab1ff-8b03-3305-89f6-77a5c2304db4 | -4.3302 | -38.01038 | 2025-03-26 04:10:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 64eb64f9-114e-3213-bc13-d70bffb44a81 | -5.99809 | -44.61205 | 2025-03-26 04:10:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fbc19a35-ceb7-3fa4-a033-41bed5fc087c | -7.062 | -44.38408 | 2025-03-26 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 12cab71e-47be-3967-b0ae-2514f9c4b223 | -7.06035 | -44.37288 | 2025-03-26 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94d6e4b0-f983-39e4-ac31-3eef3c4ccba3 | -7.05978 | -44.37642 | 2025-03-26 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f26bfde-8465-32e0-8059-c7cb320599f2 | -6.82631 | -44.39027 | 2025-03-26 04:12:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7bf73451-0394-330b-a189-1725f8c53610 | -6.56306 | -44.78415 | 2025-03-26 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d5a30b6-7aed-3147-a022-665e6c8ae43a | -8.3764 | -43.96169 | 2025-03-26 04:12:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 11571d4d-869f-3895-9688-2892adfe412e | -7.05864 | -44.38354 | 2025-03-26 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 40eed292-2d58-3844-b329-0a11133d03ff | -7.04549 | -40.40997 | 2025-03-26 04:12:00 | NOAA-20 | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 359662b6-38ed-3307-84a3-c9aab4a6429f | -8.12854 | -43.14293 | 2025-03-26 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 211b0bf7-12f2-35c3-ad52-bcfb4518faaf | -6.96356 | -43.01105 | 2025-03-26 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d7c040c6-667d-333f-886c-6c20752a4315 | -7.05921 | -44.37998 | 2025-03-26 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1fa3101-ca2e-35b3-abeb-f2a368b4669c | -6.33474 | -43.74249 | 2025-03-26 04:12:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7579e1fc-e491-37df-974f-a5291e041a21 | -6.96686 | -43.01157 | 2025-03-26 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7cf741ee-1b4c-3f19-a6ce-a1e8ac9526c8 | -6.56986 | -44.78526 | 2025-03-26 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f0738bea-6389-37ad-9393-c6c1e5234328 | -8.13184 | -43.14344 | 2025-03-26 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0f91513c-2524-316c-a547-efd5861a8221 | -7.0637 | -44.37342 | 2025-03-26 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0b6a4d7-ff9d-3780-86b2-a7b2be747a83 | -8.37971 | -43.96223 | 2025-03-26 04:12:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 862a71c2-6549-3d61-91d8-deae5bd2b86b | -8.13569 | -43.1405 | 2025-03-26 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d2b7fcb0-c30b-3b04-9dec-977c828c7ff7 | -7.06313 | -44.37696 | 2025-03-26 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18e789f6-a8c5-390f-a06d-2d85183891d2 | -6.56646 | -44.7847 | 2025-03-26 04:12:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 56473d83-cf4b-3a57-86e5-f89f95433680 | -8.39279 | -35.02336 | 2025-03-26 04:12:00 | NOAA-20 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 55c19745-dc62-3aca-9c0c-54900d4c6caa | -7.05472 | -44.38655 | 2025-03-26 04:12:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 636a4d75-16b4-3a8a-b313-d67e115f5f41 | -9.11827 | -38.16421 | 2025-03-26 04:12:00 | NOAA-20 | TACARATU | PERNAMBUCO | Brasil | 2614808 | 26 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 2f4a49ac-24d3-3e99-971c-8075f0062f77 | -8.12523 | -43.1424 | 2025-03-26 04:12:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 68701f6c-6807-33fa-9ec8-4e36ff4bf4bf | -11.51988 | -41.42002 | 2025-03-26 04:12:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1b45b77a-db09-3e59-b34e-fe935e6c10ba | -12.26149 | -42.0981 | 2025-03-26 04:12:00 | NOAA-20 | BARRA DO MENDES | BAHIA | Brasil | 2903003 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a5e7da79-eb00-3d3b-a0a4-99104f63b80f | -10.58011 | -45.13887 | 2025-03-26 04:12:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 56a55724-ca99-3d89-b7ce-bed702bdc299 | -9.15728 | -43.12431 | 2025-03-26 04:12:00 | NOAA-20 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 88ed7fed-d319-3117-a071-ad8968759501 | -12.43585 | -39.23979 | 2025-03-26 04:12:00 | NOAA-20 | SANTO ESTÊVÃO | BAHIA | Brasil | 2928802 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2ac0b11a-fb43-3024-8c8f-2bcd401ed890 | -9.12896 | -43.10883 | 2025-03-26 04:12:00 | NOAA-20 | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4f665e1b-5181-353a-87f5-5d6b6c3929bc | -9.88515 | -38.18609 | 2025-03-26 04:12:00 | NOAA-20 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 206b7fdb-258c-3fd4-9436-e92c1895d448 | -12.11535 | -38.35208 | 2025-03-26 04:12:00 | NOAA-20 | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 176f138b-5fd5-3d9c-9b2e-51566022fe0f | -10.57953 | -45.14246 | 2025-03-26 04:12:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fa70717e-768a-34f3-8420-7576e4ee0052 | -11.66945 | -38.49986 | 2025-03-26 04:12:00 | NOAA-20 | SÁTIRO DIAS | BAHIA | Brasil | 2929701 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e83f0f5f-3a1b-387c-9358-03c05839650e | -10.39815 | -37.80839 | 2025-03-26 04:12:00 | NOAA-20 | CARIRA | SERGIPE | Brasil | 2801405 | 28 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9be031c9-5b9b-370f-bbef-c15e5d18b71b | -12.11175 | -38.35283 | 2025-03-26 04:12:00 | NOAA-20 | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 64e95bde-394b-33be-b740-88356988a9a3 | -12.1255 | -39.75188 | 2025-03-26 04:12:00 | NOAA-20 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| baab2fe3-4218-3eb7-893f-6d9f7c641b18 | -18.65212 | -47.49562 | 2025-03-26 04:14:00 | NOAA-20 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7da26b91-d028-3e9c-83a3-4f9360b0dfcf | -13.39067 | -49.1246 | 2025-03-26 04:14:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea781798-2fc4-31ce-bbeb-e7ee4c08d4f2 | -19.51306 | -44.27492 | 2025-03-26 04:14:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2751549-c521-3b43-b665-56ef8779d47a | -14.1345 | -41.68999 | 2025-03-26 04:14:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8659d774-a41c-3d9b-be04-4d695e88eca8 | -15.50462 | -42.6092 | 2025-03-26 04:14:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 752cf9cb-b9fd-3513-b016-b617bb2f023e | -15.50581 | -42.60122 | 2025-03-26 04:14:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d23548c-f0ae-3560-a8c8-cb01bf86965b | -14.13272 | -41.69312 | 2025-03-26 04:14:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9497aa1c-6c0c-300f-8619-ef53c5c4ea8e | -17.00885 | -49.78189 | 2025-03-26 04:14:00 | NOAA-20 | CEZARINA | GOIÁS | Brasil | 5205455 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 951a98cd-7fef-3588-8c62-635bc668bee4 | -15.50522 | -42.60521 | 2025-03-26 04:14:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 33fb71a8-06b7-393a-b5e2-a0e813806a59 | -13.25411 | -41.33465 | 2025-03-26 04:14:00 | NOAA-20 | MUCUGÊ | BAHIA | Brasil | 2921906 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6529cf9e-ed0e-3a11-945d-e068fb0a36c3 | -17.75266 | -42.89202 | 2025-03-26 04:14:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1e90284a-eb5a-38df-ab50-61bca5278bf6 | -22.62521 | -47.21231 | 2025-03-26 04:17:00 | NOAA-20 | COSMÓPOLIS | SÃO PAULO | Brasil | 3512803 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95cecc74-8d80-3964-a8d4-9771ce1b39c6 | -19.89167 | -48.35772 | 2025-03-26 04:17:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b85cf60f-6caf-398f-9170-8fbfb39c95df | -31.04744 | -53.31677 | 2025-03-26 04:17:00 | NOAA-20 | PINHEIRO MACHADO | RIO GRANDE DO SUL | Brasil | 4314506 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 2bad293e-e3eb-3812-bee2-4fd24d439d90 | -22.90595 | -46.52946 | 2025-03-26 04:17:00 | NOAA-20 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c481133e-362d-3f1c-8363-7649e9c95f30 | -19.89235 | -48.35371 | 2025-03-26 04:17:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f627ddf4-544e-3b00-96ae-396da0b43f46 | -23.79482 | -46.68629 | 2025-03-26 04:17:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 25bd4aa4-16b5-3e32-afbf-edbfcd5b5b4f | -20.3754 | -45.60211 | 2025-03-26 04:17:00 | NOAA-20 | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56288777-4a43-3e18-ae0a-eb5eccdf653b | -23.33685 | -46.77116 | 2025-03-26 04:17:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 808d9c0b-66db-3562-b370-c0c29a1fa1af | -21.13095 | -47.80022 | 2025-03-26 04:17:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 648640af-0936-3391-927b-f264f65686ff | -23.08546 | -45.57718 | 2025-03-26 04:17:00 | NOAA-20 | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c4a22c88-2198-36da-a926-dc2b054d2989 | -22.78591 | -43.75782 | 2025-03-26 04:17:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a2cde8f7-42d0-3f68-97c4-8c777d811570 | -20.76262 | -46.76772 | 2025-03-26 04:17:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 66bd005c-6019-3872-b31d-8aa8bd6a1479 | -20.29084 | -50.01747 | 2025-03-26 04:17:00 | NOAA-20 | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9cd862d4-5e8b-3e3e-85ee-1058cc6eab46 | -20.98278 | -43.03267 | 2025-03-26 04:17:00 | NOAA-20 | DIVINÉSIA | MINAS GERAIS | Brasil | 3121902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| acd3b6b6-4b77-38ab-83fc-606e90a8490a | -21.19473 | -44.93635 | 2025-03-26 04:17:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 37d3d57f-ef41-36b2-99d3-1c1b27e063ea | -20.29247 | -50.00824 | 2025-03-26 04:17:00 | NOAA-20 | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b054c4f3-ad10-3dbc-8287-3db6586c30be | -20.47164 | -47.49343 | 2025-03-26 04:17:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 24407a16-30ba-3ef8-972f-e2f2820b6571 | -20.29165 | -50.01283 | 2025-03-26 04:17:00 | NOAA-20 | PARISI | SÃO PAULO | Brasil | 3536257 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| cf64e8aa-3c76-3b22-bcd6-1ffb782635b4 | -20.47226 | -47.48969 | 2025-03-26 04:17:00 | NOAA-20 | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27bd8142-ffa9-3991-8ffd-23f55b3f56e3 | -29.46601 | -49.83306 | 2025-03-26 04:19:00 | NOAA-20 | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 3.3 |
| 0dbc61c5-1809-3c19-b13a-cb6d51d84448 | -29.46936 | -49.83379 | 2025-03-26 04:19:00 | NOAA-20 | ARROIO DO SAL | RIO GRANDE DO SUL | Brasil | 4301057 | 43 | 33 | nan | nan | nan | Pampa | 3.3 |
| bfe8b688-689c-3283-a735-f7846a3e3096 | 1.8317 | -60.8765 | 2025-03-26 04:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 53.6 |
| adfc69ed-4250-382e-8799-7429bd691202 | 1.8135 | -60.8767 | 2025-03-26 04:30:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 4e86642e-d9e0-30c5-be2d-4d81cc72c8af | 1.8317 | -60.8765 | 2025-03-26 04:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.7 |
| a55a9e85-09fb-39b1-9257-097b1f4dc287 | 1.8135 | -60.8767 | 2025-03-26 04:40:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 77dbea40-0678-334b-8878-87ecdd03ff8a | 2.18045 | -61.25918 | 2025-03-26 05:01:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8712798-4894-37d3-a74f-a4c1f83e064b | 2.1742 | -61.82206 | 2025-03-26 05:01:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82f681dd-210d-3927-b900-52cd9fc47ce8 | 2.19887 | -61.80564 | 2025-03-26 05:01:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af7848af-a9bc-3196-824e-74ea976391a6 | 4.67201 | -60.90618 | 2025-03-26 05:01:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36bf8c7d-27b9-3514-9720-9a50b47cff68 | 3.97231 | -61.55756 | 2025-03-26 05:01:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86bdab29-735d-3cb6-994b-1d85a7e0e4b2 | 2.17092 | -61.82077 | 2025-03-26 05:01:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54343a29-e465-3156-bce2-88f32330cac5 | 2.19475 | -61.81176 | 2025-03-26 05:01:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a15c09d3-2f50-3964-b502-d079d0eafad7 | 2.10939 | -61.82602 | 2025-03-26 05:01:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |


[Clique aqui para ver as próximas entradas](README6.md)
