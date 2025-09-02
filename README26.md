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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72f257d7-1f4e-3955-b460-8514ffcc79f9 | -12.33102 | -45.71933 | 2025-09-02 03:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f57497d9-a7d0-32f7-970e-367e7e4e040c | -10.06144 | -48.09854 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 870e749f-ebec-334e-9843-e0481dc1e09e | -11.97948 | -45.87599 | 2025-09-02 03:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4daf8cd5-1b52-3fc1-b612-fcac9ed8cb5a | -14.49116 | -45.94809 | 2025-09-02 03:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18957389-a712-3a18-a158-01a3564cc901 | -8.13072 | -45.03576 | 2025-09-02 03:51:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ad1e6edc-d0a3-33e9-b54e-87c2408f56d6 | -7.98868 | -46.45805 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 010f0271-2317-32dd-8bd5-0c7290f8186a | -11.67468 | -52.19411 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| b8be404d-61b9-30a3-8076-67eb77ce7a23 | -14.04044 | -44.61477 | 2025-09-02 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ea21fa04-75be-3d86-91d8-c2d0d5c7d1f5 | -11.13671 | -46.34247 | 2025-09-02 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 572a3b47-8349-3676-a29d-aadaa546be28 | -9.73021 | -48.95914 | 2025-09-02 03:51:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87925bb4-458c-35b5-96e5-42d343c34f25 | -7.63688 | -46.56031 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e6604faa-481e-37db-b31f-f79d31c91645 | -12.81287 | -48.05928 | 2025-09-02 03:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 792bb396-aead-3ced-b80a-aaa95235ea2f | -13.70261 | -46.89062 | 2025-09-02 03:51:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1acbe346-3ea2-3a73-856d-477680e8efbb | -13.54022 | -46.98012 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 851a5c31-c1e2-3fde-a16c-0215298b6a56 | -8.46887 | -47.37587 | 2025-09-02 03:51:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b774368-191c-3d8d-a583-282978654ca3 | -8.83342 | -45.78777 | 2025-09-02 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01af83a3-18c1-3638-a24c-f2c7eb9c988d | -11.67675 | -52.21035 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 32.6 |
| ce6f5009-1201-3661-ab79-aafdc59c359d | -12.58123 | -44.80863 | 2025-09-02 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1416f0d7-0540-36a4-aae2-9f138cd67d26 | -7.5742 | -45.22316 | 2025-09-02 03:51:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c392cab5-c06f-3ec0-b0dc-01c451a30ebb | -9.47624 | -47.60629 | 2025-09-02 03:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 583a1093-af9a-3a0c-aac4-28cef6fcff88 | -10.05165 | -48.09352 | 2025-09-02 03:51:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b135d66d-7bee-33dd-ac40-53922fd55a0e | -11.00533 | -46.83504 | 2025-09-02 03:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b735ffbb-8696-3636-8ed6-a76df9a8b328 | -13.59164 | -48.13869 | 2025-09-02 03:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6778de3-fc60-3ca8-9066-eaef409fa5c2 | -11.64615 | -52.03658 | 2025-09-02 03:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9bc2d8cf-0df7-3ed1-971e-c6b83ecedc6f | -11.89468 | -44.88832 | 2025-09-02 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eed7a756-215e-3cde-8947-b6e48e71cf56 | -8.84053 | -45.80704 | 2025-09-02 03:51:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e574c346-b7a7-3a51-9d98-5160004f02c2 | -14.5943 | -48.07043 | 2025-09-02 03:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e910ca1c-f741-3386-862a-32fd4e09498d | -12.33499 | -45.67357 | 2025-09-02 03:51:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4fe0b2a0-71fb-3e1d-a970-98c17275ea20 | -8.71594 | -50.44697 | 2025-09-02 03:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 82ae1c19-395d-3217-8f3b-60ef2ee6ea16 | -10.26568 | -47.51981 | 2025-09-02 03:51:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0c404ae0-3d90-3bf0-a919-50b70862f117 | -13.49812 | -47.00631 | 2025-09-02 03:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23da4395-1b7d-3cc7-915b-eda59d1ec599 | -21.11461 | -46.85344 | 2025-09-02 03:53:00 | NPP-375D | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01cc512a-b7ba-3d28-a4a0-93dcdb2aad1f | -14.19581 | -51.66137 | 2025-09-02 03:53:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 32ec86b8-3f73-3496-8261-547cc594f15d | -15.56701 | -48.37574 | 2025-09-02 03:53:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b25cc720-2bef-3440-94a1-998e0b0196b6 | -17.8899 | -47.16182 | 2025-09-02 03:53:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 17b20e72-b35c-3987-8e7c-f70f48ea7e0c | -15.72482 | -48.93932 | 2025-09-02 03:53:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 67a81893-b043-30e6-aab0-943f7fbb17aa | -15.08881 | -48.11988 | 2025-09-02 03:53:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e48f8714-5f2f-3dbf-9b19-ee10a23b1232 | -14.76837 | -48.15969 | 2025-09-02 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4017cbbe-3903-3f0e-87e8-a29cfdf8f393 | -17.89399 | -47.16633 | 2025-09-02 03:53:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 630c28cd-19d7-388e-a8a0-4be0e51492c0 | -15.57471 | -48.393 | 2025-09-02 03:53:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7ffeb404-1dc7-3772-8148-7a1ff46133c2 | -20.70308 | -46.3017 | 2025-09-02 03:53:00 | NPP-375D | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4de7ab8a-8095-385d-ac4d-c31bf644019b | -16.86263 | -49.579 | 2025-09-02 03:53:00 | NPP-375D | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 70e831d8-c14a-3c7e-8bc9-48dd5648c071 | -16.63228 | -44.58823 | 2025-09-02 03:53:00 | NPP-375D | CORAÇÃO DE JESUS | MINAS GERAIS | Brasil | 3118809 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 845f5c0b-71eb-384d-8141-95e9efbb12c4 | -17.61753 | -46.64442 | 2025-09-02 03:53:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d02ec24-a87c-36f9-b84e-2a71bd4ca693 | -15.69312 | -48.92533 | 2025-09-02 03:53:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5a6e7c55-7f39-303f-ab33-5540043581d9 | -14.23252 | -51.66314 | 2025-09-02 03:53:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2d090c89-a5d9-3003-a065-5c034222b484 | -20.06639 | -45.40472 | 2025-09-02 03:53:00 | NPP-375D | LAGOA DA PRATA | MINAS GERAIS | Brasil | 3137205 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a07825f6-4d14-3b6d-8c29-8df181959752 | -14.79201 | -48.18942 | 2025-09-02 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 43501f03-6a4a-3db0-90bd-50ffe513eb9c | -19.41434 | -43.79292 | 2025-09-02 03:53:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 761e4fa3-c110-3a12-915d-0efeb9e1041a | -14.99018 | -50.19842 | 2025-09-02 03:53:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6f5f36d-5c56-320b-ae7d-bdbbeea91bfe | -17.88925 | -47.16534 | 2025-09-02 03:53:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 13.1 |
| d7122ebc-998d-3998-9d65-468c534b69a8 | -14.79298 | -48.21223 | 2025-09-02 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2953a109-d035-35dd-84fc-487479d5f97c | -14.79767 | -48.21671 | 2025-09-02 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a104d490-d8fc-3eeb-b51c-c652e2b6f950 | -14.76015 | -48.15394 | 2025-09-02 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4127a9cc-8e67-3092-b3cd-806ec61afab1 | -15.12694 | -48.11128 | 2025-09-02 03:53:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1eddf48-a2e5-3d3c-b9fa-8683415b626d | -18.59459 | -44.51055 | 2025-09-02 03:53:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 914b2354-721c-374b-b4c1-2bde9cd54634 | -17.28128 | -49.20314 | 2025-09-02 03:53:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac53a885-8e93-3073-8e03-902cbe437b80 | -15.57023 | -48.3875 | 2025-09-02 03:53:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8dc782b0-2b94-3086-9dfd-6361504a6bc4 | -15.56459 | -48.33242 | 2025-09-02 03:53:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7f2482a5-af09-3188-bce3-b514059d3593 | -20.69798 | -46.30511 | 2025-09-02 03:53:00 | NPP-375D | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 285285e9-149d-3bf7-bc81-906b8248186a | -17.89243 | -47.17368 | 2025-09-02 03:53:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 903cb4ee-aa2a-3a36-a007-c2f264310fd9 | -14.76954 | -48.15379 | 2025-09-02 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9cc712c8-9c9c-3a96-946a-4bff43ce54a8 | -14.97197 | -48.17619 | 2025-09-02 03:53:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1a963ebf-7aaa-3952-9268-8daa12e485a6 | -15.09176 | -48.12093 | 2025-09-02 03:53:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c537ff3b-c759-3b24-8a10-041130c3b0ac | -17.8919 | -47.17706 | 2025-09-02 03:53:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 88f14d45-6c46-36ff-b869-62075eb62a6d | -20.70125 | -46.31104 | 2025-09-02 03:53:00 | NPP-375D | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 68bc706a-84be-3d9e-9129-7bf4932cd026 | -18.5504 | -47.46029 | 2025-09-02 03:53:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5435956b-8ab9-36f2-80d8-87d3754fbefd | -20.70217 | -46.30637 | 2025-09-02 03:53:00 | NPP-375D | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5a34539-459e-3196-a12f-c0c6b762c078 | -17.70184 | -46.89017 | 2025-09-02 03:53:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85045899-d01a-3fb2-83f4-556248c689ca | -14.79599 | -48.19738 | 2025-09-02 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 049287b5-d068-3e8e-8c58-7d695e394885 | -15.67952 | -48.94385 | 2025-09-02 03:53:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 158d9d80-49b8-38e4-b4aa-1d68c3be4134 | -15.55461 | -48.32672 | 2025-09-02 03:53:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0800bbf9-1e5c-3d49-a14a-24150f8da029 | -17.28205 | -49.19949 | 2025-09-02 03:53:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f397918-d92e-357a-83ae-5b4ab3aeb827 | -14.75199 | -48.15793 | 2025-09-02 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a9870aa3-d7ad-343e-8a33-ef30fcfe4145 | -15.57675 | -48.39125 | 2025-09-02 03:53:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2da2eb70-de49-317a-99f4-b5872ff7495f | -14.97528 | -48.17736 | 2025-09-02 03:53:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f571ef01-fdbc-3e51-8bf6-e77a3671109d | -17.88452 | -47.16431 | 2025-09-02 03:53:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1881f18a-6a36-3575-943a-26f37cddafe6 | -14.22914 | -51.66891 | 2025-09-02 03:53:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4b8fe79-2e2c-3618-986b-92f14b9eace9 | -14.79661 | -48.19432 | 2025-09-02 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 813e7bb6-b4ca-3967-88b1-b5b7b63d7d2a | -14.99136 | -50.19261 | 2025-09-02 03:53:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5bf3d6b3-498a-3876-97ed-ab30606420c0 | -14.79831 | -48.21354 | 2025-09-02 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 24319ce5-cf07-3588-9627-a6b984dff22a | -16.62816 | -44.58742 | 2025-09-02 03:53:00 | NPP-375D | SÃO JOÃO DO PACUÍ | MINAS GERAIS | Brasil | 3162658 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cb99b851-5dc3-3f91-aae5-a02291c248a3 | -16.85916 | -49.5761 | 2025-09-02 03:53:00 | NPP-375D | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 10.2 |
| b4f3c130-a1bd-3ccb-add6-b1882012555b | -15.79956 | -43.56999 | 2025-09-02 03:53:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7b5d604-f75e-3896-8565-c527f5b292a8 | -14.96028 | -50.07043 | 2025-09-02 03:53:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1bc5cf76-6d6c-3599-9ab5-6eccd1df7da9 | -16.0474 | -46.30442 | 2025-09-02 03:53:00 | NPP-375D | URUANA DE MINAS | MINAS GERAIS | Brasil | 3170479 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fc48864-fdd8-34e2-8002-46352602254d | -16.42947 | -49.89984 | 2025-09-02 03:53:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 977d55e1-490f-3113-823b-39de5ed8c035 | -18.5446 | -47.46436 | 2025-09-02 03:53:00 | NPP-375D | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fda33d0d-2887-37de-a827-4c834d5de088 | -14.79702 | -48.21992 | 2025-09-02 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 185765ac-25d1-35db-b12c-e8a3549bf013 | -16.07837 | -43.62454 | 2025-09-02 03:53:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 469068be-611d-3375-a36b-4f839d99e51d | -14.76616 | -48.15187 | 2025-09-02 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b50119d3-7a77-3827-90c1-4984257a9c18 | -19.81841 | -45.00792 | 2025-09-02 03:53:00 | NPP-375D | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2000e673-1687-3ec9-9a25-ef7798b6bdc3 | -17.89352 | -47.1683 | 2025-09-02 03:53:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 8b4e6d22-b39e-31c4-807d-72adea7c8310 | -20.69887 | -46.30056 | 2025-09-02 03:53:00 | NPP-375D | SÃO JOSÉ DA BARRA | MINAS GERAIS | Brasil | 3162948 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d9d85e8-d64e-33fd-bb35-f5e40ef6c74e | -14.23053 | -51.66242 | 2025-09-02 03:53:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f7feb30-c86f-3eac-8d53-c8b9f392484c | -15.55957 | -48.35732 | 2025-09-02 03:53:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5fa6850f-ebf7-3389-9b47-683d2abf7d73 | -15.55921 | -48.3315 | 2025-09-02 03:53:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a9f75a03-a6c5-332a-adb0-31f4a0047fa5 | -14.7914 | -48.19243 | 2025-09-02 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 543aedb9-2813-3cc1-9e9e-64096c7f54e7 | -18.07079 | -45.96163 | 2025-09-02 03:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 41f57ad6-6cdc-3a68-8a23-f1721dfef675 | -14.74787 | -48.1506 | 2025-09-02 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README27.md)
