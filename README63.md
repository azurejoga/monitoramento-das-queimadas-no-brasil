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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 01c72dc7-63fa-3e8a-92b8-760f184b5b3d | -15.69166 | -48.93949 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 651e9706-56b4-3e18-b6ec-43ed07a32434 | -13.47363 | -42.47651 | 2025-09-01 04:34:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 50f95881-029e-35f1-b83e-1f1a36368251 | -14.74784 | -46.77285 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 273ef288-e283-3a6d-b684-f214d807211f | -11.91372 | -44.88311 | 2025-09-01 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c14bf195-4536-3f92-8e94-e538360abfc0 | -13.57292 | -46.93684 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 59ab195f-64d7-3c73-b20d-fb6b2ca1a7d1 | -11.04883 | -46.90087 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 067b16ab-e1d7-3a01-a097-da1cc771e929 | -13.34412 | -47.04606 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ab3fd5c-02ee-3058-9494-3bb333647a26 | -15.70389 | -48.90415 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 04dbb21d-262d-34b7-844f-79ec75f27fc8 | -8.73566 | -62.40393 | 2025-09-01 04:34:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b9493149-4ec6-3ec3-a8c6-161110be2666 | -15.6964 | -45.40969 | 2025-09-01 04:34:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5e3f950a-ddee-3dd6-a317-c11ccaccb33a | -11.02938 | -47.02916 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 96035f32-0ad7-3816-bd4c-8a12a38b0896 | -11.89864 | -46.68479 | 2025-09-01 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9ade354d-9afb-3491-b0c9-51543d61bf88 | -8.75381 | -61.43925 | 2025-09-01 04:34:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 66327641-721e-39b1-8fcf-4302a3560b0d | -11.04938 | -52.03799 | 2025-09-01 04:34:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c91ae0dd-3de8-3f1b-be82-15fa8d3c3727 | -13.57222 | -46.9375 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37a3f9e3-7254-3874-a229-524113b1af92 | -11.63581 | -46.83831 | 2025-09-01 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 947056ac-739c-30e0-9a87-6cb3d4acbef5 | -12.866 | -48.16552 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 017179e3-8ca3-39a1-b030-4e9f04643520 | -13.39414 | -46.94864 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 434c6e94-fbbe-3619-abf4-f91274bd767b | -11.52283 | -54.46579 | 2025-09-01 04:34:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9fb9fae5-05d9-3d9e-8d33-1fa411bbbc8f | -13.36669 | -46.94019 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d695fdfe-7bf3-3b70-939e-6a782fb01940 | -14.74722 | -46.75183 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96912e45-0cfe-3066-ad54-55ed80c1f403 | -8.76404 | -61.4353 | 2025-09-01 04:34:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a78109e-e425-39e1-9084-b0c69c3bcce5 | -11.9561 | -45.85229 | 2025-09-01 04:34:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d3d0c443-eb0e-3393-aae9-e9bea8797a6a | -14.22918 | -48.05655 | 2025-09-01 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5f38dea-2b51-359a-80cd-114d8fff5417 | -10.27792 | -54.24987 | 2025-09-01 04:34:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cbdb32cb-a40f-3e49-84a3-c1a1fa9b7f4a | -12.55952 | -48.2211 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 202c691c-41f4-3542-8830-e26c79312a9f | -11.36962 | -43.58418 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df17c20a-ac01-3b3d-a53b-5d84bd7d549e | -13.32075 | -46.95405 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 037e71fa-048b-3166-be04-a24971a35efc | -12.951 | -48.10467 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 002e41f8-f8d9-30ad-9751-fd935385f61f | -14.04329 | -44.55489 | 2025-09-01 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f727963-67b1-32ac-9749-a240a05614a3 | -10.12607 | -58.01883 | 2025-09-01 04:34:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| beeb0205-cc5c-3c7b-a57f-50556e7846ac | -11.07101 | -52.06287 | 2025-09-01 04:34:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7665d4dd-9d0b-3340-bb8e-f5f27f08b493 | -12.58348 | -48.19907 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b3890602-ce16-3526-bd5b-4f863af43ed0 | -12.80922 | -48.07515 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 504ff41d-3a6c-3346-957a-4a4e8230b106 | -14.04377 | -44.5513 | 2025-09-01 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c19749b-332f-3989-b599-3b94e3d1ba19 | -14.76994 | -46.77201 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de93e66c-7dc1-3171-8d22-8a717dd055f7 | -11.8152 | -46.41653 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b79c8bf5-9700-35b7-ab79-ae0ecdb81f4a | -15.23143 | -53.79829 | 2025-09-01 04:34:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f150c21b-6683-3427-b719-edc332ebadfb | -12.59689 | -48.22339 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 14120b17-8e9c-38f1-a20b-3752e7c7a48b | -11.37428 | -43.58093 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9d13edaf-5dff-3af2-a5da-e68d9605f5df | -15.29669 | -52.79259 | 2025-09-01 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7e883280-a07d-329a-93bd-a0eb2f0af857 | -14.79597 | -46.73074 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e09171e1-ce68-3b63-911a-5e6593f2c093 | -11.9124 | -46.44299 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 42340e7c-ee8d-31e5-b73b-906f0cb35aec | -16.15101 | -49.637 | 2025-09-01 04:34:00 | NOAA-20 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 21ca8c3f-9720-3fe0-ab35-2090df4a336a | -11.6019 | -51.94447 | 2025-09-01 04:34:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd888260-ce9d-3e2b-8c72-49a49bfc7080 | -14.79053 | -46.74332 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 993a91c7-975d-3c08-98f2-e6d211fbb625 | -15.29172 | -52.80031 | 2025-09-01 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e7907654-ef63-380f-9a52-d2506f01d913 | -13.31087 | -46.8996 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5814322-6ae4-319a-a3a7-1f7a5dc1eb4f | -15.71169 | -48.89803 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22008bae-96bd-3a98-89cc-b3c55bd330e0 | -11.03167 | -46.99097 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57601551-35da-33a8-a677-85ead2551ab7 | -12.60637 | -48.20643 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5957d18b-51b3-37f0-930d-f212fa78773f | -10.24631 | -51.11442 | 2025-09-01 04:34:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 42424620-11c4-3c9c-bbda-70a915c0854e | -12.87662 | -48.16352 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 82166b2f-c6bf-3b60-9c55-53b2faa343e5 | -13.69338 | -46.87656 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c995cbc9-879b-3b31-bf3e-4f210df864e2 | -14.76755 | -46.76327 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 267d52ac-7c72-3b25-be90-1f24759938b4 | -16.13331 | -49.04702 | 2025-09-01 04:34:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9dcec61e-579b-386c-98d9-c650c544deca | -15.15486 | -52.34547 | 2025-09-01 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba16e613-ff60-3cb6-8fa4-ccc59fc89331 | -11.91301 | -46.43895 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75d77d21-20d3-3ae9-a0e1-0918c8b6efc5 | -15.58374 | -48.3314 | 2025-09-01 04:34:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 3f53faa7-f7b3-3e58-b990-7ce223f22717 | -11.36857 | -43.59183 | 2025-09-01 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c40c7dfb-63a6-3a89-a98f-ffd365d32817 | -12.91587 | -56.98294 | 2025-09-01 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 420ecfcb-dd61-36a6-a166-bbb5fb90acfb | -15.73016 | -48.97926 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4a799086-2dd9-3cbd-8870-4fddf9abad82 | -11.92023 | -46.68383 | 2025-09-01 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ebd38378-bfe9-39ab-9c14-cdc1fd19f7ba | -15.70113 | -48.92231 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38ce8965-b7a2-306a-a44f-acd1fad938a9 | -14.7556 | -46.76989 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f3cd8470-5ec0-36d9-ab27-87ef51b561dc | -12.95772 | -48.10579 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25c5a87b-94a1-3308-a233-8cfceb601414 | -12.61138 | -48.19615 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6a60aaf0-7133-3301-b088-1db4f530158e | -14.75142 | -46.77343 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 14c49caf-1e54-3800-a234-45eb3bcbcdb7 | -14.74427 | -46.74693 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f14403ee-104a-3249-a1f5-c1ee4082b8a9 | -12.94148 | -48.09941 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a14ef042-fb6b-3576-9421-3fefa7979495 | -11.07319 | -52.07193 | 2025-09-01 04:34:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ee528bf3-17d4-3ee8-82e7-5f453b92450f | -11.04596 | -46.89656 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 249beb16-0257-3905-8741-00b53040b724 | -12.60135 | -48.21672 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| c8206761-85e5-3b8f-a8b1-d7be1f492ea1 | -11.87368 | -46.73311 | 2025-09-01 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7f942e2e-2d00-3192-9e1c-b8f0e386194c | -15.68891 | -48.95753 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5ee6c76b-6587-355d-99a3-2e54cc5e0299 | -11.26308 | -44.93121 | 2025-09-01 04:34:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a543b25f-09dd-3d12-9b7d-f23f1986271c | -12.56732 | -48.21496 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7acd52cb-cdcf-39b7-a00e-6d5c367d1df1 | -14.04537 | -44.5699 | 2025-09-01 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d392b08-7086-310e-b230-f5de5014b997 | -12.56119 | -44.78968 | 2025-09-01 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ca8a4b72-abc0-363c-b520-6ac70f12e948 | -11.01966 | -46.95431 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c77d56dc-c571-324c-a81b-550c219e461a | -14.55979 | -52.99186 | 2025-09-01 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22afed21-23da-3fde-b2c7-df9f53d3b094 | -14.74661 | -46.75603 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0bde1a39-08e7-37a6-af0a-35984eecd12c | -11.62646 | -47.12901 | 2025-09-01 04:34:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 89ef1ad1-bde9-3539-b797-382efde27364 | -15.75559 | -47.75898 | 2025-09-01 04:34:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07d1a748-f819-3d2e-aeb6-2955446139b9 | -15.69055 | -48.94675 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d8987f25-84ed-3513-b0b4-5d917675d617 | -13.54338 | -46.96229 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d5428603-ff93-3128-9d15-cc4cc087b063 | -11.80623 | -44.9435 | 2025-09-01 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7c0d9a9-f312-3b02-885b-05b266e39574 | -12.61217 | -45.51482 | 2025-09-01 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6f91482-291e-38cb-9538-fd8486952175 | -15.21258 | -52.34281 | 2025-09-01 04:34:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b879bbdd-9480-3bb4-b6c7-d45badcde967 | -15.72288 | -48.93712 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8cf6cced-1897-3836-841d-92329e7f9cd8 | -13.67011 | -46.93593 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9052fdfa-e98d-3c97-85fd-b005ffb3cea7 | -11.89292 | -46.74772 | 2025-09-01 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1fbdb7d3-1963-375c-8aa0-d89029dcddff | -14.79097 | -46.72847 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 746e6b46-9e60-3c5d-b2d9-45bcfc612e9e | -15.69667 | -48.90649 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 55a9de4d-b3b3-3fef-bba8-a397653dd824 | -12.57902 | -48.20574 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 8477d15d-055a-3cc9-879f-8326d6460142 | -14.75377 | -46.75718 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 14.5 |
| a104f005-dd75-3b10-a9d1-0915f2fcf9ed | -13.6902 | -46.87355 | 2025-09-01 04:34:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9f7264f-a90e-3526-ab1f-340aa8fb1d72 | -12.60411 | -48.1765 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd621f63-5c1e-3525-8547-897c839ef793 | -13.48644 | -46.93471 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a0edd7ec-578a-39fa-b174-c8b190a57775 | -13.36526 | -54.38713 | 2025-09-01 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README64.md)
