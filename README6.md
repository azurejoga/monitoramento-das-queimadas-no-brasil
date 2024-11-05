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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d111eb0f-51cf-3713-a2aa-a84a410b3e32 | -4.0608 | -46.929699 | 2024-11-05 00:20:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2cb8fcbb-e88e-3403-b8d5-727f1568048e | -3.6102 | -39.234299 | 2024-11-05 00:20:00 | METOP-B | SÃO LUÍS DO CURU | CEARÁ | Brasil | 2312601 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1f7f6c79-7296-39a7-9415-4c3de405d1bc | -5.2211 | -47.461899 | 2024-11-05 00:20:00 | METOP-B | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2304c833-d14b-3540-b696-dc132d1bde7b | -5.2181 | -46.715 | 2024-11-05 00:20:00 | METOP-B | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 98f47d95-478b-36c6-b02d-058cbc25fe24 | -10.6915 | -44.8461 | 2024-11-05 00:20:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8df404c4-8e32-37c5-a5ee-46c25c977206 | -9.797 | -43.862301 | 2024-11-05 00:20:00 | METOP-B | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 91c208e8-c115-3152-9b2c-5bf23bc903db | -4.74 | -46.742699 | 2024-11-05 00:20:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a55e934a-c520-3faa-99aa-f51bda50fabf | -3.7796 | -46.051201 | 2024-11-05 00:20:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 06db8639-9af9-399d-bc8d-3f39c348bf6a | -2.9038 | -49.391499 | 2024-11-05 00:20:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3902da0b-7201-3dda-8005-bcb006de679c | -15.5506 | -43.169399 | 2024-11-05 00:20:00 | METOP-B | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 9d54cbb3-50ed-35f2-9a7b-1a4e50a719eb | -2.3042 | -49.655602 | 2024-11-05 00:20:00 | METOP-B | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88ce9613-d6db-3888-8b7f-b14689682a88 | -4.6128 | -46.864201 | 2024-11-05 00:20:00 | METOP-B | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b54a19e1-4b7c-3df1-80b0-f3286a724ec9 | -5.2226 | -47.4688 | 2024-11-05 00:20:00 | METOP-B | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dfb17197-17a2-3fb8-a862-804312b083f7 | -10.1298 | -36.386398 | 2024-11-05 00:20:00 | METOP-B | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| fc4f2177-abcd-3815-8cf9-31156f9fdb8a | -9.7872 | -43.864601 | 2024-11-05 00:20:00 | METOP-B | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7dd396b5-96da-3b37-8971-213c62797134 | -2.4719 | -50.221199 | 2024-11-05 00:20:00 | METOP-B | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ddad5cc-c6b3-3954-842f-1181bd64c2ec | -3.9651 | -48.1534 | 2024-11-05 00:20:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65d40f2c-9ce4-3dab-89da-33fa11466326 | -5.2365 | -46.112202 | 2024-11-05 00:20:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8edd376b-dafa-3f9b-a96b-9f81d1f0c06e | -4.0698 | -48.298901 | 2024-11-05 00:20:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 424c0bb9-079c-3982-841a-e363060acf82 | -6.0975 | -43.967098 | 2024-11-05 00:20:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7bf4bf3f-1760-3539-afef-13af3dbee902 | -4.746 | -45.8125 | 2024-11-05 00:20:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5f85d76b-14bd-3239-8b7c-60c5b4d42959 | -2.9486 | -45.478298 | 2024-11-05 00:20:00 | METOP-B | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1960f07d-d33b-373d-accf-a6e5ecfa8050 | -4.0941 | -48.315601 | 2024-11-05 00:20:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1057e474-c24b-30f2-8407-a874e6a72c63 | -1.6103 | -47.259102 | 2024-11-05 00:20:00 | METOP-B | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| baa7cc92-793f-34ce-98cc-f8ebe322c653 | -3.4623 | -45.516399 | 2024-11-05 00:20:00 | METOP-B | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6a747665-8320-36cc-bd15-fb1c9a9ceacd | -10.6854 | -44.773499 | 2024-11-05 00:20:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 61759805-1a68-3e8e-b7e4-8abea86ca435 | -11.1838 | -44.6068 | 2024-11-05 00:20:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 879b41e7-9289-32a7-addd-cabca7d23e0f | -6.1054 | -43.957001 | 2024-11-05 00:20:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7b36e7fe-fa8e-3d55-a908-d2f20a1dd14d | -2.818 | -52.930099 | 2024-11-05 00:20:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19e39da1-ba9e-3a4f-8fff-72bb3ed9ed92 | -2.9022 | -49.384102 | 2024-11-05 00:20:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ff4a38a-5586-316b-b68c-17a6beefa90a | -5.8056 | -44.133099 | 2024-11-05 00:20:00 | METOP-B | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 36ba945f-cb8d-3242-85ab-e565e5213051 | -3.6431 | -50.123299 | 2024-11-05 00:20:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10abacbc-4817-3fb0-bded-9cd948479707 | -10.6931 | -44.8531 | 2024-11-05 00:20:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 28f82bc4-c0d9-38ef-8f5e-ca47283aacdb | -6.2829 | -43.3862 | 2024-11-05 00:20:00 | METOP-B | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| efb1c809-7d5a-335e-bd6d-a2e0f34a5c4c | -5.6908 | -45.842602 | 2024-11-05 00:20:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 452eed67-1888-3e94-923d-c7e38bcae442 | -3.4824 | -46.058701 | 2024-11-05 00:20:00 | METOP-B | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 06f95412-87e8-3020-ac2a-d36399af607c | -1.5137 | -47.287601 | 2024-11-05 00:20:00 | METOP-B | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ed3bff8-b830-3c47-9c8a-c1795454d617 | -3.9733 | -48.144299 | 2024-11-05 00:20:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38240329-9152-3aab-9e02-ce0142431ff3 | -4.8353 | -44.937401 | 2024-11-05 00:20:00 | METOP-B | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b0e04dd3-1bd5-3467-8e98-b2c4c631b637 | -4.4092 | -43.485298 | 2024-11-05 00:20:00 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f03fa486-f68d-3028-bec7-707aa027115e | -3.9555 | -45.8269 | 2024-11-05 00:20:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b949a880-db24-328e-893d-d644d1f3a2aa | -5.2971 | -46.243599 | 2024-11-05 00:20:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c75e0ab0-6a9d-3295-8dd4-5106be6dc4e1 | -11.7527 | -44.205399 | 2024-11-05 00:20:00 | METOP-B | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e592a4eb-28b8-3590-b1c7-65de037280eb | -11.8009 | -43.782799 | 2024-11-05 00:20:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1b7108a7-1e3b-3d92-beae-5bbcca9567d7 | -3.4805 | -50.362801 | 2024-11-05 00:20:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 358e122f-e14e-3ccb-a5be-91d14e0123ff | -6.0652 | -47.000401 | 2024-11-05 00:20:00 | METOP-B | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 42d1877a-c8e3-30e7-8299-9fa8d63ec0a5 | -3.8151 | -46.480801 | 2024-11-05 00:20:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f4ecd74f-c429-3579-ac1c-45e83b139d19 | -10.2802 | -42.431 | 2024-11-05 00:20:00 | METOP-B | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ff87f52d-5cf4-3368-8cb5-4dd801455b03 | -6.281 | -43.377899 | 2024-11-05 00:20:00 | METOP-B | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 18609ded-c267-3d71-99a6-38038a527c87 | -11.8025 | -43.7901 | 2024-11-05 00:20:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1647fb37-e4e5-37c5-a81d-677fe0616636 | -2.6521 | -46.761501 | 2024-11-05 00:20:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea4cebb9-e9fb-3c3a-afef-d0742d24038c | -11.9809 | -42.905899 | 2024-11-05 00:20:00 | METOP-B | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 18914b33-7c7d-34bf-8ee9-c55cf38dc19f | -8.3182 | -43.5788 | 2024-11-05 00:20:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b90316c8-3d63-3b31-b26b-4a9a590915f3 | -3.0994 | -50.267399 | 2024-11-05 00:20:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac735752-f09f-319d-b26c-96fbf8cc7f2d | -3.9571 | -45.834 | 2024-11-05 00:20:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aa7f6b1d-2fef-3c72-8a9d-02d9f5d053ce | -4.3839 | -43.108601 | 2024-11-05 00:20:00 | METOP-B | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5c3b238e-aaa2-3167-bf44-98f6b0d31452 | -6.092 | -43.943401 | 2024-11-05 00:20:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7799b90e-912f-38a4-b850-464787daa633 | -10.687 | -44.780602 | 2024-11-05 00:20:00 | METOP-B | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6aa7a8b3-7b5b-3e02-9a97-4dffdb564b97 | -2.8428 | -51.3311 | 2024-11-05 00:20:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a4d81bc6-c1b7-3621-872f-0bcba34d9054 | -5.9006 | -46.086601 | 2024-11-05 00:20:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2e967a45-c7a2-3550-b480-c6f26b17acd8 | -3.491 | -51.0583 | 2024-11-05 00:20:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1280f7f-d87d-326e-8d79-34fe33450364 | -3.1056 | -50.249199 | 2024-11-05 00:20:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8286685a-2be4-395a-9033-ccdec243c10d | -3.4097 | -50.2757 | 2024-11-05 00:20:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e79902a-27c1-3a5f-95aa-9b7ad8ff1860 | -2.2454 | -46.4669 | 2024-11-05 00:20:00 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e18cf7fc-35d7-334f-af3b-010ac5724246 | -3.7091 | -47.609699 | 2024-11-05 00:20:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 578973d2-434e-3272-842f-d81619ac63bc | -4.0925 | -48.308601 | 2024-11-05 00:20:00 | METOP-B | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd6c2483-76a8-3c61-bda7-04562c1f77ba | -6.0957 | -43.959202 | 2024-11-05 00:20:00 | METOP-B | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2b168cfd-de49-312b-9767-46fd47e076a3 | -8.3852 | -43.8242 | 2024-11-05 00:20:00 | METOP-B | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0090b8f8-b1fc-3528-989e-56ca34ea3b46 | -3.5443 | -47.381001 | 2024-11-05 00:20:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| db142a77-bcf3-34f3-86b7-f8d63eb4501f | -5.5641 | -42.2906 | 2024-11-05 00:20:00 | METOP-B | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cf40c7d3-44cb-3c6c-a525-befeb8a3de1f | -6.2508 | -43.559399 | 2024-11-05 00:20:00 | METOP-B | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ac535d6-0534-3211-a72f-5c80042d7c9c | -3.4799 | -45.5067 | 2024-11-05 00:30:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 60.7 |
| fcad209d-8b19-33ba-94ea-a6ccb2a47c79 | -5.0725 | -44.2182 | 2024-11-05 00:30:00 | GOES-16 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 91f514b7-60a9-3131-a0a9-ec0e283ba471 | -2.6322 | -48.5634 | 2024-11-05 00:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| c0557f72-e9d7-3c4c-be98-bb32bf7024c0 | -2.9431 | -54.6707 | 2024-11-05 00:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| e8ef3d89-8cf0-3a0e-8aa3-e71086c73661 | -2.8065 | -51.4855 | 2024-11-05 00:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 48daa42c-6159-3675-8fff-996dffd94e7b | -3.4749 | -50.3826 | 2024-11-05 00:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 6af99a36-2ae4-37df-a355-b9247a2a6ba8 | -3.1061 | -50.2686 | 2024-11-05 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 1d198467-0d21-300a-9ffb-66eee872ced7 | -2.6507 | -48.5629 | 2024-11-05 00:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 155.1 |
| d44963fb-8806-3b93-b95b-70e5a3533ec1 | -3.5632 | -47.3629 | 2024-11-05 00:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 666d409e-d389-32fc-8990-43f09833eaf1 | -2.8064 | -51.5061 | 2024-11-05 00:30:00 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 50eb46f9-d6e3-3f0a-918a-e0d8aa5d1330 | -3.0906 | -54.5073 | 2024-11-05 00:30:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 03e88368-94a4-39d6-a657-e6fa5b0dea1b | -6.1041 | -43.9593 | 2024-11-05 00:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 274.4 |
| 9f1ea002-e2d1-3eda-a2a9-975130e96dca | -11.8639 | -43.8644 | 2024-11-05 00:30:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 98.3 |
| c7ecd643-6099-3a62-8e74-286fd7f544c7 | -4.3806 | -47.2388 | 2024-11-05 00:30:00 | GOES-16 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 02504e49-2d81-3675-9bda-157bbb0c7049 | -6.1043 | -43.9362 | 2024-11-05 00:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 8a1f919b-e4b0-37c2-9567-561486eb7e94 | -5.6946 | -45.8098 | 2024-11-05 00:30:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 43.9 |
| ac9b87d2-adcf-37ef-b22c-0acf7174fbb9 | -6.1229 | -43.9578 | 2024-11-05 00:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 116.4 |
| ab110fb4-06b5-3f0b-952f-95b829af789c | -6.1039 | -43.9824 | 2024-11-05 00:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 2869773b-4ef0-3087-9d9f-d4f69ac847c4 | -2.82 | -52.9409 | 2024-11-05 00:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 83b6ae03-d168-3ec9-b237-0b3f5de78f2c | -3.4798 | -45.5291 | 2024-11-05 00:30:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 134.3 |
| 4602124e-3cdb-32c3-95dc-e7b3cd6b20e4 | -3.4796 | -45.5516 | 2024-11-05 00:30:00 | GOES-16 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 8915cb29-1d99-35e5-9120-b70b8b2752bb | -3.563 | -47.4066 | 2024-11-05 00:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 97a59227-18ab-37f8-867d-f94cf3f479a1 | -6.1226 | -43.9809 | 2024-11-05 00:30:00 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 51.1 |
| c84b83c5-420d-331c-8acf-fd42c7272194 | -3.5631 | -47.3847 | 2024-11-05 00:30:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 213.5 |
| 9e33755f-a22d-3a53-ac29-c67c66b72532 | -3.967 | -48.15 | 2024-11-05 00:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 350a8557-e3f6-38b7-94ac-b21ee17468bc | -3.1062 | -50.2476 | 2024-11-05 00:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 917961c4-7ec3-3193-a712-04897fb41f97 | -5.6943 | -45.8547 | 2024-11-05 00:30:00 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 70.5 |
| 1dcf7612-853d-3500-bf3f-2a2eed744f0d | -5.0729 | -44.1723 | 2024-11-05 00:30:00 | GOES-16 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 36.7 |
| 5553b786-59d6-3d49-97f1-4519ca7d1bc3 | -2.6691 | -48.5624 | 2024-11-05 00:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |


[Clique aqui para ver as próximas entradas](README7.md)
