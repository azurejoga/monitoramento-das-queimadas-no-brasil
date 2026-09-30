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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1721c82-bd63-3d99-b472-6079b6d355de | -16.90619 | -42.1022 | 2026-09-30 03:57:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1c45b2b2-44b8-3ae4-b778-b25f2a23fc6c | -12.62874 | -47.2454 | 2026-09-30 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49ef6ee6-b123-3d25-bbf5-80c45168572b | -14.12992 | -46.26518 | 2026-09-30 03:57:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9a7936ac-30f4-374f-a755-d3a56fb03377 | -12.78768 | -53.99741 | 2026-09-30 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5cd65df4-0b6d-3043-8ec9-238e4fb8ac4b | -11.8221 | -46.89972 | 2026-09-30 03:57:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d0eccd2f-cc09-3f3e-a2c6-8456fffccbac | -13.93953 | -42.96594 | 2026-09-30 03:57:00 | NOAA-21 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c26f364e-7391-3430-b307-52eeb4ea91cd | -13.33999 | -43.94984 | 2026-09-30 03:57:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa283000-c58f-3933-900e-64471371e88f | -18.63374 | -46.96764 | 2026-09-30 03:57:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8116365a-7c6b-3a7e-8fff-927904e4715e | -15.79057 | -44.69012 | 2026-09-30 03:57:00 | NOAA-21 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 558666b0-29f7-31c3-a3a9-82e2167d1c1a | -15.77867 | -46.03202 | 2026-09-30 03:57:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 45ebcf48-b838-3447-8080-e644791b4c2f | -18.59455 | -43.44504 | 2026-09-30 03:57:00 | NOAA-21 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 84ed1421-61b9-3737-b986-d5e1cf7ea739 | -16.11736 | -42.21951 | 2026-09-30 03:57:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 48b0219d-3670-3da4-a5d6-3a6bc6f06c69 | -12.62679 | -48.35598 | 2026-09-30 03:57:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0345045b-9830-3126-86f8-7725723195d6 | -18.04561 | -44.32595 | 2026-09-30 03:57:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 51f72499-7c18-3cc2-b8d7-26d26f001b97 | -12.76687 | -50.64775 | 2026-09-30 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3d7f7028-6ece-3c21-990e-f7d9c85ae268 | -15.13339 | -43.62294 | 2026-09-30 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c57c3e44-5a96-3747-a95b-245af95d3d2f | -15.97922 | -48.13587 | 2026-09-30 03:57:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b2751f17-b9ec-3c6e-8346-8a492ef4c01e | -18.89087 | -43.81444 | 2026-09-30 03:57:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a6a1dbe7-442e-3807-b5d9-a4c663c7c645 | -17.10428 | -46.47104 | 2026-09-30 03:57:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 13f0e045-b230-3910-bb64-c6863b10554c | -14.50942 | -48.28885 | 2026-09-30 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 738c4a91-5520-3fe7-ba57-00e5356a196c | -17.84277 | -44.3426 | 2026-09-30 03:57:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 507d72ec-ed99-3e52-9472-a99f2b939594 | -12.07506 | -46.46167 | 2026-09-30 03:57:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6e1eecfa-f2a2-3ba9-a54a-b047b2446cbe | -20.21578 | -42.31325 | 2026-09-30 03:57:00 | NOAA-21 | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f965d09a-db68-31e2-a4ec-82635991c645 | -12.78234 | -53.9971 | 2026-09-30 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 67e72281-eabe-3318-a4a9-c1054993bcb7 | -12.78506 | -54.01882 | 2026-09-30 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 415dd149-a1c4-30cf-91f0-45fa171876f2 | -14.0133 | -42.91252 | 2026-09-30 03:57:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 16.3 |
| f9b08e23-2549-3218-9a9a-6fa31104e0d9 | -18.09211 | -42.93292 | 2026-09-30 03:57:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8d981976-6cf9-392d-9de8-8ad4b73453d2 | -13.77062 | -43.65154 | 2026-09-30 03:57:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1947d907-0456-3db9-b4c9-ab38d9bc33cf | -14.0116 | -42.90781 | 2026-09-30 03:57:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 18.0 |
| 284f3538-73eb-3736-874e-d402357b76af | -15.6829 | -41.70821 | 2026-09-30 03:57:00 | NOAA-21 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| e09123d2-5dc3-3f84-b0cc-98082093285e | -14.12494 | -46.2686 | 2026-09-30 03:57:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b658500f-1cc1-3048-abaa-0c0f8c739275 | -13.0696 | -43.28164 | 2026-09-30 03:57:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| f5f46867-fd8c-3ebf-8e41-5d1fd48dcedb | -17.88739 | -40.06509 | 2026-09-30 03:57:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bf79556a-412f-3731-a42e-38abc7b0ac58 | -18.25146 | -53.04128 | 2026-09-30 03:57:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 01652974-a12c-3fef-b1bb-15a51debd4e5 | -10.76394 | -52.1283 | 2026-09-30 03:57:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8669f577-219a-3409-b224-e3bc01685796 | -14.85641 | -48.18392 | 2026-09-30 03:57:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 80f7f1e6-a609-3023-a21a-03b683638141 | -15.94513 | -40.52366 | 2026-09-30 03:57:00 | NOAA-21 | BANDEIRA | MINAS GERAIS | Brasil | 3105202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4acce92f-0503-32c6-bc2e-d5b8847d581a | -12.27856 | -50.2892 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a35c6c7-2056-3b69-8d31-d3df39a7d9db | -12.56906 | -43.07287 | 2026-09-30 03:57:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 2ffb7f36-c717-3454-8e72-0809d931986d | -16.35946 | -42.58739 | 2026-09-30 03:57:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec9693c1-80ab-3201-a31a-f41e6eceafb0 | -12.953 | -46.6445 | 2026-09-30 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5db49239-62a2-3542-8fc6-e43641f2c2aa | -15.44599 | -45.68853 | 2026-09-30 03:57:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 77075ab9-25d6-3959-bc78-34c30d9a46f8 | -12.81128 | -50.6684 | 2026-09-30 03:57:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b54101eb-b444-32f6-a9d5-363c3fb92053 | -13.14129 | -43.79273 | 2026-09-30 03:57:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0cf8a2c5-9ecc-32b5-8752-2f4b71211975 | -18.11803 | -40.33975 | 2026-09-30 03:57:00 | NOAA-21 | MONTANHA | ESPÍRITO SANTO | Brasil | 3203502 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4fe7e828-d90b-3e44-a5b8-c4727309df1b | -18.50389 | -45.14796 | 2026-09-30 03:57:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 1af5632b-85b4-35a3-ace9-3f8a3357ca8f | -12.49437 | -44.98139 | 2026-09-30 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2fcf7af9-ecf3-3ea3-b178-3e82d3840583 | -12.24111 | -50.25755 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5de2ca8-f3c9-3596-830e-b56c7eb25681 | -18.48311 | -41.17277 | 2026-09-30 03:57:00 | NOAA-21 | NOVA BELÉM | MINAS GERAIS | Brasil | 3144672 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| baff6f1f-d24c-3c25-ae08-5eb27f9553e5 | -16.12072 | -42.2201 | 2026-09-30 03:57:00 | NOAA-21 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 2863c60b-6373-3113-b895-d9dfe5331149 | -12.25168 | -50.24679 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dffc5316-90e3-3cef-aed4-c333de10caa7 | -16.91167 | -42.11071 | 2026-09-30 03:57:00 | NOAA-21 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 324e526e-e12f-3422-b274-0748a8db84da | -16.86449 | -42.46389 | 2026-09-30 03:57:00 | NOAA-21 | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 72cf1bcd-b05b-36e7-834f-51f0af7cfa26 | -13.37916 | -46.8204 | 2026-09-30 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5a013317-7012-3b15-98e0-04cc04cd2009 | -17.57651 | -43.70674 | 2026-09-30 03:57:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 8e0f304f-5a0e-3990-8a1d-bd167c0594fa | -15.19626 | -46.14011 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd57ab77-fdbe-383d-99d3-3d64a180e6df | -19.27669 | -43.76196 | 2026-09-30 03:57:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 027feb3d-4e56-3321-b2f4-b2fc7e1ccc7a | -14.91018 | -41.68588 | 2026-09-30 03:57:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 29a78c62-aab6-3af0-bc72-1a878267bfbc | -18.10447 | -44.41115 | 2026-09-30 03:57:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ab0d53c-4487-353f-8ea4-8a5dbd3d05af | -15.30238 | -42.76748 | 2026-09-30 03:57:00 | NOAA-21 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9a8004ec-2ff6-3c77-8b1b-27007092c361 | -18.30835 | -42.21295 | 2026-09-30 03:57:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 63669b87-1880-37d1-9cb3-3bd789f24aeb | -13.92922 | -43.80302 | 2026-09-30 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4383c360-66ff-3740-92d4-807a604e05f0 | -18.23663 | -53.0229 | 2026-09-30 03:57:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6761f078-14f5-32d0-abee-3d07a8db7b34 | -15.75613 | -46.03925 | 2026-09-30 03:57:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| df98e9d5-635e-3d3a-b263-cc2cc2d71f90 | -12.88164 | -44.80049 | 2026-09-30 03:57:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bde14cd7-1b74-3e88-b34b-1b9a2c86d555 | -15.12982 | -43.62232 | 2026-09-30 03:57:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 58698c40-6523-3212-9931-25579ffe1dfb | -13.74424 | -43.7638 | 2026-09-30 03:57:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26ea418f-e6e6-323e-b664-c4fe3de073cb | -16.35291 | -42.57887 | 2026-09-30 03:57:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0897a23e-a0ec-39e2-beec-f25f485ce9c6 | -14.01396 | -42.90851 | 2026-09-30 03:57:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 16.3 |
| 90bfc585-a505-3c5f-a730-fa1224e326df | -16.27144 | -43.51485 | 2026-09-30 03:57:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b9cdd15a-31b1-3e28-8bf9-bf0ff103141e | -12.35971 | -46.39062 | 2026-09-30 03:57:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d76e64bf-3922-34ea-9d78-ee6dfbf45396 | -18.63301 | -46.97159 | 2026-09-30 03:57:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f14a068-2757-3084-8cd0-652f0f994f06 | -15.77935 | -46.02834 | 2026-09-30 03:57:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e52084f4-b91c-32bc-a60c-c35f5db39924 | -12.70968 | -46.96031 | 2026-09-30 03:57:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0c815bf6-31c8-32e4-93c5-974360523d0a | -18.49083 | -45.1357 | 2026-09-30 03:57:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01c303b7-b5ff-3c64-bf0f-940f73d753f4 | -11.8184 | -46.89412 | 2026-09-30 03:57:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c9a14efa-337b-3c9d-b3c6-a37c4642f8ce | -12.26235 | -50.28184 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3ea0df99-5b28-3b72-8859-a7c46c118905 | -18.24651 | -53.03516 | 2026-09-30 03:57:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f79849e8-73f9-3570-8a30-a82128fe8a04 | -12.25669 | -50.28072 | 2026-09-30 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 74c4c37f-3540-3b8c-97d2-aa9a5f16f1b4 | -13.37544 | -46.8157 | 2026-09-30 03:57:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 949a6550-01aa-3e03-acb2-d8ccbe237453 | -12.79178 | -54.01218 | 2026-09-30 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 340c8d1b-69dd-3770-bcdd-da8d891c272c | -14.11731 | -46.26265 | 2026-09-30 03:57:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e17f3dde-bcd6-33c7-8199-d78b8932e82b | -15.3942 | -44.27306 | 2026-09-30 03:57:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e04f4187-e551-3e12-8448-1baac39a8a3a | -13.33043 | -43.93881 | 2026-09-30 03:57:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b26e3aa0-1e61-3460-9f7a-4d6c36e2710b | -18.07543 | -44.36597 | 2026-09-30 03:57:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1a1805f-bd05-35cf-bc40-676ac145abab | -14.28207 | -43.56356 | 2026-09-30 03:57:00 | NOAA-21 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 341a3fc6-a234-333f-ba5a-a6ad604c6545 | -15.29893 | -42.76698 | 2026-09-30 03:57:00 | NOAA-21 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8802e02-b65e-32b9-8d9c-2216f41976fb | -14.53247 | -48.29807 | 2026-09-30 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 293f5ecd-f724-395c-9c23-32bc69ef9cfd | -13.38115 | -44.02279 | 2026-09-30 03:57:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 46b57ae9-aed2-3d89-b980-248772a16db2 | -18.49001 | -45.14031 | 2026-09-30 03:57:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48320a4e-6b7b-3149-961b-265713d41ca1 | -17.793 | -47.17258 | 2026-09-30 03:57:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7c48592a-d1ea-3e47-a757-db7efa95a13e | -18.2878 | -43.69868 | 2026-09-30 03:57:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 048b7d81-7931-3031-9952-b285b25ad51f | -12.51604 | -43.09069 | 2026-09-30 03:57:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 0b3a44cd-4c24-3f58-9599-bfc0b19afa87 | -15.96607 | -40.51981 | 2026-09-30 03:57:00 | NOAA-21 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 78cf32ef-5c52-3080-bae4-c46ad72c8fbf | -12.77809 | -54.01728 | 2026-09-30 03:57:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 840abc1f-06be-3cac-aabd-f5ab278c28fc | -14.94149 | -49.75015 | 2026-09-30 03:57:00 | NOAA-21 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 663353c4-9b47-3a25-8425-84027e1c18f2 | -12.31932 | -47.95163 | 2026-09-30 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b824e542-4f88-3c53-ab27-634cbdc2f985 | -12.30377 | -47.95392 | 2026-09-30 03:57:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 4bee4dad-dd94-3ad5-b083-556a0c883aea | -18.23768 | -53.01815 | 2026-09-30 03:57:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31c3c4d2-f509-313b-b891-4a55df11ed84 | -13.27693 | -43.6378 | 2026-09-30 03:57:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README20.md)
