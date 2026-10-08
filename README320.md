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

## Dados Diários - Página 320

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a2e9baa8-004d-3143-b4d9-ca4aa8414dfb | -11.79849 | -46.77633 | 2026-10-08 16:37:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 431732da-c180-3c55-acaa-481730308b1a | -8.28481 | -45.7063 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| b0d5e16f-6e59-3283-9a94-404f5a3f50d9 | -7.65165 | -39.94527 | 2026-10-08 16:37:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 55ddb8a1-2be4-3512-adbc-2e31e8fd8418 | -6.10977 | -38.16817 | 2026-10-08 16:37:00 | NOAA-20 | PAU DOS FERROS | RIO GRANDE DO NORTE | Brasil | 2409407 | 24 | 33 | nan | nan | nan | Caatinga | 19.6 |
| ac4b9cd7-1e4b-3186-b674-12c2296f9dc5 | -7.11416 | -42.53635 | 2026-10-08 16:37:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| a30bb429-c091-3d5b-a7e7-99c216d1ccca | -18.82071 | -47.14281 | 2026-10-08 16:37:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 89014be1-2bb2-3146-b5ec-b274b87ed2c7 | -11.6411 | -43.69719 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 4b404005-d9ec-3510-9ea7-325782ab3e19 | -10.46824 | -47.2429 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| f87a7156-a5cb-3b1c-8e0a-e3af67610df0 | -8.07814 | -55.29753 | 2026-10-08 16:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9dce5b12-2e8b-3263-bd3c-7e14f8cdfb1e | -7.48777 | -42.81753 | 2026-10-08 16:37:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 32.8 |
| aed9aea9-361e-390f-b68d-c278edfb837a | -7.22046 | -44.1539 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8df0fd84-b074-33f0-aeca-b7c286c50f4c | -11.07393 | -47.49038 | 2026-10-08 16:37:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7aa3faf8-77e4-3640-a7bb-fe502c5a8ada | -10.46769 | -47.23907 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 73c8acec-4699-3335-bbb5-afd42e3ad013 | -11.78627 | -46.78537 | 2026-10-08 16:37:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 22f22adf-c916-3d66-8878-e42b9917299d | -13.13537 | -46.3299 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 4161392f-6725-36d0-a1f9-1f49a67810ab | -11.25018 | -46.25746 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 1674c999-2bb8-3c92-b661-1753bf356765 | -6.12727 | -44.13213 | 2026-10-08 16:37:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ef4fc9e1-d00d-3b24-b096-74bf396295cf | -7.84815 | -45.51336 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 4e5eaf95-cfa8-307d-a20e-12b0576b730e | -11.22972 | -45.23899 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 889e0c00-e814-31ba-a495-5d44ac8bc67e | -6.64553 | -43.77044 | 2026-10-08 16:37:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 4fe6a58d-a164-3921-98ec-f7503a21feaa | -6.05756 | -42.60142 | 2026-10-08 16:37:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 21.1 |
| 41a04153-e52c-3f7e-b9ba-c2a33d7dfa57 | -11.0875 | -44.00386 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 792aa5fe-2843-348a-b3fb-0afa798f8a9c | -11.87341 | -47.40482 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d1b6d6e6-debc-35af-848d-7ccfb69e9ebf | -9.95295 | -45.97195 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a4f83376-2c17-3e6b-85e3-9a6c5ab0e5de | -10.24897 | -49.67313 | 2026-10-08 16:37:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 0d5953b1-f024-3558-8f0c-0336c430394b | -8.28573 | -45.73459 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 73b47695-e7e1-36af-99b0-fba5b3e54208 | -11.14095 | -46.15923 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 110dce68-b810-31ee-9ed7-a98f1525cb49 | -9.51721 | -46.83817 | 2026-10-08 16:37:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 7b62b94c-4ff1-3768-9ad8-d5d4b4d304d7 | -5.50026 | -40.53936 | 2026-10-08 16:37:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 10.7 |
| ed6d36f9-8278-39bd-bd75-a7dc0f28e310 | -9.10828 | -45.12197 | 2026-10-08 16:37:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 28803b99-4b55-3ae0-854e-e42f75f37810 | -7.04567 | -44.33761 | 2026-10-08 16:37:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e2cf9791-be5c-3a68-87ce-de02c5653708 | -9.52525 | -45.60876 | 2026-10-08 16:37:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 1faced4c-93e4-3282-b674-54e2ee7708c1 | -10.00933 | -45.51303 | 2026-10-08 16:37:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0d1ae578-640c-3e92-8997-1a7a2ad2d394 | -10.46533 | -47.24725 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 430fe3f4-8adb-3ad9-990a-595356ce77cf | -18.0771 | -41.47942 | 2026-10-08 16:37:00 | NOAA-20 | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9bfec7ba-7211-3212-870b-58a8c3ec1ab5 | -7.07626 | -40.93897 | 2026-10-08 16:37:00 | NOAA-20 | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 47a6dd81-4dfc-3d22-b379-1e2bcdd5259c | -7.94176 | -50.96415 | 2026-10-08 16:37:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 06e94640-fda5-37b8-b833-d7b1d85efcf3 | -8.08074 | -45.61439 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1b5281f3-dfd8-3f9b-b227-995906ac7548 | -8.23309 | -54.73491 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 9a20fb11-3365-3933-8523-21e83c632868 | -11.22694 | -45.24302 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 032fc530-647a-31b8-a382-36a4fd3e227b | -6.82306 | -39.5479 | 2026-10-08 16:37:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 57942eb7-49a2-3930-9b3b-5c52f7a8273f | -8.68778 | -45.27887 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4c095a00-d421-3947-b946-8ae7ff687cb6 | -5.92347 | -39.42849 | 2026-10-08 16:37:00 | NOAA-20 | PIQUET CARNEIRO | CEARÁ | Brasil | 2310902 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 2cfa1efb-b611-3fb8-8bce-1ca6be3a94e0 | -12.82999 | -44.62941 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| a41c35fc-d351-3481-b259-dc14e80c6879 | -7.85911 | -45.14162 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fbb1f109-b120-3442-acad-0dc9f31e03ef | -6.99221 | -43.21026 | 2026-10-08 16:37:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| ff638217-c2dc-3ee8-9c89-cd00bec7ebe9 | -11.10914 | -44.01133 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 36229d57-4807-38ec-934d-1d915f1a2eac | -10.5885 | -47.30061 | 2026-10-08 16:37:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 20510e7d-8d88-32d4-b027-aef223bc80eb | -5.72394 | -41.62139 | 2026-10-08 16:37:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| c3f34c03-bf84-32d5-b835-5682ef6b0c6f | -11.35416 | -46.69951 | 2026-10-08 16:37:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| a1dbb1fd-5b09-35b9-9aa6-fbafa97384df | -9.5037 | -46.07218 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 217f922c-2551-378d-9f8c-5337efa83796 | -8.66582 | -54.53157 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 144f2df4-8546-3d1d-a94d-2dfea979483e | -7.25852 | -45.3414 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 34d2a768-30b2-3df1-bd40-b7c0b0f0cbd3 | -11.73463 | -43.6447 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 40.4 |
| cd84723f-789a-346a-b569-1a1b4aa5af83 | -11.20184 | -49.42408 | 2026-10-08 16:37:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 4e5c0542-1aff-326d-aecb-7437df9fe192 | -11.20506 | -49.41849 | 2026-10-08 16:37:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 14475bad-ebbc-3560-9d01-3d3c1d73a266 | -11.96919 | -57.58733 | 2026-10-08 16:37:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 270ee5d1-265e-3d93-aff1-3686677bb639 | -7.08897 | -43.08952 | 2026-10-08 16:37:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 29.0 |
| 593c1093-e7a0-3535-b295-d3595e5539d3 | -6.18042 | -44.95195 | 2026-10-08 16:37:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0d9918f8-8263-3cef-bbd1-ce6535998e94 | -12.40923 | -39.07944 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO CARDOSO | BAHIA | Brasil | 2901700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 91fe446d-96cf-3825-990d-8fc55351cbd7 | -7.17121 | -47.7873 | 2026-10-08 16:37:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 97209d38-5335-361e-af72-a8b6cda56088 | -6.53329 | -45.39344 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| a739987b-a3f4-388f-9eab-e51535990d7b | -10.76628 | -46.57968 | 2026-10-08 16:37:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 1de6cbe5-e843-3807-8d06-cf1d9760d9f9 | -11.62608 | -43.71065 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 49.4 |
| a1eeef61-557a-370c-805f-c3162c7aa52d | -6.59781 | -37.89398 | 2026-10-08 16:37:00 | NOAA-20 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 45.6 |
| 6013faf4-10b2-3cdf-b75c-4163b9ab67f2 | -8.19225 | -45.78871 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| bb3b31e4-b949-3508-8186-4d545bc7594d | -13.14873 | -40.21931 | 2026-10-08 16:37:00 | NOAA-20 | PLANALTINO | BAHIA | Brasil | 2924900 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 7d48684d-4605-3117-9a78-af73068a5060 | -5.99161 | -40.93183 | 2026-10-08 16:37:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 24.8 |
| 8301991f-85a2-300f-b9e2-0a9db98b4c37 | -6.08793 | -43.99316 | 2026-10-08 16:37:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b4a91a8f-105d-3526-9a9a-8568d0fbf367 | -19.0832 | -40.08982 | 2026-10-08 16:37:00 | NOAA-20 | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 456f2f42-fc98-3c80-bb03-e1cdb0beb89f | -7.54413 | -42.08832 | 2026-10-08 16:37:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 33.7 |
| 48e8291e-cdfd-37b1-a880-6d8ca31fe82e | -9.08075 | -45.11909 | 2026-10-08 16:37:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 354eedbc-1713-3a3b-ab80-b4c123a17b6d | -7.16464 | -41.99182 | 2026-10-08 16:37:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| d1871359-6703-34b1-978f-8bcc87636db6 | -12.41229 | -39.08234 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO CARDOSO | BAHIA | Brasil | 2901700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 9d324edc-677e-3744-80f0-52ab69050d8b | -9.03032 | -44.37287 | 2026-10-08 16:37:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 31.9 |
| 9dff63a0-bf19-330b-983d-a11f98dec654 | -7.82416 | -38.85723 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 0b954083-73fe-3dbb-886a-eb9963046307 | -7.17188 | -44.82517 | 2026-10-08 16:37:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 25ae005b-9456-350f-908c-19d7f09259a6 | -11.25546 | -47.74848 | 2026-10-08 16:37:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 5c6880ac-dbb7-3225-b926-581796ca4d60 | -8.93043 | -45.17976 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 9421e352-fee2-39c7-a725-9508c657694b | -6.39217 | -42.53902 | 2026-10-08 16:37:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 19.9 |
| ad4fff15-184f-35d6-98fb-1feb31aeeb3e | -8.53148 | -46.91433 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 0af1a5db-52ed-3e1b-a123-ff54fcc7a38a | -13.02103 | -48.51477 | 2026-10-08 16:37:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 23.7 |
| eaea9cbe-6022-3d1b-b328-b36fe0c4a706 | -8.9332 | -45.17577 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 83b877ce-37d7-380c-897a-8c30fd47e48a | -8.19887 | -45.78771 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f5f8a205-5be3-3599-bc2f-c1aaecf71ec6 | -11.58762 | -43.68371 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 236.1 |
| 9221ee1f-d3d3-326d-b9c8-7ae3f3df0518 | -8.79279 | -47.59274 | 2026-10-08 16:37:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 53ca5a28-6fd5-3126-8b1e-511bd5efa6ac | -11.63553 | -43.70542 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| b5faf251-11ec-3781-9afd-9d879a7d13a1 | -9.24872 | -45.64155 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| fdd0e98f-0696-314b-b598-d56e9a5fc8c8 | -7.75837 | -54.9554 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| ef616d25-0faf-30a3-8731-c556d3d57d3b | -6.32269 | -35.12595 | 2026-10-08 16:37:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| 61131674-7798-384e-a3ac-2f3d5c1b4f3e | -11.9607 | -47.76626 | 2026-10-08 16:37:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 559baa74-2be3-3b77-859d-8baf0a11afe8 | -11.7636 | -45.49678 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 608f6ba5-e5a0-3b30-a00e-94f95323868f | -6.99751 | -40.45202 | 2026-10-08 16:37:00 | NOAA-20 | FRONTEIRAS | PIAUÍ | Brasil | 2204303 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 5f5bf346-5748-3de0-b395-00777b5e5ea2 | -9.80159 | -44.77406 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d9eb05dd-dcbc-3665-8087-b07e590a0480 | -7.75792 | -54.95194 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 6659b1fb-e878-3b72-ae89-064bf0b954c2 | -9.88887 | -44.85637 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 7fc70349-9861-3944-8bc9-c95871ae71f1 | -8.94164 | -45.14241 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| e69838aa-733c-3715-9ba9-0b5844e2305c | -18.05465 | -44.5672 | 2026-10-08 16:37:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f054688c-c5fa-37d0-90eb-3feca988cace | -10.5973 | -52.84219 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3bcbbb49-51e5-396f-b6a5-60d2a907dabf | -8.75947 | -47.57427 | 2026-10-08 16:37:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README321.md)
