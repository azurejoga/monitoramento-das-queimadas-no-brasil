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
| 2ffe1aad-771c-3f48-b99b-b92d19b025dc | -10.26084 | -36.54016 | 2026-10-02 03:55:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 8f961add-842c-3987-b397-2abfa23d9189 | -11.70273 | -43.50878 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c4983b70-9c0d-32a1-aa4c-f04ee5846d9a | -10.92452 | -43.84371 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e82828e6-2038-372b-9115-6d822ea54767 | -8.02754 | -47.46853 | 2026-10-02 03:55:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 719a7f1d-fd22-35b7-9b07-87c7fd26fd29 | -11.73162 | -43.44778 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d790a4c-7d8a-38f4-82b5-5fd68b6aca4f | -10.91186 | -43.83979 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b6baf680-4ceb-3cfe-8085-d2199da1f821 | -15.61027 | -42.39715 | 2026-10-02 03:55:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78bcc90f-0885-3d77-87f0-e18de808489c | -13.48979 | -42.50539 | 2026-10-02 03:55:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a42539af-24be-37d6-820d-206202890984 | -10.52621 | -43.50406 | 2026-10-02 03:55:00 | NPP-375D | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ccfafd74-f861-3178-a4f1-3ecf31045b68 | -11.74726 | -43.44723 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c2edc623-3d6e-38d4-838f-b82c68a1cc34 | -8.74611 | -47.58749 | 2026-10-02 03:55:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4e814e61-3ff1-38ee-bd23-b63aea465316 | -12.55042 | -46.79806 | 2026-10-02 03:55:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0060aa29-34fe-3a1a-ae58-1f21b4fff889 | -13.48009 | -42.48711 | 2026-10-02 03:55:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0370e90f-c319-33d3-8418-fc13fb91b777 | -11.73345 | -43.44461 | 2026-10-02 03:55:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a08a5db7-7b07-3bb8-b0d6-f7e3ea1fa57f | -15.25434 | -46.15225 | 2026-10-02 03:57:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| da0d3650-e3a7-3d36-ae6f-6ad5daf21116 | -15.92089 | -43.52277 | 2026-10-02 03:57:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c159a6ba-f929-3eac-bd6b-d63c017e8824 | -17.22669 | -41.20136 | 2026-10-02 03:57:00 | NPP-375D | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 851cbf56-4a86-3bb9-a1fc-647b51a9ab74 | -19.0323 | -45.65088 | 2026-10-02 03:57:00 | NPP-375D | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f38c1c41-2b63-314c-b34e-2314506eb654 | -17.44424 | -41.91628 | 2026-10-02 03:57:00 | NPP-375D | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5158f0ee-b030-3bd3-88cb-b6dd418827fe | -16.99836 | -41.18017 | 2026-10-02 03:57:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 534fc768-9e06-3355-8177-45a3253bb2c9 | -17.70942 | -39.75893 | 2026-10-02 03:57:00 | NPP-375D | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 6e7ed230-276c-3e3b-b0d2-82e1ddd7dd2c | -16.99389 | -41.18398 | 2026-10-02 03:57:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ffc4b41c-5b11-3b12-bf1a-a6ddfffd4c5b | -17.21777 | -41.20895 | 2026-10-02 03:57:00 | NPP-375D | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 2157780f-0537-3891-8e64-a883ff349a58 | -15.24917 | -46.15125 | 2026-10-02 03:57:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 640350d1-27fe-38d2-ac9a-25a9d984881e | -19.26063 | -44.34643 | 2026-10-02 03:57:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d74f25ea-db55-3ddb-96ac-fdc679c76929 | -18.33722 | -40.0601 | 2026-10-02 03:57:00 | NPP-375D | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| baf17892-f909-395c-abb6-ddfe413af32c | -16.1326 | -43.7439 | 2026-10-02 03:57:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 355c168b-6873-3ac4-908b-be2a053f71fe | -15.58501 | -44.40417 | 2026-10-02 03:57:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1307196b-bf53-3ca9-a28f-edd0b7eba060 | -16.99757 | -41.18468 | 2026-10-02 03:57:00 | NPP-375D | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 56fca96f-ba5d-30d5-8f72-a0d0cc50c475 | -17.71286 | -39.75956 | 2026-10-02 03:57:00 | NPP-375D | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 6fd95460-c779-3b7a-a491-5d2791621336 | -16.52149 | -46.8656 | 2026-10-02 03:57:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 094778c0-cce2-319b-a4ea-6d51b579fb56 | -17.71008 | -39.75501 | 2026-10-02 03:57:00 | NPP-375D | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| a62dd4c6-90b7-3c79-b022-1293ecad0665 | -15.25041 | -46.14512 | 2026-10-02 03:57:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5dc4874b-9b86-3a0d-9a5f-ab81855c5166 | -17.44044 | -41.91555 | 2026-10-02 03:57:00 | NPP-375D | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| fd1cf9e7-6c82-3be7-a744-f0f2c1c42d54 | -15.24631 | -46.16539 | 2026-10-02 03:57:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6c580a6-78c7-3467-916c-538ed2877108 | -17.10129 | -41.92258 | 2026-10-02 03:57:00 | NPP-375D | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0dcc28ba-d824-365c-9654-7228cb2a4425 | -17.44131 | -41.91866 | 2026-10-02 03:57:00 | NPP-375D | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 4be22ebf-a9cf-3557-be97-7c655ae46434 | -15.26062 | -46.14775 | 2026-10-02 03:57:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1cb89ed8-2b89-3648-a5fb-4917b7a024b7 | -17.56378 | -44.75521 | 2026-10-02 03:57:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| eb34caaa-d2ff-38e9-90d6-f33f40512160 | -16.86086 | -40.57355 | 2026-10-02 03:57:00 | NPP-375D | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 599b5cec-72c3-3626-8768-7318fb4ae774 | -19.02768 | -45.64975 | 2026-10-02 03:57:00 | NPP-375D | ABAETÉ | MINAS GERAIS | Brasil | 3100203 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e472a693-6a5e-3752-acfd-6c4a97d3cf2b | -17.2141 | -41.20823 | 2026-10-02 03:57:00 | NPP-375D | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| ea404967-5ef1-3571-9be6-4544828746cb | -17.21696 | -41.21359 | 2026-10-02 03:57:00 | NPP-375D | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 34ba458d-7e7e-3438-b1ca-936f6a29da61 | -16.1214 | -42.22529 | 2026-10-02 03:57:00 | NPP-375D | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 073bff74-df26-3274-ba98-73a4622fb89a | -15.26004 | -46.15063 | 2026-10-02 03:57:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1a0e7a01-eec7-3543-9560-8c3f11979e84 | -17.71353 | -39.75565 | 2026-10-02 03:57:00 | NPP-375D | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| fe32db08-eec0-32df-90b9-2bc43383f5ee | -18.94714 | -41.00965 | 2026-10-02 03:57:00 | NPP-375D | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 19ba54dc-d810-3efe-b52a-12a7b4954db2 | -15.58595 | -44.39934 | 2026-10-02 03:57:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4538e106-35f4-3ffb-a4e3-753da4565c6c | -16.86013 | -40.5778 | 2026-10-02 03:57:00 | NPP-375D | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 40694e5c-b74b-3dd6-9f16-3cc7a35b966d | -17.21858 | -41.20434 | 2026-10-02 03:57:00 | NPP-375D | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 0fe72d62-0ef7-3f9d-97b0-b73dcaaf8287 | -16.90903 | -42.11468 | 2026-10-02 03:57:00 | NPP-375D | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| d04f470b-1007-35f1-b2cf-f42e0f33b49d | -16.1369 | -43.74497 | 2026-10-02 03:57:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5ab8b81d-8e16-3ea3-b2b8-f4a7cd15c642 | -15.25493 | -46.14935 | 2026-10-02 03:57:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 74d00932-5e99-3347-aeb6-24d69e2e6212 | -16.85657 | -40.57696 | 2026-10-02 03:57:00 | NPP-375D | BERTÓPOLIS | MINAS GERAIS | Brasil | 3106606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 726301d8-23e1-3d8d-ab8a-7b1718157699 | -15.25083 | -46.16967 | 2026-10-02 03:57:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 294a0fad-2f47-3879-8242-330a3e7fbe78 | -15.2498 | -46.14814 | 2026-10-02 03:57:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bccd661a-ee57-3ca3-815a-73e3f486297f | -19.25935 | -44.3429 | 2026-10-02 03:57:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05a1a8bd-ec2d-333d-9003-93e14789fa89 | -16.14212 | -43.74124 | 2026-10-02 03:57:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c27de07-e8d6-3f40-b22a-ea3ea9e36e36 | -19.3257 | -45.08001 | 2026-10-02 03:57:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fdb224e7-059d-37b4-ad06-67e1057db413 | -17.44218 | -41.91371 | 2026-10-02 03:57:00 | NPP-375D | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3ffc3634-7b86-3373-80c4-0ead1d20d75b | -16.1412 | -43.74608 | 2026-10-02 03:57:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c2dd69c6-1316-34e4-b885-b259018e77e5 | -15.25551 | -46.14646 | 2026-10-02 03:57:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1fe32fd4-8760-34ea-99e2-eabe38b582cb | -19.04497 | -45.66024 | 2026-10-02 03:57:00 | NPP-375D | CEDRO DO ABAETÉ | MINAS GERAIS | Brasil | 3115607 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 35c3238f-b588-3f58-8410-f55be7db1567 | -15.24183 | -46.16095 | 2026-10-02 03:57:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e89d009-a760-3bb8-a61e-58bd04663b85 | -16.9031 | -42.10309 | 2026-10-02 03:57:00 | NPP-375D | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 7b563854-0833-36b2-831c-9ee6ce343899 | -6.3952 | -56.4158 | 2026-10-02 04:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| b6fe67c6-5c17-343b-ae77-d23ae7fa03eb | 1.8037 | -55.5854 | 2026-10-02 04:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 343d2419-7e06-3ce2-b908-383b06517bc2 | -3.1299 | -53.7633 | 2026-10-02 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 681b2ae0-6b4f-3e85-bd32-8110f1267edc | -2.0393 | -56.8789 | 2026-10-02 04:00:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 991d0826-7558-3906-9092-effc80fda33f | -3.1483 | -53.7426 | 2026-10-02 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 5536f14e-6326-3172-b8d7-6b9679756735 | -11.6771 | -43.587 | 2026-10-02 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| b087377c-71a8-3eda-b85d-73d010bf4ce2 | -7.3846 | -55.2124 | 2026-10-02 04:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 91.9 |
| edb765fa-45f5-344f-9def-2e3b9a62fa2a | -5.7355 | -43.2916 | 2026-10-02 04:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 525289af-3aa7-388c-8c33-f9f851bc4504 | 1.8221 | -55.5851 | 2026-10-02 04:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 40.0 |
| be0ab995-5cf8-3ec3-a49c-1acde0058d54 | -11.7348 | -43.578 | 2026-10-02 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 5ef70f03-1f7e-3a11-9c13-1c789e042f01 | -4.2676 | -50.7506 | 2026-10-02 04:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| f97c3b42-338b-3ea2-b236-bc99c9860008 | -2.0576 | -56.8786 | 2026-10-02 04:00:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 6c3ce4c5-4b1c-3f04-ac96-9c4978fdc3bb | -11.6767 | -43.6106 | 2026-10-02 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 8b9374e8-dfb0-3856-a563-b44c90444ae2 | -11.6387 | -43.5929 | 2026-10-02 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 3944a196-729d-3fce-b105-4c2640fbdf13 | -7.8682 | -44.169 | 2026-10-02 04:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 761dcfeb-06de-309d-ab37-1ba74bf22e96 | -10.2678 | -49.6616 | 2026-10-02 04:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| abddf6cf-dd0c-3a46-8084-a2128cc72e46 | -3.1655 | -54.0844 | 2026-10-02 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 6c157a69-949b-3719-aa16-4fb3c5b22844 | -4.4507 | -47.9112 | 2026-10-02 04:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| f2e8a05c-b978-33c9-974f-18924ed153c0 | -11.7541 | -43.5749 | 2026-10-02 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 180.0 |
| 048a40af-7196-32af-9d32-08017dccf6f6 | -7.4031 | -55.2114 | 2026-10-02 04:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 71bf6660-4c75-3cc0-89a5-d8eae02792d2 | -6.914 | -43.6816 | 2026-10-02 04:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 92f52230-c5c4-3bbc-8e36-8e6b5c6b8b08 | -11.6579 | -43.5899 | 2026-10-02 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 332.1 |
| 67a62837-e59e-38bd-ad7a-314900d7c4ef | -3.295 | -53.8597 | 2026-10-02 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 80042aa5-9861-355c-a7cc-c19f417aae89 | -11.1615 | -44.6002 | 2026-10-02 04:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 168.8 |
| 37f214a7-1e03-3441-9996-1471699906f1 | -11.7733 | -43.5719 | 2026-10-02 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 25601054-750e-371d-b9dd-80c593cedf0e | -11.142 | -44.6261 | 2026-10-02 04:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| beda66b5-b463-391f-b440-b4b804d068c2 | -4.4506 | -47.9329 | 2026-10-02 04:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 40393539-7b29-3229-bf7a-157773bf8eff | -3.2767 | -53.84 | 2026-10-02 04:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 0aaa95ca-af7d-3f7c-8211-c991d2da31c6 | -6.1487 | -47.2651 | 2026-10-02 04:00:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 7ba76235-86ac-31ce-b42a-1a9b3d87accf | -12.825 | -51.4466 | 2026-10-02 04:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 477f8476-813f-3162-ba41-e1add8e6afb7 | -12.8059 | -51.4489 | 2026-10-02 04:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 77b55615-6e05-3322-9935-d9596588da06 | -11.6575 | -43.6136 | 2026-10-02 04:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 249.4 |
| 86d72f3c-28c8-3800-9835-b5f3d153145a | -11.1611 | -44.6234 | 2026-10-02 04:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 190.8 |
| 3e23887a-4482-3718-8cc9-04bbf68cae93 | 1.8037 | -55.6051 | 2026-10-02 04:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 41bd95bb-52ba-3688-9cb6-0f7c6bc2b13d | -5.7563 | -45.152 | 2026-10-02 04:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |


[Clique aqui para ver as próximas entradas](README34.md)
