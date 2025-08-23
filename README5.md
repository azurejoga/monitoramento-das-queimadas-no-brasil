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
| 288aaa71-267f-36c9-a4fd-71cd6dc41af4 | -9.2095 | -59.4609 | 2025-08-23 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 6b0f6080-826a-3d06-a0a9-816105de1eb7 | -17.5779 | -46.5756 | 2025-08-23 00:20:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 3f8f5137-8d46-35d6-b6af-6be68b30cce8 | -17.5985 | -46.5481 | 2025-08-23 00:20:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 2f86008d-6282-380f-87dc-482fd27585a5 | -9.1898 | -59.5977 | 2025-08-23 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 5a5638f1-615c-3b69-9733-c398d268e8d2 | -9.4452 | -47.6364 | 2025-08-23 00:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 177a11d2-543f-3ee8-a525-71b2f6940fd7 | -13.0114 | -45.222 | 2025-08-23 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 2a093c8e-b944-3324-9491-bc05493eb18d | -18.9683 | -46.9278 | 2025-08-23 00:20:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 80.9 |
| f5f75af2-2302-38ee-8c15-0007dcd78144 | -5.7429 | -57.6009 | 2025-08-23 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 223.2 |
| 2fd22032-dd61-310d-b969-5d5e046ce2fd | -19.638 | -46.0676 | 2025-08-23 00:20:00 | GOES-19 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 48.1 |
| dff7c3b9-aa2e-3d49-a78c-b668be1f4ed8 | -14.2934 | -58.5449 | 2025-08-23 00:20:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 9f7ddcb9-7284-313b-99d7-c2baae837695 | -3.4254 | -49.0517 | 2025-08-23 00:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 74f19c1f-3c55-3ddc-9be4-c5956e7ada2f | -17.3395 | -46.5786 | 2025-08-23 00:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 6026bc53-298f-36f1-b089-a625fc74f51b | -6.4324 | -41.2357 | 2025-08-23 00:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 79.1 |
| 11fa0797-8ab4-3e20-ba5d-12597728c021 | -12.9921 | -45.2252 | 2025-08-23 00:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 2831440b-ae67-3f4f-a761-7d9e58fe855c | -7.2157 | -45.307 | 2025-08-23 00:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| e7106d23-33f9-313b-92c0-de1bdb791a61 | -15.0186 | -54.8735 | 2025-08-23 00:20:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 6932eb97-6d2c-3053-a5e4-bb08f3424b95 | -3.444 | -49.0297 | 2025-08-23 00:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| a2ea6474-72f4-3593-bc32-d723221cae1f | -19.73 | -45.6884 | 2025-08-23 00:20:00 | GOES-19 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 106.1 |
| e84525fc-cf41-3f66-85a9-27c07bf667fb | -5.7431 | -57.5814 | 2025-08-23 00:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 169.4 |
| 39a154d9-25e1-314a-b105-a669c8ff58ea | -15.1984 | -48.2296 | 2025-08-23 00:20:00 | GOES-19 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 85a540fc-3673-3c20-9ad3-f9d2bf6f1c83 | -17.2757 | -46.7538 | 2025-08-23 00:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 94.5 |
| e9c2d751-285f-3eb5-abd1-0abcafb8a1ff | -9.1895 | -59.6364 | 2025-08-23 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 105.7 |
| 4c9fdbf0-9d1b-32ac-b2f8-51b5449e65d9 | -9.2083 | -59.6161 | 2025-08-23 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 5ed29a49-62ef-3b82-883b-b1f5b1579249 | -9.2391 | -60.4834 | 2025-08-23 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 23f3b6e8-c93e-3837-b737-83ff30e051fa | -6.5781 | -59.871 | 2025-08-23 00:20:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 0a1dc37b-d60a-3837-bd7e-a31622aab542 | -8.8921 | -62.4297 | 2025-08-23 00:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 637d7db7-e483-3eaa-8ffe-2afe80852618 | -7.7945 | -63.5663 | 2025-08-23 00:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 091517a9-15d2-3d6c-bd9e-5ff8dc573af4 | -9.4449 | -47.6585 | 2025-08-23 00:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| af99c964-98b2-370e-974c-53006640f1a4 | -15.2284 | -53.8691 | 2025-08-23 00:20:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 99021124-1c6a-32f7-9e76-bb90b8ef6d60 | -9.4638 | -47.6565 | 2025-08-23 00:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 84de1d4d-6346-3970-842f-c9cb82ad2849 | -21.4767 | -47.4159 | 2025-08-23 00:20:00 | GOES-19 | SANTA ROSA DE VITERBO | SÃO PAULO | Brasil | 3547601 | 35 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 45ecf31d-fb6a-3c32-8ee6-921eee169e24 | -17.5785 | -46.5523 | 2025-08-23 00:20:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 59.7 |
| 80f51e34-7305-33d0-a67e-5113598674c3 | -29.0074 | -49.4984 | 2025-08-23 00:20:00 | GOES-19 | ARARANGUÁ | SANTA CATARINA | Brasil | 4201406 | 42 | 33 | nan | nan | nan | Mata Atlântica | 113.2 |
| e1cc2db3-60ed-3890-9e27-536500567b56 | -9.1897 | -59.6171 | 2025-08-23 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 157.1 |
| 8127ff5c-8ff4-3ef2-a09a-af522d9112e7 | -6.5856 | -44.564 | 2025-08-23 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 46.8 |
| f4eda286-fbeb-3b44-b2dd-d3eaf33742b4 | -6.8733 | -59.8213 | 2025-08-23 00:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 7e61b6b0-430c-35ba-8875-672b2c843f13 | -7.8131 | -63.5468 | 2025-08-23 00:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 8c7e2e51-69e5-3445-b0cc-907b8aeadda8 | -6.4138 | -41.2132 | 2025-08-23 00:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 161.4 |
| 1226b6a6-65ae-3411-89f4-f80ba138d0cf | -20.0976 | -47.7442 | 2025-08-23 00:20:00 | GOES-19 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 58.8 |
| c2bd5a5c-9f3c-3ac4-9b92-34980a036492 | -18.9689 | -46.9043 | 2025-08-23 00:20:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 4139ced9-a016-39d8-a91f-b041c3083992 | -9.1712 | -59.5987 | 2025-08-23 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 502ab549-3593-3f05-bc9f-5a9afb10153b | -6.6044 | -44.5624 | 2025-08-23 00:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 109.9 |
| 3efefb72-816b-3a57-85da-74ccc2ce9d50 | -6.4327 | -41.2114 | 2025-08-23 00:20:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 284.4 |
| 089298e0-344d-3f43-8d54-994dea2c3898 | -20.0766 | -47.7723 | 2025-08-23 00:20:00 | GOES-19 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 40.6 |
| c736979e-0bf5-3fc3-a44d-834cb48ced64 | -29.0083 | -49.4735 | 2025-08-23 00:20:00 | GOES-19 | BALNEÁRIO ARROIO DO SILVA | SANTA CATARINA | Brasil | 4201950 | 42 | 33 | nan | nan | nan | Mata Atlântica | 103.6 |
| ad412cdb-9405-3c5d-86df-d02121aab8b3 | -9.1909 | -59.4619 | 2025-08-23 00:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.5 |
| ce43b976-1444-3778-9749-14bd66ea3aae | -6.4136 | -41.2374 | 2025-08-23 00:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 65.1 |
| e33faa4a-5844-3d05-922d-aa635e0e1783 | -19.638 | -46.0676 | 2025-08-23 00:30:00 | GOES-19 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 90dd7d97-5b66-3ab0-96e4-cc45473c3c87 | -9.4452 | -47.6364 | 2025-08-23 00:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 5d74f926-fb8a-3e41-8240-42814ce31968 | -7.8131 | -63.5468 | 2025-08-23 00:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 74.3 |
| b0ccb736-bcf2-331b-ab87-e818e7cdda54 | -6.5781 | -59.871 | 2025-08-23 00:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| a23ea1ef-d8f2-3151-b347-7bd71852ae12 | -5.7429 | -57.6009 | 2025-08-23 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 177.1 |
| e5ffd2b1-b9c5-38b2-9849-24110d19e722 | -15.2288 | -53.8481 | 2025-08-23 00:30:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 44c15a79-7672-375f-836b-bcfe22455c92 | -9.4449 | -47.6585 | 2025-08-23 00:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| b2e958aa-c752-3d39-b67d-f8906a2147e0 | -17.5985 | -46.5481 | 2025-08-23 00:30:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 130.4 |
| c12fa002-d498-3b7f-ac3a-45efacfdcf21 | -3.4439 | -49.051 | 2025-08-23 00:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| edd25525-8523-3c6d-9802-17280d5fe0ff | -17.2751 | -46.777 | 2025-08-23 00:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 50d2cfba-34ec-318b-8496-765f8abe1091 | -14.3317 | -58.5414 | 2025-08-23 00:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| d4684f37-7271-3682-9184-d28e974c4c21 | -5.7614 | -57.6002 | 2025-08-23 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 123.4 |
| ee39d064-e61f-36d2-96af-349f54492846 | -17.2757 | -46.7538 | 2025-08-23 00:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 103.9 |
| be6f9fa3-89b6-303b-9aae-22254d1518b5 | -14.3123 | -58.5631 | 2025-08-23 00:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 251701a5-d134-34af-b503-0d648370db37 | -3.444 | -49.0297 | 2025-08-23 00:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 6c505fff-54fe-3cee-b2d0-60047b44879b | -9.1897 | -59.6171 | 2025-08-23 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 133.2 |
| 7497070e-8322-3411-9d45-fba4a755f6f6 | -17.5785 | -46.5523 | 2025-08-23 00:30:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 573a009b-074f-327e-a74b-a5d5b7dd0577 | -6.4327 | -41.2114 | 2025-08-23 00:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 185.0 |
| 40a1035a-41f4-3042-8428-9c1fd80ffb89 | -14.2926 | -58.6048 | 2025-08-23 00:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 51.6 |
| 118a8124-d059-3a5e-a1fe-bf6fd4d7e4bf | -10.6122 | -55.413 | 2025-08-23 00:30:00 | GOES-19 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 93.8 |
| d8d4e90d-3f95-39e5-bc80-1e245659d2d1 | -15.2284 | -53.8691 | 2025-08-23 00:30:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 48fcbbbe-62a4-39f1-b109-78f96405830f | -9.1895 | -59.6364 | 2025-08-23 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 42f614ac-a081-3eb4-968a-943111f4e08d | -9.1712 | -59.5987 | 2025-08-23 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 291e3d16-27ce-3892-bf51-20aa3f498f56 | -9.2391 | -60.4834 | 2025-08-23 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 53f47a3a-bcb0-38b0-be01-d95e71979ea4 | -14.3126 | -58.5431 | 2025-08-23 00:30:00 | GOES-19 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 176.6 |
| 52f363e1-39b8-3fb6-82f6-f0fa9da06fcc | -8.8921 | -62.4297 | 2025-08-23 00:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 109.8 |
| e64cf62e-9def-3b50-ab6d-8f4e916cf459 | -11.6423 | -51.5819 | 2025-08-23 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| dbf9bd25-4b77-3ff1-8a33-b83ea19367bf | -12.9921 | -45.2252 | 2025-08-23 00:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 19bb274c-bcc4-3155-969c-3f88aef0ec95 | -9.1909 | -59.4619 | 2025-08-23 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 8be33b4d-6d3b-330a-9653-51e91677bf23 | -6.4324 | -41.2357 | 2025-08-23 00:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 82.6 |
| 93d44ef1-7693-3ed6-90d6-3f6d7f37aecf | -11.6613 | -51.5798 | 2025-08-23 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| bf833fb5-ee1c-3f67-b851-ac1059736c3a | -5.7615 | -57.5807 | 2025-08-23 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 8e04500b-ebca-382d-9906-7a6a908cc3dd | -7.813 | -63.5656 | 2025-08-23 00:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 161.0 |
| 6140878c-1c4d-3e7f-a8ec-fb75a0483b5a | -6.8733 | -59.8213 | 2025-08-23 00:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 5333c008-d9a8-3d45-9272-5cebcee9e18c | -17.5979 | -46.5715 | 2025-08-23 00:30:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 114.9 |
| 44b940b7-bf3b-3fd1-9e6b-b3dafea95429 | -9.1711 | -59.618 | 2025-08-23 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.9 |
| a4e609c9-356d-35f6-90f0-8c1252a451c3 | -20.0976 | -47.7442 | 2025-08-23 00:30:00 | GOES-19 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 39.8 |
| c0672b25-aba3-389a-a202-db79a373db62 | -19.73 | -45.6884 | 2025-08-23 00:30:00 | GOES-19 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 124.4 |
| cf423671-4ff7-3c82-a9f8-b1f320c122f2 | -5.7431 | -57.5814 | 2025-08-23 00:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 141.1 |
| 2a46f5ae-fd9d-3b6f-8630-917a13f0597a | -9.2083 | -59.6161 | 2025-08-23 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.9 |
| ff8594f9-29e3-3188-9ae8-ad97cb0f2797 | -6.4138 | -41.2132 | 2025-08-23 00:30:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 184.0 |
| 83be7dec-beb3-3bbb-a412-534439533891 | -9.2095 | -59.4609 | 2025-08-23 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 3cef9376-be03-34ba-bae0-deb1eb13251b | -20.097 | -47.7676 | 2025-08-23 00:30:00 | GOES-19 | ARAMINA | SÃO PAULO | Brasil | 3503000 | 35 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 05d4ee44-ff11-377a-9edd-aa6eda2dd344 | -19.638 | -46.0676 | 2025-08-23 00:40:00 | GOES-19 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 64.0 |
| c7be810a-fcc5-381c-9c19-ba0ba78406af | -9.5177 | -60.5653 | 2025-08-23 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 161.9 |
| 28762d1d-5cf6-3e36-8340-ca556ebc66ce | -9.2083 | -59.6161 | 2025-08-23 00:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 1082717c-bf10-3976-b15d-a98a2290a7ad | -9.5366 | -60.5258 | 2025-08-23 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 98.3 |
| 9986724d-83f1-395c-a19a-ca2132e58d7d | -9.4991 | -60.5663 | 2025-08-23 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.1 |
| dd36b2d0-9523-3fbe-b9ae-12a974612306 | -19.73 | -45.6884 | 2025-08-23 00:40:00 | GOES-19 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 144.4 |
| a27a4ef8-e25c-3154-becd-e3654e1d9a2a | -7.0352 | -44.6396 | 2025-08-23 00:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 96.6 |
| c57f0370-e30c-32f3-8f18-fc77c69a9e00 | -17.5985 | -46.5481 | 2025-08-23 00:40:00 | GOES-19 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 154.1 |
| e2798c30-0772-3b42-8d32-9de9e3bb5b9d | -5.0992 | -43.2211 | 2025-08-23 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 76d6ce9c-537d-3ab4-b4d8-819db8a7d098 | -12.9921 | -45.2252 | 2025-08-23 00:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |


[Clique aqui para ver as próximas entradas](README6.md)
