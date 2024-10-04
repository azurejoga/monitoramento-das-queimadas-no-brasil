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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90a3450c-f18c-3da4-ab05-e912b0f08c42 | -13.984 | -44.0474 | 2024-10-04 00:06:24 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 95140e8f-22ca-3f40-af77-59c53b5b67d8 | -13.9845 | -44.0236 | 2024-10-04 00:06:24 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 149.8 |
| a4173caa-f5f6-39f8-8242-1f6d1b46dfed | -14.004 | -44.0201 | 2024-10-04 00:06:24 | GOES-16 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 46d1c598-c742-3712-ac56-535333e69505 | -16.1094 | -50.4489 | 2024-10-04 00:06:36 | GOES-16 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 54182635-c7de-3b64-bd3b-fda57da77d19 | -16.1098 | -50.427 | 2024-10-04 00:06:36 | GOES-16 | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 5bebfe74-1c71-3b29-a904-fd9263dff3aa | -16.3956 | -57.3845 | 2024-10-04 00:06:38 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.9 |
| 58277738-9112-3128-8024-8b9e5e1cc5b1 | -16.4148 | -57.4028 | 2024-10-04 00:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.7 |
| db8ceaaa-ca13-34e3-96ed-08559f5a6938 | -16.4151 | -57.3823 | 2024-10-04 00:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 99.2 |
| 2f1fdf50-9980-37b0-a06b-d649c4450143 | -16.4347 | -57.3802 | 2024-10-04 00:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.5 |
| 3d839d83-4490-319e-9d6a-37ec770b6b2c | -16.4554 | -57.2962 | 2024-10-04 00:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.8 |
| 7d259495-8193-3c16-99bb-f3359167175a | -16.475 | -57.294 | 2024-10-04 00:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 64.9 |
| 00925e54-12af-334c-9aa9-8520c0168cca | -16.5783 | -58.198 | 2024-10-04 00:06:39 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 59.8 |
| b5c71fd4-a877-3efa-99f7-c09b9ce9bee3 | -16.9302 | -47.1224 | 2024-10-04 00:06:40 | GOES-16 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 87.1 |
| c45ac334-174b-3391-a407-3214c0686525 | -16.7606 | -57.7512 | 2024-10-04 00:06:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.9 |
| 00ef0a7c-4516-34f1-96fc-f913c03f6381 | -16.7856 | -57.4015 | 2024-10-04 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 68.5 |
| b023282a-c80b-3d4e-80e2-a270bdb74a15 | -16.7859 | -57.3811 | 2024-10-04 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 274.5 |
| 4d1ffbaa-8ae1-3c34-940a-c6b2759e1713 | -16.7862 | -57.3606 | 2024-10-04 00:06:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 121.8 |
| 1465e969-286e-3792-853c-d2ffe8f7e882 | -16.7985 | -57.8284 | 2024-10-04 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 42.6 |
| 5174cdf2-83fa-3f97-942a-a48860862c97 | -16.8055 | -57.3788 | 2024-10-04 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 132.3 |
| faeee2e8-aa1f-3318-9402-5b2db606054b | -16.8058 | -57.3583 | 2024-10-04 00:06:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 60.5 |
| 32ff0453-ecce-3c90-aae3-635a8bdb8dbf | -16.843 | -57.4767 | 2024-10-04 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.5 |
| 4bd0e034-4ecd-31ff-a14a-74fbaa9141d6 | -16.8433 | -57.4562 | 2024-10-04 00:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.8 |
| fe71832f-b524-33d2-bfab-f659bf253aba | -16.9087 | -55.843 | 2024-10-04 00:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 83.9 |
| 3f707f91-63cc-3367-832b-c8b9b18eb934 | -16.9283 | -55.8405 | 2024-10-04 00:06:41 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 112.4 |
| 63997764-0fe4-3071-9f1e-845d92a978d5 | -18.8617 | -42.8932 | 2024-10-04 00:06:50 | GOES-16 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 93.2 |
| 5f4dadc9-5eb8-372c-9aa4-84881c15f3ca | -18.8613 | -43.5837 | 2024-10-04 00:06:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 115.2 |
| aec5f7ed-5c52-3a07-8960-20fd02318785 | -18.862 | -43.559 | 2024-10-04 00:06:50 | GOES-16 | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 94.8 |
| 2c43d08f-4d90-356d-8e54-e11c8db45f24 | -18.7952 | -46.6393 | 2024-10-04 00:06:50 | GOES-16 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 8c169eaf-d07b-389b-b5ed-8270e0b49581 | -19.4899 | -42.8746 | 2024-10-04 00:06:53 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 155.0 |
| 8d7297bd-6255-3466-876b-407025637c99 | -20.1036 | -43.4276 | 2024-10-04 00:06:56 | GOES-16 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 82.9 |
| 4979b8c0-3c36-332d-9a44-23eec3527e61 | -20.1044 | -43.4026 | 2024-10-04 00:06:56 | GOES-16 | CATAS ALTAS | MINAS GERAIS | Brasil | 3115359 | 31 | 33 | nan | nan | nan | Mata Atlântica | 102.1 |
| bcb5ea6a-1cf3-36aa-9356-5e44fb3e7f90 | -21.3334 | -48.8044 | 2024-10-04 00:07:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 110.5 |
| cdba6641-041a-3f7a-9ba0-e853eeaba0ba | -21.3541 | -48.7996 | 2024-10-04 00:07:04 | GOES-16 | SANTA ADÉLIA | SÃO PAULO | Brasil | 3545605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 139.1 |
| a93b27be-f867-39bf-a292-266a06778390 | -21.7967 | -48.4396 | 2024-10-04 00:07:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 36795255-7cb7-38a2-bc5b-283336e2ad98 | -21.7988 | -48.3691 | 2024-10-04 00:07:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 34bd0cae-63e5-3bd5-9c5d-978e90336de3 | -21.8175 | -48.4346 | 2024-10-04 00:07:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 120.2 |
| 021bde89-2c70-3f61-96a4-0020bec78a33 | -21.8189 | -48.3876 | 2024-10-04 00:07:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 81bf3a5b-aa2a-3850-8811-c5d9e34019ac | -21.8376 | -48.4531 | 2024-10-04 00:07:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 4975d77e-41a4-3289-9307-9d925e78b03b | -21.8383 | -48.4296 | 2024-10-04 00:07:06 | GOES-16 | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 123.2 |
| 3deff746-ca70-381a-ad1e-7bde21c3b637 | -21.8397 | -48.3826 | 2024-10-04 00:07:06 | GOES-16 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 145fb85d-2d97-3bbe-8caa-26c7a2623e41 | -21.8591 | -48.4245 | 2024-10-04 00:07:06 | GOES-16 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 102.1 |
| d3d082b6-ce97-32ed-858d-cf0d9c2ac408 | -3.2349 | -50.3695 | 2024-10-04 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| b2e3ce8b-37b8-3d62-a17a-084941936cab | -3.2534 | -50.3689 | 2024-10-04 00:15:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 97.2 |
| 4bc848b7-64a8-362a-a108-17df39779188 | -3.3854 | -42.2866 | 2024-10-04 00:15:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 43.1 |
| 0329630c-372c-39bc-8ec1-9e2b6e65f36e | -3.4039 | -42.3094 | 2024-10-04 00:15:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 48.5 |
| d3fec6a4-ec8b-3221-ab30-5fa3886e6c1e | -3.404 | -42.2858 | 2024-10-04 00:15:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 179.9 |
| 36a4d6fc-d208-33b7-9bcf-4f7ba9f7e0ea | -3.4042 | -42.2621 | 2024-10-04 00:15:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 0981ba17-fa25-33bd-9b0a-3b755a7954f6 | -3.4227 | -42.2849 | 2024-10-04 00:15:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 64dd8da1-7c29-3e11-971d-0b80e840d332 | -3.2899 | -50.4725 | 2024-10-04 00:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 153.5 |
| ab57cc9a-00be-3fc2-8f3d-cd3c8b9a852c | -3.2899 | -50.4516 | 2024-10-04 00:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 370.1 |
| 172c8982-b5cf-333c-a195-9a75d1f8aa18 | -3.3083 | -50.4719 | 2024-10-04 00:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 102.6 |
| 73368d85-5b81-31e6-bbc3-c85ea67a566f | -3.3084 | -50.451 | 2024-10-04 00:15:25 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 231.2 |
| 15a5e00f-1f2e-3155-a661-a6b492f82130 | -3.4915 | -50.8004 | 2024-10-04 00:15:26 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 645d0c4c-9953-3444-996e-5d712d672669 | -4.0763 | -48.4902 | 2024-10-04 00:15:29 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 83.2 |
| aed79940-7d6e-3091-a9d4-bc3a66f0e75e | -4.0949 | -48.4894 | 2024-10-04 00:15:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 94.2 |
| 33998fae-155a-3c9a-bc1d-6dd7d1cb1281 | -4.095 | -48.4679 | 2024-10-04 00:15:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 2d91649c-09a7-342b-b88d-94e106a896e5 | -4.447 | -42.8889 | 2024-10-04 00:15:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 5581e024-5da3-301a-b74f-c4dc238bec74 | -4.4657 | -42.8877 | 2024-10-04 00:15:31 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 80c8c7ec-66c3-3e9f-832f-4c77a8d32976 | -4.5375 | -43.304 | 2024-10-04 00:15:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 133.5 |
| 77bb38fd-e766-3c65-8daf-99364d5e88a4 | -4.6686 | -45.8738 | 2024-10-04 00:15:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 64.8 |
| c891ff51-5104-355e-8b3a-aa8fca653d55 | -4.687 | -45.8951 | 2024-10-04 00:15:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 22093376-9f75-38d3-a873-acc4b46c349f | -4.6872 | -45.8727 | 2024-10-04 00:15:32 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 7efc1bbb-8465-3e39-9806-f06fc88d7f03 | -5.8214 | -44.1426 | 2024-10-04 00:15:39 | GOES-16 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| f96368a7-1d4b-3367-b6af-49058eda8b1d | -5.8216 | -44.1196 | 2024-10-04 00:15:39 | GOES-16 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 689b40d4-ad2d-3ad1-a53c-ef995ab18031 | -6.2524 | -44.132 | 2024-10-04 00:15:41 | GOES-16 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| d94f92f2-5734-3867-beda-0199e56dfc9f | -7.0529 | -71.7726 | 2024-10-04 00:15:47 | GOES-16 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 129.0 |
| 7aad406a-7fa4-38f8-ae5b-81307ba3b753 | -7.0529 | -71.7544 | 2024-10-04 00:15:47 | GOES-16 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 146.9 |
| b0fd3ad0-1bfa-3ea4-9068-0c006b3ac0b4 | -7.2125 | -45.6013 | 2024-10-04 00:15:47 | GOES-16 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 71b6fb86-18f8-3d67-95da-322be40047de | -7.4557 | -72.6984 | 2024-10-04 00:15:49 | GOES-16 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 123.9 |
| f00dd95c-6a50-3504-b5e4-41235000edbe | -7.6326 | -67.2013 | 2024-10-04 00:15:50 | GOES-16 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| a9bc69e9-5aed-37a6-ad63-de1ef20b2a96 | -7.651 | -67.2009 | 2024-10-04 00:15:50 | GOES-16 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| daf02187-612d-3aff-a0e0-4f8c6cbdc637 | -7.8164 | -50.543 | 2024-10-04 00:15:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| b470f8ec-0ff3-38ac-9043-d89dadba51d2 | -7.8166 | -50.5219 | 2024-10-04 00:15:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 98ad49b5-f6be-3118-8cfd-f47ffa8b018d | -7.8351 | -50.5416 | 2024-10-04 00:15:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 1a1f21ce-3fb1-3aac-9e19-c2a8da506fe9 | -7.8353 | -50.5204 | 2024-10-04 00:15:50 | GOES-16 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 84e5c239-611d-3bf4-9a84-ea0cbc0c4455 | -8.3128 | -49.5679 | 2024-10-04 00:15:53 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 03220db6-0149-3388-9c3b-3bc34abf4cde | -8.6448 | -50.0518 | 2024-10-04 00:15:55 | GOES-16 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 706b7146-ce62-3c8d-bde6-d3c4a9df0973 | -9.1039 | -50.9231 | 2024-10-04 00:15:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 69.0 |
| f0b719e5-f5c6-3cf5-9ce6-9163cd5ddc81 | -9.1041 | -50.902 | 2024-10-04 00:15:58 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| f9cd3d50-24fa-3dc1-a2e9-3100079b6c1d | -9.1158 | -51.5315 | 2024-10-04 00:15:58 | GOES-16 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 54f982d4-2811-37f6-b8ab-b1f3afd2bbad | -9.0898 | -67.4997 | 2024-10-04 00:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 98.3 |
| c8a04fc8-f185-30f4-b318-fc0a74676b06 | -9.0899 | -67.4812 | 2024-10-04 00:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| ffd040cd-ab14-3ae2-ae30-55806906684c | -9.1084 | -67.4993 | 2024-10-04 00:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 002778a2-ab6e-3e94-ba06-fe9b7fd1a2bf | -9.3115 | -50.8203 | 2024-10-04 00:15:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 303.0 |
| 69162b57-24b0-311b-9b15-7b0d0812ff60 | -9.3118 | -50.7991 | 2024-10-04 00:15:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 423.7 |
| 5f985772-633a-302b-8d16-fe37091d85a4 | -9.312 | -50.7779 | 2024-10-04 00:15:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 118daf0e-56b8-3936-bc61-0488f1e6e116 | -9.3303 | -50.8186 | 2024-10-04 00:15:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 9ce6681a-c9e3-3c12-9df7-9294da706943 | -9.3306 | -50.7974 | 2024-10-04 00:15:59 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 122.2 |
| ff447f04-c7cd-347d-9017-423d26aab1fc | -10.2378 | -47.726 | 2024-10-04 00:16:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 46a8c185-5659-37e3-8d25-facfb768f46d | -10.4424 | -50.7336 | 2024-10-04 00:16:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 6fe44d08-4405-3e82-a8ff-0c186ea9a00f | -10.461 | -50.7529 | 2024-10-04 00:16:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 85b76031-0160-3e3b-ae8b-6e124226371f | -10.4613 | -50.7317 | 2024-10-04 00:16:05 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 111.7 |
| a10817df-bd99-3096-b553-51bd08c3b961 | -10.7348 | -46.2145 | 2024-10-04 00:16:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 44.6 |
| 00474278-5156-38dd-9a70-7bb17c53b611 | -10.7352 | -46.1918 | 2024-10-04 00:16:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 72455056-e10f-3b9f-a3c4-974215a03099 | -10.7542 | -46.1894 | 2024-10-04 00:16:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 38.7 |
| c1a99508-1621-3378-b8b4-018b5da870ed | -10.8996 | -46.6216 | 2024-10-04 00:16:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 876d0c6e-335a-3268-8348-44cd9421efe6 | -10.9 | -46.5991 | 2024-10-04 00:16:07 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| f8c8f94c-37b8-3de1-9a5d-d2c58c5bd06a | -11.0345 | -46.5143 | 2024-10-04 00:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 330e7289-cd51-32bd-a8ac-0eb7a491a2d3 | -11.0532 | -46.5344 | 2024-10-04 00:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 92f155b0-113b-3b04-8520-eeed1b82c09f | -11.0536 | -46.5118 | 2024-10-04 00:16:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 159.3 |


[Clique aqui para ver as próximas entradas](README3.md)
