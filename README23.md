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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96614e1b-2b3c-3380-b5c3-65650c8aac4d | -4.20249 | -45.88221 | 2024-11-02 03:47:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| f2a4df82-3404-3a2a-9ced-0b2a81a7f789 | -4.20188 | -45.88578 | 2024-11-02 03:47:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 25.8 |
| dffd7c00-8030-3d21-8610-8febbf67c7e8 | -3.71921 | -46.00098 | 2024-11-02 03:47:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28e7ca89-eaa2-3e34-b394-cc23a5374952 | -3.71855 | -46.00483 | 2024-11-02 03:47:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d96a428d-9ec1-3108-8555-af0a0145f187 | -3.6449 | -45.94688 | 2024-11-02 03:47:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f15b9e1d-1040-3dcf-ae26-fffd4559a812 | -3.63928 | -45.94587 | 2024-11-02 03:47:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 623abd0c-fc5c-3089-8a1c-bc290be85160 | -3.63864 | -45.94965 | 2024-11-02 03:47:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a0bf131-8a18-3bfe-9be2-86576502ff32 | -7.12654 | -46.36709 | 2024-11-02 03:47:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ef7f9d02-5f01-3ac4-8e83-af5b94825f52 | -7.12586 | -46.3709 | 2024-11-02 03:47:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 015ab402-8733-318b-a134-befc8dfac7c2 | -7.12462 | -46.37786 | 2024-11-02 03:47:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 70e0b364-91ed-3313-bbcf-51d244f3f94e | -7.12103 | -46.36639 | 2024-11-02 03:47:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6fb75f6e-d15c-32e8-b629-8eff957aebf5 | -7.12039 | -46.36995 | 2024-11-02 03:47:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1040866a-a389-3135-8c21-c644a7bd5c18 | -7.11916 | -46.37685 | 2024-11-02 03:47:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ed4018da-1092-3ed0-b92a-f055149e404f | -7.90959 | -46.69642 | 2024-11-02 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cf4560d3-fde8-3ad2-ba1a-7c5eab9ed139 | -7.90893 | -46.70004 | 2024-11-02 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 33ddcb43-b9db-39b5-a7b0-50c44ae86e6c | -2.16284 | -46.38822 | 2024-11-02 03:47:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a36d2f8f-ed0e-3afa-a521-2cd0b03ffa1f | -2.16213 | -46.39243 | 2024-11-02 03:47:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6057eb28-e98f-311d-8d00-2baf437ad89b | -2.15691 | -46.38722 | 2024-11-02 03:47:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7ba242fe-c04e-3200-a1e6-a0e587f453dd | -2.01361 | -46.83342 | 2024-11-02 03:47:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1d9ebb3f-feb7-3818-97bb-52b28d5f9362 | -1.978 | -46.43777 | 2024-11-02 03:47:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7933a1e2-a3e3-372b-b5d2-1cb768bf71a8 | -1.97203 | -46.43677 | 2024-11-02 03:47:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 07ec72a6-f2b6-30ce-9dd6-17a39754f905 | -1.96679 | -46.43138 | 2024-11-02 03:47:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ec4e10f-8a4c-3add-999b-3195707d383f | -1.46783 | -46.72155 | 2024-11-02 03:47:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| f2438d38-b513-37c4-b39f-dd5ee75f2c18 | -1.46706 | -46.72616 | 2024-11-02 03:47:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 750d81c5-54e8-3254-8603-e01c80ee6a19 | -1.46172 | -46.72044 | 2024-11-02 03:47:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 43851459-d151-3416-ad13-a2ee07cc5474 | -1.46095 | -46.72507 | 2024-11-02 03:47:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 25abaccc-a5d5-3594-8e63-176358bf6ed1 | -3.39943 | -46.06454 | 2024-11-02 03:47:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8719a11-5532-3b6f-a3e4-936afa91b040 | -3.39876 | -46.06843 | 2024-11-02 03:47:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e94e505d-73b0-338a-9be3-7673c3b0032b | -3.3609 | -46.04995 | 2024-11-02 03:47:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5634226-55c6-382d-905d-7f3061acb879 | -3.35522 | -46.0489 | 2024-11-02 03:47:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15e19366-5e22-3970-bb3e-e6b8ac19b1cd | -3.21398 | -46.17568 | 2024-11-02 03:47:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 714cadf5-9310-349e-9682-f67a7a3127e7 | -3.21331 | -46.17968 | 2024-11-02 03:47:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| f6c321a6-e84d-3058-bd84-5b47e88d5a26 | -3.18431 | -46.59224 | 2024-11-02 03:47:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b832768c-b81e-35ed-855f-fd17184eabc3 | -3.18357 | -46.59657 | 2024-11-02 03:47:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a4f36fa7-060e-39e4-b7e4-fd5646d4e3c7 | -3.18157 | -46.59016 | 2024-11-02 03:47:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 69d2edba-86a5-3557-821d-5f39f0073cee | -3.18086 | -46.5945 | 2024-11-02 03:47:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08f39842-41ea-3b5c-9b44-b4d4e6549273 | -3.18015 | -46.59881 | 2024-11-02 03:47:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5e3f54a8-ddac-3497-a906-8352d45d04fe | -3.1784 | -46.59122 | 2024-11-02 03:47:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ee6ffe3c-7e90-34c1-a9f4-40ea1f8df039 | -3.17765 | -46.59555 | 2024-11-02 03:47:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3058b615-f77f-35a7-870b-94b50d562d31 | -3.17495 | -46.59343 | 2024-11-02 03:47:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e981cb00-181d-3318-8623-fe8981665dbb | -2.5741 | -47.30697 | 2024-11-02 03:47:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f628a3b-ffde-3857-ad9d-0d260d4bc165 | -2.56785 | -47.30595 | 2024-11-02 03:47:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e90131d-c466-37ab-8984-3db8cce26969 | -2.82589 | -46.62011 | 2024-11-02 03:47:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5435c2ae-2790-321d-aebc-ca52f83c93ca | -2.82518 | -46.62442 | 2024-11-02 03:47:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 45c468f7-b536-3e0d-9e32-88f6614debc5 | -2.82302 | -46.61776 | 2024-11-02 03:47:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c21ef461-06af-38e8-a104-d457aa69ab9f | -2.82228 | -46.62208 | 2024-11-02 03:47:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| a4576c76-2f05-31c0-8bde-ccf6aa6732fc | -2.81995 | -46.61901 | 2024-11-02 03:47:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 851e4d60-6d8d-34c6-ad28-b43d8e7900dc | -2.81923 | -46.62336 | 2024-11-02 03:47:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2b16fbf6-3f37-322f-8493-1a6e221886b4 | -2.68565 | -46.7504 | 2024-11-02 03:47:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70622e32-462e-36b6-99fe-59953eef06a2 | -2.6849 | -46.75488 | 2024-11-02 03:47:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 23215622-3fa9-3e7c-8d0e-585c148b22d1 | -2.68039 | -46.74475 | 2024-11-02 03:47:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0edfc13-4129-3502-8dce-93d15622f372 | -2.67965 | -46.74924 | 2024-11-02 03:47:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e408dc6-49aa-3d96-a81f-5b20cf61b6e8 | -2.44948 | -46.35083 | 2024-11-02 03:47:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6d1c0a91-a31c-335e-9db7-a8a947265440 | -2.44784 | -46.34874 | 2024-11-02 03:47:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3acb138-a1ce-347c-84e2-98daab42900a | -2.44712 | -46.35294 | 2024-11-02 03:47:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e725cb0-c226-35f4-a9e5-d8d74f191b29 | -2.44361 | -46.34975 | 2024-11-02 03:47:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c07afd1-5c69-3957-af67-ba83bce050e4 | -2.44196 | -46.34774 | 2024-11-02 03:47:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88fe89e0-90f0-343e-bbe6-2e549397209e | -2.38833 | -46.57488 | 2024-11-02 03:47:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 356f9aec-86f3-3707-a6b6-1babcf905aa1 | -2.38761 | -46.57926 | 2024-11-02 03:47:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9377de89-d8d3-35a1-bcef-202face9fb51 | -2.38233 | -46.57395 | 2024-11-02 03:47:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58756b81-a274-3397-a52e-9d727fcfe679 | -2.36929 | -46.50472 | 2024-11-02 03:47:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4a1e4869-f20e-3ce7-8125-cd063fa95741 | -2.36857 | -46.50903 | 2024-11-02 03:47:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 275ea9db-4e9d-3178-8025-1c28a4a24405 | -2.33955 | -46.52247 | 2024-11-02 03:47:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 257f1a3e-54a5-3f3e-9ea9-f13111b1c46d | -2.33882 | -46.52695 | 2024-11-02 03:47:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d325686e-8c7c-38ff-9267-2599635aa250 | -2.32397 | -46.5191 | 2024-11-02 03:47:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a164ace-970f-3480-8cae-e09a018b31b6 | -2.32166 | -46.51934 | 2024-11-02 03:47:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0b622f0e-c5b9-3d60-9c64-53272140acce | -2.31876 | -46.51369 | 2024-11-02 03:47:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e37548e-c3c0-30ae-9c29-315344974b39 | -2.31801 | -46.51807 | 2024-11-02 03:47:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a45ddc1-3d8b-3ceb-9bc4-6d25f9b2f9bf | -2.31641 | -46.51394 | 2024-11-02 03:47:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 22ad16a7-9800-3a7e-ae07-cdffba6475e2 | -2.3157 | -46.5183 | 2024-11-02 03:47:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| edb4b511-0648-3159-b501-45a99f499649 | -2.31278 | -46.51277 | 2024-11-02 03:47:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74b06ed0-3dc2-342a-93d8-d4a2647c9092 | -2.31205 | -46.51707 | 2024-11-02 03:47:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46a7782c-5b2e-3fe4-be4f-f09387daabc4 | -2.31044 | -46.51296 | 2024-11-02 03:47:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d49588f-3fd6-3f7c-92bb-9b25deb61dae | -2.30974 | -46.51729 | 2024-11-02 03:47:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec8be423-42c1-354b-9150-b9e0b6a48610 | -2.27658 | -46.75835 | 2024-11-02 03:47:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb3e25fe-e7b0-39e0-982a-3490fd325c7b | -2.27059 | -46.10066 | 2024-11-02 03:47:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5c04cc76-653e-3827-89f6-c56dfc93f4fd | -2.26477 | -46.09969 | 2024-11-02 03:47:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 905cf7b2-bbb0-348e-9883-d598e632c9c1 | -2.24115 | -46.52381 | 2024-11-02 03:47:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 45a1f1a2-4b3a-3ede-b444-971474e2539d | -2.19896 | -46.4653 | 2024-11-02 03:47:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c78e1dc4-daa0-348b-862e-ef6d8563273f | -2.19825 | -46.4696 | 2024-11-02 03:47:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c07612ed-dff0-3397-a862-e6bb0b29ba21 | -3.81746 | -47.47476 | 2024-11-02 03:47:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c0538c67-e62d-345b-b073-a54e1fe8487f | -3.81129 | -47.47355 | 2024-11-02 03:47:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b177398f-f9a4-38e4-b911-c5a0dc6c7b3d | -4.1105 | -46.59786 | 2024-11-02 03:47:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03d86bdf-ca0a-3fc8-a412-dc6b513d7bfd | -4.06492 | -46.2757 | 2024-11-02 03:47:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38ce0175-48b9-34d0-bebd-b95e8146eb54 | -4.06427 | -46.27938 | 2024-11-02 03:47:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 177eb9c6-f9a5-3894-b188-57e40b364258 | -4.06383 | -46.27704 | 2024-11-02 03:47:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b9571560-f2ad-3209-8a51-320f3fa21b5d | -4.0632 | -46.28081 | 2024-11-02 03:47:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7cd3864e-ec42-3cd6-b409-f54559cf921f | -4.05583 | -46.93704 | 2024-11-02 03:47:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf589453-85d3-396b-8bb2-1ed647dc9ce4 | -4.05329 | -46.93617 | 2024-11-02 03:47:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 741cedf7-bef6-36da-8622-e33124b28deb | -3.99179 | -46.45773 | 2024-11-02 03:47:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 3b7248cf-7854-3929-8314-238e5ffc71e4 | -3.99111 | -46.46176 | 2024-11-02 03:47:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 593529b4-ef81-3b06-9450-866fd42fb31a | -3.89117 | -47.0818 | 2024-11-02 03:47:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 40f313f8-2da4-33a5-9cf8-59f11356ad4e | -7.8095 | -47.47367 | 2024-11-02 03:47:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 672126d1-9a43-37d4-8a24-7033b610c645 | -7.80369 | -47.47262 | 2024-11-02 03:47:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d706e72b-df1c-3def-8a67-29bb502581aa | -8.68543 | -47.95927 | 2024-11-02 03:47:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d998f12f-10a2-3b82-a632-e08c9260f613 | -8.68363 | -47.95404 | 2024-11-02 03:47:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ee6bd19-5a9d-3675-a1da-56e525c03658 | -8.6828 | -47.95833 | 2024-11-02 03:47:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d76d1fd-10fd-3088-90f3-c5dfca15a70c | -8.68033 | -47.95387 | 2024-11-02 03:47:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6dbe0adb-7bbb-366f-959a-4295fcedf24c | -2.11914 | -48.28512 | 2024-11-02 03:47:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a4f6f284-1188-3fdd-8f27-96d8ffd13f0f | -2.11818 | -48.29089 | 2024-11-02 03:47:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |


[Clique aqui para ver as próximas entradas](README24.md)
