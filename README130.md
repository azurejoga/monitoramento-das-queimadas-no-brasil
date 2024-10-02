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

## Dados Diários - Página 130

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7cd0f96a-842c-3c1f-810f-e34aca5cbe14 | -12.283 | -47.64334 | 2024-10-02 05:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c1a5fbfc-4aeb-3741-9842-da3262da68ce | -12.28247 | -47.64786 | 2024-10-02 05:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| df5a1d9c-af74-3cfb-8091-10701af81c5a | -12.28192 | -47.65247 | 2024-10-02 05:10:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 7900a0f2-d6bb-3b41-ad50-ba4217a497e6 | -6.12362 | -47.27058 | 2024-10-02 05:10:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7757b8dd-3515-36b4-b903-e74d201db258 | -6.1231 | -47.27442 | 2024-10-02 05:10:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5712d938-533f-3ddb-b6f0-209a4f4a92d8 | -6.12098 | -47.27138 | 2024-10-02 05:10:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f7050dbd-7b4f-34d4-8e22-4941b0caff95 | -6.12043 | -47.27524 | 2024-10-02 05:10:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b9752024-22e7-3691-a3f5-3ac40680dcc7 | -6.11794 | -47.26974 | 2024-10-02 05:10:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bdbdf361-3182-3278-85ce-dd57b3964832 | -6.11742 | -47.27361 | 2024-10-02 05:10:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 313cc5d0-138e-3bc7-8c39-d42dff8b9674 | -7.18096 | -46.94682 | 2024-10-02 05:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e50b1324-0497-3ee2-82b9-1a4255851076 | -7.18034 | -46.95141 | 2024-10-02 05:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 12b8e9ef-cb8f-306d-97c8-acd8eea4be9c | -7.17974 | -46.95588 | 2024-10-02 05:10:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6d0498d4-7836-3fac-8bb9-a4aa65e6b601 | -7.10034 | -47.8673 | 2024-10-02 05:10:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4c7955c7-7d64-348e-8f13-2c90347f9028 | -7.10029 | -47.86995 | 2024-10-02 05:10:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a1eb64b-3c77-35e2-823b-c6f2fc491503 | -7.09987 | -47.87081 | 2024-10-02 05:10:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 18f13be7-8020-3130-8a3a-7f6b3931f41d | -7.0998 | -47.87344 | 2024-10-02 05:10:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f5c16e8-730d-38bb-bdd8-5ea8f0c6399a | -7.0994 | -47.87432 | 2024-10-02 05:10:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d234a48e-f5f1-3fd5-ab1f-ad2a8df9a408 | -6.94457 | -47.65477 | 2024-10-02 05:10:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfcf01bc-cd47-318d-8252-be983d34553f | -9.17067 | -48.75223 | 2024-10-02 05:10:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 012a2f1b-4ecf-3b4d-8aa7-e3da6f7adc51 | -8.5274 | -47.32244 | 2024-10-02 05:10:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7d7b2430-b63c-35c6-aa1f-7d7ffe12c15b | -8.52102 | -47.32567 | 2024-10-02 05:10:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8362129a-c7cb-341e-8fb1-6584e6c9dc29 | -10.70717 | -48.72298 | 2024-10-02 05:10:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4fe6100e-9f6c-3283-974d-724b21ab7dd3 | -10.70679 | -48.72591 | 2024-10-02 05:10:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a7d3ddef-cc53-393d-8d34-3cf04b4b9866 | -10.70675 | -48.72343 | 2024-10-02 05:10:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a71d69f3-5729-3689-ac08-845e7b8dc814 | -10.7064 | -48.7289 | 2024-10-02 05:10:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6917b2d6-c5a3-326f-be69-e46d3b9d6495 | -10.70639 | -48.72638 | 2024-10-02 05:10:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aea8bf8e-c292-3028-8ff3-37e1ad6edda0 | -10.70212 | -48.71883 | 2024-10-02 05:10:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8113994a-749b-3ed1-8ac0-97c561dfe390 | -10.70206 | -48.71618 | 2024-10-02 05:10:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3958e75e-31f4-3d23-9d59-cc7dbaf50182 | -10.70172 | -48.72192 | 2024-10-02 05:10:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b84c6148-d696-3b7a-8132-ddba6ac91688 | -10.70168 | -48.71928 | 2024-10-02 05:10:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3068b6ea-fb76-3304-bcba-1ae0d3aa6225 | -10.7013 | -48.72237 | 2024-10-02 05:10:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46a45efb-e855-3011-a47f-c4c1a72d6552 | -10.23942 | -47.68539 | 2024-10-02 05:10:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 0d7f0f24-3a2d-3239-afa1-3f8ac941440e | -10.2389 | -47.68953 | 2024-10-02 05:10:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| ed4e6ece-7e3b-3242-a415-2ceb893d0c20 | -10.23356 | -47.68473 | 2024-10-02 05:10:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c57375c-1591-329c-bf54-96b19b832f98 | -10.22301 | -47.68565 | 2024-10-02 05:10:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bfb239b2-82e8-3a96-8188-c94c72f528fc | -10.22136 | -47.68736 | 2024-10-02 05:10:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73fd0d5d-a372-31f7-87d9-569205f2e4f8 | -10.74484 | -47.97555 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 740cb711-0cc1-3ed0-8334-26bfb9a792bc | -10.74428 | -47.98006 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b9605c4-f111-389a-b86b-fac958f74e37 | -10.59358 | -48.05621 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1cdd852-eaec-3ad4-b67c-a907e809c660 | -10.59277 | -48.06282 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1ec52e47-49dd-31b7-82d8-5689610e05df | -10.59236 | -48.06614 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f19605d8-ba18-3c52-8755-021d1f190c5a | -10.59222 | -48.0612 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8fe16c93-1a99-3ffb-a4bc-c69b34706cc0 | -10.59195 | -48.06952 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2dd44e40-517d-3125-8141-daaaa38e912a | -10.59179 | -48.06456 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a5c46010-df10-3378-b811-61be7017cf51 | -10.59135 | -48.06796 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 137953da-907b-38e1-bd80-7c6d5f237633 | -10.58834 | -48.04615 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f484bfc-06c7-3d8c-9eb2-03738c5ba165 | -10.58786 | -48.04983 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 53febc5d-952d-3cba-aed1-0fbd17680af3 | -10.58746 | -48.05865 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 03328e50-5aed-3564-a2b2-f618fb290fb6 | -10.58703 | -48.06218 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 977812d9-7ff1-3478-986e-fc9f233bbe16 | -10.58657 | -48.06595 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 09ff5b45-f1a5-391b-989a-46f7a20dd978 | -10.58651 | -48.06034 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5eabe0e9-3ddb-32c8-b65a-dd1aab1cf0b6 | -10.5861 | -48.06979 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| e2c04f02-2aca-3964-a7b4-8598df0ac4b8 | -10.58605 | -48.06393 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 48c2b713-d437-3ef4-894d-f17186067d4f | -10.58568 | -48.07326 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 7e879349-3dc9-3f12-858d-6c208f01ef2d | -10.58554 | -48.06785 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 67aefb33-6cfc-3e67-8fe9-8e1686cac5f3 | -10.58505 | -48.07162 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 53ddb0f6-5e18-3acd-be8d-6fe0665db951 | -10.58463 | -48.07487 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 5a97374c-1cc0-39ea-b5e0-b765a7e02e13 | -10.5804 | -48.06878 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 2ddafa10-bdc8-30af-81db-f12496434ecb | -10.57994 | -48.07261 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| f61c334c-34ed-3919-9004-8230ee1737f9 | -10.57934 | -48.0708 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 330b4c71-aebd-3379-a4ae-a853af14677d | -10.57396 | -48.02579 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7eff7897-e537-3f42-a5ab-6ef89788c6d1 | -10.5737 | -48.02387 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2b6e146d-d401-3a08-96ef-6a31d1bd689d | -10.57316 | -48.02807 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 57afa91f-f411-33de-b54a-e220efafd66e | -10.56745 | -48.02716 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 267e70a4-59e7-332a-b587-24911ba89f60 | -10.56696 | -48.03096 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b1441bec-4f99-3ba1-b510-9651cb429db7 | -10.56179 | -48.02578 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1e989629-c479-3945-825e-5cc8bbf9ccd7 | -10.55622 | -48.0237 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5c3addb-7bda-33dd-8312-ce9d621cf02d | -10.55572 | -48.0276 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b39ca63-a803-385f-a4d5-04c9dd2c3c7a | -10.5539 | -48.04195 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cca08b53-97dd-3cf0-bbc1-00d3197b65d9 | -10.54911 | -48.03373 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3eaca1b-e35e-39ed-9cd3-388ddca8ed05 | -10.54865 | -48.03746 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd82f2b3-baf7-3b01-bad6-8bb8636abfcc | -10.54818 | -48.04111 | 2024-10-02 05:10:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 459a41e7-20df-343c-9d4d-45eae4b0f905 | -10.46504 | -48.19688 | 2024-10-02 05:10:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 626bb14d-7a3b-3f00-b752-8e4096e529d7 | -10.46256 | -48.23998 | 2024-10-02 05:10:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 02de8304-92ba-3fc2-8f40-85cfe3f32150 | -10.46009 | -48.19029 | 2024-10-02 05:10:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08dd5fd5-fa22-3ec5-a599-10304aa4ba83 | -10.45964 | -48.19398 | 2024-10-02 05:10:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a042a19b-2359-3544-b855-42d88625107c | -10.45954 | -48.24166 | 2024-10-02 05:10:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80845bf6-b3d1-3138-a769-04efd88f51ca | -10.45642 | -48.243 | 2024-10-02 05:10:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d542b108-1a9d-351b-a50e-42b328b5de42 | -10.45388 | -48.24097 | 2024-10-02 05:10:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b212b1b3-cfc7-304f-b612-64e4c54a6f62 | -8.23668 | -49.7686 | 2024-10-02 05:10:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 60743939-b548-337f-b98d-52f81c039374 | -8.2363 | -49.76644 | 2024-10-02 05:10:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 44a642bb-f317-3240-80a6-5679a86a174c | -9.59809 | -50.19318 | 2024-10-02 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6d4bbe9f-e4d3-394e-bd89-d69a591d4095 | -9.5932 | -50.1925 | 2024-10-02 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 30f2eea8-3abe-3c2e-bb0d-23f8c5172776 | -9.59247 | -50.19795 | 2024-10-02 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4501d632-778d-3340-8d8d-ff5a39f3aec1 | -9.5883 | -50.19183 | 2024-10-02 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9109d266-8723-3aba-9cd0-5bd40611799f | -9.58758 | -50.19728 | 2024-10-02 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a3430835-9b8d-3aa2-86c8-e58099f637b4 | -9.58685 | -50.20274 | 2024-10-02 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 08791803-cd11-372c-8fa1-c55495a2c2dd | -9.58341 | -50.19115 | 2024-10-02 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9febab7b-b063-3162-b1ed-2321b831d6ae | -9.57851 | -50.19048 | 2024-10-02 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e8642164-baf4-337e-aa84-94cf0b7f3ec3 | -9.57491 | -50.21773 | 2024-10-02 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 179bfdb9-debf-34e0-851e-0a63464e65e8 | -9.57191 | -50.22018 | 2024-10-02 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 52f97229-c5e3-3bcb-913d-1b4851c0d7d4 | -9.57016 | -50.17814 | 2024-10-02 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| f2a8b3ca-5fab-3b0b-88af-28f6eb526011 | -9.56944 | -50.18362 | 2024-10-02 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| e57cd321-e499-36ec-8d2b-7942e82d9f12 | -9.56931 | -50.22249 | 2024-10-02 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9694ff54-18ea-34a4-97a4-1000ec4ef337 | -9.56743 | -50.18074 | 2024-10-02 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 7741800c-6b84-37b4-99f6-5220ff1daa9a | -9.56526 | -50.17746 | 2024-10-02 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e542bf5e-8656-3f0d-a4d0-68b9c073e7df | -9.56454 | -50.18293 | 2024-10-02 05:10:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3a05480a-41d9-3d91-b208-79a4e8806687 | -12.15728 | -50.06148 | 2024-10-02 05:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 6d5b7f76-0160-3a2e-98ef-73d15359a468 | -12.15329 | -50.05161 | 2024-10-02 05:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3cf7caf3-7d48-3943-92e7-101391cfb334 | -12.15291 | -50.05466 | 2024-10-02 05:10:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |


[Clique aqui para ver as próximas entradas](README131.md)
