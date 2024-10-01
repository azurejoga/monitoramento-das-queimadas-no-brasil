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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b1d783a-ca88-3d30-a19f-781297c91675 | -18.69902 | -57.33189 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 2ba3c9d1-48ea-34bf-b9a2-ce366f8834dd | -20.77777 | -57.89324 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 7840c998-02eb-3c05-a8af-df190a69d308 | -20.77442 | -57.89268 | 2024-10-01 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| c56c40d5-290f-3f8e-b189-4cbafbad4243 | -14.78014 | -58.2205 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 21c95255-8fd5-371e-b79a-e3eed5d91e45 | -14.70013 | -57.82389 | 2024-10-01 05:08:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0a2e00e-bb9c-32f3-b236-96fa2d7b94ff | -14.69957 | -57.82743 | 2024-10-01 05:08:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56f623db-2fb3-3b89-8f8c-b3acc293f292 | -14.69739 | -57.81979 | 2024-10-01 05:08:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e29bc806-5351-344d-b520-67e09f1e81b0 | -14.69683 | -57.82334 | 2024-10-01 05:08:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74f2654b-02a9-3c7e-933c-786ac364da12 | -14.69352 | -57.82279 | 2024-10-01 05:08:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c386baf2-ca93-30ee-bfdd-491939de28d7 | -14.94627 | -57.94513 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ffde934-540a-351b-b65f-ea3bafe3f4d9 | -14.93636 | -57.94347 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5edd4fcb-d146-370c-b322-7762f4195510 | -14.93306 | -57.94292 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 05f82ed0-58bb-3924-8d22-1e5e0f0bcb57 | -14.9325 | -57.94648 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a44ed472-44b2-38d7-bdda-82140d19e394 | -14.93194 | -57.95003 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6e9d8ec-526d-39db-bce0-1de227cac082 | -14.92919 | -57.94592 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 04671859-5df4-37f8-a86e-6967f3aba12d | -14.92863 | -57.94948 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a569f6c4-afa9-3d67-b43d-1882551a7f41 | -14.90215 | -57.96695 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 323f8b84-3dd8-3599-971b-17adde63329b | -14.90159 | -57.9705 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47eb6022-53e0-3184-a38f-ed7f3f9bc582 | -14.90035 | -58.02123 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e59b39d9-e7c1-3fb9-a0e6-b3fdedb63abb | -14.89979 | -58.02478 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13b01045-c4cf-3aae-a9e3-bec03366a07c | -14.89923 | -58.02832 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cfe28c72-b18a-35c4-972c-2f2f073c3106 | -14.89705 | -58.02068 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21d705de-fdcc-396a-84f2-f72fcf34bbdb | -14.89649 | -58.02422 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 801920e0-94aa-316b-9ca5-1b60d97c9b80 | -14.89599 | -58.00595 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cfb6b723-37e9-39e6-b7b9-0272f407dac6 | -14.89543 | -58.0095 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b161fe22-5591-331a-9ae7-4775b2fdc963 | -14.89487 | -58.01304 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d775c87-474c-3c9d-853f-26cb44182d34 | -14.89374 | -58.02013 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 50ce67b2-0148-3869-9421-d8c39a3b5446 | -14.89318 | -58.02368 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9e8fb0f6-c2ca-3bef-b1f3-e9173cf10dc4 | -14.89268 | -58.00539 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 41a80c25-e2b8-33f5-8f07-d706924e0028 | -14.89212 | -58.00894 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f10bad3-98e2-3608-992e-8625275cba39 | -14.89156 | -58.01248 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f919c01d-eee2-346d-b398-b02d62ae168f | -14.891 | -58.01603 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc2e0fc6-d9e7-3122-ad64-1746a8f65e80 | -14.89044 | -58.01957 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9c2b9cb4-dd1b-3bec-a2e7-a43a482991f6 | -14.88882 | -58.00838 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f79dcacb-ae0c-38e5-897f-f9b72bb16541 | -14.88826 | -58.01193 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0a52b9e0-9a2d-377a-be46-0e29edae0f39 | -14.88552 | -58.00784 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c7bcf087-7845-3172-88f0-872b8b986082 | -14.88496 | -58.01139 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 66d15dd1-1507-3f74-b8a6-e8c1bf1f7513 | -14.88439 | -58.01494 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e7f414cf-f78e-32a2-a1d9-0a7100810fae | -14.88333 | -58.00023 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bed64333-ce1b-38b8-9b11-b2c7fc3987b2 | -14.88277 | -58.00377 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c5939d8-0258-35ed-a4c1-29cd1912e0d7 | -14.88221 | -58.00731 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5a7bdef6-5fb5-35d4-8b73-cb5e6795d5d4 | -14.88165 | -58.01086 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| af5a3047-58c8-3cf8-8c4e-47105037bc39 | -14.88109 | -58.0144 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6b738c5a-9fe3-34e3-865d-2ed0fbf1dc0a | -14.88002 | -57.99969 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c7ae60b-a943-3db7-8af7-0d8017b5f5dc | -14.87946 | -58.00324 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 40e01e0b-4ba6-3dca-840c-17e39dcf2d51 | -14.8789 | -58.00678 | 2024-10-01 05:08:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 65ad1910-97e4-3582-a3e5-841ffadb326e | -16.30638 | -58.61866 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 330e02cf-08e3-36e6-839e-1dba2c46b3ba | -16.18362 | -58.42794 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 228c73f8-1994-3e30-9305-4ad86938c805 | -16.18032 | -58.42738 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 1a14019f-835a-3c72-9d8d-891b9196a65e | -16.17975 | -58.43095 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ba8dbceb-f920-356f-aee7-c231b47fd03f | -16.1768 | -58.427 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 1c4681cf-e91a-319a-8cc1-8e36c7d2f3f5 | -16.17623 | -58.43059 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d1cc10cb-6b3f-3686-af5c-effa515caaea | -16.17349 | -58.42644 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 037a5dac-3915-380f-a4a8-2fea5590704d | -16.17292 | -58.43003 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 99932e25-8a7c-3be9-b934-0f9154296d6d | -16.16961 | -58.42947 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 7e75b2fa-e9c0-3dbd-a742-4f6e9749f712 | -15.37813 | -58.1638 | 2024-10-01 05:08:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30e8f665-aa39-3fe9-862c-c56abc08f76d | -15.37539 | -58.15968 | 2024-10-01 05:08:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0cb7e0aa-9d4e-3e87-a54f-366bf2b12d9c | -15.37483 | -58.16323 | 2024-10-01 05:08:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3984ba50-edcd-30c8-bb22-fa48871df5bc | -15.27972 | -58.1834 | 2024-10-01 05:08:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40abcfb7-d967-3f0f-8cd6-b1f6958200ac | -15.27641 | -58.18286 | 2024-10-01 05:08:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 181c4960-e8fc-33b7-867b-69f1fcd7e7a7 | -17.04912 | -58.39787 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 454d0844-c163-337f-b8fd-f9ab01c962b1 | -17.04855 | -58.40146 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| f019723a-dd9c-3242-bc64-8803d4f6cb6d | -17.04581 | -58.39731 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 9660b709-62b5-35a6-b27c-39eb90dad545 | -17.04525 | -58.4009 | 2024-10-01 05:08:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8e1d9540-0e2e-3b3c-b85c-0ecd37555df0 | -13.41838 | -61.92896 | 2024-10-01 05:08:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ae99561-40ad-337e-9151-a1d84665573d | -13.41516 | -61.93143 | 2024-10-01 05:08:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee025f15-c7de-3760-a011-e042489f8159 | -13.41452 | -61.92824 | 2024-10-01 05:08:00 | NOAA-21 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92192881-123a-3641-8a96-91f58464a3e7 | -20.00868 | -44.52842 | 2024-10-01 05:08:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 9aa7ba4e-1656-3554-bedd-63c9694a8803 | -20.00814 | -44.53568 | 2024-10-01 05:08:00 | NOAA-21 | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 2d4fe268-431b-3075-8e67-246ba9a04038 | -18.80794 | -45.7994 | 2024-10-01 05:08:00 | NOAA-21 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db9b8efd-1d36-355a-a1e8-254573a1807e | -20.53836 | -46.28947 | 2024-10-01 05:08:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ea961ddf-aeee-3441-ad71-7d59f5dae0a6 | -20.53796 | -46.29459 | 2024-10-01 05:08:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ccf8c1b4-d451-31c0-b168-6ec0cdc132ea | -20.53775 | -46.29074 | 2024-10-01 05:08:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ea431c28-31ec-34a3-b433-13f724515140 | -20.53731 | -46.29593 | 2024-10-01 05:08:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0c2a9c42-fc47-3c9b-9dec-972ef1e36d97 | -20.53138 | -46.28874 | 2024-10-01 05:08:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 55b3ed72-a32a-3cd1-9b2f-1935f3630a2a | -20.53089 | -46.29451 | 2024-10-01 05:08:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b2abb08-b80d-3f27-a138-be8ce27eba70 | -20.53042 | -46.30011 | 2024-10-01 05:08:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 422f40b3-0b55-304b-9ffb-06463a762ee9 | -20.52401 | -46.29861 | 2024-10-01 05:08:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c4141d3e-42de-3bda-8e47-39450ee05638 | -20.51719 | -46.3021 | 2024-10-01 05:08:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c177e631-8f18-33cf-b202-18f23d3fe7b2 | -22.3847 | -45.80568 | 2024-10-01 05:08:00 | NOAA-21 | CACHOEIRA DE MINAS | MINAS GERAIS | Brasil | 3109709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| bde13036-54b7-3440-8198-214549848e90 | -22.38017 | -45.80106 | 2024-10-01 05:08:00 | NOAA-21 | CACHOEIRA DE MINAS | MINAS GERAIS | Brasil | 3109709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| b86d2959-c480-3b0c-bb0b-2c99d3b258ed | -22.37981 | -45.80638 | 2024-10-01 05:08:00 | NOAA-21 | CACHOEIRA DE MINAS | MINAS GERAIS | Brasil | 3109709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| e5ff331e-b502-37ff-96ad-88a62236fef5 | -21.33338 | -46.43174 | 2024-10-01 05:08:00 | NOAA-21 | MUZAMBINHO | MINAS GERAIS | Brasil | 3144102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 9575fe76-89e6-3d5b-9a41-72bd24eb1989 | -21.3101 | -46.64156 | 2024-10-01 05:08:00 | NOAA-21 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 0953a01f-3ec1-3422-81db-cd949ece12ec | -21.30968 | -46.64682 | 2024-10-01 05:08:00 | NOAA-21 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 3d4085b6-134f-3fcb-8445-b168c52621b2 | -21.30928 | -46.65173 | 2024-10-01 05:08:00 | NOAA-21 | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| f1d7cf70-8dc2-3380-9a1b-6e5709deba0c | -22.77866 | -46.81853 | 2024-10-01 05:08:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| da30f7da-a31a-3240-ac5d-facafbd31590 | -22.7728 | -46.81039 | 2024-10-01 05:08:00 | NOAA-21 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f05fcdb7-abf6-3e21-90dd-1f633d3273f3 | -22.72392 | -46.6796 | 2024-10-01 05:08:00 | NOAA-21 | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| e8ea64a7-ad9d-3fc3-bedb-4522ca56b30a | -22.72357 | -46.68454 | 2024-10-01 05:08:00 | NOAA-21 | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| d66758aa-e33a-3b3c-b61f-073a0eb55f1d | -22.72351 | -46.68058 | 2024-10-01 05:08:00 | NOAA-21 | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 05d8b833-ba74-3051-a231-721f7a2fa74c | -22.72314 | -46.68537 | 2024-10-01 05:08:00 | NOAA-21 | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| e119c653-a3d5-39ca-aeda-dc76d1e21306 | -17.58818 | -46.95597 | 2024-10-01 05:08:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d3242e28-37a4-31b5-af93-951b9fb44350 | -17.58775 | -46.96029 | 2024-10-01 05:08:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f97bf9d4-e37e-3f03-be28-302c829bb3ef | -17.58604 | -46.77881 | 2024-10-01 05:08:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 67909abb-1c95-3c14-b77e-d9bb1de25b13 | -19.29998 | -47.43249 | 2024-10-01 05:08:00 | NOAA-21 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 462d6df4-a8fa-3aae-b65f-720d038d5f8e | -19.29955 | -47.43683 | 2024-10-01 05:08:00 | NOAA-21 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 91bfbc19-bb21-342e-9b79-da7c5dfa8297 | -19.29681 | -47.43274 | 2024-10-01 05:08:00 | NOAA-21 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5e80477f-29e4-3a2d-ba0d-6f4812e5f130 | -18.92314 | -47.03125 | 2024-10-01 05:08:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8b4b82d7-c632-3fb9-857f-b6297b753c64 | -18.92248 | -47.03095 | 2024-10-01 05:08:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README125.md)
